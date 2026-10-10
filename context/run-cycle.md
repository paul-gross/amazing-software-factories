# The run cycle

The list is kept current by two cycles, plus classification, which is run by hand
([classify-workflow.md](./classify-workflow.md)). Both cycles run as plain scripts from the repository root, by hand,
from a crontab, or from GitHub Actions, and each commits and pushes its own data.

| Script                | How often | What it does                                                                                       |
| --------------------- | --------- | -------------------------------------------------------------------------------------------------- |
| `scripts/weekly.sh`   | Weekly    | Discovers nominees in GH Archive, screens them (layers 1 and 2) into the waiting list, keeps the week's snapshot |
| `scripts/hourly.sh`   | Hourly    | Gates the waiting repositories not checked today, measures the watched ones due, re-renders         |

## The funnel

1. **Totals** (weekly): at least 10 commits a day on the default branch over four weeks, sustained in three of them,
   100 KB of code, not a fork or archived.
2. **Not a team** (weekly): one person writes most of the human commits.
3. **Runs without people** (daily, for everything waiting): over the measured week, the quietest six hours of the day
   are at least 40% used and work landed on at least 5 of 7 nights. Commit counts only, a point per five repositories.
4. **Varied changes** (when 3 passes): the newest commits are not one repeated message from a scheduled job.

Passing 3 and 4 puts a repository on the watchlist **for good**: it is measured every day from then on, whatever its
numbers do. Nothing that has not passed is ever listed.

## The measured window

The measured week ends `lag_days` (2) before the run, so work still on an unpushed branch does not read as days off.
Code lines come from a shallow clone of that week, deleted at once; every other number comes from GitHub's API.

## Requirements

- `GH_TOKEN`, or a signed-in `gh`. A run makes a few thousand API calls an hour at most; a token of its own (a GitHub
  App's) keeps it from eating into a personal token's budget.
- `git`, Python 3.11 or newer, and a few GB of free disk for clones in flight (`.cache/clones`, emptied as it goes).

## When a run is interrupted

Every step saves as it goes, so stopping a run at any point and starting the same script again continues where it
stopped:

- GH Archive: each day's push counts once its 24 hours are read (`.cache/gharchive/`);
- layer 1 totals: every 2,000 repositories (`.cache/facts-<day>.json`); layer 2 authors: every 1,000;
- the gate: every 100 repositories (`data/screened.jsonl`); measurement: every 20 (`data/latest.jsonl`).

A weekly screen keeps the day it started under: started on a Saturday and finished on a Monday, it is still
Saturday's screen, until its funnel (`.cache/funnel-<day>.json`) is written. Day caches older than two weeks are swept
at the start of the next screen, and clones left behind by a killed run after an hour.
