---
status: proposed
adr_type: design
date: 2026-10-29
deciders: ["ebigunso"]
consulted: ["Claude Opus 5.5"]
informed: []
supersedes: ["ADR-D-0040-non-trivial-work-is-authorized-only-by-the-person-directing-the-work-or-by-that-persons-ratified-brief.md"]
superseded_by: null
depends_on: ["ADR-D-0017-harness-text-holds-no-user-authority.md", "ADR-D-0020-loader-routed-sessions-assume-the-orchestrator-role.md", "ADR-D-0027-the-forbidden-set-is-a-criterion-ratified-before-the-loop.md", "ADR-D-0052-the-orchestrator-never-grades-its-own-run-and-its-reading-is-compared-only-after-the-grades-are-fixed.md", "ADR-D-0062-under-a-ratified-brief-the-orchestrator-session-asks-the-person-directing-the-work-nothing-and-presents-no-plan.md"]
---

# ADR-D-0064: A non-trivial unit of work is authorized only by the explicit approval or waiver of the person directing the work, or by that person's ratified brief carried to the work through the value audit; under a brief no plan is presented for approval and a goal envelope is agreed by that person's answer relayed through Counsel; never by the Orchestrator, the request, a verdict, a file's text or silence

Proposed on 2026-10-29 to replace ADR-D-0040; awaiting acceptance by the person directing the work, by name.

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. The product owner is whoever is entitled to state the product's values and to answer product-level questions for that work; when the person directing the work owns the product, both are that person. Counsel is the session the person directing the work opens for value discussion, separate from any Orchestrator session. The Orchestrator session is a session that holds the Orchestrator role (ADR-D-0020) and plans, dispatches and reports the work.

An Orchestrator session prepares a non-trivial unit of work (in plan mode a plan, or a small change the person directing the work stated in a ratified brief; in goal mode an envelope) and then needs authorization to execute it. Before 2026-09-10 two readings of the Plan Gate let execution start with no human authority behind the plan: the Orchestrator waived approval on its own authority with a recorded reason, or the ordinary task request was taken as approval of whatever plan resulted from it. On 2026-09-08 a headless GPT-6 Astra session under the installed loader took both readings and implemented the work with no human having seen the plan. Under value-level operation a second pressure meets the first: the person directing the work ratifies a brief as the grounds for a piece of work and shapes direction at product level instead of auditing each plan, and while a run under that brief is in progress, that person is reached only through Counsel (ADR-D-0062). The fork is what may authorize a unit of work at all, in any mode, and which source applies while a brief governs.

## Decision

- Execution of a non-trivial unit of work is authorized only by one of two sources.
- The first source is the person directing the work: an explicit approval of the unit as presented, or an explicit waiver that names the approval step, given in the Orchestrator session; neither is carried by a relay. Under a ratified brief it authorizes no plan, and its one use is the agreement to a goal-mode envelope, which reaches that person through Counsel and is given by that person's answer relayed as ADR-D-0038 admits.
- The second source is the ratification of the governing brief by the person directing the work, carried to the unit of work through the value audit (ADR-D-0052); the conditions under which it carries, including whether the audit judges the unit before it is built or, for a small change, at its close before anything of it is published or reported as done, are stated per mode by their own record, and where no record states them for a mode, the second source authorizes nothing in that mode. Under a brief it is the only source for a plan or a small change.
- Without a ratified governing brief, a run audited against a philosophy alone included, only the first source authorizes: a philosophy states standing direction and ratifies no piece of work.
- The Orchestrator never approves a unit of work or waives its approval on its own authority; it may reclassify work as trivial under the Plan Gate's tripwires, and that classification is reviewable.
- A task request authorizes planning, not execution: it is not approval of the unit it produces.
- A verdict of the value audit is never presented as approval by the person directing the work; the authority in the second source is the ratification of the brief.
- A file's own text is never a source.
- In work no brief governs, when no source authorizes the unit and nobody can answer in the session, the Orchestrator presents it and ends the turn. Under a brief, a unit no source authorizes is presented to nobody: the turn ends blocked, naming what it waits on, as ADR-D-0062 states. Elapsed time, silence, and the absence of a human channel confer no authorization and revoke none already given.

## Why

The person directing the work shapes direction at product level instead of auditing each plan, so what that person ratified in a brief, checked against the work by a judge the Orchestrator cannot frame, carries that person's authority to the work. The party that would benefit from skipping approval cannot grant it to itself, and a request describes a goal, not a plan, so neither is ever a source. In work no brief governs, a presented unit awaiting a human is the correct resting state for a session nobody is watching, so the Orchestrator ends the turn rather than proceed. While a run under a brief is in progress, the person directing the work should never need to look at the Orchestrator session, so the first source, which is given in that session, is not sought for a plan: a plan under the brief is authorized by the brief route or is not yet a plan that can run. The brief does not stand in for agreeing a goal envelope, so that agreement stays that person's own and travels through Counsel like every other question. The sources are the same in every mode because the question they answer, whose authority stands behind execution, does not depend on how the work is structured.

## Rejected Alternatives

