#!/usr/bin/env bash
# Commit what a run changed and push it, rebasing onto anything pushed meanwhile (a classification run from a laptop,
# say). Data files keep both sides' rows; the generated README, site and report are rendered again on top.
set -euo pipefail
cd "$(dirname "$0")/.."
message="$1"
git add data docs README.md reports
if git diff --cached --quiet; then
  echo "publish: nothing new to commit"
  exit 0
fi
git commit --quiet -m "$message"
for attempt in 1 2 3; do
  if git push --quiet; then
    echo "publish: pushed"
    exit 0
  fi
  git pull --rebase --quiet -X theirs
  python3 -m asf render
  git add docs README.md reports
  git diff --cached --quiet || git commit --quiet --amend --no-edit
done
echo "publish: could not push after three attempts" >&2
exit 1
