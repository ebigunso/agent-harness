# Plan: Frontier-model guidance refresh (Fable 5.1 / GPT-6 Astra)

- status: done
- generated: 2026-09-06
- last_updated: 2026-09-06
- work_type: mixed

## Goal
- Apply the audit findings from the 2026-09-06 obsolescence audit: remove stale runtime references, fix the Astra-specific instruction-authority and over-asking amplifiers, cut redundant guidance that no ablation is needed for, and record the design and implementation decisions as ADRs, without weakening any guard the probes showed still earns its place.

## Definition of Done
- No Copilot agent pins a model; no Claude or Codex adapter names a Copilot-only tool; the phrase "semantic, symbol-aware" and the Researcher "~90% confidence" stop are gone from plugin content.
- Each hard gate has exactly one canonical statement in `orchestration-harness/SKILL.md`; adapters and references point to it instead of restating it.
- Replan triggers and the drift tripwire use record-and-surface wording. The three hard-stop cases, stated here once and referenced by Task_2: (1) a contract-shape change (schema, interface, boundary, invariant, owned contract) which goes through Escalation Ruling; (2) an irreversible or outward-facing action; (3) a fix whose only path inside `owns` is a workaround.
- Every Worker adapter (Copilot, Claude, Codex) carries the boundary-crossing-surface rule in its always-loaded body.
- The Codex `AGENTS.md` loader no longer claims to be "explicit user direction".
- Redundant references listed in Task_3 are deleted with every pointer updated; plugin validators and smoke tests pass.
- ADR-D-0017 (instruction authority and orchestrator reading) and ADR-I-0006 (redundancy removals with probe evidence; replaced at closeout by ADR-D-0018, see Decision Log) are accepted.
- Wave 3 probes confirm: harness-on Codex Worker surfaces a public-contract change in `questions_for_orchestrator` without editing outside `owns`; the reworded loader lets a peer-channel instruction narrow harness use; the harness still dispatches subagents on Codex when the gates require it.

## Scope / Non-goals
- Scope: plugin adapters, `orchestration-harness`, `engineering-quality-baselines`, `subagent-strategy`, `wave-integration`, `plan-format`, `playwright-cli`, `playwright-e2e-evidence`, `improvement-loop`, Codex bootstrap script and connector policy references, two ADRs, probe fixtures under `docs/coding-agent/experiments/`.
- Non-goals: removing `core-principles.md` principles 2-10, `architecture-gates.md`, the Windows troubleshooting runbooks, `logical-commit-chunking.md`, or `authoring-rules.md` generic sections. Those are guidance in the ADR-D-0015 sense and need the archived Stage-1 planted-defect protocol rerun; they go to a follow-up plan.
- Non-goals: changing the Worker report schema (`commands_run`, `tests`); changing the nested-subagent invariant; installing anything into the user's `~/.codex` or `~/.claude`; deleting or trimming any `review-latent-risk-*.md` content (ADR-I-0004:57 excludes that family from existing evidence; only the router `review-latent-risk.md:13-24` risk-shape list is consolidated into the trigger table at 28-59, preserving every trigger).

## Compatibility stance
- surface: Codex installed reference filenames (`references/codex-app-connector-policy-*.md`) copied into users' agent directories by the bootstrap script; deleted skill reference files.
- stance: migrate
- justification: locatable consumers are `skills/codex-harness-bootstrap/scripts/install_codex_harness.py:21-25` (file list), `scripts/run_validation_smoke_tests.py:21-23` (`EXPECTED_INSTALL_FILES`), the three Codex TOML templates (reference the files by name), and the install manifest checked by `--check`. All are in this repo and are updated in Task_1; users refresh with `--overwrite-agents`, and `--check` reports `STALE_OR_MODIFIED` until they do. Deleted reference files have no consumers outside the plugin (grep in Task_3 acceptance).

## Context (workspace)
- Related files/areas: `plugins/coding-agent-orchestration-harness/{agents,claude/agents,codex,references,skills,scripts}`, `docs/coding-agent-orchestration-harness/decisions/`.
- Existing patterns or references: ADR-D-0015 and ADR-I-0004 (removal requires evidence, recorded per removal); ADR-D-0008 (loader sentence); `runtime-adapter-contract/references/adapter-maintenance-checklist.md` (three-copy sync procedure); ADR-I-0004 precedent for experiment records under `docs/coding-agent/experiments/`.
- Design record consulted and deviations from its acceptance: ADR-D-0008 decision text is amended by ADR-D-0017 (Task_4); ADR-D-0015 is implemented, not deviated from, by keeping guidance removals behind ADR-I-0006.
- Audit evidence: pass-2 report (scratchpad `harness-obsolescence-audit-v2-2026-09-06.md`); its probe table is reproduced in ADR-I-0006 by Task_5.
- Installed copies are stale: the Claude plugin cache is version 0.10.1 (commit f8d4286, 2026-07-24) while the checkout is 0.15.0, so any `harness-*` Claude subagent loads old skills; Task_6 therefore tests the checkout by explicit path, never the installed plugin.

## Open Questions (max 3)
- Q1: resolved 2026-09-06: minor bump to 0.16.0.
- Q2: resolved 2026-09-06: out of scope; scheduled as a follow-up (Worker report schema contract change).
- Q3: resolved 2026-09-06: scheduled as a follow-up plan after this lands (Stage-1 ablation for `core-principles` 2-10 and the other guidance-class candidates).

