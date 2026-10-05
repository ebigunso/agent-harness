# Plan: Setup names what is missing

- status: draft
- generated: 2026-10-05
- last_updated: 2026-10-05
- work_type: docs

## Goal
- The harness gives what the governing brief `docs/coding-agent/briefs/active/setup-names-what-is-missing-brief.md` states.
- The brief is the requirement and is not restated here; where this plan and the brief differ, the brief governs and the difference is a plan defect.
- This is the only plan of the run recorded in `docs/coding-agent/plans/active/setup-names-what-is-missing-run.md`.

## Definition of Done
- Every gives-statement and constraint of the brief is carried by the plugin text, each stated once in the file that owns that moment; its means are built from, and a departure from one is recorded as a finding.
- Scenarios 1 and 2 hold on a fixture repository: a fresh agent following the built setup text on each fixture produces the report and the common rule file the scenarios describe, and on the second fixture a later piece of work, planned by a fresh agent under the built text and graded by a fresh Auditor dispatch, is graded against the product philosophy the pointer names.
- No setup text drafts, templates or offers a form for a philosophy.
- A run in a repository whose philosophies are marked missing behaves exactly as a run does today in a repository without one: a line saying a philosophy is missing turns nothing on and nothing off (value-level operation is on under a governing brief as today, and off without one), and no run mentions what is missing.
- Any decision record this plan proposes is checked and accepted by the owner by name before text is built on it.
- Package validators and smoke tests pass; the branch has Reviewer `APPROVED`.
- The run closes as `completion-closeout.md` states: scenario by scenario, its branch published on the stack and a pull request opened under the standing approval, the note to Counsel sent, nothing merged.

## Planner-added requirements
- Setup looks among tracked files, as it does for decision records, and records a pointer for a document that states, in whatever words, that it is the repository's product philosophy or its engineering philosophy and that carries a ratification record; where more than one document fits one philosophy it records none, names them in the report and leaves that philosophy listed as missing. This is how setup looks, not a form a philosophy must take. Needed because: to record a pointer setup has to tell a philosophy from any other document and tell which of the two it is; the ratification record is the one thing the form asks of every philosophy, and the document's own statement of what it is is the only thing in it that says which. With two that fit, setup cannot know which the person means, and the brief lets a philosophy go unfound and be corrected by a sentence.
- The line that lists a philosophy as missing is worded so that it cannot be read as a pointer, and the texts that find philosophies through pointer lines say so. Needed because: a pointer turns value-level operation on, and the brief's constraint is that a run behaves as today while a philosophy is missing.
- The lines are derived again at every refresh, in a repository set up before this change as well. Needed because: the brief's "stays visible" is the common rule file, and an accepted record has no stored state decide what a rule file says.
- This repository's own rule file gets its two lines by a refresh under the built text. Needed because: it is the first repository the owner will see them in.
- One plugin version bump. Needed because: the package validator requires the three manifests to agree per installed version.

## Scope / Non-goals
- Scope: `rulebook` (SKILL.md, `bootstrap-lifecycle.md`, `rules-files.md`, `rule-suite-templates.md`), `value-documents/SKILL.md`, `counsel/SKILL.md`, `orchestration-harness` (SKILL.md, `value-level-operation.md`, `value-audit-mandate.md`), the three manifests, two fixture repositories under `tests/coding-agent-orchestration-harness/fixtures/`, a decision record if the admission test passes, this repository's `docs/coding-agent/rules/common.md`.
- Non-goals: the brief's "Left out on purpose" (standing approvals and initiative briefs as missing items); a script that performs setup; a validator for the rule files' content; any change to how a philosophy is written or ratified; the fixed dispatch templates.

