# Plan: The value audit at a plan's draft and close

- status: draft
- generated: 2026-10-05
- last_updated: 2026-10-05
- work_type: docs

## Goal
- The harness gives what the governing brief `docs/coding-agent/briefs/active/value-level-operation-brief.md` states, as amended on 2026-10-05, in its section "Value audit": in a run of plans the audit runs at each plan's draft and at each plan's close, and nowhere between; a plan review catches a plan that is unacceptably long.
- The brief is the requirement and is not restated here; where this plan and the brief differ, the brief governs and the difference is a plan defect.
- This is the only plan of the run recorded in `docs/coding-agent/plans/active/audit-at-plan-draft-and-close-run.md`.

## Definition of Done
- In a plan-mode run the plugin text has the value audit dispatched at a plan's draft and at its close and at no other moment; no text asks for an audit at a wave boundary of a plan.
- A goal-mode run's audit moments are as the accepted record on goal mode states, unchanged.
- The plan-review instructions have the Reviewer report a plan that is unacceptably long.
- The value audit's fixed dispatch template is byte-identical to this plan's start revision.
- Package validators and smoke tests pass; the branch has Reviewer `APPROVED`.
- The run closes as `completion-closeout.md` states: its branch published on the stack and a pull request opened under the standing approval, the note to Counsel sent, nothing merged.

## Planner-added requirements
- A plan is unacceptably long, for the Reviewer's purpose, when its build would run so far between its draft audit and its close audit that drift from the value documents would be costly to undo; the Reviewer says so and names where the plan could end sooner. Needed because: the brief gives the check and not its measure, and the reason he gave for the check is that no audit runs between a plan's draft and its close.
- One plugin version bump. Needed because: the package validator requires the three manifests to agree per installed version.

## Scope / Non-goals
- Scope: `orchestration-harness/references/value-level-operation.md` and `value-audit-mandate.md`, `wave-integration/references/integration-checklist.md`, `subagent-strategy/references/prompt-snippets.md`, the three manifests.
- Non-goals: the fixed dispatch template, whose `wave boundary` fill-in stays and names an assessment event in a goal run; goal mode; any decision record (none fixes the audit's positions); a numeric limit on a plan's length.

## Design
- Proportional form: the change removes one audit position from plan-mode text and adds one check to the plan-review instructions; it touches no responsibility, contract, persisted state, new component, trust boundary or hot path.

## Context (workspace)
- Governing brief: `docs/coding-agent/briefs/active/value-level-operation-brief.md`, ratified 2026-09-30; the amendment of 2026-10-05 carries the owner's quoted words beside it, and Counsel relayed on 2026-10-05 his word on when it is built: "Yes, do it first before the next one prepared."
- Run record: `docs/coding-agent/plans/active/audit-at-plan-draft-and-close-run.md`. Readings file: `docs/coding-agent/plans/active/audit-at-plan-draft-and-close-readings.md`. This plan starts from revision: 2e237902.
- Where the position is stated today: `value-level-operation.md` (the list of positions; "Record the revision at each wave's dispatch as well"), `value-audit-mandate.md` (the artifact "wave boundary and closeout"; the first paragraph), `wave-integration/references/integration-checklist.md` (the wave-boundary audit step). The goal-run section of the mandate uses the template's `wave boundary` fill-in for an assessment event and stays.
- Research waived: the five places were found by search of the plugin, the decision records and the rule files; no record or rule file states the position.
- This run itself is audited at this plan's draft and close only, by the brief as amended.
- Design record consulted: ADR-D-0052 (leaves the positions to the workflow text), ADR-D-0056 (goal-run moments; kept).

## Open Questions (max 3)
- None.

## Assumptions
- A1: the template's `Position` fill-in keeps its three values; in a plan-mode run `wave boundary` is not used. source: ADR-D-0050 and ADR-D-0056 keep the template unchanged.

## Tasks

### Task_1: Two positions in a plan-mode run; a long plan is reported at plan review
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/value-level-operation.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/value-audit-mandate.md
  - plugins/coding-agent-orchestration-harness/skills/wave-integration/references/integration-checklist.md
  - plugins/coding-agent-orchestration-harness/skills/subagent-strategy/references/prompt-snippets.md
  - plugins/coding-agent-orchestration-harness/.claude-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.codex-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.github/plugin/plugin.json
- depends_on: []
- description: |
  The plan-mode text states two audit positions, a plan's draft and its close, and no audit between; every line that asks for or serves a wave-boundary audit of a plan is removed or reworded; the goal-run text and the fixed template stay. The plan-review snippet has the Reviewer report a plan that is unacceptably long, by the measure in this plan's planner-added requirements.
- acceptance:
  - No plugin text has a value audit dispatched at a wave boundary of a plan, and nothing left depends on one (the revision recorded at each wave's dispatch, the checklist step).
  - The goal-run section of the mandate and the Fixed Dispatch Template block are byte-identical to this plan's start revision.
  - The plan-review snippet states the check on a plan's length once.
  - The three manifests agree at the next version.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "python scripts/validate_harness_package.py; python scripts/run_validation_smoke_tests.py; git diff --check; hash of the template block against the start revision"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review against the brief's amended lines and this task's acceptance"

### Task_2: Close the plan and the run
- type: review
- owns:
  - docs/coding-agent/plans/**
- depends_on: [Task_1]
- description: |
  The Orchestrator closes the plan (closeout audit with its reading; the review of Task_1 is the branch's final review) and the run: the branch pushed on the stack, a pull request opened under the standing approval, the note to Counsel, `candidate ready`.
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

## Decision Log (append-only; re-plans and major discoveries)
- 2026-10-05 Decision: requirement challenge before decomposition.
  - Trigger / new insight: the amendment asks for less auditing and one check at plan review.
  - Plan delta (what changed): no record is proposed, since none fixes the positions; no numeric limit on a plan's length is added.
  - Tradeoffs considered: a limit in tasks or waves; not taken, the brief gives a judgement and a count would be the run's own.
  - User approval: not applicable at draft
  - Record proposed: none

## Notes
- The audits of this run: this plan's draft and its close.
