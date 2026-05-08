---
status: accepted
adr_type: design
date: 2026-05-09
deciders:
  - ebigunso
consulted:
  - GPT-5.5
informed: []
supersedes: []
superseded_by: null
---

# ADR-D-0001: Keep Harness Workflow Mechanics In The Orchestration Skill

## Context and Problem Statement

The coding-agent orchestration harness is consumed by multiple runtimes: GitHub Copilot, Claude Code, and Codex. Each runtime has different discovery rules, agent metadata formats, and instruction-loading behavior. If workflow mechanics are copied into `AGENTS.md`, runtime adapters, README sections, or bootstrap snippets, those copies will drift and agents may follow stale planning, delegation, validation, or reporting rules.

At the same time, `SKILL.md` files are runtime instructions for agents. They should not carry long maintainer rationale or implementation notes that are only useful when modifying the harness itself.

## Decision Drivers

- Keep one canonical runtime policy for planning, delegation, validation, review, rule updates, and final reporting.
- Avoid duplicated workflow mechanics across runtime-specific adapter files.
- Keep runtime skill contents lean and directly actionable for agents.
- Preserve maintainer rationale somewhere stable without polluting runtime instructions.

## Decision

The runtime workflow mechanics for the harness live in `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/SKILL.md`.

Other files may route agents to that skill, but they must not restate the harness workflow. Design rationale for this arrangement lives in plugin-scoped ADRs under `docs/coding-agent-orchestration-harness/decisions/`.

`SKILL.md` may include concise runtime precedence language, but maintainer-facing rationale belongs in ADRs.

## Considered Options

1. Duplicate the workflow in every runtime adapter.
2. Put workflow mechanics in `AGENTS.md`.
3. Keep workflow mechanics in the orchestration skill and store design rationale in ADRs.

## Decision Outcome

Chosen option: **Option 3**.

This keeps agent-facing runtime instructions centralized while preserving design history outside the skill body. Runtime adapters and bootstrap snippets can stay small, and future maintainers can still inspect the ADRs to understand why the structure exists.

## Consequences

### Positive

- Runtime agents have one canonical workflow policy to follow.
- `AGENTS.md` and runtime adapters remain loader/adapter surfaces instead of policy copies.
- Maintenance rationale is retained without adding meta-instructions to agent runtime prompts.

### Negative / Tradeoffs

- Maintainers must know to check ADRs for architectural rationale.
- The skill frontmatter and body must remain clear enough that agents reliably load and apply it.

## Validation

- Review `AGENTS.md` snippets and runtime adapters for loader-only wording.
- Search for duplicated plan gates, validation gates, and reporting contracts outside `orchestration-harness/SKILL.md`.
- Review `orchestration-harness/SKILL.md` for runtime-focused language rather than maintainer rationale.

## Revisit When

- A runtime adds a first-class way to declare shared instruction dependencies without loader text.
- Agents stop reliably loading or applying the orchestration skill from loader-only instructions.
- The harness splits into multiple independent workflows that no longer share one source of runtime policy.

## More Information

- `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/SKILL.md`
- `plugins/coding-agent-orchestration-harness/codex/snippets/AGENTS.md`
