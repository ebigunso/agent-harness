---
status: accepted
adr_type: design
date: 2026-09-06
deciders: ["ebigunso"]
consulted: ["GPT-5.5 Pro", "Claude Fable 5.1"]
informed: []
warrant:
  warranted_by: "without this record, future work would likely treat a loader-routed Codex session as a plain assistant that happens to have read a skill, skipping the Orchestrator's repository rules and gates because no physical Orchestrator agent was selected"
  detected_signals: "cross-boundary identity shape (which role a session holds); rejected alternative likely to be re-proposed (loader carrying the workflow)"
  cost_of_violation: "a session that does not know it is the Orchestrator plans and dispatches without the Orchestrator rules, and the miss is invisible until review"
  cost_of_over_extension: "loading the full rule-suite lifecycle on every task; only the three rule files are loaded here"
supersedes: ["superseded/ADR-D-0008-codex-explicit-subagent-authorization-and-async-dispatch-lifecycle--superseded-by-ADR-D-0021.md"]
superseded_by: null
supersession_scope: full
---

# ADR-D-0021: Loader-routed sessions assume the Orchestrator role

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