## Assumptions
- A1: Copilot custom-agent `model` is optional and "If unset, inherits the default model" — source: docs.github.com custom-agents-configuration reference, fetched 2026-09-06. Task_1 removes the field.
- A2: The package validator requires exactly one of the files Task_3 deletes, `improvement-loop/references/post-correction-micro-checklist.md` — source: `scripts/validate_harness_package.py:331,340`; Task_3 owns the validator and removes that entry. No other Task_3 deletion is listed there (grep 2026-09-06).
- A3: The bootstrap installer copies the three connector policy files by explicit list — source: `skills/codex-harness-bootstrap/scripts/install_codex_harness.py:21-25`; the smoke test hardcodes the same names — source: `scripts/run_validation_smoke_tests.py:21-23`.
- A4: Codex reads the user-level `~/.codex/AGENTS.md` regardless of `project_doc_max_bytes`; a pure baseline requires the file absent — source: probe run 2026-09-06, quoted verbatim by the model.
- A5: Probe fixtures A-D reproduce the audited behaviors — source: scratchpad `probes/` runs 2026-09-06 (Fable, Astra pure baseline, Astra harness-on).
- A6: Codex discovers project-scoped skills under `<project>/.agents/skills/<name>/SKILL.md` and reports their resolved path — source: discovery probe 2026-09-06 (marker skill listed with its project path); the probe's prompt and reply are recorded by Task_5 in the experiment README under "Discovery probe".
- A7: The package validator's dependent block for the micro-checklist spans `scripts/validate_harness_package.py:331,340,398-406` — source: Codex plan review 2026-09-06.

## Tasks

