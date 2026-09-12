# Plan: Ablate the repeat-check rules in testing-validation.md (Astra guide, part 3 of 3)

- status: draft
- generated: 2026-09-13
- last_updated: 2026-09-13
- work_type: mixed

## Goal
- Decide, with class-matched evidence under ADR-D-0019's guidance class, whether the three repeat-check rules in `engineering-quality-baselines/references/testing-validation.md` (targeted rerun plus no-skip confirmation; verifying gated live tests once with the service deliberately down; baseline rerun when an untouched test fails) change what Claude Fable 5.1 and GPT-6 Astra do when they already hold conclusive evidence, and delete, compress, or keep each rule by the pre-registered outcome. Item 15 of the accepted 2026-09-13 audit list; the article's "Astra self-verifies" claim is the motivation, and the two-model design keeps the decision honest for Fable.

## Definition of Done
- The protocol is pre-registered in this plan before any cell runs: three arms per rule (A: rule deleted; B: rule as on main; C: a one-sentence compression), twelve planted fixtures and four decoys per rule where a planted fixture is a change whose only defect is what the rule catches (a skipped test hidden by a green summary; a gated live test that passes only because the gate is off; a pre-existing failure attributed to the change), one seed, two models, blinded grading with the arm hidden, and the decision rule of the 2026-09-08 ablation (worst model; dB under 10 points DELETE; dC within 5 points of dB COMPRESS; else KEEP; false-positive guard on decoys).
- The three rules are each classified DELETE, COMPRESS, or KEEP by that rule, the text edited accordingly, and the outcome table plus caveats recorded in this plan's Decision Log.
- The experiment tree (protocol, fixtures, keys, arms, runners, results, grades) lives on the plan branch during execution and is removed in the closeout commit, with the pre-removal commit named in the Decision Log, per ebigunso's 2026-09-10 ruling on experiment artifacts.
- No other line of `testing-validation.md` changes; the required-check waiver template, evidence fields, and the anti-theater guidance stay.

## Scope / Non-goals
- Scope: `testing-validation.md:74` and `:77` (the two lines carrying the three rules) and the experiment tree during execution.
- Non-goals: any other guidance in `engineering-quality-baselines`; Reviewer-owned checks (independent evidence stays per ADR-D-0004); required checks and waivers (never removable per ADR-D-0019).

## Compatibility stance
- surface: one reference file read by Workers and Reviewers on non-trivial validation work.
- stance: migrate
- justification: consumers are in this repository; refresh after merge with the part-2 or a later version bump.

## Context (workspace)
- Related files/areas: `plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/testing-validation.md:74,77`; the removed `docs/coding-agent/experiments/guidance-class-ablation/` tree in git history at `2a5ebf9` (`protocol.md`, `fixture-plan.md`, `manifest.yaml`, `score.py`, `validate_pilot.py`, `run/gen_prompts.py`, `run/run_astra.sh`, `run/run_fable.sh`, `run/blind.py`, `run/unblind.py`), whose method this plan reuses unchanged except for the section list.
- Existing patterns or references: ADR-D-0019 (guidance class: pre-registered ablation; removal only with class-matched evidence); the 2026-09-08 and 2026-09-09 ablation outcomes recorded in `docs/coding-agent/plans/completed/frontier-guidance-follow-ups-plan.md` (Decision Log: grading ruling, one-seed cap, per-section blinded grading, rulings scoped to runbooks).
- Design record consulted and deviations from its acceptance: ADR-D-0019 followed as written.
- Prior evidence: the Codex Researcher audit (agmsg, 2026-09-12 16:30Z) item 11 marks these rules Astra-only in motivation and says a static audit justifies no weakening; the cost of the 2026-09-09 runs (about $0.07 per Fable cell through the headless CLI, Astra cells through ephemeral `codex exec`) bounds this plan at 3 rules x 3 arms x 16 fixtures x 2 models = 288 cells plus six blinded graders.

## Open Questions (max 3)
- Q1: Grading rule for these fixtures. Proposed: a hit requires the response to detect the specific defect (the hidden skip, the ungated pass, the pre-existing failure) and to name a remediation of the kind the rule prescribes; ebigunso's 2026-09-08 runbook ruling (any working remediation counts) is not extended here, matching the 2026-09-09 scope decision.
- Q2: Runners. Proposed: reuse `run_fable.sh` and `run_astra.sh` from `2a5ebf9` byte-for-byte (web search disabled, loader aside and restored by hash, restricted Claude CLI), relaunched detached as before.

## Assumptions
- A1: The three rules are separable into three sections for the manifest (tv-1 targeted rerun and no-skip confirmation; tv-2 gated live test with service down; tv-3 baseline rerun on untouched-test failure) — source: the two lines' structure; the fixture author confirms each fixture targets exactly one.
- A2: The ablation tooling at `2a5ebf9` runs unchanged against a new manifest — source: `score.py --self-test` and `validate_pilot.py` at that commit; Task_1 verifies before any cell runs.

