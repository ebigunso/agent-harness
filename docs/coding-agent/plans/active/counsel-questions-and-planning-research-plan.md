# Plan: Counsel's questions while drafting, and research before a plan

- status: in_progress
- generated: 2026-10-15
- last_updated: 2026-10-15
- work_type: docs

## Goal
- The harness gives what the governing brief `docs/coding-agent/briefs/active/counsel-questions-and-planning-research-brief.md` states: Counsel's questions while drafting a brief pass the experience-framing test before reaching the owner, who ratifies on framings and sees the unassisted path as the default; an execution plan is drafted only after the research that makes it concrete, with unknowns stated and plan review flagging an investigation-first plan; the plugin's version becomes 1.0 as the last change before the stack is reported ready.
- The brief is the requirement and is not restated here; where this plan and the brief differ, the brief governs and the difference is a plan defect.
- This is the first plan of the run recorded in `docs/coding-agent/plans/active/counsel-questions-and-planning-research-run.md`.

## Definition of Done
- The Counsel skill states, where the conversation is held, that before a question reaches the owner while a brief is being drawn out Counsel writes it as an experience change (who, what they do, what they then experience, the options side by side); options that read the same at that level are Counsel's to decide, written into the brief tagged inferred or agent-proposed; options that read differently go to the owner in that form; the framing is the test. A conflict between statements Counsel itself drafted is resolved the same way when the discussion made the intent plain. The same test applies any time Counsel puts a question to the owner, not only while a brief is drafted (during a run, at closeout, in any discussion); the acts the owner reserved reach the owner regardless (brief amendment of 2026-10-15).
- The Counsel skill states, where ratification is, that the owner is shown the experience framings for the decisions in the brief that changed anything, not the brief; the brief stays the record on disk for the run and the audit. The sentence that presents the full text again after a correction, and the closeout list of inferred lines, agree with this: the framings are what the owner sees, the tags stay in the brief for the audit.
- The Counsel skill states that where the work could be done with or without the owner's help, the brief states the unassisted path as the default and the assisted path as the backup; Counsel does not ask which and at most tells the owner once that the backup may be needed.
- No repository rule file carries any of these rules; the definitions of the brief's tags and of what ratification covers in the value-documents skill agree with ratification on framings.
- The Research Dispatch Gate and its procedure say that before an execution plan is drafted the investigation needed to decide what it should contain is done (current behaviour, affected areas, constraints, validation approach), depth proportional to the change, and that its findings are what the tasks are written from; the plan still states what, why and constraints.
- The plan template and the planning rules carry a material unknown as: what is unknown, why, and what decision or evidence is needed, with dependent work conditional or awaiting replanning, never settled behind a generic investigate-first task; a research task that is a legitimate deliverable states the question it answers, the expected evidence and how its outcome affects later work.
- The plan-review snippet flags an investigation-first plan when that task merely postpones research needed to make the rest of the plan concrete, and does not flag a research task that is a legitimate deliverable: the request is itself an investigation, or a bounded experiment or implementation-stage check is genuinely necessary, and the task states its question, expected evidence and effect on later work; the three statements alone exempt nothing.
- Scenarios 3 and 4 of the brief are shown on a fixture in a temporary directory, the outcome recorded in the Progress Log: for scenario 3 the fresh session's record shows the investigation and its findings before its first plan draft, and the draft's tasks rest on them; a genuinely necessary bounded research task in the same fixture is not flagged.
- The plugin's version is 1.0 in every file that states the plugin's version, made as the last change before the run is reported ready.
- Package validators and smoke tests pass; the branch has Reviewer `APPROVED`; the plan closes and the run is reported ready: branch published on the stack, pull request opened under the standing approval, note to Counsel, nothing merged.

## Planner-added requirements
- The scenario 4 fixture also holds a control plan whose first task is a legitimate research deliverable by the brief's condition (a bounded check that is genuinely necessary because its answer cannot be read from the repository, with its question, expected evidence and effect on later work stated), and the plan review must not flag it. Needed because: the brief's constraint that research remains a legitimate deliverable is otherwise unchecked by the fixture, and a check that flags every research-first plan would meet scenario 4 while breaking the constraint.

## Scope / Non-goals
- Scope: `skills/counsel/SKILL.md`; `skills/value-documents/SKILL.md` (tag definitions and what ratification covers); a decision record where the admission test passes on the framing test as a filter on what reaches the owner, revised to any time by Task_5 (whether ADR-D-0046 changes is decided by whether its own decision or boundary words are broken, not assumed); `skills/orchestration-harness/SKILL.md` (Research Dispatch Gate); `skills/orchestration-harness/references/lifecycle-gates.md` (Research Dispatch Details); `skills/orchestration-harness/references/dispatch-guidance.md` (Researcher dispatch); `skills/plan-format/SKILL.md` and `references/plan-template.md`; `skills/subagent-strategy/references/prompt-snippets.md` (plan-review snippet; the Researcher snippets); the Orchestrator adapters where they restate the gate; the three plugin manifests and the two marketplace plugin entries for the version; a fixture in a temporary directory.
- Non-goals: issues 87, 88 and 89; the both-ways line on matters differing from what the owner believes was agreed; any repository rule file; the fixed audit dispatch template; validators for prose (ADR-I-0007); the level test of what reaches the owner from a run (Contacts with a run; `value-level-operation.md` Asking The Owner), which stays as it is: the framing test is placed beside it by Task_5, not in place of it; the audit's closeout list of marked items (ADR-D-0042), a different mechanism from the brief's inferred lines.

