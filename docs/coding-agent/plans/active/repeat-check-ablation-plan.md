# Plan: Ablate the repeat-check rules in testing-validation.md (Astra guide, part 3 of 3)

- status: in_progress
- generated: 2026-09-13
- last_updated: 2026-09-16
- work_type: mixed

## Goal
- Decide, with class-matched evidence under ADR-D-0019's guidance class, whether the rerun mechanics prescribed by two lines of `engineering-quality-baselines/references/testing-validation.md` (line 74: rerun targeted and confirm no skip, verify gated live tests once with the service down; line 77: rerun against baseline HEAD when an untouched test fails) change what Claude Fable 5.1 and GPT-6 Astra do when equivalent conclusive evidence already exists. The evidence obligations those lines carry (specific-test evidence shows executed, unskipped tests; a gated live test has negative evidence when its gate could be off; a failure in untouched tests is classified pre-existing or regression before remediation) are invariant and ship in every outcome; only the prescribed mechanics are under test, and the intervention is conditional on equivalent evidence being present. Item 15 of the accepted 2026-09-13 audit list; the article's "Astra self-verifies" claim is the motivation, and the two-model design keeps the decision honest for Fable.

## Definition of Done
- The protocol is pre-registered in this plan before any cell runs: three sections (tv-1 skip confirmation, tv-2 gated live test, tv-3 baseline classification), three arms per section (A: the invariant obligation stated with no prescribed mechanics; B: the line as on main; C: the obligation plus a one-clause hint of the mechanic, conditional on evidence being absent), twelve planted fixtures and four decoys per section: a planted fixture presents a validation summary whose evidence is inconclusive in the way the section names (a green summary hiding a skip; a live test whose gate state is unshown; an untouched-test failure with no baseline information) and the hit is detecting the gap and requiring the evidence by any adequate means; a decoy presents equivalent conclusive evidence already (executed-test counts and no-skip output, the gate verified, the baseline classification shown) and a false positive is demanding a further rerun anyway. One seed, two models, blinded grading, the 2026-09-08 decision rule in full (worst control model; dB under 10 points DELETE the mechanics; dC within 5 points of dB COMPRESS; else KEEP; per-model false-positive guard on decoys; protective tie handling; INCOMPLETE when cells are missing).
- Each section's mechanics are classified DELETE, COMPRESS, or KEEP by that rule; the invariant obligation is retained verbatim in every outcome; the text is edited accordingly and the outcome table plus caveats recorded in this plan's Decision Log.
- The experiment tree (protocol, fixtures, keys, arms, runners, results, grades) lives on the plan branch during execution and is removed in the closeout commit, with the pre-removal commit named in the Decision Log, per ebigunso's 2026-09-10 ruling on experiment artifacts.
- No other line of `testing-validation.md` changes; the required-check waiver template, evidence fields, and the anti-theater guidance stay.

## Scope / Non-goals
- Scope: `testing-validation.md:74` and `:77` (the two lines carrying the three rules) and the experiment tree during execution.
- Non-goals: any other guidance in `engineering-quality-baselines`; Reviewer-owned checks (independent evidence stays per ADR-D-0004); required checks and waivers (never removable per ADR-D-0019).

## Compatibility stance
- surface: one reference file read by Workers and Reviewers on non-trivial validation work.
- stance: migrate
- justification: consumers are in this repository; this plan's closeout bumps the plugin version (Task_5) and ebigunso refreshes after merge.

