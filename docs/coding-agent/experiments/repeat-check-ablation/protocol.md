# Repeat-check ablation: pre-registered protocol (fixed before any cell runs)

Decides, section by section, whether the prescribed rerun mechanics in two testing-validation.md lines change model behavior when equivalent evidence already exists; every evidence obligation remains invariant. Recovered and adapted from the archived Stage-1 protocol (`47c409c:docs/coding-agent/experiments/language-guide-ablation/stage1/protocol.md` and `stage1/protocol-v2.md`, ADR-I-0004) and the batch-2 layout (`e221d34:docs/coding-agent/experiments/language-guide-ablation/batch2-eqb-generic/protocol.md`, ADR-I-0005). Nothing below changes after a result exists; a change to the decision rule or a tier boundary is a new decision record per `durable-docs-authoring/references/adr.md`.

## Measured scope (section level)

Frozen revision: `76434f6e0b45360412c073d8fd02eb86161dcffe` (part-3 branch tip at Task_1 start). Source: `plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/testing-validation.md`. Re-baselined source lines remain 74 and 77.

| Section | Source obligation / prescribed mechanic (exact quotation) | Invariant obligation retained in every outcome |
|---|---|---|
| tv-1 skip confirmation | `- Skip-capable tests can report green with unexecuted bodies: when specific-test evidence matters, rerun it targeted and confirm no skip message` | - Specific-test evidence must show executed, unskipped tests. |
| tv-2 gated live test | `verify gated live tests once with the service deliberately down.` | - Gated live tests require negative evidence when the gate could be off. |
| tv-3 baseline classification | `- When validation fails in tests the change did not touch, rerun against baseline HEAD (stash/worktree) to classify pre-existing vs regression before remediating.` | - Classify failures in untouched tests as pre-existing or regression before remediation. |

Arm B extraction is byte-preserving within each source line: tv-1 is line 74 before `, and `; tv-2 is the remainder after that separator; tv-3 is the whole of line 77. The two line-74 spans plus that separator reconstruct line 74. Arm files use LF with one terminal newline; the source span excludes its line terminator.

Three measured sections. Fixture ids: `tv-<n>-01` through `tv-<n>-12`; clean decoys `tv-<n>-c1` through `tv-<n>-c4`. All other source lines, evidence obligations, required checks and waivers remain unchanged.

## Fleet and seeds

- Models: Claude Fable 5.1 and GPT-6 Astra (plan Q1, resolved 2026-09-06). Delta from ADR-I-0004's fleet (Fable 5, Sol 5.6, Luna 5.6): two models, the current frontier pair; recorded in `outcome.md`.
- Seeds: 1 per cell, per the approved repeat-check plan.
- Runners: Fable via restricted headless CLI calls with user settings disabled and successful, non-empty JSON results required; Astra via `codex exec --ephemeral --disable plugins --disable hooks -c project_doc_max_bytes=0` with the user `~/.codex/AGENTS.md` moved aside and hash-restored, loaded instructions confirmed as "none" (the pure-baseline method in `frontier-guard-probes/run_baseline.sh`).

## Arms

| Arm | Context loaded before the prompt |
|---|---|
| A | The invariant obligation, without prescribed mechanics (control). |
| B | The exact registered source span for that section. |
| C | The same invariant obligation plus one hint clause conditional on absent evidence. |

Load nothing else: no SKILL.md, no sibling sections, no other references. Every arm retains its section's evidence obligation. Exact arm text follows; each arm file contains that text and one terminal LF.

### tv-1 A

```text
- Specific-test evidence must show executed, unskipped tests.
```

### tv-1 B

```text
- Skip-capable tests can report green with unexecuted bodies: when specific-test evidence matters, rerun it targeted and confirm no skip message
```

### tv-1 C

```text
- Specific-test evidence must show executed, unskipped tests. If that evidence is absent, rerun the specific test and check for skips.
```

### tv-2 A

```text
- Gated live tests require negative evidence when the gate could be off.
```

### tv-2 B

```text
verify gated live tests once with the service deliberately down.
```

### tv-2 C

