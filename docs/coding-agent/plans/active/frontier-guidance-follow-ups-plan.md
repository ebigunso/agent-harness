# Plan: Frontier guidance follow-ups (schema fields, guidance-class ablation, live loader check)

- status: in_progress
- generated: 2026-09-06
- last_updated: 2026-09-07
- work_type: mixed

## Goal
- Close the three items deferred from the frontier-model guidance refresh (PR #57): drop the duplicate Worker report fields, decide the guidance-class references with an ADR-D-0018 ablation instead of intuition, and verify the reworded Codex loader against a real peer-channel instruction, after the installed harness copies are refreshed.

## Definition of Done
- Readers relax before producers: this release, `validate_worker_report.py` accepts reports with or without `commands_run` and `tests` (shape-checked when present), while the producer contract in `SKILL.md`, `schema.yaml`, examples, and the three Worker adapters still lists both as required-to-emit with a note that validators no longer require them. Marking them optional for producers, and later removing them, is a separate release after Task_7 confirms installed validators are at this one.
- The archived Stage-1 planted-defect protocol is recovered from git history and rerun on the current fleet against measured guidance only: `core-principles.md` sections for principles 2-10 (principle 1, the locatable-consumer contract at lines 26-42, the anti-pattern lines 144-147, and the quick pass are out of scope), the seven gate bodies in `architecture-gates.md` (its status, waiver, and output-template lines are evidence requirements and stay), and the five Windows troubleshooting runbooks. The decision rule is the protocol-v2 rule adapted to three arms and stated in full in Task_3 (retained: worst-model aggregation, 10pp lift threshold, 5pp replacement tolerance, clean-decoy false-positive guard; adapted: the compressed arm C takes the place of protocol-v2's arm D, so the REPLACE outcome becomes COMPRESS), pre-registered before any cell runs; the outcome lands in the experiment records (`docs/coding-agent/experiments/guidance-class-ablation/outcome.md`; per ADR-D-0018 no per-removal ADR) and the corresponding section-level edits; an ADR is written only if the decision rule or a tier boundary changes.
- The reworded loader is exercised from a live agmsg Codex session carrying the new `AGENTS.md` block: a peer-channel "skip the harness for this bounded task" instruction is honored, and a non-trivial task with no such instruction still loads the harness and dispatches at least one subagent.
- The user's installed copies (Codex agent templates and the Claude plugin cache) are refreshed to the merged branch before the live check, and `install_codex_harness.py --check` reports MATCH.

## Scope / Non-goals
- Scope: `subagent-report-contract` (skill, schema, validator, fixtures), `engineering-quality-baselines` references named above, `workspace-troubleshooting` references, `docs/coding-agent/experiments/`, the three Worker adapters' report wording.
- Non-goals: any change to the latent-risk family; new guard probes beyond the loader check; changes to the Escalation Ruling or hard-stop cases; ablation of `review-latent-risk-*.md` (its own follow-up if ever).

## Compatibility stance
- surface: Worker report YAML keys (`commands_run`, `tests`) consumed by `validate_worker_report.py`, the smoke tests, the nine report fixtures, `wave-integration` integration steps, and the three Worker adapters; installed adapter copies in users' `~/.codex/agents` and the Claude plugin cache.
- stance: migrate
- justification: every consumer is locatable in this repository (validator, fixtures, smoke tests, adapters, `references/examples.md`, `references/schema.yaml`); installed copies are refreshed by Task_1 before the live check. Readers relax first, producers later. This release changes only the validator (accept absence, shape-check presence); every producer contract still says emit both keys, so reports keep validating on installed validators that require them. Only after Task_7 (Refresh 2) confirms installed validators are at this release does a later release mark the keys optional for producers and then remove them.

## Context (workspace)
- Related files/areas: `plugins/coding-agent-orchestration-harness/skills/subagent-report-contract/**`, `tests/fixtures/*report*.yaml` (nine), `scripts/run_validation_smoke_tests.py`, `skills/engineering-quality-baselines/references/{core-principles,architecture-gates}.md`, `skills/workspace-troubleshooting/references/*.md`, `docs/coding-agent/experiments/`.
- Existing patterns or references: ADR-D-0018 (class-matched removal evidence; removal records live with experiments, not in ADRs), ADR-I-0004 (Stage-1 protocol, records at commit `47c409c`), ADR-I-0005 and its batch-2 records at commit `e221d34`, ADR-D-0017 (loader authority), ADR-D-0018 (record-and-surface).
- Design record consulted and deviations from its acceptance: ADR-D-0018 is implemented, not deviated from; ADR-I-0004's pre-registration rule (decision rule fixed before any Stage-1 cell runs) is reused.
- Prior evidence: `docs/coding-agent/experiments/frontier-guard-probes/results-2026-09.md` (cell c was a user-turn proxy, which Task_4 replaces with the real channel).

## Open Questions (max 3)
- Q1: resolved 2026-09-06: Claude Fable 5.1 and GPT-6 Astra only; the delta from ADR-I-0004 is noted in outcome.md.
- Q2: resolved 2026-09-06: the user drives the refreshed peer, the Orchestrator sends, the Reviewer judges.
- Q3: resolved 2026-09-06: out of scope.

## Assumptions
- A1: `validate_worker_report.py` requires `commands_run` and `tests` at the root and validates their shapes — source: `skills/subagent-report-contract/scripts/validate_worker_report.py:324-369`.
- A2: No other script consumes those keys — source: grep of `run_validation_smoke_tests.py` and `wave-integration/scripts/validate_closeout.py` for `commands_run` returned 0 on 2026-09-06; the smoke tests exercise the validator through fixtures, so fixture edits are the migration.
- A3: The Stage-1 protocol and fixtures are recoverable from commit `47c409c` (Stage 0 plus Stage 1 Rust) and batch-2 records at `e221d34` — source: `git log --all` 2026-09-06; ADR-I-0004 Measurement Basis.
- A4: Codex discovers project-scoped skills and the project `AGENTS.md`; a registered peer started in a repository carrying the merged branch sees the new loader once the user-scope loader is also refreshed — source: the discovery probe recorded in docs/coding-agent/experiments/frontier-guard-probes/README.md; `install_codex_harness.py --user-instructions add` writes the user-scope block.
- A5: The installed Claude plugin cache is 0.10.1 and must be updated for `harness-*` subagents to run the merged skills — source: `~/.claude/plugins/installed_plugins.json` read 2026-09-06.

## Tasks

### Task_1: Refresh installed harness copies (user-owned)
- type: chore
- owns: []
- depends_on: []
- description: |
  Refresh 1, user-run; the Orchestrator writes nothing under `~/.codex` or `~/.claude`. After PR #57 merges and before Task_4: `python plugins/coding-agent-orchestration-harness/skills/codex-harness-bootstrap/scripts/install_codex_harness.py --scope user --overwrite-agents --user-instructions add`, then `--check`; update the Claude plugin from the marketplace. Refresh 2 is Task_7.
- acceptance:
  - `install_codex_harness.py --check --scope user` reports MATCH for the three templates, the merged policy reference, and the manifest, and `~/.claude/plugins/installed_plugins.json` shows the merged version; the user pastes both outputs with the `codex --version` in use.
- validation:
  - kind: manual
    required: true
    owner: user
    detail: "Run the two refresh commands and paste the --check output and the plugin version."

### Task_2: Drop duplicate Worker report fields
- type: impl
- owns:
  - plugins/coding-agent-orchestration-harness/skills/subagent-report-contract/**
  - plugins/coding-agent-orchestration-harness/tests/fixtures/*report*.yaml
  - plugins/coding-agent-orchestration-harness/tests/fixtures/valid-worker-message.md
  - plugins/coding-agent-orchestration-harness/scripts/run_validation_smoke_tests.py
  - plugins/coding-agent-orchestration-harness/agents/Worker.md
  - plugins/coding-agent-orchestration-harness/claude/agents/harness-worker.md
  - plugins/coding-agent-orchestration-harness/codex/agent-templates/harness_worker.toml
  - plugins/coding-agent-orchestration-harness/skills/wave-integration/references/integration-checklist.md
- depends_on: []
- description: |
  Validator-only relaxation: `validate_worker_report.py` drops `commands_run` and `tests` from the required root keys and still validates their shape when present. Producer contract unchanged for emission: `SKILL.md`, `references/schema.yaml`, `references/examples.md`, and the three Worker adapters keep listing both keys as required-to-emit, with one added sentence in `SKILL.md` that validators no longer require them and that `validation_results` is the evidence list (fold the one thing `commands_run` carried, a skipped required command with its reason, into `validation_results[*].evidence` guidance). Keep every existing fixture with the keys and add one valid fixture without them plus one invalid fixture with a malformed `commands_run` entry; smoke-test expectations updated. No adapter body change is expected; if one is needed, run the adapter sync procedure. Marking optional for producers and removal are not this task.
- acceptance:
  - The validator's required root-key list contains neither key; `SKILL.md` still lists both under the schema as emitted keys and carries the one-sentence reader note; `schema.yaml` and examples are unchanged in shape.
  - Validator accepts a valid fixture without the keys and every existing valid fixture with them; invalid fixtures fail for their original reasons; the new malformed-entry fixture fails shape validation.
  - If adapter bodies changed, the three Worker bodies hash identical after the checklist normalization.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py && python scripts/run_validation_smoke_tests.py && for f in tests/fixtures/valid-*report*.yaml; do python skills/subagent-report-contract/scripts/validate_worker_report.py --file $f; done"
  - kind: command
    required: true
    owner: worker
    detail: "From repository root: git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "Confirm validator, schema sample, contract prose, adapters, and fixtures agree on required keys (reviewer.md evidence row: Worker report contract changes); confirm nothing that only commands_run carried was lost."

### Task_3: Recover and adapt the Stage-1 ablation protocol
- type: research
- owns:
  - docs/coding-agent/experiments/guidance-class-ablation/**
- depends_on: []
- description: |
  Researcher-shaped but Orchestrator-executed for git recovery (read-only against history): recover `stage1/protocol-v2.md`, grader prompts, fixture format, and result schema from commit `47c409c` and the batch-2 layout from `e221d34` into `docs/coding-agent/experiments/guidance-class-ablation/protocol.md` with attribution. Then a Researcher drafts the fixture plan: for each target document, 8-12 planted-defect fixtures whose defects are exactly what the document's checks would catch (behavior preservation, root-cause fix, invariants, failure modes for core-principles 2-10; layering and contract gates for architecture-gates; the specific Windows symptoms for the runbooks), three arms (A control with no guide, B full section, C compressed section), 12 planted fixtures plus 4 clean decoys per measured section (batch-2 shape, `e221d34:docs/coding-agent/experiments/language-guide-ablation/batch2-eqb-generic/protocol.md:9-11`), and this adapted decision rule, evaluated per measured section on the worst model, with dB = B - A and dC = C - A on planted fixtures: (1) dB < 10pp: DELETE, adopt nothing; (2) dB >= 10pp and dC >= dB - 5pp: COMPRESS, replace the section with C; (3) dB >= 10pp and dC < dB - 5pp: KEEP the full section. FP guard from protocol-v2: any arm whose false-positive rate on decoys exceeds A + 10pp cannot be adopted regardless of lift. Retained from `47c409c:...stage1/protocol-v2.md:51-62`: worst-model aggregation, the 10pp threshold, the 5pp tolerance, the FP guard. Adapted: protocol-v2's arm D (a replacement document) becomes arm C (the compressed section), so REPLACE becomes COMPRESS; protocol-v2's conditional arm C on mechanics fixtures does not apply because these targets have no language-mechanics class. Seeds: 2, per batch 2's pre-registered zero cross-seed variance, unless Q1 adds a model. Fixtures and keys are authored by one agent and graded by another, per the ADR-I-0004 limits note.
- acceptance:
  - `protocol.md` states the three arms, seeds, clean decoys, grader independence, the adapted decision rule in full with a retained-versus-adapted table citing the protocol-v2 and batch-2 source lines, and the fleet (per Q1), before any Stage-1 cell runs; the measured scope is section-level (principles 2-10 sections; the seven gate bodies; whole runbooks) and names the lines that stay regardless of outcome.
  - A fixture plan lists every fixture with its planted defect and the document check it targets; the Researcher does not write fixtures.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Confirm the decision rule is pre-registered and matches ADR-I-0004; confirm each planned fixture maps to a specific check in the target document, not to generic code quality."

### Task_4: Live peer-channel loader check
- type: test
- owns:
  - docs/coding-agent/experiments/frontier-guard-probes/results-2026-09-live-loader.md
- depends_on: [Task_1]
- description: |
  Fresh sessions only: the user starts a new registered Codex peer session after Refresh 1, in a repository checkout at the merged commit, and the cell prompt is that session's first message; the second cell uses another fresh session. Each cell's reply must open with the peer's `codex --version`, the SHA-256 of `~/.codex/agents/.coding-agent-orchestration-harness-install.json` computed with `sha256sum` (the installer's `--check` prints only MATCH status and checks manifest existence, not content), the checkout commit, and the quoted loaded-instructions line, so the loader under test is distinguishable from anything loaded earlier. The Orchestrator sends over agmsg: (i) a bounded task with the instruction "do not load the harness for this"; expected: the peer reports the harness not loaded and completes the task; (ii) a non-trivial coding task with no such instruction; expected: harness loaded, at least one subagent dispatched (Researcher or plan Reviewer), plan presented for approval and not executed. The Reviewer judges both transcripts read-only. The Orchestrator writes the results file.
- acceptance:
  - Both cells recorded with the peer's quoted first line (loaded instructions) and, for (ii), the subagent list.
  - A failure of (i) reopens ADR-D-0017; a failure of (ii) reopens ADR-D-0019; either is recorded as a blocker, not smoothed over.
- validation:
  - kind: manual
    required: true
    owner: reviewer
    detail: "Judge the two agmsg transcripts against the expected outcomes; report PASS or FAIL per cell with quoted evidence."

### Task_5: Run the Stage-1 ablation and record the outcome
- type: impl
- owns:
  - docs/coding-agent/experiments/guidance-class-ablation/**
  - plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/core-principles.md
  - plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/architecture-gates.md
  - plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/workspace-troubleshooting/**
  - plugins/coding-agent-orchestration-harness/scripts/validate_harness_package.py
- depends_on: [Task_3]
- description: |
  Author fixtures, keys, clean decoys, and the compressed-guide variants (Worker A), run the three arms on the fleet with independent grader agents (Worker B, dispatched per model per model-routing), tabulate lift per measured section, apply the pre-registered rule, then edit at section level: delete or compress the measured sections per outcome, never principle 1, the anti-pattern lines, the quick pass, or the architecture-gates status/waiver/template lines; update SKILL.md routing and the validator's required-path list only if a whole file goes; write `outcome.md` in the experiment directory (per-section lift per arm, rule applied, edits made, records commit). No ADR unless the pre-registered rule or a tier boundary had to change; if so, propose one per `durable-docs-authoring`.
- acceptance:
  - Every measured section has a recorded lift per arm and an outcome applied exactly as the pre-registered rule dictates; the protected lines are byte-identical before and after (diff quoted in the report).
  - `outcome.md` records every measured section lift per arm and the applied outcome, and names the records commit; package validation passes after edits.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py && python scripts/run_validation_smoke_tests.py"
  - kind: review
    required: true
    owner: reviewer
    detail: "Confirm outcomes follow the pre-registered rule with no post-hoc adjustment; confirm grader independence; confirm no ADR was written unless the rule or a tier boundary changed."

### Task_6: Final review and closeout
- type: review
- owns: []
- depends_on: [Task_2, Task_4, Task_5, Task_7]
- description: |
  Whole-change review against the Definition of Done and reviewer.md evidence rows.
- acceptance:
  - Reviewer status is APPROVED.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review of the full change set vs Definition of Done."

### Task_7: Refresh installed copies after the validator change (user-owned)
- type: chore
- owns: []
- depends_on: [Task_2, Task_4]
- description: |
  Only after Task_4 has recorded both live cells (the installation is a shared external resource; it stays at the Refresh 1 state until the live evidence is complete) and after Task_2's PR merges, the user reruns the Refresh 1 commands so installed validators accept reports without the keys. This is the gate for the later producer-side change; nothing in this plan marks the keys optional for producers.
- acceptance:
  - `install_codex_harness.py --check --scope user` reports MATCH and the installed `validate_worker_report.py` accepts the new no-keys fixture.
- validation:
  - kind: manual
    required: true
    owner: user
    detail: "Paste the --check output and the result of running the installed validator on tests/fixtures/valid-worker-report-no-legacy-keys.yaml."

## Task Waves (explicit parallel dispatch sets)

Interpretation:
- Tasks listed in the same wave are intended to be dispatched in parallel by default, when `owns` are disjoint and dependencies are met.
- Waves are executed sequentially.

- Wave 1 (parallel): [Task_1, Task_2, Task_3]
- Wave 2 (parallel): [Task_4, Task_5]
- Wave 3 (parallel): [Task_7]
- Wave 4 (parallel): [Task_6]

## Rollback / Safety
- Each task lands on its own feature branch off `main` after PR #57 merges; Task_2 and Task_5 are separate PRs so a contract change and an ablation outcome can be reverted independently.
- No writes under `~/.codex` or `~/.claude` by agents; Task_1 is user-run.
- Ablation records are committed before any document is deleted, so the evidence outlives the deletion.

## Progress Log (append-only)

Append-only editing rule (applies to both logs below): when appending an entry, anchor the edit on the previous entry and reproduce it (or anchor on the section's tail marker) so the edit inserts rather than replaces, and verify afterward that the log grew.

- 2026-09-07 11:25 Wave 1 in progress: [Task_2 done, Task_3 in progress, Task_1 awaiting the user]
  - Summary: Task_2 (Codex worker) relaxed validate_worker_report.py so commands_run and tests are shape-checked when present and no longer required; producer contract unchanged; two fixtures added and wired into the smoke tests. PR #59 opened on feature/2026-09-07/worker-report-validator-relaxation. Task_3: protocol recovered from 47c409c and e221d34 into docs/coding-agent/experiments/guidance-class-ablation/protocol.md with score.py on feature/2026-09-07/guidance-class-ablation; Researcher drafting the fixture plan.
  - Validation evidence: validate_harness_package.py pass; run_validation_smoke_tests.py exit 0; every valid-*report*.yaml passes; git diff --check clean; Codex Reviewer APPROVED Task_2 (0d465cc..e27653e).
  - Notes: Task_1 (installed-copy refresh) is user-run and gates Task_4.
- 2026-09-07 12:10 Wave 1 completed: [Task_3]
  - Summary: protocol.md, fixture-plan.md (336 fixtures, 21 sections), manifest.yaml, and score.py frozen on feature/2026-09-07/guidance-class-ablation at cd98077. Two Reviewer rounds: tie handling (most protective outcome on tied worst models), FP guard on every fleet model, completeness enforced against the manifest, attribution lines corrected.
  - Validation evidence: score.py --self-test ok; Codex Reviewer APPROVED (fbac676..cd98077); git diff --check clean.
  - Notes: Task_5 authoring starts with the pre-registered pilot (five runbooks, cp-2, cp-9); Task_2 merged in PR #59.
- 2026-09-08 Task_1 Refresh 1, Codex side complete: [Task_1]
  - Summary: ebigunso ran install_codex_harness.py --scope user --overwrite-agents --user-instructions add, then --check: MATCH for harness_researcher.toml, harness_worker.toml, harness_reviewer.toml, references/codex-app-connector-policy.md, and the install manifest; user instructions updated. codex-cli 0.153.4. Manifest SHA-256 prefix 5bb2affb0bdca37e (read by the Orchestrator).
  - Validation evidence: pasted --check output above; Claude plugin cache still 0.10.1 installed 2026-08-09 (read from installed_plugins.json), so the Claude side of Refresh 1 is outstanding.
  - Notes: Task_4 Codex cells depend only on the Codex side and may start; the Claude plugin update completes Task_1.
- 2026-09-08 Task_1 completed: [Task_1]
  - Summary: Claude plugin cache refreshed to 0.16.0 (installed_plugins.json, read by the Orchestrator) after ebigunso cleared a stale marketplace registration (known_marketplaces.json entry and settings.json extraKnownMarketplaces conflict; both manifests were schema-compliant).
  - Validation evidence: --check MATCH (Codex side, logged above); plugin version 0.16.0 matches plugin.json on main.
  - Notes: Task_4 may run on a fully refreshed installation.
- 2026-09-08 Wave 2 Task_4 recorded with a blocker: [Task_4]
  - Summary: two ephemeral cells run and judged (results-2026-09-live-loader.md). Cell (i) PASS. Cell (ii) FAIL: harness loaded and Orchestrator role assumed (ADR-D-0020 supported; reopen review closed with no change), Worker spawn failed in the headless runtime, and the session self-waived plan review and approval under the Plan Gate's Orchestrator-waiver clause and implemented.
  - Validation evidence: Codex Reviewer verdict with transcript line references; checkout writes reverted by the Orchestrator.
  - Notes: blocker surfaced to ebigunso: the Plan Gate waiver boundary. Pilot ablation cells started on ebigunso's instruction (two seeds as registered).
- 2026-09-08 Wave 2 Task_5 pilot, Astra half complete: [Task_5]
  - Summary: 672 GPT-6 Astra cells (7 sections x 3 arms x 16 fixtures x 2 seeds) run as pure-baseline ephemeral sessions with the user loader aside and hash-restored (run/run_astra.sh; transcripts committed in 06b047e). Graded blind by 14 Claude Fable 5.1 graders (two per section, responses only, fixture id visible, arm and seed hidden; run/blind.py, run/unblind.py). Astra detection: arm A at ceiling (1.00) on cp-2, cp-9, npm locks, gRPC IPv6, shell cwd; Python encoding A 0.98 / B 1.00 / C 1.00; PowerShell JSON A 0.88 / B 0.98 / C 1.00. FP rate 0 everywhere except cp-9 arm C (0.12, one decoy finding).
  - Validation evidence: 672/672 cells exit 0 and non-empty; unblind: 672 records, 0 ungraded, 0 id or fixture mismatches; results in work/results-astra.yaml (41e99e1).
  - Notes: verdicts wait for the Fable half (worst-model rule). Grading caveat for outcome.md: the seven PowerShell JSON partials are responses that named the mechanism and proposed a different valid remediation than the key's; recorded as graded, not adjudicated. Fable runner method pending ebigunso's decision (subagent preamble cost).
- 2026-09-08 Wave 2 Task_5 pilot complete and applied: [Task_5]
  - Summary: Fable half run through the Claude Code CLI in restricted headless mode (672 cells, $49.07, mean 1,146 input tokens; run/run_fable.sh) after ebigunso installed and signed in to the CLI; a 16-cell subagent trial was set aside as contaminated. Both halves graded blind (14 graders each). Rule applied on the worst model: DELETE for cp-2, cp-9, npm locks, gRPC IPv6, Python encoding, shell cwd; COMPRESS for PowerShell JSON. Edits: two principles removed and the rest renumbered 2-8; four runbooks and their routing lines removed; the PowerShell JSON runbook body replaced with the arm-C text. outcome.md and key-errata.md written (cp-9-c2 decoy invalidated).
  - Validation evidence: validate_harness_package.py pass; run_validation_smoke_tests.py exit 0; unblind: 672/672 per model with zero mismatches; scorer verdicts as recorded.
  - Notes: the pre-registered one-seed cap condition is not met (Fable arm A below ceiling on two runbooks); the 14 remaining sections need ebigunso's call: run at two seeds, cap, or stop. Reviewer dispatched for Task_5.
- 2026-09-08 Wave 2 Task_5 pilot revised after review: [Task_5]
  - Summary: Task_5 review (NEEDS_REVISION) found 23 Astra control cells had used web search, decoy cp-9-c2 lacked an import, and the PowerShell JSON key was stricter than the protocol's partial definition. Reruns: 23 control cells with web_search disabled and 12 cp-9-c2 cells on the corrected fixture. Round-2 blind regrade of every runbook section and cp-9 on both models under ebigunso's ruling (24 graders). Result: arm A at ceiling on both models on six sections and 0.98 on the seventh; all seven outcomes DELETE, so the PowerShell JSON runbook is removed rather than compressed. outcome.md rewritten with both rounds recorded; key-errata.md updated; blind mappings committed.
  - Validation evidence: unblind 672/672 per model, zero mismatches; scorer verdicts as recorded; validate_harness_package.py and smoke tests rerun below.
  - Notes: the one-seed cap condition is met on six sections and missed by one Astra cell on the seventh; the 14 remaining sections await ebigunso's call. Delta re-review dispatched.
- 2026-09-08 Wave 2 Task_5 pilot APPROVED: [Task_5]
  - Summary: second delta review found the cp-2 carry-forward missing from the reproducible aggregation path and one Astra Python-encoding partial still graded on the key's route. Fixed in ff91d53: unblind.py carries cp-2 from the round-1 results explicitly and applies work/adjudications.yaml (one entry, grader original preserved); outcome.md narrative corrected. Codex Reviewer APPROVED (2b67d98..ff91d53): both result files reproduce, all seven DELETE, arm A at 1.00 on every pilot section on both models.
  - Validation evidence: unblind 672 unique rows per model, 0 ungraded; validate_harness_package.py pass; smoke tests exit 0.
  - Notes: cap condition met; the 14 remaining sections await ebigunso's recorded choice (two seeds as registered, one-seed cap, or stop). Task_7 (Refresh 2) and Task_6 (final review) follow.

## Decision Log (append-only; re-plans and major discoveries)

- 2026-09-06 Decision: Research waived for plan drafting.
  - Trigger / new insight: the refresh session already established every fact this plan rests on (validator key list, consumer greps, archived protocol commits, installed-copy versions, discovery probe).
  - Plan delta (what changed): no Researcher before drafting; Task_3 dispatches one for the fixture plan.
  - Tradeoffs considered: none material.
  - User approval: pending with plan approval.
- 2026-09-06 Decision: Plan review round 1 (Codex Reviewer) findings applied.
  - Trigger / new insight: installed validators lag producers, so removing keys would break old readers; the ablation scope reached into contract lines (principle 1, architecture-gates status/waiver text) that ADR-D-0015 excludes; the decision rule was a bare threshold, not the archived protocol; a compress outcome had no arm to justify it; Task_2 acceptance contradicted its own legacy fixture; Task_4 lacked session-identity evidence.
  - Plan delta (what changed): Task_2 makes the keys optional (two-step migration with a second refresh in Task_1); ablation scope is section-level with protected lines named; three arms and the verbatim protocol-v2 plus batch-2 decoy rule; Task_2 acceptance reconciled; Task_4 requires fresh sessions and version/manifest/commit/loaded-line evidence.
  - Tradeoffs considered: a one-step key removal was simpler but unsafe for readers on installed copies.
  - User approval: pending with plan approval.
- 2026-09-06 Decision: Plan review round 2 (Codex Reviewer) findings applied.
  - Trigger / new insight: marking keys optional for producers in the same release still let new Workers omit them before installed validators were refreshed; the protocol-v2 rule branches on a fourth arm, so "verbatim" could not fit three arms; `--check` prints status and checks manifest existence, not content.
  - Plan delta (what changed): Task_2 is validator-only, producer contract keeps both keys as required-to-emit with a reader note; Refresh 2 is a new user-owned Task_7 depending on Task_2, in Wave 2; the adapted three-arm rule is written in full with retained-versus-adapted attribution; Task_4 hashes the manifest file directly.
  - Tradeoffs considered: a fourth arm mirroring protocol-v2's replacement document has no candidate document here; the compressed arm is the honest substitute and is labeled as an adaptation.
  - User approval: pending with plan approval.
- 2026-09-06 Decision: Plan review round 3 (Codex Reviewer) finding applied.
  - Trigger / new insight: Task_7 in the same wave as Task_4 could mutate the shared installed copies between the live cells.
  - Plan delta (what changed): Task_7 depends on Task_4 as well as Task_2 and moves to its own Wave 3; Task_6 moves to Wave 4.
  - Tradeoffs considered: one extra wave versus a corrupted live measurement.
  - User approval: pending with plan approval.
- 2026-09-06 Decision: Ablation outcome recorded with the experiment, not as ADR-I-0007.
  - Trigger / new insight: ADR-D-0018 (written at PR #57 closeout) moves removal ledgers to experiment records; only a change to the decision rule or a tier boundary warrants an ADR.
  - Plan delta (what changed): Task_5 writes outcome.md instead of an ADR; owns and acceptance updated; pointers to ADR-I-0006 replaced.
  - Tradeoffs considered: none material.
  - User approval: pending with plan approval.
- 2026-09-06 Decision: Plan approved by user with the proposed answers to all open questions.
  - Trigger / new insight: user approval after reviewer approval.
  - Plan delta (what changed): status approved; execution begins after PR #57 merges.
  - Tradeoffs considered: none.
  - User approval: yes (2026-09-06).
- 2026-09-07 Decision: Decision-record pointers corrected after the PR #57 renumbering.
  - Trigger / new insight: this plan was drafted before ADR-D-0018 was renumbered; the loader-authority record is ADR-D-0017, discoveries are ADR-D-0018, class-matched removal evidence is ADR-D-0019, and loader-routed sessions assuming the Orchestrator role is ADR-D-0020.
  - Plan delta (what changed): Task_4 acceptance reads as: a failure of (i) reopens ADR-D-0017; a failure of (ii) reopens ADR-D-0020. Context references to "ADR-D-0018 (class-matched removal evidence)" mean ADR-D-0019. No task content changes.
  - Tradeoffs considered: none.
  - User approval: not needed (pointer repair, no decision changed); recorded for the record.
- 2026-09-07 Decision: Fixture mapping is primary-target with disclosed secondaries, not exclusive.
  - Trigger / new insight: the Task_3 Researcher dispatch asked that each planted defect map to its section and to no other measured section; the Researcher showed that reading admits zero plants in every code-review section (cp-3/ag-3, cp-5/ag-5, cp-6/ag-4 share checks; cp-10 is encompassing). The plan requires only that a defect map to a specific check, not generic code quality.
  - Plan delta (what changed): protocol.md Fixtures now reads: one primary named check per plant, quoted; secondary mappings disclosed; overlap is harmless because arm B loads only the measured section. The Researcher is re-commissioned for the 16 code-review sections under that criterion; cp-10 plants must target its own quoted checks and the section reports fewer than 12 if they do not exist. Recorded before any cell ran; the decision rule is unchanged.
  - Tradeoffs considered: literal exclusivity would mark 16 of 21 sections unmeasurable and infer nothing; rejected.
  - User approval: not needed (pre-registration detail below the decision rule); surfaced in the report.
- 2026-09-08 Decision: Task_4 cells run as ephemeral headless Codex sessions, not user-driven registered peers.
  - Trigger / new insight: ebigunso chose codex exec --ephemeral for both cells: no roster changes, and the harness-less cell cannot be contaminated by a stray skill or session state.
  - Plan delta (what changed): each cell is a fresh `codex exec --ephemeral -s read-only` in the main checkout with the installed user loader active (no project_doc_max_bytes override, plugins and skills enabled); the "do not load the harness" instruction arrives in the first user turn rather than over a peer channel; the evidence header (codex --version, manifest SHA-256, checkout commit, loaded-instructions line) is requested in the prompt. Q2's "user drives the peer" is replaced by the Orchestrator launching the runs; the Reviewer still judges the transcripts read-only.
  - Tradeoffs considered: the peer-channel form would test the same loader through a second instruction source, at the cost of manual roster work and contamination risk; not pursued.
  - User approval: yes (2026-09-08).
- 2026-09-08 Decision: Runbook grading credits a correct mechanism with any working remediation as a hit.
  - Trigger / new insight: Task_5 review (Codex Reviewer) found the PowerShell JSON key stricter than the protocol's partial definition ("wrong or missing mechanism"): control-arm responses that named the mechanism and prescribed a different working fix were scored partial, and that alone decided COMPRESS over DELETE. The Reviewer also found 23 Astra control cells had used web search (protocol forbids other references) and that decoy cp-9-c2 omitted an import (authoring error).
  - Plan delta (what changed): ebigunso ruled that a response naming the planted mechanism and prescribing any working remediation scores 1.0; the key's remediation route no longer decides between hit and partial. Applied after results existed, so it is recorded here as a post-hoc grading clarification, applied uniformly to every runbook section, both models, all arms by a full blind regrade; the decision thresholds are unchanged. The 23 searching Astra control cells are rerun with web search disabled (run_astra.sh now passes web_search=disabled); cp-9-c2 gets its import context and its 12 cells are rerun and regraded; superseded outputs are kept under work/rerun-superseded/.
  - Tradeoffs considered: keeping the strict key would ship a compressed runbook on the strength of a remediation-route disagreement, not a detection difference.
  - User approval: yes (2026-09-08, "Credit correct mechanism with any working remediation as a hit").
- 2026-09-08 Decision: One-seed cap recorded for the fourteen remaining sections.
  - Trigger / new insight: the pre-registered cap condition (every pilot section with arm A at ceiling) is met on both models after the approved pilot (ff91d53).
  - Plan delta (what changed): principles 3 through 8 and 10 and gates 1 through 7 run at one seed (14 x 3 arms x 16 fixtures x 2 models = 1,344 review calls) with the same runners, blinding, grading rule, and decision rule; recorded here before any of those cells run. Everything else in protocol.md stands.
  - Tradeoffs considered: two seeds as registered (double cost for a variance the pilot showed to be zero on ceiling cells); stopping with the sections unmeasured (leaves the plan's Definition of Done open).
  - User approval: yes (2026-09-08, "Record the one-seed cap and run the remaining sections").

## Notes
- Risks: the ablation is the expensive item (fixtures times arms times models times seeds); Task_3 sizes it and the user can cap it at plan approval. Task_4 depends on the user's install refresh and on PR #57 merging first.
- Edge cases: if the validator ever starts rejecting unknown keys, the one-release compatibility note in Task_2 must be revisited.
