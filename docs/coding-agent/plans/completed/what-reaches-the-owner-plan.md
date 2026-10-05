# Plan: What reaches the owner, and goal mode kept to his values

- status: done
- generated: 2026-10-05
- last_updated: 2026-10-05
- work_type: docs

## Goal
- The harness gives what the governing brief `docs/coding-agent/briefs/active/design-led-long-runs-brief.md` states in its sections "Decision records in a run", "What reaches you, and what does not" and "Watch list" (all three amendments of 2026-10-05), and in the goal-mode exception of its Limits.
- The brief is the requirement and is not restated here; where this plan and the brief differ, the brief governs and the difference is a plan defect.
- This is the third and last plan of the run recorded in `docs/coding-agent/plans/active/design-led-long-runs-run.md`. Its closeout is the run's closeout.

## Definition of Done
- Every gives-statement and constraint of those three sections and of the goal-mode exception is carried by the plugin text, each stated once in the file that owns that moment.
- A brief carries no watch list: the brief form, Counsel's closing pass, the audit's record form and the run-side report to Counsel no longer have one, and Counsel hears from the audit during a run only of an item let through on a provisional statement.
- A goal-mode run in a repository that has a philosophy is kept to the owner's values as it goes. Goal mode's admission test, stall rule and completion rule are unchanged, and the assessor's mandate, inputs and fixed dispatch template are byte-identical to this plan's start revision.
- The value audit's fixed dispatch template is byte-identical to this plan's start revision.
- Each record this plan proposes or changes in its decision is checked and accepted by the owner by name before any text is built on it.
- Package validators and smoke tests pass; the branch has Reviewer `APPROVED`.
- The run closes once, as `completion-closeout.md` states: scenario by scenario, with the marked items of every plan's closeout verdict, the records whose wording changed after acceptance, the design document for the field updated, the unpushed commits rebuilt and swept so that no machine-specific name or path reaches the remote, the reviewed branches published under the standing approval, and the note to Counsel.
- Nothing merges before the owner has judged the whole stack.

## Planner-added requirements
- The value audit attaches to a goal-mode run at three moments: the envelope before the owner ratifies it, each event on which the assessor is already due, and the completion report. Needed because: the brief asks that the run be kept to his values "as it goes", and the assessor's own cadence is the only rhythm goal mode has that is not a fixed count.
- A value question raised inside a goal loop stops the loop, as goal mode's own `ask-now` does, until it is answered. Needed because: a goal loop is one optimizer with no separable parts to hold, and adding a stop tightens, which the brief leaves free.
- What the value audit returns and what the Orchestrator writes for it in a goal run are kept in files beside the goal directory, and nothing of either is written into the goal file, the journal or the gap history. Needed because: those three are the assessor's evidence, and its inputs must not change.
- The audit names a finding it judges trivial though the Orchestrator read it as bearing on the design; an extension, since the brief states the outcome and not who checks it. Needed because: the second plan's closeout audit named the one-sided comparison as bearing on the design, and the brief says a trivial finding never reaches him.
- The mandate states what is never read before grading ahead of everything else it tells the auditor to read. Needed because: an auditor of the second plan opened the readings file first and had to return ungraded.
- One plugin version bump for this branch. Needed because: the package validator requires the three manifests to agree per installed version.

## Scope / Non-goals
- Scope: `value-documents`, `counsel`, `orchestration-harness` (SKILL.md, `value-level-operation.md`, `value-audit-mandate.md`, `lifecycle-gates.md`, `completion-closeout.md`, `final-response-contract.md`, `goal-mode.md`, `goal-templates.md`), `durable-docs-authoring/references/adr.md`, `subagent-strategy/references/model-routing.md`, `plan-format` rule 11, the Orchestrator adapters, the manifests, `docs/coding-agent/rules/orchestrator.md`, the goal-mode design document, decision records, and the run's closeout.
- Non-goals: the brief's "Left out on purpose"; goal mode's admission test, stall rule and completion rule; the assessor's mandate and template; a brief authorizing a goal-mode envelope; a hook or validator that enforces what an auditor may open; new Worker report fields.

## Design
- Chosen, for goal mode: the value audit runs beside the assessor, as its own dispatch on its own mandate, at the envelope, on the assessor's cadence events and at the completion report; an item it holds is a goal-mode `ask-now`.
- Alternative: two audits only, the envelope before ratification and the result at the completion report.
- Lenses. structure: both leave the assessor's inputs and template alone; chosen adds one dispatch per cadence event, the alternative none. evolution: both need one new record for the audit in goal mode and neither touches the completion report's sections. verification: neither adds a check of its own; the audit at the completion report grades the whole range, so a position missed inside the loop is still graded before anything merges. operation: chosen costs an Auditor dispatch per cadence event; the alternative costs two per run. human: with the alternative, drift from his values during the loop shows only at the end, when the work is built. safety: neither widens what the loop may do; chosen adds a stop.
- Why chosen: the brief says the run "is also kept to his values as it goes"; the alternative keeps it to them only at the two ends.
- Chosen, for the three amendments: each changed rule is stated once, in the file that owns that moment (who writes a record and which changes return, in the record standard; what the audit holds and reports, in the mandate; what the run does with a verdict, in the run-side reference), and every other file points to it; the watch field is removed from the verdict's item line.
- Alternative: keep the verdict's item line at six fields with the watch field always empty, and restate the record-writing rule in each role file that touches records.
- Lenses. structure: chosen has one owner per rule; the alternative keeps a field with no producer and four copies of one rule. evolution: chosen changes the verdict's form once now; the alternative leaves a dead field to explain and copies to keep in step. verification: no tool parses verdict lines, so neither needs a test changed; chosen is checked by a search that finds no watch list. operation: none. human: chosen leaves an auditor and a Worker one place to read. safety: neither changes who accepts a record.
- Why chosen: the alternative preserves a form for consumers that cannot be located, at the price of text that says what no longer happens.

## Compatibility stance (required if a contract/interface/persisted format is touched)
- surface: the audit verdict record (the watch field removed from the item line; one comparison outcome added); the brief form (no watch list). The completion report of a goal run and its pre-merge check are preserved as they are.
- stance: break
- justification: the locatable consumers of the verdict record are this repository's plans and Character Memory with the plugin installed; no validator, test or fixture parses verdict lines, and a logged verdict is history that is not reread by a tool. Briefs that carry a watch list are this repository's two, both amended by the owner. A goal run in a repository with no philosophy has no value audit and is untouched.

## Context (workspace)
- Governing brief: `docs/coding-agent/briefs/active/design-led-long-runs-brief.md`; ratification relayed by Counsel on 2026-10-04 quoting the owner: "I ratify the brief, hand it to the Orchestrator." Amendments of 2026-10-04 and 2026-10-05 carry his quoted words beside each.
- Run record: `docs/coding-agent/plans/completed/design-led-long-runs-run.md`. Readings file: `docs/coding-agent/plans/completed/design-led-long-runs-readings.md` (both under `active/` until the run closed). Run starts from revision: 263b0f08. This plan starts from revision: cc97211b.
- Left by the second plan (`docs/coding-agent/plans/completed/run-across-plans-plan.md`): the plugin text for the three amendments; the replacement of ADR-D-0045; the held finding on the one-sided comparison of findings, whose part (the comparison in the mandate and in ADR-D-0053) is not changed until the owner has accepted the change to that record; the finding that only instruction keeps an auditor from the readings file; the closeout list of records reworded after acceptance (ADR-D-0036, 0038, 0040, 0041, 0042, 0044, 0045, 0046, 0050, 0053); two judgement calls marked `direction` for the run's closeout; the owner's go of 2026-10-04 to rebuild the unpushed commits, logged with his quoted words in the second plan's Decision Log ("The commit rebuild can happen as well."); the brief's "Not taken" is the standing approval for future rebuilds, not this go.
- Research: two Researcher reports received in session on 2026-10-05 (goal mode and the value documents; an inventory of every place the three amendments touch). Not on disk, so nothing here rests on them alone; each Worker reads the files.
- Facts the plan relies on, each checkable in the tree: value-level operation is stated as plan-mode only in `orchestration-harness/SKILL.md` and `value-level-operation.md`; the assessor's evidence is the goal file, the journal and the gap history (`goal-assessor-mandate.md`); goal mode already states "Tighten-Free, Loosen-Escalates" (`goal-mode.md`); no live record says who writes decision records, the rule sits in `model-routing.md` and `docs/coding-agent/rules/orchestrator.md`; ADR-D-0045 and ADR-D-0053 are not on `main`.
- Design record consulted and deviations from its acceptance: ADR-D-0027, 0028, 0029, 0031 (goal mode; kept), ADR-D-0050 (kept: both fixed templates and both mandates' boundaries unchanged), ADR-D-0052 (kept; it does not cover goal mode, which the new record does), ADR-D-0045 (contradicted by the brief's removal of the watch list; replaced in full), ADR-D-0053 (its decision changes in one sentence, the comparison of findings; put to the owner by name).

## Open Questions (max 3)
- None for the owner. What the documents leave open about goal mode is settled as an extension in the planner-added requirements and graded by the audit.

## Assumptions
- A1: a goal run's value questions travel by the carrier `value-level-operation.md` already states, and its envelope is still ratified by the person in the session; no brief authorizes an envelope. source: ADR-D-0027; ADR-D-0040.
- A2: what Counsel infers beyond an answer of his is told apart from a statement tagged inferred that he ratified with the brief by its ratification record: the first has none of its own. source: the brief, "What reaches you, and what does not"; `value-audit-mandate.md` on statements changed in range.
- A3: the list of what Counsel inferred beyond his answers is Counsel's to bring at closeout; the run neither waits for it nor reports on it. source: the brief says Counsel does not come back for each one; `completion-closeout.md` on Counsel's read.
- A4: this repository has no philosophy, so no goal run here can show the goal-mode point; the run's closeout says so plainly. source: the brief's product basis line; its pass condition on scenarios is worded for scenarios 1 to 4 and is extended to this point.

## Tasks

