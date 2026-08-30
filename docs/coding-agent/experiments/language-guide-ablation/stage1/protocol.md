# Stage 1 — Run Protocol

## Cell structure

`(arm, language, fixture, seed)`. 3 arms x 4 languages x 12 fixtures x 3 seeds = 432 review
calls. Each call is an independent clean session.

## Reviewer prompt (identical across arms — only the loaded reference differs)

System/context: paste the arm's reference material (see below), then:

> You are reviewing a proposed change. The task the author was given is stated at the top of
> the fixture, followed by the diff. Report every defect you would block or flag in review,
> as a list. For each finding give: file/location, what is wrong, why it matters, and what
> you would require instead. If the change is acceptable as-is, say so explicitly. Do not
> pad the list — report only findings you would actually raise.

Then paste the fixture file body (framing + diff + notes). The notes in fixtures are part of
the fixture — they carry context a real reviewer would have (e.g. deployment sizes, existing
domain packages). Never strip them.

## Arm contexts

| Arm | Loaded before the reviewer prompt |
|---|---|
| A | `references/core-principles.md` only |
| B | `core-principles.md` + full `references/language-<lang>.md` |
| C | `core-principles.md` + `arms/compressed-<lang>.md` |

Load nothing else — no SKILL.md, no language-gates.md, no other references. The router is a
separate question (see top-level README).

## Blinding

The grader must not know which arm produced a transcript. Randomize transcript filenames
(`stage1/transcripts/<uuid>.md` with a private mapping file kept out of the grader's view)
and grade against `keys/<lang>.md` only.

## Grading

Per transcript, per planted fixture:

- `hit` (1.0) — the finding names the planted mechanism at the planted location and requires
  the fix direction stated in the key
- `partial` (0.5) — right area, wrong or missing mechanism
- `miss` (0.0)

Per clean decoy: count findings that would block or demand rework as **false positives**.
Nitpicks listed as "known acceptable" in the key count as neither. If a reviewer finds a
*real* defect the authors missed (planted or clean fixture), log it in `key-errata.md` and
re-grade all arms after the key revision — never credit only the arm that found it.

Also record output tokens per call.

## Metrics

Per (arm, language): detection = mean hit-score over planted fixtures x seeds;
FP rate = FP findings / clean-fixture reviews; tokens = mean output tokens.

## Pre-registered decision rule (fixed before any run)

Computed on detection, per language:

- `B - A < 10pp` -> **obsolete** — delete the language ref
- `B - A >= 10pp` and `C >= B - 5pp` -> **salience-only** — replace ref with compressed arm C text
- `B - A >= 10pp` and `C < B - 5pp` -> **load-bearing** — keep the full ref

Guard: any arm whose FP rate exceeds arm A's by more than 10pp is flagged as a regression
regardless of detection lift, and cannot be adopted.

Verdicts are **per language**. A mixed result (e.g. Rust load-bearing, Python obsolete) is a
legitimate outcome and should be applied per file, not averaged into one decision.

## Results format

Fill `results.yaml` (template below is also the schema `score_stage1.py` expects):

```yaml
model: claude-opus-5
run_date: ""
records:
  - arm: A            # A|B|C
    language: go
    fixture: go-01
    seed: 1
    score: 0.0        # planted fixtures: 0 | 0.5 | 1
    false_positives: 0 # clean fixtures: count of blocking FP findings; planted: FPs beyond the planted one
    output_tokens: 0
```

## Stage 2 note

Stage 2 reuses these fixtures and this protocol unchanged — arms A and B only, swept across
Opus/Sonnet/Haiku, recorded in `stage2-results.yaml` with an added `model` field per record.
The decision there is not delete-vs-keep but whether to gate language-ref loading on
dispatch tier.
