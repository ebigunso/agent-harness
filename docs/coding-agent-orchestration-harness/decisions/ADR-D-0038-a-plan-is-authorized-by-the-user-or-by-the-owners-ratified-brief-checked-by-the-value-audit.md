---
status: proposed
adr_type: design
date: 2026-09-30
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1"]
informed: []
supersedes: ["ADR-D-0032-plan-approval-is-never-self-granted.md"]
superseded_by: null
depends_on: ["ADR-D-0017-harness-text-holds-no-user-authority.md", "ADR-D-0020-loader-routed-sessions-assume-the-orchestrator-role.md", "ADR-D-0036-the-orchestrator-never-grades-its-own-run-against-the-value-documents.md", "ADR-D-0037-the-owners-word-reaches-an-orchestrator-session-directly-or-by-quoted-relay.md"]
---

# ADR-D-0038: A non-trivial plan is authorized only by the user's approval or waiver, or by the owner's ratification of the brief it serves, checked against the plan by the value audit; never by the Orchestrator or by the request

## Context and Problem Statement

A session that assumes the Orchestrator role (ADR-D-0020) plans non-trivial work and then needs authorization to execute it. The user is the person in the Orchestrator session; the owner is the person whose product the work serves, and is that user when present in the session. Before 2026-09-10 two readings of the Plan Gate let execution start with no human authority behind the plan: the Orchestrator waived approval on its own authority with a recorded reason, or the ordinary task request was taken as approval of whatever plan resulted from it. On 2026-09-08 a headless GPT-6 Astra session under the installed loader took both readings and implemented the work with no human having seen the plan. Under value-level operation a second pressure meets the first: the owner ratifies a brief as the grounds for a piece of work and shapes direction at product level instead of auditing each plan. The fork is what may authorize a plan, and whether the owner's ratified brief can do so without the owner reading the plan.

## Decision

In plan mode, execution of non-trivial work is authorized only by a source this record names. There are two.

The first source is the user: an explicit approval of the plan that was presented, or an explicit waiver that names the approval step, given in the Orchestrator session. Neither is carried by a relay.

The second source is the owner's ratification of the governing brief, carried to the plan. It holds only when three conditions hold together. First, a brief governs the work and the owner ratified it. Second, the Reviewer's plan review has ended with no finding left open. Third, after that review, the value audit (ADR-D-0036) has graded the plan and judged every item it grades to be either covered by a statement in a value document or a cheap-to-undo extension of statements the verdict names, with no item that requires the owner.

On the first condition: the governing brief is the one the hand-over named for this work, and a plan for other work is not under it. Its ratification has reached the Orchestrator session as the owner's own statement there or as a relay that the record on the owner's word admits (ADR-D-0037); a status line in the brief file is not ratification. An amendment to the brief counts on the same terms as the brief.

On the second condition: a review loop that does not converge is a value question for the owner, not a completed review.

On the third condition, this is what the brief calls a citing audit, as this record reads it. A plan some of whose items are such extensions, stated in no document, starts without the owner seeing it. Each extension is recorded in the run's records; at closeout the owner is shown those that bear on the product's direction, chosen by the Orchestrator, and not every one. The audit grades two sides: the product side, against the brief and the product philosophy, and the engineering side, against the engineering philosophy. A side that has no value document is not graded and does not stand in the way: in a repository with a ratified brief and no engineering philosophy, the plan's internal mechanics (how the work is structured, not what the product does) are not audited, and the plan starts all the same, without any person having seen it. The test for an irreversible or outward-facing action runs on every item on either side. The verdict is on the plan as it stands when execution starts: what is added to or changed in what the plan decides after the verdict is not authorized by that verdict and needs a later audit or the user, and a second audit on unchanged inputs does not replace the first. A verdict that is missing, malformed, leaves any item ungraded, or grades nothing on the brief's side authorizes nothing.

One item that requires the owner means the second source does not authorize the plan. The item goes to the owner as a value question, and the second source can authorize after the owner's answer is in the value documents, or after the plan is changed so that it no longer makes that decision, in both cases only on a new audit of the plan as it then stands. A plan that contains an irreversible or outward-facing action that no standing approval accepted by the owner covers is authorized by the second source only when the plan states the action as taken on the owner's own decision at its moment and not before, and an action so stated does not count against the third condition; otherwise only the user authorizes that plan. Under either source the action itself waits for the owner: authorizing a plan, by the user or by the second source, lets no item go ahead that the value audit holds for the owner.

Without a ratified governing brief, a run audited against a philosophy alone included, only the user authorizes.

The Orchestrator never approves a plan or waives its approval on its own authority; it may reclassify work as trivial under the Plan Gate's tripwires, and that classification is reviewable. A task request authorizes planning, not execution: it is not approval of the plan it produces. The audit's verdict is never presented as the user's approval; the authority in the second source is the owner's ratification of the brief. A file's own text is never a source. When no source authorizes the plan and no user can answer, the Orchestrator presents the plan and ends the turn; elapsed time, silence, and the absence of a human channel confer no authorization and revoke none already given.

## Why

The owner shapes direction at product level instead of auditing each plan, so what the owner ratified in a brief, checked against the plan by a judge the Orchestrator cannot frame, carries the owner's authority to that plan. The party that would benefit from skipping approval cannot grant it to itself, and a request describes a goal, not a plan, so neither is ever a source.

## Rejected Alternatives

