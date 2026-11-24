---
status: proposed
adr_type: design
date: 2026-11-24
deciders: ["ebigunso"]
consulted: ["Claude Opus 5.5"]
informed: []
supersedes: ["ADR-D-0064-non-trivial-work-is-authorized-only-by-the-person-directing-the-work-or-by-that-persons-ratified-brief.md"]
superseded_by: null
depends_on: ["ADR-D-0105-harness-text-holds-none-of-the-users-authority.md", "ADR-D-0090-a-session-holds-a-role-only-by-its-openers-choice-or-the-default.md", "ADR-D-0112-the-persons-word-reaches-an-orchestrator-session-in-it-or-by-counsels-quoted-relay.md", "ADR-D-0052-the-orchestrator-never-grades-its-own-run-and-its-reading-is-compared-only-after-the-grades-are-fixed.md", "ADR-D-0084-no-goal-loop-starts-without-an-authority-envelope.md"]
---

# ADR-D-0139: Non-trivial work is authorized only by the person directing the work, by that person's own approval or waiver or by that person's ratified brief, and nothing else is ever an authority

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. The Orchestrator session is a session that holds the Orchestrator role (ADR-D-0090) and plans, dispatches and reports the work.

An Orchestrator session prepares a non-trivial unit of work, such as a plan or the envelope of a goal-mode run, and needs authorization to execute it. Execution is to have the authority of the person directing the work behind it, and that person is to be free of auditing each plan for drift: a brief that person ratifies is the grounds for a piece of work in place of that person's approval of each unit of it. A rule that can be read so that the Orchestrator waives approval on its own authority, or so that a task request counts as approval of the unit it produces, fails this by letting execution start with no human authority behind it. A ratified brief alone fails this too, since whether a unit fits the brief has to be judged by someone and the party that wrote the unit cannot be the judge of it. The fork is whose authority may stand behind the execution of a non-trivial unit of work, in any mode, and what can never be that authority.

## Decision

- Execution of a non-trivial unit of work, in any mode, starts only on the authority of the person directing the work, given as that person's own explicit approval of the unit or explicit waiver of its approval, or as that person's ratification of the governing brief, carried to the unit by the value audit (ADR-D-0052, which the proposed ADR-D-0134 takes over for a plan-mode run; ADR-D-0082 for a goal run) on conditions a record states for that kind of unit.
- For a kind of unit no record states conditions for, the ratification authorizes nothing.
- Without a ratified governing brief, a run audited against a philosophy alone included, only that person's own approval or waiver authorizes: a philosophy states standing direction and ratifies no piece of work.
- Nothing else authorizes: not the Orchestrator's own judgement (it may classify work as trivial, and that classification is reviewable), not a task request (which authorizes planning only), not a verdict of the value audit (never presented as that person's approval), not a file's text, and not elapsed time, silence or the absence of anyone to ask, which confer no authorization and revoke none already given.
- Work that nothing authorizes does not start.

## Why

Approving every unit keeps the person directing the work auditing each plan for drift, so a brief that person ratified carries that person's authority to a unit once a judge the Orchestrator cannot frame has checked the unit against it. Every other source leaves the unit with none of that person's authority behind it: a waiver the Orchestrator records is written by the party it benefits and constrains nothing, a request describes a goal and not the unit it produces, and silence carries no authority. This is what the product philosophy's "What it must not be" asks: "Not its own judge. A builder's confidence in its own work is not evidence, and a longer list of rules does not make it so."

## Rejected Alternatives

