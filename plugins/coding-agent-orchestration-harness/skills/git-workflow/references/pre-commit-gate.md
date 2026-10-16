# Pre-Commit Gate

Use this checklist before any commit-affecting Git mutation.

1) Confirm authority
- If you are a subagent, verify the Orchestrator explicitly delegated the Git mutation.
- If shared-state mutation was not delegated, stop before running commit-affecting commands.

2) Verify the current branch
- Check the current branch with `git rev-parse --abbrev-ref HEAD`.
- If the branch is `main` or `develop`, stop and do not commit unless the user explicitly waives that gate.

3) Inspect the current change set
- Review `git status --short`.
- Review `git diff --stat` or a narrower diff for the exact paths involved.
- Confirm the intended commit contents map to one coherent intent.

4) Resolve mixed-intent changes before committing
- If the worktree contains multiple intents, split them into separate commits when that can be done safely.
- If the split would need hunk-level staging, do it non-interactively first: stage per file, or `git apply --cached` a prepared patch (`git add -p` is interactive and is not used); escalate only when no non-interactive split exists.
- If the split would require history editing or an interactive tool, stop and surface the split decision instead of forcing a commit.

5) Commit non-interactively
- Use an explicit commit message.
- Prefer command forms that do not open an editor.

6) Verify the result
- Review `git show --stat --oneline HEAD` or equivalent read-only confirmation.
- Confirm the worktree state afterward with `git status --short` when appropriate.

7) Before claiming the branch clean or opening a PR
- Verify `git status` AND a targeted `git diff` of the last-touched files; a clean-looking status alone is not proof after follow-up edits.
- Before every push, run a privacy sweep over every commit the push publishes, patch and message alike (`git log -p @{u}..HEAD`; every commit on the branch when it has no upstream), not over the net diff: a line added in one unpushed commit and removed in a later one is still published. Match case-insensitively for machine-specific paths and names: home-directory paths in any form (`C:\Users\`, the escaped `C:\\Users\\`, `C:/Users/`, `/c/Users/`, `/Users/<name>/`, `/home/<name>/`, `%USERPROFILE%`, `%APPDATA%`, `%LOCALAPPDATA%`), the local account name itself (`$USER` or `$USERNAME`) wherever it appears, in a path or alone, and the machine's host name (`hostname` or `$COMPUTERNAME`). Quoted material is not exempt: a hit inside a quoted command, log line or statement is redacted before the push. Replace hits in the working tree with repo-relative or environment-agnostic forms. A hit in a commit message or in an earlier unpushed commit can be removed only by rewriting history: stop and escalate before the push. A hit already on the remote is outside the sweep; report it if seen, and do not rewrite it.

Notes:
- This checklist does not define branch naming conventions beyond the branch gate in step 2.
- Repo-specific branch or release policy belongs in repo rules, not here.
