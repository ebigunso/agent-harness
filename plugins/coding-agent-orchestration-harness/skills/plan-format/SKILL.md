---
name: plan-format
description: Standard execution plan format for decomposing non-trivial work into Task_X tasks with owns/depends_on, explicit validation ownership, and explicit Task Waves (parallel dispatch sets). Use when asked to make a plan, break down tasks, outline implementation steps, execute multi-step work, or when non-trivial work requires a plan.
---

# Skill: plan-format

This skill defines the standard **execution plan** structure used for non-trivial work.

Design assumptions:
- Plans are drafted at the start, reviewed by a Reviewer, then approved by the user.
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

10) Plan altitude: a plan states what, why, and constraints, and leaves how to the Worker; it does not restate what the Worker can discover cheaply. This does not override user-requested decomposition depth (rule 9).

11) ADR-producing tasks: use "propose an ADR if the admission test passes" per `durable-docs-authoring/references/adr.md`; do not enumerate record contents in acceptance criteria.

12) Planner-added requirements: a `planner-added requirement` is a Definition of Done item, acceptance bullet, or constraint that entered the plan during drafting rather than from the request, a document the request names, or the repository's rule suite and lessons. Every planner-added requirement is listed in the plan's `Planner-added requirements` section with the reason the request cannot be met without it under the chosen design; the section is present on every plan and reads `- None` when nothing was added. An addition found anywhere else in the plan but not in that section is a plan defect.

13) Design comparison:
- The plan's `Design` section states the design chosen and at least one alternative that differs from it on a lens, with what each changes on every lens group (consumers stay in the Compatibility stance, rule 8), and why the chosen one wins.
- Lens groups and their members (each lens is its name with at most one short clause):
  - `structure`: dependencies; duplicated state; conversions; one owner per piece of state; coupling direction (volatile depends on stable); boundary crossings (representation, process, trust level).
  - `evolution`: technical debt; blast radius of the next change; fit with the project's stated direction; concept count (abstractions, knobs, vocabulary); deletion path.
  - `verification`: test seam (clear of network, clock, filesystem, UI); cost to run the tests; cost to change the tests when the design changes; tests pin the contract, not the implementation; determinism (randomness, time, ordering, concurrency injectable); failure observability.
  - `operation`: runtime cost and how it scales; degradation when a dependency is slow, down, or wrong.
  - `human`: cognitive load (names predict behavior); debuggability (reproducible locally).
  - `safety`: trust boundary handling; least privilege (permissions, secrets, reach); data exposure (logs, caches, errors).
- A fit claim (a statement that a design fits or conflicts with the project's stated direction) names the document where the repository states that direction: a decision record, roadmap, README or contributing guide, rule file, or a reference document the rule suite lists.
- Proportional form: when the change touches no responsibility, contract, persisted state, new component, trust boundary, or hot path, the section is the one-line form the template shows.

---

## Progressive disclosure (read only what you need)

If you are writing or updating a plan:
- Read `references/plan-template.md`

If you are unsure how to express validation items:
- Read `references/validation-items.md`

If you need lifecycle guidance (active → completed, logs, replans):
- Read `references/execution-plan-lifecycle.md`

If the user asked for language/tech-specific planning depth:
- Read language/framework-specific quality gates and references before finalizing decomposition.
