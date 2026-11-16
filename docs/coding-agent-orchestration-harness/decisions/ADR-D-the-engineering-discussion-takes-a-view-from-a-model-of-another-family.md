---
status: proposed
adr_type: design
date: 2026-11-17
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "Claude Fable 5.2"]
informed: []
supersedes: ["ADR-D-0035-counsel-reaches-into-the-work-only-by-quick-reads-a-read-only-researcher-and-consulted-advice.md"]
superseded_by: null
---

# ADR-D (not yet numbered): For the engineering discussion Counsel obtains a view from a model of a family other than its own, by whatever route the environment provides

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session role that person talks with about what the product does or should do. The engineering discussion is the part of that talk that settles how the project is to be engineered, the engineering philosophy included.

The engineering discussion is held between one person and one model, and gains from the view of a model of another family. The harness runs in many environments, on different platforms, and the model Counsel runs on differs between them, so no single way of reaching another model exists everywhere. The fork is whether the outside view is optional, bound to one route, or required by whatever route the environment provides.

## Decision

- For the engineering discussion, Counsel obtains a view from a model of a different family than its own.
- No route is named. Counsel uses whatever route the environment provides and says which it used.
- The view enters the discussion as that model's, marked with its source: an input, never the view of the person directing the work and never a decision.
- Where the environment provides no route, Counsel says so, and that person decides whether to go on without the view.

## Why

An engineering philosophy written with one model family alone carries that family's defaults unexamined, and the engineering philosophy's "Where the value is" puts the worth of the harness where an agent's instinct would take it the wrong way: a second family is how an instinct shared by the first is found. Because platforms and Counsel's model differ between environments, the duty names no route, only that one is used and said.

## Rejected Alternatives

- A named route for the outside view, one peer seat for example: it lost because it binds the harness to one environment; reopen if one route is found available in every supported runtime.
- The outside view left optional, Counsel asking another model only when it chooses: it lost because a family's defaults then go unexamined exactly where Counsel does not think to ask; reopen if the views obtained are found to add nothing the person directing the work uses.

## Decision Boundary

Not covered: which route Counsel uses and which model of another family; how the question is put and how the reply is kept, which Counsel's text states; how a runtime lets Counsel consult another model; advice Counsel asks for outside the engineering discussion; that an adviser is given no part of the work (`ADR-D-counsel-reads-code-only-to-serve-a-discussion-and-takes-no-part-in-doing-or-checking-a-runs-work.md`); how a role's model is chosen (ADR-D-0068).

## Validation

The decision is broken where an engineering philosophy, or a change to one, was settled with no view from a model of another family and the person directing the work was not told that none was to be had; where such a view was presented as that person's or acted on as a decision; where Counsel did not say by which route the view came; or where harness text requires one route.

## Revisit When

- The premise that a model of another family sees defaults the first does not fails: the views obtained are found to add nothing the person directing the work uses.
- One route to a model of another family is found available in every supported runtime, so that naming it would bind the harness to no single environment.

## More Information

With `ADR-D-counsel-reads-code-only-to-serve-a-discussion-and-takes-no-part-in-doing-or-checking-a-runs-work.md`, replaces ADR-D-0035 in full; the decision carried here is the same. ADR-D-0035 stated no revisit condition for this decision; the two above restate the conditions on which its rejected alternatives reopen. Moved out: that the question is put as the discussion put it and that the reply is kept verbatim with its model and route named, which Counsel's text states. Source of intent: `docs/coding-agent/briefs/completed/first-use-in-a-fresh-repository-brief.md`, "A view from a model of another family".
