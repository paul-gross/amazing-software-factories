"""Turn the watched repositories' latest rows into the README tables, the site's data file, and the weekly report.

Only repositories that passed the gate are watched, and of those only software factories are listed: what the
classifier has read and found to be an assembly line, or something built by one. Nothing that sleeps is ever shown,
nor anything not yet classified."""
import json
import re

from . import CONFIG, DATA, ROOT, grade
from .kind import kind_of, kinds
from .store import annotations, daily, daily_dates, latest, screened, snapshot, snapshot_dates, today, watchlist

SECTIONS = ("Assembly lines", "Built by an assembly line", "Awaiting classification", "Not software", "Copies and forks",
            "Agent-assisted")
LISTED = SECTIONS[:2]
BY_KIND = {"assembly line": SECTIONS[0], "built by an assembly line": SECTIONS[1], "not software": SECTIONS[3],
           "agent-assisted": SECTIONS[5]}


def section(row, notes, stored):
    """(section, reason): what kind of watched repository this is, from a hand annotation or the classifier."""
    note = notes.get(row["repo"].lower()) or {}
    if note.get("kind") == "copy" or row["meta"].get("fork"):
        return SECTIONS[4], note.get("reason", "fork")
    found = kind_of(row["repo"], stored, notes)
    reason = note.get("reason") or (stored.get(row["repo"].lower()) or {}).get("reason", "")
    return BY_KIND.get(found, SECTIONS[2]), reason


def lines(row):
    """Lines per day as graded: code (source and tests, each file netted per day) from the week's clone, and all files.
    Without a clone, all-file lines fall back to GitHub's stats or the commit read, and code is unknown."""
    code = row.get("code_lines") or {}
    if code.get("status") == "ok":
        return dict(code=code.get("code_added_daily_median"), code_mean=code["code_added_per_day"],
                    code_net=code["code_added_per_day"] - code["code_deleted_per_day"],
                    all=code["all_added_per_day"], source=f"clone of the last {code['days']} days")
    return dict(code=None, code_net=None, all=grade.value(row, "added_per_day"), source="commit read",
                missing=code.get("status"))


def latest_judgments():
    """{repo: final judgment} from the most recent judgment file of each repository."""
    out = {}
    for path in sorted((DATA / "judgments").glob("*/*.json")):
        j = json.loads(path.read_text())
        out[j["repo"]] = j
    return out


def history():
    """{repo: [{date, stars, prs, code, all, commits, grades}]} from the daily records, oldest first."""
    out = {}
    for day in daily_dates():
        for repo, rec in daily(day).items():
            out.setdefault(repo, []).append({k: rec.get(k) for k in ("date", "stars", "prs", "code", "all", "commits", "grades")})
    return out


def star_change(points):
    return points[-1]["stars"] - points[-2]["stars"] if len(points) >= 2 else None


def num(x, unit=""):
    if x is None:
        return "–"
    return f"{x:,.1f}{unit}" if isinstance(x, float) and x < 100 else f"{round(x):,}{unit}"


def pct(x):
    return "–" if x is None else f"{round(x * 100)}%"


def letters(row):
    g = grade.grades(row)
    return " ".join(g[a]["grade"] for a in grade.AXES)


def table(rows, hist):
    head = ("| Repository | Output · Autonomy · Discipline | Code lines/day | All lines/day | PRs/day | Night utilization | Day utilization "
            "| Main CI green | Largest file | Stars (week) |\n|---|:-:|--:|--:|--:|--:|--:|--:|--:|--:|")
    out = [head]
    for r in rows:
        v, s, c, n = r["volume"], r.get("structure") or {}, r.get("ci") or {}, lines(r)
        delta = star_change(hist.get(r["repo"], []))
        stars = f'{r["meta"]["stars"]:,}' + (f" ({delta:+,})" if delta is not None else "")
        out.append(f'| [{r["repo"]}](https://github.com/{r["repo"]}) | {letters(r)} | {num(n["code"])} | {num(n["all"])} '
                   f'| {num(v["merged_prs_per_day"])} | {pct(grade.value(r, "night_utilization"))} | {pct(grade.value(r, "day_utilization"))} '
                   f'| {pct(c.get("green_share"))} | {num(s.get("largest_file_kb"), " KB")} | {stars} |')
    return "\n".join(out)


DIMENSIONS = ("architecture", "code_quality", "test_substance", "product_reality", "change_discipline", "factory_harness")


def judged_table(judged):
    head = ("| Repository | Architecture | Code | Tests | Product reality | Change discipline | Harness | Judges |\n"
            "|---|:-:|:-:|:-:|:-:|:-:|:-:|---|")
    out = [head]
    for j in sorted(judged.values(), key=lambda j: j["repo"].lower()):
        f = j["final"]
        cells = " | ".join(str(f[d]["score"]) + ("±" if f[d]["spread"] > 1 else "") for d in DIMENSIONS)
        out.append(f'| [{j["repo"]}](https://github.com/{j["repo"]}) | {cells} | {len(j["judges"])}, {j["date"]} |')
    return "\n".join(out)


def sort_key(r):
    return -(lines(r)["code"] or 0), -(r["volume"]["merged_prs_per_day"] or 0)


