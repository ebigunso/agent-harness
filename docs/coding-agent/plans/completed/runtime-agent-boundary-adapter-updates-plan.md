# Plan: Runtime Agent Boundary And Adapter Updates

- status: done
- generated: 2026-05-14
- last_updated: 2026-05-14
- work_type: docs

## Goal

- Align runtime Reviewer/Researcher guidance and adapters with the new lesson targets, harness migration staging route, and no-direct-bundled-edit boundary.

## Definition of Done

- Reviewer and Researcher guidance no longer names `references/*` or `global-skill` as lesson promotion targets.
- Runtime adapters explain `harness_migration` as the route for cross-repo improvements staged in `docs/coding-agent/skill-candidates.md` or `skill-drafts`.
- Ordinary target-repository work is explicitly barred from editing bundled harness skills, references, agents, validators, or plugin files.
- Copilot, Claude, and Codex runtime adapter surfaces remain concise and consistent.

## Scope / Non-goals

- Scope:
  - Update first-party runtime agent docs and adapter templates that mention report schemas, lesson targets, or direct bundled edits.
  - Align adapter language with the report schema and improvement-loop model.
- Non-goals:
  - Do not modify the report validator; that is covered by Report Schema Split.
  - Do not change runtime role identities, tool permissions, or bootstrap install behavior.
  - Do not add new skills or references.

## Context (workspace)

- Related files/areas:
  - `plugins/coding-agent-orchestration-harness/agents/Reviewer.md`
  - `plugins/coding-agent-orchestration-harness/agents/Worker.md`
  - `plugins/coding-agent-orchestration-harness/agents/Orchestrator.md`
  - `plugins/coding-agent-orchestration-harness/claude/agents/harness-reviewer.md`
  - `plugins/coding-agent-orchestration-harness/claude/agents/harness-worker.md`
  - `plugins/coding-agent-orchestration-harness/claude/agents/harness-orchestrator.md`
  - `plugins/coding-agent-orchestration-harness/codex/agent-templates/harness_reviewer.toml`
  - `plugins/coding-agent-orchestration-harness/codex/agent-templates/harness_worker.toml`
  - `plugins/coding-agent-orchestration-harness/codex/agent-templates/harness_researcher.toml`
  - `plugins/coding-agent-orchestration-harness/skills/runtime-adapter-contract/references/adapter-maintenance-checklist.md`
- Existing patterns or references:
  - Runtime adapters should stay short and route to shared skills/references.
  - Shared semantics live in skills and references, not duplicated in every adapter.
- Repo reference docs consulted:
  - `docs/coding-agent/plans/completed/runtime-adapter-alignment-plan.md`

## Open Questions (max 3)

- Q1: resolved. Researcher adapters should receive boundary wording only if they currently mention promotion, lessons, reports, or bundled edits; otherwise leave them alone.

## Assumptions

- A1: This plan runs after Report Schema Split and Lessons And Improvement Loop Promotion Model, so adapters can point to already-updated shared guidance.
- A2: Adapter updates should be minimal and avoid copying schema blocks where a skill reference already owns the detailed contract.
- A3: Runtime agents may read bundled harness guidance, but ordinary target-repo work should stage changes in repo docs instead of editing plugin files.

Required-check waiver
- What is waived: Separate Reviewer-owned validation evidence for Task_5.
- Why waived now: This desktop session did not use a separate Reviewer subagent, and the change is prompt/documentation text with package validation and direct acceptance-criteria review available.
- Risk accepted and impact: A second reviewer might have caught wording drift or prompt-budget issues that Orchestrator review missed.
- Mitigation and follow-up: Orchestrator performed strict diff review, stale-token searches, completed-plan validation, package validation, and `git diff --check`; future runtime adapter changes should use independent Reviewer validation when available.
- Owner and expiration: Orchestrator; expires after this completed plan is superseded by a future runtime-adapter update.

## Tasks

### Task_1: Locate Runtime Schema And Promotion Mentions

- type: research
- owns: []
- depends_on: []
- description: |
  Search runtime agent docs and adapter templates for stale lesson targets, direct bundled edit guidance, and report schema copies.
