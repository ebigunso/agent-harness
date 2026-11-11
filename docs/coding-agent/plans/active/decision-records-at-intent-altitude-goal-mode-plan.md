# Plan: Decision records at intent altitude, the goal-mode records rewritten at the same decision

- status: draft 2026-11-11 (revised after plan review GM-P1 to GM-P7 and GM-R1)
- generated: 2026-11-11
- last_updated: 2026-11-11
- work_type: docs

## Goal
- Bring to the record standard the five accepted goal-mode records the census classed as holding one decision that needs rewriting: ADR-D-0009, 0014, 0028, 0031 and 0067, under the governing brief `docs/coding-agent/briefs/active/decision-records-at-intent-altitude-brief.md`. The decisions do not change; the records move altitude.
- The brief is the requirement and is not restated here; where this plan and the brief differ, the brief governs and the difference is a plan defect.
- This is the first of two units for the goal-mode area in the run recorded in `docs/coding-agent/plans/active/decision-records-at-intent-altitude-run.md`. The second unit takes the four records the census classed as bundles (ADR-D-0011, 0029, 0063, 0066; ten records by its count) and has its own plan and pull request. The census's classifications are the Researcher's and are checked again here before anything is written from them.

## Definition of Done
- Each of the five records is checked again against the standard, and the check's result is recorded in the run record (brief, the second pass condition): rewritten (to which); meets the standard (nothing written); holds more than one decision (moved to the area's second unit); operational only (reported, nothing written); or its decision stale or contradicted (to the owner through Counsel, nothing written).
- For each record the check confirms as one decision that the standard's admission test admits, a new complete proposed record states that decision at intent altitude (brief, "What the work gives", the third entry).
- No decision's outcome changes (brief, the constraint on decisions).
- Every clause of each old record is accounted for: carried into the new record, or left to plugin text that the report quotes by file and line. Where the plugin states a clause nowhere, the old record is not ready to be retired: the gap is reported and the Orchestrator settles where the material goes before any retirement.
- Each new record's `consulted` field names the models consulted on the decision and the model that wrote the record (brief, Directed during the run, the last entry).
- This plan ends with the new records proposed, the branch reviewed `APPROVED`, and value audits at plan draft and closeout logged. It retires nothing and marks nothing accepted.
- What follows the plan, as a change of its own in the run's changes file, with its own review and closeout audit before anything is published: the rewrites whose decision this plan's closeout audit confirmed unchanged, record by record, are marked accepted, their old records are retired with references repaired, and the owner is given the list (brief, the entry of 2026-11-11 on rewrites). A record the audit does not confirm reaches him by name instead.

## Planner-added requirements
- Every clause of each old record is accounted for in the Worker's report. Needed because: the brief has operational material stay in, or be placed in, the rule or skill text, and a rewrite that silently dropped a clause the plugin does not state would lose it; the account is also what lets the closeout audit confirm, record by record, that a decision is unchanged.
- The `consulted` field carries over the old record's entries and adds the writing model. Needed because: the brief asks for the models he talked with and the model that wrote the record; for a record rewritten at the same decision the models consulted on the decision are those the old record names, and a past consultation is not replaced by the present writer.

