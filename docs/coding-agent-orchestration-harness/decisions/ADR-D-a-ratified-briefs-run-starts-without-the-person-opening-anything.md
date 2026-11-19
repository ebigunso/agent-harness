---
status: proposed
adr_type: design
date: 2026-11-14
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.2"]
informed: []
supersedes: []
superseded_by: null
---

# ADR-D (not yet numbered): When the person directing the work ratifies a brief, its run starts without that person opening anything

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session role that person talks with about what the product does or should do. The Orchestrator is the session role that plans, dispatches and reports the work. A run is the work done under one ratified brief.

The person directing the work is asked for what they want and for their judgement of what they got, and for nothing about how agents are organised to do it. The grounds for a piece of work pass from Counsel to an Orchestrator session as a ratified brief (ADR-D-0034). Where that person has to open the Orchestrator session and hand the brief over in it, ratifying does not get the work begun: they must know of the Orchestrator role, open a session in it, and carry the brief into it. The fork is whether ratifying a brief is the last thing asked of that person before the work begins, or the first of several.

## Decision

- When the person directing the work ratifies a brief, its run starts without that person opening, starting or carrying anything.
- Getting the run started is Counsel's work. The run is done by a session that holds the Orchestrator role, never by Counsel and never inside Counsel's session.
- Where a run could be started but not reached by Counsel afterwards, Counsel says so plainly and starts none.

## Why

The product philosophy's "Who it is for" rules out a design that works only if the person understands a role or a step of the process, and opening a second session to carry a brief into it is such a step. A run that Counsel cannot reach would put that person back to carrying answers to it by hand, which is why none is started.

## Rejected Alternatives

- The person directing the work opens the Orchestrator session and hands the brief over there: it lost because it asks for the knowledge of roles and sessions the harness exists to spare them; reopen if no supported runtime lets one session start another in a role without a person.
- Counsel does the run itself, or runs the Orchestrator inside its own session as a subagent: rejected outright, as in ADR-D-0034; the session that person talks with would work at the level of plans.

## Decision Boundary

Not covered: by what means a run is started, watched and ended, which is a means in the brief and the workspace's record to state; what a runtime asks of a person once before any session can be started in a folder; when a ratified brief is handed over, and a brief held because it builds on a change another run has not finished, whose run starts when it is handed over (`ADR-D-when-a-ratified-brief-is-handed-over-is-counsels-to-settle.md`); that that person is told a brief is held (`ADR-D-only-what-needs-the-person-reaches-them-and-when-follows-what-waiting-costs.md`); which Orchestrator session does a brief's run where one is already at work, which is a means in the brief; the session that sets a repository up the first time; how that person's word reaches the started session, and what admits Counsel's relays (ADR-D-0038); how many Counsel sessions a repository has at once; what a session opened by that person's own choice may do, which is unchanged.

## Validation

The decision is broken where a brief has been ratified and its run does not begin until the person directing the work opens a session, starts a seat or carries the brief somewhere, a brief held as its own record states excepted; where the work of a run is done in Counsel's own session; or where a run is going that Counsel cannot reach.

## Revisit When

- The premise that a session can be started in the Orchestrator role with a first message and without a person fails. On 2026-11-12 it was seen in the Claude Code terminal CLI, only in a folder a person had trusted once in that runtime, and in Codex for a run of a single turn. On 2026-11-13 the sessions so started in trials were started for setup and none for a ratified brief; a run that could not be started for a ratified brief without that person reopens this record.
- That person is found talking to Counsel less promptly while runs are being started and watched: on 2026-11-13 it had not been shown that Counsel answers as promptly then as when nothing is running.

## More Information

Source of intent: the brief "One conversation with Counsel", "Who it is for and why", "One conversation", "Runs side by side" and "Core scenarios". Related: ADR-D-0034 (Counsel, and the brief as the grounds for work), ADR-D-0043 (what Counsel says to an Orchestrator session), ADR-D-0062 (under a brief the Orchestrator session asks that person nothing), ADR-D-0064 (what authorizes non-trivial work).
