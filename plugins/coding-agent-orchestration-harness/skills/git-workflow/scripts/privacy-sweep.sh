#!/usr/bin/env bash
# Read-only pre-push inventory for one local branch -> same-named remote branch.
# Usage: bash privacy-sweep.sh [REMOTE [BRANCH]] (defaults: origin, current branch).
# Exit 0: no candidates; 1: candidates/inspection needed; 2: incomplete inventory.
# Requires Bash 4+, Git and coreutils. Temporary files only; no fetch or hooks.
set -eo pipefail
export LC_ALL=C GIT_NO_REPLACE_OBJECTS=1 GIT_NO_LAZY_FETCH=1 GIT_OPTIONAL_LOCKS=0

incomplete() { printf 'INSPECT commit=- path=- line=0 reason=%q\n' "$1"; exit 2; }
[ "${BASH_VERSINFO[0]}" -ge 4 ] || incomplete 'Bash 4+ required'
[ "$#" -le 2 ] || incomplete 'usage: privacy-sweep.sh [REMOTE [BRANCH]]'
REMOTE=${1:-origin}
BRANCH=${2:-$(git symbolic-ref --quiet --short HEAD)} || incomplete 'specify a local branch'
BRANCH=${BRANCH#refs/heads/}
[[ $REMOTE != -* && -n $REMOTE ]] || incomplete 'invalid remote'
git check-ref-format "refs/heads/$BRANCH" >/dev/null || incomplete 'invalid branch'
TIP=$(git rev-parse --verify "refs/heads/$BRANCH^{commit}") || incomplete 'local branch missing'
[ "$(git rev-parse --is-shallow-repository)" = false ] || incomplete 'shallow history; obtain complete history and rerun'
GRAFTS=$(git rev-parse --git-path info/grafts)
[ ! -s "$GRAFTS" ] || incomplete 'legacy grafts hide publication history'

SCRATCH=$(mktemp -d)
trap 'rm -rf -- "$SCRATCH"' EXIT
trap 'incomplete "read failed; inventory incomplete"' ERR
FOUND=0
COUNT=0
COMMIT=-
# Valid UTF-8 scalar values plus printable ASCII/tab/CR/LF; reject overlong
# forms, surrogate code points, out-of-range values and binary control bytes.
TEXT_RE=$'^([\t\r\n -~]|[\xc2-\xdf][\x80-\xbf]|\xe0[\xa0-\xbf][\x80-\xbf]|[\xe1-\xec\xee-\xef][\x80-\xbf]{2}|\xed[\x80-\x9f][\x80-\xbf]|\xf0[\x90-\xbf][\x80-\xbf]{2}|[\xf1-\xf3][\x80-\xbf]{3}|\xf4[\x80-\x8f][\x80-\xbf]{2})*$'
report() {
  printf '%s commit=%s path=%q line=%s reason=%q\n' "$1" "$COMMIT" "$2" "$3" "$4"
  FOUND=1
}

# Preserve literal path components while normalizing case and separators.
canonicalize() {
  NORMAL=${1,,}
  NORMAL=${NORMAL//\\//}
  local marker
  for marker in '%userprofile%' '%appdata%' '%localappdata%' '%home%' '%user%' \
    '%username%' '%computername%' '<name>' '<user>' '<username>' '<hostname>' \
    '$HOME' '${HOME}' '$USER' '${USER}' '$USERNAME' '${USERNAME}'; do
    marker=${marker,,}
    NORMAL=${NORMAL//"$marker"/PLACEHOLDER}
  done
}

# Decode only defined ASCII URL/JSON/C forms. Never use eval or printf on input
# as a format string. Keep a literal pass too: a Windows path can contain \n.
decode() {
  local rest=$1 prefix token number char
  DECODED= UNSUPPORTED=0
  while [[ $rest == *[\\%]* ]]; do
    prefix=${rest%%[\\%]*}
    DECODED+=$prefix
    rest=${rest:${#prefix}}
    token= number=
    if [[ $rest =~ ^%([[:xdigit:]]{2}) ]]; then
      token=${BASH_REMATCH[0]}; number=$((16#${BASH_REMATCH[1]}))
    elif [[ $rest =~ ^\\x([[:xdigit:]]{2}) || $rest =~ ^\\u([[:xdigit:]]{4}) || $rest =~ ^\\U([[:xdigit:]]{8}) ]]; then
      token=${BASH_REMATCH[0]}; number=$((16#${BASH_REMATCH[1]}))
    elif [[ $rest =~ ^\\([0-7]{1,3}) ]]; then
      token=${BASH_REMATCH[0]}; number=$((8#${BASH_REMATCH[1]}))
    elif [[ $rest == \\* ]]; then
      case ${rest:1:1} in
        \\|/|'"'|"'") token=${rest:0:2}; DECODED+=${rest:1:1} ;;
        n|r|t|a|b|f|v|e) token=${rest:0:2}; DECODED+=' ' ;;
      esac
    fi
    if [ -n "$number" ]; then
      if (( number == 0 )); then
        UNSUPPORTED=1; char=' '
      elif (( number > 127 )); then
        char=$token
      else
        printf -v char '\\%03o' "$number"
        printf -v char '%b' "$char"
      fi
      DECODED+=$char
    fi
    if [ -n "$token" ]; then rest=${rest:${#token}};
    else DECODED+=${rest:0:1}; rest=${rest:1}; fi
  done
  DECODED+=$rest
}

declare -a PATHS=() NAMES=() HOSTS=()
add_identity() {
  local kind=$1 value=$2 mounted drive suffix
  [ -n "$value" ] || return 0
  canonicalize "$value"
  [[ -n $NORMAL && $NORMAL != / && $NORMAL != *PLACEHOLDER* ]] || return 0
  case $kind in
    path)
      PATHS+=("${NORMAL%/}")
      # Keep the literal home; alternate drive spellings come only from its root.
      mounted=$NORMAL
      if [[ $mounted =~ ^/(mnt/)?([a-z])/(.*)$ ]]; then
        mounted="${BASH_REMATCH[2]}:/${BASH_REMATCH[3]}"
      fi
      if [[ $mounted =~ ^([a-z]):/(.*)$ ]]; then
        drive=${BASH_REMATCH[1]}; suffix=${BASH_REMATCH[2]%/}
        PATHS+=("${mounted%/}" "/$drive/$suffix" "/mnt/$drive/$suffix")
      fi
      ;;
    name) NAMES+=("$NORMAL") ;;
    host) HOSTS+=("$NORMAL"); [[ $NORMAL != *.* ]] || HOSTS+=("${NORMAL%%.*}") ;;
  esac
}
for value in "${HOME:-}" "${USERPROFILE:-}" "${APPDATA:-}" "${LOCALAPPDATA:-}"; do
  add_identity path "$value"
done
if [ -n "${HOMEDRIVE:-}" ] && [ -n "${HOMEPATH:-}" ]; then add_identity path "$HOMEDRIVE$HOMEPATH"; fi
for value in "${USER:-}" "${USERNAME:-}"; do add_identity name "$value"; done
MACHINE_HOST=$(uname -n) || incomplete 'cannot read machine host name'
for value in "$MACHINE_HOST" "${HOSTNAME:-}" "${HOST:-}" "${COMPUTERNAME:-}"; do add_identity host "$value"; done
# Optional hostname variants supplement uname/environment on systems providing it.
if command -v hostname >/dev/null 2>&1; then
  for flag in -s -f -a; do
    aliases=$(hostname "$flag" 2>/dev/null) || continue
    for value in $aliases; do add_identity host "$value"; done
  done
fi
# Hosts-file aliases are useful even when hostname has no -a (macOS/Windows).
for hosts_file in /etc/hosts "${SYSTEMROOT:-}/System32/drivers/etc/hosts"; do
  [ -r "$hosts_file" ] || continue
  while IFS= read -r row || [ -n "$row" ]; do
    row=${row%%#*}
    read -r -a fields <<< "$row"
    for value in "${fields[@]:1}"; do
      for host in "${HOSTS[@]}"; do
        if [ "${value,,}" = "$host" ]; then
          for alias in "${fields[@]:1}"; do add_identity host "$alias"; done
          break 2
        fi
      done
    done
  done < "$hosts_file"
done
[ "$((${#PATHS[@]} + ${#NAMES[@]} + ${#HOSTS[@]}))" -gt 0 ] || incomplete 'no runtime identities available'

matches() {
  local text=$1 identity rest before after preceding
  for identity in "${PATHS[@]}"; do
    rest=$text
    while [[ $rest == *"$identity"* ]]; do
      after=${rest#*"$identity"}
      [[ ${after:0:1} =~ [[:alnum:]_.-] ]] || return 0
      rest=$after
    done
  done
  for identity in "${NAMES[@]}" "${HOSTS[@]}"; do
    rest=$text
    preceding=
    while [[ $rest == *"$identity"* ]]; do
      before=${rest%%"$identity"*}; after=${rest#*"$identity"}
      [ -z "$before" ] || preceding=${before: -1}
      if [[ ! $preceding =~ [[:alnum:]_-] && ! ${after:0:1} =~ [[:alnum:]_-] ]]; then return 0; fi
      preceding=${identity: -1}
      rest=$after
    done
  done
  return 1
}

scan_line() {
  local path=$1 line_number=$2 text=$3 previous
  if [[ ! $text =~ $TEXT_RE ]]; then
    report INSPECT "$path" "$line_number" 'invalid UTF-8 or binary control bytes'; return
  fi
  canonicalize "$text"
  if matches "$NORMAL"; then report CANDIDATE "$path" "$line_number" 'runtime identity'; return; fi
  [[ $text == *[\\%]* ]] || return 0
  # Each successful decoding shortens the input, including nested encodings.
  while :; do
    previous=$text
    decode "$text"
    if [ "$UNSUPPORTED" -eq 1 ]; then report INSPECT "$path" "$line_number" 'NUL escape'; fi
    text=$DECODED
    canonicalize "$text"
    if matches "$NORMAL"; then report CANDIDATE "$path" "$line_number" 'encoded runtime identity'; return; fi
    [ "$text" != "$previous" ] || break
  done
}

searchable() {
  local bad content
  bad=$(tr -d '\11\12\15\40-\176\200-\377' < "$1" | wc -c) || incomplete 'cannot classify content'
  if [ "$bad" -ne 0 ]; then report INSPECT "$2" 0 'binary control bytes'; return 1; fi
  content=$(cat -- "$1") || incomplete 'cannot read content'
  if [[ ! $content =~ $TEXT_RE ]]; then report INSPECT "$2" 0 'invalid UTF-8'; return 1; fi
}
scan_file() {
  local path=$1 file=$2 line number=0
  if ! searchable "$file" "$path"; then return; fi
  while IFS= read -r line || [ -n "$line" ]; do
    number=$((number + 1)); scan_line "$path" "$number" "$line"
  done < "$file"
}

URLS=$(git remote get-url --push --all "$REMOTE") || incomplete 'cannot resolve destination'
[[ -n $URLS && $URLS != *$'\n'* ]] || incomplete 'exactly one push URL required'
git ls-remote -- "$URLS" > "$SCRATCH/remote" || incomplete 'cannot read destination refs'
printf '%s\n' "$TIP" > "$SCRATCH/revisions"
while read -r oid ref; do
  [[ $oid =~ ^[[:xdigit:]]+$ && -n $ref ]] || incomplete 'invalid remote advertisement'
  if ! kind=$(git cat-file -t "$oid^{}" 2>/dev/null); then
    [ "$ref" != "refs/heads/$BRANCH" ] || incomplete 'destination branch tip missing locally; obtain remote history and rerun'
    # Unfetched provider refs are not required to prove any exclusion. Omitting
    # them only widens the scan; a normal fetch need not retrieve PR merge refs.
    printf 'NOTE ref=%q oid=%s reason=%q\n' "$ref" "$oid" 'object unavailable locally; not used for exclusion'
    continue
  fi
  if [ "$kind" = commit ]; then
    base=$(git rev-parse --verify "$oid^{commit}") || incomplete 'unreadable remote commit'
    printf '^%s\n' "$base" >> "$SCRATCH/revisions"
  fi
done < "$SCRATCH/remote"
git rev-list --reverse --topo-order --stdin < "$SCRATCH/revisions" > "$SCRATCH/commits"
scan_line '<destination-ref>' 0 "refs/heads/$BRANCH"

while IFS= read -r COMMIT; do
  COUNT=$((COUNT + 1))
  git cat-file commit "$COMMIT" > "$SCRATCH/metadata"
  scan_file '<commit>' "$SCRATCH/metadata"
  PARENTS=()
  while IFS= read -r row && [ -n "$row" ]; do
    [[ $row != parent\ * ]] || PARENTS+=("${row#parent }")
  done < "$SCRATCH/metadata"
  [ "${#PARENTS[@]}" -gt 0 ] || PARENTS=('')
  for parent in "${PARENTS[@]}"; do
    args=(--root -r --no-commit-id --raw -z --no-abbrev --find-renames)
    [ -z "$parent" ] || args+=("$parent")
    git diff-tree "${args[@]}" "$COMMIT" > "$SCRATCH/changes"
    while IFS= read -r -d '' header; do
      read -r oldmode newmode oldoid newoid status <<< "$header"
      IFS= read -r -d '' path
      scan_line "$path" 0 "$path"
      if [[ $status == R* || $status == C* ]]; then
        IFS= read -r -d '' path
        scan_line "$path" 0 "$path"
      fi
      [ "$newmode" != 000000 ] || continue
      if [ "$newmode" = 160000 ]; then report INSPECT "$path" 0 'submodule content'; continue; fi
      git cat-file blob "$newoid" > "$SCRATCH/new"
      if ! searchable "$SCRATCH/new" "$path"; then continue; fi
      IFS= read -r first_line < "$SCRATCH/new" || true
      if [ "$first_line" = 'version https://git-lfs.github.com/spec/v1' ]; then
        report INSPECT "$path" 0 'external Git LFS content'
      fi
      if [ "$oldmode" = :000000 ]; then
        scan_file "$path" "$SCRATCH/new"
        continue
      fi
      if [ "$oldmode" = :160000 ]; then
        report INSPECT "$path" 0 'submodule replaced'; scan_file "$path" "$SCRATCH/new"; continue
      fi
      git cat-file blob "$oldoid" > "$SCRATCH/old"
      rc=0
      git -c core.autocrlf=false diff --no-index --no-ext-diff --no-textconv --no-color --text --unified=0 --inter-hunk-context=0 \
        -- "$SCRATCH/old" "$SCRATCH/new" > "$SCRATCH/patch" || rc=$?
      [ "$rc" -le 1 ] || incomplete 'cannot inspect blob diff'
      number=0
      while IFS= read -r row || [ -n "$row" ]; do
        if [[ $row =~ ^@@\ -[0-9]+(,[0-9]+)?\ \+([0-9]+)(,[0-9]+)?\ @@ ]]; then
          number=${BASH_REMATCH[2]}
        elif [[ $row == +* && $number -gt 0 ]]; then
          scan_line "$path" "$number" "${row:1}"
          number=$((number + 1))
        elif [[ $row == ' '* && $number -gt 0 ]]; then
          number=$((number + 1))
        fi
      done < "$SCRATCH/patch"
    done < "$SCRATCH/changes"
  done
done < "$SCRATCH/commits"
if [ "$FOUND" -ne 0 ]; then printf 'REVIEW commits=%s\n' "$COUNT"; exit 1; fi
printf 'CLEAN commits=%s tip=%s ref=%q (runtime identities in UTF-8; ASCII folding and escapes)\n' "$COUNT" "$TIP" "refs/heads/$BRANCH"
