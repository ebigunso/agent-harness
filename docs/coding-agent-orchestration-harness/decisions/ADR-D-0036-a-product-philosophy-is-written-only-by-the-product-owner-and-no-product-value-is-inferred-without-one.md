---
status: accepted
adr_type: design
date: 2026-10-01
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1"]
informed: []
supersedes: []
superseded_by: null
---

# ADR-D-0036: A product philosophy is written and amended only by the product owner, may pre-exist whoever directs the work, and where none exists no product value is inferred on the product owner's behalf

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. The product owner is whoever is entitled to state the product's values and to answer product-level questions for that work; when the person directing the work owns the product, both are that person. Counsel is the session the person directing the work opens for value discussion, separate from any Orchestrator session. The Orchestrator session is a session that holds the Orchestrator role (ADR-D-0020) and plans, dispatches and reports the work.

Two philosophy documents may govern a run: the product philosophy, which states what the product owner wants from the product, and the engineering philosophy, which states how the person directing the work wants the project to look. The person directing the work is sometimes not the product owner, and a product philosophy may already exist for such a product or may not exist at all. The fork is who may write the product values, what the brief traces to, and what Counsel and the value audit do on the product side when no product philosophy exists.

## Decision

- A product philosophy is amended only on the product owner's ratification; where Counsel writes it, it writes what the product owner ratified; nobody else changes the text.
- A product philosophy may pre-exist for a product the person directing the work does not own, and where one exists it governs the product side whoever directs the work.
- The brief traces to the product philosophy where there is one, and to the request as received where there is not.
- Counsel never infers product values on the product owner's behalf.
- The value audit grades the product side against the product owner's own words in a brief or a philosophy, inferred grades included, because a philosophy is written to be reasoned from.
- Against a request as received, an item is graded cited only where the request explicitly covers it, and never inferred.
- Every other product-side item, and any amendment to a product philosophy, goes to the product owner through the person directing the work.
- The engineering philosophy is unaffected: who writes it and how the engineering side is graded do not turn on who owns the product.

## Why

Only the product owner is entitled to state the product's values, and a philosophy that owner wrote was written to be reasoned from, so the audit may extend it; a request states a goal and not values, so nothing is reasoned from it on the product owner's behalf, and the gap goes to the product owner.

## Rejected Alternatives

- A product philosophy exists only where the person directing the work owns the product: rejected outright; a product's philosophy is written by its owner before any given piece of work, so it can exist for a product the person directing the work does not own, and a rule that denies it would ignore a document that governs.
- Counsel inferring product values for an absent product owner from the request: rejected outright; a product's values are the product owner's to state.
- Grading a pre-existing product philosophy as cited only, with no inferred grade: it lost because the philosophy was written to be reasoned from, and refusing to reason from it would stop the run on what the product owner already answered; reopen if the product owner, shown inferred items, regularly rejects them.
- Grading a request as received with inferred grades: rejected outright; a request states a goal, not values to reason from.
- The person directing the work amending a product philosophy for a product that person does not own: rejected outright; the amendment is the product owner's act.

## Decision Boundary

Invariant: the product values are stated and amended only by the product owner; where no product philosophy exists nothing is inferred on the product owner's behalf, and the product side is graded only on the product owner's own words; the Decision list states the rest.

Not covered: the forms and locations of the philosophies and the brief, which the value-documents reference owns; how a product-level question travels from the person directing the work to the product owner and back; how the audit records a grade and what the Orchestrator does with one, which ADR-D-0039 and the run-side procedure own; what Counsel is and whom it serves (ADR-D-0034).

## Validation

- Counsel's policy states that a product philosophy changes only on the product owner's ratification, that Counsel infers no product values on the product owner's behalf, and that product-level questions for a product the person directing the work does not own go to the product owner through that person.
- The value audit's mandate states that an item is graded against a request as received only as cited where the request explicitly covers it, and that inferred grades apply against a product philosophy and a brief.
- Review of any change to the value documents' rules asks: does this let anyone but the product owner state or amend a product value, or let the audit infer one from a request?

## Revisit When

- Use by a person directing work on a product that person does not own, none having occurred on 2026-10-01, shows product-level questions decided in the Counsel session or by the audit instead of reaching the product owner.
- A product owner, shown items graded inferred against a pre-existing philosophy, regularly rejects them.

## More Information

Source of intent: `docs/coding-agent/briefs/active/value-level-operation-brief.md`, "Roles and sessions", "Documents, in the target repository" and "Value audit". Related: the record on Counsel (ADR-D-0034), the record on the value audit (ADR-D-0039).
