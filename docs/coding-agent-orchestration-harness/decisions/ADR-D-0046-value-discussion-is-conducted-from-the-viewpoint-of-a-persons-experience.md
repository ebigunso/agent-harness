---
status: accepted
adr_type: design
date: 2026-10-02
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1"]
informed: []
supersedes: []
superseded_by: null
depends_on: ["ADR-D-0034-counsel-is-a-separate-session-at-the-level-of-behaviour-and-decisions.md", "ADR-D-0036-a-product-philosophy-is-stated-only-by-the-product-owner-and-no-product-value-is-inferred-without-one.md"]
---

# ADR-D-0046: A value discussion with the person directing the work is conducted from the viewpoint of a person's experience, as a chain of four parts: a person with a given persona does something, experiences something as a result, and so gains certain values

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. The product owner is whoever is entitled to state the product's values and to answer product-level questions for that work; when the person directing the work owns the product, both are that person. Counsel is the session the person directing the work opens for value discussion, separate from any Orchestrator session. The Orchestrator session is a session that holds the Orchestrator role (ADR-D-0020) and plans, dispatches and reports the work.

Counsel works at the level of behaviour and decisions (ADR-D-0034), but that level can still be spoken in several terms: what the product does, what state it reaches, what a mechanism guarantees. The person directing the work has to judge, in the discussion and without reading the work, whether something is wrong and what it should be instead. The fork is the terms in which the discussion is held.

## Decision

- A value discussion with the person directing the work is conducted from the viewpoint of a person's experience.
- Its unit is a chain of four parts: a person with a given persona, does something, experiences something as a result, and so gains certain values.
- The third part is what the person experiences, not an abstract state of the product.
- Counsel puts every question, proposal and restatement it brings to the person directing the work as that chain, and says which part it cannot fill when one is missing.
- A matter that arrives in terms of mechanism, an escalation from a run included, is put into the chain before it reaches that person; the mechanism is stated too where the experience alone would hide a risk.
- A persona is defined when a philosophy is formed, or at the moment a discussion needs one. A philosophy may hold several. A product persona is the product owner's to state: Counsel supplies none and no values for one (ADR-D-0036). For the engineering side the persona is whoever works on the project later.

## Why

A person recognises what is wrong in an experience, and what it should be instead, more readily than in a mechanism or an abstract state: stating who does what, what they then experience and what they gain puts the judgement where that person's intuition works, and a chain with a part missing shows what has not yet been thought through. That is worth most while the discussion is taking place, which is where this record applies it.

## Rejected Alternatives

- Value discussion in terms of what the product does, with no person or experience named: it lost because a behaviour stated alone gives nothing to judge it against, so whether it is right has to be worked out by the person each time; reopen if chains are found to be filled in mechanically, the persona and the gain adding nothing to what the behaviour already said.
- Fixed product personas written into the harness: rejected outright; who uses a product is that product's own matter, stated by its owner (ADR-D-0036).
- Mechanism never stated to the person directing the work: it lost because some risks do not show in the experience until they happen; reopen if mechanism is found crowding the chain out of what reaches that person.

## Decision Boundary

Invariant: what Counsel brings to the person directing the work in a discussion is stated as a person with a persona doing something, experiencing something and gaining values from it, with a missing part named as missing; product personas are stated by the product owner, not by the harness or by Counsel; the Decision list states the rest.

Not covered: what Counsel is responsible for and the level it works at (ADR-D-0034); who writes a product philosophy and what is done without one (ADR-D-0036); the terms in which the durable documents a discussion produces are written (ADR-D-0047); how the Orchestrator reports to the person directing the work in its own session; the wording of a chain or its length; how the value audit grades, which reads the documents as they are written.

## Validation

- Counsel's policy states the chain, that the third part is an experience, that a missing part is named, that mechanism-level matters are put into the chain before they reach the person directing the work, and where personas come from.
- Review of any change to Counsel's text asks: does what reaches the person directing the work in a discussion say who does what, what they experience and what they gain?

## Revisit When

- Chains are found to be filled in mechanically, adding nothing to the behaviour they restate.
- The person directing the work is found judging a matter only after asking for it to be put another way.
- On 2026-10-02 no discussion had been conducted in this form under this record on any runtime; a discussion in which that person had to translate before judging reopens this record.

## More Information

Source of intent: `docs/coding-agent/briefs/active/value-level-operation-brief.md`, "How a conversation with Counsel should go". Related: ADR-D-0034 (Counsel's level), ADR-D-0036 (the philosophy documents), ADR-D-0047 (the documents a discussion produces), ADR-D-0043 (what Counsel says to the Orchestrator, which this record does not change).
