# Plan: Setup holds and asks when several documents fit

- status: draft
- generated: 2026-10-06
- last_updated: 2026-10-06
- work_type: docs

## Goal
- The harness gives what the governing brief `docs/coding-agent/briefs/active/setup-names-what-is-missing-brief.md` states in the statement added on 2026-10-06 under "A philosophy that already exists": where more than one document fits, setup records nothing by itself and does not write the philosophy down as simply missing; it holds, shows the person the candidates, and the person picks.
- The brief is the requirement and is not restated here; where this plan and the brief differ, the brief governs and the difference is a plan defect.
- This is the only plan of the run recorded in `docs/coding-agent/plans/active/setup-holds-when-several-fit-run.md`. It follows the run that closed on 2026-10-06 (`docs/coding-agent/plans/completed/setup-names-what-is-missing-plan.md`), whose closed plan is not reopened.

## Definition of Done
- Where more than one tracked document fits one philosophy, the setup text has setup record no pointer, write a line that names the candidates as awaiting the person's word and not the none-yet line, and bring the candidates to the person in its report; the person's pick records that document's pointer, which ends the looking.
- The rest of setup's philosophy step behaves as it does at this plan's start revision.
- On a fixture repository that holds two fitting documents, a fresh agent following the setup text records no pointer, writes the awaiting line naming both, and brings both for the person to pick.
- The value audit's fixed dispatch template is byte-identical to this plan's start revision.
- Package validators and smoke tests pass; the branch has Reviewer `APPROVED`.
- The run closes as `completion-closeout.md` states: its branch published on the stack and a pull request opened under the standing approval, the note to Counsel sent, nothing merged.

## Planner-added requirements
- When the person answers that none of the candidates is the philosophy, the line that replaces the awaiting line names each as not it, as a file is named after an objection. Needed because: the lines are derived again at every refresh, and without that record the next refresh would find the same documents and ask again. A pick needs no such record: the pointer it writes ends the looking.

## Scope / Non-goals
- Scope: `rulebook/references/bootstrap-lifecycle.md` and `rules-files.md`, `counsel/SKILL.md` where it speaks of an awaiting line, one fixture under `tests/coding-agent-orchestration-harness/fixtures/setup-philosophy/`.
- Non-goals: any other branch of setup's philosophy step; the texts on what is not a pointer, which already cover every line that is not settled; the fixed dispatch templates; a decision record (none states setup's step).

## Design
- Chosen: the awaiting line form carries one or more paths, and the several-fit branch writes it with every candidate; the report lists the candidates and asks the person to pick; a pick is the person's word for that pointer, and the candidates not picked are named in the pointer's place only if no pick is made.
- Alternative: a separate fifth line form for several candidates.
- Lenses. structure: chosen keeps four line forms and one branch for "held"; the alternative adds a form that differs only in number. evolution: chosen leaves one sentence on what is not a pointer true as written; the alternative would need each text that lists forms checked again. verification: both are shown by the same fixture. operation: none. human: the person reads the same kind of line whether one document or several are held. safety: neither records a pointer without the person's word.
- Why chosen: the brief says "likewise"; the same held state serves both cases.

## Compatibility stance (required if a contract/interface/persisted format is touched)
- surface: the awaiting line of the "Repository Reference Documents" section (it may name more than one file); what setup does when several documents fit.
- stance: break
- justification: the several-fit behaviour changes on the owner's word. The locatable consumers are this repository and Character Memory; neither holds a line written by the several-fit branch, since the text that wrote it has not been released.