- The person directing the work approves every unit of work: it keeps that person auditing each plan for drift; reopen if units started on the ratified brief turn out, when that person reads them afterwards, to be ones that person would have stopped, and the miss does not trace to how items are graded, which reopens the grade definitions before this record (ADR-D-0052, which the proposed ADR-D-0134 takes over for a plan-mode run).
- The ratification authorizes work on a philosophy alone, with no ratified brief: rejected outright; no ratification of that piece of work exists for the audit to carry.
- A ratified brief authorizes every unit made under it, with no audit: rejected outright; the Orchestrator would be the judge of whether its own unit fits the brief.
- Orchestrator self-waiver with a recorded reason and evidence: rejected outright; the record is written by the party the waiver benefits, so it constrains nothing.
- A task request counts as approval of the resulting unit: it lost because a request describes a goal, not approval of the unit it produces; reopen only if every runtime the harness supports shows the unit to the person directing the work before any execution step.
- Proceeding when nobody answers within some time: rejected outright; silence carries no authority.
- Authority stated for plan mode only, goal mode keeping its own: it leaves the same question, whose authority stands behind execution, answered twice and lets the answers drift; reopen if a mode needs an authority that is neither that person's own approval or waiver nor that person's ratified brief.

## Decision Boundary

Not covered: what counts as trivial; the conditions under which the ratification authorizes a plan or a goal envelope (ADR-D-0141) or a small change built without a plan (ADR-D-0147); that under a ratified brief the ratification is the only authority for every unit and no unit is put to the person directing the work for approval or agreement (ADR-D-0140); what an envelope consists of and that the loop never changes it (ADR-D-0084, ADR-D-0086); where and how that person's approval or waiver is given and reaches the run, and how a relay is admitted (ADR-D-0112 and the harness text); what the Orchestrator does while a unit awaits authorization or when the ratification does not authorize it, which the harness text states; how a goal run is graded once its loop starts (ADR-D-0082); the grade names and the audit's procedure (ADR-D-0052, which the proposed ADR-D-0134 takes over for a plan-mode run; ADR-D-0082 for a goal run; and the audit's mandate); merge authorization; how the authority is recorded; the wording of the harness text.

## Validation

The decision is broken where:

- a non-trivial unit of work started on no authority, or on one other than the person directing the work's own explicit approval or waiver or that person's ratified brief carried to it by the value audit on conditions a record states for its kind;
- a unit of a kind no record states conditions for started on the ratification;
- work no ratified brief governs, a run audited against a philosophy alone included, started without that person's own approval or waiver;
- a verdict of the value audit was presented as that person's approval.

## Revisit When

- Units of work started on the ratified brief turn out, when the person directing the work reads them afterwards, to be ones that person would have stopped. A miss that traces to how items are graded reopens the grade definitions before this record, as ADR-D-0052 says (the proposed ADR-D-0134 takes it over for a plan-mode run); any other reopens this record.
- A supported runtime gains its own step that shows a unit to the person directing the work before execution, so that the request-as-approval alternative can be re-examined.
- A mode needs an authority that is neither that person's own approval nor that person's ratified brief.

## More Information

With ADR-D-0140, replaces ADR-D-0064 in full; the decision carried here is the same. Carried here from it: the authority on which non-trivial work starts in any mode, that the ratification authorizes no kind of unit for which no record states conditions, the rule where no ratified brief governs, what never authorizes, and that work nothing authorizes does not start. It is a record of its own because it binds whether or not, under a brief, units are kept from being put to the person directing the work; ADR-D-0040 stated it without that. The rejected alternative that the person directing the work approves every unit, and the revisit condition it shares, are carried by ADR-D-0140 as well, for its own decision. Source of intent: `docs/coding-agent/briefs/completed/value-level-operation-brief.md`, "Who it is for and why", "Stops during a run", "Roles and sessions" and "Lifecycle"; the brief "A quiet Orchestrator session under a brief" (`docs/coding-agent/briefs/completed/quiet-orchestrator-session-brief.md`), "Who it is for and why", "What the plugin states" and "Directed during the run". Related records: ADR-D-0105 (harness text holds no user authority), ADR-D-0112 (the word of the person directing the work), ADR-D-0052 and the proposed ADR-D-0134 (the value audit in a plan-mode run), ADR-D-0147 (a small change built without a plan), ADR-D-0141 (when a ratified brief authorizes a plan or a goal envelope), ADR-D-0082 (the value audit in a goal run), ADR-D-0084 (the envelope).