```text
- Gated live tests require negative evidence when the gate could be off. If that evidence is absent, verify once with the service deliberately down.
```

### tv-3 A

```text
- Classify failures in untouched tests as pre-existing or regression before remediation.
```

### tv-3 B

```text
- When validation fails in tests the change did not touch, rerun against baseline HEAD (stash/worktree) to classify pre-existing vs regression before remediating.
```

### tv-3 C

```text
- Classify failures in untouched tests as pre-existing or regression before remediation. If that evidence is absent, compare against baseline HEAD.
```

## Fixtures

Per measured section: 12 planted fixtures whose validation summary leaves the section's specific evidence gap, plus 4 clean decoys with equivalent conclusive evidence already present. Each fixture contains task framing, a diff, a commit message, and Reviewer notes containing the validation summary a Worker would see. Each plant maps to exactly one section; the key names the gap, its location, and the evidence needed to close it by any adequate means. The fixture plan (`fixture-plan.md`) registers all 48 mapping slots before authoring.

Planted cases: tv-1 presents green or exit-zero evidence that does not establish executed, unskipped tests; tv-2 leaves the live-test gate or its negative evidence unestablished; tv-3 presents a failure in untouched tests without a pre-existing/regression classification. Decoys explicitly show executed-test counts and no skips, a verified gate with negative evidence, or baseline classification respectively, and invite an unnecessary rerun. No unrelated defect is planted.

Fixtures, keys and decoys are authored by the fixture Worker after the arms are registered by the protocol Worker. Six independent graders (one per section per model) never see arm labels; transcript filenames are randomized with a private mapping. Only successful cells enter grading; missing or failed cells remain missing for the completeness rule. A real defect the authors missed goes to `key-errata.md` and every arm is regraded; no arm is credited alone.

## Prompt

Identical across arms. Review targets use the archived reviewer prompt verbatim:

> You are reviewing a proposed change. The task the author was given is stated at the top of the fixture, followed by the diff. Report every defect you would block or flag in review, as a list. For each finding give: file/location, what is wrong, why it matters, and what you would require instead. If the change is acceptable as-is, say so explicitly. Do not pad the list; report only findings you would actually raise.

Runbook targets:

> A command failed in the workspace described below. State the cause, the smallest safe remediation, and how you would confirm it worked. If the failure is not a workspace problem, say so.

Fixture frontmatter (`type: planted | clean`) is stripped before the prompt.

## Grading

Per planted fixture: `hit` (1.0) detects the section's specific evidence gap at its location and requires obtaining that evidence by any adequate means (a targeted rerun, an executed-test count from the log, a gate check, or a baseline comparison); a prescribed command sequence is not required. `partial` (0.5) identifies the right area but misses the specific gap or the evidence needed; `miss` (0.0) does neither. Per clean decoy: a blocking demand for further verification when the shown evidence already settles the question is a false positive; known acceptable optional nitpicks count as neither. Output tokens recorded per call. This is the Q1 grading rule for this experiment; no runbook-specific grading ruling is reused or extended.

Detection per (section, model, arm) = mean hit score over planted fixtures x seeds. FP rate = FP findings / decoy reviews.

## Decision rule (pre-registered; evaluated per measured section on the worst model)

Let dB = B - A and dC = C - A on planted fixtures, worst model. The worst model for a section is the one with the lowest arm-A detection on that section (the model the guidance could help most); its dB and dC decide. Ties on arm-A detection: the rule is evaluated on every tied model and the most protective outcome stands (KEEP over COMPRESS over DELETE), so the verdict never depends on input order.

1. dB < 10pp: DELETE the prescribed mechanics; retain the arm-A obligation text.
2. dB >= 10pp and dC >= dB - 5pp: COMPRESS; retain the obligation plus the arm-C conditional hint.
3. dB >= 10pp and dC < dB - 5pp: KEEP the full source span; the invariant obligation remains.

FP guard: an arm whose FP rate on decoys exceeds that model's A + 10pp on any fleet model cannot be adopted regardless of lift; the guard is checked on every model, not only the worst one, because the adopted text ships to the whole fleet. A KEEP or COMPRESS candidate failing the guard is recorded as a blocker in `outcome.md`, not resolved by the rule.

