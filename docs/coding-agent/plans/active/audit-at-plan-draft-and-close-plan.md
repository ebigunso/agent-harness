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
- One plugin version bump. Needed because: the package validator requires the three manifests to agree per installed version.

## Scope / Non-goals
- Scope: `orchestration-harness/references/value-level-operation.md` and `value-audit-mandate.md`, `wave-integration/references/integration-checklist.md`, `subagent-strategy/references/prompt-snippets.md`, the three manifests.
- Non-goals: the fixed dispatch template, whose `wave boundary` fill-in stays and names an assessment event in a goal run; goal mode; any decision record (none fixes the audit's positions); a numeric limit on a plan's length.

## Design
- Chosen: the plan-mode text names two audit positions, a plan's draft and its close; the wave-boundary step and what serves it are removed; the plan-review instructions gain the brief's check on a plan's length, in the brief's words, with the fact that no audit runs between a plan's draft and its close offered to the Reviewer as the thing to weigh.
- Alternative: keep the wave-boundary position in the text and make it conditional, dispatched only for a wave the Orchestrator judges risky.
- Lenses. structure: chosen removes a position and its bookkeeping (the revision recorded at each wave); the alternative keeps both and adds a judgement. evolution: chosen leaves one rule to maintain; the alternative leaves a condition to tune. verification: chosen is checked by a search that finds no wave-boundary audit of a plan; the alternative cannot be checked from the text. operation: chosen costs two audits a plan; the alternative costs between two and one per wave. human: with the chosen design drift inside a plan shows at its close, which is why the plan review looks at length; the alternative shows it sooner where the Orchestrator guessed right. safety: the alternative has the audited party decide when it is audited.
- Why chosen: the brief says "nowhere between", and the alternative puts the choice of when to audit with the party being audited.

## Compatibility stance (required if a contract/interface/persisted format is touched)
- surface: when the value audit runs in a plan-mode run; what a plan review reports.
- stance: break
- justification: the consumers that can be located are this repository's own runs and Character Memory with the plugin installed; the owner asked for the change in cadence by amendment. A plan-mode run stops dispatching an audit at wave boundaries. Preserved: a goal-mode run's audit moments, and the fixed dispatch template, whose `wave boundary` value keeps its one remaining consumer, an assessment event in a goal run.

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
  The plan-mode text states two audit positions, a plan's draft and its close, and no audit between; every line that asks for or serves a wave-boundary audit of a plan is removed or reworded; the goal-run text and the fixed template stay. The plan-review snippet has the Reviewer report a plan that is unacceptably long, in the brief's words, and tells the Reviewer the one fact that bears on it: under value-level operation no audit runs between a plan's draft and its close.
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
  - Plan delta (what changed): no record is proposed, since none fixes the positions; no numeric limit on a plan's length and no definition of "unacceptably long" is added; the Reviewer judges.
  - Tradeoffs considered: a limit in tasks or waves; not taken, the brief gives a judgement and a count would be the run's own.
  - User approval: not applicable at draft
  - Record proposed: none
- 2026-10-05 Decision: draft-plan review (Codex reviewer): NEEDS_REVISION, three minor findings, all applied.
  - Trigger / new insight: the proportional design form does not fit a change to when the audit runs and to what the Reviewer reports; the compatibility stance was missing; the planner-added measure of a plan's length was not shown to be needed.
  - Plan delta (what changed): the Design section compares the chosen design with a conditional wave-boundary audit; the stance is stated (break for the plan-mode cadence, the goal-mode moments and the template preserved); the measure is dropped and the snippet uses the brief's words.
  - Tradeoffs considered: none further.
  - User approval: not applicable at draft
  - Record proposed: none

## Notes
- The audits of this run: this plan's draft and its close.
