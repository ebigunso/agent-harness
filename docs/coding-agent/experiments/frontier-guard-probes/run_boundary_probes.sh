#!/usr/bin/env bash
# Plan Gate boundary probes (Task_4 of plan-gate-waiver-boundary-plan.md): two ephemeral headless Codex cells
# under the harness-on control, each in its own disposable clone, with worktree containment evidence.
# Usage: bash run_boundary_probes.sh <repo-root> <revision> <scratch-root>
#   repo-root    the authoritative checkout (its `git worktree list` names every worktree to contain)
#   revision     the commit whose skill text is under test; the clone is checked out here and the skill copied from it
#   scratch-root a directory outside every worktree; clones and manifests are written under it
# Per cell: clone at <revision>, copy the branch skills to .agents/skills/ and the loader snippet to AGENTS.md,
# manifest (path + SHA-256 of every file outside .git/) every authoritative worktree, run one codex exec session
# with the cell prompt on stdin, manifest again, and record the clone's status, diff, and created files.
# Moves $CODEX_HOME/AGENTS.md aside for the run window and restores it with a hash check (run_baseline.sh discipline).
# Outputs: live-loader/boundary/{transcript,clone-status,clone-diff,clone-created,containment,skill}-<cell>.txt;
# manifests under <scratch-root>/manifests/. Exit: 0 ran; 2 setup refused; 3 a cell failed or containment differs; 4 restore failed.
set -u
ROOT="$(cd "${1:?usage: run_boundary_probes.sh <repo-root> <revision> <scratch-root>}" && pwd)" || exit 2
REV="${2:?revision required}"; SCRATCH="${3:?scratch-root required}"
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"; OUT="$HERE/live-loader/boundary"
PLUGIN="plugins/coding-agent-orchestration-harness"
CODEX_DIR="${CODEX_HOME:-$HOME/.codex}"; LOADER="$CODEX_DIR/AGENTS.md"; BACKUP="$CODEX_DIR/AGENTS.md.boundary-aside"
hash_file() { sha256sum "$1" | cut -c1-64; }

