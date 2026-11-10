---
status: proposed
adr_type: design
date: 2026-11-07
deciders: ["ebigunso"]
consulted: ["Claude Opus 5.5"]
informed: []
supersedes: ["ADR-D-0040-non-trivial-work-is-authorized-only-by-the-person-directing-the-work-or-by-that-persons-ratified-brief.md", "ADR-D-0056-a-goal-mode-run-in-a-repository-with-a-philosophy-is-graded-by-the-value-audit-beside-the-assessor.md"]
superseded_by: null
depends_on: ["ADR-D-0017-harness-text-holds-no-user-authority.md", "ADR-D-0020-loader-routed-sessions-assume-the-orchestrator-role.md", "ADR-D-0038-the-word-of-the-person-directing-the-work-reaches-an-orchestrator-session-directly-or-by-quoted-relay.md", "ADR-D-0052-the-orchestrator-never-grades-its-own-run-and-its-reading-is-compared-only-after-the-grades-are-fixed.md", "ADR-D-0066-a-goal-loops-forbidden-set-is-a-criterion-and-its-envelope-is-fixed-before-the-loop-and-never-changed-by-it.md"]
---

# ADR-D-0064: Non-trivial work is authorized only by the person directing the work or by that person's ratified brief

Proposed to replace ADR-D-0040, and ADR-D-0056 together with ADR-D-0063; awaiting acceptance by the person directing the work, by name.

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session the person directing the work opens for value discussion, separate from any Orchestrator session. The Orchestrator session is a session that holds the Orchestrator role (ADR-D-0020) and plans, dispatches and reports the work.

An Orchestrator session prepares a non-trivial unit of work (a plan, a small change the person directing the work stated in a ratified brief, or the envelope of a goal-mode run) and needs authorization to execute it. Before 2026-09-10 the approval rule could be read so that the Orchestrator waived approval on its own authority, or so that the task request counted as approval of whatever plan resulted from it, and execution then started with no human authority behind it. Under value-level operation the person directing the work ratifies a brief as the grounds for a piece of work instead of auditing each plan, and while a run under that brief is in progress that person is asked nothing in the Orchestrator session (ADR-D-0062). The fork is whose authority may stand behind execution, in any mode, and whether any unit under a brief still needs that person's own word.

## Decision

- Execution of a non-trivial unit of work, in any mode, starts only on the authority of the person directing the work, given in one of two forms: that person's own explicit approval of the unit or explicit waiver of its approval; or that person's ratification of the governing brief, carried to the unit by the value audit (ADR-D-0052) on conditions a record states for that kind of unit. For a kind of unit no record states conditions for, the ratification authorizes nothing.
- Under a ratified governing brief the ratification is the only authority for every unit, a goal envelope included. No unit under a brief needs that person's own approval or agreement, none is put to that person for it, and a unit the ratification does not authorize does not run.
- Without a ratified governing brief, a run audited against a philosophy alone included, only that person's own approval or waiver authorizes: a philosophy states standing direction and ratifies no piece of work.
- Nothing else authorizes: not the Orchestrator's own judgement (it may classify work as trivial, and that classification is reviewable), not a task request (which authorizes planning only), not a verdict of the value audit (never presented as that person's approval), not a file's text, and not elapsed time, silence or the absence of anyone to ask, which confer no authorization and revoke none already given.
- Work that nothing authorizes does not start.

## Why

Approving every unit keeps the person directing the work auditing each plan for drift, so a brief that person ratified carries that person's authority to a unit once a judge the Orchestrator cannot frame has checked the unit against it. Under a brief this is the only authority, a goal envelope included, since requiring that person's agreement to an envelope would put before every goal run a stop no plan has and make goal mode costlier to choose where it is the fitting shape.

## Rejected Alternatives

