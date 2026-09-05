#!/usr/bin/env bash
# Poll GitHub pull requests and their stacks for count or terminal-state changes.
#
# Usage:
#   pr-comment-watch.sh [-i SECONDS] OWNER/REPO:PR[:comments[:reviews[:state]]] ...
#   pr-comment-watch.sh --once OWNER/REPO:PR[:comments[:reviews[:state]]] ...
#   pr-comment-watch.sh --wait SECONDS [-i SECONDS] OWNER/REPO:PR[:comments[:reviews[:state]]] ...
#
# Hard-won implementation invariants (do not simplify these away):
#   - One GraphQL query per spec per poll supplies counts, state, and membership.
#     Parse with gh's --jq; no separate jq process or dependency.
#   - ARMED is startup confirmation, not a heartbeat. Subsequent watch polls
#     stay silent until the first NEW_ACTIVITY or TERMINAL, then exit.
#   - Posting replies can fire the watcher. After handling a review round,
#     restart or re-baseline it so self-induced activity is not mistaken for a
#     new reviewer round.
#   - A transient API failure is "no change" only after watch startup.
#     Startup failures and probe-mode failures exit 4.
#   - Terminal transitions take precedence over counts; terminal baselines
#     never fire again, even if their counts change.
set -u

INTERVAL=120
INTERVAL_SET=0
MODE=watch
MODE_SET=0
WAIT_DURATION=

usage() {
  printf '%s\n' \
    "usage: $0 [-i SECONDS] OWNER/REPO:PR[:comments[:reviews[:state]]] ..." \
    "       $0 --once OWNER/REPO:PR[:comments[:reviews[:state]]] ..." \
    "       $0 --wait SECONDS [-i SECONDS] OWNER/REPO:PR[:comments[:reviews[:state]]] ..." >&2
}

usage_error() {
  [ $# -eq 0 ] || printf 'error: %s\n' "$1" >&2
  usage
  exit 2
}

set_mode() {
  [ "$MODE_SET" -eq 0 ] || usage_error "choose exactly one of --once or --wait"
  MODE=$1
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
    --) shift; break ;;
    -*) usage_error "unknown option: $1" ;;
    *) break ;;
  esac
done

