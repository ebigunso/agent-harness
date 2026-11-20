---
status: accepted
adr_type: design
date: 2026-11-14
deciders: ["ebigunso"]
consulted: ["GPT-6 Astra", "Claude Fable 5.2"]
informed: []
supersedes: []
superseded_by: null
---

# ADR-D-0093: A run that has stopped making progress is found without the person directing the work

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. A run is the work done under one ratified brief.

A run goes on in a session the person directing the work does not watch (ADR-D-0088). When that session stops, nothing in it tells anyone: a stopped run, a run that is working long and a run that is rightly waiting for an answer are all quiet. That person is not to be the one who watches the machinery; with nothing else finding a stop, they are the one who notices it, and the run sits stopped until they do. The fork is who notices a stop.

## Decision

- The person directing the work does not have to notice that a run or a seat has stopped. A run that has stopped making progress is found without that person.
- A stopped run is told apart from one that is working long and from one that is rightly waiting.

## Why

A stop that only the person directing the work can notice makes that person the monitor of the machinery, which the product philosophy's "Who it is for" says is never asked of them, and a run that sits stopped is a wait nobody chose.

## Rejected Alternatives

- That person looks in on the runs, or is told only when they ask: it lost because that person would be watching sessions to learn whether the work is going; rejected outright.
- A quiet run is treated as stopped after a fixed time: it lost because a run working long and a run rightly waiting are quiet too, and stopping or restarting either undoes sound work; reopen if a supported runtime is found to give no way at all to tell them apart.

## Decision Boundary

Not covered: what is done about a run found stopped (ADR-D-0094); by what means a run is watched and how its state is read, which the workspace's record states; what a run's own reports say of where it stands; a run that stops because it has stopped getting closer to its goal and says so, which the workflow text states; what a session does about something it dispatched work to that has stopped (ADR-D-0021).

## Validation

The decision is broken where a run has stopped making progress and the first to notice is the person directing the work; or where a run that was working or rightly waiting is taken to have stopped.

## Revisit When

- What can be read of a session from outside changes. On 2026-11-12, in Claude Code, a started session's state could be read from outside as working, waiting with the kind of thing waited for, finished its turn, or stopped; nothing seen told a session working long from one that was stuck while its process lived, so that case rested on a judgement from the run's last report. A stuck run that went unnoticed under that judgement, or a working run treated as stopped, reopens how a stop is told apart.

## More Information

Source of intent: the brief "One conversation with Counsel", "What reaches him" and "Core scenarios". Related: ADR-D-0044 (Counsel's pause, which is a stop Counsel issues and not one it finds), ADR-D-0051 (the run).
