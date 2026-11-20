---
status: accepted
adr_type: design
date: 2026-11-19
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "Claude Fable 5.2", "GPT-6 Astra"]
informed: []
supersedes: ["superseded/ADR-D-0035-counsel-reaches-into-the-work-only-by-quick-reads-a-read-only-researcher-and-consulted-advice--superseded-by-ADR-D-0098.md"]
superseded_by: null
---

# ADR-D-0101: Counsel takes a view from another model before a consequential new direction is settled or a foundational assumption is revised

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session role that person talks with about what the product does or should do. A view is another model's answer to a question of the discussion.

A discussion held between one person and one model carries that model's defaults unexamined, and that costs most where a new direction or a foundational assumption is being settled; what is settled there is to have been examined by more than the one model that helped shape it. Counsel may take a view from any other model the environment offers (ADR-D-0098). Left to Counsel's judgement throughout, the view is missing exactly where Counsel does not think to ask. Required on every matter, its cost is paid where little is at stake. Tied to one kind of discussion, it follows the kind and not what is at stake. And some environments offer no other model at all. The fork is when taking a view is a duty, and what is done where none is to be had.

## Decision

- Taking a view from another model is a duty before a consequential new direction is settled or a foundational assumption is revised. Otherwise it is Counsel's judgement, or the asking of the person directing the work.
- Where no other model is available, Counsel says so and goes on. That person is not asked to authorise going on each time.

## Why

Counsel's confidence in a direction it helped shape is a builder's confidence, and the product philosophy's "What goes wrong, in order" does not take confidence on the builder's word. The duty follows what is at stake and not a kind of document, and it does not turn a missing model into a question that person cannot weigh ("Who it is for").

## Rejected Alternatives

- The duty follows the kind of discussion, the engineering discussion, as ADR-D-0035 had it: it lost because a direction settled in any other discussion is left unexamined however much is at stake; reopen if views taken outside the engineering discussion are found to add nothing that person uses.
- A view is a duty on every matter: it lost because the cost of obtaining one is then paid where little is at stake; reopen if directions settled on Counsel's judgement without a view are found to have carried a default another model would have caught.
- The view is left to Counsel's judgement throughout: it lost because a model's defaults go unexamined exactly where Counsel does not think to ask; reopen if the views obtained under the duty are found to add nothing that person uses.
- Where no other model is available, that person decides each time whether to go on: it lost because it puts to that person a question about the machinery whose options they cannot tell apart; reopen if directions settled without a view are found to be ones that person would have waited on.

## Decision Boundary

Not covered: from which model and on which matters a view may be taken, and what a view is once taken (ADR-D-0098); what makes a direction consequential or an assumption foundational in a given case, which is Counsel's judgement; by which route a view is obtained; how the question is put and how the reply is kept, which Counsel's text states.

## Validation

The decision is broken where a consequential new direction was settled or a foundational assumption revised with no view from another model and that person was not told that none was to be had; or where that person was asked to authorise going on without one.

## Revisit When

- The premise that Counsel can tell when a direction is consequential or an assumption foundational fails: one is found settled without a view that should have had one.

## More Information

With ADR-D-0099 and ADR-D-0098, replaces ADR-D-0035 in full. Changed here: ADR-D-0035 required the view for the engineering discussion and had the person directing the work decide whether to go on without one; this record makes the view a duty by what is at stake, and has Counsel say that none is available and go on. Source of intent: the brief "One conversation with Counsel", "Directed during the run".
