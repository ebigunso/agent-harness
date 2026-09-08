# Guidance-class ablation: outcome (pilot, 2026-09-08)

Pre-registered protocol: `protocol.md` (frozen 2026-09-07); fixtures per `fixture-plan.md` and `manifest.yaml`; scorer `score.py`. This record covers the pre-registered pilot: the five Windows runbooks and core principles 2 and 9. The remaining fourteen sections (principles 3 through 8 and 10, gates 1 through 7) have not run; see "Remaining sections" below.

## Fleet, runs, and grading

- Models: GPT-6 Astra (codex-cli 0.153.4, `codex exec --ephemeral --disable plugins --disable hooks -c project_doc_max_bytes=0 -s read-only`, user `~/.codex/AGENTS.md` moved aside for the run window and restored with a matching SHA-256; runner `run/run_astra.sh`) and Claude Fable 5.1 (Claude Code CLI 2.1.263, `claude -p --restricted --disallowedTools "*" --strict-mcp-config` with an empty MCP config, a fixed one-line system prompt, one turn, no session persistence, run from an empty directory; runner `run/run_fable.sh`; mean 1,146 input and 1,245 output tokens per cell, $49.07 for the half). Delta from ADR-I-0004's fleet (Fable 5, Sol 5.6, Luna 5.6): the two current frontier models, per plan Q1.
- Cells: 7 sections x 3 arms x 16 fixtures x 2 seeds x 2 models = 1,344; all completed with exit 0 and a non-empty response. Transcripts: `work/astra/`, `work/fable/` (with `work/fable-json/` carrying usage).
- Grading: blinded. `run/blind.py` keeps only the model's response under a random id with the fixture id visible (needed to apply the key) and the arm and seed hidden; the mapping stays with the Orchestrator. Fourteen Claude Fable 5.1 grader agents per model, two per section, each grading 48 responses against `keys/<section>.md` and the fixtures only. `run/unblind.py` merged 672 records per model with zero unknown, duplicate, or mismatched ids. Deviation from `protocol.md` ("one grader per model per arm"): graders were split per section instead, because a per-arm grader would know the arm; per-section blinding is stricter.
- A first attempt to run Fable cells as Claude Code subagents was abandoned after 16 cells: each carried about 54,000 tokens of session preamble, which is neither clean nor affordable. Those 16 outputs are set aside in `work/fable-subagent-trial/` and were not graded.

## Results (detection = mean hit score over 12 planted fixtures x 2 seeds; FP = false-positive findings per decoy review, 4 decoys x 2 seeds)

| Section | Model | A det | B det | C det | A FP | B FP | C FP |
|---|---|---|---|---|---|---|---|
| cp-2 root-cause fixes | Fable | 1.00 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 |
| cp-2 root-cause fixes | Astra | 1.00 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 |
| cp-9 explicit safe failures | Fable | 1.00 | 1.00 | 1.00 | 1.12 | 0.75 | 0.75 |
| cp-9 explicit safe failures | Astra | 1.00 | 1.00 | 1.00 | 0.00 | 0.00 | 0.12 |
| rb npm EPERM locks | Fable | 1.00 | 0.94 | 1.00 | 0.00 | 0.00 | 0.00 |
| rb npm EPERM locks | Astra | 1.00 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 |
| rb Docker gRPC IPv6 | Fable | 1.00 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 |
| rb Docker gRPC IPv6 | Astra | 1.00 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 |
| rb Python console encoding | Fable | 0.98 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 |
| rb Python console encoding | Astra | 0.98 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 |
| rb PowerShell JSON cardinality | Fable | 0.88 | 1.00 | 1.00 | 0.12 | 0.00 | 0.00 |
| rb PowerShell JSON cardinality | Astra | 0.88 | 0.98 | 1.00 | 0.00 | 0.00 | 0.00 |
| rb shell cwd normalization | Fable | 0.92 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 |
| rb shell cwd normalization | Astra | 1.00 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 |

Full per-cell records: `work/results-fable.yaml`, `work/results-astra.yaml`; grader notes: `work/grades/`.

