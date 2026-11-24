# Plan: Decision records at intent altitude: authorization and the run

- status: draft
- generated: 2026-11-24
- last_updated: 2026-11-24
- work_type: docs

## Goal
- The seven other active records of the area "Authority, the audit and the run" (ADR-D-0051, 0055, 0057, 0058, 0062, 0064, 0065), the ones on what authorizes work, what a run is and what a discovery does to it, are checked against the record standard as it stands, and each decision that fails the check has a new complete record proposed for it. No decision changes.

## Definition of Done
- Each of the seven records has its check's result ready for the run record's table: meets, rewritten (to which), split (into which), retired (material where), or raised.
- Each new record is in the template's present form, states one decision by the owner's test, and names in `consulted` the old record's entries and the model that wrote it.
- Every Decision clause of an old record has one of three fates, listed clause by clause: carried by a new record; held by a named accepted record, or by a proposed record of the pull request this unit is stacked on, whose line that states it is quoted; or, only for what the brief lists as mechanics (routes, moves, file names, admission of a relay, template fill-ins) and for exact strings, left to the plugin's text, quoted by file and line, with which of those it is named.
- These reach the owner by name: a record split in two or more; a record the run cannot show to keep its decision; a record whose revisit condition says something the old record's reason does not. Every other rewrite waits for the closeout audit's confirmation, record by record, that its decision is unchanged, and he is given the list afterwards.
- The package validator and the smoke tests pass.

## Planner-added requirements
- `consulted` carries the old record's entries as well as the model that wrote the new record. Needed because: the brief asks for the models talked with, and the old record's entries are the only record of who was consulted when the decision was made.
- Each task's report lists every Decision clause of the old record and where it went, quotes a holder's line, and also lists each old Validation line not carried with where its content lives, each term the new record defines that the old did not, and anything a new Decision holds that the old record had in another section. Needed because: the brief's rule on a clause not carried cannot be reviewed without the list, and the previous unit's review found a scope narrowed by an added definition, an allowance lost with a Validation line, and sentences moved into a Decision unnamed (`docs/coding-agent/lessons.md`, the two entries of 2026-11-24).
- A new record's file name, once numbered, is at most 109 characters. Needed because: a retired record's name gains 26 characters and names beyond 135 have failed the smoke test's copy of the tree (`docs/coding-agent/lessons.md`, the entry on file-name length).

## Scope / Non-goals
- Scope: new proposed records under `docs/coding-agent-orchestration-harness/decisions/`.
- Non-goals:
  - Changing any decision's outcome; a decision found stale or contradicted is brought to the owner through Counsel and not rewritten.
  - The plugin's text, the record standard and its template.
  - Marking any record accepted, retiring any old record, and repairing references to it: these follow acceptance, as a small change of the run.
  - Rewriting ADR-D-0058 or ADR-D-0062 for their older form alone (Decision Log).
  - The records of pull requests 113 and 114, and the area "Roles, routing, runtimes and rules".

## Design
- Chosen: one task per old record or closely tied pair, each writing the new records for it; no alternative required. The change touches no responsibility, contract, persisted state, new component, trust boundary or hot path.

