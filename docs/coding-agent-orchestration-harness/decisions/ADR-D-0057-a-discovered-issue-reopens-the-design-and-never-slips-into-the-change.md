---
status: proposed
adr_type: design
date: 2026-10-08
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1"]
informed: []
supersedes: []
superseded_by: null
depends_on: ["ADR-D-0040-non-trivial-work-is-authorized-only-by-the-person-directing-the-work-or-by-that-persons-ratified-brief.md", "ADR-D-0041-a-ratified-brief-authorizes-a-plan-only-through-a-closed-plan-review-and-a-value-audit-that-holds-nothing-above-the-run.md", "ADR-D-0053-a-design-level-finding-is-escalated-by-the-orchestrator-with-the-part-it-concerns-held.md", "ADR-D-0058-a-worker-acts-alone-only-within-the-acceptance-criteria.md"]
---

# ADR-D-0057: A discovered issue reopens the design and never slips into the current change: whatever is found during authorized work, by a dispatched agent or by the Orchestrator itself, the Orchestrator reads as within the task, a change to the design or a matter for later, and a plan revised or extended mid-run goes back through the gate that admitted it before any of the change is built

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. The Orchestrator session is a session that holds the Orchestrator role (ADR-D-0020) and plans, dispatches and reports the work.

During authorized work, issues are found by everyone taking part: a Worker whose check fails, a Reviewer or a Researcher reading the code, the Auditor grading the work, and the Orchestrator itself. ADR-D-0033 let the Orchestrator rule a discovery into the current change, sorted discoveries into no kinds, re-ran no review when the plan grew, and returned a discovery to the person directing the work in two cases only: a contract-shape change, or an irreversible or outward-facing action. It spoke of what a Worker surfaces and said nothing of what the Orchestrator or another dispatched agent finds. A change can then grow past what any gate admitted, on the Orchestrator's judgement alone and seen by nobody outside it. Putting every discovery aside for a plan of its own instead stalls work on things that belong to the task's design. The fork is what happens to a discovery made during authorized work, whoever makes it: where it goes, and what stands between it and being built.

## Decision

- This applies to anything found during authorized work, by anyone: a Worker, a Reviewer, a Researcher, the Auditor, any other dispatched agent, or the Orchestrator itself.
- The Orchestrator reads each discovered issue as one of three:
  - within the task as given: fixed in place, since it was always part of it; this is not a revision of the plan and asks nothing;
  - a change to the design: it revises or extends the current plan;
  - a matter for later: noted for its own task.
- An issue is never absorbed into the current change as if it had been part of the task, whoever found it.
- A plan revised or extended mid-run goes back through the gate that admitted it, for what changed, before any of the change is built.
  - Under a ratified brief: the plan review, and the value audit on the plan as it now stands, graded as a whole against the brief and the philosophies and not against the issue that prompted it.
  - Without a brief: the plan review, and the explicit approval of the revision by the person directing the work, or that person's explicit waiver naming the approval step (ADR-D-0040's first source).
  - The audit's scope test, which escalates expansion beyond the brief, applies to the revision as to a draft, and each piece the revision adds is asked what it is for and what it costs.
  - No extension is built on the Orchestrator's judgement alone.
- The reading into three is of the implementation design. A finding that bears on the design in ADR-D-0053's sense, because acting on it would change what someone experiences from the feature, is still escalated at once as a value question with the part it concerns held, as ADR-D-0053 states.
- Material discoveries are written into the plan record and surfaced at the next report or integration point.
- Within work already authorized, the Orchestrator seeks the confirmation of the person directing the work for a discovery when it is a contract-shape change or an irreversible or outward-facing action, and, without a brief, when it is a change to the design as above. The initial authorization of a plan and every other consent gate stay governed by their own records (ADR-D-0040, ADR-D-0041).

## Why

