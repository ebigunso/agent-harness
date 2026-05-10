---
status: accepted
adr_type: design
date: 2026-05-09
deciders:
  - ebigunso
consulted:
  - GPT-5.5 Pro
informed: []
supersedes: []
superseded_by: null
---

# ADR-D-0002: Treat The Orchestrator As The Explicit Harness Entrypoint

## Context and Problem Statement

GitHub Copilot and Claude Code expose user-selectable agents. In those runtimes, harness users are expected to explicitly choose the Orchestrator as the main-thread agent for coding work that needs planning, delegation, validation, review, or governance.

The harness also ships support skills. Those skills must have useful descriptions and should remain discoverable, but they are capability modules rather than the primary runtime entrypoint for Copilot and Claude Code.

## Decision Drivers

- Preserve a clear main-thread controller for non-trivial work.
- Avoid depending on exact automatic skill-trigger behavior as the main reliability mechanism.
- Keep support skills focused and reusable.
- Allow runtime adapters to carry a small operating kernel because the Orchestrator is explicitly selected.

## Decision

GitHub Copilot and Claude Code users explicitly select the Orchestrator as the main thread agent when using the harness workflow.

Support skills are capability modules. Their descriptions should remain accurate and useful, but exact auto-trigger behavior is not the primary reliability mechanism in Copilot or Claude Code.

Runtime Orchestrator adapters may include a small operating kernel that routes to the canonical orchestration skill, names hard gates, and identifies physical subagents. They must not duplicate the full workflow mechanics owned by `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/SKILL.md`.

## Considered Options

1. Depend primarily on automatic skill discovery.
2. Put full workflow instructions in every runtime adapter.
3. Treat Orchestrator selection as explicit and keep adapters as small kernels.

## Decision Outcome

Chosen option: **Option 3**.

Explicit Orchestrator invocation gives the harness a stable entrypoint while keeping support skills modular and avoiding large duplicated runtime prompts.

## Consequences

### Positive

- Users and maintainers have a clear agent to invoke for harness work.
- Runtime adapters can stay concise while still providing enough operating context.
- Support skills can evolve as capability modules without becoming accidental entrypoints.

### Negative / Tradeoffs

- Users must know to choose the Orchestrator in Copilot and Claude Code.
- Skill descriptions still matter for assistance and discoverability, but they are not the main activation contract.

## Validation

- Verify Copilot and Claude documentation describe explicit Orchestrator selection.
- Verify runtime adapters route to `orchestration-harness` instead of duplicating the full workflow.
- Verify support skill descriptions describe capabilities without claiming to be the main harness entrypoint.

## Revisit When

- A runtime provides reliable first-class dependency loading from a selected agent to shared skills.
- Automatic skill discovery becomes deterministic enough to replace explicit Orchestrator invocation.

## More Information

- `plugins/coding-agent-orchestration-harness/agents/Orchestrator.md`
- `plugins/coding-agent-orchestration-harness/claude/agents/harness-orchestrator.md`
- `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/SKILL.md`