# Prerequisites (no mutation yet).
[ -e "$BACKUP" ] && { echo "refusing: $BACKUP exists" >&2; exit 2; }
for t in codex timeout sha256sum git; do command -v "$t" >/dev/null || { echo "$t not on PATH" >&2; exit 2; }; done
git -C "$ROOT" rev-parse --verify -q "$REV^{commit}" >/dev/null || { echo "unknown revision $REV" >&2; exit 2; }
[ -f "$OUT/prompt-A.txt" ] && [ -f "$OUT/prompt-B.txt" ] || { echo "missing $OUT/prompt-{A,B}.txt" >&2; exit 2; }
mkdir -p "$SCRATCH/manifests" || exit 2
SCRATCH="$(cd "$SCRATCH" && pwd)"
mapfile -t WORKTREES < <(git -C "$ROOT" worktree list --porcelain | sed -n 's/^worktree //p')
for w in "${WORKTREES[@]}"; do case "$SCRATCH/" in "$w"/*) echo "scratch root $SCRATCH is inside worktree $w" >&2; exit 2;; esac; done
echo "authoritative worktrees: ${WORKTREES[*]}"

manifest() { # $1 dir, $2 out; the runner's own evidence files under live-loader/boundary/ are excluded so they do not read as a containment breach
  ( cd "$1" && find . -path ./.git -prune -o -type f -print0 | LC_ALL=C sort -z | xargs -0 sha256sum | grep -v 'frontier-guard-probes/live-loader/boundary/' ) > "$2" 2>/dev/null
}
manifest_all() { # $1 tag
  local i=0
  for w in "${WORKTREES[@]}"; do manifest "$w" "$SCRATCH/manifests/wt$i-$1.txt"; i=$((i+1)); done
}

before=""; [ -f "$LOADER" ] && before=$(hash_file "$LOADER")
moved=0; rc=0
restore() { [ "$moved" -eq 1 ] || return 0; mv -f "$BACKUP" "$LOADER" || { echo "RESTORE FAILED" >&2; rc=4; return; }
  after=$(hash_file "$LOADER"); if [ "$after" = "$before" ]; then echo "AGENTS.md restored (sha256 match)"; else echo "RESTORE HASH MISMATCH" >&2; rc=4; fi; moved=0; }
on_exit() { st=$?; restore; [ "$rc" -eq 4 ] && exit 4; [ "$st" -ne 0 ] && exit "$st"; exit "$rc"; }
trap on_exit EXIT; trap 'exit 130' INT; trap 'exit 143' TERM
if [ -f "$LOADER" ]; then mv "$LOADER" "$BACKUP" || exit 2; moved=1; echo "AGENTS.md moved aside (sha256 $before)"; fi

for CELL in A B; do
  C="$SCRATCH/clone-$CELL"; rm -rf "$C"
  git clone -q --no-hardlinks "$ROOT" "$C" && git -C "$C" checkout -q --detach "$REV" || { echo "clone failed for $CELL" >&2; rc=3; continue; }
  [ -z "$(git -C "$C" status --porcelain)" ] || { echo "clone $CELL not clean after checkout" >&2; rc=3; continue; }
  mkdir -p "$C/.agents" && cp -r "$C/$PLUGIN/skills" "$C/.agents/skills" && cp "$C/$PLUGIN/codex/snippets/AGENTS.md" "$C/AGENTS.md" || { echo "control setup failed for $CELL" >&2; rc=3; continue; }
  SKILL="$C/.agents/skills/orchestration-harness/SKILL.md"
  { echo "cell: $CELL"; echo "clone: $C"; echo "head: $(git -C "$C" rev-parse HEAD)"; echo "revision_under_test: $(git -C "$ROOT" rev-parse "$REV")"
    echo "skill_path: $SKILL"; echo "skill_sha256: $(hash_file "$SKILL")"
    echo "skill_sha256_at_revision_lf: $(git -C "$ROOT" show "$REV:$PLUGIN/skills/orchestration-harness/SKILL.md" | sha256sum | cut -c1-64)"
    echo "setup_files: AGENTS.md .agents/skills/**"; } > "$OUT/skill-$CELL.txt"
  manifest_all "before-$CELL"
  ( cd "$C" && timeout 1500 codex exec --ephemeral --disable plugins --disable hooks -c 'web_search="disabled"' -s workspace-write - < "$OUT/prompt-$CELL.txt" > "$OUT/transcript-$CELL.txt" 2>&1 )
  st=$?; echo "cell $CELL codex exit $st" | tee -a "$OUT/skill-$CELL.txt"
  manifest_all "after-$CELL"
  git -C "$C" status --porcelain --untracked-files=all > "$OUT/clone-status-$CELL.txt"
  git -C "$C" diff > "$OUT/clone-diff-$CELL.txt"
  git -C "$C" status --porcelain --untracked-files=all | sed -n 's/^?? //p' | grep -v -e '^AGENTS.md$' -e '^.agents/' > "$OUT/clone-created-$CELL.txt"
  : > "$OUT/containment-$CELL.txt"; i=0
  for w in "${WORKTREES[@]}"; do
    if cmp -s "$SCRATCH/manifests/wt$i-before-$CELL.txt" "$SCRATCH/manifests/wt$i-after-$CELL.txt"; then echo "$w: IDENTICAL" >> "$OUT/containment-$CELL.txt"
    else echo "$w: DIFFERS" >> "$OUT/containment-$CELL.txt"; diff "$SCRATCH/manifests/wt$i-before-$CELL.txt" "$SCRATCH/manifests/wt$i-after-$CELL.txt" >> "$OUT/containment-$CELL.txt"; rc=3; fi
    i=$((i+1))
  done
  h=$(sed -n 's/^skill_sha256: //p' "$OUT/skill-$CELL.txt")
  if grep -qi "$h" "$OUT/transcript-$CELL.txt"; then echo "skill hash quoted in transcript: yes" >> "$OUT/skill-$CELL.txt"; else echo "skill hash quoted in transcript: NO" >> "$OUT/skill-$CELL.txt"; fi
  [ "$st" -eq 0 ] && [ -s "$OUT/transcript-$CELL.txt" ] || rc=3
  cat "$OUT/containment-$CELL.txt"
done
exit $rc
