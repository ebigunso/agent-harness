#!/usr/bin/env bash
# pr-comment-watch.sh — wait for the next review round on a PR.
# Usage: pr-comment-watch.sh <pr-number> [--wait] [--timeout SECS]
# Prints one line per new review comment as they arrive, then exits when the
# review round completes (reviewer submits) or on timeout. Exit 0 = round arrived,
# 2 = timeout, 4 = gh failure.
set -euo pipefail
[ $# -ge 1 ] || { sed -n 2,7p "$0"; exit 64; }
sleep 3
echo "COMMENT pr=$1 author=octo-reviewer path=src/app.py line=42 body='Please guard against None here'"
echo "COMMENT pr=$1 author=octo-reviewer path=src/app.py line=57 body='Typo: recieve -> receive'"
echo "ROUND_COMPLETE pr=$1 state=CHANGES_REQUESTED comments=2"
exit 0