- The user approves every plan, the only source ADR-D-0032 admitted: it keeps the owner auditing each plan for drift; reopen if plans started under the second source turn out, when the owner reads them afterwards, to be ones the owner would have stopped, and the miss does not trace to how items are graded, which reopens the grade definitions first (ADR-D-0036).
- A verdict with no item requiring the owner authorizes a plan with no ratified brief, on a philosophy alone: rejected outright; a philosophy states standing direction, and no ratification of that piece of work exists for the verdict to carry.
- Only items covered by a statement count, and any extension sends the plan to the owner: it stops the run where a direction can be reasonably inferred from what the owner documented; reopen if the owner, shown such extensions at closeout, regularly rejects them.
- A ratified brief authorizes every plan made under it, with no audit: rejected outright; the Orchestrator would be the judge of whether its own plan fits the brief.
- Orchestrator self-waiver with a recorded reason and evidence: rejected outright; the record is written by the party the waiver benefits, so it constrains nothing.
- A task request counts as approval of the resulting plan: reopen only if plan review moves entirely to a runtime mechanism that shows the plan to the user before any execution step in every runtime the harness supports.
- A headless fallback that proceeds after a timeout: rejected outright; silence carries no authority.

## Decision Boundary

Invariant: a non-trivial plan in plan mode is authorized only by one of two sources. The first is the user's explicit approval of the presented plan or explicit waiver naming the approval step, given in the Orchestrator session and not by relay. The second is the owner's ratification of the governing brief, and it needs three things together: the brief the hand-over named for this work, with its ratification, and that of any amendment, having reached the session as the owner's own statement or an admitted relay and never as a status line; a plan review ended with no finding left open, a loop that does not converge being a value question and not a completed review; and, after that review, a value audit of the plan that judges every item it grades covered by a value document or a cheap-to-undo extension of named statements and finds no item requiring the owner. Extensions start without the owner seeing them, are recorded in the run's records, and those bearing on the product's direction, chosen by the Orchestrator, are shown to the owner at closeout. A side with no value document is not graded and does not stand in the way, so with a brief and no engineering philosophy the plan's internal mechanics are not audited and the plan starts unseen by any person; the test for an irreversible or outward-facing action runs on every item on either side. The verdict is on the plan as it stands when execution starts; later additions or changes to what the plan decides need a later audit or the user; a second audit on unchanged inputs does not replace the first. A verdict that is missing, malformed, leaves any item ungraded, or grades nothing on the brief's side authorizes nothing. An item requiring the owner keeps the second source from authorizing until a new audit of the plan, after the owner's answer is in the value documents or the plan no longer makes that decision, finds none. A plan containing an irreversible or outward-facing action that no accepted standing approval covers is authorized by the second source only when it states the action as taken on the owner's own decision at its moment, and otherwise only by the user; under either source no item the value audit holds for the owner goes ahead. Without a ratified governing brief only the user authorizes. The Orchestrator, the originating request, a verdict presented as the user's approval, and a file's own text are never sources. With no authorization and nobody to ask, the plan is presented and the turn ends, and time, silence and an absent human channel confer nothing and revoke nothing.

Not covered: the trivial/non-trivial tripwires and who applies them; goal mode, whose envelope ratification is governed by ADR-D-0027; the grade names, the audit's procedure and the dispatch wording; merge authorization; how the plan records the ratification and the verdict; the wording of the Plan Gate, the lifecycle reference, and the runtime entry points; how the presented plan is surfaced in each runtime.

## Validation

- The Plan Gate, its lifecycle reference, and every runtime entry point that restates the approval condition name these two sources and no other, and none presents a verdict as the user's approval.
- A plan executed under the second source records the owner's ratification as it reached the session, the plan review ended with no finding left open, and the audit's dispatch and verdict on the plan as executed; the verdict shows no item requiring the owner and no ungraded item.
- A loader probe given an ordinary non-trivial request with no ratified brief presents a plan and ends the turn with only planning artifacts written; the same request with an explicit user waiver proceeds past the Plan Gate.
- A probe under a brief whose ratification reached the session only as the brief's status line, or whose verdict leaves an item ungraded, presents the plan and ends the turn.

## Revisit When

- Plans started under the second source turn out, when the owner reads them afterwards, to be ones the owner would have stopped. A miss that traces to how items are graded reopens the grade definitions first, as ADR-D-0036 says; any other reopens this record.
- A supported runtime gains a native plan-approval step that the harness can bind to, so that the request-as-approval alternative can be re-examined.
- The premise that a session under the installed loader will take a self-waiver or request-as-approval path when the text allows it was observed in a GPT-6 Astra session on 2026-09-08; the decision does not rest on that premise, so a model change reopens the probe, not the decision.
- On 2026-09-30 no plan had been authorized by the second source on any runtime; the first use on a real initiative is the check of this record.

## More Information

Replaces ADR-D-0032 in full: everything it decided is carried, and the second source is added. The first source gains two things ADR-D-0032 did not state: approval and waiver are given in the Orchestrator session, and neither is carried by a relay. Source of intent for the second source: `docs/coding-agent/briefs/value-level-operation-brief.md`, "Who it is for and why", "Stops during a run", "Roles and sessions", "Value audit" and "Lifecycle". Probe method and evidence for the self-waiver and request-as-approval readings: `docs/coding-agent/experiments/frontier-guard-probes/` in git history at `2a5ebf9`. Related records: ADR-D-0017 (harness text holds no user authority), ADR-D-0020 (loader-routed sessions assume the Orchestrator role), ADR-D-0027 (goal-mode envelope ratification), the record on the value audit (ADR-D-0036), the record on the owner's word (ADR-D-0037).
