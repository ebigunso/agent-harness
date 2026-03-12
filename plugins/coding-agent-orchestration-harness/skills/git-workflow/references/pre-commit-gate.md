# Pre-Commit Gate

Use this checklist before any commit-affecting Git mutation.

1) Confirm authority
- If you are a subagent, verify the Orchestrator explicitly delegated the Git mutation.
- If shared-state mutation was not delegated, stop before running commit-affecting commands.

2) Verify the current branch
- Check the current branch with `git rev-parse --abbrev-ref HEAD`.
- If the current branch is `main`, stop and do not commit unless the user explicitly waived the branch gate.

3) Inspect the current change set
- Review `git status --short`.
- Review `git diff --stat` or a narrower diff for the exact paths involved.
- Confirm the intended commit contents map to one coherent intent.

4) Resolve mixed-intent changes before committing
- If the worktree contains multiple intents, split them into separate commits when that can be done safely.
- If safe separation is not practical without interactive or risky manipulation, stop and surface the split decision instead of forcing a commit.

5) Commit non-interactively
- Use an explicit commit message.
- Prefer command forms that do not open an editor.

6) Verify the result
- Review `git show --stat --oneline HEAD` or equivalent read-only confirmation.
- Confirm the worktree state afterward with `git status --short` when appropriate.

Notes:
- This checklist does not define branch naming conventions beyond the `main` safety gate.
- Repo-specific branch or release policy belongs in repo rules, not here.
