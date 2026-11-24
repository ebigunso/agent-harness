---
status: proposed
adr_type: design
date: 2026-11-24
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "Claude Fable 5.2"]
informed: []
supersedes: ["ADR-D-0052-the-orchestrator-never-grades-its-own-run-and-its-reading-is-compared-only-after-the-grades-are-fixed.md"]
superseded_by: null
---

# ADR-D-0135: The Orchestrator states its own reading of each item before the value audit grades it, and that reading is compared only after the grades are fixed

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. The Orchestrator session is a session that holds the Orchestrator role and plans, dispatches and reports the work. The value documents are a ratified brief, a product philosophy and an engineering philosophy, whichever of them exist for the work. A plan-mode run is a run that carries out a plan, as distinct from a run in goal mode, in which a loop works toward a stated goal condition. An item is a decision a plan or a result makes. The value audit is the independent judgement of how each item of a run stands against the value documents, made by an auditor that takes nothing the Orchestrator says about the work as evidence (ADR-D-0134); a grade is what it gives an item. The Orchestrator's reading of an item is its own statement of how that item stands against the same documents.

The person directing the work should not have to wonder whether the Orchestrator still cares what the value documents say. With grading taken from the Orchestrator altogether, the Orchestrator can stop reading the value documents and do whatever the grades say, so responsibility for the values moves to the audit alone. Keeping it with the Orchestrator needs the Orchestrator's own reading to be stated and checked, which means showing the auditor something the Orchestrator wrote, and the audit's worth rests on its grades owing nothing to the Orchestrator. The fork is whether the Orchestrator states a reading at all, who compares it with the grades and when, and what a difference between the two does to the run.

## Decision

- In a plan-mode run governed by value documents, the Orchestrator states its own reading of each item before each value audit, in terms the audit's grades can be compared with.
- The reading, with whatever else the workflow has the Orchestrator state for the audit to compare, is kept apart from the plan or result under review, and the auditor does not open it until its grades are fixed.
- The auditor then compares it with the grades and reports each difference.
- What the Orchestrator states for comparison is a claim under comparison: nothing in it supports, changes or reopens a grade.
- A difference between the Orchestrator's reading and a grade is corrected inside the run, by the Orchestrator returning to the value documents and redoing the item. A difference is by itself no reason to stop work.

## Why

An Orchestrator that only receives grades can leave the values to the audit, so it states its own reading first and is shown where it differed; opening that reading only after the grades are fixed keeps the audit's independence whole while adding this. A difference caught and corrected is the audit doing its work, and stopping on each would return the person directing the work to supervising the run, which the product philosophy's "What goes wrong, in order" names as "The person's attention, spent on what could have been settled."

## Rejected Alternatives

- The Orchestrator states no reading and only receives grades: it lost because responsibility for the values then sits with the audit alone, and the Orchestrator has no occasion to read the documents it is supposed to work from; reopen if readings are found written to match what the audit is expected to say, the comparison showing no difference run after run.
- The auditor given what the Orchestrator wrote before or while it grades: rejected outright; an account by the Orchestrator is the surface being defended, and the rejection holds for anything that could reach a grade.
- The comparison made by the Orchestrator itself, from the verdict: rejected outright; the party that diverged would judge its own divergence.
- A difference between reading and grade stops the affected work: it lost because a difference caught and corrected is the audit doing its work, and stopping on each returns the person directing the work to supervising the run; reopen if corrected differences are found recurring on the same decision without the documents changing.

## Decision Boundary

Not covered: goal mode; who grades a run, on what evidence, and what a grade holds (ADR-D-0134); the words by which a reading is written and the names of the grades it is compared with; what the Orchestrator states for comparison beyond the reading (ADR-D-0137 for its reading of a finding); that what is stated for comparison is a file, its name and place, and how the audit's mandate keeps it closed until grading is done; how the comparison is reported and where it is recorded; how an item is redone and when the redone work is graded; which role holds the audit (ADR-D-0050).

## Validation

The decision is broken where:

- an audit graded an item of which the Orchestrator had stated no reading beforehand;
- the auditor had the Orchestrator's reading, or anything else stated for comparison, before its grades were fixed, or a grade was supported, changed or reopened by it;
- the comparison of a reading with a grade was made by the Orchestrator;
- a difference between reading and grade was left as it was, or work stopped for such a difference alone.

## Revisit When

- Grades are found to have moved toward the Orchestrator's reading, what was written for comparison having been read before grading.
- On 2026-10-04 no audit had compared a reading on any runtime; readings that match every grade run after run, or a grade changed after the comparison, reopen this record.

## More Information

With ADR-D-0134 and ADR-D-0136, replaces ADR-D-0052 in full; the decision carried here is the same. Carried here from it: that the Orchestrator states a reading, that the auditor compares it only after its grades are fixed, and that a difference is corrected inside the run and is no stop. It is a record of its own because it would still bind if a party other than the value audit graded the run. The second rejected alternative is carried by ADR-D-0134 as well, for its own decision. The reading and its comparison are what the brief `docs/coding-agent/briefs/completed/design-led-long-runs-brief.md` states as a means under "Keeping to the philosophy without you"; this record fixes that means as a rule. Related: ADR-D-0050 (the role that holds the audit), ADR-D-0137 (the Orchestrator's reading of a finding, compared the same way), ADR-D-0082 (the value audit in a goal run).
