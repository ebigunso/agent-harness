---
status: proposed
adr_type: design
date: 2026-10-29
deciders: ["ebigunso"]
consulted: ["Claude Opus 5.5"]
informed: []
supersedes: ["ADR-D-0040-non-trivial-work-is-authorized-only-by-the-person-directing-the-work-or-by-that-persons-ratified-brief.md", "ADR-D-0056-a-goal-mode-run-in-a-repository-with-a-philosophy-is-graded-by-the-value-audit-beside-the-assessor.md"]
superseded_by: null
depends_on: ["ADR-D-0017-harness-text-holds-no-user-authority.md", "ADR-D-0020-loader-routed-sessions-assume-the-orchestrator-role.md", "ADR-D-0027-the-forbidden-set-is-a-criterion-ratified-before-the-loop.md", "ADR-D-0038-the-word-of-the-person-directing-the-work-reaches-an-orchestrator-session-directly-or-by-quoted-relay.md", "ADR-D-0052-the-orchestrator-never-grades-its-own-run-and-its-reading-is-compared-only-after-the-grades-are-fixed.md"]
---

# ADR-D-0064: Non-trivial work is authorized only by the person directing the work or by that person's ratified brief

Proposed on 2026-10-29 to replace ADR-D-0040, and ADR-D-0056 together with ADR-D-0063; awaiting acceptance by the person directing the work, by name.

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. The product owner is whoever is entitled to state the product's values and to answer product-level questions for that work; when the person directing the work owns the product, both are that person. Counsel is the session the person directing the work opens for value discussion, separate from any Orchestrator session. The Orchestrator session is a session that holds the Orchestrator role (ADR-D-0020) and plans, dispatches and reports the work.

An Orchestrator session prepares a non-trivial unit of work (in plan mode a plan, or a small change the person directing the work stated in a ratified brief; in goal mode an envelope) and then needs authorization to execute it. Before 2026-09-10 two readings of the approval rule let execution start with no human authority behind the plan: the Orchestrator waived approval on its own authority with a recorded reason, or the ordinary task request was taken as approval of whatever plan resulted from it. On 2026-09-08 a headless GPT-6 Astra session under the installed loader took both readings and implemented the work with no human having seen the plan. Under value-level operation a second pressure meets the first: the person directing the work ratifies a brief as the grounds for a piece of work and shapes direction at product level instead of auditing each plan, and while a run under that brief is in progress, that person is not to be asked anything in the Orchestrator session (ADR-D-0062). The fork is what may authorize a unit of work at all, in any mode, and which source applies while a brief governs.

## Decision

- Execution of a non-trivial unit of work, in any mode, is authorized only by one of two sources.
- The first source is the person directing the work: an explicit approval of the unit as presented, or an explicit waiver that names the approval step. In work no brief governs it is given in the Orchestrator session and never carried by a relay.
- The second source is the ratification of the governing brief by the person directing the work, carried to the unit of work through the value audit (ADR-D-0052). The conditions under which it carries, when the audit judges the unit among them, are stated per mode by a record of their own; where no record states them for a mode, the second source authorizes nothing in that mode.
- Under a ratified brief the second source is the only source for a plan or a small change: no plan is put to the person directing the work for approval, in the Orchestrator session or through Counsel, and a plan the second source does not authorize does not run.
- Under a ratified brief the first source's one use is agreement to a goal-mode envelope: that agreement is the person directing the work's own word, which may reach the run through Counsel, and the brief never stands in for it.
- Without a ratified governing brief, a run audited against a philosophy alone included, only the first source authorizes: a philosophy states standing direction and ratifies no piece of work.
- The Orchestrator never approves a unit of work or waives its approval on its own authority; it may classify work as trivial, and that classification is reviewable.
- A task request authorizes planning, not execution: it is not approval of the unit it produces.
- A verdict of the value audit is never presented as approval by the person directing the work; the authority in the second source is the ratification of the brief.
- A file's own text is never a source.
- Work no source authorizes does not execute. In work no brief governs, a unit awaiting the first source rests presented, and nobody being able to answer does not move it on. Elapsed time, silence and the absence of a human channel confer no authorization and revoke none already given.

## Why

The person directing the work shapes direction at product level instead of auditing each plan ("Value-level operation", "Who it is for and why"), so what that person ratified in a brief, checked against the work by a judge the Orchestrator cannot frame, carries that person's authority to the work, and neither the party that would benefit from skipping approval nor a request that describes a goal rather than a unit can stand in for it. While a run under a brief is in progress that person should never need to look at the Orchestrator session ("A quiet Orchestrator session under a brief", "Who it is for and why"), so no plan is put to that person for approval, while agreeing a goal envelope stays that person's own because the brief does not stand in for it ("Directed during the run").

## Rejected Alternatives

- The person directing the work approves every unit of work, the only source ADR-D-0032 admitted: it keeps that person auditing each plan for drift; reopen if units started under the second source turn out, when that person reads them afterwards, to be ones that person would have stopped, and the miss does not trace to how items are graded, which reopens the grade definitions first (ADR-D-0052).
- The second source authorizes work on a philosophy alone, with no ratified brief: rejected outright; no ratification of that piece of work exists for the audit to carry.
- A ratified brief authorizes every unit made under it, with no audit: rejected outright; the Orchestrator would be the judge of whether its own plan fits the brief.
- Orchestrator self-waiver with a recorded reason and evidence: rejected outright; the record is written by the party the waiver benefits, so it constrains nothing.
- A task request counts as approval of the resulting unit: reopen only if plan review moves entirely to a runtime mechanism that shows the plan to the person directing the work before any execution step in every runtime the harness supports.
- A headless fallback that proceeds after a timeout: rejected outright; silence carries no authority, and a unit resting presented is the correct state for a session nobody is watching.
- Sources stated for plan mode only, goal mode keeping its own: it leaves the same question, whose authority stands behind execution, answered twice and lets the answers drift; reopen if a mode needs a source neither of these two can be.
- Under a brief, the first source kept as the fallback for a plan the second does not authorize: it lost because the person directing the work would have to look at the Orchestrator session for it; reopen if runs under a brief are found unable to end with nothing asked of that person in the Orchestrator session without it.
- Under a brief, approval of a plan the second source does not authorize carried to the person directing the work through Counsel: it lost because a plan the brief route does not authorize is not yet a plan that can run, so there is nothing for an approval to add; reopen if runs under a brief are found unable to end with nothing asked of that person in the Orchestrator session without it.

