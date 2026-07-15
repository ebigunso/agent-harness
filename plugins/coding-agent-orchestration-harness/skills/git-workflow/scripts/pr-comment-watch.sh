#!/usr/bin/env bash
# Poll GitHub pull requests for comment or review-count changes.
#
# Usage:
#   pr-comment-watch.sh [-i SECONDS] OWNER/REPO:PR[:comments[:reviews]] ...
#   pr-comment-watch.sh --once OWNER/REPO:PR[:comments[:reviews]] ...
#   pr-comment-watch.sh --wait SECONDS [-i SECONDS] OWNER/REPO:PR[:comments[:reviews]] ...
#
# Hard-won implementation invariants (do not simplify these away):
#   - Every count uses `gh api --paginate` and a `wc -l` pipeline. Using a
#     single-page length pins the count once an endpoint crosses 30 items.
#   - Watch mode emits no heartbeat and exits on the first change. Every output
#     line can wake an agent, so silence must continue to mean "no activity".
#   - Posting replies can fire the watcher. After handling a review round,
#     restart or re-baseline it so self-induced activity is not mistaken for a
#     new reviewer round.
#   - A transient API failure is "no change" only in persistent watch mode.
set -u

INTERVAL=120
INTERVAL_SET=0
MODE=watch
MODE_SET=0
WAIT_DURATION=

usage() {
  printf '%s\n' \
    "usage: $0 [-i SECONDS] OWNER/REPO:PR[:comments[:reviews]] ..." \
    "       $0 --once OWNER/REPO:PR[:comments[:reviews]] ..." \
    "       $0 --wait SECONDS [-i SECONDS] OWNER/REPO:PR[:comments[:reviews]] ..." >&2
}

usage_error() {
  if [ $# -gt 0 ]; then
    printf 'error: %s\n' "$1" >&2
  fi
  usage
  exit 2
}

set_mode() {
  local requested=$1
  if [ "$MODE_SET" -eq 1 ]; then
    usage_error "choose exactly one of --once or --wait"
  fi
  MODE=$requested
  MODE_SET=1
}

while [ $# -gt 0 ]; do
  case "$1" in
    -i)
      [ $# -ge 2 ] || usage_error "-i requires a duration"
      [[ $2 =~ ^[1-9][0-9]*$ ]] || usage_error "-i duration must be a positive integer"
      INTERVAL=$2
      INTERVAL_SET=1
      shift 2
      ;;
    --once)
      set_mode once
      shift
      ;;
    --wait)
      [ $# -ge 2 ] || usage_error "--wait requires a duration"
      [[ $2 =~ ^(0|[1-9][0-9]*)$ ]] || usage_error "--wait duration must be a non-negative integer"
      set_mode wait
      WAIT_DURATION=$2
      shift 2
      ;;
    --)
      shift
      break
      ;;
    -*)
      usage_error "unknown option: $1"
      ;;
    *)
      break
      ;;
  esac
done