## Tasks

### Task_1: Recover the tooling and pre-register the protocol
- type: docs
- owns:
  - docs/coding-agent/experiments/repeat-check-ablation/**
- depends_on: []
- description: |
  Orchestrator: `git checkout 2a5ebf9 -- docs/coding-agent/experiments/guidance-class-ablation/{protocol.md,score.py,validate_pilot.py,run/}` into `docs/coding-agent/experiments/repeat-check-ablation/`, adapt `protocol.md` only in its section list and arm definitions (three sections, arm C text per rule drafted here), write `manifest.yaml`, run `score.py --self-test`, and record the protocol hash in the Decision Log before Task_2 starts.
- acceptance:
  - The protocol names the three sections, the three arms per section with their exact texts, the fixture counts, the seed, the models, the grading rule per Q1, and the decision rule; its SHA-256 is in the Decision Log; the self-test passes.
- validation:
  - kind: command
    required: true
    owner: orchestrator
    detail: "python score.py --self-test from the experiment directory; sha256sum protocol.md recorded"
  - kind: review
    required: true
    owner: reviewer
    detail: "Protocol is complete and pre-registered; arm C texts are compressions, not rewrites; the decision rule matches the 2026-09-08 protocol."

### Task_2: Author fixtures and keys
- type: impl
- owns:
  - docs/coding-agent/experiments/repeat-check-ablation/fixtures/**
  - docs/coding-agent/experiments/repeat-check-ablation/keys/**
- depends_on: [Task_1]
- description: |
  Worker (Codex): twelve planted fixtures and four decoys per section following `fixture-plan.md` conventions (a diff plus the validation summary the Worker would see; planted: the summary hides the defect the rule catches; decoy: a clean change with a summary that invites a false alarm), with keys naming the defect, its location, and the remediation kind; `validate_pilot.py` passes against the frozen arm-B text.
- acceptance:
  - 48 fixtures and 3 keys validate; each planted fixture targets exactly one section (A1); decoys contain the hardening a naive reviewer would demand, per the 2026-09-06 decoy-design lesson.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "python validate_pilot.py from the experiment directory: PASS over 3 sections"
  - kind: review
    required: true
    owner: reviewer
    detail: "Spot-check six planted and two decoy fixtures per section against the keys and the section's rule; confirm no fixture is solvable without the rule's mechanism and no decoy is a trap."

### Task_3: Run the cells and grade blind
- type: test
- owns:
  - docs/coding-agent/experiments/repeat-check-ablation/work/**
- depends_on: [Task_2]
- description: |
  Orchestrator: generate prompts, run both runners detached (Q2), purge and rerun any cell that did not exit 0 with the done marker, blind the outputs, dispatch one Claude grader per section per model with the arm hidden, unblind, score, and write `outcome.md` with the per-section table, the rule applied, and caveats.
- acceptance:
  - 288 cells complete with exit 0; six graders; 0 ungraded records; the outcome table names DELETE, COMPRESS, or KEEP per section with dB and dC and the false-positive guard result.
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
  Worker: edit lines 74 and 77 per the outcome (delete the rule, replace it with its arm-C text, or leave it); nothing else in the file changes.
- acceptance:
  - The file differs from main only on the two lines, and each edit matches the outcome table.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py; from repo root: git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "Edits match the outcome; compressed text equals the arm-C text byte for byte; nothing else changed."

### Task_5: Final review and closeout with artifact removal
- type: review
- owns:
  - docs/coding-agent/experiments/**
- depends_on: [Task_4]
- description: |
  Reviewer reviews the full diff against the Definition of Done with the experiment tree present; on APPROVED the Orchestrator records the outcome table and caveats in this plan's Decision Log, names the pre-removal commit, removes `docs/coding-agent/experiments/` in the closeout commit, and moves the plan to completed.
- acceptance:
  - Reviewer status is APPROVED; the tree is gone on the merged branch; the Decision Log carries the outcome and the commit that holds the evidence.
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

- (none yet)

## Decision Log (append-only; re-plans and major discoveries)

- 2026-09-13 Decision: Plan drafted as part 3 of the Astra-guide follow-up.
  - Trigger / new insight: item 15 of the accepted list is a guidance removal, which ADR-D-0019 admits only with a pre-registered ablation; the article's rationale is Astra-specific, so both models run.
  - Plan delta (what changed): this plan exists; draft pending Reviewer plan review and ebigunso's approval. Research waived: the audit is the research; the method is the 2026-09-08 protocol.
  - Tradeoffs considered: editing the rules on the article's authority alone (rejected: ADR-D-0019); running Astra only (rejected: the harness serves Fable, and the 2026-09-09 run showed the models differ per section).
  - User approval: pending.

## Notes
- Cost bound: 288 cells and six graders, about a third of the 2026-09-09 remaining-sections run.