def readme(day, rows, notes, hist, judged, stored):
    grouped = {name: [] for name in LISTED}
    for r in rows:
        grouped[section(r, notes, stored)[0]].append(r)
    out = [f"_{len(rows)} repos, last measured {day}. Sorted by code lines on the median day. The "
           "[site](https://paul-gross.github.io/amazing-software-factories/) has the same data and sorts by anything._"]
    for name in LISTED:
        group = sorted(grouped[name], key=sort_key)
        if group:
            out.append(f"\n### {name} ({len(group)})\n")
            out.append(table(group, hist))
    if judged:
        out.append(f"\n### Cold reads ({len(judged)})\n")
        out.append("Each repository below was read by independent LLM judges against [the judge rubric](rubric/judge-v1.md),"
                   " scored 1–5. ± marks a dimension where judges disagreed by more than a point.\n")
        out.append(judged_table(judged))
    return "\n".join(out)


def write_readme(text):
    path = ROOT / "README.md"
    body = path.read_text()
    new = re.sub(r"(<!-- BEGIN GENERATED -->\n).*?(<!-- END GENERATED -->)", lambda m: m.group(1) + text + "\n" + m.group(2),
                 body, flags=re.S)
    path.write_text(new)


def site_data(day, rows, notes, hist, judged, stored, counts):
    items = []
    for r in rows:
        name, reason = section(r, notes, stored)
        items.append(dict(r, section=name, reason=reason, grades=grade.grades(r), lines=lines(r),
                          aclock=grade.autonomy_clock(r),
                          history=hist.get(r["repo"], []), judgment=judged.get(r["repo"])))
    payload = dict(asof=day, window_days=CONFIG["window"]["days"], lag_days=CONFIG["window"]["lag_days"],
                   sections=LISTED, axes=grade.AXES, ladders=CONFIG["grades"], gate=CONFIG["gate"], counts=counts,
                   rows=items)
    (ROOT / "docs" / "data.js").write_text("window.ASF = " + json.dumps(payload, ensure_ascii=False) + ";\n")


def listed(rows=None, notes=None, stored=None):
    """The rows to show: watched repositories, newest row each, that are software and not copies."""
    notes = annotations() if notes is None else notes
    stored = kinds() if stored is None else stored
    watched = {r.lower() for r, e in watchlist().items() if e["status"] in ("active", "archived")}
    rows = list(latest().values()) if rows is None else rows
    return [r for r in rows if r["repo"].lower() in watched and section(r, notes, stored)[0] in LISTED]


def render(rows=None):
    notes, hist, judged, stored = annotations(), history(), latest_judgments(), kinds()
    rows = listed(rows, notes, stored)
    day = max((r.get("measured", "") for r in rows), default=today())
    waiting = screened()
    counts = dict(watched=len(watchlist()), listed=len(rows),
                  waiting=sum(1 for r in waiting.values() if r.get("status") == "waiting"),
                  checked_today=sum(1 for r in waiting.values() if r.get("gate_checked") == today()))
    judged = {k: v for k, v in judged.items() if k in {r["repo"] for r in rows}}
    write_readme(readme(day, rows, notes, hist, judged, stored))
    site_data(day, rows, notes, hist, judged, stored, counts)
    print(f"render: {len(rows)} repositories listed, as of {day}")


# --- the weekly report ------------------------------------------------------------------------------------------

def report():
    days = snapshot_dates()
    if not days:
        return
    day = days[-1]
    now = snapshot(day)
    notes, stored = annotations(), kinds()
    out = [f"# Week of {day}", ""]
    if len(days) < 2:
        out.append(f"First snapshot: {len(now)} repositories measured. Changes are reported from the next run on.")
    else:
        before = snapshot(days[-2])
        tier_now = {r: letters(row) for r, row in now.items()}
        tier_before = {r: letters(row) for r, row in before.items()}
        new = sorted(set(now) - set(before), key=str.lower)
        gone = sorted(set(before) - set(now), key=str.lower)
        moved = sorted((r for r in now if r in before and tier_now[r] != tier_before[r]), key=str.lower)
        out.append(f"Compared with {days[-2]}: {len(now)} repositories measured, {len(new)} new, {len(gone)} no longer "
                   f"measured, {len(moved)} changed grade.")
        if new:
            out += ["", "## New", ""] + [f"- [{r}](https://github.com/{r}): {section(now[r], notes, stored)[0]}, "
                                         f"grades {tier_now[r]}, {num(now[r]['volume']['merged_prs_per_day'])} PRs/day, "
                                         f"{num(lines(now[r])['code'])} code lines/day" for r in new]
        if gone:
            out += ["", "## No longer measured", ""] + [f"- [{r}](https://github.com/{r})" for r in gone]
        if moved:
            out += ["", "## Changed grade (output, autonomy, discipline)", ""] + [
                f"- [{r}](https://github.com/{r}): {tier_before[r]} → {tier_now[r]}" for r in moved]
        both = [r for r in now if r in before]
        measures = (("merged PRs per day", lambda row: row["volume"]["merged_prs_per_day"]),
                    ("code lines per day", lambda row: lines(row)["code"]))
        for title, get in measures:
            change = sorted(((get(now[r]) or 0) - (get(before[r]) or 0), r) for r in both)
            top = [c for c in change[::-1][:5] if c[0] > 0] + [c for c in change[:5] if c[0] < 0]
            if top:
                out += ["", f"## Biggest moves: {title}", ""]
                out += [f"- [{r}](https://github.com/{r}): {num(get(before[r]))} → {num(get(now[r]))}" for _, r in top]
        stars = sorted(((now[r]["meta"]["stars"] - before[r]["meta"]["stars"], r) for r in both), reverse=True)[:5]
        if stars and stars[0][0] > 0:
            out += ["", "## Most new stars", ""] + [f"- [{r}](https://github.com/{r}): {d:+,}" for d, r in stars if d > 0]
    (ROOT / "reports").mkdir(exist_ok=True)
    (ROOT / "reports" / f"{day}.md").write_text("\n".join(out) + "\n")
    print(f"report: reports/{day}.md")
