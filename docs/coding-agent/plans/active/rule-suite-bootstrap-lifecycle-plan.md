# Plan: Rule Suite Bootstrap Lifecycle

- status: draft
- generated: 2026-05-13
- last_updated: 2026-05-13
- work_type: mixed

## Goal
- Implement the repository rule-suite bootstrap lifecycle described in the user-provided plan and ADR draft, using the current `plugins/coding-agent-orchestration-harness/` structure.

## Definition of Done
- The rulebook defines a full six-file rule suite with `reviewer.md` and `_lifecycle.json`.
- Orchestrator, Researcher, Worker, Reviewer, planning, dispatch, packet, report-contract, and quality-baseline guidance are updated consistently.
- Package validation checks structure without enforcing exact prose.
- ADR-D-0006 is added under the existing decisions directory.
- Required plugin validators pass from `plugins/coding-agent-orchestration-harness/`.

## Scope / Non-goals
- Scope:
  - Update harness skills, runtime adapters, fixtures, package validators, and ADR documentation.
  - Keep changes instructional and repo-adaptive.
- Non-goals:
  - Do not add a universal quality-gate runner for arbitrary repositories.
  - Do not require full rule bootstrap or lifecycle freshness discovery at every task start.
  - Do not inline the full lifecycle or latent-risk checklists into runtime adapters.

## Context (workspace)
- Related files/areas:
  - `plugins/coding-agent-orchestration-harness/skills/`
  - `plugins/coding-agent-orchestration-harness/agents/`
  - `plugins/coding-agent-orchestration-harness/claude/agents/`
  - `plugins/coding-agent-orchestration-harness/codex/agent-templates/`
  - `plugins/coding-agent-orchestration-harness/scripts/`
  - `plugins/coding-agent-orchestration-harness/tests/fixtures/`
  - `docs/coding-agent-orchestration-harness/decisions/`
- Existing patterns or references:
  - ADR front matter in `docs/coding-agent-orchestration-harness/decisions/ADR-D-0005-runtime-prompt-budgeting.md`.
  - Validator commands documented in `plugins/coding-agent-orchestration-harness/README.md`.
  - Current repo rules are the older `index.md`, `common.md`, `worker.md`, `orchestrator.md` shape.
- Repo reference docs consulted:
  - `docs/coding-agent/rules/index.md`
  - `docs/coding-agent/rules/common.md`
  - `docs/coding-agent/rules/orchestrator.md`
  - `plugins/coding-agent-orchestration-harness/README.md`
  - `plugins/coding-agent-orchestration-harness/skills/rulebook/SKILL.md`
  - `plugins/coding-agent-orchestration-harness/skills/rulebook/references/rules-files.md`
  - `docs/coding-agent-orchestration-harness/decisions/ADR-D-0005-runtime-prompt-budgeting.md`

## Plan Validity Check
- The provided implementation plan is valid against the current repository structure.
- The ADR target path is valid and follows the current ADR naming and front matter style.
- The plan correctly identifies that Reviewer adapters currently consult only `common.md`.
- The plan correctly identifies that Worker report audience currently excludes `reviewer`.
- Local adjustment: include `plugins/coding-agent-orchestration-harness/skills/subagent-report-contract/references/schema.yaml` in Task_5 because it also encodes the old `common|worker|orchestrator` audience shape.
- Local note: `docs/coding-agent/rules/` is currently untracked in this checkout; implementation should avoid treating those files as committed baseline unless explicitly staged later.

## Open Questions (max 3)
- Q1: None.

## Assumptions
- A1: The user-provided ADR date `2026-05-12` should be preserved in ADR-D-0006.
- A2: New rulebook lifecycle references should be instructional documentation, not executable bootstrap automation in this pass.
- A3: Package validation should remain structure-oriented and should not validate exact prompt or template wording.

## Tasks

