# Final Response Contract

Use this structure for user-facing closeout after harness work.

1. Outcome: `done` or `blocked`, per `SKILL.md` Validation Gate; `candidate ready` in place of `done` for a run under a brief (below).
2. Changed files/artifacts: only those from the completed work.
3. Validation summary: each required check as `pass`, `fail`, `skipped` with reason, or `waived` with evidence; name checks that could not run.
4. Review summary: Reviewer status (`APPROVED`, `NEEDS_REVISION`, `FAILED`, or waived with evidence) for non-trivial work; flows, viewports, and artifact paths when UI/E2E evidence was run.
5. Repo rule updates, or none.
6. Skill staging updates, or none.
7. ADRs proposed, with acceptance state, or none — `durable-docs-authoring/references/adr.md`.
8. Questions or blockers, max 3; omit when none.

Prefer short paragraphs; use lists only for parallel items.

## Under a brief

When a brief governs the run (`references/value-level-operation.md`) and its required work and validation are complete, the outcome is `candidate ready`, in exactly those two words, and the response is written for the owner's judgement of the result. After the outcome it leads with behaviour, then lists the rest in this order:

- Behaviour: what the product now does, in terms the owner can judge without a plan, a diff or code. Implementation detail is neither the default nor prohibited: give it only where the owner's judgement needs it, and state that reason with it.
- Evidence for each agent-checkable pass condition of the brief.
- Each human-only pass condition, as pending. A proxy such as a passing test or a metric never stands in for one.
- The judgement calls (choices Workers reported, rulings the Orchestrator made) that bear on the product's direction: each one that is a decision at the level of the product philosophy or the engineering philosophy. And the items the value audit graded `inferred` and marked `direction`: those and no others, each as the verdict states it, with its grade and the statements it extends, and with no account added of why it was made; an `inferred` item the verdict did not mark is not listed. Flag each that rests on a provisional statement. The rest stay in the plan's records and are not listed; say where that full list is. This selection covers questions of judgement only: irreversible or outward-facing actions, merges, decision records, changes to either philosophy and standing approvals still come to the owner.
- What was learned that the philosophies do not account for, or none.

Items 2 to 8 above follow that list where they are needed; decision records proposed are always listed. A run without a brief uses items 1 to 8 as they stand. When such a run was audited (value-level operation on through a philosophy alone), it keeps `done` or `blocked` and lists after item 7 the items the value audit graded `inferred` and marked `direction`, as above.
