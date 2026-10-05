---
status: accepted
adr_type: design
date: 2026-09-30
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1"]
informed: []
supersedes: ["superseded/ADR-D-0032-plan-approval-is-never-self-granted--superseded-by-ADR-D-0040.md"]
superseded_by: null
depends_on: ["ADR-D-0017-harness-text-holds-no-user-authority.md", "ADR-D-0020-loader-routed-sessions-assume-the-orchestrator-role.md", "ADR-D-0027-the-forbidden-set-is-a-criterion-ratified-before-the-loop.md", "ADR-D-0052-the-orchestrator-never-grades-its-own-run-and-its-reading-is-compared-only-after-the-grades-are-fixed.md"]
---

# ADR-D-0040: A non-trivial unit of work is authorized only by the explicit approval or waiver of the person directing the work given in the Orchestrator session, or by that person's ratified brief carried to the work through the value audit; never by the Orchestrator, the request, a verdict, a file's text or silence

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. The product owner is whoever is entitled to state the product's values and to answer product-level questions for that work; when the person directing the work owns the product, both are that person. Counsel is the session the person directing the work opens for value discussion, separate from any Orchestrator session. The Orchestrator session is a session that holds the Orchestrator role (ADR-D-0020) and plans, dispatches and reports the work.

An Orchestrator session prepares a non-trivial unit of work (in plan mode a plan, or a small change the person directing the work stated in a ratified brief; in goal mode an envelope) and then needs authorization to execute it. Before 2026-09-10 two readings of the Plan Gate let execution start with no human authority behind the plan: the Orchestrator waived approval on its own authority with a recorded reason, or the ordinary task request was taken as approval of whatever plan resulted from it. On 2026-09-08 a headless GPT-6 Astra session under the installed loader took both readings and implemented the work with no human having seen the plan. Under value-level operation a second pressure meets the first: the person directing the work ratifies a brief as the grounds for a piece of work and shapes direction at product level instead of auditing each plan. The fork is what may authorize a unit of work at all, in any mode.

## Decision

- Execution of a non-trivial unit of work is authorized only by one of two sources.
- The first source is the person directing the work: an explicit approval of the unit as presented, or an explicit waiver that names the approval step, given in the Orchestrator session; neither is carried by a relay.
- The second source is the ratification of the governing brief by the person directing the work, carried to the unit of work through the value audit (ADR-D-0052); the conditions under which it carries, including whether the audit judges the unit before it is built or, for a small change, at its close before anything of it is published or reported as done, are stated per mode by their own record, and where no record states them for a mode, the second source authorizes nothing in that mode.
- Without a ratified governing brief, a run audited against a philosophy alone included, only the first source authorizes: a philosophy states standing direction and ratifies no piece of work.
- The Orchestrator never approves a unit of work or waives its approval on its own authority; it may reclassify work as trivial under the Plan Gate's tripwires, and that classification is reviewable.
- A task request authorizes planning, not execution: it is not approval of the unit it produces.
- A verdict of the value audit is never presented as approval by the person directing the work; the authority in the second source is the ratification of the brief.
- A file's own text is never a source.
- When no source authorizes the unit and nobody can answer in the session, the Orchestrator presents it and ends the turn; elapsed time, silence, and the absence of a human channel confer no authorization and revoke none already given.

## Why

The person directing the work shapes direction at product level instead of auditing each plan, so what that person ratified in a brief, checked against the work by a judge the Orchestrator cannot frame, carries that person's authority to the work. The party that would benefit from skipping approval cannot grant it to itself, and a request describes a goal, not a plan, so neither is ever a source. A presented unit awaiting a human is the correct resting state for a session nobody is watching, so the Orchestrator ends the turn rather than proceed. The sources are the same in every mode because the question they answer, whose authority stands behind execution, does not depend on how the work is structured.

## Rejected Alternatives

