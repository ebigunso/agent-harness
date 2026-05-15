# Plan: Latent-Risk Reference Hardening

- status: draft
- generated: 2026-05-16
- last_updated: 2026-05-16
- work_type: docs

## Goal
- Sharpen selected latent-risk references and reviewer rule template wording so Reviewers catch concrete API, diagnostics, build parity, and canonical policy-path risks without expanding every review into an always-on checklist.

## Definition of Done
- Public API reference names concrete API-evolution traps.
- Diagnostics reference names precise failing-source metadata risks.
- Build/CI reference distinguishes production-reachable behavior from test-only paths.
- Future-surface reference includes canonical policy-path checks.
- Reviewer rule template keeps mechanical gates repo-local first and stages bundled-harness checks as HMCs.
- Required validation passes or is explicitly waived with evidence.

## Scope / Non-goals
- Scope:
  - `plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/review-latent-risk-public-api.md`
  - `plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/review-latent-risk-diagnostics.md`
  - `plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/review-latent-risk-build-ci.md`
  - `plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/review-latent-risk-future-surface.md`
  - `plugins/coding-agent-orchestration-harness/skills/rulebook/references/rule-suite-templates.md`
- Non-goals:
  - Do not change the latent-risk router.
  - Do not change Reviewer adapters or prompt snippets; those belong to the operational routing plan.
  - Do not add package validator checks; those belong to the enforcement plan.

## Context (workspace)
- Related files/areas:
  - `plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/review-latent-risk.md`
  - `plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/review-rubric.md`
  - `plugins/coding-agent-orchestration-harness/skills/rulebook/references/rules-files.md`
- Existing patterns or references:
  - Latent-risk references are conditional review aids; they should not be emitted wholesale in reports.
  - Repo reviewer rules can capture local mechanical gates, while cross-repo harness improvements should be staged as HMCs.
- Repo reference docs consulted:
  - `docs/coding-agent/rules/index.md`
  - `docs/coding-agent/rules/common.md`
  - `docs/coding-agent/rules/orchestrator.md`
  - `docs/coding-agent/rules/worker.md`

## Open Questions (max 3)
- Q1: None.

## Assumptions
- A1: The four latent-risk references already exist and should be amended in place.
- A2: The reviewer rule template should describe desired repo-local rule-file contents, not bundled-harness maintenance procedures.

## Tasks

### Task_1: Sharpen Public API Compatibility Reference
- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/review-latent-risk-public-api.md`
- depends_on: []
- description: |
  Add explicit public API evolution traps, including Rust-style struct, enum, trait, constructor, builder, non-exhaustive, and export completeness concerns.
- acceptance:
  - Reference mentions public struct field additions and downstream struct literal breakage.
  - Reference mentions enum exhaustiveness and trait required item additions.
  - Reference mentions function arity, generic bounds, return type, error type, and feature availability changes.
  - Reference mentions constructor, builder, accessor, private-field, or `non_exhaustive` strategy.
  - Reference mentions crate-root, prelude, module, generated-doc, and example import consistency.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "rg -n \"struct field|exhaustive|trait required|generic bounds|non_exhaustive|crate-root|prelude\" plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/review-latent-risk-public-api.md"
  - kind: review
    required: true
    owner: reviewer
    detail: "Confirm additions remain broadly applicable and do not make Rust the only supported public API model."

### Task_2: Sharpen Diagnostic Fidelity Reference
- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/review-latent-risk-diagnostics.md`
- depends_on: []
- description: |
  Add precise diagnostic metadata checks and loop-diagnostic failure patterns.
- acceptance:
  - Reference lists field name, column index, path, object id, operation, backend/store, scope, request/user/tenant/config, and candidate status metadata.
  - Reference warns about diagnostics inside loops using constant, default, or outer values instead of the current failing item.
  - Existing actionable-cause guidance remains intact.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "rg -n \"field name|column index|object id|backend/store|request/user/tenant/config|candidate vs accepted|outer value\" plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/review-latent-risk-diagnostics.md"
  - kind: review
    required: true
    owner: reviewer
    detail: "Confirm diagnostics guidance focuses on correctness of emitted metadata, not stylistic wording preferences."

