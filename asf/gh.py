"""Read-only access to GitHub's APIs over HTTPS, with retries for rate limits and transient failures.

The token is the bot's when ASF_APP_ID and ASF_APP_PRIVATE_KEY are set: a GitHub App installation token, minted
from the App's key (signed with openssl) and minted again before its hour runs out, so a run of any length keeps a
budget of its own. Otherwise it comes from GH_TOKEN or GITHUB_TOKEN, or else from the signed-in GitHub CLI. Calls go straight over HTTP
rather than through a gh process each, which matters when tens of thousands of queries run in a week.

Every answer says how much of the hour's budget is left. When it falls to the reserve in config.toml ([github]), calls
wait for the hour to reset rather than spend the rest: the token may be shared, and a spent budget fails every query.
"""
import base64
import calendar
import http.client
import json
import os
import subprocess
import tempfile
import threading
import time
import urllib.error
import urllib.request

from . import CONFIG

API = "https://api.github.com"
AGENT = "amazing-software-factories (+https://github.com/paul-gross/amazing-software-factories)"
_token = None
_budget = {}   # resource ("graphql", "core", "search") -> (remaining, reset epoch), from the latest answer
_lock = threading.Lock()


class GhError(RuntimeError):
    pass


def _b64(data):
    return base64.urlsafe_b64encode(data).rstrip(b"=").decode()


def app_jwt(app_id, key, now=None):
    """A ten-minute JWT that authenticates as the App itself, RS256-signed by openssl with the App's private key."""
    now = int(now or time.time())
    head = _b64(json.dumps({"alg": "RS256", "typ": "JWT"}).encode())
    body = _b64(json.dumps({"iat": now - 60, "exp": now + 540, "iss": str(app_id)}).encode())
    with tempfile.TemporaryDirectory() as tmp:
        path = os.path.join(tmp, "key.pem")
        fd = os.open(path, os.O_WRONLY | os.O_CREAT, 0o600)
        with os.fdopen(fd, "w") as f:
            f.write(key)
        sig = subprocess.run(["openssl", "dgst", "-sha256", "-sign", path], input=f"{head}.{body}".encode(),
                             capture_output=True, check=True).stdout
    return f"{head}.{body}.{_b64(sig)}"


def _app_token(app_id, key, repo):
    """(token, expiry epoch) for the App's installation on `repo`."""
    headers = {"Authorization": f"Bearer {app_jwt(app_id, key)}", "Accept": "application/vnd.github+json",
               "User-Agent": AGENT, "X-GitHub-Api-Version": "2022-11-28"}
    call = lambda url, data=None: json.loads(urllib.request.urlopen(urllib.request.Request(
        url, data=data, headers=headers, method="POST" if data is not None else "GET"), timeout=60).read())
    installation = call(f"{API}/repos/{repo}/installation")["id"]
    out = call(f"{API}/app/installations/{installation}/access_tokens", b"{}")
    return out["token"], calendar.timegm(time.strptime(out["expires_at"], "%Y-%m-%dT%H:%M:%SZ"))


_expires = None


def token():
    global _token, _expires
    with _lock:
        app_id, key = os.environ.get("ASF_APP_ID"), os.environ.get("ASF_APP_PRIVATE_KEY")
        if app_id and key and (_token is None or time.time() > _expires - 300):
            repo = os.environ.get("GITHUB_REPOSITORY", "paul-gross/amazing-software-factories")
            _token, _expires = _app_token(app_id, key, repo)
        if _token is None:
            _token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN") or subprocess.run(
                ["gh", "auth", "token"], capture_output=True, text=True, check=True).stdout.strip()
    return _token


def _resource(url):
    return "graphql" if url.endswith("/graphql") else "search" if "/search/" in url else "core"


def _note(resource, headers):
    """Remember the budget an answer reports."""
    remaining, reset = headers.get("x-ratelimit-remaining"), headers.get("x-ratelimit-reset")
    if remaining is not None and reset is not None:
        with _lock:
            _budget[headers.get("x-ratelimit-resource") or resource] = (int(remaining), int(reset))


def _wait_for_budget(resource):
    """Sleep until the hour resets when this resource's budget is down to the reserve."""
    reserve = CONFIG["github"]["reserve"].get(resource, 0)
    with _lock:
        remaining, reset = _budget.get(resource, (None, 0))
    wait = reset - time.time() + 5
    if remaining is not None and remaining <= reserve and wait > 0:
        print(f"github: {resource} budget down to {remaining}; waiting {wait / 60:.0f} minutes for the reset", flush=True)
        time.sleep(wait)
        with _lock:
            _budget.pop(resource, None)


def _request(url, body=None, accept="application/vnd.github+json", attempts=8):
    err = ""
    resource = _resource(url)
    for attempt in range(attempts):
        _wait_for_budget(resource)
        req = urllib.request.Request(url, data=json.dumps(body).encode() if body is not None else None, headers={
            "Authorization": f"Bearer {token()}", "Accept": accept, "User-Agent": AGENT,
            "X-GitHub-Api-Version": "2022-11-28"})
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                _note(resource, resp.headers)
                text = resp.read().decode("utf-8", errors="replace")
            # A spent GraphQL budget answers 200 with a RATE_LIMITED error and no data: wait for the reset and ask again.
            if resource == "graphql" and '"RATE_LIMITED"' in text:
                with _lock:
                    _budget[resource] = (0, _budget.get(resource, (0, int(time.time()) + 60))[1])
                err = "RATE_LIMITED"
                continue
            return text
        except urllib.error.HTTPError as exc:
            _note(resource, exc.headers)
            text = exc.read().decode("utf-8", errors="replace")
            # GraphQL can answer partial data with an error status; the caller decides what a null alias means.
            if text.lstrip().startswith("{") and '"data"' in text and '"RATE_LIMITED"' not in text:
                return text
            err = f"HTTP {exc.code}: {text[:300]}"
            if exc.code in (404, 422, 451):
                raise GhError(err)
            # A gateway error that repeats is usually a query too heavy to finish, not a passing outage.
            if exc.code in (502, 504) and attempt >= 2:
                raise GhError(err)
            low = text.lower()
            # A spent primary limit says when it resets; a secondary limit asks for minutes of quiet.
            reset = exc.headers.get("x-ratelimit-reset")
            if exc.headers.get("x-ratelimit-remaining") == "0" and reset:
                wait = max(5, int(reset) - time.time() + 5)
            else:
                wait = 180 if "secondary rate limit" in low else 420 if "rate limit" in low else 5 * (attempt + 1)
        except (urllib.error.URLError, http.client.HTTPException, TimeoutError, ConnectionError) as exc:
            err = str(exc)
            wait = 5 * (attempt + 1)
        time.sleep(wait)
    raise GhError(err[:300])


def graphql(query, **variables):
    body = json.loads(_request(f"{API}/graphql", {"query": query, "variables": variables}))
    if body.get("data") is None:
        raise GhError(json.dumps(body.get("errors"))[:300])
    return body["data"]


def rest(path, accept=None):
    out = _request(f"{API}/{path.lstrip('/')}", accept=accept or "application/vnd.github+json")
    return out if accept and "json" not in accept else json.loads(out)


def batched(items, size):
    for i in range(0, len(items), size):
        yield items[i:i + size]
