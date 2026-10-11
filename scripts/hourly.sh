#!/usr/bin/env bash
# One hourly cycle: the gate for waiting repositories not checked today, daily measurement of the watched ones that
# are due, a re-render, and a commit and push of the data. Needs the bot's credentials, GH_TOKEN, or a signed-in `gh` for GitHub's API.
set -euo pipefail
cd "$(dirname "$0")/.."
git pull --rebase --quiet
nice -n 15 python3 -u -m asf hourly
python3 -m unittest discover -s tests -q
scripts/publish.sh "data: hourly run $(date -u +'%F %H:00')"
