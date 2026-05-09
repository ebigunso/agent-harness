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

# ADR-D-0003: Keep Logical Roles Stable While Namespacing Runtime Agent Identities

## Context and Problem Statement

The harness uses four logical roles: Orchestrator, Researcher, Worker, and Reviewer. Plans, skills, and governance docs should use those logical role names consistently.

Runtime platforms may also ship built-in or predefined agents with generic names such as `worker`. Using generic physical names everywhere can create ambiguity or collisions. Existing Copilot agent names are already public and should be preserved in this pass unless a migration plan is added.

## Decision Drivers

- Keep shared planning and skill semantics stable.
- Avoid collisions with platform-provided agent names.
- Preserve existing public Copilot physical names.
- Make runtime-specific physical names explicit and documented.

## Decision

Logical roles remain stable:

- Orchestrator
- Researcher
- Worker
- Reviewer

Physical agent names may differ by runtime. New physical names should be namespaced where collisions are plausible. Do not rely on generic names such as `worker` in runtimes where platform-provided agents or user agents could collide.

The canonical role mapping lives in `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/runtime-role-map.md`.

## Considered Options

1. Force every runtime to use generic physical names.
2. Rename all existing physical agents to namespaced names immediately.
3. Keep logical role names stable and document runtime-specific physical names.

## Decision Outcome

Chosen option: **Option 3**.

This preserves public compatibility while documenting namespacing as the preferred path for new runtime agent identities.

## Consequences

### Positive

- Plans and skills can use stable logical roles.
- Runtime adapters can avoid physical-name collisions.
- Existing Copilot users do not need a migration for this change.

### Negative / Tradeoffs

- Maintainers must consult the role map when editing runtime adapters.
- Documentation must distinguish logical role names from physical runtime names.

## Validation

- Verify runtime role map entries match actual adapter/template files.
- Verify plans and shared skills use logical roles, not runtime-specific physical names.
- Verify new runtime agent identities prefer namespaced names unless a compatibility reason exists.

## Revisit When

- A runtime adds collision-free namespacing or unique role binding independent of physical filenames.
- A future release intentionally migrates existing public physical names.

## More Information

- `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/runtime-role-map.md`
- `plugins/coding-agent-orchestration-harness/agents/`
- `plugins/coding-agent-orchestration-harness/claude/agents/`
- `plugins/coding-agent-orchestration-harness/codex/agent-templates/`
