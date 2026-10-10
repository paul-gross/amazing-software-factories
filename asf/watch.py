"""Screen nominees into the watchlist, and keep the watchlist's statuses current.

The screen is a funnel of layers, cheapest first; each sends on only what it cannot rule out:

1. Totals: not archived, not a fork, enough code, at least the daily commit floor over four weeks, sustained in most
   of those weeks. Forty repositories per query, one point each.
2. Not a team: authors of the newest commits. One human writing most of the human commits passes, and so does a
   repository whose commits all come from bots or unclaimed identities.
3. Runs without people: commits in each two-hour slot of the measured week, counts only, so every repository waiting
   here is checked again each day. Work must land through the night, on most nights. Anyone can open ten terminals
   and land hundreds of commits; landing them while asleep, night after night, takes a factory.
4. Varied changes by one person: the newest hundred commits of the last week. A scheduled job that rewrites a data
   file repeats one message; the strict one-person test applies here, since a hundred commits needs no slack.

What passes layer 4 joins the watchlist for good, one way: it is measured every day from then on, however its numbers
move. What passes layer 2 but not the rest waits in data/screened.jsonl and is checked again the next day.

Every threshold lives in config.toml.
"""
import json
import os
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime, timedelta, timezone

from . import CONFIG, ROOT
from .gh import GhError, batched
from .measure import authors, clock_slots, created, facts, parse, recent, slot_clock
from .store import save_screened, save_watchlist, screened, today, watchlist

AUTHOR_CACHE_VERSION = 2  # bump when the meaning of a cached author sample changes


def not_a_team(lead_share, machine_share, threshold=None):
    """The one-person test rules out teams, nothing else. One human writing most of the human commits passes; so does a
    repository with no human authors at all, since a fleet committing under bot accounts is not a team either."""
    threshold = CONFIG["admit"]["min_lead_human_share"] if threshold is None else threshold
    if lead_share is None:
        return machine_share == 1.0
    return lead_share >= threshold