[ "$MODE" != once ] || [ "$INTERVAL_SET" -eq 0 ] || usage_error "-i is not used with --once"
[ $# -gt 0 ] || usage_error "at least one pull request spec is required"

declare -a REPOS PRS
declare -a HAS_SUPPLIED_BASE COMMENT_BASE_SET COMMENT_BASES
declare -a REVIEW_BASE_SET REVIEW_BASES CURRENT_COMMENTS CURRENT_REVIEWS

for spec in "$@"; do
  if [[ ! $spec =~ ^([^/:[:space:]]+)/([^/:[:space:]]+):([1-9][0-9]*)(:([0-9]+)(:([0-9]+))?)?$ ]]; then
    usage_error "malformed pull request spec: $spec"
  fi

  REPOS+=("${BASH_REMATCH[1]}/${BASH_REMATCH[2]}")
  PRS+=("${BASH_REMATCH[3]}")
  if [ -n "${BASH_REMATCH[4]:-}" ]; then
    HAS_SUPPLIED_BASE+=(1)
    COMMENT_BASE_SET+=(1)
    COMMENT_BASES+=("${BASH_REMATCH[5]}")
  else
    HAS_SUPPLIED_BASE+=(0)
    COMMENT_BASE_SET+=(0)
    COMMENT_BASES+=("")
  fi
  if [ -n "${BASH_REMATCH[6]:-}" ]; then
    REVIEW_BASE_SET+=(1)
    REVIEW_BASES+=("${BASH_REMATCH[7]}")
  else
    REVIEW_BASE_SET+=(0)
    REVIEW_BASES+=("")
  fi
done

count_endpoint() {
  local repo=$1
  local pr=$2
  local endpoint=$3
  local output count

  # Watch mode stays silent on transient failures; probe modes (--once/--wait)
  # surface the underlying gh/API error on stderr so exit 4 is diagnosable
  # (auth, rate limit, 404) without breaking the no-heartbeat contract.
  if [ "$MODE" = watch ]; then
    output=$(gh api "repos/$repo/pulls/$pr/$endpoint" --paginate --jq '.[].id' 2>/dev/null) || return 1
  else
    output=$(gh api "repos/$repo/pulls/$pr/$endpoint" --paginate --jq '.[].id') || return 1
  fi
  if [ -z "$output" ]; then
    printf '0\n'
    return 0
  fi

  count=$(printf '%s\n' "$output" | wc -l | tr -d '[:space:]')
  [ -n "$count" ] || return 1
  printf '%s\n' "$count"
}

fetch_counts() {
  local repo=$1
  local pr=$2
  local comments reviews

  comments=$(count_endpoint "$repo" "$pr" comments) || return 1
  reviews=$(count_endpoint "$repo" "$pr" reviews) || return 1
  printf '%s %s\n' "$comments" "$reviews"
}

load_current_counts() {
  local index=$1
  local counts

  counts=$(fetch_counts "${REPOS[$index]}" "${PRS[$index]}") || return 1
  CURRENT_COMMENTS[$index]=${counts%% *}
  CURRENT_REVIEWS[$index]=${counts##* }
}

fill_missing_baselines() {
  local index=$1

  if [ "${COMMENT_BASE_SET[$index]}" -eq 0 ]; then
    COMMENT_BASES[$index]=${CURRENT_COMMENTS[$index]}
    COMMENT_BASE_SET[$index]=1
  fi
  if [ "${REVIEW_BASE_SET[$index]}" -eq 0 ]; then
    REVIEW_BASES[$index]=${CURRENT_REVIEWS[$index]}
    REVIEW_BASE_SET[$index]=1
  fi
}

counts_changed() {
  local index=$1

  [ "${CURRENT_COMMENTS[$index]}" -ne "${COMMENT_BASES[$index]}" ] ||
    [ "${CURRENT_REVIEWS[$index]}" -ne "${REVIEW_BASES[$index]}" ]
}

print_new_activity() {
  local index=$1

  printf 'NEW_ACTIVITY repo=%s pr=%s comments=%s (was %s) reviews=%s (was %s)\n' \
    "${REPOS[$index]}" "${PRS[$index]}" \
    "${CURRENT_COMMENTS[$index]}" "${COMMENT_BASES[$index]}" \
    "${CURRENT_REVIEWS[$index]}" "${REVIEW_BASES[$index]}"
}

print_current_line() {
  local label=$1
  local index=$2

  printf '%s repo=%s pr=%s comments=%s reviews=%s\n' \
    "$label" "${REPOS[$index]}" "${PRS[$index]}" \
    "${CURRENT_COMMENTS[$index]}" "${CURRENT_REVIEWS[$index]}"
}

api_failure() {
  local index=$1

  printf 'error: could not fetch counts for repo=%s pr=%s\n' \
    "${REPOS[$index]}" "${PRS[$index]}" >&2
  exit 4
}

run_watch() {
  local index

  # Establish only missing baselines at startup. Fully supplied baselines do
  # not need an eager API call; all watches retain the original sleep-first
  # polling behavior.
  for index in "${!REPOS[@]}"; do
    if [ "${COMMENT_BASE_SET[$index]}" -eq 0 ] || [ "${REVIEW_BASE_SET[$index]}" -eq 0 ]; then
      if load_current_counts "$index"; then
        fill_missing_baselines "$index"
      fi
    fi
  done

  while true; do
    sleep "$INTERVAL"
    for index in "${!REPOS[@]}"; do
      # Persistent watch mode alone treats a transient API failure as no
      # change, preserving the last in-memory baseline.
      load_current_counts "$index" || continue
      fill_missing_baselines "$index"
      if counts_changed "$index"; then
        print_new_activity "$index"
        exit 0
      fi
    done
  done
}

run_once() {
  local index
  local saw_activity=0
  local initialized=0

  # Fetch everything before emitting output so an API failure cannot leave a
  # caller with a partial set of apparently valid baselines.
  for index in "${!REPOS[@]}"; do
    load_current_counts "$index" || api_failure "$index"
  done

  for index in "${!REPOS[@]}"; do
    if [ "${HAS_SUPPLIED_BASE[$index]}" -eq 0 ]; then
      fill_missing_baselines "$index"
      print_current_line BASELINE "$index"
      initialized=1
      continue
    fi

    fill_missing_baselines "$index"
    if counts_changed "$index"; then
      print_new_activity "$index"
      saw_activity=1
    else
      print_current_line NO_CHANGE "$index"
    fi
  done

  if [ "$saw_activity" -eq 1 ] || [ "$initialized" -eq 1 ]; then
    exit 0
  fi
  exit 3
}

emit_first_change() {
  local index

  for index in "${!REPOS[@]}"; do
    if counts_changed "$index"; then
      print_new_activity "$index"
      return 0
    fi
  done
  return 1
}

run_wait() {
  local index sleep_for remaining
  local deadline=$((SECONDS + WAIT_DURATION))

  for index in "${!REPOS[@]}"; do
    load_current_counts "$index" || api_failure "$index"
    fill_missing_baselines "$index"
  done
  if emit_first_change; then
    exit 0
  fi

  while [ "$SECONDS" -lt "$deadline" ]; do
    remaining=$((deadline - SECONDS))
    sleep_for=$INTERVAL
    if [ "$sleep_for" -gt "$remaining" ]; then
      sleep_for=$remaining
    fi
    sleep "$sleep_for"

    for index in "${!REPOS[@]}"; do
      load_current_counts "$index" || api_failure "$index"
    done
    if emit_first_change; then
      exit 0
    fi
  done

  for index in "${!REPOS[@]}"; do
    print_current_line NO_CHANGE "$index"
  done
  exit 3
}

case "$MODE" in
  watch) run_watch ;;
  once) run_once ;;
  wait) run_wait ;;
esac
