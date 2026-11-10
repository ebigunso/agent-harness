---
status: proposed
adr_type: design
date: 2026-11-11
deciders: ["ebigunso"]
consulted: []
informed: []
supersedes: ["ADR-D-0020-loader-routed-sessions-assume-the-orchestrator-role.md"]
superseded_by: null
---

# ADR-D-0072: A session that a repository's installed loader routes to the Orchestrator's policy holds the Orchestrator role, and the role comes from that routing, not from the policy being in context

## Context and Problem Statement

Terms used here: the Orchestrator is the session role that plans, dispatches and reports the work. Its policy is the skill text that states what the role must do. A loader is a block of instructions that a person installs in a repository or a user account and that sends a session to the Orchestrator's policy for coding tasks, without selecting an agent.

ADR-D-0037 holds that a session takes a session role by an explicit act of the person opening it, and leaves to this record the runtime that offers no such act for the Orchestrator. Codex was that runtime when ADR-D-0037's facts were checked on 2026-10-01: it reaches the harness through an installed loader, which puts the Orchestrator's policy in the session's context and selects no agent. On 2026-05-17 the main Codex thread, routed that way, was seen to skip the Orchestrator's repository rules, because it held the policy and no role. The fork is whether a session routed by the loader is the Orchestrator, and if it is, whether the role comes from the loader's routing or from the policy being in the session's context.

## Decision

- A session that an installed loader routes to the Orchestrator's policy for a coding task holds the Orchestrator role for that task, with every obligation the role carries.
- The role comes from the routing a person installed. The policy being in a session's context does not by itself make the session the Orchestrator; apart from this route, the ways into the role are the ones ADR-D-0037 names.

## Why

A session that follows the Orchestrator's policy without holding the role proceeds while the role's gates and rules bind nobody, and nothing reports the omission. Tying the role to the installed routing keeps the entry a deliberate one: someone chose to install the loader, whereas a policy can arrive in a session's context on a description match that nobody chose.

## Rejected Alternatives

- Any session with the Orchestrator's policy in context takes the role, whatever brought the policy there: it lost because a load by description match would then make a session the Orchestrator with nobody having chosen it, which ADR-D-0037 decides against; it reopens only with that record.
- The role and its obligations written into the loader itself: it lost because that states the Orchestrator's workflow outside its one home, against ADR-D-0049; rejected outright.

## Decision Boundary

Invariant: a loader-routed session is the Orchestrator for the task and holds the role's obligations; the role follows from the installed routing, never from the policy's presence in context alone.

Not covered: what the Orchestrator's obligations are and how a session takes them up, including which repository rules it reads and when; the loader's wording (ADR-D-0017) and how it is installed; every other way into a session role (ADR-D-0037).

## Validation

- The Orchestrator's policy states that a loader-routed session holds the role, and that a load by description match or an incidental reference does not confer it.
- Review of a change to the loader or to the policy's entry text asks: does a loader-routed session still hold the role and its obligations, and does anything other than the installed routing or an act ADR-D-0037 names confer the role?

## Revisit When

- Codex offers the person opening a session a way to open it as the Orchestrator's agent, so that the loader route is no longer needed (it offered none on 2026-10-01, the date of the check ADR-D-0037 records).

## More Information

Replaces ADR-D-0020 in full. What it decided for a loader-routed session is carried. Its statement that the role is assumed whatever routed the session to the policy is not carried: ADR-D-0037 decides the ways into a session role. Its list of the repository rule files the Orchestrator reads is the policy's own text and is not part of this record. Related: ADR-D-0037 (ways into a session role), ADR-D-0049 (one home for each session role's workflow mechanics), ADR-D-0017 (harness text holds no user authority).
