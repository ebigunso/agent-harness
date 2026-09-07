---
status: accepted
adr_type: design
date: 2026-09-06
deciders: ["ebigunso"]
consulted: ["GPT-5.5 Pro", "Claude Fable 5.1"]
informed: []
supersedes: ["superseded/ADR-D-0008-codex-explicit-subagent-authorization-and-async-dispatch-lifecycle--superseded-by-ADR-D-0020.md"]
superseded_by: null
---

# ADR-D-0020: Loader-routed sessions assume the Orchestrator role

## Context and Problem Statement

Codex enters the harness through a managed `AGENTS.md` block that loads `$orchestration-harness` without selecting a physical Orchestrator agent. A session routed that way has the workflow policy in context but no role, and on 2026-05-17 the main Codex thread was observed skipping `docs/coding-agent/rules/orchestrator.md` for that reason. This record was first decided on 2026-05-17 as part of ADR-D-0008 and is restated here on its own after that record was retired.

## Decision

Once `$orchestration-harness` is loaded for a coding task, the main-thread agent assumes the logical Orchestrator role for that task, whatever routed it there. For repository coding tasks it performs the minimal rule load, `docs/coding-agent/rules/index.md`, `common.md`, and `orchestrator.md` when present, as instruction loading only; rule-suite lifecycle, bootstrap, refresh, and repair stay behind their own triggers.

## Why

Role follows the policy in context, not the agent selector; a session that holds the Orchestrator policy must hold the Orchestrator obligations, or the gates bind nobody.

## Rejected Alternatives

- Put the role and rule-loading mechanics in the loader block: duplicates workflow text outside the canonical skill (ADR-D-0001, ADR-I-0002 keep the loader loader-only).

## Decision Boundary

Invariant: a loader-routed session is the Orchestrator for the task and loads the three rule files when they exist.

Not covered: the loader's wording (ADR-D-0017 forbids authority claims) and the rule-suite lifecycle triggers, which live in `orchestration-harness` references.

## Validation

`orchestration-harness/SKILL.md` states the role assumption and the minimal rule load; the Codex loader snippet stays loader-only.

## Revisit When

Codex selects a physical Orchestrator agent on loader routing, making the assumption redundant, or the rule-suite entry files change.
