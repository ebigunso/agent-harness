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

## Notes
- Risks: the ablation is the expensive item (fixtures times arms times models times seeds); Task_3 sizes it and the user can cap it at plan approval. Task_4 depends on the user's install refresh and on PR #57 merging first.
- Edge cases: if the validator ever starts rejecting unknown keys, the one-release compatibility note in Task_2 must be revisited.
