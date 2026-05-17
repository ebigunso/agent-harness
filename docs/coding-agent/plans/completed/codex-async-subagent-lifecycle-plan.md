# Plan: Codex Async Subagent Lifecycle

- status: done
- generated: 2026-05-17
- last_updated: 2026-05-17
- work_type: docs

## Goal
- Integrate Codex-specific orchestration guidance for explicit harness-required subagent authorization, runtime-loader Orchestrator identity, minimal repository-rule entry, async/background dispatch waiting, final-report integration, and completed child-process cleanup.

## Definition of Done
- ADR-D-0008 exists and follows the existing ADR style.
- ADR-D-0008 includes the runtime-loader Orchestrator identity and repository-rule entry decision point rather than creating ADR-D-0009.
- `orchestration-harness/SKILL.md` clarifies that a main-thread runtime session loading the skill assumes the logical Orchestrator role.
- `orchestration-harness/SKILL.md` adds a minimal Repository Rule Entry step for `index.md`, `common.md`, and `orchestrator.md` without turning it into full lifecycle/readiness work.
- `orchestration-harness/SKILL.md` has only a concise runtime-neutral async/background dispatch hook.
- `subagent-strategy` routes async/background runtime details through a progressive-disclosure reference.
- `wave-integration` includes Orchestrator-owned cleanup for completed async/background child processes.
- Codex `AGENTS.md` loader explicitly authorizes bounded harness-required subagent dispatch while staying loader-only.
- Codex `AGENTS.md` loader does not receive Orchestrator identity wording, role mechanics, rule-loading details, plan gates, validation gates, or report schemas.
- Codex subagent TOML templates are not changed for idle-open process behavior.
- Package validation and smoke tests pass, or failures are reported with exact causes.

## Scope / Non-goals
- Scope:
  - Add one ADR under `docs/coding-agent-orchestration-harness/decisions/`.
  - Update the orchestration, subagent-strategy, wave-integration, and Codex loader documentation surfaces.
  - Add runtime-loader Orchestrator identity and minimal repository-rule entry guidance primarily in `orchestration-harness/SKILL.md`.
- Non-goals:
  - Do not change Researcher, Worker, or Reviewer TOML templates for "stop after final report" behavior.
  - Do not duplicate plan gates, validation gates, role mechanics, report formats, repository rule-loading algorithms, or async lifecycle details in the Codex loader.
  - Do not add hard validators for exact wording or unstable file layout.
  - Do not add a Codex loader duplication validator in this task; enforce loader-only behavior by review and existing validation.
  - Do not create ADR-D-0009 for this addendum unless ADR-D-0008 has already been completed and becomes too narrowly scoped to amend cleanly.
  - Do not perform broad progressive-disclosure refactors unrelated to this fix.

## Context (workspace)
- Related files/areas:
  - `docs/coding-agent-orchestration-harness/decisions/`
  - `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/SKILL.md`
  - `plugins/coding-agent-orchestration-harness/skills/subagent-strategy/SKILL.md`
  - `plugins/coding-agent-orchestration-harness/skills/subagent-strategy/references/`
  - `plugins/coding-agent-orchestration-harness/skills/wave-integration/SKILL.md`
  - `plugins/coding-agent-orchestration-harness/codex/snippets/AGENTS.md`
  - `plugins/coding-agent-orchestration-harness/scripts/validate_harness_package.py`
  - `docs/coding-agent/rules/index.md`
  - `docs/coding-agent/rules/common.md`
  - `docs/coding-agent/rules/orchestrator.md`
- Existing patterns or references:
  - ADR-D-0001 establishes `orchestration-harness/SKILL.md` as the canonical workflow policy surface.
  - ADR-I-0002 establishes the Codex `AGENTS.md` snippet as loader-only.
  - ADR-D-0007 provides the current ADR frontmatter and section style.
  - `subagent-strategy/SKILL.md` keeps detailed guidance behind references.
  - `orchestration-harness/SKILL.md` is the canonical workflow entrypoint and should stay concise.
  - Codex `AGENTS.md` snippet is loader-only.
- Repo reference docs consulted:
  - Existing ADR list under `docs/coding-agent-orchestration-harness/decisions/`.
  - Target skills and Codex loader snippet listed by the request.
  - ADR-D-0001 and ADR-I-0002.
  - Repository rule suite entry files: `index.md`, `common.md`, and `orchestrator.md`.

## Open Questions (max 3)
- None.

