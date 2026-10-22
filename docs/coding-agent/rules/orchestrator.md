---
rule_schema_version: 2
suite_id: "rules-20260513-b80f05e"
rule_file: "orchestrator"
last_updated: "2026-10-22"
---

# Orchestrator Repository Rules

## Repo-Specific Orchestrator Policies

- Keep first-party skill procedures in `references/` when they are not always-on routing rules.
- For first-party skills, keep `SKILL.md` limited to trigger/scope boundaries, core runtime rules, and progressive-disclosure pointers; put design rationale, history, and maintenance decisions in ADRs or maintainer references.
- Preserve exact user-provided ADR consultation provenance unless the user explicitly asks to normalize it.
- Before adding validators for skill changes, distinguish objective package integrity from editable skill prose. Prefer Reviewer checks for wording, criteria quality, and prompt-bloat concerns unless a structural packaging contract is at risk.
- When adding package validation for enum/schema changes, check the exact enum owner or contract field rather than a broad substring.
- Use `rulebook` for full rule-suite bootstrap, schema migration, targeted refresh, and repair. Do not run full bootstrap as a per-task ritual.
- Propose a decision record only after the admission test in `durable-docs-authoring/references/adr.md` passes, present it for acceptance on its own, and never count plan approval or a merge as acceptance.
- Keep implementation-time artifacts (self-tests, fixtures, dry checks) out of `skills/`; every file there is one a session reads or runs at runtime, and a Reviewer packet for a skill change asks what runtime text invokes each added non-Markdown file.

## Repo-Specific Integration / Git Policy

- Shared-state Git mutations remain Orchestrator-controlled unless explicitly delegated.
- Prefer `feature/YYYY-MM-DD/<feature-name>` branch names in this repository unless the user requests another convention.
- If nested branch creation fails with `unable to create directory for .git/refs/heads/...`, verify there is no conflicting loose or packed ref, then rerun the Git branch/switch command with filesystem approval; do not change naming conventions or edit `.git` internals as a workaround.
- Stage only intended files when the worktree is mixed; never include unrelated untracked files silently.
- A change reaches the remote only after it has been reviewed, an open pull request included: commit locally, get the review, apply its findings, have the final delta re-reviewed until no finding is open, then push. Log the validator result and the review for each change in the plan (or the run's changes file) before the push.
- Merge only on the owner's word naming what is merged: his acceptance of a stack by name, as his own statement in this session or Counsel's quoted relay, covers each pull request in that stack; a pull request outside a stack is merged only on an instruction naming it. A conditional or standing authorization given for one never extends to another. The runtime's own merge permission is his to grant once in the session; no rule stands in for it.
- PR titles describe the change; plugin version numbers stay in the manifests and the PR body, never in the title.
