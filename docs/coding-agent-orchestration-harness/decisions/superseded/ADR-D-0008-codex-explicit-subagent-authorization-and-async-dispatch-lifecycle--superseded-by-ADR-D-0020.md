---
status: superseded
adr_type: design
date: 2026-05-17
deciders:
  - ebigunso
consulted:
  - GPT-5.5 Pro
informed: []
supersedes: []
superseded_by: ADR-D-0020-loader-routed-sessions-assume-the-orchestrator-role.md
supersession_scope: full
---

# ADR-D-0008: Codex Explicit Subagent Authorization, Orchestrator Identity, And Async Dispatch Lifecycle

> Retired on 2026-09-06. This record bundled three decisions. The loader-authority clause is replaced by ADR-D-0017 (harness text holds no user authority); the Orchestrator-identity and rule-load clauses by ADR-D-0020; the async child lifecycle by ADR-D-0021.

## Context and Problem Statement

Codex can enter the harness through a managed `AGENTS.md` loader block that directs the current session to load `$orchestration-harness`. That loader route is intentionally lightweight and may not select a physical Orchestrator custom agent.

This creates three related Codex runtime risks:

- the main Codex thread may not recognize that loading `$orchestration-harness` is explicit user direction to follow the harness workflow, including bounded harness subagent dispatch when required;
- the main Codex thread may not consistently recognize itself as the logical Orchestrator and may skip repository Orchestrator rules such as `docs/coding-agent/rules/orchestrator.md`;
- Codex subagents run asynchronously or as background processes, so the parent thread may become impatient, duplicate active child work, or leave completed child processes open after final reports.

These are Orchestrator-side runtime workflow issues. They do not require changing Researcher, Worker, or Reviewer templates to keep working or stop after a final report.

## Decision Drivers

- Preserve `orchestration-harness/SKILL.md` as the canonical runtime workflow policy.
- Keep the Codex `AGENTS.md` snippet loader-only.
- Make Codex loader-routed sessions assume the logical Orchestrator role for coding tasks.
- Ensure repository Orchestrator rules are loaded when a repository rule suite is present.
- Keep minimal rule instruction loading separate from lifecycle, readiness, bootstrap, and refresh work.
- Keep async/background dispatch mechanics behind progressive-disclosure references.
- Make completed async child cleanup an Orchestrator responsibility when the runtime exposes a close or terminate action.

## Decision

Using the managed Codex loader or otherwise invoking `$orchestration-harness` for a coding task is explicit user direction to follow the harness workflow, including bounded harness subagent dispatch when the harness requires it, unless the user explicitly disables subagents.

Runtime loaders may route an agent into `$orchestration-harness` without selecting a physical Orchestrator agent. Once the skill is loaded for a coding task, the current main-thread agent assumes the logical Orchestrator role for that task. This includes Codex sessions routed by the managed `AGENTS.md` loader.

For repository coding tasks, the Orchestrator performs a minimal repository rule load when a repository rule suite is present:

- `docs/coding-agent/rules/index.md`
- `docs/coding-agent/rules/common.md`
- `docs/coding-agent/rules/orchestrator.md`

This is rule instruction loading, not full rule-suite lifecycle or readiness work. `_lifecycle.json`, bootstrap, refresh, repair, and `rulebook` remain behind the Rule Suite Fast Path and task-specific lifecycle triggers.

In async/background runtimes such as Codex, the Orchestrator owns child-process lifecycle:

- dispatch tracking;
- dependency-aware waiting;
- final-report validation and integration;
- cleanup, close, or termination of completed runtime child processes when the platform exposes such an action.

A final subagent report means the assignment is complete. The runtime child process may still remain open in an idle state. That open idle process is an Orchestrator cleanup concern, not a reason to change subagent work behavior.

Detailed runtime behavior belongs behind progressive-disclosure references, not in a large Codex-specific block inside the top-level orchestration skill.

## Considered Options

### Option 1: Put Codex role and rule-loading mechanics in the loader

This would make the behavior visible to Codex immediately, but it would duplicate workflow mechanics in `AGENTS.md` and violate the loader-only architecture.

Rejected because ADR-D-0001 keeps canonical workflow mechanics in `orchestration-harness/SKILL.md`, and ADR-I-0002 keeps the Codex `AGENTS.md` block loader-only.

