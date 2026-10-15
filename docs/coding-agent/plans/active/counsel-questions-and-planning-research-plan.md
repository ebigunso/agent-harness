# Plan: Counsel's questions while drafting, and research before a plan

- status: draft
- generated: 2026-10-15
- last_updated: 2026-10-15
- work_type: docs

## Goal
- The harness gives what the governing brief `docs/coding-agent/briefs/active/counsel-questions-and-planning-research-brief.md` states: Counsel's questions while drafting a brief pass the experience-framing test before reaching the owner, who ratifies on framings and sees the unassisted path as the default; an execution plan is drafted only after the research that makes it concrete, with unknowns stated and plan review flagging an investigation-first plan; the plugin's version becomes 1.0 as the last change before the stack is reported ready.
- The brief is the requirement and is not restated here; where this plan and the brief differ, the brief governs and the difference is a plan defect.
- This is the first plan of the run recorded in `docs/coding-agent/plans/active/counsel-questions-and-planning-research-run.md`.

## Definition of Done
- The Counsel skill states, where the conversation is held, that before a question reaches the owner while a brief is being drawn out Counsel writes it as an experience change (who, what they do, what they then experience, the options side by side); options that read the same at that level are Counsel's to decide, written into the brief tagged inferred or agent-proposed; options that read differently go to the owner in that form; the framing is the test. A conflict between statements Counsel itself drafted is resolved the same way when the discussion made the intent plain.
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
- Scope: `skills/counsel/SKILL.md`; `skills/value-documents/SKILL.md` (tag definitions and what ratification covers); a decision record where the admission test passes on the framing test as a filter on what reaches the owner (whether ADR-D-0046 changes is decided by whether its own decision or boundary words are broken, not assumed); `skills/orchestration-harness/SKILL.md` (Research Dispatch Gate); `skills/orchestration-harness/references/lifecycle-gates.md` (Research Dispatch Details); `skills/orchestration-harness/references/dispatch-guidance.md` (Researcher dispatch); `skills/plan-format/SKILL.md` and `references/plan-template.md`; `skills/subagent-strategy/references/prompt-snippets.md` (plan-review snippet; the Researcher snippets); the Orchestrator adapters where they restate the gate; the three plugin manifests and the two marketplace plugin entries for the version; a fixture in a temporary directory.
- Non-goals: issues 87, 88 and 89; the both-ways line on matters differing from what the owner believes was agreed; any repository rule file; the fixed audit dispatch template; validators for prose (ADR-I-0007); the run-time test of what reaches the owner from a run (Contacts with a run; `value-level-operation.md` Asking The Owner), which stays as it is; the audit's closeout list of marked items (ADR-D-0042), a different mechanism from the brief's inferred lines.

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
- depends_on: [Task_1, Task_2, Task_3]
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

## Task Waves (explicit parallel dispatch sets)
- Wave 1: Task_1, Task_2
- Wave 2: Task_3
- Wave 3: Task_4

## E2E / Visual Validation Spec
- Not applicable: no UI.

## Rollback / Safety
- Text and manifest changes on a feature branch stacked on pull request 85; revert by reverting the branch's commits. The fixture lives outside the repository.

## Progress Log
- 2026-10-15 Plan drafted from the two Researchers' reports; this plan starts from revision 25f9831 (the brief committed first). Codex peers pinged: the reviewer answered available.
- 2026-10-15 Plan review (Codex reviewer, at b6aff90): FINDINGS, 1 MAJOR and 2 MINOR, all taken as fix. F1: scenario 3 must show research before the first draft, not be judged from the finished plan (DoD 8 and Task_3 acceptance). F2: the record is not predetermined; the admission test runs on the new decision and ADR-D-0046 changes only where its own words are broken (Scope, Task_1). F3: the three statements of a research task exempt nothing by themselves; the brief's legitimacy condition is the test (DoD 7, Planner-added 1, Task_2 and Task_3). Re-review requested.

## Decision Log
- 2026-10-15 Relays admitted by the Standing Approvals entry of 2026-10-01 in `common.md`; the hand-over acted on as Counsel's relay of 2026-10-15 quoting the owner's ratification of 2026-10-14.

## Notes (Risks / Edge cases)
- The Counsel skill is 3559 words; the four rules add sentences, not sections. If the Reviewer reports the skill unacceptably long, the remedy is tightening elsewhere in the same sections, not a reference file (Design).