- The person directing the work approves every unit of work, the only source ADR-D-0032 admitted: it keeps that person auditing each plan for drift; reopen if units started under the second source turn out, when that person reads them afterwards, to be ones that person would have stopped, and the miss does not trace to how items are graded, which reopens the grade definitions first (ADR-D-0052).
- The second source authorizes work on a philosophy alone, with no ratified brief: rejected outright; no ratification of that piece of work exists for the audit to carry.
- A ratified brief authorizes every unit made under it, with no audit: rejected outright; the Orchestrator would be the judge of whether its own plan fits the brief.
- Orchestrator self-waiver with a recorded reason and evidence: rejected outright; the record is written by the party the waiver benefits, so it constrains nothing.
- A task request counts as approval of the resulting unit: reopen only if plan review moves entirely to a runtime mechanism that shows the plan to the person directing the work before any execution step in every runtime the harness supports.
- A headless fallback that proceeds after a timeout: rejected outright; silence carries no authority.
- Sources stated for plan mode only, goal mode keeping its own: it leaves the same question answered twice and lets the answers drift; reopen if a mode needs a source neither of these two can be.
- Under a brief, the first source kept as the fallback for a plan the brief route does not authorize: it lost because the person directing the work would have to look at the Orchestrator session for it; reopen if runs under a brief are found unable to end with nothing asked of that person in the Orchestrator session without it.

## Decision Boundary

Invariant: a non-trivial unit of work is authorized only by the explicit approval or waiver of the person directing the work in the Orchestrator session, or by that person's ratified governing brief carried to the work through the value audit under the conditions a per-mode record states; under a brief, a plan or a small change has the second source alone, a unit no source authorizes ends the turn blocked with nothing presented, and a goal envelope is agreed by that person's answer relayed through Counsel; the Orchestrator, the request, a verdict, a file's text and silence are never sources; the Decision list states the rest.

Not covered: the trivial/non-trivial tripwires and who applies them; the conditions under which the second source authorizes a plan in plan mode (ADR-D-0065) and a small change built without a plan (ADR-D-0055); the conditions under which it would authorize a goal-mode envelope, which a record for goal mode would state: this record decides goal mode's sources and not its conditions, and because ADR-D-0027's invariant admits only ratification by the person directing the work, that record would supersede ADR-D-0027, which this one leaves in force; what a goal-mode envelope consists of and that it is immutable during the loop (ADR-D-0027); how a question travels through Counsel and what the Orchestrator does when the brief route does not authorize a plan (ADR-D-0062); how a relay is admitted (ADR-D-0038); the grade names and their definitions, which no record states and the audit's mandate owns (ADR-D-0052 leaves them uncovered); the audit's procedure and the dispatch wording (ADR-D-0052); merge authorization; how the plan records the source; the wording of the Plan Gate, the lifecycle reference and the runtime entry points; how the presented unit is surfaced in each runtime.

## Validation

- The Plan Gate, its lifecycle reference and every runtime entry point that restates the approval condition name these two sources and no other, and state that under a brief a plan has the second source alone; the goal-mode reference names the first source, states that under a brief the envelope is agreed by the relayed answer of the person directing the work, and states that the second authorizes nothing in goal mode until a record states its conditions; and none presents a verdict as approval by the person directing the work.
- A loader probe given an ordinary non-trivial request with no ratified brief presents a plan and ends the turn with only planning artifacts written; the same request with an explicit waiver from the person directing the work proceeds past the Plan Gate.
- A probe under a governing brief whose plan the brief route does not authorize ends the turn blocked, naming the condition that failed, with no plan presented and no question asked in the Orchestrator session.

## Revisit When

- Units of work started under the second source turn out, when the person directing the work reads them afterwards, to be ones that person would have stopped. A miss that traces to how items are graded reopens the grade definitions first, as ADR-D-0052 says; any other reopens this record.
- A supported runtime gains a native plan-approval step that the harness can bind to, so that the request-as-approval alternative can be re-examined.
- The premise that a session under the installed loader will take a self-waiver or request-as-approval path when the text allows it was observed in a GPT-6 Astra session on 2026-09-08; the decision does not rest on that premise, so a model change reopens the probe, not the decision.
- A mode needs a source of authorization that is neither the person directing the work nor that person's ratified brief.
- On 2026-10-29 no run under a brief had yet ended with nothing asked of the person directing the work in the Orchestrator session; a run under a brief that asks that person anything there reopens this record.
- A run without Counsel is found to need its questions kept out of the Orchestrator session as a run under a brief has them.

## More Information

Replaces ADR-D-0040 in full: everything it decided is carried; under a ratified brief the first source authorizes no plan and agrees a goal envelope by an answer relayed through Counsel, and a unit no source authorizes ends the turn blocked with nothing presented. ADR-D-0040 replaced ADR-D-0032 and says "the person directing the work" where ADR-D-0032 said "the user". Source of intent for the second source: `docs/coding-agent/briefs/completed/value-level-operation-brief.md`, "Who it is for and why", "Stops during a run", "Roles and sessions" and "Lifecycle"; for the narrowing under a brief: the brief "A quiet Orchestrator session under a brief" (`quiet-orchestrator-session-brief.md`), "Who it is for and why", "What the plugin states" and "Directed during the run". Probe method and evidence for the self-waiver and request-as-approval readings: `docs/coding-agent/experiments/frontier-guard-probes/` in git history at `2a5ebf9`. Related records: ADR-D-0017 (harness text holds no user authority), ADR-D-0020 (loader-routed sessions assume the Orchestrator role), ADR-D-0027 (goal-mode envelope), ADR-D-0038 (the word of the person directing the work), ADR-D-0052 (the value audit), ADR-D-0062 (no question in the Orchestrator session under a brief), ADR-D-0065 (when a ratified brief authorizes a plan), ADR-D-0055 (a small change built without a plan), ADR-D-0042 (extensions at closeout).