- acceptance:
  - Search covers `agents/`, `claude/agents/`, `codex/agent-templates/`, and runtime-adapter references.
  - Findings identify every occurrence of `global-skill`, `references/*`, `intended_home`, `global_candidate`, first-party skill/reference promotion, and direct bundled edit guidance.
  - Findings distinguish required edits from harmless historical text, if any.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "Run `rg \"global-skill|references/\\*|intended_home|global_candidate|first-party skill|first-party reference\" plugins/coding-agent-orchestration-harness/agents plugins/coding-agent-orchestration-harness/claude/agents plugins/coding-agent-orchestration-harness/codex/agent-templates plugins/coding-agent-orchestration-harness/skills/runtime-adapter-contract`."

### Task_2: Update Core Runtime Agent Guidance

- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/agents/Reviewer.md`
  - `plugins/coding-agent-orchestration-harness/agents/Worker.md`
  - `plugins/coding-agent-orchestration-harness/agents/Orchestrator.md`
- depends_on: [Task_1]
- description: |
  Update core runtime role docs with the new lesson targets and harness migration staging boundary where applicable.
- acceptance:
  - Reviewer output guidance uses `promotion_target: repo_rule | harness_migration | troubleshooting | residual_risk`.
  - Reviewer guidance explains that `harness_migration` stages cross-repo improvements in `docs/coding-agent/skill-candidates.md` or `docs/coding-agent/skill-drafts/`.
  - Worker report guidance routes detailed schema ownership to `subagent-report-contract` and does not preserve stale fields.
  - Orchestrator guidance says ordinary target-repo work must stage cross-repo harness improvements instead of editing bundled plugin content.
  - Core runtime docs contain no stale `global-skill`, `references/*`, `intended_home`, or `global_candidate` routing.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "Run targeted `rg` checks in `agents/` for stale routing tokens after edits."
  - kind: review
    required: true
    owner: worker
    detail: "Confirm role authority is unchanged: Reviewer remains review-only, Worker owns assigned Task_X only, Orchestrator owns integration."

### Task_3: Update Claude And Codex Adapter Templates

- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/claude/agents/harness-reviewer.md`
  - `plugins/coding-agent-orchestration-harness/claude/agents/harness-worker.md`
  - `plugins/coding-agent-orchestration-harness/claude/agents/harness-orchestrator.md`
  - `plugins/coding-agent-orchestration-harness/codex/agent-templates/harness_reviewer.toml`
  - `plugins/coding-agent-orchestration-harness/codex/agent-templates/harness_worker.toml`
  - `plugins/coding-agent-orchestration-harness/codex/agent-templates/harness_researcher.toml`
- depends_on: [Task_2]
- description: |
  Align runtime-specific adapters with the core guidance while keeping adapter bodies compact.
- acceptance:
  - Adapters do not mention removed lesson targets or `intended_home`.
  - Adapters use shared skill routing instead of duplicating full schema details.
  - Any boundary wording is concise and consistent across runtimes.
  - No adapter instructs ordinary target-repo agents to edit bundled harness files.
  - Researcher adapter remains unchanged unless Task_1 finds stale promotion or direct edit wording.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "Run targeted `rg` checks in Claude and Codex adapters for stale routing tokens."
  - kind: review
    required: true
    owner: reviewer
    detail: "Review adapters against runtime-adapter-contract prompt budgeting guidance."

### Task_4: Update Adapter Maintenance Guidance If Needed

- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/runtime-adapter-contract/references/adapter-maintenance-checklist.md`
  - `plugins/coding-agent-orchestration-harness/skills/runtime-adapter-contract/SKILL.md`
- depends_on: [Task_3]
- description: |
  Add or adjust adapter maintenance guidance only if implementation finds the runtime boundary is not already represented in shared adapter maintenance rules.
- acceptance:
  - Adapter maintenance guidance tells maintainers to keep schema semantics in shared skills/references.
  - Adapter maintenance guidance avoids direct ordinary-runtime bundled edit instructions.
  - No change is made if existing guidance already covers the concern.
- validation:
  - kind: review
    required: true
    owner: worker
    detail: "Record whether runtime-adapter-contract changed and why."

### Task_5: Final Runtime Adapter Consistency Review

- type: review
- owns: []
- depends_on: [Task_2, Task_3, Task_4]
- description: |
  Review runtime guidance and adapters for consistency with the new schema and staging model.
- acceptance:
  - All runtime surfaces use the new promotion target enum.
  - `harness_migration` is explained as staging, not direct bundled edits.
  - Runtime adapters remain compact and do not duplicate shared contract content.
  - Existing package validation passes.
- validation:
  - kind: command
    required: true
    owner: reviewer
    detail: "Run `python plugins/coding-agent-orchestration-harness/scripts/validate_harness_package.py` or review equivalent Worker evidence."
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review against this plan and runtime-adapter-contract guidance."

## Task Waves (explicit parallel dispatch sets)

- Wave 1 (parallel): [Task_1]
- Wave 2 (parallel): [Task_2]
- Wave 3 (parallel): [Task_3]
- Wave 4 (parallel): [Task_4]
- Wave 5 (parallel): [Task_5]

## E2E / Visual Validation Spec

- Not applicable. This plan changes runtime guidance and adapter text only.

## Rollback / Safety

- Revert adapter and runtime guidance changes together if they conflict with the updated report contract.
- Do not restore old promotion target names once Report Schema Split has landed.

## Progress Log (append-only)

- 2026-05-14 Plan drafted.
  - Summary: Added implementation plan for runtime adapter schema alignment and ordinary-runtime bundled edit boundary.
  - Validation evidence: Plan-format self-check.
  - Notes: Awaiting approval before execution.
- 2026-05-14 Waves 1-4 completed: [Task_1, Task_2, Task_3, Task_4]
  - Summary: Updated Reviewer and Researcher runtime surfaces across Copilot, Claude, and Codex templates to use new lesson targets and staged harness migration wording.
  - Validation evidence: Runtime stale-token search for old promotion targets returned no matches.
  - Notes: Researcher wording changed only because Researcher already emitted lesson and skill-candidate suggestions.
- 2026-05-14 Wave 5 completed: [Task_5]
  - Summary: Strict runtime adapter consistency review completed by Orchestrator.
  - Validation evidence: `python plugins\coding-agent-orchestration-harness\scripts\validate_harness_package.py` passed; `git diff --check` passed.
  - Notes: Required independent Reviewer validation was waived by Orchestrator for this branch because the review scope is prompt text only and the follow-up review pass was performed directly against the plan acceptance criteria.

## Decision Log (append-only; re-plans and major discoveries)

- 2026-05-14 Decision: Keep adapters concise and reference shared contract ownership.
  - Trigger / new insight: Runtime adapters already rely on shared skills for detailed behavior.
  - Plan delta (what changed): Adapter tasks focus on stale-token removal and compact boundary wording.
  - Tradeoffs considered: Duplicating full schema blocks would reduce ambiguity but create drift risk.
- 2026-05-14 Decision: Do not add Researcher boundary wording unless Researcher surfaces already touch promotion or bundled edits.
  - Trigger / new insight: Researcher adapters should not grow prompt text for symmetry alone.
  - Plan delta (what changed): Researcher adapter edits are conditional on Task_1 finding relevant stale wording.
  - Tradeoffs considered: Symmetric wording is easier to audit but increases adapter noise when the role does not emit lessons or promotions.
  - User approval: yes.
- 2026-05-14 Decision: Waive separate Reviewer subagent validation for this branch.
  - Trigger / new insight: The branch updates runtime prompt text only, and no separate Reviewer subagent was available in this desktop session.
  - Plan delta (what changed): Task_5 was completed with Orchestrator-owned strict review evidence instead of a separate Reviewer report.
  - Tradeoffs considered: Independent Reviewer evidence would be stronger, but the branch also has package validation, stale-token searches, and direct acceptance-criteria review.
  - User approval: no; Orchestrator waiver recorded.

## Notes

- Risks:
  - Stale schema fragments may exist in runtime-specific templates outside obvious Reviewer files.
  - Package validation guards for stale tokens are intentionally deferred until the final guard plan.
- Edge cases:
  - Explicit harness-maintenance work in this repository may edit bundled files; ordinary target-repo work should not.
