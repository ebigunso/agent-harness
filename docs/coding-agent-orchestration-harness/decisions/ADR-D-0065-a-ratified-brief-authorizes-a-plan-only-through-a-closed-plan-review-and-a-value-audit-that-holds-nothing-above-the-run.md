---
status: proposed
adr_type: design
date: 2026-10-29
deciders: ["ebigunso"]
consulted: ["Claude Opus 5.5"]
informed: []
supersedes: ["ADR-D-0041-a-ratified-brief-authorizes-a-plan-only-through-a-closed-plan-review-and-a-value-audit-that-holds-nothing-above-the-run.md"]
superseded_by: null
depends_on: ["ADR-D-0036-a-product-philosophy-is-stated-only-by-the-product-owner-and-no-product-value-is-inferred-without-one.md", "ADR-D-0038-the-word-of-the-person-directing-the-work-reaches-an-orchestrator-session-directly-or-by-quoted-relay.md", "ADR-D-0052-the-orchestrator-never-grades-its-own-run-and-its-reading-is-compared-only-after-the-grades-are-fixed.md", "ADR-D-0064-non-trivial-work-is-authorized-only-by-the-person-directing-the-work-or-by-that-persons-ratified-brief.md"]
---

# ADR-D-0065: A ratified brief authorizes a plan only through a closed plan review and a value audit that holds nothing above the run

Proposed on 2026-10-29 to replace ADR-D-0041; awaiting acceptance by the person directing the work, by name.

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. The product owner is whoever is entitled to state the product's values and to answer product-level questions for that work; when the person directing the work owns the product, both are that person. The Orchestrator session is a session that holds the Orchestrator role (ADR-D-0020) and plans, dispatches and reports the work.

ADR-D-0064 names the ratified brief, carried to the work through the value audit, as the second source of authorization, makes it the only source for a plan under a brief, and leaves the conditions to a record per mode. In plan mode the unit of work is a plan, reviewed by a Reviewer and graded by the value audit (ADR-D-0052) before execution. The fork is which conditions on the brief, the review and the verdict must hold together for the plan to start without the person directing the work reading it, and what the verdict then covers.

## Decision

- In plan mode the second source authorizes a plan only when three conditions hold together, all on the same unchanged plan, before it executes.
  - A brief governs the work and the person directing the work ratified it; an amendment to the brief counts on the same terms as the brief.
  - The Reviewer's plan review has closed with no finding left open.
  - The value audit, judging independently, has graded every item of that same plan on each side that has a value document, and judged each either covered by a statement in a value document or a cheap-to-undo extension of statements the verdict names, holding none for a decision above the run.
- A plan some of whose items are such extensions, stated in no document, starts without the person directing the work seeing it.
- The audit grades two sides: the product side, against the brief and the product philosophy as ADR-D-0036 states, and the engineering side, against the engineering philosophy. A side that has no value document is not graded and does not stand in the way: in a repository with a ratified brief and no engineering philosophy, the plan's internal mechanics (how the work is structured, not what the product does) are not audited, and the plan starts all the same, without any person having seen it.
- The test for an irreversible or outward-facing action runs on every item on either side.
- A verdict that is missing, leaves any item ungraded, or grades nothing on the brief's side authorizes nothing.
- One item held for a decision above the run means this route does not authorize the plan; it can authorize only on a new audit of the plan as it then stands, once the answer is in the value documents or the plan no longer makes that decision.
- A plan containing an irreversible or outward-facing action that no standing approval in effect covers (ADR-D-0052) is authorized by this route only when the plan states the action as taken on the decision of whoever holds the authority for it, at its moment and not before; an action so stated does not count against the third condition; otherwise this route does not authorize that plan.
- The action itself waits in every case: authorizing a plan lets no item go ahead that the value audit holds for a decision above the run.
- The verdict covers the plan as it stands when execution starts. What is added to or changed in what the plan decides afterwards is not authorized by it and needs fresh authorization before it is built, from the same authority on that authority's own terms: under a brief, this route on the plan as it then stands; without one, the person directing the work's own approval or waiver. A second judgement on unchanged inputs is not fresh authorization.

## Why

The brief carries the authority of the person directing the work only as far as the plan actually fits it, and the party that wrote the plan cannot be the one who says it fits, so only a verdict that grades every item of the reviewed plan and holds none above the run can carry it, and only for the plan it judged. An item stated in no document but cheaply undone is let through because stopping on it would return that person to auditing each plan, which the brief exists to end ("Value-level operation", "Who it is for and why" and "Stops during a run": where a direction can be reasonably inferred, the run keeps going).

