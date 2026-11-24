---
status: proposed
adr_type: design
date: 2026-11-24
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "Claude Fable 5.2"]
informed: []
supersedes: ["ADR-D-0046-value-discussion-is-conducted-from-the-viewpoint-of-a-persons-experience.md"]
superseded_by: null
---

# ADR-D-0124: A value discussion with the person directing the work is conducted from the viewpoint of a person's experience

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. The product owner is whoever is entitled to state the product's values and to answer product-level questions for that work; when the person directing the work owns the product, both are that person. Counsel is the session role that person talks with about what the product does or should do. A persona is the kind of person an experience is told of.

The person directing the work is to judge, in the discussion and without reading the work, whether something is wrong and what it should be instead. Counsel works at the level of behaviour and decisions (ADR-D-0117), and that level alone does not serve this: it can still be spoken as what the product does, as a state the product reaches, or as what a mechanism guarantees, and each of those leaves that person to work out for themselves what it would mean for anyone. The fork is the terms in which the discussion is held.

## Decision

- A value discussion with the person directing the work is conducted from the viewpoint of a person's experience.
- Its unit is an experience told whole: a person with a given persona does something, experiences something as a result, and so gains certain values.
- What that person experiences is stated as an experience, never as an abstract state of the product.
- Whatever Counsel asks of the person directing the work, proposes to them or restates for them is put as such an experience. Where Counsel cannot fill a part of it, it says which.
- A matter that arrives in terms of mechanism, from wherever it comes, is put as such an experience before it reaches that person. The mechanism is stated too where the experience alone would hide a risk.
- A persona is stated when a philosophy is formed or at the moment a discussion needs one. A philosophy may hold several. A product persona is the product owner's to state: Counsel supplies none, and no values for one. On the engineering side the persona is whoever works on the project later.

## Why

The product philosophy's "What goes wrong, in order" has what is meant established in terms the person can judge. A person recognises what is wrong in an experience, and what it should be instead, more readily than in a mechanism or an abstract state: saying who does what, what they then experience and what they gain puts the judgement where that person's intuition works, and an experience with a part missing shows what has not yet been thought through.

## Rejected Alternatives

- Value discussion in terms of what the product does, with no person or experience named: it lost because a behaviour stated alone gives nothing to judge it against, so whether it is right has to be worked out by the person each time; reopen if experiences are found to be filled in mechanically, the persona and the gain adding nothing to what the behaviour already said.
- Product personas fixed in the harness: it lost because who uses a product is that product's own matter, stated by its owner, as a product's values are its owner's to state (ADR-D-0119); rejected outright.
- Mechanism never stated to the person directing the work: it lost because some risks do not show in the experience until they happen; reopen if mechanism is found crowding the experience out of what reaches that person.

## Decision Boundary

Not covered: what Counsel is responsible for and the level it works at (ADR-D-0117); who states a product's values and what is done where no product philosophy exists (ADR-D-0119, ADR-D-0120); the terms in which the durable documents a discussion produces are written (ADR-D-0047); which questions reach the person directing the work at all (ADR-D-0125), and when and how many at a time (ADR-D-0106, ADR-D-0116); what Counsel says to an Orchestrator session (ADR-D-0097, ADR-D-0100, ADR-D-0102); how an Orchestrator session reports to that person in its own session; how an experience is worded and at what length; how the value audit grades, which reads the documents as they are written.

## Validation

The decision is broken where:

- something Counsel asked of, proposed to or restated for the person directing the work did not say who does what, what they experience and what they gain, and did not say which of these it could not fill;
- what a person experiences was given to them as an abstract state of the product;
- a matter reached that person in terms of mechanism alone, or a risk the experience would hide reached them with the mechanism left out;
- a product persona, or values for one, came from Counsel or from the harness and not from the product owner.

## Revisit When

- The premise that a person recognises what is wrong in an experience more readily than in a mechanism or an abstract state no longer holds: experiences are found to be filled in mechanically, adding nothing to the behaviour they restate, or the person directing the work is found judging a matter only after asking for it to be put another way.
- On 2026-10-02 no discussion had been conducted in this form under this decision on any runtime; a discussion in which that person had to translate before judging reopens this record.

## More Information

Replaces ADR-D-0046 whole. Source of intent: `docs/coding-agent/briefs/completed/value-level-operation-brief.md`, "How a conversation with Counsel should go". Related: ADR-D-0117 (Counsel's level), ADR-D-0119 (a product's values are its owner's to state, which is what leaves a product persona to the product owner), ADR-D-0047 (the documents a discussion produces), ADR-D-0125 (which questions reach that person).
