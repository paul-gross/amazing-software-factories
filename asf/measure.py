"""Measure one repository from GitHub's APIs. Nothing is cloned, checked out or run.

Every number lands in the snapshot raw; tiers and judgments are computed later from these facts.
"""
import json
import re
import statistics
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone

from . import CONFIG
from .gh import GhError, batched, graphql, rest

BOT = re.compile(r"(\[bot\]|-bot|bot)$", re.I)


def since(days):
    return (datetime.now(timezone.utc) - timedelta(days=days)).replace(microsecond=0)


def window(days, lag=0):
    """(start, end) of `days` ending `lag` days ago."""
    end = since(lag)
    return end - timedelta(days=days), end


def iso(dt):
    return dt.isoformat().replace("+00:00", "Z")


def parse(stamp):
    return datetime.fromisoformat(stamp.replace("Z", "+00:00"))


def _split(repo):
    owner, name = repo.split("/", 1)
    return owner, name


# --- the cheap passes over many nominees -----------------------------------------------------------------------

def _aliased(chunks, build, parse, workers):
    """Run one aliased GraphQL query per chunk, a few at a time, and merge the parsed results."""
    def run(chunk):
        try:
            data = graphql("query { " + " ".join(build(i, repo) for i, repo in enumerate(chunk)) + " }")
        except GhError as exc:
            if len(chunk) == 1:
                print(f"graphql {chunk[0]}: {exc}")
                return {}
            # One heavy repository can time a whole batch out; retry its members alone so only that one is lost.
            print(f"graphql batch of {len(chunk)} failed, retrying one by one: {exc}")
            out = {}
            for repo in chunk:
                out.update(run([repo]))
            return out
        return {repo: parse(data.get(f"r{i}")) for i, repo in enumerate(chunk) if data.get(f"r{i}")}

    out = {}
    with ThreadPoolExecutor(workers) as pool:
        for n, part in enumerate(pool.map(run, chunks), 1):
            out.update(part)
            if n % 200 == 0:
                print(f"graphql batches: {n} of {len(chunks)}")
    return out


def _repo(i, repo, body):
    owner, name = _split(repo)
    return f"r{i}: repository(owner: {json.dumps(owner)}, name: {json.dumps(name)}) {{ {body} }}"


def facts(repos, days, workers=2, size=40):
    """{repo: {canonical, created, fork, archived, stars, code_bytes, size_kb, merged_all, commits, total_commits,
    weeks}}, forty per query.

    One point per query: totals only, no nodes. `weeks` holds the commit count of each of the last four weeks, newest
    first, so a one-week burst can be told from sustained work before anything expensive runs.
    """
    now = datetime.now(timezone.utc).replace(microsecond=0)
    edges = [iso(now - timedelta(days=7 * i)) for i in range(5)]
    weeks = " ".join(f'w{i}: history(since: "{edges[i + 1]}", until: "{edges[i]}") {{ totalCount }}' for i in range(4))
    body = ("nameWithOwner createdAt isFork isArchived stargazerCount diskUsage languages { totalSize } "
            "pullRequests(states: MERGED) { totalCount } "
            f'defaultBranchRef {{ target {{ ... on Commit {{ history(since: "{iso(since(days))}") {{ totalCount }} '
            f'total: history {{ totalCount }} {weeks} }} }} }}')

    def parse(r):
        target = (r.get("defaultBranchRef") or {}).get("target") or {}
        return dict(canonical=r["nameWithOwner"], created=r["createdAt"], fork=r["isFork"], archived=r["isArchived"], stars=r["stargazerCount"],
                    code_bytes=(r.get("languages") or {}).get("totalSize") or 0, size_kb=r.get("diskUsage"),
                    merged_all=r["pullRequests"]["totalCount"],
                    commits=(target.get("history") or {}).get("totalCount", 0),
                    total_commits=(target.get("total") or {}).get("totalCount", 0),
                    weeks=[(target.get(f"w{i}") or {}).get("totalCount", 0) for i in range(4)])

    return _aliased(list(batched(repos, size)), lambda i, r: _repo(i, r, body), parse, workers)


