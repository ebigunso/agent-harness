# Readings: A middle size for a small change

Written by the Orchestrator for the value audit to compare after its grades are fixed. Not read by an auditor before grading.

## Readings

### `middle-size-for-a-small-change-plan.md`, plan draft

Item | reading | statement relied on

- DoD 1: a third size; no plan, plan review or plan-draft audit; the review and one closing audit kept; the audit holds what went beyond his statement | covered | brief: "A small change that comes from his word keeps two checks: the review of the change, and one closing value audit, which checks that what was built is what he said and nothing more."; "It drops the separate plan, the plan's review and the plan-draft audit."
- DoD 2: smallness is the Orchestrator's call, guarded by the closing audit | covered | brief: "Whether a change is small is the Orchestrator's call. The guard on that call is the closing audit"
- DoD 3: on top of the last branch, no pull request of its own, while the stack is unmerged | covered | brief: "While the stack it belongs to is unmerged, it takes no branch and no pull request of its own; it goes on top of the last one."
- DoD 4: trivial and full-size work unchanged | covered | brief: "Trivial work and work of full size are handled as they are today."
- DoD 5: the accepted records revised and each accepted by name before text is built on it | covered | brief: "the accepted record that states it returns to him for acceptance by name"; pass condition "the record that states the Plan Gate is accepted by him by name before the change lands"
- DoD 6: the fixed template byte-identical | covered as mechanics; no statement needed
- DoD 7: validators, smoke tests, Reviewer APPROVED | covered | brief: "the package validators pass"
- DoD 8: the run closes with publication, pull request, note to Counsel, nothing merged | covered as mechanics; the standing approval covers publication
- Planner-added: a short record file for a small change, named after `Plan:` in the template | extends | brief: "one closing value audit"; "For a change this small his statement in the brief is the plan." The file logs and plans nothing.
- Planner-added: the middle size only under a governing brief, for a change stated in it | extends | brief: "his statement in the brief is the plan"; "A small change that comes from his word"
- Non-goals: trivial work, full size, goal mode, the two sources and the conditions for a plan, templates | covered | brief: "Trivial work and work of full size are handled as they are today."
- Non-goals: a rule on test artifacts; the full suite on small changes | covered | brief, Left out on purpose
- Non-goal: no version bump | covered as mechanics; no statement needed
- Design: a third unit; the accepted records revised in place to carry it and returned by name | covered | brief: "the accepted record that states it returns to him for acceptance by name"
- Design: nothing published or reported before the closing audit holds nothing | extends | brief: "The guard on that call is the closing audit: where the change went beyond his statement, the audit holds it."
- A1: his word arrives as a statement Counsel writes into a governing brief | extends | brief: "his statement in the brief is the plan"
- A2: after the stack merges a small change takes a branch and pull request as usual | extends | brief: "While the stack it belongs to is unmerged"
- A3: what the brief does not drop stays (Worker builds, note to Counsel, candidate ready, nothing remote before review and audit) | extends | brief: "keeps two checks"; "he is told when it is done"
- Task_1, Task_2, Task_3 | covered, as the Definition of Done items they carry
- Decision Log: the accepted records are revised, not a new record added; adapters owned | covered for the first, mechanics for the second | as the first Design line
- Scenario, the Orchestrator's expectation only: 1 not yet at plan draft.

#### The audit's comparison, plan draft (2026-10-06), as returned

Reading compared:
- DoD 1, 2, 3, 4, 5, 7: agrees.
- DoD 6: diverges. Orchestrator: covered as mechanics, no statement needed. Audit: inferred, user-facing.
- DoD 8: diverges in basis. Orchestrator: covered as mechanics, with the standing approval for publication. Audit: cited on the standing approval; outward-facing, not mechanics.
- Planner-added 1 and 2: agrees (extends / inferred). The audit adds `direction` to both.
- Non-goals trivial work, full size, conditions for a plan: agrees.
- Non-goals goal mode, the two sources, templates: diverges. Orchestrator: covered. Audit: inferred.
- Non-goals test artifacts, full suite: agrees.
- Non-goal version bump: diverges. Orchestrator: covered as mechanics. Audit: inferred.
- A1: agrees. The audit adds `direction`.
- A2: agrees.
- A3: diverges. Orchestrator: extends. Audit: cited.
- Task_1, Task_2, Task_3: agrees.
- Decision Log 1: agrees. Decision Log 2: agrees (mechanics / not audited).
- The Orchestrator's two Design readings: the audit graded no Design item, because the mandate's item list does not include the Design section.

Findings compared: none found (the readings file records "None yet"; no departure from a means was noted, and the brief marks no means).

Readings corrected after this comparison: the template kept fixed, goal mode, the two sources and the version bump are extensions of the brief's statements and not mechanics or covered; publication is outward-facing and rests on the standing approval; A3 is what the brief's core scenario states.

## Findings

- None yet.