## Assumptions
- A1: The new ADR should be numbered `ADR-D-0008` and use status `accepted` unless repository maintainers prefer draft ADRs during implementation.
- A2: The async lifecycle reference belongs under `subagent-strategy/references/` because dispatch/waiting behavior is the owning progressive-disclosure surface.
- A3: Validation should run from `plugins/coding-agent-orchestration-harness` using the two requested Python scripts.
- A4: The runtime-loader Orchestrator identity and minimal repository-rule entry addendum should be incorporated into ADR-D-0008 as a related decision point because ADR-D-0008 has not been written yet.
- A5: ADR-D-0008 should use `status: accepted`, matching the existing implemented harness decision style.

## Tasks

### Task_1: Add ADR-D-0008
- type: docs
- owns:
  - `docs/coding-agent-orchestration-harness/decisions/ADR-D-0008-codex-explicit-subagent-authorization-and-async-dispatch-lifecycle.md`
- depends_on: []
- description: |
  Add the decision record that establishes Codex loader or harness invocation as explicit user direction for bounded harness-required subagent dispatch, records Orchestrator ownership of async child lifecycle, and includes runtime-loader Orchestrator identity plus minimal repository-rule entry as a related decision point.
- acceptance:
  - ADR frontmatter and section structure match existing decision records.
  - Decision covers explicit authorization, dependency-aware waiting, report integration, and cleanup/close behavior.
  - ADR states that an idle-open runtime child after final report is an Orchestrator lifecycle concern, not a subagent work-behavior concern.
  - ADR states that detailed runtime behavior belongs behind progressive-disclosure references.
  - ADR states that runtime loaders may route the main-thread agent into `$orchestration-harness` without selecting a physical Orchestrator agent.
  - ADR states that once `$orchestration-harness` is loaded for a coding task, the current main-thread agent assumes the logical Orchestrator role.
  - ADR states that the Orchestrator performs a minimal repository rule load when `docs/coding-agent/rules/index.md` is present: `common.md` and `orchestrator.md`.
  - ADR distinguishes minimal rule instruction loading from lifecycle/readiness/bootstrap/refresh work.
  - ADR confirms Codex `AGENTS.md` remains loader-only.
- validation:
  - kind: review
    required: true
    owner: orchestrator
    detail: "Compare ADR-D-0008 style and content against existing ADR-D records plus ADR-D-0001 and ADR-I-0002."

### Task_2: Add Orchestrator Identity, Repository Rule Entry, And Async Hook
- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/SKILL.md`
- depends_on: [Task_1]
- description: |
  Clarify near the top that the current main-thread agent assumes the logical Orchestrator role when the skill is loaded by a runtime loader or skill reference. Add a minimal Repository Rule Entry section before detailed gates or repository exploration rules. Add a short runtime-neutral pointer near Worker dispatch guidance that routes async/background runtime mechanics to the subagent-strategy reference.
- acceptance:
  - Skill clarifies that sessions routed by a runtime loader or skill reference, including Codex sessions routed by the managed `AGENTS.md` loader, assume the logical Orchestrator role.
  - Skill adds Repository Rule Entry before detailed gates or repository exploration rules.
  - Repository Rule Entry checks for `docs/coding-agent/rules/index.md`.
  - When the suite is present, Repository Rule Entry reads `docs/coding-agent/rules/common.md` and `docs/coding-agent/rules/orchestrator.md` for the current main-thread role.
  - Repository Rule Entry explicitly treats this as rule instruction loading, not full rule-suite readiness work.
  - Repository Rule Entry keeps `_lifecycle.json`, bootstrap, refresh, repair, and `rulebook` behind Rule Suite Fast Path or task-specific lifecycle triggers.
  - Rule Suite Fast Path wording is adjusted if needed to distinguish minimal rule instruction loading from lifecycle/readiness/bootstrap/refresh work.
  - Hook appears near dispatch guidance, ideally after the existing parallel Worker dispatch sentence.
  - Hook names `subagent-strategy/references/async-dispatch-lifecycle.md`.
  - Hook remains concise and does not duplicate lifecycle mechanics.
- validation:
  - kind: review
    required: true
    owner: orchestrator
    detail: "Confirm top-level orchestration skill receives concise identity/rule-entry guidance and only a small progressive-disclosure async hook."

### Task_3: Add Async Dispatch Lifecycle Reference
- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/subagent-strategy/references/async-dispatch-lifecycle.md`
  - `plugins/coding-agent-orchestration-harness/skills/subagent-strategy/SKILL.md`
- depends_on: [Task_2]
- description: |
  Add the Orchestrator-owned async/background lifecycle reference and route to it from the subagent-strategy progressive-disclosure list.
