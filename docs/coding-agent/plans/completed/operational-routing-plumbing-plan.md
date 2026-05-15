# Plan: Operational Routing Plumbing

- status: done
- generated: 2026-05-16
- last_updated: 2026-05-16
- work_type: docs

## Goal
- Route the new latent-risk review lenses and `harness_migration_candidates` through the operational surfaces that shape runtime Reviewer and Orchestrator behavior.

## Definition of Done
- Reviewer packet routing hints include the newer latent-risk categories.
- Reviewer latent-risk prompt snippet matches the current router vocabulary.
- Wave integration aggregates and routes `harness_migration_candidates`.
- Researcher HMC suggestion shape includes `id` and `rationale` across generic, Claude, and Codex adapters.
- Required validation passes or is explicitly waived with evidence.

## Scope / Non-goals
- Scope:
  - `plugins/coding-agent-orchestration-harness/skills/wave-integration/references/reviewer-packet-template.md`
  - `plugins/coding-agent-orchestration-harness/skills/subagent-strategy/references/prompt-snippets.md`
  - `plugins/coding-agent-orchestration-harness/skills/wave-integration/references/integration-checklist.md`
  - `plugins/coding-agent-orchestration-harness/skills/wave-integration/SKILL.md`
  - `plugins/coding-agent-orchestration-harness/agents/Researcher.md`
  - `plugins/coding-agent-orchestration-harness/claude/agents/harness-researcher.md`
  - `plugins/coding-agent-orchestration-harness/codex/agent-templates/harness_researcher.toml`
- Non-goals:
  - Do not change latent-risk reference substance; that is covered by the latent-risk hardening plan.
  - Do not change validators; that is covered by the enforcement and closeout schema plan.
  - Do not edit repository rule files.

## Context (workspace)
- Related files/areas:
  - `plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/review-latent-risk.md`
  - `plugins/coding-agent-orchestration-harness/skills/subagent-report-contract/SKILL.md`
  - `plugins/coding-agent-orchestration-harness/skills/subagent-report-contract/scripts/validate_worker_report.py`
- Existing patterns or references:
  - Runtime adapters should route to shared skills/references rather than inline full checklists.
  - `rule_candidates` are repo-local; `harness_migration_candidates` are staged for later harness-maintenance work.
- Repo reference docs consulted:
  - `docs/coding-agent/rules/index.md`
  - `docs/coding-agent/rules/common.md`
  - `docs/coding-agent/rules/orchestrator.md`
  - `docs/coding-agent/rules/worker.md`

## Open Questions (max 3)
- Q1: None.

## Assumptions
- A1: The supplied implementation notes accurately reflect the intended vocabulary for new latent-risk routing.
- A2: Researcher HMC suggestions should mirror Worker schema shape for curation consistency even though Researcher output is not machine-validated as Worker YAML.

## Tasks

### Task_1: Update Reviewer Packet Latent-Risk Routing Hints
- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/wave-integration/references/reviewer-packet-template.md`
- depends_on: []
- description: |
  Add packet template sections for public API compatibility, entrypoint admission, diagnostics, build/CI, collection semantics, and runtime model compatibility.
- acceptance:
  - Packet template includes routing blocks for all six newer categories.
  - Each new block includes plugin skill, reference, repo reviewer hotspot, required evidence, and applicability rationale placeholders.
  - Existing older category blocks remain intact.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "rg -n \"review-latent-risk-public-api|review-latent-risk-entrypoints-admission|review-latent-risk-diagnostics|review-latent-risk-build-ci|Collection semantics|Runtime model compatibility\" plugins/coding-agent-orchestration-harness/skills/wave-integration/references/reviewer-packet-template.md"
  - kind: review
    required: true
    owner: reviewer
    detail: "Confirm packet routing hints are concise dispatch aids and do not inline full latent-risk checklists."

### Task_2: Refresh Reviewer Latent-Risk Prompt Snippet
- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/subagent-strategy/references/prompt-snippets.md`
- depends_on: []
- description: |
  Update the reusable Reviewer latent-risk snippet so it names the current router vocabulary and instructs Reviewers to read only matching conditional references.
- acceptance:
  - Snippet mentions public API, diagnostics, build cfg/features or strict-CI, entrypoint intent/admission, collection semantics, and runtime model compatibility.
  - Snippet keeps the rules to read the router first, then only matching conditional references.
  - Snippet still prohibits printing full checklists and irrelevant `N/A` criteria.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "rg -n \"public API|diagnostics|build cfg/features|strict-CI|entrypoint intent|collection semantics|runtime model compatibility|Do not report irrelevant\" plugins/coding-agent-orchestration-harness/skills/subagent-strategy/references/prompt-snippets.md"
  - kind: review
    required: true
    owner: reviewer
    detail: "Confirm snippet vocabulary matches `review-latent-risk.md` without duplicating the conditional reference content."

