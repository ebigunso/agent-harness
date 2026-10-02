#!/usr/bin/env bash
# Deterministic public-CLI checks. All Git mutations stay in throwaway repos.
set -euo pipefail
SCRIPT_DIR=$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")/../../plugins/coding-agent-orchestration-harness/skills/git-workflow/scripts" && pwd)
TEST_DIR=$(mktemp -d)
trap 'rm -rf -- "$TEST_DIR"' EXIT
export GIT_CONFIG_NOSYSTEM=1 GIT_CONFIG_GLOBAL=/dev/null
export GIT_AUTHOR_NAME='Fixture Author' GIT_AUTHOR_EMAIL='fixture@example.invalid'
export GIT_COMMITTER_NAME='Fixture Committer' GIT_COMMITTER_EMAIL='fixture@example.invalid'
export GIT_AUTHOR_DATE='2025-01-01T00:00:00Z' GIT_COMMITTER_DATE='2025-01-01T00:00:00Z'
export HOME="$TEST_DIR/home" USER=sweep_local USERNAME=sweep_windows
export USERPROFILE='F:\Profiles\sweep_windows' APPDATA='F:\Profiles\sweep_windows\AppData\Roaming'
export LOCALAPPDATA='F:\Profiles\sweep_windows\AppData\Local' HOMEDRIVE=F: HOMEPATH='\Profiles\sweep_windows'
export HOSTNAME=sweep-host.example.invalid HOST=sweep-host COMPUTERNAME=SWEEP-HOST
mkdir -p "$HOME" "$TEST_DIR/hooks"
# Test doubles prevent real host discovery; identity collection itself still runs.
uname() { printf '%s\n' 'sweep-host.example.invalid'; }
hostname() { case ${1:-} in -a) printf '%s\n' 'sweep-alias' ;; *) uname ;; esac; }
export -f uname hostname

PASSED=0 CASE= OUT= ERR= SERIAL=0
fail() { printf 'FAIL %s: %s\nstdout:\n%s\nstderr:\n%s\n' "$CASE" "$1" "$OUT" "$ERR" >&2; exit 1; }
pass() { PASSED=$((PASSED + 1)); printf 'PASS %s\n' "$CASE"; }
has() { [[ $OUT == *"$1"* ]] || fail "missing $1"; }
lacks() { [[ $OUT != *"$1"* ]] || fail "unexpected $1"; }
commit() { git add --all; git commit --quiet -m "${1:-fixture}"; }
fixture() {
  SERIAL=$((SERIAL + 1))
  CASE=$1
  cd "$TEST_DIR"
  git init --quiet --bare "remote-$SERIAL"
  git init --quiet --initial-branch=topic "repo-$SERIAL"
  cd "repo-$SERIAL"
  git config core.hooksPath "$TEST_DIR/hooks"
  git config core.autocrlf false
  git remote add origin "../remote-$SERIAL"
  printf 'base\n' > file.txt
  commit
  BASE=$(git rev-parse HEAD)
  git push --quiet origin 'refs/heads/topic:refs/heads/topic'
}
run() {
  local expected=$1 rc=0 before after
  shift
  before=$(git for-each-ref; git status --porcelain=v1; git config --local --list)
  OUT=$(bash "$SCRIPT_DIR/privacy-sweep.sh" "$@" 2> "$TEST_DIR/stderr") || rc=$?
  ERR=$(<"$TEST_DIR/stderr")
  [ "$rc" -eq "$expected" ] || fail "exit $rc, expected $expected"
  after=$(git for-each-ref; git status --porcelain=v1; git config --local --list)
  [ "$before" = "$after" ] || fail 'sweep changed refs, worktree or configuration'
  if [ "$expected" -ne 0 ]; then lacks 'CLEAN '; fi
}

fixture 'one-letter Unix identity ignores longer tokens'
printf '/home/adam/project allocation alpha\n' >> file.txt
commit
HOME=/home/a USER=a USERNAME= USERPROFILE= APPDATA= LOCALAPPDATA= HOMEDRIVE= HOMEPATH= run 0
has 'CLEAN commits=1'; pass