- acceptance:
  - Reference states when to use it: runtimes launching Researcher/Worker/Reviewer asynchronously or as background processes.
  - Reference describes parent-owned lifecycle: dispatch, track, wait, integrate, close/terminate when supported.
  - Reference defines active dispatch state fields, statuses, and cleanup status.
  - Reference instructs that no report yet means running, not failed.
  - Reference prohibits prompting for immediate final reports right after dispatch.
  - Reference prohibits duplicating active child work unless cancelled, blocked, or reassigned.
  - Reference describes cleanup after final report validation/integration.
  - `subagent-strategy/SKILL.md` links to the new reference without expanding lifecycle detail inline.
- validation:
  - kind: review
    required: true
    owner: orchestrator
    detail: "Confirm lifecycle details live in the new reference and the main skill only routes to it."

### Task_4: Add Wave Cleanup Step
- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/wave-integration/SKILL.md`
- depends_on: [Task_3]
- description: |
  Add one concise checklist item making completed async/background child cleanup an Orchestrator-owned wave lifecycle responsibility.
- acceptance:
  - Checklist instructs closing or terminating completed async/background subagent processes after final reports are validated and integrated.
  - Checklist covers runtimes without close/terminate support by recording cleanup unavailable.
  - Checklist says not to reuse completed processes for unrelated work when cleanup is unavailable.
- validation:
  - kind: review
    required: true
    owner: orchestrator
    detail: "Confirm wave-integration owns the cleanup checklist item without adding unrelated workflow detail."

### Task_5: Update Codex Loader Authorization
- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/codex/snippets/AGENTS.md`
- depends_on: [Task_2]
- description: |
  Add one loader-level sentence authorizing bounded harness-required subagent dispatch when `$orchestration-harness` requires it, unless the user disables subagents.
- acceptance:
  - Loader explicitly treats use of the managed loader for a coding task as user direction to follow harness workflow, including bounded subagent dispatch.
  - Loader remains loader-only.
  - Loader does not duplicate role details, schemas, gates, validation mechanics, rule-loading details, or async lifecycle details.
  - Loader does not add Orchestrator, Researcher, Worker, Reviewer, `Task_X`, plan gates, validation gates, report contracts, or repository-rule entry wording for the addendum.
- validation:
  - kind: review
    required: true
    owner: orchestrator
    detail: "Confirm Codex loader remains concise and does not copy canonical workflow mechanics."

### Task_6: Validation And Closeout
- type: test
- owns: []
- depends_on: [Task_1, Task_2, Task_3, Task_4, Task_5]
- description: |
  Run package validation and smoke tests. Do not add a Codex loader duplication validator in this task; verify loader-only behavior by review and existing package validation.
- acceptance:
  - No hard exact-wording validator is added.
  - No hard validator locks the new reference to an unstable path unless that path is already part of a durable contract.
  - No validator requires the exact Repository Rule Entry section title.
  - No validator requires an ADR-D-0009 filename because the addendum is planned for ADR-D-0008.
  - No warning-only Codex loader duplication guard is added in this task.
  - Validation output is captured for final reporting.
  - Any progressive-disclosure candidates found in `orchestration-harness/SKILL.md` are reported, not refactored.
- validation:
  - kind: command
    required: true
    owner: orchestrator
    detail: "From plugins/coding-agent-orchestration-harness: python scripts/validate_harness_package.py"
  - kind: command
    required: true
    owner: orchestrator
    detail: "From plugins/coding-agent-orchestration-harness: python scripts/run_validation_smoke_tests.py"
  - kind: review
    required: true
    owner: orchestrator
    detail: "Confirm Codex TOML subagent templates were not changed for idle-open process behavior."

## Task Waves (explicit parallel dispatch sets)

Interpretation:
- Tasks listed in the same wave are intended to be dispatched in parallel by default,
  when `owns` are disjoint and dependencies are met.
- Waves are executed sequentially.

- Wave 1 (parallel): [Task_1]
- Wave 2 (parallel): [Task_2, Task_5]
- Wave 3 (parallel): [Task_3]
- Wave 4 (parallel): [Task_4]
- Wave 5 (parallel): [Task_6]

## E2E / Visual Validation Spec

- provider: n/a
- artifact_root: n/a
- base_url: n/a
- app_start_command: n/a
- readiness_check: n/a
- flows: n/a
- viewports: n/a
- evidence_requirements: n/a
- known_flakiness: n/a

## Rollback / Safety
- Revert the documentation files and any optional validator warning change in one patch if validation exposes a design issue.
- Do not modify Codex TOML templates for this issue.
- Do not add hard phrase validators, so rollback should not affect package validation policy.
- Do not add a loader-duplication warning validator in this task; revisit only if duplication recurs or a durable structural marker emerges.
- Keep Codex loader-only architecture intact; put runtime-loader identity and repository-rule entry behavior in `orchestration-harness/SKILL.md`.

## Progress Log (append-only)

