---
status: accepted
adr_type: design
date: 2026-10-04
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1"]
informed: []
supersedes: ["superseded/ADR-D-0039-the-orchestrator-never-grades-its-own-run-against-the-value-documents--superseded-by-ADR-D-0052.md"]
superseded_by: null
depends_on: ["ADR-D-0036-a-product-philosophy-is-stated-only-by-the-product-owner-and-no-product-value-is-inferred-without-one.md"]
---

# ADR-D-0052: The Orchestrator never grades its own run against the value documents; a fresh dispatch that takes only those documents and the artifact as evidence does, a grade that requires a decision above the run holds the item until it is given, and what the Orchestrator writes for comparison is opened only after the grades are fixed

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. The product owner is whoever is entitled to state the product's values and to answer product-level questions for that work; when the person directing the work owns the product, both are that person. Counsel is the session the person directing the work opens for value discussion, separate from any Orchestrator session. The Orchestrator session is a session that holds the Orchestrator role (ADR-D-0020) and plans, dispatches and reports the work.

A plan-mode run governed by value documents (a ratified brief, a product philosophy, an engineering philosophy) goes ahead on some items without asking anyone and must wait on others for the person directing the work, or for the product owner through that person. Someone has to judge, for each item of a plan or a result, which it is. The Orchestrator is the party whose work waits when the answer is that a decision is needed, and any account it gives of that work chooses what a judge sees. The fork is who makes the judgement and on what evidence: the Orchestrator itself, a reviewer it briefs, or a party that reads the value documents and the artifact for itself. A second question follows from the first answer: when grading is taken from the Orchestrator altogether, the Orchestrator can stop reading the value documents and do whatever the grades say, so responsibility for the values moves to the audit alone. Keeping it with the Orchestrator needs the Orchestrator's own reading to be stated and checked, which means showing the auditor something the Orchestrator wrote.

## Decision

- In a plan-mode run governed by value documents, the judgement of how each item of a plan or a result stands against them is the value audit's and never the Orchestrator's.
- The audit is a dispatch with fresh context each time, run at positions the workflow fixes and the Orchestrator does not choose.
- Its evidence is the value documents that exist and the artifact under review, each read by the auditor itself from disk or from git.
- The dispatch carries locations and nothing the Orchestrator says about the work.
- Nothing the Orchestrator wrote counts as evidence: its plan and its changes are the thing under review, and no summary or account of the work is given to the auditor before its grades are fixed.
- Before each audit the Orchestrator writes its own reading of each item (covered by the value documents, extending them, or needing a decision above the run), together with what else the workflow has it state for comparison, in a file kept apart from the artifact. The auditor does not open that file until its grades are fixed. It then compares and reports each difference. The file is a claim under comparison: nothing in it supports, changes or reopens a grade.
- A difference between the Orchestrator's reading and a grade is corrected inside the run by the Orchestrator returning to the value documents and redoing the item; a difference is by itself no reason to stop work.
- Unratified discussion notes are not evidence.
- A standing approval is an approval for all future runs given by whoever holds the authority for that action in that repository, recorded in the repository rule files.
  - The entry records who gave it.
  - The person directing the work may grant one only within that person's own authority.
  - The Orchestrator writes the entry, and the entry counts only once the giver has accepted it and it records that acceptance, so a file the Orchestrator can write never becomes a source the Orchestrator decides.
  - A standing approval never discharges acceptance of a decision record, a change to a philosophy, plan approval, or acceptance of another standing approval; it may cover a merge only where that repository's rule files allow it and only when given by the product owner of that repository.
- The audit grades the items on a side, product or engineering, that has a value document; what the product side is graded against, and how, is ADR-D-0036's.
- An item on a side with no document is reported as not audited: it is not graded and this record does not hold it, except that the test for an irreversible or outward-facing action runs on every item on either side.
- An item whose grade requires a decision above the run does not go ahead until the person directing the work, or the product owner through that person, has given it.
- The Orchestrator does not overrule, change or work around a grade.
- An item that a verdict leaves ungraded for want of an input, and every item when the verdict is missing or malformed, is treated neither as graded nor as not audited: it does not go ahead on that verdict.

## Why

A verdict framed by the party it would hold up cannot be what lets that party go on. The freedom of the person directing the work from checking each step of a run rests on the grades, so they have to come from a reader of the value documents and of the work who took nothing the Orchestrator said about either as support. That person should also not have to wonder whether the Orchestrator still cares what the documents say: an Orchestrator that only receives grades can leave the values to the audit, so it states its own reading first and is shown where it differed. Opening that reading only after the grades are fixed keeps the first protection whole while adding the second.

## Rejected Alternatives

