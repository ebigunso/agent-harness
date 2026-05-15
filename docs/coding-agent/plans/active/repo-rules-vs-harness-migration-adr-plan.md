# Plan: Repo Rules Vs Harness Migration ADR

- status: draft
- generated: 2026-05-16
- last_updated: 2026-05-16
- work_type: docs

## Goal
- Document the architectural boundary between repo-local rule candidates and cross-repo harness migration candidates in a dedicated ADR.

## Definition of Done
- ADR-D-0007 exists under the harness decisions directory.
- ADR states runtime agents maintain target-repository rules under `docs/coding-agent/rules/*.md`.
- ADR states cross-repo harness improvements are staged in `docs/coding-agent/skill-candidates.md` or `docs/coding-agent/skill-drafts/*.md`.
- ADR states `rule_candidates` are repo-local and `harness_migration_candidates` are for later harness-maintenance work.
- ADR explicitly rejects legacy global-candidate shapes that blur repo-local rules and harness-global changes.
- ADR documents the exception for explicit harness-maintenance tasks and plugin-modification tasks in this harness repository.
- Required validation passes or is explicitly waived with evidence.

## Scope / Non-goals
- Scope:
  - `docs/coding-agent-orchestration-harness/decisions/ADR-D-0007-repo-rules-vs-harness-migration-candidates.md`
- Non-goals:
  - Do not update bundled skill behavior in this plan.
  - Do not update validators in this plan.
  - Do not edit repository rule files.

## Context (workspace)
- Related files/areas:
  - `docs/coding-agent-orchestration-harness/decisions/ADR-D-0006-repository-rule-suite-bootstrap-lifecycle.md`
  - `plugins/coding-agent-orchestration-harness/skills/subagent-report-contract/SKILL.md`
  - `plugins/coding-agent-orchestration-harness/skills/rulebook/SKILL.md`
  - `plugins/coding-agent-orchestration-harness/skills/rulebook/references/rules-files.md`
- Existing patterns or references:
  - ADRs under `docs/coding-agent-orchestration-harness/decisions/` capture durable architecture and implementation decisions.
  - ADR-D-0006 documents bootstrap lifecycle but not the later clean split between repo rules and harness migration candidates.
- Repo reference docs consulted:
  - `docs/coding-agent/rules/index.md`
  - `docs/coding-agent/rules/common.md`
  - `docs/coding-agent/rules/orchestrator.md`
  - `docs/coding-agent/rules/worker.md`

## Open Questions (max 3)
- Q1: None.

## Assumptions
- A1: ADR numbering should continue after ADR-D-0006.
- A2: The ADR should be compact and focused on the clean split, not a complete restatement of the rulebook lifecycle.
- A3: Rejected legacy shapes should be named directly because this ADR protects a runtime boundary, not only a schema cleanup.

## Tasks

### Task_1: Add ADR-D-0007
- type: docs
- owns:
  - `docs/coding-agent-orchestration-harness/decisions/ADR-D-0007-repo-rules-vs-harness-migration-candidates.md`
- depends_on: []
- description: |
  Create an ADR documenting the clean split between repo-local rule candidates and staged cross-repo harness migration candidates.
- acceptance:
  - ADR has title, status/date, context, decision, consequences, and rejected alternatives or non-goals.
  - Decision states runtime agents maintain target-repository operating rules under `docs/coding-agent/rules/*.md`.
  - Decision states cross-repo harness improvements discovered during target-repository work are not written directly into bundled skills, references, agents, validators, or plugin files.
  - Decision names staging locations: `docs/coding-agent/skill-candidates.md` and `docs/coding-agent/skill-drafts/*.md`.
  - Decision states `rule_candidates` are always repo-local and `harness_migration_candidates` are always staged for later harness-maintenance work.
  - ADR includes a Rejected Legacy Shapes section naming `rule_candidates[].intended_home: global_candidate`.
  - ADR rejects `lesson_candidates[].promotion_target: global-skill` and `lesson_candidates[].promotion_target: references/*`.
  - ADR rejects `Global Migration Candidates` sections inside role rule files such as `common.md`, `worker.md`, `orchestrator.md`, and `reviewer.md`.
  - ADR documents the exception that bundled harness skills, references, adapters, and validators may be edited directly during explicit harness-maintenance tasks or when the target repository is the harness repository and the requested task is to modify the plugin.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "git diff --check -- docs/coding-agent-orchestration-harness/decisions/ADR-D-0007-repo-rules-vs-harness-migration-candidates.md"
  - kind: review
    required: true
    owner: reviewer
    detail: "Confirm ADR documents the boundary without changing runtime process by itself."

### Task_2: Cross-Check Clean-Split Terminology
- type: review
- owns: []
- depends_on:
  - Task_1
- description: |
  Compare ADR terminology against existing Worker report contract, rulebook guidance, and active references that mention `rule_candidates` or `harness_migration_candidates`.
- acceptance:
  - ADR terminology is consistent with Worker report contract.
  - ADR terminology is consistent with rulebook staging guidance.
  - ADR does not reintroduce `global_candidate`, `global-skill`, or role-file "Global Migration Candidates" as acceptable current shapes.
  - ADR distinguishes historical legacy references from current rejected shapes where `rg` finds old terms.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "rg -n \"rule_candidates|harness_migration_candidates|skill-candidates.md|global_candidate|global-skill|Global Migration Candidates\" docs plugins/coding-agent-orchestration-harness"
  - kind: review
    required: true
    owner: reviewer
    detail: "Confirm cross-check results support the ADR wording and note any intentional legacy references."

## Task Waves (explicit parallel dispatch sets)

Interpretation:
- Tasks listed in the same wave are intended to be dispatched in parallel by default when `owns` are disjoint and dependencies are met.
- Waves are executed sequentially.

- Wave 1 (parallel): [Task_1]
- Wave 2 (parallel): [Task_2]

## E2E / Visual Validation Spec

- Not applicable; no UI or user flow is impacted.

## Rollback / Safety
- Remove only the new ADR file if the decision is withdrawn.
- If ADR wording requires updates to skills or validators, record that as follow-up work rather than expanding this plan.

## Progress Log (append-only)

- 2026-05-16 00:00 Plan drafted.
  - Summary: Created scoped implementation plan for documenting the repo-rule vs harness-migration split.
  - Validation evidence: Not run; draft plan only.
  - Notes: Research waived because the user supplied current-file findings and work is limited to plan creation.

## Decision Log (append-only; re-plans and major discoveries)

- 2026-05-16 00:00 Decision: Keep ADR work separate from implementation routing and validator hardening.
  - Trigger / new insight: User requested plans with clear responsibility boundaries.
  - Plan delta (what changed): This plan creates only the ADR and terminology cross-check.
  - Tradeoffs considered: Adding ADR edits to routing or validator plans would mix durable design record with operational changes.
  - User approval: yes, user requested actual plan files after reviewing the split.

- 2026-05-16 00:00 Decision: ADR-D-0007 must reject legacy global-candidate shapes explicitly.
  - Trigger / new insight: User clarified the rejected shapes and the explicit harness-maintenance exception.
  - Plan delta (what changed): Task_1 now requires a Rejected Legacy Shapes section and exception wording.
  - Tradeoffs considered: Leaving the rejection implicit would make future reintroduction more likely.
  - User approval: yes, user provided the desired ADR content.

## Notes
- Risks:
  - ADR could overstate enforcement before validator and routing plans are implemented.
  - Legacy terms may still exist in historical ADRs or completed plans; distinguish history from current accepted shape.
- Edge cases:
  - If ADR numbering already advanced in the branch, rename before implementation rather than creating a duplicate decision number.