## Design
- Chosen: setup stays what it is, the rulebook's bootstrap and refresh, followed as text. It gains one step beside the one for decision records: look among tracked files for a philosophy that names itself and carries a ratification record; record a pointer line for one found, or a line saying there is none yet, what it gives and how to start; say in the report which it did. Counsel reads that section of the common rule file when it opens.
- Alternative: setup records no pointer by itself; it lists every philosophy as missing unless a pointer already exists, and the person names the file.
- Lenses. structure: chosen adds one detection rule to the rulebook; the alternative adds none. evolution: chosen changes who writes a pointer first, which the brief states as a rule in force that changes; the alternative leaves that rule alone. verification: both are checked by a fresh agent on a fixture; chosen needs the second fixture. operation: none. human: with the alternative a person who already has a philosophy is told it is missing every time, which the brief's "everything is in place" rules out. safety: chosen can record a wrong file, bounded by the self-naming and ratification test and corrected by his objection; the alternative cannot.
- Why chosen: the brief gives that an existing philosophy is found and its pointer recorded.

## Compatibility stance (required if a contract/interface/persisted format is touched)
- surface: the "Repository Reference Documents" section of `docs/coding-agent/rules/common.md` (two line forms added); who may add a philosophy pointer line.
- stance: preserve
- justification: the locatable consumers are this repository and Character Memory. An existing pointer line keeps its form and meaning. A repository set up earlier gains the lines at its next refresh and nothing in it stops working before that. A line that says a philosophy is missing is not a pointer, so value-level operation stays off where it was off.

## Context (workspace)
- Governing brief: `docs/coding-agent/briefs/active/setup-names-what-is-missing-brief.md`, ratified 2026-10-05 ("I ratify the brief, hand it over after the run closes."), handed over by Counsel's relay of 2026-10-05, taken up after the audit-positions change on his word.
- Run record: `docs/coding-agent/plans/active/setup-names-what-is-missing-run.md`. Readings file: `docs/coding-agent/plans/active/setup-names-what-is-missing-readings.md`. This plan starts from revision: 6935b2c3.
- Research: a Researcher report received in session on 2026-10-05; not on disk, so nothing here rests on it alone. Facts the plan relies on, each checkable in the tree: setup is the rulebook's full bootstrap, followed as text (`skills/rulebook/references/bootstrap-lifecycle.md`); it detects a decision-record convention among tracked files, records it without asking, reports what it recorded and flags a contradiction at refresh; the section "Repository Reference Documents" is required and its lines are free; the rule that a pointer line is added only on the owner's word is in `value-documents/SKILL.md` and `value-level-operation.md` and in no decision record; Counsel reads no rule file when it opens; no fixture repository exists.
- The audits of this run: this plan's draft and its close.
- Design record consulted and deviations from its acceptance: ADR-D-0036 (kept: setup states no value and infers none; it leaves forms and locations to the value-document form), ADR-D-0024 and ADR-D-0025 (kept: the lines sit in the common rule file and are derived again at refresh), ADR-D-0052 and ADR-D-0056 (kept).

## Open Questions (max 3)
- None for the owner.

## Assumptions
- A1: a pointer whose file is gone or moved is flagged at refresh and the line is left as it is; removing or repointing it stays on the owner's word. source: the brief's means on refresh; `value-level-operation.md` on a pointer that names an absent file.
- A2: a Counsel session mentions what is missing once, when it opens, and offers to start; it does not raise it again in that session. source: the brief, "may offer to start" and "Nothing nags"; a reading.
- A3: scenario 2's "a later run there is kept to that product philosophy" is shown on the fixture by the start of a run, not a whole one: a plan drafted under the built text and a value audit of it at plan draft, whose verdict names the philosophy as its product basis. source: `orchestration-harness/SKILL.md` on what turns value-level operation on; a reading of how much of a run shows that it is kept to the philosophy.

## Tasks