### Option 2: Change Codex subagent templates to close themselves after final reports

This treats idle-open child processes as a subagent behavior issue.

Rejected because the subagents already complete their assignments by emitting final reports. Runtime process cleanup belongs to the parent Orchestrator.

### Option 3: Add exact-word validators for Codex authorization and lifecycle language

This could catch accidental prose removal, but it would make skill wording brittle and overfit to current phrasing.

Rejected because the repository rules prefer review for wording and prompt-bloat concerns unless a structural packaging contract is at risk.

### Option 4: Keep loader-only routing and clarify Orchestrator-owned behavior in skills and references

Chosen. The Codex loader receives only concise authorization language. Orchestrator identity, minimal repository-rule entry, and async dispatch routing live in `orchestration-harness/SKILL.md`. Detailed async lifecycle mechanics live under `subagent-strategy/references/`.

## Decision Outcome

Chosen option: **Option 4**.

The harness keeps Codex loader text small while making `$orchestration-harness` responsible for:

- recognizing the current main thread as the logical Orchestrator when loaded through a runtime loader;
- loading repository `common.md` and `orchestrator.md` rules when a rule suite is present;
- routing async/background lifecycle mechanics to progressive-disclosure references;
- treating completed child-process cleanup as parent-owned lifecycle work.

## Consequences

### Positive

- Codex loader-routed sessions have a clear Orchestrator identity without duplicating role mechanics in the loader.
- Repository Orchestrator rules are less likely to be skipped.
- Trivial work still avoids full rule lifecycle, bootstrap, and refresh rituals.
- Async/background subagent behavior is handled by Orchestrator dispatch tracking, waiting, integration, and cleanup.
- Subagent templates remain focused on their assignments and report contracts.

### Negative / Tradeoffs

- The orchestration skill gains a small always-loaded repository-rule entry section.
- Orchestrators must distinguish minimal rule instruction loading from lifecycle/readiness checks.
- Runtimes without close or terminate actions can only record cleanup as unavailable.

## Implementation Impact

- `orchestration-harness/SKILL.md` clarifies runtime-loader Orchestrator identity.
- `orchestration-harness/SKILL.md` adds a minimal repository rule entry step before detailed gates.
- `orchestration-harness/SKILL.md` routes async/background dispatch lifecycle details to `subagent-strategy/references/async-dispatch-lifecycle.md`.
- `subagent-strategy/SKILL.md` links to the new async lifecycle reference.
- `wave-integration/SKILL.md` includes completed async/background child cleanup.
- `codex/snippets/AGENTS.md` keeps loader-only architecture and receives only bounded-dispatch authorization language.
- Codex Researcher, Worker, and Reviewer TOML templates are unchanged for idle-open process behavior.

## Validation

Validate with:

```bash
python scripts/validate_harness_package.py
python scripts/run_validation_smoke_tests.py
```

Additional validation:

- Review the Codex loader snippet to confirm it does not duplicate role details, rule-loading algorithms, plan gates, validation gates, or report schemas.
- Review `orchestration-harness/SKILL.md` to confirm Repository Rule Entry remains a minimal rule instruction load and does not require `_lifecycle.json` for ordinary work.
- Review Codex subagent templates to confirm they were not changed for this idle-open process issue.

## Revisit When

- Codex changes how it authorizes or represents background child agents.
- Codex exposes stronger lifecycle APIs for child process close or termination.
- The harness introduces a durable manifest for runtime references that can support structural validation without exact prose checks.
- Runtime loaders gain first-class role binding that removes the need for skill-level Orchestrator identity clarification.

## More Information

- `docs/coding-agent-orchestration-harness/decisions/ADR-D-0001-canonical-harness-workflow-location.md`
- `docs/coding-agent-orchestration-harness/decisions/ADR-I-0002-codex-bootstrap-and-loader-strategy.md`
- `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/SKILL.md`
- `plugins/coding-agent-orchestration-harness/skills/subagent-strategy/SKILL.md`
- `plugins/coding-agent-orchestration-harness/skills/subagent-strategy/references/async-dispatch-lifecycle.md`
- `plugins/coding-agent-orchestration-harness/skills/wave-integration/SKILL.md`
- `plugins/coding-agent-orchestration-harness/codex/snippets/AGENTS.md`
