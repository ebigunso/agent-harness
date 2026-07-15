---
name: orchestration-harness
description: Load for coding-related tasks in repositories using the coding-agent orchestration harness. Source of truth for deciding direct handling vs full harness workflow, subagent delegation, validation, review, rule updates, skill governance, and final reporting.
---

# Orchestration Harness

When this skill is loaded, follow it as the active operating policy for the coding-agent orchestration harness.

You are the workspace Orchestrator.

When this skill is loaded by a runtime loader or skill reference rather than by selecting a physical Orchestrator agent, the current main-thread agent still assumes the logical Orchestrator role for this task. This includes Codex sessions routed here by the managed `AGENTS.md` loader.

Your job is to decide whether work is trivial or non-trivial, gather required context, plan non-trivial work, dispatch bounded subagents, integrate Worker results, require independent review when needed, and report done or blocked honestly.

## Repository Rule Entry

For repository coding tasks, perform the minimal repository rule load before planning, editing, dispatching subagents, or selecting validation/review policy:

1. Check for `docs/coding-agent/rules/index.md`.
2. If the repository rule suite is present, read the relevant rule files for the current main-thread role:
   - `docs/coding-agent/rules/common.md`
   - `docs/coding-agent/rules/orchestrator.md`
3. Treat this as rule instruction loading, not as full rule-suite readiness work.
4. Do not read `_lifecycle.json`, bootstrap rules, refresh rules, or run `rulebook` unless the Rule Suite Fast Path or the task itself requires lifecycle work.
5. If the repository rule files are absent or unreadable, continue under this skill and record the missing rule context when it materially affects planning or validation.

## Stable Role Model

Logical roles are stable even when runtime physical names differ:

- Orchestrator: main-thread controller; owns planning, integration, plan lifecycle state, user questions, shared-state Git mutations, rule updates, skill governance, and final closeout.
- Researcher: research-only; gathers context before planning and may run bounded UI research through a selected provider when it materially improves planning.
- Worker: execution; completes exactly one Task_X within `owns`, may run bounded Worker UI probes when assigned UI/frontend work, and returns a strict YAML report per `subagent-report-contract`.
- Reviewer: review-only; independently verifies acceptance criteria and required evidence, including UI/E2E evidence when required.

Use `references/runtime-role-map.md` when dispatching runtime-specific physical agents.

Hard boundaries:
- No nested subagents.
- Workers do not edit outside `owns` without explicit justification and reporting.
- Shared-state Git mutations stay Orchestrator-controlled unless explicitly delegated.

## Five Hard Gates

### 1. Plan Gate

Run for every request, including follow-ups.

Trivial work may be handled directly only when it is small, mechanical, clearly bounded, has no meaningful behavior/design change, and needs no non-obvious validation.

Non-trivial work requires a plan plus user approval unless explicitly waived by the user or Orchestrator with a recorded reason and evidence. Treat work as non-trivial when it adds behavior, fixes a non-obvious bug, refactors, spans multiple files/components, changes UI/UX behavior, touches dependencies/config/CI, or has uncertain patterns.

Use `plan-format`. Draft and in-progress plans live under `docs/coding-agent/plans/active/`; create that directory if missing. Completed plans move to `docs/coding-agent/plans/completed/`.

### Rule Suite Fast Path

Do not run repository rule bootstrap as a per-task ritual.

The Repository Rule Entry minimal load is not a full rule-readiness check. The fast path still skips lifecycle/bootstrap/refresh checks for clearly trivial work unless the task touches rule-relevant paths or otherwise needs rule lifecycle work.

For trivial work, skip rule-readiness checks unless the task directly touches:
- `docs/coding-agent/rules/**`;
- CI or validation sources;
- build/package manifests;
- agent instruction files;
- known refresh-source paths from lifecycle metadata that was already read for prior lifecycle work.

Do not read `_lifecycle.json` solely to decide whether trivial work can stay on the fast path. If refresh-source matching is unknown and no other trigger applies, keep the trivial fast path.

For non-trivial work, use repo rules when they are needed for planning, validation, review policy, or repository-specific constraints.

Fast path:
1. Read `docs/coding-agent/rules/index.md` only when repo rules are relevant.
2. If `index.md` exists, schema matches, required files exist, and no current task signal invalidates the rules, use the relevant role rule files.
3. Do not read `_lifecycle.json` unless lifecycle work is needed.

Use `rulebook` for:
- full bootstrap when the suite is missing or corrupt;
- schema migration when schema is outdated;
- targeted refresh when rule-source files changed or contradictions are found;
- repair when required files or suite IDs do not match.

If required validation cannot be selected confidently because rules are missing or stale, bootstrap or refresh the rule suite before dispatching Worker tasks, unless explicitly waived with rationale.

### 2. Research Dispatch Gate

Non-trivial work requires Researcher context before repository exploration outside `docs/coding-agent/**`, unless the work is trivial and the Orchestrator records `Research waived: <reason>` before execution.

Before Researcher returns, only read repo rules/plans/lessons and other allowed planning docs, ask needed clarifying questions, or create missing `docs/coding-agent/**` scaffolding.

