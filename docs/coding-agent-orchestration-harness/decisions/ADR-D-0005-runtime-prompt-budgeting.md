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

# ADR-D-0005: Let Runtime Adapters Diverge For Prompt Budget

## Context and Problem Statement

The harness supports GPT-oriented runtimes, Claude Code, and Codex. These runtimes do not have identical instruction-loading behavior, prompt budget sensitivity, or agent metadata conventions.

Forcing one long Orchestrator prompt shape across all runtimes would increase drift risk and weaken adherence in runtimes that perform better with shorter agent definitions and progressive references.

## Decision Drivers

- Preserve shared semantics across runtimes.
- Avoid overlong runtime adapters where shorter kernels work better.
- Keep Codex loader instructions small and bootstrap-owned.
- Avoid duplicating full workflow mechanics into every adapter.

## Decision

Runtime adapters may differ in prompt length and wording while preserving shared semantics through the shared skill tree.

- GPT-oriented adapters may carry a medium-length Orchestrator kernel.
- Claude adapters should use a shorter kernel plus references/skills.
- Codex should keep loader-style instructions plus installed role templates.
- Shared workflow mechanics remain consolidated in `orchestration-harness` and its references.

## Considered Options

1. Use one identical Orchestrator body for every runtime.
2. Make every adapter loader-only with almost no local kernel.
3. Use runtime-specific kernels that route to shared skills and references.

## Decision Outcome

Chosen option: **Option 3**.

This keeps shared behavior centralized while allowing each runtime adapter to fit its model and tool behavior.

## Consequences

### Positive

- Claude can keep a shorter prompt surface.
- Copilot can retain a medium operating kernel for explicit selection.
- Codex stays aligned with the accepted loader/bootstrap strategy.

### Negative / Tradeoffs

- Adapter validation must allow wording differences.
- Maintainers must avoid interpreting prompt divergence as semantic divergence.

## Validation

- Verify runtime adapters point to `orchestration-harness` instead of duplicating the full workflow.
- Verify Claude Orchestrator stays materially shorter than the Copilot Orchestrator.
- Verify Codex `AGENTS.md` snippets remain loader-only.

## Revisit When

- Runtime instruction-loading behavior changes materially.
- The harness gains a generated-adapter system that can preserve semantics while emitting runtime-specific prompt shapes.

## More Information

- `docs/coding-agent-orchestration-harness/decisions/ADR-D-0001-canonical-harness-workflow-location.md`
- `docs/coding-agent-orchestration-harness/decisions/ADR-I-0002-codex-bootstrap-and-loader-strategy.md`
- `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/SKILL.md`
