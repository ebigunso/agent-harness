---
name: plan-format
description: Standard execution plan format for decomposing non-trivial work into Task_X tasks with owns/depends_on, explicit validation ownership, and explicit Task Waves (parallel dispatch sets). Use when asked to make a plan, break down tasks, outline implementation steps, execute multi-step work, or when non-trivial work requires a plan.
---

# Skill: plan-format

This skill defines the standard **execution plan** structure used for non-trivial work.

Design assumptions:
- Plans are drafted at the start and reviewed by humans.
- Plans may evolve during execution (progress logs + decision logs).
- The format should remain easy to evolve; avoid over-constraining.

---

## Core rules (always apply)

1) Plan locations:
- Draft and execute under: `docs/coding-agent/plans/active/<kebab>-plan.md`
- When finished and validated: move to `docs/coding-agent/plans/completed/`

2) Task IDs:
- Must be `Task_1`, `Task_2`, ... (Task_X format)

3) Each Task_X must include:
- `type`: design | impl | test | docs | slides | research | review | chore
- `owns`: paths/globs the Worker is allowed to modify (keep narrow)
- `depends_on`: list of Task_X IDs (or [])
- `acceptance`: 2–6 concrete bullets
- `validation`: explicit validation items (required/owner/kind/detail)

4) Task Waves (parallel dispatch semantics):
- A plan MUST include a “Task Waves” section.
- Tasks listed in the same wave are intended to be dispatched **in parallel by default**
  when `owns` are disjoint and dependencies are satisfied.
- Waves are executed **sequentially**.

5) Plan-integrity checklist (before dispatch):
- For each Task_X, confirm every acceptance bullet is satisfiable using only its `owns` scope.
- If acceptance requires edits outside `owns`, split/re-scope tasks before execution.
- Every `validation` item must explicitly state `required` and `owner`.
- If `required: true`, do not mark that task done without evidence for that item.
- For non-trivial repository work, derive validation items from the repo rule suite when available. Do not require bootstrap for trivial work.

6) Execution logs:
- A plan MUST include:
  - “Progress Log” (append after each wave)
  - “Decision Log” (append when re-planning or assumptions change)

7) UI / E2E / visual:
- If UI or user flows are impacted:
  - include a Reviewer-owned E2E/visual validation item
  - define an E2E spec in the plan
  - name the browser automation provider and artifact root explicitly
  - keep provider-specific execution details in progressive-disclosure references
  - if the selected provider is `playwright-cli`, artifacts typically live under `.playwright-cli/`

8) Compatibility stance:
- If the plan touches a contract, interface, or persisted format, it MUST include a plan-level "Compatibility stance" section declaring one of: `break | preserve | migrate | ask-user`.
- The stance must be justified by locatable consumers (per the locatable-consumer definition in `engineering-quality-baselines/references/core-principles.md`), not by hypothetical ones.
- Boundary-crossing surfaces whose consumers cannot be verified default to `ask-user`.
- One plan-level stance suffices; add per-task stance notes only when stances differ across tasks.

9) Decomposition depth + harmonization:
- When the user explicitly requests language/framework depth, decompose implementation tasks by that depth (for example, API/data/model/UI/test slices).
- If a plan intentionally mixes abstraction levels (for example, feature-level and file-level tasks), add a final harmonization pass before review to verify naming, boundaries, and validation coverage remain coherent.

---

## Progressive disclosure (read only what you need)

If you are writing or updating a plan:
- Read `references/plan-template.md`

If you are unsure how to express validation items:
- Read `references/validation-items.md`

If you are unsure how to define waves:
- Read `references/task-waves.md`

If you need lifecycle guidance (active → completed, logs, replans):
- Read `references/execution-plan-lifecycle.md`

If you want examples across task types:
- Read `references/examples.md`

If the user asked for language/tech-specific planning depth:
- Read language/framework-specific quality gates and references before finalizing decomposition.
