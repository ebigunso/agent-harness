# Integration Checklist

Run this checklist after each Worker wave and before Reviewer dispatch.

## 1. Parse Worker Reports

- Collect every Worker final YAML report from the wave.
- Confirm each report maps to exactly one assigned Task_X.
- Record status: `done`, `blocked`, or `failed`.

## 2. Validate Report Contracts

- Validate each report against `subagent-report-contract`.
- Treat malformed reports as blockers.
- Request a corrected report or dispatch follow-up work before review.

## 3. Reconcile Changed Files

- Compare `files_changed` against each task's `owns`.
- Accept files outside `owns` only when minimal and explicitly explained.
- Record unexplained cross-owns edits as blockers.

## 4. Confirm Worker-Owned Validation

- Every required Worker-owned validation item must be `pass` or explicitly waived.
- `skipped` is not a waiver.
- Missing evidence blocks progression.

## 5. Collect Blockers And Questions

- Aggregate `blockers`.
- Aggregate `questions_for_orchestrator`.
- Decide whether the Orchestrator can answer, the user must answer, or a follow-up Worker is needed.

## 6. Collect Rule And Lesson Candidates

- Aggregate `rule_candidates`.
- Aggregate `lesson_candidates`.
- Normalize duplicates before rulebook or lessons updates.

## 7. Update Progress Log

Append a plan Progress Log entry with:

- wave completed;
- Worker task statuses;
- files changed;
- validation evidence;
- blockers/questions;
- follow-up decision.

## 8. Decide Next Dispatch

Dispatch follow-up Workers when:

- required Worker validation is missing;
- implementation blockers remain;
- Reviewer would lack required context;
- acceptance is not yet satisfied.

Dispatch Reviewer when:

- tasks in scope are done or waived;
- Worker-owned required validation is pass or waived;
- blockers are resolved or explicitly carried as review risks.

## 9. Prepare Reviewer Packet

Use `reviewer-packet-template.md` to prepare concise Reviewer context.
