---
status: superseded
adr_type: design
date: 2026-08-29
deciders: ["ebigunso"]
consulted: ["Claude Fable 5"]
informed: []
warrant:
  warranted_by: "without this record, future work would likely treat shipped guidance documents as permanent fixtures, accumulating context-token cost and maintenance surface for content that newer models already carry natively"
  detected_signals: "a decider's ruling setting a durable governance default; premises likely to expire (model capability advances continuously, and each fleet change re-poses the question)"
  cost_of_violation: "guidance keeps accreting without an obsolescence path; every review-shaped task pays growing context cost for zero lift, and the harness drifts toward being tuned for models no longer in use"
  cost_of_over_extension: "deleting guidance on intuition alone, or treating output contracts, repository-specific policy, and evidence requirements as 'guidance' — those encode agreements between agents and reviewers, not model knowledge, and no capability level makes them redundant"
supersedes: []
superseded_by: ADR-D-0020-remove-harness-content-only-with-class-matched-evidence.md
supersession_scope: full
---

# ADR-D-0015: Remove obsolete guidance as models improve

> Retired on 2026-09-06. Replaced in full by ADR-D-0020, which keeps the ablation principle and adds evidence classes for redundancy and guards; the per-removal implementation-ADR clause is gone.

## Context and Problem Statement

The harness ships guidance documents (idiom baselines, checklists, routing rules) written to compensate for the capability limits of the models in use at authoring time. Model capability advances; guidance does not expire on its own. Content a current model already applies natively costs context tokens in every task that loads it, competes for attention with the change under review, and adds maintenance surface — while its presence keeps signaling that it is needed. The harness needs a standing decision on what to do with guidance that capability growth has made redundant, and on when to check.

## Decision Drivers

- Context budget and attention are per-task costs paid by every loaded document, justified only by measurable behavior change.
- Guidance quality claims should rest on evidence against the actual fleet, not on intuition in either direction.
- The fleet changes over time in both directions (stronger defaults, cheaper weak tiers), so obsolescence is not a one-time question.

## Decision

When guidance is demonstrated obsolete for the current daily-use model fleet, remove it rather than keep, compress, or replace it. Obsolescence is demonstrated by ablation evidence — the guidance shows no measurable behavior lift on its own subject matter with the guidance absent — not by intuition. Preferably run this obsolescence check whenever a model used daily is replaced by a better alternative; a fleet change in the weaker direction instead reopens previously removed guidance (see Revisit When). Each concrete removal is recorded as an implementation ADR citing its evidence.

## Considered Options

1. Keep guidance indefinitely once shipped; rely on progressive-disclosure routing to bound its cost.
2. Compress aging guidance to short checklists instead of removing it.
3. Remove guidance when ablation shows no lift on the current fleet, rechecking on fleet upgrades.

## Decision Outcome

Chosen option: **Remove on demonstrated obsolescence, recheck on fleet upgrades**. Routing (option 1) still pays the routing overhead itself and keeps the maintenance surface. Compression (option 2) presumes a salience gap that must itself be demonstrated; where an ablation control arm shows no gap, a compressed doc has nothing to fix. The first application (ADR-I-0004) tested both alternatives directly and both showed zero lift.

### Rejected Alternatives

Keeping guidance "just in case" is rejected because the cost is paid on every task while the benefit is hypothetical; the reopening path in Revisit When is the safety valve that makes removal reversible. Compression is rejected as a default but remains available where an ablation actually shows salience-only lift (guide helps, compressed version helps equally).

## Consequences

- Positive: the harness tracks the capability of the fleet it actually runs on; context budget concentrates on documents that change behavior.
- Negative / tradeoffs: each check costs an ablation run; removed guidance leaves no compensation in place if a weaker model quietly enters daily use before anyone reruns the check.

## Decision Boundary

Invariant: guidance removal under this ADR requires ablation evidence against the current daily fleet; removal on intuition alone is not covered by this decision. Reintroducing removed guidance likewise requires new evidence.

Not covered: output contracts, report schemas, repository-specific policy, and evidence requirements — these encode agreements between agents, reviewers, and tooling rather than model knowledge, and are not "guidance" in this ADR's sense. Also not covered: the specific ablation methodology, which each implementation ADR documents for its own check.

## Validation

Each removal lands as an implementation ADR citing its evidence and preserving the experiment protocol in git history so the check is rerunnable. Reviews of guidance-removal PRs verify the evidence exists and the removal scope matches it.

## Revisit When

A model used daily is replaced or a new tier is added. Better alternative: run the obsolescence check across shipped guidance. Weaker or unknown alternative: rerun the archived checks for previously removed guidance before assuming the removals still hold.

## More Information

First implementation: ADR-I-0004 (per-language baseline references).
