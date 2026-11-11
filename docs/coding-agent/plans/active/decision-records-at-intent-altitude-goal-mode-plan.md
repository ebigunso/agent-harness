# Plan: Decision records at intent altitude, the goal-mode records rewritten at the same decision

- status: authorized 2026-11-11 by the brief route (plan review closed, plan-draft audit holds nothing); in execution
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
- 2026-11-11T07:24Z Value audit dispatched (Claude subagent `harness-auditor` on Fable, a new dispatch), text verbatim:
  You are the value auditor. Read references/value-audit-mandate.md of the orchestration-harness skill and follow it exactly. Position: plan draft. Plan: <worktree>/docs/coding-agent/plans/active/decision-records-at-intent-altitude-goal-mode-plan.md. Governing brief: <worktree>/docs/coding-agent/briefs/active/decision-records-at-intent-altitude-brief.md. Changes since: none.
- 2026-11-11T07:30Z Verdict as returned (machine paths shortened; the two comparison lines are in the readings file):
  Verdict: no item is `ask-now` and none is `ungraded`. Six lines are `inferred` (none marked `direction`), the rest `cited` or `not audited`.
  The dispatch matched the fixed template. The mandate was the first file content opened: a guessed path failed, and two name-only listings located it. The readings file was opened once, after the grades were fixed.
  Paths held back before grading: every `*-notes.md` (never opened), including `docs/coding-agent/briefs/active/decision-records-at-intent-altitude-notes.md`, and `docs/coding-agent/plans/active/decision-records-at-intent-altitude-readings.md`.
  ## Verdict record
  Position: plan draft
  Documents read:
  - `docs/coding-agent/briefs/active/decision-records-at-intent-altitude-brief.md`
  - `docs/coding-agent/plans/active/decision-records-at-intent-altitude-goal-mode-plan.md` (the artifact)
  - `docs/coding-agent/rules/common.md` (pointer lines and Standing Approvals; working tree clean, so as at HEAD 8760dcd)
  - Read to understand, not as support: `plugins/coding-agent-orchestration-harness/skills/durable-docs-authoring/references/adr.md` and `docs/coding-agent-orchestration-harness/decisions/ADR-D-0009-goal-mode-as-second-operating-mode.md`
  Product basis: brief in the product owner's words ("product basis: the product owner's own words in this brief").
  Not audited: the engineering side has no document. `common.md` reads "Engineering philosophy: none yet", which is not a pointer line. There is no product philosophy either ("none yet"); the product side is graded on the brief.
  Missing inputs: none.
  Value documents changed in range: none (plan draft, no range).
  Items:
  1. DoD 1, each of the five checked again and the result recorded in the run record, five outcomes | maps to the brief | cited | Brief: "Every accepted record in `docs/coding-agent-orchestration-harness/decisions/` is checked against the standard the plugin already carries"; "The check's result for every record is recorded: meets, rewritten (to which), split (into which), retired (material where), or raised."; "where a check finds a decision itself wrong, stale or contradicted, that is a value question for the owner through Counsel, not a rewrite." The outcome "operational only (reported, nothing written)" defers the brief's retire-and-place to a re-scope and does not settle it. | -
  2. DoD 2, a new complete proposed record for each record confirmed as one admitted decision | maps to the brief | cited | Brief: "A record that fails the check is rewritten to meet it, under the standard's own lifecycle: a new complete record, the old one retired, accepted by name." (tagged inferred, ratified with the brief on 2026-11-02) | -
  3. DoD 3, no decision's outcome changes | maps to the brief | cited | Brief: "The decisions themselves do not change. The work moves altitude, not outcome" | -
  4. DoD 4, every clause accounted for; a clause the plugin states nowhere holds the retirement until the Orchestrator settles where it goes | maps to the brief | inferred | Extends brief: "a record found to carry only operational material is retired and its material placed in the rule or skill text that already states it, or added there"; scenario 1, "with the route left to the plugin text". Cheap to undo: a report and a held retirement. | -
  5. DoD 5, each new record's `consulted` names the models consulted and the writing model | maps to the brief | inferred | Extends brief (told 2026-11-11): "Each of the two records names, in its `consulted` field, the model he talked with about the decision and the model that wrote the record." The line the plan cites ("The same holds of every record this run writes after these two") is tagged inferred, was added after ratification and has no ratification record of its own, so it is no support; the grade does not rest on it. Cheap to undo: a front-matter field in a proposed file. | -
  6. DoD 6, the plan ends with records proposed, branch reviewed, audits logged; retires nothing, accepts nothing | maps to the brief | cited | Brief: "it goes in once the closeout audit has confirmed, record by record, that its decision is unchanged"; "Acceptance is by name, as the standard says". The item tightens. | -
  7. DoD 7, a following change of its own with its own review and closeout audit before anything is published: audit-confirmed rewrites marked accepted, old records retired, references repaired, the owner given the list; an unconfirmed record reaches him by name | maps to the brief | cited | Brief: "A rewrite that does not materially change what its decision is about goes in without his reading it."; "Such a rewrite does not wait for a statement of his naming it: it goes in once the closeout audit has confirmed, record by record, that its decision is unchanged, and he is given the list afterwards. This departs, for this run only, from the record standard's rule"; for the unconfirmed record, "Acceptance is by name, as the standard says". Publication passes step 1 on `common.md` Standing Approvals: "A finished, reviewed run may publish its branch and open pull requests in this repository without asking first. Merges are not covered and wait for the owner.", with its record "Given and accepted by the repository's owner, ebigunso, on 2026-09-30, relayed by Counsel: \"The common rule proposed, accepted.\"", committed at HEAD. Whether the quoted words were said is not something a file can show. The item states no merge. | -
  8. Planner-added 1, the Worker's report accounts for every clause | maps to the brief | inferred | Extends the same statements as item 4, and "once the closeout audit has confirmed, record by record, that its decision is unchanged". Cheap to undo. | -
  9. Planner-added 2, `consulted` carries over the old record's entries and adds the writing model | maps to the brief | inferred | Extends brief (told 2026-11-11): "the model he talked with about the decision and the model that wrote the record". Reading "the models consulted on the decision" as the old record's entries is the plan's. Cheap to undo. | -
  10. Non-goal, the four goal-mode bundles (the area's second unit) | maps to the brief | inferred | Same decision as item 20; extends "The rest reaches him in batches by area, each batch its own pull request and its own acceptance, of about ten records." Not graded here: the second unit taking ADR-D-0063 and 0066, which the constraint of 2026-11-02 lists. The brief's line that the constraint "now leaves no record out" is tagged inferred with no ratification record of its own. | -
  11. Non-goal, the other three areas | maps to the brief | cited | Brief: "The rest reaches him in batches by area, each batch its own pull request and its own acceptance" | -
  12. Non-goal, any change to a decision | maps to the brief | cited | Brief: "The decisions themselves do not change." | -
  13. Non-goal, marking accepted, retiring and reference repair (left to the following change) | maps to the brief | cited | As item 7: "it goes in once the closeout audit has confirmed, record by record, that its decision is unchanged" | -
  14. Non-goal, the record standard and its template; the census's two observations go to the owner as a question with this unit's report | maps to the brief | cited | Brief: "that is reported to the owner through Counsel as a value question; the standard is not changed by this work without his word." The brief's route is through Counsel; the plan says "to the owner". | -
  15. Non-goal, plugin text | maps to the brief | inferred | Extends "its material placed in the rule or skill text that already states it, or added there" by deferring any adding to a re-scope (item 4 holds the retirement meanwhile). Cheap to undo. | -
  16. Assumption, the census's classification holds; where a Worker's check differs it writes nothing and reports | maps to the brief | cited | Brief: "Every accepted record ... is checked against the standard the plugin already carries" | -
  17. Task_1 (ADR-D-0009, 0014, 0028 to proposed ADR-D-0073 to 0075), its record-content acceptance | maps to the brief | cited | Brief: "one decision per record; the constraint stated so that any rewording of the plugin text that preserves it stays valid; the why in prose at intent altitude; exact mechanics ... not covered"; "names the thing it means rather than its position, order or relation to something else"; "a new complete record"; pass condition "a reader can state what it decides in one sentence from its title". Its `consulted` clause is item 9 and its reason-written-nowhere clause is item 24. | -
  18. Task_2 (ADR-D-0031, 0067 to proposed ADR-D-0076, 0077), its record-content acceptance | maps to the brief | cited | Same statements as item 17. | -
  19. Tasks' validation items, owns globs, filename length, Wave 1 | internal mechanics | not audited | - | -
  20. Decision Log 1, the area is two units: five rewrites, then the four bundles | maps to the brief | inferred | Extends "in batches by area, each batch its own pull request and its own acceptance, of about ten records", and the two acceptance routes ("goes in without his reading it"; "Acceptance is by name"). No statement says an area is divided by acceptance route, and a batch of five is the plan's. Cheap to undo. | -
  21. Decision Log 1, acceptance, retirement and reference repair leave the plan as a change of its own with its own review and audit | maps to the brief | cited | As item 7. | -
  22. Decision Log 1, an outcome before writing; a new record only if the admission test passes | maps to the brief | cited | Brief: "checked against the standard the plugin already carries"; "under the standard's own lifecycle" | -
  23. Decision Log 1, a changed count re-scoped and never written outside owns; each task carries its own validation | internal mechanics | not audited | - | -
  24. Decision Log 2, where a reason or reopen condition is written nowhere the Worker invents nothing and the record waits until the Orchestrator has the reason settled and logged | maps to the brief | inferred | Extends "The decisions themselves do not change" and "the why in prose at intent altitude". The brief has no statement on a reason written nowhere, and the record standard is not a value document. Cheap to undo: nothing is written. The plan does not say who settles such a reason. That settling, when it happens, is a Decision Log ruling graded at the next audit, and a record whose reason comes from outside its old record is one the old record does not show to be unchanged. | -
  Human-only conditions pending: none. The brief's two pass conditions carry no agent-checkable or human-only mark.
  Scenarios: none
- Acting on the verdict: nothing is held and nothing is ungraded, so the plan is authorized by the brief route. Taken from the verdict: the reading of a reason written nowhere is corrected to extends; a reason settled from outside an old record makes that record one the run cannot show unchanged, so it reaches him by name; the census's observations on the template go through Counsel.

## Decision Log (append-only; re-plans and major discoveries)
- 2026-11-11 Plan review (Codex review seat) returned CHANGES REQUESTED on the first draft, which held all nine goal-mode records and fifteen new ones in one unit, with acceptance and retirement as a task after the closeout audit. Changed: the area is two units and this plan holds the five rewrites (GM-P6, GM-P2); acceptance, retirement and reference repair leave the plan and follow it as a change of its own with its own review and audit (GM-P5, and the absence search's scope with it, GM-P7); each record gets an outcome before writing and a new record is proposed only if the admission test passes (GM-P3); a changed count is reported and re-scoped, never written outside owns (GM-P4); each task carries its own validation items (GM-P1).
- 2026-11-11 Second plan review: GM-P1 to GM-P7 closed; GM-R1 raised on the revision, which had a Worker list what it derived where a reason is written nowhere. Changed to the standard's route: the Worker reports the gap and invents nothing, and the record waits until the reason is settled and recorded here.

## Notes (Risks / Edge cases)
- A rewrite judged "same decision" by its writer may shift the decision's reach by a changed word. The clause account, the review against the old record and the closeout audit's record-by-record confirmation are the three checks; a record any of them cannot confirm reaches the owner by name.
- ADR-D-0067 was accepted within the week and is close to the standard already; its check may find it meets the standard, in which case nothing is written for it.
