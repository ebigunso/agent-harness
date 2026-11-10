---
status: accepted
adr_type: design
date: 2026-11-07
deciders: ["ebigunso"]
consulted: ["Claude Opus 5.5"]
informed: []
supersedes: ["superseded/ADR-D-0041-a-ratified-brief-authorizes-a-plan-only-through-a-closed-plan-review-and-a-value-audit--superseded-by-ADR-D-0065.md"]
superseded_by: null
depends_on: ["ADR-D-0036-a-product-philosophy-is-stated-only-by-the-product-owner-and-no-product-value-is-inferred-without-one.md", "ADR-D-0038-the-word-of-the-person-directing-the-work-reaches-an-orchestrator-session-directly-or-by-quoted-relay.md", "ADR-D-0052-the-orchestrator-never-grades-its-own-run-and-its-reading-is-compared-only-after-the-grades-are-fixed.md", "ADR-D-0064-non-trivial-work-is-authorized-only-by-the-person-directing-the-work-or-by-that-persons-ratified-brief.md"]
---

# ADR-D-0065: A ratified brief authorizes a plan or a goal envelope only on a closed review and a value audit that holds nothing

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. The product owner is whoever is entitled to state the product's values and to answer product-level questions for that work; when the person directing the work owns the product, both are that person. The Orchestrator session is a session that holds the Orchestrator role (ADR-D-0020) and plans, dispatches and reports the work. A unit here is a plan, or the envelope of a goal-mode run together with its goal condition.

ADR-D-0064 makes the ratified governing brief, carried to the work by the value audit, the only authority for every unit of work under a brief, and leaves the conditions to a record for each kind of unit. A plan and a goal envelope are each fixed before anything of them executes, reviewed by a Reviewer and graded by the value audit (ADR-D-0052). The fork is which conditions on the brief, the review and the verdict must hold together for such a unit to start without the person directing the work reading it, and what the verdict then covers.

## Decision

- Under a ratified governing brief, the ratification authorizes a plan or a goal envelope only when all of these hold together, on the same unchanged unit, before it executes:
  - A brief governs the work and the person directing the work ratified it; an amendment to the brief counts on the same terms as the brief.
  - A Reviewer's review of the whole unit, for a goal envelope its goal condition and every clause of the envelope, has closed with no finding left open.
  - The value audit, judging independently, has graded every item of that same unit on each side that has a value document, judged each either covered by a statement in a value document or a cheap-to-undo extension of statements the verdict names, and held none for a decision above the run.
- A unit some of whose items are such extensions, stated in no document, starts without the person directing the work seeing it.
- The audit grades two sides: the product side, against the brief and the product philosophy as ADR-D-0036 states, and the engineering side, against the engineering philosophy. A side that has no value document is not graded and does not stand in the way: in a repository with a ratified brief and no engineering philosophy, the unit's internal mechanics (how the work is structured, not what the product does) are not audited, and the unit starts all the same, without any person having seen it.
- The test for an irreversible or outward-facing action runs on every item on either side.
- A verdict that is missing, leaves any item ungraded, or grades nothing on the brief's side authorizes nothing.
- One item held for a decision above the run means the ratification does not authorize the unit; it can authorize only on a new audit of the unit as it then stands, once the answer is in the value documents or the unit no longer makes that decision.
- A unit containing an irreversible or outward-facing action that no standing approval in effect covers (ADR-D-0052) is authorized only when the unit states the action as taken on the decision of whoever holds the authority for it, at its moment and not before; an action so stated does not count as an item held above the run; otherwise the ratification does not authorize the unit.
- The action itself waits in every case: authorizing a unit lets no item go ahead that the value audit holds for a decision above the run.
- The verdict covers the unit as it stands when execution starts. What is added to or changed in what a plan decides, or in a goal envelope, afterwards is not authorized by it and needs fresh authorization before it is built or acted on, from the same authority on that authority's own terms: under a brief, these conditions on the unit as it then stands; without one, the person directing the work's own approval or waiver. A repeated judgement on unchanged inputs is not fresh authorization.

## Why

The brief carries the authority of the person directing the work only as far as the unit actually fits it, and the party that wrote the unit cannot be the one who says it fits, so only a verdict that grades every item of the reviewed unit and holds none above the run can carry it, and only for the unit it judged. An item stated in no document but cheaply undone is let through, because stopping on it would return that person to auditing each plan.

## Rejected Alternatives

