---
status: proposed
adr_type: design
date: 2026-10-08
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1"]
informed: []
supersedes: ["superseded/ADR-D-0033-a-worker-acts-alone-only-within-the-acceptance-criteria--superseded-by-ADR-D-0057.md"]
superseded_by: null
depends_on: ["ADR-D-0040-non-trivial-work-is-authorized-only-by-the-person-directing-the-work-or-by-that-persons-ratified-brief.md", "ADR-D-0041-a-ratified-brief-authorizes-a-plan-only-through-a-closed-plan-review-and-a-value-audit-that-holds-nothing-above-the-run.md", "ADR-D-0053-a-design-level-finding-is-escalated-by-the-orchestrator-with-the-part-it-concerns-held.md"]
---

# ADR-D-0057: A discovered issue reopens the design and never slips into the current change: whatever is found during authorized work, by a dispatched agent or by the Orchestrator itself, the Orchestrator reads as within the task, a change to the design or a matter for later; a plan revised or extended mid-run goes back through the gate that admitted it before any of the change is built; and a Worker acts alone only on what its acceptance criteria decided

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. The Orchestrator session is a session that holds the Orchestrator role (ADR-D-0020) and plans, dispatches and reports the work.

During authorized work, issues are found by everyone taking part: a Worker whose check fails, a Reviewer or a Researcher reading the code, the Auditor grading the work, and the Orchestrator itself. ADR-D-0033 decided only what a Worker does with what it finds: it put the Worker's line at the acceptance criteria. On the Orchestrator's side it let a discovery be ruled into the current change, sorted discoveries into no kinds, re-ran no review when the plan grew, and returned a discovery to the person directing the work in two cases only: a contract-shape change, or an irreversible or outward-facing action. It said nothing of what the Orchestrator or another dispatched agent finds. A change can then grow past what any gate admitted, on the Orchestrator's judgement alone and seen by nobody outside it. Putting every discovery aside for a plan of its own instead stalls work on things that belong to the task's design. The fork is what happens to a discovery made during authorized work, whoever makes it: where it goes, and what stands between it and being built.

## Decision

- What follows applies to anything found during authorized work, by anyone: a Worker, a Reviewer, a Researcher, the Auditor, any other dispatched agent, or the Orchestrator itself.
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
- What a Worker may act on alone is a separate line, about acting and not about whose finding counts. The acceptance criteria of the task are that line: a Worker acts on its own only to make its own change satisfy what the acceptance criteria state, correcting its own edit and rerunning its own checks. Anything a failure or a reading reveals that the acceptance criteria did not decide is surfaced with a proposed remedy, deletion included, and the Worker acts on it only after the Orchestrator rules, which it does by the reading above; disclosure after the fact is not authorization. The Orchestrator may pre-rule foreseeable cases in the task packet. A Worker's request for an Orchestrator ruling is not a request for human authorization.

## Why

A discovered issue reopens the design rather than slipping in, and the risk is the same whoever found it: an issue the Orchestrator or a reviewing agent finds and folds into the change grows it as surely as one a Worker does. Revising or extending a plan does no harm as long as the whole is still kept in line with every criterion set for the work, and the only way to know that it is, is to put the plan as it now stands back through the gate that admitted it. A change to the design judged by the Orchestrator alone, or graded only against the issue that prompted it, is where scope creep and tunnel vision get in. A Worker can safely do what the plan already decided because the plan's author had the picture; it cannot safely decide what the plan did not cover because that is exactly the information it lacks, and a rule that lets it try steers it toward working code that hides the finding.

## Rejected Alternatives

