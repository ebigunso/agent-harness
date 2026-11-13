---
status: proposed
adr_type: design
date: 2026-11-14
deciders: ["ebigunso"]
consulted: ["GPT-5.5 Pro", "Claude Fable 5.1", "Claude Fable 5.2"]
informed: []
supersedes: ["ADR-D-0020-loader-routed-sessions-assume-the-orchestrator-role.md", "ADR-D-0037-a-session-role-is-entered-by-an-explicit-act-of-the-person-opening-it.md"]
superseded_by: null
---

# ADR-D (not yet numbered): A session holds a session role only by its opener's choice or by the default; a skill loaded by a description match gives none, and no installed text makes a session the Orchestrator unchosen

## Context and Problem Statement

Terms used here: a session role is a role a session itself holds, the Orchestrator's or Counsel's. The opener is whoever opens the session, a person or a session acting for one. The default is the role a session holds when its opener chose none (`ADR-D-a-session-opened-with-no-role-chosen-is-counsel.md`).

Every runtime the harness supports discovers skills by their descriptions and may load one on its own when a request seems to match, and a harness installs text that a session reads before anyone has chosen anything. ADR-D-0020 held that a session with the orchestration workflow in context is the Orchestrator for a coding task, whatever routed it there, so that the workflow's gates would bind somebody. With a default role, that makes the role of a person's session depend on what they happened to type: a coding request would take them out of the conversation the default gives them. The fork is whether a role follows the text a session has in context or only what its opener chose.

## Decision

- A session holds a session role only by its opener's choice or by the default.
- A skill loaded because its description matched gives a session no role, and neither does a passing reference to a role's skill.
- No text the harness installs makes a session the Orchestrator unless its opener chose that.

## Why

A description match is nobody's choice, and it fails silently: a session that was meant to run under a role and did not simply goes on without that role's gates, and one given a role by a match holds gates nobody asked it to hold. A person who chose nothing is owed the default conversation (the product philosophy's "Who it is for"), and a role that turns on the wording of a request hands them the Orchestrator's level of plans without their knowing a choice was made.

## Rejected Alternatives

- A session that has the Orchestrator's workflow in context is the Orchestrator, whatever routed it there, as ADR-D-0020 had it: it lost because a match or a line of installed text then decides the role in place of the opener; reopen if a supported runtime is found where an opener's choice of the Orchestrator cannot be told from a load nobody chose.
- Rely on automatic skill discovery to start a role: it lost because an automatic activation fails silently; reopen if a runtime documents deterministic activation of a named skill.
- Make every support skill self-sufficient as a way into a role: rejected outright; it multiplies the workflow across skills against ADR-D-0049.

## Decision Boundary

Not covered: the forms an opener's choice takes (`ADR-D-either-session-role-is-the-openers-to-choose.md`); which role the default is; that a session holding one role never takes the other (ADR-D-0034); which rule files an Orchestrator session reads when it starts, which the Orchestrator's skill states; how skill descriptions and installed text are worded; that harness text holds none of the user's authority (ADR-D-0017).

## Validation

The decision is broken where a session nobody opened as the Orchestrator plans, dispatches or applies the Orchestrator's gates because a skill matched or because installed text sent a request there; or where a session is taken to hold a role because that role's skill is in its context.

## Revisit When

- A runtime provides deterministic, documented activation of a named skill (neither GitHub Copilot nor Claude Code did on 2026-09-07).
- The premise that a role held by instruction text alone is honoured fails. In Codex nothing in the runtime fixes a session's role (seen 2026-11-12), and on 2026-11-13 a Codex home that still held text installed before this decision sent a coding request to the Orchestrator's skill in a repository without the default, in one run. A session found acting as the Orchestrator unchosen with the text of this decision installed reopens this record.

## More Information

Replaces ADR-D-0020 in full, reversing it: a session routed to the orchestration workflow by installed text is no longer the Orchestrator for that reason. Dropped from ADR-D-0020: the list of rule files an Orchestrator session loads, which the Orchestrator's skill states and which is not a decision of record. With `ADR-D-a-session-opened-with-no-role-chosen-is-counsel.md` and `ADR-D-either-session-role-is-the-openers-to-choose.md`, replaces ADR-D-0037 in full; carried here from it: that a description match is never the way into a role, and that no support skill presents itself as one. Source of intent: the brief "One conversation with Counsel", "One conversation" and "Limits". Related: ADR-D-0049 (one home per session role).
