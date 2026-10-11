"""python -m asf <command>

  find               discover nominees and screen them (layers 1 and 2) into the waiting list, weekly
  gate [minutes]     layers 3 and 4 for the waiting repositories not checked today; what passes is watched for good
  measure [minutes]  measure the classified watched repositories due this hour and not yet measured today
  classify           classify watched repositories the classifier has not seen (runs `claude` locally)
  render             regenerate the README tables, the site data, and the report
  hourly             gate, check the dormant, measure, render: the hourly job
  weekly             find, then keep the week's snapshot
  judge              cold-read the top repositories with LLM judges (run by hand; see rubric/judge-v1.md)
"""
import hashlib
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone

from . import CONFIG, discover, grade, render, watch
from .gh import GhError
from .measure import measure
from .store import (daily, daily_dates, latest, save_daily, save_latest, save_snapshot, screened, today, utc_date,
                    watchlist)


def find():
    discover.sweep()
    day = discover.run_day()
    watch.screen(discover.nominate(day), day.isoformat())


def prior_weeks(repo, snapshots, day):
    """The week tallies of the three weeks before `day`, oldest last, or fewer when a week has no snapshot.

    snapshots: {date: {repo: row}}. A snapshot taken a day early or late still stands for its week, so one delayed
    scheduled run does not throw away a month of history.
    """
    week = CONFIG["window"]["week_days"]
    weeks = CONFIG["window"]["days"] // week - 1
    out = []
    for k in range(1, weeks + 1):
        due = day - timedelta(days=week * k)
        for offset in (0, -1, 1):
            rows = snapshots.get((due + timedelta(days=offset)).isoformat(), {})
            row = next((r for name, r in rows.items() if name.lower() == repo.lower()), None)
            if row and row.get("week_tally"):
                out.append(row["week_tally"])
                break
        else:
            return out
    return out


def baseline(repo, screens, day):
    """The screen's four-week tally, when the screen read this repository within the last week."""
    row = next((r for name, r in screens.items() if name.lower() == repo.lower()), None)
    fresh = (day - timedelta(days=CONFIG["window"]["week_days"])).isoformat()
    return row["month_tally"] if row and row.get("month_tally") and row["screened"] >= fresh else None


def record(row):
    """The compact daily record of a measurement: what trends and the four-week figures need, not the whole row."""
    g = grade.grades(row)
    clock = grade.autonomy_clock(row)
    return dict(repo=row["repo"], date=row["measured"], week_tally=row.get("week_tally"),
                grades={a: g[a]["grade"] for a in grade.AXES}, stars=row["meta"]["stars"],
                prs=row["volume"]["merged_prs_per_day"], commits=row["volume"]["commits_per_day"],
                code=grade.value(row, "code_added_daily_median"), all=grade.value(row, "all_added_per_day"),
                night=grade.value(row, "night_utilization"), day=clock.get("day_utilization"),
                nights=clock.get("nights_covered"))


def hour_of(repo):
    """The UTC hour of the day a repository is measured in, spread evenly by a hash of its name, so each hourly run
    measures a twenty-fourth of the list."""
    return int(hashlib.sha1(repo.lower().encode()).hexdigest(), 16) % 24


def measurable(repo, stored, notes):
    """Only software factories are measured: an active repository classified as an assembly line or built by one."""
    from .kind import KINDS, kind_of
    note = notes.get(repo.lower()) or {}
    return note.get("kind") != "copy" and kind_of(repo, stored, notes) in KINDS[:2]


def measure_due(minutes=None, workers=None, hour=None):
    """Measure the classified watched repositories whose hour of the day has come and that were not measured today,
    earliest hour first, until `minutes` pass. A run that missed an hour catches up on the next one. Each row replaces
    the repository's row in data/latest.jsonl and adds a record to data/daily/."""
    from .kind import kinds
    from .store import annotations
    cfg = CONFIG["measure"]
    minutes = cfg["minutes"] if minutes is None else minutes
    deadline = time.monotonic() + minutes * 60
    hour = datetime.now(timezone.utc).hour if hour is None else hour
    rows = latest()
    by_lower = {r.lower(): r for r in rows}
    current = lambda repo: rows.get(by_lower.get(repo.lower(), repo)) or {}
    stored, notes = kinds(), annotations()
    due = sorted((r for r, e in watchlist().items() if e["status"] == "active" and hour_of(r) <= hour
                  and current(r).get("measured", "") < today() and measurable(r, stored, notes)),
                 key=lambda r: (hour_of(r), current(r).get("measured", "")))
    print(f"measure: {len(due)} watched repositories due; {minutes} minutes to measure them")
    day = utc_date()
    oldest = (day - timedelta(days=CONFIG["window"]["days"])).isoformat()
    records = {d: daily(d) for d in daily_dates() if oldest <= d < day.isoformat()}
    screens = screened()

    def one(repo):
        if time.monotonic() > deadline:
            return None
        try:
            return measure(repo, prior_weeks(repo, records, day), baseline(repo, screens, day))
        except (GhError, KeyError, TypeError) as exc:
            print(f"measure {repo}: {exc}")
            return None

    done = []
    with ThreadPoolExecutor(workers or cfg["workers"]) as pool:
        for row in pool.map(one, due):
            if not row:
                continue
            rows.pop(by_lower.get(row["repo"].lower(), row["repo"]), None)
            rows[row["repo"]] = row
            by_lower[row["repo"].lower()] = row["repo"]
            done.append(row)
            if len(done) % 20 == 0:
                save_latest(rows)
                save_daily(today(), [record(r) for r in done[-20:]])
    save_latest(rows)
    save_daily(today(), [record(r) for r in done[len(done) // 20 * 20:]])
    watch.update_statuses(done)
    print(f"measure: measured {len(done)}; {len(due) - len(done)} still due today")
    return done


def snapshot_week():
    """Keep this week's full rows: every watched repository's latest row measured in the last two days."""
    cut = (utc_date() - timedelta(days=2)).isoformat()
    rows = [r for r in latest().values() if r.get("measured", "") >= cut]
    save_snapshot(today(), rows)
    print(f"snapshot: kept {len(rows)} rows")


def classify():
    from .kind import classify as run
    rows, wl = latest(), watchlist()
    watched = [r for r, e in wl.items() if e["status"] != "opted-out"]
    run(watched, rows={r: rows[r] for r in watched if r in rows}, gates={r: wl[r]["gate"] for r in watched if wl[r].get("gate")})


def main(argv):
    command = argv[1] if len(argv) > 1 else ""
    minutes = float(argv[2]) if len(argv) > 2 else None
    if command == "find":
        find()
    elif command == "gate":
        watch.gate(minutes)
    elif command == "measure":
        measure_due(minutes)
    elif command == "classify":
        classify()
    elif command == "render":
        render.render()
        render.report()
    elif command == "hourly":
        watch.gate()
        watch.revive()
        measure_due()
        render.render()
        render.report()
    elif command == "weekly":
        find()
        snapshot_week()
    elif command == "judge":
        from . import judge
        judge.run(argv[2:])
    else:
        print(__doc__)
        return 2
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