## Rule applied (worst model = lowest arm-A detection; ties evaluated on every tied model, most protective outcome stands)

| Section | Worst model | dB | dC | FP guard | Outcome | Edit made |
|---|---|---|---|---|---|---|
| cp-2 | tie (both 1.00) | +0pp | +0pp | pass | DELETE | section "2) Prefer Root-Cause Fixes Over Symptom Patches" removed from `core-principles.md` |
| cp-9 | tie (both 1.00) | +0pp | +0pp | Astra arm C 0.12 vs A 0.00 exceeds A+10pp; moot under DELETE | DELETE | section "9) Make Failure Modes Explicit and Safe" removed from `core-principles.md` |
| rb npm EPERM locks | tie (both 1.00) | Fable -6pp, Astra +0pp | +0pp | pass | DELETE | `windows-npm-eperm-locks.md` removed; routing line removed |
| rb Docker gRPC IPv6 | tie (both 1.00) | +0pp | +0pp | pass | DELETE | `windows-docker-grpc-localhost-ipv6.md` removed; routing line removed |
| rb Python console encoding | tie (both 0.98) | +2pp | +2pp | pass | DELETE | `windows-python-console-encoding.md` removed; routing line removed |
| rb PowerShell JSON cardinality | tie (both 0.88) | Fable +12pp, Astra +10pp | +12pp both | pass | COMPRESS | body of `powershell-json-array-cardinality.md` replaced with the arm-C text; routing line kept |
| rb shell cwd normalization | Fable (0.92) | +8pp | +8pp | pass | DELETE | `persistent-shell-cwd-normalization.md` removed; routing line removed |

Protected lines were not touched: principle 1, Common Anti-Patterns, Quick Review Pass, and the rest of `core-principles.md`; `workspace-troubleshooting/SKILL.md` core rules; the three process runbooks. The remaining principles were renumbered 2 through 8 so the list stays contiguous. No validator required-path list names any removed file, so `validate_harness_package.py` is unchanged.

## Caveats recorded as graded, not adjudicated

- Ceiling: on five of seven sections both models detect every planted defect with no guidance loaded. As in the archived Rust block, the fixtures are the section's own check list, the most favorable case for the guidance, and the models apply the checks unaided. The ceiling is the finding for a content-redundancy question; it does not test subtler mixed-defect diffs or generation-time behavior.
- PowerShell JSON lift rests on partials for remediation route: every arm-A partial (Fable 6, Astra 6, plus one Astra arm-B partial) named the mechanism (Write-Output unrolling, `@()` masking) and prescribed a different working remediation (`-NoEnumerate` plus a parsed-type check, or dropping the re-pipe) rather than the key's raw-framing check on Windows PowerShell 5.1. Graders flagged two rows as key-errata candidates. Under the pre-registered rule the outcome is COMPRESS either way; had those partials been scored as hits, the section would be DELETE. The compressed text is what ships.
- npm locks arm B partials (Fable, 3 cells): responses went straight to `taskkill /F` on the identified PID without the graceful-stop step the runbook orders; this is the only place the full section scored below the control.
- Decoy `cp-9-c2` is a key error: its diff omits an import it uses, and reviewers in every arm correctly blocked on it (graders flagged it as a key-errata candidate in all six cells). Per protocol it is invalidated; it inflates cp-9 FP rates equally across arms and does not change any verdict. `key-errata.md` records it.
- Astra arm-C FP regression on cp-9 comes from a single decoy finding (`cp-9-c1`, one cell); the section is DELETE, so no adoption was at stake.
- Seed variance was zero on every cell pair except the sub-ceiling arm-A cells, consistent with batch 2's pre-registered two-seed choice.

## Remaining sections

The pre-registered cap ("if every section in the pilot shows arm A at ceiling, the user may cap the remainder at one seed") is not met: Fable arm A is below ceiling on the PowerShell JSON (0.88) and shell cwd (0.92) runbooks. The fourteen unmeasured sections therefore run at two seeds (2,688 review calls plus grading) unless ebigunso records a different cap or stops here. No outcome is inferred for any unmeasured section.

Records commit: see the plan's Progress Log for the hashes.
