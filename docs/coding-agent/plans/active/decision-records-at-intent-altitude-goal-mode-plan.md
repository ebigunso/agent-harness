# Plan: Decision records at intent altitude, the goal-mode records

- status: draft 2026-11-11
- generated: 2026-11-11
- last_updated: 2026-11-11
- work_type: docs

## Goal
- Bring the nine accepted records on goal mode to the record standard, under the governing brief `docs/coding-agent/briefs/active/decision-records-at-intent-altitude-brief.md`: ADR-D-0009, 0011, 0014, 0028, 0029, 0031, 0063, 0066 and 0067. The decisions do not change; the records move altitude.
- The brief is the requirement and is not restated here; where this plan and the brief differ, the brief governs and the difference is a plan defect.
- This is the first unit by area of the run recorded in `docs/coding-agent/plans/active/decision-records-at-intent-altitude-run.md`. The census of 2026-11-10 classed five of the nine as a rewrite at the same decision (0009, 0014, 0028, 0031, 0067) and four as holding more than one decision (0011 three, 0029 two, 0063 three, 0066 two). Those classifications are the Researcher's and are checked again by this plan before anything is written from them.

## Definition of Done
- Each of the nine records is checked again against the standard, and the check's result is recorded in the run record: rewritten (to which), split (into which), or, where the check disagrees with the census, what it found instead (brief, the second pass condition).
- Each record the check confirms as a rewrite at the same decision has a new complete record that states that decision at intent altitude; each record it confirms as a bundle has one new record for each decision it holds (brief, "What the work gives", the third entry).
- No decision's outcome changes. Where the check finds a decision stale, contradicted, or not separable as the census says, nothing is written for it and it goes to the owner through Counsel (brief, the constraint on decisions; scenario 4).
- Every clause of each old record is accounted for: carried into a new record, or left to plugin text that the report shows already states it. Operational material the plugin does not state anywhere is reported, not dropped and not added by this plan's Workers.
- Acceptance follows the brief's entry of 2026-11-11: a rewrite at the same decision goes in once the closeout audit has confirmed, record by record, that its decision is unchanged, and the owner is given the list afterwards; a record that comes of a split, and any record the run cannot show to keep its decision, reaches him by name.
- An old record is retired only when its replacements are accepted: in one operation, with inbound references repaired and an absence search.
- The new records' numbers run from ADR-D-0073 with no gap within this pull request.
- Each new record's `consulted` field names the models consulted on the decision and the model that wrote the record (brief, Directed during the run, the last entry).
- Package validators and smoke tests pass; the branch has Reviewer `APPROVED`; value audits at plan draft and closeout are logged; the unit is reported: branch published, pull request opened under the standing approval, note to Counsel, nothing merged.

## Planner-added requirements
- Every clause of each old record is accounted for in the Worker's report. Needed because: the brief has operational material stay in, or be placed in, the rule or skill text, and a rewrite that silently dropped a clause the plugin does not state would lose it; the account is also what lets the closeout audit confirm, record by record, that a decision is unchanged.
- The `consulted` field carries over the old record's entries and adds the writing model. Needed because: the brief asks for the models he talked with and the model that wrote the record; for a record rewritten at the same decision the models consulted on the decision are those the old record names.

## Scope / Non-goals
- Scope: new proposed records under `docs/coding-agent-orchestration-harness/decisions/`, numbered from ADR-D-0073; at acceptance, the retirement of the nine old records and the repair of references to them, wherever they are.
- Non-goals: the other three areas' records; any change to a decision; the record standard and its template (the census's two observations on the template go to the owner as a question with this unit's report); plugin text, unless the check shows material that must be placed there, which is then a change of its own put to the Orchestrator first.

## Design
- Chosen: each old record is replaced by new complete records under the standard's lifecycle, as the brief fixes; the nine are divided among three Workers by how they are classed, so that a Worker holds neighbouring decisions together; no alternative.

## Compatibility stance
- migrate. The records' filenames are cited by other records' front matter and by text in the repository; every such citation is locatable by search and is repaired in the same operation that retires a record. No consumer outside the repository reads a record's filename that any accessible source shows.

## Context (workspace)
- The standard: `plugins/coding-agent-orchestration-harness/skills/durable-docs-authoring/references/adr.md`, with its template.
- The plugin text the goal-mode records mirror, by the census: `skills/orchestration-harness/references/goal-mode.md`, `goal-assessor-mandate.md`, `goal-templates.md`, `value-level-operation.md`, and `skills/orchestration-harness/SKILL.md` (Plan Gate).
- Two records written to the standard in this run, accepted 2026-11-11, show the form: ADR-D-0071 and ADR-D-0072.
- Readings file: `docs/coding-agent/plans/active/decision-records-at-intent-altitude-readings.md`.
- Research: the census is this plan's research; `Research waived: the census covers the nine records line by line, and each Worker checks its records again before writing`.

## Open Questions (max 3)
- None.

## Assumptions
- The census's counts hold (five rewrites, four splits into ten), giving fifteen new records, ADR-D-0073 to ADR-D-0087. Where a Worker's check gives another count, the Orchestrator renumbers before review so that no number is skipped.
- Ten of the fifteen reach the owner by name, which is the "about ten" the brief asks a batch to be; the five rewrites reach him as a list.

## Tasks

### Task_1: The five records rewritten at the same decision
- type: docs
- owns:
  - docs/coding-agent-orchestration-harness/decisions/ADR-D-0073-*.md to ADR-D-0077-*.md (new proposed records only)
