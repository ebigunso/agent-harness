# Plan: Decision records at intent altitude: the value audit and what it shows

- status: draft
- generated: 2026-11-24
- last_updated: 2026-11-24
- work_type: docs

## Goal
- Four active records of the area "Authority, the audit and the run" (ADR-D-0042, 0052, 0053, 0054), the ones on the value audit, findings and what a brief's statements bind, are checked against the record standard as it stands, and each decision that fails the check has a new complete record proposed for it. No decision changes.

## Definition of Done
- Each of the four records has its check's result ready for the run record's table: meets, rewritten (to which), split (into which), retired (material where), or raised.
- Each new record is in the template's present form, states one decision by the owner's test, and names in `consulted` the old record's entries and the model that wrote it.
- Every Decision clause of an old record has one of three fates, listed clause by clause: carried by a new record; held by a named accepted record, whose line that states it is quoted; or, only for what the brief lists as mechanics (routes, moves, file names, admission of a relay, template fill-ins), left to the plugin's text, quoted by file and line.
- These reach the owner by name: a record split in two or more; a record the run cannot show to keep its decision; a record whose revisit condition says something the old record's reason does not. Every other rewrite waits for the closeout audit's confirmation, record by record, that its decision is unchanged.
- The package validator and the smoke tests pass.

## Planner-added requirements
- `consulted` carries the old record's entries as well as the model that wrote the new record. Needed because: the brief asks for the models talked with, and the old record's entries are the only record of who was consulted when the decision was made.
- Each task's report lists every Decision clause of the old record and where it went, and a statement that a named record holds a clause quotes that record's line. Needed because: the brief's rule that a clause not carried is held by a named accepted record cannot be reviewed without the list, and the previous unit withdrew two rulings made without the quotation (`docs/coding-agent/lessons.md`, 2026-11-24).
- Anything a new record's Decision holds that the old record had in another section is named in the task's report. Needed because: the previous unit's review found a Validation line promoted into a Decision without being named, and such a move is one the owner is told of with the record.
- A new record's file name, once numbered, is at most 109 characters. Needed because: a retired record's name gains 26 characters and names beyond 135 have failed the smoke test's copy of the tree (`docs/coding-agent/lessons.md`, the entry on file-name length).

## Scope / Non-goals
- Scope: new proposed records under `docs/coding-agent-orchestration-harness/decisions/`, and the run record brought up to date for this session taking the two areas not started.
- Non-goals:
  - Changing any decision's outcome; a decision found stale or contradicted is brought to the owner through Counsel and not rewritten.
  - The plugin's text, the record standard and its template.
  - Marking any record accepted, retiring any old record, and repairing references to it: these follow acceptance, as a small change of the run.
  - The seven other records of the area (ADR-D-0051, 0055, 0057, 0058, 0062, 0064, 0065), which are the next unit, and the area "Roles, routing, runtimes and rules".
  - Anything of pull request 113: its ten proposed records, their acceptance, the retirements that follow and its merge stay with the session that built it.

## Design
- Chosen: the area's eleven records go in two units, this one of four old records (six new records expected) and a next one of seven (about ten expected), each its own pull request; within the unit, one task per old record or closely tied pair. Alternative considered: the whole area as one unit and one pull request, which keeps every sibling pointer inside one acceptance. It loses because the research counts sixteen to nineteen new records for the area and the brief has him receive batches "of about ten records"; the ties that cross the two units are pointers and no clause of these four is left where only a record of the next unit could hold it: ADR-D-0065 leans on ADR-D-0052 for which sides are graded and for a held item, which the next unit, stacked on this one, points at; and the record from ADR-D-0042 points at accepted ADR-D-0051 for the moment a run is reported ready and at ADR-D-0065 for what an extension is, pointers the next unit repairs when it replaces those two. The change touches no responsibility, contract, persisted state, new component, trust boundary or hot path.

