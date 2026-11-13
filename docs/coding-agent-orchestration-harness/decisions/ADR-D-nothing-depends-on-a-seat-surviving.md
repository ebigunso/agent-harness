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

# ADR-D (not yet numbered): Nothing depends on a seat surviving: a first dispatch stands alone, and a seat that takes over part-way is handed where the unit of work stands

## Context and Problem Statement

Terms used here: a seat is a session that another session creates to do work for it and reaches over a peer channel; what is decided here for a dispatch holds as well where the work goes to a subagent the runtime starts for that one dispatch. A dispatch is the message that hands the work over. A unit of work is one assignment a seat can finish and report on.

A seat that has done earlier work holds what it saw, and the session that dispatches to it is tempted to write the next dispatch short on the strength of that. But a seat may be gone when the next dispatch is due, and whether one that is still there holds what it saw cannot be read from outside it. Where results rest on a seat's memory, the seat has to be kept alive, somebody has to repair it when it fails, and work waits for the one seat that knows. The fork is whether continuity of the work is carried by the seats or by what is handed to them.

## Decision

- Nothing depends on a seat surviving. How long a seat lives is not fixed: a session may keep one while it is useful and may end one at any time.
- The first dispatch of a unit of work stands alone: a seat that has seen nothing before it can do the work from the dispatch and the files it names.
- A seat that takes over a unit of work part-way is handed where that unit stands: what it is for, what is decided and on whose word, what is done and at which revision, what remains, what is still open, and what may already have been done outside the repository.
- A seat so handed neither repeats an act already performed nor undoes a decision already made. That the earlier messages are stored somewhere is not enough.

## Why

The person directing the work asked on 2026-11-12 for the outcome "where I am the bottle neck, not the machinery", and on 2026-11-11 said of seats: "I think a seat should be freely spawned and destroyed to allow maximum freedom and parallelism." Seats can be created and ended freely only if no result rests on one having lived: work that waits for a particular seat waits on the machinery, and a person who has to start or repair a seat is doing what the product philosophy's "Who it is for" says is never asked of them. A store of messages does not say which of them still hold, so a seat that takes over is told where the work stands and not left to reconstruct it.

## Rejected Alternatives

- Seats are kept alive for the length of a run, and later dispatches rely on what a seat has seen: it lost because a seat can be lost at any moment and what it still holds cannot be checked from outside, so a result that rests on it fails without anything saying so; reopen if a supported runtime gives a session a way to read from outside what a seat holds and to restore it.
- A new seat reads the stored history of the seat it replaces: it lost because a history does not say which of its messages still hold, and reading another seat's history is not the same as being told what is decided; reopen if a seat taking over from a history alone is found never to repeat an act or undo a decision.
- A new seat is started for every dispatch and none is ever kept: it lost because a kept seat can save reading, and the decision needs only that no result rests on it; reopen if kept seats are found to produce results that a seat handed where the unit stands would not have.

## Decision Boundary

Not covered: who creates and ends a seat and by what means, which are means in the brief and the workspace's record to state; whether two sessions may share a seat; the form of a dispatch and of the hand-off, which the dispatch text states; what a seat is told of the machine it runs on; the identity a session holds on a peer channel (`ADR-D-a-session-holds-one-identity-on-the-peer-channel.md`); who tracks and cleans up subagents that run asynchronously (ADR-D-0021); which option a seat runs on (ADR-D-0068); how long a new seat takes to find its way in an area and what that costs, which the brief leaves out.

## Validation

The decision is broken where a result depends on a seat having seen an earlier unit of work; where a first dispatch can be acted on only by a seat that was there before; where a seat that takes over part-way repeats an act already performed, undoes a decision already made, or has to ask what an earlier seat knew; or where work waits for a particular seat to be started, kept or repaired.

## Revisit When

- The premise that what a seat still holds cannot be read from outside it no longer holds. The decision rests on two rounds of research on 2026-11-12 into the channel history and session transcripts of four repositories.
- A seat handed where a unit stands is found to do measurably worse work than the seat it replaced would have. On 2026-11-12 the logs could not show how long a new seat takes to find its way in an area or what that costs in money.

## More Information

Source of intent: the brief "One conversation with Counsel", "Seats" and "Core scenarios". Related: ADR-D-0021 (the lifecycle of asynchronous subagents), ADR-D-0068 (how a role's option is chosen).
