# Stacked PRs

Read this reference when a PR will be based on an unmerged feature branch, or the work will land as more than one dependent PR.

- GitHub stacks are managed by the `gh stack` extension (`github/gh-stack`), not core gh. Check `gh extension list` for the extension and `gh api repos/<owner>/<repo>/stacks` for repository support (a list, not 404). Ask the user before `gh extension install github/gh-stack`. If either check fails or the user declines, ask the user how to proceed; do not fall back silently.
- Read `gh stack --help` and `gh stack <cmd> --help` before first use, and pick each command's non-interactive form from its help.
- Traps that are unsafe to discover by trial:
  - `gh stack submit --auto` creates drafts; add `--open` or mark each PR ready before arming review monitoring.
  - `gh stack link` creates no local tracking; run `gh stack checkout <member-pr>` before local stack commands.
  - Argument-less `gh stack merge` in a non-interactive terminal merges the whole stack without prompting. Never run it without explicit user authorization, and when authorized always name a target, `--yes`, and a merge method.
  - `gh stack modify` and `gh stack switch` are interactive-only; `gh stack sync` aborts on divergence when unattended, so prefer `gh stack rebase` then `gh stack push`.
- Stack mutations stay Orchestrator-controlled per core rule 3; run `gh stack unstack` only on explicit user request.
- Review loop: arm monitoring with any member PR; the watcher covers the whole stack. See `pr-review-monitoring.md`.