## Context (workspace)
- Related files/areas: `plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/testing-validation.md:74,77`; the removed `docs/coding-agent/experiments/guidance-class-ablation/` tree in git history at `2a5ebf9` (`protocol.md`, `fixture-plan.md`, `manifest.yaml`, `score.py`, `validate_pilot.py`, `run/gen_prompts.py`, `run/run_astra.sh`, `run/run_fable.sh`, `run/blind.py`, `run/unblind.py`), whose method this plan reuses with the bounded tooling adaptations listed in A2.
- Existing patterns or references: ADR-D-0019 (guidance class: pre-registered ablation; removal only with class-matched evidence); the 2026-09-08 and 2026-09-09 ablation outcomes recorded in `docs/coding-agent/plans/completed/frontier-guidance-follow-ups-plan.md` (Decision Log: grading ruling, one-seed cap, per-section blinded grading, rulings scoped to runbooks).
- Design record consulted and deviations from its acceptance: ADR-D-0019 followed as written.
- Prior evidence: the Codex Researcher audit (agmsg, 2026-09-12 16:30Z) item 11 marks these rules Astra-only in motivation and says a static audit justifies no weakening; the cost of the 2026-09-09 runs (about $0.07 per Fable cell through the headless CLI, Astra cells through ephemeral `codex exec`) bounds this plan at 3 rules x 3 arms x 16 fixtures x 2 models = 288 cells plus six blinded graders.

## Open Questions (max 3)
- Q1: resolved 2026-09-13 by ebigunso as proposed. Grading rule: a hit requires the response to detect the specific evidence gap the section names and to require obtaining that evidence by any adequate means (a targeted rerun, an executed-test count from the log, a gate check, a baseline comparison); a prescribed command sequence is not required. A false positive on a decoy is a blocking demand for further verification when the shown evidence already settles the question. This is the grading rule for this protocol; the 2026-09-08 runbook ruling is neither reused nor extended.
- Q2: resolved 2026-09-13 by ebigunso as proposed: recover `run_fable.sh` and `run_astra.sh` from `2a5ebf9` with one correction to `run_fable.sh`: a cell counts as complete only when the CLI JSON has `is_error` false and a non-empty result, never on the done marker alone; the marker is written only on that condition. Everything else unchanged (web search disabled, loader aside and restored by hash, restricted Claude CLI), relaunched detached as before.
- Q3: resolved 2026-09-13 by ebigunso as proposed: 288 initial calls plus at most 96 retries in aggregate, no more than two per cell, for a maximum of 384 model calls, whichever limit is reached first stops the run; the six grader dispatches are accounted separately; at a stop the affected section stays INCOMPLETE and ebigunso decides. At the 2026-09-09 rates the Fable half is about $10 before retries; Astra runs on the ephemeral CLI.

## Assumptions
- A1: The two lines separate into three sections (tv-1 skip confirmation; tv-2 gated live test; tv-3 baseline classification), each with one invariant obligation and one prescribed mechanic — source: the lines' structure at `testing-validation.md:74,77`; Task_1 writes the obligation and mechanic per section into the protocol and the fixture author confirms each fixture targets exactly one.
- A2: The ablation tooling at `2a5ebf9` needs bounded adaptation: `validate_pilot.py` hard-codes 21 sections and frozen revision `2710486` and treats non-cp/ag sections as runbooks; `gen_prompts.py` defaults to the seven pilot sections and reads `arms/<section>-B.md` and `-C.md`; `run_fable.sh` has the completion predicate defect in Q2; `score.py` accepts a three-section manifest (the Reviewer ran its self-test against a synthetic tv manifest on 2026-09-13). Task_1 owns these adaptations and proves the whole chain (generate, validate, blind, score) on a stub run without model calls before Task_3 spends anything — source: the Reviewer's plan review of 2026-09-13.

## Tasks