### Task_3: Sharpen Build/CI Parity Reference
- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/review-latent-risk-build-ci.md`
- depends_on: []
- description: |
  Add checks that tests exercise behavior compiled and reachable in the intended runtime configuration.
- acceptance:
  - Reference states tests must exercise production-reachable behavior.
  - Reference warns about `#[cfg(test)]`, mock-only paths, debug-only behavior, feature-gated public items, and platform cfg divergence.
  - Existing strict-CI and feature/cfg parity guidance remains intact.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "rg -n \"production-reachable|#\\[cfg\\(test\\)\\]|mock-only|debug-only|feature-gated|platform cfg\" plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/review-latent-risk-build-ci.md"
  - kind: review
    required: true
    owner: reviewer
    detail: "Confirm guidance distinguishes test-production parity from requiring a universal repo test runner."

### Task_4: Add Canonical Policy Path To Future Surface Reference
- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/review-latent-risk-future-surface.md`
- depends_on: []
- description: |
  Add a canonical policy path section that directs Reviewers to identify the constructor, validator, helper, error builder, or policy function that owns the domain decision.
- acceptance:
  - Reference includes a numbered or clearly titled canonical policy path section.
  - Section flags bypasses through direct construction, duplicated matching, local constants, parallel validation, and direct error construction that bypasses common metadata.
  - Section allows bypasses only when the change documents why the existing owner is inappropriate.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "rg -n \"Canonical policy path|constructor|validator|direct construction|duplicated matching|parallel validation|direct error construction\" plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/review-latent-risk-future-surface.md"
  - kind: review
    required: true
    owner: reviewer
    detail: "Confirm canonical policy guidance does not forbid intentional new boundaries when documented."

### Task_5: Adjust Reviewer Template Mechanical Gate Wording
- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/rulebook/references/rule-suite-templates.md`
- depends_on:
  - Task_1
  - Task_2
  - Task_3
  - Task_4
- description: |
  Revise the `reviewer.md` template's Mechanical Gate Candidates section to be repo-local first and route bundled-harness validation ideas through HMC staging.
- acceptance:
  - Template lists repo-local destinations: `worker.md` check mapping, repository CI, repository hooks, repository scripts, and repository validators.
  - Template states bundled harness validators or plugin package validation candidates should be staged in `docs/coding-agent/skill-candidates.md`.
  - Wording does not encourage ordinary target-repo runtime agents to mutate bundled harness validators.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "rg -n \"Repo-local checks|worker.md check mapping|repository CI|repository hooks|repository scripts|repository validators|skill-candidates.md\" plugins/coding-agent-orchestration-harness/skills/rulebook/references/rule-suite-templates.md"
  - kind: review
    required: true
    owner: reviewer
    detail: "Confirm rule template wording preserves the repo-local vs harness-migration split."

## Task Waves (explicit parallel dispatch sets)

Interpretation:
- Tasks listed in the same wave are intended to be dispatched in parallel by default when `owns` are disjoint and dependencies are met.
- Waves are executed sequentially.

- Wave 1 (parallel): [Task_1, Task_2, Task_3, Task_4]
- Wave 2 (parallel): [Task_5]

## E2E / Visual Validation Spec

- Not applicable; no UI or user flow is impacted.

## Rollback / Safety
- Revert only the files listed in the affected task.
- If a reference addition begins changing router behavior, pause and move that work to a separate routing task.

## Progress Log (append-only)

- 2026-05-16 00:00 Plan drafted.
  - Summary: Created scoped implementation plan for latent-risk reference hardening and reviewer template wording.
  - Validation evidence: Not run; draft plan only.
  - Notes: Research waived because the user supplied current-file findings and work is limited to plan creation.

## Decision Log (append-only; re-plans and major discoveries)

- 2026-05-16 00:00 Decision: Keep reference substance separate from operational routing.
  - Trigger / new insight: User requested logical boundaries without scope creep.
  - Plan delta (what changed): This plan owns review-reference substance and one closely related reviewer rule template section.
  - Tradeoffs considered: Combining this with packet/snippet routing would mix review criteria quality with dispatch plumbing.
  - User approval: yes, user requested actual plan files after reviewing the split.

## Notes
- Risks:
  - The public API section could become Rust-specific; keep examples concrete but generally portable.
  - The build/CI section should not imply every target repository has the same CI model.
- Edge cases:
  - If existing headings differ from the supplied notes, preserve local heading style while adding the requested checks.