def clock_slots(repos, lag=0, days=7, workers=2, size=5):
    """{repo: commits on the default branch in each two-hour slot of `days` ending `lag` days ago}, oldest slot first.

    Counts only, no commits: one point per query however busy a repository is, so the whole screen can be checked
    every day. Slots start on even UTC hours, so they line up with the hours of the day the clock reads.
    """
    end = since(lag).replace(minute=0, second=0)
    end -= timedelta(hours=end.hour % 2)
    edges = [iso(end - timedelta(hours=2 * i)) for i in range(days * 12, -1, -1)]
    body = ("defaultBranchRef { target { ... on Commit { " + " ".join(
        f's{i}: history(since: "{edges[i]}", until: "{edges[i + 1]}") {{ totalCount }}' for i in range(days * 12))
        + " } } }")

    def parse(r):
        target = (r.get("defaultBranchRef") or {}).get("target") or {}
        return dict(end=iso(end), slots=[(target.get(f"s{i}") or {}).get("totalCount", 0) for i in range(days * 12)])

    return _aliased(list(batched(repos, size)), lambda i, r: _repo(i, r, body), parse, workers)


def slot_clock(slots, end, days=7):
    """The clock of a repository from its two-hour slot counts, as `clock` reads it from commits."""
    end = parse(end)
    stamps = [end - timedelta(hours=2 * (len(slots) - i) - 1) for i, n in enumerate(slots) for _ in range(n)]
    return clock([dict(committedDate=iso(s)) for s in sorted(stamps, reverse=True)], days, True, end)


def created(repos, workers=2):
    """{repo: creation timestamp}, forty repositories per query."""
    return _aliased(list(batched(repos, 40)), lambda i, r: _repo(i, r, "createdAt"), lambda r: r["createdAt"], workers)


def authors(repos, days, sample=20, workers=2):
    """{repo: {commits, lead_human_share, machine_share}} from the authors of the newest `sample` commits, ten
    repositories per query. No line counts: those make GitHub diff every commit, and a sample cannot estimate them."""
    body = (f'defaultBranchRef {{ target {{ ... on Commit {{ history(first: {sample}, since: "{iso(since(days))}") {{ '
            "totalCount nodes { parents { totalCount } author { name user { login } } } } } } }")

    def parse(r):
        h = (((r.get("defaultBranchRef") or {}).get("target") or {}).get("history")) or {}
        p = people(tally(h.get("nodes") or [], h.get("totalCount", 0), False))
        return dict(commits=h.get("totalCount", 0), lead_human_share=p["lead_human_share"],
                    machine_share=p["bot_commit_share"])

    return _aliased(list(batched(repos, 10)), lambda i, r: _repo(i, r, body), parse, workers)


VARYING = re.compile(r"\b[0-9a-f]{7,40}\b|\d+|\b(mon|tue|wed|thu|fri|sat|sun|jan|feb|mar|apr|may|jun|jul|aug|sep|"
                     r"oct|nov|dec)[a-z]*\b|\b(utc|gmt|am|pm)\b", re.I)


def template(headline):
    """A commit message with its counters, dates, times and hashes blanked, so a scheduled job's messages collapse."""
    return " ".join(VARYING.sub(" ", headline.lower()).split())


def variety(headlines):
    """Distinct message templates per message: near 1 when every change is different, near 0 for a scheduled job."""
    return round(len({template(h) for h in headlines}) / len(headlines), 3) if headlines else None


