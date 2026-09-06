---
status: accepted
adr_type: design
date: 2026-09-06
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "GPT-6 Astra"]
informed: []
warrant:
  warranted_by: "without this record, future work would likely demand an ablation before deleting a tool-help mirror, or relax an incident-backed guard because a model 'seems' to behave, or write an ADR per removed file; the three classes look alike in a diff and the evidence each needs is not derivable from ADR-D-0015 alone"
  detected_signals: "cross-boundary evidence-ownership shape (what proof unlocks which removal); rejected alternative likely to be re-proposed (per-removal ADRs, judgment-only guard relaxation); a decider's ruling setting a durable governance default"
  cost_of_violation: "under-evidenced guard relaxation is silent: the model keeps looking careful while a drifted behavior returns (a public contract widened without a question, a shared type worked around without a design alert); over-evidenced redundancy removal freezes dead content in place at per-task token cost"
  cost_of_over_extension: "treating a contract, schema, evidence requirement, or consent gate as 'redundancy' because it is restated somewhere; those are not removable under any tier here, they are deduplicated to one canonical copy and kept"
supersedes: ["ADR-D-0015-remove-obsolete-guidance-as-models-improve.md"]
superseded_by: null
supersession_scope: partial
---

# ADR-D-0018: Evidence tiers for removing harness content

## Context and Problem Statement

ADR-D-0015 requires ablation evidence before removing guidance and asks for an implementation ADR per removal. The 2026-09-06 audit showed that harness content is not one class. Some of it duplicates text that lives elsewhere; some teaches a practice; some pins a behavior that has drifted before. One evidence rule for all three either blocks trivial deletions behind expensive experiments or lets guards go on intuition. The audit's first pass made the second mistake twice; probes caught both.

## Decision Drivers

- Evidence cost must scale with what the content protects: nothing, information, or a behavior.
- A behavior guard's value is only visible when the guard is absent and the model is otherwise clean; a "no harness skills loaded" run is not clean.
- Records of what was removed belong with the evidence; ADRs carry constraints forward.

## Decision

Harness content is classified by what it protects, and each class carries its own evidence obligation before removal or relaxation:

1. **Redundancy** (a mirror of a tool's own help, a worked example that restates its template, a second copy of a canonical statement, an artifact with no consumer): a consumer check, and for canonical statements the surviving copy named. No ablation.
2. **Guidance** (content that teaches a practice or an idiom): ablation under ADR-D-0015 with a pre-registered decision rule.
3. **Guard** (content traced to an incident, a promotion record, or an ADR, or that encodes consent or coordination): before any relaxation, a behavior probe with the guard text absent on a pure baseline where the model reports loaded instructions as "none", plus the same probe with the modified harness loaded. A guard whose probe shows the behavior is native may be relaxed to record-and-surface; one whose probe shows it is not native stays.

Obligations accumulate; they do not rank. Content that is both guidance and guard is separated into its parts first, and each part carries its own obligation; where separation is impossible, both obligations apply. Consent gates, output contracts, schemas, and evidence requirements are never in any removable set; they are deduplicated to one canonical copy and kept.

Removal ledgers (which files, which class, which check) live with the experiment records and the closing plan, not in an ADR. Removal itself never warrants an ADR. Whether any other change warrants one is decided by the ordinary warrant and supersession rules: a change to a class boundary, an evidence obligation, or the authority or behavior a retained guard fixes (for example, which discoveries require confirmation under ADR-D-0017) goes through that route; wording-only calibration of retained content is skill text and does not.

## Considered Options

1. One rule for everything: ablation before any removal (ADR-D-0015 as written).
2. Judgment-only removal with a reviewer check.
3. Classes keyed to what the content protects, with accumulating obligations and probes for guards.

## Decision Outcome

Chosen option: **Classes with accumulating obligations**. Option 1 spends an experiment on deleting a `--help` mirror and still says nothing about guards, which ablation of review quality does not measure. Option 2 is how the audit's first pass proposed relaxing the workaround tripwire and the replan surfacing; probes showed GPT-6 Astra with nothing loaded widens a documented public contract silently and neither model names a cleaner boundary change unprompted. Option 3 makes the cheap case cheap and the risky case evidenced, without letting one kind of proof stand in for another.

### Rejected Alternatives

Per-removal implementation ADRs (ADR-D-0015's recording clause) are rejected: they record history without adding a constraint, and the same facts are in git and the experiment directory. Reopen only if removal records prove unfindable in practice. Accepting "no harness skills loaded" as a baseline is rejected: one unrelated skill in context changed a probe's outcome; the baseline must report "none". A single "higher tier wins" rule was considered and rejected because probes and ablations measure different things; neither substitutes for the other.

## Consequences

- Positive: redundancy cuts proceed on a consumer check; guard relaxations carry probe evidence; guidance removals keep their ablation; ADR count tracks decisions, not deletions.
- Negative / tradeoffs: classifying content is itself a judgment, and separating mixed content is work; a reviewer who disputes a class adds the disputed obligation rather than picking one.

## Decision Boundary

Invariant: no guard is relaxed without a pure-baseline probe and a harness-on probe; no guidance is removed without ADR-D-0015 ablation; obligations accumulate on mixed content; consent gates, contracts, schemas, and evidence requirements are never removed under any class.

Not covered: the probe fixtures, the ablation thresholds, what counts as a consumer check, and the wording of retained content; those are calibrated in experiment records and skill text.

## Measurement Basis

`docs/coding-agent/experiments/frontier-guard-probes/` (records commits `a8fc57a78d6c` and `4ace1fdf5eab`): the pure-baseline method, the discovery probe, sixteen guard-probe cells, five verification cells, and the 2026-09 removal ledger. Single run per cell; enough to sort content into classes, not to size effects.

## Validation

A removal PR names the class per file and links the evidence that class requires; a guard relaxation PR links both probe cells; a disputed class adds the disputed obligation.

## Revisit When

A daily-use model changes: rerun the guard probes before keeping any relaxation, and rerun ADR-D-0015 checks before keeping any guidance removal. A removal that should have been guarded shows up as a real-task miss: reclassify and restore as a guard.

## More Information

Partially supersedes ADR-D-0015 (the per-removal ADR clause and the single evidence rule); its ablation requirement for guidance stands. Companion: ADR-D-0017 (the guard relaxations made under class 3). Removal ledger for 2026-09: `docs/coding-agent/experiments/frontier-guard-probes/README.md`.