## Design
- Chosen: each rule tightens the sentence nearest to where it acts. Issue 90: the framing test enters "How a conversation goes" beside the sentence that already puts every question as the chain, and the ratification and unassisted-default rules enter "Drafting and ratification", with the two sentences that conflict (present the full text again; the closeout list of inferred lines) reworded to agree; the value-documents definitions of inferred, agent-proposed and ratification are tightened so that a line Counsel decided and the owner ratified on its framing has its support. Issue 86: the Research Dispatch Gate's two lines say what the research is for and when it is enough; the procedure in lifecycle-gates carries the unknown's form and the research task's three statements; the plan template's Assumptions line carries the unknown's form; the plan-review snippet gains one check.
- Alternative: a new reference `skills/counsel/references/drafting-a-brief.md` holding the four rules with a pointer from SKILL.md, and a new reference `planning-research.md` holding the issue 86 behaviour with pointers from the gate, the template and the snippet.
- Lenses. structure: chosen edits sentences that already govern those moments; the alternative adds two files and four pointers, and the rules would sit apart from the sentences they qualify (the chain sentence; the ratification steps; the gate). evolution: chosen leaves the skill's shape as it is; the alternative adds files to keep in step with SKILL.md. verification: both checked by reading against the brief; chosen is checked by "the Counsel skill carries the rules" and "the planning text carries the behaviour" directly. operation: chosen adds no read; the alternative adds a read at every brief drafting and every plan. human: an agent meets the rule where it acts. safety: neither touches a trust boundary; neither adds a code norm.
- Why chosen: the brief's constraint puts the rules in the Counsel skill, and its means builds on the existing gate; a second home for either is what the alternative adds.

## Compatibility stance (required if a contract/interface/persisted format is touched)
- surface: the brief's tag definitions (what inferred and agent-proposed mean, what ratification covers); the plan-review snippet's checks; the plan template's Assumptions line.
- stance: migrate
- justification: existing briefs keep their tags and ratification records (the definitions widen what the tags may cover, they do not change what an existing tag means); existing plans stay valid for `validate_plan.py`, which checks no field this plan adds; the readers of each surface (Counsel drafting; the Auditor grading support; the Reviewer at plan review; the Orchestrator drafting) have their text changed in this plan, so no layer carries the old meaning.

## Context (workspace)
- Governing brief: `docs/coding-agent/briefs/active/counsel-questions-and-planning-research-brief.md`. Ratification reached this session on 2026-10-15 as Counsel's relay quoting the owner (2026-10-14): "I ratify the brief, hand it over now." Relays admitted by the Standing Approvals entry of 2026-10-01 in `common.md`.
- Run record: `docs/coding-agent/plans/active/counsel-questions-and-planning-research-run.md`. Readings file: `docs/coding-agent/plans/active/counsel-questions-and-planning-research-readings.md`. This plan starts from revision: 25f9831 (the brief committed on the run's branch, on top of pull request 85's branch).
- Research: two Researchers. Issue 90: the Counsel skill's sections and word counts; the chain sentence (L28-31) and the run-time level test (L73) exist, nothing for questions while drafting; L54 "present the full text again" and L56 (closeout list of inferred lines) conflict with ratification on framings; value-documents L53 defines inferred as "nobody objected" and agent-proposed as "it was accepted", L64 gives an inferred line its support only when "ratified with the brief"; no rule file carries Counsel conduct; no validator limits SKILL.md length; ADR-D-0046 (the chain governs the discussion) and ADR-D-0054 (nobody but the owner makes a gives-statement into a means) bear on the framing test; "inferred" also names the audit's grade on run items (`completion-closeout.md:65`), a different thing. Issue 86: no plugin text speaks of investigate-first tasks or unknowns; the gate (`SKILL.md:57-60`, `lifecycle-gates.md:40-46`), the template's Assumptions line (`unverified, checked by Task_N`) and Open Questions, plan-format rule 10, the plan-review snippet (`prompt-snippets.md:62-79`, no concreteness check) and the three Researcher snippets are the places; the adapters restate the gate (`agents/Orchestrator.md:33-35`, `claude/agents/harness-orchestrator.md:28`); `validate_plan.py` checks `type` is present, not its value; the version is in three manifests (equality is the only check) and the two marketplace plugin entries carry a stale `0.2.0`; fixtures under `tests/` are validator inputs only, and the fresh-repository run showed scenarios with an invented repository in a temporary directory and a fresh agent told it is the Orchestrator.
- Existing code norms: none touched.
- The audits of this run: this plan's draft and its close.

## Open Questions (max 3)
- None.

## Assumptions
- A1: "1.0" is written `1.0.0`, the three-part form every earlier bump used, in the three manifests and in the two marketplace plugin entries, which state the plugin's version to an installer. source: the brief's Version section; `validate_harness_package.py:82-88`; commit f7fcc30.
- A2: the closeout list of inferred lines in the Counsel skill (L56) is the issue's lever that the brief's means replaces; the audit's closeout list of marked items (ADR-D-0042, `completion-closeout.md:56`) is a different mechanism and is not touched. source: the brief's means in the issue 90 section; ADR-D-0042.
- A3: the framing test is a filter on what reaches the owner, which ADR-D-0046 (the chain is how the discussion is held) did not decide; whether that needs a record is the admission test's outcome, run in Task_1. source: ADR-D-0046 L26; `durable-docs-authoring/references/adr.md`.

## Tasks