### Task_1: Recover the tooling and pre-register the protocol
- type: impl
- owns:
  - docs/coding-agent/experiments/repeat-check-ablation/protocol.md
  - docs/coding-agent/experiments/repeat-check-ablation/manifest.yaml
  - docs/coding-agent/experiments/repeat-check-ablation/fixture-plan.md
  - docs/coding-agent/experiments/repeat-check-ablation/arms/**
  - docs/coding-agent/experiments/repeat-check-ablation/run/**
  - docs/coding-agent/experiments/repeat-check-ablation/score.py
  - docs/coding-agent/experiments/repeat-check-ablation/validate_pilot.py
- depends_on: []
- description: |
  Worker (Codex): recover `protocol.md`, `fixture-plan.md`, `score.py`, `validate_pilot.py`, and `run/` from `2a5ebf9` with `git show` into `docs/coding-agent/experiments/repeat-check-ablation/` (never into the old path); adapt them to this experiment and nothing more: the protocol's section list, arm definitions, one seed, and the grading rule per Q1 (all other protocol text carried over unchanged); `validate_pilot.py` takes its section list from `manifest.yaml`, its frozen revision from a `--frozen` argument recorded in the protocol, maps every tv section's source and arm-B text to `testing-validation.md` (replacing the cp/ag/runbook branches for these sections), takes the fixtures-per-section count from the manifest, and reads `authoring-notes.md` only when present; `gen_prompts.py` takes sections from the manifest and reads arm A from `arms/<section>-A.md` instead of the archived empty literal; `run_fable.sh` per Q2; write `manifest.yaml` (three sections, `seeds: 1`, both models) and the nine arm files (`arms/tv-<n>-A.md` the invariant obligation with no mechanics, `arms/tv-<n>-B.md` byte-equal to the main line's text for that section, `arms/tv-<n>-C.md` the conditional compression), with the same texts registered in the protocol. Prove the chain without model calls: generate prompts for a stub manifest (two fixtures per section, declared in the stub manifest), assert that each generated A, B, and C prompt contains exactly its registered arm text, run `validate_pilot.py --frozen <rev>`, `blind.py`, a stub runner that writes one fake success and one fake `is_error` result, `unblind.py`, and `score.py`, and show the `is_error` cell is not counted complete. Adaptations beyond this list are reported, not made. The Orchestrator then records the protocol SHA-256 and the frozen revision in the Decision Log before Task_2 starts.
- acceptance:
  - The protocol names the three sections with their invariant obligation and prescribed mechanic, the three arms per section with exact texts, the fixture counts, the seed, the models, the grading rule per Q1, the decision rule in full, and the spend cap per Q3; its SHA-256 and the frozen revision are in the Decision Log; the stub chain run passes and rejects the `is_error` cell.
- validation:
  - kind: command
    required: true
    owner: orchestrator
    detail: "From the experiment directory: python score.py --self-test; the stub chain run (gen_prompts, validate_pilot --frozen <rev>, blind, stub runner, unblind, score) with its output captured in the Worker report; sha256sum protocol.md recorded"
  - kind: review
    required: true
    owner: reviewer
    detail: "Protocol complete and pre-registered; arm A states the obligation without mechanics, arm B is byte-equal to main, arm C is conditional on absent evidence; the decision rule matches the 2026-09-08 protocol in full; the tooling diffs against 2a5ebf9 are only the listed adaptations; the stub chain proves every script and the generated prompts carry exactly the registered arm texts."

### Task_2: Author fixtures and keys
- type: impl
- owns:
  - docs/coding-agent/experiments/repeat-check-ablation/fixtures/**
  - docs/coding-agent/experiments/repeat-check-ablation/keys/**
- depends_on: [Task_1]
- description: |
  Worker (Codex): twelve planted fixtures and four decoys per section following `fixture-plan.md` conventions (a diff plus the validation summary the Worker would see; planted: the summary's evidence is inconclusive in the section's way; decoy: the summary already carries equivalent conclusive evidence and invites a redundant rerun), with keys naming the evidence gap, its location, and what evidence would close it; `validate_pilot.py --frozen <rev>` passes against the arm-B text.
- acceptance:
  - 48 fixtures and 3 keys validate; each planted fixture targets exactly one section (A1); each decoy shows the conclusive evidence explicitly so a demand for another run is a false positive, per the 2026-09-06 decoy-design lesson.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "python validate_pilot.py from the experiment directory: PASS over 3 sections"
  - kind: review
    required: true
    owner: reviewer
    detail: "Spot-check six planted and two decoy fixtures per section against the keys; confirm each planted gap is real and closable by more than one adequate means, and each decoy's evidence genuinely settles the question."

### Task_3: Run the cells and grade blind
- type: test
- owns:
  - docs/coding-agent/experiments/repeat-check-ablation/work/**
  - docs/coding-agent/experiments/repeat-check-ablation/outcome.md
- depends_on: [Task_2]
- description: |
  Orchestrator: generate prompts, run both runners detached (Q2), purge and rerun any cell whose JSON is not a success (Fable) or whose output lacks the done marker with exit 0 (Astra), within the Q3 cap, blind the outputs, dispatch one Claude grader per section per model with the arm hidden, unblind, score, and write `outcome.md` with the per-section table, the rule applied in full (including any protective tie or INCOMPLETE), and caveats.
- acceptance:
  - 288 cells complete under the success predicate within the cap (or the section is INCOMPLETE and ebigunso decides); six graders; 0 ungraded records; the outcome table names DELETE, COMPRESS, KEEP, or INCOMPLETE per section with dB, dC, ties, and the per-model false-positive guard.
- validation:
  - kind: command
    required: true
    owner: orchestrator
    detail: "python score.py --manifest manifest.yaml --seeds 1 work/results-fable.yaml work/results-astra.yaml reproduces the outcome table"
  - kind: review
    required: true
    owner: reviewer
    detail: "Recompute dB and dC from the results files; confirm grader independence and blinding; confirm the verdicts follow the pre-registered rule."

### Task_4: Apply the outcomes
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/testing-validation.md
- depends_on: [Task_3]
- description: |
  Worker: edit lines 74 and 77 per the outcome: DELETE replaces the line with its arm-A text (the obligation without mechanics), COMPRESS with its arm-C text, KEEP leaves it; the obligation survives in every case; nothing else in the file changes.
- acceptance:
  - The file differs from main only on the two lines; each edit matches the outcome table; every invariant obligation from the protocol is present in the edited text.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py; from repo root: git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "Edits match the outcome; replaced text equals the arm-A or arm-C text byte for byte; each obligation present; nothing else changed."

### Task_5: Final review and closeout with artifact removal
- type: review
- owns:
  - docs/coding-agent/experiments/**
  - plugins/coding-agent-orchestration-harness/.claude-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.codex-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.github/plugin/plugin.json
- depends_on: [Task_4]
- description: |
  Reviewer reviews the full diff against the Definition of Done with the experiment tree present; on APPROVED the Orchestrator records the outcome table and caveats in this plan's Decision Log, names the pre-removal commit and tags it (`evidence/repeat-check-ablation-<date>`, pushed to the remote) so it stays reachable after the squash merge and branch deletion, removes `docs/coding-agent/experiments/` in the closeout commit, bumps the three plugin manifests together, and moves the plan to completed.
- acceptance:
  - Reviewer status is APPROVED; the tree is gone on the merged branch; the Decision Log carries the outcome and the tag that keeps the evidence commit reachable; the manifests agree on the new version.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review vs Definition of Done before removal; after removal, confirm the Decision Log entry cites a commit that contains the tree."

## Task Waves (explicit parallel dispatch sets)

Interpretation:
- Tasks listed in the same wave are intended to be dispatched in parallel by default, when `owns` are disjoint and dependencies are met.
- Waves are executed sequentially.

- Wave 1 (parallel): [Task_1]
- Wave 2 (parallel): [Task_2]
- Wave 3 (parallel): [Task_3]
- Wave 4 (parallel): [Task_4]
- Wave 5 (parallel): [Task_5]

## Rollback / Safety
- Own feature branch off `main` after parts 1 and 2 merge; one PR. Runners move the user loader aside and restore it by hash; Fable cells run with tools disabled; nothing is written under `~/.codex` or `~/.claude` by agents; the experiment tree never reaches `main`.

## Progress Log (append-only)

Append-only editing rule (applies to both logs below): when appending an entry, anchor the edit on the previous entry and reproduce it (or anchor on the section's tail marker) so the edit inserts rather than replaces, and verify afterward that the log grew.

- 2026-09-16 Task_1 done (Codex Worker; Codex Reviewer NEEDS_REVISION at 5362943 on the missing log entry only; protocol, arms, and tooling passed). Tooling recovered from `2a5ebf9` into `docs/coding-agent/experiments/repeat-check-ablation/`; `score.py` and `run/run_astra.sh` byte-identical to the originals; the other scripts adapted within the three rulings below. Validation: `python score.py --self-test` exit 0 (Worker and Reviewer); stub chain (`run/self_check.py --frozen 76434f6`) exit 0 with the `is_error` cell rejected and the stale done marker ignored; `git diff --check` clean.

## Decision Log (append-only; re-plans and major discoveries)

- 2026-09-13 Decision: Plan drafted as part 3 of the Astra-guide follow-up.
  - Trigger / new insight: item 15 of the accepted list is a guidance removal, which ADR-D-0019 admits only with a pre-registered ablation; the article's rationale is Astra-specific, so both models run.
  - Plan delta (what changed): this plan exists; draft pending Reviewer plan review and ebigunso's approval. Research waived: the audit is the research; the method is the 2026-09-08 protocol.
  - Tradeoffs considered: editing the rules on the article's authority alone (rejected: ADR-D-0019); running Astra only (rejected: the harness serves Fable, and the 2026-09-09 run showed the models differ per section).
  - User approval: pending.
- 2026-09-13 Decision: Plan review round 1 (Codex Reviewer) findings applied.
  - Trigger / new insight: the draft let a guidance score delete whole evidence-integrity rules, while ADR-D-0019 protects evidence requirements and the audit had asked only whether redundant reruns are needed when equivalent evidence exists; A2 was false (the archived validator hard-codes 21 sections and revision 2710486, the prompt generator defaults to the old sections and needs arm files no task produced, the Fable runner counts an is_error cell as complete); Task_3 wrote outcome.md outside its owns; the cost comparison was wrong (288 of 1,344 is about a fifth) and unbounded by retries; no version bump owner.
  - Plan delta (what changed): the question is narrowed to the prescribed mechanics with the obligation invariant in every arm and outcome; arm A states the obligation without mechanics, arm C is conditional on absent evidence; fixtures and grading are built around evidence gaps versus equivalent evidence (Q1 restated); Task_1 becomes a Codex Worker task that owns the bounded tooling adaptations, produces the arm files, corrects the Fable success predicate (Q2), and proves the chain on a stub run before any spend; Task_3 owns outcome.md; Q3 sets the retry and spend cap with the stop rule; Task_5 owns the manifests and makes the evidence commit recoverable.
  - Tradeoffs considered: skipping the ablation and keeping the lines (rejected by ebigunso's choice to do all items); running the mechanics question on Astra only (rejected: the harness serves Fable).
  - User approval: pending with plan approval.
- 2026-09-13 Decision: Plan review round 2 (Codex Reviewer) findings applied.
  - Trigger / new insight: the archived prompt generator hard-codes arm A to an empty string, so registering A only in the protocol would leave A cells without the obligation text; the validator's tv sections would fall into the runbook branches and its fixed fixture count and unconditional authoring-notes read break the stub; Q3's two-retries-per-cell wording allowed 864 calls; pushing a branch that is later deleted does not keep the evidence commit reachable.
  - Plan delta (what changed): arm A files exist and the generator reads them; the validator maps tv sections to testing-validation.md and takes counts from the manifest; the pre-spend check asserts generated prompt contents; Q3 is 288 plus at most 96 retries, two per cell, 384 maximum, graders separate; the evidence commit is tagged and pushed.
  - Tradeoffs considered: none.
  - User approval: pending with plan approval.

- 2026-09-13 Decision: Q1, Q2, and Q3 resolved by ebigunso as proposed.
  - Trigger / new insight: ebigunso: "All questions in the three plans are otherwise settled as accepting your given recommendations."
  - Plan delta (what changed): the grading rule, the runner correction, and the call cap are registered as decided.
  - Tradeoffs considered: none.
  - User approval: yes for the three questions (2026-09-13); plan approval pending.

- 2026-09-15 Decision: Plan approved by ebigunso.
  - Trigger / new insight: Codex Reviewer plan review APPROVED (a3d8908); ebigunso: "I accept all the plans as well as the ADR. Get to work."
  - Plan delta (what changed): status approved. Executes after parts 1 and 2 merge.
  - Tradeoffs considered: none.
  - User approval: yes (2026-09-15).

- 2026-09-16 Decision: Execution as the third member of the stacked pull requests, per ebigunso.
  - Trigger / new insight: ebigunso: "You can go ahead and implement part 2 and 3 of the plans, as stacked PRs." Part 2 is closed and open as #68 on top of #67.
  - Plan delta (what changed): branch feature/2026-09-16/astra-guide-part3 is based on feature/2026-09-15/astra-guide-part2 and joins the gh stack; the `testing-validation.md` line numbers in Context are re-baselined against the part-2 result before the frozen revision is recorded (part 1 and part 2 did not edit that file, so the two lines are expected unchanged); the frozen revision for arm B is the part-3 branch tip at Task_1 time, recorded in the protocol.
  - Tradeoffs considered: waiting for #67 and #68 to merge (rejected by ebigunso's instruction).
  - User approval: yes (2026-09-15).

- 2026-09-16 Decision: Task_1 pre-registration recorded; three bounded tooling adaptations granted.
  - Trigger / new insight: the acceptance requires the protocol hash and frozen revision in this log before any model call; the Worker asked three questions the archived tooling raised (a C-length cap that no longer applies, protocol passages contradicting the approved design, and Fable cells that must not count on the done marker alone).
  - Plan delta (what changed): protocol `docs/coding-agent/experiments/repeat-check-ablation/protocol.md` SHA-256 `8506d6118e1d251fe6ae33d5a657b8ddc2e6f785585ca03b7a8523b76a3c3f43`; frozen revision `76434f6e0b45360412c073d8fd02eb86161dcffe` (the rebased branch base; `testing-validation.md` is byte-identical to the pre-rebase `c931246` it replaced, lines 74 and 77 unchanged since the audit). Rulings: (1) `validate_pilot.py` checks arm C against the registered contract (obligation plus one conditional hint) instead of the archived C <= B/3 cap and routes tv fixtures through the diff, commit-message, and Reviewer-notes checks; (2) protocol passages that contradicted the approved design were changed and every changed passage listed in the Worker report, all else verbatim; `fixture-plan.md` carries the tv authoring conventions and the 48 mapping slots; (3) `run/run_fable.sh` passes `--setting-sources ""` and counts a cell complete only on `is_error` false with a non-empty result; `unblind.py` takes the run date from the run; blinding admits successful cells only. Reviewer condition for Task_3: before each blinding pass create empty `work/blind/<model>/` and clear `work/grades/<model>/`, reconcile the file count with `mapping.json` before grading, import nothing from the 2026-09-08 experiment.
  - Tradeoffs considered: keeping the pre-rebase frozen revision (rejected: the commit no longer exists on the branch); re-running the stub chain after the repoint (done by the Reviewer, exit 0).
  - User approval: not required (within the approved plan; the Worker acted only on rulings, per ADR-D-0033).

## Notes
- Planned calls: 288 cells and six graders, about a fifth of the 2026-09-09 remaining-sections run (1,344 cells); the spend cap and stop rule are Q3.
