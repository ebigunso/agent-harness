---
status: proposed
adr_type: design
date: 2026-11-19
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "Claude Fable 5.2", "GPT-6 Astra"]
informed: []
supersedes: ["ADR-D-0035-counsel-reaches-into-the-work-only-by-quick-reads-a-read-only-researcher-and-consulted-advice.md"]
superseded_by: null
---

# ADR-D (not yet numbered): Counsel may take a view from any other model the environment offers on any matter of a discussion, and takes one before a consequential new direction is settled or a foundational assumption is revised

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session role that person talks with about what the product does or should do. A view is another model's answer to a question of the discussion.

What Counsel and the person directing the work settle between them is to be examined by more than the one model that helped shape it, because a discussion held between one person and one model carries that model's defaults unexamined, and that costs most where a new direction or a foundational assumption is being settled. Requiring the view for the engineering discussion, from a model of a family other than Counsel's own, fails that in two ways. It leaves every other matter unexamined, though the need is the same there. And it presumes an arrangement: which model Counsel runs on, and that exactly one other kind is at hand, when environments differ in both, some offering several models to consult and some none. The fork is on which matters a view is taken, from which model, and when taking one is a duty.

## Decision

- Counsel may take a view from any other model the environment offers, on any matter of the discussion, chosen for what the workspace's record says that model is good for. No family is named, and nothing assumes which model Counsel runs on.
- Taking a view is a duty before a consequential new direction is settled or a foundational assumption is revised. Otherwise it is Counsel's judgement, or the asking of the person directing the work.
- Where no other model is available, Counsel says so and goes on. That person is not asked to authorise going on each time.
- The view is input, marked with its source: never that person's view and never a decision.

## Why

Counsel's confidence in a direction it helped shape is a builder's confidence, and the product philosophy's "What goes wrong, in order" does not take confidence on the builder's word; another model is how a default the first does not see is found. The duty follows what is at stake and not a kind of document or a pairing of models, so that it holds whichever model Counsel runs on, and it does not turn a missing model into a question that person cannot weigh ("Who it is for").

## Rejected Alternatives

- The view is required for the engineering discussion and from a model of a family other than Counsel's, as ADR-D-0035 had it: it lost because it presumes which models are in use and leaves other matters unexamined; reopen if views taken outside the engineering discussion are found to add nothing that person uses.
- A view is a duty on every matter: it lost because the cost of obtaining one is then paid where little is at stake; reopen if directions settled on Counsel's judgement without a view are found to have carried a default another model would have caught.
- The view is left to Counsel's judgement throughout: it lost because a model's defaults go unexamined exactly where Counsel does not think to ask; reopen if the views obtained under the duty are found to add nothing that person uses.
- Where no other model is available, that person decides each time whether to go on: it lost because it puts to that person a question about the machinery whose options they cannot tell apart; reopen if directions settled without a view are found to be ones that person would have waited on.
- A named route for the view: it lost because it binds the harness to one environment; reopen if one route is found available in every supported runtime.

## Decision Boundary

Not covered: by which route a view is obtained and from which model; what the workspace's record says each model is good for, and how a role's model is chosen (ADR-D-0068); what makes a direction consequential or an assumption foundational in a given case, which is Counsel's judgement; how the question is put and how the reply is kept, which Counsel's text states; that an adviser is given no part of the work (`ADR-D-counsel-reads-code-only-to-serve-a-discussion-and-takes-no-part-in-doing-or-checking-a-runs-work.md`).

## Validation

The decision is broken where a consequential new direction was settled or a foundational assumption revised with no view from another model and that person was not told that none was to be had; where a view was presented as that person's or acted on as a decision; where a view entered a discussion without its source; where that person was asked to authorise going on without one; or where harness text names a family of model or assumes which model Counsel runs on.

## Revisit When

- The premise that another model sees defaults the first does not fails: the views obtained are found to add nothing the person directing the work uses.
- The premise that Counsel can tell when a direction is consequential or an assumption foundational fails: one is found settled without a view that should have had one.

## More Information

With `ADR-D-counsel-reads-code-only-to-serve-a-discussion-and-takes-no-part-in-doing-or-checking-a-runs-work.md`, replaces ADR-D-0035 in full. Changed here: ADR-D-0035 required the view for the engineering discussion, from a model of a family other than Counsel's, and had the person directing the work decide whether to go on without one; this record allows a view on any matter from any other model, makes it a duty by what is at stake, and has Counsel say that none is available and go on. Carried from it: that no route is named, and that the view is input marked with its source. Moved out: that the question is put as the discussion put it and that the reply is kept verbatim with its model and route named, which Counsel's text states. Source of intent: the brief "One conversation with Counsel", "Directed during the run".