def recent(repos, days, sample=100, workers=2):
    """{repo: {commits, variety, lead_human_share, machine_share, sampled}} from the newest `sample` commits of the
    last `days`, ten repositories per query. Messages and authors only: no line counts, which are the slow part."""
    body = (f'defaultBranchRef {{ target {{ ... on Commit {{ history(first: {sample}, since: "{iso(since(days))}") {{ '
            "totalCount nodes { messageHeadline parents { totalCount } author { name user { login } } } } } } }")

    def parse(r):
        h = (((r.get("defaultBranchRef") or {}).get("target") or {}).get("history")) or {}
        nodes = h.get("nodes") or []
        p = people(tally(nodes, h.get("totalCount", 0), False))
        single = [n["messageHeadline"] for n in nodes if n["parents"]["totalCount"] <= 1]
        return dict(commits=h.get("totalCount", 0), variety=variety(single), sampled=len(single),
                    lead_human_share=p["lead_human_share"], machine_share=p["bot_commit_share"])

    return _aliased(list(batched(repos, 10)), lambda i, r: _repo(i, r, body), parse, workers)


def merged_pr_counts(repos, days, workers=1, lag=0):
    """{repo: merged pull requests in the window}, through GraphQL search, ten per query."""
    start, end = window(days, lag)
    day = f"{iso(start)}..{iso(end)}" if lag else f">={start.date().isoformat()}"

    def run(chunk):
        parts = [f's{i}: search(query: {json.dumps(f"repo:{repo} is:pr is:merged merged:{day}")}, type: ISSUE, '
                 f'first: 0) {{ issueCount }}' for i, repo in enumerate(chunk)]
        try:
            data = graphql("query { " + " ".join(parts) + " }")
        except GhError as exc:
            print(f"merged_pr_counts: {exc}")
            return {}
        return {repo: data[f"s{i}"]["issueCount"] for i, repo in enumerate(chunk) if data.get(f"s{i}") is not None}

    out = {}
    # Search is the API most prone to secondary rate limits, so it never runs wider than asked.
    with ThreadPoolExecutor(workers) as pool:
        for part in pool.map(run, list(batched(repos, 10))):
            out.update(part)
    return out


# --- commits: lines, people, the clock --------------------------------------------------------------------------

COMMIT_FIELDS = "oid committedDate messageHeadline parents { totalCount } author { name user { login } }"
# Asking for each commit's line counts makes GitHub diff every commit, many times slower than the rest of the read.
LINE_FIELDS = " additions deletions"
HISTORY = """query($o: String!, $n: String!, $since: GitTimestamp!, $until: GitTimestamp, $after: String, $page: Int!) {
  repository(owner: $o, name: $n) { defaultBranchRef { target { ... on Commit {
    history(first: $page, since: $since, until: $until, after: $after) {
      totalCount pageInfo { hasNextPage endCursor } nodes { %s } } } } } } }"""


def history(repo, days, limit, with_prs=False, lines=True, lag=0):
    """The default branch's commits over the window, newest first, up to `limit`. Line counts and the pull request each
    commit came from are extra work for GitHub, so each is asked for only when wanted."""
    owner, name = _split(repo)
    query = HISTORY % (COMMIT_FIELDS + (LINE_FIELDS if lines else "")
                       + (" associatedPullRequests(first: 1) { totalCount }" if with_prs else ""))
    nodes, after, total, complete = [], None, 0, False
    start, end = window(days, lag)
    while len(nodes) < limit:
        # Line counts make GitHub diff every commit on the page; a full page of them can outlast its gateway timeout.
        data = graphql(query, o=owner, n=name, since=iso(start), until=iso(end) if lag else None,
                       after=after, page=25 if lines else 100)
        target = ((data["repository"] or {}).get("defaultBranchRef") or {}).get("target")
        if not target:
            complete = True
            break
        h = target["history"]
        total = h["totalCount"]
        nodes += h["nodes"]
        if not h["pageInfo"]["hasNextPage"]:
            complete = True
            break
        after = h["pageInfo"]["endCursor"]
    return nodes, total, complete


def author_key(node):
    """(GitHub account, is_human). Only a linked, non-bot GitHub account is a human. Bots, and identities no account
    claims — agents often commit as `agent-7@example.com` or `CI <ci@local>` — are machine work."""
    a = node.get("author") or {}
    login = (a.get("user") or {}).get("login")
    if login and not BOT.search(login):
        return login, True
    return login or a.get("name") or "?", False