## Context (workspace)
- Governing brief: `docs/coding-agent/briefs/active/setup-names-what-is-missing-brief.md`, ratified 2026-10-05; the statement of 2026-10-06 on several fitting documents carries the owner's quoted words: "Yes, hold and ask when several fit."
- Run record: `docs/coding-agent/plans/active/setup-holds-when-several-fit-run.md`. Readings file: `docs/coding-agent/plans/active/setup-holds-when-several-fit-readings.md`. This plan starts from revision: 34cb534.
- Where the behaviour is stated today: `bootstrap-lifecycle.md`, Philosophy Lines ("More than one, wherever each sits: record none and write the none-yet line."; the report's clause on "the files found where more than one fitted"); `rules-files.md`, the awaiting form with one path.
- Research waived: the change is confined to the section this run's predecessor wrote, read in full before drafting.
- The audits of this run: this plan's draft and its close.
- Design record consulted: none states setup's philosophy step; ADR-D-0024 and ADR-D-0025 (the lines are derived at refresh; kept).

## Open Questions (max 3)
- None.

## Assumptions
- A1: when the person picks one of several, the picked document's pointer is recorded on that word and the awaiting line is replaced by it; nothing is written about the others, since a pointer line ends the looking. source: `bootstrap-lifecycle.md`, "An existing pointer line is left as it is"; a reading.
- A2: when the person says none of them is it, the line becomes the none-yet line naming each as not it. source: the same section's rule for a no to an awaiting line.

## Tasks

### Task_1: Several fitting documents are held for the person to pick
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/rulebook/references/bootstrap-lifecycle.md
  - plugins/coding-agent-orchestration-harness/skills/rulebook/references/rules-files.md
  - plugins/coding-agent-orchestration-harness/skills/counsel/SKILL.md
  - tests/coding-agent-orchestration-harness/fixtures/setup-philosophy/**
- depends_on: []
- description: |
  The several-fit branch of setup's philosophy step writes the awaiting line with every candidate and brings them to the person to pick; the awaiting line form allows more than one path; the report and Counsel's opening mention follow. A fourth fixture holds two fitting documents: the repository's own product philosophy and a vendored project's.
- acceptance:
  - More than one fitting document: no pointer recorded, the awaiting line names each candidate, the report lists them and says the person's pick decides; the none-yet line is not written for that philosophy.
  - The person's pick replaces the awaiting line with that document's pointer; "none of them" replaces it with the none-yet line naming each as not it; a later refresh that changes nothing does not ask again.
  - Every other branch of the step, the fixed dispatch template, the mandate and the manifests read as at this plan's start revision.
  - The fourth fixture is a file set whose ratification lines are kept apart, as the other fixtures' are, so that nothing in this repository is itself a ratified philosophy.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "python scripts/validate_harness_package.py; python scripts/run_validation_smoke_tests.py; git diff --check"
  - kind: manual
    required: true
    owner: orchestrator
    detail: "After the Worker's report and before the review: a fresh agent's setup on the fourth fixture in a temporary repository, its whole reply stored with the fixtures' records"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review against the brief's statement; independent reading of the stored fixture reply against this task's acceptance"

### Task_2: Close the plan and the run
- type: review
- owns:
  - docs/coding-agent/plans/**
- depends_on: [Task_1]
- description: |
  The Orchestrator closes the plan (closeout audit with its reading; the review of Task_1, which covers the stored fixture reply, is the branch's final review) and the run: the branch pushed on the stack, a pull request opened under the standing approval, the note to Counsel, `candidate ready`.
- acceptance:
  - The closeout audit is dispatched by the fixed template and logged.
  - Every outgoing commit, message and pull request text is swept for machine-specific names and paths before it is pushed; nothing is merged.
- validation:
  - kind: command
    required: true
    owner: orchestrator
    detail: "package validator and smoke tests; privacy sweep over every commit to be pushed"

## Task Waves (explicit parallel dispatch sets)
- Wave 1: Task_1
- Wave 2: Task_2

## Rollback / Safety
- The branch reverts on its own; no migration, no persisted data.

## Progress Log (append-only)
- 2026-10-06 Plan review (Codex reviewer): NEEDS_REVISION with three minor findings, applied (see the Decision Log); re-review APPROVED with no finding open. Plan validator passes.
- 2026-10-06 Plan-draft audit, dispatch text (to a fresh Auditor dispatch on Fable):

  ```text
  You are the value auditor. Read references/value-audit-mandate.md of the orchestration-harness skill and follow it exactly. Position: plan draft. Plan: docs/coding-agent/plans/active/setup-holds-when-several-fit-plan.md. Governing brief: docs/coding-agent/briefs/active/setup-names-what-is-missing-brief.md. Changes since: none.
  ```

## Decision Log (append-only; re-plans and major discoveries)
- 2026-10-06 Decision: requirement challenge before decomposition.
  - Trigger / new insight: the statement is one sentence and asks for one branch to change.
  - Plan delta (what changed): no new line form, no record, no change to the texts on what is not a pointer.
  - Tradeoffs considered: see Design.
  - User approval: not applicable at draft
  - Record proposed: none
- 2026-10-06 Decision: draft-plan review (Codex reviewer): NEEDS_REVISION, three minor findings, all applied.
  - Trigger / new insight: the planner-added line recorded every candidate not picked, against A1 and for a reason that does not hold once a pointer exists; the fixture evidence Task_1 needs was placed in Task_2; the version bump's stated reason was not true of the validator.
  - Plan delta (what changed): the record of rejected candidates is kept only for an explicit "none of them"; the fresh agent's setup on the fourth fixture is the Orchestrator's validation item inside Task_1, before the review, which reads the stored reply; the version bump is dropped, no rule or check asking for one.
  - Tradeoffs considered: none further.
  - User approval: not applicable at draft
  - Record proposed: none

## Notes
- The audits of this run: this plan's draft and its close.
