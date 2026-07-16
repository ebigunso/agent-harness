---
status: accepted
adr_type: design
date: 2026-07-16
deciders:
  - ebigunso
consulted:
  - Claude Fable 5
informed: []
supersedes: []
superseded_by: null
---

# ADR-D-0014: The Assessor Re-Examines Goal Validity, Not Only Progress

## Context and Problem Statement

A goal-mode loop can make perfect progress toward a goal that should no longer be pursued. Long horizons magnify this: requirements shift, mid-run evidence reveals the goal was framed on a wrong assumption, or the stated condition turns out to reward an outcome nobody wants. In plan mode, direction is implicitly re-checked at every human touchpoint; goal mode removes those touchpoints, so nothing re-checks direction unless the duty is explicitly assigned. The optimizer cannot carry it — an agent optimizing a goal is the least likely party to question that goal, for the same conflict-of-interest reason it cannot judge its own stall.

The most common error of a capable engineer is optimizing a thing that should not exist; a goal loop automates that error at scale unless goal validity is examined by someone other than the goal's pursuer.

## Decision Drivers

- Efficient pursuit of a wrong goal is a worse failure than a stall, and harder to notice from inside the loop.
- Goal questioning must be structurally assigned; it does not happen by default in a self-driving loop.
- Goal changes are direction decisions that belong to the goal's owner (the user), never to the loop.
- The examination must be grounded in evidence the loop has produced, not speculation.

## Decision

Goal validity re-examination is a first-class, co-equal duty of the independent assessor (ADR-D-0012), performed at every assessment alongside trajectory assessment. The assessor asks, from fresh context and the run's own evidence:

- Do the requirements behind this goal still hold — is the consumer of the outcome still real, and has anything in the journal falsified the goal's founding assumptions?
- Is the goal condition still measuring what the user meant — or has the run revealed that satisfying the stated condition would not deliver the intended outcome (a framing-level gaming risk, distinct from tampering with the condition's invariants)?
- Should the goal be re-scoped, split, or abandoned in light of what the run has learned — applying the ordered engineering discipline recorded in `engineering-quality-baselines/references/long-horizon-audit.md`: question the requirements before anything else, and never keep optimizing a thing whose existence is unjustified?

The outcome of a failed validity examination is a goal-challenge escalation: the loop stops (the ask-now level — a successful termination by design) and the challenge is surfaced to the user with the evidence that prompted it. The loop never re-scopes, reframes, or abandons a goal autonomously; challenges are surfaced to the goal's owner, mirroring the harness rule that requirement challenges are surfaced, never silently acted on.

## Considered Options

1. No explicit validity duty — rely on the user noticing a wrong goal at the retrospective.
2. The optimizer self-questions the goal on a cadence.
3. Goal validity re-examination as a co-equal assessor duty, with goal-challenge escalation to the user as its only outcome.

## Decision Outcome

Chosen option: **Option 3**.

Option 1 discovers a wrong goal after the run's cost is sunk — the retrospective can revert changes but not spent effort. Option 2 assigns the question to the party structurally motivated to answer "yes, continue." Option 3 places the question with the uninvested party that already examines the run's evidence, and routes the answer to the only party entitled to change direction.

## Consequences

### Positive

- The worst goal-mode failure — efficiently reaching a wrong destination — has a named detector and a defined stop.
- Mid-run evidence that falsifies the goal's premise becomes an escalation trigger instead of an ignored journal footnote.
- The user's goal ownership is preserved structurally: direction changes always pass through a human moment.

### Negative / Tradeoffs

- Validity examination is judgment-heavy and can produce false challenges; the cost is one human touch per challenge, consistent with the burden-of-proof asymmetry (ADR-D-0012).
- A subtle wrong goal whose evidence never surfaces in the journal remains undetectable until retrospective; the duty improves the odds, it does not guarantee detection.

## Validation

- Every assessment record contains a validity verdict, not only a progress verdict.
- Goal-challenge escalations cite journal evidence for the challenged assumption.
- No goal file shows autonomous mid-run changes to its condition, scope, or framing.

## Revisit When

- Trials show validity challenges are so frequent they indicate a weakness in goal construction (then strengthen the pre-loop condition checklist instead).
- Trials show wrong goals surviving to retrospective despite the duty (then the examination questions need sharpening or the cadence needs tightening).

## More Information

- `docs/coding-agent-orchestration-harness/design/goal-mode-design.md` (pillar 4)
- ADR-D-0012 (the assessor carrying this duty), ADR-D-0011 (condition-level invariant protection — the tampering case this ADR's framing-level case complements)