def tally(nodes, total, complete, merged=None, lines=True):
    """Additive counts for a window, scaled from the sample to the window's total when the window was sampled.

    Tallies of consecutive weeks sum to the tally of the month, which is how the weekly measurement builds its
    four-week figures without reading the month again.
    """
    single = [n for n in nodes if n["parents"]["totalCount"] <= 1]
    scale = 1.0 if complete or not nodes else total / len(nodes)
    humans = Counter(k for k, human in map(author_key, single) if human)
    added = sum(n.get("additions", 0) for n in single)
    top3 = sum(sorted((n.get("additions", 0) for n in single), reverse=True)[:3])
    return dict(
        commits=total, merged_prs=merged, complete=complete,
        added=round(added * scale) if lines else None,
        deleted=round(sum(n.get("deletions", 0) for n in single) * scale) if lines else None,
        authored=round(len(single) * scale), humans={k: round(v * scale, 1) for k, v in humans.items()},
        # When three commits carry most of the added lines, the line rate is a few bulk drops, not a steady flow.
        top3_share=round(top3 / added, 2) if lines and added else None,
    )


def combine(tallies):
    """The tally of consecutive windows taken together."""
    humans = Counter()
    for t in tallies:
        humans.update(t["humans"])
    merged = [t["merged_prs"] for t in tallies]
    total = lambda key: None if any(t[key] is None for t in tallies) else sum(t[key] for t in tallies)
    return dict(commits=sum(t["commits"] for t in tallies), merged_prs=total("merged_prs"),
                complete=all(t["complete"] for t in tallies), added=total("added"), deleted=total("deleted"),
                authored=sum(t["authored"] for t in tallies), humans=dict(humans), top3_share=None)


def people(t):
    """Who wrote the non-merge commits: the lead human's share among humans, and how much was machine work."""
    humans = Counter(t["humans"])
    human_total = sum(humans.values())
    lead, lead_n = humans.most_common(1)[0] if humans else (None, 0)
    return dict(
        lead_human=lead,
        lead_human_share=round(lead_n / human_total, 3) if human_total else None,
        human_authors=len(humans),
        bot_commit_share=round(1 - human_total / t["authored"], 3) if t["authored"] else None,
    )


def rates(t, days):
    """Per-day figures from a tally."""
    return dict(
        commits_per_day=round(t["commits"] / days, 1),
        merged_prs_per_day=round(t["merged_prs"] / days, 1) if t["merged_prs"] is not None else None,
        added_per_day=round(t["added"] / days) if t["added"] is not None else None,
        deleted_per_day=round(t["deleted"] / days) if t["deleted"] is not None else None,
        net_per_day=round((t["added"] - t["deleted"]) / days) if t["added"] is not None else None,
        lines_estimated=not t["complete"], lines_top3_share=t["top3_share"], **people(t),
    )


