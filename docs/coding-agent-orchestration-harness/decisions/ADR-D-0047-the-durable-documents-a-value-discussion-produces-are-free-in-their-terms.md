---
status: accepted
adr_type: design
date: 2026-10-02
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1"]
informed: []
supersedes: []
superseded_by: null
depends_on: ["ADR-D-0046-value-discussion-is-conducted-from-the-viewpoint-of-a-persons-experience.md"]
---

# ADR-D-0047: The durable documents a value discussion produces state the concept it settled on in whatever terms state it best; they may use the experience framing of the discussion and are never required to take that form

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. The product owner is whoever is entitled to state the product's values and to answer product-level questions for that work; when the person directing the work owns the product, both are that person. Counsel is the session the person directing the work opens for value discussion, separate from any Orchestrator session. The Orchestrator session is a session that holds the Orchestrator role (ADR-D-0020) and plans, dispatches and reports the work.

A value discussion with the person directing the work is conducted as a chain of a person's experience (ADR-D-0046), because that is where that person's judgement works best. What the discussion settles is then written into durable documents: a philosophy, a brief, a decision record. Those are read later, by that person and by agents, to reason from, and their job is to state the concept that was settled. The fork is whether the documents are bound to the terms the discussion was held in.

## Decision

- The experience chain governs the discussion, not the durable documents it produces.
- A philosophy, a brief or a decision record states the concept the discussion settled on in whatever terms state it best.
- Such a document may use the experience framing where it helps communicate.
- No document form and no record standard requires a statement to be written as a chain.

## Why

The framing matters most while a discussion is taking place. A durable document has to carry the core concept the discussion settled on, and a reader of a philosophy written only as experience chains would find the concept harder to take from it: limiting the documents to that form would give up too much freedom to state the concept itself.

## Rejected Alternatives

- The value documents written as chains, every value statement in the form: it lost because it would sacrifice the freedom to state the core concept a discussion settled on; reopen if documents written freely are found to lose what the discussion's chain had made clear.
- The experience framing kept out of the durable documents altogether: it lost because the framing does help communicate where a statement is about what someone experiences; reopen if its use in documents is found to blur statements the audit has to match.

## Decision Boundary

Invariant: a philosophy, a brief or a decision record is free in its terms; it may use the experience framing and is never required to; the Decision list states the rest.

Not covered: the terms in which the discussion itself is conducted (ADR-D-0046); who writes each document and what its form otherwise requires (ADR-D-0036 and the documents' own forms); the form of decision records, which the record standard states; how the value audit reads the documents, which is as they are written.

## Validation

- The forms of the value documents and the record standard contain no requirement that a statement be written as a chain, and say the framing may be used where it helps.
- Review of any change to a document form asks: does this bind the document to the terms of the discussion?

## Revisit When

- Documents written freely are found to lose what the discussion's chain had made clear.
- On 2026-10-02 no philosophy had been written after a discussion conducted under ADR-D-0046 on any runtime; a document whose reader had to ask what experience a statement was about reopens this record.

## More Information

Source of intent: `docs/coding-agent/briefs/active/value-level-operation-brief.md`, "How a conversation with Counsel should go". Related: ADR-D-0046 (the discussion), ADR-D-0036 (the philosophy documents).