### Task_1: Draft the record
- type: docs
- owns:
  - docs/coding-agent-orchestration-harness/decisions/**
- depends_on: []
- description: |
  A Worker runs the admission test on one decision: setup may record a philosophy's pointer line itself for a document that names itself and carries a ratification record, the person hearing of it in the report and removing it by objecting; no philosophy is drafted, templated or inferred by setup. The brief already states the changed rule, so a record that only repeats it does not pass: the Worker has to find a decision that binds later work and cannot be read back from the brief or this plan, or return that the test failed. If the test passes it drafts the record as proposed, writing only what the brief and this plan's log state and reporting gaps. The Orchestrator checks it says what was decided, a Reviewer checks it against the record standard, and it goes to the owner by name. If the test fails, no record is written, the content stays in the plugin text, and Task_2 starts with nothing asked of the owner.
- acceptance:
  - The admission test's result is reported with its reasons.
  - A record, if drafted, states only what the brief or this plan's log states; every gap is reported, none filled.
  - No text of Task_2 is written before the owner has accepted the record by name, or before the test has failed.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "python scripts/validate_harness_package.py from the plugin root; git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "ADR review per the subagent-strategy ADR-review snippet"

### Task_2: Setup, the pointer rule, Counsel's opening
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/rulebook/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/rulebook/references/bootstrap-lifecycle.md
  - plugins/coding-agent-orchestration-harness/skills/rulebook/references/rules-files.md
  - plugins/coding-agent-orchestration-harness/skills/rulebook/references/rule-suite-templates.md
  - plugins/coding-agent-orchestration-harness/skills/value-documents/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/counsel/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/value-level-operation.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/value-audit-mandate.md
  - plugins/coding-agent-orchestration-harness/.claude-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.codex-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.github/plugin/plugin.json
- depends_on: [Task_1]
- description: |
  The rulebook's bootstrap and refresh gain the philosophy step and its two line forms; the report says which philosophies were found and recorded and which are missing, with what each gives and how to start; the pointer rule in the value-document form and the run-side reference follows the brief; a line saying a philosophy is missing is not a pointer for any text that finds philosophies through pointer lines; Counsel reads that section when it opens and may offer once; an Orchestrator session and a run say nothing of what is missing.
- acceptance:
  - At bootstrap and at refresh the common rule file's "Repository Reference Documents" section has, for each of the two philosophies, either a pointer line or one line saying there is none yet, what it gives once it exists, and that it starts by opening a Counsel session; the report says the same and lists nothing else as missing.
  - A pointer is recorded by setup only as the planner-added requirement states, and the report names the file; the person's objection removes it; a pointer whose file is gone or moved is flagged at refresh and left as it is.
  - Setup writes, drafts, templates and offers nothing for a philosophy's content, and no text has it infer one.
  - A line saying a philosophy is missing is not a pointer: it turns value-level operation neither on nor off, so a run under a governing brief is audited as today and a run with no value documents has no audit as today; no Orchestrator text mentions what is missing to the person; a Counsel session mentions it once when it opens and offers to start.
  - The value audit's fixed dispatch template is byte-identical to this plan's start revision; the three manifests agree at the next version.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "python scripts/validate_harness_package.py; python scripts/run_validation_smoke_tests.py; git diff --check; hash of the template block against the start revision"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review against the brief and this task's acceptance; a trace of scenario 3 through Counsel's and the Orchestrator's text"

### Task_3: Two fixture repositories and the scenarios on them
- type: test
- owns:
  - tests/coding-agent-orchestration-harness/fixtures/setup-philosophy/**
- depends_on: [Task_2]
- description: |
  Two small fixture repositories are added as file sets: one with no philosophy, one with a ratified product philosophy under a path and name of its own. A fresh agent that has read nothing of this run copies each into a temporary git repository and follows the built rulebook text from the working tree to set it up; its report and the resulting common rule file are returned as evidence for scenarios 1 and 2. On the second fixture, after setup, a second fresh agent takes the small request the fixture carries and, following the built orchestration text from the working tree, drafts a plan for it; the Orchestrator of this run then dispatches a fresh Auditor on that plan by the fixed template, in the fixture. Each dispatch text and whatever else the runtime put in the agent's context is kept with the returned artifacts.
- acceptance:
  - On the first fixture the report and the common rule file each name both philosophies as missing, with what each gives and how to start, and list nothing else as missing.
  - On the second the pointer to the product philosophy is recorded and the report says so, and only the engineering philosophy is listed as missing.
  - Neither setup wrote, drafted or templated a philosophy.
  - On the second fixture the later plan's audit verdict names the product philosophy, found through the pointer setup recorded, as its product basis and grades the plan's items against it; this shows the start of a run kept to it, and is not claimed as a whole run.
- validation:
  - kind: manual
    required: true
    owner: reviewer
    detail: "A fresh agent's setup on each fixture in a temporary repository (the report text and the common rule file's section are the evidence); on the second, a fresh agent's plan draft and a fresh Auditor's verdict on it"

### Task_4: Land the record; refresh this repository's rule file; close
- type: review
- owns:
  - docs/coding-agent-orchestration-harness/decisions/**
  - docs/coding-agent/rules/common.md
  - docs/coding-agent/plans/**
- depends_on: [Task_1, Task_2, Task_3]
- description: |
  On the owner's acceptance naming the record the Orchestrator sets it accepted and logs the quoted words. After Task_3 it refreshes this repository's own common rule file under the built text, which lists both philosophies as missing here. It then closes the plan (closeout audit with its reading; final review) and the run: the branch pushed on the stack, a pull request opened under the standing approval, the note to Counsel, `candidate ready`.
- acceptance:
  - No record is set accepted without the owner's acceptance naming it, logged with the quoted words.
  - This repository's common rule file names both philosophies as missing in the built form and carries no pointer for either.
  - Every outgoing commit, message and pull request text is swept for machine-specific names and paths before it is pushed; nothing is merged.
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
- Wave 1: Task_1
- Wave 2: Task_2
- Wave 3: Task_3
- Wave 4: Task_4

Task_2 waits for the owner's acceptance of the record, or for the admission test to fail.

## Rollback / Safety
- The branch reverts on its own; no migration, no persisted data. A repository refreshed under the new text and then under the old one keeps two free lines the old text ignores.

## Progress Log (append-only)

## Decision Log (append-only; re-plans and major discoveries)
- 2026-10-05 Decision: requirement challenge before decomposition.
  - Trigger / new insight: the brief, read for what need not exist, and the questions research left open.
  - Plan delta (what changed): no setup script and no rule-file validator are added, since setup is text a model follows and the brief asks for no more. Settled from the brief without asking: with two candidate files for one philosophy setup records neither and names both; a repository set up earlier gains the lines at its next refresh; a pointer whose file is gone is flagged and left; Counsel offers once per session.
  - Tradeoffs considered: detecting a philosophy by file name alone; not taken, it would record documents nobody ratified.
  - User approval: not applicable at draft
  - Record proposed: one, at Task_1, if the admission test passes
- 2026-10-05 Decision: draft-plan review (Codex reviewer): NEEDS_REVISION, two major and one minor finding, all applied.
  - Trigger / new insight: (1) the plan said value-level operation is off while philosophies are missing, which would have switched off the audit of a run under a brief, this one included; (2) scenario 2's later run had only a trace behind it though the plan promised it on a fixture; (3) the reason given for the detection rule leaned on a record that does not say it, and the tracked-files limit was not listed as added.
  - Plan delta (what changed): a missing line turns nothing on and nothing off. Task_3 adds, on the second fixture, a plan drafted by a fresh agent and a fresh Auditor's verdict on it. The detection rule is restated as how setup looks, with its own reason, and names tracked files. Task_1 says a record that only repeats the brief fails the test, and that a failed test starts Task_2 with nothing asked.
  - Tradeoffs considered: a whole run on the fixture; not taken, the plan draft and its audit are where being kept to a philosophy first shows.
  - User approval: not applicable at draft
  - Record proposed: unchanged

## Notes
- A record is checked by the owner before anything is built on it; the audits of this run are at this plan's draft and close.
