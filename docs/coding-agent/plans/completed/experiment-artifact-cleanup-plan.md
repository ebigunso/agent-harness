# Plan: Remove the experiment artifacts from the docs tree

- status: completed
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
- Q1: resolved 2026-09-10 by ebigunso ("Q1 OK."): the Orchestrator performs the deletion and the three pointer edits directly; Worker dispatch waived for this task with that ruling as the record; the Reviewer reviews the diff.

## Assumptions
- A1: The only files outside `docs/coding-agent/experiments/` that mention the tree (any of `experiments/`, `frontier-guard-probes`, `guidance-class-ablation`) are: the three accepted records (repaired here); `.gitattributes` (removed here); the two frozen superseded records ADR-I-0004 and ADR-I-0005 (already cite git history; untouched); the four completed plans and `lessons.md` (dated history; untouched); and this plan — source: repository-wide grep on 2026-09-10, confirmed by the Reviewer's plan review with `rg --hidden --no-ignore` (12 files, no other consumer).

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
  `git rm -r docs/coding-agent/experiments`; delete `.gitattributes` (its only content is the evidence exemption and its comment); in each of the three records keep the specific evidence path and qualify it with "in git history at `<commit>`" where `<commit>` is the main commit immediately before the removal, changing no other word (ADR-D-0019's separate language-guide-ablation pointer already reads that way and stays).
- acceptance:
  - The tree is gone; `git ls-files docs/coding-agent/experiments` is empty; the three records differ from main only on the pointer line.
- validation:
  - kind: command
    required: true
    owner: orchestrator
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py && python scripts/run_validation_smoke_tests.py; from repo root: git diff --check; a repository-wide search for 'experiments/', 'frontier-guard-probes', and 'guidance-class-ablation' (excluding .git) returns only: the three repaired records with their commit-qualified pointers, the two superseded records, the four completed plans, lessons.md, and this plan; any other hit is a missed consumer and blocks."
  - kind: review
    required: true
    owner: reviewer
    detail: "Confirm the diff is the tree removal, the .gitattributes deletion, and three pointer-only edits; confirm the named commit is the main commit immediately before the removal and contains each cited path (git ls-tree); confirm no decision, boundary, reason, or reopen condition changed; rerun the three-term search."

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

- 2026-09-10 Wave 1 Task_1 executed, review pending: [Task_1]
  - Summary: `git rm -r docs/coding-agent/experiments` (4,660 files) and `.gitattributes`; pointer repairs in ADR-D-0019, ADR-D-0022, ADR-D-0032 qualifying the frontier-guard-probes path with "in git history at `2a5ebf9`" (the main tip and merge base at execution, which holds both subtrees). No other word changed.
  - Validation evidence: validate_harness_package.py pass; run_validation_smoke_tests.py exit 0; git diff --check clean; three-term search returns exactly the allowed set (three repaired records, ADR-I-0004, ADR-I-0005, four completed plans, lessons.md, this plan) and nothing else.
  - Notes: Reviewer review dispatched.
- 2026-09-10 Wave 1 Task_1 done; plan closed: [Task_1]
  - Summary: as above, at c9aa484.
  - Validation evidence: Codex Reviewer Task_1 APPROVED (diff is the removal, the .gitattributes deletion, and three pointer-only edits; 2a5ebf9 holds both subtrees; search set exact; package and smoke checks pass).
  - Notes: no lessons; the precedent (ADR-I-0004/0005) was followed. Plan moved to completed/.

## Decision Log (append-only; re-plans and major discoveries)

- 2026-09-10 Decision: Plan drafted on ebigunso's request to remove the experiment artifacts from the docs tree.
  - Trigger / new insight: ebigunso: "clean up the docs so that all of the experiment artifacts are removed ... Remove and reduce clutter rather than keeping them persisted indefinitely." Reference grep: three accepted records cite the tree (ADR-D-0019:57, ADR-D-0022:47, ADR-D-0032:51); the superseded ADR-I-0004 and ADR-I-0005 already model the "in git history at commit" form; completed plans and one lessons line cite paths as dated history; nothing under `plugins/` or the rules references the tree.
  - Plan delta (what changed): this plan exists; draft pending Reviewer plan review and ebigunso's approval. Research waived: the Orchestrator ran the reference grep directly (a read is cheaper than a dispatch and the result is reproduced here).
  - Tradeoffs considered: keeping the summary records (`outcome.md`, the results files) and deleting only raw transcripts and fixtures (rejected: ebigunso asked for the artifacts to go, the closing plans already carry the outcomes, and partial trees invite the same question again).
  - User approval: pending.
- 2026-09-10 Decision: Plan review round 1 (Codex Reviewer) findings applied.
  - Trigger / new insight: the required reference check was unsatisfiable as written (the two frozen superseded records and this plan itself carry the path text and must stay); A1 omitted the same exceptions and named only one of the three search terms; Q1 is a proposal until ebigunso rules on it.
  - Plan delta (what changed): A1 lists every citing file and its disposition; the Task_1 command check names all three terms and the exact allowed set; pointers keep the specific evidence path qualified with the commit; `.gitattributes` is deleted as a whole file; the Reviewer check verifies the commit contains each cited path.
  - Tradeoffs considered: none.
  - User approval: pending with plan approval, including Q1.
- 2026-09-10 Decision: Plan approved by ebigunso with Q1 as proposed.
  - Trigger / new insight: Codex Reviewer Plan_Review APPROVED at ecae8c7; ebigunso: "Q1 OK. I approve of the plan. Get to work."
  - Plan delta (what changed): status in_progress; Worker dispatch waived for Task_1 by ebigunso's ruling; pointer target fixed at 2a5ebf9.
  - Tradeoffs considered: none.
  - User approval: yes (2026-09-10).

## Notes
- The removal commit's parent on main is the pointer target; it is known only at execution time and is filled in then.