## Context (workspace)
- Governing brief: `docs/coding-agent/briefs/active/decision-records-at-intent-altitude-brief.md`. Ratification as it reached this session: Counsel's relay over the peer channel, 2026-11-24T09:42:31Z, handing over the part of the open run that is not begun and quoting the owner's words from the run record's hand-over line: "Nothing to add, I ratify the brief, hand it over." (2026-11-02). Relays are admitted by the Standing Approvals entry "Relays from Counsel" in `docs/coding-agent/rules/common.md`, accepted 2026-11-20.
- This session holds the peer seat `agent-harness-orchestrator-records`. The session holding `agent-harness-orchestrator` carried the run until 2026-11-24 and keeps what follows the acceptance of pull request 113.
- Run record: `docs/coding-agent/plans/active/decision-records-at-intent-altitude-run.md`. Readings file: `docs/coding-agent/plans/active/decision-records-at-intent-altitude-readings.md`.
- Branch: `feature/2026-11-24/decision-records-authority-area`, in its own working tree, stacked on the branch of pull request 113 (d3585e80), which carries proposed ADR-D-0117 to ADR-D-0126.
- Related files/areas: the record standard `plugins/coding-agent-orchestration-harness/skills/durable-docs-authoring/references/adr.md` and its template `adr-template.md`; the plugin text the four records were compared with (`skills/orchestration-harness/references/value-level-operation.md`, `value-audit-mandate.md`, `completion-closeout.md`, `final-response-contract.md`, `skills/value-documents/SKILL.md`); ADR-D-0050, 0045, 0036, 0069, 0082 and the proposed ADR-D-0120 and ADR-D-0122.
- Existing patterns: `docs/coding-agent/plans/completed/decision-records-at-intent-altitude-counsel-area-plan.md` for how a unit of this run is planned, what a record task's acceptance holds, and what its review found.
- Research: a Researcher (a Claude subagent on Fable 5.2 at high reasoning effort; the researcher seat shows no placement in the team's roster and was not seen live) checked each of the area's eleven records on 2026-11-24 against the standard, the owner's test, the plugin's present text, the newer records and the branch of the run "lessons keep their purpose". Its classifications for this unit's four, which each task checks again before acting: ADR-D-0052 three decisions (the Orchestrator never grades its own run; its reading is stated before grading and compared only after the grades are fixed; a standing approval is given only by whoever holds the authority and never stands in for the acts that keep their own acceptance), arguable from two to four; ADR-D-0042, 0053 and 0054 one each, failing on clauses that mirror the plugin's text or fix what happens to be so. None is operational only, and no clause was found contradicted. That other run's branch proposes ADR-D-0127 to ADR-D-0131 and names none of the eleven.
- Numbers: another run proposes records at the same time, so a draft is named by its subject and takes its number when the work lands (`adr.md`, Lifecycle). A draft's working name here is `ADR-D-from-<old number>-<slug>.md`, and a sibling is named in a draft by that working name.

## Open Questions (max 3)
- None.

## Assumptions
- A1: the Researcher's counts hold. source: unverified: they are one application of the owner's test, and the previous unit's review moved a count; each task applies the test again in both directions and writes to the count the test gives, reporting a count that differs from the one expected as a judgement call; every split reaches the owner by name and the review checks the count.
- A2: no Decision clause of the four is stale or contradicted. source: the Researcher's comparison of 2026-11-24, which read some newer records by their Decision sections or titles only. A task that finds a clause stale or contradicted writes no record for that decision and reports it, and the decision goes to the owner through Counsel as raised; the Orchestrator then rules, before anything of the unit is published, what the unit's other records do, since the brief has a raised decision reach him before the rest is rewritten.
- A3: the ten proposed records of pull request 113 are not yet accepted. source: the tree at d3585e80. Where a clause is held by a record that pull request retires (ADR-D-0045, ADR-D-0036), the new record names the accepted record and, beside it, the proposed record that takes it over, so that the pointer is repaired by whichever lands later.

## Tasks

### Task_1: ADR-D-0052
- type: docs
- owns:
  - docs/coding-agent-orchestration-harness/decisions/ADR-D-from-0052-*.md
- depends_on: []
- description: |
  Check ADR-D-0052 against the record standard and the owner's test (the brief: a clause belongs to the same decision only if it could not stand once the first is retired), applied in both directions for each pair of clauses, and write a new complete proposed record for each decision it holds. Three are expected. (A) The Orchestrator never grades its own run against the value documents: a party with fresh context does, on what it reads for itself, and its grade binds. (B) The Orchestrator's own reading of each item is stated before grading and compared only after the grades are fixed; a difference is corrected inside the run and stops nothing. (C) A standing approval is given only by whoever holds the authority for the action, counts only once its giver has accepted the written entry, and never stands in for the acts that keep their own acceptance.
  How the test is read for B, the same reading Task_2 applies: a clause is part of another decision when no way of retiring that decision leaves the clause anything to constrain. A can be retired so that someone other than the Orchestrator still grades, as its own rejected alternatives show, and B would then still bind; B also has rejected alternatives and revisit conditions of its own. So B is expected to be a record of its own. C is expected to be one record, what it never discharges being the limit of the thing given; the test is applied to its two halves all the same, and two records are written if each binds with the other gone.
  Pre-rulings. The scope "in a plan-mode run" and the Not covered "goal mode" stay as they are on the records from A and B, ADR-D-0082 leaning on them; the record from C carries no such scope, the old clauses on standing approvals having none. The list of acts a standing approval never discharges is decision content and stays. Every clause on standing approvals is carried, who writes the entry included, restated as its criterion where it fixes what happens to be so. Left to the plugin's text: that the reading is a file and where it is kept (a file name), and the exact names of the readings and of the verdict's values (exact strings, which the standard has not covered). That a dispatch carries locations only is held by ADR-D-0050 ("A dispatch to the Auditor carries locations only"), and the boundary it serves, that nothing the Orchestrator says is evidence, is still carried. A held item waiting, a side with no document, and unratified notes not being evidence are held by no other record and are carried. Each title states its decision.
- acceptance:
  - Each new record states one decision by the owner's test, in the template's present form, with nothing that merely happens to be so, wording that names a thing by what it is and not by its position, order or count, and a problem statement that says what was wanted, why, and what failed to serve it.
  - The report lists every Decision clause of the old record with its fate, as the Definition of Done states the three fates; a clause that is decision content is never left to the plugin's text, and a holder's line is quoted.
  - The Why names the philosophy statement the decision serves where one does, quoted from the philosophy, and invents none.
  - Rejected alternatives, their reasons and reopen conditions, and revisit conditions are the old record's, restated and not replaced or narrowed; an act stays an act and a limit stays a limit; anything moved into a Decision from another section is named in the report.
  - `status: proposed`; `supersedes` names the old record; `consulted` as Planner-added requirements states; the file name, once numbered, is at most 109 characters; the old record itself is unchanged.
  - A count by the owner's test that differs from the one expected is written to and reported as a judgement call.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness: python scripts/validate_harness_package.py and python scripts/run_validation_smoke_tests.py; from the root: git diff --check, and git diff --no-index --check /dev/null <each new file>"
  - kind: review
    required: true
    owner: reviewer
    detail: "Each new record against the record standard, the owner's test and the old record, clause by clause; the decision is unchanged"

### Task_2: ADR-D-0053 and ADR-D-0054
- type: docs
- owns:
  - docs/coding-agent-orchestration-harness/decisions/ADR-D-from-0053-*.md
  - docs/coding-agent-orchestration-harness/decisions/ADR-D-from-0054-*.md
- depends_on: []
- description: |
  As Task_1, for ADR-D-0053 and ADR-D-0054; one record each is expected, and the two are accepted together, each pointing at the other.
  ADR-D-0053: a finding that would change what someone experiences reaches the person directing the work at once, whatever acting on it would cost, with only the part it concerns held. Whether the value audit's check of the Orchestrator's reading of a finding is a decision of its own is decided by the test as Task_1 reads it; it is expected to be part of this one, since no way of retiring the escalation rule leaves a reading of a finding to check, which is where it differs from the reading of ADR-D-0052. Every commitment of the old clause on that check is carried, as acts where the old record has acts: the reading is compared by the audit only after its grades are fixed, and in both directions; the Orchestrator escalates each finding the audit judges to bear on the design the same way and holds its part; the part held for a finding the audit names trivial is released, unless the person directing the work has already answered, in which case the answer stands; a trivial finding is kept from the person by more than the Orchestrator's own reading. Only the route is left to the plugin's text: where readings are kept, that the comparison is at the audit's next position, and that a question is withdrawn by the carrier. "The rest of the run continues" is worded so that a goal loop, where the part concerned is the loop, does not make it false. That the audit sends nothing about findings to Counsel is held by ADR-D-0045 ("During a run Counsel hears from the value audit of one thing only"), which the proposed record on what Counsel hears from the value audit during a run takes over.
  ADR-D-0054: a way of doing something written in a brief does not bind the run; what the work must give and its constraints do. The kinds are named by what each is. That an item departing from a means is judged on what the means serves, and is never held for the departure alone, is decision content and is carried; only the exact names of the audit's grade reasons are the plugin's. On a departure from a means, the record from ADR-D-0054 states that it is recorded as a finding and read by the test for every finding, and when it reaches the person; the record from ADR-D-0053 states the test and points at it by its working name.
- acceptance:
  - As Task_1's six bullets, for each of the two old records.
  - No Decision line mirrors a passage of the plugin's procedure.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "As Task_1"
  - kind: review
    required: true
    owner: reviewer
    detail: "As Task_1"

### Task_3: ADR-D-0042
- type: docs
- owns:
  - docs/coding-agent-orchestration-harness/decisions/ADR-D-from-0042-*.md
- depends_on: []
- description: |
  As Task_1, for ADR-D-0042; one record is expected: of what a run decided without the person, that person is shown only what the value audit marked as bearing on direction, as the audit stated it, and the rest stays in the run's records. Whether keeping every extension and judgement call in the run's records is a decision of its own is decided by the test. The enumeration of whose choices count ("the choices Workers reported and the rulings the Orchestrator made") is restated as its criterion, every judgement call a run makes without the person, so that a further kind of reporter does not make it false. The moment the marked items are shown is named by what it is, the run being reported ready for that person's judgement, where "at closeout" would read as each unit's; accepted ADR-D-0051 states that moment ("A unit of a run closes with its own checks and is not reported as ready for judgement"; "When the run's last unit has closed, the result is reported as ready for that person's judgement") and the new record points at it. What the two philosophies are is a detail that stays if a first-time reader needs it to know what direction means.
- acceptance:
  - As Task_1's six bullets, for ADR-D-0042.
  - No Decision line mirrors a passage of the plugin's procedure.
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

- Wave 1 (parallel): [Task_1, Task_2, Task_3]

## Rollback / Safety
- New files only, all proposed; reverting the branch removes them. No record is accepted, retired or merged by this plan. The push and pull request go under the standing approval for a finished, reviewed run; acceptance of each record that reaches the owner by name, and the merge, wait for the owner.

## Progress Log (append-only)

Append-only editing rule (applies to both logs below): when appending an entry, anchor the edit on the previous entry and reproduce it (or anchor on the section's tail marker) so the edit inserts rather than replaces, and verify afterward that the log grew.

- 2026-11-24 Plan starts from revision d3585e80 (the head of pull request 113's branch; the brief is unchanged since pull request 111).
- 2026-11-24 Plan review of the draft at b0481d9e (Reviewer, a Claude subagent on Fable 5.2, the reviewer seat showing no placement in the roster): NEEDS_REVISION, three major and seven minor findings; `validate_plan.py` passed. Both quoted holder lines confirmed in ADR-D-0050 and ADR-D-0045. All taken; see the Decision Log entry of this date.

## Decision Log (append-only; re-plans and major discoveries)

- 2026-11-24 Decision: the area is built as two units, this one first.
  - Trigger / new insight: the research counts sixteen to nineteen new records for the eleven.
  - Tradeoffs considered: Design, above.
  - User approval: no (Orchestrator ruling, from the brief's batch size)
  - Record proposed: none
- 2026-11-24 Decision: ADR-D-0054 is rewritten and not passed as meeting the standard in its older form.
  - Trigger / new insight: the Researcher called it arguable under the previous unit's reading of "mirrors a passage of the plugin's procedure", a reading that unit's audit marked as a matter of direction and the owner has not answered.
  - Tradeoffs considered: apart from form, its Decision words a grade as the audit's mandate does and its Validation fixes the count of a brief's kinds, which fail the standard's line on what merely happens to be so whichever way "mirrors" is read.
  - User approval: no (Orchestrator ruling)
  - Record proposed: none
- 2026-11-24 Decision: plan revised on the plan review's findings, all taken.
  - Trigger / new insight: the review found that "who writes a standing approval's entry" was ruled mechanics though it is none of the brief's and no record holds it; that the commitments of ADR-D-0053's clause on the audit's check were summarized with parts dropped; that the expected counts read the owner's test two ways for the same shape without saying why; and seven smaller points.
  - Plan delta (what changed): every clause on standing approvals is carried; Task_2 lists each commitment of the check and leaves only the route to the plugin's text, and says what of ADR-D-0054's grading clause is carried; one reading of the test is stated for both tasks with the reason the two expected counts differ, and the two halves of the standing-approval decision are tested; the plan-mode scope is placed on two of ADR-D-0052's three records; the records from ADR-D-0053 and ADR-D-0054 are accepted together; Task_3 quotes ADR-D-0051 for the moment; Design names both ties across the units; A2 says what happens to the wave when a decision is raised; one more planner-added requirement is listed; the Definition of Done has the retired result; a Decision Log ground corrected.
  - User approval: no
  - Record proposed: none

## Notes
- Risks: ADR-D-0052 is pointed at by fifteen accepted records and nine front-matter paths; after acceptance each pointer is repaired by what it means (the audit, the reading, or standing approvals). A Worker will be tempted to keep wording the plugin's text has. Counts may move under review.
- Edge cases: the retired names of ADR-D-0052 and its neighbours pass 135 characters with the retirement suffix and need the slug shortened at retirement, which is the small change after acceptance.
