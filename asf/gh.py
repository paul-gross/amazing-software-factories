"""Read-only access to GitHub's APIs over HTTPS, with retries for rate limits and transient failures.

The token comes from GH_TOKEN or GITHUB_TOKEN, or else from the signed-in GitHub CLI. Calls go straight over HTTP
rather than through a gh process each, which matters when tens of thousands of queries run in a week.
"""
import http.client
import json
import os
import subprocess
import time
import urllib.error
import urllib.request

API = "https://api.github.com"
AGENT = "amazing-software-factories (+https://github.com/paul-gross/amazing-software-factories)"
_token = None


class GhError(RuntimeError):
    pass


def token():
    global _token
    if _token is None:
        _token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN") or subprocess.run(
            ["gh", "auth", "token"], capture_output=True, text=True, check=True).stdout.strip()
    return _token


def _request(url, body=None, accept="application/vnd.github+json", attempts=8):
    err = ""
    for attempt in range(attempts):
        req = urllib.request.Request(url, data=json.dumps(body).encode() if body is not None else None, headers={
            "Authorization": f"Bearer {token()}", "Accept": accept, "User-Agent": AGENT,
            "X-GitHub-Api-Version": "2022-11-28"})
        try:
            with urllib.request.urlopen(req, timeout=120) as resp:
                return resp.read().decode("utf-8", errors="replace")
        except urllib.error.HTTPError as exc:
            text = exc.read().decode("utf-8", errors="replace")
            # GraphQL can answer partial data with an error status; the caller decides what a null alias means.
            if text.lstrip().startswith("{") and '"data"' in text:
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