- Only items covered by a statement count, and any extension sends the unit to the person directing the work: it stops the run where a direction can be reasonably inferred from what was documented; reopen if that person, shown such extensions at closeout, regularly rejects them.
- A verdict on a version of the unit other than the one whose review closed, such as one graded while the review was changing it: it lost because the verdict would bind a unit it did not judge; reopen if reviews come to leave the unit's decisions untouched.
- A verdict missing a side's grades authorizes the other side: rejected outright; the unit is one unit of work, and half a verdict is no verdict on it.
- The verdict follows the unit through later changes: rejected outright; the Orchestrator would decide which changes need no new audit, which is the judgement ADR-D-0052 keeps from it.
- An irreversible action in a unit always keeps the unit from starting until the person directing the work has read it: it makes every plan with a publish or a merge in it one that person must read; reopen if an action stated as waiting for its decision is found executed before that decision.
- A goal envelope authorized on a review of part of it, such as its goal condition and its exclusion of irreversible actions: rejected outright; a review of part of the unit is not a review closed on the unit the verdict authorizes, and an unreviewed clause would bound the loop on a grade alone.

## Decision Boundary

Invariant: under a ratified governing brief, a plan or a goal envelope is authorized only through a review of the whole unit closed with nothing open and an independent value audit, both on the same unchanged unit before it executes, the audit grading every item on each side that has a document, finding each covered or a cheap-to-undo extension, and holding none above the run; an irreversible or outward-facing action counts only when stated as waiting for its moment; the verdict covers the unit as it stood when execution started, and a change after it needs fresh authorization from the same authority before it is built; no item the audit holds goes ahead.

Not covered: the authorities themselves, what is never one, and that under a brief nothing else authorizes (ADR-D-0064); which brief governs the work and what counts as its ratification having reached the session (ADR-D-0038 and the harness text); what the Orchestrator does when these conditions are not met, which the harness text states; how a review of a plan or an envelope is carried out, how a revision is reviewed and audited and at which position, and whether the review or the audit runs ahead of the other, which the harness text states; how a question the audit holds reaches the person directing the work or the product owner (ADR-D-0062); what an envelope consists of and that the loop never changes it (ADR-D-0066); how a goal run is graded once its loop starts, and what the run does with an item held during it (ADR-D-0063, ADR-D-0067); what a goal loop may tighten in its own stops and pass conditions, which goal mode's text states; a small change built without a plan (ADR-D-0055); the grade names and their definitions, which no record states and the audit's mandate owns (ADR-D-0052 leaves them uncovered); the audit's procedure and how it is asked (ADR-D-0052); what the product side is graded against where no product philosophy exists (ADR-D-0036); what is shown of the extensions at closeout (ADR-D-0042); merge authorization; how the unit records the ratification and the verdict; the wording of the harness text that states these conditions.

## Validation

- Review of any change to the harness text asks: can a plan or a goal envelope start on a ratified brief without a closed review of the whole unit and a verdict that grades every item, both on that same unchanged unit, or with an item the verdict holds above the run other than an action stated as waiting for its moment; and can a change to what a plan decides, or to an envelope, be built or acted on by the verdict given before it?

## Revisit When

- Units started on the ratified brief turn out, when the person directing the work reads them afterwards, to be ones that person would have stopped. A miss that traces to how items are graded reopens the grade definitions before this record, as ADR-D-0052 says; a miss on these conditions reopens this record.
- An action a unit stated as waiting for its decision is found executed before that decision.
- On 2026-09-30 no run on any runtime had met these conditions together for a plan; a run that meets them and is later found to have needed the person directing the work to read the plan reopens this record.
- On 2026-11-07 no goal envelope had been authorized on these conditions; a goal run so authorized and later found to have needed the person directing the work to read its envelope reopens this record.

## More Information

Replaces ADR-D-0041 in full: everything it decided is carried and extended to a goal envelope, except what follows when the ratification does not authorize a plan under a brief, which the harness text holds; where ADR-D-0041 sent a plan with an unstated irreversible action, or a revision under a brief, to the person directing the work's own approval, the ratification simply does not authorize it. Source of intent: `docs/coding-agent/briefs/completed/value-level-operation-brief.md`, "Who it is for and why", "Stops during a run", "Value audit" and "Lifecycle"; the brief "A quiet Orchestrator session under a brief" (`docs/coding-agent/briefs/active/quiet-orchestrator-session-brief.md`), "What the plugin states" and "Directed during the run". Where a held question goes, how a review that does not converge is handled, the position at which a revision is audited, and the moves when the ratification does not authorize a unit are the harness text's and change without this record. Related records: ADR-D-0064 (who authorizes non-trivial work), ADR-D-0062 (no question in the Orchestrator session under a brief), ADR-D-0063 (the value audit in a goal run), ADR-D-0067 (a determined remedy carried out without a stop under a brief), ADR-D-0066 (the envelope), ADR-D-0052 (the value audit), ADR-D-0038 (how the ratification reaches the session), ADR-D-0036 (the product side's documents), ADR-D-0042 (extensions at closeout), ADR-D-0055 (a small change built without a plan).