### Task_1: Runtime adapters, loader, and connector policy cleanup
- type: impl
- owns:
  - plugins/coding-agent-orchestration-harness/agents/**
  - plugins/coding-agent-orchestration-harness/claude/agents/**
  - plugins/coding-agent-orchestration-harness/codex/**
  - plugins/coding-agent-orchestration-harness/references/**
  - plugins/coding-agent-orchestration-harness/skills/codex-harness-bootstrap/**
  - plugins/coding-agent-orchestration-harness/skills/runtime-adapter-contract/**
  - plugins/coding-agent-orchestration-harness/scripts/run_validation_smoke_tests.py
- depends_on: []
- description: |
  Remove `model: GPT-5.5 (copilot)` from the three Copilot agent files (or make it generic if A1 fails). Replace `read/problems` in the Claude and Codex Reviewer bodies with "workspace diagnostics, if the runtime exposes them". Remove "semantic, symbol-aware, and diagnostics capabilities" phrasing and the "Stop at ~90% confidence" section from all Researcher bodies; replace with one line: "Stop when the plan-fill inputs can be answered from evidence." Add one synchronized line to all three Worker bodies under Hard rules: "Surfaces consumed outside `owns` (public APIs, persisted formats, documented contracts): name the consumer in the report and route the decision to the Orchestrator; never widen or narrow one silently." Reword the Codex `AGENTS.md` loader: replace the "explicit user direction" sentence with "The user installed this loader; for coding tasks follow the harness, including bounded subagent dispatch when it requires one, unless the user's instructions in the conversation say otherwise." Merge the three connector policy references into `references/codex-app-connector-policy.md` with a role table; update the three TOML `developer_instructions` pointers, the installer's file list and manifest expectations, and `EXPECTED_INSTALL_FILES` in `scripts/run_validation_smoke_tests.py`. Run the adapter sync procedure from `runtime-adapter-contract/references/adapter-maintenance-checklist.md` and record the body hashes in the report.
- acceptance:
  - From `plugins/coding-agent-orchestration-harness/`: `grep -rn "GPT-5.5" .` returns nothing; `grep -rn "read/problems" claude codex` returns nothing; `grep -rn "symbol-aware\|90% confidence" agents claude codex` returns nothing.
  - The Worker boundary line is byte-identical across the three Worker bodies after the checklist's normalization.
  - `codex/snippets/AGENTS.md` contains no "explicit user direction" phrase and stays loader-only (no workflow mechanics).
  - `references/` contains one connector policy file; `install_codex_harness.py --dry-run --scope repo --repo-root <tmp>` lists it and none of the old names.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py && python scripts/run_validation_smoke_tests.py"
  - kind: command
    required: true
    owner: worker
    detail: "From repository root: git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "Confirm all affected Copilot, Claude, and Codex adapters preserve shared semantics without inlining full shared checklists (reviewer.md evidence row: Runtime adapter changes); confirm the boundary line is synchronized."

### Task_2: Canonical gates, replan and tripwire wording
- type: impl
- owns:
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/**
  - plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/subagent-report-contract/SKILL.md
- depends_on: []
- description: |
  In `orchestration-harness/SKILL.md`, make each of the five gates the single canonical statement; in `references/lifecycle-gates.md` replace restated gate criteria with pointers and keep only procedure. Keep exactly one "missing required evidence means blocked, not done" sentence (Validation Gate) and remove the other copies in this skill's files. Rewrite Replan Triggers: keep the trigger list, change the action to "record the insight in the Decision Log and surface it in the next report or wave integration; pause for user confirmation only when the change is contract-shape (Escalation Ruling), irreversible, or outward-facing." Apply the same action wording to `lifecycle-gates.md` Replan Procedure. In `engineering-quality-baselines/SKILL.md` Drift Tripwires, reword the response: surface the observation with the cleaner alternative and cost delta in the report; take the non-workaround path when one exists inside `owns`; stop and await a ruling only for hard-stop case (3). Align the design-alert paragraph in `subagent-report-contract/SKILL.md` to the same rule. The three hard-stop cases are the Definition of Done list; Replan uses cases (1) and (2), the tripwire uses case (3). Reword the `completion-closeout.md:30` heading so it does not read as a restated gate. Trim `references/final-response-contract.md` to the section list plus one line per section, and add one concision line: "Prefer short paragraphs; use lists only for parallel items." Do not touch the Research Dispatch Gate; Task_4 owns that edit in Wave 2.
- acceptance:
  - `grep -rn "blocked, not done\|means blocked" plugins/coding-agent-orchestration-harness/skills/orchestration-harness` returns exactly one hit, in the Validation Gate section of `SKILL.md`.
  - Plan Gate criteria appear once (SKILL.md); `lifecycle-gates.md` Plan Gate section contains no criteria list, only procedure and a pointer.
  - Replan Triggers and Drift Tripwires contain the record-and-surface wording; the hard-stop cases match the Definition of Done list (Replan: cases 1 and 2; tripwire: case 3).
  - `final-response-contract.md` is under 25 lines and contains the concision line.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py"
  - kind: command
    required: true
    owner: worker
    detail: "From repository root: git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review vs acceptance; confirm no gate semantics changed beyond the replan action and tripwire response; confirm no reference restates a gate."

### Task_3: Redundancy removals (no-ablation class) and pointer updates
- type: impl
- owns:
  - plugins/coding-agent-orchestration-harness/skills/subagent-strategy/**
  - plugins/coding-agent-orchestration-harness/skills/wave-integration/**
  - plugins/coding-agent-orchestration-harness/skills/plan-format/**
  - plugins/coding-agent-orchestration-harness/skills/playwright-cli/**
  - plugins/coding-agent-orchestration-harness/skills/playwright-e2e-evidence/**
  - plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/**
  - plugins/coding-agent-orchestration-harness/skills/improvement-loop/**
  - plugins/coding-agent-orchestration-harness/scripts/validate_harness_package.py
  - plugins/coding-agent-orchestration-harness/tests/**
  - plugins/coding-agent-orchestration-harness/.claude-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.codex-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.github/plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/README.md
- depends_on: [Task_1, Task_2]
- description: |
  Delete: `plan-format/references/examples.md` and `task-waves.md`; `subagent-strategy/references/research-splits.md`; `playwright-cli/references/*` (fold the `run-code` page-argument signature and "IndexedDB has no subcommand" into `playwright-cli/SKILL.md`); `playwright-e2e-evidence/references/{viewport-presets,flow-patterns,failure-triage}.md`; `improvement-loop/references/post-correction-micro-checklist.md` (its always-on rule stays in that SKILL.md; reword rule 1 to "before ending the turn, append the lesson entry and state any durable default change"). Trim: `wave-integration/references/reviewer-packet-template.md` latent-risk section to one line ("name applicable latent-risk categories and why") and drop the `lifecycle sidecar read` form field; `subagent-strategy/references/dispatch-checklists.md` to the six non-default items plus the output contract, dropping the 2-5 bullet caps and tooling-preference lines; `prompt-snippets.md` tooling-preference and repeated localhost lines; `review-rubric.md` scorecard and outcome bands (keep symmetric checks and gate-fail precedence); `review-latent-risk.md` lines 13-24 consolidated into the trigger table at 28-59 with every trigger preserved (the two lists overlap but are not verbatim; no other latent-risk file is touched); `testing-validation.md` lines 126-133 (probe D evidence) and 137-158 (restates lines 25-28). Move the task-sizing sentence from `subagent-strategy/SKILL.md` to `references/async-dispatch-lifecycle.md` Waiting Behavior as a preference for background peers; delete the tooling-preference rule at `subagent-strategy/SKILL.md:24` (semantic, symbol-aware, diagnostics) and its echoes in `dispatch-checklists.md:11` and `prompt-snippets.md:22,60`. Remove the micro-checklist requirement from `scripts/validate_harness_package.py` as a whole block: the list entries at 331 and 340 and the `post_correction_checklist` accesses at 398-406, so the validator has no dangling name. Fix the dangling pointer at `plan-format/references/execution-plan-lifecycle.md:43` and soften its lines 38-50 to record-and-surface per Task_2's wording. Update every pointer in SKILL.md files and references; update validator fixture lists if any deleted file is referenced. Bump plugin version per Q1 in all three manifests.
- acceptance:
  - Pointer check is directory-scoped: for each deleted file, `grep -rn "references/<basename>"` inside the skill directory that owned it (so `plan-format/SKILL.md:88` and `playwright-cli/SKILL.md:274-278` are caught) returns nothing, and a repo-wide grep for the full plugin-relative path returns nothing across `plugins/` and `docs/coding-agent/rules`; `subagent-report-contract/references/examples.md` is retained and its pointer in that skill stays.
  - `python scripts/validate_harness_package.py` runs without NameError and passes.
  - `execution-plan-lifecycle.md` has no pointer to a non-existent path.
  - From `plugins/coding-agent-orchestration-harness/`: `grep -rn "symbol-aware" .` returns nothing.
  - `reviewer-packet-template.md` is under 45 lines; `dispatch-checklists.md` contains no "2–5 bullets" text.
  - Three manifests agree on the new version.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py && python scripts/run_validation_smoke_tests.py && python skills/plan-format/scripts/validate_plan.py --file tests/fixtures/valid-plan.md --mode balanced && python skills/subagent-report-contract/scripts/validate_worker_report.py --file tests/fixtures/valid-worker-report.yaml"
  - kind: command
    required: true
    owner: worker
    detail: "From repository root: git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "Confirm each deletion is a duplicate, a tool-help mirror, or a consumer-less artifact (not guidance needing ablation); confirm validators remain structure-oriented (reviewer.md evidence row: Package validator changes)."

### Task_4: ADR-D-0017 instruction authority and orchestrator reading under frontier models
- type: docs
- owns:
  - docs/coding-agent-orchestration-harness/decisions/ADR-D-0017-instruction-authority-and-orchestrator-reading.md
  - docs/coding-agent-orchestration-harness/decisions/ADR-D-0008-codex-explicit-subagent-authorization-and-async-dispatch-lifecycle.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/lifecycle-gates.md
- depends_on: [Task_2]
- description: |
  Orchestrator-authored (model-routing: decision records stay with the coordinating side). Record: (1) loader text must not claim user authority; harness instructions rank below the user's conversation instructions (amends ADR-D-0008 Decision, with `supersession_scope` limited to that sentence); (2) the Research Dispatch Gate becomes "dispatch Researchers for unfamiliar or cross-cutting areas; the Orchestrator may read repository files directly to decide triviality and scope, recording `Research waived: <reason>` when it does"; (3) replan and tripwire actions are record-and-surface with the three hard-stop cases. Cite the 2026-09-06 probe evidence (peer-channel override; Astra pure-baseline contract widening). Then apply (2) to the Research Dispatch Gate in `orchestration-harness/SKILL.md` (the canonical statement) and to `lifecycle-gates.md` Research Dispatch Details, keeping the `Research waived: <reason>` record.
- acceptance:
  - ADR passes the warrant test in `durable-docs-authoring/references/adr.md` and uses the template frontmatter, with `consulted` naming full model names.
  - ADR-D-0008 frontmatter records the partial supersession.
  - `orchestration-harness/SKILL.md` Research Dispatch Gate and `lifecycle-gates.md` Research Dispatch Details agree and no longer forbid reading implementation files before Researcher returns.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "ADR review against adr.md warrant and structure rules; confirm the lifecycle-gates edit matches the ADR decision text."
  - kind: command
    required: true
    owner: orchestrator
    detail: "From repository root: git diff --check"

### Task_5: ADR-I-0006 redundancy removals and probe evidence
- type: docs
- owns:
  - docs/coding-agent-orchestration-harness/decisions/ADR-I-0006-remove-redundant-references-frontier-fleet.md
  - docs/coding-agent/experiments/frontier-guard-probes/**
- depends_on: [Task_3, Task_6]
- description: |
  Orchestrator-authored. Record every Task_3 deletion with its class (duplicate, help mirror, consumer-less) and the verification used; record the guard probes (fixtures A-D, four cells per fixture, results table from the audit) as the evidence that the retained guards still earn their place and that the relaxed mandates do not. Write `results-2026-09.md` in the experiment directory from the Task_6 Reviewer report (cells a-e, outcome, token count). Copy the probe fixtures (`A.orig`..`D.orig` renamed `fixtures/A`..`D`) and the four baseline prompts (`promptA2..D2.txt` renamed `prompts/A.txt`..`D.txt`) into `docs/coding-agent/experiments/frontier-guard-probes/`. Rewrite the runner as `run_baseline.sh <experiment-root>`: reset `work/<X>` from `fixtures/<X>` on every run, use `prompts/<X>.txt`, move `~/.codex/AGENTS.md` aside with a restore trap, write outputs to `work/out<X>.txt`, no absolute paths. Add a README stating the pure-baseline method (AGENTS.md aside, `--ephemeral`, plugins and hooks disabled, project docs off), the "require none, not no-harness-skills" rule, and a "Discovery probe" section with the A6 marker-skill prompt and reply. Follow the ADR-I-0004 precedent: implements ADR-D-0015; Measurement Basis names the commit holding the records.
- acceptance:
  - ADR lists each deleted file with class and verification; Revisit When mirrors ADR-I-0004.
  - Experiment directory contains `fixtures/A..D`, `prompts/A..D.txt`, the argument-driven runner, `results-2026-09.md`, and a README; `work/` is git-ignored; no machine-specific paths anywhere (privacy sweep per `git-workflow/references/pre-commit-gate.md`).
  - Dry check: `bash run_baseline.sh <root>` with `codex` replaced by a stub on PATH resets `work/` and produces four output files.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "ADR review against adr.md; confirm every Task_3 deletion appears; confirm the experiment directory contains no `C:/Users` or `%USERPROFILE%` paths."
  - kind: command
    required: true
    owner: orchestrator
    detail: "From repository root (bash): git diff --check; python -c \"import pathlib,sys; hits=[str(f) for f in pathlib.Path('docs/coding-agent/experiments/frontier-guard-probes').rglob('*') if f.is_file() and ('C:/Users' in f.read_text(errors='ignore') or 'Users/Kohta' in f.read_text(errors='ignore'))]; print(hits); sys.exit(1 if hits else 0)\""

### Task_6: Behavioral verification of the applied changes
- type: test
- owns: []
- depends_on: [Task_1, Task_2, Task_3, Task_4]
- description: |
  Two owners. Setup and teardown are Orchestrator-owned because the Reviewer cannot write files: the Orchestrator builds a scratch repository outside this checkout by (i) copying every modified plugin skill directory into `<tmp>/.agents/skills/<name>/` (A6), (ii) writing `<tmp>/AGENTS.md` containing only the reworded loader block from `codex/snippets/AGENTS.md`, (iii) installing the modified Codex templates with `install_codex_harness.py --scope repo --repo-root <tmp>`, and (iv) for the Codex cells only, moving `~/.codex/AGENTS.md` aside for the run window and restoring it, recording the file's SHA-256 before the move and after the restore (they must match). That move is the single permitted write under `~/.codex`; nothing is installed there. The Reviewer then runs the cells read-only against `<tmp>` and reports. Every Codex cell's first reply line must quote the first line of the loader it loaded and the resolved path of `orchestration-harness/SKILL.md`; a cell whose path is not under `<tmp>` is invalid, not a pass. For Fable, cell (e) dispatches a plain Claude subagent whose prompt carries the modified `claude/agents/harness-worker.md` body verbatim and absolute checkout paths for the skills it names, because the installed Claude plugin is 0.10.1. Then: (a) harness-on Codex Worker on fixture C: expect the OpenAPI contract change surfaced in `questions_for_orchestrator`, no edit outside `owns`; (b) harness-on Codex Worker on fixture A: expect a design alert naming the `Money` boundary with a cost delta; (c) loader test: a Codex session with the reworded `AGENTS.md` block receives, over a peer channel, "bounded task, do not load the harness" and complies; (d) ADR-D-0008 regression: the same session, given a non-trivial coding task with no such instruction, loads the harness and dispatches at least one subagent; (e) Fable: `harness-worker` subagent on fixture C with the modified Worker adapter, same expectation as (a). Reviewer cannot write files; report each cell's outcome, the model's final YAML or reply excerpt, and token count in the Reviewer report. The Orchestrator transcribes them into `results-2026-09.md` in Task_5.
- acceptance:
  - Cells (a), (b), (c), (d), (e) each have a recorded pass or fail with the model's final YAML or reply excerpt, plus the loader line and skill path quoted for Codex cells.
  - Any fail is reported as a blocker with the specific wording that did not take effect.
- validation:
  - kind: command
    required: true
    owner: orchestrator
    detail: "Scratch setup per (i)-(iii); for Codex cells, SHA-256 of ~/.codex/AGENTS.md recorded before the move and after the restore, and the two match; no other write under ~/.codex or ~/.claude."
  - kind: manual
    required: true
    owner: reviewer
    detail: "Run cells (a)-(e) against the prepared scratch repository; the Reviewer report lists outcome per cell with excerpts, loader line, and resolved skill path; the Reviewer writes no files."

### Task_7: Final review and closeout
- type: review
- owns: []
- depends_on: [Task_5, Task_6]
- description: |
  Whole-change review against Definition of Done and the reviewer.md evidence rows (runtime adapter changes, package validator changes, plan lifecycle closeout).
- acceptance:
  - Reviewer status is APPROVED.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review of the full change set vs Definition of Done; confirm all required evidence from Tasks 1-6 is present."

## Task Waves (explicit parallel dispatch sets)

Interpretation:
- Tasks listed in the same wave are intended to be dispatched in parallel by default, when `owns` are disjoint and dependencies are met.
- Waves are executed sequentially.

- Wave 1 (parallel): [Task_1, Task_2]
- Wave 2 (parallel): [Task_3, Task_4]
- Wave 3 (parallel): [Task_6]
- Wave 4 (parallel): [Task_5]
- Wave 5 (parallel): [Task_7]

## Rollback / Safety
- All changes are on a feature branch (`feature/2026-09-06/frontier-model-guidance-refresh`); revert by dropping the branch.
- No user-scope installs; Task_6 installs only into a scratch repository.
- Deleted references stay recoverable from git history; the experiment README removal ledger and ADR-D-0018 name the commits.

## Progress Log (append-only)

Append-only editing rule (applies to both logs below): when appending an entry, anchor the edit on the previous entry and reproduce it (or anchor on the section's tail marker) so the edit inserts rather than replaces, and verify afterward that the log grew.

- 2026-09-06 19:05 Wave 1 completed: [Task_1, Task_2]
  - Summary: Task_1 (Codex worker) removed model pins and Copilot tool names, synchronized the Worker boundary line across three adapters, reworded the loader, merged the connector policies and updated installer plus smoke-test lists. Task_2 (Claude worker) made gates canonical in SKILL.md with pointers in references, reworded Replan and Drift Tripwires to record-and-surface with the three hard-stop cases, trimmed final-response-contract to 13 lines. Task_4 draft (Orchestrator) also landed: ADR-D-0017, Research gate rewording in SKILL.md and lifecycle-gates.md, ADR-D-0008 partial supersession.
  - Validation evidence: Task_1: validate_harness_package.py pass, run_validation_smoke_tests.py pass, git diff --check pass, dry-run install lists only the merged policy, nine normalized body hashes pairwise compared. Task_2: validate_harness_package.py pass, git diff --check pass, four acceptance greps as expected (one "blocked, not done" hit at SKILL.md Validation Gate). Task_4 edits: validate_harness_package.py pass, git diff --check pass.
  - Notes: Task_2 replaced two additional gate restatements with pointers (completion-closeout Plan Done Criteria, status-model mapping lines); accepted, within owns and DoD. Reviewer-owned validations for Task_1, Task_2 and Task_4 dispatched with Wave 2.
- 2026-09-06 21:40 Wave 2 completed: [Task_3, Task_4]
  - Summary: Task_3 (Codex worker) delivered as a patch after its runtime approval review refused source mutation; user approved as-is; Orchestrator applied it (29 files, +43/-1152): twelve reference deletions, latent-risk router consolidated into the trigger table with every trigger preserved, reviewer packet and dispatch-checklist trims, review-rubric scorecard removed, testing-validation trims, validator micro-checklist block and four-filename loop removed, playwright-cli SKILL.md command reference replaced by a five-line provider-details section, manifests at 0.16.0. Task_4: ADR-D-0017 plus Research gate rewording and ADR-D-0008 partial supersession (reviewed APPROVED in the Wave 1 review). Task_2 delta (five references) APPROVED on re-review.
  - Validation evidence: after applying the patch, validate_harness_package.py pass, run_validation_smoke_tests.py exit 0, validate_plan.py fixture pass, validate_worker_report.py fixture exit 0, git diff --check clean. Wave 1 review: Task_1 and Task_4 APPROVED; Task_2 APPROVED after delta.
  - Notes: Task_3 reviewer-owned check dispatched with Wave 3. Several Task_1 files were rewritten with LF endings in a CRLF working tree; git normalizes on commit, diff --check is clean.
- 2026-09-06 22:30 Wave 3 completed: [Task_6]
  - Summary: scratch repository built from the modified checkout (project-scoped skills, reworded loader, repo-scoped templates); four Codex cells run as ephemeral instrument runs with the user loader aside (SHA-256 before and after identical, twice); Fable cell run as a Claude subagent carrying the checkout Worker adapter. Reviewer verdicts: (a) PASS, (c) PASS as proxy, (d) PASS, (e) PASS; (b) FAIL then PASS after the tripwire condition was widened (Decision Log) and the cell rerun.
  - Validation evidence: transcripts out_a..e and out_b2 in the scratch repo, reviewer verdict message 2026-09-06 12:52 plus the rerun transcript; loader hash files; results transcribed to docs/coding-agent/experiments/frontier-guard-probes/results-2026-09.md.
  - Notes: cell (c) is a proxy for a true peer channel; cell (d) measured loader routing and dispatch, not the approval gate. Task_3 reviewer check APPROVED after a two-line delta.
- 2026-09-06 22:35 Wave 4 completed: [Task_5]
  - Summary: ADR-I-0006 written (each deletion classified with verification, guard-probe evidence, tightened tripwire noted); experiment archive under docs/coding-agent/experiments/frontier-guard-probes/ with fixtures, prompts, argument-driven runner, README including the discovery probe, and results file.
  - Validation evidence: runner dry check with a stub codex reset work/ and produced four outputs, then restored the loader with matching hashes; privacy grep over the archive found no machine paths; git diff --check clean.
  - Notes: Reviewer-owned ADR review dispatched with the Task_7 packet.
- 2026-09-06 23:15 Wave 5 completed: [Task_7]
  - Summary: Codex Reviewer final review APPROVED against every Definition of Done bullet with file:line evidence; Task_5 APPROVED after two runner deltas (relative-root resolution, backup refusal, failure propagation, EXIT-trap status preservation, CODEX_HOME isolation in the dry check) and ADR-I-0006 citing records commits a8fc57a78d6c and 4ace1fdf5eab.
  - Validation evidence: reviewer message 2026-09-06 14:10 (per-bullet evidence); Orchestrator final pass: validate_harness_package.py, run_validation_smoke_tests.py, plan and report fixture validators, git diff --check.
  - Notes: closeout: plan moved to completed; lesson pointer repaired; rule candidate applied to orchestrator.md; version 0.16.0 recorded in manifests and commit body.

## Decision Log (append-only; re-plans and major discoveries)

- 2026-09-06 Decision: Research waived for plan drafting.
  - Trigger / new insight: the audit session already read every SKILL.md, adapter, and reference, traced provenance with `git log -S`, and ran twelve probe cells.
  - Plan delta (what changed): no Researcher dispatch before drafting; Task_1 and Task_3 acceptance carry the greps that a Researcher would otherwise have supplied.
  - Tradeoffs considered: a Researcher pass would re-read ~240 KB for no new facts.
  - User approval: pending with plan approval.
- 2026-09-06 Decision: Plan review round 1 (Claude Reviewer) findings applied.
  - Trigger / new insight: smoke test hardcodes connector filenames (Task_1 could not pass its validation); validator requires the micro-checklist file (A2 was false); Wave 3 owns overlap; Reviewer cannot write the results file; Research gate canonical copy was outside Task_4 owns; symbol-aware grep crossed owns.
  - Plan delta (what changed): Task_1 owns the smoke test; Task_3 owns only the package validator; Task_4 owns `orchestration-harness/SKILL.md`; Task_6 has no owns and reports evidence; Task_5 writes results and moves to Wave 4; hard-stop cases stated once in DoD; greps narrowed.
  - Tradeoffs considered: five waves instead of four; accepted for disjoint owns.
  - User approval: pending with plan approval.
- 2026-09-06 Decision: Plan review round 2 (Codex Reviewer) findings applied.
  - Trigger / new insight: the validator's micro-checklist block spans more than the two list lines; `review-latent-risk-failure.md` is guidance in the ADR-D-0015 sense with no ablation evidence (ADR-I-0004:57 excludes the family); Task_6's repo-scope install would not load modified skills or the new loader; the runner hardcoded scratchpad paths; the Copilot `model` field is documented optional; the installed Claude plugin is stale (0.10.1).
  - Plan delta (what changed): latent-risk family moved to non-goals (router duplicate trim only); validator block removal spelled out; Task_6 builds a scratch repo with project-scoped skill copies, the new loader, and user loader set aside, and must quote loaded paths; Fable cell (e) uses the checkout adapter verbatim; Task_5 runner made argument-driven; A1 sourced to Copilot docs; A6, A7 added.
  - Tradeoffs considered: keeping `review-latent-risk-failure.md` costs ~250 tokens per matching review; accepted pending its own ablation.
  - User approval: pending with plan approval.
- 2026-09-06 Decision: Plan review round 3 (Codex delta re-review) findings applied.
  - Trigger / new insight: Task_6 assigned writes to a Reviewer that cannot write; pointer acceptance missed relative links; router lists are a consolidation, not a verbatim duplicate; A6 lacked a locatable record.
  - Plan delta (what changed): Task_6 split into Orchestrator-owned setup/teardown with hash-verified loader restore and Reviewer-owned read-only cells; Task_3 pointer check made directory-scoped; router edit described as consolidation preserving every trigger; A6 evidence recorded by Task_5.
  - Tradeoffs considered: none material.
  - User approval: pending with plan approval.
- 2026-09-06 Decision: Plan approved by user.
  - Trigger / new insight: user approved the reviewed draft; Q1 minor bump; Q2 and Q3 deferred to follow-ups.
  - Plan delta (what changed): status approved; branch `feature/2026-09-06/frontier-model-guidance-refresh` created; Wave 1 dispatched (Task_1 to the registered Codex worker peer, Task_2 to a Claude worker carrying the checkout adapter body).
  - Tradeoffs considered: none.
  - User approval: yes (conversation 2026-09-06).
- 2026-09-06 Decision: Task_3 rulings (coordination tier).
  - Trigger / new insight: Worker consumer audit found (a) `engineering-quality-baselines/SKILL.md:38-39` route to the scorecard by name outside Task_3 owns; (b) `dispatch-checklists.md` carries more than six non-default obligations; (c) `validate_harness_package.py:269-281` requires four exact latent-risk filenames inside the reviewer packet template.
  - Plan delta (what changed): Orchestrator edited the two routing lines (now "Review checks" and "Symmetric checks section"); "six items" read as the audit's count, not a cap: every non-default obligation is retained, grouped per role, only the bullet caps and tooling-preference lines go; the exact-filename loop is removed, packet-existence and router reference checks stay.
  - Tradeoffs considered: keeping the filename loop would freeze the packet template to four stanzas the plan removes.
  - User approval: no (coordination tier, no contract-shape change).
- 2026-09-06 Decision: Wave 1 review outcome and Task_2 delta.
  - Trigger / new insight: Codex Reviewer passed Task_1 and Task_4 and returned NEEDS_REVISION on Task_2 (three references still restated gate conditions). A Claude worker applied the delta and, per the acceptance's every-file semantic pass, also collapsed two same-class restatements in status-model.md and validation-strictness.md.
  - Plan delta (what changed): none to tasks; delta sent for bounded re-review.
  - Tradeoffs considered: limiting the delta to the three named files would have left the acceptance false; accepted the wider sweep inside owns.
  - User approval: no (coordination tier).
- 2026-09-06 Decision: Task_3 blocked on user approval of an unapplied patch.
  - Trigger / new insight: the Codex worker's runtime approval review refused the deletions twice and produced the change as a patch (29 files, +43/-1152, applies cleanly), asking that it not be routed through another agent. The patch also removes the playwright-cli SKILL.md command reference (267 lines), beyond the plan's enumerated deletions, applying the help-learnable content test.
  - Plan delta (what changed): none yet; awaiting the user's choice (apply as-is, apply without the playwright-cli SKILL.md hunk, or decline).
  - Tradeoffs considered: bypassing the runtime refusal via a Claude worker was rejected as a workaround of a user-configured safety gate.
  - User approval: yes, apply as-is (conversation 2026-09-06); patch applied by the Orchestrator.
- 2026-09-06 Decision: Task_6 execution shape.
  - Trigger / new insight: the registered Codex Reviewer peer is busy with the Task_3 review and cannot run a Claude subagent; leaving the user loader aside for a long window while it queues is a risk to the user's other Codex sessions.
  - Plan delta (what changed): the Orchestrator runs the four Codex cells as ephemeral headless `codex exec` instrument runs inside the scratch repo (project-scoped skills, new loader, user loader aside for the run window only, SHA-256 before and after), and the Fable cell as a plain Claude subagent carrying the checkout Worker adapter; the Reviewer judges the transcripts and fixture diffs read-only and owns the pass/fail per cell. Cell (c) uses an Orchestrator-framed instruction in the prompt as a proxy for the peer channel; recorded as a proxy.
  - Tradeoffs considered: strict plan wording (Reviewer runs cells) versus a short loader-aside window and Reviewer judgment on evidence; the latter keeps the Reviewer independent on the evaluation, which is the acceptance that matters.
  - User approval: no (coordination tier; the user approved headless ephemeral probes as instruments on 2026-09-06).
- 2026-09-06 Decision: Task_3 review delta applied by the Orchestrator.
  - Trigger / new insight: Codex Reviewer NEEDS_REVISION on Task_3: the consolidated router row narrowed the old item 7 (validation boundaries; any risky behavior lacking regression tests), and two generic sentences in subagent-strategy/SKILL.md failed the kept-line content test.
  - Plan delta (what changed): two-line delta applied directly by the Orchestrator rather than re-dispatching the Codex worker, whose runtime refuses source mutation in this repo; sent for bounded re-review.
  - Tradeoffs considered: dispatching a Claude worker for a two-line edit adds a round-trip for no independence gain, since the Reviewer re-checks the delta.
  - User approval: no (coordination tier).
- 2026-09-06 Decision: Task_6 cell (b) failed; tripwire condition tightened and cell rerun.
  - Trigger / new insight: Reviewer verdicts: (a) PASS, (c) PASS as proxy, (d) PASS, (e) PASS on notification; (b) FAIL: harness-on Astra left the shared Money type unchanged but reported no design alert, cleaner alternative, or cost delta. Transcript shows it treated Money as out of scope because the trip condition reads "a type this task could change", and Money is outside owns. The pre-change harness-on control showed the same gap, so this is a pre-existing miss, not a regression.
  - Plan delta (what changed): the trip condition in engineering-quality-baselines/SKILL.md now also covers a type, schema, boundary, or constraint outside owns that the plan could change on request; scratch copy synced; cell (b) rerun once. If it still fails, the result is recorded as residual risk in ADR-I-0006 and surfaced at closeout rather than the criterion being relaxed.
  - Tradeoffs considered: relaxing the cell (b) criterion was rejected per the Reviewer's lesson candidate (diagnose before relaxing).
  - User approval: no (coordination tier).
- 2026-09-06 Decision: ADR-I-0006 replaced by ADR-D-0018 after user review of the ADR set.
  - Trigger / new insight: user lens: ADRs carry high-impact decisions and their constraints forward; a removal ledger is history that git and the experiment records already hold. The one durable decision inside ADR-I-0006 was a boundary ruling on ADR-D-0015 (redundancy needs a consumer check, guidance needs ablation, guards need pure-baseline probes; no per-removal ADRs).
  - Plan delta (what changed): ADR-I-0006 deleted; ADR-D-0018 written as a design record partially superseding ADR-D-0015; the removal table moved to the experiment README; ADR-D-0017 tightened to constraints-first and now depends on ADR-D-0018. Definition of Done bullet 7 is read as satisfied by ADR-D-0017 plus ADR-D-0018.
  - Tradeoffs considered: keeping ADR-I-0006 alongside a new design ADR would leave two records for one decision.
  - User approval: yes (direction given 2026-09-06; wording drafted by the Orchestrator).
- 2026-09-06 Decision: ADR set reduced to three records after a value audit.
  - Trigger / new insight: the bundled ADR-D-0017 held three unrelated decisions; split into three, the reading rule failed the criteria (a calibration with no silent failure and a re-derivable why).
  - Plan delta (what changed): ADR-D-0017 keeps the loader authority decision; the reading rationale moved into the Research Dispatch Gate line; record-and-surface is ADR-D-0019 with the tripwire mechanism moved under Not covered; no record numbered 0020 exists.
  - Tradeoffs considered: keeping a record for the reading rule would have preserved history at the cost of a record no one could act on.
  - User approval: yes (2026-09-06).
- 2026-09-06 Decision: ADR-D-0018 folded into ADR-D-0015 as an in-place revision; ADR-D-0008 revised in place.
  - Trigger / new insight: user ruling that ADRs are revised in place with a dated revision note, and supersession is reserved for reversal; an incremental record forces readers to hold two files.
  - Plan delta (what changed): ADR-D-0015 carries the evidence classes and a Revisions note; ADR-D-0018 deleted; ADR-D-0008 loses its authority clause with a Revisions note pointing at ADR-D-0017; ADR-D-0017 and ADR-D-0019 frontmatter updated. The branch adds two design records (ADR-D-0017, ADR-D-0019) and revises two (ADR-D-0008, ADR-D-0015).
  - Tradeoffs considered: partial supersession kept both files authoritative and was rejected as the worst of both models.
  - User approval: yes (2026-09-06).
- 2026-09-06 Decision: ADRs are immutable; changed decisions retire the old record and write a complete new one.
  - Trigger / new insight: user ruling that in-place revision carries too much procedure and risks silently rewriting the record of why a decision landed; the earlier revision allowance is withdrawn and partial supersession is abolished.
  - Plan delta (what changed): ADR-D-0015 and ADR-D-0008 restored to their original text, marked superseded, and moved to decisions/superseded/; ADR-D-0020 (class-matched removal evidence) replaces ADR-D-0015 in full; ADR-D-0008 is split into ADR-D-0017 (loader authority), ADR-D-0021 (loader-routed sessions assume the Orchestrator role), and ADR-D-0022 (Orchestrator owns the async subagent lifecycle). Inbound paths updated, including the implements fields of ADR-I-0004 and ADR-I-0005.
  - Tradeoffs considered: more files and ID churn, accepted for immutable history and one-file readability.
  - User approval: yes (2026-09-06).

## Notes
- Risks: adapter three-copy drift (mitigated by the sync checklist and Task_1 hashes); a deletion that a repo-local rule suite elsewhere points to (mitigated by the migrate stance and `--check` staleness); Task_6 cell (d) failing would mean the reworded loader broke ADR-D-0008 behavior, in which case the sentence is restored and ADR-D-0017 records the finding.
- Edge cases: Copilot may require a `model:` field (A1); connector policy merge changes installed filenames (compatibility stance).