### Task_3: Wire Harness Migration Candidates Through Wave Integration
- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/wave-integration/references/integration-checklist.md`
  - `plugins/coding-agent-orchestration-harness/skills/wave-integration/SKILL.md`
- depends_on: []
- description: |
  Update wave integration checklist section 6 and the core SKILL checklist item so Orchestrator integration collects, dedupes, and stages `harness_migration_candidates`.
- acceptance:
  - Integration checklist section 6 title and bullets include rule, lesson, and harness migration candidates.
  - Checklist explicitly routes HMCs to `docs/coding-agent/skill-candidates.md` or `docs/coding-agent/skill-drafts/*.md` through Orchestrator curation.
  - `wave-integration/SKILL.md` core checklist item 6 mentions `harness_migration_candidates`.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "rg -n \"harness_migration_candidates|skill-candidates.md|skill-drafts\" plugins/coding-agent-orchestration-harness/skills/wave-integration"
  - kind: review
    required: true
    owner: reviewer
    detail: "Confirm HMC routing does not imply Workers directly edit bundled harness skills or validators."

### Task_4: Normalize Researcher HMC Suggestion Shape
- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/agents/Researcher.md`
  - `plugins/coding-agent-orchestration-harness/claude/agents/harness-researcher.md`
  - `plugins/coding-agent-orchestration-harness/codex/agent-templates/harness_researcher.toml`
- depends_on: []
- description: |
  Update the optional Researcher HMC suggestion section to include `id` and `rationale`, and mirror the shape in Claude and Codex Researcher adapters.
- acceptance:
  - Generic Researcher section includes `id: HMC-YYYYMMDD-short-kebab-description`.
  - Generic, Claude, and Codex Researcher instructions include `rationale`.
  - All three surfaces keep the prohibition on editing bundled harness skills, references, agents, validators, or plugin files during ordinary target-repository research.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "rg -n \"HMC-YYYYMMDD-short-kebab-description|rationale|Do not edit bundled harness\" plugins/coding-agent-orchestration-harness/agents/Researcher.md plugins/coding-agent-orchestration-harness/claude/agents/harness-researcher.md plugins/coding-agent-orchestration-harness/codex/agent-templates/harness_researcher.toml"
  - kind: review
    required: true
    owner: reviewer
    detail: "Confirm Researcher shape is consistent across runtime adapters and remains suggestion-only."

## Task Waves (explicit parallel dispatch sets)

Interpretation:
- Tasks listed in the same wave are intended to be dispatched in parallel by default when `owns` are disjoint and dependencies are met.
- Waves are executed sequentially.

- Wave 1 (parallel): [Task_1, Task_2, Task_3, Task_4]

## E2E / Visual Validation Spec

- Not applicable; no UI or user flow is impacted.

## Rollback / Safety
- Revert only the files listed in each task's `owns` scope.
- If terminology conflicts with the router or Worker report schema, pause and replan before widening scope.

## Progress Log (append-only)

- 2026-05-16 00:00 Plan drafted.
  - Summary: Created scoped implementation plan for routing and wave integration gaps.
  - Validation evidence: Not run; draft plan only.
  - Notes: Research waived because the user supplied current-file findings and work is limited to plan creation.

- 2026-05-16 00:00 Wave 1 completed: [Task_1, Task_2, Task_3, Task_4]
  - Summary: Updated Reviewer packet routing hints, Reviewer latent-risk snippet vocabulary, wave integration HMC collection, and Researcher HMC suggestion shape across generic, Claude, and Codex surfaces.
  - Validation evidence: Targeted `rg` checks passed for packet references, prompt snippet vocabulary, wave integration HMC routing, and Researcher HMC fields; `python scripts/validate_harness_package.py` passed from `plugins/coding-agent-orchestration-harness/`; `git diff --check` passed.
  - Notes: No UI/E2E validation required.

## Decision Log (append-only; re-plans and major discoveries)

- 2026-05-16 00:00 Decision: Split operational routing from latent-risk substance and validator enforcement.
  - Trigger / new insight: User requested plans split by logical boundaries.
  - Plan delta (what changed): This plan owns runtime routing/plumbing only.
  - Tradeoffs considered: Keeping all suggestions in one plan would make validation and review ownership too broad.
  - User approval: yes, user requested actual plan files after reviewing the split.

## Notes
- Risks:
  - Prompt snippets can become too broad if they inline checklist content.
  - Runtime adapter wording can drift if only the generic Researcher is updated.
- Edge cases:
  - If Codex TOML escaping makes multiline wording awkward, preserve semantic parity rather than exact formatting.
