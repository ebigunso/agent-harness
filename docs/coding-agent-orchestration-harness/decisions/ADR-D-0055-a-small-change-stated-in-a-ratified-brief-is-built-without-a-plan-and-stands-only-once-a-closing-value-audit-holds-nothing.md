---
status: proposed
adr_type: design
date: 2026-10-06
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1"]
informed: []
supersedes: []
superseded_by: null
depends_on: ["ADR-D-0040-non-trivial-work-is-authorized-only-by-the-person-directing-the-work-or-by-that-persons-ratified-brief.md", "ADR-D-0041-a-ratified-brief-authorizes-a-plan-only-through-a-closed-plan-review-and-a-value-audit-that-holds-nothing-above-the-run.md", "ADR-D-0052-the-orchestrator-never-grades-its-own-run-and-its-reading-is-compared-only-after-the-grades-are-fixed.md"]
---

# ADR-D-0055: A small change the person directing the work stated in a ratified brief is built without a plan, a plan review or a plan-draft audit; it keeps the review of the change and one closing value audit, which holds it where it went beyond the statement, and nothing of it is published or reported as done before that audit holds nothing

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. The Orchestrator session is a session that holds the Orchestrator role (ADR-D-0020) and plans, dispatches and reports the work.

The harness knows two sizes of work. Trivial work is handled directly, but only when it changes no behaviour; everything else is a plan, which takes a plan review, a plan-draft audit, the build, the review of the change, the closing audit, a branch and a pull request. ADR-D-0040 names the ratified brief, carried to the work through the value audit, as the second source of authorization, and ADR-D-0041 states the conditions under which it authorizes a plan. A change the person directing the work states always changes behaviour, so it is never trivial work, and with a plan as the only other unit even a one-sentence change takes the whole suite. The fork is whether such a change, when it is small, needs a plan at all, and what then stands between it and being reported as done.

## Decision

- The second source authorizes a small change without a plan, a plan review or a plan-draft audit when the person directing the work stated the change in a governing brief, or in an amendment to it, whose ratification reached the session on the terms ADR-D-0041 states for a plan; that person's statement in the brief stands in place of the plan.
- A small change keeps two checks: the review of the change, and one closing value audit that checks that what was built is what the statement said and nothing more. Where the change went beyond the statement, the audit holds it.
- Nothing of the change is published or reported as done before that audit holds nothing.
- Whether a change is small is the Orchestrator's call; the guard on that call is the closing audit.

## Why

For a change this small the full suite is out of proportion, and the statement of the person directing the work in the brief is the plan. This knowingly loosens the gate for that class of change; the closing audit, which holds whatever went beyond the statement, guards the Orchestrator's call that a change is small.

## Rejected Alternatives

- A small change stated by the person directing the work takes a plan, its review and its draft audit like any other change that alters behaviour: it lost because for a one-sentence change that suite is out of proportion; exercising the guards is a reason to test them, not a reason for the harness to behave this way; reopen if small changes are found to have gone beyond the statement without the closing audit holding them.
- A small change keeps a plan document in a short form and drops only its review and its draft audit: rejected outright; the plan would repeat the statement it is built from.

## Decision Boundary

Invariant: a small change stated by the person directing the work in a governing brief whose ratification reached the session is built without a plan, a plan review or a plan-draft audit; it keeps the review of the change and one closing value audit, which holds it where it went beyond the statement; nothing of it is published or reported as done before that audit holds nothing; whether a change is small is the Orchestrator's call, guarded by that audit; the Decision list states the rest.

Not covered: trivial work and its tripwires (ADR-D-0040 leaves them uncovered); how the Orchestrator judges that a change is small; how a small change is recorded, and the branch and pull request it is published on; goal mode; the conditions under which the second source authorizes a plan (ADR-D-0041); the audit's procedure and the dispatch wording (ADR-D-0052).

## Validation

- A small change built under the second source records where the statement stands in the brief, the ratification as it reached the session, the result of the review of the change, and the closing audit's dispatch and verdict; nothing of it is published or reported as done before a verdict that holds nothing.

## Revisit When

- A small change is found to have gone beyond the statement it was built from without the closing audit holding it.
- On 2026-10-06 no small change had been built this way on any runtime; a small change later found to have needed a plan reopens this record.

## More Information

Source of intent: `docs/coding-agent/briefs/active/small-change-from-his-word-brief.md`, "Who it is for and why", "The middle size" and "Limits". Related records: ADR-D-0040 (the sources of authorization), ADR-D-0041 (when a ratified brief authorizes a plan), ADR-D-0052 (the value audit), ADR-D-0051 (a run of plans, from which a small change is excepted).
