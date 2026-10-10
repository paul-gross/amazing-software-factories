"""Rubric v1: place a measured repository in a tier from its gates and its health. Documented in rubric/v1.md.

The rubric reads a snapshot row and nothing else, so any past snapshot can be rescored under a later version.
"""
VERSION = "v1"
TIERS = ("Gated and holding", "Gated, under strain", "Lightly gated")


def gate_points(row):
    g, s = row.get("gates") or {}, row.get("structure") or {}
    points = 2 * bool(g.get("pr_runs_tests")) + bool(g.get("pr_runs_lint")) + bool(g.get("pr_runs_typecheck"))
    points += min(2, len(g.get("boundary_tools") or []))
    points += bool(g.get("strict_typing"))
    ratio = s.get("test_ratio") or 0
    points += 2 if ratio >= 0.8 else 1 if ratio >= 0.4 else -1 if ratio < 0.15 else 0
    return points


def health_points(row):
    c, s = row.get("ci") or {}, row.get("structure") or {}
    points = 0
    green = c.get("green_share")
    if green is not None and c.get("ci_runs", 0) >= 10:
        points += 2 if green >= 0.8 else 1 if green >= 0.5 else -2 if green < 0.3 else 0
    largest = s.get("largest_file_kb")
    if largest is not None:
        points += 1 if largest <= 100 else -2 if largest > 1024 else -1 if largest > 500 else 0
    tenth = s.get("tenth_largest_file_kb")
    if tenth is not None and tenth > 200:
        points -= 1
    return points


def tier(row):
    g, h = gate_points(row), health_points(row)
    if g >= 6 and h >= 1:
        name = TIERS[0]
    elif g >= 6 or (g >= 4 and h >= 1):
        name = TIERS[1]
    else:
        name = TIERS[2]
    return dict(tier=name, gate_points=g, health_points=h, rubric=VERSION)
