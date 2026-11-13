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

# ADR-D (not yet numbered): When the person directing the work ratifies a brief, its run starts without that person opening anything, and when it starts is Counsel's to settle

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session role that person talks with about what the product does or should do. The Orchestrator is the session role that plans, dispatches and reports the work. A run is the work done under one ratified brief.

The grounds for a piece of work pass from Counsel to an Orchestrator session as a ratified brief (ADR-D-0034). Until 2026-11-12 the person directing the work opened that Orchestrator session and handed the brief over in it, which asks that person to know that there are two roles, to open the second, to carry something from one to the other, and to judge the moment at which the work can begin. The fork is whether ratifying a brief is the last thing asked of that person before the work begins, or the first of several.

## Decision

- When the person directing the work ratifies a brief, its run starts without that person opening, starting or carrying anything.
- Starting the run is Counsel's work. The run is still done by a session of its own that holds the Orchestrator role, never by Counsel and never inside Counsel's session.
- That person can ratify a brief at any moment. When it is handed over is Counsel's to settle, and that person is not asked: a brief that builds on a change another run has not finished is held until its work can start.
- That person is told that a brief is held and what it waits for. No brief waits without that person knowing.
- Where a run could be started but not reached by Counsel afterwards, Counsel says so plainly and starts none.

## Why

The product philosophy's "What it aspires to" is that person's part shrinking to saying what they want and judging what they got, and its "Who it is for" rules out a design that needs them to understand a role or a step of the process; the brief has such a person never "open a second session, start a seat or repair one." The moment of hand-over is a step of the process in the same sense, so it is settled for that person, who said on 2026-11-12: "I think it's better if I get to approve them anytime and when it gets handed over is handled by Counsel." A run that Counsel cannot reach would put that person back to carrying answers to it by hand, which is why none is started.

## Rejected Alternatives

- The person directing the work opens the Orchestrator session and hands the brief over there: it lost because it asks for the knowledge of roles and sessions the harness exists to spare them; reopen if no supported runtime lets one session start another in a role without a person.
- Counsel does the run itself, or runs the Orchestrator inside its own session as a subagent: rejected outright, as in ADR-D-0034; the session that person talks with would work at the level of plans.
- That person is asked, at ratification or after, when a brief should be handed over: it lost because whether a brief's work can start is a fact about the runs in progress that Counsel holds and that person would have to be told in order to answer; reopen if briefs held by Counsel are found to have been ones that person wanted started, or briefs handed over to have been ones that person wanted held.
- A held brief is not mentioned until that person asks: it lost because that person cannot correct a wait they do not know of; rejected outright.

## Decision Boundary

Not covered: by what means a run is started, watched and ended, which is a means in the brief and the workspace's record to state; what a runtime asks of a person once before any session can be started in a folder; that a brief which does not build on unfinished work is not held for the runs in progress (`ADR-D-runs-go-side-by-side-and-settle-what-they-share-without-the-person.md`); the session that sets a repository up the first time; how that person's word reaches the started session, and what admits Counsel's relays (ADR-D-0038); how many Counsel sessions a repository has at once; what a session opened by that person's own choice may do, which is unchanged.

## Validation

The decision is broken where a brief has been ratified and its run does not begin until the person directing the work opens a session, starts a seat or carries the brief somewhere; where that person is asked when a ratified brief should start; where a brief is held and that person has not been told, or not told for what; where the work of a run is done in Counsel's own session; or where a run is going that Counsel cannot reach.

## Revisit When

- The premise that a session can be started in the Orchestrator role with a first message and without a person fails. On 2026-11-12 it was seen in the Claude Code terminal CLI, only in a folder a person had trusted once in that runtime, and in Codex for a run of a single turn. On 2026-11-13 the sessions so started in trials were started for setup and none for a ratified brief; a run that could not be started for a ratified brief without that person reopens this record.
- That person is found talking to Counsel less promptly while runs are being started and watched: on 2026-11-13 it had not been shown that Counsel answers as promptly then as when nothing is running.
- The premise that Counsel judges soundly whether a brief builds on unfinished work fails. Nothing had exercised it on 2026-11-14; a brief handed over whose work could not start, or one held that built on nothing unfinished, reopens how the moment is settled.

## More Information

Source of intent: the brief "One conversation with Counsel", "Who it is for and why", "One conversation", "Runs side by side" and "Core scenarios". Related: ADR-D-0034 (Counsel, and the brief as the grounds for work), ADR-D-0043 (what Counsel says to an Orchestrator session), ADR-D-0062 (under a brief the Orchestrator session asks that person nothing), ADR-D-0064 (what authorizes non-trivial work).
