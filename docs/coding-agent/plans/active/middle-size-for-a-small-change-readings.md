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

### `middle-size-for-a-small-change-plan.md`, closeout

Item | reading | statement relied on

- Every item read under the plan-draft heading keeps its reading as corrected after that comparison, with these changes and additions.
- DoD 1 as reworded: a small change may be built without a plan, the Orchestrator choosing per change, a plan right for more than one task or an open choice of how; review and one closing audit kept; the audit holds what went beyond the statement | covered | brief, The middle size, second statement (amendment 2026-10-06) and first statement
- DoD 4 as reworded: trivial unchanged, its definition unchanged | covered | brief: "the definition of trivial work does not change"
- DoD 5 as reworded: ADR-D-0055 proposed and accepted by name; ADR-D-0040 and ADR-D-0051 revised and accepted by name; ADR-D-0041 pointing only | covered | brief, Limits: "the accepted record that states it returns to him for acceptance by name"; his acceptance 2026-10-06
- Planner-added 1 as reworded: the small change logged in the run record, no file of its own | covered | brief, A small change and the run: the change belongs to the run; "no plan document"
- The text as built: a run is one or more units; reported ready after the last unit and again after each directed change; stays open on its stack; closes once on his acceptance; a small change against an accepted-and-merged brief starts a run of its own under a brief Counsel hands over | covered | brief, A small change and the run; his words "Yes, that reading is right."; the hand-over mechanics are the existing ones
- The text as built: the closing audit for a small change grades the change against the statement, holding what is built beyond it on the product side; sides and bases as elsewhere | covered | brief: "checks that what was built is what he said and nothing more"; "where the change went beyond his statement, the audit holds it"
- The text as built: a small change goes on top of its stack's last branch with no branch or pull request of its own while the stack is unmerged, with or without a drafted plan; full-size plans keep the ordinary policy | covered | brief: "While the stack it belongs to is unmerged, it takes no branch and no pull request of its own; it goes on top of the last one."; "work of full size are handled as they are today"
- Worker judgement calls (Task_2): run record and readings file stay under active/ until acceptance | extends | brief: the run stays open and takes directed changes
- Worker judgement calls (Task_2): Scenarios and Units audit-stated, the small change's section its trace | extends | ADR-D-0055 Validation line; ADR-D-0051 "holds only what audits stated" (tension named to the owner)
- Worker judgement calls (Task_2): scenarios and getting-closer judged at a small change's closeout too; stopping reads "a further unit"; "no plan" said plainly; a rejection while open is a directed change | extends | brief: "he is told when it is done"; A small change and the run
- Orchestrator rulings: ADR-D-0051 left alone (overturned by review), then revised on his word; a new record first, then the accepted ones revised, then split on his word; the merged case's governing brief left to the hand-over; depends_on left alone; plan alternative kept rejected outright; the derived reopen premises kept | covered as mechanics or by his words, as each Decision Log entry records
- Decision Log: the owner's three answers (split the record; may be built, trivial unchanged; revise the run's closing) | covered | his quoted words of 2026-10-06
- Removal of the setup fixture folder and the close of the old value-level-operation plan, in the range but outside this brief | covered | his words relayed 2026-10-06: "Remove all."; "Just make sure it's not forgotten."
- Scenario 1, the Orchestrator's expectation only: not yet; the text exists and no small change has been built under it.

#### The audit's comparison, closeout (2026-10-06), as returned

Reading compared:
- C1 (DoD 1 as reworded), C3, C5a, C9, C10, C14-type items (J11, J14): agrees.
- C2 (statement in the brief or an amendment): agrees (plan-draft Planner-added 2, extends / inferred, kept).
- C4 and Planner-added 1 as reworded: diverges. Orchestrator: covered ("the change belongs to the run; no plan document"). Audit: inferred, with `direction`.
- C6a: agrees (covered / cited).
- C6b (closes on acceptance; `candidate ready` and the note recur): diverges. Orchestrator: covered under "The text as built: a run is one or more units ... closes once on his acceptance". Audit: inferred, `direction`.
- C7 (merged case under a brief Counsel hands over): diverges. Orchestrator: covered ("the hand-over mechanics are the existing ones"). Audit: inferred, `direction`.
- C5b (pull-request text brought up to date): unread.
- C8 (`no plan` said plainly; told when done): diverges. Orchestrator: extends. Audit: cited.
- C11 (Counsel's contacts each time reported ready): unread.
- D1 (ADR-D-0055): agrees (covered / cited).
- D2, D3 (ADR-D-0040, ADR-D-0051): diverges. Orchestrator: covered, relying on "his acceptance 2026-10-06". Audit: ask-now; the relayed acceptance is in the plan's log and in no document, and the mandate returns a record whose decision changed to the owner by name.
- D4: unread (ADR-D-0041 pointers) / not audited.
- J1: agrees. J2: agrees (mechanics / not audited).
- J3 (split on his word): diverges in basis. Orchestrator: covered by his quoted words. Audit: inferred; the words are in the plan, not a document.
- J4 (ADR-D-0051 left alone, overturned): diverges. Orchestrator: covered as mechanics or by his words. Audit: inferred, superseded.
- J5, J6: agrees. J7: agrees (mechanics / not audited).
- J8 (between acceptance and merge left Not covered): unread; the audit marks it `direction`.
- J9: agrees (extends / inferred).
- J10: agrees (extends / inferred); the audit adds `direction`.
- J11: diverges. Orchestrator: extends. Audit: cited.
- J12: unread as its own item (the final form is read under "the text as built ... product side", which agrees).
- J13: diverges, as C7.
- H1, H2 (old plan closed; fixtures removed): diverges. Orchestrator: covered by his relayed words "Remove all." and "Just make sure it's not forgotten." Audit: internal mechanics, not audited; the relayed words are in no document and are not support; the changes are not work of this brief and the fixture removal is not logged in the plan.
- H3: unread.

Findings compared: none found. The readings file's `Findings` section reads "None yet."; the brief marks no statement as a means, so no departure from a means was noted on any item line. Not under Findings but recorded as a reading (line 68): the tension between ADR-D-0051's "holds only what audits stated" and the small change's section of the run record; acting on it would change what the owner reads of a run, so if it is raised it bears on the design; it ends with its grade, inferred with `direction` (J10).

Readings corrected after this comparison: the run record's trace, the run closing on acceptance, the merged case's hand-over and Counsel's recurring note are extensions of the brief's statements, not covered by them; `no plan` said plainly and a rejection while open as a directed change are what the brief states; the owner's acceptance of the revised records and his other relayed words live in the plan's Decision Log, not in a value document, so they are claims to the audit and the readings now say so; the old plan's close and the fixture removal are mechanics outside this brief.

## Findings

- ADR-D-0051 keeps "The record holds only what audits stated" while the text built here makes a small change's section of the run record the Orchestrator's trace (noticed by the Task_2 Worker and the reviewer). Reading: bears on the design if raised, since it changes what the owner reads of a run; the audit graded it inferred with `direction` (J10), so it reaches him at closeout as a marked item and is not escalated twice.