- The person directing the work approves every unit of work, the only form ADR-D-0032 admitted: it keeps that person auditing each plan for drift; reopen if units started on the ratified brief turn out, when that person reads them afterwards, to be ones that person would have stopped, and the miss does not trace to how items are graded, which reopens the grade definitions before this record (ADR-D-0052).
- The ratification authorizes work on a philosophy alone, with no ratified brief: rejected outright; no ratification of that piece of work exists for the audit to carry.
- A ratified brief authorizes every unit made under it, with no audit: rejected outright; the Orchestrator would be the judge of whether its own unit fits the brief.
- Orchestrator self-waiver with a recorded reason and evidence: rejected outright; the record is written by the party the waiver benefits, so it constrains nothing.
- A task request counts as approval of the resulting unit: it lost because a request describes a goal, not approval of the unit it produces; reopen only if every runtime the harness supports shows the unit to the person directing the work before any execution step.
- Proceeding when nobody answers within some time: rejected outright; silence carries no authority.
- Authority stated for plan mode only, goal mode keeping its own: it leaves the same question, whose authority stands behind execution, answered twice and lets the answers drift; reopen if a mode needs an authority that neither form can be.
- Under a brief, a goal envelope needs that person's own agreement, the brief never standing in for it: it lost because it puts before every goal run under a brief a stop that no plan has, which makes goal mode costlier to choose than a plan where goal mode is the fitting shape; reopen if goal runs started on the ratified brief turn out, when that person reads them afterwards, to be ones that person would have stopped, and the miss traces to the envelope rather than to how items are graded.
- Under a brief, that person's own approval kept as the fallback for a unit the ratification does not authorize: it lost because that person would have to look at the Orchestrator session for it; reopen if runs under a brief are found unable to end with nothing asked of that person in the Orchestrator session without it.
- Under a brief, approval of a unit the ratification does not authorize sought from that person through Counsel: it lost because a unit the brief does not authorize is not yet a unit that can run, so there is nothing for an approval to add; reopen if runs under a brief are found unable to end with nothing asked of that person in the Orchestrator session without it.

## Decision Boundary

Invariant: execution of non-trivial work starts only on the authority of the person directing the work, given as that person's own explicit approval or waiver, or as that person's ratified brief carried to the work by the value audit on conditions a record states for the kind of unit; under a brief the ratification is the only authority for every unit, a goal envelope included, and no unit is put to that person for approval or agreement; without a brief only that person's own approval or waiver authorizes; nothing else is ever an authority, and unauthorized work does not start.

Not covered: what counts as trivial; the conditions under which the ratification authorizes a plan or a goal envelope (ADR-D-0065) or a small change built without a plan (ADR-D-0055); what an envelope consists of and that the loop never changes it (ADR-D-0066); where and how that person's approval or waiver is given and reaches the run, and how a relay is admitted (ADR-D-0038 and the harness text); what the Orchestrator does while a unit awaits authorization or when the ratification does not authorize it, which the harness text states; how a question reaches that person under a brief (ADR-D-0062); how a goal run is graded once its loop starts (ADR-D-0063); the grade names and the audit's procedure (ADR-D-0052 and the audit's mandate); merge authorization; how the authority is recorded; the wording of the harness text.

## Validation

- Review of any change to the harness text asks: does it let non-trivial work start on any authority other than that person's own approval or waiver and that person's ratified brief; under a brief, does it put any unit, a goal envelope included, to that person for approval or agreement; or does it present a verdict as that person's approval?

## Revisit When

- Units of work started on the ratified brief turn out, when the person directing the work reads them afterwards, to be ones that person would have stopped. A miss that traces to how items are graded reopens the grade definitions before this record, as ADR-D-0052 says; any other reopens this record.
- A supported runtime gains its own step that shows a unit to the person directing the work before execution, so that the request-as-approval alternative can be re-examined.
- A mode needs an authority that is neither that person's own approval nor that person's ratified brief.
- On 2026-10-29 no run under a brief had yet ended with nothing asked of the person directing the work in the Orchestrator session; a run under a brief found unable to do so without that person's own approval of a unit reopens this record.
- On 2026-11-07 no goal envelope had been authorized by a ratified brief; a goal run so started and later found to have needed that person's own agreement to its envelope reopens this record.

## More Information

Replaces ADR-D-0040 in full, and ADR-D-0056 together with ADR-D-0063: of ADR-D-0056 this record holds who authorizes a goal envelope, which ADR-D-0056 kept with the person directing the work in the Orchestrator session, and ADR-D-0063 holds the value audit's grading of a goal run. What changes from ADR-D-0040: under a ratified brief the ratification is the only authority for every unit, a goal envelope included, and no unit is put to the person directing the work. Source of intent: `docs/coding-agent/briefs/completed/value-level-operation-brief.md`, "Who it is for and why", "Stops during a run", "Roles and sessions" and "Lifecycle"; the brief "A quiet Orchestrator session under a brief" (`docs/coding-agent/briefs/active/quiet-orchestrator-session-brief.md`), "Who it is for and why", "What the plugin states" and "Directed during the run". Related records: ADR-D-0017 (harness text holds no user authority), ADR-D-0038 (the word of the person directing the work), ADR-D-0052 (the value audit), ADR-D-0055 (a small change built without a plan), ADR-D-0062 (no question in the Orchestrator session under a brief), ADR-D-0063 (the value audit in a goal run), ADR-D-0065 (when a ratified brief authorizes a plan or a goal envelope), ADR-D-0066 (the envelope).
