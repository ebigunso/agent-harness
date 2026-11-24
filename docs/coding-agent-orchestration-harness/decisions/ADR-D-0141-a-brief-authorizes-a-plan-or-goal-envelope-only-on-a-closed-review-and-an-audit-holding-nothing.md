---
status: proposed
adr_type: design
date: 2026-11-24
deciders: ["ebigunso"]
consulted: ["Claude Opus 5.5"]
informed: []
supersedes: ["ADR-D-0065-a-ratified-brief-authorizes-a-plan-or-a-goal-envelope-only-on-a-closed-review-and-a-value-audit-that-holds-nothing.md"]
superseded_by: null
depends_on: ["ADR-D-0036-a-product-philosophy-is-stated-only-by-the-product-owner-and-no-product-value-is-inferred-without-one.md", "ADR-D-0112-the-persons-word-reaches-an-orchestrator-session-in-it-or-by-counsels-quoted-relay.md", "ADR-D-0134-the-orchestrator-never-grades-its-own-run-against-the-value-documents.md", "ADR-D-0139-non-trivial-work-is-authorized-only-by-the-person-directing-the-work.md", "ADR-D-0140-under-a-ratified-brief-no-unit-of-work-is-put-to-the-person-directing-the-work-for-approval.md"]
---

# ADR-D-0141: A ratified brief authorizes a plan or a goal envelope only on a closed review of the whole unit and an independent value audit that holds nothing

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. The product owner is whoever is entitled to state the product's values and to answer product-level questions for that work; when the person directing the work owns the product, both are that person. The Orchestrator session is a session that holds the Orchestrator role (ADR-D-0090) and plans, dispatches and reports the work. A unit here is a plan, or the envelope of a goal-mode run together with its goal condition.

The person directing the work ratifies a brief as the grounds for a piece of work so as not to audit each plan, and under that brief the ratification is the only authority for a unit, on conditions a record states for each kind of unit (ADR-D-0139, ADR-D-0140). A plan and a goal envelope are each fixed before anything of them executes. The ratification carries that person's authority only as far as the unit fits the brief, and the Orchestrator, which wrote the unit, cannot be the one to say that it fits; a run that stops on every item the documents do not state word for word, though, returns that person to auditing each plan. The fork is which conditions on the brief, the review and the value audit (ADR-D-0134, ADR-D-0082) must hold together for a plan or a goal envelope to start without that person reading it.

## Decision

- Under a ratified governing brief, the ratification authorizes a plan or a goal envelope only when all of these hold together, on the same unchanged unit, before any of it executes:
  - A brief governs the work and the person directing the work ratified it; an amendment to the brief counts on the same terms as the brief.
  - A Reviewer's review of the whole unit, for a goal envelope its goal condition and every clause of the envelope, has closed with no finding left open.
  - The value audit, judging independently, has given a verdict on that same unit that grades every item on each side that has a value document and grades at least one item on the brief's side, judges each item either covered by a statement in a value document or a cheap-to-undo extension of statements the verdict names, and holds none for a decision above the run.
- A unit some of whose items are such extensions, stated in no document, starts without the person directing the work seeing it.
- The product side is graded against the brief and the product philosophy, as ADR-D-0036 states, and the engineering side against the engineering philosophy. A side that has no value document is not graded and does not stand in the way of the authorization; the test for an irreversible or outward-facing action runs on every item all the same, on either side. For a plan-mode run, ADR-D-0134 states of the value audit that it grades the items on a side that has a value document, that an item on a side with none is not graded, and that the test for an irreversible or outward-facing action runs on every item.
- An item the value audit holds for a decision above the run does not go ahead, as ADR-D-0134 also states for a plan-mode run.
- One item held for a decision above the run means the ratification does not authorize the unit; it can authorize the unit only on a new audit of the unit as it then stands, once the answer is in the value documents or the unit no longer makes that decision.

## Why

The brief carries the authority of the person directing the work only as far as the unit actually fits it, and the party that wrote the unit cannot be the one who says it fits, so only a verdict that grades every item of the reviewed unit and holds none above the run can carry it, and only for the unit it judged; this is what the product philosophy's "What it must not be" states as "Not its own judge. A builder's confidence in its own work is not evidence, and a longer list of rules does not make it so." An item stated in no document but cheaply undone is let through, because stopping on it would return that person to auditing each plan, where the product philosophy's "What goes wrong, in order" has "If a decision can be undone and stays inside the work, it is made and reported, and not asked."

## Rejected Alternatives

