---
status: proposed
adr_type: design
date: 2026-11-19
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.2", "GPT-6 Astra"]
informed: []
supersedes: []
superseded_by: null
---

# ADR-D (not yet numbered): The order in which matters are taken up is the choice of the person directing the work; Counsel recommends it

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session role that person talks with about what the product does or should do. Something needs that person when it waits on that person's word or judgement.

The person directing the work is to give their attention to what needs them at their own pace, and to what matters most to them first. Several matters can wait for that person at once, and that person knows of each from a short list (`ADR-D-nothing-waits-for-the-person-without-their-knowing.md`). A Counsel that puts the matters to that person in an order of its own has chosen for them which comes first. A Counsel that lists them and says nothing leaves that person to order them without the view of the session that knows where each stands. The fork is who chooses the order in which matters are taken up.

## Decision

- Counsel recommends the order, naming with the list of what needs the person directing the work the one it would settle first.
- That person chooses the order, at their own pace.

## Why

The order weighs the matters against each other by what that person cares about, and that person is the only one who can weigh that; a recommendation gives them Counsel's view of it without taking the choice, as the product philosophy's "What goes wrong, in order" has a choice made for someone told and easy to change.

## Rejected Alternatives

- Counsel sets the order and puts the matters to that person one after another: it lost because the order weighs what that person cares about, which is theirs to weigh; reopen if that person is found to take Counsel's recommended order every time and to want it without being asked.

## Decision Boundary

Not covered: how many matters are put to that person at a time, and when a matter itself is put (`ADR-D-matters-are-put-to-the-person-one-at-a-time.md`); how that person comes to know what waits, and the list itself (`ADR-D-nothing-waits-for-the-person-without-their-knowing.md`); what is brought at once and does not wait for that person to take it up (`ADR-D-when-the-person-is-told-follows-what-waiting-costs.md`); on what grounds Counsel recommends one matter before another.

## Validation

The decision is broken where Counsel fixes the order in which the person directing the work takes matters up; or where what needs that person is listed with nothing said of which Counsel would settle first.

## Revisit When

- The premise that a short list is enough for that person to choose what to take up fails. Nothing had exercised it with several runs on 2026-11-19; matters taken up in an order that person says they would not have chosen had they known more reopens what an item carries, not the decision.

## More Information

Source of intent: the brief "One conversation with Counsel", "What reaches him", "Directed during the run" and "Core scenarios". Related: ADR-D-0034 (Counsel).
