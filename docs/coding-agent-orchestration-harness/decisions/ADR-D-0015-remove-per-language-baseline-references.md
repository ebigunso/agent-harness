---
status: accepted
adr_type: design
date: 2026-08-29
deciders: ["ebigunso"]
consulted: ["Claude Fable 5", "GPT-5.6 Sol", "GPT-5.6 Luna"]
informed: []
warrant:
  warranted_by: "without this record, future work would likely reintroduce per-language baseline reference docs on the intuition that models need idiom checklists, re-adding token cost and maintenance surface the ablation showed buys nothing"
  detected_signals: "rejected alternative likely to be re-proposed; premises likely to expire (model capability is the premise and it moves in both directions across model generations and fleet changes)"
  cost_of_wrong_preservation: "if a future fleet model regresses on language-level review quality, keeping this removal in force silently lowers review depth until the regression is noticed downstream"
  cost_of_over_extension: "reading this as license to delete other reference categories (latent-risk routing, security boundaries, validation/evidence contracts) that were explicitly out of the experiment's scope"
supersedes: []
superseded_by: null
supersession_scope: null
---

# ADR-D-0015: Remove per-language baseline references from engineering-quality-baselines

## Context and Problem Statement

The `engineering-quality-baselines` skill shipped four per-language baseline references
(`language-rust.md`, `language-typescript-javascript.md`, `language-python.md`,
`language-go.md`) plus a routing document (`language-gates.md`) with a four-level
progressive-disclosure model for deciding which to load. These docs date from a period
when frontier models needed idiom and anti-pattern checklists to review reliably. Model
capability has since advanced; every loaded reference costs context tokens in every
review-shaped task, and unneeded guidance competes for attention with the change under
review. The question was empirical: do these docs still change reviewer behavior on the
fleet actually used for day-to-day coding (Claude Fable 5, GPT-5.6 Sol, GPT-5.6 Luna)?

## Decision Drivers

- Context-token cost and routing overhead paid on every non-trivial change.
- Suspicion that guidance content is fully absorbed by current frontier models.
- Fleet heterogeneity: a doc is deletable only if redundant for the weakest fleet model.
- Maintenance burden of keeping four language docs plus a router current.

## Decision

Delete the four per-language baseline references and `language-gates.md` from
`engineering-quality-baselines`, and remove the progressive-disclosure routing levels
from `SKILL.md`. Do not replace them with a compressed or cross-language substitute.

## Considered Options

1. Keep all five documents as shipped.
2. Compress each language doc to a short checklist (salience-only hypothesis).
3. Replace all four with a single cross-language boundary-modeling reference.
4. Delete outright with no replacement.

## Decision Outcome

Chosen option: **Delete outright**. A two-stage ablation (2026-08-28/29) tested the
alternatives directly. Stage 0 (regeneration probes) showed partial unprompted recall of
the docs' content (Rust worst at 54–68% across the fleet), which motivated testing
options 2–4. Stage 1 (planted-defect review ablation, Rust block: 324 reviews, 3 models ×
3 arms × 12 fixtures × 3 seeds) found 100% detection of all planted defects in every
cell — including the no-guide control arm and including the architectural defects the
models never volunteer in the abstract. Guide lift and boundary-doc lift were both
exactly zero, with no false-positive regression between arms. Rust was run first because
it was the worst Stage 0 regenerator; with zero lift there, the weaker-regeneration
argument for the other languages collapses.

### Rejected Alternatives

Compression (option 2) and the cross-language boundary-modeling doc (option 3) were both
rejected because the control arm left no gap for them to fill: the pre-registered decision
rule (protocol-v2) selects "delete, adopt nothing" when the full guide itself shows less
than 10pp lift. Option 3 remains the first candidate to re-propose if the Revisit
condition fires, since Stage 0 located the models' abstract-recall gaps precisely in its
content (transport-vs-domain separation, typed domain modeling, pure-logic/IO separation);
the drafted doc is preserved in the experiment records.

## Consequences

- Positive: every review-shaped task drops the language-doc token load and the L0–L3
  routing decision; five documents leave the maintenance surface.
- Negative / tradeoffs: if a weaker model joins the fleet, no language baseline exists to
  compensate; the experiment tested review of small single-defect diffs under an explicit
  review framing, not large mixed diffs or generation-time behavior.

## Decision Boundary

Invariant: no per-language baseline reference returns to this skill without new ablation
evidence showing detection lift on the then-current fleet. This ADR covers only the five
deleted documents.

Not covered: `tech-web-frameworks.md` (untested, retained), `core-principles.md`, the
`review-latent-risk-*` family, security/validation/test references, and the evidence-note
output contract — all explicitly outside the experiment's scope.

## Measurement Basis

Experiment records: `docs/coding-agent/experiments/language-guide-ablation/` — Stage 0
regeneration results per model (`stage0/results-{fable,sol,luna}.yaml`, cross-model
`stage0/summary.md`), pre-registered protocol (`stage1/protocol-v2.md`, decision rule
fixed before any Stage 1 cell ran), fixtures and keys (`stage1/fixtures/`, `stage1/keys/`),
and the Rust block outcome (`stage1/results-rust.yaml`). Known limits recorded there:
ceiling effect in the control arm, two decoy fixtures invalidated as authoring errors,
key author also graded (Stage 0) with independent grader agents used for Stage 1.

## Validation

`SKILL.md` contains no references to deleted files; harness package validation passes;
review behavior on real PRs is the ongoing check (see Revisit When).

## Revisit When

The fleet's day-to-day coding models change materially — a new default model, a weaker
tier added for cost, or observed language-idiom misses in real reviews. Any of these
reopens the question; rerun the archived Stage 1 protocol against the new fleet before
reintroducing anything.

## More Information

Experiment directory: `docs/coding-agent/experiments/language-guide-ablation/`.
