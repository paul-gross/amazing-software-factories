#!/usr/bin/env bash
# The weekly cycle: discover nominees in GH Archive and screen them (layers 1 and 2) into the waiting list, keep the
# week's snapshot, then commit and push. The hourly cycle gates what now waits.
set -euo pipefail
cd "$(dirname "$0")/.."
git pull --rebase --quiet
nice -n 15 python3 -u -m asf weekly
python3 -m unittest discover -s tests -q
git add data docs README.md reports
if git diff --cached --quiet; then
  echo "weekly: nothing new to commit"
  exit 0
fi
git commit --quiet -m "data: weekly screen $(date -u +%F)"
git push --quiet
echo "weekly: committed and pushed"
