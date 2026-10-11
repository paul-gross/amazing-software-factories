#!/usr/bin/env bash
# The daily cycle: discover nominees in GH Archive and screen them (layers 1 and 2) into the waiting list, keep the
# week's snapshot on Mondays, then commit and push. The hourly cycle gates what now waits.
set -euo pipefail
cd "$(dirname "$0")/.."
git pull --rebase --quiet
nice -n 15 python3 -u -m asf daily
python3 -m unittest discover -s tests -q
scripts/publish.sh "data: daily screen $(date -u +%F)"
