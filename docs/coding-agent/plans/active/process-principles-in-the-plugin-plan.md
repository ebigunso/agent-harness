# Plan: Process principles in the plugin

- status: draft
- generated: 2026-10-08
- last_updated: 2026-10-08
- work_type: docs

## Goal
- The harness gives what the governing brief `docs/coding-agent/briefs/active/process-principles-in-the-plugin-brief.md` states: five process principles present once each in the plugin text at the place where it acts, as what the agent does and not what code must be; the record on discoveries brought in line with the second principle.
- The brief is the requirement and is not restated here; where this plan and the brief differ, the brief governs and the difference is a plan defect.
- This is the first plan of the run recorded in `docs/coding-agent/plans/active/process-principles-in-the-plugin-run.md`.

## Definition of Done
- Plan review asks, of each piece of a design, what it is for (the thing in the goal it serves; for a piece that prevents something, the situation and how likely it is in everyday use) and what it costs (debt, operational complexity, effect on future change, blast radius relative to the task); a preventive piece that does not make its case is a finding, and so is a smaller design the questions point to. Stated once, where the plan-review check lives; the Plan Gate points to it.
- A discovered issue is read by the Orchestrator as one of three: within the task as given, fixed in place; a change to the design, which revises or extends the plan; a matter for later, noted for its own task. It is never absorbed into the current change. A plan revised or extended mid-run goes back through the gate that admitted it, for what changed, before any of it is built: the plan review, and the value audit on the plan as it now stands (under a brief), or the user's approval of the revision (without one); the audit's scope test applies to the revision; the two questions apply to each added piece. Stated once, in the replan procedure; the triggers and the wave checklist point to it.
- Reports say what was left out and why, what was not verified, and where the work scoped down, out loud; the final response states it once and the Worker report's summary feeds it with no new key.
- The closing review names any evidence artifact (test output, probe results, captured samples and the like) left in the change or lying in the working tree once its claim is recorded; it stays only where the change makes the case that future work rests on it; regression tests are not evidence. Stated once, in the Reviewer's final check.
- A guard, a limit or a compromise states where it is added what it is for and when it could go. Stated once, in the core principles, widening the existing line on suppressions and scaffolding.
- No new text states a code norm; the existing code norms in the plugin are left as they are and named to the owner.
- The record on discoveries (ADR-D-0033) is revised to the second principle and accepted by the owner by name before harness text is built on it; ADR-D-0041 where its decision on changes after the verdict tightens, and ADR-D-0051 where a reason becomes false, likewise.
- Package validators and smoke tests pass; the branch has Reviewer `APPROVED`.
- The plan closes and the run is reported ready: branch published on the stack, pull request opened under the standing approval, note to Counsel, nothing merged.

## Planner-added requirements
- Without a brief, "the same gate that admitted it" is the plan review and the user's approval of the revision; the record's two pause cases toward the user (contract-shape; irreversible or outward-facing) widen by this one. Needed because: the brief's guard names the gate that admitted the plan, and outside a brief that gate is the user's approval (ADR-D-0040); without this the principle would hold only under a brief.
- A mid-run revision is audited at position `plan draft` on the whole revised plan, dispatched by the fixed template with `Changes since: none`, after the plan review of the revision closes. Needed because: the mandate names positions and the template is fixed; the revision needs a position the auditor already knows how to grade.

## Scope / Non-goals
- Scope: `subagent-strategy/references/prompt-snippets.md` (plan-review check); `orchestration-harness/SKILL.md` (Plan Gate pointer; Replan Triggers' action line); `orchestration-harness/references/{lifecycle-gates,final-response-contract,value-audit-mandate (positions text only)}.md`; `wave-integration/references/integration-checklist.md`; `subagent-report-contract/SKILL.md` (the summary line) and its schema comment; `engineering-quality-baselines/references/{review-rubric,core-principles}.md`; records ADR-D-0033, ADR-D-0041, ADR-D-0051.
- Non-goals: any code norm, new or existing (compatibility stance, smallness as a target, refactoring, irreversibility: left as they are); a mechanism to carry a philosophy between repositories; the Reviewer adapters' output format; the fixed dispatch template; a fixture (the brief's pass conditions are agent-checkable on the text, and its scenarios are his next real run).

