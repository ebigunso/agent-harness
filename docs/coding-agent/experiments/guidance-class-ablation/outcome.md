# Guidance-class ablation: outcome (pilot 2026-09-08; remaining sections 2026-09-09)

Pre-registered protocol: `protocol.md` (frozen 2026-09-07); fixtures per `fixture-plan.md` and `manifest.yaml`; scorer `score.py`. The first part of this record covers the pre-registered pilot (the five Windows runbooks and core principles 2 and 9). The second part, "Remaining sections", covers principles 3 through 8 and 10 and gates 1 through 7, run at the one-seed cap ebigunso recorded on 2026-09-08.

## Fleet, runs, and grading

- Models: GPT-6 Astra (codex-cli 0.153.4, `codex exec --ephemeral --disable plugins --disable hooks -c project_doc_max_bytes=0 -c web_search="disabled" -s read-only`, user `~/.codex/AGENTS.md` moved aside for each run window and restored with a matching SHA-256; runner `run/run_astra.sh`) and Claude Fable 5.1 (Claude Code CLI 2.1.263, `claude -p --restricted --disallowedTools "*" --strict-mcp-config` with an empty MCP config, a fixed one-line system prompt, one turn, no session persistence, run from an empty directory; runner `run/run_fable.sh`; mean 1,146 input and 1,245 output tokens per cell, $49.07 for the half). Delta from ADR-I-0004's fleet (Fable 5, Sol 5.6, Luna 5.6): the two current frontier models, per plan Q1.
- Cells: 7 sections x 3 arms x 16 fixtures x 2 seeds x 2 models = 1,344; all completed with exit 0 and a non-empty response. Transcripts: `work/astra/`, `work/fable/` (with `work/fable-json/` carrying usage).
- Reruns (2026-09-08, after the first Task_5 review): 23 Astra control cells had used the Responses web-search tool (21 in the PowerShell JSON section, 2 in npm locks), which the protocol's "load nothing else" condition forbids; they were rerun with `web_search="disabled"`, and no cell in the final set searched. Decoy `cp-9-c2` omitted the import its diff uses; the fixture gained the import as context and its 12 cells (both models, all arms) were rerun. Superseded outputs are kept under `work/rerun-superseded/`.
- Grading: blinded. `run/blind.py` keeps only the model's response under a random id with the fixture id visible (needed to apply the key) and the arm and seed hidden; the mapping (`work/blind/<model>/mapping.json`, committed) stays with the Orchestrator. Two grading rounds by Claude Fable 5.1 grader agents, two per section per model, each grading 48 responses against `keys/<section>.md` and the fixtures only. Round 1 (`work/grades-v1/`, `work/results-*-v1.yaml`) graded runbook remediations against the key's route. Round 2 (`work/grades/`, `work/results-*.yaml`) regraded every runbook section and cp-9 under the ruling below and the rerun cells; cp-2 grades carry over from round 1 (its cells did not change). `run/unblind.py` merged 672 records per model with zero unknown, duplicate, or mismatched ids; it carries cp-2 forward from `work/results-<model>-v1.yaml` explicitly (printed on each run) and applies `work/adjudications.yaml` on top of the grader files, whose originals are untouched. One adjudication exists: Astra `A-rb-windows-python-console-encoding-02-s1`, graded 0.5 in round 2 because its primary fix (default JSON ASCII escaping, value preserved and round-trip confirmed) differs from the key's UTF-8 stdout route; the fixture does not require a literal emoji, so under the ruling it is a hit. Deviation from `protocol.md` ("one grader per model per arm"): graders were split per section instead, because a per-arm grader would know the arm; per-section blinding is stricter.
- Grading ruling (ebigunso, 2026-09-08, after round-1 results existed; recorded in the plan's Decision Log): a runbook response that names the planted mechanism and prescribes any remediation that would work scores a hit; the key's preferred route no longer separates hit from partial. Applied uniformly to every runbook section, both models, all arms. Decision thresholds unchanged.
- A first attempt to run Fable cells as Claude Code subagents was abandoned after 16 cells: each carried about 54,000 tokens of session preamble, which is neither clean nor affordable. Those 16 outputs are set aside in `work/fable-subagent-trial/` and were not graded.

## Results (round 2; detection = mean hit score over 12 planted fixtures x 2 seeds; FP = false-positive findings per decoy review, 4 decoys x 2 seeds)

| Section | Model | A det | B det | C det | A FP | B FP | C FP |
|---|---|---|---|---|---|---|---|
| cp-2 root-cause fixes | Fable | 1.00 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 |
| cp-2 root-cause fixes | Astra | 1.00 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 |
| cp-9 explicit safe failures | Fable | 1.00 | 1.00 | 1.00 | 1.12 | 0.25 | 0.38 |
| cp-9 explicit safe failures | Astra | 1.00 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 |
| rb npm EPERM locks | Fable | 1.00 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 |
| rb npm EPERM locks | Astra | 1.00 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 |
| rb Docker gRPC IPv6 | Fable | 1.00 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 |
| rb Docker gRPC IPv6 | Astra | 1.00 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 |
| rb Python console encoding | Fable | 1.00 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 |
| rb Python console encoding | Astra | 1.00 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 |
| rb PowerShell JSON cardinality | Fable | 1.00 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 |
| rb PowerShell JSON cardinality | Astra | 1.00 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 |
| rb shell cwd normalization | Fable | 1.00 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 |
| rb shell cwd normalization | Astra | 1.00 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 |

Round-1 figures, for the record (key-route grading, searching control cells included): Fable arm A was 0.88 on PowerShell JSON and 0.92 on shell cwd, Astra arm A 0.88 on PowerShell JSON; every other cell was within 0.06 of round 2. Under round-1 grading PowerShell JSON would have been COMPRESS: Fable's control cells (never rerun) stayed at 0.88 under the key-route reading, so the search-free rerun alone would not have changed the verdict; the grading ruling is what moves it to DELETE, and the rerun removes the contamination from the control's evidence.

## Rule applied (worst model = lowest arm-A detection; ties evaluated on every tied model, most protective outcome stands)

| Section | Worst model | dB | dC | FP guard | Outcome | Edit made |
|---|---|---|---|---|---|---|
| cp-2 | tie (both 1.00) | +0pp | +0pp | pass | DELETE | section "2) Prefer Root-Cause Fixes Over Symptom Patches" removed from `core-principles.md` |
| cp-9 | tie (both 1.00) | +0pp | +0pp | pass (B and C below A on Fable; Astra 0) | DELETE | section "9) Make Failure Modes Explicit and Safe" removed from `core-principles.md` |
| rb npm EPERM locks | tie (both 1.00) | +0pp | +0pp | pass | DELETE | `windows-npm-eperm-locks.md` removed; routing line removed |
| rb Docker gRPC IPv6 | tie (both 1.00) | +0pp | +0pp | pass | DELETE | `windows-docker-grpc-localhost-ipv6.md` removed; routing line removed |
| rb Python console encoding | tie (both 1.00) | +0pp | +0pp | pass | DELETE | `windows-python-console-encoding.md` removed; routing line removed |
| rb PowerShell JSON cardinality | tie (both 1.00) | +0pp | +0pp | pass | DELETE | `powershell-json-array-cardinality.md` removed; routing line removed |
| rb shell cwd normalization | tie (both 1.00) | +0pp | +0pp | pass | DELETE | `persistent-shell-cwd-normalization.md` removed; routing line removed |

Protected lines were not touched: principle 1, Common Anti-Patterns, Quick Review Pass, and the rest of `core-principles.md`; `workspace-troubleshooting/SKILL.md` core rules; the three process runbooks. The remaining principles were renumbered 2 through 8 so the list stays contiguous. No validator required-path list names any removed file, so `validate_harness_package.py` is unchanged.

## Caveats

- Ceiling: on all seven sections both models detect every planted defect with no guidance loaded (one Astra control cell reached that score by adjudication under the ruling; the grader's 0.5 is preserved in `work/grades/`). As in the archived Rust block, the fixtures are the section's own check list, the most favorable case for the guidance, and the models apply the checks unaided. The ceiling is the finding for a content-redundancy question; it does not test subtler mixed-defect diffs, larger diffs where salience competes, or generation-time behavior.
- Control-arm tool use: with web search disabled, some Astra control cells still ran local shell commands in the read-only sandbox to confirm a diagnosis (for example a PowerShell conversion check). The protocol forbids loading other references, not executing commands; this is recorded, not treated as a deviation.
- cp-9 decoy false positives on Fable are highest in the control arm (1.12 per review) and lower with the section loaded (0.25, 0.38): the control demanded tests and broader timeout handling on clean diffs more often. Under DELETE no adoption is at stake, and the FP guard compares B and C against A, so it passes.
- `cp-9-c2`: authoring error (missing import context), fixed and rerun; see `key-errata.md`. Round-2 grades on the corrected fixture are used throughout; no round-2 grader raised the missing import. The corrected decoy still draws false positives on Fable (control 1 and 3, arms B and C fewer): demands for tests and logging, not the import, and they are counted as graded.
- Seed variation: in round 2 every planted-fixture cell pair agrees (the one Astra Python-encoding disagreement, fixture 02, closed under the adjudication); decoy false-positive counts on Fable cp-9 vary between seeds.

## Remaining sections

The pre-registered cap ("if every section in the pilot shows arm A at ceiling, the user may cap the remainder at one seed") is met: arm A is 1.00 on every pilot section on both models. ebigunso recorded the one-seed cap on 2026-09-08 (plan Decision Log) before any of those cells ran; the fourteen sections run at one seed (1,344 review calls plus grading). No outcome is inferred for any unmeasured section until it is measured.

## Records

The branch was rebased onto main after the pilot, so the pilot commits carry rebased hashes: transcripts `8f3455c` (Astra round 1), `a4ae72c` (Fable), `794a48a` (reruns, with superseded outputs); grades round 1 `94a4c3f` (Astra) and `265f2b0` (Fable); round 2 and the blind mappings `794a48a`; the adjudication and the reproducible aggregation path in the commit that follows. Every hash named here is in the ancestry of the commit that carries this record.

## Remaining sections (2026-09-09, one seed)

- Cells: 14 sections x 3 arms x 16 fixtures x 1 seed x 2 models = 1,344; all completed with exit 0 (39 Fable cells hit a usage-limit 429 mid-run and were rerun after the reset; a wedged runner was relaunched once with no lost cells). Same runners and flags as the pilot; Astra with `web_search="disabled"` throughout, loader aside and hash-restored on each run.
- Fixtures: batch 1 (principles) and batch 2 (gates) authored by the Codex worker under the pilot rulings, validated by `validate_pilot.py` against the frozen revision 2710486 (arm-B texts byte-equal to the original sections; 336 fixtures, 21 keys, 42 arms).
- Grading: one blinded Claude Fable 5.1 grader per section per model (48 responses each, review rule: hit requires the planted mechanism at the planted location and the key's fix direction); 28 graders. Pilot sections carried forward from `work/results-<model>-pilot.yaml` by `run/unblind.py` (printed on each run). No adjudication was applied to these sections.

| Section | Model | A det | B det | C det | A FP | B FP | C FP |
|---|---|---|---|---|---|---|---|
| cp-3 small cohesive changes | Fable | 1.00 | 1.00 | 1.00 | 0.00 | 0.25 | 0.00 |
| cp-3 small cohesive changes | Astra | 0.79 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 |
| cp-4 readability | Fable | 1.00 | 1.00 | 1.00 | 1.50 | 1.25 | 1.00 |
| cp-4 readability | Astra | 0.96 | 1.00 | 0.96 | 0.00 | 0.00 | 0.00 |
| cp-5 invariants | Fable | 1.00 | 1.00 | 1.00 | 1.50 | 1.00 | 1.75 |
| cp-5 invariants | Astra | 1.00 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 |
| cp-6 contract fidelity | Fable | 1.00 | 1.00 | 1.00 | 1.00 | 0.50 | 1.00 |
| cp-6 contract fidelity | Astra | 1.00 | 1.00 | 1.00 | 0.25 | 0.25 | 0.25 |
| cp-7 testability | Fable | 0.96 | 1.00 | 1.00 | 0.25 | 0.25 | 0.00 |
| cp-7 testability | Astra | 0.88 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 |
| cp-8 complexity | Fable | 1.00 | 1.00 | 1.00 | 1.25 | 1.00 | 0.75 |
| cp-8 complexity | Astra | 0.92 | 1.00 | 1.00 | 0.25 | 0.25 | 0.25 |
| cp-10 easier to change | Fable | 1.00 | 1.00 | 1.00 | 0.50 | 0.50 | 0.50 |
| cp-10 easier to change | Astra | 1.00 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 |
| ag-1 responsibility boundaries | Fable | 0.88 | 1.00 | 1.00 | 0.75 | 0.00 | 0.25 |
| ag-1 responsibility boundaries | Astra | 1.00 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 |
| ag-2 dependency direction | Fable | 1.00 | 1.00 | 1.00 | 1.50 | 0.00 | 0.50 |
| ag-2 dependency direction | Astra | 1.00 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 |
| ag-3 cohesive change surface | Fable | 1.00 | 1.00 | 1.00 | 0.50 | 0.75 | 1.00 |
| ag-3 cohesive change surface | Astra | 1.00 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 |
| ag-4 interface contracts | Fable | 1.00 | 1.00 | 1.00 | 2.00 | 1.25 | 2.75 |
| ag-4 interface contracts | Astra | 0.96 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 |
| ag-5 data and state integrity | Fable | 1.00 | 1.00 | 1.00 | 0.25 | 0.25 | 0.75 |
| ag-5 data and state integrity | Astra | 1.00 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 |
| ag-6 failure containment | Fable | 1.00 | 1.00 | 1.00 | 1.25 | 1.75 | 0.50 |
| ag-6 failure containment | Astra | 0.96 | 1.00 | 1.00 | 0.50 | 0.00 | 0.75 |
| ag-7 observability | Fable | 1.00 | 1.00 | 1.00 | 2.50 | 2.00 | 1.25 |
| ag-7 observability | Astra | 1.00 | 1.00 | 1.00 | 0.00 | 0.00 | 0.00 |

### Rule applied (worst model = lowest arm-A detection)

| Section | Worst model | dB | dC | Arm-C FP guard (both models) | Outcome | Edit made |
|---|---|---|---|---|---|---|
| cp-3 | Astra (0.79) | +21pp | +21pp | pass (C 0.00 vs A 0.00 on both) | COMPRESS | principle "Keep Changes Small, Cohesive, and Reversible" body replaced with `arms/cp-3-C.md` |
| cp-4 | Astra (0.96) | +4pp | +0pp | n/a | DELETE | section removed |
| cp-5 | tie (1.00) | +0pp | +0pp | n/a | DELETE | section removed |
| cp-6 | tie (1.00) | +0pp | +0pp | n/a | DELETE | section removed |
| cp-7 | Astra (0.88) | +12pp | +12pp | pass (Fable C 0.00 vs A 0.25; Astra 0.00 vs 0.00) | COMPRESS | principle "Build for Testability and Verifiability" body replaced with `arms/cp-7-C.md` |
| cp-8 | Astra (0.92) | +8pp | +8pp | n/a | DELETE | section removed |
| cp-10 | tie (1.00) | +0pp | +0pp | n/a | DELETE | section removed |
| ag-1 | Fable (0.88) | +12pp | +12pp | pass (Fable C 0.25 vs A 0.75; Astra 0.00 vs 0.00) | COMPRESS | Gate 1 body replaced with `arms/ag-1-C.md` |
| ag-2 | tie (1.00) | +0pp | +0pp | n/a | DELETE | gate removed |
| ag-3 | tie (1.00) | +0pp | +0pp | n/a | DELETE | gate removed |
| ag-4 | Astra (0.96) | +4pp | +4pp | n/a | DELETE | gate removed |
| ag-5 | tie (1.00) | +0pp | +0pp | n/a | DELETE | gate removed |
| ag-6 | Astra (0.96) | +4pp | +4pp | n/a | DELETE | gate removed |
| ag-7 | tie (1.00) | +0pp | +0pp | n/a | DELETE | gate removed |

Resulting files: `core-principles.md` keeps principle 1 (protected) plus the two compressed principles, renumbered 1 through 3, with Common Anti-Patterns, Durable-Code Hygiene, Quick Review Pass, and Non-Goals untouched. `architecture-gates.md` keeps its Purpose, How to Use, Decision Guidance, Output Template, and Non-Goals sections (protected) with Gate 1 compressed and gates 2 through 7 removed. Routing in `engineering-quality-baselines/SKILL.md` is unchanged because both files remain. Package validation and smoke tests pass after the edits.

### Caveats for this part

- Three sections show real lift on the worst model, the first in this study: cp-3 (the Astra control accepted scope-coupled changes without requiring a split in three cells), cp-7 (both models accepted a formatting check as behavioral evidence in one cell each; Astra also chose a set/restore fixture over a seam in one cell), ag-1 (the Fable control endorsed domain policy inside a decoder and routed a scheduler bypass without moving policy). The grader notes are in `work/grades/`.
- cp-7 is decision-sensitive to the grading rule: the Astra partial on `cp-7-03` is a remediation-route disagreement with the mechanism named. ebigunso's 2026-09-08 ruling (any working remediation is a hit) was stated for runbook sections; applied as graded here, cp-7 is COMPRESS at +12pp; if the ruling extended to review sections that cell would be a hit and cp-7 would be DELETE at +8pp. Recorded, not adjudicated; the compressed text ships unless ebigunso extends the ruling.
- One seed makes the FP guard coarse: with four decoys per section, one extra blocking finding moves an arm's FP rate by 0.25, above the 0.10 threshold, so `score.py` flags FP regressions on eight non-adopted arms (for example Fable arm C on ag-4, 2.75 vs 2.00). None of them is an adopted arm; every adopted arm-C text passes the guard on both models. The flags are reported, not acted on.
- Fable's decoy false-positive rates are high across the gate sections in every arm (up to 2.50 findings per decoy review on the ag-7 control): Fable demands tests, logging, and rollback notes on clean diffs regardless of guidance. That is a model trait, not an arm effect, and does not enter the detection rule.
- Seeds: one per cell by the recorded cap, so cross-seed variance is not measured here; the pilot's two-seed cells showed zero variance on planted fixtures.

### Records

Transcripts and Astra grades for these sections: `9c931a0`. Fable grades, the edits, and this section: `f1f913e`.
