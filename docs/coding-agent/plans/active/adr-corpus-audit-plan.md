# Plan: ADR corpus audit and cleanup

- status: in_progress
- generated: 2026-09-06
- last_updated: 2026-09-07
- work_type: docs

## Goal
- Apply the admission criteria ebigunso set on 2026-09-06 to every live decision record in this repository, retire or fold what no longer binds, split bundles, rewrite what passes on substance but fails on form, and land each new or rewritten record only after its own explicit acceptance.

## Definition of Done
- Every live record under `docs/coding-agent-orchestration-harness/decisions/` has a recorded verdict (keep, rewrite, split, fold, retire) with the five criteria scored and a one-line reason each.
- Every verdict is applied, or its decline by ebigunso is recorded in the Decision Log; a declined rewrite leaves the record as accepted, and that record is exempt from the conformance bullet below.
- Every live record without a recorded decline conforms to `durable-docs-authoring/references/adr.md` as landed; retirements carry the header and live in `superseded/` with no dangling inbound pointer inside this repository.
- Every new or rewritten record has a standalone acceptance entry in this plan's Decision Log.

## Scope / Non-goals
- Scope: `docs/coding-agent-orchestration-harness/decisions/**`, and pointer-only edits (a filename or ID reference to a moved or renumbered record, nothing else on the line) in `docs/coding-agent/rules/_lifecycle.json`, `docs/coding-agent/rules/*.md`, `docs/coding-agent/lessons.md`, `docs/coding-agent/plans/completed/**`, `docs/coding-agent/plans/active/**`, and `docs/coding-agent/experiments/**`. Plan and lesson prose is not rewritten; only links are repaired so they resolve.
- Non-goals: changing the standard (that is `adr-standard-revision-plan.md`, which this plan depends on); auditing other repositories (the handoff text lives in the 2026-09-06 conversation, not in this repository).

## Compatibility stance
- surface: record filenames and IDs cited by other repositories' records or by plans.
- stance: migrate
- justification: inbound pointers inside this repository are repaired in the same commit as each move (Task_2). A citation from another repository to the old path does not follow a move; the moved file keeps its header naming the replacement, and repairing external citations is that repository's obligation when it runs the audit handoff. No external citer is known on 2026-09-06.

## Context (workspace)
- Related files/areas: twenty-four live records and two retired ones on the PR #57 branch at commit `227fa65`; `docs/coding-agent/plans/completed/adr-corpus-survey.md` (an earlier survey of another repository's records, not this corpus).
- Existing patterns or references: the records shaped under the criteria on PR #57 (ADR-D-0017 through ADR-D-0021) are the exemplars; `superseded/` mechanics and the retirement header form are in `durable-docs-authoring/references/adr.md` after the standard revision lands.
- Design record consulted and deviations from its acceptance: none applies.

## Open Questions (max 3)
- Q1: resolved 2026-09-06: yes, retire without replacement when nothing binds, header pointing at the absorbing record.
- Q2: resolved 2026-09-06: one record per acceptance ask.

## Assumptions
- A1: The standard revision has landed on `main` before Wave 1 starts — checked by the Orchestrator at dispatch (the plan is blocked otherwise).
- A2: The live record set is twenty-four files on the PR #57 branch at commit `227fa65` — source: `git ls-tree` at that commit, per the 2026-09-06 plan review; re-listed at dispatch.

## Tasks

### Task_1: Audit every live record
- type: research
- owns: []
- depends_on: []
- description: |
  Researcher, read-only. Inventory every live record (not under `superseded/`) with its date, consulted models or people, and every inbound pointer (grep the repository for its ID and filename). Apply the admission test and the structural rules in `durable-docs-authoring/references/adr.md` as landed, scoring the decision rather than the author or the record's age and scoring each decision separately where a record holds more than one. Classify each record as keep, rewrite, split, fold (into which record), or retire, citing the `adr.md` criterion or rule that decides it. For split or rewrite, state in one line the decision each resulting record would carry. Return the verdict table and, separately, every place the standard was unclear when applied.
- acceptance:
  - Every live record has a verdict citing the deciding `adr.md` criterion or rule; no record is scored on precedent or on its author.
  - Standard gaps are listed separately from verdicts.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Spot-check five verdicts against the records and the criteria; confirm the table covers every live file."

