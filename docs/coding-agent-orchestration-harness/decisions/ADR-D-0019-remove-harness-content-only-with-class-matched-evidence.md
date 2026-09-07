---
status: accepted
adr_type: design
date: 2026-09-06
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "GPT-6 Astra"]
informed: []
supersedes: ["superseded/ADR-D-0015-remove-obsolete-guidance-as-models-improve--superseded-by-ADR-D-0019.md"]
superseded_by: null
---

# ADR-D-0019: Remove harness content only with evidence matched to what it protects

## Context and Problem Statement

The harness ships content written to compensate for the limits of the models in use when it was written; capability moves and content does not expire on its own, while every loaded document costs tokens and attention on every task. Content is not one class: some duplicates text that lives elsewhere, some teaches a practice, some pins a behavior that has drifted before. ADR-D-0015 applied one rule to all of it, ablation first and an implementation ADR per removal, which blocked trivial deletions behind experiments and said nothing about guards, where intuition fails silently.

## Decision

Harness content is removed or relaxed only with evidence matched to what the content protects. Content is classified into three classes, and each class carries its own evidence obligation:

- **Redundancy** (a mirror of a tool's own help, a worked example that restates its template, a second copy of a canonical statement, an artifact with no consumer): a consumer check, and for a canonical statement the surviving copy named. No ablation.
- **Guidance** (content that teaches a practice or an idiom): removal only on demonstrated obsolescence, shown by an ablation with a pre-registered decision rule in which the content produces no measurable lift on its own subject matter. Intuition does not count. A demonstrated salience-only lift (the full text and a compressed text help equally) permits compression instead of removal.
- **Guard** (content traced to an incident, a promotion record, or an ADR, or encoding consent or coordination): before any relaxation, a behavior probe with the guard absent on a baseline that reports loaded instructions as "none", and the same probe with the modified harness loaded. A guard whose probe shows the behavior is native may be relaxed to record-and-surface; one whose probe shows it is not native stays.

Obligations accumulate; mixed content is separated first, and where it cannot be, both apply. Consent gates, output contracts, schemas, and evidence requirements are never removable; they are deduplicated to one copy. Removal ledgers live with the experiment records and the closing plan; removal itself never warrants an ADR.

## Why

A duplicate protects nothing worth measuring. An ablation measures review lift and a probe measures behavior; neither substitutes for the other. A baseline with any skill loaded is not a baseline: one unrelated skill in context changed a probe's outcome on 2026-09-06.

## Rejected Alternatives

- Keep guidance indefinitely and bound its cost by routing: routing pays its own overhead and keeps the maintenance surface.
- Compress aging guidance by default: presumes a salience gap that must itself be demonstrated; the ablation of 2026-08-29 showed a control arm with no gap to fill.
- One rule for everything, ablation first (ADR-D-0015): spends an experiment on a help mirror and says nothing about guards.
- Judgment plus reviewer check for guards: two guard relaxations were proposed this way on 2026-09-06 and both were wrong on probe.
- Highest class wins on dispute: the proofs measure different things; a disputed class adds its obligation.
- One implementation ADR per removal: history without a constraint; git and the experiment records hold the same facts. Reopens only if removal records prove unfindable.

## Decision Boundary

Invariant: no guidance removed without ablation; no guard relaxed without both probes; obligations accumulate on mixed content; consent gates, contracts, schemas, and evidence requirements are never removed; reintroducing removed content needs new evidence of the same class.

Not covered: fixtures, thresholds, what counts as a consumer check, and the wording of retained content; those live in experiment records and skill text.

## Validation

A removal PR names the class per file and links the evidence that class requires; a guard relaxation PR links both probe cells; the experiment protocol stays in git history so a check is rerunnable.

## Revisit When

Guidance ablations were run on 2026-08-29 against Claude Fable 5, GPT-5.6 Sol, and GPT-5.6 Luna, and guard probes on 2026-09-06 against Claude Fable 5.1 and GPT-6 Astra. Replacing any of those models with another: rerun the guard probes before keeping any relaxation, and rerun the archived ablations before keeping any guidance removal. A removal that should have been guarded shows up as a real-task miss: reclassify and restore it as a guard.

## More Information

Replaces ADR-D-0015 in full. Records: guidance ablations under `docs/coding-agent/experiments/language-guide-ablation/` in git history (ADR-I-0004 and ADR-I-0005, retired into this record on 2026-09-07 and kept under `superseded/`); guard probes and the PR #57 removal ledger under `docs/coding-agent/experiments/frontier-guard-probes/`. Guard relaxations made under the guard class: ADR-D-0018.
