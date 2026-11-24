---
status: proposed
adr_type: design
date: 2026-11-24
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "Claude Opus 5.5"]
informed: []
supersedes: ["ADR-D-0055-a-small-change-stated-in-a-ratified-brief-may-be-built-without-a-plan-and-stands-only-once-a-closing-value-audit-holds-nothing.md"]
superseded_by: null
depends_on: ["ADR-D-0139-non-trivial-work-is-authorized-only-by-the-person-directing-the-work.md", "ADR-D-0141-a-brief-authorizes-a-plan-or-goal-envelope-only-on-a-closed-review-and-an-audit-holding-nothing.md", "ADR-D-0134-the-orchestrator-never-grades-its-own-run-against-the-value-documents.md"]
---

# ADR-D-0147: A small change the person directing the work stated in a ratified brief may be built without a plan, and stands only once a closing value audit holds nothing

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. The Orchestrator session is a session that holds the Orchestrator role (ADR-D-0090) and plans, dispatches and reports the work.

The person directing the work wants a change that person states in a ratified brief built as stated, at a cost in proportion to the change. Trivial work is handled directly, but only when it changes no behaviour; a change that person states always changes behaviour, so it is never trivial work. That person's ratified brief, carried to the work through the value audit, authorizes a unit of work on conditions a record states for that kind of unit (ADR-D-0139), and ADR-D-0141 states them for a plan. With a plan as the only other unit, even a one-sentence change takes a plan and every check a plan goes through. The fork is whether such a change, when it is small, must have a plan, who decides that for each change, and what then stands between it and being reported as done.

## Decision

- The ratified brief of the person directing the work authorizes a small change to be built without a plan, and so without the checks a plan goes through before it is built, when that person stated the change in the governing brief, or in an amendment to it, whose ratification reached the Orchestrator session on the terms ADR-D-0141 states for a plan; that person's statement in the brief then stands in place of the plan.
- The Orchestrator chooses, for each change, whether to draft a plan; when it drafts one, that plan is authorized as any plan under the brief is (ADR-D-0141). A plan is the right choice where the work cannot be done as a single task, or where the statement leaves open a choice about how to do it that someone should see before it is built.
- Whether or not a plan is drafted, a small change keeps the review of the change and a value audit at its close, which checks that what was built is what the statement said and nothing more, and holds whatever went beyond the statement.
- Nothing of the change is published or reported as done before that audit holds nothing.
- Whether a change is small is the Orchestrator's call, and the closing audit is the guard on that call.
- What counts as trivial work does not change: that class has no audit behind it.

## Why

For a change this small the whole of a plan's checks is often out of proportion, and the statement of the person directing the work in the brief can stand as the plan, as the product philosophy's "What it must not be" asks: "Not heavier than the request. A small ask gets a small process." Yet what is being worked on sometimes wants a plan even when the change is small, so the choice is left open rather than fixed by a rule, and a rule strict in either direction would force suboptimal choices. This knowingly loosens the gate for that class of change: the closing audit, which holds whatever went beyond the statement, guards the Orchestrator's call that a change is small, and the condition under Revisit When on a change found to have needed a plan is the check on its choice to draft none. The trivial class stays strict because nothing audits it.

## Rejected Alternatives

- A small change stated by the person directing the work takes a plan, its review and its draft audit like any other change that alters behaviour: it lost because for a one-sentence change that suite is out of proportion; exercising the guards is a reason to test them, not a reason for the harness to behave this way; reopen if small changes are found to have gone beyond the statement without the closing audit holding them.
- A small change keeps a plan document in a short form and drops only its review and its draft audit: rejected outright; where a plan is worth drafting it is worth its review, and where it is not the plan would repeat the statement it is built from.
- A small change is always built without a plan: it lost because whether a plan is needed depends on what is being worked on, and a rule that waives it entirely forces the Orchestrator past that judgement; reopen if the per-change choice is found to be made the same way every time.

## Decision Boundary

Not covered: trivial work and its tripwires (ADR-D-0139 leaves them uncovered); how the Orchestrator judges that a change is small; that a small change is a unit of the run its governing brief governs, and how it closes and is reported as part of that run (ADR-D-0144); how and where a small change is recorded; the branch and pull request it is published on; goal mode; the conditions under which the ratified brief of the person directing the work authorizes a plan (ADR-D-0141); the value audit itself, its procedure and the dispatch wording (ADR-D-0052, which the proposed ADR-D-0134, ADR-D-0135 and ADR-D-0136 take over; ADR-D-0050).

## Validation

The decision is broken where:

- a change was built without a plan on the authority of the ratified brief of the person directing the work though that person had not stated it in that brief or in an amendment to it whose ratification reached the Orchestrator session;
- a small change went without the review of the change or without a value audit at its close;
- something of a small change was published or reported as done before its closing audit held nothing;
- a small change was handled as trivial work.

## Revisit When

- A small change is found to have gone beyond the statement it was built from without the closing audit holding it.
- On 2026-10-06 no small change had been built this way on any runtime; a small change later found to have needed a plan reopens this record.

## More Information

Replaces ADR-D-0055 in full; the decision carried here is the same. ADR-D-0055 named the ratified brief of the person directing the work by its place among the sources of authorization; this record names it by what it is. Its line that a small change is a unit of the run its governing brief governs, as a plan is, is carried by ADR-D-0144 ("Each unit of a run is a plan-mode plan or a small change as ADR-D-0147 states"). Source of intent: `docs/coding-agent/briefs/completed/small-change-from-his-word-brief.md`, "Who it is for and why", "The middle size", "A small change and the run" and "Limits". Related: ADR-D-0139 (the sources of authorization), ADR-D-0141 (when a ratified brief authorizes a plan), ADR-D-0134 (the value audit), ADR-D-0144 (a run of units, of which a small change is one).
