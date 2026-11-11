# Plan: Decision records at intent altitude, the goal-mode records that hold more than one decision

- status: draft 2026-11-11 (revised after plan review BUNDLE-P1 and BUNDLE-R1)
- generated: 2026-11-11
- last_updated: 2026-11-11
- work_type: docs

## Goal
- Bring to the record standard the four accepted goal-mode records the census classed as holding more than one decision: ADR-D-0011, 0029, 0063 and 0066, under the governing brief `docs/coding-agent/briefs/active/decision-records-at-intent-altitude-brief.md`. Each decision gets a record of its own; the decisions do not change.
- The brief is the requirement and is not restated here; where this plan and the brief differ, the brief governs and the difference is a plan defect.
- This is the second unit for the goal-mode area in the run recorded in `docs/coding-agent/plans/active/decision-records-at-intent-altitude-run.md`. It is built on top of the first unit's branch, as the owner directed on 2026-11-11, and published as a pull request stacked on pull request 97.
- One clause from outside the four comes with it: that a goal loop never re-scopes, reframes or abandons its goal, a change of goal being the owner's. It came out of ADR-D-0076 on the owner's word and is to be held by the record on the protection of the goal condition that this unit splits from ADR-D-0011 (brief, Directed during the run).

## Definition of Done
- Each of the four records is checked again against the standard and read by the owner's test for one decision (brief: "a clause belongs to the same decision only if it could not stand once the first is retired. A clause that would still bind with the first gone is a decision of its own"). The check's result is recorded in the run record (brief, the second pass condition): split (into which); or, where the check differs from the census, one decision rewritten, meets the standard, operational only, or its decision stale or contradicted (to the owner through Counsel, nothing written).
- For each decision the test finds and the standard's admission test admits, a new complete proposed record states it at intent altitude, in the template's form as changed on 2026-11-11 (no Invariant line; Validation says only what would show the decision broken).
- No decision's outcome changes (brief, the constraint on decisions).
- The clause that came out of ADR-D-0076, with the clauses of ADR-D-0014 that go with it (listed in the run's changes file, section "ADR-D-0076 narrowed to the examination"), is carried by the record on the protection of the goal condition, if it belongs there by the test. If it does not, nothing is forced: where it is held returns to the owner through Counsel.
- Every clause of each old record is accounted for: carried into a named new record; or, for a clause of a Decision that is not carried, held by a named accepted record; or, for mechanics, left to plugin text quoted by file and line (brief, Directed during the run, the ruling kept on 2026-11-11). A clause of a Decision that no record holds is a gap: reported, and the old record is not retired until it is settled.
- Each new record's `consulted` field carries over the old record's entries and adds the model that wrote the record.
- This plan ends with the new records proposed, the branch reviewed `APPROVED`, and value audits at plan draft and closeout logged. It marks nothing accepted and retires nothing: every record that comes of a split reaches the owner by name, and the old records are retired, with references repaired, in a change of its own after his acceptance.

## Planner-added requirements
- Every clause of each old record is accounted for in the Worker's report. Needed because: it is what shows that a split carries everything the old record decided, once, and what the owner's kept ruling on uncarried Decision clauses is checked against.
- The `consulted` field carries over the old record's entries and adds the writing model. Needed because: the brief asks for the models he talked with and the model that wrote the record, and a past consultation is not replaced by the present writer.

## Scope / Non-goals
- Scope: new proposed records under `docs/coding-agent-orchestration-harness/decisions/`, ADR-D-0077 to ADR-D-0086 by the census's count.
- Non-goals: the other three areas; any change to a decision; marking a record accepted, retiring a record or repairing references; the record standard and its template; plugin text; ADR-D-0076 and ADR-D-0014 themselves.

## Design
- Fixed by the brief and the standard, and not compared: a bundle is split into new complete records and the old one retired; a record is never amended in place. Fixed by the owner: the unit is built on top of the first unit's branch.
- The choice is how the four records are divided among Workers.
- Chosen: one Worker for each old record, four in parallel, each owning a range of numbers fixed here.
- Alternative: one Worker for all four, writing the records in sequence.
- structure: under the chosen design the sibling records of one old record are written by one mind, and records of different old records cite each other only by the numbers this plan assigns; under the alternative every cross-citation is settled by the one writer as it goes.
- evolution: under the chosen design a changed count in one record moves every later number, since numbers may not skip: the Orchestrator renumbers the later records and repairs every citation between the new records before review, and checks each repaired citation by what it means, not by its number. No Worker enlarges its own range. Under the alternative the one writer numbers as it goes and that cost does not arise, but a late finding in the first record delays the rest.
- verification: the review and the audit read the same ten records either way; the chosen design gives them four clause accounts to check, each against one old record.
- operation: no runtime cost under either.
- human: the owner reads the same records either way.
- safety: neither changes a trust boundary.
- Why chosen wins: the test is applied clause by clause to one old record at a time, which is the unit a Worker can hold whole, and four in parallel finish in the time of one. The price is the renumbering and citation repair across all ranges when a count changes, which is the Orchestrator's, is done once, and is checked by the review.

## Compatibility stance
- preserve, for this plan: it adds proposed files and changes no accepted record, filename or reference. The change that follows his acceptance retires records and repairs references, and states its own stance.

## Context (workspace)
- The standard: `plugins/coding-agent-orchestration-harness/skills/durable-docs-authoring/references/adr.md`, with its template as changed on 2026-11-11.
- The plugin text these records mirror, by the census: `skills/orchestration-harness/references/goal-mode.md`, `goal-assessor-mandate.md`, `goal-templates.md`, `goal-condition-checklist.md`, `value-level-operation.md`, `value-audit-mandate.md`.
- Records written to the standard in this run show the form: ADR-D-0076 (proposed, the new template's form); ADR-D-0073 to 0075 (accepted; they keep an Invariant line the template no longer asks for).
- The numbers and what each record is expected to hold, by the census; a Worker's test may find otherwise:

  | Old record | New records |
  | --- | --- |
  | ADR-D-0011 | ADR-D-0077 (progress refers only to the goal); ADR-D-0078 (what counts as a stall); ADR-D-0079 (the protection of the goal condition, with the clause from ADR-D-0014) |
  | ADR-D-0029 | ADR-D-0080 (continuation is judged by a party other than the optimizer); ADR-D-0081 (uncertainty resolves against continuing) |
  | ADR-D-0063 | ADR-D-0082 (the value audit covers a goal run throughout); ADR-D-0083 (the audit's evidence stays apart from the assessor's); ADR-D-0084 (an item the audit holds stops the loop) |
  | ADR-D-0066 | ADR-D-0085 (forbidden actions are judged by a criterion); ADR-D-0086 (the loop never changes its own envelope) |

- Readings file: `docs/coding-agent/plans/active/decision-records-at-intent-altitude-readings.md`.
- Research: the census is this plan's research. `Research waived: the census covers the four records line by line, and each Worker checks its record again before writing.`

## Open Questions (max 3)
- None. Settled by the owner on 2026-11-11 (brief, Directed during the run): ADR-D-0076 is accepted together with the record of this unit that holds the clause removed from it, not before. Its acceptance stays outside this plan.

## Assumptions
- The census's counts hold. Where a Worker's test gives another count for its record, it writes nothing for that record and reports; the Orchestrator re-scopes and renumbers.

## Tasks

### Task_1: ADR-D-0011
- type: docs
- owns:
  - docs/coding-agent-orchestration-harness/decisions/ADR-D-0077-*.md
  - docs/coding-agent-orchestration-harness/decisions/ADR-D-0078-*.md
  - docs/coding-agent-orchestration-harness/decisions/ADR-D-0079-*.md
- depends_on: []
- description: |
  Check ADR-D-0011 again against the standard and read it by the owner's test. For each decision the test finds and the admission test admits, propose a new complete record, numbered as the Context table gives. Decide by the test whether the clause that came out of ADR-D-0076 belongs with the protection of the goal condition, and carry it there if it does.
- acceptance:
  - Before writing, the record gets its outcome and the test's result clause by clause. Where the count differs from the Context table, or the clause from ADR-D-0014 does not belong with the goal's protection by the test, nothing is written and the report says what was found.
  - Each new record states one decision of the old record and nothing else, so that any rewording of the plugin's text that preserves it stays valid; no exact mechanics; the title states the decision; no wording names a thing by its position, order or relation to something else. Between them the new records carry everything the old record decided, once.
  - Each Why is prose, present tense, a sentence or two, built from the old record's own reasons, with its source named in the report. Every rejected alternative carries why it lost and its reopen condition or an outright rejection. Where a reason or a reopen condition is written nowhere, the Worker invents nothing: it reports the gap under questions and does not write that record.
  - The new template's form: no Invariant line; Validation says only what would show the decision broken. Status proposed; `supersedes` names every old record the new one replaces in part (ADR-D-0079 names ADR-D-0014 as well as ADR-D-0011 if it carries that clause); `consulted` carries over the old entries and adds the writing model; filename at most 109 characters.
  - The report accounts for every clause of the old record, and of the ADR-D-0014 clauses it takes: carried into a named new record; held by a named accepted record; left to plugin text quoted by file and line; or stated nowhere.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: from `plugins/coding-agent-orchestration-harness/`, `py -I scripts/validate_harness_package.py`, unpiped; from the root, a whitespace check of each new file against an empty one (`git diff --no-index --check /dev/null <file>`; exit 1 with no complaint is a pass); every filename a record cites exists.
  - kind: review
    required: true
    owner: reviewer
    detail: each new record against the standard, the owner's test and its old record; the decisions unchanged and every clause accounted for.

### Task_2: ADR-D-0029
- type: docs
- owns:
  - docs/coding-agent-orchestration-harness/decisions/ADR-D-0080-*.md
  - docs/coding-agent-orchestration-harness/decisions/ADR-D-0081-*.md
- depends_on: []
- description: |
  Check ADR-D-0029 again against the standard and read it by the owner's test. For each decision the test finds and the admission test admits, propose a new complete record, numbered as the Context table gives.
- acceptance:
  - Before writing, the record gets its outcome and the test's result clause by clause. Where the count differs from the Context table, nothing is written and the report says what was found.
  - Each new record states one decision of the old record and nothing else, so that any rewording of the plugin's text that preserves it stays valid; no exact mechanics; the title states the decision; no wording names a thing by its position, order or relation to something else. Between them the new records carry everything the old record decided, once.
  - Each Why is prose, present tense, a sentence or two, built from the old record's own reasons, with its source named in the report. Every rejected alternative carries why it lost and its reopen condition or an outright rejection. Where a reason or a reopen condition is written nowhere, the Worker invents nothing: it reports the gap under questions and does not write that record.
  - The new template's form: no Invariant line; Validation says only what would show the decision broken. Status proposed; `supersedes` names the old record; `consulted` carries over the old entries and adds the writing model; filename at most 109 characters.
  - The report accounts for every clause of the old record: carried into a named new record; held by a named accepted record; left to plugin text quoted by file and line; or stated nowhere.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: from `plugins/coding-agent-orchestration-harness/`, `py -I scripts/validate_harness_package.py`, unpiped; from the root, a whitespace check of each new file against an empty one (`git diff --no-index --check /dev/null <file>`; exit 1 with no complaint is a pass); every filename a record cites exists.
  - kind: review
    required: true
    owner: reviewer
    detail: each new record against the standard, the owner's test and its old record; the decisions unchanged and every clause accounted for.

### Task_3: ADR-D-0063
- type: docs
- owns:
  - docs/coding-agent-orchestration-harness/decisions/ADR-D-0082-*.md
  - docs/coding-agent-orchestration-harness/decisions/ADR-D-0083-*.md
  - docs/coding-agent-orchestration-harness/decisions/ADR-D-0084-*.md
- depends_on: []
- description: |
  Check ADR-D-0063 again against the standard and read it by the owner's test. For each decision the test finds and the admission test admits, propose a new complete record, numbered as the Context table gives.
- acceptance:
  - Before writing, the record gets its outcome and the test's result clause by clause. Where the count differs from the Context table, nothing is written and the report says what was found.
  - Each new record states one decision of the old record and nothing else, so that any rewording of the plugin's text that preserves it stays valid; no exact mechanics; the title states the decision; no wording names a thing by its position, order or relation to something else. Between them the new records carry everything the old record decided, once.
  - Each Why is prose, present tense, a sentence or two, built from the old record's own reasons, with its source named in the report. Every rejected alternative carries why it lost and its reopen condition or an outright rejection. Where a reason or a reopen condition is written nowhere, the Worker invents nothing: it reports the gap under questions and does not write that record.
  - The new template's form: no Invariant line; Validation says only what would show the decision broken. Status proposed; `supersedes` names the old record; `consulted` carries over the old entries and adds the writing model; filename at most 109 characters.
  - The report accounts for every clause of the old record: carried into a named new record; held by a named accepted record; left to plugin text quoted by file and line; or stated nowhere.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: from `plugins/coding-agent-orchestration-harness/`, `py -I scripts/validate_harness_package.py`, unpiped; from the root, a whitespace check of each new file against an empty one (`git diff --no-index --check /dev/null <file>`; exit 1 with no complaint is a pass); every filename a record cites exists.
  - kind: review
    required: true
    owner: reviewer
    detail: each new record against the standard, the owner's test and its old record; the decisions unchanged and every clause accounted for.

### Task_4: ADR-D-0066
- type: docs
- owns:
  - docs/coding-agent-orchestration-harness/decisions/ADR-D-0085-*.md
  - docs/coding-agent-orchestration-harness/decisions/ADR-D-0086-*.md
- depends_on: []
- description: |
  Check ADR-D-0066 again against the standard and read it by the owner's test. For each decision the test finds and the admission test admits, propose a new complete record, numbered as the Context table gives.
- acceptance:
  - Before writing, the record gets its outcome and the test's result clause by clause. Where the count differs from the Context table, nothing is written and the report says what was found.
  - Each new record states one decision of the old record and nothing else, so that any rewording of the plugin's text that preserves it stays valid; no exact mechanics; the title states the decision; no wording names a thing by its position, order or relation to something else. Between them the new records carry everything the old record decided, once.
  - Each Why is prose, present tense, a sentence or two, built from the old record's own reasons, with its source named in the report. Every rejected alternative carries why it lost and its reopen condition or an outright rejection. Where a reason or a reopen condition is written nowhere, the Worker invents nothing: it reports the gap under questions and does not write that record.
  - The new template's form: no Invariant line; Validation says only what would show the decision broken. Status proposed; `supersedes` names the old record; `consulted` carries over the old entries and adds the writing model; filename at most 109 characters.
  - The report accounts for every clause of the old record: carried into a named new record; held by a named accepted record; left to plugin text quoted by file and line; or stated nowhere.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: from `plugins/coding-agent-orchestration-harness/`, `py -I scripts/validate_harness_package.py`, unpiped; from the root, a whitespace check of each new file against an empty one (`git diff --no-index --check /dev/null <file>`; exit 1 with no complaint is a pass); every filename a record cites exists.
  - kind: review
    required: true
    owner: reviewer
    detail: each new record against the standard, the owner's test and its old record; the decisions unchanged and every clause accounted for.

## Task Waves (explicit parallel dispatch sets)
- Wave 1: Task_1, Task_2, Task_3, Task_4 (owns disjoint).

## Rollback / Safety
- Nothing accepted is touched: the new records are proposed files, and removing them restores the folder. If a record is not written or a count changes, the Orchestrator renumbers before review so that no number is skipped within the pull request, and repairs the citations between the new records.

## Progress Log (append-only)
- 2026-11-11T08:45Z Plan review requested of the Codex seat `agent-harness-reviewer` over agmsg. 08:47Z CHANGES REQUESTED, BUNDLE-P1; 08:48Z CHANGES REQUESTED on the revision, BUNDLE-R1; 08:50Z APPROVED at 317bf68, no findings remain. The changes are in the Decision Log.
- 2026-11-11T08:51Z The reading is written in the readings file before the plan-draft audit is dispatched.

## Decision Log (append-only; re-plans and major discoveries)
- 2026-11-11 Plan review (Codex review seat): CHANGES REQUESTED at 43dc34c, one minor finding. BUNDLE-P1: the Design said a changed count disturbs only one Worker's range, which the plan's own rule against skipped numbers makes false. The comparison now states the cost: later numbers move and every citation between the new records is repaired by the Orchestrator before review, checked by meaning.
- 2026-11-11 Second plan review: BUNDLE-P1 closed; BUNDLE-R1 (minor): Open Questions still called the timing of ADR-D-0076's acceptance open, which the brief's entry committed since then settles. Replaced with the settled dependency.

## Notes (Risks / Edge cases)
- The owner's test may find a count other than the census's for any of the four; the census was made before the test was stated. The plan's numbers are a starting assignment, not a requirement.
- ADR-D-0063, 0066 were accepted on 2026-11-07 and 2026-11-11 and are close to the standard's form; the work on them is the split, not the altitude.
- The new records cite each other across old records (the audit's stop names the remedy exception, ADR-D-0067; the stall record names who judges it). A citation to a sibling of another Worker uses the number in the Context table and is repaired by the Orchestrator if numbers change.
