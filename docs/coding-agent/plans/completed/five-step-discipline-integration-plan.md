# Plan: Integrate The Five-Step Engineering Discipline (Long-Horizon Audit + Drift Tripwires)

- status: done (Reviewer APPROVED 2026-07-15)
- generated: 2026-07-15
- last_updated: 2026-07-15
- work_type: docs

## Goal
- Encode the five-step engineering discipline (question requirements -> delete -> optimize -> accelerate -> automate, order-gated) so the full spectrum is available as an on-demand long-horizon audit, and agents automatically notice and surface drift from the principle during ordinary work.

## Definition of Done
- Gated audit reference exists; per-task slivers and drift tripwires are in place per the Design section; always-read additions total under ~10 lines across all files; validators pass; Reviewer APPROVED.

## Scope / Non-goals
- Scope: `plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/**` and `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/**` (one replan-trigger line + routing-table line only).
- Non-goals: transcript text or attribution in skill content; changes to the worker report schema; scheduling machinery (cadence stays user-driven).

## Design (converged with user, 2026-07-15 via agmsg)

Three layers:

1. Long-horizon audit reference (`engineering-quality-baselines/references/long-horizon-audit.md`): walks all five steps in order as an examination lens — requirements that no longer earn their existence (challenge surfaced to the owner, never silently dropped/obeyed); deletion candidates across code, process steps, validations, and automation, with "never adding anything back means not deleting enough" as the calibration signal; only-then simplification/optimization; cycle-time and feedback-loop friction; premature versus ripe automation. Output is surfaced findings (user, plan Decision Log, lessons/candidates), not silent action. Routing condition: project/process health review, refactor scoping, retrospectives, explicit longer-horizon requests, or a tripped drift tripwire that warrants the full lens.
2. Per-task slivers (tiny, always effective):
   - Plan-time step-1 hook: one line in the Plan Gate area of `orchestration-harness/references/lifecycle-gates.md` — challenge requirements before decomposing work and surface doubts to the requirement owner, regardless of who authored the requirement.
   - Anti-pattern line in `core-principles.md` Common Anti-Patterns: optimizing or polishing a thing whose existence is unjustified.
3. Drift tripwires (the automatic-noticing layer; always-read but compact):
   - `engineering-quality-baselines/SKILL.md`: 3 one-line tripwires for Workers/Reviewers — (a) about to optimize, extend, or test something whose consumer or necessity cannot be named; (b) adding a process step, validation, or automation justified mainly by "in case"; (c) repeatedly working around the same component, process step, or rule. Tripwire action: surface the observation through existing channels (report questions/blockers, lesson candidates, or directly to the user) and consult the audit reference when the pattern looks systemic — do not act on it silently, and do not silently suppress it.
   - `orchestration-harness/SKILL.md` Replan Triggers: one added line — a requirement, component, or process step appears not to need to exist, or planned work is optimizing something unjustified.
   - Routing table: one line for the audit reference.

Design rules carried over: thin prompts; guidelines only (no provenance); explicit routing conditions on the gated reference.

## Context (workspace)
- Repo rules read this session; placement survey of engineering-quality-baselines and orchestration-harness done during convergence.
- Research waived: design fully converged with user over three agmsg rounds; target files inspected this session.

## Open Questions (max 3)
- None; design converged (tripwire layer added per user refinement 2026-07-15).

## Assumptions
- A1: Version bump to 0.6.0 at closeout (user decision 2026-07-15: the addition is significant enough for a minor bump).
- A2: Tripwire surfacing uses existing report/blocker/lesson channels; no report-contract schema change.

## Tasks

### Task_1: Audit reference, slivers, and tripwires
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/**
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/lifecycle-gates.md
- depends_on: []
- description: |
  Implement the three Design layers exactly. Keep the audit reference in the skill's existing reference style; keep every always-read addition to one line per item (tripwires may share a compact block). No duplication with test-authoring.md, core-principles.md existing content, or review-latent-risk-* references.
- acceptance:
  - All three layers present as specified; always-read additions total under ~10 lines across all touched files.
  - Audit reference carries its routing condition at the top; tripwires name their surfacing action.
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
  Reviewer verifies the diff against the Design section: five-step order preserved and gated, tripwires concrete and non-duplicative, surfacing actions explicit, always-read budget respected, no wording that lets agents silently delete or reject requirements.
- acceptance:
  - Reviewer status is APPROVED
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Full-diff review vs plan Design section"

### Task_3: Closeout
- type: chore
- owns:
  - plugins/coding-agent-orchestration-harness/.claude-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.codex-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.github/plugin/plugin.json
- depends_on: [Task_2]
- description: |
  Orchestrator-owned: bump plugin version to 0.6.0 in all three manifests, run full validators, commit in logical chunks, open PR.
- acceptance:
  - Version bumped; validators green; PR open.
- validation:
  - kind: command
    required: true
    owner: orchestrator
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py && python scripts/run_validation_smoke_tests.py; from repo root: git diff --check"

## Task Waves (explicit parallel dispatch sets)

- Wave 1: [Task_1]
- Wave 2: [Task_2]
- Wave 3: [Task_3]

## Rollback / Safety
- Docs-only on `feature/2026-07-15/five-step-discipline`; revert by dropping the branch.

## Progress Log (append-only)

- 2026-07-15 Wave 1 completed: [Task_1]
  - Summary: all three layers implemented — gated long-horizon-audit.md, two per-task slivers, tripwire block + replan trigger + routing line; worktree matches owns (5 files); always-read additions total 9 lines (within budget).
  - Validation evidence: validate_harness_package.py pass (Worker); duplication grep clean across engineering-quality-baselines references.
  - Notes: no blockers; Worker kept the eq-baselines category list unchanged (discovery via tripwire action line + routing table, per Design).

- 2026-07-15 Wave 2 completed: [Task_2]
  - Summary: independent Reviewer (codex via agmsg) APPROVED with no findings; step ordering/gating, no-silent-rejection wording, tripwire concreteness, sliver placement, 9-line budget, and non-duplication all verified.
  - Validation evidence: Reviewer rerun of validate_harness_package.py pass; targeted git diff --check pass; mechanical counts confirmed.
  - Notes: none.

- 2026-07-15 Wave 3 completed: [Task_3]
  - Summary: version bumped to 0.6.0 in all three manifests; full validators green (package validator, smoke tests, git diff --check); committed and PR opened.
  - Validation evidence: validate_harness_package.py pass; run_validation_smoke_tests.py pass; git diff --check clean.
  - Notes: targeted repo-rule refresh waived — no repository facts in docs/coding-agent/rules/*.md changed.

## Decision Log (append-only; re-plans and major discoveries)

- 2026-07-15 Decision: three-layer design converged over three agmsg rounds.
  - Trigger / new insight: user corrections — (1) the discipline is longer-horizon than a single task, so the full spectrum must not enter standard task flow; (2) agents must notice and surface drift automatically when it happens.
  - Plan delta (what changed): direct-integration proposal replaced by gated audit reference + per-task slivers + always-read drift tripwires with explicit surfacing actions.
  - Tradeoffs considered: always-read five-step block (rejected: prompt budget, per-task noise); audit-only with no tripwires (rejected: no automatic noticing).
  - User approval: design converged; execution approval pending.

## Notes
- Risks: tripwires too vague to fire or so broad they fire constantly — mitigated by concrete phrasing (consumer cannot be named, "in case" justification, repeated workarounds) and Reviewer scrutiny.