- The person directing the work approves every unit of work, the only source ADR-D-0032 admitted: it keeps that person auditing each plan for drift; reopen if units started under the second source turn out, when that person reads them afterwards, to be ones that person would have stopped, and the miss does not trace to how items are graded, which reopens the grade definitions first (ADR-D-0052).
- The second source authorizes work on a philosophy alone, with no ratified brief: rejected outright; no ratification of that piece of work exists for the audit to carry.
- A ratified brief authorizes every unit made under it, with no audit: rejected outright; the Orchestrator would be the judge of whether its own plan fits the brief.
- Orchestrator self-waiver with a recorded reason and evidence: rejected outright; the record is written by the party the waiver benefits, so it constrains nothing.
- A task request counts as approval of the resulting unit: reopen only if plan review moves entirely to a runtime mechanism that shows the plan to the person directing the work before any execution step in every runtime the harness supports.
- A headless fallback that proceeds after a timeout: rejected outright; silence carries no authority.
- Sources stated for plan mode only, goal mode keeping its own: it leaves the same question answered twice and lets the answers drift; reopen if a mode needs a source neither of these two can be.

## Decision Boundary

Invariant: a non-trivial unit of work is authorized only by the explicit approval or waiver of the person directing the work in the Orchestrator session, or by that person's ratified governing brief carried to the work through the value audit under the conditions a per-mode record states; the Orchestrator, the request, a verdict, a file's text and silence are never sources; the Decision list states the rest.

Not covered: the trivial/non-trivial tripwires and who applies them; the conditions under which the second source authorizes a plan or a small change in plan mode (ADR-D-0041); the conditions under which it would authorize a goal-mode envelope, which a record for goal mode would state: this record decides goal mode's sources and not its conditions, and because ADR-D-0027's invariant admits only ratification by the person directing the work, that record would supersede ADR-D-0027, which this one leaves in force; what a goal-mode envelope consists of and that it is immutable during the loop (ADR-D-0027); the grade names and their definitions, which no record states and the audit's mandate owns (ADR-D-0052 leaves them uncovered); the audit's procedure and the dispatch wording (ADR-D-0052); merge authorization; how the plan records the source; the wording of the Plan Gate, the lifecycle reference and the runtime entry points; how the presented unit is surfaced in each runtime.

## Validation

- The Plan Gate, its lifecycle reference, the goal-mode reference and every runtime entry point that restates the approval condition name these two sources and no other, and none presents a verdict as approval by the person directing the work.
- A loader probe given an ordinary non-trivial request with no ratified brief presents a plan and ends the turn with only planning artifacts written; the same request with an explicit waiver from the person directing the work proceeds past the Plan Gate.

## Revisit When

- Units of work started under the second source turn out, when the person directing the work reads them afterwards, to be ones that person would have stopped. A miss that traces to how items are graded reopens the grade definitions first, as ADR-D-0052 says; any other reopens this record.
- A supported runtime gains a native plan-approval step that the harness can bind to, so that the request-as-approval alternative can be re-examined.
- The premise that a session under the installed loader will take a self-waiver or request-as-approval path when the text allows it was observed in a GPT-6 Astra session on 2026-09-08; the decision does not rest on that premise, so a model change reopens the probe, not the decision.
- A mode needs a source of authorization that is neither the person directing the work nor that person's ratified brief.

## More Information

Replaces ADR-D-0032 in full: everything it decided is carried, the second source is added, and the rule is stated for a unit of work in any mode rather than for a plan. ADR-D-0032 says "the user" for the person present in the Orchestrator session; this record says the person directing the work. The first source gains two things ADR-D-0032 did not state: approval and waiver are given in the Orchestrator session, and neither is carried by a relay. Source of intent for the second source: `docs/coding-agent/briefs/active/value-level-operation-brief.md`, "Who it is for and why", "Stops during a run", "Roles and sessions" and "Lifecycle". Probe method and evidence for the self-waiver and request-as-approval readings: `docs/coding-agent/experiments/frontier-guard-probes/` in git history at `2a5ebf9`. Related records: ADR-D-0017 (harness text holds no user authority), ADR-D-0020 (loader-routed sessions assume the Orchestrator role), ADR-D-0027 (goal-mode envelope), ADR-D-0038 (the word of the person directing the work), ADR-D-0052 (the value audit), ADR-D-0041 (when a ratified brief authorizes a plan or a small change), ADR-D-0042 (extensions at closeout).
