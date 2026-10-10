"""Nominate repositories that might be one-person factories. Nomination decides nothing; the screen does.

Three sources, all open:
- GH Archive: busy repositories whose pushes come mostly from one non-bot account.
- Source lists: every GitHub repository linked from the READMEs named in data/source-lists.txt.
- Manual: data/manual.txt, repositories someone named by hand.
"""
import gzip
import json
import re
import urllib.request
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import date, timedelta

from . import CONFIG, DATA, ROOT
from .gh import GhError, rest
from .store import read_list

AGENT = "amazing-software-factories (+https://github.com/paul-gross/amazing-software-factories)"
BOT_ACTOR = re.compile(r"(\[bot\]|-bot|bot|actions|dependabot|renovate)$", re.I)


def _hour(stamp):
    """Push counts per (repo, actor) for one GH Archive hour, e.g. `2026-10-08-15`."""
    counts = Counter()
    req = urllib.request.Request(f"https://data.gharchive.org/{stamp}.json.gz", headers={"User-Agent": AGENT})
    try:
        with urllib.request.urlopen(req, timeout=120) as resp, gzip.GzipFile(fileobj=resp) as lines:
            for raw in lines:
                if b'"PushEvent"' not in raw:
                    continue
                event = json.loads(raw)
                if event.get("type") == "PushEvent":
                    counts[(event["repo"]["name"], event["actor"]["login"])] += 1
    except Exception as exc:  # a missing or truncated hour costs one hour of signal, never the run
        print(f"gharchive {stamp}: {exc}")
    return stamp[:10], counts


def gharchive(end=None):
    cfg = CONFIG["discover"]["gharchive"]
    end = end or date.today()
    days = [end - timedelta(days=i) for i in range(1, cfg["days"] + 1)]
    stamps = [f"{d.isoformat()}-{h}" for d in days for h in range(24)]
    pushes = defaultdict(Counter)
    active = defaultdict(set)
    with ThreadPoolExecutor(cfg["parallel_downloads"]) as pool:
        for day, counts in pool.map(_hour, stamps):
            for (repo, actor), n in counts.items():
                pushes[repo][actor] += n
                active[repo].add(day)
    out = []
    for repo, actors in pushes.items():
        total = sum(actors.values())
        if total < cfg["min_push_events"] or len(active[repo]) < cfg["min_active_days"]:
            continue
        humans = {a: n for a, n in actors.items() if not BOT_ACTOR.search(a)}
        if humans and max(humans.values()) / sum(humans.values()) < cfg["min_lead_pusher_share"]:
            continue
        out.append(repo)
    return out


RESERVED = {"orgs", "topics", "sponsors", "features", "marketplace", "apps", "settings", "login", "about", "search",
            "collections", "trending", "pricing", "enterprise", "readme", "site", "contact", "security", "users"}
LINK = re.compile(r"github\.com/([A-Za-z0-9-]{1,39})/([A-Za-z0-9._-]{1,100})")


def links(markdown):
    """Every `owner/repo` a README links to, in order of first appearance."""
    seen = {}
    for owner, name in LINK.findall(markdown):
        name = re.sub(r"\.git$", "", name).rstrip(".")
        if owner.lower() in RESERVED or not name:
            continue
        seen.setdefault(f"{owner}/{name}".lower(), f"{owner}/{name}")
    return list(seen.values())


def source_lists():
    out = []
    for lst in read_list(DATA / "source-lists.txt"):
        try:
            readme = rest(f"repos/{lst}/readme", accept="application/vnd.github.raw")
        except GhError as exc:
            print(f"source list {lst}: {exc}")
            continue
        out += [r for r in links(readme) if r.lower() != lst.lower()]
    return out


def nominate():
    """Nominees by source, deduplicated case-insensitively; the first source to name a repository keeps it.

    Cached for the day in .cache/, so a rerun after an interruption does not stream the archive again.
    """
    cache = ROOT / ".cache" / f"nominees-{date.today().isoformat()}.json"
    if cache.exists():
        return [tuple(x) for x in json.loads(cache.read_text())]
    found = {}
    for source, repos in (("manual", read_list(DATA / "manual.txt")), ("source-list", source_lists()),
                          ("gharchive", gharchive())):
        for repo in repos:
            found.setdefault(repo.lower(), (repo, source))
        print(f"discover: {source} named {len(repos)}")
    cache.parent.mkdir(exist_ok=True)
    cache.write_text(json.dumps(list(found.values())))
    return list(found.values())
