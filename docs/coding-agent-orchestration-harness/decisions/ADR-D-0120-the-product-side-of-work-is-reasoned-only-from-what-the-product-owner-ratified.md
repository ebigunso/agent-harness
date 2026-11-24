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

# ADR-D-0120: The product side of work is reasoned only from what the product owner ratified

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. The product owner is whoever is entitled to state the product's values and to answer product-level questions for that work; when the person directing the work owns the product, both are that person. A product philosophy is the document that states what the product owner wants from the product. A brief is the statement of what one piece of work must give, ratified before the work starts. A request as received is what a product owner who is not the person directing the work asked for, kept in that owner's words. The value audit is the independent judgement of how each item of a run stands against these documents (ADR-D-0052); an item is a decision the work makes.

Work is to go ahead without anybody being asked what the product owner has already answered, and is never to be built on a product value that owner did not hold. A run makes many product-side decisions that no document states word for word. An audit that lets through only what is stated stops the run on what the owner's philosophy already answers by its reasoning. An audit that extends whatever it is given also extends a bare request, and so supplies values the owner never stated. The fork is what the product side of work is judged against, and from which of those things a judgement may be extended to an item they do not state.

## Decision

- The value audit judges the product side of work against what the product owner ratified, in a product philosophy or in a brief, whoever worded it.
- What the product owner ratified is written to be reasoned from: an item it does not state may be judged an extension of what it states, as well as covered by it.
- A request as received is not reasoned from. Against one, an item is supported only where the request explicitly covers it, and no item is judged an extension of it.
- A brief traces to the product philosophy where there is one, and to the request as received where there is not.
- Every other product-side item goes to the product owner, through the person directing the work.
- How the engineering side of work is judged does not turn on who owns the product.

## Why

A philosophy its owner ratified is there to be reasoned from, so an item that follows from it is one the owner has already answered, and stopping on it spends attention on what could have been settled, which the product philosophy's "What goes wrong, in order" names as a failure. A request states a goal and not values, so whatever is reasoned from it is supplied on the owner's behalf; that gap is a question only the product owner can answer, and it goes to the owner.

## Rejected Alternatives

- An item counts against a product philosophy only where a statement covers it, and none is judged an extension: it lost because the philosophy was written to be reasoned from, and refusing to reason from it would stop the run on what the product owner already answered; reopen if the product owner, shown items judged extensions, regularly rejects them.
- An item may be judged an extension of a request as received: rejected outright; a request states a goal, not values to reason from.

## Decision Boundary

Not covered: who states and amends a product's values, and that nobody infers one on the product owner's behalf (ADR-D-0119); how the engineering side is judged; who makes the judgement, on what evidence, and that an item needing a decision above the run waits for it (ADR-D-0052); when an extension may go ahead without the person directing the work seeing it (ADR-D-0065); what is shown of extensions when a run closes (ADR-D-0042); the names of the grades and their definitions, which the audit's own text states; how a brief says which of these its product side rests on, and the forms and locations of the documents, which the value documents' own text states; how a product-level question travels from the person directing the work to the product owner and back.

## Validation

The decision is broken where:

- a product-side item went ahead as an extension of a request as received, or as covered by one that does not explicitly cover it;
- a product-side item was judged against something the product owner did not ratify and that is not the owner's request as received;
- a product-side item that nothing the product owner ratified or asked for supports was decided without reaching the product owner;
- work stopped on a product-side item that extends what the product owner ratified, for the sole reason that no statement covers it word for word.

## Revisit When

- The premise that what a product owner ratified can be reasoned from as that owner would reason fails: a product owner, shown items judged extensions of a product philosophy that existed before the work, regularly rejects them.
- The premise that an item a request does not cover reaches the product owner fails. On 2026-10-01 no person had directed work on a product that person does not own; such use showing product-level questions decided by the audit, and not by the product owner, reopens this record.

## More Information

Replaces ADR-D-0036 at what the product side of work is judged against; ADR-D-0119 replaces the rest of it. ADR-D-0052 and ADR-D-0065 leave what the product side is graded against, where no product philosophy exists included, to this record. Source of intent: `docs/coding-agent/briefs/completed/value-level-operation-brief.md`, "Documents, in the target repository" and "Value audit". Related: ADR-D-0052 (the value audit), ADR-D-0065 (what a verdict authorizes), ADR-D-0042 (extensions at closeout).
