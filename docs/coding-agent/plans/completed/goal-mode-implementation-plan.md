# Plan: Implement Goal Mode In The Harness (Adoption Steps 1-2)

- status: done (Reviewer APPROVED 2026-07-16 after one remediation round)
- generated: 2026-07-16
- last_updated: 2026-07-16
- work_type: docs

## Goal
- Implement the goal-mode mechanism per the ratified design (`docs/coding-agent-orchestration-harness/design/goal-mode-design.md`, ADR-D-0009..0014): the content layer and instruments that let an Orchestrator run a governed goal loop on any platform's engine. Adoption steps 1-2 only.

## Definition of Done
- An Orchestrator reading the harness can: apply the mode-selection test, negotiate and record an envelope, construct a checklist-passing goal condition, run the loop with journal + checkpoints, dispatch the assessor via the fixed template, escalate on the graded protocol, and produce a completion report the pre-merge reviewer can verify — all from shipped references and templates. Validators pass; Reviewer APPROVED against the design doc and ADRs.

## Scope / Non-goals
- Scope: goal-mode content under `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/**` and one routing/test surface change to its SKILL.md; per-runtime engine mapping reference.
- Non-goals (explicit, per design): no validators, no automation, no scripts (adoption step 4 is evidence-gated after trials); no fourth assessor role (evidence-gated upgrade); no trial run (adoption step 3 happens in a target repo with a real goal, as its own effort); no changes to plan mode semantics.

## Design Rules (carried over)
- Thin prompts: SKILL.md gains at most ~4 always-read lines (the mode-selection test at the Plan Gate position + routing); everything else is gated references.
- The design doc and ADRs are the authoritative spec; where wording must be condensed, semantics may not drift (Reviewer checks against source).
- Skills hold guidelines, not provenance: no design-history narrative in runtime content.

## Context (workspace)
- Spec: `docs/coding-agent-orchestration-harness/design/goal-mode-design.md` (six pillars) and ADR-D-0009..0014, committed on this branch's base.
- Research waived: the spec was authored and converged in this workstream; target file layout inspected throughout.

## Open Questions (max 3)
- Q1 (resolved 2026-07-16): version bump 0.8.0 approved.

## Assumptions
- A1: Goal-mode content lives in orchestration-harness (the Orchestrator owns the loop), not a separate skill: mode selection must sit at the Plan Gate position, which is orchestration-harness territory.
- A2: `docs/coding-agent/goals/active|completed/` directories are created per-repo at first goal (like plans); the reference documents the convention, no scaffolding ships.
- A3: Worker split by strengths: reference prose to Claude workers; Codex worker gets the review-adjacent artifacts (assessor mandate + condition checklist — the adversarial-detail pieces); Codex reviewer verifies the whole set.

## Tasks

### Task_1: Core goal-mode reference and SKILL.md integration
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/goal-mode.md
- depends_on: []
- description: |
  Create references/goal-mode.md as the loop's operating reference: the two-modes framing and mode-selection test (three conditions; when in doubt, plan mode); envelope negotiation and recording (decision scope, progress obligation with stall semantics per pillar 1, irreversibility-criterion forbidden set, immutability during run); the iteration lifecycle (attempt -> journal entry with committed prediction -> checkpoint commit); progress/stall semantics (single-object: direct gap or epistemic goal-linkage; tighten-free/loosen-escalates); the graded escalation protocol (proceed / decide-and-journal / ask-now / abort, ask-now as successful termination); assessment cadence events; goals/ lifecycle convention. SKILL.md: add the mode-selection test as 1-2 lines at the Plan Gate section plus one routing line to goal-mode.md. Follow the design doc pillar by pillar; do not restate assessor mandate or template content (Task_2/Task_3 own those, cross-route instead).
- acceptance:
  - Every pillar-1/2/5 semantic present per the design doc; SKILL.md additions within the always-read budget; no duplication with the Task_2/Task_3 artifacts.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py"
  - kind: review
    required: true
    owner: reviewer
    detail: "Semantic fidelity vs design doc pillars 1, 2, 5 and ADR-D-0009/0010"

### Task_2: Assessor mandate reference and condition-construction checklist
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/goal-assessor-mandate.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/goal-condition-checklist.md
- depends_on: []
- description: |
  goal-assessor-mandate.md is the immutable-during-run mandate the fixed dispatch template points at: fresh-context inputs (goal file, gap history, journal only); the two co-equal duties — trajectory assessment (re-run the gap check yourself, judge circularity and plateau goal-linkage semantically, unfulfilled committed predictions are stall evidence) and goal validity re-examination (the three ADR-D-0014 questions; outcome is goal-challenge escalation only); burden-of-proof tie-break toward escalation with the asymmetric-cost rationale; verdict format. Include the fixed dispatch template verbatim as the only sanctioned dispatch wording. goal-condition-checklist.md is the pre-loop checklist with reviewer pass: target named with a countable gap reading where possible; every invariant that may not be touched enumerated (tests, measurement harness, gap reading, linkage bar); the escalation clause present (target met OR ask-now/abort reached = termination); framing check (would satisfying the stated condition deliver the intended outcome?).
