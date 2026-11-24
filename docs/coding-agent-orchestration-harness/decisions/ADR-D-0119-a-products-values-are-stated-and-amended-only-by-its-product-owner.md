---
status: proposed
adr_type: design
date: 2026-11-24
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "Claude Fable 5.2"]
informed: []
supersedes: ["ADR-D-0036-a-product-philosophy-is-stated-only-by-the-product-owner-and-no-product-value-is-inferred-without-one.md"]
superseded_by: null
---

# ADR-D-0119: A product's values are stated and amended only by its product owner

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. The product owner is whoever is entitled to state the product's values and to answer product-level questions for that work; when the person directing the work owns the product, both are that person. A product philosophy is the document that states what the product owner wants from the product. Counsel is the session role the person directing the work talks with about what the product does or should do.

What is built for a product is to be what its owner meant, and the product philosophy is what later work takes that meaning from. The person directing a piece of work is not always the product owner, and others besides the owner are in a position to put a product value into words: Counsel when it writes the document or reads a request, the person directing the work when the work in hand would go more easily with the philosophy amended. A value that enters the philosophy that way reads afterwards as the owner's, and work is built on it as such. The fork is who may state and amend a product's values, and whether a product philosophy belongs to the product or to whoever directs a piece of work on it.

## Decision

- A product's values are the product owner's to state. A product philosophy changes only on the product owner's ratification: Counsel, where it writes the text, writes what the product owner ratified, and nobody else changes it.
- A product philosophy belongs to the product and not to a piece of work. It may exist for a product the person directing the work does not own, and where it exists it governs the product side of the work whoever directs it.
- Nobody states a product value on the product owner's behalf. Counsel infers none, and the person directing work on a product that person does not own amends none.
- An amendment to a product philosophy goes to the product owner, through the person directing the work.
- Who states and amends the engineering philosophy does not turn on who owns the product.

## Why

Only the product owner is entitled to say what the product is for, and a value somebody else supplied, once it stands in the philosophy, is built upon as what the owner meant. That is the failure the product philosophy's "What goes wrong, in order" names "The wrong thing, built confidently", and what a product's owner wants from it is a question only the owner can answer.

## Rejected Alternatives

- A product philosophy exists only where the person directing the work owns the product: rejected outright; a product's philosophy is stated by its owner before any given piece of work, so it can exist for a product the person directing the work does not own, and a rule that denies it would ignore a document that governs.
- Counsel infers product values for an absent product owner from the request: rejected outright; a product's values are the product owner's to state.
- The person directing the work amends the product philosophy of a product that person does not own: rejected outright; the amendment is the product owner's act.

## Decision Boundary

Not covered: what the product side of work is judged against, and from what a judgement may be extended (ADR-D-0120); who states and amends the engineering philosophy; the forms and locations of the philosophies and what records a ratification, which the value documents' own text states; how a product-level question travels from the person directing the work to the product owner and back; what Counsel is and whom it serves (ADR-D-0117); that a product persona is the product owner's to state (ADR-D-0124).

## Validation

The decision is broken where:

- a product philosophy's text changed without its product owner's ratification, or says something that owner did not ratify;
- a product value that the product owner did not state was written down or acted on as the owner's;
- a product philosophy that exists was set aside because the person directing the work does not own the product.

## Revisit When

- The premise that an amendment and a product-level question can reach the product owner through the person directing the work fails. On 2026-10-01 no person had directed work on a product that person does not own; such use showing product-level questions decided in the Counsel session instead of reaching the product owner reopens this record.

## More Information

Replaces ADR-D-0036 at who states and amends a product's values; ADR-D-0120 replaces the rest of it. Source of intent: `docs/coding-agent/briefs/completed/value-level-operation-brief.md`, "Roles and sessions" and "Documents, in the target repository". Related: ADR-D-0117 (Counsel), ADR-D-0124 (a product persona is the product owner's to state).