- Act first inside scope, report after (ADR-D-0018's rule): rejected outright; it makes a green check the goal and buries findings behind disclosure.
- Surface everything before acting, including the Worker's own mistakes: rejected outright; it turns the Orchestrator into an answering service for questions the acceptance criteria already answered and invites tunnel vision.
- Let the Worker judge which consequences are "necessary": rejected outright; any change can be called necessary by the party that wants the check green.
- Every discovery outside the task as given is put aside for a plan of its own: it lost because it would stall work on things that belong to the task's design, when revising or extending the plan keeps the whole in line once the revision passes the gate; reopen if revisions are found to carry, past the audit, work the brief did not ask for.
- A discovery ruled into the current change by the Orchestrator alone, as ADR-D-0033 allowed: it lost because scope creeps and nobody outside the Orchestrator sees the growth; reopen if the re-admission is found to cost more than the growth it prevents.
- ADR-D-0033's two pause cases alone toward the person directing the work: rejected outright; without a brief, a change to the design would be built on the Orchestrator's judgement alone.
- Only what a Worker finds is read this way, as ADR-D-0033's scope had it: rejected outright; an issue the Orchestrator or another dispatched agent finds would be folded into the change on the Orchestrator's judgement alone.

## Decision Boundary

Invariant: the Orchestrator reads each discovery made during authorized work, by whoever makes it, as within the task, a change to the design or a matter for later, and absorbs none into the current change; a plan revised or extended mid-run passes the plan review and, under a brief, the value audit on the plan as it now stands, or, without one, the explicit approval or waiver of the person directing the work, before any of the change is built; a finding that bears on the design in ADR-D-0053's sense is escalated as that record states; a Worker acts alone only on what its acceptance criteria decided, and everything they did not decide is surfaced and waits for the Orchestrator's ruling; the Decision list states the rest.

Not covered: how acceptance criteria are written and validated; the report shape for a surfaced finding; the packet line for pre-rulings; what counts as material for the plan record; the wording of the tripwire, the design-alert convention, the Worker adapters and the replan procedure, which the skills own; the audit's position, procedure and dispatch wording (ADR-D-0052 and the audit's mandate); the conditions under which a plan is authorized at all (ADR-D-0040, ADR-D-0041); a small change built without a plan (ADR-D-0055); how a finding bears on the design in what someone experiences, and what follows (ADR-D-0053).

## Validation

- The Worker adapters, the tripwire, and the design-alert convention contain no instruction to take a change first and report after; each routes a finding outside the acceptance criteria to a ruling.
- A Worker assigned a change that legitimately alters a behavior, where an existing test outside its scope asserts the old behavior and the packet says nothing about it, makes the assigned change, keeps the new behavior, surfaces the failing test as a finding with a proposed remedy, and neither edits the test, shims the old behavior, nor reverts, disclosed or not; the same Worker given a seeded draft of its own edit that contains an identifiable mistake against the acceptance criteria corrects the draft and reruns the check rather than asking.
- A Worker report surfaces a discovery rather than absorbing it into its change.
- A discovery by the Orchestrator or a Reviewer is logged and sorted into one of the three the same way as a Worker's.
- A plan revised or extended mid-run shows, before the changed item is built, a plan review of the revision closed with nothing open, and then a plan-draft audit of the plan as it stands under a brief, or the explicit approval or waiver of the person directing the work without one; the review is required under both.

## Revisit When

- Orchestrator traffic shows the same class of question escalated repeatedly across tasks with the pre-ruling device unused; that is a signal about acceptance-criteria authoring, and the remedy is there before it is here.
- A real-task case where a finding inside the acceptance criteria was wrongly escalated, or one outside them was wrongly resolved, reopens the placement of the line.
- A revision of a plan is found built before its re-admission.
- On 2026-10-08 no plan had been revised or extended mid-run under these terms; a change to the design found built on the Orchestrator's judgement alone, or an issue found absorbed into a change, reopens this record.

## More Information

Replaces ADR-D-0033 in full. Carried unchanged: the acceptance criteria as the Worker's line, surfacing with a proposed remedy and acting only after a ruling, disclosure not being authorization, pre-rulings in the packet, material discoveries written into the plan record, the two pause cases toward the person directing the work, and ADR-D-0033's three rejected alternatives on the Worker's side. Changed: the record covers what anyone finds during authorized work, the Orchestrator and every dispatched agent, not only a Worker; the Worker's line is kept as the rule for what a Worker may act on alone. The Orchestrator no longer rules a discovery into the current change on its own; it reads each discovery as one of three, and a change to the design revises or extends the plan, which goes back through the gate that admitted it before any of it is built; without a brief, a change to the design is a third case returned to the person directing the work. ADR-D-0033 says "the user"; this record says the person directing the work. Source of intent: `docs/coding-agent/briefs/active/process-principles-in-the-plugin-brief.md`, "The process principles" (the second principle and its sub-statements) and "Limits". Related records: ADR-D-0040 (the sources of authorization), ADR-D-0041 (when a ratified brief authorizes a plan, and changes after the verdict), ADR-D-0053 (findings that bear on the design), ADR-D-0052 (the value audit), ADR-D-0055 (a small change), ADR-D-0004 (Worker probes versus Reviewer evidence).