A discovered issue reopens the design rather than slipping in, and the risk is the same whoever found it: an issue the Orchestrator or a reviewing agent finds and folds into the change grows it as surely as one a Worker does. Revising or extending a plan does no harm as long as the whole is still kept in line with every criterion set for the work, and the only way to know that it is, is to put the plan as it now stands back through the gate that admitted it. A change to the design judged by the Orchestrator alone, or graded only against the issue that prompted it, is where scope creep and tunnel vision get in.

## Rejected Alternatives

- Every discovery outside the task as given is put aside for a plan of its own: it lost because it would stall work on things that belong to the task's design, when revising or extending the plan keeps the whole in line once the revision passes the gate; reopen if revisions are found to carry, past the audit, work the brief did not ask for.
- A discovery ruled into the current change by the Orchestrator alone, as ADR-D-0033 allowed: it lost because scope creeps and nobody outside the Orchestrator sees the growth; reopen if the re-admission is found to cost more than the growth it prevents.
- ADR-D-0033's two pause cases alone toward the person directing the work: rejected outright; without a brief, a change to the design would be built on the Orchestrator's judgement alone.
- Only one kind of agent's findings are read this way: rejected outright; an issue found by any other party, the Orchestrator included, would be folded into the change on the Orchestrator's judgement alone.

## Decision Boundary

Invariant: the Orchestrator reads each discovery made during authorized work, by whoever makes it, as within the task, a change to the design or a matter for later, and absorbs none into the current change; a plan revised or extended mid-run passes the plan review and, under a brief, the value audit on the plan as it now stands, or, without one, the explicit approval or waiver of the person directing the work, before any of the change is built; a finding that bears on the design in ADR-D-0053's sense is escalated as that record states; the Decision list states the rest.

Not covered: what a Worker may act on alone, and that everything else it finds waits for the Orchestrator's ruling (ADR-D-0058), and the report shape in which a finding is surfaced; what counts as material for the plan record; the wording of the replan procedure, which the skills own; the audit's position, procedure and dispatch wording (ADR-D-0052 and the audit's mandate); the conditions under which a plan is authorized at all (ADR-D-0040, ADR-D-0041); a small change built without a plan (ADR-D-0055); how a finding bears on the design in what someone experiences, and what follows (ADR-D-0053).

## Validation

- A dispatched agent's report surfaces a discovery rather than absorbing it into its work.
- A discovery by the Orchestrator or a Reviewer is logged and sorted into one of the three the same way as a Worker's.
- A plan revised or extended mid-run shows, before the changed item is built, a plan review of the revision closed with nothing open, and then a plan-draft audit of the plan as it stands under a brief, or the explicit approval or waiver of the person directing the work without one; the review is required under both.

## Revisit When

- A revision of a plan is found built before its re-admission.
- On 2026-10-08 no plan had been revised or extended mid-run under these terms; a change to the design found built on the Orchestrator's judgement alone, or an issue found absorbed into a change, reopens this record.

## More Information

ADR-D-0033's clauses on the Orchestrator's handling of a discovery are superseded by this record; its decision on what a Worker may act on alone is carried unchanged by ADR-D-0058, which replaces it, and ADR-D-0033 is retired with ADR-D-0058 as its replacement. Carried from ADR-D-0033 into this record: material discoveries written into the plan record, and the two pause cases toward the person directing the work. Changed: the record covers what anyone finds during authorized work, the Orchestrator and every dispatched agent; the Orchestrator no longer rules a discovery into the current change on its own; it reads each discovery as one of three, and a change to the design revises or extends the plan, which goes back through the gate that admitted it before any of it is built; without a brief, a change to the design is a third case returned to the person directing the work. ADR-D-0033 says "the user"; this record says the person directing the work. Source of intent: `docs/coding-agent/briefs/active/process-principles-in-the-plugin-brief.md`, "The process principles" (the second principle and its sub-statements) and "Limits". Related records: ADR-D-0058 (what a Worker may act on alone), ADR-D-0040 (the sources of authorization), ADR-D-0041 (when a ratified brief authorizes a plan, and changes after the verdict), ADR-D-0053 (findings that bear on the design), ADR-D-0052 (the value audit), ADR-D-0055 (a small change).