- Only items covered by a statement count, and any extension sends the unit to the person directing the work: it stops the run where a direction can be reasonably inferred from what was documented; reopen if that person, shown such extensions at closeout, regularly rejects them.
- A verdict on a version of the unit other than the one whose review closed, such as one graded while the review was changing it: it lost because the verdict would bind a unit it did not judge; reopen if reviews come to leave the unit's decisions untouched.
- A verdict missing a side's grades authorizes the other side: rejected outright; the unit is one unit of work, and half a verdict is no verdict on it.
- A goal envelope authorized on a review of part of it, such as its goal condition and its exclusion of irreversible actions: rejected outright; a review of part of the unit is not a review closed on the unit the verdict authorizes, and an unreviewed clause would bound the loop on a grade alone.

## Decision Boundary

Not covered: the authorities themselves, what is never one, and that under a brief nothing else authorizes (ADR-D-0139, ADR-D-0140); which brief governs the work and what counts as its ratification having reached the session (ADR-D-0112 and the harness text); an irreversible or outward-facing action stated as waiting for its moment, which does not count as an item held above the run, and what a standing approval in effect does for such an action (ADR-D-0143); what a change to the unit after execution starts needs (ADR-D-0142); what the Orchestrator does when these conditions are not met, which the harness text states; how a review of a plan or an envelope is carried out, how a review that does not converge is handled, how a revision is reviewed and audited and at which position, and whether the review or the audit runs ahead of the other, which the harness text states; how a question the audit holds reaches the person directing the work or the product owner (ADR-D-0062); what an envelope consists of and that the loop never changes it (ADR-D-0084, ADR-D-0086); how a goal run is graded once its loop starts, and what the run does with an item held during it (ADR-D-0082, ADR-D-0067); what a goal loop may tighten in its own stops and pass conditions, which goal mode's text states; a small change built without a plan (ADR-D-0147); the grade names and their definitions, which no record states and the audit's mandate owns (ADR-D-0134 leaves them uncovered); the audit's procedure, which the harness text states, and the dispatch wording (ADR-D-0050); what the product side is graded against where no product philosophy exists (ADR-D-0036); which extensions are shown to the person directing the work, and that every one is kept in the run's records (ADR-D-0133, ADR-D-0132); merge authorization; how the unit records the ratification and the verdict; the wording of the harness text that states these conditions.

## Validation

The decision is broken where:

- a plan or a goal envelope started on a ratified brief without a review of the whole unit closed with no finding open, or without a verdict that graded every item on each side that has a value document and graded the brief's side, both on that same unchanged unit;
- a plan or a goal envelope started on a ratified brief with an item the verdict held above the run, other than an action stated as waiting for its moment;
- an item the value audit held for a decision above the run went ahead.

## Revisit When

- Units started on the ratified brief turn out, when the person directing the work reads them afterwards, to be ones that person would have stopped. A miss that traces to how items are graded reopens the grade definitions before this record, as ADR-D-0134 says for a plan-mode run; a miss on these conditions reopens this record.
- On 2026-09-30 no run on any runtime had met these conditions together for a plan; a run that meets them and is later found to have needed the person directing the work to read the plan reopens this record.
- On 2026-11-07 no goal envelope had been authorized on these conditions; a goal run so authorized and later found to have needed the person directing the work to read its envelope reopens this record.

## More Information

With ADR-D-0142 and ADR-D-0143, replaces ADR-D-0065 in full; the decision carried here is the same. Carried here from it: the conditions on which a ratified brief authorizes a plan or a goal envelope, what the audit grades for that purpose, that a side with no value document does not stand in the way, that a held item does not go ahead, and the condition for authorizing again after a held item. ADR-D-0065's example of a repository with a ratified brief and no engineering philosophy is not carried: the line on a side with no value document states it in general. Source of intent: `docs/coding-agent/briefs/completed/value-level-operation-brief.md`, "Who it is for and why", "Stops during a run", "Value audit" and "Lifecycle"; the brief "A quiet Orchestrator session under a brief" (`docs/coding-agent/briefs/completed/quiet-orchestrator-session-brief.md`), "What the plugin states" and "Directed during the run". Related records: ADR-D-0139 (who authorizes non-trivial work), ADR-D-0134 (the value audit in a plan-mode run), ADR-D-0082 (the value audit in a goal run), ADR-D-0062 (no question in the Orchestrator session under a brief), ADR-D-0067 (a determined remedy carried out without a stop under a brief), ADR-D-0084 (the envelope), ADR-D-0112 (how the ratification reaches the session), ADR-D-0036 (the product side's documents), ADR-D-0132 and ADR-D-0133 (extensions kept and shown), ADR-D-0147 (a small change built without a plan).
