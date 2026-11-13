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

# ADR-D (not yet numbered): What becomes ready for the person directing the work reaches that person as a line and then waits, taken up in the order and at the pace that person chooses

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session role that person talks with about what the product does or should do. A run is the work done under one ratified brief. Something is ready for that person when it waits on that person's word or judgement: a question, a result, a held brief, a report that a run has stopped.

With several runs going at once and one conversation, things become ready for the person directing the work while that person is discussing something else, and more than one at a time. Each can be put to that person in full the moment it is ready, which breaks into whatever that person is doing as often as the runs produce something. Or each can be kept until that person asks, which leaves that person not knowing that anything waits. The fork is how something ready reaches that person, and who chooses the order in which it is taken up.

## Decision

- When something becomes ready for the person directing the work, that person is told that it is there: what it is and what it holds up, briefly, and not put to that person in full.
- It then waits. That person takes things up in the order and at the pace that person chooses.
- Nothing is held without that person knowing it is there.
- Counsel can always tell that person everything that is waiting on them, which item holds up the most work, and where every brief stands, without that person looking at any other session.

## Why

Offered each item reaching them as it is ready against its being held for them, that person said on 2026-11-12: "Yes, I think it's better to leave the choice of order to me rather than having to constantly switch tasks." And of a case in which nothing was said until asked: "I think it's better if I get to know what is waiting, so I can choose to pick it up at my own pace, rather than be silently held and never know it's there." That person's attention is the scarce thing in the product philosophy's "What goes wrong, in order", and a thing decided for someone and never mentioned leaves them unable to correct it ("The line"); a line that says what waits and what it holds up spends little attention and keeps the choice with the one person who can weigh it.

## Rejected Alternatives

- Each item is put to that person in full as soon as it is ready: it lost because that person is made to switch tasks at the pace of the runs and not at their own; reopen if items that waited behind a line are found to have held up work longer than that person would have chosen had they seen them in full.
- Items are held until that person asks what is waiting: it lost because a person who does not know something waits cannot choose to take it up, and work stays held without anyone having decided that it should; rejected outright.
- Counsel orders the waiting items and puts them to that person one after another: it lost because the order weighs what that person cares about against what each item holds up, which is that person's to weigh; reopen if that person is found to ask Counsel for the order every time.

## Decision Boundary

Not covered: the wording and length of the line; how Counsel keeps what it tells from the runs' reports; what may be brought to that person at all, and at what level (ADR-D-0059, ADR-D-0062); how a question is framed when that person takes it up (ADR-D-0046, ADR-D-0059); a matter Counsel judges severe enough to pause part of the work, which is raised as its own record states (ADR-D-0044); how that person's answer travels back (ADR-D-0038); how promptly Counsel answers while runs are starting and reporting.

## Validation

The decision is broken where something ready for the person directing the work is put to that person in full without having been asked for; where something waits on that person and that person has not been told it is there and what it holds up; where Counsel chooses the order in which that person takes things up; or where that person has to look at another session to learn what waits on them or where a brief stands.

## Revisit When

- The premise that a line is enough for that person to choose an order fails. Nothing had exercised it with several runs on 2026-11-14; items taken up in an order that person says they would not have chosen had they known more reopens what the line carries, not the decision.
- The lines themselves are found to interrupt that person as putting items in full would have.

## More Information

Source of intent: the brief "One conversation with Counsel", "What reaches him", "Runs side by side" and "Core scenarios". Related: ADR-D-0034 (Counsel), ADR-D-0044 (Counsel's pause), ADR-D-0059 (which questions reach that person), ADR-D-0062 (everything that needs that person reaches them through Counsel).
