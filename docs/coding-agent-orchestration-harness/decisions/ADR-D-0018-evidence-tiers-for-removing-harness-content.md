---
status: accepted
adr_type: design
date: 2026-09-06
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "GPT-6 Astra"]
informed: []
warrant:
  warranted_by: "without this record, future work would likely demand an ablation to delete a tool-help mirror, relax an incident-backed guard on intuition, or write an ADR per removed file"
  detected_signals: "evidence-ownership shape; rejected alternatives likely to be re-proposed; a decider's ruling setting a durable default"
  cost_of_violation: "an under-evidenced guard relaxation is silent: the model keeps looking careful while a drifted behavior returns"
  cost_of_over_extension: "treating a contract, schema, evidence requirement, or consent gate as redundancy because it is restated; those are deduplicated, never removed"
supersedes: ["ADR-D-0015-remove-obsolete-guidance-as-models-improve.md"]
superseded_by: null
supersession_scope: partial
---

# ADR-D-0018: Evidence classes for removing harness content

## Context and Problem Statement

ADR-D-0015 treats every removal alike: ablation first, and an implementation ADR per removal. Harness content protects different things: nothing (a duplicate or a help mirror), information (guidance), or a behavior (a guard). One kind of proof does not fit all three, and guards are where intuition fails silently.

## Decision

Content is classified by what it protects, and each class has its own evidence obligation before removal or relaxation:

- **Redundancy**: a consumer check; for a canonical statement, the surviving copy named. No ablation.
- **Guidance**: ablation under ADR-D-0015 with a pre-registered rule.
- **Guard** (traced to an incident, a promotion record, or an ADR, or encoding consent or coordination): a behavior probe with the guard absent on a baseline that reports loaded instructions as "none", and the same probe with the modified harness loaded, before any relaxation.

Obligations accumulate; mixed content is separated first, and where it cannot be, both apply. Consent gates, output contracts, schemas, and evidence requirements are never removable; they are deduplicated to one copy. Removal ledgers live with the experiment records and the closing plan; removal itself never warrants an ADR. Any other change goes through the ordinary warrant test.

## Why

A probe measures behavior and an ablation measures review lift; neither substitutes for the other, and a duplicate protects nothing worth measuring. A baseline with any skill loaded is not a baseline: one unrelated skill in context changed a probe's outcome.

## Rejected Alternatives

- One rule for everything (ADR-D-0015 as written): spends an experiment on a help mirror and says nothing about guards.
- Judgment plus reviewer check for guards: this is how two guard relaxations were proposed and both were wrong on probe.
- Highest class wins on dispute: the proofs measure different things, so a disputed class adds its obligation instead.
- Per-removal ADRs: history without a constraint; reopens only if removal records prove unfindable.

## Decision Boundary

Invariant: no guard relaxed without both probes; no guidance removed without ablation; obligations accumulate; consent gates, contracts, schemas, and evidence requirements are never removed.

Not covered: fixtures, thresholds, what counts as a consumer check, and the wording of retained content.

## Validation

A removal PR names the class per file and links the evidence that class requires; a guard relaxation PR links both probe cells.

## Revisit When

Checked 2026-09 against Claude Fable 5.1 and GPT-6 Astra. A change in the daily-use fleet: rerun the guard probes before keeping any relaxation. A removal that should have been guarded shows up as a real-task miss: reclassify and restore it as a guard.

## More Information

Partially supersedes ADR-D-0015 (the per-removal ADR clause and the single evidence rule); its ablation requirement for guidance stands. Records for the 2026-09 removals and probes: `docs/coding-agent/experiments/frontier-guard-probes/`.