[ "$MODE" != once ] || [ "$INTERVAL_SET" -eq 0 ] || usage_error "-i is not used with --once"
[ $# -gt 0 ] || usage_error "at least one pull request spec is required"

declare -a REPOS=() PRS=() SUPPLIED_COMMENTS=() SUPPLIED_REVIEWS=() SUPPLIED_STATES=()
for spec in "$@"; do
  spec=${spec#spec=}
  if [[ ! $spec =~ ^([^/:[:space:]]+)/([^/:[:space:]]+):([1-9][0-9]*)(:([0-9]+)(:([0-9]+)(:(open|merged|closed))?)?)?$ ]]; then
    usage_error "malformed pull request spec: $spec"
  fi
  REPOS+=("${BASH_REMATCH[1]}/${BASH_REMATCH[2]}")
  PRS+=("${BASH_REMATCH[3]}")
  SUPPLIED_COMMENTS+=("${BASH_REMATCH[5]:-}")
  SUPPLIED_REVIEWS+=("${BASH_REMATCH[7]:-}")
  SUPPLIED_STATES+=("${BASH_REMATCH[9]:-open}")
done

# Ordered keys preserve input/member order; maps identify members across specs.
declare -a MEMBERS=() POLLED=()
declare -A BASE_COMMENTS=() BASE_REVIEWS=() BASE_STATES=() SUPPLIED=()
declare -A COMMENTS=() REVIEWS=() STATES=() STACKS=()

QUERY='query($o:String!,$r:String!,$n:Int!){
  repository(owner:$o,name:$r){ pullRequest(number:$n){
    number state merged reviews{totalCount} totalCommentsCount
    stack{ number entries(first:100){ nodes{ pullRequest{
      number state merged reviews{totalCount} totalCommentsCount
    } } } }
  } }
}'
FILTER='.data.repository.pullRequest as $p | ($p.stack.number // "none") as $s |
  (if $p.stack then [$p.stack.entries.nodes[].pullRequest] else [$p] end)[] |
  "\(.number) \($s) \(.totalCommentsCount) \(.reviews.totalCount) \(if .merged then "merged" elif .state=="CLOSED" then "closed" else "open" end)"'

fetch_members() {
  local repo=$1 pr=$2 output row
  # ponytail: stacks stop at 100 entries; add cursor handling if that ceiling matters.
  if [ "$MODE" = watch ]; then
    output=$(gh api graphql -f query="$QUERY" -f o="${repo%/*}" -f r="${repo#*/}" -F n="$pr" --jq "$FILTER" 2>/dev/null) || return 1
  else
    output=$(gh api graphql -f query="$QUERY" -f o="${repo%/*}" -f r="${repo#*/}" -F n="$pr" --jq "$FILTER") || return 1
  fi
  [ -n "$output" ] || return 1
  while IFS= read -r row; do
    [[ $row =~ ^[1-9][0-9]*\ (none|[1-9][0-9]*)\ [0-9]+\ [0-9]+\ (open|merged|closed)$ ]] || return 1
  done <<< "$output"
  printf '%s\n' "$output"
}

api_failure() {
  printf 'error: could not fetch counts for repo=%s pr=%s\n' "${REPOS[$1]}" "${PRS[$1]}" >&2
  exit 4
}

poll() {
  local startup=$1 index rows pr stack comments reviews state key
  local -A seen=()
  POLLED=()
  for index in "${!REPOS[@]}"; do
    if ! rows=$(fetch_members "${REPOS[$index]}" "${PRS[$index]}"); then
      if [ "$startup" -eq 1 ] || [ "$MODE" != watch ]; then
        api_failure "$index"
      fi
      continue
    fi
    while read -r pr stack comments reviews state; do
      key="${REPOS[$index]}:$pr"
      if [ -z "${seen[$key]:-}" ]; then
        POLLED+=("$key")
        seen[$key]=1
      fi
      COMMENTS[$key]=$comments
      REVIEWS[$key]=$reviews
      STATES[$key]=$state
      STACKS[$key]=$stack
      if [ -z "${BASE_STATES[$key]:-}" ]; then
        MEMBERS+=("$key")
        BASE_COMMENTS[$key]=$comments
        BASE_REVIEWS[$key]=$reviews
        BASE_STATES[$key]=$state
      fi
    done <<< "$rows"
  done
}

normalize_count() {
  local value=$1
  while [[ $value == 0* && ${#value} -gt 1 ]]; do value=${value#0}; done
  printf '%s' "$value"
}

apply_supplied_baselines() {
  local index key comments reviews state baseline
  for index in "${!REPOS[@]}"; do
    [ -n "${SUPPLIED_COMMENTS[$index]}" ] || continue
    key="${REPOS[$index]}:${PRS[$index]}"
    [ -n "${BASE_STATES[$key]:-}" ] || api_failure "$index"
    comments=$(normalize_count "${SUPPLIED_COMMENTS[$index]}")
    reviews=$(normalize_count "${SUPPLIED_REVIEWS[$index]:-${REVIEWS[$key]}}")
    state=${SUPPLIED_STATES[$index]}
    baseline="$comments:$reviews:$state"
    if [ -n "${SUPPLIED[$key]:-}" ] && [ "${SUPPLIED[$key]}" != "$baseline" ]; then
      usage_error "conflicting baselines for $key"
    fi
    SUPPLIED[$key]=$baseline
    BASE_COMMENTS[$key]=$comments
    BASE_REVIEWS[$key]=$reviews
    BASE_STATES[$key]=$state
  done
}

print_line() {
  local label=$1 key=$2
  local comments=${COMMENTS[$key]} reviews=${REVIEWS[$key]} state=${STATES[$key]}
  if [ "$label" = ARMED ]; then
    comments=${BASE_COMMENTS[$key]}
    reviews=${BASE_REVIEWS[$key]}
    state=${BASE_STATES[$key]}
  fi
  printf '%s repo=%s pr=%s stack=%s' "$label" "${key%:*}" "${key##*:}" "${STACKS[$key]}"
  if [ "$label" = NEW_ACTIVITY ]; then
    printf ' comments=%s (was %s) reviews=%s (was %s)' "$comments" "${BASE_COMMENTS[$key]}" "$reviews" "${BASE_REVIEWS[$key]}"
  elif [ "$label" != TERMINAL ]; then
    printf ' comments=%s reviews=%s' "$comments" "$reviews"
  fi
  printf ' state=%s spec=%s:%s:%s:%s\n' "$state" "$key" "$comments" "$reviews" "$state"
}

emit_change() {
  local key=$1
  [ "${BASE_STATES[$key]}" = open ] || return 1
  if [ "${STATES[$key]}" != open ]; then
    print_line TERMINAL "$key"
  elif [ "${COMMENTS[$key]}" != "${BASE_COMMENTS[$key]}" ] || [ "${REVIEWS[$key]}" != "${BASE_REVIEWS[$key]}" ]; then
    print_line NEW_ACTIVITY "$key"
  else
    return 1
  fi
}

emit_first_change() {
  local key
  for key in "${POLLED[@]}"; do
    emit_change "$key" && return 0
  done
  return 1
}

# Fetch every spec before printing anything or applying supplied baselines.
# This makes overlap precedence independent of argument order.
deadline=$((SECONDS + ${WAIT_DURATION:-0}))
poll 1
apply_supplied_baselines

case "$MODE" in
  once)
    result=3
    # Only bare input specs request initialization; fetched siblings still
    # emit BASELINE tokens without changing an otherwise quiet probe's exit.
    for comments in "${SUPPLIED_COMMENTS[@]}"; do
      [ -n "$comments" ] || result=0
    done
    for key in "${MEMBERS[@]}"; do
      if [ -z "${SUPPLIED[$key]:-}" ]; then
        print_line BASELINE "$key"
      elif emit_change "$key"; then
        result=0
      else
        print_line NO_CHANGE "$key"
      fi
    done
    exit "$result"
    ;;
  watch)
    for key in "${MEMBERS[@]}"; do print_line ARMED "$key"; done
    while true; do
      sleep "$INTERVAL"
      poll 0
      emit_first_change && exit 0
    done
    ;;
  wait)
    emit_first_change && exit 0
    while [ "$SECONDS" -lt "$deadline" ]; do
      remaining=$((deadline - SECONDS))
      sleep_for=$INTERVAL
      [ "$sleep_for" -le "$remaining" ] || sleep_for=$remaining
      sleep "$sleep_for"
      poll 0
      emit_first_change && exit 0
    done
    for key in "${POLLED[@]}"; do print_line NO_CHANGE "$key"; done
    exit 3
    ;;
esac
