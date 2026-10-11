"""The committed data files: the watchlist, screen results, latest rows, daily records, weekly snapshots and
annotations."""
import json
import tomllib
from datetime import date, datetime, timezone

from . import DATA


def read_jsonl(path):
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text().splitlines() if line.strip()]


def write_jsonl(path, rows, key="repo"):
    path.parent.mkdir(parents=True, exist_ok=True)
    rows = sorted(rows, key=lambda r: r[key].lower())
    path.write_text("".join(json.dumps(r, sort_keys=True, ensure_ascii=False) + "\n" for r in rows))


def read_list(path):
    """A plain list file: one `owner/repo` per line, `#` starts a comment."""
    if not path.exists():
        return []
    out = []
    for line in path.read_text().splitlines():
        line = line.split("#", 1)[0].strip()
        if line:
            out.append(line)
    return out


def watchlist():
    return {r["repo"]: r for r in read_jsonl(DATA / "watchlist.jsonl")}


def save_watchlist(rows):
    write_jsonl(DATA / "watchlist.jsonl", rows.values())


def screened():
    return {r["repo"]: r for r in read_jsonl(DATA / "screened.jsonl")}


def save_screened(rows):
    write_jsonl(DATA / "screened.jsonl", rows.values())


def latest():
    """{repo: its newest measurement}: every watched repository's current row, rewritten as each is measured."""
    return {r["repo"]: r for r in read_jsonl(DATA / "latest.jsonl")}


def save_latest(rows):
    write_jsonl(DATA / "latest.jsonl", sorted(rows.values(), key=lambda r: r["repo"].lower()))


def daily_dates():
    return sorted(p.stem for p in (DATA / "daily").glob("*.jsonl"))


def daily(day):
    """{repo: the compact record of its measurement on `day`}: grades, headline numbers and the week's tally."""
    return {r["repo"]: r for r in read_jsonl(DATA / "daily" / f"{day}.jsonl")}


def save_daily(day, records):
    """Merge records into the day's file: a repository measured twice in a day keeps its later record."""
    rows = daily(day)
    rows.update({r["repo"]: r for r in records})
    write_jsonl(DATA / "daily" / f"{day}.jsonl", rows.values())


def annotations():
    """{owner/repo in lower case: {kind, reason}}."""
    path = DATA / "annotations.toml"
    notes = tomllib.loads(path.read_text()).get("repo", {}) if path.exists() else {}
    return {repo.lower(): note for repo, note in notes.items()}


def snapshot_dates():
    return sorted(p.stem for p in (DATA / "snapshots").glob("*.jsonl"))


def snapshot(day):
    return {r["repo"]: r for r in read_jsonl(DATA / "snapshots" / f"{day}.jsonl")}


def save_snapshot(day, rows):
    write_jsonl(DATA / "snapshots" / f"{day}.jsonl", rows)


def utc_date():
    """Today's date in UTC: every date the data records is a UTC date, wherever the run happens."""
    return datetime.now(timezone.utc).date()


def today():
    return utc_date().isoformat()
