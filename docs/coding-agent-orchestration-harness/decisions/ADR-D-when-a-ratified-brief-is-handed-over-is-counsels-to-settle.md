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

# ADR-D (not yet numbered): The person directing the work can ratify a brief at any moment; when it is handed over is Counsel's to settle, and a brief that builds on unfinished work is held until its work can start

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session role that person talks with about what the product does or should do. A run is the work done under one ratified brief. A brief is handed over when Counsel gives it to the session that does its run.

The person directing the work is to be free to ratify a brief whenever they are ready to judge it, and is not to be asked about the state of the work in order to do so. A ratified brief's run starts without that person opening anything (`ADR-D-a-ratified-briefs-run-starts-without-the-person-opening-anything.md`). A brief may build on a change another run has not finished, and its work cannot start until that change is there, so somebody has to judge that moment. Tying ratification to it makes that person's decision wait on the runs, and asking that person for it puts to them a fact about the runs that they do not hold. The fork is whether that person ratifies only what can start at once, or is asked when a brief should start, or ratifies whenever they are ready and leaves the moment to Counsel.

## Decision

- The person directing the work can ratify a brief at any moment, whatever the runs in progress.
- When a ratified brief is handed over is Counsel's to settle, and that person is not asked.
- A brief that builds on a change another run has not finished is held by Counsel until its work can start, and handed over then.

## Why

Whether a brief's work can start is a fact about the runs in progress, which Counsel holds and that person would have to be told in order to answer; the product philosophy's "Who it is for" has a choice the person cannot weigh made for them. Ratifying is that person's judgement of the brief and does not depend on that fact, so it is not made to wait for it.

## Rejected Alternatives

- That person is asked, at ratification or after, when a brief should be handed over: it lost because whether a brief's work can start is a fact about the runs in progress that Counsel holds and that person would have to be told in order to answer; reopen if briefs held by Counsel are found to have been ones that person wanted started, or briefs handed over to have been ones that person wanted held.
- A brief is ratified only once its work can start: it lost because that person's readiness to decide would then wait on the runs in progress, and they would have to come back to a brief they had already judged; reopen if briefs ratified early are found to have been overtaken by the work they waited for, so that what was ratified was no longer what that person meant.
- A brief that builds on unfinished work is handed over at once: it lost because a run started on a change that is not finished builds on something that may still move, and what it delivers may then not be what the brief meant; reopen if runs are found able to start on unfinished work and bring their own onto its final state without that person.

## Decision Boundary

Not covered: that a held brief is told to that person, with what it waits for, which its own record states (`ADR-D-nothing-waits-for-the-person-without-their-knowing.md`); that a ratified brief's run starts without that person opening anything, and by whom it is started (`ADR-D-a-ratified-briefs-run-starts-without-the-person-opening-anything.md`); whether a brief that builds on nothing unfinished waits for other work, and which session it is handed to, which the brief states; how Counsel learns what a run touches and when a change is finished; part of a run held back by the session that does it; what ratifying a brief requires, which is unchanged.

## Validation

The decision is broken where that person is asked when a ratified brief should start, or to wait with ratifying until other work has finished; where a brief is handed over whose work cannot start because it builds on a change another run has not finished; or where a brief stays held after its work could start.

## Revisit When

- The premise that Counsel judges soundly whether a brief builds on unfinished work fails. Nothing had exercised it on 2026-11-14; a brief handed over whose work could not start, or one held that built on nothing unfinished, reopens how the moment is settled.

## More Information

Source of intent: the brief "One conversation with Counsel", "Runs side by side" and "Core scenarios". Related: ADR-D-0034 (Counsel, and the brief as the grounds for work), ADR-D-0043 (what Counsel says to an Orchestrator session).
