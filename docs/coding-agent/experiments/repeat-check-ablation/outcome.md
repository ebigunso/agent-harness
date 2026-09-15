# Repeat-check ablation: outcome

Protocol: `protocol.md` (SHA-256 `d7218c9d7ed6b2684f43d5d78c2d0c86460fab34761b7337b13710534d6fab6b`), frozen revision `f7b81bba928b9ec0386f5f8c8131db1f41488e4e`. Run 2026-09-16 (local; the results files carry the UTC date 2026-09-15 from the output mtimes). 288 cells, 288 complete on the first call, 0 retries, 0 failed; six blinded Claude graders (one per section per model), 0 ungraded records, no key errata. One grading adjudication (below): tv-2 was regraded on both models by two fresh blinded graders after the Reviewer found the round-1 Astra grader had relaxed the Q1 hit condition; the round-1 tv-2 grades are preserved in `work/grades-round1/`.

Scoring: `python score.py --manifest manifest.yaml --seeds 1 work/results-fable.yaml work/results-astra.yaml`.

## Per-section table

Detection = mean hit score over 12 planted fixtures (1 seed); FP = false positives over 4 decoys.

| Section | Model | A det | B det | C det | A FP | B FP | C FP |
|---|---|---|---|---|---|---|---|
| tv-1 skip confirmation | claude-fable-5-1 | 1.000 | 1.000 | 1.000 | 0/4 | 0/4 | 0/4 |
| tv-1 skip confirmation | gpt-6-astra | 1.000 | 1.000 | 1.000 | 0/4 | 0/4 | 0/4 |
| tv-2 gated live test | claude-fable-5-1 | 0.542 | 0.542 | 0.583 | 0/4 | 0/4 | 0/4 |
| tv-2 gated live test | gpt-6-astra | 0.708 | 0.958 | 0.875 | 0/4 | 0/4 | 0/4 |
| tv-3 baseline classification | claude-fable-5-1 | 1.000 | 1.000 | 1.000 | 0/4 | 0/4 | 0/4 |
| tv-3 baseline classification | gpt-6-astra | 1.000 | 1.000 | 1.000 | 0/4 | 0/4 | 0/4 |

| Section | Worst model | dB | dC | FP guard | Rule applied | Outcome |
|---|---|---|---|---|---|---|
| tv-1 | tie: both models at A = 1.000; evaluated on both | +0pp / +0pp | +0pp / +0pp | pass on both (every arm 0/4; threshold A + 10pp) | ceiling note; rule 1 (dB < 10pp) on both tied models; the most protective of two DELETEs is DELETE | DELETE |
| tv-2 | claude-fable-5-1 (A = 0.542 < 0.708) | +0pp | +4.2pp | pass on both models | rule 1 (dB < 10pp) | DELETE |
| tv-3 | tie: both models at A = 1.000; evaluated on both | +0pp / +0pp | +0pp / +0pp | pass on both | ceiling note; rule 1 on both tied models | DELETE |

Completeness: every registered model appears once; every section has all three arms and all 16 fixtures graded at the registered seed count on both models. No section is INCOMPLETE. No protective tie changed an outcome (the tied models agree).

Non-hits on tv-1 and tv-3: none. Non-hits on tv-2 after the adjudication: Fable, 32 of 36 planted responses are partial (0.5): every one names the gate value or the missing service-down run at its location, then offers the author an alternative to obtaining it (strike, reword, or narrow the live-validation claim and merge); the four hits (A tv-2-11, B tv-2-05, C tv-2-10, C tv-2-11) make the evidence a blocking condition with no such alternative. Astra: seven partials of the same kind (A on tv-2-02, -03, -04, -06, -07; B on tv-2-06; C on tv-2-07) and two misses on tv-2-10 (A and C accept the change as-is, dismissing the missing gate identity). No false positive on any decoy in any arm on either model.

## Adjudication (tv-2 regrade)

The Reviewer's Task_3 review (finding R1) showed that the round-1 Astra tv-2 grader had scored seven responses as hits under a condition it adopted after reading them ("evidence required only for the claim as made"), while Q1 requires the response to require obtaining the missing evidence. A response that lets the author retract or relabel the claim instead has identified the gap without requiring the evidence, which is Q1's partial. The Reviewer's sensitivity copy (those seven records at 0.5, nothing else changed) gave Astra A 0.708, B 0.958, C 0.875, dB +25pp, dC +16.7pp, which would be KEEP on the worst model at that point.

Resolution: tv-2 was regraded on both models by two fresh blinded Claude graders (same packet, same key, same blind directories, no access to the round-1 grades or the mapping) with one added sentence stating the Q1 hit condition literally: a response offering retraction, relabeling, or narrowing of the live-validation claim as an alternative to obtaining the gate identity or the negative-control evidence scores 0.5 at most. Applied to every tv-2 response in every arm on both models. The Astra regrade reproduces the Reviewer's seven records exactly and changes nothing else; the Fable regrade finds the same pattern in 32 of 36 planted responses in all three arms (round 1 had scored 34 as hits). Under the same condition on both models the worst model on tv-2 is Fable (A 0.542), where dB is +0pp and dC +4.2pp; rule 1 applies and the outcome is DELETE, not KEEP. The Reviewer's KEEP illustration held Fable at its round-1 grades; applied consistently, the retraction pattern is a property of the model's review style in every arm, and the mechanics text does not remove it (B and C on Fable carry it as often as A). The round-1 grade files are preserved unchanged in `work/grades-round1/<model>/tv-2.yaml`; the results files and the scorer output use the regrade.

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

- Ceiling: arm A scores 1.000 on tv-1 and tv-3 on both models; per the protocol's ceiling note the ceiling is itself the finding for a content-redundancy question. On those sections the obligation alone produces the detection; the experiment does not show that the mechanics harm.
- tv-2 is not a ceiling result. Fable detects the gap in every planted case but requires the evidence in only four; Astra requires it in 27 of 36. The line under test did not change that on the worst model (Fable A = B), and on Astra the B lift (+25pp) is real but Astra is not the worst model, so it does not decide under the pre-registered rule. A future guidance question about tv-2 is whether an obligation can be phrased so that Fable requires the evidence rather than offering a relabel; that is a different experiment.
- One seed per cell (Q3); on tv-2 the Astra arm differences rest on a handful of fixtures, and a second seed could move individual grades without changing the worst-model outcome (Fable dB is 0 with 24 partials on each of A and B).
- Graders were Claude subagents; the rule text and keys were fixed before grading, and graders never saw arms or the mapping. One round-1 borderline call stands: Fable tv-1-09 "flag, not block" scored as a hit because the rerun was stated as a requirement with no alternative offered, which the Reviewer's spot check supported. The other round-1 borderline call (Astra tv-2) was the subject of the adjudication above.
- Fixtures are review targets only (diff plus validation summary); no runbook targets and no generation-time behavior were measured.