## Context (workspace)
- Governing brief: `docs/coding-agent/briefs/active/decision-records-at-intent-altitude-brief.md`. Ratification as it reached this session: Counsel's relay over the peer channel, 2026-11-24T09:42:31Z, handing over the part of the open run that is not begun and quoting the owner's words from the run record's hand-over line: "Nothing to add, I ratify the brief, hand it over." (2026-11-02). Relays are admitted by the Standing Approvals entry "Relays from Counsel" in `docs/coding-agent/rules/common.md`, accepted 2026-11-20.
- Run record: `docs/coding-agent/plans/active/decision-records-at-intent-altitude-run.md`. Readings file: `docs/coding-agent/plans/active/decision-records-at-intent-altitude-readings.md`.
- Branch: `feature/2026-11-24/decision-records-authorization-and-run`, stacked on the branch of pull request 114 (a6d0628d), which carries proposed ADR-D-0132 to ADR-D-0138 and is itself stacked on pull request 113.
- What the previous unit leaves to this one (`docs/coding-agent/plans/completed/decision-records-at-intent-altitude-audit-area-plan.md`): the area is built as two units; how the owner's test is read (a clause is part of another decision only when no way of retiring that decision leaves it anything to constrain), which that unit's closeout audit marks as a matter of direction and as applied unevenly; ADR-D-0133 points at ADR-D-0051 for when a run under a brief is reported ready, and ADR-D-0136 at ADR-D-0065 for a standing approval's effect on a unit being authorized, pointers this unit's successors must still answer.
- Related files/areas: the record standard `plugins/coding-agent-orchestration-harness/skills/durable-docs-authoring/references/adr.md` and its template; the plugin text the seven records were compared with (`skills/orchestration-harness/SKILL.md`, `references/lifecycle-gates.md`, `completion-closeout.md`, `value-level-operation.md`, `final-response-contract.md`, `agents/Worker.md`); ADR-D-0072, 0086, 0089, 0094, 0096, 0112.
- Research: the Researcher's report of 2026-11-24 on the area's eleven records (a Claude subagent on Fable 5.2 at high reasoning effort), read for the previous unit's plan. Its classifications for these seven, which each task checks again: ADR-D-0064 two decisions (non-trivial work is authorized only by the person directing the work or that person's ratified brief; under a ratified brief no unit is put to that person for approval), arguable as one; ADR-D-0065 two (the conditions on which a ratified brief authorizes a unit; an authorization covers the unit as it stood, and what changes afterwards needs fresh authorization), arguable as three; ADR-D-0057 three (a discovered issue is never absorbed into the change; a revised plan passes again the gate that admitted it, which is ADR-D-0065's fresh authorization seen from the other side; a discovery that changes a contract's shape or is irreversible or outward-facing still needs the person's confirmation); ADR-D-0051 three (a run of units that goes from unit to unit without the person; a run reported ready stays open, takes directed changes and closes once on acceptance; a result is reported as behaviour and what only the person can judge is never reported as met), arguable from two to four; ADR-D-0055 one; ADR-D-0058 and ADR-D-0062 meeting the standard in the older form. None is operational only. No clause was found contradicted; three points need care and are pre-ruled in the tasks.
- Numbers: another run proposes records at the same time, so a draft is named by its subject and takes its number when the work lands. A draft's working name here is `ADR-D-from-<old number>-<slug>.md`, and a sibling is named in a draft by that working name.

## Open Questions (max 3)
- None.

## Assumptions
- A1: the Researcher's counts hold. source: unverified: each task applies the owner's test again in both directions, as the previous unit read it, and writes to the count the test gives, reporting a count that differs from the one expected as a judgement call; every split reaches the owner by name and the review checks the count.
- A2: no Decision clause of the seven is stale or contradicted. source: the Researcher's comparison of 2026-11-24, which read some newer records by their Decision sections or titles only; unverified for ADR-D-0057's confirmation of a contract-shape discovery beside ADR-D-0072, which Task_3 settles. A task that finds a clause stale or contradicted writes no record for that decision and reports it, and the decision goes to the owner through Counsel as raised; the Orchestrator then rules, before anything of the unit is published, what the unit's other records do.
- A3: the seven proposed records of pull request 114 and the ten of pull request 113 are not yet accepted. source: the tree at a6d0628d. This unit is stacked on both, so a record of theirs cannot land after this unit's; a clause one of them states may be held by it, named with the accepted record it replaces beside it.

## Tasks

### Task_1: ADR-D-0064, and the check of ADR-D-0062
- type: docs
- owns:
  - docs/coding-agent-orchestration-harness/decisions/ADR-D-from-0064-*.md
- depends_on: []
- description: |
  Check ADR-D-0064 against the record standard and the owner's test (the brief: a clause belongs to the same decision only if it could not stand once the first is retired; read here as: a clause is part of another decision when no way of retiring that decision leaves the clause anything to constrain), applied in both directions for each pair of clauses, and write a new complete proposed record for each decision it holds. Two are expected: that non-trivial work is authorized only by the person directing the work, by that person's own approval or waiver or by that person's ratified brief, and nothing else is ever an authority; and that under a ratified brief no unit of work is put to that person for approval or agreement, the ratification authorizing it or it not running. The list of what never authorizes stands under the closure "Nothing else authorizes" and is decision content. The forms an authorization takes are named by what each is, without their count. ADR-D-0055's successor must remain a record that "states conditions" for its kind of unit in the sense this record relies on. Check ADR-D-0062 against the standard apart from its older form and report meets or fails with the passages; write nothing for it.
- acceptance:
  - Each new record states one decision by the owner's test, in the template's present form, with nothing that merely happens to be so, wording that names a thing by what it is and not by its position, order or count, a problem statement that says what was wanted, why, and what failed to serve it, and no term defined so that it narrows what the old record reached.
  - The report holds what Planner-added requirements lists; a clause that is decision content is never left to the plugin's text, and a clause that says when, who or whether is not mechanics.
  - The Why names the philosophy statement the decision serves where one does, quoted from the philosophy, and invents none; where the old record gives no reason for a clause, the gap is reported and nothing is written for it.
  - Rejected alternatives, their reasons and reopen conditions, and revisit conditions are the old record's, restated and not replaced or narrowed; dated lines stay as written; an act stays an act and a limit stays a limit; a pointer to another record is checked against that record's scope and Not covered.
  - `status: proposed`; `supersedes` names the old record; `consulted` as Planner-added requirements states; the file name, once numbered, is at most 109 characters; the old record itself is unchanged.
  - A count by the owner's test that differs from the one expected is written to and reported as a judgement call.
  - ADR-D-0062's check result is reported with the evidence.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness: python scripts/validate_harness_package.py and python scripts/run_validation_smoke_tests.py; from the root: git diff --check, and git diff --no-index --check /dev/null <each new file>"
  - kind: review
    required: true
    owner: reviewer
    detail: "Each new record against the record standard, the owner's test and the old record, clause by clause; the decision is unchanged; ADR-D-0062's check"

### Task_2: ADR-D-0065
- type: docs
- owns:
  - docs/coding-agent-orchestration-harness/decisions/ADR-D-from-0065-*.md
- depends_on: []
- description: |
  As Task_1, for ADR-D-0065. Two records are expected: that a ratified brief authorizes a plan or a goal envelope only on a closed review of the whole unit and an independent value audit that holds nothing; and that an authorization covers the unit as it stood when execution started, what is added to or changed in what a plan decides, or in a goal envelope, afterwards needing fresh authorization from the same authority before it is built. The second also takes ADR-D-0057's clauses on a revised plan (a plan revised or extended after it was authorized passes again, as a whole, the gate that admitted it, before any of the change is built; without a brief the revision takes the plan review as well as the person's approval or waiver; the revision is judged as a whole and not against the issue that prompted it) and names both old records in `supersedes`; "or in a goal envelope" is kept, ADR-D-0086 relying on it. Whether "an irreversible or outward-facing action waits for the decision of whoever holds the authority for it, at its moment, whatever authorized the unit that contains it" is a decision of its own is decided by the test; it is expected to be a condition of the first, as the old record words it, and if the test gives a record of its own it is written. The conditions are stated as what must hold, not as the plugin's list item for item. That the audit grades only a side that has a value document, that the test for an irreversible or outward-facing action runs on every item, and that a held item waits are stated by the proposed ADR-D-0134 and pointed at; that a side with no document does not stand in the way of authorization, and the condition for authorizing again after a held item, are this record's and are carried. The worked example of a repository with a brief and no engineering philosophy is left out or kept by the standard's two grounds. The dated revisit line stays as written.
