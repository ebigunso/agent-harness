# Status Model

Use this vocabulary when writing plans, Worker reports, Reviewer outputs, validation summaries, and closeout decisions.

## Worker report statuses

- `done`
- `blocked`
- `failed`

## Reviewer statuses

- `APPROVED`
- `NEEDS_REVISION`
- `FAILED`

## Validation statuses

- `pass`
- `fail`
- `skipped`
- `waived`

## Plan statuses

- `draft`
- `approved`
- `in_progress`
- `done`

## Mappings And Rules

- Worker `done` means the assigned Task_X report completed successfully; it does not imply the plan is done.
- Reviewer `APPROVED` is required for non-trivial completion unless explicitly waived by the Orchestrator or user.
- `skipped` is not the same as `waived`.
- Required validation may be skipped only with explicit waiver evidence.
- Missing required evidence blocks final completion.
- A plan can be `done` only after all tasks are done or waived, required validation is pass or waived, blockers are resolved, and required review is approved or waived.
