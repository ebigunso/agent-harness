---
status: accepted
adr_type: implementation
date: 2026-09-01
deciders: ["ebigunso"]
consulted: ["Claude Fable 5", "GPT-5.6 Sol", "GPT-5.6 Luna"]
informed: []
warrant:
  warranted_by: "without this record, future work would likely reintroduce stack/security/framework checklist docs on the intuition that cross-cutting review needs them, re-adding context cost the ablation showed buys nothing"
  detected_signals: "rejected alternative likely to be re-proposed; premises likely to expire (model capability is the premise and moves across generations and fleet changes)"
  cost_of_wrong_preservation: "a future fleet regression on cross-cutting review quality would go uncompensated until noticed downstream"
  cost_of_over_extension: "treating the review-latent-risk report contract, the remaining latent-risk defect-class docs, or testing-validation evidence rules as covered by this removal — they were explicitly retained"
supersedes: []
superseded_by: null
supersession_scope: null
implements: ["superseded/ADR-D-0015-remove-obsolete-guidance-as-models-improve--superseded-by-ADR-D-0019.md"]
---

# ADR-I-0005: Remove generic stack, security, web-framework, and latent-risk-performance references

## Context and Problem Statement

The ADR-D-0015 obsolescence sweep (2026-09-01) classified the harness's remaining reference documents by whether they encode model knowledge, contracts, or operational facts. Four `engineering-quality-baselines` references were classified as uniformly generic review-checklist content: `tech-web-frameworks.md` (188 lines), `stack-backend-frontend.md` (158), `security-boundaries.md` (57), and `review-latent-risk-performance.md` (22). Per ADR-D-0015, removal requires ablation evidence against the daily-use fleet (Claude Fable 5, GPT-5.6 Sol, GPT-5.6 Luna).

## Decision

Delete the four references. Keep the hot-path criterion and its report obligation in `review-latent-risk.md` and the reviewer packet template (they are contract), with the per-doc reference removed. Update `SKILL.md` routing accordingly.

## Decision Outcome

Ablation batch 2 (protocol pre-registered before any cell ran): 192 reviews — 3 models × arms A (core-principles only) / B (A + the fixture's home doc) × 16 fixtures × 2 seeds, fixtures drawn from the four docs' own concern lists. On valid fixtures, detection was 22/22 in every cell of every arm: B − A = 0 for every document on every model. The false-positive guard passed — decoy-flag profiles were arm-independent within each model. One fixture (twf-01, hydration mismatch) was invalidated as an authoring error: its framing pinned a server-only component where the planted mechanism cannot occur, and the reviewers' analyses were more precise than the key (Luna arm B stated the invalidation reason verbatim).

Two seeds were used instead of batch 1's three, pre-registered on batch 1's observed zero cross-seed variance; the only cross-seed disagreements in batch 2 occurred on the invalidated fixture and gray-zone decoy cells, confirming the deviation harmless.

## Implementation Impact

Four files removed from `engineering-quality-baselines/references/`; `SKILL.md` category list updated and its removal note extended; `review-latent-risk.md` hot-path routing rewritten as a direct-assessment criterion; `wave-integration/references/reviewer-packet-template.md` hot-path and runtime-compatibility slots repointed to the latent-risk router (the latter fixed a pre-existing wrong reference to the performance doc). Version bumped to 0.12.0.

## Consequences

- Positive: ~425 further reference lines leave the routing surface and context budget.
- Negative / tradeoffs: security review depth now rests entirely on native model capability plus the retained contract docs; a weaker future fleet model would have no security checklist to fall back on until the Revisit check runs.

## Decision Boundary

Invariant: none of the four documents returns without new ablation evidence on the then-current fleet (per ADR-D-0015).

Not covered: the `review-latent-risk-*` defect-class docs other than performance, `review-latent-risk.md` routing and report contract, `core-principles.md`, `architecture-gates.md`, `testing-validation.md`, `test-authoring.md`, `review-rubric.md`, `long-horizon-audit.md` — all retained; the sweep classified them contract, operational, or mixed, and the mixed ones remain candidates for their own future evidence-gated changes.

## Measurement Basis

Experiment records live in git history on the `remove-eqb-generic-refs` branch, commit `e221d34` ("Ablation batch 2 records"), under `docs/coding-agent/experiments/language-guide-ablation/batch2-eqb-generic/`: pre-registered protocol, keys, all 16 fixtures, and adjudicated results including the twf-01 invalidation and the decoy-design lesson (minimal clean diffs invite defensible boundary-hardening claims; future decoys must include the hardening). Records were removed from the working tree after the decision landed; recover from that commit to rerun. Grading by six independent Fable grader agents; disputes adjudicated by the experiment author against raw transcripts.

## Validation

No references to deleted files remain in `plugins/` (grep-verified); harness package validation in CI; review behavior on real PRs is the ongoing check.

## Revisit When

Per ADR-D-0015: material fleet change — a new default model, a weaker tier added, or observed cross-cutting review misses (security especially) in real PRs. Rerun the archived batch-2 protocol (commit `e221d34`) against the new fleet before reintroducing anything.

## More Information

Implements ADR-D-0015. Second application, after ADR-I-0004 (per-language baselines). Companion trim of playwright-cli references landed as PR #46 without an ablation gate (illustrations, not guidance).