## Rejected Alternatives

- Only items covered by a statement count, and any extension sends the plan to the person directing the work: it stops the run where a direction can be reasonably inferred from what was documented; reopen if that person, shown such extensions at closeout, regularly rejects them.
- A verdict on a version of the plan other than the one whose review closed, such as one graded while the review was changing it: it lost because the verdict would bind a plan it did not judge; reopen if plan reviews come to leave the plan's decisions untouched.
- A verdict missing a side's grades authorizes the other side: rejected outright; the plan is one unit of work, and half a verdict is no verdict on it.
- The verdict follows the plan through later changes: rejected outright; the Orchestrator would decide which changes need no new audit, which is the judgement ADR-D-0052 keeps from it.
- An irreversible action in a plan always keeps the plan from starting until the person directing the work has read it: it makes every plan with a publish or a merge in it one that person must read; reopen if an action stated as waiting for its decision is found executed before that decision.

## Decision Boundary

Invariant: in plan mode the second source authorizes a plan only through a ratified governing brief, a plan review closed with nothing open and an independent value audit, both on the same unchanged plan before it executes, the audit grading every item on each side that has a document, finding each covered or a cheap-to-undo extension, and holding none above the run; an irreversible or outward-facing action counts only when stated as waiting for its moment; the verdict covers the plan as it stood when execution started, and a change after it needs fresh authorization from the same authority before it is built; no item the audit holds goes ahead on either source.

Not covered: the sources of authorization themselves, what is never one, and what follows when this route does not authorize a plan (ADR-D-0064); which brief governs the work and what counts as its ratification having reached the session (ADR-D-0038 and the harness text); how a revision is reviewed and audited and at which position, which the harness text states; whether the review or the audit runs first, and how they are scheduled, which the harness text states; how a question the audit holds reaches the person directing the work or the product owner (ADR-D-0062); a small change built without a plan (ADR-D-0055); goal mode; the grade names and their definitions, which no record states and the audit's mandate owns (ADR-D-0052 leaves them uncovered); the audit's procedure and how it is asked (ADR-D-0052); what the product side is graded against where no product philosophy exists (ADR-D-0036); what is shown of the extensions at closeout (ADR-D-0042); merge authorization; how the plan records the ratification and the verdict; the wording of the harness text that states the route.

## Validation

- Review of any change to the harness text asks: can a plan start on a ratified brief without a closed plan review and a verdict that grades every item, both on that same unchanged plan, or with an item the verdict holds above the run other than an action stated as waiting for its moment; and can a change to what a plan decides be built on the verdict given before it?

## Revisit When

- Plans started under the second source turn out, when the person directing the work reads them afterwards, to be ones that person would have stopped. A miss that traces to how items are graded reopens the grade definitions first, as ADR-D-0052 says; a miss on the conditions reopens this record.
- An action a plan stated as waiting for its decision is found executed before that decision.
- On 2026-09-30 the three conditions had been met together by no run on any runtime; a run that meets them and is later found to have needed the person directing the work to read the plan reopens this record.

## More Information

Replaces ADR-D-0041 in full: everything it decided is carried, except what follows when this route does not authorize a plan under a brief, which ADR-D-0064 holds; where ADR-D-0041 sent a plan with an unstated irreversible action, or a revision under a brief, to the first source, this route simply does not authorize it. Source of intent: `docs/coding-agent/briefs/completed/value-level-operation-brief.md`, "Who it is for and why", "Stops during a run", "Value audit" and "Lifecycle"; the brief "A quiet Orchestrator session under a brief" (`docs/coding-agent/briefs/active/quiet-orchestrator-session-brief.md`), "What the plugin states". Where a held question goes, how a non-converging plan review is handled, the position at which a revision is audited, and the moves when this route does not authorize a plan are the harness text's and change without this record. Related records: ADR-D-0064 (the sources of authorization), ADR-D-0062 (no question in the Orchestrator session under a brief), ADR-D-0052 (the value audit), ADR-D-0038 (how the ratification reaches the session), ADR-D-0036 (the product side's documents), ADR-D-0042 (extensions at closeout), ADR-D-0055 (a small change built without a plan).
