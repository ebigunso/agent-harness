# Plan: Remove the experiment artifacts from the docs tree

- status: draft
- generated: 2026-09-10
- last_updated: 2026-09-10
- work_type: docs

## Goal
- Remove `docs/coding-agent/experiments/` in full (the frontier guard probes and the guidance-class ablation: 4,660 tracked files, about 32 MB of transcripts, fixtures, manifests, and scripts) now that every decision they served has landed, and repair the three live records that point at the tree so they point at git history instead, following the precedent set when the language-guide ablation records were removed after ADR-I-0004 and ADR-I-0005 (their records cite the commit that holds the evidence).

## Definition of Done
- `docs/coding-agent/experiments/` no longer exists in the working tree; the last commit that holds it is named in every repaired pointer so the evidence stays recoverable from history.
- The `.gitattributes` line whose only purpose was that tree is removed (the file goes with it if nothing else remains).
- Pointer repairs, and nothing else, in the three accepted records that cite the tree (ADR-D-0019 More Information, ADR-D-0022 Revisit When, ADR-D-0032 More Information): each names the pre-removal commit as the location, with no change to any decision, boundary, reason, or reopen condition (adr.md permits pointer repair after merge).
- Historical mentions in completed plans and in `lessons.md` stay as written; they are dated chronicles of the state at the time.
- Package validation and smoke tests pass; nothing under `plugins/` changes.

## Scope / Non-goals
- Scope: `docs/coding-agent/experiments/**`, `.gitattributes`, the three pointer lines named above.
- Non-goals: rewriting completed plans or lessons; retiring or rewriting any record; removing `docs/coding-agent/skill-candidates.md` or any plan file; touching `plugins/`.

## Compatibility stance
- surface: documentation only; no runtime consumer reads the experiments tree (grep over `plugins/` and the rules finds no reference).
- stance: migrate
- justification: the evidence remains in git history at the named commit; the records that cite it are repaired to say so.

## Context (workspace)
- Related files/areas: `docs/coding-agent/experiments/frontier-guard-probes/` (README, fixtures, prompts, two runners, three results records, the Task_1 inventory, live-loader transcripts and boundary runs); `docs/coding-agent/experiments/guidance-class-ablation/` (protocol, manifest, fixtures, keys, arms, runners, outcome, work/ grades and results); `.gitattributes` (one line, added for the boundary transcripts).
- Existing patterns or references: ADR-I-0004 and ADR-I-0005 (superseded) cite `47c409c` and `e221d34` for evidence removed from the tree after the decision landed.
- Design record consulted and deviations from its acceptance: ADR-D-0019 (removal evidence lives with the experiment and the closing plan); after this change "with the experiment" means the named commit, which the record's More Information will say.
- Prior evidence: reference grep on 2026-09-10 (this plan's Decision Log).

## Open Questions (max 3)
- Q1: the Orchestrator performs the deletion and the three pointer edits directly rather than dispatching a Worker (a `git rm -r` of one tree plus three one-line edits, all shared-state Git work the Orchestrator controls anyway); the Reviewer reviews the diff. Proposed: yes, with the Worker-dispatch waiver recorded in the Decision Log per lessons.md 2026-05-17.

## Assumptions
- A1: No file outside `docs/coding-agent/experiments/`, the three records, `.gitattributes`, completed plans, and `lessons.md` references the tree — source: `grep -rn "experiments/"` and `grep -rn "frontier-guard-probes\|guidance-class-ablation"` over the repository on 2026-09-10.

## Tasks

### Task_1: Remove the tree and repair the pointers
- type: docs
- owns:
  - docs/coding-agent/experiments/**
  - .gitattributes
  - docs/coding-agent-orchestration-harness/decisions/ADR-D-0019-remove-harness-content-only-with-class-matched-evidence.md
  - docs/coding-agent-orchestration-harness/decisions/ADR-D-0022-workflow-mechanics-have-one-home.md
  - docs/coding-agent-orchestration-harness/decisions/ADR-D-0032-plan-approval-is-never-self-granted.md
- depends_on: []
- description: |
  `git rm -r docs/coding-agent/experiments`; remove the `.gitattributes` entry; in each of the three records replace the tree path with "in git history at `<commit>`" where `<commit>` is the main commit immediately before the removal, changing no other word.
- acceptance:
  - The tree is gone; `git ls-files docs/coding-agent/experiments` is empty; the three records differ from main only on the pointer line.
- validation:
  - kind: command
    required: true
    owner: orchestrator
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py && python scripts/run_validation_smoke_tests.py; from repo root: git diff --check; grep -rn 'experiments/' outside completed plans and lessons returns only the repaired pointers."
  - kind: review
    required: true
    owner: reviewer
    detail: "Confirm the diff is the tree removal, the attribute line, and three pointer-only edits; confirm each pointer names a commit that contains the removed path; confirm no decision text changed."

## Task Waves (explicit parallel dispatch sets)

Interpretation:
- Tasks listed in the same wave are intended to be dispatched in parallel by default, when `owns` are disjoint and dependencies are met.
- Waves are executed sequentially.

- Wave 1 (parallel): [Task_1]

## Rollback / Safety
- Own feature branch off `main`; one PR; reverting it restores the tree and the pointers.
- Evidence stays in history at the named commit; nothing is force-pushed or rewritten.

## Progress Log (append-only)

Append-only editing rule (applies to both logs below): when appending an entry, anchor the edit on the previous entry and reproduce it (or anchor on the section's tail marker) so the edit inserts rather than replaces, and verify afterward that the log grew.

- (none yet)

## Decision Log (append-only; re-plans and major discoveries)

- 2026-09-10 Decision: Plan drafted on ebigunso's request to remove the experiment artifacts from the docs tree.
  - Trigger / new insight: ebigunso: "clean up the docs so that all of the experiment artifacts are removed ... Remove and reduce clutter rather than keeping them persisted indefinitely." Reference grep: three accepted records cite the tree (ADR-D-0019:57, ADR-D-0022:47, ADR-D-0032:51); the superseded ADR-I-0004 and ADR-I-0005 already model the "in git history at commit" form; completed plans and one lessons line cite paths as dated history; nothing under `plugins/` or the rules references the tree.
  - Plan delta (what changed): this plan exists; draft pending Reviewer plan review and ebigunso's approval. Research waived: the Orchestrator ran the reference grep directly (a read is cheaper than a dispatch and the result is reproduced here).
  - Tradeoffs considered: keeping the summary records (`outcome.md`, the results files) and deleting only raw transcripts and fixtures (rejected: ebigunso asked for the artifacts to go, the closing plans already carry the outcomes, and partial trees invite the same question again).
  - User approval: pending.

## Notes
- The removal commit's parent on main is the pointer target; it is known only at execution time and is filled in then.
