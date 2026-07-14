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

## Destructive operations on shared mutable resources

- Freeze the target list first: enumerate the targets once, freeze that list, and act only on the frozen list — never pipe a fresh listing into a destructive loop.
- If a safety property was announced to peers (e.g. "only pre-snapshot items will be deleted"), verify the implementation actually enforces it before running.

## Boundary notes

- This reference is procedural, not a repository branch-policy document.
- Repo-specific naming, protection, merge, or release rules belong elsewhere.
- Failure recovery belongs in `workspace-troubleshooting`.