Completeness: `manifest.yaml` registers the fleet, the seed count, and every fixture per section, frozen with this protocol. A verdict is issued only when every registered model appears exactly once and the section has, on every model, all three arms and every registered fixture (plants and decoys) graded at the registered seed count or the recorded cap; a missing record or a missing grading value makes the section INCOMPLETE, never zero.

Ceiling note, carried from the Rust block (`47c409c:...stage1/results-rust.yaml`): if arm A scores at ceiling on a section, dB = 0 and outcome 1 applies; the ceiling is itself the finding for a content-redundancy question.

### Retained versus adapted

| Element | Source | Status |
|---|---|---|
| Worst-model aggregation | `protocol-v2.md:51-53` ("evaluated on the WORST of the 3 models") | retained; tie handling added above |
| 10pp lift threshold | `protocol-v2.md:55`; `protocol.md` decision rule | retained |
| 5pp replacement tolerance | `protocol-v2.md:56-57` | retained |
| Clean-decoy FP guard, A + 10pp, any arm cannot be adopted | `protocol-v2.md:62-63` | retained, scope stated as every fleet model (batch-2 `protocol.md:11` uses the same threshold with the opposite consequence, cannot delete; not adopted here) |
| Hit / partial / miss grading, key-errata regrade, blinding | `protocol.md` Grading and Blinding | retained |
| 12 planted + 4 decoys per unit | batch-2 `protocol.md:9` | retained (unit is a section, not a document) |
| One seed | approved repeat-check plan | adapted: one seed in every registered cell |
| Arm D (replacement document `boundary-modeling.md`) | `protocol-v2.md:13-14, 23, 56` | adapted: no candidate replacement document exists; arm C (compressed section) takes its place, so REPLACE becomes COMPRESS |
| Conditional arm C on mechanics fixtures | `protocol-v2.md:45-46, 59-60` | adapted: one hint conditional on absent evidence, with the obligation invariant |
| Architectural versus mechanics fixture split | `protocol-v2.md:25-41` | dropped: one class per section |
| Arm A loads `core-principles.md` | `protocol.md` Arm contexts | adapted: arm A loads only the invariant evidence obligation |
| Fleet Fable 5 / Sol 5.6 / Luna 5.6, 3 seeds | `protocol-v2.md:9, 43-44` | adapted per approved plan: Fable 5.1 and Astra, one seed |

## Results format

`results.yaml`, one record per (arm, section, fixture, seed):

```yaml
model: claude-fable-5-1   # or gpt-6-astra
run_date: ""
records:
  - arm: A            # A|B|C
    section: tv-1     # tv-1 | tv-2 | tv-3
    fixture: tv-1-01
    seed: 1
    score: 0.0        # planted: 0 | 0.5 | 1
    false_positives: 0
    output_tokens: 0
```

`score.py` (adapted from `47c409c:...score_stage1.py`) validates results against `manifest.yaml`, tabulates detection and FP rate per (section, arm, model), and prints the verdict per section under the rule above; `python score.py --self-test` exercises every branch, the tie rule in both argument orders, the per-model FP guard, and seven incompleteness cases. A recorded seed cap is passed as `--seeds N`.

## Cost and run order

3 sections x 3 arms x 16 fixtures x 2 models x 1 seed = 288 initial calls. At most 96 retries in aggregate and at most two retries per cell; the maximum is 384 model calls. Stop when either retry limit or the total-call limit is reached. The six blinded grader dispatches are accounted separately. At a stop, an affected section remains INCOMPLETE and ebigunso decides. At the 2026-09-09 rates the Fable half costs about $10 before retries; Astra uses ephemeral CLI calls. Run each complete section on both models; no score-based early exit or seed reduction is authorized.

## Outcome record

`outcome.md` carries, per measured section, detection per arm per model, dB and dC on the worst model, FP guard status, the applied outcome, and the edit made; plus the records commit, the fleet delta from ADR-I-0004, and any invalidated fixture with its reason. Per ADR-D-0019, no per-removal decision record.