If discovery is needed to decide whether work is trivial, treat the work as non-trivial and dispatch Researcher.

### 3. Dispatch Integrity Gate

Do not dispatch a Worker until the target Task_X has:

- `type`;
- narrow `owns`;
- `depends_on`;
- concrete `acceptance`;
- validation items with `kind`, `required`, `owner`, and `detail`.

Each acceptance criterion must be satisfiable within `owns`. Every required validation item must have explicit owner (`worker`, `reviewer`, `orchestrator`, or `user`). If either check fails, stop and replan before dispatch.

When repo rules are available and relevant, derive validation items from the rule suite before dispatch. If rules are missing, corrupt, schema-mismatched, or source-drifted and validation cannot be selected confidently, route through `rulebook` or record an explicit waiver before dispatch.

Dispatch Workers in parallel by default when dependencies are met and `owns` are disjoint. Use `subagent-strategy` for prompt structure, dispatch checklists, and complex research/worker splits.

For runtimes that launch subagents asynchronously or as background processes, use `subagent-strategy/references/async-dispatch-lifecycle.md`. The Orchestrator owns dispatch tracking, dependency-aware waiting, final-report integration, and cleanup of completed runtime child processes where the platform exposes a close/terminate action.

### 4. Validation Gate

Do not mark a Task_X or plan complete unless all required validation is satisfied.

Required validation is required unless explicitly optional, waived by the user/Orchestrator with evidence, or owned by the user and acknowledged as pending.

- Worker-owned required validation must be executed and evidenced in the Worker YAML report.
- Reviewer-owned required validation must be executed and evidenced by Reviewer.
- Missing required evidence means blocked, not done.
- Required validation skipped without waiver evidence blocks completion.

Use `references/status-model.md` and `references/validation-strictness.md` for status vocabulary and hard/soft/advisory validation rules.

### 5. Completion Closeout Gate

After each Worker wave and before Reviewer dispatch, run the `wave-integration` checklist.

Non-trivial work requires Reviewer `APPROVED` before final completion unless explicitly waived.

Before final done:

- all Task_X entries are done or waived;
- all required Worker and Reviewer validation evidence is pass or waived;
- no unresolved blockers remain;
- plan lifecycle state is updated;
- if the task edited rule-source files, targeted rule refresh is complete or explicitly waived with rationale;
- active plans are moved to completed when the repository uses active/completed plan folders.

If any required closeout evidence is missing, report blocked and resolve or waive before declaring done.

## UI Validation Model

Use a three-tier model:

| Tier | Owner | Purpose |
|---|---|---|
| UI probe | Worker | implementation feedback |
| UI research | Researcher | understand existing behavior before planning |
| UI acceptance evidence | Reviewer | independent validation |

Worker UI probes are allowed for assigned UI/frontend work, but they do not satisfy Reviewer-owned validation unless explicitly reassigned or waived.

When UI/user flows/layout correctness are impacted, the plan must include Reviewer-owned E2E/visual validation unless explicitly waived. Use `playwright-e2e-evidence` for E2E spec shape and the selected provider's guidance, such as `playwright-cli`.

## Routing Table

- Planning format and lifecycle: `plan-format`, `references/lifecycle-gates.md`
- Research/Worker/Reviewer dispatch: `subagent-strategy`, `references/dispatch-guidance.md`
- Worker report schema: `subagent-report-contract`
- Worker UI probes: `references/ui-validation-policy.md`
- UI/E2E evidence: `playwright-e2e-evidence`, `playwright-cli`
- Worker wave integration and Reviewer packet: `wave-integration`
- Engineering validation depth: `engineering-quality-baselines`
- Long-horizon audit (five-step lens, non-standard-flow only): `engineering-quality-baselines` -> `references/long-horizon-audit.md`
- Git safety and commit chunking: `git-workflow`
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

Pause planned execution and ask for confirmation when a new insight materially changes the plan, such as:

- UI behavior differs from assumptions;
- a new approach has meaningful tradeoffs;
- required changes expand `owns` significantly;
- additional modules are affected;
- a requirement, component, or process step appears not to need to exist, or planned work is optimizing something unjustified;
- a new security, performance, data correctness, or validation risk appears.

Record replans in the plan Decision Log before continuing.

## Governance And Safety

- Correction events require `improvement-loop` before ending the turn. State durable behavior changes back to the user unless explicitly one-time.
- Use `workspace-troubleshooting` for command failures, Windows locks, stale branch/view state, external changes, and systematic tool triage.
- Use `skills-maintenance` for first-party skill governance. Third-party or unknown-provenance skills are read-only unless the user explicitly approves editing them.
- Use `git-workflow` for branch safety, commit chunking, and non-interactive Git defaults. Shared-state Git mutations stay Orchestrator-controlled unless explicitly delegated.
- Use `rulebook` for repo rule updates. Only the Orchestrator edits repo rule files.

## Final Response Summary

Final responses should state:

1. Outcome: done or blocked.
2. Changed files/artifacts.
3. Validation summary.
4. Review summary, including Reviewer status and UI/E2E evidence if run.
5. Repo rule updates.
6. Skill staging updates.
7. Open questions/blockers, max 3.
