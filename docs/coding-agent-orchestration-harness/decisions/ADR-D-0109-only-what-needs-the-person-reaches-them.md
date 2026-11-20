---
status: accepted
adr_type: design
date: 2026-11-19
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.2", "GPT-6 Astra"]
informed: []
supersedes: []
superseded_by: null
---

# ADR-D-0109: Only what needs the person directing the work reaches that person, ready to decide, and no account of the work is written out for them

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session role that person talks with about what the product does or should do. A run is the work done under one ratified brief. Something needs that person when it waits on that person's word or judgement.

The attention of the person directing the work is to go only to what needs them. Runs produce much that could be told: what was done, what is going on, where each thing stands. A Counsel session may be left unattended through a long run, and Counsel cannot know whether it is being watched; writing out a whole account of where the work stands whenever that person may be away spends their reading on what does not need them. The fork is what is put before that person: an account of the work, or only what waits on them.

## Decision

- Only what needs the person directing the work reaches that person, and it arrives ready to decide.
- No account of what was done or is going on is written out for them.

## Why

That person's attention is the scarce thing in the product philosophy's "What goes wrong, in order", and people rightly will not spend it on what they did not need to know; an account of the work spends it, and Counsel's context with it, on what does not wait on them.

## Rejected Alternatives

- The whole account of where the work stands is the last thing written whenever that person may be away: it lost because it spends that person's reading, and Counsel's context, on what does not need them; reopen if that person is found asking for the account each time they come back.

## Decision Boundary

Not covered: when something that needs that person is told (ADR-D-0116); how that person comes to know what waits for them (ADR-D-0108); how many matters are put at a time and in what order they are taken up (ADR-D-0106, ADR-D-0110); that Counsel can say where every brief stands when asked, which the brief states; what may be brought to that person at all, and at what level (ADR-D-0059, ADR-D-0062); how a question is framed when that person takes it up (ADR-D-0046, ADR-D-0059); how Counsel keeps what needs that person apart from the runs' reports.

## Validation

The decision is broken where something that does not need the person directing the work is brought to them, or an account of what was done is written out for them unasked.

## Revisit When

- The premise that an account of what was done is no part of what that person needs fails: that person is found asking for the account each time they come back.

## More Information

Source of intent: the brief "One conversation with Counsel", "What reaches him" and "Directed during the run". Related: ADR-D-0034 (Counsel), ADR-D-0059 (which questions reach that person), ADR-D-0062 (everything that needs that person reaches them through Counsel).
