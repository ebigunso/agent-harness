---
status: proposed
adr_type: design
date: 2026-09-07
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1"]
informed: []
supersedes: ["ADR-D-0002-explicit-orchestrator-entrypoint.md"]
superseded_by: null
---

# ADR-D-0023: Where a runtime offers agent selection, the harness is entered by selecting the Orchestrator

## Context and Problem Statement

GitHub Copilot and Claude Code let the user pick an agent for the session, and both also discover skills by description and may load one on their own when a request seems to match. The harness needs a session to be running under the Orchestrator role before any plan gate or delegation rule applies. The fork is whether that entry is an explicit user selection or a skill's automatic activation.

## Decision

In a runtime that offers agent selection, the harness is entered by selecting the Orchestrator agent. Automatic skill activation is never the entry mechanism: support skills are capability modules whose descriptions serve discovery and assistance, and no support skill claims to be the harness entrypoint. Runtimes without agent selection enter through the loader route governed by ADR-D-0020.

## Why

A session that was supposed to run the harness but did not simply proceeds without gates, and nothing reports the omission; an explicit selection fails visibly, an auto-trigger fails silently.

## Rejected Alternatives

- Rely on automatic skill discovery to start the harness: reopen if a runtime documents deterministic activation for a named skill.
- Make every support skill self-sufficient as an entrypoint: rejected outright; it multiplies the workflow across skills against ADR-D-0022.

## Decision Boundary

Invariant: in a runtime with agent selection, no path into the harness other than selecting the Orchestrator is relied on or documented as one.

Not covered: what the Orchestrator adapter says once selected, how skill descriptions are worded, and the loader route for runtimes without selection.

## Validation

- Runtime documentation and adapters describe explicit Orchestrator selection as the way in.
- Support skill descriptions describe capabilities and do not present themselves as the harness entrypoint.

## Revisit When

- A runtime provides deterministic, documented activation of a named skill from a selected agent (neither Copilot nor Claude Code did on 2026-09-07).

## More Information

Replaces ADR-D-0002 in full. Loader-routed sessions: ADR-D-0020. Single home of workflow mechanics: ADR-D-0022.
