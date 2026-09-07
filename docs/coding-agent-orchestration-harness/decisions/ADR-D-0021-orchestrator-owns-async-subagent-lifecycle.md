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

# ADR-D-0021: The Orchestrator owns the async subagent lifecycle

## Context and Problem Statement

Codex runs subagents asynchronously or as background processes. A child that has delivered its final report may stay open and idle, and a parent that reads silence as failure duplicates the work or terminates the child early. This record was first decided on 2026-05-17 as part of ADR-D-0008 and is restated here on its own after that record was retired.

## Decision

In runtimes where subagents run asynchronously, the Orchestrator owns dispatch tracking, dependency-aware waiting, final-report validation and integration, and the cleanup, close, or termination of completed child processes where the runtime exposes such an action. A final subagent report means the assignment is complete; an open idle process afterwards is an Orchestrator cleanup concern and never a reason to change subagent behavior. Where no close action exists, the idle process is recorded as unavailable for cleanup and not reused for unrelated work.

## Why

Only the parent knows which children are still needed; a child cannot tell whether its silence is being waited on or misread.

## Rejected Alternatives

- Make subagent templates close themselves after the final report: the subagent already completed its assignment by reporting; process cleanup is the parent's concern, and self-exit races the report handoff.

## Decision Boundary

Invariant: subagents finish by reporting, never by exiting; the Orchestrator waits, integrates, and cleans up.

Not covered: waiting patience, checkpoint prompts, and per-runtime close mechanics, which live in `subagent-strategy/references/async-dispatch-lifecycle.md`.

## Validation

Worker, Researcher, and Reviewer templates contain no self-termination step; `async-dispatch-lifecycle.md` assigns waiting and cleanup to the Orchestrator.

## Revisit When

A runtime makes child processes exit on final report by itself, or adds a synchronous dispatch mode that removes the idle-child state.
