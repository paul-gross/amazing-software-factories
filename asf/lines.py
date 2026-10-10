"""Lines of code a repository's last days of commits added, from a short-lived shallow clone.

GitHub's APIs either diff one commit per call or only serve line stats it has already cached, so the lines come from
git itself: a bare, shallow clone of just the window, counted with `git log --numstat`, then deleted at once. Nothing
is checked out, built or run; hooks are pointed at /dev/null and LFS content is never fetched.

Lines are split by kind of file (source, test, other: docs, data, generated, vendored), and four kinds of produced
code are kept out of the code count, judged by content rather than by name:

- generated: a file whose newest version opens with a code generator's marker (`Code generated ... DO NOT EDIT.`,
  `@generated`, `auto-generated`);
- copies: a file version whose exact content was already counted at another path counts once;
- templates: when one commit adds the same number of lines to many files at once, they were stamped out, not written;
- rewrites: each file's changes are netted per day, so a file regenerated hundreds of times a day counts by how much it
  really grew that day.

The clone also gives the times of the commits that changed code, the clock autonomy is graded on: a scheduled job
refreshing data or a dependency bot bumping a lock file lands at night too, but writes no code.

A shallow clone cuts history at the window's edge, and git diffs a commit whose parents were cut against nothing, as
if it added the whole tree. Commits without parents are therefore skipped: they are cut-off edges or a repository's
first import, not work written in the window.
"""
import os
import re
import shutil
import statistics
import subprocess
import tempfile
import time
from collections import Counter, defaultdict

from . import CONFIG, ROOT
from .measure import classify, clock, iso, parse, window

GIT_ENV = {"GIT_TERMINAL_PROMPT": "0", "GIT_LFS_SKIP_SMUDGE": "1", "GIT_CONFIG_NOSYSTEM": "1", "HOME": "/nonexistent",
           "PATH": "/usr/bin:/bin"}
GIT = ["git", "-c", "core.hooksPath=/dev/null", "-c", "gc.auto=0", "-c", "protocol.file.allow=never"]


FORMAT = "--format=%x00%H %cs %cI %P"
TEMPLATE_FILES = 5   # this many files in one commit with the same added line count are a template batch
TEMPLATE_MIN = 20    # ... when each adds at least this many lines
GENERATED = re.compile(r"(?i)\bdo not edit\b|@generated\b|\bcode generated\b|\bauto-?generated\b")
HEAD_LINES = 10      # a generator's marker sits in a file's opening lines


def _path(field):
    """The new path from a numstat path, which writes a rename as `a/{old => new}/b` or `old => new`."""
    if " => " not in field:
        return field
    head, _, tail = field.partition("{")
    if tail:
        old_new, _, rest = tail.partition("}")
        return (head + old_new.split(" => ")[-1] + rest).replace("//", "/")
    return field.split(" => ")[-1]


def parse_log(text):
    """[(commit, day, path, added, deleted, blob)] from `git log --raw --numstat`, binary files and commits without
    parents skipped.

    Per commit, git prints a raw line for each changed file (with the new content's blob id) and then a numstat line
    for each, in the same order; the two are paired by position.
    """
    out = []
    for block in text.split("\0")[1:]:
        lines = block.splitlines()
        commit, day, _, *parents = lines[0].split()
        if not parents:
            continue
        raw = [l for l in lines[1:] if l.startswith(":")]
        stat = [l for l in lines[1:] if l and not l.startswith(":")]
        for r, n in zip(raw, stat):
            added, deleted, path = n.split("\t", 2)
            if added == "-":
                continue
            out.append((commit, day, _path(path), int(added), int(deleted), r.split()[3]))
    return out


def generated(git_dir, changes):
    """The code paths whose newest version opens with a code generator's marker."""
    newest = {}
    for _, _, path, _, _, blob in changes:   # git log lists newest first
        if classify(path):
            newest.setdefault(path, blob)
    paths = list(newest)
    out = subprocess.run(GIT + [f"--git-dir={git_dir}", "cat-file", "--batch"], env=GIT_ENV, check=True,
                         input="".join(newest[p] + "\n" for p in paths).encode(), capture_output=True).stdout
    found, at = set(), 0
    for path in paths:
        end = out.index(b"\n", at)
        header = out[at:end].split()
        if len(header) != 3:   # "<blob> missing": the file was deleted
            at = end + 1
            continue
        size = int(header[2])
        head = out[end + 1:end + 1 + min(size, 4000)].decode(errors="replace").splitlines()[:HEAD_LINES]
        if GENERATED.search("\n".join(head)):
            found.add(path)
        at = end + 1 + size + 1
    return found


def code_commit_times(text, changes):
    """The commit times, newest first, of the commits in `changes` that changed source or test files."""
    code = {c for c, _, p, a, d, _ in changes if (a or d) and classify(p)}
    heads = (block.split("\n", 1)[0].split() for block in text.split("\0")[1:])
    return [stamp for commit, _, stamp, *_ in heads if commit in code]


