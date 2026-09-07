# Guidance-class ablation: pre-registered protocol (fixed 2026-09-07, before any cell ran)

Decides, section by section, whether three guidance documents in the harness still change model behavior on the frontier fleet. Recovered and adapted from the archived Stage-1 protocol (`47c409c:docs/coding-agent/experiments/language-guide-ablation/stage1/protocol.md` and `stage1/protocol-v2.md`, ADR-I-0004) and the batch-2 layout (`e221d34:docs/coding-agent/experiments/language-guide-ablation/batch2-eqb-generic/protocol.md`, ADR-I-0005). Nothing below changes after a result exists; a change to the decision rule or a tier boundary is a new decision record per `durable-docs-authoring/references/adr.md`.

## Measured scope (section level)

| Target | Measured sections | Stays regardless of outcome |
|---|---|---|
| `engineering-quality-baselines/references/core-principles.md` | principles 2 through 10 (`### 2)` to `### 10)`, lines 44-133 at `0d465cc`), each its own measured section | principle 1 (lines 26-42, the locatable-consumer contract), Common Anti-Patterns (lines 134-147), Quick Review Pass (lines 155-163), Contents, How to Use, Durable-Code Hygiene, Non-Goals |
| `engineering-quality-baselines/references/architecture-gates.md` | the seven gate bodies (`### Gate 1` to `### Gate 7`, lines 37-149), each its own measured section | Purpose, How to Use in Planning, How to Use in Review, Decision Guidance (status and waiver lines), Output Template, Non-Goals |
| `workspace-troubleshooting/references/` Windows runbooks | `windows-npm-eperm-locks.md`, `windows-docker-grpc-localhost-ipv6.md`, `windows-python-console-encoding.md`, `powershell-json-array-cardinality.md`, `persistent-shell-cwd-normalization.md`, each a whole-file section | `SKILL.md` core rules and routing; the process runbooks `external-changes-triage.md`, `stale-view-or-branch-mismatch.md`, `github-cli-auth-failures.md` (not Windows-specific, out of scope) |

Twenty-one measured sections. Fixture ids: `cp-<n>-<k>` for principle n, `ag-<n>-<k>` for gate n, `rb-<slug>-<k>` for runbooks; clean decoys carry `c` before k (`cp-2-c1`).

## Fleet and seeds

- Models: Claude Fable 5.1 and GPT-6 Astra (plan Q1, resolved 2026-09-06). Delta from ADR-I-0004's fleet (Fable 5, Sol 5.6, Luna 5.6): two models, the current frontier pair; recorded in `outcome.md`.
- Seeds: 2 per cell, per batch 2's pre-registered deviation from 3 (batch 1 observed zero cross-seed variance at 216/216).
- Runners: Fable via clean subagents carrying only the arm context; Astra via `codex exec --ephemeral --disable plugins --disable hooks -c project_doc_max_bytes=0` with the user `~/.codex/AGENTS.md` moved aside and hash-restored, loaded instructions confirmed as "none" (the pure-baseline method in `frontier-guard-probes/run_baseline.sh`).

## Arms

| Arm | Context loaded before the prompt |
|---|---|
| A | nothing from the target document (control) |
| B | the full measured section, verbatim |
| C | a compressed variant of the section, at most one third its length, authored before any cell runs and frozen |

Load nothing else: no SKILL.md, no sibling sections, no other references. For core-principles and architecture-gates, arm A loads no guidance at all (the archived Stage-1 arm A loaded `core-principles.md`; here that document is itself under test).

## Fixtures

Per measured section: 12 planted fixtures whose defect is exactly what that section's checks would catch, plus 4 clean decoys that exercise the same area without the defect (batch-2 shape, `e221d34:...batch2-eqb-generic/protocol.md:9-11`). Planted defects map to one primary named check in the section (quoted in the fixture plan), never to generic code quality; a defect that also falls under a check in another measured section is admitted with that secondary mapping disclosed, because each section is measured in isolation (arm B loads only that section). The fixture plan (`fixture-plan.md`) records the mapping per fixture, and a fixture with no primary named check is dropped before authoring.

- core-principles and architecture-gates fixtures: task framing, a diff, and notes a real reviewer would have; the archived format (`47c409c:...stage1/fixtures/rs-01.md`).
- runbook fixtures: a failure transcript (exact command, exit code, stdout/stderr, cwd, OS and runtime versions) whose cause is the runbook's mechanism; the check is a correct diagnosis of the mechanism and the runbook's safe remediation.

Fixtures, keys, decoys, and the arm-C variants are authored by one agent (Worker A); grading is by different agents (Worker B, one per model per arm) that never see the arm label; transcript filenames are randomized with a private mapping (ADR-I-0004 limits note; `stage1/protocol.md` Blinding). A real defect the authors missed goes to `key-errata.md` and every arm is regraded; no arm is credited alone.

