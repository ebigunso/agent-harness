# Logical Commit Chunking

Use this checklist when deciding how to group changes into commits.

## Standard

A commit should represent one coherent intent unless the user explicitly asks for a different grouping.

Examples of coherent intent:
- one bug fix
- one refactor with no behavior change
- one documentation-only update
- one test addition that belongs to a specific code change

Signals that a change set should be split:
- behavior changes and refactors are mixed together
- unrelated files changed for different reasons
- broad formatting churn obscures the real functional change
- follow-up fixes are included with the original change instead of being isolated

## Decision checklist

1) Name the intent in one sentence.
- If you cannot summarize the change cleanly, the commit boundary is probably too broad.

2) Check whether every staged path supports that same intent.
- Remove or defer files that do not belong to that sentence.

3) Separate tests and docs based on coupling.
- Keep tests or docs with the code change when they directly validate or describe that same intent.
- Split them when they represent distinct follow-up work.

4) Avoid interactive-by-default separation.
- Prefer explicit path-based staging and clear commit boundaries.
- If only hunk-level interactive staging would make the split possible, escalate instead of defaulting to an interactive flow.

5) Write a commit message that matches the intent.
- Keep it concise and specific.
- Describe the change itself, not the entire session.

## Commit hygiene reminders

- Do not use placeholder messages.
- Do not bundle cleanup that happened "while you were there" unless it is required for the same change.
- Do not create a catch-all commit just because multiple edits are already present.