def day_of(text, start, days):
    """{commit: which of the window's whole days (0 is the first, counted in 24 hours from `start`) it landed on}."""
    heads = (block.split("\n", 1)[0].split() for block in text.split("\0")[1:])
    return {commit: min(max(int((parse(stamp) - start).total_seconds() // 86400), 0), days - 1)
            for commit, _, stamp, *_ in heads}


def tally(changes, days, made=frozenset(), days_of=None):
    """Per-day figures by kind of file, and how much code the four produced-code checks kept out. made: the paths a
    code generator wrote. days_of: {commit: day of the window}; without it, days are the commits' calendar dates.

    code_added_daily_median is the median of the days' code growth, days with none counting as zero: a steady week
    and a week carried by one large drop can share a mean, not a median."""
    gross, net_by = defaultdict(int), defaultdict(lambda: [0, 0])
    batches = Counter((c, a) for c, _, p, a, d, _ in changes if a >= TEMPLATE_MIN and d == 0 and classify(p))
    seen, kept_out = set(), Counter()
    for commit, day, path, added, deleted, blob in changes:
        kind = classify(path) or "other"
        gross[f"{kind}_added"] += added
        gross[f"{kind}_deleted"] += deleted
        if kind != "other" and path in made:
            kept_out["generated"] += added
            continue
        if kind != "other" and batches[(commit, added)] >= TEMPLATE_FILES and deleted == 0:
            kept_out["template"] += added
            continue
        if kind != "other" and blob in seen and added:
            kept_out["copy"] += added
            continue
        seen.add(blob)
        day = days_of.get(commit, day) if days_of else day
        net_by[(day, path, kind)][0] += added
        net_by[(day, path, kind)][1] += deleted
    net, daily = defaultdict(int), defaultdict(int)
    for (day, _, kind), (added, deleted) in net_by.items():
        if kind != "other":
            daily[day] += max(added - deleted, 0)
        net[f"{kind}_grew"] += max(added - deleted, 0)
        net[f"{kind}_shrank"] += max(deleted - added, 0)
    code_gross = gross["source_added"] + gross["test_added"]
    code = net["source_grew"] + net["test_grew"]
    per_day = lambda v: round(v / days)
    out = {f"gross_{k}_per_day": per_day(v) for k, v in gross.items()}
    out.update({f"net_{k}_per_day": per_day(v) for k, v in net.items()})
    out["code_added_per_day"] = per_day(code)
    out["code_added_daily_median"] = round(statistics.median(sorted(daily.values())[-days:] + [0] * (days - len(daily))))
    if days_of:
        out["code_added_by_day"] = [daily.get(i, 0) for i in range(days)]
    out["code_deleted_per_day"] = per_day(net["source_shrank"] + net["test_shrank"])
    out["all_added_per_day"] = per_day(sum(v for k, v in gross.items() if k.endswith("_added")))
    out["kept_out_per_day"] = dict(generated=per_day(kept_out["generated"]), template=per_day(kept_out["template"]),
                                   copy=per_day(kept_out["copy"]),
                                   rewrite=per_day(max(code_gross - sum(kept_out.values()) - code, 0)))
    out["files_changed"] = len({p for _, _, p, _, _, _ in changes})
    return out


def sweep(work, older_than=3600):
    """Remove clones left behind by an interrupted run."""
    for entry in work.glob("tmp*"):
        if time.time() - entry.stat().st_mtime > older_than:
            shutil.rmtree(entry, ignore_errors=True)


def clone_lines(repo, days, size_kb=None, lag=0):
    """Line figures for `days` ending `lag` days ago, with the clock of the commits that changed code, or {status}
    saying why there are none."""
    limit = CONFIG["lines"]["max_repo_mb"] * 1024
    if size_kb and size_kb > limit:
        return dict(status="too large", size_mb=round(size_kb / 1024))
    work = ROOT / ".cache" / "clones"
    work.mkdir(parents=True, exist_ok=True)
    sweep(work)
    timeout = CONFIG["lines"]["timeout_seconds"]
    with tempfile.TemporaryDirectory(dir=work) as tmp:
        dest = os.path.join(tmp, "repo.git")
        try:
            subprocess.run(GIT + ["clone", "-q", "--bare", "--no-tags", "--single-branch",
                                  f"--shallow-since={days + lag + 1} days ago", f"https://github.com/{repo}.git", dest],
                           env=GIT_ENV, cwd=tmp, check=True, capture_output=True, timeout=timeout)
            start, end = window(days, lag)
            log = subprocess.run(GIT + [f"--git-dir={dest}", "log", f"--since={iso(start)}", f"--until={iso(end)}",
                                        "--raw", "--numstat", "--no-abbrev", FORMAT, "-M"],
                                 env=GIT_ENV, cwd=tmp, check=True, capture_output=True, timeout=timeout)
            text = log.stdout.decode(errors="replace")
            changes = parse_log(text)
            made = generated(dest, changes)
            days_of = day_of(text, start, days)
        except subprocess.TimeoutExpired:
            return dict(status="timed out")
        except subprocess.CalledProcessError as exc:
            return dict(status="clone failed", error=exc.stderr.decode(errors="replace")[-200:])
    stamps = [dict(committedDate=t) for t in code_commit_times(text, changes)]
    return dict(status="ok", days=days, lag_days=lag, ends=iso(end), **tally(changes, days, made, days_of),
                clock=clock(stamps, days, True, end) if stamps else None)
