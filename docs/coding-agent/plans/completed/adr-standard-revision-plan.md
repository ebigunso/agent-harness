# Plan: ADR standard revision

- status: completed
- generated: 2026-09-06
- last_updated: 2026-09-06
- work_type: docs

## Goal
- Make the `durable-docs-authoring` skill produce ADRs that pass the admission criteria ebigunso set on 2026-09-06 (load-bearing, severe if ignored, not derivable from the artifact, the why stated for a first-time reader, only active content), and stop it from producing removal ledgers, evidence dumps, bundled decisions, partial supersessions, and records nobody explicitly accepted.

## Definition of Done
- `references/adr.md` opens with the admission test (the five criteria plus the two negatives: re-derivable from git or the plan; "do not re-add these files") and states: one decision per record; the sentence-level altitude rule; the ban on time-relative wording; the precedence rule (a directive in an older record or a precedent's shape is not a warrant); the draft/accepted/superseded lifecycle with immutability attaching at merge; full replacement only, partial supersession abolished; standalone human acceptance for every record, never implied by plan approval or merge.
- `references/adr-template.md` has no Measurement Basis, Implementation Impact, Consultation Impact, or `supersession_scope`; it has a required prose Why; its comment lines are one-line prohibitions that point at `adr.md` and carry no rationale.
- Plan-format, prompt-snippets, the reviewer packet, the Escalation Ruling reference, and the skill trigger route to `adr.md` by path and carry only their operational form (a question list, a field, a one-line gate) with no rationale; the final-response contract carries an "ADRs proposed" line; the package validator rejects a live record with `supersession_scope: partial`.
- The 2026-09-06 lesson on ADR drift carries its final prevention list and one orchestrator rule encodes it.

## Scope / Non-goals
- Scope: `plugins/coding-agent-orchestration-harness/skills/durable-docs-authoring/**`; the routing lines in `plan-format`, `subagent-strategy/references/prompt-snippets.md`, `wave-integration/references/reviewer-packet-template.md`, `orchestration-harness/references/{lifecycle-gates,final-response-contract}.md`; `scripts/validate_harness_package.py`; `docs/coding-agent/rules/orchestrator.md`; `docs/coding-agent/lessons.md`.
- Non-goals: auditing or changing existing records (that is `adr-corpus-audit-plan.md`, which depends on this plan landing); a cross-repository skill reference for the audit (handoff text is given in chat); the follow-ups in `frontier-guidance-follow-ups-plan.md`.

## Compatibility stance
- surface: ADR frontmatter keys and the `superseded/` naming convention, read by humans and by other repositories that copied the template.
- stance: migrate
- justification: no tool parses ADR frontmatter (A1); records in this repository migrate under the corpus audit plan; other repositories migrate when they run the audit handoff.

## Context (workspace)
- Related files/areas: `plugins/coding-agent-orchestration-harness/skills/durable-docs-authoring/{SKILL.md,references/adr.md,references/adr-template.md,references/adr-repo-readme.md}` and the routing surfaces in Scope.
- Existing patterns or references: the records shaped under the criteria on PR #57 (ADR-D-0017 through ADR-D-0021) are the exemplars; the `superseded/` mechanics in `adr.md` already exist and stay; `docs/coding-agent/lessons.md` entry "ADRs Drifted Into Removal Ledgers Despite The Warrant Standard" (2026-09-06) lists the root causes this plan removes.
- Rulings from the 2026-09-06 conversation that this plan encodes: ADR acceptance is its own explicit ask; drafts on a branch are mutable and renumberable, records on `main` are immutable; retire and replace rather than revise; one decision per record; the why in a sentence or two, no evidence sections; no relative time; plan-time proposal is preferred but mid-implementation discoveries follow record-and-surface and are still accepted on their own.
- Design record consulted and deviations from its acceptance: none applies; Task_1 runs the admission test on the standard change itself.

## Open Questions (max 3)
- Q1: resolved 2026-09-06: replace the `warrant` block; Decision and Why carry it.
- Q2: resolved 2026-09-06: Task_1 runs the admission test and proposes a record only if it passes.

## Assumptions
- A1: No script parses ADR frontmatter — source: `grep -rn "warrant\|supersession_scope" plugins/coding-agent-orchestration-harness/scripts` returns nothing on 2026-09-06.
- A2: The exemplar records ADR-D-0017 through ADR-D-0021 were accepted by ebigunso on 2026-09-06 as standalone decisions — source: `docs/coding-agent/plans/completed/frontier-model-guidance-refresh-plan.md` Decision Log.

## Tasks

### Task_1: Rewrite the ADR standard
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/durable-docs-authoring/**
  - docs/coding-agent-orchestration-harness/decisions/ADR-D-0022-*.md
- depends_on: []
- description: |
  Orchestrator-authored (writing-strength, per model-routing). Rewrite `references/adr.md` so the admission test comes first and the warrant vocabulary is gone: the five criteria; the two negatives; one decision per record (test: can it be retired alone); altitude (the why is a sentence or two, no evidence sections, a dated model check in Revisit When is the only pointer); no time-relative wording (name models, dates, PRs); precedence (a directive in an older record or a precedent's shape is not a warrant; run the test on every proposed record); lifecycle (draft on a branch is mutable and renumberable, immutable from merge, changes retire and replace in full, partial supersession abolished, reversal and refinement both replace); acceptance (each record presented to a human on its own as title, decision, constraint, why, and accepted explicitly; plan approval and merge do not accept; a no is terminal; plan time is preferred, mid-implementation discoveries follow record-and-surface). Rewrite `references/adr-template.md` to match (required prose Why; drop Measurement Basis, Implementation Impact, Consultation Impact, `supersession_scope`; comments forbid ledgers, evidence, implementation wording, relative time). Update `adr-repo-readme.md` for the retirement header and full-retirement-only `superseded/`. Update `SKILL.md` to trigger also when a plan or record directs an ADR to be written. Then run the admission test on this standard change itself: if it passes, draft one new record (the next free number, expected ADR-D-0022) and present it to ebigunso on its own, landing it only on acceptance; if it fails, say so in the report. This is the only record this plan may create; existing records belong to the corpus audit plan.
- acceptance:
  - `adr.md` contains no occurrence of "warrant" as the admission concept and its first section is the admission test.
  - `adr-template.md` contains none of the four removed sections or keys and has a Why section.
  - Every rule listed in the description is stated, with its rationale, exactly once, in `adr.md`; `adr-template.md` comment lines and `SKILL.md` carry only one-line prohibitions or triggers that point at `adr.md`.
  - If a record was drafted, it was presented on its own and the acceptance answer is in this plan's Decision Log.
- validation:
  - kind: command
    required: true
    owner: orchestrator
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py; from repository root: git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "Read the rewritten standard against the 2026-09-06 rulings listed in Context; flag any rule missing, any rule duplicated, any wording that would have admitted the ADR-I-0006 ledger or the bundled first ADR-D-0017."

### Task_2: Route the harness to the standard
- type: impl
- owns:
  - plugins/coding-agent-orchestration-harness/skills/plan-format/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/plan-format/references/plan-template.md
  - plugins/coding-agent-orchestration-harness/skills/subagent-strategy/references/prompt-snippets.md
  - plugins/coding-agent-orchestration-harness/skills/wave-integration/references/reviewer-packet-template.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/lifecycle-gates.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/final-response-contract.md
  - plugins/coding-agent-orchestration-harness/scripts/validate_harness_package.py
  - plugins/coding-agent-orchestration-harness/tests/fixtures/invalid-adr-partial-supersession.md
- depends_on: [Task_1]
- description: |
  Plan-format: a task that would produce a record reads "propose an ADR if the admission test passes"; acceptance never enumerates a record's contents; the plan template's Decision Log entry shape gains a "record proposed" line. Prompt-snippets: an ADR review snippet asking the admission test questions plus: can a maintainer act on the Decision alone; which section is re-derivable; is implementation wording mirrored; is any wording time-relative; is more than one decision present. Reviewer packet: an "ADRs proposed" field. Lifecycle-gates Escalation Ruling: point at the admission test and state that the acceptance ask is separate from the ruling. Final-response contract: an "ADRs proposed, with acceptance state" line. Validator: fail when a live record under `decisions/` (not `superseded/`) carries `supersession_scope: partial`, with a fixture that exercises the failure.
- acceptance:
  - Each routing surface names `durable-docs-authoring/references/adr.md` by path once and carries only its operational form (question list, field, or gate line) with no rationale; the rules themselves are not restated.
  - The validator check fires on the fixture and passes on the live set.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py && python scripts/run_validation_smoke_tests.py; from repository root: git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "Confirm routing lines point, not restate; confirm the reviewer snippet asks the listed questions and nothing structural-only."

### Task_3: Promote the lesson into a rule
- type: docs
- owns:
  - docs/coding-agent/rules/orchestrator.md
  - docs/coding-agent/lessons.md
- depends_on: [Task_1]
- description: |
  Orchestrator-authored (single writer for rules). Replace the preliminary prevention list in the lessons entry "ADRs Drifted Into Removal Ledgers Despite The Warrant Standard" with the final one, and add one orchestrator rule: a record is proposed only after the admission test in `durable-docs-authoring/references/adr.md` passes, presented for acceptance on its own, and never counted as accepted by plan approval or merge. Update `last_updated`.
- acceptance:
  - The rule is one sentence, checkable, and does not restate the standard.
  - The lessons entry no longer says "preliminary".
- validation:
  - kind: command
    required: true
    owner: orchestrator
    detail: "From repository root: git diff --check"

### Task_4: Final review and closeout
- type: review
- owns: []
- depends_on: [Task_2, Task_3]
- description: |
  Whole-change review against the Definition of Done.
- acceptance:
  - Reviewer status is APPROVED.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review of the full change set vs Definition of Done; if Task_1 drafted a record, confirm its acceptance entry exists."

## Task Waves (explicit parallel dispatch sets)

Interpretation:
- Tasks listed in the same wave are intended to be dispatched in parallel by default, when `owns` are disjoint and dependencies are met.
- Waves are executed sequentially.

- Wave 1 (parallel): [Task_1]
- Wave 2 (parallel): [Task_2, Task_3]
- Wave 3 (parallel): [Task_4]

## Rollback / Safety
- One feature branch off `main` after PR #57 merges; revert by dropping the branch.
- No record lands without a recorded standalone acceptance.

## Progress Log (append-only)

Append-only editing rule (applies to both logs below): when appending an entry, anchor the edit on the previous entry and reproduce it (or anchor on the section's tail marker) so the edit inserts rather than replaces, and verify afterward that the log grew.

- 2026-09-06 23:40 Wave 1 completed: [Task_1]
  - Summary: adr.md rewritten around the admission test, form, lifecycle (proposed, accepted, superseded; immutable at merge with the confirmed pointer-repair and typo exception), and standalone acceptance; template, readme, and skill trigger aligned; the standard change itself failed the admission test and its draft record was withdrawn.
  - Validation evidence: validate_harness_package.py pass; git diff --check clean; grep for warrant in the skill returns nothing; Codex Reviewer APPROVED after one delta round, with the exception ruling confirmed by the user.
  - Notes: no record lands from this plan.
- 2026-09-07 11:15 Wave 2 completed: [Task_2, Task_3]
  - Summary: Task_2 (Codex worker) routed plan-format, prompt-snippets, the reviewer packet, the Escalation Ruling reference, and the final-response contract to adr.md by path with operational forms only, and added the validator check for supersession_scope: partial on live records with its fixture; the Orchestrator added the acceptance-state item to the Final Response Summary line in orchestration-harness/SKILL.md (outside Task_2 owns, ruling recorded). Task_3 (Orchestrator): final prevention list in the lessons entry and one orchestrator rule.
  - Validation evidence: validate_harness_package.py pass; run_validation_smoke_tests.py exit 0; git diff --check clean; worker reports eight temporary-copy fixture checks with the validator firing on the partial-supersession fixture.
  - Notes: Task_4 final review dispatched.
- 2026-09-07 11:20 Wave 3 completed: [Task_4]
  - Summary: Codex Reviewer final review: DoD bullets 1-4 PASS with one MAJOR (the partial-supersession fixture was not exercised by any runnable check). Fixed in commit 1525974: run_validation_smoke_tests.py now places the fixture in a temporary live decisions directory (validator exit 3) and under superseded/ (exit 0). Delta re-review APPROVED.
  - Validation evidence: validate_harness_package.py pass; run_validation_smoke_tests.py exit 0 including the new check; git diff --check clean.
  - Notes: plan closed; PR opened for the branch.

## Decision Log (append-only; re-plans and major discoveries)

- 2026-09-06 Decision: Research waived for plan drafting.
  - Trigger / new insight: the standard's content was settled in conversation on 2026-09-06 across six rulings; nothing in the workspace needs discovery before drafting.
  - Plan delta (what changed): none.
  - Tradeoffs considered: none material.
  - User approval: pending with plan approval.
- 2026-09-06 Decision: Plan review round 1 (Codex Reviewer) findings applied.
  - Trigger / new insight: the no-duplication acceptance contradicted the template and routing deliverables; Task_1 had no scope to land a record if the admission test passed.
  - Plan delta (what changed): canonical rule plus rationale lives once in adr.md, while the template and routing surfaces carry pointers and operational forms only; Task_1 owns the single new record it may create (ADR-D-0022) and nothing else under decisions/.
  - Tradeoffs considered: none material.
  - User approval: pending with plan approval.
- 2026-09-06 Decision: Plan approved by user with the proposed answers to all open questions.
  - Trigger / new insight: user approval after reviewer approval.
  - Plan delta (what changed): status approved; execution begins after PR #57 merges.
  - Tradeoffs considered: none.
  - User approval: yes (2026-09-06).
- 2026-09-06 Decision: Record proposed under the admission test (Task_1).
  - Trigger / new insight: the standard change itself passes the admission test: it constrains how every future record is written (load-bearing); reverting to ledgers or in-place amendment is silent drift (severe); the skill text states the rules but not the failure modes that produced them (not derivable); the why is one sentence; the premises are active.
  - Plan delta (what changed): draft ADR-D-0022 "Decision records carry active decisions, one each, immutable once merged, and accepted on their own" committed on the branch as a draft; presented to ebigunso for standalone acceptance; lands only on a yes.
  - Tradeoffs considered: recording nothing would leave the four rules as skill text with no record of why the previous standard was replaced.
  - User approval: pending (standalone acceptance ask, 2026-09-06).
- 2026-09-06 Decision: ADR-D-0022 proposal withdrawn before acceptance.
  - Trigger / new insight: Task_1 review: the draft bundled three separately retirable decisions and its why repeated adr.md, so it failed the admission test it was drafted under (criterion 3 and the one-decision rule). No single decision in the standard change carries reasoning the skill text does not already state.
  - Plan delta (what changed): draft deleted; number 0022 freed; Task_1 reports the admission test as failed for the standard change.
  - Tradeoffs considered: splitting into three records would produce three whose why is re-derivable from the skill; rejected.
  - User approval: withdrawn by the Orchestrator before the user answered the acceptance ask; recorded here.
- 2026-09-06 Decision: Post-merge edit exception narrowed and surfaced.
  - Trigger / new insight: Task_1 review flagged "meaning-preserving wording edits" as an unapproved exception to immutability.
  - Plan delta (what changed): adr.md now permits after merge only pointer repairs forced by a retirement elsewhere and typo fixes that change no meaning; everything else replaces. Status lifecycle is proposed, accepted, superseded, with acceptance (the human yes) separate from immutability (the merge).
  - Tradeoffs considered: strict zero-edit immutability would make retirement pointer repair impossible.
  - User approval: yes, exception confirmed as written (2026-09-06).

## Notes
- Risks: rewriting the standard while keeping the retirement mechanics intact; the Reviewer check in Task_1 targets exactly the two failure shapes this session produced.
- Edge cases: Q2, the standard change may itself warrant a record; the plan neither presumes nor forbids it.
