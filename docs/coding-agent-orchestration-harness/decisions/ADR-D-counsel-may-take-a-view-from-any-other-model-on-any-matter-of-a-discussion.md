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

# ADR-D (not yet numbered): Counsel may take a view from any other model the environment offers, on any matter of a discussion, as input marked with its source

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session role that person talks with about what the product does or should do. A view is another model's answer to a question of the discussion.

What Counsel and the person directing the work settle between them is to be examined by more than the one model that helped shape it, because a discussion held between one person and one model carries that model's defaults unexamined. Keeping the view to the engineering discussion, and to a model of a family other than Counsel's own, fails that in two ways. It leaves every other matter unexamined, though the need is the same there. And it presumes an arrangement: which model Counsel runs on, and that exactly one other kind is at hand, when environments differ in both, some offering several models to consult and some none. The fork is on which matters a view may be taken, from which model, and what a view is once taken.

## Decision

- Counsel may take a view from any other model the environment offers, on any matter of the discussion, chosen for what the workspace's record says that model is good for. No family is named, and nothing assumes which model Counsel runs on.
- The view is input, marked with its source: never the view of the person directing the work and never a decision.

## Why

Another model is how a default the first does not see is found, and the product philosophy's "What goes wrong, in order" does not take confidence on the builder's word; neither the matter nor a pairing of models bounds that, so it holds whichever model Counsel runs on. A view marked with its source stays one model's answer, and a decision stays the act of the person directing the work.

## Rejected Alternatives

- The view is kept to the engineering discussion and to a model of a family other than Counsel's, as ADR-D-0035 had it: it lost because it presumes which models are in use and leaves other matters unexamined; reopen if views taken outside the engineering discussion are found to add nothing that person uses.
- A named route for the view: it lost because it binds the harness to one environment; reopen if one route is found available in every supported runtime.

## Decision Boundary

Not covered: when taking a view is a duty, and what is done where no other model is available (`ADR-D-counsel-takes-a-view-from-another-model-before-a-consequential-direction-is-settled.md`); by which route a view is obtained and from which model; what the workspace's record says each model is good for, and how a role's model is chosen (ADR-D-0068); how the question is put and how the reply is kept, which Counsel's text states; that an adviser is given no part of the work (`ADR-D-counsel-reads-code-only-to-serve-a-discussion-and-takes-no-part-in-doing-or-checking-a-runs-work.md`).

## Validation

The decision is broken where a view was presented as that person's or acted on as a decision; where a view entered a discussion without its source; or where harness text names a family of model or assumes which model Counsel runs on.

## Revisit When

- The premise that another model sees defaults the first does not fails: the views obtained are found to add nothing the person directing the work uses.

## More Information

With `ADR-D-counsel-reads-code-only-to-serve-a-discussion-and-takes-no-part-in-doing-or-checking-a-runs-work.md` and `ADR-D-counsel-takes-a-view-from-another-model-before-a-consequential-direction-is-settled.md`, replaces ADR-D-0035 in full. Changed here: ADR-D-0035 kept the view to the engineering discussion and to a model of a family other than Counsel's; this record allows a view on any matter from any other model. Carried from it: that no route is named, and that the view is input marked with its source. Moved out: that the question is put as the discussion put it and that the reply is kept verbatim with its model and route named, which Counsel's text states. Source of intent: the brief "One conversation with Counsel", "Directed during the run".
