#!/usr/bin/env bash
# One hourly cycle: the gate for waiting repositories not checked today, daily measurement of the watched ones that
# are due, a re-render, and a commit and push of the data. Needs GH_TOKEN (or a signed-in `gh`) for GitHub's API.
set -euo pipefail
cd "$(dirname "$0")/.."
git pull --rebase --quiet
nice -n 15 python3 -u -m asf hourly
python3 -m unittest discover -s tests -q
git add data docs README.md reports
if git diff --cached --quiet; then
  echo "hourly: nothing new to commit"
  exit 0
fi
git commit --quiet -m "data: hourly run $(date -u +'%F %H:00')"
git push --quiet
echo "hourly: committed and pushed"