CASE='one-letter Unix account and literal home remain detectable'
printf '/home/a/project\n' >> file.txt
commit
HOME=/home/a USER=a USERNAME= USERPROFILE= APPDATA= LOCALAPPDATA= HOMEDRIVE= HOMEPATH= run 1
has 'path=file.txt line=3'
HOME=/home/a USER= USERNAME= USERPROFILE= APPDATA= LOCALAPPDATA= HOMEDRIVE= HOMEPATH= run 1
has 'path=file.txt line=3'; pass

fixture 'published history is excluded without an upstream'
printf 'sweep_local\n' >> file.txt
commit
git push --quiet origin topic
run 0
has 'CLEAN commits=0'
printf 'safe addition\n' >> file.txt
commit
GIT_CONFIG_COUNT=1 GIT_CONFIG_KEY_0=core.autocrlf GIT_CONFIG_VALUE_0=true run 0
[ -z "$ERR" ] || fail 'blob diff emitted conversion warnings with scratch paths'
has 'CLEAN commits=1'; pass

fixture 'unpublished stack ancestors survive local upstream and later deletion'
printf 'sweep_local\n' >> file.txt
commit
LEAK=$(git rev-parse HEAD)
git branch unpublished-base
git branch --set-upstream-to=unpublished-base >/dev/null
printf 'base\n' > file.txt
commit
run 1
has "CANDIDATE commit=$LEAK path=file.txt line=2"; has 'REVIEW commits=2'; pass

fixture 'destination has a distinct push URL and unrelated upstream'
git init --quiet --bare "$TEST_DIR/push-only"
git remote set-url --push origin "$TEST_DIR/push-only"
printf 'sweep_local\n' >> file.txt
commit
git -C "../remote-$SERIAL" fetch --quiet "../repo-$SERIAL" topic:topic
git fetch --quiet origin
git branch --set-upstream-to=origin/topic >/dev/null
run 1 origin topic
has 'REVIEW commits=2'; has 'path=file.txt line=2'; pass

fixture 'platform and encoding identity forms'
FORMS=(windows git-bash wsl macos linux custom-home json unicode hex octal url host alias)
for form in "${FORMS[@]}"; do
  case $form in
    windows) value='f:\profiles\SWEEP_WINDOWS\source' ;;
    git-bash) value='/f/Profiles/sweep_windows/source' ;;
    wsl) value='/mnt/f/Profiles/sweep_windows/source' ;;
    macos) value='/Users/sweep_local/source' ;;
    linux) value='/home/sweep_local/source' ;;
    custom-home) value="$HOME/source" ;;
    json) value='F:\\Profiles\\sweep_windows\\source' ;;
    unicode) value='\u0073weep_local' ;;
    hex) value='\x73weep_local' ;;
    octal) value='\163weep_local' ;;
    url) value='%73%77%65%65%70%5F%6C%6F%63%61%6C' ;;
    host) value='SWEEP-HOST' ;;
    alias) value='sweep-alias' ;;
  esac
  printf '%s\n' "$value" >> file.txt
done
commit
run 1
number=2
for form in "${FORMS[@]}"; do
  CASE="runtime identity: $form"
  has "path=file.txt line=$number reason="; pass
  number=$((number + 1))
done

fixture 'home match works independently of account name'
USER= USERNAME= run 0
printf '/mnt/f/Profiles/sweep_windows/source\n' >> file.txt
commit
USER= USERNAME= run 1
has 'path=file.txt line=2'; pass

fixture 'full message body and both identities are inspected inside UTF-8'
printf 'caf\303\251: SWEEP_LOCAL\n' >> file.txt
GIT_AUTHOR_NAME=sweep_local GIT_COMMITTER_EMAIL=sweep_windows@example.invalid commit $'\360\237\224\222 summary\n\nquoted sweep-alias'
run 1
has 'path=\<commit\> line=3'; has 'path=\<commit\> line=4'; has 'path=\<commit\> line=8'
has 'path=file.txt line=2'; lacks 'INSPECT '
pass

fixture 'emoji subject and valid UTF-8 punctuation are clean'
printf 'caf\303\251 \342\200\224 text\360\237\224\222\n' >> file.txt
# Classify the stored bytes, even when a commit declares a different encoding.
git config i18n.commitEncoding ISO-8859-1
commit $'\360\237\224\222 fixture'
run 0
has 'CLEAN commits=1'; lacks 'INSPECT '; pass