def clock(nodes, days, complete=True, now=None):
    """How evenly commits land around the clock over the most recent days.

    quietest_6h_share is the fewest commits in any six consecutive UTC hours (three two-hour bins, wrapping past
    midnight), divided by all commits in the span: 0.25 is perfectly even, near 0 is a person who sleeps.
    night_utilization is the same measure against that even share: 1.0 is work landing round the clock, 0 a daily gap.
    nights_seen counts the times those quietest six hours came round whole inside the span, and nights_covered how many
    of them had any commit: whether work lands every night, not just on a few long ones.
    day_utilization does the same across the week: the fewest commits in any 24 hours in a row (twelve two-hour bins,
    not wrapping), against the share an even spread puts in a day. 1.0 is work landing every day; 0 is a day off.
    commits_by_day counts commits in each whole 24 hours from the span's start.
    complete: whether `nodes` holds every commit of the days. When the read stopped at its limit, the days are those
    the read reached, and a span under a day has no day_utilization. now: when the days end; without it they end at
    the newest commit.
    """
    if not nodes:
        return dict(quietest_6h_share=None, activity_commits=0, activity_span_days=0)
    stamps = sorted((parse(n["committedDate"]).astimezone(timezone.utc) for n in nodes), reverse=True)
    newest = stamps[0]
    oldest_allowed = newest - timedelta(days=days)
    stamps = [s for s in stamps if s >= oldest_allowed]
    span = (newest - min(stamps)).total_seconds() / 86400
    bins = [0] * 12
    for s in stamps:
        bins[s.hour // 2] += 1
    quiet_at = min(range(12), key=lambda i: sum(bins[(i + k) % 12] for k in range(3)))
    quiet = sum(bins[(quiet_at + k) % 12] for k in range(3)) / len(stamps)
    end = now or newest
    start = end - timedelta(days=days) if complete else min(stamps)
    reached = len(stamps) if complete else len(stamps) - 1   # an incomplete read's oldest commit opens the span
    slots = int((end - start).total_seconds() // 7200)
    day_utilization, daily = None, []
    if slots >= 12 and reached:
        week_bins = [0] * slots
        for s in stamps:
            if (s >= start) if complete else (s > start):
                week_bins[min(int((s - start).total_seconds() // 7200), slots - 1)] += 1
        quiet_day = min(sum(week_bins[i:i + 12]) for i in range(slots - 11)) / reached
        day_utilization = round(min(quiet_day * slots / 12, 1.0), 3)
        daily = [sum(week_bins[i:i + 12]) for i in range(0, slots - 11, 12)]
    night = start.replace(hour=quiet_at * 2, minute=0, second=0, microsecond=0)
    night += timedelta(days=1) if night < start else timedelta(0)
    seen = covered = 0
    while night + timedelta(hours=6) <= end:
        seen += 1
        covered += any(night <= s < night + timedelta(hours=6) for s in stamps)
        night += timedelta(days=1)
    return dict(quietest_6h_share=round(quiet, 3), night_utilization=round(quiet * 4, 3),
                day_utilization=day_utilization, nights_seen=seen, nights_covered=covered,
                quietest_6h_starts_utc=f"{quiet_at * 2:02d}:00", commits_by_day=daily, activity_commits=len(stamps),
                activity_span_days=round(span, 1),
                active_days=len({s.date() for s in stamps if (newest.date() - s.date()).days < days}),
                commits_by_2h_utc=bins)


REWORK = re.compile(r"recover|stranded|stuck|deadlock|orphan|wedge|limbo|flak|stabiliz|quarantin|revert|regression|"
                    r"hotfix|broke|repair|restore|unbreak|again", re.I)
WIP = re.compile(r"\bwip\b|checkpoint|^update\b|^updates?$|^changes?$|^fix$|^misc|^save|auto-?commit|^\.$", re.I)


def habits(nodes):
    """Raw facts about how work lands. None of them is scored: fast iteration and repair look alike from here."""
    single = [n for n in nodes if n["parents"]["totalCount"] <= 1]
    if not single:
        return dict(direct_push_share=None, rework_share=None, wip_share=None)
    share = lambda pred: round(sum(1 for n in single if pred(n)) / len(single), 3)
    return dict(
        direct_push_share=share(lambda n: n["associatedPullRequests"]["totalCount"] == 0),
        rework_share=share(lambda n: REWORK.search(n["messageHeadline"])),
        wip_share=share(lambda n: WIP.search(n["messageHeadline"])),
    )


# --- pull requests ----------------------------------------------------------------------------------------------

PRS = """query($o: String!, $n: String!) { repository(owner: $o, name: $n) {
  pullRequests(states: MERGED, first: 100, orderBy: {field: UPDATED_AT, direction: DESC}) {
    nodes { createdAt mergedAt author { login __typename } mergedBy { login __typename } } } } }"""


def is_bot_actor(actor):
    return bool(actor) and (actor.get("__typename") == "Bot" or bool(BOT.search(actor.get("login", ""))))


def pull_requests(repo, days, lag=0):
    owner, name = _split(repo)
    data = graphql(PRS, o=owner, n=name)
    start, end = window(days, lag)
    nodes = [p for p in data["repository"]["pullRequests"]["nodes"]
             if p["mergedAt"] and start <= parse(p["mergedAt"]) <= end]
    if not nodes:
        return dict(pr_sample=0, bot_authored_pr_share=None, bot_merged_pr_share=None, median_minutes_to_merge=None)
    share = lambda pred: round(sum(1 for p in nodes if pred(p)) / len(nodes), 3)
    minutes = [(parse(p["mergedAt"]) - parse(p["createdAt"])).total_seconds() / 60 for p in nodes]
    return dict(pr_sample=len(nodes), bot_authored_pr_share=share(lambda p: is_bot_actor(p["author"])),
                bot_merged_pr_share=share(lambda p: is_bot_actor(p["mergedBy"])),
                median_minutes_to_merge=round(statistics.median(minutes), 1), peak_open_prs=peak_open(nodes))


def peak_open(prs):
    """The most of these pull requests open at the same moment: several agents at work at once show as overlap."""
    events = sorted([(parse(p["createdAt"]), 1) for p in prs] + [(parse(p["mergedAt"]), -1) for p in prs])
    peak = now = 0
    for _, step in events:
        now += step
        peak = max(peak, now)
    return peak


# --- continuous integration on the default branch ---------------------------------------------------------------

def ci(repo, branch):
    """Conclusions of the last hundred push-triggered workflow runs on the default branch.

    green_share counts only runs that finished with a verdict; cancelled and skipped runs are reported, not judged.
    """
    try:
        runs = rest(f"repos/{repo}/actions/runs?branch={branch}&event=push&per_page=100")["workflow_runs"]
    except GhError:
        runs = []
    c = Counter(r.get("conclusion") or "in_progress" for r in runs)
    judged = c["success"] + c["failure"] + c["timed_out"] + c["startup_failure"]
    return dict(ci_runs=len(runs), ci_conclusions=dict(c), green_share=round(c["success"] / judged, 3) if judged else None)


# --- the tree: size, centralization, tests ----------------------------------------------------------------------

SRC = re.compile(r"\.(ts|tsx|js|jsx|mjs|cjs|py|rs|go|java|kt|swift|rb|ex|exs|ml|mli|cs|cpp|cc|c|h|hpp|scala|clj|cljs|"
                 r"cljc|dart|php|lua|zig|hs|elm|vue|svelte|lean|agda|raku|rakumod|sql|css|scss|sass|less|html|htm|sh|bash|zsh)$")
TEST = re.compile(r"(^|/)(tests?|__tests__|spec|specs|e2e|testing)/|[._-](test|spec)\.[a-z]+$|(^|/)test_[^/]+\.py$|"
                  r"_test\.(go|rs|py)$|Tests?\.(swift|kt|java|cs)$")
GEN = re.compile(r"(^|/)(node_modules|vendor|third_party|dist|build|out|target|\.next|coverage|generated|gen|"
                 r"fixtures?|vectors|migrations?)/|\.gen\.|\.min\.js$|_pb2\.py$|\.pb\.go$|\.d\.ts$")


def classify(path):
    """'source', 'test' or None for a tree path; generated, vendored and fixture code is neither."""
    if not SRC.search(path) or GEN.search(path):
        return None
    return "test" if TEST.search(path) else "source"


def structure(files):
    """files: [(path, bytes)]. Size, centralization and test weight of the source."""
    src = sorted(((p, s) for p, s in files if classify(p) == "source"), key=lambda x: -x[1])
    tst = [s for p, s in files if classify(p) == "test"]
    src_bytes = sum(s for _, s in src)
    root = {p for p, _ in files if "/" not in p}
    return dict(
        source_kb=src_bytes // 1024, source_files=len(src), test_kb=sum(tst) // 1024,
        test_ratio=round(sum(tst) / src_bytes, 2) if src_bytes else None,
        largest_file=src[0][0] if src else None,
        largest_file_kb=src[0][1] // 1024 if src else None,
        tenth_largest_file_kb=src[9][1] // 1024 if len(src) >= 10 else None,
        largest_file_share=round(src[0][1] / src_bytes, 3) if src_bytes else None,
        agent_instructions=sorted(root & {"AGENTS.md", "CLAUDE.md", "GEMINI.md", ".cursorrules"}),
    )


CONFIG_FILE = re.compile(r"(^|/)(tsconfig(\.base)?\.json|pyproject\.toml|Cargo\.toml|setup\.cfg|mypy\.ini|"
                         r"pyrightconfig\.json|\.eslintrc[^/]*|eslint\.config\.[mc]?[jt]s|biome\.jsonc?|clippy\.toml|"
                         r"deny\.toml|\.dependency-cruiser\.[cm]?js|sgconfig\.yml|\.importlinter|go\.mod|"
                         r"\.golangci\.ya?ml|package\.json)$")
WORKFLOW = re.compile(r"^\.github/workflows/[^/]+\.ya?ml$")


def config_paths(files):
    workflows = [p for p, _ in files if WORKFLOW.match(p)][:20]
    configs = [p for p, _ in files if CONFIG_FILE.search(p) and p.count("/") <= 2 and "node_modules" not in p][:25]
    return workflows + configs


def blobs(repo, oid, paths):
    """{path: text} for small files at a commit, twenty per query."""
    owner, name = _split(repo)
    out = {}
    for chunk in batched(paths, 20):
        parts = [f'f{i}: object(expression: {json.dumps(f"{oid}:{p}")}) {{ ... on Blob {{ text }} }}'
                 for i, p in enumerate(chunk)]
        q = (f"query {{ repository(owner: {json.dumps(owner)}, name: {json.dumps(name)}) {{ "
             + " ".join(parts) + " } }")
        try:
            data = graphql(q)["repository"]
        except GhError as exc:
            print(f"blobs {repo}: {exc}")
            continue
        for i, p in enumerate(chunk):
            text = ((data or {}).get(f"f{i}") or {}).get("text")
            if text:
                out[p] = text[:20000]
    return out


BOUNDARY_TOOLS = {
    "dependency-cruiser": r"dependency-cruiser", "eslint-boundaries": r"eslint-plugin-boundaries|import/no-restricted-paths|no-restricted-imports",
    "import-linter": r"import-linter|\[importlinter", "ast-grep": r"ast-grep|sgconfig", "cargo-deny": r"\[bans\]|cargo-deny",
    "clippy-deny": r"-D warnings|deny\(warnings|\[lints", "archunit": r"archunit", "knip/madge": r"\bknip\b|\bmadge\b",
}
TESTS = (r"\b(pytest|vitest|jest|cargo (nextest|test)|go test|npm (run )?test|pnpm (run )?test|yarn test|bun test|"
         r"swift test|gradle\w* test|dotnet test|mix test|dune (test|runtest)|lake (build|test)|make test|just test|"
         r"\btest\b:)")
LINT = r"(eslint|ruff|clippy|golangci|biome|swiftlint|flake8|pylint|rumdl|lint)"
TYPECHECK = r"(tsc|typecheck|type-check|mypy|pyright|cargo check|clippy|svelte-check|vue-tsc)"


def gates(texts):
    """What the repository is configured to refuse. 'Configured' is read from files; enforcement is not proven."""
    workflows = {p: t for p, t in texts.items() if WORKFLOW.match(p)}
    pr = " ".join(t for t in workflows.values() if re.search(r"pull_request|merge_group", t))
    everything = " ".join(texts.values())
    found = lambda pattern, text: bool(re.search(pattern, text, re.I))
    return dict(
        workflows=len(workflows), pr_workflows=sum(1 for t in workflows.values() if re.search(r"pull_request|merge_group", t)),
        pr_runs_tests=found(TESTS, pr), pr_runs_lint=found(LINT, pr), pr_runs_typecheck=found(TYPECHECK, pr),
        merge_queue=found(r"merge_group", pr),
        strict_typing=found(r'"strict"\s*:\s*true', everything)
        or found(r'(strict\s*=\s*true|typeCheckingMode\s*=\s*"strict"|disallow_untyped_defs)', everything),
        boundary_tools=sorted(k for k, p in BOUNDARY_TOOLS.items() if re.search(p, everything, re.I)),
    )


# --- one repository, end to end ---------------------------------------------------------------------------------

META = """query($o: String!, $n: String!) { repository(owner: $o, name: $n) {
  nameWithOwner description isFork isArchived stargazerCount forkCount createdAt pushedAt diskUsage
  primaryLanguage { name } languages(first: 6, orderBy: {field: SIZE, direction: DESC}) { totalSize edges { size node { name } } }
  defaultBranchRef { name target { oid } } } }"""


def meta(repo):
    owner, name = _split(repo)
    r = graphql(META, o=owner, n=name)["repository"]
    if not r:
        raise GhError(f"{repo}: not found")
    langs = r["languages"]
    total = langs["totalSize"] or 1
    return dict(
        canonical=r["nameWithOwner"], description=(r["description"] or "")[:200], fork=r["isFork"],
        archived=r["isArchived"], stars=r["stargazerCount"], forks=r["forkCount"], created=r["createdAt"][:10],
        pushed=r["pushedAt"][:10], language=(r["primaryLanguage"] or {}).get("name"),
        languages={e["node"]["name"]: round(e["size"] / total, 2) for e in langs["edges"]},
        branch=(r["defaultBranchRef"] or {}).get("name"), head=((r["defaultBranchRef"] or {}).get("target") or {}).get("oid"),
        size_kb=r["diskUsage"],
    )


def volume(repo, days, limit, with_prs=False, lines=True, lag=0):
    """Read a window exactly: commits, merged pull requests, the people behind them and, if asked, lines, as a tally."""
    nodes, total, complete = history(repo, days, limit, with_prs, lines, lag)
    merged = merged_pr_counts([repo], days, lag=lag).get(repo)
    return nodes, tally(nodes, total, complete, merged, lines)


def measure(repo, prior_weeks=(), baseline=None):
    """One weekly measurement: the last seven days read exactly, and four-week figures.

    The four weeks are the sum of this week and the three before it when those snapshots exist; otherwise the screen's
    four-week read from the past week, or a fresh read.
    """
    cfg = CONFIG["window"]
    days, week, lag = cfg["days"], cfg["week_days"], cfg["lag_days"]
    m = meta(repo)
    read_at = window(0, lag)[1]
    # Commits are read without line counts, which make GitHub diff every commit; the week's lines come from a
    # short-lived clone instead, split by kind of file.
    read_lines = False
    nodes, this_week = volume(repo, week, cfg["max_commits"], with_prs=True, lines=read_lines, lag=lag)
    from .lines import clone_lines  # lines classifies paths with this module's rules, so it imports it in turn
    code = clone_lines(repo, week, m.get("size_kb"), lag)
    if len(prior_weeks) == days // week - 1:
        month, source = combine([this_week, *prior_weeks]), "weekly snapshots"
    elif baseline:
        month, source = baseline, "screen read"
    else:
        # Four weeks of line counts would cost four times the week's slow read; the week stands in for them.
        month, source = volume(repo, days, cfg["max_commits"], lines=False, lag=lag)[1], "read"
    row = dict(repo=m["canonical"], measured=datetime.now(timezone.utc).date().isoformat(), window_days=days,
               meta={k: v for k, v in m.items() if k not in ("canonical", "head")},
               volume=dict(rates(month, days), source=source), week=rates(this_week, week), week_tally=this_week,
               code_lines=code,
               clock=clock(nodes, week, this_week.get("complete", True), read_at), habits=habits(nodes), prs=pull_requests(repo, week, lag),
               ci=ci(repo, m["branch"]) if m["branch"] else {})
    if m["head"]:
        tree = rest(f"repos/{repo}/git/trees/{m['head']}?recursive=1")
        files = [(t["path"], t.get("size", 0)) for t in tree["tree"] if t["type"] == "blob"]
        row["structure"] = dict(structure(files), tree_truncated=tree.get("truncated", False))
        row["gates"] = gates(blobs(repo, m["head"], config_paths(files)))
    return row
