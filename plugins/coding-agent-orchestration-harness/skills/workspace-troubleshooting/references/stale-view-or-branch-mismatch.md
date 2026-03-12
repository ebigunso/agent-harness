# Triage: “Missing change” / branch mismatch / stale view

## Minimal reconciliation steps
1) git rev-parse --abbrev-ref HEAD
2) re-read file(s) from workspace (not memory/cached)
3) git status --porcelain
4) git diff --name-only

If mismatch persists:
- state branch
- provide evidence (excerpt/diff summary)
- ask up to 3 reconciliation questions