- acceptance:
  - As Task_1's first six bullets, for ADR-D-0065 and for ADR-D-0057's clauses on a revised plan.
  - No Decision line mirrors a passage of the plugin's procedure.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "As Task_1"
  - kind: review
    required: true
    owner: reviewer
    detail: "As Task_1, for ADR-D-0065 and ADR-D-0057's clauses on a revised plan"

### Task_3: ADR-D-0057, and the check of ADR-D-0058
- type: docs
- owns:
  - docs/coding-agent-orchestration-harness/decisions/ADR-D-from-0057-*.md
- depends_on: []
- description: |
  As Task_1, for ADR-D-0057 apart from its clauses on a revised plan, which Task_2's record on fresh authorization takes and which this task's records point at by that record's subject. Two records are expected: that an issue discovered during authorized work is never absorbed into the current change, whoever found it, the Orchestrator ruling what it is; and that inside authorized work a discovery that changes a contract's shape or is irreversible or outward-facing still needs the confirmation of the person directing the work. Who may discover is stated as its criterion (anyone), and the readings an issue may be given are named by what each is, without their count. The commitment that a discovery is recorded and seen outside the Orchestrator is carried; where it is written and when it is surfaced are a file name and a route. That no extension is built on the Orchestrator's judgement alone is stated by ADR-D-0064 ("Nothing else authorizes: not the Orchestrator's own judgement") and by its successor. The second record: accepted ADR-D-0072 has the person asked whether a consumer exists "only where no accessible source settles it", and a change go ahead "without asking" where sources settle that there is none; the plugin's text still has the pause for a contract-shape change. Where the old clause can be stated at intent altitude so that it is true beside ADR-D-0072 without narrowing what it decides, the record is written; where staying true beside ADR-D-0072 would narrow it, nothing is written for that decision, its result is raised, and the report gives the two readings for the Orchestrator to take to the owner through Counsel. Check ADR-D-0058 as Task_1 checks ADR-D-0062.
