---
status: superseded
adr_type: design
date: 2026-11-07
deciders: ["ebigunso"]
consulted: ["Claude Opus 5.5"]
informed: []
supersedes: ["ADR-D-0027-the-forbidden-set-is-a-criterion-ratified-before-the-loop--superseded-by-ADR-D-0066.md"]
superseded_by: ../ADR-D-0084-no-goal-loop-starts-without-an-authority-envelope.md
---

# ADR-D-0066: A goal loop's forbidden set is a criterion and its envelope is fixed before the loop and never changed by it

Retired on 2026-11-14. Replaced by ADR-D-0084, ADR-D-0085 and ADR-D-0086.

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. The authority envelope is the boundary of a goal-mode loop's autonomy.

A goal-mode loop acts autonomously between human touchpoints, so the boundary of its autonomy has to exist before the loop takes any step. The fork is how the boundary is expressed, as a list of forbidden actions, which rots as tools and kinds of action appear, or as a criterion new actions are judged against; and whether the loop may change it once it runs. Who authorizes the envelope differs with whether a ratified brief governs the run (ADR-D-0064), so the boundary's form and its fixity have to hold whichever authority stands behind it.

## Decision

- No goal loop starts without an authority envelope: a decision scope, what the loop may change freely, and a forbidden set.
- The forbidden set is defined by one criterion, not a list: any action that is irreversible or outward-facing is outside the envelope, and a new kind of action is judged against the criterion.
- The envelope is fixed before the loop starts and the loop never changes it. Renegotiating it is never a loop decision; a changed envelope is authorized afresh, as a new one is.

## Why

A list of forbidden actions is silently incomplete the day a new tool appears, while a criterion keeps judging actions nobody enumerated; and an envelope the loop may amend is no boundary, since the party under goal pressure would be widening its own permissions. Who authorizes the envelope differs with whether a ratified brief governs the run, so the record leaves it out and the boundary holds whoever authorizes it.

## Rejected Alternatives

- An enumerated forbidden-action list: it lost because a list is incomplete the day a new tool appears; reopen if platforms gain a native, complete action taxonomy the harness can bind to.
- Envelope renegotiation by the loop, with journaling: rejected outright; the party under goal pressure would be widening its own permissions.

## Decision Boundary

Invariant: no goal loop starts without an envelope; its forbidden set is a criterion; the envelope is fixed before the loop starts and the loop never changes it.

Not covered: who authorizes the envelope and on what conditions (ADR-D-0064, ADR-D-0065); the example action classes named as illustrations, how the envelope is recorded, how borderline judgements are journaled, and what happens at the boundary (escalation levels), which goal mode's text states; how a goal run is graded against the value documents (ADR-D-0063).

## Validation

- Every goal carries its decision scope and its forbidden-set criterion before the loop starts.
- A forbidden-class action taken autonomously is a critical defect; a change to the envelope during the run without fresh authorization is an envelope violation.

## Revisit When

- The criterion is found ambiguous for a recurring kind of action in a way that naming that kind as an illustration does not settle.
- Platform engines gain native envelope or boundary primitives worth delegating to; on 2026-09-07 none had.

## More Information

Replaces ADR-D-0027 in full: everything it decided is carried except that the person directing the work ratifies the envelope, which this record leaves to ADR-D-0064 and ADR-D-0065. Source of intent for leaving it out: the brief "A quiet Orchestrator session under a brief" (`docs/coding-agent/briefs/completed/quiet-orchestrator-session-brief.md`), "Directed during the run". Design: `docs/coding-agent-orchestration-harness/design/goal-mode-design.md`, "Authority envelope". Related: ADR-D-0064 (who authorizes non-trivial work), ADR-D-0065 (when a ratified brief authorizes a goal envelope), ADR-D-0063 (the value audit in a goal run), ADR-D-0011 and ADR-D-0074 (progress and stall), ADR-D-0029 (who judges continuation).
