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
- Collect design alerts: entries in either list stating what is worked around, the cleaner alternative, and the cost delta (per `subagent-report-contract`).
- When any aggregated item requests or implies a contract-shape or design ruling, you MUST read and apply `skills/orchestration-harness/references/lifecycle-gates.md#escalation-ruling` before answering it or dispatching further work.
- Decide whether the Orchestrator can answer, the user must answer, or a follow-up Worker is needed.

## 6. Collect Rule, Lesson, and Harness Migration Candidates

- Aggregate `rule_candidates`.
- Aggregate `lesson_candidates`.
- Aggregate `harness_migration_candidates`.
- Normalize duplicates before rulebook, lessons, or skill-candidate staging updates.
- Route `harness_migration_candidates` to `docs/coding-agent/skill-candidates.md` or `docs/coding-agent/skill-drafts/*.md` through Orchestrator curation.

## 7. Update Progress Log

Append a plan Progress Log entry with:

- wave completed;
- Worker task statuses;
- files changed;
- validation evidence;
- blockers/questions;
- follow-up decision.

## 8. Decide Next Dispatch

Third-bounce detector: if a follow-up dispatch would be the third attempt to fix the same seam, stop and apply the value-audit appendix in `skills/engineering-quality-baselines/references/long-horizon-audit.md` before dispatching again.

Dispatch follow-up Workers when:

- required Worker validation is missing;
- implementation blockers remain;
- Reviewer would lack required context;
- acceptance is not yet satisfied.

Dispatch Reviewer when:

- tasks in scope are done or waived;
- Worker-owned required validation is pass or waived;
- blockers are resolved or explicitly carried as review risks.

Low-risk internal delta re-review: when a follow-up wave changed only files already reviewed, introducing no new contracts, boundaries, or validation surfaces, the Reviewer re-dispatch may scope to the delta diff instead of the full wave.

## 9. Prepare Reviewer Packet

Use `reviewer-packet-template.md` to prepare concise Reviewer context.
