# Safe Git Defaults

This reference keeps Git workflow defaults explicit and reusable across repositories.

## Preferred defaults

- Inspect before mutating: prefer `git status`, `git diff`, `git log`, and `git show` before commit-affecting commands.
- Prefer non-interactive commands: use explicit flags and messages instead of opening editors or interactive consoles.
- Prefer deterministic scope: operate on explicit paths or clearly bounded commands rather than broad mutations.
- Prefer reversible decisions: stop and ask before taking a risky shortcut.

## Defaults to avoid unless explicitly approved

- destructive resets
- checkout-style file reverts
- aggressive clean operations
- history rewrites that were not explicitly requested
- branch changes or commits performed by a subagent without explicit delegation

## Boundary notes

- This reference is procedural, not a repository branch-policy document.
- Repo-specific naming, protection, merge, or release rules belong elsewhere.
- Failure recovery belongs in `workspace-troubleshooting`.
