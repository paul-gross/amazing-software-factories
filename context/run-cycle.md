# The run cycle

The list is kept current by two cycles, plus classification, which is run by hand
([classify-workflow.md](./classify-workflow.md)). Both cycles run as plain scripts from the repository root, by hand,
from a crontab, or from GitHub Actions (`.github/workflows/hourly.yml` and `daily.yml`, one at a time), and each
commits and pushes its own data through `scripts/publish.sh`, which rebases onto anything pushed meanwhile.

| Script                | How often | What it does                                                                                       |
| --------------------- | --------- | -------------------------------------------------------------------------------------------------- |
| `scripts/daily.sh`    | Daily, 06:23 UTC | Discovers nominees in GH Archive, screens them (layers 1 and 2) into the waiting list, keeps the week's snapshot on Mondays |
| `scripts/hourly.sh`   | Hourly at :23, but not in the 06 UTC hour | Gates the waiting repositories not checked today, checks the dormant ones, measures the classified ones whose hour has come, re-renders |

## The funnel

1. **Totals** (daily, for the new nominees and the stale): at least 10 commits a day on the default branch over four
   weeks, sustained in three of them, 100 KB of code, not a fork or archived. A nominee's totals are read the day it
   is first nominated, then again one day in every `reread_days` (7), picked by a hash of its name, and kept in
   `.cache/totals.json` between runs, so each day reads the new nominees and a seventh of the rest. Reading stops
   after `[screen] minutes` (30), new nominees first, then the stalest; the rest is read the next day, and a nominee
   with nothing read yet keeps its status. Layer 2 gets the same budget after it.

   In Actions, `.cache/` is carried between runs in the Actions cache. When none is restored (the first run, or after
   GitHub evicts it once unused for a week), `daily.yml` seeds totals and author samples from the asset
   `cache-seed.tar.gz` on the release `cache-seed`, so the first run reads what is due rather than every nominee.
2. **Not a team** (daily, from author samples kept for 28 days): one person writes most of the human commits.
3. **Runs without people** (daily, for everything waiting): over the measured week, the quietest six hours of the day
   are at least 40% used and work landed on at least 5 of 7 nights. Commit counts only, a point per five repositories.
4. **Varied changes** (when 3 passes): the newest commits are not one repeated message from a scheduled job.

Passing 3 and 4 puts a repository on the watchlist **for good**. Nothing that has not passed is ever listed.

## After the gate

1. **Classified** ([classify-workflow.md](./classify-workflow.md)), by hand: an assembly line, built by one,
   agent-assisted, or not software. Nothing is measured or listed before this.
2. **Measured once a day**, if it is an assembly line, whatever its numbers do. Each repository has a
   fixed UTC hour (a hash of its name, modulo 24); a run measures those whose hour has come and that were not measured
   today, so a missed hour is caught up by the next run.
3. **Dormant** when a measurement sees no commits in the whole four-week window: not measured, not listed, history
   kept. Each run counts a dormant repository's commits per day over the last week, once a day; work on 3 of 7 days
   makes it active again.

A waiting repository GitHub has nothing for (deleted, private) counts as checked for the day, and stops waiting after
seven misses.

## The API budget

Every answer from GitHub reports the hour's remaining budget. When it falls to the reserve in `[github]` of
config.toml (1,000 GraphQL points by default), the run waits for the reset instead of spending the rest, so a shared
token is never run dry and a run never spins on rate-limit errors.

## The measured window

The measured week ends `lag_days` (2) before the run, so work still on an unpushed branch does not read as days off.
Code lines come from a shallow clone of that week, deleted at once; every other number comes from GitHub's API.

## Requirements

- GitHub API access, one of:
  - the bot: `ASF_APP_ID` and `ASF_APP_PRIVATE_KEY` (the App's PEM key, as text). The code mints the App's
    installation token with `openssl` and mints a new one before each hour runs out, so the API budget is the bot's
    own. The workflows pass these from the repository's secrets of the same names.
  - `GH_TOKEN`, or a signed-in `gh`: a personal token, whose budget is shared with everything else using it.
- `git`, `openssl`, Python 3.11 or newer, and a few GB of free disk for clones in flight (`.cache/clones`, emptied as
  it goes).
- `git`, Python 3.11 or newer, and a few GB of free disk for clones in flight (`.cache/clones`, emptied as it goes).

## When a run is interrupted

Every step saves as it goes, so stopping a run at any point and starting the same script again continues where it
stopped:

- GH Archive: each day's push counts once its 24 hours are read (`.cache/gharchive/`);
- layer 1 totals: every 2,000 repositories (`.cache/totals.json`); layer 2 authors: every 1,000;
- the gate: every 100 repositories (`data/screened.jsonl`); measurement: every 20 (`data/latest.jsonl`).

A screen keeps the day it started under: started on a Saturday and finished on a Monday, it is still Saturday's
screen, until its funnel (`.cache/funnel-<day>.json`) is written. Day caches older than two weeks are swept
at the start of the next screen, and clones left behind by a killed run after an hour.
