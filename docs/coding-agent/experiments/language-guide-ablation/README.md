# Language Guide Ablation

Does `engineering-quality-baselines/references/language-*.md` still change agent behavior,
or has foundation-model capability absorbed it?

## Question under test

Three outcomes are possible, and the experiment is built to separate them:

| Outcome | Meaning | Action |
|---|---|---|
| **Obsolete** | Model applies the guidance without being told | Delete the refs |
| **Salience-only** | Model knows it but does not check it unprompted | Replace with the compressed arm C text |
| **Load-bearing** | Guidance measurably changes review output | Keep as-is |

The distinction that matters is **knowledge vs. attention**. A guide can be fully redundant
as information and still earn its tokens by making the model spend attention on error
wrapping instead of on the feature.

## Scope

In scope: `language-go.md`, `language-python.md`, `language-rust.md`,
`language-typescript-javascript.md`, and (separately) `language-gates.md`.

Explicitly out of scope:

- The routing note / evidence template in `SKILL.md` — an *output contract*, not knowledge.
  Models do not spontaneously emit that format and no capability boost changes that.
- The `review-latent-risk-*` family — far more specific than the language refs, different
  obsolescence profile, should not be swept up in this result.

## Stage 0 — Regeneration probe

Cheap filter. Ask a clean model to produce the guidance unprompted, diff against the real doc.

    python score_stage0.py stage0/results.yaml

Decision:

- **>= 80% bullet coverage** -> prima facie obsolescence, proceed to Stage 1
- **~50% coverage** -> the docs carry real signal; stop suspecting them

Caveat: regeneration proves *knowledge*, not *in-situ application*. This stage cannot
conclude anything on its own — it only decides whether Stage 1 is worth running.

> **AMENDED 2026-08-28** after Stage 0 completed (see `stage0/summary.md`): Stage 1 now
> follows `stage1/protocol-v2.md` — arms A/B/D (C conditional), a pre-registered
> mechanics-vs-architectural fixture split, per-model runs across Fable/Sol/Luna, and the
> old Stage 2 tier sweep is dropped. The sections below describe the original design and
> are kept for provenance; where they conflict, protocol-v2 wins.

## Stage 1 — Ablation on planted-defect fixtures

48 fixtures: 4 languages x (8 planted defects + 4 clean decoys). Every planted defect is
drawn from the guide's own "Common anti-patterns" list, so this is the most favorable
possible test for the guide. A null result here is therefore decisive.

Clean decoys measure false-positive noise — a guide that lifts detection by also inflating
spurious findings has not helped.

Arms (same fixtures, blind-graded against `stage1/keys/`):

| Arm | Context loaded |
|---|---|
| A | `core-principles.md` only |
| B | `core-principles.md` + full `language-<lang>.md` (current state) |
| C | `core-principles.md` + `stage1/arms/compressed-<lang>.md` |

Run >= 3 seeds per cell. Single-shot review variance will otherwise swamp the effect size
being measured.

### Pre-registered decision rule

Fix this before looking at any results.

    B - A  <  10pp                     -> OBSOLETE       (delete)
    B - A >=  10pp  and  C ~= B        -> SALIENCE-ONLY  (compress)
    B - A >=  10pp  and  C  <  B       -> LOAD-BEARING   (keep)

`C ~= B` means within 5pp. Detection deltas are computed on planted fixtures; any arm whose
false-positive rate on clean decoys exceeds arm A's by more than 10pp is reported as a
regression regardless of its detection lift.

    python score_stage1.py stage1/results.yaml

## Stage 2 — Model-tier sweep

Re-run arms A and B against Opus, Sonnet, and Haiku.

This is the crux for the harness specifically: guidance can be obsolete for the Orchestrator
and still load-bearing for a Haiku Worker. If lift is zero on Opus but real on Haiku, the
outcome is **not** deletion — it is making language refs conditional on dispatch tier, which
the L0-L3 progressive disclosure model in `language-gates.md` already has the vocabulary to
express.

## Router question (deferred)

`language-gates.md` spends 118 lines of routing overhead to decide whether to read a 55-line
doc. If Stage 1 kills the language refs, the router largely dies with them. If it does not,
the router still needs its own check: does L0-L3 actually change *which* docs get read, or
does the model read the relevant one regardless?
