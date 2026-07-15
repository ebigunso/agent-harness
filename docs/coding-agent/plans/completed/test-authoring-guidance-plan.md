# Plan: Add Test-Authoring Guidance To Engineering Quality Baselines

- status: done (Reviewer APPROVED 2026-07-15)
- generated: 2026-07-15
- last_updated: 2026-07-15
- work_type: docs

## Goal
- Encode the converged test-authoring principle in the harness skill set: tests assert behavior contracts that prove business-logic integrity, not developer-convenience surfaces.

## Definition of Done
- New `references/test-authoring.md` exists in engineering-quality-baselines with the agreed content; SKILL.md routes to it with one condition line; review-latent-risk-validation-tests.md gains a one-line reviewer hook; validators pass; Reviewer APPROVED.

## Scope / Non-goals
- Scope: `plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/**` only.
- Non-goals: language-specific test frameworks; changes to validation process (required/recommended checks); a standalone skill.

## Design (converged with user, 2026-07-15 via agmsg)
- General principle with named examples, not a logs-only rule: assert behavior contracts, not incidental surfaces.
- Anchor heuristic: "if this assertion failed, would it indicate a real defect or just a changed implementation detail?"
- Named low-signal surfaces: log output/format, exact error-message prose (assert error types/codes instead), over-specified mock interactions (call counts/order not in the contract), snapshot tests of incidental formatting.
- Contract exception: logs/diagnostics that are themselves contracts (audit trails, compliance events, alert-feeding telemetry, documented operator diagnostics) are tested at that contract boundary.
- Rationale to state briefly: convenience-surface assertions punish refactoring and produce low-signal failures.
- Design rules carried over: thin prompts; content lives in the reference; SKILL.md gains one routing line only.

## Context (workspace)
- Repo rules: docs/coding-agent/rules/{common,orchestrator}.md (read this session).
- Research waived: placement survey done during the convergence discussion (testing-validation.md structure inspected; no existing test-authoring content found).

## Open Questions (max 3)
- None; design converged.

## Assumptions
- A1: No version bump needed for a single-reference addition unless the user wants a release; deferred to closeout.

## Tasks

### Task_1: Write test-authoring reference, routing line, and reviewer hook
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/**
- depends_on: []
- description: |
  Create references/test-authoring.md per the Design section: principle, anchor heuristic, named low-signal surfaces, contract exception, brief rationale. Add one routing line to SKILL.md (condition: writing, modifying, or reviewing tests). Add one line to references/review-latent-risk-validation-tests.md flagging tests that assert convenience surfaces outside a stated contract.
- acceptance:
  - Reference exists with all five design elements; no duplication with testing-validation.md or review-latent-risk-validation-tests.md.
  - SKILL.md gains exactly one routing entry; reviewer hook is one line.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review vs Design section and thin-prompt rules"

### Task_2: Independent review
- type: review
- owns: []
- depends_on: [Task_1]
- description: |
  Reviewer verifies the diff against the Design section, checks for duplication/contradiction with existing references, and confirms routing wording.
- acceptance:
  - Reviewer status is APPROVED
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Full-diff review vs plan Design section"

## Task Waves (explicit parallel dispatch sets)

- Wave 1: [Task_1]
- Wave 2: [Task_2]

## Rollback / Safety
- Docs-only on a feature branch (`feature/2026-07-15/test-authoring-guidance`); revert by dropping the branch.

## Progress Log (append-only)

- 2026-07-15 Wave 1 completed: [Task_1]
  - Summary: test-authoring.md created with all five design elements; exactly one SKILL.md routing line and one reviewer-hook line added; worktree matches owns (3 files, 3 always-read insertions).
  - Validation evidence: validate_harness_package.py pass (Worker report); Reviewer diff review pending (Task_2).
  - Notes: no blockers; no version bump per A1.

- 2026-07-15 Wave 2 completed: [Task_2]
  - Summary: independent Reviewer (codex agent-harness-reviewer via agmsg) returned APPROVED with no findings; all five design elements, the contract exception, non-duplication, and routing counts verified; validator and targeted git diff --check rerun by Reviewer.
  - Validation evidence: Reviewer rerun of validate_harness_package.py pass; mechanical counts (1 route, 1 hook) confirmed.
  - Notes: targeted repo-rule refresh waived — no repository facts in docs/coding-agent/rules/*.md changed.

## Decision Log (append-only; re-plans and major discoveries)

- 2026-07-15 Decision: design converged via agmsg (general principle with examples; contract exception; placement in engineering-quality-baselines reference plus reviewer hook).
  - Trigger / new insight: user agreement with all three convergence points.
  - Plan delta (what changed): initial plan drafted from the converged design.
  - Tradeoffs considered: logs-only rule (too narrow); standalone skill (overkill); section in testing-validation.md (wrong document role).
  - User approval: design yes; execution approval pending.

## Notes
- Risks: rule misapplied to delete legitimate contract-log coverage (mitigated by the explicit exception).
