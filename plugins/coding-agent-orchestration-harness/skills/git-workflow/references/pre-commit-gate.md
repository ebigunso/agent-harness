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
- Before every push, run the bundled `scripts/privacy-sweep.sh` from the repository being pushed: `bash "<git-workflow>/scripts/privacy-sweep.sh" "origin" "<branch>"`, replacing the quoted placeholders with the skill directory and reviewed local branch. It requires Bash 4+, Git and coreutils; omitted arguments select `origin` and the current branch. It reads the destination's live push-URL refs and local objects, excluding history already reachable there, without relying on an upstream. Unpublished stack ancestors, full commit messages, author and committer identities, added lines in every commit, both rename paths and diffs against every merge parent are checked. A later deletion does not remove an earlier outgoing hit. An unavailable destination branch tip, shallow history or an unreadable destination stops the sweep; obtain the required history separately and rerun. Other advertised refs whose objects are unavailable locally produce a `NOTE` and are omitted from exclusions, which can only widen the scan. The helper writes only temporary scratch files and installs no hook.
  - Review each `CANDIDATE` by commit, path and line; record justified false positives. Matching uses runtime home/profile/app-data paths, both account variables when set, and observed host names and aliases. Valid UTF-8, including emoji and non-ASCII punctuation, is scanned as text. Non-ASCII identities match literally; case-folding and escape normalization are ASCII-only. Slash variants, drive mounts, ASCII JSON/C escapes and percent encoding are normalized; bare names use token boundaries. Empty identities and literal portable placeholders such as `%USERPROFILE%`, `%APPDATA%`, `%LOCALAPPDATA%` and `<name>` are not hits. Quoted commands, logs and statements receive the same check. `INSPECT` means incomplete or unsearchable content, not clean; binary/control bytes, invalid UTF-8, submodules and Git LFS content require separate inspection. Non-ASCII escapes, Base64, compressed/encrypted payloads, other encodings and unobserved machine identities are outside automatic matching and need separate inspection when present. Exit 0 (`CLEAN`) covers only the stated identities and supported forms; candidates or inspection items exit non-zero.
  - Replace a confirmed working-tree hit with a repo-relative or environment-agnostic form **before creating the affected commit**. A confirmed hit in **any outgoing commit, including HEAD**, requires an authorized amend or rewrite and a rescan: stop and escalate before pushing. Report a hit already on the remote if observed; do not rewrite published history for this sweep.
  - Push only the reviewed tip to the reviewed same-named branch on that destination, with no additional refs, tags, notes, mirror or submodule pushes. For `origin`, after review, the explicit form is `git -c "remote.origin.mirror=false" push --no-follow-tags --recurse-submodules=no "origin" "<reviewed-tip>:refs/heads/<branch>"`. Substitute the `tip` from the sweep and the branch; adapt the remote name in both places for another destination. These quoted command forms parse in Bash and PowerShell. Re-run the sweep if the tip or destination changes; stacked submissions that publish multiple branches require each branch to be swept and reviewed before submission.

Notes:
- This checklist does not define branch naming conventions beyond the branch gate in step 2.
- Repo-specific branch or release policy belongs in repo rules, not here.