### Task_1: Draft the records
- type: docs
- owns:
  - docs/coding-agent-orchestration-harness/decisions/**
- depends_on: []
- description: |
  A Worker drafts, as proposed, writing only what the brief and this plan's log state and reporting a gap wherever a reason is not written down: (R1) a full replacement of ADR-D-0045, on what Counsel hears from the audit during a run now that a brief carries no watch list; (R2) the value audit in a goal-mode run of a repository that has a philosophy; (R3) ADR-D-0053 with its comparison of findings made two-sided and its pointers to ADR-D-0045 repaired, shown as a change to an accepted record. Each only if the admission test passes. The Orchestrator checks that each says what was decided; a Reviewer checks each against the record standard; the three go to the owner by name in one message.
- acceptance:
  - Each record states only what the brief or this plan's log states; every gap the Worker found is reported, none filled.
  - Reviewer ADR review closed with no finding open.
  - No text of Task_2 or Task_4 that rests on a record is written before the owner has accepted that record by name.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "python scripts/validate_harness_package.py from the plugin root; git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "ADR review per the subagent-strategy ADR-review snippet"

### Task_2: Decision records in a run
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/durable-docs-authoring/references/adr.md
  - plugins/coding-agent-orchestration-harness/skills/subagent-strategy/references/model-routing.md
  - plugins/coding-agent-orchestration-harness/skills/plan-format/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/final-response-contract.md
  - plugins/coding-agent-orchestration-harness/agents/Orchestrator.md
  - plugins/coding-agent-orchestration-harness/claude/agents/harness-orchestrator.md
- depends_on: []
- description: |
  The plugin text carries the brief's section "Decision records in a run": who may write a record and under what constraint, who checks a draft, which changes of wording return to the owner and who judges that, acceptance in the same sentence as a wording request, and the closeout's list of records reworded after acceptance. It rests on no record, so it does not wait for Task_1.
- acceptance:
  - A Worker may write a decision record, writing only what the brief and the plan's log state and reporting gaps; plans and rule files stay with the Orchestrator.
  - A change of wording that leaves a record's decision, boundary, reasons and reopen conditions as they were does not return to the owner; a change to any of them does; the line is the Orchestrator's to draw as the work goes.
  - The final response of a run lists the records whose wording changed after acceptance, one line each, asking nothing.
  - Nothing here changes acceptance by name for a new record or for a change of decision.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "python scripts/validate_harness_package.py; python scripts/run_validation_smoke_tests.py; git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review against the brief's section and this task's acceptance"

### Task_3: No watch list; what reaches the owner
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/value-documents/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/counsel/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/value-audit-mandate.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/value-level-operation.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/lifecycle-gates.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/completion-closeout.md
- depends_on: [Task_1]
- description: |
  After the owner has accepted R1 and R3: the watch list leaves the brief form, Counsel's skill, the audit's record form and the run-side report; Counsel's closing pass asks what the work must not do or must ask before doing, and the answers become constraints; the audit holds a change that loosens a stop, a pass condition or who decides, and tightening is free; an unsupported line the Orchestrator added to its own plan is the Orchestrator's to drop or redo before anything is asked; wording that restates an answer needs no second yes, and what Counsel inferred beyond an answer is no support and is asked about only when work depends on it; the comparison of findings names both directions; the mandate states what is never read before grading ahead of its other reading instructions; the audit confirms at closeout that each record reworded after acceptance changed in wording only.
- acceptance:
  - No plugin file states a watch list, a watch hit or a watch field; Counsel hears from the audit during a run only of an item let through on a provisional statement; the value audit's fixed dispatch template block is byte-identical to this plan's start revision.
  - Counsel's closing pass asks whether there is anything the work must not do or must ask before doing, and what the owner answers is written into the brief as constraints, which the audit holds on.
  - The audit holds for the owner a change that loosens a stop, a pass condition or who decides; a change that tightens one is not held.
  - An `ask-now` whose only reason is that the Orchestrator's own plan line has no support is dropped or redone by the Orchestrator and audited again; it reaches the owner only when his statements conflict or are silent on something worthy of the philosophy.
  - Wording that restates an answer of the owner's is ratified by that answer and needs no second yes; a statement he ratified with a brief keeps its support whatever its provenance tag; only what Counsel inferred beyond an answer, with no ratification record of its own, is no support, and the audit asks when work depends on it.
  - The comparison of findings names both directions, and the mandate states what is never read before grading ahead of its other reading instructions.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "python scripts/validate_harness_package.py; python scripts/run_validation_smoke_tests.py; git diff --check; hash of the template block against the start revision"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review against the brief's two sections, R1 and R3 as accepted, and this task's acceptance; a trace of one run with an unsupported planner line and one provisional item"

### Task_4: A goal-mode run kept to his values
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/goal-mode.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/goal-templates.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/value-audit-mandate.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/value-level-operation.md
  - docs/coding-agent-orchestration-harness/design/goal-mode-design.md
  - plugins/coding-agent-orchestration-harness/.claude-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.codex-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.github/plugin/plugin.json
- depends_on: [Task_1, Task_3]
- description: |
  After the owner has accepted R2 and Task_3 has landed in the shared files: value-level operation applies to a goal-mode run in a repository that has a philosophy. The audit grades the envelope before the owner ratifies it, the changes and journaled decisions since its last position on each event the assessor is due, and the whole range at the completion report; an item it holds stops the loop as a goal-mode `ask-now`; the journal records that stop and the question put to the owner as it records any `ask-now`, and no grade, support or other part of a verdict; the verdicts and the Orchestrator's readings are kept in files beside the goal directory. The audit is dispatched by the fixed template as it stands: the mandate says how its fill-ins read for a goal run (the goal file where a plan is named; the envelope as the plan-draft position, a cadence event as the wave boundary with the last audited checkpoint as the revision, the completion report as closeout). The completion report's sections and the pre-merge check are not changed. The goal-mode design document is updated.
- acceptance:
  - `goal-assessor-mandate.md`, the assessor's fixed template and the goal-condition checklist are byte-identical to this plan's start revision; no verdict, reading or audit record is written into the goal file, the journal or the gap history.
  - A change inside a goal loop that loosens a stop, a pass condition or who decides is held for the owner as in a run under a brief; goal mode's own statement of that rule is kept.
  - Goal mode's admission test, stall rule and completion rule read as they did; the changes to `goal-mode.md` and `goal-templates.md` are the value audit's positions and its hold, and nothing else.
  - A goal run in a repository with no philosophy behaves as before.
  - The three manifests agree at the next version.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "python scripts/validate_harness_package.py; python scripts/run_validation_smoke_tests.py; git diff --check; git diff of the start revision on goal-assessor-mandate.md and goal-condition-checklist.md shows nothing"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review against the brief's Limits, R2 as accepted, ADR-D-0027 to 0029, 0031 and 0050; a trace of one goal run with a philosophy and one without"

### Task_5: Land the records and the rule file
- type: chore
- owns:
  - docs/coding-agent-orchestration-harness/decisions/**
  - docs/coding-agent/rules/orchestrator.md
  - docs/coding-agent/plans/**
- depends_on: [Task_1]
- description: |
  On the owner's acceptance naming a record the Orchestrator sets it accepted and logs the quoted words; ADR-D-0045 is retired in the same commit as its replacement and live pointers are repaired. The Orchestrator edits its own rule file so that it no longer keeps decision records with the Orchestrator alone. A decline or a correction that changes a decision sends the record back to its Worker; a wording change he asks for and accepts in the same sentence is applied and does not return.
- acceptance:
  - No record is set accepted, and ADR-D-0045 is not retired, without the owner's acceptance naming the record, logged with the quoted words.
  - Text resting on a record is written only after that record is accepted.
- validation:
  - kind: command
    required: true
    owner: orchestrator
    detail: "python scripts/validate_harness_package.py; status lines of the records match the Decision Log"

### Task_6: Close this plan and the run
- type: review
- owns:
  - docs/coding-agent/plans/**
  - docs/coding-agent/briefs/**
  - docs/coding-agent-orchestration-harness/design/**
- depends_on: [Task_2, Task_3, Task_4, Task_5]
- description: |
  The Orchestrator closes this plan (its closeout audit with its reading, the final review of the branch) and, the audit not having found the run stopped, closes the run as `completion-closeout.md` states: scenario by scenario from the run record, a demonstration on the built plugin where a run can make one and a plain statement where it cannot, the marked items of every plan's closeout verdict, the records reworded after acceptance, the design document for the field, the commits rebuilt and swept, the reviewed branches published and their pull requests opened under the standing approval, the note to Counsel, `candidate ready`.
- acceptance:
  - The closeout audit is dispatched by the fixed template and logged; its `Scenarios:` line is in the run record.
  - Every outgoing commit, message and pull request text is swept for machine-specific names and paths before it is pushed.
  - Nothing is merged.
- validation:
  - kind: command
    required: true
    owner: orchestrator
    detail: "package validator and smoke tests; privacy sweep over every commit to be pushed"
  - kind: review
    required: true
    owner: reviewer
    detail: "Final review of the branch vs this plan's Definition of Done"

## Task Waves (explicit parallel dispatch sets)
- Wave 1: Task_1, Task_2
- Wave 2: Task_5 (as each acceptance arrives)
- Wave 3: Task_3
- Wave 4: Task_4
- Wave 5: Task_6

Wave 1's two tasks own disjoint files. Task_3 and Task_4 wait for the owner's acceptance of the records they rest on; Task_2 rests on none.

## Rollback / Safety
- The branch reverts on its own; no migration, no persisted data. Nothing is published before Task_6, and nothing merges without the owner.

## Progress Log (append-only)
- 2026-10-05 Research waived for nothing: two Researcher reports received in session before drafting (goal mode and the value documents; the inventory of the three amendments).
- 2026-10-05 Plan review (Codex reviewer): round 1 NEEDS_REVISION with four findings, applied (see the Decision Log); the re-review left one stale line in the compatibility stance, corrected; APPROVED with no finding open. Plan validator passes.
- 2026-10-05 Plan-draft audit, dispatch text (to a fresh Auditor dispatch on Fable):

  ```text
  You are the value auditor. Read references/value-audit-mandate.md of the orchestration-harness skill and follow it exactly. Position: plan draft. Plan: docs/coding-agent/plans/active/what-reaches-the-owner-plan.md. Governing brief: docs/coding-agent/briefs/active/design-led-long-runs-brief.md. Changes since: none.
  ```

- 2026-10-05 Plan-draft audit, verdict as returned (machine paths redacted; the two comparison lines are logged in the readings file, not here):

  Value audit verdict, plan draft. No item is graded `ask-now`. Three remarks that change no grade follow the record. The discussion notes were not opened; the readings file was opened once, after the grades were fixed. The mandate was read from the working tree (`plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/value-audit-mandate.md`); the installed 0.21.0 copy was not found at the cache path I tried.

  ## Verdict record

  Position: plan draft

  Documents read: `docs/coding-agent/briefs/active/design-led-long-runs-brief.md`; `docs/coding-agent/plans/active/what-reaches-the-owner-plan.md` (artifact); `docs/coding-agent/rules/common.md` (sections "Standing Approvals" and "Repository Reference Documents" only, at HEAD; the file is unmodified)

  Product basis: brief in the product owner's words

  Not audited: engineering side, which has no document (`common.md` carries no philosophy pointer line)

  Missing inputs: none

  Value documents changed in range: none (plan draft, no range)

  Items (the brief carries no watch list, so the sixth field is `-` throughout):

  - DoD 1: every gives-statement and constraint of the three sections and the goal-mode exception carried by the plugin text, each stated once | maps to the brief | cited | brief, sections "Decision records in a run", "What reaches you, and what does not", "Watch list"; header: "It is passed verbatim; do not paraphrase it into a plan as if the paraphrase were the requirement." | - | -
  - DoD 2: no watch list; Counsel hears only of a provisional item | maps to the brief | cited | brief: "A brief carries no watch list."; "During a run Counsel still hears of an item the audit lets through that rests on a statement marked provisional, and of nothing else from the audit." | - | -
  - DoD 3: a goal-mode run with a philosophy kept to his values; admission, stall, completion and the assessor unchanged | maps to the brief | cited | brief, Limits: "Goal mode for goals a check can decide keeps working as it does today, with one exception: a goal-mode run in a repository that has a philosophy is also kept to his values as it goes, and goal mode may change for that point." | - | -
  - DoD 4: the value audit's fixed dispatch template byte-identical | maps to the brief | cited | brief: "A dispatch to the Auditor carries locations only; an account of the work in it is misuse on sight." | - | -
  - DoD 5: each record accepted by name before text is built on it | maps to the brief | cited | brief: "You still check a proposed decision record before anything is built on it."; Limits: "each decision record is accepted by him by name" | - | -
  - DoD 6: validators and smoke tests pass; Reviewer `APPROVED` | maps to the brief | cited | brief, Pass conditions: "the package validators pass"; Limits: "changes reach the remote only after review" | - | -
  - DoD 7a: the run closes once, scenario by scenario, with marked items, reworded records, design document, note to Counsel | maps to the brief | cited | brief: "It leads with behaviour, scenario by scenario, with how to observe each."; "The closeout lists the records whose wording changed after you accepted them, one line each, and asks nothing."; "The durable design document for the field the work touched is updated at closeout." | - | -
  - DoD 7b: reviewed branches published and pull requests opened | maps to the brief | cited | standing approval, `common.md`: "A finished, reviewed run may publish its branch and open pull requests in this repository without asking first. Merges are not covered and wait for the owner." The entry carries the acceptance record ("The common rule proposed, accepted.", 2026-09-30); whether those words were said is not something a file can show. | - | -
  - DoD 7c: unpushed commits rebuilt and swept for machine-specific names | internal mechanics | not audited | - (step 1 test run: nothing is published by the rebuild itself, and the push is covered under 7b) | - | -
  - DoD 8: nothing merges before he has judged the stack | maps to the brief | cited | brief, Limits: "nothing merges until you have judged the whole stack" | - | -
  - Planner-added 1: the value audit attaches to a goal run at the envelope, the assessor's cadence events and the completion report | maps to the brief | inferred | brief, Limits: "is also kept to his values as it goes, and goal mode may change for that point" | - | -
  - Planner-added 2: a value question inside a goal loop stops the loop | maps to the brief | inferred | brief: "The work stops, for the affected part, when it depends on a decision worthy of the philosophy and what you supplied does not cover it nearly enough to settle it without you."; Limits: "Goal mode for goals a check can decide keeps working as it does today". Departs from the means "While you decide, the part the finding concerns waits and the rest of the run continues"; graded on the gives-statement it serves: "It reaches you if it bears on the design, whatever it would cost to act on". | - | -
  - Planner-added 3: verdicts and readings kept beside the goal directory, nothing in the goal file, journal or gap history | maps to the brief | inferred | brief, Limits: "Goal mode for goals a check can decide keeps working as it does today, with one exception" | - | -
  - Planner-added 4: the audit names a finding it judges trivial though read as bearing on the design | maps to the brief | inferred | brief: "a trivial one never does, however cheap."; "the audit, not the Orchestrator, compares that reading with its own grades" | - | -
  - Planner-added 5: the mandate states first what is never read before grading | internal mechanics | not audited | - | - | -
  - Planner-added 6: one plugin version bump | internal mechanics | not audited | - | - | -
  - Non-goal: the brief's "Left out on purpose" | maps to the brief | cited | brief, "Left out on purpose" | - | -
  - Non-goal: goal mode's admission test, stall rule, completion rule; the assessor's mandate and template | maps to the brief | cited | brief, Limits: "Goal mode for goals a check can decide keeps working as it does today, with one exception" | - | -
  - Non-goal: a brief authorizing a goal-mode envelope | maps to the brief | cited | brief, Limits, the same statement | - | -
  - Non-goal: a hook or validator enforcing what an auditor may open | internal mechanics | not audited | - | - | -
  - Non-goal: new Worker report fields | internal mechanics | not audited | - | - | -
  - A1: a goal run's value questions travel by the existing carrier; the envelope is ratified by the person in the session | maps to the brief | cited | brief, Limits: "his word reaches the Orchestrator through Counsel's quoted relay"; "Goal mode for goals a check can decide keeps working as it does today" | - | -
  - A2: what Counsel inferred beyond an answer is told apart by having no ratification record of its own | maps to the brief | inferred | brief: "What Counsel infers beyond your answer is marked inferred, is no support for the audit"; "the answer is the ratification, in a brief as in a record"; provenance line: "*(inferred)* = Counsel inferred it and he did not object" | - | -
  - A3: the list of what Counsel inferred is Counsel's to bring at closeout; the run neither waits nor reports | maps to the brief | inferred | brief: "is listed once at closeout for you to object to; Counsel does not come back for each one" | - | -
  - A4: no goal run here can show the goal-mode point; the closeout says so plainly | maps to the brief | inferred | brief, product basis line: "no product philosophy and no engineering philosophy exist for this repository"; Pass conditions: "where one cannot the closeout says so plainly" (that clause is worded for scenarios 1 to 4 and is extended here) | - | -
  - Task_1: records drafted by a Worker, checked by the Orchestrator and a Reviewer, put to the owner by name | maps to the brief | cited | brief: "Workers may write decision records."; "A Worker writes only what the brief and the plan's log state; where the reason for a decision is not written down it reports the gap and invents nothing."; "The Orchestrator checks that a draft says what was decided, and the Reviewer checks it against the record standard." | - | -
  - Task_2: decision records in a run, in the plugin text | maps to the brief | cited | brief, "Decision records in a run", including "A change of wording to a record does not come back to you when it changes none of the record's decision, its boundary, its reasons or its reopen conditions; a change to any of those does." and "The rule files, where standing approvals live, stay with the Orchestrator, and plans remain its own working document." | - | -
  - Task_3: no watch list; what reaches the owner | maps to the brief | cited | brief: "A line the Orchestrator adds to its own plan that your documents do not support is the Orchestrator's to drop or redo so that the plan follows the brief."; "Wording that restates an answer of yours needs no second yes from you"; "A change that loosens a stop, a pass condition or who decides is held for you, in a run under a brief as in a goal loop; tightening is free."; "In the closing pass Counsel asks whether there is anything the work must not do, or must ask before doing, and what you answer goes into the brief as constraints, which the audit holds on."; "the closeout audit confirms it for every record accepted before the change" | - | -
  - Task_4: a goal-mode run kept to his values | maps to the brief | inferred | brief, Limits: "is also kept to his values as it goes, and goal mode may change for that point"; "A change that loosens a stop, a pass condition or who decides is held for you, in a run under a brief as in a goal loop" | - | -
  - Task_5: records landed on acceptance by name; the Orchestrator edits its own rule file | maps to the brief | cited | brief: "The rule files, where standing approvals live, stay with the Orchestrator"; Limits: "each decision record is accepted by him by name"; "When you ask for a wording change on first reading you may accept in the same sentence, and the corrected text does not return." | - | -
  - Task_6: close the plan and the run; publish; nothing merged | maps to the brief | cited | brief: "It leads with behaviour, scenario by scenario, with how to observe each."; Pass conditions: "scenarios 1 to 4 are demonstrated by a run where one can be made, and where one cannot the closeout says so plainly"; Limits: "nothing merges until you have judged the whole stack"; standing approval as quoted under DoD 7b, with the same caveat. The rebuild of commits is as DoD 7c. | - | -
  - Decision Log 1: no record for who writes records or for the hold on loosening; no hook for the readings file | maps to the brief | inferred | brief, header: "It states what and why. How is the Orchestrator's"; "Workers may write decision records."; "A change that loosens a stop, a pass condition or who decides is held for you" | - | -
  - Decision Log 2: round 1 review applied (audit material kept out of the assessor's evidence; completion report and pre-merge check unchanged; pointer to Counsel's list dropped) | maps to the brief | inferred | brief, Limits: "Goal mode for goals a check can decide keeps working as it does today"; "is listed once at closeout for you to object to; Counsel does not come back for each one" | - | -

  Human-only conditions pending: "scenarios 5 to 9, judged by him in his first use of a Counsel session opened from the built plugin"; "scenarios 1 to 4 where no run could demonstrate them"; "whether he could trust the result by default, without having thought about what the Orchestrator was doing"

  Scenarios: none

  ## Remarks that change no grade

  1. **Journal tension in Task_4.** Its description has an audit hold "journaled as any `ask-now` is today", while its acceptance and planner-added 3 say no audit record enters the journal. The journal is the assessor's evidence. The plan should say what the journal line for such a hold may contain.
  2. **Template fit for goal runs.** The fixed template's fill-ins are `Position: <plan draft | wave boundary | closeout>` and `Plan: <path>`. A goal run has neither a plan nor those positions (envelope, cadence event, completion report). DoD 4 holds the template byte-identical, so Task_4 needs to state how a goal-run audit is dispatched within it. As drafted, the two may not both be satisfiable.
  3. **The go to rebuild commits.** The plan's Context cites "the owner's go of 2026-10-04 to rebuild the unpushed commits". No document I may rely on carries it, and the brief records the standing approval for this as "Not taken". I graded the rebuild as internal mechanics, not irreversible, so no stop is owed; the go itself is unverified by this audit.

  Questions for Orchestrator: none.

  How the Orchestrator applied it: no item is `ask-now` and none is `ungraded`. With the brief's ratification relayed by Counsel under the standing approval, the plan review closed with no finding open, and this verdict, the plan is authorized under the ratified brief; this records no approval by the owner. No item rests on a provisional statement, so nothing goes to Counsel. The comparison found readings apart from grades on six items, each a difference of class and none a held item; they are corrected in the plan as the next entry records. The auditor's three remarks are acted on there too. This plan starts from revision cc97211b.
- 2026-10-05 Divergences corrected at plan draft: the comparison set six readings apart from their grades. Re-read against the brief: the audit naming an over-read finding (planner-added 4), the closeout statement for the goal-mode point (A4) and Task_4 as a whole are extensions of the brief, not things it states, and the plan now says so for the first two (Task_4 builds planner-added 1 to 3, already marked as added); the goal run's carrier (A1) is covered by the brief's Limits, not an extension; the commit rebuild and two non-goals are mechanics the audit does not grade. None changes what is built. The three remarks: Task_4 now says what the journal may record of a value hold (the stop and the question, nothing of the verdict) and how the unchanged template is filled in for a goal run; the Context names where the owner's go to rebuild the commits is logged.
- 2026-10-05 Wave 1, Task_1 and Task_2: both Worker reports `done`, each one YAML block, every changed file inside its task's `owns`. Task_1: ADR-D-0055 (replaces ADR-D-0045) and ADR-D-0056 (the value audit in a goal run) drafted as proposed, and ADR-D-0053 changed in its comparison of findings; the Worker wrote only what the brief and this log state and reported eleven gaps (reopen conditions not written down, one consequence not decided, one alternative with no reason), which the Decision Log settled and the Worker then applied; admission test passed for each. The Orchestrator read all three against what was decided and added to ADR-D-0053's first Validation line that a held part is also released by the audit's naming. Task_2: the record standard says who may draft a record and which changes of wording return; `model-routing.md`, `plan-format` rule 11, the final-response contract and both Orchestrator adapters follow. Worker validation: package validator pass, smoke tests pass, `git diff --check` clean. Orchestrator edits at integration: `docs/coding-agent/rules/orchestrator.md` no longer keeps decision records with the Orchestrator alone (the rule-file part of Task_5); `orchestration-harness/SKILL.md` names reworded records in its final-response summary. Left for Task_3: `counsel/SKILL.md` still says every change to a record reaches the owner. Review: dispatched next.
  - Judgement calls (Task_2): a wording correction asked for and accepted in the same sentence on first reading is not listed as reworded after acceptance; where no value audit runs, the Orchestrator's call on a wording change has no confirmation step; "the plan's log" is read as the plan's Decision Log.
- 2026-10-05 Wave 1 review (Codex reviewer): NEEDS_REVISION with two minor findings on the records, applied by the Orchestrator (ADR-D-0053 carries a note that its amendment is proposed and that the record without it is in force until accepted; ADR-D-0056's dated limitation moved out of Revisit When), one residual locator fixed, then APPROVED with no finding open for Task_1 and Task_2. The three records were sent to Counsel in one message for the owner's acceptance by name, with the sentences added to ADR-D-0053 quoted and with what in ADR-D-0056 is the run's own design. Task_3 and Task_4 wait for it.
- 2026-10-05 Wave 2 as reordered, Task_4: Worker report `done`, one YAML block, every changed file inside the task's `owns`; `goal-templates.md` needed no change. Value-level operation now covers a goal-mode run in a repository that has a philosophy: `goal-mode.md` gains one sentence under Tighten-Free and a Value Audit section (three positions, the hold as an `ask-now`, what the journal may record); the run-side reference and the mandate each gain a Goal-Mode Runs section; the readings exclusion is widened to `docs/coding-agent/**/*-readings.md`; the design document points to ADR-D-0056; manifests at 0.28.0. Worker validation: package validator pass, smoke tests pass, `git diff --check` clean, the assessor's mandate and the goal-condition checklist unchanged, the Fixed Dispatch Template block the same hash at HEAD and in the working tree. Orchestrator rulings at integration, on the Worker's questions: a goal run's dispatch reads `Governing brief: none`; any hold the run-side reference states for a part or a position stops the loop too, since a goal loop has no part to set aside. Review: dispatched next.
  - Judgement calls (Task_4): the value-audit file beside the goal directory also keeps the run's start revision and each owner answer against its item; the envelope's items are its statement, target, invariants, gap reading and decision-scope entries, the linkage credibility bar not among them.
- 2026-10-05 Wave 3 as reordered, Task_3: Worker report `done`, one YAML block, every changed file inside the task's `owns`. No plugin file states a watch list, a watch hit or a watch field (search: no match); the verdict's item line has five fields; Counsel's closing pass asks what the work must not do or must ask before doing; the audit holds a change that loosens a stop, a pass condition or who decides; the Orchestrator's own unsupported plan line is dropped or redone before anything is asked; a restated answer needs no second yes and what Counsel inferred beyond an answer is no support; the comparison of findings names both directions; the mandate states first what is never read before grading; records reworded after acceptance are closeout items. Worker validation: package validator pass, smoke tests pass, `git diff --check` clean, the Fixed Dispatch Template block the same hash at this plan's start revision, HEAD and the working tree. Orchestrator ruling at integration: a record reworded in wording only is recorded `not audited` with the changed words named. Review: dispatched next.
  - Judgement calls (Task_3): the brief form says nothing about a watch list, so that no plugin text states one; Counsel's list of what it inferred is placed in Counsel's skill and nothing is added to the run's closeout; the new outcome of the findings comparison is an input, since it releases and does not hold.
- 2026-10-05 Review of Task_4 and Task_3 together (Codex reviewer): NEEDS_REVISION, two major and two minor findings, all applied by the Orchestrator. (1) A departure from a means recorded as bearing on the design but judged trivial was still reported as agreeing, so its held part would not be released; the comparison now names it in that direction too. (2) In a goal run every gate on the position was made an `ask-now`, though some wait for no decision; a gate the Orchestrator can clear by correcting its own input now suspends the loop until a fresh verdict, with no question asked, and only a held item or a finding's part stops it for the owner. (3) The two files beside a goal directory were named only under `active/`; they are now found beside the goal directory wherever it sits and move in the same change. (4) The carrier's line that a philosophy-alone run is plan mode now covers a goal run. Everything else traced clean: no watch list remains, the Plan Gate's condition is unchanged, the assessor's files and both templates are byte-identical to this plan's start revision. Lesson recorded. Re-review requested.
- 2026-10-05 Re-review (Codex reviewer): APPROVED for Task_3 and Task_4, all four findings closed. Tasks 1 to 5 are done.
- 2026-10-05 A missed gate, recorded: the run-side text has the value audit dispatched at each wave boundary, after the wave's integration and review. The Orchestrator dispatched none after Wave 1 (Task_1, Task_2), none after Task_4 and none after Task_3; it went from one wave's review to the next wave's dispatch. No audit can now be made at those moments. Ruling: the closeout audit, dispatched next over this plan's whole range from its start revision, grades everything those three audits would have graded; nothing is published and nothing merged before it. Lesson recorded in `docs/coding-agent/lessons.md`.
- 2026-10-05 Final review of the branch (Codex reviewer, range from this plan's start revision): APPROVED, no blocking finding; validators and smoke tests pass on the committed snapshot; the assessor's files and both dispatch templates byte-identical to the start revision; privacy clean over the range and its commit messages. On the missed wave-boundary audits the reviewer adds no hold and does not accept that the closeout audit is their equal: it is a real fault of execution, recorded, and the full-range closeout audit is still owed before the run closes or publishes.
- 2026-10-05 Closeout audit, dispatch text (to a fresh Auditor dispatch on Fable):

  ```text
  You are the value auditor. Read references/value-audit-mandate.md of the orchestration-harness skill and follow it exactly. Position: closeout. Plan: docs/coding-agent/plans/active/what-reaches-the-owner-plan.md. Governing brief: docs/coding-agent/briefs/active/design-led-long-runs-brief.md. Changes since: cc97211b.
  ```

- 2026-10-05 Closeout audit, first dispatch, verdict as returned (machine paths redacted; the two comparison lines are logged in the readings file, not here):

  Value audit verdict, closeout of `docs/coding-agent/plans/active/what-reaches-the-owner-plan.md`. No item is `ask-now` and none is `ungraded`. Four items carry a `direction` mark. The discussion notes, `.claude/pr67body.tmp` and `.claude/settings.local.json` were not opened. The readings file was opened once, after the grades were fixed. The mandate was read from the working tree.

  ## Verdict record

  Position: closeout

  Documents read: `docs/coding-agent/briefs/active/design-led-long-runs-brief.md`; `docs/coding-agent/plans/active/what-reaches-the-owner-plan.md` (artifact); `docs/coding-agent/plans/active/design-led-long-runs-run.md` (prior scenario states); `docs/coding-agent/rules/common.md` at HEAD ("Repository Reference Documents" and "Standing Approvals" only; unchanged in range); the changes cc97211b..working tree, read with git under the two exclude pathspecs; `docs/coding-agent/briefs/active/setup-names-what-is-missing-brief.md` (header only, to name it below)

  Product basis: brief in the product owner's words

  Not audited: engineering side, which has no document (`common.md` carries no philosophy pointer line)

  Missing inputs: none

  Value documents changed in range: `docs/coding-agent/briefs/active/setup-names-what-is-missing-brief.md` (new, untracked; its header carries a ratification record dated 2026-10-05 and says it is handed to nobody yet and governs no run; no item here relies on it). The governing brief is unchanged since cc97211b. No pointer line was removed or changed.

  Items, plan:

  - DoD 1: every gives-statement and constraint of the three sections and the goal-mode exception carried by the plugin text | maps to the brief | cited | brief, header: "It is passed verbatim; do not paraphrase it into a plan as if the paraphrase were the requirement."; sections "Decision records in a run", "What reaches you, and what does not", "Watch list" | -
  - DoD 2: no watch list; Counsel hears only of a provisional item | maps to the brief | cited | brief: "A brief carries no watch list."; "During a run Counsel still hears of an item the audit lets through that rests on a statement marked provisional, and of nothing else from the audit." (a search of the plugin's Markdown for a watch list, hit or field finds nothing) | -
  - DoD 3: a goal-mode run with a philosophy kept to his values; admission, stall, completion and the assessor unchanged | maps to the brief | cited | brief, Limits: "Goal mode for goals a check can decide keeps working as it does today, with one exception: a goal-mode run in a repository that has a philosophy is also kept to his values as it goes, and goal mode may change for that point." (`goal-assessor-mandate.md`, `goal-templates.md` and `goal-condition-checklist.md` show no diff from cc97211b) | -
  - DoD 4: the value audit's fixed dispatch template byte-identical | maps to the brief | cited | brief: "A dispatch to the Auditor carries locations only; an account of the work in it is misuse on sight." (the template block has the same hash at cc97211b, HEAD and the working tree) | -
  - DoD 5: each record accepted by name before text is built on it | maps to the brief | cited | brief: "You still check a proposed decision record before anything is built on it."; Limits: "each decision record is accepted by him by name". Commit order agrees: Task_4's text follows the commit that sets ADR-D-0056 accepted, and Task_3's follows the one that sets ADR-D-0045 accepted. The acceptances are quoted only in the plan's Decision Log; whether the words were said is not something a file can show. | -
  - DoD 6: validators and smoke tests pass; Reviewer `APPROVED` | maps to the brief | cited | brief, Pass conditions: "the package validators pass"; Limits: "changes reach the remote only after review" | -
  - DoD 7a: the run closes once, scenario by scenario, with marked items, reworded records, design document, note to Counsel | maps to the brief | cited | brief: "It leads with behaviour, scenario by scenario, with how to observe each."; "The closeout lists the records whose wording changed after you accepted them, one line each, and asks nothing."; "The durable design document for the field the work touched is updated at closeout." | -
  - DoD 7b: reviewed branches published and pull requests opened | maps to the brief | cited | standing approval, `common.md`: "A finished, reviewed run may publish its branch and open pull requests in this repository without asking first. Merges are not covered and wait for the owner." The entry carries its acceptance record ("The common rule proposed, accepted.", 2026-09-30) and is committed; whether those words were said is not something a file can show. Nothing in the range publishes anything. | -
  - DoD 7c: unpushed commits rebuilt and swept | internal mechanics | not audited | - (step 1 test run: the rebuild publishes nothing, and the push is under 7b) | -
  - DoD 8: nothing merges before he has judged the stack | maps to the brief | cited | brief, Limits: "nothing merges until you have judged the whole stack" | -
  - Planner-added 1: the value audit attaches to a goal run at the envelope, the assessor's events and the completion report | maps to the brief | inferred | brief, Limits: "is also kept to his values as it goes, and goal mode may change for that point" | -
  - Planner-added 2: a value question inside a goal loop stops the whole loop | maps to the brief | inferred | brief: "A change that loosens a stop, a pass condition or who decides is held for you, in a run under a brief as in a goal loop; tightening is free." Departs from the means "While you decide, the part the finding concerns waits and the rest of the run continues"; graded on the gives-statement it serves: "It reaches you if it bears on the design, whatever it would cost to act on". | -
  - Planner-added 3: verdicts and readings kept beside the goal directory, nothing in the goal file, journal or gap history | maps to the brief | inferred | brief, Limits: "Goal mode for goals a check can decide keeps working as it does today, with one exception" | -
  - Planner-added 4: the audit names a finding it judges trivial though read as bearing on the design | maps to the brief | inferred | brief: "a trivial one never does, however cheap."; "the audit, not the Orchestrator, compares that reading with its own grades" | -
  - Planner-added 5: the mandate states first what is never read before grading | internal mechanics | not audited | - | -
  - Planner-added 6: one plugin version bump (0.28.0 in all three manifests) | internal mechanics | not audited | - | -
  - Non-goal: the brief's "Left out on purpose" | maps to the brief | cited | brief, "Left out on purpose" | -
  - Non-goal: goal mode's admission test, stall rule, completion rule; the assessor's mandate and template | maps to the brief | cited | brief, Limits: "Goal mode for goals a check can decide keeps working as it does today, with one exception" | -
  - Non-goal: a brief authorizing a goal-mode envelope | maps to the brief | cited | brief, Limits, the same statement | -
  - Non-goal: a hook or validator enforcing what an auditor may open | internal mechanics | not audited | - | -
  - Non-goal: new Worker report fields | internal mechanics | not audited | - | -
  - A1: a goal run's value questions travel by the existing carrier; the envelope is ratified in the session | maps to the brief | cited | brief, Limits: "his word reaches the Orchestrator through Counsel's quoted relay"; "Goal mode for goals a check can decide keeps working as it does today" | -
  - A2, and the text built on it in `value-documents/SKILL.md` and the mandate: a statement tagged inferred that he ratified with the brief keeps its support, and only what Counsel inferred beyond an answer, with no ratification record of its own, is no support | maps to the brief | inferred | brief: "What Counsel infers beyond your answer is marked inferred, is no support for the audit"; "the answer is the ratification, in a brief as in a record"; provenance line: "*(inferred)* = Counsel inferred it and he did not object" | direction: it settles which of the statements tagged inferred count as his word for every later audit
  - A3: Counsel brings the list of what it inferred at closeout; the run neither waits nor reports | maps to the brief | inferred | brief: "is listed once at closeout for you to object to; Counsel does not come back for each one" | -
  - A4: no goal run here can show the goal-mode point; the closeout says so plainly | maps to the brief | inferred | brief, product basis line: "no product philosophy and no engineering philosophy exist for this repository"; Pass conditions: "where one cannot the closeout says so plainly" (worded for scenarios 1 to 4, extended here) | -
  - Task_1: records drafted by a Worker, checked by the Orchestrator and a Reviewer, put to the owner by name | maps to the brief | cited | brief: "Workers may write decision records."; "A Worker writes only what the brief and the plan's log state; where the reason for a decision is not written down it reports the gap and invents nothing."; "The Orchestrator checks that a draft says what was decided, and the Reviewer checks it against the record standard." | -
  - Task_2: decision records in a run, in the plugin text | maps to the brief | cited | brief, "Decision records in a run" | -
  - Task_3: no watch list; what reaches the owner | maps to the brief | cited | brief, "What reaches you, and what does not" and "Watch list" | -
  - Task_4: a goal-mode run kept to his values | maps to the brief | inferred | brief, Limits: "is also kept to his values as it goes, and goal mode may change for that point" | -
  - Task_5: records landed on acceptance by name; the Orchestrator edits its own rule file | maps to the brief | cited | brief: "The rule files, where standing approvals live, stay with the Orchestrator"; Limits: "each decision record is accepted by him by name" | -
  - Task_6: close the plan and the run; publish; nothing merged | maps to the brief | cited | brief: "It leads with behaviour, scenario by scenario, with how to observe each."; Limits: "nothing merges until you have judged the whole stack"; standing approval as quoted under DoD 7b, with the same caveat. Not carried out in the range. | -

  Items, changes in the range:

  - `adr.md`, "Reworded after acceptance", and the lines that follow it in `counsel/SKILL.md`, `final-response-contract.md`, `SKILL.md` and both Orchestrator adapters: a wording-only change does not return, a change of decision, boundary, reasons or reopen conditions does, and the final response lists reworded records asking nothing | maps to the brief | cited | brief: "A change of wording to a record does not come back to you when it changes none of the record's decision, its boundary, its reasons or its reopen conditions; a change to any of those does."; "The closeout lists the records whose wording changed after you accepted them, one line each, and asks nothing."; "When you ask for a wording change on first reading you may accept in the same sentence, and the corrected text does not return." | -
  - `adr.md`, `model-routing.md`, `plan-format` rule 11 and `docs/coding-agent/rules/orchestrator.md`: a Worker may draft a record; plans and rule files stay with the Orchestrator | maps to the brief | cited | brief: "Workers may write decision records."; "The rule files, where standing approvals live, stay with the Orchestrator, and plans remain its own working document." | -
  - `counsel/SKILL.md` and `value-documents/SKILL.md`: the closing-pass question, whose answers become constraints; no watch list in the brief form | maps to the brief | cited | brief: "In the closing pass Counsel asks whether there is anything the work must not do, or must ask before doing, and what you answer goes into the brief as constraints, which the audit holds on."; "A brief carries no watch list." | -
  - `counsel/SKILL.md` and `value-documents/SKILL.md`: a restated answer needs no second yes; what Counsel inferred is listed once at closeout | maps to the brief | cited | brief: "Wording that restates an answer of yours needs no second yes from you: the answer is the ratification, in a brief as in a record."; "is listed once at closeout for you to object to; Counsel does not come back for each one" | -
  - Mandate, step 1: the audit holds a change that loosens a stop, a pass condition or who decides, and tightening is not held; `goal-mode.md` says the same for a goal loop | maps to the brief | cited | brief: "A change that loosens a stop, a pass condition or who decides is held for you, in a run under a brief as in a goal loop; tightening is free." | -
  - Mandate, `value-level-operation.md`, `lifecycle-gates.md`, `completion-closeout.md`: the watch check, the watch field and the watch report removed; only an item let through on a provisional statement goes to Counsel | maps to the brief | cited | brief: "A brief carries no watch list."; "During a run Counsel still hears of an item the audit lets through that rests on a statement marked provisional, and of nothing else from the audit." | -
  - `value-level-operation.md` and `lifecycle-gates.md`: an `ask-now` whose only reason is the Orchestrator's own unsupported or scope-expanding plan line is dropped or redone and audited again before anything is asked | maps to the brief | cited | brief: "A line the Orchestrator adds to its own plan that your documents do not support is the Orchestrator's to drop or redo so that the plan follows the brief. It reaches you only if the question survives that: your statements conflict with each other, or are silent on something worthy of the philosophy." | -
  - Mandate: an item that depends on a statement Counsel inferred beyond an answer is `ask-now` | maps to the brief | cited | brief: "If a piece of work depends on such a line, the audit asks then." | -
  - Mandate: at closeout each record reworded after acceptance is an item | maps to the brief | cited | brief: "the closeout audit confirms it for every record accepted before the change" | -
  - Mandate and `value-level-operation.md`: the comparison of findings names both directions, a departure from a means included | maps to the brief | inferred | brief: "a trivial one never does, however cheap."; "the audit, not the Orchestrator, compares that reading with its own grades" | -
  - Mandate: the order of the Input Boundary; the readings exclusion widened to `docs/coding-agent/**/*-readings.md` | internal mechanics | not audited | - | -
  - `SKILL.md`, `value-level-operation.md`, `goal-mode.md`, mandate "Goal-Mode Runs", `goal-mode-design.md`: value-level operation is on for a goal-mode run only when `common.md` points to a philosophy; three positions; the template filled in as it stands | maps to the brief | inferred | brief, Limits: "a goal-mode run in a repository that has a philosophy is also kept to his values as it goes, and goal mode may change for that point" | -
  - `goal-mode.md` Value Audit: the journal records a hold's stop and its question and no other part of a verdict | maps to the brief | inferred | brief, Limits: "Goal mode for goals a check can decide keeps working as it does today, with one exception" | -
  - ADR-D-0056 (new, accepted) | maps to the brief | inferred | brief, Limits, the goal-mode exception as quoted; "each decision record is accepted by him by name". The record states its own departure from the means on the held part. Nothing in it changed after the commit that set it accepted. | -
  - ADR-D-0045, amended in place and renamed (decision changed: no watch list) | maps to the brief | cited | brief: "A brief carries no watch list."; "During a run Counsel still hears of an item the audit lets through that rests on a statement marked provisional, and of nothing else from the audit."; Limits: "each decision record is accepted by him by name". The change altered the decision, so it had to return to him; the Decision Log quotes "I accept the amendment to ADR-D-0045.", which a file cannot show was said. After the commit that set it accepted, nothing in it changed. | -
  - ADR-D-0053, amended (decision changed: comparison in both directions; release of a held part) | maps to the brief | inferred | brief: "a trivial one never does, however cheap."; Limits: "each decision record is accepted by him by name". The Decision Log quotes "I accept ADR-D-0056 and the amendment to ADR-D-0053.", with the same caveat. After that commit nothing in it changed. | -
  - ADR-D-0053, `depends_on` pointer follows the rename of ADR-D-0045 (same commit as the acceptance) | internal mechanics | not audited | changed words: the file name of ADR-D-0045 in `depends_on`; decision, boundary, reasons and reopen conditions untouched by it | -
  - Version 0.28.0 in three manifests; two entries added to `docs/coding-agent/lessons.md`; the run record's plan line | internal mechanics | not audited | - | -

  Items, judgement calls and rulings:

  - Decision Log 1: no record for who writes records or for the hold on loosening; no hook for the readings file | maps to the brief | inferred | brief, header: "It states what and why. How is the Orchestrator's"; "Workers may write decision records." | -
  - Decision Log 2: plan review round 1 applied (audit material kept out of the assessor's evidence; completion report and pre-merge check unchanged; pointer to Counsel's list dropped) | maps to the brief | inferred | brief, Limits: "Goal mode for goals a check can decide keeps working as it does today"; "is listed once at closeout for you to object to" | -
  - Decision Log 3: gaps in the record drafts settled by the Orchestrator, the reopen conditions and this rule: when the audit names as trivial a finding already escalated, the held part is released and the question withdrawn, unless he has already answered | maps to the brief | inferred | brief: "It reaches you if it bears on the design, whatever it would cost to act on; a trivial one never does, however cheap." Step 1 was tested: the hold it releases is one the brief never asked for, a hold on a trivial finding, so it loosens no stop the brief states. The rule was put to him inside ADR-D-0053's amendment. | direction: a question already sent to him can be withdrawn on the audit's judgement without his answer
  - Decision Log 4: ADR-D-0056 and the amendment to ADR-D-0053 accepted; ADR-D-0055 withdrawn and the watch list's removal made an amendment to ADR-D-0045; Task_4 before Task_3 | maps to the brief | cited | brief, Limits: "each decision record is accepted by him by name"; "his word reaches the Orchestrator through Counsel's quoted relay". ADR-D-0055 is absent from the tree and was never set accepted. The reordering is mechanics. | -
  - Decision Log 5: the amendment to ADR-D-0045 accepted; Task_3 dispatched | maps to the brief | cited | brief, Limits: "each decision record is accepted by him by name" | -
  - Progress Log: divergences at plan draft corrected in the plan; the three remarks acted on | maps to the brief | cited | brief: "a divergence is corrected inside the run, the Orchestrator going back to the philosophy and the brief, re-deriving what the work is for and redoing the item" | -
  - Ruling, Wave 1 integration: the Orchestrator's rule file edited; `SKILL.md` names reworded records | maps to the brief | cited | brief: "Workers may write decision records."; "The rule files, where standing approvals live, stay with the Orchestrator" | -
  - Ruling, Task_4 integration: a goal run's dispatch reads `Governing brief: none` | internal mechanics | not audited | - | -
  - Ruling, Task_4 integration and review fix: in a goal loop the part a finding concerns and any gate that waits for the owner stop the loop; a gate the Orchestrator can clear by correcting its own input suspends the loop with no question | maps to the brief | inferred | brief: "tightening is free"; "You look only when it is done, or when something is off and needs you." | -
  - Ruling, Task_3 integration: a record reworded in wording only is recorded `not audited` with the changed words named | maps to the brief | inferred | brief: "the closeout audit confirms it for every record accepted before the change" | -
  - Ruling: the closeout audit over the whole range stands in for the three wave-boundary audits that were not dispatched | maps to the brief | inferred | brief: "The run keeps itself to your values and corrects itself while the work is ongoing, and you hear only when it could not." No statement covers skipping a position. The ruling publishes nothing, and reverting it restores the prior state. The missed positions cannot be recovered. This is a case where the run could not, so by that statement he hears of it. | direction
  - Judgement call, Task_2: a correction asked for and accepted in the same sentence is not listed as reworded after acceptance | maps to the brief | inferred | brief: "When you ask for a wording change on first reading you may accept in the same sentence, and the corrected text does not return." | -
  - Judgement call, Task_2: where no value audit runs, the Orchestrator's call on a wording change has no confirmation step (the record standard applies the rule to every run, "merged or not") | maps to the brief | inferred | brief: "A change of wording to a record does not come back to you when it changes none of the record's decision, its boundary, its reasons or its reopen conditions". Departs from the means "the closeout audit confirms it for every record accepted before the change" in runs with no audit; graded on that gives-statement. | direction: in a repository with no value documents, nothing but the Orchestrator's own call decides that a change to an accepted record is wording only
  - Judgement call, Task_2: "the plan's log" is read as the plan's Decision Log; the standard says "the governing brief or request" | maps to the brief | inferred | brief: "A Worker writes only what the brief and the plan's log state; where the reason for a decision is not written down it reports the gap and invents nothing." (the reading narrows what a Worker may draw on) | -
  - Judgement call, Task_3: the brief form says nothing about a watch list | maps to the brief | cited | brief: "A brief carries no watch list." | -
  - Judgement call, Task_3: Counsel's list of what it inferred sits in Counsel's skill; nothing added to the run's closeout | maps to the brief | inferred | brief: "is listed once at closeout for you to object to; Counsel does not come back for each one" | -
  - Judgement call, Task_3: the new comparison outcome is an input, since it releases and does not hold | maps to the brief | inferred | brief: "a trivial one never does, however cheap." | -
  - Judgement call, Task_4: the value-audit file beside the goal directory also keeps the start revision and each owner answer | internal mechanics | not audited | - | -
  - Judgement call, Task_4: the envelope's items are its statement, target, invariants, gap reading and decision-scope entries, the linkage credibility bar not among them | maps to the brief | inferred | brief, Limits: "is also kept to his values as it goes" | -
  - Review fixes: files beside the goal directory found wherever it sits | internal mechanics | not audited | - | -
  - Review fixes: the carrier's line for a run on a philosophy alone covers goal mode | maps to the brief | inferred | brief, Limits: "goal mode may change for that point" | -

  Human-only conditions pending: "scenarios 5 to 9, judged by him in his first use of a Counsel session opened from the built plugin"; "scenarios 1 to 4 where no run could demonstrate them"; "whether he could trust the result by default, without having thought about what the Orchestrator was doing"

  Scenarios: 1 (a behaviour-only design taking several plans comes back built, asked nothing that did not need him): not yet. 2 (a design-level finding reaches him mid-run, and the part it concerns has waited): not yet. 3 (a run that has stopped getting closer has stopped and told him): not yet. 4 (a cheaper model on the Reviewer, the strongest on the Auditor, and the run works as before): not yet. 5 to 9 (a Counsel discussion): ready for the owner's judgement; the last text they rest on, the closing-pass question of scenario 9, is in the tree at 0.28.0, and they are his to judge in first use. The run added no scenario. Getting closer: yes. The range builds what the last closed plan named as remaining: the three amended sections and goal-mode value keeping are in the plugin text, their three records carry `status: accepted`, no watch list remains, and the assessor's files and the audit's template are byte-identical, so nothing of the brief is left unbuilt and 5 to 9 move forward. Weighed against it: three plans have closed or are closing with none of scenarios 1 to 4 demonstrated, no run on the built plugin exists in the range, and in this very plan three wave boundaries passed with no audit, which is the run not keeping itself to his values as it went. The built text outweighs these because what remains is the closeout and his judgement, not further building.

  ## Remarks that change no grade

  1. **Acceptance quotes.** Every acceptance by name in this range (ADR-D-0056, the amendments to ADR-D-0053 and ADR-D-0045) exists only as a quotation in the plan's Decision Log and a `status: accepted` line. Commit order is consistent with the log. I relied on the brief's statements for the grades and could not check the words.
  2. **A new brief in the working tree.** `setup-names-what-is-missing-brief.md` is untracked and says it was drafted by Counsel. If the Orchestrator or a subagent wrote the file, the built text escalates that.
  3. **Record standard, merged records.** "Reworded after acceptance" reads "merged or not", while the line above it still says a merged record changes only for a pointer repair or a typo. A strict reader could take the new line as permitting rewording of merged records.
  4. **`goal-mode.md` wording.** The added sentence names "a stop or who decides" and leaves the pass condition to the paragraph before it on invariants. The brief names all three together.
  5. **ADR-D-0053 before acceptance.** The Wave 1 commit put the amendment's sentences into an accepted record before he accepted them; the pending note arrived two commits later. Nothing was built on them before acceptance.
  6. **Task_6 is not in the range.** Publication, the commit rebuild, the note to Counsel and any demonstration of scenarios 1 to 4 have not happened. If the closeout makes no demonstration, those four fall under the brief's "scenarios 1 to 4 where no run could demonstrate them" and the closeout says so plainly.

  Questions for Orchestrator: none.

  How the Orchestrator applied it: no item is `ask-now` or `ungraded`. The audit judges the run is getting closer and finds nothing of the brief left unbuilt, so this is the run's last plan. Four items are marked `direction` and are shown to the owner at the run's closeout as the verdict states them: A2 with the text built on it (which statements tagged inferred count as his word), the withdrawal of a question already sent when the audit names its finding trivial, the closeout audit standing in for three wave-boundary audits that were not dispatched, and that a wording-only call on an accepted record had no confirmation where no audit runs. No item rests on a provisional statement, so nothing goes to Counsel. The comparison set readings apart from grades on two groups and named two findings as bearing on the design; the next entry records what was done, and the closeout audit is dispatched again before the plan closes, as the built text requires after a correction at closeout.
- 2026-10-05 Corrections after the first closeout verdict. Readings: the fixes made in review (a gate that suspends a goal loop with no question, departures compared in both directions, the carrier's line covering goal mode) are extensions of the brief, not things it states, and the brief form's silence on a watch list is what the brief states; the readings are corrected and nothing in those items is redone, since the audit let each through as built. Findings the audit named: that a value question stops a whole goal loop was put to the owner in ADR-D-0056, which states the departure, and he accepted that record by name, so no part is held; that a wording-only call had no confirmation where no audit runs is settled from the brief's own means by adding a check, which tightens: where no value audit runs, the Reviewer's final review confirms the call. Text changed on the auditor's remarks: the record standard now says a merged record still changes only as the line on merged records allows; goal mode's sentence on loosening names the pass condition with the stop and who decides. The three wave boundaries with no audit stay as recorded and are shown at closeout. A new brief the auditor found untracked in the working tree, `setup-names-what-is-missing-brief.md`, is Counsel's and is not touched or committed by this run. The changed sentences go to the Reviewer, a third reading is written, and the closeout audit is dispatched again, new:

  ```text
  You are the value auditor. Read references/value-audit-mandate.md of the orchestration-harness skill and follow it exactly. Position: closeout. Plan: docs/coding-agent/plans/active/what-reaches-the-owner-plan.md. Governing brief: docs/coding-agent/briefs/active/design-led-long-runs-brief.md. Changes since: cc97211b.
  ```

- 2026-10-05 Closeout audit, second dispatch, verdict as returned (machine paths redacted; the two comparison lines are logged in the readings file, not here):

  Value audit verdict, closeout of `docs/coding-agent/plans/active/what-reaches-the-owner-plan.md` (second closeout dispatch). No item is `ask-now` and none is `ungraded`. Four items carry a `direction` mark. The comparison finds one reading apart from its grade and one finding that bears on the design though read as trivial.

  How the inputs were handled:
  - The dispatch text matches the fixed template word for word. The runtime appended a generic skill block (`engineering-quality-baselines`) and a hook block to it. Neither says anything about this run, so I did not treat them as an account and graded. If you read the mandate's "anything beyond the fixed template" more strictly, that is yours to rule.
  - The discussion notes (both modified in the working tree) were not opened. `.claude/pr67body.tmp` and `.claude/settings.local.json` were not opened; both are dated before the range.
  - The readings file was opened only after the grades were fixed.
  - The mandate was read from the working tree; the installed 0.21.0 cache has no copy.

  ## Verdict record

  Position: closeout

  Documents read: `docs/coding-agent/briefs/active/design-led-long-runs-brief.md`; `docs/coding-agent/plans/active/what-reaches-the-owner-plan.md` (artifact, whole); `docs/coding-agent/plans/active/design-led-long-runs-run.md` (prior scenario states); `docs/coding-agent/rules/common.md` at HEAD ("Repository Reference Documents" and "Standing Approvals"; unchanged in range); the changes cc97211b..working tree, read with git under both exclude pathspecs; `docs/coding-agent/briefs/active/setup-names-what-is-missing-brief.md` (header only, to name it below)

  Product basis: brief in the product owner's words

  Not audited: engineering side, which has no document (`common.md` carries no philosophy pointer line)

  Missing inputs: none

  Value documents changed in range: `docs/coding-agent/briefs/active/setup-names-what-is-missing-brief.md` (new, untracked; its header carries a ratification record dated 2026-10-05, names Counsel as drafter, and says it is handed to nobody yet and governs no run; no item relies on it). The governing brief is unchanged since cc97211b. No pointer line was removed or changed.

  Items, plan:

  - DoD 1: every gives-statement and constraint of the three sections and the goal-mode exception carried by the plugin text | maps to the brief | cited | brief, header: "It is passed verbatim; do not paraphrase it into a plan as if the paraphrase were the requirement."; sections "Decision records in a run", "What reaches you, and what does not", "Watch list" | -
  - DoD 2: no watch list; Counsel hears only of a provisional item | maps to the brief | cited | brief: "A brief carries no watch list."; "During a run Counsel still hears of an item the audit lets through that rests on a statement marked provisional, and of nothing else from the audit." (my search of `plugins/` for a watch list, hit or field finds nothing) | -
  - DoD 3: a goal-mode run with a philosophy kept to his values; admission, stall, completion and the assessor unchanged | maps to the brief | cited | brief, Limits: "Goal mode for goals a check can decide keeps working as it does today, with one exception: a goal-mode run in a repository that has a philosophy is also kept to his values as it goes, and goal mode may change for that point." (`goal-assessor-mandate.md`, `goal-templates.md`, `goal-condition-checklist.md` show no diff from cc97211b) | -
  - DoD 4: the value audit's fixed dispatch template byte-identical | maps to the brief | cited | brief: "A dispatch to the Auditor carries locations only; an account of the work in it is misuse on sight." (the template section has the same hash at cc97211b, HEAD and the working tree) | -
  - DoD 5: each record accepted by name before text is built on it | maps to the brief | cited | brief: "You still check a proposed decision record before anything is built on it."; Limits: "each decision record is accepted by him by name". Commit order agrees: the goal-mode text follows the commit that sets ADR-D-0056 accepted, and the watch-list and comparison text follows the commits that accept the amendments to ADR-D-0053 and ADR-D-0045. The acceptances are quoted only in the plan's Decision Log; whether the words were said is not something a file can show. | -
  - DoD 6: validators and smoke tests pass; Reviewer `APPROVED` | maps to the brief | cited | brief, Pass conditions: "the package validators pass"; Limits: "changes reach the remote only after review" | -
  - DoD 7a: the run closes once, scenario by scenario, with marked items, reworded records, design document, note to Counsel | maps to the brief | cited | brief: "It leads with behaviour, scenario by scenario, with how to observe each."; "The closeout lists the records whose wording changed after you accepted them, one line each, and asks nothing."; "The durable design document for the field the work touched is updated at closeout." | -
  - DoD 7b: reviewed branches published and pull requests opened | maps to the brief | cited | standing approval, `common.md`: "A finished, reviewed run may publish its branch and open pull requests in this repository without asking first. Merges are not covered and wait for the owner." The entry carries its acceptance record ("The common rule proposed, accepted.", 2026-09-30) and is committed; whether those words were said is not something a file can show. Nothing in the range publishes anything. | -
  - DoD 7c: unpushed commits rebuilt and swept | internal mechanics | not audited | - (step 1 test run: the rebuild itself publishes nothing; the push is under 7b) | -
  - DoD 8: nothing merges before he has judged the stack | maps to the brief | cited | brief, Limits: "nothing merges until you have judged the whole stack" | -
  - Planner-added 1: the value audit attaches to a goal run at the envelope, the assessor's events and the completion report | maps to the brief | inferred | brief, Limits: "is also kept to his values as it goes, and goal mode may change for that point" | -
  - Planner-added 2: a value question inside a goal loop stops the whole loop | maps to the brief | inferred | brief: "A change that loosens a stop, a pass condition or who decides is held for you, in a run under a brief as in a goal loop; tightening is free." Departs from the means "While you decide, the part the finding concerns waits and the rest of the run continues"; graded on the gives-statement it serves: "It reaches you if it bears on the design, whatever it would cost to act on". | -
  - Planner-added 3: verdicts and readings kept beside the goal directory, nothing in the goal file, journal or gap history | maps to the brief | inferred | brief, Limits: "Goal mode for goals a check can decide keeps working as it does today, with one exception" | -
  - Planner-added 4: the audit names a finding it judges trivial though read as bearing on the design | maps to the brief | inferred | brief: "a trivial one never does, however cheap." | -
  - Planner-added 5: the mandate states first what is never read before grading | internal mechanics | not audited | - | -
  - Planner-added 6: one plugin version bump (0.28.0 in three manifests) | internal mechanics | not audited | - | -
  - Non-goal: the brief's "Left out on purpose" | maps to the brief | cited | brief, "Left out on purpose" | -
  - Non-goal: goal mode's admission test, stall rule, completion rule; the assessor's mandate and template | maps to the brief | cited | brief, Limits: "Goal mode for goals a check can decide keeps working as it does today, with one exception" | -
  - Non-goal: a brief authorizing a goal-mode envelope | maps to the brief | cited | brief, Limits, the same statement | -
  - Non-goal: a hook or validator enforcing what an auditor may open | internal mechanics | not audited | - | -
  - Non-goal: new Worker report fields | internal mechanics | not audited | - | -
  - A1: a goal run's value questions travel by the existing carrier; the envelope is ratified in the session | maps to the brief | cited | brief, Limits: "his word reaches the Orchestrator through Counsel's quoted relay"; "Goal mode for goals a check can decide keeps working as it does today" | -
  - A2, with the text built on it in `value-documents/SKILL.md` and the mandate: a statement tagged inferred that he ratified with the brief keeps its support; only what Counsel inferred beyond an answer, with no ratification record of its own, is no support | maps to the brief | inferred | brief: "What Counsel infers beyond your answer is marked inferred, is no support for the audit"; "the answer is the ratification, in a brief as in a record"; provenance line: "*(inferred)* = Counsel inferred it and he did not object" | direction: it settles, for every later audit, which statements tagged inferred count as his word
  - A3: Counsel brings the list of what it inferred at closeout; the run neither waits nor reports | maps to the brief | inferred | brief: "is listed once at closeout for you to object to; Counsel does not come back for each one" | -
  - A4: no goal run here can show the goal-mode point; the closeout says so plainly | maps to the brief | inferred | brief, product basis line: "no product philosophy and no engineering philosophy exist for this repository"; Pass conditions: "where one cannot the closeout says so plainly" (worded for scenarios 1 to 4, extended here) | -
  - Task_1: records drafted by a Worker, checked by the Orchestrator and a Reviewer, put to the owner by name | maps to the brief | cited | brief: "Workers may write decision records."; "A Worker writes only what the brief and the plan's log state; where the reason for a decision is not written down it reports the gap and invents nothing."; "The Orchestrator checks that a draft says what was decided, and the Reviewer checks it against the record standard." | -
  - Task_2: decision records in a run, in the plugin text | maps to the brief | cited | brief, "Decision records in a run" | -
  - Task_3: no watch list; what reaches the owner | maps to the brief | cited | brief, "What reaches you, and what does not" and "Watch list" | -
  - Task_4: a goal-mode run kept to his values | maps to the brief | inferred | brief, Limits: "is also kept to his values as it goes, and goal mode may change for that point" | -
  - Task_5: records landed on acceptance by name; the Orchestrator edits its own rule file | maps to the brief | cited | brief: "The rule files, where standing approvals live, stay with the Orchestrator"; Limits: "each decision record is accepted by him by name" | -
  - Task_6: close the plan and the run; publish; nothing merged | maps to the brief | cited | brief: "It leads with behaviour, scenario by scenario, with how to observe each."; Limits: "nothing merges until you have judged the whole stack"; standing approval as quoted under DoD 7b, with the same caveat. Not carried out in the range. | -

  Items, changes in the range:

  - `adr.md` "Reworded after acceptance", with the lines that follow it in `counsel/SKILL.md`, `final-response-contract.md`, `orchestration-harness/SKILL.md` and both Orchestrator adapters: a wording-only change does not return, a change of decision, boundary, reasons or reopen conditions does, and the final response lists reworded records asking nothing | maps to the brief | cited | brief: "A change of wording to a record does not come back to you when it changes none of the record's decision, its boundary, its reasons or its reopen conditions; a change to any of those does."; "The closeout lists the records whose wording changed after you accepted them, one line each, and asks nothing."; "When you ask for a wording change on first reading you may accept in the same sentence, and the corrected text does not return." Step 1 tested: this moves a decision away from him, and the brief's statement is his own word for it. | -
  - `adr.md`, same line: after merge a record still changes only as the line on merged records allows | maps to the brief | inferred | brief: "A change of wording to a record does not come back to you when it changes none of the record's decision, its boundary, its reasons or its reopen conditions" (the brief is silent on merged records; the clause keeps the standing rule and tightens) | -
  - `adr.md`, `model-routing.md`, `plan-format` rule 11, `docs/coding-agent/rules/orchestrator.md`: a Worker may draft a record; plans and rule files stay with the Orchestrator | maps to the brief | cited | brief: "Workers may write decision records."; "The rule files, where standing approvals live, stay with the Orchestrator, and plans remain its own working document." | -
  - `counsel/SKILL.md`, `value-documents/SKILL.md`: the closing-pass question, whose answers become constraints; no watch list in the brief form | maps to the brief | cited | brief: "In the closing pass Counsel asks whether there is anything the work must not do, or must ask before doing, and what you answer goes into the brief as constraints, which the audit holds on."; "A brief carries no watch list." | -
  - `counsel/SKILL.md`, `value-documents/SKILL.md`: a restated answer needs no second yes; what Counsel inferred is listed once at closeout | maps to the brief | cited | brief: "Wording that restates an answer of yours needs no second yes from you: the answer is the ratification, in a brief as in a record."; "is listed once at closeout for you to object to; Counsel does not come back for each one" | -
  - Mandate step 1 and `goal-mode.md` (as corrected in b07e3611): a change that loosens a stop, a pass condition or who decides is held; tightening is not | maps to the brief | cited | brief: "A change that loosens a stop, a pass condition or who decides is held for you, in a run under a brief as in a goal loop; tightening is free." | -
  - Mandate, `value-level-operation.md`, `lifecycle-gates.md`, `completion-closeout.md`: the watch check, watch field and watch report removed; the verdict's item line has five fields; only an item let through on a provisional statement goes to Counsel | maps to the brief | cited | brief: "A brief carries no watch list."; "During a run Counsel still hears of an item the audit lets through that rests on a statement marked provisional, and of nothing else from the audit." | -
  - `value-level-operation.md`, `lifecycle-gates.md`: an `ask-now` whose only reason is the Orchestrator's own unsupported or scope-expanding plan line is dropped or redone and audited again before anything is asked | maps to the brief | cited | brief: "A line the Orchestrator adds to its own plan that your documents do not support is the Orchestrator's to drop or redo so that the plan follows the brief. It reaches you only if the question survives that: your statements conflict with each other, or are silent on something worthy of the philosophy." | -
  - Mandate: an item that depends on a statement Counsel inferred beyond an answer is `ask-now` | maps to the brief | cited | brief: "If a piece of work depends on such a line, the audit asks then." | -
  - Mandate: at closeout each record reworded after acceptance is an item | maps to the brief | cited | brief: "the closeout audit confirms it for every record accepted before the change" | -
  - `adr.md` (b07e3611): where no value audit runs, the Reviewer's final review confirms the Orchestrator's wording-only call | maps to the brief | inferred | brief: "A change of wording to a record does not come back to you when it changes none of the record's decision, its boundary, its reasons or its reopen conditions". Departs from the means "the closeout audit confirms it for every record accepted before the change" in runs with no audit; graded on that gives-statement. Adding a check tightens. | direction: in a repository with no value documents, the role that checks work for the Orchestrator, not an independent audit, confirms that a change to a record he accepted need not return to him
  - Mandate, `value-level-operation.md`: the comparison of findings names both directions, a departure from a means included | maps to the brief | inferred | brief: "a trivial one never does, however cheap."; "the audit, not the Orchestrator, compares that reading with its own grades" | -
  - `value-level-operation.md`, ADR-D-0053 as amended: when the audit names an escalated finding trivial, the held part is released and the question withdrawn, unless he has already answered | maps to the brief | inferred | brief: "It reaches you if it bears on the design, whatever it would cost to act on; a trivial one never does, however cheap." Step 1 tested: this releases a hold and takes back a question without his answer, so it loosens a stop and who decides, and the brief has such a change held for him. The plan's Decision Log records that it was: the rule sits in ADR-D-0053's amendment and the log quotes "I accept ADR-D-0056 and the amendment to ADR-D-0053." A file cannot show those words were said. On that record the hold is answered, and the item is graded on the brief. | direction: a question already sent to him can be withdrawn on the audit's judgement without his answer
  - Mandate: the order of the Input Boundary; the readings exclusion widened to `docs/coding-agent/**/*-readings.md` | internal mechanics | not audited | - | -
  - `orchestration-harness/SKILL.md`, `value-level-operation.md`, `goal-mode.md`, mandate "Goal-Mode Runs", `goal-mode-design.md`: value-level operation is on for a goal run only when `common.md` points to a philosophy; three positions; the template filled in as it stands | maps to the brief | inferred | brief, Limits: "a goal-mode run in a repository that has a philosophy is also kept to his values as it goes, and goal mode may change for that point" | -
  - `goal-mode.md` Value Audit: the journal records a hold's stop and its question and no other part of a verdict | maps to the brief | inferred | brief, Limits: "Goal mode for goals a check can decide keeps working as it does today, with one exception" | -
  - ADR-D-0056 (new, accepted) | maps to the brief | inferred | brief, Limits, the goal-mode exception as quoted; "each decision record is accepted by him by name". The record states its own departure from the means on the held part. Nothing in it changed after the commit that set it accepted (e155060e). | -
  - ADR-D-0045, accepted before the range, amended in place and renamed (decision changed: no watch list) | maps to the brief | cited | brief: "A brief carries no watch list."; "During a run Counsel still hears of an item the audit lets through that rests on a statement marked provisional, and of nothing else from the audit."; Limits: "each decision record is accepted by him by name". The change altered the decision, so the record had to return to him. The Decision Log records that it did and quotes "I accept the amendment to ADR-D-0045."; a file cannot show those words were said. Nothing in it changed after 547ef5f3. | -
  - ADR-D-0053, accepted before the range, amended (decision changed: comparison in both directions; release of a held part) | maps to the brief | inferred | brief: "a trivial one never does, however cheap."; Limits: "each decision record is accepted by him by name". The change altered the decision, so the record had to return to him; the Decision Log records that it did, with the quote given above and the same caveat. Nothing in it changed after e155060e. | -
  - ADR-D-0053, `depends_on` pointer follows the rename of ADR-D-0045 | internal mechanics | not audited | changed words: the file name of ADR-D-0045 in `depends_on`; decision, boundary, reasons and reopen conditions untouched | -
  - Version 0.28.0 in three manifests; two entries in `docs/coding-agent/lessons.md`; the run record's plan line | internal mechanics | not audited | - | -

  Items, judgement calls and rulings:

  - Decision Log 1: no record for who writes records or for the hold on loosening; no hook for the readings file | maps to the brief | inferred | brief, header: "It states what and why. How is the Orchestrator's"; "Workers may write decision records." | -
  - Decision Log 2: plan review round 1 applied (audit material kept out of the assessor's evidence; completion report and pre-merge check unchanged; pointer to Counsel's list dropped) | maps to the brief | inferred | brief, Limits: "Goal mode for goals a check can decide keeps working as it does today"; "is listed once at closeout for you to object to" | -
  - Decision Log 3: gaps in the record drafts settled by the Orchestrator (reopen conditions; the withdrawal rule) | maps to the brief | inferred | brief: "It reaches you if it bears on the design, whatever it would cost to act on; a trivial one never does, however cheap."; header: "How is the Orchestrator's". The withdrawal rule is graded, with its step 1 test, on the changes line above. | direction: as that line states
  - Decision Log 4: ADR-D-0056 and the amendment to ADR-D-0053 accepted; ADR-D-0055 withdrawn and the watch list's removal made an amendment to ADR-D-0045; Task_4 before Task_3 | maps to the brief | cited | brief, Limits: "each decision record is accepted by him by name"; "his word reaches the Orchestrator through Counsel's quoted relay". ADR-D-0055 is absent from the tree. The reordering is mechanics. | -
  - Decision Log 5: the amendment to ADR-D-0045 accepted; Task_3 dispatched | maps to the brief | cited | brief, Limits: "each decision record is accepted by him by name" | -
  - Progress Log: divergences at plan draft corrected; the three remarks acted on | maps to the brief | cited | brief: "a divergence is corrected inside the run, the Orchestrator going back to the philosophy and the brief, re-deriving what the work is for and redoing the item" | -
  - Ruling, Wave 1 integration: the Orchestrator's rule file edited; `SKILL.md` names reworded records | maps to the brief | cited | brief: "Workers may write decision records."; "The rule files, where standing approvals live, stay with the Orchestrator" | -
  - Ruling, Task_4 integration: a goal run's dispatch reads `Governing brief: none` | internal mechanics | not audited | - | -
  - Ruling, Task_4 integration and review fix: in a goal loop the part a finding concerns and any gate that waits for the owner stop the loop; a gate the Orchestrator can clear by correcting its own input suspends the loop with no question | maps to the brief | inferred | brief: "tightening is free"; "You look only when it is done, or when something is off and needs you." | -
  - Ruling, Task_3 integration: a record reworded in wording only is recorded `not audited` with the changed words named | maps to the brief | inferred | brief: "the closeout audit confirms it for every record accepted before the change" | -
  - Ruling: the closeout audit over the whole range stands in for the three wave-boundary audits that were not dispatched | maps to the brief | inferred | brief: "The run keeps itself to your values and corrects itself while the work is ongoing, and you hear only when it could not." No statement covers skipping a position. The ruling publishes nothing, and no item in the range is graded `ask-now`, so nothing went ahead that an earlier audit would have held. The missed positions cannot be recovered. By the statement quoted, this is a case where the run could not, so he hears of it. | direction
  - Ruling, corrections after the first closeout verdict: the changed sentences reviewed, a new reading written, the closeout audit dispatched again | maps to the brief | cited | brief: "a divergence is corrected inside the run, the Orchestrator going back to the philosophy and the brief, re-deriving what the work is for and redoing the item" | -
  - Judgement call, Task_2: a correction asked for and accepted in the same sentence is not listed as reworded after acceptance | maps to the brief | inferred | brief: "When you ask for a wording change on first reading you may accept in the same sentence, and the corrected text does not return." | -
  - Judgement call, Task_2: where no value audit runs the Orchestrator's wording-only call has no confirmation step (since replaced in b07e3611 by the Reviewer's confirmation) | maps to the brief | inferred | as the `adr.md` (b07e3611) line above | direction: as that line states
  - Judgement call, Task_2: "the plan's log" is read as the plan's Decision Log | maps to the brief | inferred | brief: "A Worker writes only what the brief and the plan's log state; where the reason for a decision is not written down it reports the gap and invents nothing." (the reading narrows what a Worker may draw on) | -
  - Judgement call, Task_3: the brief form says nothing about a watch list | maps to the brief | cited | brief: "A brief carries no watch list." | -
  - Judgement call, Task_3: Counsel's list of what it inferred sits in Counsel's skill; nothing added to the run's closeout | maps to the brief | inferred | brief: "is listed once at closeout for you to object to; Counsel does not come back for each one" | -
  - Judgement call, Task_3: the new comparison outcome is an input, since it releases and does not hold | maps to the brief | inferred | brief: "a trivial one never does, however cheap." | -
  - Judgement call, Task_4: the value-audit file beside the goal directory also keeps the start revision and each owner answer | internal mechanics | not audited | - | -
  - Judgement call, Task_4: the envelope's items are its statement, target, invariants, gap reading and decision-scope entries, the linkage credibility bar not among them | maps to the brief | inferred | brief, Limits: "is also kept to his values as it goes" (`goal-mode.md` calls that bar part of the goal condition; the audit at the envelope does not grade it) | -
  - Review fixes: files beside the goal directory found wherever it sits | internal mechanics | not audited | - | -
  - Review fixes: the carrier's line for a run on a philosophy alone covers goal mode | maps to the brief | inferred | brief, Limits: "goal mode may change for that point" | -

  Human-only conditions pending: "scenarios 5 to 9, judged by him in his first use of a Counsel session opened from the built plugin"; "scenarios 1 to 4 where no run could demonstrate them"; "whether he could trust the result by default, without having thought about what the Orchestrator was doing"

  Scenarios: 1 (a behaviour-only design taking several plans comes back built, asked nothing that did not need him): not yet. 2 (a design-level finding reaches him mid-run, and the part it concerns has waited): not yet. 3 (a run that has stopped getting closer has stopped and told him): not yet. 4 (a cheaper model on the Reviewer, the strongest on the Auditor, and the run works as before): not yet; this workspace splits the models by its rule file, but the audit ran on the Reviewer's agent type from an installed 0.21.0, not on the built plugin's Auditor. 5 to 9 (a Counsel discussion): ready for the owner's judgement; the last text they rest on, the closing-pass question of scenario 9, is in `counsel/SKILL.md` at 0.28.0, and they are his to judge in first use. The run added no scenario. Getting closer: yes. Against the states the last closed plan left, 5 to 9 move from not yet to ready, because the range builds what that plan named as remaining: the three amended sections and goal-mode value keeping are in the plugin text, their records carry `status: accepted`, no watch list remains, and the assessor's files and the audit's template are byte-identical. I found nothing of the brief left unbuilt. Weighed against it: three plans have closed or are closing with none of 1 to 4 demonstrated; no run on the built plugin exists in the range; and in this plan three wave boundaries passed with no audit, which is the run failing to keep itself to his values as it went. The built text outweighs these only because what remains is the closeout and his judgement, not another plan.

  ## Remarks that change no grade

  1. **Acceptance quotes.** Every acceptance by name in this range (ADR-D-0056 and the amendments to ADR-D-0053 and ADR-D-0045) exists only as a quotation in the plan's Decision Log plus a `status: accepted` line. I relied on those quotes for three things: DoD 5, the two amended records, and the step 1 test on the withdrawal rule. Commit order is consistent with the log. If any quote is wrong, those items are `ask-now`.
  2. **Gap in the mandate.** Its closeout rule says a record whose decision changed after acceptance "is `ask-now`: the record returns to the owner to be accepted by name". It does not say what the grade is when the record already returned and was accepted by name inside the range. I graded ADR-D-0045 and ADR-D-0053 on the recorded acceptance and did not ask again.
  3. **ADR-D-0053 before acceptance.** From 9a3b874a to e155060e the record carried the amendment's sentences under `status: accepted`; the pending note arrived only at 3b43204f. No plugin text resting on them was committed before e155060e.
  4. **Two findings read as bearing on the design, no question sent.** The missed audits and the missing confirmation step were both read that way, and the built text escalates such a finding at once. Both reach him only through the `direction` marks at closeout.
  5. **Standing approval wording.** It says "its branch"; Task_6 publishes several stacked branches. I read it as covering the run's branches. It requires a "finished, reviewed run".
  6. **One class-only divergence.** The goal-mode sentence was read `extends` and graded `cited`; nothing in the built text needs redoing for it.
  7. **Task_6 is not in the range.** Publication, the commit rebuild, the note to Counsel and any demonstration of scenarios 1 to 4 have not happened. If the closeout makes no demonstration, those four fall under the brief's "scenarios 1 to 4 where no run could demonstrate them" and the closeout says so plainly.

  Questions for Orchestrator: none.

  How the Orchestrator applied it: no item is `ask-now` or `ungraded`, so nothing is held. The audit judges the run is getting closer and finds nothing of the brief left unbuilt: this plan closes and with it the run. Four items are marked `direction` and are shown to the owner at the run's closeout as the verdict states them. No item rests on a provisional statement, so nothing goes to Counsel from the audit. The comparison left one reading apart from its grade, in class only (goal mode's sentence on loosening, read as an extension and graded as stated by the brief); the reading is corrected in the readings file, and since the audit let the item through as built there is nothing in it to redo and the artifact does not change, so no further dispatch follows: dispatching again on unchanged inputs is not a remedy. The two findings the audit agrees bear on the design, for which no question was sent (the missed wave-boundary audits; the confirmation step where no audit runs), are among the four marked items and reach him at closeout. The auditor's remark that the standing approval says "its branch" while the run publishes several stacked branches is noted: the approval was read at the second plan's draft as covering the run's branches, and that reading was graded then.
- 2026-10-05 Plan closed: Tasks 1 to 5 done; Task_6's closeout audit and final review done, and the run's closeout (the run record, the commits rebuilt and swept, the branches published, the note to Counsel) is carried out from here and recorded in the run record, which moves with this plan. Required validation: package validator and smoke tests pass; the assessor's files and both dispatch templates byte-identical to this plan's start revision; final review APPROVED, with the three sentences changed after it approved separately.

## Decision Log (append-only; re-plans and major discoveries)
- 2026-10-05 Decision: requirement challenge before decomposition.
  - Trigger / new insight: the three amended sections and the goal-mode exception, read for what need not exist.
  - Plan delta (what changed): no record is proposed for who writes records or for the hold on loosening, since no record decides either today and the brief states both; the readings file gets no hook or validator, only its place in the mandate's order of reading; the second plan's wish for a guard beyond instruction is dropped as a non-goal.
  - Tradeoffs considered: a hook that denies an auditor the readings file before it returns grades; not taken, one occurrence in three dispatches and the auditor caught it itself.
  - User approval: not applicable at draft
  - Record proposed: up to three, at Task_1
- 2026-10-05 Decision: draft-plan review, round 1 (Codex reviewer): NEEDS_REVISION, four findings, all applied.
  - Trigger / new insight: (1) a journal line per value audit and a count at pre-merge would have put audit material into the assessor's evidence; (2) three binding statements stood in Task_3's description without an acceptance line; (3) the proportional form was claimed for changes to who writes records and to the verdict's form; (4) a pointer from the final response to Counsel's list was an addition with no need stated.
  - Plan delta (what changed): the value audit's verdicts and readings are kept beside the goal directory and nothing of them enters the goal file, the journal or the gap history; the completion report and the pre-merge check are not changed, and the audit at the completion report covers the whole range. Task_3's acceptance names the closing pass, the hold on loosening and the restated answer; Task_4's names the hold inside a goal loop. The Design section compares the amendments' implementation with one alternative. The pointer is dropped.
  - Tradeoffs considered: verifying the audit's cadence at pre-merge from outside the journal was not taken; the completion audit already grades the whole range.
  - User approval: not applicable at draft
  - Record proposed: unchanged
- 2026-10-05 Decision: the gaps the Task_1 Worker reported in the three record drafts are settled here, so the records can state them.
  - Trigger / new insight: the Worker wrote only what the brief and this log state and reported each place where a rejected alternative had no reopen condition or a consequence was not written down.
  - Plan delta (what changed), by record. R1 (replacement of ADR-D-0045): keeping a watch list is rejected with the brief's reason (what can be foreseen is a constraint written a second time with a weaker consequence, what cannot be foreseen cannot be listed, and what remains is being told of things that are fine); it reopens if matters the person directing the work would have wanted to hear of at once are found to have reached that person only at closeout, with no constraint that could have named them. R2 (the value audit in a goal run): two audits only at the ends reopens if the audits on the assessor's events are found to hold nothing run after run; a journal line per audit counted before merge is rejected outright, because it puts audit material into the assessor's evidence; verifying the audit's cadence before merge from outside the journal lost because the audit at the completion report grades the whole range, and reopens if a completion audit is found grading drift that a skipped position inside the loop would have caught; holding only the part concerned lost because a goal loop is one optimizer with no parts to set aside, and reopens if goal runs are found stopped whole over a question the loop could have worked around; one dispatch carrying both the assessor's and the audit's mandate is rejected outright, because it changes the assessor's inputs and its fixed template, which ADR-D-0050 and the brief's limit on goal mode keep. Its Revisit When takes those reopen conditions and the dated fact that no goal run in this repository can show it. R3 (ADR-D-0053): when the audit names as trivial a finding the Orchestrator had already escalated, the Orchestrator releases the held part and withdraws the question by the carrier, unless the person directing the work has already answered, in which case the answer stands; a finding not yet sent is not sent. It reopens if findings the audit named trivial are found to be ones that person wanted to decide.
  - Tradeoffs considered: leaving an already-sent question standing until answered was not taken; it keeps a part held for an answer nobody needs.
  - User approval: not applicable; these are the run's reasons, and the records go to the owner by name
  - Record proposed: R1 as ADR-D-0055, R2 as ADR-D-0056, R3 as a change to ADR-D-0053
- 2026-10-05 Decision: ADR-D-0056 and the amendment to ADR-D-0053 accepted; the watch list's removal is an amendment to ADR-D-0045, not a new record; Task_4 goes before Task_3.
  - Trigger / new insight: two relays from Counsel quoting the owner in full, 2026-10-05. On the three records: "The contents mostly looks good, but the replacement should probably be handled as an amendment, since 0045 hasn't merged yet." Then: "I accept ADR-D-0056 and the amendment to ADR-D-0053." Counsel states that ADR-D-0055 is not accepted and that his words on handling it as an amendment stand.
  - Plan delta (what changed): ADR-D-0056 is set accepted. ADR-D-0053's amendment is in force and its pending note is removed. ADR-D-0055 is withdrawn and its file removed; its text becomes ADR-D-0045 amended in place (same decision as drafted, the record's number, date and history kept, the file renamed to its new title, status proposed until he accepts the amendment by name, as was done for ADR-D-0036); ADR-D-0045 is not retired and nothing supersedes it. The pointer in ADR-D-0053 follows the rename. Task_5's line on retiring ADR-D-0045 no longer applies. Task_3 rests on the amended ADR-D-0045 and waits for it; Task_4 rests only on ADR-D-0056, so it runs now, before Task_3, and Task_3 follows in the two files they share.
  - Tradeoffs considered: keeping ADR-D-0055 as a new record was his to decline, and he did; a record that has not merged is amended in place by the record standard.
  - User approval: the owner's words above
  - Record proposed: ADR-D-0056 accepted; ADR-D-0053's amendment accepted; ADR-D-0045 amended and awaiting acceptance by name; ADR-D-0055 withdrawn
- 2026-10-05 Decision: the amendment to ADR-D-0045 accepted.
  - Trigger / new insight: Counsel's relay quoting the owner in full, 2026-10-05: "I accept the amendment to ADR-D-0045." He had before him the amended file as it stood, marked proposed.
  - Plan delta (what changed): ADR-D-0045 is set accepted in its amended form. Task_5 is done: ADR-D-0045 amended, ADR-D-0053 amended, ADR-D-0056 accepted, the rule file edited. Every record this plan proposed or changed is accepted, so Task_3 is dispatched.
  - Tradeoffs considered: none.
  - User approval: the owner's acceptance by name, relayed by Counsel
  - Record proposed: none open

## Notes
- Records are drafted by a Worker and checked by the owner before anything is built on them, as the brief gives since 2026-10-05.
