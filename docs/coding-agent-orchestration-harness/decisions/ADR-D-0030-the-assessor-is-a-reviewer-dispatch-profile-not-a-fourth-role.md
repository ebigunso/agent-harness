---
status: proposed
adr_type: design
date: 2026-09-07
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1"]
informed: []
supersedes: ["ADR-D-0012-independent-in-loop-assessor.md"]
superseded_by: null
---

# ADR-D-0030: The assessor is a Reviewer dispatch profile with a fixed, journaled template, not a fourth role

## Context and Problem Statement

The independent assessor (ADR-D-0029) has to be packaged somewhere. A fourth named role would put its mandate into runtime instruction blocks, which are enforced above thread content, but it adds replicated instruction blocks across three runtimes, role-map and permission entries, and it does not solve the starvation case, since the loop controls when any assessor is dispatched. The fork is a new role versus a dispatch profile of the existing Reviewer role.

## Decision

The assessor is a Reviewer-role dispatch profile. Its mandate lives in the goal-mode skill reference, versioned and immutable during the run, never in dispatch prose. The dispatch template is fixed and minimal, and the actual dispatch text is journaled verbatim, so any framing beyond the template is a visible envelope violation at retrospective. Assessment cadence compliance is asserted in the completion report and verified by the pre-merge reviewer against the journal, so a starved assessor invalidates the report. A fourth named role is the recorded upgrade path if dispatcher bias leaks through the fixed template.

## Why

The dispatch profile's only subversion surface is the dispatcher's wording, and template deviation inside an append-only journal is as detectable as not dispatching at all, so the fourth role's extra parts buy protection against a failure the journal already exposes.

## Rejected Alternatives

- A fourth named assessor role with the mandate in instruction blocks: reopen if retrospectives find dispatcher framing effects despite the fixed template; this is the upgrade path, not a rejected idea.
- Mandate carried in dispatch prose: rejected outright; it is the surface being defended.

## Decision Boundary

Invariant: the mandate is in the reference, the dispatch text is fixed and journaled, and cadence compliance is verified at the merge gate.

Not covered: the cadence schedule, the three hardenings' exact wording, and the template text, which the goal-mode reference owns.

## Validation

- Journaled dispatch texts match the fixed template across a goal run.
- The pre-merge reviewer verifies the cadence assertion against the journal.

## Revisit When

- Retrospectives find dispatcher framing effects despite the fixed template (promote to the fourth role).
- Runtimes gain a way to bind a mandate to a dispatch without a named role (none on 2026-09-07).

## More Information

Replaces ADR-D-0012 together with ADR-D-0029. Design: `docs/coding-agent-orchestration-harness/design/goal-mode-design.md`, pillar 4. Role identities: ADR-D-0003. Merge gate: ADR-D-0031.
