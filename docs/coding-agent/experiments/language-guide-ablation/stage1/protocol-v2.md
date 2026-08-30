# Stage 1 — Run Protocol v2 (amended after Stage 0, before any Stage 1 cell ran)

Supersedes `protocol.md` (kept for provenance). Amendments were fixed on 2026-08-28 based
on Stage 0 findings and BEFORE running any Stage 1 cell — the decision rules below are
pre-registered and must not change after results exist.

## What Stage 0 changed

1. Fleet is Fable 5, Sol 5.6, Luna 5.6 (user-defined). The old model-tier Stage 2
   (Opus/Sonnet/Haiku) is dropped; Stage 1 runs per model instead.
2. Rust and Python guides already survived the delete question (regeneration 54-77%).
   For them Stage 1 decides keep-vs-replace-with-D only.
3. New primary hypothesis: the guides' live value is the cross-language architectural
   residue, captured in `arms/boundary-modeling.md` (arm D).

## Arms

| Arm | Context loaded with the reviewer prompt |
|---|---|
| A | `core-principles.md` only |
| B | `core-principles.md` + full `language-<lang>.md` |
| C | `core-principles.md` + `arms/compressed-<lang>.md` (conditional, see rule) |
| D | `core-principles.md` + `arms/boundary-modeling.md` (same doc for every language) |

## Fixture classes (pre-registered split)

Class membership is determined by Stage 0 evidence: a fixture is **architectural** iff its
planted bullet was missed or only partially hit by the models (G5/G6, R1/R12, R2/R14, R8,
R16, P3/P12, T2, T10, T12, T15); fixtures testing reliably-regenerated bullets are
**mechanics**.

- **architectural**: go-08, go-09, py-05, rs-03, rs-04, rs-06, ts-05, ts-06, ts-07, ts-08
- **mechanics**: go-01..07, py-01..04, py-06..08, rs-01, rs-02, rs-05, rs-07, rs-08, ts-01..04
- go-09 (planting G5: dumping-ground util package + dependency cycle) was ADDED with this
  amendment because Go otherwise had a single architectural fixture; added before any cell ran.
- clean decoys unchanged (FP guard applies to both classes)

Detection is reported per class per (model, language, arm). The headline metric is the
architectural class; mechanics is the control (Stage 0 predicts B-A ~ 0 there).

## Cells

- Languages x models: all 4 languages x Fable/Sol/Luna.
- Arms A, B, D everywhere; >= 3 seeds.
- Arm C runs ONLY where (B - A >= 10pp on mechanics fixtures) — i.e. only if the
  per-language doc shows lift D cannot explain. Expected: nowhere.
- Runners: Fable via clean subagents; Sol/Luna via `codex exec` with the Stage 0 isolation
  flags (`--ignore-user-config --ignore-rules --ephemeral`, read-only empty dir, global
  AGENTS.md parked). Reviewer prompt as in protocol.md; twin-separation rule unchanged.

## Pre-registered decision rule (per language, evaluated on the WORST of the 3 models)

Let dB = B - A and dD = D - A on architectural fixtures, worst-model.

1. dB < 10pp                          -> guide obsolete AND D unnecessary: delete, adopt nothing
2. dB >= 10pp and dD >= dB - 5pp      -> REPLACE: delete the language guide; D covers it
3. dB >= 10pp and dD <  dB - 5pp      -> KEEP full guide (language-specific content is load-bearing)

Mechanics-class guard: if B - A >= 10pp on mechanics for some language, trigger arm C
there and re-apply the old C-vs-B rule for that language's mechanics content.

FP guard unchanged: any arm with FP rate > A + 10pp is a regression and cannot be adopted
regardless of detection lift.

Adoption rule across languages: D is adopted only once — if outcome 2 holds for at least
two languages and outcome 3 for none, all four guides are replaced by
`boundary-modeling.md`; a language hitting outcome 3 keeps its guide alongside D.

## Cost note

A/B/D x 4 langs x 3 models x 12 fixtures x 3 seeds = 1296 reviews at full grid. Run order
to allow early exit: (1) Rust on all 3 models — if even Rust (worst regeneration) shows
dB < 10pp, outcome 1 likely generalizes and the rest can run at reduced seeds;
(2) Go on all 3 models — the strongest obsolescence claim, needs confirmation that
knowledge translates to application; (3) TS, then Python.
