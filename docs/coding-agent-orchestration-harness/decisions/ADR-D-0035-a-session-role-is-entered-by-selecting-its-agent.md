---
status: proposed
adr_type: design
date: 2026-09-30
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1"]
informed: []
supersedes: ["ADR-D-0023-the-harness-is-entered-by-selecting-the-orchestrator.md"]
superseded_by: null
depends_on: ["ADR-D-0020-loader-routed-sessions-assume-the-orchestrator-role.md", "ADR-D-0034-counsel-is-a-separate-session-at-the-level-of-behaviour-and-decisions.md"]
---

# ADR-D-0035: Where a runtime offers agent selection, a session role (Orchestrator or Counsel) is taken by explicitly selecting that role's agent; a skill's activation by description match is never the way into one

## Context and Problem Statement

GitHub Copilot and Claude Code let the person opening a session pick an agent for it, and both also discover skills by description and may load one on their own when a request seems to match. Two harness roles are held by a session itself: the Orchestrator, whose plan gates and delegation rules apply only to a session running under that role, and Counsel, whose limits hold only in a session opened as Counsel. For Counsel the person opening the session is the owner, the person whose product the work serves (ADR-D-0034). The fork is whether a session comes to hold such a role by an explicit selection or by a skill's automatic activation.

## Decision

In a runtime that offers agent selection, a session takes a session role, Orchestrator or Counsel, by the person opening the session explicitly selecting that role's agent. In a runtime without agent selection, Counsel's role is taken by that person explicitly invoking the `counsel` skill, which holds Counsel's policy; the Orchestrator's route in such a runtime is the loader route, which ADR-D-0020 governs and this record does not. A skill's activation by description match is never the way into a session role: support skills, meaning every skill other than the ones that hold a session role's policy, are capability modules whose descriptions serve discovery and assistance, and no support skill presents itself as the way into a session role.

## Why

A session that was supposed to run under a role but did not simply proceeds without that role's gates or limits, and nothing reports the omission; an explicit selection fails visibly, an auto-trigger fails silently.

## Rejected Alternatives

- Rely on automatic skill discovery to start a role: reopen if a runtime documents deterministic activation for a named skill.
- Make every support skill self-sufficient as an entrypoint: rejected outright; it multiplies the workflow across skills against ADR-D-0022.

## Decision Boundary

Invariant: in a runtime with agent selection, no way into a session role other than explicitly selecting that role's agent is relied on or documented as one; in a runtime without it, no way into Counsel's role other than the person opening the session explicitly invoking the `counsel` skill is relied on or documented as one.

Not covered: what an adapter says once selected; how skill descriptions are worded; the Orchestrator's loader route in runtimes without agent selection (ADR-D-0020); what each session role may do.

## Validation

- For a runtime with agent selection, runtime documentation and adapters describe explicit selection of the role's agent as the way in.
- For a runtime without agent selection, runtime documentation describes explicit invocation of the `counsel` skill as the way into Counsel's role, and the loader does not route to that skill.
- Support skill descriptions describe capabilities and do not present themselves as the way into a session role.

## Revisit When

- A runtime provides deterministic, documented activation of a named skill from a selected agent (neither GitHub Copilot nor Claude Code did on 2026-09-07).

## More Information

Replaces ADR-D-0023 in full: what it decided for the Orchestrator is unchanged, and the same rule is stated for Counsel, the second role a session itself holds. Loader-routed sessions: ADR-D-0020. Single home of workflow mechanics: ADR-D-0022. Counsel: the record on Counsel (ADR-D-0034).
