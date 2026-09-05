#!/usr/bin/env bash
# Deterministic public-CLI checks; gh fixtures are the rows returned by --jq.
set -u

command -v timeout >/dev/null 2>&1 || { printf 'error: this self-check needs the timeout(1) command on PATH
' >&2; exit 1; }

SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)
TEST_DIR=$(mktemp -d)
trap 'rm -rf -- "$TEST_DIR"' EXIT
export TEST_DIR
export PATH="$TEST_DIR:$PATH"

cat > "$TEST_DIR/gh" <<'GH'
#!/usr/bin/env bash
set -u

command -v timeout >/dev/null 2>&1 || { printf 'error: this self-check needs the timeout(1) command on PATH
' >&2; exit 1; }
call=$(<"$TEST_DIR/calls")
call=$((call + 1))
printf '%s\n' "$call" > "$TEST_DIR/calls"
[ "${1:-} ${2:-}" = 'api graphql' ] || exit 90
[[ " $* " == *' --jq '* && " $* " != *' --paginate '* ]] || exit 91
printf '%s\n' "$*" >> "$TEST_DIR/requests"
[ -f "$TEST_DIR/response-$call" ] || { echo 'fixture exhausted' >&2; exit 92; }
while IFS= read -r row; do
  if [ "$row" = FAIL ]; then echo 'fake API failure' >&2; exit 1; fi
  printf '%s\n' "$row"
done < "$TEST_DIR/response-$call"
GH
chmod +x "$TEST_DIR/gh"

CASE=
OUT=
ERR=
PASSED=0
fail() {
  printf 'FAIL %s: %s\nstdout:\n%s\nstderr:\n%s\n' "$CASE" "$1" "$OUT" "$ERR" >&2
  exit 1
}
responses() {
  local row index=0
  rm -f -- "$TEST_DIR"/response-*
  printf '0\n' > "$TEST_DIR/calls"
  : > "$TEST_DIR/requests"
  for row in "$@"; do
    index=$((index + 1))
    printf '%s\n' "$row" > "$TEST_DIR/response-$index"
  done
}
run() {
  CASE=$1
  local expected_exit=$2 expected_calls=$3 rc=0
  shift 3
  # Bound a broken watch loop so an assertion failure cannot hang this check.
  OUT=$(timeout 12 bash "$SCRIPT_DIR/pr-comment-watch.sh" "$@" 2>"$TEST_DIR/stderr") || rc=$?
  ERR=$(<"$TEST_DIR/stderr")
  [ "$rc" -eq "$expected_exit" ] || fail "exit $rc, expected $expected_exit"
  [ "$(<"$TEST_DIR/calls")" -eq "$expected_calls" ] || fail "unexpected gh invocation count"
}
has() { [[ $OUT == *"$1"* ]] || fail "missing $1"; }
lacks() { [[ $OUT != *"$1"* ]] || fail "unexpected $1"; }
lines() {
  local label=$1 expected=$2 line count=0
  while IFS= read -r line; do
    [[ $line == "$label "* ]] && count=$((count + 1))
  done <<< "$OUT"
  [ "$count" -eq "$expected" ] || fail "$label lines: $count, expected $expected"
}
pass() {
  local line
  while IFS= read -r line; do
    [ -z "$line" ] || [[ $line =~ \ spec=[^[:space:]]+:[0-9]+:[0-9]+:(open|merged|closed)$ ]] || fail 'line lacks final spec token'
  done <<< "$OUT"
  PASSED=$((PASSED + 1))
  printf 'PASS %s\n' "$CASE"
}

responses '1 none 5 2 open' '1 none 5 2 open' '1 none 5 3 open'
run 'watch reviews-only, silence, one call per poll' 0 3 -i 1 org/repo:1
lines ARMED 1; lines NEW_ACTIVITY 1; lines NO_CHANGE 0; lines BASELINE 0
has 'comments=5 (was 5) reviews=3 (was 2)'; pass

responses '1 none 5 2 open' '1 none 6 2 open'
run 'watch comments-only' 0 2 -i 1 org/repo:1
has 'comments=6 (was 5) reviews=2 (was 2)'; pass

responses '1 10 5 2 open' $'1 10 5 2 open\n2 10 99 9 open' $'1 10 5 2 open\n2 10 99 10 open'
run 'stack growth baselines silently' 0 3 -i 1 org/repo:1
lines ARMED 1; lines NEW_ACTIVITY 1; lines BASELINE 0
has 'NEW_ACTIVITY repo=org/repo pr=2 stack=10 comments=99 (was 99) reviews=10 (was 9)'; pass

responses '1 none 5 2 open' FAIL '1 none 6 2 open'
run 'watch transient failure preserves baseline' 0 3 -i 1 org/repo:1
lines ARMED 1; lines NEW_ACTIVITY 1
[ -z "$ERR" ] || fail 'watch failure was not silent'; pass

responses FAIL
run 'once API failure' 4 1 --once org/repo:1:5:2
[ -z "$OUT" ] || fail 'failure printed baseline'; pass

responses FAIL
run 'watch startup failure with supplied baseline' 4 1 -i 1 org/repo:1:5:2
[ -z "$OUT" ] || fail 'startup failure armed'
[[ $ERR == *'error: could not fetch counts for repo=org/repo pr=1'* ]] || fail 'missing startup diagnostic'; pass

responses '1 none 5 2 open' '1 none 6 3 merged'
run 'terminal beats simultaneous count change' 0 2 -i 1 org/repo:1
lines TERMINAL 1; lines NEW_ACTIVITY 0
has 'state=merged spec=org/repo:1:6:3:merged'; pass

responses '1 none 6 3 merged' '1 none 6 3 merged'
run 'watch arms supplied counts and default open state' 0 2 -i 1 org/repo:1:5:2
has 'ARMED repo=org/repo pr=1 stack=none comments=5 reviews=2 state=open spec=org/repo:1:5:2:open'
lines TERMINAL 1; lines NEW_ACTIVITY 0; pass

responses '1 none 6 3 closed'
run 'closed transition' 0 1 --once org/repo:1:5:2:open
lines TERMINAL 1; lines NEW_ACTIVITY 0; has 'state=closed'; pass

responses '1 none 6 3 merged' '2 none 7 4 open'
run 'once prints every changed member' 0 2 --once org/repo:1:5:2 org/repo:2:6:4
lines TERMINAL 1; lines NEW_ACTIVITY 1; pass

responses '1 none 5 2 merged'
run 'bare merged baseline never fires' 0 1 --once org/repo:1
lines BASELINE 1; lines TERMINAL 0; has 'spec=org/repo:1:5:2:merged'; pass

responses '1 none 5 2 merged'
run 'explicit merged baseline ignores changed counts' 3 1 --once org/repo:1:0:0:merged
lines NO_CHANGE 1; lines NEW_ACTIVITY 0; lines TERMINAL 0; pass

responses '1 none 5 2 open' '1 none 6 3 open'
run 'same PR number in different repos' 0 2 --once org/one:1 org/two:1
lines BASELINE 2; has 'spec=org/one:1:5:2:open'; has 'spec=org/two:1:6:3:open'; pass

stack=$'1 10 5 2 open\n2 10 6 3 open'
responses "$stack"
run 'supplied spec emits sibling BASELINE but exits 3' 3 1 --once spec=org/repo:1:5:2:open
lines NO_CHANGE 1; lines BASELINE 1
has 'BASELINE repo=org/repo pr=2 stack=10 comments=6 reviews=3 state=open spec=org/repo:2:6:3:open'; pass

responses '1 none 5 2 open' '1 none 5 2 open'
run 'bare input alongside supplied baseline exits 0' 0 2 --once org/repo:1:5:2 org/repo:1
lines NO_CHANGE 1; lines BASELINE 0; pass

for order in fetched-first supplied-first; do
  responses "$stack" "$stack"
  if [ "$order" = fetched-first ]; then
    run "supplied-over-fetched $order" 0 2 --once org/repo:1 org/repo:2:0:0
  else
    run "supplied-over-fetched $order" 0 2 --once org/repo:2:0:0 org/repo:1
  fi
  lines BASELINE 1; lines NEW_ACTIVITY 1
  has 'pr=2 stack=10 comments=6 (was 0) reviews=3 (was 0)'; pass
done

responses '1 none 5 2 open' '1 none 5 2 open'
run 'identical supplied duplicates collapse' 3 2 --once org/repo:1:5:2 org/repo:1:5:2:open
lines NO_CHANGE 1; pass

for order in low-first high-first; do
  responses '1 none 5 2 open' '1 none 5 2 open'
  if [ "$order" = low-first ]; then
    run "differing supplied duplicates $order" 2 2 --once org/repo:1:4:2 org/repo:1:5:2
  else
    run "differing supplied duplicates $order" 2 2 --once org/repo:1:5:2 org/repo:1:4:2
  fi
  [ -z "$OUT" ] || fail 'conflicting baselines emitted output'; pass
done

responses '1 none 5 2 open'
run 'bare token reference' 3 1 --once org/repo:1:5:2:open
bare_output=$OUT; pass
responses '1 none 5 2 open'
run 'spec= prefix matches bare token' 3 1 --once spec=org/repo:1:5:2:open
[ "$OUT" = "$bare_output" ] || fail 'prefix changed behavior'; pass

responses '1 none 5 2 open'
run 'wait initial change' 0 1 --wait 0 org/repo:1:4:2
lines NEW_ACTIVITY 1; lines ARMED 0; pass

responses '1 none 5 2 open' '1 none 5 2 open'
run 'wait deadline' 3 2 --wait 1 -i 1 org/repo:1:5:2
lines NO_CHANGE 1; lines ARMED 0; pass

responses "$stack" '1 10 5 2 open'
run 'wait drops removed sibling from timeout and re-feed' 3 2 --wait 1 -i 1 org/repo:1:5:2
lines NO_CHANGE 1; lacks 'pr=2 '; lacks 'spec=org/repo:2:'
refeed=()
while IFS= read -r line; do refeed+=("${line##* }"); done <<< "$OUT"
responses '1 10 5 2 open'
run 'wait drops removed sibling from timeout and re-feed' 3 1 --once "${refeed[@]}"
lines NO_CHANGE 1; lacks 'pr=2 '; lacks 'spec=org/repo:2:'; pass

responses "$stack" FAIL
run 'wait failed final poll emits no replacement tokens' 4 2 --wait 1 -i 1 org/repo:1:5:2
[ -z "$OUT" ] || fail 'failed final poll emitted replacement tokens'; pass

responses '1 none 5 2 open' FAIL
run 'wait post-startup API failure' 4 2 --wait 5 -i 1 org/repo:1:5:2
[ -z "$OUT" ] || fail 'failed wait emitted output'; pass

responses FAIL
run 'wait startup API failure' 4 1 --wait 0 org/repo:1
[ -z "$OUT" ] || fail 'failed wait emitted output'; pass

responses "$stack" "$stack" $'1 10 5 2 open\n2 10 6 4 open' $'1 10 5 2 open\n2 10 6 4 open'
run 'overlapping specs queried once each per poll' 0 4 -i 1 org/repo:1 org/repo:2
lines ARMED 2; lines NEW_ACTIVITY 1; pass

responses '1 none 5 2 open'
run 'comments-only baseline fetches missing reviews' 3 1 --once org/repo:1:05
lines NO_CHANGE 1; has 'spec=org/repo:1:5:2:open'; pass

responses ''
run 'empty API payload is fetch failure' 4 1 --once org/repo:1
[ -z "$OUT" ] || fail 'empty payload emitted output'; pass

printf 'PASS all %s cases\n' "$PASSED"
