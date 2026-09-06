#!/usr/bin/env bash
# Pure-baseline guard probes: ephemeral headless Codex runs with nothing loaded.
# Usage: bash run_baseline.sh <experiment-root>
# Resets work/<X> from fixtures/<X>, runs prompts/<X>.txt in each, writes work/out<X>.txt.
# Moves ~/.codex/AGENTS.md aside for the run window and restores it on exit; prints the hash before and after.
# Exit codes: 0 all probes ran and the loader was restored intact; 2 setup refused; 3 a probe failed; 4 restore or hash check failed (takes precedence); 130/143 interrupted, loader restored first.
set -u
ROOT="$(cd "${1:?usage: run_baseline.sh <experiment-root>}" && pwd)" || exit 2
CODEX_DIR="${CODEX_HOME:-$HOME/.codex}"
LOADER="$CODEX_DIR/AGENTS.md"; BACKUP="$CODEX_DIR/AGENTS.md.probe-aside"
if [ -e "$BACKUP" ]; then echo "refusing to run: $BACKUP already exists (a previous run did not restore?)" >&2; exit 2; fi
hash_file() {
  if command -v sha256sum >/dev/null 2>&1; then sha256sum "$1" | cut -c1-64
  elif command -v shasum >/dev/null 2>&1; then shasum -a 256 "$1" | cut -c1-64
  else return 1; fi
}
moved=0; before=""; rc=0
if [ -f "$LOADER" ]; then
  before=$(hash_file "$LOADER") && [ -n "$before" ] || { echo "cannot hash $LOADER (sha256sum/shasum missing or failed); aborting" >&2; exit 2; }
  mv "$LOADER" "$BACKUP" || { echo "could not move $LOADER aside; aborting" >&2; exit 2; }
  moved=1; echo "AGENTS.md moved aside (sha256 $before)"
fi
restore() {
  [ "$moved" -eq 1 ] || return 0
  mv -f "$BACKUP" "$LOADER" || { echo "RESTORE FAILED: $BACKUP -> $LOADER" >&2; rc=4; return; }
  after=$(hash_file "$LOADER") || after=""
  if [ -n "$after" ] && [ "$after" = "$before" ]; then echo "AGENTS.md restored (sha256 match)"; else echo "RESTORE HASH MISMATCH: before=$before after=$after" >&2; rc=4; fi
  moved=0
}
on_exit() { st=$?; restore; if [ "$rc" -eq 4 ]; then exit 4; fi; if [ "$st" -ne 0 ]; then exit "$st"; fi; exit "$rc"; }
trap on_exit EXIT; trap 'exit 130' INT; trap 'exit 143' TERM
mkdir -p "$ROOT/work" || exit 2
pids=(); names=()
for X in A B C D; do
  rm -rf "$ROOT/work/$X" && cp -r "$ROOT/fixtures/$X" "$ROOT/work/$X" || { echo "fixture reset failed for $X" >&2; rc=3; continue; }
  PROMPT="$ROOT/prompts/$X.txt"; OUT="$ROOT/work/out$X.txt"
  [ -f "$PROMPT" ] || { echo "missing prompt $PROMPT" >&2; rc=3; continue; }
  ( cd "$ROOT/work/$X" && timeout 900 codex exec --ephemeral --disable plugins --disable hooks -c project_doc_max_bytes=0 --skip-git-repo-check -s workspace-write "$(cat "$PROMPT")" < /dev/null > "$OUT" 2>&1 ) &
  pids+=($!); names+=("$X")
done
for i in "${!pids[@]}"; do
  if wait "${pids[$i]}"; then echo "probe ${names[$i]} ok"; else echo "probe ${names[$i]} FAILED (exit $?)" >&2; rc=3; fi
done
for X in A B C D; do [ -s "$ROOT/work/out$X.txt" ] || { echo "missing output for $X" >&2; rc=3; }; done
exit $rc
