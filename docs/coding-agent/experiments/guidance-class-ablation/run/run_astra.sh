#!/usr/bin/env bash
# Astra cells for the ablation: pure-baseline ephemeral codex exec per prompt file, N in parallel.
# Usage: bash run/run_astra.sh <experiment-dir> [parallel]
# Reads work/prompts/*.txt, writes work/astra/<cell>.txt (skips cells whose output already ends with the done marker).
# Moves $CODEX_HOME/AGENTS.md aside for the run window and restores it with a hash check (same discipline as
# frontier-guard-probes/run_baseline.sh). Runs in an empty scratch directory so no repository content is visible.
set -u
ROOT="$(cd "${1:?usage: run_astra.sh <experiment-dir> [parallel]}" && pwd)" || exit 2
PAR="${2:-6}"
CODEX_DIR="${CODEX_HOME:-$HOME/.codex}"; LOADER="$CODEX_DIR/AGENTS.md"; BACKUP="$CODEX_DIR/AGENTS.md.ablation-aside"
hash_file() { sha256sum "$1" | cut -c1-64; }
[ -e "$BACKUP" ] && { echo "refusing: $BACKUP exists" >&2; exit 2; }
command -v codex >/dev/null || { echo "codex not on PATH" >&2; exit 2; }
mkdir -p "$ROOT/work/astra" "$ROOT/work/empty" || exit 2
before=""; [ -f "$LOADER" ] && before=$(hash_file "$LOADER")
moved=0; rc=0
restore() { [ "$moved" -eq 1 ] || return 0; mv -f "$BACKUP" "$LOADER" || { echo "RESTORE FAILED" >&2; rc=4; return; }
  after=$(hash_file "$LOADER"); if [ "$after" = "$before" ]; then echo "AGENTS.md restored (sha256 match)"; else echo "RESTORE HASH MISMATCH" >&2; rc=4; fi; moved=0; }
on_exit() { st=$?; restore; [ "$rc" -eq 4 ] && exit 4; [ "$st" -ne 0 ] && exit "$st"; exit "$rc"; }
trap on_exit EXIT; trap 'exit 130' INT; trap 'exit 143' TERM
if [ -f "$LOADER" ]; then mv "$LOADER" "$BACKUP" || exit 2; moved=1; echo "AGENTS.md moved aside (sha256 $before)"; fi

run_one() {
  local p="$1" cell out
  cell=$(basename "$p" .txt); out="$ROOT/work/astra/$cell.txt"
  if [ -f "$out" ] && grep -q '^__ABLATION_DONE__' "$out"; then return 0; fi
  ( cd "$ROOT/work/empty" && timeout 600 codex exec --ephemeral --disable plugins --disable hooks -c project_doc_max_bytes=0 --skip-git-repo-check -s read-only - < "$p" > "$out.tmp" 2>&1 )
  local st=$?
  { cat "$out.tmp"; echo; echo "__ABLATION_DONE__ exit=$st"; } > "$out"; rm -f "$out.tmp"
  [ "$st" -eq 0 ] || echo "cell $cell exit $st" >&2
}
export -f run_one; export ROOT
ls "$ROOT"/work/prompts/*.txt | xargs -P "$PAR" -I{} bash -c 'run_one "$@"' _ {}
done_count=$(grep -l '^__ABLATION_DONE__ exit=0' "$ROOT"/work/astra/*.txt 2>/dev/null | wc -l)
total=$(ls "$ROOT"/work/prompts/*.txt | wc -l)
echo "astra cells complete: $done_count / $total"
[ "$done_count" -eq "$total" ] || rc=3
exit $rc
