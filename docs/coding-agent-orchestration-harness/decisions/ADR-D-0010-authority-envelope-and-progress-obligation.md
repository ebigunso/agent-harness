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

# ADR-D-0010: Authority Envelope With Irreversibility Criterion And Progress Obligation

## Context and Problem Statement

A goal-mode loop decides autonomously between human touchpoints, so the boundary of its autonomy must be defined before the loop starts. Two sub-problems need durable answers: which actions the loop may never take on its own, and what stops a loop that keeps consuming resources without getting closer to its goal. Enumerated forbidden-action lists rot as tooling grows, and resource budgets (tokens, wall-clock, turn counts) are consumption-rate proxies that shift with every model release and platform change.

## Decision Drivers

- Autonomy boundaries must not rot as new tools and action types appear.
- The runaway defense must track the actual failure mode and stay valid across model and platform changes.
- Boundary definitions must be negotiated once, up front, and stay immutable during the run.
- Vague mechanisms invite both over-blocking and rationalized continuation.

## Decision

Every goal is accepted only with a user-ratified authority envelope containing:

- decision scope: paths, components, and operation classes the loop may change freely;
- the forbidden set, defined by the irreversibility criterion as a class, not a list: any action that is irreversible or outward-facing (merge, deploy, force-push, data deletion, publishing, external-service mutation) is outside the envelope; new action types are judged against the criterion;
- a progress obligation as the primary runaway defense: the loop continues only while it demonstrably reduces expected distance to the goal, and a stall triggers an ask-now escalation — the goal-mode escalation level at which the loop stops and waits for the user, which the design treats as a successful termination rather than a failure. Resource ceilings (wall-clock, cost) may optionally be set by the user as coarse backstops but are never the load-bearing mechanism, because consumption rates are model- and platform-dependent while "continuing without learning" is not.

The envelope is recorded in the goal file and is immutable during the run; renegotiation is a human moment.

## Considered Options

1. Enumerated forbidden-action lists plus mandatory resource budgets.
2. Irreversibility criterion for the forbidden set plus mandatory resource budgets.
3. Irreversibility criterion plus progress obligation with stall escalation; resource ceilings optional and non-load-bearing.

## Decision Outcome

Chosen option: **Option 3**.

Asking what failure mode budgets were meant to stop exposed that runaway spend, thrash, and unattended divergence share one core — continuing without progress — and that absolute resource caps are a poor proxy for it. Stall detection tracks the failure mode itself and survives model selection changes and new frontier releases that alter consumption rates.

## Consequences

### Positive

- The forbidden set does not rot: new tools are judged by the criterion, not matched against a stale list.
- The runaway defense is model-agnostic and self-calibrating to the work.
- Users are not forced to guess budget numbers that depend on unknowable consumption rates.

### Negative / Tradeoffs

- Stall detection requires trustworthy progress judgment, which needs independent assessment (ADR-D-0012) to resist optimizer rationalization.
- Borderline actions require criterion judgment rather than list lookup; judgment calls are journaled.
- Without mandatory hard ceilings, a slowly-progressing loop can legitimately run long; the optional backstop exists for users who care.

## Validation

- Every goal file contains scope, forbidden-set acknowledgment, and the progress obligation before the loop starts.
- Escalations at the envelope boundary appear in the journal; forbidden-class actions taken autonomously are treated as critical defects.
- Stall escalations reference concrete gap history rather than narrative claims.

## Revisit When

- Trials show the irreversibility criterion is ambiguous for a recurring action class (then name that class explicitly).
- Stall detection systematically fires too early or too late for a category of goals.
- Platform engines gain native envelope or boundary primitives worth delegating to.

## More Information

- `docs/coding-agent-orchestration-harness/design/goal-mode-design.md` (pillar 1)
- ADR-D-0011 (how progress and stall are defined), ADR-D-0012 (who judges them)
