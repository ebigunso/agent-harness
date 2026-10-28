---
status: proposed
adr_type: design
date: 2026-10-29
deciders: ["ebigunso"]
consulted: ["Claude Opus 5.5"]
informed: []
supersedes: ["ADR-D-0041-a-ratified-brief-authorizes-a-plan-only-through-a-closed-plan-review-and-a-value-audit-that-holds-nothing-above-the-run.md"]
superseded_by: null
depends_on: ["ADR-D-0036-a-product-philosophy-is-stated-only-by-the-product-owner-and-no-product-value-is-inferred-without-one.md", "ADR-D-0038-the-word-of-the-person-directing-the-work-reaches-an-orchestrator-session-directly-or-by-quoted-relay.md", "ADR-D-0052-the-orchestrator-never-grades-its-own-run-and-its-reading-is-compared-only-after-the-grades-are-fixed.md", "ADR-D-0064-non-trivial-work-is-authorized-only-by-the-person-directing-the-work-or-by-that-persons-ratified-brief.md", "ADR-D-0062-under-a-ratified-brief-the-orchestrator-session-asks-the-person-directing-the-work-nothing-and-presents-no-plan.md"]
---

# ADR-D-0065: In plan mode a ratified brief authorizes a plan only when the brief governs the work and its ratification reached the session, the plan review closed with nothing open, and the value audit finds every graded item covered or a cheap-to-undo extension and holds nothing above the run; the verdict covers the plan as it stands, and a plan under the brief that this route does not authorize does not run

Proposed on 2026-10-29 to replace ADR-D-0041; awaiting acceptance by the person directing the work, by name.

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. The product owner is whoever is entitled to state the product's values and to answer product-level questions for that work; when the person directing the work owns the product, both are that person. Counsel is the session the person directing the work opens for value discussion, separate from any Orchestrator session. The Orchestrator session is a session that holds the Orchestrator role (ADR-D-0020) and plans, dispatches and reports the work.

ADR-D-0064 names the ratified brief, carried to the work through the value audit, as the second source of authorization, makes it the only source for a plan under a brief, and leaves the conditions to a record per mode. In plan mode the unit of work is a plan, reviewed by a Reviewer and graded by the value audit (ADR-D-0052) before execution. The fork is which conditions on the brief, the review and the verdict must hold together for the plan to start without the person directing the work reading it, what the verdict then covers, and what becomes of a plan they do not authorize.

## Decision

- The second source authorizes a plan only when three conditions hold together.
  - A brief governs the work and the person directing the work ratified it: the governing brief is the one the hand-over named for this work, and a plan for other work is not under it; the ratification has reached the Orchestrator session as that person's own statement there or as a relay ADR-D-0038 admits, a status line in the brief file being no ratification; an amendment to the brief counts on the same terms as the brief.
  - The Reviewer's plan review has ended with no finding left open; a review loop that does not converge is a value question for the person directing the work, not a completed review.
  - After that review, the value audit has graded the plan and judged every item it grades to be either covered by a statement in a value document or a cheap-to-undo extension of statements the verdict names, with no item that requires a decision above the run.
- The third condition is what the brief calls a citing audit, as this record reads it: a plan some of whose items are such extensions, stated in no document, starts without the person directing the work seeing it.
- The audit grades two sides: the product side, against the brief and the product philosophy as ADR-D-0036 states, and the engineering side, against the engineering philosophy.
- A side that has no value document is not graded and does not stand in the way: in a repository with a ratified brief and no engineering philosophy, the plan's internal mechanics (how the work is structured, not what the product does) are not audited, and the plan starts all the same, without any person having seen it.
- The test for an irreversible or outward-facing action runs on every item on either side.
- The verdict is on the plan as it stands when execution starts: what is added to or changed in what the plan decides after the verdict is not authorized by that verdict, and before the changed item is built it goes back through its gate, for what changed: the plan review of the revision closed with nothing open, and then, under a governing brief, a new audit of the plan as it then stands, at plan draft, on which this route authorizes the revision or it does not run. A plan without a brief, which the first source authorized, is authorized again by that source (its explicit approval or its explicit waiver naming the approval step, as ADR-D-0064 defines it) after the review. Neither stands in for the review or the audit, and a second audit on unchanged inputs does not replace the first.
- A verdict that is missing, malformed, leaves any item ungraded, or grades nothing on the brief's side authorizes nothing.
- One item that requires a decision above the run means the second source does not authorize the plan: the item goes to the person directing the work through Counsel, or to the product owner through that person, as a value question, and the second source can authorize only on a new audit of the plan as it then stands, after the answer is in the value documents or the plan no longer makes that decision.
- A plan that contains an irreversible or outward-facing action that no standing approval in effect covers (ADR-D-0052) is authorized by the second source only when the plan states the action as taken on the decision of the one who holds the authority for it at its moment and not before; an action so stated does not count against the third condition; otherwise this route does not authorize that plan.
- A plan under the brief that this route does not authorize does not run and is never presented for approval, in the Orchestrator session or through Counsel; what the Orchestrator does then is ADR-D-0062's.
- The action itself waits in every case: authorizing a plan lets no item go ahead that the value audit holds for a decision above the run.