- acceptance:
  - Mandate matches ADR-D-0012/0014 exactly (two co-equal duties; template verbatim; escalate tie-break); checklist covers condition, invariants, escalation clause, framing check; nothing contradicts Task_1's reference.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py"
  - kind: review
    required: true
    owner: reviewer
    detail: "Line-level fidelity vs ADR-D-0011/0012/0014 — this is the adversarial-detail surface"

### Task_3: Goal file, journal, and completion-report templates
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/goal-templates.md
- depends_on: []
- description: |
  One reference holding the three templates. Goal file: condition (target + invariants + escalation clause), gap reading, envelope (scope, progress obligation, optional backstops, forbidden-set acknowledgment), assessment cadence events. Journal entry: iteration id, hypothesis, attempt, observed evidence, gap value, committed prediction for next iteration, decision + escalation level; assessor entries with verbatim dispatch text and verdict. Completion report: the six pillar-6 sections (condition evidence inline; one-line assessment assertion; per-invariant integrity assertions; envelope compliance with decide-and-journal items; trajectory summary; checkpoint index) — concise by design, verbatim evidence stays in the journal.
- acceptance:
  - Templates carry every field the design doc names and nothing speculative; report template readable at a glance per ADR-D-0013.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py"
  - kind: review
    required: true
    owner: reviewer
    detail: "Field-by-field check vs design doc pillars 2, 6 and ADR-D-0013"

### Task_4: Runtime goal-engine mapping
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/goal-engines.md
- depends_on: []
- description: |
  Environment-gated reference (condition at top: read when running a goal loop on a runtime with a native goal/autopilot engine): Claude Code /goal (evaluator-gated turns, --resume survival; the harness condition given verbatim, evaluator advisory — pillar-3 evidence decides); Codex goals (features.goals opt-in, thread-attached, harness-driven cadence); GitHub Copilot Autopilot (task_complete + synthetic continuation nudge + --max-autopilot-continues; the nudge never overrides ask-now/abort — the escalation clause is part of task completion). Manual loop (no engine) as the baseline that always works.
- acceptance:
  - Gating condition at top; all three engines plus the engine-less baseline; the nudge caution explicit.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py"
  - kind: review
    required: true
    owner: reviewer
    detail: "Consistency with the design doc's runtime mapping section"

### Task_5: Independent review
- type: review
- owns: []
- depends_on: [Task_1, Task_2, Task_3, Task_4]
- description: |
  Reviewer verifies the full set against the design doc and ADR-D-0009..0014: semantic fidelity per pillar, no drift between the four artifacts (parallel-written), no contradiction with plan-mode content, always-read budget respected, all cross-routes resolve, self-containment (a fresh reader needs no session context).
- acceptance:
  - Reviewer status is APPROVED
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Full-set review vs design doc + ADRs; cross-artifact drift check"

### Task_6: Closeout
- type: chore
- owns:
  - plugins/coding-agent-orchestration-harness/.claude-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.codex-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.github/plugin/plugin.json
- depends_on: [Task_5]
- description: |
  Orchestrator-owned: version bump per Q1, full validators, logical commits, PR on this branch (which already carries the design doc + ADRs).
- acceptance:
  - Version bumped; validators green; PR open.
- validation:
  - kind: command
    required: true
    owner: orchestrator
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py && python scripts/run_validation_smoke_tests.py; from repo root: git diff --check"

## Task Waves (explicit parallel dispatch sets)

- Wave 1 (parallel; disjoint owns; Claude workers for the first and third and fourth, Codex worker for the adversarial-detail second): [Task_1, Task_2, Task_3, Task_4]
- Wave 2 (review): [Task_5]
- Wave 3 (closeout): [Task_6]

## Rollback / Safety
- Docs-only on `feature/2026-07-16/goal-mode-design-records` (extends the committed design records); revert by dropping the branch.

## Progress Log (append-only)