## Design
- Chosen: each principle tightens the one existing statement nearest to where it acts (the plan-review snippet; the replan procedure; the final-response contract with the Worker summary feeding it; the Reviewer's final check; the core principles' reason line), with the Plan Gate, the triggers and the wave checklist pointing rather than restating; the records that decide discoveries and post-verdict changes are revised in place and return by name.
- Alternative: one new reference, `process-principles.md`, stating the five together, pointed to from each place.
- Lenses. structure: chosen keeps one statement per principle at its point of action; the alternative adds a file every role reads and five pointers. evolution: chosen edits text that already loads at those moments; the alternative risks a sixth statement drifting from the five places. verification: both checked by reading; chosen is checked by the brief's "present once at the place where it acts". operation: chosen adds no read. human: an agent meets the principle where it acts, not in a separate list. safety: neither adds a code norm; chosen touches lines that sit beside code norms (core-principles 68) and must edit only the reason clause.
- Why chosen: the brief's means says tighten rather than add a second statement.

## Compatibility stance (required if a contract/interface/persisted format is touched)
- surface: the Worker report's `summary` meaning (no key added); the replan procedure.
- stance: preserve
- justification: no schema key changes; existing reports remain valid.

## Context (workspace)
- Governing brief: `docs/coding-agent/briefs/active/process-principles-in-the-plugin-brief.md`. Ratification reached this session on 2026-10-08 as Counsel's relay quoting the owner: "I ratify the brief, hand it over after the current run closes." Relays admitted by the Standing Approvals entry of 2026-10-01 in `common.md`.
- Run record: `docs/coding-agent/plans/active/process-principles-in-the-plugin-run.md`. Readings file: `docs/coding-agent/plans/active/process-principles-in-the-plugin-readings.md`. This plan starts from revision: 099d78f.
- Research: a Researcher mapped each principle to the text that states it in part (file and line) and found the record on discoveries: ADR-D-0033, which agrees on the Worker's side and differs on the Orchestrator's (it lets a discovery be ruled into the current change, sorts nothing, re-runs no review, and caps the return to the user at two cases). ADR-D-0041 says a post-verdict change needs a later audit or the first source, with no plan review. ADR-D-0051's rejected alternative gives "no fresh plan review" as a reason, which the guard makes false.
- Existing code norms named to the owner, left as they are: plan-format rule 8 (compatibility stance); core-principles §1 and §2 (locatable consumer; small, cohesive, reversible changes; smallest root-cause fix); long-horizon-audit's deletion bias; ADR-D-0016.
- Research waived for dispatch: the Researcher's map is the basis of the Scope and Tasks.
- The audits of this run: this plan's draft and its close.

## Open Questions (max 3)
- None.

## Assumptions
- A1: "the smaller design wins" is the outcome of the two questions, not a size target; the text says so. source: the brief's constraint that no stance on smallness enters.
- A2: ADR-D-0053's test (a finding bears on the design when acting on it changes what someone experiences) stays the value question's test; the second principle's "change to the design" is the implementation design, read by the Orchestrator in the replan procedure; the two are reconciled in ADR-D-0033's revision. source: the brief's second principle; ADR-D-0053.

## Tasks