### Task_1: Define the Full Rule Suite in Rulebook
- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/rulebook/SKILL.md`
  - `plugins/coding-agent-orchestration-harness/skills/rulebook/references/rules-files.md`
  - `plugins/coding-agent-orchestration-harness/skills/rulebook/references/bootstrap-lifecycle.md`
  - `plugins/coding-agent-orchestration-harness/skills/rulebook/references/rule-suite-templates.md`
  - `plugins/coding-agent-orchestration-harness/skills/rulebook/references/lifecycle-sidecar.md`
- depends_on: []
- description: |
  Expand rulebook from three role files plus index into the full rule suite lifecycle owner.
  Add full bootstrap, schema migration, targeted refresh, repair, templates, and lifecycle sidecar guidance.
- acceptance:
  - `rules-files.md` requires `index.md`, `common.md`, `worker.md`, `orchestrator.md`, `reviewer.md`, and `_lifecycle.json`.
  - `reviewer.md` is required, not optional.
  - `index.md` is documented as low-token routing and the bootstrap success marker.
  - `_lifecycle.json` is documented as rarely read machine lifecycle data.
  - Full bootstrap, schema migration, targeted refresh, and repair are distinct.
  - No rulebook workflow requires full bootstrap at every task start.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Review rulebook files against Task_1 acceptance and prompt-budget constraints."

### Task_2: Add Rule Suite Fast Path to Orchestrator Policy
- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/SKILL.md`
- depends_on: [Task_1]
- description: |
  Add the Rule Suite Fast Path and update relevant gates so rule readiness is lazy, derived, and routed through rulebook.
- acceptance:
  - The policy avoids per-task full bootstrap.
  - Trivial work can skip rule-readiness checks unless touching rule or lifecycle source paths.
  - Non-trivial work uses repo rules when relevant for planning, validation, review, or repo constraints.
  - Missing, corrupt, schema-mismatched, or drifted rules route through rulebook operations.
  - `_lifecycle.json` is only read for lifecycle work.
  - Closeout requires targeted refresh or a waiver when rule-source files changed.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Review Orchestrator policy for consistency with rulebook lifecycle and existing hard gates."

### Task_3: Update Reviewer Adapters for Reviewer Rules
- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/agents/Reviewer.md`
  - `plugins/coding-agent-orchestration-harness/claude/agents/harness-reviewer.md`
  - `plugins/coding-agent-orchestration-harness/codex/agent-templates/harness_reviewer.toml`
- depends_on: [Task_1]
- description: |
  Update Reviewer runtime adapters to consult `common.md` and `reviewer.md`, and broaden latent-risk routing triggers without inlining the checklist.
- acceptance:
  - All Reviewer adapters mention `docs/coding-agent/rules/reviewer.md`.
  - Adapter text remains compact.
  - Adapters route latent-risk review to `engineering-quality-baselines`.
  - No adapter inlines the full rule lifecycle or latent-risk checklist.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Review adapter diffs for compact runtime-adapter style and reviewer rule consultation."

### Task_4: Add Conditional Researcher Rule Freshness Output
- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/agents/Researcher.md`
  - `plugins/coding-agent-orchestration-harness/claude/agents/harness-researcher.md`
  - `plugins/coding-agent-orchestration-harness/codex/agent-templates/harness_researcher.toml`
- depends_on: [Task_1]
- description: |
  Add a conditional Researcher output section for rule bootstrap, schema migration, targeted refresh, repair, and freshness research.
- acceptance:
  - Researcher can report rule-suite status and freshness observations when requested.
  - Researcher remains read-only.
  - The new section is conditional and not required for every research task.
  - Suggested operations use the planned enum: `full_bootstrap`, `schema_migration`, `targeted_refresh`, `repair`, `none`.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Review Researcher adapters for read-only scope and conditional output wording."

