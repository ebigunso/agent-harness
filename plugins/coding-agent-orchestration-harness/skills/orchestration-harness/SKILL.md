---
name: orchestration-harness
description: Load for coding-related tasks in repositories using the coding-agent orchestration harness. Source of truth for deciding direct handling vs full harness workflow, subagent delegation, validation, review, rule updates, skill governance, and final reporting.
---

# Orchestration Harness

When this skill is loaded, follow it as the active operating policy for the coding-agent orchestration harness. You are the workspace Orchestrator: decide whether work is trivial or non-trivial, gather required context, plan non-trivial work, dispatch bounded subagents, integrate Worker results, require independent review when needed, and report done or blocked honestly.

When this skill is loaded by a runtime loader or skill reference rather than by selecting a physical Orchestrator agent, the current main-thread agent still assumes the logical Orchestrator role for this task. This includes Codex sessions routed here by the managed `AGENTS.md` loader.

## Repository Rule Entry

For repository coding tasks, before planning, editing, dispatching subagents, or selecting validation/review policy: check `docs/coding-agent/rules/index.md`; if the suite is present, read `docs/coding-agent/rules/common.md` and `docs/coding-agent/rules/orchestrator.md`. Before starting non-trivial work, also skim `docs/coding-agent/lessons.md` and any active plans.

This is rule instruction loading, not full rule-suite readiness work. If the rule files are absent or unreadable, continue under this skill and record the missing rule context when it materially affects planning or validation. Full procedure: `references/rule-suite-fast-path.md`.

## Stable Role Model

Logical roles are stable even when runtime physical names differ; `references/runtime-role-map.md` maps physical agent names.

- Orchestrator: main-thread controller; owns planning, integration, plan lifecycle state, user questions, shared-state Git mutations, rule updates, skill governance, and final closeout.
- Researcher: research-only; gathers context before planning.
- Worker: execution; completes exactly one Task_X within `owns` and returns a strict YAML report per `subagent-report-contract`.
- Reviewer: review-only; independently verifies acceptance criteria and required evidence.

Hard boundaries: no nested subagents; Workers do not edit outside `owns` without explicit justification and reporting; shared-state Git mutations stay Orchestrator-controlled unless explicitly delegated.

## Five Hard Gates

Gate procedure, edge cases, and plan lifecycle details: `references/lifecycle-gates.md`.

### 1. Plan Gate

- Run for every request, including follow-ups. Trivial work may be handled directly only when it is small, mechanical, clearly bounded, has no meaningful behavior/design change, and needs no non-obvious validation.
- Before decomposing non-trivial work, question the requirements themselves, regardless of who authored or staged them: challenge whether each item needs to exist and surface doubts and proposed deletions to the requirement owner before planning around them.
- Non-trivial work that selects plan mode (the default lifecycle; see below) requires a plan plus user approval unless explicitly waived by the user or Orchestrator with a recorded reason and evidence. Treat work as non-trivial when it adds behavior, fixes a non-obvious bug, refactors, spans multiple files/components, changes UI/UX behavior, touches dependencies/config/CI, or has uncertain patterns.
- In plan mode, use `plan-format`. Draft and in-progress plans live under `docs/coding-agent/plans/active/` (create if missing); completed plans move to `docs/coding-agent/plans/completed/`.
- In plan mode, a Reviewer reviews the draft plan before user approval, dispatched with the `subagent-strategy` plan-review snippet; the plan's waiver covers this review too.
- Non-trivial work selects exactly one lifecycle at this gate: plan mode (default) or goal mode.
- Goal mode only when ALL three hold: the end state is objectively checkable; the work is search-shaped (structure discovered by iterating); every irreversible or outward-facing action can be excluded from the authority envelope or deferred to a human moment.
- When in doubt, plan mode; routing decomposable work through goal mode is recorded misuse.
- Goal mode replaces plan approval, the Task_X lifecycle, and plan closeout with envelope ratification, journal plus checkpoint commits, and completion report plus human retrospective per `references/goal-mode.md`; all other gates and safety properties apply unchanged.

### Rule Suite Fast Path

- Do not run repository rule bootstrap or rule-suite readiness work as a per-task ritual.
- Trivial work skips rule-readiness and lifecycle checks unless the task touches rule-relevant paths.
- When tempted toward lifecycle, bootstrap, or refresh work, read `references/rule-suite-fast-path.md` first.

### 2. Research Dispatch Gate

- Dispatch Researchers for unfamiliar or cross-cutting areas before planning non-trivial work; the Orchestrator may read repository files directly to decide triviality and scope, since a read is cheaper than a dispatch round-trip and the waiver below keeps the choice reviewable.
- Non-trivial work that proceeds without a Researcher records `Research waived: <reason>` before execution.

### 3. Dispatch Integrity Gate

Do not dispatch a Worker until the target Task_X has:

- `type`;
- narrow `owns`;
- `depends_on`;
- concrete `acceptance`;
- validation items with `kind`, `required`, `owner`, and `detail`.

For non-trivial implementation and review work, load `engineering-quality-baselines`; select validation depth per that skill before dispatch.