## Why

The brief carries the authority of the person directing the work only as far as the plan actually fits it, and the party that wrote the plan cannot be the one who says it fits; a closed review removes the plan defects that would make grading meaningless, and a verdict that grades every item and holds none above the run is the whole of what the audit can say for the plan. An item stated in no document but cheaply undone is let through because stopping the run on it would return the person directing the work to auditing each plan, which the brief exists to end. The verdict covers the plan as it stood because an audit of a plan that later changes has judged something else. A plan under the brief that the route does not authorize is not yet a plan that can run, and the person directing the work should never need to look at the Orchestrator session while the run is in progress, so no other approval is sought for it.

## Rejected Alternatives

- Only items covered by a statement count, and any extension sends the plan to the person directing the work: it stops the run where a direction can be reasonably inferred from what was documented; reopen if that person, shown such extensions at closeout, regularly rejects them.
- The audit runs before the plan review closes: the audit would grade items the review is about to change, and the verdict would bind a plan that no longer exists; reopen if plan reviews come to leave the plan's decisions untouched.
- A verdict missing a side's grades authorizes the other side: rejected outright; the plan is one unit of work, and half a verdict is no verdict on it.
- The verdict follows the plan through later changes: rejected outright; the Orchestrator would decide which changes need no new audit, which is the judgement ADR-D-0052 keeps from it.
- An irreversible action in a plan always keeps the plan from starting until the person directing the work has read it: it makes every plan with a publish or a merge in it one that person must read; reopen if an action stated as waiting for its decision is found executed before that decision.

## Decision Boundary

Invariant: in plan mode the second source authorizes a plan only through a governing brief whose ratification reached the session, a plan review closed with nothing open, and a value audit that grades every item on each side that has a document, finds each covered or a cheap-to-undo extension, and holds none above the run; the verdict covers the plan as it stood when execution started; a plan under the brief that the route does not authorize does not run and is presented to nobody; no item the audit holds goes ahead on either source; the Decision list states the rest.

Not covered: the sources of authorization themselves and what is never one (ADR-D-0064); what the Orchestrator does when this route does not authorize a plan, and how questions travel under a brief (ADR-D-0062); a small change built without a plan (ADR-D-0055); goal mode; the grade names and their definitions, which no record states and the audit's mandate owns (ADR-D-0052 leaves them uncovered); the audit's procedure and the dispatch wording (ADR-D-0052); what the product side is graded against where no product philosophy exists (ADR-D-0036); what is shown of the extensions at closeout (ADR-D-0042); merge authorization; how the plan records the ratification and the verdict; the wording of the Plan Gate and the lifecycle reference.

## Validation

- A plan executed under the second source records the ratification as it reached the session, the plan review ended with no finding left open, and the audit's dispatch and verdict on the plan as executed; the verdict shows no ungraded item and no item requiring a decision above the run other than an action the plan states as taken on the decision of the one who holds the authority for it at its moment.
- A probe under a brief whose ratification reached the session only as the brief's status line has no governing brief, and presents the plan and ends the turn; a probe under a governing brief whose verdict leaves an item ungraded ends the turn blocked, naming that condition, with no plan presented.
- A change to what the plan decides after the verdict shows a plan review closed with nothing open and then, under a governing brief, a later audit of the plan as it then stands, before the changed item is executed; a plan without a brief shows the first source's approval or waiver of the revision after the review.

## Revisit When

- Plans started under the second source turn out, when the person directing the work reads them afterwards, to be ones that person would have stopped. A miss that traces to how items are graded reopens the grade definitions first, as ADR-D-0052 says; a miss on the conditions reopens this record.
- An action a plan stated as waiting for its decision is found executed before that decision.
- On 2026-09-30 the three conditions had been met together by no run on any runtime; a run that meets them and is later found to have needed the first source reopens this record.
- On 2026-10-29 no run under a brief had yet ended with nothing asked of the person directing the work in the Orchestrator session; a run under a brief whose plan this route did not authorize and that asked that person anything there reopens this record.

## More Information

Replaces ADR-D-0041 in full: everything it decided is carried; a plan under a brief that this route does not authorize does not run and is presented to nobody, the irreversible-action case and a revision under a brief no longer fall back to the first source, and a value question goes through Counsel. Source of intent: `docs/coding-agent/briefs/completed/value-level-operation-brief.md`, "Stops during a run", "Value audit" and "Lifecycle"; the brief "A quiet Orchestrator session under a brief" (`quiet-orchestrator-session-brief.md`), "Who it is for and why" and "What the plugin states". Related records: ADR-D-0064 (the sources of authorization), ADR-D-0062 (no question in the Orchestrator session under a brief), ADR-D-0052 (the value audit), ADR-D-0038 (how the ratification reaches the session), ADR-D-0036 (the product side's documents), ADR-D-0042 (extensions at closeout), ADR-D-0055 (a small change built without a plan).
