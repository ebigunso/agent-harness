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

# ADR-D (not yet numbered): Matters are put to the person directing the work one at a time, each when they take it up

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session role that person talks with about what the product does or should do. Something needs that person when it waits on that person's word or judgement.

The person directing the work is to give their attention to what needs them at their own pace. Several matters can wait for that person at once, and that person knows of each from a short list (`ADR-D-nothing-waits-for-the-person-without-their-knowing.md`). Putting the matters themselves to that person together, in one message, has them read all of it before they can answer any of it, and answer at the pace of the message. The fork is how many matters are put to that person at a time.

## Decision

- Matters are taken one at a time.
- The matter itself is put to the person directing the work when they take it up.

## Why

That person's attention is the scarce thing in the product philosophy's "What goes wrong, in order", and a matter put before it is taken up is attention spent on what that person has not yet chosen to decide.

## Rejected Alternatives

- Everything that waits is put to that person in full in one message: it lost because that person has to read every matter in order to answer one, and is made to switch between them; reopen if that person is found asking for the matters together.

## Decision Boundary

Not covered: who chooses which matter is taken up next (`ADR-D-the-order-in-which-matters-are-taken-up-is-the-persons-to-choose.md`); how that person comes to know what waits, and the list itself (`ADR-D-nothing-waits-for-the-person-without-their-knowing.md`); what is brought at once and does not wait for that person to take it up (`ADR-D-when-the-person-is-told-follows-what-waiting-costs.md`); how a question is framed when that person takes it up (ADR-D-0046, ADR-D-0059); how that person's answer travels back (ADR-D-0038).

## Validation

The decision is broken where several matters are put to the person directing the work at once; or where a matter is put to them in full before they took it up, what is being lost excepted.

## Revisit When

- The premise that the matters waiting for that person can be decided apart fails: matters are found that that person could only decide together, having been put to them one by one.

## More Information

Source of intent: the brief "One conversation with Counsel", "What reaches him", "Directed during the run" and "Core scenarios". Related: ADR-D-0034 (Counsel), ADR-D-0059 (which questions reach that person).