## Scope / Non-goals
- Scope: up to five new proposed records under `docs/coding-agent-orchestration-harness/decisions/`, ADR-D-0073 to ADR-D-0077.
- Non-goals: the four goal-mode bundles (the area's second unit); the other three areas; any change to a decision; marking a record accepted, retiring a record or repairing references (the change that follows this plan); the record standard and its template (the census's two observations on the template go to the owner as a question with this unit's report); plugin text.

## Design
- Fixed by the brief and the standard, and not compared: a record that fails the check is replaced by a new complete record and the old one retired; a record is never amended in place.
- The choice is how the nine goal-mode records are divided into units.
- Chosen: two units. This one holds the five rewrites at the same decision; the second holds the four bundles and their ten records. Each has its own plan, pull request and acceptance.
- Alternative: one unit of nine old records and fifteen new ones, in one pull request.
- structure: under the chosen design the two units touch disjoint old records, and the second unit's records may cite this unit's new numbers (ADR-D-0063's exception names ADR-D-0067), so this unit lands first; under the alternative that dependency sits inside one branch and needs no order.
- evolution: the chosen design keeps each batch at the size the brief asks for (about ten records): five, then ten. The alternative makes one batch of fifteen. A finding in one record holds back fewer others under the chosen design.
- verification: the chosen design pays for two plan reviews, two final reviews and two sets of audits; the alternative pays once. Under the chosen design each closeout audit confirms one kind of thing: here, that five decisions are unchanged; there, that four bundles are split truly.
- operation: no runtime cost under either.
- human: under the chosen design the owner gets a list of five he need not read, then ten records to accept by name; under the alternative he gets fifteen in one pull request, of two kinds, and must tell them apart.
- safety: neither changes a trust boundary. Under the chosen design the acceptance route that departs from the standard (unread rewrites) is confined to a pull request holding nothing else.
- Why chosen wins: the brief asks for batches of about ten, and the two kinds of record are accepted by two different routes; keeping each route in its own pull request is worth the second round of review and audit.

## Compatibility stance
- preserve, for this plan: it adds proposed files and changes no accepted record, filename or reference. The change that follows the plan retires records and repairs the references to their filenames; it states its own stance.

## Context (workspace)
- The standard: `plugins/coding-agent-orchestration-harness/skills/durable-docs-authoring/references/adr.md`, with its template; its Admission section holds the admission test.
- The plugin text these records mirror, by the census: `skills/orchestration-harness/references/goal-mode.md`, `goal-assessor-mandate.md`, `goal-templates.md`, `value-level-operation.md`, and `skills/orchestration-harness/SKILL.md` (Plan Gate).
- Two records written to the standard in this run, accepted 2026-11-11, show the form: ADR-D-0071 and ADR-D-0072.
- Readings file: `docs/coding-agent/plans/active/decision-records-at-intent-altitude-readings.md`.
- Research: the census is this plan's research. `Research waived: the census covers the five records line by line, and each Worker checks its records again before writing.`

## Open Questions (max 3)
- None.

## Assumptions
- The census's classification of the five holds. Where a Worker's check differs for a record, it writes nothing for that record and reports; the Orchestrator re-scopes.

## Tasks

### Task_1: ADR-D-0009, ADR-D-0014 and ADR-D-0028
- type: docs
- owns:
  - docs/coding-agent-orchestration-harness/decisions/ADR-D-0073-*.md
  - docs/coding-agent-orchestration-harness/decisions/ADR-D-0074-*.md
  - docs/coding-agent-orchestration-harness/decisions/ADR-D-0075-*.md
- depends_on: []
- description: |
  Check ADR-D-0009, ADR-D-0014 and ADR-D-0028 again against the standard. For each that the check confirms holds one decision, propose a new complete record if the admission test passes: ADR-D-0073 (for 0009), ADR-D-0074 (for 0014), ADR-D-0075 (for 0028).
- acceptance:
  - Before writing, each old record gets one of the outcomes in the Definition of Done. Only "one decision, admitted" leads to a new record; for any other outcome nothing is written for that record and the report says what was found and on what evidence.
  - Each new record states the old record's decision and nothing else, so that any rewording of the plugin's text that preserves it stays valid; no exact mechanics; the title states the decision; no wording names a thing by its position, order or relation to something else.
  - Each Why is prose, present tense, a sentence or two, the fork and the reason one branch won, built from the old record's own reasons; every rejected alternative carries its reopen condition or is rejected outright, with why it lost. A faithful restatement of a written reason, or what follows from one, is named in the report with its source. Where a reason or a reopen condition is written nowhere, the Worker invents nothing: it reports the gap under questions and does not write that record, which waits until the Orchestrator has the reason settled and recorded in the Decision Log.
  - Status proposed; `supersedes` names the old record; `consulted` carries over the old record's entries and adds the model writing the record; filename at most 109 characters.
  - The report accounts for every clause of each old record: carried into the new record, or left to plugin text quoted by file and line, or stated nowhere in the plugin.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: from `plugins/coding-agent-orchestration-harness/`, `py -I scripts/validate_harness_package.py`; from the root, a whitespace check of each new file against an empty one (`git diff --no-index --check /dev/null <file>`; exit 1 with no complaint is a pass); every filename a record cites exists.
  - kind: review
    required: true
    owner: reviewer
    detail: each new record against the standard and against its old record, the decision unchanged and every clause accounted for.

### Task_2: ADR-D-0031 and ADR-D-0067
- type: docs
- owns:
  - docs/coding-agent-orchestration-harness/decisions/ADR-D-0076-*.md
  - docs/coding-agent-orchestration-harness/decisions/ADR-D-0077-*.md
- depends_on: []
- description: |
  Check ADR-D-0031 and ADR-D-0067 again against the standard. For each that the check confirms holds one decision, propose a new complete record if the admission test passes: ADR-D-0076 (for 0031), ADR-D-0077 (for 0067).
- acceptance:
  - Before writing, each old record gets one of the outcomes in the Definition of Done. Only "one decision, admitted" leads to a new record; for any other outcome nothing is written for that record and the report says what was found and on what evidence.
  - Each new record states the old record's decision and nothing else, so that any rewording of the plugin's text that preserves it stays valid; no exact mechanics; the title states the decision; no wording names a thing by its position, order or relation to something else.
  - Each Why is prose, present tense, a sentence or two, the fork and the reason one branch won, built from the old record's own reasons; every rejected alternative carries its reopen condition or is rejected outright, with why it lost. A faithful restatement of a written reason, or what follows from one, is named in the report with its source. Where a reason or a reopen condition is written nowhere, the Worker invents nothing: it reports the gap under questions and does not write that record, which waits until the Orchestrator has the reason settled and recorded in the Decision Log.
  - Status proposed; `supersedes` names the old record; `consulted` carries over the old record's entries and adds the model writing the record; filename at most 109 characters.
  - The report accounts for every clause of each old record: carried into the new record, or left to plugin text quoted by file and line, or stated nowhere in the plugin.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: from `plugins/coding-agent-orchestration-harness/`, `py -I scripts/validate_harness_package.py`; from the root, a whitespace check of each new file against an empty one (`git diff --no-index --check /dev/null <file>`; exit 1 with no complaint is a pass); every filename a record cites exists.
  - kind: review
    required: true
    owner: reviewer
    detail: each new record against the standard and against its old record, the decision unchanged and every clause accounted for.

## Task Waves (explicit parallel dispatch sets)
- Wave 1: Task_1, Task_2 (owns disjoint).

## Rollback / Safety
- Nothing accepted is touched: the new records are proposed files, and removing them restores the folder. If a record is not written, the Orchestrator renumbers the rest before review so that no number is skipped within the pull request.

## Progress Log (append-only)
- 2026-11-11T07:13Z Plan review requested of the Codex seat `agent-harness-reviewer` over agmsg. 07:18Z CHANGES REQUESTED, GM-P1 to GM-P7; 07:21Z CHANGES REQUESTED on the revision, GM-R1; 07:22Z APPROVED at 51c442f, no findings remain. The changes are in the Decision Log.
- 2026-11-11T07:24Z The reading is written in the readings file before the plan-draft audit is dispatched.

## Decision Log (append-only; re-plans and major discoveries)
- 2026-11-11 Plan review (Codex review seat) returned CHANGES REQUESTED on the first draft, which held all nine goal-mode records and fifteen new ones in one unit, with acceptance and retirement as a task after the closeout audit. Changed: the area is two units and this plan holds the five rewrites (GM-P6, GM-P2); acceptance, retirement and reference repair leave the plan and follow it as a change of its own with its own review and audit (GM-P5, and the absence search's scope with it, GM-P7); each record gets an outcome before writing and a new record is proposed only if the admission test passes (GM-P3); a changed count is reported and re-scoped, never written outside owns (GM-P4); each task carries its own validation items (GM-P1).
- 2026-11-11 Second plan review: GM-P1 to GM-P7 closed; GM-R1 raised on the revision, which had a Worker list what it derived where a reason is written nowhere. Changed to the standard's route: the Worker reports the gap and invents nothing, and the record waits until the reason is settled and recorded here.

## Notes (Risks / Edge cases)
- A rewrite judged "same decision" by its writer may shift the decision's reach by a changed word. The clause account, the review against the old record and the closeout audit's record-by-record confirmation are the three checks; a record any of them cannot confirm reaches the owner by name.
- ADR-D-0067 was accepted within the week and is close to the standard already; its check may find it meets the standard, in which case nothing is written for it.
