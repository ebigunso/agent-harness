---
status: proposed
adr_type: design
date: 2026-11-24
deciders: ["ebigunso"]
consulted: ["Claude Opus 5.5"]
informed: []
supersedes: ["ADR-D-0064-non-trivial-work-is-authorized-only-by-the-person-directing-the-work-or-by-that-persons-ratified-brief.md"]
superseded_by: null
depends_on: ["ADR-D-from-0064-non-trivial-work-is-authorized-only-by-the-person-directing-the-work.md", "ADR-D-0084-no-goal-loop-starts-without-an-authority-envelope.md"]
---

# ADR-D-XXXX: Under a ratified brief no unit of work is put to the person directing the work for approval or agreement; the ratification is its only authority, and a unit the ratification does not authorize does not run

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session role that person talks with about what the product does or should do. The Orchestrator session is a session that holds the Orchestrator role and plans, dispatches and reports the work.

A person who ratifies a brief makes it the grounds for a piece of work, and is to be free of auditing each unit of that work for drift; while a run under the brief is in progress, that person is asked nothing in the Orchestrator session (ADR-D-0062). The ratification, carried to a unit by the value audit, can authorize the unit (ADR-D-from-0064-non-trivial-work-is-authorized-only-by-the-person-directing-the-work). A unit under the brief that still needs that person's own word fails this: approval kept as the fallback for a unit the ratification does not authorize has that person looking at the Orchestrator session for it, and agreement required for the envelope of a goal-mode run puts before every goal run a stop that no plan has. The fork is whether any unit under a brief, a goal envelope included, still needs that person's own approval or agreement and is put to that person for it.

## Decision

- Under a ratified governing brief the ratification is the only authority for every unit, a goal envelope included.
- No unit under a brief needs the person directing the work's own approval or agreement, and none is put to that person for it.
- A unit the ratification does not authorize does not run.

## Why

Approving every unit keeps the person directing the work auditing each plan for drift, and a unit the ratification does not authorize is not yet a unit that can run, so there is nothing for that person's approval to add. A goal envelope is no exception, since requiring that person's agreement to it would put before every goal run a stop no plan has and make goal mode costlier to choose where it is the fitting shape. This is what the product philosophy's "What it must not be" asks: "Not a permission-seeker. Asking before each step feels careful and is the second failure."

## Rejected Alternatives

- The person directing the work approves every unit of work: it keeps that person auditing each plan for drift; reopen if units started on the ratified brief turn out, when that person reads them afterwards, to be ones that person would have stopped, and the miss does not trace to how items are graded, which reopens the grade definitions before this record (ADR-D-0052, which the proposed ADR-D-0134 takes over).
- Under a brief, a goal envelope needs that person's own agreement, the brief never standing in for it: it lost because it puts before every goal run under a brief a stop that no plan has, which makes goal mode costlier to choose than a plan where goal mode is the fitting shape; reopen if goal runs started on the ratified brief turn out, when that person reads them afterwards, to be ones that person would have stopped, and the miss traces to the envelope rather than to how items are graded.
- Under a brief, that person's own approval kept as the fallback for a unit the ratification does not authorize: it lost because that person would have to look at the Orchestrator session for it; reopen if runs under a brief are found unable to end with nothing asked of that person in the Orchestrator session without it.
- Under a brief, approval of a unit the ratification does not authorize sought from that person through Counsel: it lost because a unit the brief does not authorize is not yet a unit that can run, so there is nothing for an approval to add; reopen if runs under a brief are found unable to end with nothing asked of that person in the Orchestrator session without it.

## Decision Boundary

Not covered: the authority on which non-trivial work starts, that the ratification authorizes no kind of unit for which no record states conditions, and what is never an authority (ADR-D-from-0064-non-trivial-work-is-authorized-only-by-the-person-directing-the-work); the conditions under which the ratification authorizes a plan or a goal envelope (ADR-D-0065) or a small change built without a plan (ADR-D-0055); how a question reaches that person under a brief (ADR-D-0062); what an envelope consists of and that the loop never changes it (ADR-D-0084, ADR-D-0086); what the Orchestrator does when the ratification does not authorize a unit, which the harness text states; how a goal run is graded once its loop starts (ADR-D-0082); merge authorization; the wording of the harness text.

## Validation

The decision is broken where:

- under a ratified brief a unit, a goal envelope included, was put to the person directing the work for approval or agreement;
- under a ratified brief a unit ran on that person's own approval or agreement, or on any authority other than the ratification;
- a unit the ratification did not authorize ran.

## Revisit When

- Units of work started on the ratified brief turn out, when the person directing the work reads them afterwards, to be ones that person would have stopped. A miss that traces to how items are graded reopens the grade definitions before this record, as ADR-D-0052 says (the proposed ADR-D-0134 takes it over); any other reopens this record.
- On 2026-10-29 no run under a brief had yet ended with nothing asked of the person directing the work in the Orchestrator session; a run under a brief found unable to do so without that person's own approval of a unit reopens this record.
- On 2026-11-07 no goal envelope had been authorized by a ratified brief; a goal run so started and later found to have needed that person's agreement to its envelope reopens this record.

## More Information

With ADR-D-from-0064-non-trivial-work-is-authorized-only-by-the-person-directing-the-work, replaces ADR-D-0064 in full; the decision carried here is the same. Carried here from it: that under a ratified brief the ratification is the only authority for every unit, a goal envelope included, that no unit under a brief needs that person's own approval or agreement or is put to that person for it, and that a unit the ratification does not authorize does not run. It is a record of its own because it would still bind if the authority on which non-trivial work starts were decided otherwise: it would still keep every unit under a brief from being put to the person directing the work. The rejected alternative that the person directing the work approves every unit, and the revisit condition it shares, are carried by ADR-D-from-0064-non-trivial-work-is-authorized-only-by-the-person-directing-the-work as well, for its own decision. Source of intent: `docs/coding-agent/briefs/completed/value-level-operation-brief.md`, "Who it is for and why", "Stops during a run", "Roles and sessions" and "Lifecycle"; the brief "A quiet Orchestrator session under a brief" (`docs/coding-agent/briefs/completed/quiet-orchestrator-session-brief.md`), "Who it is for and why", "What the plugin states" and "Directed during the run". Related records: ADR-D-0062 (no question in the Orchestrator session under a brief), ADR-D-0065 (when a ratified brief authorizes a plan or a goal envelope), ADR-D-0055 (a small change built without a plan), ADR-D-0084 (the envelope), ADR-D-0082 (the value audit in a goal run), ADR-D-0112 (approval or waiver of a plan is not carried by relay).