fixture 'non-ASCII runtime identities match literally'
printf 'sweep_\303\251\n' >> file.txt
commit
USER=$'sweep_\303\251' USERNAME= run 1
has 'path=file.txt line=2'; lacks 'INSPECT '; pass

fixture 'rename path is scanned even with unchanged content'
git mv file.txt sweep_local.txt
commit
run 1
has 'path=sweep_local.txt line=0'; pass

fixture 'NUL path records keep tab and newline names intact'
# Windows filesystems cannot create control-character filenames; Git trees can.
blob=$(printf 'safe\n' | git hash-object -w --stdin)
tree=$(printf '100644 blob %s\tsweep_local\twith\nnewline\0' "$blob" | git mktree -z)
tip=$(printf 'rename fixture\n' | git commit-tree "$tree" -p HEAD)
git update-ref refs/heads/topic "$tip"
run 1
has "path=\$'sweep_local\twith\nnewline' line=0"; pass

fixture 'merge resolution is inspected against every parent'
git checkout --quiet -b side
printf 'side\n' > side.txt
commit
git checkout --quiet topic
printf 'topic\n' > topic.txt
commit
git merge --quiet --no-commit --no-ff side
printf 'sweep_local\n' >> file.txt
commit 'merge'
MERGE=$(git rev-parse HEAD)
run 1
has "CANDIDATE commit=$MERGE path=file.txt line=2"; pass

fixture 'portable placeholders, longer tokens and empty identities are clean'
printf '%s\n' '%USERPROFILE% %APPDATA% %LOCALAPPDATA% <name> <user> <username>' \
  'prefix_sweep_local_suffix sweep_locality mysweep-host.example.invalid' >> file.txt
printf '%s\n' 'sweep_localsweep_local rootless allocation userland' >> file.txt
commit
run 0
has 'CLEAN commits=1'
USER= USERNAME= USERPROFILE= APPDATA= LOCALAPPDATA= HOMEDRIVE= HOMEPATH= HOME= run 0
has 'CLEAN commits=1'
USER=name USERNAME=user run 0
has 'CLEAN commits=1'; pass

fixture 'binary and malformed UTF-8 content require inspection'
printf 'safe\0opaque' > binary.dat
printf '\303\050\n' > invalid.txt
printf '\300\257\n' > overlong.txt
printf '\355\240\200\n' > surrogate.txt
printf '\364\220\200\200\n' > out-of-range.txt
printf '\360\237' > truncated.txt
printf 'version https://git-lfs.github.com/spec/v1\noid sha256:fixture\nsize 1\n' > pointer.txt
printf '\\u0000\n' > escape.txt
commit
run 1
has 'INSPECT '; has 'path=binary.dat line=0'; has 'path=invalid.txt line=0'
has 'path=overlong.txt line=0'; has 'path=surrogate.txt line=0'
has 'path=out-of-range.txt line=0'; has 'path=truncated.txt line=0'
has 'path=pointer.txt line=0'; has 'path=escape.txt line=1'; pass

fixture 'unfetched provider refs are noted without blocking or hiding candidates'
git init --quiet --initial-branch=other "$TEST_DIR/other"
printf 'unavailable\n' > "$TEST_DIR/other/file"
git -C "$TEST_DIR/other" add file
git -C "$TEST_DIR/other" commit --quiet -m other
git -C "../remote-$SERIAL" fetch --quiet "$TEST_DIR/other" other:refs/pull/9/merge
run 0
has 'NOTE ref=refs/pull/9/merge '; has 'CLEAN commits=0'; lacks 'INSPECT '
printf 'sweep_local\n' >> file.txt
commit
run 1
has 'NOTE ref=refs/pull/9/merge '; has 'path=file.txt line=2'; lacks 'INSPECT '; pass

CASE='missing destination branch tip still refuses a clean result'
remote_tip=$(git -C "$TEST_DIR/other" rev-parse HEAD)
git -C "../remote-$SERIAL" update-ref refs/heads/topic "$remote_tip"
run 2
has 'destination\ branch\ tip\ missing'; pass

fixture 'one destination only and invalid branch fail closed'
git remote set-url --add --push origin "../remote-$SERIAL"
git remote set-url --add --push origin "../remote-$SERIAL"
run 2
has 'exactly\ one\ push\ URL'
run 2 origin 'missing-branch'
has 'local\ branch\ missing'; pass

printf 'PASS all %s cases\n' "$PASSED"
