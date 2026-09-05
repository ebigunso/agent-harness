# Stacked PRs

Read this reference when a PR will be based on an unmerged feature branch, or the work will land as more than one dependent PR.

- GitHub stacks are managed by the `gh stack` extension (`github/gh-stack`), not core gh. Check `gh extension list` for the extension and `gh api repos/<owner>/<repo>/stacks` for repository support (a list, not 404). Ask the user before `gh extension install github/gh-stack`. If either check fails or the user declines, ask the user how to proceed; do not fall back silently.
- Read `gh stack --help` and `gh stack <cmd> --help` before first use, and pick each command's non-interactive form from its help.
- Traps that are unsafe to discover by trial:
  - `submit --auto` creates drafts; add `--open` or mark each PR ready before arming review monitoring.
  - `link` creates no local tracking; run `checkout <member-pr>` before local stack commands.
  - Argument-less `merge` in a non-interactive terminal merges the whole stack without prompting. Merge waits for user authorization and always names a target, `--yes`, and a merge method.
  - `modify` and `switch` are interactive-only; `sync` aborts on divergence when unattended, so prefer `rebase` then `push`.
- Stack mutations stay Orchestrator-controlled per core rule 3; run `unstack` only on explicit user request.
- Review loop: arm monitoring with any member PR; the watcher covers the whole stack. See `pr-review-monitoring.md`.
