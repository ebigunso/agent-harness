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

# ADR-D-0134: The Orchestrator never grades its own run against the value documents; a party that reads them and the work for itself does, and its grade binds

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. The product owner is whoever is entitled to state the product's values and to answer product-level questions for that work; when the person directing the work owns the product, both are that person. The Orchestrator session is a session that holds the Orchestrator role and plans, dispatches and reports the work. The value documents are a ratified brief, a product philosophy and an engineering philosophy, whichever of them exist for the work. A plan-mode run is any run that is not a goal-mode run, a goal-mode run being one in which a loop works toward a stated goal condition. An item is a decision a plan or a result makes. A side of the work is its product side, what the product does, or its engineering side, how the project is built; each side has its own value documents. The value audit is the judgement this record states, and the auditor is the party that makes it. Discussion notes are the notes kept of a value discussion, which nobody has ratified.

The person directing the work is to be free of checking each step of a run. A plan-mode run governed by value documents therefore goes ahead on some items without asking anyone and must wait on others for that person, or for the product owner through that person, and someone has to judge, for each item of a plan or a result, which it is. The Orchestrator is the party whose work waits when the answer is that a decision is needed, and any account it gives of that work chooses what a judge sees, so neither its own judgement nor a judgement made on its account serves. The fork is who makes the judgement and on what evidence: the Orchestrator itself, a reviewer it briefs, or a party that reads the value documents and the work for itself.

## Decision

- In a plan-mode run governed by value documents, the judgement of how each item of a plan or a result stands against them is the value audit's and never the Orchestrator's.
- The audit is made with fresh context each time, at points of the run that the workflow fixes and the Orchestrator does not choose.
- Its evidence is the value documents that exist and the plan or result under review, each read by the auditor itself from where it is kept.
- Nothing the Orchestrator says or wrote counts as evidence. Its plan and its changes are the thing under review, and no summary or account of the work reaches the auditor before its grades are fixed.
- Unratified discussion notes are not evidence.
- The audit grades the items on a side of the work that has a value document.
- An item on a side with no value document is not graded and nothing here holds it; the audit reports that it was not audited. The test for an irreversible or outward-facing action runs on every item all the same, on either side.
- An item whose grade requires a decision above the run does not go ahead until the person directing the work, or the product owner through that person, has given it.
- The Orchestrator does not overrule, change or work around a grade.
- An item that a verdict leaves without a grade for want of an input, and every item when the verdict is missing or malformed, counts neither as graded nor as not audited: it does not go ahead on that verdict.

## Why

A verdict framed by the party it would hold up cannot be what lets that party go on. The freedom of the person directing the work from checking each step of a run rests on the grades, so they have to come from a reader of the value documents and of the work who took nothing the Orchestrator said about either as support. This is what the product philosophy's "What it must not be" asks: "Not its own judge. A builder's confidence in its own work is not evidence, and a longer list of rules does not make it so."

## Rejected Alternatives

- The Orchestrator grades its own plan and results against the value documents: rejected outright; the conflicted party sits in the judge's seat, the reasoning ADR-D-0080 records for goal loops.
- An auditor given the value documents together with the Orchestrator's summary of the work before or while it grades: rejected outright; the summary is the surface being defended. The rejection holds for anything that could reach a grade; what the Orchestrator writes for comparison is opened after the grades are fixed, for comparison only (ADR-D-0135).
- Folding the audit into the Reviewer's ordinary review, one dispatch instead of two: it lost because an ordinary review packet frames the work for its reader and so cannot keep the audit's evidence boundary; reopen if review packets come to consist of disk locations alone, with no text authored by the Orchestrator.
- No audit, and the Orchestrator asks the person directing the work whenever it is unsure: rejected outright; it returns that person to auditing the run, and for decisions that can be undone a stop on something the value documents already answer is itself a defect.

## Decision Boundary

Not covered: goal mode (ADR-D-0082 states the audit for a goal run); the Orchestrator's own reading of each item and its comparison with the grades (ADR-D-0135); standing approvals (ADR-D-0136); the grade names and their definitions, including which items require a decision above the run; what the product side is graded against, and how, where no product philosophy exists included (ADR-D-0036, which the proposed ADR-D-0120 takes over); the scope test and the verdict's shape; at which points of the run the audit is made; which role holds the audit, and that a dispatch to it carries locations only, with the dispatch wording (ADR-D-0050); what becomes of an item on a side with no value document, beyond its being reported as not audited; what else in a run waits when an item is held or a verdict is incomplete, which the run-side procedure decides; how a held item reaches the person directing the work or the product owner; whether a verdict can authorize a plan, which this record does not grant and the record on plan approval governs (ADR-D-0064).

## Validation

The decision is broken where:

- the Orchestrator judged how an item of its own run stands against the value documents, or overruled, changed or worked around a grade;
- a summary or account of the work by the Orchestrator reached the auditor before its grades were fixed, or a grade was supported by anything other than a value document or an accepted standing approval, a statement of the Orchestrator's and unratified discussion notes included;
- an item whose grade requires a decision above the run went ahead without that decision;
- an item went ahead on a verdict that left it without a grade, or on a verdict that was missing or malformed.

## Revisit When

- Verdicts on real runs show stops on decisions that can be undone and that the value documents already answered, or decisions that should have reached the person directing the work or the product owner and did not. That reopens the grade definitions first; it reopens this record only when the miss traces to the evidence boundary, for example a plan or result the auditor could not judge without an account of it.
- Dispatch texts recorded across runs show the Orchestrator's framing of the work. That reopens how the audit is packaged (ADR-D-0050), not the boundary.

## More Information

With ADR-D-0135 and ADR-D-0136, replaces ADR-D-0052 in full; the decision carried here is the same. Carried here from it: who judges how a run stands against the value documents, on what evidence, and what a grade holds. ADR-D-0052's line that the dispatch carries locations and nothing the Orchestrator says about the work is held by ADR-D-0050 ("A dispatch to the Auditor carries locations only"); the boundary that line serves is stated here. Its pointer for what the product side is graded against is held by ADR-D-0036 ("The value audit grades the product side against what the product owner ratified in a brief or a philosophy, whoever worded it"). The rejected alternative of an auditor given the Orchestrator's summary of the work before or while it grades is carried by ADR-D-0135 as well, for its own decision. Source of intent: `docs/coding-agent/briefs/completed/value-level-operation-brief.md`, "Value audit". Related: ADR-D-0080 and ADR-D-0050 (the same separation for goal-loop continuation, and the role that holds both judgements), ADR-D-0082 (the value audit in a goal run), ADR-D-0064 (plan approval), ADR-D-0065 (what a verdict authorizes), ADR-D-0057 (the Orchestrator's own pause cases for a discovery within authorized work, which leaves every other consent gate to its own record; the hold stated here is such a gate), ADR-D-0036 (the philosophy documents).
