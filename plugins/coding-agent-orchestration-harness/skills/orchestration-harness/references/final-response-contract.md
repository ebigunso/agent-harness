# Final Response Contract

Use this structure for user-facing closeout after harness work.

1. Outcome: `done` or `blocked`, per `SKILL.md` Validation Gate; `candidate ready` in place of `done` when a run under a brief is reported ready (below).
2. Changed files/artifacts: only those from the completed work.
3. Validation summary: each required check as `pass`, `fail`, `skipped` with reason, or `waived` with evidence; name checks that could not run.
4. Review summary: Reviewer status (`APPROVED`, `NEEDS_REVISION`, `FAILED`, or waived with evidence) for non-trivial work; flows, viewports, and artifact paths when UI/E2E evidence was run.
5. Repo rule updates, or none.
6. Skill staging updates, or none.
7. ADRs proposed, with acceptance state, or none; then each ADR whose wording changed after acceptance, one line each (the record and what changed), asking nothing — `durable-docs-authoring/references/adr.md`.
8. Questions or blockers, max 3; omit when none.

Prefer short paragraphs; use lists only for parallel items.

## Under a brief

When a run under a brief is reported ready (`references/completion-closeout.md`), after its last unit has closed or after a change the owner directed while it was open, with its required work and validation complete, the outcome is `candidate ready`, in exactly those two words, and the response is written for the owner's judgement of the result. After the outcome it leads with behaviour, then lists the rest in this order:

- Behaviour: what the product now does, one scenario of the brief at a time, each with its state from the run record (`not yet`, `demonstrated`, `ready for the owner's judgement`) and how to observe it, in terms the owner can judge without a plan, a diff or code; then the scenarios the run added, as the run's own reading of the design. A scenario only the owner can judge is `ready for the owner's judgement`, never met. Scenarios are evidence of the experience, not its definition: the response does not claim the design delivered because every scenario is demonstrated. Implementation detail is neither the default nor prohibited: give it only where the owner's judgement needs it, and state that reason with it.
- Evidence for each agent-checkable pass condition of the brief.
- Each human-only pass condition, as pending. A proxy such as a passing test or a metric never stands in for one.
- Each small change of the run built without a plan, named as the owner stated it, with `no plan` said plainly.
- The items marked `direction` by the closeout audit of each unit of the run: the judgement calls in the run's records (choices Workers reported, rulings the Orchestrator made) and the items graded `inferred`. Those and no others, each as the verdict states it, with its grade or record value and whatever statements the verdict names for it (a `not audited` call has none, and none is invented), and with no account added of why it was made; an item the verdict did not mark is not listed, and the Orchestrator selects none. Flag each that rests on a provisional statement. The rest stay in the plan's records, or a small change's section of the run's changes file, and are not listed; say where that full list is. This selection covers questions of judgement only: irreversible or outward-facing actions, merges, decision records, changes to either philosophy and standing approvals still come to the owner.
- The design document updated when the run is reported ready, or that the repository keeps none for the field.
- What was learned that the philosophies do not account for, or none.

Items 2 to 8 above follow that list where they are needed; decision records proposed, and those reworded after acceptance, are always listed. A run without a brief uses items 1 to 8 as they stand. When such a run was audited (value-level operation on through a philosophy alone), it keeps `done` or `blocked` and lists after item 7 the items the value audit marked `direction`, as above.