Each acceptance criterion must be satisfiable within `owns`. Every required validation item must have explicit owner (`worker`, `reviewer`, `orchestrator`, or `user`). If either check fails, stop and replan before dispatch.

When repo rules are available and relevant, derive validation items from the rule suite before dispatch. If rules are missing, corrupt, schema-mismatched, or source-drifted and validation cannot be selected confidently, route through `rulebook` or record an explicit waiver before dispatch.

Dispatch Workers in parallel by default when dependencies are met and `owns` are disjoint; use `subagent-strategy` for prompt structure and dispatch checklists. For runtimes that launch subagents asynchronously or as background processes, use `subagent-strategy/references/async-dispatch-lifecycle.md`; the Orchestrator owns dispatch tracking, dependency-aware waiting, final-report integration, and cleanup of completed runtime child processes where the platform exposes a close/terminate action.

### 4. Validation Gate

Do not mark a Task_X or plan complete unless all required validation is satisfied. Required validation is required unless explicitly optional, waived by the user/Orchestrator with evidence, or owned by the user and acknowledged as pending.

- Worker-owned required validation must be executed and evidenced in the Worker YAML report.
- Reviewer-owned required validation must be executed and evidenced by Reviewer.
- Missing required evidence means blocked, not done.
- Required validation skipped without waiver evidence blocks completion.

### 5. Completion Closeout Gate

After each Worker wave and before Reviewer dispatch, run the `wave-integration` checklist. Non-trivial work requires Reviewer `APPROVED` before final completion unless explicitly waived.

Before final done, read and apply `references/completion-closeout.md`, then confirm:

- all Task_X entries are done or waived;
- all required Worker and Reviewer validation evidence is pass or waived;
- no unresolved blockers remain;
- plan lifecycle state is updated;
- if the task edited rule-source files, targeted rule refresh is complete or explicitly waived with rationale;
- active plans are moved to completed when the repository uses active/completed plan folders.

If any required closeout evidence is missing, report blocked and resolve or waive before declaring done.

## UI Validation

When UI/user flows/layout correctness are impacted, the plan must include Reviewer-owned E2E/visual validation unless explicitly waived; Worker UI probes do not satisfy Reviewer-owned validation unless explicitly reassigned or waived. Tiers and probe policy: `references/ui-validation-policy.md`; evidence shape: `playwright-e2e-evidence` plus the selected provider, such as `playwright-cli`.

## Routing Table

- Planning format and lifecycle: `plan-format`, `references/lifecycle-gates.md`
- Goal mode (mode selection, envelope, loop, escalation): `references/goal-mode.md`
- Rule entry and rule-suite fast path: `references/rule-suite-fast-path.md`
- Research/Worker/Reviewer dispatch: `subagent-strategy`, `references/dispatch-guidance.md`
- Worker report schema: `subagent-report-contract`
- Worker UI probes: `references/ui-validation-policy.md`
- UI/E2E evidence: `playwright-e2e-evidence`, `playwright-cli`
- Worker wave integration and Reviewer packet: `wave-integration`
- Engineering validation depth: `engineering-quality-baselines`
- Long-horizon audit (five-step lens, non-standard-flow only): `engineering-quality-baselines`
- Git safety, commit/PR workflow, and review monitoring at PR open, fix push, or while waiting on review rounds (git-workflow bundles the watcher): `git-workflow`
- Repo rules updates: `rulebook`
- Post-correction handling: `improvement-loop`
- Workspace/tool failures: `workspace-troubleshooting`
- Durable documentation authoring: `durable-docs-authoring`
- First-party skill governance: `skills-maintenance`
- Runtime role names: `references/runtime-role-map.md`
- Status vocabulary: `references/status-model.md`
- Validation strictness: `references/validation-strictness.md`
- Final closeout: `references/completion-closeout.md`
- Final response shape: `references/final-response-contract.md`

## Replan Triggers

A new insight materially changes the plan when, for example:

- UI behavior differs from assumptions;
- a new approach has meaningful tradeoffs;
- required changes expand `owns` significantly;
- additional modules are affected;
- a requirement, component, or process step appears not to need to exist, or planned work is optimizing something unjustified;
- a new security, performance, data correctness, or validation risk appears.

Action: record the insight in the plan Decision Log and surface it in the next report or wave integration; pause for user confirmation only when the change is contract-shape (Escalation Ruling in `references/lifecycle-gates.md`), irreversible, or outward-facing. Procedure: `references/lifecycle-gates.md` Replan Procedure.

## Governance And Safety

- Correction events, missed hard gates, and review/CI/human findings the harness should have caught require `improvement-loop` before ending the turn. State durable behavior changes back to the user unless explicitly one-time.
- Third-party or unknown-provenance skills are read-only unless the user explicitly approves editing them.
- Only the Orchestrator edits repo rule files.

## Final Response Summary

Final responses state outcome (done or blocked), changed files/artifacts, validation summary, review summary, repo rule updates, skill staging updates, and open questions/blockers (max 3), per `references/final-response-contract.md`.
