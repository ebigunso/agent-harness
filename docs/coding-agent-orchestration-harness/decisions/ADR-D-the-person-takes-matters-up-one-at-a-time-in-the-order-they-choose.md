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

# ADR-D (not yet numbered): The person directing the work takes matters up one at a time, in the order they choose; Counsel recommends the order

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session role that person talks with about what the product does or should do. Something needs that person when it waits on that person's word or judgement.

The person directing the work is to give their attention to what needs them at their own pace. Several matters can wait for that person at once, and that person knows of each (`ADR-D-nothing-waits-for-the-person-without-their-knowing.md`). Putting several matters to that person in one message takes from them the choice of which to take up. A Counsel that puts them one after another in an order of its own has made that choice for them. The fork is how many matters are put to that person at a time, and who chooses the order.

## Decision

- Matters are taken one at a time. The matter itself is put to the person directing the work when they take it up.
- Counsel recommends the order, naming with the list of what needs that person the one it would settle first, and that person chooses it, at their own pace.

## Why

The order weighs the matters against each other by what that person cares about, and that person is the only one who can weigh that; a recommendation gives them Counsel's view of it without taking the choice, and one matter at a time spares the attention the product philosophy's "What goes wrong, in order" calls the scarce thing.

## Rejected Alternatives

- Counsel sets the order and puts the matters to that person one after another: it lost because the order weighs what that person cares about, which is theirs to weigh; reopen if that person is found to take Counsel's recommended order every time and to want it without being asked.

## Decision Boundary

Not covered: how that person comes to know what waits, and the list itself (`ADR-D-nothing-waits-for-the-person-without-their-knowing.md`); what is brought at once and does not wait for that person to take it up (`ADR-D-when-the-person-is-told-follows-what-waiting-costs.md`); how a question is framed when that person takes it up (ADR-D-0046, ADR-D-0059); how that person's answer travels back (ADR-D-0038).

## Validation

The decision is broken where several matters are put to the person directing the work at once; where Counsel fixes the order in which that person takes matters up; or where what needs that person is listed with nothing said of which Counsel would settle first.

## Revisit When

- The premise that a short list is enough for that person to choose what to take up fails. Nothing had exercised it with several runs on 2026-11-19; matters taken up in an order that person says they would not have chosen had they known more reopens what an item carries, not the decision.

## More Information

Source of intent: the brief "One conversation with Counsel", "What reaches him", "Directed during the run" and "Core scenarios". Related: ADR-D-0034 (Counsel), ADR-D-0059 (which questions reach that person).
