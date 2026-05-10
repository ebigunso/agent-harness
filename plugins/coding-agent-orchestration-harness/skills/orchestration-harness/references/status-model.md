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

## Worker report validation result statuses

- `pass`
- `fail`
- `skipped`

Worker YAML reports use only these values for `validation_results[*].status`.
When a required Worker-owned validation is explicitly waived rather than run,
the Worker report records `status: skipped` plus waiver evidence in `evidence`.

## Plan and closeout validation states

- `pass`
- `fail`
- `skipped`
- `waived`

`waived` is an Orchestrator plan/closeout state, not a Worker report status.

## Plan statuses

- `draft`
- `approved`
- `in_progress`
- `done`

## Mappings And Rules

- Worker `done` means the assigned Task_X report completed successfully; it does not imply the plan is done.
- Reviewer `APPROVED` is required for non-trivial completion unless explicitly waived by the Orchestrator or user.
- `skipped` is not the same as `waived`.
- A required validation that was not run can be treated as `waived` in plan/closeout state only when explicit waiver evidence exists.
- In Worker YAML, that same situation is represented as `status: skipped` plus waiver evidence.
- Missing required evidence blocks final completion.
- A plan can be `done` only after all tasks are done or waived, required validation is pass or waived, blockers are resolved, and required Reviewer status is `APPROVED` or explicitly waived.