- acceptance:
  - As Task_1's first six bullets, for ADR-D-0057, or, where the decision on confirmation would be narrowed, no record for it and the two readings reported.
  - ADR-D-0058's check result is reported with the evidence.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "As Task_1"
  - kind: review
    required: true
    owner: reviewer
    detail: "As Task_1, and ADR-D-0058's check"

### Task_4: ADR-D-0051 and ADR-D-0055
- type: docs
- owns:
  - docs/coding-agent-orchestration-harness/decisions/ADR-D-from-0051-*.md
  - docs/coding-agent-orchestration-harness/decisions/ADR-D-from-0055-*.md
- depends_on: []
- description: |
  As Task_1, for ADR-D-0051 (three records expected) and ADR-D-0055 (one). ADR-D-0051: that work under a ratified brief is a run of one or more units that goes from unit to unit without the person directing the work; that a run reported as ready stays open for that person's judgement, takes the changes that person directs against its brief as its own work, and closes once, on that person's acceptance; and that a result is reported as ready as behaviour, scenario by scenario, what only the person can judge never being reported as met. Carried, no other record holding them: that each unit is authorized on its own and being in a run authorizes nothing; that the run's state between units is only what audits stated; what a scenario only the person can judge is. The kinds of unit and their order, the note to Counsel, where the run's record is kept and what its sections are, and that reviewed branches are published where a standing approval covers that are routes, moves and file names. The list of what reaches the person between units is restated as its criterion, only what already reaches that person during a unit, so that a further kind of stop does not make it false; the reopen condition built on the same list is restated on the same criterion and named to the owner. A small change stated against a brief whose run is already accepted and merged is worded so that it does not read as governed by the completed brief. ADR-D-0055: a small change the person directing the work stated in a ratified brief may be built without a plan, and stands only once a closing value audit holds nothing. "The second source" is named by what it is, the person's ratified brief, in every place the old record has it. The checks that stay are named by what each is, without their count, and the steps left out are not listed as the plugin lists them. The criterion for when a plan is the better choice is carried as a criterion; that what counts as trivial work does not change is carried as a boundary. That a small change is a unit of the run is stated in the record from ADR-D-0051 on the run of units, and the record from ADR-D-0055 points at it by its working name. ADR-D-0133 points at the record on the run reported as ready for when that is; that record must state it.
