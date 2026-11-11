---
status: proposed
adr_type: design
date: 2026-11-11
deciders: ["ebigunso"]
consulted: ["Claude Opus 5.5", "Claude Fable 5.2"]
informed: []
supersedes: ["ADR-D-0066-a-goal-loops-forbidden-set-is-a-criterion-and-its-envelope-is-fixed-before-the-loop-and-never-changed-by-it.md"]
superseded_by: null
depends_on: ["ADR-D-0084-no-goal-loop-starts-without-an-authority-envelope.md"]
---

# ADR-D-0086: A goal loop never changes its own authority envelope

## Context and Problem Statement

Terms used here: a goal loop is the loop of a run in goal mode. The authority envelope is the boundary of a goal loop's autonomy, fixed before the loop starts (ADR-D-0084).

A loop that runs long enough meets its boundary: the way forward it sees lies outside what it may decide. The fork is whether the loop may then move the boundary itself, recording that it did, or whether the envelope stays as it was fixed and any change to it is made by someone other than the loop.

## Decision

- The loop never changes its envelope.
- Renegotiating the envelope is never a loop decision.

## Why

An envelope the loop may amend is no boundary, since the party under goal pressure would be widening its own permissions.

## Rejected Alternatives

- Envelope renegotiation by the loop, with journaling: rejected outright; the party under goal pressure would be widening its own permissions.

## Decision Boundary

Not covered: that a changed envelope is authorized afresh, as a new one is, and by whom (ADR-D-0065, ADR-D-0064); that an envelope exists before the loop starts and what it consists of (ADR-D-0084); how the forbidden set is defined (ADR-D-0085); the protection of the goal condition against change by the loop (ADR-D-0079); what the loop does when it meets its boundary and how a renegotiation is brought about, which goal mode's text states; how a goal run is graded against the value documents (ADR-D-0082).

## Validation

The decision is broken where:

- the envelope a goal loop ran under differed from the one fixed before it started, and the difference was the loop's own doing;
- a loop acted on a widened or reworded envelope that nothing but the loop had authorized.

## Revisit When

- The premise that the engines running goal loops offer no boundary of their own worth relying on no longer holds: platform engines gain native envelope or boundary primitives worth delegating to. On 2026-09-07 none had.

## More Information

Replaces ADR-D-0066 together with ADR-D-0084 and ADR-D-0085: this record holds that the loop never changes its envelope. ADR-D-0066's clause that a changed envelope is authorized afresh is not carried here; ADR-D-0065 holds it. Design: `docs/coding-agent-orchestration-harness/design/goal-mode-design.md`, "Authority envelope". Related: ADR-D-0084 (the envelope), ADR-D-0064 and ADR-D-0065 (who authorizes an envelope, and on what conditions), ADR-D-0079 (the goal condition's protection).
