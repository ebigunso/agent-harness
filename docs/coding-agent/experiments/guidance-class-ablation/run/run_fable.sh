#!/usr/bin/env bash
# Fable cells for the ablation: one headless Claude Code CLI call per prompt file, N in parallel.
# Usage: bash run/run_fable.sh <experiment-dir> [parallel]
# Reads work/prompts/*.txt, writes work/fable/<cell>.txt (the model's text) and work/fable-json/<cell>.json
# (the CLI result with usage). Skips cells whose text output already ends with the done marker.
# Context: fixed minimal system prompt, no built-in tools (--restricted, all tools disallowed), no MCP servers,
# one turn, no session persistence, run from an empty directory so no CLAUDE.md is discovered.
set -u
ROOT="$(cd "${1:?usage: run_fable.sh <experiment-dir> [parallel]}" && pwd)" || exit 2
PAR="${2:-6}"
command -v claude >/dev/null || { echo "claude not on PATH" >&2; exit 2; }
mkdir -p "$ROOT/work/fable" "$ROOT/work/fable-json" "$ROOT/work/empty" || exit 2
echo '{"mcpServers":{}}' > "$ROOT/work/empty-mcp.json"
SYS="You are a careful senior engineer. Answer the request in the message directly."

run_one() {
  local p="$1" cell out js
  cell=$(basename "$p" .txt); out="$ROOT/work/fable/$cell.txt"; js="$ROOT/work/fable-json/$cell.json"
  if [ -f "$out" ] && grep -q '^__ABLATION_DONE__ exit=0' "$out"; then return 0; fi
  ( cd "$ROOT/work/empty" && timeout 600 claude -p --no-session-persistence --model claude-fable-5-1 \
      --system-prompt "$SYS" --tools "" --restricted --disallowedTools "*" \
      --strict-mcp-config --mcp-config "$ROOT/work/empty-mcp.json" --max-turns 1 \
      --output-format json < "$p" > "$js.tmp" 2> "$js.err" )
  local st=$?
  if [ "$st" -eq 0 ] && python -c "import json,sys;d=json.load(open(sys.argv[1],encoding='utf-8'));sys.exit(1 if d.get('is_error') else 0)" "$js.tmp"; then
    mv -f "$js.tmp" "$js"
    python - "$js" "$out" <<'EOF'
import json, sys
d = json.load(open(sys.argv[1], encoding="utf-8"))
with open(sys.argv[2], "w", encoding="utf-8", newline="\n") as f:
    f.write(str(d.get("result", "")).rstrip() + "\n\n__ABLATION_DONE__ exit=0\n")
EOF
    rm -f "$js.err"
  else
    { cat "$js.tmp" 2>/dev/null; echo; echo "__ABLATION_DONE__ exit=${st:-1}"; } > "$out"
    echo "cell $cell failed (exit $st)" >&2
  fi
}
export -f run_one; export ROOT SYS
ls "$ROOT"/work/prompts/*.txt | xargs -P "$PAR" -I{} bash -c 'run_one "$@"' _ {}
done_count=$(grep -l '^__ABLATION_DONE__ exit=0' "$ROOT"/work/fable/*.txt 2>/dev/null | wc -l)
total=$(ls "$ROOT"/work/prompts/*.txt | wc -l)
echo "fable cells complete: $done_count / $total"
[ "$done_count" -eq "$total" ] || exit 3
