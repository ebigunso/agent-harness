# Guidance-class ablation: outcome (pilot, 2026-09-08)

Pre-registered protocol: `protocol.md` (frozen 2026-09-07); fixtures per `fixture-plan.md` and `manifest.yaml`; scorer `score.py`. This record covers the pre-registered pilot: the five Windows runbooks and core principles 2 and 9. The remaining fourteen sections (principles 3 through 8 and 10, gates 1 through 7) have not run; see "Remaining sections" below.

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

The pre-registered cap ("if every section in the pilot shows arm A at ceiling, the user may cap the remainder at one seed") is met: arm A is 1.00 on every pilot section on both models. The cap is an option for ebigunso to record, not an automatic change; until recorded, the fourteen unmeasured sections run at two seeds (2,688 review calls plus grading). No outcome is inferred for any unmeasured section.

## Records

Transcripts: `06b047e` (Astra round 1), `254ed81` (Fable), `2b67d98` (reruns, with superseded outputs). Grades: round 1 `41e99e1` (Astra) and `7602c63` (Fable); round 2 and the blind mappings `2b67d98`; the adjudication and the reproducible aggregation path land with this revision. Every commit named is in the ancestry of the commit that carries this record.