- 2026-07-16 Wave 1 completed: [Task_1, Task_2, Task_3, Task_4]
  - Summary: five new references landed (goal-mode, goal-assessor-mandate, goal-condition-checklist, goal-templates, goal-engines) plus 3 always-read SKILL.md lines (cap was 4; SKILL.md now 142 lines total). Worktree matches owns exactly; Orchestrator reran package validator + smoke tests on the integrated set — pass.
  - Validation evidence: all four Worker reports green on required items; Task_2 additionally ran 15 targeted semantic assertions against the ADRs.
  - Notes: for Task_5 — Task_3 invented a goal-file status vocabulary (draft|ratified|in_progress|terminated_ask_now|aborted|completed) absent from the design doc; cross-check against Task_1's reference. Task_2 lesson candidate (stale session skill-catalog path; verify before reading, repo-local fallback) held for closeout lessons capture.

- 2026-07-16 Wave 2a completed: [Task_5 NEEDS_REVISION -> Task_7 remediation]
  - Summary: reviewer found five findings (lifecycle-gate ambiguity, dispatch/layout drift, unratified enum, template contract gaps, mandate self-containment); Orchestrator closed the underlying spec gaps in the design doc (layout, status semantics, lifecycle selection), then a single remediation Worker applied all six fixes plus two swept residual mismatches (mandate input order; credibility-bar field name). SKILL.md goal-mode always-read content: exactly 5 lines per the revised budget.
  - Validation evidence: package validator + smoke tests pass post-remediation (Worker and Orchestrator runs); Worker grep sweep confirms no residual old enum/paths/dispatch text.
  - Notes: Worker rule candidate (reviewer contract-sweep for goal references) and lesson candidate (mark contract fields TBD instead of inventing when the authoritative source is unratified) held for closeout.

- 2026-07-16 Wave 2b completed: [Task_5 re-review APPROVED]
  - Summary: all five findings verified resolved finding-by-finding; cross-artifact sweep clean (terminology, cadence, escalation levels, paths, status vocabulary aligned across the five references + SKILL.md); design-doc pillar-2 additions confirmed as completing, not contradicting, ADR-D-0009/0010/0014; old-contract sweep zero matches.
  - Validation evidence: reviewer independently reran package validator, smoke tests, git diff --check — all pass.
  - Notes: none.

- 2026-07-16 Wave 3 completed: [Task_6]
  - Summary: rule candidates applied (worker.md: TBD-not-invent for unratified contracts; reviewer.md: goal-reference contract sweep); two lessons captured (spec-completeness before parallel authoring; stale skill-catalog path verification); version bumped to 0.8.0; full validators green; committed and PR opened.
  - Validation evidence: validate_harness_package.py + run_validation_smoke_tests.py pass post-bump; git diff --check clean.
  - Notes: targeted rule refresh satisfied by the applied candidates; no other repo facts changed.

## Decision Log (append-only; re-plans and major discoveries)

- 2026-07-16 Decision: Task_5 NEEDS_REVISION (5 findings: lifecycle-gate ambiguity, dispatch-template and layout drift, unratified status enum, template contract gaps, mandate self-containment). Spec gaps closed by Orchestrator in the design doc before remediation: goal artifact layout (directory per goal: goal.md + journal.md under goals/active/<goal-id>/), status vocabulary with terminal archiving semantics (draft|active|awaiting_decision|completed|aborted|abandoned; all terminals archive to goals/completed/ preserving outcome), and explicit lifecycle-selection statement (goal mode replaces plan approval/Task_X/closeout with envelope/journal+checkpoints/report+retrospective; all other gates unchanged).
  - Trigger / new insight: reviewer findings exposed that workers improvised where the spec was silent — the invented enum and layout were symptoms of spec gaps, not worker error.
  - Plan delta (what changed): one remediation task (Task_7) added before re-review; SKILL.md always-read budget raised to ~5 lines to surface all three selection predicates and one-lifecycle selection at the gate, per the reviewer's Required clause.
  - Tradeoffs considered: dispatching per-finding remediation to multiple workers (rejected — cross-file consistency is the defect class; one worker gets the whole set); leaving the enum out entirely (rejected — ask-now outcomes need a recorded awaiting-decision state for the archive semantics to work).
  - User approval: within ratified design authority; spec completions recorded here and in the design doc on the same branch.

- 2026-07-16 Decision: plan drafted for adoption steps 1-2 only, per the design doc's own sequencing (content -> instruments -> trial -> automation).
  - Trigger / new insight: user instruction to draft the implementation plan after ratifying the ADRs.
  - Plan delta (what changed): initial draft.
  - Tradeoffs considered: including a trial task (rejected — trials need a real goal in a target repo and belong to that repo's workflow); separate goal-mode skill (rejected — mode selection must sit at the Plan Gate position inside orchestration-harness).
  - User approval: pending.

## Notes
- Risks: four parallel-written artifacts drifting from each other or the spec (mitigated: each task names its authoritative pillars/ADRs; Task_5 checks cross-artifact drift explicitly); SKILL.md budget creep (mitigated: hard ~4-line cap in Task_1 acceptance).
