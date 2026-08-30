# Stage 0 — Cross-model summary (2026-08-28)

Coverage of each language guide's key bullets, regenerated unprompted in clean sessions
(3 seeds/cell; hit=1, partial=0.5). Graded by Opus 5 against `probe.md` keys; raw outputs
retained (Fable: task transcripts; Sol/Luna: probe-run/out/*.txt).

| Language | Fable 5 | Sol 5.6 | Luna 5.6 | Fleet verdict |
|---|---|---|---|---|
| Go | 82% | 87% | 76% | prima facie obsolete -> Stage 1 to confirm |
| TypeScript/JS | 76% | 86% | 74% | inconclusive -> Stage 1 |
| Python | 58% | 77% | 58% | carries signal for 2 of 3 models |
| Rust | 63% | 68% | 54% | carries signal -> most load-bearing guide |

Fleet rule: a guide is deletable only if it is obsolete for EVERY model that does day-to-day
coding. Rust and Python fail that test outright; Go and TS need the Stage 1 ablation.

## The consistent residue (missed by all three models, nearly all seeds)

- Pure-logic vs I/O separation (R8) — 0/9 seeds across models
- Transport-vs-domain separation (G6, R16, T10) — Luna names cross-layer *duplication*,
  nobody names the *leakage*
- Exhaustive-match over if-chains as compiler leverage (R14; R2 weak) — only Fable rs-1 hit it
- Newtypes/typed models over primitives and dicts (R1, R12, P3, P12) — sporadic at best
  (exception: Sol py-3)

These are design/boundary-modeling checks, not language mechanics. Mechanics (error
wrapping, panic/unwrap, async hygiene, races, security, deterministic tests) regenerate at
near-100% in every model, often deeper than the guides themselves.

## Implication for Stage 1

Test a fourth arm if convenient: a single ~10-bullet cross-language "boundary modeling"
reference (the residue above) replacing all four per-language docs. Stage 1's architectural
fixtures (go-06, go-08, rs-03, rs-04, rs-06, ts-07, ts-08, py-05) directly test exactly
these bullets; the mechanics fixtures test what Stage 0 says the models already know.

## Method notes

- Fable via clean subagent threads (0 tool uses/probe). Sol/Luna via `codex exec` in an
  empty read-only dir, `--ignore-user-config --ignore-rules --ephemeral`, global
  AGENTS.md (harness loader) parked during the run and restored after.
- Sol outputs were 2-3x longer than the others; coverage may partly reflect output budget,
  not just knowledge salience. Stage 1 measures application, which is the question that matters.
- Grader = key author (flagged in protocol). Borderline conventions recorded in each
  results file.

---

# Stage 1 Rust block result (2026-08-29)

216/216 planted-defect detections across Fable/Sol/Luna x arms A/B/D (see
`../stage1/results-rust.yaml`). B-A = 0, D-A = 0, architectural subset included.
Pre-registered outcome 1: **language-rust.md obsolete; arm D unnecessary** — with the
ceiling caveat recorded in the results file. Since Rust was the worst Stage 0 regenerator,
outcome 1 is expected to generalize to Go/TS/Python; per protocol-v2 the remaining language
blocks may run at reduced seeds, or the fleet may accept the Rust result as decisive.
Decoys rs-c2/rs-c3 invalidated as authoring errors (rs-c3's "clean" transfer is genuinely
non-atomic — flagging it was correct).