- The Orchestrator grades its own plan and results against the value documents: rejected outright; the conflicted party sits in the judge's seat, the reasoning ADR-D-0029 records for goal loops.
- An auditor given the value documents together with the Orchestrator's summary of the work before or while it grades: rejected outright; the summary is the surface being defended. ADR-D-0039 rejected an auditor given the summary at all; this record keeps that rejection for anything that could reach a grade and allows the Orchestrator's reading to be opened after the grades are fixed, for comparison only.
- The Orchestrator states no reading and only receives grades, the decision of ADR-D-0039: it lost because responsibility for the values then sits with the audit alone, and the Orchestrator has no occasion to read the documents it is supposed to work from; reopen if readings are found written to match what the audit is expected to say, the comparison showing no difference run after run.
- The comparison made by the Orchestrator itself, from the verdict: rejected outright; the party that diverged would judge its own divergence.
- A difference between reading and grade stops the affected work: it lost because a difference caught and corrected is the audit doing its work, and stopping on each returns the person directing the work to supervising the run; reopen if corrected differences are found recurring on the same decision without the documents changing.
- Folding the audit into the Reviewer's ordinary review, one dispatch instead of two: it lost because an ordinary review packet frames the work for its reader and so cannot keep the audit's evidence boundary; reopen if review packets come to consist of disk locations alone, with no text authored by the Orchestrator.
- No audit, and the Orchestrator asks the person directing the work whenever it is unsure: rejected outright; it returns that person to auditing the run, and for decisions that can be undone a stop on something the value documents already answer is itself a defect.
- A standing approval given by the person directing the work for any action, authority or not: rejected outright; an approval reaches no further than the authority of the one who gives it.

## Decision Boundary

Invariant: grading against the value documents is done by a fresh dispatch on evidence it reads itself, never by the Orchestrator and never on the Orchestrator's account of the work; what the Orchestrator writes for comparison is opened only after the grades are fixed and is never evidence; an item whose grade requires a decision above the run waits for it; the Decision list states the rest.

Not covered: goal mode; the grade names and their definitions, including which items require a decision above the run; what the product side is graded against where no product philosophy exists (ADR-D-0036); the scope test and the verdict's shape; which positions the audit runs at; the dispatch wording; which role holds the audit (ADR-D-0050); what the file for comparison contains beyond the reading, its name and place, and how the mandate keeps it closed until grading is done; what becomes of an item on a side with no value document, beyond its being reported as not audited; what else in a run waits when an item is held or a verdict is incomplete, which the run-side procedure decides; how a held item reaches the person directing the work or the product owner; how a standing approval is recorded and brought to its giver; who holds the authority for each action in a repository, which that repository's rules state; whether a verdict can authorize a plan, which this record does not grant and the record on plan approval governs (ADR-D-0040).

## Validation

- The dispatch text recorded for each audit carries the position, locations and a revision, and nothing the Orchestrator says about the work.
- A verdict supports each grade by quoting a value document or an accepted standing approval, never a statement of the Orchestrator's.
- The audit's mandate excludes the file for comparison from everything the auditor reads before its grades are fixed, and a verdict reports the comparison apart from the grades.
- No plan record shows work stopped for a difference between reading and grade alone.
- Each standing approval entry names who gave it and records that person's acceptance.
- No plan record shows an item whose grade requires a decision above the run going ahead without that decision recorded beside it.

## Revisit When

- Verdicts on real runs show stops on decisions that can be undone and that the value documents already answered, or decisions that should have reached the person directing the work or the product owner and did not. That reopens the grade definitions first; it reopens this record only when the miss traces to the evidence boundary, for example an artifact the auditor could not judge without an account of it.
- Dispatch texts recorded across runs show the Orchestrator's framing of the work. That reopens how the audit is packaged (ADR-D-0050), not the boundary.
- Grades are found to have moved toward the Orchestrator's reading, the file for comparison having been read before grading.
- On 2026-10-04 no audit had compared a reading on any runtime; readings that match every grade run after run, or a grade changed after the comparison, reopen this record.

## More Information

Replaces ADR-D-0039 in full: everything it decided is carried; what changes is that the Orchestrator states a reading the auditor compares after its grades are fixed, that a difference is corrected inside the run and is no stop, and that its outright rejection of an auditor given the Orchestrator's account now holds only for anything that could reach a grade, and that the question it left open, which role holds the audit, is now a pointer to ADR-D-0050. The one rejected alternative on folding the audit into ordinary review gains its reason. The reading and its comparison are what the brief `docs/coding-agent/briefs/active/design-led-long-runs-brief.md` states as a means under "Keeping to the philosophy without you"; this record fixes that means as a rule. Source of intent for the rest: `docs/coding-agent/briefs/active/value-level-operation-brief.md`, "Stops during a run" (who gives a standing approval; a merge approval in a repository the person directing the work does not own is the product owner's to give; merge looseness is a per-repository matter for that repository's rule files) and "Value audit". Related: ADR-D-0029 and ADR-D-0050 (the same separation for goal-loop continuation, and the role that holds both judgements), the record on plan approval (ADR-D-0040), ADR-D-0057, which replaced ADR-D-0033's clauses on this (the Orchestrator's own pause cases for a discovery within authorized work, which leaves every other consent gate to its own record; the hold stated here is such a gate), the record on Counsel (ADR-D-0034), the record on the philosophy documents (ADR-D-0036).