- depends_on: []
- description: |
  Check ADR-D-0009, 0014, 0028, 0031 and 0067 again against the standard, then write one new complete record for each that the check confirms holds one decision: ADR-D-0073 (for 0009), 0074 (0014), 0075 (0028), 0076 (0031), 0077 (0067).
- acceptance:
  - Each new record states the old record's decision and nothing else: one decision, tested with every neighbouring decision held fixed; the constraint stated so that any rewording of the plugin's text that preserves it stays valid; no exact mechanics.
  - Each Why is prose, present tense, a sentence or two, the fork and the reason one branch won, built from the old record's own reasons; every rejected alternative carries its reopen condition or is rejected outright with why it lost; no wording names a thing by its position, order or relation to something else; the title states the decision.
  - Status proposed; `supersedes` names the old record; `consulted` carries over the old record's entries and adds the model writing the record; filename at most 109 characters.
  - The report accounts for every clause of each old record: carried into the new record, or left to plugin text quoted by file and line. Material the plugin states nowhere is reported and not dropped silently.
  - Where the check finds more than one decision, a decision no longer true, or a reason written nowhere, nothing is invented and the record is not written: the report says what was found.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: from `plugins/coding-agent-orchestration-harness/`, `py -I scripts/validate_harness_package.py`; from the root, a whitespace check of each new file against an empty one (`git diff --no-index --check /dev/null <file>`, exit 1 with no complaint is a pass); every filename a record cites exists.
  - kind: review
    required: true
    owner: reviewer
    detail: each record against the standard and against its old record, decision unchanged.

### Task_2: ADR-D-0011 and ADR-D-0029 split
- type: docs
- owns:
  - docs/coding-agent-orchestration-harness/decisions/ADR-D-0078-*.md to ADR-D-0082-*.md (new proposed records only)
- depends_on: []
- description: |
  Check ADR-D-0011 and ADR-D-0029 again against the standard, then write one new complete record for each decision the check confirms they hold. By the census: ADR-D-0011 holds three (progress refers only to the goal; what counts as a stall; who may tighten or loosen how progress is read), ADR-D-0078 to 0080; ADR-D-0029 holds two (continuation is judged by a party other than the optimizer; uncertainty resolves against continuing), ADR-D-0081 and 0082.
- acceptance:
  - As Task_1's first four bullets, for each new record; each record names the other records that come of the same old record as not covered.
  - The split is tested, not assumed: each new record could be retired with the others held fixed. Where two of the census's decisions cannot stand apart, or the check finds a different number, the report says so and writes the number the test supports.
  - Between them the new records carry everything the old record decided, once.
- validation:
  - as Task_1.

### Task_3: ADR-D-0063 and ADR-D-0066 split
- type: docs
- owns:
  - docs/coding-agent-orchestration-harness/decisions/ADR-D-0083-*.md to ADR-D-0087-*.md (new proposed records only)
- depends_on: []
- description: |
  Check ADR-D-0063 and ADR-D-0066 again against the standard, then write one new complete record for each decision the check confirms they hold. By the census: ADR-D-0063 holds three (the value audit covers a goal run throughout; the audit's evidence stays apart from the continuation assessment; a held item stops the whole loop, subject to ADR-D-0067), ADR-D-0083 to 0085; ADR-D-0066 holds two (forbidden actions are judged by a criterion, not a list; the loop cannot change its own envelope), ADR-D-0086 and 0087.
- acceptance:
  - As Task_2.
  - Where a new record must name the record that replaces ADR-D-0067, it names ADR-D-0077.
- validation:
  - as Task_1.

### Task_4: Acceptance, retirement and references (Orchestrator)
- type: chore
- owns:
  - docs/coding-agent-orchestration-harness/decisions/ (status fields, the nine old records, `superseded/`)
  - every file that cites one of the nine old records' filenames or names it as the record in force
- depends_on: [Task_1, Task_2, Task_3]
- description: |
  After the closeout audit: mark accepted the rewrites whose decision it confirms unchanged and retire their old records; give the owner the list. The records that come of a split wait for his acceptance by name, and their old records are retired then. Each retirement is one operation with references repaired and an absence search.
- acceptance:
  - No old record is retired before every record that replaces it is accepted.
  - No number is skipped among the new records.
  - After each retirement, a search for the old filename finds nothing outside the run's own plan, changes and readings files.
- validation:
  - kind: command
    required: true
    owner: orchestrator
    detail: `py -I scripts/validate_harness_package.py`, `py -I scripts/run_validation_smoke_tests.py`, `git diff --check`, and the absence searches.

## Task Waves (explicit parallel dispatch sets)
- Wave 1: Task_1, Task_2, Task_3 (owns disjoint).
- Wave 2: Task_4, after review and the closeout audit.

## Rollback / Safety
- Until Task_4 nothing accepted is touched: the new records are proposed files and removing them restores the folder. A retirement is undone by moving the file back and restoring its status and references, from the commit that made it.

## Progress Log (append-only)

## Decision Log (append-only; re-plans and major discoveries)

## Notes (Risks / Edge cases)
- A rewrite judged "same decision" by its writer may shift the decision's reach by a changed word. The clause account, the review against the old record and the closeout audit's record-by-record confirmation are the three checks; a record any of them cannot confirm reaches the owner by name.
- ADR-D-0063, 0066 and 0067 were accepted within the week; their text is close to the standard already and their rewrites may be small.