### Task_1: Counsel's questions while drafting
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/counsel/**
  - plugins/coding-agent-orchestration-harness/skills/value-documents/SKILL.md
  - docs/coding-agent-orchestration-harness/decisions/**
- depends_on: []
- description: |
  The four rules of the brief's issue 90 section, each tightened into the Counsel skill at the place where it acts (the framing test and the conflict rule beside the chain sentence in "How a conversation goes"; ratification on framings and the unassisted default in "Drafting and ratification"), with L54 and L56 reworded to agree and the tags kept in the brief for the audit. The value-documents definitions of inferred, agent-proposed and what ratification covers made to agree (a line Counsel decided and the owner ratified on its framing has its support; a line not shown as a framing because it changed nothing is tagged and has the support the skill gives an inferred line). Run the admission test of `durable-docs-authoring/references/adr.md` on the new decision (the framing as a filter on what reaches the owner while drafting). If it passes, read ADR-D-0046's decision and boundary words: where none is broken, propose a separate record (lowest free number, depending on ADR-D-0046); where one is, revise ADR-D-0046 in place if it is not on `main` (check with `git merge-base --is-ancestor`) or propose a replacement. If it fails, no record. Name any record so it returns to the owner by name. Write only what the brief and this plan state; no rule file is touched.
- acceptance:
  - Each gives-statement and the constraint of the brief's issue 90 section can be pointed to in exactly one sentence group of the Counsel skill; the means is met: the framings are what the owner sees at ratification, the tags stay in the brief.
  - No sentence of the Counsel skill or the value-documents skill contradicts ratification on framings; the run-time test in "Contacts with a run" is unchanged.
  - The admission test's result is reported with the ADR-D-0046 words checked; a revised or proposed record, if any, meets adr.md's form and is named in the report.
  - `docs/coding-agent/rules/*.md` unchanged.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py; python scripts/run_validation_smoke_tests.py; git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review against the brief's issue 90 section: each rule once at its place; no contradiction left; the record, if any, against adr.md"

### Task_2: Research before an execution plan
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/lifecycle-gates.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/dispatch-guidance.md
  - plugins/coding-agent-orchestration-harness/skills/plan-format/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/plan-format/references/plan-template.md
  - plugins/coding-agent-orchestration-harness/skills/subagent-strategy/references/prompt-snippets.md
  - plugins/coding-agent-orchestration-harness/agents/Orchestrator.md
  - plugins/coding-agent-orchestration-harness/claude/agents/harness-orchestrator.md
- depends_on: []
- description: |
  The brief's issue 86 section tightened into the existing text: the Research Dispatch Gate says what the research before a plan is for and when it is enough; Research Dispatch Details carries the unknown's form (what, why, what decision or evidence is needed; dependent work conditional or awaiting replanning) and the three statements of a research task that is a deliverable; the plan template's Assumptions line carries the unknown's form; plan-format's rules say a task is written from the research's findings, altitude kept (rule 10); the plan-review snippet gains the one check (an investigation-first task that merely postpones the research the rest needs is a finding; a research task is not when the brief's legitimacy condition holds and it states its question, evidence and effect); the adapters restate the gate only where they already do. The fixed audit dispatch template is untouched.
- acceptance:
  - Each gives-statement and the constraint of the brief's issue 86 section can be pointed to in exactly one place, the others pointing; the means is met: the gate is the place built on.
  - The plan-review snippet's check flags the postponing task and not the legitimate research task, by its wording; the exemption rests on the brief's legitimacy condition, not on the three statements alone.
  - The Orchestrator adapters agree with the skill text; `validate_plan.py` passes on the existing fixtures unchanged.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py; python scripts/run_validation_smoke_tests.py; python skills/plan-format/scripts/validate_plan.py --file ../../tests/coding-agent-orchestration-harness/fixtures/valid-plan.md --mode balanced; git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review against the brief's issue 86 section: once at its place; adapter parity; no restatement of how"

### Task_3: Scenarios 3 and 4 on a fixture
- type: test
- owns:
  - <the Orchestrator's scratchpad directory, outside the repository>/fx/**
- depends_on: [Task_2]
- description: |
  Build, in the scratchpad `fx/` directory and naming no real project, an invented git repository with a small piece of code holding one non-obvious coupling a plan would need to discover and one existing validation command, with a one-line request (scenario 3); two invented draft plans for it in plan-format: one whose Task_1 is a generic "investigate X" task on which vague later tasks depend (scenario 4), and a control plan whose Task_1 is a genuinely necessary bounded check (its answer cannot be read from the repository, for example a measurement only a run gives) stating its question, expected evidence and effect on later work. Report the paths and the request. The Orchestrator then dispatches: a fresh agent told it is the Orchestrator session of that repository, pointed at the plugin as changed by Task_2, asked to draft the plan and commit nothing (scenario 3); and the Reviewer with the plan-review snippet on each draft plan (scenario 4 and the control). Nothing of the fixture is committed to this repository.
- acceptance:
  - The fixture exists as described, with the coupling and the validation command noted in the report so the drafted plan can be checked against them.
  - The two draft plans pass `validate_plan.py --mode balanced`, so the review turns on the check and not on form.
  - Scenario 3's session record shows the investigation (Researcher dispatch or recorded reads) and its findings before its first plan draft; the drafted plan has no investigate-first task for what it needed to know, and its tasks name the coupling and the validation command; scenario 4's review names the postponement; the control plan's review does not flag its research task. Each outcome is recorded in the Progress Log with the dispatch texts; where an outcome fails, the closeout says so plainly.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "python plugins/coding-agent-orchestration-harness/skills/plan-format/scripts/validate_plan.py --file <each draft plan> --mode balanced"
  - kind: manual
    required: true
    owner: orchestrator
    detail: "The three dispatches made and their outcomes read against the acceptance bullets; recorded in the Progress Log"

### Task_4: Version 1.0
- type: chore
- owns:
  - plugins/coding-agent-orchestration-harness/.claude-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.codex-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.github/plugin/plugin.json
  - .claude-plugin/marketplace.json
  - .github/plugin/marketplace.json
- depends_on: [Task_1, Task_2, Task_3, Task_5]
- description: |
  The plugin's version becomes `1.0.0` (A1) in the three manifests and the two marketplace plugin entries; nothing else changes. This is the last change before the run is reported ready.
- acceptance:
  - The three manifests and the two marketplace plugin entries read `1.0.0`; no other file changes.
  - `validate_harness_package.py` passes.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py; python scripts/run_validation_smoke_tests.py; git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "Final review of the branch's whole delta since 25f9831"

### Task_5: Counsel's questions at any time
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/counsel/SKILL.md
  - docs/coding-agent-orchestration-harness/decisions/**
- depends_on: [Task_1]
- description: |
  The brief's amendment of 2026-10-15 (issue 90 section, second statement): the framing test applies any time Counsel puts a question to the owner, not only while a brief is drafted; the acts the owner reserved still reach the owner regardless. The sentence group Task_1 placed beside the chain sentence is reworded so the test governs every question to the owner, with what happens to a choice that is Counsel's while a brief is drafted (decided, written into the brief, tagged) kept there; "Contacts with a run" names the same test for a question brought to the owner during a run, in one clause pointing to that sentence group, with the level test and the reserved acts unchanged. ADR-D-0059 is revised in place (proposed, not on `main`): title, decision, boundary and filename widened from "while a brief is drafted" to any time, the reserved acts named as not covered, the source of intent pointing at the amendment; ADR-D-0060's `depends_on` carries the new filename. Nothing else is touched; no rule file.
- acceptance:
  - The amended statement can be pointed to in exactly one sentence group of the Counsel skill; "Contacts with a run" points to it without restating it; the level test and the reserved acts in that section are unchanged in substance.
  - ADR-D-0059 holds one decision, meets `durable-docs-authoring/references/adr.md`, and every link in ADR-D-0059 and ADR-D-0060 resolves; ADR-D-0059 stays `proposed` and is named in the report so it returns to the owner by name.
  - `docs/coding-agent/rules/*.md` unchanged.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py; python scripts/run_validation_smoke_tests.py; git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review against the brief's amended statement: the test once at its place, the run-time clause pointing to it; the revised record against adr.md"

## Task Waves (explicit parallel dispatch sets)
- Wave 1: Task_1, Task_2
- Wave 2: Task_3, Task_5
- Wave 3: Task_4

## E2E / Visual Validation Spec
- Not applicable: no UI.

## Rollback / Safety
- Text and manifest changes on a feature branch stacked on pull request 85; revert by reverting the branch's commits. The fixture lives outside the repository.

## Progress Log
- 2026-10-15 Plan drafted from the two Researchers' reports; this plan starts from revision 25f9831 (the brief committed first). Codex peers pinged: the reviewer answered available.
- 2026-10-15 Plan review (Codex reviewer, at b6aff90): FINDINGS, 1 MAJOR and 2 MINOR, all taken as fix. F1: scenario 3 must show research before the first draft, not be judged from the finished plan (DoD 8 and Task_3 acceptance). F2: the record is not predetermined; the admission test runs on the new decision and ADR-D-0046 changes only where its own words are broken (Scope, Task_1). F3: the three statements of a research task exempt nothing by themselves; the brief's legitimacy condition is the test (DoD 7, Planner-added 1, Task_2 and Task_3). Re-review requested.
- 2026-10-15 Plan re-review (Codex reviewer, at d4b06bf): APPROVED, no finding open.
- 2026-10-15 Plan-draft audit, dispatch text (to a fresh Auditor dispatch on Fable):

  ```text
  You are the value auditor. Read references/value-audit-mandate.md of the orchestration-harness skill and follow it exactly. Position: plan draft. Plan: docs/coding-agent/plans/active/counsel-questions-and-planning-research-plan.md. Governing brief: docs/coding-agent/briefs/active/counsel-questions-and-planning-research-brief.md. Changes since: none.
  ```

- 2026-10-15 Plan-draft audit, verdict as returned (machine paths redacted; the two comparison lines are logged in the readings file, not here):

  - Position: plan draft
  - Documents read: [machine path redacted] (instructions); [machine path redacted] (instructions); [machine path redacted]\docs\coding-agent\briefs\active\counsel-questions-and-planning-research-brief.md; [machine path redacted]\docs\coding-agent\plans\active\counsel-questions-and-planning-research-plan.md; [machine path redacted]\docs\coding-agent\rules\common.md (Repository Reference Documents pointer lines; Standing Approvals, unmodified in the working tree so equal to HEAD). For understanding only, never as support: file names of ADR-D-0042/0046/0054, the `version` lines of the three manifests and two marketplace files, Counsel SKILL.md L54/L56, orchestration-harness SKILL.md L57-60. Readings file opened after grades were fixed. No notes file opened.
  - Product basis: brief in the product owner's words (brief: "the product owner's own words in the two issues and in this ratified brief. ebigunso owns the harness; no product philosophy and no engineering philosophy exist")
  - Not audited: engineering side, no engineering philosophy (pointer line reads "none yet"); product philosophy also none yet, so the product side runs on the brief alone
  - Missing inputs: none (brief under `active/`, carries ratification "ratified by ebigunso on 2026-10-14 ('I ratify the brief, hand it over now.')" and the product basis)
  - Value documents changed in range: none (no range at plan draft; the working tree shows `docs/coding-agent/briefs/active/first-use-in-a-fresh-repository-brief.md` modified, a different brief, outside any range and not read)

  Items (item | mapping | grade | support | ask-now text / direction):

  - DoD 1 (framing test and conflict rule in the Counsel skill) | maps to the brief | cited | brief, issue 90 gives: "Before a question reaches the owner while a brief is being drawn out, Counsel writes it as an experience change ... The framing is itself the test"; "A conflict between statements Counsel itself drafted is Counsel's to resolve the same way when the discussion made the intent plain." | -
  - DoD 2 (ratification on framings; L54 and L56 reworded to agree; tags stay in the brief) | maps to the brief | cited | brief gives: "At ratification the owner is shown the experience framings for the decisions in the brief that changed anything, not the brief itself. The brief stays the record on disk for the run and the audit"; means: "The issue's own lever, a list of tagged decisions at ratification and at closeout, is replaced by the framings above as what the owner sees; the tags stay in the brief for the audit." The plan follows the means, no departure. | -
  - DoD 3 (unassisted path as default, backup told once) | maps to the brief | cited | brief gives: "the brief states the unassisted path as the default and the assisted path as the backup. Counsel does not ask which; at most it tells the owner once that the backup may be needed." | -
  - DoD 4 (no rule file carries the rules; value-documents tag and ratification definitions agree with ratification on framings) | maps to the brief (first half); the value-documents edit extends it | inferred | the rule-file half is covered: constraint "These rules live in the Counsel skill ... and not in a repository's rules." No brief statement names the value-documents skill; the edit extends the gives "decided, written into the brief, and tagged inferred or agent-proposed" and the means "the tags stay in the brief for the audit", and is text on a branch, cheap to undo. The brief already has the owner ratifying the brief on the framings, so the widened definition does not loosen who decides. | -
  - DoD 5 (Research Dispatch Gate says what the research is for and when it is enough) | maps to the brief | cited | brief, issue 86 gives: "Before an execution plan is drafted, the investigation needed to decide what the plan should contain is done ... Depth stays proportional to the change"; means: "the existing Research Dispatch Gate is the place it builds on." | -
  - DoD 6 (the unknown's form in template and planning rules; the research task's three statements) | maps to the brief | cited | brief gives: "the plan states what remains unknown, why, and what decision or evidence is needed; dependent work is conditional or awaits replanning"; constraint: "such a task states the question it answers, the expected evidence, and how its outcome affects later work"; means: "The planning guidance, the plan template and the plan-review expectations are aligned around this". | -
  - DoD 7 (plan-review snippet flags the postponing task, exempts only on the legitimacy condition) | maps to the brief | cited | brief gives: "Plan review flags an investigation-first plan when that task merely postpones research needed to make the rest of the plan concrete"; constraint: "Research remains a legitimate deliverable when the request is itself an investigation, or when a bounded experiment or implementation-stage check is genuinely necessary". | -
  - DoD 8 (scenarios 3 and 4 shown on a fixture in a temporary directory, outcome in the Progress Log) | maps to the brief | cited | brief, pass conditions: "scenarios 3 and 4 are shown on a fixture where one can be made, and where one cannot the closeout says so plainly." | -
  - DoD 9 (version 1.0 in every file stating the plugin's version, last change before reported ready) | maps to the brief | cited | brief, Version gives: "the bump is made in this work, as the last change before the stack is reported ready." Not outward-facing: a manifest edit on a branch reaches installers only when shipped. | -
  - DoD 10 (validators; Reviewer APPROVED; plan closes; branch published, pull request opened, note to Counsel, nothing merged) | maps to the brief ("Two small fixes ... ship with the current stack") | cited | publish and open pull request are outward-facing; passed on the standing approval, `common.md` Standing Approvals: "A finished, reviewed run may publish its branch and open pull requests in this repository without asking first. Merges are not covered and wait for the owner ... Given and accepted by the repository's owner, ebigunso, on 2026-09-30, relayed by Counsel: 'The common rule proposed, accepted.'" The entry carries its acceptance record and is committed; whether the words were said is not something the file can show. "Nothing merged" keeps the entry's limit. The note to Counsel is the run's channel to the person directing the work (common.md names it), not a reach outside the repository. | -
  - Planner-added 1 (control plan with a legitimate research task the review must not flag) | maps to the brief | cited | brief constraint: "Research remains a legitimate deliverable when ... such a task states the question it answers, the expected evidence, and how its outcome affects later work." An added check of a constraint tightens, it does not loosen. | -
  - Non-goal: issues 87, 88, 89 | maps to the brief | cited | brief constraint: "Nothing of the bigger issues (89, 87, 88) is taken on here." | -
  - Non-goal: the both-ways line | maps to the brief | cited | brief, Limits: "A matter that differs from what the owner believes was agreed is not made a standing reason to ask him during a run." | -
  - Non-goal: any repository rule file | maps to the brief | cited | brief constraint: "These rules live in the Counsel skill ... and not in a repository's rules." | -
  - Non-goal: the fixed audit dispatch template | maps to the brief (scope held) | inferred | no statement names it; extends the issue 86 means ("the existing Research Dispatch Gate is the place it builds on") by leaving a neighbouring text untouched; cheap to undo | -
  - Non-goal: validators for prose (ADR-I-0007) | maps to the brief (scope held) | inferred | extends the agent-checkable pass condition "the package validators pass" by adding no validator; cheap to undo | -
  - Non-goal: the run-time test of what reaches the owner from a run stays as it is | maps to the brief (scope held) | inferred | extends the issue 90 gives, whose scope is "while a brief is being drawn out", and the Limits constraint declining a standing reason to ask during a run; cheap to undo | -
  - Non-goal: the audit's closeout list of marked items (ADR-D-0042) untouched | maps to the brief (scope held) | inferred | extends the means "a list of tagged decisions at ratification and at closeout, is replaced by the framings" by reading the closeout list as Counsel's inferred-lines list, not the auditor's marked-items list; cheap to undo | -
  - A1 ("1.0" written `1.0.0` in the three manifests and the two marketplace plugin entries) | maps to the brief | inferred | extends the Version gives ("The plugin's version becomes 1.0"); the three-part form is what the files already use (0.31.0); the marketplace entries state the plugin's version (currently 0.2.0); cheap to undo | -
  - A2 (the Counsel skill's closeout list of inferred lines is the lever the means replaces; the audit's marked-items list is a different mechanism) | maps to the brief | inferred | extends the means quoted under DoD 2; the brief does not name which closeout list; cheap to undo | -
  - A3 (framing test as a filter ADR-D-0046 did not decide; admission test run in Task_1; a record, if any, returns to the owner by name) | internal mechanics (a maintainer decision record under `docs/`, nothing a plugin user observes) | not audited | engineering side has no document; the step 1 test passes: proposing or revising a record on a branch is cheap to undo, and acceptance of a decision record keeps its own rule, which the task honours ("Name any record so it returns to the owner by name") | -
  - Task_1 (issue 90 rules into the Counsel skill; value-documents made to agree; admission test; no rule file) | maps to the brief | cited | the four gives and the constraint quoted under DoD 1-4; the value-documents and record portions carry DoD 4 and A3's values | -
  - Task_2 (issue 86 into the gate, lifecycle-gates, template, plan-format, snippet, adapters where they already restate the gate) | maps to the brief | cited | the three gives, the constraint and the means quoted under DoD 5-7 | -
  - Task_3 (fixture outside the repository; fresh Orchestrator session draft; Reviewer on the two draft plans) | maps to the brief | cited | pass condition quoted under DoD 8; scenarios 3 and 4 as the brief words them. Nothing committed, nothing leaves the repository. | -
  - Task_4 (version `1.0.0` in five files, last change) | maps to the brief | cited | Version gives quoted under DoD 9; form from A1 | -
  - Decision Log 2026-10-15 (relays admitted; hand-over acted on as Counsel's relay quoting the owner's ratification of 2026-10-14) | internal mechanics of the run's channel; it reads who decides, so graded | cited | `common.md` Standing Approvals: "a relay from the agmsg identity `agent-harness-counsel` that quotes the person directing the work carries that person's decisions to an Orchestrator session ... plan approval and its waiver are not carried ... Given and accepted by the repository's owner, ebigunso ... on 2026-10-01, relayed by Counsel: 'I accept ADR-D-0038 and the standing approval entry.'" Record present and committed; the file cannot show the words were said. The brief's own ratification record agrees with the relayed words. | -

  - Human-only conditions pending: "scenarios 1 and 2 in his next Counsel discussion; whether plans in his next real run were concrete on first draft"
  - Scenarios: none
  Summary for the Orchestrator: no `ask-now`. Every item is cited, inferred or (one, engineering-side) not audited; the two outward-facing steps rest on the committed Standing Approvals entries. Plan approval is decided at the Plan Gate, not by this verdict.

  How the Orchestrator applied it: no item is `ask-now`, none is `ungraded`, and no item is marked `direction`. Inferred calls, as the verdict states them: DoD 4 (the value-documents definitions made to agree), the four scope-held non-goals (the fixed dispatch template; validators for prose; the run-time test; the ADR-D-0042 list), A1 and A2; A3 is not audited, the engineering side having no document. The plan review closed with no finding open and this verdict holds nothing, so the plan is authorized under the ratified brief and Wave 1 is dispatched. The auditor read the mandate from the installed plugin (0.31.0) rather than the repository copy on this branch; the two carry the same mandate text, and the Orchestrator rules that the verdict counts. The comparison set readings apart from grades in class or basis only (DoD 4, DoD 10, Planner-added 1, A2, A3), corrected in the readings file with nothing to redo.
- 2026-10-15 Plan authorized under the ratified brief (plan review APPROVED; plan-draft audit holds nothing). Wave 1 dispatched: Task_1 and Task_2 to Claude Workers in parallel.
- 2026-10-15 Wave 1 integrated. Task_1 (Claude Worker, Opus) done at 1f65e8b: the framing test and the conflict rule beside the chain sentence (counsel SKILL.md L29), the unassisted default (L51), ratification on framings (L56), L57 and L59 reworded to agree; value-documents L53 and new L65 agree; admission test passed with ADR-D-0046 unbroken (its decision and boundary fix the form of what is brought, not which questions), so ADR-D-0059 is proposed as a separate record depending on ADR-D-0046; ADR-D-0054 and ADR-D-0034 hold; Counsel SKILL.md 3559 to 3782 words. Task_2 (Claude Worker, Opus) done at f3a5332: the gate at orchestration-harness SKILL.md L59 says what the research is for and when it is enough; the unknown form at lifecycle-gates.md step 4 and the legitimate research task at step 5; the template Assumptions line carries the form; rule 10 and dispatch-guidance.md point; the plan-review check at prompt-snippets.md L75; the adapters restate the gate in one line each. Validators pass for both. Judgement calls, ruled: the snippet repeats the legitimacy test briefly and points to its home (kept: the Reviewer applies it from the plan file); the adapters' one line each grew by about 120 characters (kept: one line each); ADR-D-0059 holds the filter and ratification on framings as one decision (kept, the review to judge); the gloss "the plan shows its answer cannot be had before drafting" is the Worker reading of "genuinely necessary" (kept, the review to judge whether it narrows the constraint); counsel SKILL.md L54 (drops and departures listed before ratification) left as compatible. Lesson candidate noted: an ADR filename over about 135 characters breaks the smoke test on Windows path length; the Worker shortened the name. Wave review dispatched to the Codex reviewer.
- 2026-10-15 Wave 1 review (Codex reviewer, range 5d6f3a2..f3a5332): FINDINGS, 1 MAJOR and 2 MINOR, all taken as fix. W1-F1: the plan-review check added "because the plan shows its answer cannot be had before drafting", a condition the brief does not state; the clause removed by the Orchestrator (5f36a93). W1-F2: ADR-D-0059 bundled two decisions; a follow-up Worker split it: ADR-D-0059 holds the drafting-question test and the conflict rule, ADR-D-0060 ratification on framings, each admitted on its own. W1-F3: the proposals logged in the Decision Log below. Worker question, ruled: ADR-D-0054 has a statement's kind ratified with the statement, while ADR-D-0060 has the owner ratify on framings; the brief itself settles it (the brief stays the record, its tags stay in it, and ratification covers the whole brief as the value-documents text now states), so the kinds are ratified with the brief as ratified on its framings; an Orchestrator ruling, cheap to undo, no question sent. Delta re-review requested.
- 2026-10-15 Wave 1 delta re-review (Codex reviewer, range f3a5332..7aa690b): APPROVED, no finding open. Task_1 and Task_2 done. ADR-D-0059 and ADR-D-0060 go to the owner through Counsel for acceptance, each by its own name (the texts before him: the files at 952f044). Wave 2 dispatched: Task_3 fixture build to a Claude Worker.

- 2026-10-15 Counsel's relay of 02:34Z, quoting the owner: ADR-D-0060 accepted ("I accept ADR-D-0060."; status set to accepted, text as at 952f044); ADR-D-0059 not accepted, to be extended (words in the Decision Log). The brief on disk amended by Counsel under the issue 90 section with those words; committed as left on disk (e5e0bc8). Replan: Task_5 added (Wave 2, beside Task_3; Task_4 waits on it); plan review of the revision dispatched to the Codex reviewer, the plan-draft audit of the revised plan to follow before Task_5 is dispatched.
- 2026-10-15 Wave 2, Task_3 (fixture build, Claude Worker, Opus) done: `fx/planrepo` (invented package `tallybook`, one commit), coupling `tallybook/store.py:14` writes `date|cents|memo` and `tallybook/monthly.py:13` unpacks exactly three fields (nothing names the shared format; `export_csv` splits at most twice), validation command `sh scripts/precommit.sh` (doctests plus a round trip; not named in the README), request `fx/request.txt` ("Add a currency field to the tallybook entries, so each entry records which currency its amount is in (default EUR)."), `fx/plans/postponing-plan.md` and `fx/plans/control-plan.md` both passing `validate_plan.py --mode balanced`, answer key `fx/README-fixture.md`. Nothing committed to this repository. The first control plan's Task_1 (a timing measurement) was flagged by its review on necessity, not postponement, so it did not show the constraint either way; the Orchestrator rewrote the control plan so Task_1 is an implementation-stage check whose answer cannot be read from the repository (whether an outside `tallysum` tool named in the request reads a four-field line; the chosen design or the Design alternative depends on it; stance ask-user), with the request extended for it in `fx/request-control.txt` ("... Note: the file is also read nightly by our tallysum tool on the shared box; it is not in this repository."). The three dispatches and their outcomes, judged against Task_3's acceptance (machine paths replaced by `<scratchpad>` and `<repository>`):

  Scenario 4, dispatch text (fresh Reviewer, Claude, Opus):

  ```text
  Reviewer snippet (plan review).

  Scope:
  - Review the draft plan at `<scratchpad>\fx\plans\postponing-plan.md` before it is approved or authorized. The artifact is the plan file, not a diff. The repository it plans for is `<scratchpad>\fx\planrepo` (read it as needed; read nothing else under `fx/` except the plan named above). It has no rule suite and no lessons file.
  - Inputs: the plan; the request as given, verbatim: "Add a currency field to the tallybook entries, so each entry records which currency its amount is in (default EUR)."; Researcher output: none; the plugin root: `<repository>\plugins\coding-agent-orchestration-harness`.

  Procedure:
  - Run `python <plugin root>/skills/plan-format/scripts/validate_plan.py --file <plan> --mode balanced` first. Its pass output is the required validation evidence; do not re-check by hand what it checks.
  - Read `<plugin root>/skills/plan-format/SKILL.md`; apply `<plugin root>/skills/engineering-quality-baselines/SKILL.md` per its plan-review routing entry.
  - Then apply every bullet of the "Reviewer snippet (plan review)" in `<plugin root>/skills/subagent-strategy/references/prompt-snippets.md` exactly as written there (open that file and follow its Procedure and Deliverables bullets; they are the authority for this review, including every check it names on tasks).
  - This repository has no engineering philosophy and no rules, so nothing overrides the snippet.

  Deliverables:
  - Each finding names the fact, record, or reference it contradicts.
  - Your verdict is advisory to the Orchestrator. Question the decomposition given; do not rewrite the plan.
  - Do not edit any file.
  ```

  Scenario 4, outcome: NEEDS_REVISION with a CRITICAL finding that Task_1 only postpones research the rest of the plan needs, naming Tasks 2 to 4's scope, acceptance and validation deferred to its outcome ("as Task_1 found"), citing the prompt-snippets check, plan-format rule 10 and lifecycle-gates Research Dispatch Details items 3 to 5. Shown.

  Control, dispatch text (fresh Reviewer, Claude, Opus; the request in `fx/request-control.txt`):

  ```text
  Plan review, using the Reviewer snippet (plan review) in `<repository>\plugins\coding-agent-orchestration-harness\skills\subagent-strategy\references\prompt-snippets.md` (section "Reviewer snippet (plan review)"); follow that snippet's Scope, Procedure and Deliverables exactly.

  Scope:
  - Review the draft plan at `<scratchpad>\fx\plans\control-plan.md` before it is approved. The artifact is the plan file, not a diff.
  - The request as given, verbatim, is in `<scratchpad>\fx\request-control.txt` (original text, not a paraphrase).
  - Researcher output: none.
  - The repository the plan is for: `<scratchpad>\fx\planrepo` (a small Python package; it has no rule suite and no lessons file).
  - Plugin root: `<repository>\plugins\coding-agent-orchestration-harness`. Read the skills from this path (the repository copy), not from an installed plugin cache.

  Constraints:
  - Read-only. Do not edit any file. Do not read anything under `fx/` other than the plan, the request file and `planrepo`.
  - Do not read `fx/README-fixture.md`.

  Deliverables:
  - Status (APPROVED or NEEDS_REVISION), then each finding with its severity, the plan line, and the fact, record or reference it contradicts, per the snippet. State explicitly, as its own line, whether Task_1 is a finding under the snippet's investigation-task check, and why.
  ```

  Control, outcome: NEEDS_REVISION on other grounds (1 MAJOR: the planner-added CSV column's reason and a second format surface outside the stance; 6 MINOR, on rule 12 listings and wording), with the investigation-task check answered explicitly: "Task_1 is not a finding", because the request names the outside reader as not in the repository so no reading before drafting could settle it, A1 states the unknown in the form of Research Dispatch Details item 4, Task_1 is a bounded experiment (item 5) and the plan already fixes Task_2's owns, acceptance and validation whatever the result; "Those three statements are not what exempts it". The answer key allows other findings. Shown.

  Scenario 3: three earlier dispatches of a fresh agent worded as "You are the Orchestrator session of the repository at ..." ended in API-side request failures before any work (two on Opus, one on Sonnet, 2026-10-15 ~02:40Z to 03:00Z); the dispatch was reworded as a plain task with the same inputs and policy. Dispatch text (fresh general-purpose agent, Claude, Opus):

  ```text
  Task: draft an execution plan for a small request in a sample repository, following the orchestration-harness plugin's planning policy. Commit nothing.

  Inputs:
  - Repository: `<scratchpad>\fx\planrepo` (a git repository; a small Python package).
  - Request (verbatim, in the file): `<scratchpad>\fx\request.txt`.
  - Policy: the plugin at `<repository>\plugins\coding-agent-orchestration-harness`. Start by reading `skills/orchestration-harness/SKILL.md` there, then follow what it routes you to for the Plan Gate and the Research Dispatch Gate (`skills/orchestration-harness/references/lifecycle-gates.md`, `skills/plan-format/SKILL.md`, `skills/plan-format/references/plan-template.md`). Read those from this path, not from an installed plugin cache. Treat the request as non-trivial work in plan mode.

  Procedure:
  - Do whatever the policy says must happen before a plan is drafted. You may read the repository's files yourself instead of dispatching a researcher; if you do, that counts as the research when it is recorded (see Report).
  - Write the plan to `docs/coding-agent/plans/active/currency-field-plan.md` inside the sample repository, in the plan-format template. Then run `python <repository>\plugins\coding-agent-orchestration-harness\skills\plan-format\scripts\validate_plan.py --file <that plan> --mode balanced` and fix the plan until it passes.
  - Stop after the plan is drafted and validated: do not dispatch workers, do not implement, do not run git commit, and do not present the plan for approval to anyone. Make no change outside the sample repository.
  - Do not read `fx/README-fixture.md`, `fx/plans/`, or anything under `fx/` other than `planrepo` and `request.txt`.

  Report, in this order:
  1. The sequence of what you did before the first line of the plan was written: each file read or command run, in order, with the finding each gave that the plan rests on (one line each).
  2. The plan's path and the validator's output.
  3. Any question or unknown the plan records, quoted.
  ```

  Scenario 3, outcome: the report lists thirteen reads before the first plan line, each with its finding (the SKILL.md gates; the request; lifecycle-gates' unknown form; the tree; no rule suite; the README's store and timing statement; `precommit.sh`'s positional call; `store.py`'s format and `split("|", 2)`; `monthly.py`'s three-field unpack; plan-format rules; the template; the locatable-consumer definition). The drafted plan (`fx/planrepo/docs/coding-agent/plans/active/currency-field-plan.md`, validator passed first run, uncommitted) has no investigate-first task: Task_1 store and export, Task_2 monthly totals owning `tallybook/monthly.py`, Task_3 the integrated check with `sh scripts/precommit.sh` in validation; `Research waived` names the five files read; three open questions on output shapes with a stance of ask-user, dependent work conditional. Shown. Task_3's acceptance met on all three; the fixture stays outside the repository.
- 2026-10-15 Plan revision review (Codex reviewer, at 82908a0): FINDINGS, 1 MINOR, taken as fix. R-F1: Task_5's acceptance set a filename length cap the brief, rules and lessons did not state, an undeclared planner-added requirement; the cap removed, the smoke test (which copies the tree) being the required check that catches a path too long. The investigation-task check on Task_5 answered not applicable. Delta re-review requested.

## Decision Log
- 2026-10-15 Relays admitted by the Standing Approvals entry of 2026-10-01 in `common.md`; the hand-over acted on as Counsel's relay of 2026-10-15 quoting the owner's ratification of 2026-10-14.
- 2026-10-15 Proposal, ADR-D-0059 (proposed, awaiting the owner's acceptance by name): "While a brief is drafted, a choice reaches the person directing the work only when its options, written as experience changes, read differently; a choice whose framings read the same is Counsel's to decide". Decision: Counsel frames each drafting choice as an experience change and the framing is the test; same-reading options are Counsel's to decide, write into the brief and tag; differing ones go to the person directing the work in that form; a conflict between Counsel-drafted statements is resolved the same way. Constraint on future work: nothing may have Counsel ask about a choice whose framings read the same, or judge which questions are the owner's before framing them. Why: a person who would see at once from the experience that a choice does not affect them should not be asked it.
- 2026-10-15 Proposal, ADR-D-0060 (proposed, awaiting the owner's acceptance by name): "A brief is ratified on the experience framings of the decisions in it that changed anything, not on its text, and the brief stays the record". Decision: at ratification the person directing the work is shown the framings of the decisions that changed anything, not the brief; the brief and its tags stay the record for the run and the audit. Constraint on future work: nothing may make ratification depend on reading the brief, or on a list of its tagged decisions. Why: reading a long brief to ratify it is the same burden as reading a plan.

- 2026-10-15 Owner's answer on ADR-D-0059, relayed by Counsel 2026-10-15, quoted: "For 0059, I'd like it to be extended to be any time rather than only brief writing time." Read as a change to the design (Replan Procedure step 1): the brief now states the framing test for any question Counsel puts to the owner, which Task_1 built for drafting time only. Impact: the Counsel skill's test sentence and its run-time contacts section, ADR-D-0059's title, decision, boundary and filename, ADR-D-0060's dependency line; value-documents unchanged. Plan delta: Task_5 (docs) added, Wave 2 becomes Task_3 and Task_5, Task_4 depends on Task_5; DoD 1, Scope and the run-time non-goal reworded. Not contract-shape, irreversible or outward-facing (text on a branch); no pause. ADR-D-0059 revised returns to the owner by name.
- 2026-10-15 ADR-D-0060 accepted by the owner, relayed by Counsel 2026-10-15, quoted: "I accept ADR-D-0060." The ruling on statement kinds under ADR-D-0060 was told to him, not asked, by the framing test.

## Notes (Risks / Edge cases)
- The Counsel skill is 3559 words; the four rules add sentences, not sections. If the Reviewer reports the skill unacceptably long, the remedy is tightening elsewhere in the same sections, not a reference file (Design).
