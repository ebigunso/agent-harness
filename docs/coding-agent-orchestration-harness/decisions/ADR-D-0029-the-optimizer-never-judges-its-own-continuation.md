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

# ADR-D-0029: The optimizer never judges its own continuation

## Context and Problem Statement

A goal loop must repeatedly decide whether it is still making progress and whether to continue or escalate. The agent pursuing the goal is under goal pressure, and any criterion loose enough to need judgment gives it room to rationalize continuing. The fork is who makes the continuation judgment: the optimizer itself, a mechanical check over the journal, or an independent party.

## Decision

Continuation is judged by an independent assessor with fresh context that reads only the goal file, the journal, and the gap history, never the optimizer's working context. Its mandate is assessment accuracy, not goal completion. It re-runs the goal condition's gap check itself rather than trusting reported numbers, judges circularity and claimed plateau progress from the journal, and tie-breaks toward escalation: continuation bears the burden of proof.

## Why

A wrong stop costs one human touch while a wrong continuation compounds, and the only party that cannot be trusted to weigh that is the one whose work would stop.

## Rejected Alternatives

- Self-assessment by the optimizer against well-defined criteria: rejected outright; the conflicted party sits in the judge's seat.
- Mechanical stall detection over self-authored journal labels: reopen if journals gain machine-verified structure that wording drift cannot defeat.

## Decision Boundary

Invariant: the assessor is a different dispatch with fresh context, reads the named inputs only, and ties break toward stopping.

Not covered: how the assessor is packaged (ADR-D-0030), its cadence, and its second duty of re-examining the goal itself (ADR-D-0014).

## Validation

- Assessor verdicts cite re-run gap checks, not optimizer-reported numbers.
- No journal entry shows the optimizer recording its own continuation verdict.

## Revisit When

- Platform evaluator hooks become expressive enough to host the trajectory-level mandate natively (none did on 2026-09-07).

## More Information

Replaces ADR-D-0012 together with ADR-D-0030. Design: `docs/coding-agent-orchestration-harness/design/goal-mode-design.md`, pillar 4. What is judged: ADR-D-0011.