## Prompt

Identical across arms. Review targets use the archived reviewer prompt verbatim:

> You are reviewing a proposed change. The task the author was given is stated at the top of the fixture, followed by the diff. Report every defect you would block or flag in review, as a list. For each finding give: file/location, what is wrong, why it matters, and what you would require instead. If the change is acceptable as-is, say so explicitly. Do not pad the list; report only findings you would actually raise.

Runbook targets:

> A command failed in the workspace described below. State the cause, the smallest safe remediation, and how you would confirm it worked. If the failure is not a workspace problem, say so.

Fixture frontmatter (`type: planted | clean`) is stripped before the prompt.

## Grading

Per planted fixture: `hit` (1.0) names the planted mechanism at the planted location and requires the key's fix direction; `partial` (0.5) right area, wrong or missing mechanism; `miss` (0.0). Per clean decoy: findings that would block or demand rework count as false positives; nitpicks the key lists as known acceptable count as neither. Output tokens recorded per call.

Detection per (section, model, arm) = mean hit score over planted fixtures x seeds. FP rate = FP findings / decoy reviews.

## Decision rule (pre-registered; evaluated per measured section on the worst model)

Let dB = B - A and dC = C - A on planted fixtures, worst model. The worst model for a section is the one with the lowest arm-A detection on that section (the model the guidance could help most); its dB and dC decide. Ties on arm-A detection: the rule is evaluated on every tied model and the most protective outcome stands (KEEP over COMPRESS over DELETE), so the verdict never depends on input order.

1. dB < 10pp: DELETE the section; adopt nothing.
2. dB >= 10pp and dC >= dB - 5pp: COMPRESS; replace the section with the arm-C text.
3. dB >= 10pp and dC < dB - 5pp: KEEP the full section.

FP guard: an arm whose FP rate on decoys exceeds that model's A + 10pp on any fleet model cannot be adopted regardless of lift; the guard is checked on every model, not only the worst one, because the adopted text ships to the whole fleet. A KEEP or COMPRESS candidate failing the guard is recorded as a blocker in `outcome.md`, not resolved by the rule.

Completeness: a verdict is issued only when the section has, on every fleet model, all three arms, every planted fixture at the registered seed count (or the recorded cap), and every decoy graded; missing evidence is reported as INCOMPLETE, never scored as zero.

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
| 2 seeds, pre-registered deviation from 3 | batch-2 `protocol.md:7-8` | retained |
| Arm D (replacement document `boundary-modeling.md`) | `protocol-v2.md:13-14, 23, 56` | adapted: no candidate replacement document exists; arm C (compressed section) takes its place, so REPLACE becomes COMPRESS |
| Conditional arm C on mechanics fixtures | `protocol-v2.md:45-46, 59-60` | dropped: these targets have no language-mechanics class |
| Architectural versus mechanics fixture split | `protocol-v2.md:25-41` | dropped: one class per section |
| Arm A loads `core-principles.md` | `protocol.md` Arm contexts | adapted: arm A loads nothing, because core-principles is under test |
| Fleet Fable 5 / Sol 5.6 / Luna 5.6, 3 seeds | `protocol-v2.md:9, 43-44` | adapted per plan Q1: Fable 5.1 and Astra, 2 seeds |

## Results format

`results.yaml`, one record per (arm, section, fixture, seed):

```yaml
model: claude-fable-5-1   # or gpt-6-astra
run_date: ""
records:
  - arm: A            # A|B|C
    section: cp-2     # cp-<n> | ag-<n> | rb-<slug>
    fixture: cp-2-01
    seed: 1
    score: 0.0        # planted: 0 | 0.5 | 1
    false_positives: 0
    output_tokens: 0
```

`score.py` (adapted from `47c409c:...score_stage1.py`) tabulates detection and FP rate per (section, arm, model), enforces completeness, and prints the verdict per section under the rule above; `python score.py --self-test` exercises every branch, the tie rule, the per-model FP guard, and the incompleteness cases. A recorded seed cap is passed as `--seeds N`.

## Cost and run order

21 sections x 3 arms x 16 fixtures x 2 models x 2 seeds = 4032 calls at full grid. Run order for early exit: (1) the five runbooks on both models; (2) core-principles 2 and 9, chosen before any cell ran as the two principles whose review checks are most specific, on both models; (3) the rest. If every section in steps 1 and 2 shows arm A at ceiling, the user may cap the remainder at one seed; the cap is recorded in `outcome.md` before the capped cells run.

## Outcome record

`outcome.md` carries, per measured section, detection per arm per model, dB and dC on the worst model, FP guard status, the applied outcome, and the edit made; plus the records commit, the fleet delta from ADR-I-0004, and any invalidated fixture with its reason. Per ADR-D-0019, no per-removal decision record.