### Task_5: Allow Reviewer Rule Candidates in Worker Reports
- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/agents/Worker.md`
  - `plugins/coding-agent-orchestration-harness/claude/agents/harness-worker.md`
  - `plugins/coding-agent-orchestration-harness/codex/agent-templates/harness_worker.toml`
  - `plugins/coding-agent-orchestration-harness/skills/subagent-report-contract/SKILL.md`
  - `plugins/coding-agent-orchestration-harness/skills/subagent-report-contract/references/schema.yaml`
  - `plugins/coding-agent-orchestration-harness/skills/subagent-report-contract/scripts/validate_worker_report.py`
  - `plugins/coding-agent-orchestration-harness/tests/fixtures/valid-worker-report.yaml`
  - `plugins/coding-agent-orchestration-harness/tests/fixtures/valid-worker-report-reviewer-candidate.yaml`
- depends_on: [Task_1]
- description: |
  Extend Worker report schema and validation to accept `rule_candidates[].audience: reviewer`, while keeping Workers execution-only.
- acceptance:
  - Validator accepts `common`, `worker`, `orchestrator`, and `reviewer`.
  - Report contract prose and schema reference include `reviewer`.
  - Guidance limits `audience: reviewer` to review policy, hotspots, Reviewer evidence, or review misses.
  - Existing valid fixture still passes.
  - A reviewer-audience fixture proves the new audience is valid.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "python skills/subagent-report-contract/scripts/validate_worker_report.py --file tests/fixtures/valid-worker-report.yaml"
  - kind: command
    required: true
    owner: worker
    detail: "python skills/subagent-report-contract/scripts/validate_worker_report.py --file tests/fixtures/valid-worker-report-reviewer-candidate.yaml"
  - kind: review
    required: true
    owner: reviewer
    detail: "Review Worker adapters to confirm they still do not edit rule files."

### Task_6: Derive Plan Validation from Repo Rules
- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/plan-format/SKILL.md`
  - `plugins/coding-agent-orchestration-harness/skills/plan-format/references/validation-items.md`
- depends_on: [Task_1, Task_2]
- description: |
  Update plan-format guidance so non-trivial repository work derives validation from the rule suite when available, without requiring bootstrap for trivial work.
- acceptance:
  - Plan authoring points to `common.md`, `worker.md`, and `reviewer.md` for validation selection.
  - Missing or invalid rules route to bootstrap, refresh, repair, or an explicit waiver when validation cannot be selected confidently.
  - Explicit validation ownership remains required.
  - Trivial work does not require bootstrap.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "python skills/plan-format/scripts/validate_plan.py --file tests/fixtures/valid-plan.md --mode balanced"
  - kind: review
    required: true
    owner: reviewer
    detail: "Review plan-format guidance for validation ownership preservation."

### Task_7: Add Sparse Rule Context to Reviewer Packet Template
- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/wave-integration/references/reviewer-packet-template.md`
- depends_on: [Task_1, Task_3]
- description: |
  Add optional repo-rule context fields to the Reviewer packet template without encouraging normal reads of `_lifecycle.json`.
- acceptance:
  - Template can carry rule-suite context when applicable.
  - Lifecycle sidecar read is recorded only when it happened and why.
  - Irrelevant rule sections can be omitted.
  - Existing sparse packet style is preserved.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Review Reviewer packet template for sparse optional rule context."

### Task_8: Update Dispatch Strategy Snippets
- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/subagent-strategy/references/dispatch-checklists.md`
  - `plugins/coding-agent-orchestration-harness/skills/subagent-strategy/references/prompt-snippets.md`
- depends_on: [Task_1, Task_3, Task_4]
- description: |
  Add bounded Researcher bootstrap/refresh guidance and Reviewer dispatch hints for `reviewer.md`.
- acceptance:
  - Dispatch guidance supports read-only rule bootstrap, migration, repair, and refresh research.
  - Deliverables include status, inspected sources, validation mapping, review hotspots, contradictions, operation, and confidence.
  - Reviewer dispatch can include `reviewer.md` and relevant hotspots when review-specific policy matters.
  - Prompts remain bounded and reference-based.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Review dispatch snippets for bounded scope and rule-suite consistency."