- 2026-05-17 Draft plan created.
  - Summary: Captured implementation tasks, ownership boundaries, validation commands, and non-goals.
  - Validation evidence: pending.
  - Notes: Branch checked out as `codex-async-subagent-lifecycle`.
- 2026-05-17 Plan updated with runtime-loader identity addendum.
  - Summary: Folded Orchestrator identity and minimal repository-rule entry into ADR-D-0008 and Task_2; kept Codex loader-only constraint explicit.
  - Validation evidence: pending.
  - Notes: Repository rules `index.md`, `common.md`, and `orchestrator.md` were present and consulted.
- 2026-05-17 Open question resolved.
  - Summary: Accepted recommendation to skip a Codex loader duplication validator in this task and use review plus existing validation instead.
  - Validation evidence: pending.
  - Notes: ADR-D-0008 remains planned as `status: accepted`.
- 2026-05-17 Implementation completed.
  - Summary: Added ADR-D-0008, Orchestrator identity/rule-entry wording, async dispatch lifecycle reference, wave cleanup checklist item, and Codex loader authorization sentence.
  - Validation evidence: `python scripts/validate_harness_package.py` passed; `python scripts/run_validation_smoke_tests.py` passed; plan validation passed; `git diff --check` passed.
  - Notes: No Codex subagent TOML templates or package validator files were changed.
- 2026-05-17 Reviewer validation completed.
  - Summary: Reviewer `Rawls` returned `APPROVED_WITH_NOTES` with no findings.
  - Validation evidence: Reviewer independently confirmed `validate_harness_package.py`, `run_validation_smoke_tests.py`, and `git diff --check` passed.
  - Notes: Reviewer child process was closed after report integration.

## Decision Log (append-only; re-plans and major discoveries)

- 2026-05-17 Decision:
  - Trigger / new insight: The requested `codex/` branch prefix could not be created in this sandbox, so a flat Codex-named branch was used.
  - Plan delta (what changed): Work branch is `codex-async-subagent-lifecycle`.
  - Tradeoffs considered: Preserves isolated branch workflow while avoiding the ref creation failure.
  - User approval: implicit for branch creation; branch name adjusted due local Git ref creation failure.
- 2026-05-17 Decision:
  - Trigger / new insight: Addendum requested runtime-loader Orchestrator identity and repository-rule entry, and asked to prefer inclusion in the planned ADR.
  - Plan delta (what changed): ADR-D-0008 now includes a related runtime-loader identity and minimal repository-rule entry decision point; no ADR-D-0009 is planned.
  - Tradeoffs considered: Keeps related Codex loader behavior in one planned decision record while preserving ADR-D-0001 and ADR-I-0002 boundaries.
  - User approval: yes.
- 2026-05-17 Decision:
  - Trigger / new insight: User accepted recommendation on open questions.
  - Plan delta (what changed): Removed the optional validator question; Task_6 now explicitly avoids adding a Codex loader duplication validator.
  - Tradeoffs considered: Review-only enforcement avoids brittle prose checks while preserving acceptance criteria for loader-only behavior.
  - User approval: yes.
- 2026-05-17 Decision:
  - Trigger / new insight: Current runtime tool policy permits spawning subagents only when the user explicitly asks for subagents, delegation, or parallel agent work.
  - Plan delta (what changed): Independent Reviewer subagent was waived; Orchestrator performed direct diff review against acceptance criteria and validation evidence.
  - Tradeoffs considered: Preserves higher-priority runtime constraints while still completing review by explicit acceptance checks and repository validation.
  - User approval: no, Orchestrator waiver.
- 2026-05-17 Decision:
  - Trigger / new insight: User clarified that the planned harness wording should authorize dispatch and instructed continuing from here under dispatch rules.
  - Plan delta (what changed): Reviewer dispatch waiver was superseded by explicit Reviewer dispatch; `Rawls` reviewed the draft implementation.
  - Tradeoffs considered: Keeps existing draft edits while restoring harness review flow before closeout.
  - User approval: yes.

## Notes
- Risks:
  - Over-expanding `orchestration-harness/SKILL.md` would violate the progressive-disclosure architecture.
  - Adding validators for exact wording would make ordinary documentation evolution brittle.
  - Editing Codex subagent templates would put lifecycle responsibility in the wrong layer.
  - Putting repository rule-loading details in the Codex loader would violate the loader-only architecture.
- Edge cases:
  - Runtimes without close/terminate actions should record cleanup as unavailable.
  - An async child with no final report yet should remain `running` until a dependency boundary or runtime polling requirement is reached.
  - Minimal repository rule loading should not read `_lifecycle.json` or trigger rulebook unless lifecycle/readiness work is independently required.