## Decision Boundary

Invariant: a non-trivial unit of work is authorized only by the explicit approval or waiver of the person directing the work, or by that person's ratified governing brief carried to the work through the value audit under the conditions a per-mode record states; under a brief, a plan or a small change has the second source alone, no plan is put to that person for approval and an unauthorized plan does not run, while a goal envelope is agreed by that person's own word and never by the brief; without a brief only the first source authorizes; the Orchestrator, the request, a verdict, a file's text and silence are never sources; no unauthorized work executes.

Not covered: what counts as trivial and who applies it; the conditions under which the second source authorizes a plan in plan mode (ADR-D-0065) and a small change built without a plan (ADR-D-0055); the conditions under which it would authorize a goal-mode envelope, which a record for goal mode would state: this record decides goal mode's sources and not its conditions, and because ADR-D-0027's invariant admits only ratification by the person directing the work, that record would supersede ADR-D-0027, which this one leaves in force; what a goal-mode envelope consists of and that it is immutable during the loop (ADR-D-0027); how a question under a brief reaches the person directing the work (ADR-D-0062) and what the Orchestrator does when the second source does not authorize a plan, which the harness text states; how a relay is admitted (ADR-D-0038); the grade names and their definitions, which no record states and the audit's mandate owns (ADR-D-0052 leaves them uncovered); the audit's procedure and how it is asked (ADR-D-0052); merge authorization; how the source is recorded; the wording of the harness text that states the approval rule; how the presented unit is surfaced in each runtime.

## Validation

- Every place the harness text states what authorizes execution names these two sources and no other; states that under a brief a plan has the second source alone and a goal envelope the agreement of the person directing the work; states that the second source authorizes nothing in goal mode until a record states its conditions; and presents no verdict as approval by the person directing the work.
- A probe given an ordinary non-trivial request with no ratified brief presents a plan and ends the turn with only planning artifacts written; the same request with an explicit waiver from the person directing the work proceeds past the approval step.
- A probe under a governing brief whose plan the brief route does not authorize does not execute the plan, presents it to nobody, and asks nothing in the Orchestrator session.
- A goal run under a brief shows the agreement of the person directing the work to its envelope, as that person's own word, before its first iteration.

## Revisit When

- Units of work started under the second source turn out, when the person directing the work reads them afterwards, to be ones that person would have stopped. A miss that traces to how items are graded reopens the grade definitions first, as ADR-D-0052 says; any other reopens this record.
- A supported runtime gains a native plan-approval step that the harness can bind to, so that the request-as-approval alternative can be re-examined.
- The premise that a session under the installed loader will take a self-waiver or request-as-approval path when the text allows it was observed in a GPT-6 Astra session on 2026-09-08; the decision does not rest on that premise, so a model change reopens the probe, not the decision.
- A mode needs a source of authorization that is neither the person directing the work nor that person's ratified brief.
- On 2026-10-29 no run under a brief had yet ended with nothing asked of the person directing the work in the Orchestrator session; a run under a brief found unable to do so without the first source for its plan, or in which that person had to look at the Orchestrator session to agree a goal envelope, reopens this record.

## More Information

Replaces ADR-D-0040 in full: everything it decided is carried; under a ratified brief the first source authorizes no plan and its one use is agreement to a goal envelope, which may reach the run through Counsel, and a plan the second source does not authorize does not run and is put to nobody for approval. This record also holds who ratifies a goal envelope, which ADR-D-0056 stated beside the value audit's attachment to a goal loop. ADR-D-0040 replaced ADR-D-0032 and says "the person directing the work" where ADR-D-0032 said "the user". Source of intent for the second source: `docs/coding-agent/briefs/completed/value-level-operation-brief.md`, "Who it is for and why", "Stops during a run", "Roles and sessions" and "Lifecycle"; for the narrowing under a brief and the goal envelope: the brief "A quiet Orchestrator session under a brief" (`docs/coding-agent/briefs/active/quiet-orchestrator-session-brief.md`), "Who it is for and why", "What the plugin states" and "Directed during the run". What the Orchestrator does when the brief route does not authorize a plan, and how the envelope is put to the person directing the work, are the harness text's and change without this record. Probe method and evidence for the self-waiver and request-as-approval readings: `docs/coding-agent/experiments/frontier-guard-probes/` in git history at `2a5ebf9`. Related records: ADR-D-0017 (harness text holds no user authority), ADR-D-0020 (loader-routed sessions assume the Orchestrator role), ADR-D-0027 (goal-mode envelope), ADR-D-0038 (the word of the person directing the work), ADR-D-0052 (the value audit), ADR-D-0062 (no question in the Orchestrator session under a brief), ADR-D-0063 (the value audit in a goal run), ADR-D-0065 (when a ratified brief authorizes a plan), ADR-D-0055 (a small change built without a plan), ADR-D-0042 (extensions at closeout).
