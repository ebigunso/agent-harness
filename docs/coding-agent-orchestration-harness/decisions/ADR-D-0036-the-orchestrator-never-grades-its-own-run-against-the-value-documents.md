---
status: proposed
adr_type: design
date: 2026-09-30
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1"]
informed: []
supersedes: []
superseded_by: null
---

# ADR-D-0036: The Orchestrator never grades its own run against the value documents; a fresh dispatch that takes only those documents and the artifact as evidence does, and a grade that requires the owner holds the item until the owner decides

## Context and Problem Statement

A plan-mode run governed by value documents (a ratified brief, a product philosophy, an engineering philosophy) goes ahead on some items without asking the owner, the person whose product the work serves, and must wait for the owner on others. Someone has to judge, for each item of a plan or a result, which it is. The Orchestrator is the party whose work waits when the answer is that the owner is needed, and any account it gives of that work chooses what a judge sees. The fork is who makes the judgement and on what evidence: the Orchestrator itself, a reviewer it briefs, or a party that reads the value documents and the artifact for itself.

## Decision

In a plan-mode run governed by value documents, the judgement of how each item of a plan or a result stands against them is the value audit's and never the Orchestrator's. The audit is a dispatch with fresh context each time, run at positions the workflow fixes and the Orchestrator does not choose. Its evidence is the value documents that exist and the artifact under review, each read by the auditor itself from disk or from git, and the dispatch carries locations and nothing the Orchestrator says about the work. Nothing the Orchestrator wrote counts as evidence: its plan and its changes are the thing under review, and its summary or account of the work is not given to the auditor. Unratified discussion notes are not evidence either. A standing approval is what the owner approved for all future runs, recorded in the repository rule files. The Orchestrator writes the entry, and the entry counts only once the owner has accepted it and it records that acceptance, so a file the Orchestrator can write never becomes a source the Orchestrator decides; a standing approval never discharges a merge, acceptance of a decision record, a change to a philosophy, plan approval, or acceptance of another standing approval. The audit grades the items on a side, product or engineering, that has a value document. An item on a side with no document is reported as not audited; it is not graded and this record does not hold it, except that the test for an irreversible or outward-facing action runs on every item on either side. An item whose grade requires the owner does not go ahead until the owner has decided it. The Orchestrator does not overrule, change or work around a grade. An item that a verdict leaves ungraded for want of an input, and every item when the verdict is missing or malformed, is treated neither as graded nor as not audited: it does not go ahead on that verdict.

## Why

A verdict framed by the party it would hold up cannot be what lets that party go on. The owner's freedom from checking each step of a run rests on the grades, so they have to come from a reader of the value documents and of the work who took nothing the Orchestrator said about either as support.

## Rejected Alternatives

- The Orchestrator grades its own plan and results against the value documents: rejected outright; the conflicted party sits in the judge's seat, the reasoning ADR-D-0029 records for goal loops.
- An auditor given the value documents together with the Orchestrator's summary of the work: rejected outright; the summary is the surface being defended.
- Folding the audit into the Reviewer's ordinary review, one dispatch instead of two: reopen if review packets come to consist of disk locations alone, with no text authored by the Orchestrator.
- No audit, and the Orchestrator asks the owner whenever it is unsure: rejected outright; it returns the owner to auditing the run, and for decisions that can be undone a stop on something the value documents already answer is itself a defect.

## Decision Boundary

Invariant: in a plan-mode run governed by value documents, grading is done by a separate dispatch with fresh context, at positions the workflow fixes and the Orchestrator does not choose; its evidence is the value documents and the artifact, read by itself from disk or git; nothing the Orchestrator wrote counts as evidence, and its account of the work is not given to the auditor; a standing approval counts only after the owner's own acceptance; an item whose grade requires the owner waits for the owner; the Orchestrator cannot change a grade; an item left ungraded for want of an input, or any item under a missing or malformed verdict, does not go ahead on that verdict.

Not covered: goal mode; the grade names and their definitions, including which items require the owner; the scope test and the verdict's shape; which positions the audit runs at; the dispatch wording; whether the audit is a dispatch profile of another role or a role of its own; what becomes of an item on a side with no value document, beyond its being reported as not audited; what else in a run waits when an item is held or a verdict is incomplete, which the run-side procedure decides; how an item that requires the owner reaches the owner; how a standing approval is recorded and brought to the owner; whether a verdict can authorize a plan, which this record does not grant and the record on plan approval (ADR-D-0032) governs.

## Validation

- The dispatch text recorded for each audit carries the position, locations and a revision, and nothing the Orchestrator says about the work.
- A verdict supports each grade by quoting a value document or an accepted standing approval, never a statement of the Orchestrator's.
- No plan record shows an item whose grade requires the owner going ahead without the owner's decision recorded beside it.

## Revisit When

- Verdicts on real runs show stops on decisions that can be undone and that the value documents already answered, or decisions that should have reached the owner and did not. That reopens the grade definitions first; it reopens this record only when the miss traces to the evidence boundary, for example an artifact the auditor could not judge without an account of it.
- Dispatch texts recorded across runs show the Orchestrator's framing of the work. That reopens how the audit is packaged, as ADR-D-0030 provides for the goal assessor, not the boundary.

## More Information

Source of intent: `docs/coding-agent/briefs/value-level-operation-brief.md`, "Stops during a run" and "Value audit". Related: ADR-D-0029 and ADR-D-0030 (the same separation for goal-loop continuation), the record on plan approval (ADR-D-0032), ADR-D-0033 (the Orchestrator's own pause cases for a discovery within authorized work, which leaves every other consent gate to its own record; the hold stated here is such a gate).