### Task_9: Extend Conditional Latent-Risk Routing
- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/SKILL.md`
  - `plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/review-latent-risk.md`
  - `plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/review-latent-risk-public-api.md`
  - `plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/review-latent-risk-entrypoints-admission.md`
  - `plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/review-latent-risk-diagnostics.md`
  - `plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/review-latent-risk-build-ci.md`
  - `plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/review-latent-risk-state.md`
  - `plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/review-latent-risk-performance.md`
  - `plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/review-latent-risk-future-surface.md`
  - `plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/review-latent-risk-validation-tests.md`
- depends_on: []
- description: |
  Add conditional latent-risk references for public API, entrypoints/admission, diagnostics, and build/CI, and refresh existing related files.
- acceptance:
  - Router remains short and conditional.
  - New criteria live in separate reference files.
  - Existing state, performance, future-surface, and validation-tests references include the requested additions.
  - Runtime adapters only point to the router and do not inline the criteria.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Review latent-risk router and references for conditional scope and non-duplicative guidance."

### Task_10: Extend Harness Package Validation
- type: test
- owns:
  - `plugins/coding-agent-orchestration-harness/scripts/validate_harness_package.py`
  - `plugins/coding-agent-orchestration-harness/tests/fixtures/*`
- depends_on: [Task_1, Task_3, Task_5, Task_9]
- description: |
  Add structure-only validation checks for lifecycle references, rule-suite mentions, reviewer adapter references, reviewer audience, and latent-risk references.
- acceptance:
  - Validator checks the new rulebook lifecycle reference files exist.
  - Validator checks `rules-files.md` mentions the six required suite files.
  - Validator checks Reviewer adapters mention `docs/coding-agent/rules/reviewer.md`.
  - Validator checks Worker report validator allows `audience: reviewer`.
  - Validator checks latent-risk router references the new conditional files and that referenced files exist.
  - Validator does not check exact template or prompt prose.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "python scripts/validate_harness_package.py"
  - kind: command
    required: true
    owner: worker
    detail: "python scripts/run_validation_smoke_tests.py"
  - kind: review
    required: true
    owner: reviewer
    detail: "Review validator additions for structure-only scope."

### Task_11: Add ADR-D-0006
- type: docs
- owns:
  - `docs/coding-agent-orchestration-harness/decisions/ADR-D-0006-repository-rule-suite-bootstrap-lifecycle.md`
- depends_on: [Task_1, Task_2, Task_3, Task_4, Task_5, Task_6, Task_7, Task_8, Task_9, Task_10]
- description: |
  Add the durable ADR for the full rule suite, low-token index, lifecycle sidecar, and derived freshness model.
- acceptance:
  - ADR uses the existing decision front matter style.
  - ADR captures context, drivers, decision, considered options, outcome, consequences, implementation impact, validation, and revisit triggers.
  - ADR preserves the non-goal of avoiding a universal quality-gate runner.
  - ADR references current harness files and prior ADRs.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Review ADR-D-0006 for consistency with implemented behavior and existing ADR style."

## Task Waves (explicit parallel dispatch sets)

Interpretation:
- Tasks listed in the same wave are intended to be dispatched in parallel by default when `owns` are disjoint and dependencies are met.
- Waves are executed sequentially.

- Wave 1 (parallel): [Task_1, Task_9]
- Wave 2 (parallel): [Task_2, Task_3, Task_4, Task_5]
- Wave 3 (parallel): [Task_6, Task_7, Task_8]
- Wave 4 (parallel): [Task_10]
- Wave 5 (parallel): [Task_11]

## E2E / Visual Validation Spec (optional; required if UI impacted)

- Not applicable. This work does not affect UI or browser flows.

## Rollback / Safety
- Keep implementation changes scoped to the listed owns.
- If package validation surfaces a broader structural requirement, stop and replan before expanding owns.
- Do not modify unrelated repository rule files except through an explicit rulebook task.

## Progress Log (append-only)

- 2026-05-13 Plan drafted:
  - Summary: Verified the provided implementation plan against local repository structure and created this implementation-ready plan.
  - Validation evidence: Local file/path checks confirmed referenced harness areas exist. Added `schema.yaml` to Task_5 based on local report-contract schema content.
  - Notes: No implementation work has started.

## Decision Log (append-only; re-plans and major discoveries)

- 2026-05-13 Decision:
  - Trigger / new insight: `skills/subagent-report-contract/references/schema.yaml` contains the old rule candidate audience shape but was not listed in the provided Task_5 owns.
  - Plan delta (what changed): Added `schema.yaml` to Task_5 owns and acceptance scope.
  - Tradeoffs considered: Leaving it out would make the contract prose, validator, and schema reference inconsistent.
  - User approval: pending.

## Notes
- Risks:
  - Runtime adapter updates can drift into duplicated shared semantics; keep adapters compact.
  - Validator additions can become too prose-specific; keep them structural.
  - New latent-risk references can bloat review routing; keep the router conditional.
- Edge cases:
  - Existing old skeleton rule suites should route to lifecycle repair or migration, not normal task bootstrap.
  - Repositories without git should still allow lifecycle sidecar baseline commit to be unknown.