### Task_1: The records carry the second principle
- type: docs
- owns:
  - docs/coding-agent-orchestration-harness/decisions/**
- depends_on: []
- description: |
  Revise ADR-D-0033 to the brief's second principle and its guard (the three-way reading; a design change revises or extends the plan and goes back through the admitting gate for what changed before any is built; never absorbed); ADR-D-0041 where its decision on changes after the verdict gains the plan review; ADR-D-0051 only where a reason becomes false. Write only what the brief and this plan state.
- acceptance:
  - ADR-D-0033 states the three-way reading and the guard, keeps the Worker's side as it is, and reconciles with ADR-D-0053 (A2).
  - ADR-D-0041 says a change to what the plan decides after the verdict goes through the plan review and a new audit of the plan as it stands before the changed item is built.
  - ADR-D-0051 changed only if a reason it gives becomes false; the change named.
  - Each record whose decision, boundary, reasons or reopen conditions changed is named in the report, so each returns to the owner by name.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "python scripts/validate_harness_package.py; python scripts/run_validation_smoke_tests.py; git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "The records against adr.md and the brief; which return by name"
  - kind: manual
    required: true
    owner: user
    detail: "The owner accepts each revised record by its own name, carried by Counsel's relay; Task_2 is not dispatched before that"

### Task_2: The five principles at the place where each acts
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/subagent-strategy/references/prompt-snippets.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/lifecycle-gates.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/final-response-contract.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/value-audit-mandate.md
  - plugins/coding-agent-orchestration-harness/skills/wave-integration/references/integration-checklist.md
  - plugins/coding-agent-orchestration-harness/skills/subagent-report-contract/**
  - plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/review-rubric.md
  - plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/core-principles.md
  - plugins/coding-agent-orchestration-harness/agents/Orchestrator.md
  - plugins/coding-agent-orchestration-harness/claude/agents/harness-orchestrator.md
- depends_on: [Task_1]
- description: |
  Each principle tightened into its one place as the Definition of Done states; the other places point to it; the mandate's positions text admits a revision audited at plan draft; the fixed template byte-identical; the Orchestrator adapters only where they restate the replan action.
- acceptance:
  - Each Definition of Done item on the five principles holds, and each statement of the brief's "The process principles" can be pointed to in exactly one place, the others pointing.
  - No new text states a code norm; the lines named in Context as existing code norms are unchanged.
  - The fixed dispatch template is byte-identical; the adapters agree with each other and with the skill text.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "python scripts/validate_harness_package.py; python scripts/run_validation_smoke_tests.py; python skills/subagent-report-contract/scripts/validate_worker_report.py --file ../../tests/coding-agent-orchestration-harness/fixtures/valid-worker-report.yaml; git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review against the brief and the accepted records: each principle once at its place; no code norm; adapter parity. This is also the branch's final review."

### Task_3: Close the plan and report the run ready
- type: review
- owns:
  - docs/coding-agent/plans/**
- depends_on: [Task_2]
- description: |
  The Orchestrator closes the plan (closeout audit with its reading) and reports the run ready: branch pushed on the stack, pull request opened under the standing approval, note to Counsel; the run stays open until the owner's acceptance of its stack.
- acceptance:
  - The closeout audit is dispatched by the fixed template and logged; the closeout says plainly that no fixture was run and that the scenarios are his next real run.
  - Every outgoing commit, message and pull request text is swept for machine names and paths and for the names of his other repositories; nothing is merged.
- validation:
  - kind: command
    required: true
    owner: orchestrator
    detail: "package validator and smoke tests; privacy sweep over every commit to be pushed"

## Task Waves (explicit parallel dispatch sets)
- Wave 1: Task_1
- Wave 2: Task_2
- Wave 3: Task_3

## Rollback / Safety
- The branch reverts on its own; no migration, no persisted data.

## Progress Log (append-only)
- 2026-10-08 Brief committed on the run's branch; the plan starts from revision 099d78f.

## Decision Log
- 2026-10-08 Outside a brief the admitting gate is the user's approval, so a design change returns to the user with the plan review; ADR-D-0033's two pause cases widen by one (Planner-added 1). A revision is audited at plan draft on the whole revised plan (Planner-added 2).