### Task_2: Apply the verdicts
- type: docs
- owns:
  - docs/coding-agent-orchestration-harness/decisions/**
  - docs/coding-agent/rules/_lifecycle.json
  - docs/coding-agent/rules/*.md
  - docs/coding-agent/lessons.md
  - docs/coding-agent/plans/completed/**
  - docs/coding-agent/plans/active/**
  - docs/coding-agent/experiments/**
- depends_on: [Task_1]
- description: |
  Orchestrator-authored, in batches by verdict. Retirements and folds first: set `status: superseded`, add the retirement header under the title, move to `superseded/` with the `--superseded-by-ADR-X` or `--retired` suffix, repair every inbound pointer, run an absence search for the old filename. Then splits and rewrites: draft each resulting record to the template, one decision each, present it to ebigunso on its own as title, decision, constraint, and why, and land it only on an explicit yes; a no retires nothing and is recorded in this plan's Decision Log. Numbers are assigned in landing order; a dropped draft frees its number. Outside `decisions/`, this task edits only pointer lines (a filename or ID reference to a moved or renumbered record) so links resolve; prose in plans, lessons, and rules is left as written. This plan runs after the standard revision has merged, so its pointer-only edits to `lessons.md` and `rules/*.md` never overlap that plan in time. An active plan that cites a record slated for retirement (on 2026-09-06, `frontier-guidance-follow-ups-plan.md` cites ADR-I-0004 and ADR-I-0005) gets its pointer repaired in the same commit; if that plan is under execution at the time, the Orchestrator records the pointer change in that plan's Decision Log.
- acceptance:
  - Every Task_1 verdict is applied or declined with the decline recorded.
  - Every live record without a recorded decline conforms to `adr.md` as landed, by the Reviewer's check.
  - Every new or rewritten record has an acceptance entry in the Decision Log; every decline has a decline entry.
- validation:
  - kind: command
    required: true
    owner: orchestrator
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py; from repository root: git diff --check; absence search for every retired filename outside superseded/ and plans/completed/"
  - kind: review
    required: true
    owner: reviewer
    detail: "Per live record without a recorded decline: conformance to durable-docs-authoring/references/adr.md as landed; retirements have headers and no dangling inbound pointer inside the repository; pointer-only edits outside decisions/ changed nothing but the reference."

### Task_3: Final review and closeout
- type: review
- owns: []
- depends_on: [Task_2]
- description: |
  Whole-change review against the Definition of Done.
- acceptance:
  - Reviewer status is APPROVED.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review of the full change set vs Definition of Done; confirm every accepted record has its acceptance entry and every decline is recorded."

## Task Waves (explicit parallel dispatch sets)

Interpretation:
- Tasks listed in the same wave are intended to be dispatched in parallel by default, when `owns` are disjoint and dependencies are met.
- Waves are executed sequentially.

- Wave 1 (parallel): [Task_1]
- Wave 2 (parallel): [Task_2]
- Wave 3 (parallel): [Task_3]

## Rollback / Safety
- Own feature branch off `main` after the standard revision merges; retired records are moved, never deleted, so every retirement reverses by moving the file back.
- No record lands without a recorded standalone acceptance.

## Progress Log (append-only)

Append-only editing rule (applies to both logs below): when appending an entry, anchor the edit on the previous entry and reproduce it (or anchor on the section's tail marker) so the edit inserts rather than replaces, and verify afterward that the log grew.

- (none yet)

## Decision Log (append-only; re-plans and major discoveries)

- 2026-09-06 Decision: Research is Task_1, not a prerequisite.
  - Trigger / new insight: the audit itself is the research; nothing needs discovery before it is dispatched.
  - Plan delta (what changed): none.
  - Tradeoffs considered: none material.
  - User approval: pending with plan approval.
- 2026-09-06 Decision: Plan review round 1 (Codex Reviewer) findings applied.
  - Trigger / new insight: pointer repairs outside decisions/ had no owner; a declined rewrite contradicted the conformance bullet; the plan restated the standard; the superseded/ move does not preserve external URLs; the inventory count was wrong (twenty-four live records, not twenty-one).
  - Plan delta (what changed): Task_2 owns pointer-only edits in the named docs paths, sequenced after the standard plan merges; declines exempt a record from conformance and are recorded; the audit cites adr.md instead of restating it; the compatibility stance states the external-citation limitation; the count is corrected.
  - Tradeoffs considered: none material.
  - User approval: pending with plan approval.
- 2026-09-06 Decision: Plan review round 2 (Codex Reviewer) finding applied.
  - Trigger / new insight: active plans cite records this plan may retire (ADR-I-0004 and ADR-I-0005 in the follow-ups plan), and pointer repair there had no owner.
  - Plan delta (what changed): `docs/coding-agent/plans/active/**` added to Task_2's pointer-only owns, with the Decision Log note rule for plans under execution.
  - Tradeoffs considered: none material.
  - User approval: pending with plan approval.
- 2026-09-06 Decision: Plan approved by user with the proposed answers to all open questions.
  - Trigger / new insight: user approval after reviewer approval.
  - Plan delta (what changed): status approved; execution begins after PR #57 merges.
  - Tradeoffs considered: none.
  - User approval: yes (2026-09-06).

## Notes
- Risks: many rewrites at once; Task_2 presents one record per ask so acceptance stays deliberate. A citation from another repository to a moved record breaks until that repository runs the audit handoff; the moved file's header limits the damage to a stale path.
- Edge cases: a record that is both bundled and stale is split first, then each part is judged.
