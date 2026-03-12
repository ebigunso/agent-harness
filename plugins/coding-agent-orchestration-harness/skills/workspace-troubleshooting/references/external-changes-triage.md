# Triage: External changes detected (formatter/user/tool edits)

## Default policy
Treat external changes as EXPECTED by default.

Proceed unless:
1) changes conflict with the current task objective, OR
2) changes materially change behavior/risk, OR
3) changes expand scope into unrelated modules.

## Minimal triage steps
- git diff --name-only
- git diff (or limit to affected paths)

If you must pause:
- 1–3 bullets describing the conflict
- recommended default action
- up to 3 questions