- acceptance:
  - As Task_1's first six bullets, for each of the two old records.
  - No Decision line mirrors a passage of the plugin's procedure, and no record names a thing by its position.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "As Task_1"
  - kind: review
    required: true
    owner: reviewer
    detail: "As Task_1"

## Task Waves (explicit parallel dispatch sets)

- Wave 1 (parallel): [Task_1, Task_2, Task_3, Task_4]

## Rollback / Safety
- New files only, all proposed; reverting the branch removes them. No record is accepted, retired or merged by this plan. The push and pull request go under the standing approval for a finished, reviewed run; acceptance of each record that reaches the owner by name, and the merge, wait for the owner.

## Progress Log (append-only)

Append-only editing rule (applies to both logs below): when appending an entry, anchor the edit on the previous entry and reproduce it (or anchor on the section's tail marker) so the edit inserts rather than replaces, and verify afterward that the log grew.

- 2026-11-24 Plan starts from revision a6d0628d (the head of pull request 114's branch; the brief is unchanged since pull request 111).

## Decision Log (append-only; re-plans and major discoveries)

- 2026-11-24 Decision: a merged accepted record that fails the standard only by its older form meets the standard and is not rewritten; ADR-D-0058 and ADR-D-0062 are expected to be such.
  - Trigger / new insight: the Researcher classed both as meeting the standard in the older form.
  - Tradeoffs considered: the brief has "Records already accepted stay as they are" for the template change, and the two earlier units of this kind ruled the same for ADR-D-0047, ADR-D-0060 and ADR-D-0067. Each is still checked against the rest of the standard by its task.
  - User approval: no (Orchestrator ruling, from the brief)
  - Record proposed: none
- 2026-11-24 Decision: ADR-D-0057's confirmation of a contract-shape discovery is not raised before the unit starts.
  - Trigger / new insight: the Researcher reported a possible tension with ADR-D-0072, unresolved.
  - Tradeoffs considered: no closure word of ADR-D-0057 is broken by ADR-D-0072, whose "only" and "without asking" are about whether a consumer exists, and the plugin's text still states the pause; so the files do not show the clause stale. Task_3 settles whether it can be stated without narrowing, and raises it if not; the brief has a raised decision reach him before the rest is rewritten, which A2 keeps for that case.
  - User approval: no (Orchestrator ruling)
  - Record proposed: none
- 2026-11-24 Decision: ADR-D-0057's clauses on a revised plan are written once, in the record on fresh authorization that Task_2 writes from ADR-D-0065.
  - Trigger / new insight: the Researcher found them the same decision as ADR-D-0065's clause that what changes after authorization needs fresh authorization, seen from the other side; this run already ruled that ADR-D-0065 holds that clause for ADR-D-0066.
  - Tradeoffs considered: two records stating one decision would have to be retired together; one record superseding both old ones in part is what the standard's "no partial supersession" allows only when every other clause of each old record has its own new record in the same acceptance, which this unit gives.
  - User approval: no (Orchestrator ruling)
  - Record proposed: none

## Notes
- Risks: ADR-D-0064 and ADR-D-0065 are pointed at by sixteen and thirteen accepted records; after acceptance each pointer is repaired by what it means. A Worker will be tempted to keep the plugin's wording in ADR-D-0065 and ADR-D-0057. Counts may move under review.
- Edge cases: the retired names of ADR-D-0055, ADR-D-0064 and ADR-D-0065 pass 135 characters with the retirement suffix and need the slug shortened at retirement.
