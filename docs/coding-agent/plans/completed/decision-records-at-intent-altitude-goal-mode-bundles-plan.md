# Plan: Decision records at intent altitude, the goal-mode records that hold more than one decision

- status: done 2026-11-11 (review APPROVED; closeout audit holds nothing; eleven proposed records and ADR-D-0076 await the owner's acceptance by name)
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
- Scope: new proposed records under `docs/coding-agent-orchestration-harness/decisions/`, ADR-D-0077 to ADR-D-0087 (ADR-D-0077 to ADR-D-0086 by the census's count when the plan was drafted).
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
- The numbers and what each record holds, as the Workers' tests found and the Orchestrator renumbered on 2026-11-11 (the census had three for ADR-D-0063 and two for ADR-D-0066):

  | Old record | New records |
  | --- | --- |
  | ADR-D-0011 | ADR-D-0077 (progress refers only to the goal); ADR-D-0078 (what counts as a stall); ADR-D-0079 (the loop loosens no measure of its goal without its owner's word) |
  | ADR-D-0014, the clause taken out of ADR-D-0076 | ADR-D-0087 (the loop never changes its goal on its own) |
  | ADR-D-0029 | ADR-D-0080 (continuation is judged by a party other than the optimizer); ADR-D-0081 (uncertainty resolves against continuing) |
  | ADR-D-0063 | ADR-D-0082 (the value audit covers a goal run throughout, and an item it holds stops the loop); ADR-D-0083 (the audit's evidence stays apart from the assessor's) |
  | ADR-D-0066 | ADR-D-0084 (no goal loop starts without an authority envelope); ADR-D-0085 (forbidden actions are judged by a criterion); ADR-D-0086 (the loop never changes its own envelope) |

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
- 2026-11-11T08:51Z Value audit dispatched (Claude subagent `harness-auditor` on Fable, a new dispatch), text verbatim:
  You are the value auditor. Read references/value-audit-mandate.md of the orchestration-harness skill and follow it exactly. Position: plan draft. Plan: <worktree>/docs/coding-agent/plans/active/decision-records-at-intent-altitude-goal-mode-bundles-plan.md. Governing brief: <worktree>/docs/coding-agent/briefs/active/decision-records-at-intent-altitude-brief.md. Changes since: none.
- 2026-11-11T08:58Z Verdict as returned (machine paths shortened; the two comparison lines are in the readings file):
  Value audit verdict, plan draft. Nothing is held: no item is `ask-now` and none is `ungraded`. Three items are `inferred` (none marked `direction`), and four readings diverge.
  **Before the record**
  - **Audited tree:** the worktree, branch `feature/2026-11-11/decision-records-goal-mode-bundles`, clean at f73b617.
  - **Dispatch:** it matched the fixed template. The other text in context was the harness's reminder on how to return this report, a session hook on coding style, the memory index and a git status snapshot of the main checkout. None of it says anything about this work.
  - **First step, departures:**
    - My first call was a Read of the mandate at a guessed path in the main checkout, which does not exist. One Glob then returned the mandate's file name, and I read it from the audited worktree's copy.
    - Several Read calls were sent in one block, each on one named path. No command printed more than one file, and no git command printed content.
    - One Grep printed the headings of the changes file, so that I could read the section the plan names.
    - That section ("ADR-D-0076 narrowed to the examination"), read to its end, includes an earlier audit's logged verdict. I took nothing from it as support.
  - **Notes and readings:** no notes file was opened. The readings file was opened once, after the grades were fixed, and no grade changed afterwards.
  **Verdict record**
  Position: plan draft
  Documents read:
  - `docs/coding-agent/briefs/active/decision-records-at-intent-altitude-brief.md`
  - `docs/coding-agent/rules/common.md` (pointer lines and Standing Approvals, at HEAD)
  - `docs/coding-agent/plans/active/decision-records-at-intent-altitude-goal-mode-bundles-plan.md` (the artifact, claims under review)
  - Read to understand the plan, not as support: ADR-D-0011, ADR-D-0014, ADR-D-0029, ADR-D-0063, ADR-D-0066 and ADR-D-0076 at HEAD; `durable-docs-authoring/references/adr.md`; the changes file's section "ADR-D-0076 narrowed to the examination".
  Product basis: brief in the product owner's words ("product basis: the product owner's own words in this brief. ebigunso owns the harness")
  Not audited: the engineering side. `common.md` reads "Engineering philosophy: none yet", so it has no document. The product philosophy line also reads "none yet"; the product side is graded on the brief. (The main checkout lists an untracked `docs/engineering-philosophy.md`; no pointer line names it, so it is not a document for this audit.)
  Missing inputs: none
  Value documents changed in range: none (plan draft has no range)
  Statements quoted below, by short name. All are from the brief except the last.
  - **Checked:** "Every accepted record in `docs/coding-agent-orchestration-harness/decisions/` is checked against the standard the plugin already carries: one decision per record; the constraint stated so that any rewording of the plugin text that preserves it stays valid; the why in prose at intent altitude; exact mechanics (routes, moves, file names, admission of a relay, template fill-ins) not covered." (told 2026-11-02)
  - **Wording:** "The check also asks whether a record's wording names the thing it means rather than its position, order or relation to something else" (told 2026-11-07)
  - **Split:** "A record that fails the check is rewritten to meet it, under the standard's own lifecycle: a new complete record, the old one retired, accepted by name. A record found to be a bundle is split" (tagged inferred, ratified with the brief)
  - **Unchanged:** "The decisions themselves do not change. The work moves altitude, not outcome; where a check finds a decision itself wrong, stale or contradicted, that is a value question for the owner through Counsel, not a rewrite." (constraint, ratified with the brief)
  - **Standard reserved:** "the standard is not changed by this work without his word" (constraint)
  - **Batches:** "The rest reaches him in batches by area, each batch its own pull request and its own acceptance, of about ten records." (accepted 2026-11-11: "Go with your takes on all three.")
  - **Numbering:** "so that the run's proposed records skip no number" (told 2026-11-11: "renumber the ADRs so the numbering skip within one PR is not there anymore.")
  - **Consulted:** "Each of the two records names, in its `consulted` field, the model he talked with about the decision and the model that wrote the record." (told 2026-11-11: "Name the model who I talked to, and have written the document, in the consulted section")
  - **Template:** "its Validation prompt asks only what would show the decision broken, and it has no separate Invariant prompt. \"Not covered\" stays. Records already accepted stay as they are." (accepted 2026-11-11: "Go with your takes on both.")
  - **Clause held:** "A clause of an old record's Decision that a rewrite does not carry must be held by a named accepted record; the plugin's text stating it is not enough." (accepted 2026-11-11: "Go with your takes on all four of them.")
  - **On top:** "The area's second unit is planned now and built on top of the first unit's branch, without waiting for pull request 97 to land." (accepted in the same words)
  - **Test:** "a clause belongs to the same decision only if it could not stand once the first is retired. A clause that would still bind with the first gone is a decision of its own. The run applies this test to every record it checks, the twenty the census classed as holding more than one decision included." (accepted 2026-11-11: "Take that read and that test.")
  - **Line moved:** "Its third Decision line, that the loop never changes its goal and a change of goal is the owner's, comes out and is held by the record on protecting the goal condition that the next unit splits from ADR-D-0011, so that no record is added for it." (accepted in the same words)
  - **Together:** "ADR-D-0076 is accepted together with the record of the next unit that holds the line taken out of it, not before" (accepted 2026-11-11: "Go with your takes on both.")
  - **By name:** Limits: "Acceptance is by name, as the standard says; one statement may accept several records when it names each."
  - **Scenario 1:** "rewritten as one decision (who may be asked, by whom) with the route left to the plugin text"
  - **Scenario 2:** "A record deciding two things that could be retired separately: split into two, each accepted by name."
  - **Result recorded:** pass condition: "The check's result for every record is recorded: meets, rewritten (to which), split (into which), retired (material where), or raised."
  - **Publish approval:** `common.md`, Standing Approvals: "A finished, reviewed run may publish its branch and open pull requests in this repository without asking first. Merges are not covered and wait for the owner."
  - **Not relied on:** four sentences of the brief tagged inferred with no ratification record of their own: that the two closed runs' constraint "now leaves no record out"; "A record split in two or more ... still reach him by name"; "If the next unit finds that line does not belong with the goal's protection, where it is held returns to him"; "The same holds of every record this run writes after these two".
  Items (item | maps | grade | statement relied on | reasons, value question, direction):
  1. Goal: the unit is built on the first unit's branch and published as a pull request stacked on pull request 97 | maps to the brief | cited | On top; Batches; Publish approval | -
     - Publishing is outward-facing and is covered by the standing approval. The entry carries its record ("Given and accepted by the repository's owner, ebigunso, on 2026-09-30, relayed by Counsel: 'The common rule proposed, accepted.'") and is committed at HEAD. Whether the quoted words were said is not something a file can show. Merges are not covered and wait.
  2. Definition of Done 1: each of the four records is checked again and read by his test; the result is recorded in the run record, with the outcomes where the check differs from the census | maps to the brief | cited | Checked; Test; Result recorded; Unchanged | -
     - ADR-D-0063 and ADR-D-0066 are in the brief's list of 2026-11-02 of records left to runs in progress. That constraint reaches "Records a run in progress proposes or supersedes". Both are accepted at HEAD and the brief they name as their source is under `briefs/completed/`, so by its own words the constraint no longer reaches them. The brief's later sentence saying so is not relied on.
     - The plan's quotation of the test matches the brief word for word.
  3. Definition of Done 2: for each decision the test finds and the admission test admits, a new complete proposed record at intent altitude in the changed template's form | maps to the brief | cited | Split; Checked; Template | -
  4. Definition of Done 3: no decision's outcome changes | maps to the brief | cited | Unchanged | -
  5. Definition of Done 4: the clause that came out of ADR-D-0076, with the ADR-D-0014 clauses that go with it, is carried by the record on the goal's protection if it belongs there by the test; if not, where it is held returns to the owner | maps to the brief | cited | Line moved; Test; Clause held | -
     - The list in the changes file agrees with ADR-D-0014 itself: its Decision sentence, its driver on goal changes, its Validation line and its consequence on direction changes.
     - The fallback asks him rather than choosing between Line moved and Test, so it needs no support of its own.
  6. Definition of Done 5: every clause is accounted for (carried, held by a named accepted record, or left to plugin text quoted by file and line); an unheld Decision clause is a gap and the old record is not retired until it is settled | maps to the brief | cited | Clause held; Checked; Scenario 1 | -
     - The entry says nothing on mechanics that plugin text states nowhere; the tasks only report them. Nothing is retired by this plan, so nothing is lost here. It bears on the later retirement.
  7. Definition of Done 6: each new record's `consulted` carries over the old record's entries and adds the writing model | maps to the brief | inferred | extends Consulted, told of two records; cheap to undo, the records being proposed | -
     - The plan names the old entries and the writer. His words also name the model he talked with. For ADR-D-0079, whose content he discussed with Counsel, that is the same model if a Fable 5.2 Worker writes it.
  8. Definition of Done 7: the plan ends with the records proposed, reviewed and audited; it accepts and retires nothing; every record from a split reaches him by name; retirement follows his acceptance as a change of its own | maps to the brief | cited | Scenario 2; By name; Split; Together | -
  9. Planner-added: every clause of each old record is accounted for in the Worker's report | maps to the brief | cited | Clause held; Unchanged | -
  10. Planner-added: `consulted` carries over the old entries and adds the writing model | maps to the brief | inferred | extends Consulted; cheap to undo | -
  11. Scope: new proposed records ADR-D-0077 to ADR-D-0086 by the census's count | maps to the brief | cited | Split; Batches; Numbering | -
  12. Non-goal: the other three areas | maps to the brief | cited | Batches | -
  13. Non-goal: any change to a decision | maps to the brief | cited | Unchanged | -
  14. Non-goal: marking a record accepted, retiring a record or repairing references; Compatibility stance preserve | maps to the brief | cited | By name; Split; Together | -
  15. Non-goal: the record standard and its template | maps to the brief | cited | Standard reserved; Template | -
  16. Non-goal: plugin text | maps to the brief | inferred | extends Checked ("exact mechanics ... not covered") and Scenario 1; cheap to undo, since a later unit can add text | -
  17. Non-goal: ADR-D-0076 and ADR-D-0014 themselves | maps to the brief | cited | Line moved; Together | -
  18. Assumption: the census's counts hold; where a Worker's test gives another count it writes nothing and reports, and the Orchestrator re-scopes and renumbers | maps to the brief | cited | Test; Numbering | -
  19. Task_1 (ADR-D-0011, with the ADR-D-0076 clause; `supersedes` names ADR-D-0014 as well) | maps to the brief | cited | Checked; Wording; Split; Unchanged; Template; Clause held; Line moved; Test; Together | -
      - Its `consulted` clause is graded at item 7 and its validation at item 24. The same holds for items 20 to 22.
      - "Where a reason or a reopen condition is written nowhere, the Worker invents nothing" rests on Checked and Split, which bring in the standard, and on Unchanged.
      - ADR-D-0011 states why its two rejected options lost and gives neither a reopen condition nor an outright rejection. By the task's own rule the Worker will report that gap and not write the record that carries them. ADR-D-0079 is the record ADR-D-0076's acceptance waits for.
  20. Task_2 (ADR-D-0029) | maps to the brief | cited | Checked; Wording; Split; Unchanged; Template; Clause held; Test | -
  21. Task_3 (ADR-D-0063) | maps to the brief | cited | the same statements as item 20 | -
  22. Task_4 (ADR-D-0066) | maps to the brief | cited | the same statements as item 20 | -
  23. Design and Task Waves: one Worker for each old record, four in parallel; the Orchestrator renumbers and repairs citations when a count changes | internal mechanics | not audited | the engineering side has no document; not irreversible or outward-facing | -
  24. The tasks' validation (the package checker, the whitespace check, cited filenames exist, the review) and the research waiver | internal mechanics | not audited | the engineering side has no document; not irreversible or outward-facing | -
  25. Decision Log, BUNDLE-P1: a changed count moves the later numbers, and every citation between the new records is repaired before review | maps to the brief | cited | Numbering | -
  26. Decision Log, BUNDLE-R1: Open Questions records as settled that ADR-D-0076 is accepted together with this unit's record holding the removed clause, outside this plan | maps to the brief | cited | Together | -
  Human-only conditions pending: none marked human-only. The brief marks neither of its two pass conditions agent-checkable or human-only.
  Scenarios: none
- Acting on the verdict: nothing is held and nothing is ungraded, so the plan is authorized by the brief route. Taken from the verdict: ADR-D-0011 gives its two rejected options a reason and neither a reopen condition nor an outright rejection, so that question goes to the owner through Counsel now, before Task_1 reaches it; the consulted field of the record he discussed with Counsel names that model as well.
- 2026-11-11T08:59Z Wave 1 dispatched, each task to a Claude subagent `harness-worker` on Fable 5.2 at low reasoning effort, with the plan's task as the assignment and the census's counts given as unchecked. Task_1 was dispatched in two parts, the check and drafts first and the writing after, because the plan-draft audit had found that ADR-D-0011 gives its two rejected alternatives no disposition; that question went to the owner through Counsel at 08:59Z.
- 2026-11-11T09:12Z Wave 1 integrated, except ADR-D-0077: nine proposed records written, each Worker inside its owns (as re-scoped in the Decision Log); required Worker checks pass and were rerun by the Orchestrator. By old record, with the owner's test applied clause by clause in each Worker's report:
  - ADR-D-0011: three decisions, as the census had. ADR-D-0077 (progress in a goal run is measured against the goal condition and nothing else) is drafted and not written: both of ADR-D-0011's rejected alternatives belong to it and wait for the owner's word. ADR-D-0078, "A goal loop is stalled only when it is not progressing and is repeating approaches that failed". ADR-D-0079, "A goal loop never changes its goal or loosens how it is measured", carries the clause that came out of ADR-D-0076 as the head of its decision: with the loop free to change its goal a guard on loosening its measures is empty, so the guard falls with it and is not a decision of its own. It names ADR-D-0014 as well as ADR-D-0011 in `supersedes`.
  - ADR-D-0029: two decisions, as the census had. ADR-D-0080, "Whether a goal loop continues is judged by a party other than the optimizer". ADR-D-0081, "A goal loop whose continuation the evidence does not justify stops and escalates", which would bind whoever judges.
  - ADR-D-0063: two decisions, where the census had three. A held item stopping the loop cannot stand with the audit's coverage of the loop retired, the shape the owner ruled one decision in ADR-D-0076. ADR-D-0082, "The value audit grades a goal run that has a brief or a philosophy over the whole run", holds the stop. ADR-D-0083, "Nothing of a value audit reaches what a goal loop's assessor reads but a stop and its question".
  - ADR-D-0066: three decisions, where the census had two. That no goal loop starts without an authority envelope, and what one consists of, binds with either of the others retired and is held by no other record. ADR-D-0084, "No goal loop starts without an authority envelope". ADR-D-0085, "A goal loop's forbidden actions are defined by a criterion, not a list". ADR-D-0086, "A goal loop never changes its own authority envelope". ADR-D-0066's clause that a changed envelope is authorized afresh is not carried: accepted ADR-D-0065 holds it.
  - Numbers: with the counts changed, the Orchestrator renumbered before review so that none is skipped (ADR-D-0077 to ADR-D-0086) and checked each citation between the new records by what it means. The Worker reports for ADR-D-0066 call its records ADR-D-0085 to ADR-D-0087.
  - Written from a restatement and not from a written reopen condition or reason, each named in its Worker's report and to be shown to the owner with the records: the Revisit When premises of ADR-D-0079, ADR-D-0081 and ADR-D-0083; the premise ADR-D-0066 wrote once for the envelope, carried into both ADR-D-0084 and ADR-D-0086; a clause in ADR-D-0084's Why; the closing clause of ADR-D-0081's Why; the tie in ADR-D-0082 between ADR-D-0063's unexercised premises and its three reopen conditions. Four records have no Rejected Alternatives section, their old records stating no alternative for that decision: ADR-D-0078, 0079, 0081, 0084.
  - Found and not built: ADR-D-0011 has an early assessment choose how the gap is read, where the plugin's text has the reading set in the goal file before the loop; ADR-D-0077's draft says "early in its run" and names no one. ADR-D-0011's phrase "treated like pressure on a protected invariant" rests on a protection of a goal condition's named invariants that only the plugin's text states. Both go to the owner through Counsel with the unit's report.
- 2026-11-11T09:12Z Review requested of the Codex seat `agent-harness-reviewer` over agmsg, range 9f91e67..3aa509f, the nine written records.
- 2026-11-11T09:13Z Review: CHANGES REQUESTED at 3aa509f, two major findings, both in ADR-D-0079; no finding on the other eight. BUNDLE-W1-F1: by the owner's test ADR-D-0079 is two decisions. With the prohibition on the loop changing its goal retired, the rule that it tightens its measures freely and stops before loosening them still binds; a way round a rule does not make it unable to stand. BUNDLE-W1-F2: its Validation counts any autonomous change to the goal's condition as breaking it, while its Decision makes the measures part of that condition and lets the loop tighten them. The reviewer confirms the other splits by its own application of the test (ADR-D-0029 two, ADR-D-0063 two, ADR-D-0066 three, ADR-D-0011's stall a decision of its own), the conservation of each old record, "a changed envelope is authorized afresh" as held by ADR-D-0065, every listed restatement as a restatement and not an invention, the four omitted Rejected Alternatives sections, and every cross-citation after renumbering. The required checks pass, run independently.
- 2026-11-11T09:15Z BUNDLE-W1-F1 taken to the owner through Counsel, by the route the brief names for the case where the line from ADR-D-0076 does not belong with the goal's protection: one record holding both, or two. Nothing is changed in ADR-D-0079 until he answers; BUNDLE-W1-F2 is fixed with whichever shape he chooses.
- 2026-11-11T09:34Z The owner's answers, by Counsel's relay, to the four matters put to him ("Go with your takes on all four."), written into the brief under Directed during the run: ADR-D-0011's rejected alternatives are settled (fixed measures for all goals reopens if goal runs turn out to be of so few kinds that one set fits them all; a separate instrument for each goal is rejected outright); that only the owner changes the goal gets a record of its own, and ADR-D-0076 is accepted together with it; how the gap is read is settled before the loop starts, as the plugin's text has it and not as ADR-D-0011 worded it; a goal condition's named invariants are part of the goal and need no record of their own.
- 2026-11-11T09:40Z Built on those answers by Task_1's Worker, checks rerun by the Orchestrator:
  - ADR-D-0077 written, "Progress in a goal run is measured against the goal condition and nothing else", with both alternatives as settled and the reading of the gap settled before the loop starts. On that line it states the plugin's text and not the old record's wording, and says so.
  - ADR-D-0079 narrowed to the measures and renamed, "A goal loop loosens no measure of its goal without its owner's word": the loop tightens either measure freely, and loosening either needs the owner's word, the loop stopping for it. It no longer says loosening is a change of the goal. BUNDLE-W1-F2 is fixed: a tightening by the loop does not break it. It supersedes ADR-D-0011 only.
  - ADR-D-0087 written, "A goal loop never changes its goal on its own", carrying the five clauses of ADR-D-0014 that waited, and that the invariants a goal condition names are part of the goal, which the loop weakens none of on its own. The Worker checked that against the plugin's text (the invariants are listed under the goal condition and protected against weakening) and finds the record covers the protection, so nothing returns to the owner on it. It supersedes ADR-D-0014 only.
  - The unit is eleven records, ADR-D-0077 to ADR-D-0087, none skipped.
  - Citations repaired by the Orchestrator, each by what the sentence means: ADR-D-0086 names ADR-D-0087 for the loop never changing its goal; ADR-D-0076 names ADR-D-0087 for the line taken out of it, ADR-D-0079 for the measures, and ADR-D-0080 and ADR-D-0081 where it named ADR-D-0029, and its closing section now says ADR-D-0087 replaces the rest of ADR-D-0014 in place of the sentence about ADR-D-0014 waiting.
  - Written from a restatement, named in the Worker's report and to be shown to the owner: the Revisit When premises of ADR-D-0079 (the measures are what the loop's pursuit presses on) and ADR-D-0087 (a change of goal is a decision about direction); the first clause of ADR-D-0079's Why; a Validation line in ADR-D-0077 that follows from the reading being settled before the loop.
  - Noted by the Worker: the plugin's checklist lists the gap reading and the credibility bar among a condition's invariants, so ADR-D-0087's line on invariants and ADR-D-0079 both forbid the loop loosening those two; the records agree, each names the other, and neither forbids tightening.
- 2026-11-11T09:41Z Re-review: CHANGES REQUESTED at 432ec13, one minor finding. BUNDLE-W1-F1 and BUNDLE-W1-F2 closed; ADR-D-0077 passes; ADR-D-0011 is conserved across ADR-D-0077, 0078 and 0079, and ADR-D-0014 across ADR-D-0076 and ADR-D-0087; the Orchestrator's edits to ADR-D-0076 are pointers and its decision is unchanged; the listed restatements are restatements. BUNDLE-W1-R1: ADR-D-0087's Validation counted any change to the goal's condition without the owner's decision as breaking it, which described a tightening ADR-D-0079 permits as a violation.
- 2026-11-11T09:43Z BUNDLE-W1-R1 fixed by Task_1's Worker: ADR-D-0087's Validation says a tightening by the loop of how the gap is read, or of the bar a plateau argument must clear, does not break it. Its Decision is unchanged. Checks rerun by the Orchestrator.
- 2026-11-11T09:43Z Re-review: APPROVED at 3c5b7ec for the whole wave 9f91e67..3c5b7ec; BUNDLE-W1-R1 closed, no findings remain. Per old record: ADR-D-0011 is covered by ADR-D-0077, 0078 and 0079 with the reading settled before the loop as he directed; ADR-D-0014 jointly by ADR-D-0076 and ADR-D-0087; ADR-D-0029 by ADR-D-0080 and 0081; ADR-D-0063 by ADR-D-0082 and 0083; ADR-D-0066 by ADR-D-0084, 0085 and 0086, with the fresh authorization of a changed envelope held by ADR-D-0065. The required checks pass, run by the reviewer.
- 2026-11-11T09:45Z The reading is written in the readings file before the closeout audit is dispatched.
- 2026-11-11T09:45Z Value audit dispatched (Claude subagent `harness-auditor` on Fable, a new dispatch), text verbatim:
  You are the value auditor. Read references/value-audit-mandate.md of the orchestration-harness skill and follow it exactly. Position: closeout. Plan: <worktree>/docs/coding-agent/plans/active/decision-records-at-intent-altitude-goal-mode-bundles-plan.md. Governing brief: <worktree>/docs/coding-agent/briefs/active/decision-records-at-intent-altitude-brief.md. Changes since: 3f1e75e.
- 2026-11-11T09:54Z Verdict as returned (machine paths shortened; the two comparison lines are in the readings file):
  Value audit verdict, closeout. Nothing is held: no item is `ask-now` and none is `ungraded`. One judgement call carries the `direction` mark (J9, premises written from restatements). One reading diverges in part (the ADR-D-0076 edits).
  **Five things to act on or know, none of them a hold**
  - **No plan-draft audit of the plan as extended is logged.** The plan's Scope line and Context table were changed after the plan-draft audit of 08:58Z, and ADR-D-0087, the narrowed ADR-D-0079 and the edits to ADR-D-0076 were built on the owner's answers of 09:34Z. The mandate has a plan-draft audit again when a plan is revised or extended mid-run. What was built is covered by the brief (C1, C3, C11, C12); the gate itself is yours to apply (J13).
  - **Definition of Done 1 is not met yet.** The run record is unchanged in the range: its result table has no row for ADR-D-0011, 0029, 0063 or 0066, its ADR-D-0014 row still says the line waits for the record split from ADR-D-0011, and its State line says this unit is not started.
  - **The list of restatements to show the owner is incomplete.** Not listed in the Progress Log: the premise sentences in the Revisit When of ADR-D-0077 and ADR-D-0078, and "it lost because wording drift defeats matching over such labels" in ADR-D-0080's second rejected alternative. Each restates the old record's own condition.
  - **ADR-D-0082 names its exception only by record number.** Its Decision says "the one ADR-D-0067 states", where ADR-D-0063 said what it is ("an item whose remedy is already determined within the run's authority"). The brief's wording check asks that a record name the thing it means. Also, its `depends_on` names ADR-D-0066 and ADR-D-0083's names ADR-D-0029, both of which this unit's records replace, while their bodies cite ADR-D-0084, 0080 and 0081.
  - **ADR-D-0080 restates one Decision clause more broadly.** ADR-D-0029's "fresh context that reads only the goal file, the journal, and the gap history" is now "from the run's recorded evidence and never from the optimizer's working context", with the inputs left to goal mode's text. I read the decision as unchanged; he accepts it by name either way.
  **Before the record**
  - **Audited tree:** the worktree, branch `feature/2026-11-11/decision-records-goal-mode-bundles`, clean at c865e4f; range 3f1e75e to the working tree, twelve commits. The branch has no upstream, so nothing of the range is on the remote.
  - **Dispatch:** it matched the fixed template. The other text in context was the harness's reminder on how to return this report, a session hook on coding style, the memory index and a git status snapshot of the main checkout; none says anything about this work.
  - **First step, departures:**
    - My first call was a Read of the mandate at a guessed path that does not exist. Two Globs then returned file names only.
    - I read the mandate from the installed plugin copy (1.5.0); it is byte-identical to the worktree's copy, as is `value-documents/SKILL.md`.
    - Several Read calls went in one block, each on one named path. No command printed more than one file. Every git command that printed content carried both exclude pathspecs.
    - Two Greps printed the headings of the run record and the changes file. I read the changes file's section "ADR-D-0076 narrowed to the examination" only as far as its list of ADR-D-0014 clauses; it includes the start of an earlier logged verdict, from which I took nothing.
  - **Notes and readings:** no notes file was opened. The readings file was opened once, after the grades were fixed, and no grade changed afterwards.
  **Verdict record**
  Position: closeout
  Documents read:
  - `docs/coding-agent/briefs/active/decision-records-at-intent-altitude-brief.md`
  - `docs/coding-agent/rules/common.md` (pointer lines and Standing Approvals, at HEAD)
  - `docs/coding-agent/plans/active/decision-records-at-intent-altitude-goal-mode-bundles-plan.md` (artifact, claims under review)
  - The range's changes, read with git and from disk: ADR-D-0076 (diff) and ADR-D-0077 to ADR-D-0087 under `docs/coding-agent-orchestration-harness/decisions/`; the brief's diff.
  - Read to understand, not as support: ADR-D-0011, 0014, 0029, 0063, 0065 and 0066 at HEAD; `plugins/coding-agent-orchestration-harness/skills/durable-docs-authoring/references/adr.md`; `docs/coding-agent/plans/active/decision-records-at-intent-altitude-run.md` (Scenarios for prior states); the changes file section named above.
  Product basis: brief in the product owner's words ("product basis: the product owner's own words in this brief. ebigunso owns the harness")
  Not audited: the engineering side. `common.md` reads "Engineering philosophy: none yet", so it has no document. The product philosophy line also reads "none yet"; the product side is graded on the brief.
  Missing inputs: none
  Value documents changed in range: the brief, by two blocks of amendments under "Directed during the run", each with its ratification record (2026-11-11 "Go with your takes on both."; 2026-11-11 "Go with your takes on all four."). Four sentences added in the range are tagged inferred with no record of their own and are not relied on: "This is how his earlier answer that setup's refresh updates that copy is read"; "This replaces the entry above ... ADR-D-0076 is accepted together with the new record on the goal"; "The record that carries this states a decision other than the old record's wording, so it reaches him by name"; "If the run finds that record does not cover them, where the protection is held returns to him". No pointer line was removed or changed.
  Statements quoted below, by short name. All are from the brief except the last.
  - **Checked:** "Every accepted record ... is checked against the standard the plugin already carries: one decision per record; the constraint stated so that any rewording of the plugin text that preserves it stays valid; the why in prose at intent altitude; exact mechanics ... not covered." (told 2026-11-02)
  - **Split:** "A record that fails the check is rewritten to meet it, under the standard's own lifecycle: a new complete record, the old one retired, accepted by name. A record found to be a bundle is split" (ratified with the brief)
  - **Unchanged:** "The decisions themselves do not change. The work moves altitude, not outcome; where a check finds a decision itself wrong, stale or contradicted, that is a value question for the owner through Counsel, not a rewrite." (constraint)
  - **Standard reserved:** "the standard is not changed by this work without his word" (constraint)
  - **Batches:** "The rest reaches him in batches by area, each batch its own pull request and its own acceptance, of about ten records."
  - **Numbering:** "so that the run's proposed records skip no number" (told 2026-11-11)
  - **Consulted:** "Each of the two records names, in its `consulted` field, the model he talked with about the decision and the model that wrote the record." (told 2026-11-11)
  - **Template:** "its Validation prompt asks only what would show the decision broken, and it has no separate Invariant prompt. \"Not covered\" stays. Records already accepted stay as they are."
  - **Clause held:** "A clause of an old record's Decision that a rewrite does not carry must be held by a named accepted record; the plugin's text stating it is not enough."
  - **On top:** "The area's second unit is planned now and built on top of the first unit's branch, without waiting for pull request 97 to land."
  - **Test:** "a clause belongs to the same decision only if it could not stand once the first is retired. A clause that would still bind with the first gone is a decision of its own. The run applies this test to every record it checks, the twenty the census classed as holding more than one decision included." (accepted 2026-11-11: "Take that read and that test.")
  - **One shape:** "By that test the proposed ADR-D-0076 holds two decisions. It keeps the assessor's examination of whether the goal is still worth pursuing and what happens when the examination fails." (accepted in the same words)
  - **Together:** "ADR-D-0076 is accepted together with the record of the next unit that holds the line taken out of it, not before" (added in range; "Go with your takes on both.")
  - **Alternatives:** "Fixed progress measures defined once for all goals reopens if goal runs turn out to be of so few kinds that one fixed set of measures fits them all. A progress definition made for each goal and kept as an instrument of its own is rejected outright." (added in range; "Go with your takes on all four.")
  - **Own record:** "The line taken out of ADR-D-0076, that the loop never changes its goal and a change of goal is the owner's, is held by a record of its own, and the record on how the gap to the goal is read (tightened freely, loosened only with the loop stopping for its owner) holds only that." (added in range; same words)
  - **Before the loop:** "How the gap to the goal is read is settled before the loop starts, as the plugin's text has it, not chosen by early assessments during the run as ADR-D-0011 words it." (added in range; same words)
  - **Invariants:** "invariants named in the goal condition are part of the goal, and the record that the loop never changes its goal covers them." (added in range; same words)
  - **By name:** Limits: "Acceptance is by name, as the standard says; one statement may accept several records when it names each."
  - **Scenario 1 / Scenario 2:** the brief's core scenarios 1 and 2.
  - **Result recorded:** pass condition: "The check's result for every record is recorded: meets, rewritten (to which), split (into which), retired (material where), or raised."
  - **Publish approval:** `common.md`, Standing Approvals: "A finished, reviewed run may publish its branch and open pull requests in this repository without asking first. Merges are not covered and wait for the owner." The entry carries its record ("Given and accepted by the repository's owner, ebigunso, on 2026-09-30, relayed by Counsel: 'The common rule proposed, accepted.'") and is committed at HEAD. Whether the quoted words were said is not something a file can show.
  Items (item | maps | grade | statement relied on | reasons, value question, direction):
  The plan's items
  - P1. Goal: built on the first unit's branch, published as a pull request stacked on pull request 97 | maps to the brief | cited | On top; Batches; Publish approval | -
  - P2. Definition of Done 1: each of the four checked again and read by his test; the result recorded in the run record | maps to the brief | cited | Checked; Test; Result recorded | -
  - P3. Definition of Done 2: a new complete proposed record for each decision, in the changed template's form | maps to the brief | cited | Split; Checked; Template | -
  - P4. Definition of Done 3: no decision's outcome changes | maps to the brief | cited | Unchanged | -
  - P5. Definition of Done 4: the ADR-D-0076 clause carried by the record on the goal's protection if it belongs by the test, otherwise returned to the owner | maps to the brief | cited | Test; Own record | -
  - P6. Definition of Done 5: every clause accounted for; an unheld Decision clause is a gap | maps to the brief | cited | Clause held; Checked | -
  - P7. Definition of Done 6: `consulted` carries over the old entries and adds the writing model | maps to the brief | inferred | extends Consulted, told of two records; cheap to undo | -
  - P8. Definition of Done 7: ends with the records proposed, reviewed and audited; accepts and retires nothing; each split record reaches him by name | maps to the brief | cited | By name; Scenario 2; Together | -
  - P9. Planner-added: every clause accounted for in the Worker's report | maps to the brief | cited | Clause held; Unchanged | -
  - P10. Planner-added: `consulted` carries over and adds the writer | maps to the brief | inferred | extends Consulted; cheap to undo | -
  - P11. Scope: proposed records ADR-D-0077 to ADR-D-0087 | maps to the brief | cited | Split; Own record; Numbering; Batches | -
  - P12. Non-goal: the other three areas | maps to the brief | cited | Batches | -
  - P13. Non-goal: any change to a decision | maps to the brief | cited | Unchanged | -
  - P14. Non-goal: marking accepted, retiring, repairing references; Compatibility stance preserve | maps to the brief | cited | By name; Split; Together | -
  - P15. Non-goal: the record standard and its template | maps to the brief | cited | Standard reserved; Template | -
  - P16. Non-goal: plugin text | maps to the brief | inferred | extends Checked and Scenario 1; cheap to undo | -
  - P17. Non-goal: ADR-D-0076 and ADR-D-0014 themselves | maps to the brief | cited | Together | - (the range departs from it for ADR-D-0076; see C12 and C13)
  - P18. Assumption: the census's counts hold; on another count the Worker writes nothing and the Orchestrator re-scopes and renumbers | maps to the brief | cited | Test; Numbering | -
  - P19. Task_1 (ADR-D-0011, with the ADR-D-0076 clause) | maps to the brief | cited | Checked; Split; Unchanged; Template; Clause held; Test | -
  - P20. Task_2 (ADR-D-0029) | maps to the brief | cited | the same statements | -
  - P21. Task_3 (ADR-D-0063) | maps to the brief | cited | the same statements | -
  - P22. Task_4 (ADR-D-0066) | maps to the brief | cited | the same statements | -
  - P23. Design and Task Waves: one Worker for each old record, four in parallel | internal mechanics | not audited | the engineering side has no document; not irreversible or outward-facing | -
  - P24. The tasks' validation and the research waiver | internal mechanics | not audited | the same | -
  The changes in the range
  - C1. ADR-D-0077, proposed: progress is measured against the goal condition and nothing else; the reading of the gap is settled before the loop starts; two rejected alternatives as he settled them | maps to the brief | cited | Split; Test; Before the loop; Alternatives | -
    - On when the reading is settled, the record states a decision other than ADR-D-0011's wording, on his word, and says so in More Information.
  - C2. ADR-D-0078, proposed: a stall is the three signals together | maps to the brief | cited | Split; Test; Unchanged | -
  - C3. ADR-D-0079, proposed: the gap reading and the plateau bar are tightened freely and loosened only with the owner's word, the loop stopping | maps to the brief | cited | Own record; Unchanged | -
    - The brief's entry names how the gap is read; the record holds the plateau bar as well, as ADR-D-0011 did.
  - C4. ADR-D-0080, proposed: continuation is judged by a party other than the optimizer | maps to the brief | cited | Split; Test; Unchanged | -
  - C5. ADR-D-0081, proposed: continuation bears the burden of proof, binding whoever judges | maps to the brief | cited | Split; Test; Unchanged | -
  - C6. ADR-D-0082, proposed: the value audit grades a goal run with a brief or a philosophy over the whole run, and a held item stops the whole loop | maps to the brief | cited | Split; Test; One shape; Unchanged | -
    - The stop on a held item keeps its own rejected alternative and reopen condition inside this record. That is what his test yields, as in ADR-D-0076.
  - C7. ADR-D-0083, proposed: nothing of a value audit reaches what the assessor reads but a stop and its question | maps to the brief | cited | Split; Test; Unchanged | -
  - C8. ADR-D-0084, proposed: no goal loop starts without an authority envelope | maps to the brief | cited | Split; Test; Unchanged | -
  - C9. ADR-D-0085, proposed: forbidden actions are defined by a criterion | maps to the brief | cited | Split; Test; Unchanged | -
  - C10. ADR-D-0086, proposed: the loop never changes its envelope; "a changed envelope is authorized afresh" is not carried | maps to the brief | cited | Split; Test; Clause held | -
    - ADR-D-0065, accepted, holds the uncarried clause in its Decision: what is "added to or changed in ... a goal envelope, afterwards is not authorized by it and needs fresh authorization".
  - C11. ADR-D-0087, proposed: the loop never changes its goal on its own, the named invariants included; what a run learns against its goal is surfaced | maps to the brief | cited | Own record; Invariants; Unchanged | -
    - It carries the ADR-D-0014 clauses the changes file lists as waiting: the Decision sentence, the driver, the Validation line and the consequence.
  - C12. ADR-D-0076 edited: its Not covered names ADR-D-0087 for the line taken out, and More Information says ADR-D-0087 replaces the rest of ADR-D-0014 | maps to the brief | cited | Own record; Together | -
    - ADR-D-0076 is proposed and was never accepted, so this is not a record reworded after acceptance. Its Decision, Why, alternatives, Validation and Revisit When are untouched.
  - C13. ADR-D-0076 edited: it cites the proposed ADR-D-0079, 0080 and 0081 where it cited the accepted ADR-D-0011 and ADR-D-0029 | maps to the brief | inferred | extends Split and Together; cheap to undo, the record being proposed | -
    - The citations hold only if those three are accepted with it.
  - C14. All eleven records: no Invariant line; Validation says what would show the decision broken | maps to the brief | cited | Template | -
  - C15. All eleven records: `consulted` carries the old record's entries and adds Claude Fable 5.2 | maps to the brief | inferred | extends Consulted; cheap to undo | -
  - C16. All eleven records and ADR-D-0076 are `proposed`; nothing is accepted or retired | maps to the brief | cited | By name; Scenario 2; Together | -
  - C17. Numbers ADR-D-0077 to ADR-D-0087 with none skipped | maps to the brief | cited | Numbering | -
  Judgement calls and rulings in the plan's logs
  - J1. Decision Log, BUNDLE-P1: a changed count moves later numbers; citations repaired before review | maps to the brief | cited | Numbering | -
  - J2. Decision Log, BUNDLE-R1: ADR-D-0076's acceptance timing recorded as settled | maps to the brief | cited | Together | -
  - J3. Re-scope of Task_4: ADR-D-0066 is three decisions by his test | maps to the brief | cited | Test | -
  - J4. Ruling on Task_3: ADR-D-0063 is two decisions; his test governs where the standard's separate-retirability reading differs | maps to the brief | cited | Test; One shape | -
  - J5. Ruling that the ADR-D-0014 clause heads ADR-D-0079 as one decision, withdrawn on BUNDLE-W1-F1 and returned to the owner | maps to the brief | cited | Own record ("by the test he accepted the two stand apart, as the review found") | -
  - J6. ADR-D-0011's two rejected alternatives, left without a disposition, put to the owner before ADR-D-0077 is written | maps to the brief | cited | Alternatives | -
  - J7. "Found and not built": ADR-D-0011's early assessment choosing the gap reading, and its phrase resting on an invariant protection only the plugin states, both put to the owner | maps to the brief | cited | Unchanged; Before the loop; Invariants | -
  - J8. BUNDLE-W1-F1 taken to the owner with nothing changed in ADR-D-0079 until he answered | maps to the brief | cited | Unchanged; Own record | -
  - J9. Premises, reasons and a Validation line written from a restatement where the old record wrote none in those words, each named as a reading and to be shown to the owner (the Revisit When premises of ADR-D-0079, 0081, 0083 and 0087; ADR-D-0066's premise carried into ADR-D-0084 and 0086; clauses in the Whys of ADR-D-0079, 0081 and 0084; the tie in ADR-D-0082; a Validation line in ADR-D-0077) | maps to the brief | inferred | extends Split ("under the standard's own lifecycle") and Unchanged; cheap to undo, the records being proposed | direction
    - A Revisit When premise sets what reopens a decision. The brief has twice sent an unwritten reopen condition to him (ADR-D-0014's and ADR-D-0011's alternatives). In this unit he reads every record by name; in the areas still to come, a rewrite at the same decision goes in without his reading it.
  - J10. Five records have no Rejected Alternatives section, their old records stating none for that decision (ADR-D-0078, 0079, 0081, 0084, 0087) | maps to the brief | inferred | extends Unchanged; cheap to undo | -
  - J11. The Worker's finding that ADR-D-0087 covers the invariant protection, so nothing returns to the owner on it | maps to the brief | cited | Invariants | -
  - J12. ADR-D-0087's line on invariants and ADR-D-0079 both forbid loosening the gap reading and the plateau bar; left as they are, each naming the other; BUNDLE-W1-R1 fixed so that a tightening breaks neither | maps to the brief | cited | Own record; Invariants | -
  - J13. The owner's answers of 09:34Z built in this unit (ADR-D-0077, ADR-D-0079 narrowed, ADR-D-0087, ADR-D-0076's citations), with the plan's Scope and Context changed and no plan-draft audit of the plan as extended in the log | internal mechanics | not audited | the engineering side has no document; not irreversible or outward-facing | -
  - J14. Sequencing and dispatch: Task_1 in two parts; ADR-D-0078 and 0079 written while ADR-D-0077 waited; Workers on Claude Fable 5.2 at low reasoning effort; the Codex review seat | internal mechanics | not audited | the same | -
  Human-only conditions pending: none marked human-only. The brief marks neither of its two pass conditions agent-checkable or human-only.
  Scenarios:
  - 1 (a Decision that lists a route, rewritten as one decision): not yet. Prior: not yet.
  - 2 (a record deciding two things, split, each accepted by name): demonstrated for the one earlier instance, unchanged (ADR-D-0071 and ADR-D-0072 accepted, ADR-D-0016 under `superseded/`). For the first accepted records split, ready for the owner's judgement: read ADR-D-0077 to ADR-D-0087 and ADR-D-0076, all `proposed`, against ADR-D-0011, 0014, 0029, 0063 and 0066, still accepted.
  - 3 (a rule with a status field, retired): not yet. Prior: not yet.
  - 4 (a decision the check finds no longer true, brought to the owner): demonstrated, as before. A further instance in this range: the brief's entry "How the gap to the goal is read is settled before the loop starts ... not chosen by early assessments during the run as ADR-D-0011 words it".
  - Getting closer: yes. Before this unit no accepted record holding more than one decision had been split. The range holds eleven proposed records that between them carry each decision of four such records and the rest of ADR-D-0014, once each, with the one uncarried Decision clause held by an accepted record. Nothing is accepted yet, so no state reaches demonstrated on this unit's evidence.
- Acting on the verdict: nothing is held, so the plan closes with its records proposed. Taken from the verdict: the run record now carries each old record's result; ADR-D-0082 names its exception by what it is and the two depends_on fields name this unit's records; the list of restatements is completed; the judgement call marked direction (premises written from restatements) and ADR-D-0080's broader statement of what the assessor reads go to the owner through Counsel; the missed plan-draft audit of the plan as extended is recorded in the Decision Log; the reading is corrected where the grades differ.
- 2026-11-11T09:56Z On the closeout audit's points, by Task_3's Worker: ADR-D-0082 names its exception by what it is (an item whose remedy is already determined within the run's authority, ADR-D-0067); `depends_on` in ADR-D-0082 and ADR-D-0083 names the records of this unit in place of the records they replace. Also to be shown to the owner as restatements, beside those listed above: the premise sentences in the Revisit When of ADR-D-0077 and ADR-D-0078, and the reason given for the mechanical alternative in ADR-D-0080. The run record now carries the result for each of the four old records.

## Decision Log (append-only; re-plans and major discoveries)
- 2026-11-11 Plan review (Codex review seat): CHANGES REQUESTED at 43dc34c, one minor finding. BUNDLE-P1: the Design said a changed count disturbs only one Worker's range, which the plan's own rule against skipped numbers makes false. The comparison now states the cost: later numbers move and every citation between the new records is repaired by the Orchestrator before review, checked by meaning.
- 2026-11-11 Second plan review: BUNDLE-P1 closed; BUNDLE-R1 (minor): Open Questions still called the timing of ADR-D-0076's acceptance open, which the brief's entry committed since then settles. Replaced with the settled dependency.
- 2026-11-11 Re-scope of Task_4 on its Worker's finding, before anything was written: ADR-D-0066 holds three decisions by the owner's test, so Task_4 owns three records. Rulings with it: the record on the envelope existing builds its Why from ADR-D-0066's Context, which gives that reason; it has no Rejected Alternatives section, the old record stating none; the premise ADR-D-0066 wrote once under Revisit When for the envelope is carried into the two records it fits, named as a reading.
- 2026-11-11 Ruling on Task_3's count, before anything was written: two records. The owner's test is the one the brief has the run apply, and he ruled the same shape (a thing, and what happens when it fails or holds) one decision in ADR-D-0076; the standard's separate-retirability reading gives way to it. The census's third record is not written.
- 2026-11-11 Rulings on Task_1: the clause from ADR-D-0014 heads ADR-D-0079 and is not an addition to it; its title is one clause; its Revisit When restates ADR-D-0014's written driver as the premise, named as a reading. ADR-D-0078 and ADR-D-0079 are written while ADR-D-0077 waits for the owner.
- 2026-11-11 The ruling above that the clause from ADR-D-0014 heads ADR-D-0079 as one decision is withdrawn on the review's finding BUNDLE-W1-F1: the Worker's ground (a guard on loosening the measures is empty where the loop may change its goal) shows a way round the guard, not that the guard cannot stand. By the brief, where that clause is held returns to the owner.
- 2026-11-11 A gate missed, found by the closeout audit: after the owner's answers of 09:34Z the plan was extended (a record added, one narrowed, ADR-D-0076 edited, the Scope and the Context table changed) and built without a plan review and a plan-draft audit of the plan as extended. The extension rested on his words in the brief and the closeout audit grades what was built as covered, so nothing is undone; the rule stands that a plan revised or extended mid-run is reviewed and audited again before it is built on, his words settling what is built but not that the plan still fits them.

## Notes (Risks / Edge cases)
- The owner's test may find a count other than the census's for any of the four; the census was made before the test was stated. The plan's numbers are a starting assignment, not a requirement.
- ADR-D-0063, 0066 were accepted on 2026-11-07 and 2026-11-11 and are close to the standard's form; the work on them is the split, not the altitude.
- The new records cite each other across old records (the audit's stop names the remedy exception, ADR-D-0067; the stall record names who judges it). A citation to a sibling of another Worker uses the number in the Context table and is repaired by the Orchestrator if numbers change.
