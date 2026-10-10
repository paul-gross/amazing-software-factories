"""Letter grades on three axes: output, autonomy and discipline.

On each axis a repository earns the highest letter whose every requirement it meets, and F when it meets none. The
requirements live in config.toml under [grades.<axis>.<letter>], from A down. A requirement names a measurement with a
floor (`added_per_day = 10000`), a ceiling (`largest_file_kb_max = 500`), or a list of pull-request checks that must
all run (`pr_checks = ["tests", "lint"]`).

Grades read a snapshot row and nothing else, so any past snapshot can be regraded when the requirements change.
"""
from . import CONFIG

AXES = ("output", "autonomy", "discipline")
CHECKS = {"tests": "pr_runs_tests", "lint": "pr_runs_lint", "typecheck": "pr_runs_typecheck"}


def value(row, name):
    """One measurement from a snapshot row, by the name the requirements use."""
    volume, prs = row.get("volume") or {}, row.get("prs") or {}
    clock = autonomy_clock(row)
    structure, ci = row.get("structure") or {}, row.get("ci") or {}
    if name in ("added_per_day", "deleted_per_day", "net_per_day"):
        # All files' lines from the four-week read if it counted any, else the last week's.
        return volume[name] if volume.get(name) is not None else (row.get("week") or {}).get(name)
    if name in ("code_added_daily_median", "code_added_per_day", "code_deleted_per_day", "all_added_per_day"):
        code = row.get("code_lines") or {}
        return code.get(name) if code.get("status") == "ok" else None
    return {
        "merged_prs_per_day": volume.get("merged_prs_per_day"),
        "commits_per_day": volume.get("commits_per_day"),
        "quietest_6h_share": clock.get("quietest_6h_share"),
        "night_utilization": night_utilization(clock),
        "day_utilization": clock.get("day_utilization"),
        "nights_missed": (clock["nights_seen"] - clock["nights_covered"]) if "nights_seen" in clock else None,
        "active_days": clock.get("active_days"),
        "peak_open_prs": prs.get("peak_open_prs"),
        "ci_runs": ci.get("ci_runs"),
        "ci_green": ci.get("green_share") if (ci.get("ci_runs") or 0) >= 10 else None,
        "largest_file_kb": structure.get("largest_file_kb"),
        "test_ratio": structure.get("test_ratio"),
    }.get(name)


def autonomy_clock(row):
    """The clock autonomy is graded on: the commits that changed code, from the week's clone; without a clone, every
    commit on the default branch."""
    code = row.get("code_lines") or {}
    return (code.get("clock") if code.get("status") == "ok" else None) or row.get("clock") or {}


def night_utilization(clock):
    """The quietest six hours' share of commits against an even spread's quarter: 1.0 is round the clock."""
    if clock.get("night_utilization") is not None:
        return clock["night_utilization"]
    quiet = clock.get("quietest_6h_share")
    return None if quiet is None else round(quiet * 4, 3)


def check(row, key, want):
    """(met, wanted, has) for one requirement."""
    if key == "pr_checks":
        gates = row.get("gates") or {}
        has = [c for c in want if gates.get(CHECKS[c])]
        return len(has) == len(want), want, has
    if key.endswith("_max"):
        has = value(row, key[:-4])
        return has is not None and has <= want, want, has
    has = value(row, key)
    return has is not None and has >= want, want, has


def grade(row, axis):
    """{grade, missing}: the letter earned on one axis, and what stands between the repository and the next one up."""
    ladder = CONFIG["grades"][axis]
    letters = list(ladder)
    earned, missing = "F", {}
    for i, letter in enumerate(letters):
        results = {k: check(row, k, v) for k, v in ladder[letter].items()}
        if all(met for met, _, _ in results.values()):
            earned = letter
            break
    if earned == "F":
        above = letters[-1]
    elif earned != letters[0]:
        above = letters[letters.index(earned) - 1]
    else:
        above = None
    if above:
        missing = {k: dict(want=w, has=h) for k, (met, w, h) in
                   ((k, check(row, k, v)) for k, v in ladder[above].items()) if not met}
    return dict(grade=earned, missing=missing)


def grades(row):
    """{axis: {grade, missing}} for every axis."""
    return {axis: grade(row, axis) for axis in AXES}