def passes_totals(f, days=None, now=None):
    """Layer 1 on one repository's totals: live, original, real code, and the daily commit floor both over the window
    and in most of its weeks, so a single burst does not carry a quiet month. A repository younger than the window is
    held to the floor over the days and whole weeks it has existed, not over weeks before it was created."""
    cfg = CONFIG["screen"]
    days = days or CONFIG["window"]["days"]
    week = CONFIG["window"]["week_days"]
    age = days
    if f.get("created"):
        now = now or datetime.now(timezone.utc)
        age = min(days, max(week, (now - parse(f["created"])).days))
    weeks_needed = min(cfg["min_active_weeks"], max(1, age // week))
    return (not f["archived"] and not f["fork"] and f["code_bytes"] >= cfg["min_code_kb"] * 1024
            and f["commits"] >= cfg["min_commits_per_day"] * age
            and sum(1 for c in f.get("weeks", ()) if c >= cfg["min_commits_per_day"] * week) >= weeks_needed)


def runs_unattended(c):
    """Layer 3 on one repository's clock: work lands through the night, on most nights of the week."""
    g = CONFIG["gate"]
    return ((c.get("night_utilization") or 0) >= g["min_night_utilization"]
            and (c.get("nights_covered") or 0) >= g["min_nights_covered"])


def passes_recent(r):
    """Layer 4 on one repository's newest commits: varied messages, and not a team by the strict test."""
    cfg = CONFIG["screen"]
    return (r["sampled"] >= cfg["min_message_sample"] and (r["variety"] or 0) >= cfg["min_message_variety"]
            and not_a_team(r["lead_human_share"], r["machine_share"]))


def _cache(name):
    path = ROOT / ".cache" / name
    return path, (json.loads(path.read_text()) if path.exists() else {})


def _save(path, data):
    path.parent.mkdir(exist_ok=True)
    path.write_text(json.dumps(data))


def screen(nominees, workers=None):
    """nominees: [(repo, source)]. Layers 1 and 2, weekly: what passes waits in data/screened.jsonl for the gate
    (layers 3 and 4), and what no longer passes stops waiting. Returns the repositories now waiting."""
    cfg, a, w = CONFIG["screen"], CONFIG["admit"], CONFIG["window"]
    days, week = w["days"], w["week_days"]
    workers = workers or int(os.environ.get("ASF_WORKERS", cfg["workers"]))
    funnel = {"nominated": len(nominees)}
    # Author samples stand this long, so most nominees are not sampled again each week.
    fresh = (date.today() - timedelta(days=cfg["rescreen_after_days"])).isoformat()

    # Whatever is on the watchlist passed the gate for good and is measured instead.
    watched = {r.lower() for r in watchlist()}
    todo = list({r.lower(): (r, s) for r, s in nominees if r.lower() not in watched}.values())
    source = {r.lower(): s for r, s in todo}
    funnel["to check"] = len(todo)
    print(f"screen: {len(todo)} nominees to check")

    # Layer 1: totals, cached for the day so a rerun after an interruption starts further on.
    facts_path, known = _cache(f"facts-{today()}.json")
    if not known:
        known = facts([r for r, _ in todo], days, workers)
        _save(facts_path, known)
    # Totals cached before weekly counts were recorded get them now, but only where the other totals already pass:
    # a weekly count walks history, which is the slow part of the query.
    lacking = [f["canonical"] for f in known.values()
               if "weeks" not in f and passes_totals(dict(f, weeks=[float("inf")] * 4), days)]
    if lacking:
        print(f"screen: counting weekly commits for {len(lacking)} repositories")
        weekly = {f["canonical"]: f["weeks"] for f in facts(lacking, days, workers, size=20).values()}
        for f in known.values():
            if f["canonical"] in weekly:
                f["weeks"] = weekly[f["canonical"]]
        _save(facts_path, known)
    # Totals cached before creation dates were recorded get them where youth could matter: everything else passes
    # and the repository committed at least a week's floor.
    young = [f["canonical"] for f in known.values()
             if "created" not in f and not passes_totals(f, days)
             and passes_totals(dict(f, commits=float("inf"), weeks=[float("inf")] * 4), days)
             and f["commits"] >= cfg["min_commits_per_day"] * week]
    if young:
        print(f"screen: reading creation dates for {len(young)} repositories")
        born = created(young, workers)
        for f in known.values():
            if f["canonical"] in born:
                f["created"] = born[f["canonical"]]
        _save(facts_path, known)
    busy = {f["canonical"]: f for f in known.values() if passes_totals(f, days) and f["canonical"].lower() not in watched}
    funnel["layer 1, totals"] = len(busy)
    print(f"screen: {len(busy)} pass layer 1 (totals)")

    # Layer 2: not a team, from a small author sample with a loose margin.
    author_path, sampled = _cache("authors.json")
    stale = [r for r in busy if sampled.get(r, {}).get("v") != AUTHOR_CACHE_VERSION
             or sampled[r].get("date", "") < fresh]
    print(f"screen: sampling authors for {len(stale)} repositories")
    for part in batched(stale, 1000):
        for r, v in authors(part, days, cfg["author_sample"], workers).items():
            sampled[r] = dict(v, date=today(), v=AUTHOR_CACHE_VERSION)
        _save(author_path, sampled)
    solo = [r for r in busy if r in sampled and not_a_team(sampled[r]["lead_human_share"], sampled[r]["machine_share"],
                                                            a["min_lead_human_share"] * cfg["author_slack"])]
    funnel["layer 2, not a team"] = len(solo)
    print(f"screen: {len(solo)} pass layer 2 (not a team)")

    # Everything that passed layer 2 waits for layer 3, which `gate` runs: today for what is new, daily after that.
    waiting = screened()
    for r in solo:
        row = waiting.get(r) or dict(repo=r, source=source.get(r.lower(), "gharchive"))
        row.update(screened=today(), status="waiting", commits_per_day=round(busy[r]["commits"] / days, 1),
                   lead_human_share=sampled[r]["lead_human_share"])
        waiting[r] = row
    keep = set(solo)
    for r, row in waiting.items():
        if r not in keep and row.get("status") == "waiting":
            row.update(status="out", out_since=today())   # fell below layer 1 or 2; back if it qualifies again
    save_screened(waiting)
    _save(ROOT / ".cache" / f"funnel-{today()}.json", funnel)
    return solo


def gate(minutes=None, workers=None):
    """Layers 3 and 4 for the repositories waiting in data/screened.jsonl that were not checked today, oldest check
    first, until `minutes` run out. What passes both joins the watchlist for good. Returns the newly admitted."""
    cfg, g, w = CONFIG["screen"], CONFIG["gate"], CONFIG["window"]
    workers = workers or int(os.environ.get("ASF_WORKERS", cfg["workers"]))
    minutes = g["minutes"] if minutes is None else minutes
    deadline = time.monotonic() + minutes * 60
    rows, wl = screened(), watchlist()
    listed = {r.lower() for r in wl}
    due = sorted((r for r, row in rows.items() if row.get("status") == "waiting" and r.lower() not in listed
                  and row.get("gate_checked", "") < today()), key=lambda r: rows[r].get("gate_checked", ""))
    print(f"gate: {len(due)} waiting repositories due; {minutes} minutes to check them")
    passed, checked = [], 0
    for part in batched(due, g["batch"]):
        if time.monotonic() > deadline:
            break
        for r, v in clock_slots(part, w["lag_days"], w["week_days"], workers).items():
            c = slot_clock(v["slots"], v["end"], w["week_days"])
            rows[r].update(gate_checked=today(), night_utilization=c["night_utilization"],
                           nights_covered=c["nights_covered"], nights_seen=c["nights_seen"])
            checked += 1
            if runs_unattended(c):
                passed.append(r)
        save_screened(rows)
    # Layer 4 for what passed layer 3: a scheduled job repeats itself; a team is not one person.
    last = recent(passed, w["week_days"], cfg["message_sample"], workers) if passed else {}
    added = []
    for r in passed:
        lead = last.get(r)
        rows[r].update(variety=(lead or {}).get("variety"))
        if lead and passes_recent(lead):
            rows[r].update(status="admitted", admitted=today())
            wl[r] = dict(repo=r, added=today(), source=rows[r].get("source", "gharchive"), status="active",
                         status_since=today(), gate_passed=today(),
                         gate=dict(night_utilization=rows[r]["night_utilization"], nights_covered=rows[r]["nights_covered"]))
            added.append(r)
    save_screened(rows)
    save_watchlist(wl)
    print(f"gate: checked {checked}; {len(passed)} run unattended; admitted {len(added)}")
    return added


def update_statuses(rows):
    """After measuring: mark archived repositories, which are no longer measured. Nothing else leaves the watchlist:
    passing the gate is for good."""
    wl = watchlist()
    by_lower = {r.lower(): r for r in wl}
    for row in rows:
        key = by_lower.get(row["repo"].lower())
        if key and row["meta"].get("archived") and wl[key]["status"] != "archived":
            wl[key].update(status="archived", status_since=today())
    save_watchlist(wl)
