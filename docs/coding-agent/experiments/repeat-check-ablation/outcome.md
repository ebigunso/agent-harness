# Repeat-check ablation: outcome

Protocol: `protocol.md` (SHA-256 `d7218c9d7ed6b2684f43d5d78c2d0c86460fab34761b7337b13710534d6fab6b`), frozen revision `f7b81bba928b9ec0386f5f8c8131db1f41488e4e`. Run 2026-09-16 (local; the results files carry the UTC date 2026-09-15 from the output mtimes). 288 cells, 288 complete on the first call, 0 retries, 0 failed; six blinded Claude graders (one per section per model), 0 ungraded records, 0 adjudications, no key errata.

Scoring: `python score.py --manifest manifest.yaml --seeds 1 work/results-fable.yaml work/results-astra.yaml`.

## Per-section table

Detection = mean hit score over 12 planted fixtures (1 seed); FP = false positives over 4 decoys.

| Section | Model | A det | B det | C det | A FP | B FP | C FP |
|---|---|---|---|---|---|---|---|
| tv-1 skip confirmation | claude-fable-5-1 | 1.000 | 1.000 | 1.000 | 0/4 | 0/4 | 0/4 |
| tv-1 skip confirmation | gpt-6-astra | 1.000 | 1.000 | 1.000 | 0/4 | 0/4 | 0/4 |
| tv-2 gated live test | claude-fable-5-1 | 0.958 | 0.958 | 1.000 | 0/4 | 0/4 | 0/4 |
| tv-2 gated live test | gpt-6-astra | 0.917 | 1.000 | 0.917 | 0/4 | 0/4 | 0/4 |
| tv-3 baseline classification | claude-fable-5-1 | 1.000 | 1.000 | 1.000 | 0/4 | 0/4 | 0/4 |
| tv-3 baseline classification | gpt-6-astra | 1.000 | 1.000 | 1.000 | 0/4 | 0/4 | 0/4 |

| Section | Worst model | dB | dC | FP guard | Rule applied | Outcome |
|---|---|---|---|---|---|---|
| tv-1 | tie: both models at A = 1.000; evaluated on both | +0pp / +0pp | +0pp / +0pp | pass on both (every arm 0/4; threshold A + 10pp) | ceiling note; rule 1 (dB < 10pp) on both tied models; the most protective of two DELETEs is DELETE | DELETE |
| tv-2 | gpt-6-astra (A = 0.917 < 0.958) | +8.3pp | +0pp | pass on both models | rule 1 (dB < 10pp) | DELETE |
| tv-3 | tie: both models at A = 1.000; evaluated on both | +0pp / +0pp | +0pp / +0pp | pass on both | ceiling note; rule 1 on both tied models | DELETE |

Completeness: every registered model appears once; every section has all three arms and all 16 fixtures graded at the registered seed count on both models. No section is INCOMPLETE. No protective tie changed an outcome (the tied models agree).

Non-hits, all on one fixture: tv-2-10 (recorded run without gate identity). Fable: arms A and B partial (0.5; the gap identified, gate identity not required). Astra: arms A and C miss (0.0; accepted as-is, dismissing the missing gate identity). Arm B on Astra hit it, which is the +8.3pp; below the pre-registered 10pp lift threshold.

## Edit made (Task_4)

DELETE replaces the prescribed mechanics with the arm-A obligation text, byte for byte, in `plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/testing-validation.md`:

- Line 74 (hosts tv-1 and tv-2, one bullet joined by "and") becomes two bullets, `arms/tv-1-A.md` then `arms/tv-2-A.md`:
  - `- Specific-test evidence must show executed, unskipped tests.`
  - `- Gated live tests require negative evidence when the gate could be off.`
- Line 77 (tv-3) becomes `arms/tv-3-A.md`:
  - `- Classify failures in untouched tests as pre-existing or regression before remediation.`

Every invariant obligation survives; nothing else in the file changes.

## Records and fleet

- Records: `work/results-fable.yaml`, `work/results-astra.yaml` (one record per arm, section, fixture, seed), `work/grades/<model>/<section>.yaml` (grader output with a rationale per record), `work/output-tokens.yaml` (per-cell token and cost record: Fable 178,099 output tokens, $13.55; Astra 974,360 tokens as the CLI's total). The raw outputs, prompts, blinded copies, and the private mapping stay under `work/` in the checkout for review and are removed at closeout (Task_5).
- Fleet delta from ADR-I-0004 (consulted Claude Fable 5, GPT-5.6 Sol, GPT-5.6 Luna; three seeds): this run used Claude Fable 5.1 and GPT-6 Astra, one seed, per Q2 and Q3 of the plan.
- Invalidated fixtures: none.

## Caveats

- Ceiling: arm A scores 1.000 on tv-1 and tv-3 on both models and 0.917 or better on tv-2; per the protocol's ceiling note the ceiling is itself the finding for a content-redundancy question. The experiment shows the obligation alone produces the detection; it does not show that the mechanics harm.
- One seed per cell (Q3); the tv-2 differences rest on a single fixture (tv-2-10), and a second seed could move them by one grade either way without crossing the 10pp threshold on the observed values.
- Graders were Claude subagents; the rule text and keys were fixed before grading, and graders never saw arms or the mapping. Two graders noted borderline calls in their rationale fields (Fable tv-1-09 "flag, not block" scored as a hit because the rerun was stated as a requirement; Astra tv-2 "retract the claim or supply the evidence" scored as hits because the evidence is a blocking condition for the claim as made). Both readings were applied consistently within their section and do not affect any outcome.
- Fixtures are review targets only (diff plus validation summary); no runbook targets and no generation-time behavior were measured.
