# Plan: Harness Migration Backlog Format

- status: done
- generated: 2026-05-14
- last_updated: 2026-05-14
- work_type: docs

## Goal

- Define `docs/coding-agent/skill-candidates.md` and `docs/coding-agent/skill-drafts/*.md` as the canonical repo-local staging backlog for proposed harness-global migrations.

## Definition of Done

- Harness docs define the required `skill-candidates.md` format with `HMC-*` candidate entries.
- Guidance explains when a small candidate can stay inline and when a fuller draft belongs in `skill-drafts/*.md`.
- The backlog format aligns with `harness_migration_candidates` report fields.
- Rulebook and improvement-loop guidance point to the same candidate/draft format.

## Scope / Non-goals

- Scope:
  - Add or update references that describe the skill-candidates backlog and skill-drafts.
  - Wire the format into rulebook and improvement-loop routing at a concise level.
- Non-goals:
  - Do not create target-repo `docs/coding-agent/skill-candidates.md` files in this harness repo unless a template fixture already requires it.
  - Do not implement automated promotion from candidates into harness files.
  - Do not update report validation; that is covered by Report Schema Split.

## Context (workspace)

- Related files/areas:
  - `plugins/coding-agent-orchestration-harness/skills/rulebook/SKILL.md`
  - `plugins/coding-agent-orchestration-harness/skills/rulebook/references/rules-files.md`
  - `plugins/coding-agent-orchestration-harness/skills/rulebook/references/rule-suite-templates.md`
  - `plugins/coding-agent-orchestration-harness/skills/improvement-loop/SKILL.md`
  - `plugins/coding-agent-orchestration-harness/skills/improvement-loop/references/promotion-guidelines.md`
  - possible new reference: `plugins/coding-agent-orchestration-harness/skills/rulebook/references/skill-candidates-file.md`
- Existing patterns or references:
  - Rulebook references already define file shapes for rule suites.
  - Improvement-loop references already define lesson and promotion templates.
- Repo reference docs consulted:
  - `docs/coding-agent/plans/completed/rule-suite-bootstrap-lifecycle-plan.md`

## Open Questions (max 3)

- Q1: resolved. Rulebook owns the canonical backlog-file reference because it already owns `docs/coding-agent/` governance file shapes; improvement-loop links to it.

## Assumptions

- A1: Candidate IDs should use `HMC-YYYYMMDD-short-kebab-description` unless an existing candidate id is supplied.
- A2: Candidate status starts as `staged`.
- A3: Draft links are optional; large or complex candidates should use `docs/coding-agent/skill-drafts/HMC-*.md`.

## Tasks

### Task_1: Add Canonical Skill Candidates File Reference

- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/rulebook/references/skill-candidates-file.md`
- depends_on: []
- description: |
  Add a reference defining the required `docs/coding-agent/skill-candidates.md` shape and optional `skill-drafts` draft behavior.
- acceptance:
  - Reference title is `Harness Migration Candidates` or equivalent.
  - Purpose says candidates are staged cross-repository improvements, not active repo rules.
  - Required candidate fields include status, category, proposed home, generalized rule, trigger, evidence from this repo, why it generalizes, suggested change, and optional draft.
  - Template uses `HMC-YYYYMMDD-...` ids.
  - Categories align with the report contract enum.
  - Draft guidance explains when to create `docs/coding-agent/skill-drafts/*.md`.
- validation:
  - kind: review
    required: true
    owner: worker
    detail: "Compare the backlog reference fields with `harness_migration_candidates` in the report contract."

### Task_2: Wire Backlog Format Into Rulebook

- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/rulebook/SKILL.md`
  - `plugins/coding-agent-orchestration-harness/skills/rulebook/references/rules-files.md`
- depends_on: [Task_1]
- description: |
  Point rulebook users to the new backlog reference whenever cross-repo harness improvements are discovered during rule work.
- acceptance:
  - Rulebook names `docs/coding-agent/skill-candidates.md` as the canonical staging backlog.
  - Rulebook names `docs/coding-agent/skill-drafts/*.md` for larger drafts.
  - Rulebook links or routes to `references/skill-candidates-file.md`.
  - `rules-files.md` does not embed a conflicting candidate template.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "Run targeted `rg` checks for `skill-candidates-file.md`, `skill-candidates.md`, and stale `Global Migration Candidates` wording in rulebook docs."

### Task_3: Wire Backlog Format Into Improvement Loop

- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/improvement-loop/SKILL.md`
  - `plugins/coding-agent-orchestration-harness/skills/improvement-loop/references/promotion-guidelines.md`
  - `plugins/coding-agent-orchestration-harness/skills/improvement-loop/references/review-finding-triage.md`
- depends_on: [Task_1]
- description: |
  Make improvement-loop promotion guidance refer to the canonical backlog format instead of redefining it.
- acceptance:
  - Improvement-loop docs route harness migration candidates to the canonical backlog format.
  - Promotion guidelines keep concise destination guidance and link to the detailed file-shape owner.
  - Review finding triage uses the same backlog and draft paths.
  - No conflicting `HMC-*` field list exists in improvement-loop references.
- validation:
  - kind: review
    required: true
    owner: worker
    detail: "Confirm rulebook remains the detailed file-shape owner and improvement-loop remains the promotion workflow owner."

### Task_4: Add Draft Template Guidance

- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/rulebook/references/skill-candidates-file.md`
  - possible `plugins/coding-agent-orchestration-harness/skills/rulebook/references/skill-draft-template.md`
- depends_on: [Task_1]
- description: |
  Provide a concise fuller-draft structure for candidates that are too large for the backlog entry.
- acceptance:
  - Draft guidance includes problem, generalized rule, trigger, proposed owner/home, examples, validation idea, and open questions.
  - Draft guidance says drafts are proposals for future harness-maintenance PRs/issues, not active runtime instructions.
  - If a separate draft template file is added, it is linked from the canonical backlog reference.
- validation:
  - kind: review
    required: true
    owner: worker
    detail: "Review draft guidance for clear separation from active repo rules."

### Task_5: Final Backlog Format Review

- type: review
- owns: []
- depends_on: [Task_1, Task_2, Task_3, Task_4]
- description: |
  Confirm the migration backlog format is canonical, discoverable, and aligned with the report contract and promotion model.
- acceptance:
  - The hand-off document's suggested `skill-candidates.md` shape is covered.
  - Backlog docs distinguish staged proposals from active repo rules.
  - Rulebook and improvement-loop references do not diverge.
  - Existing package validation passes.
- validation:
  - kind: command
    required: true
    owner: reviewer
    detail: "Run `python plugins/coding-agent-orchestration-harness/scripts/validate_harness_package.py` or review equivalent Worker evidence."
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review against this plan and hand-off coverage."

## Task Waves (explicit parallel dispatch sets)

- Wave 1 (parallel): [Task_1]
- Wave 2 (parallel): [Task_2, Task_3, Task_4]
- Wave 3 (parallel): [Task_5]

## E2E / Visual Validation Spec

- Not applicable. This plan changes documentation and templates only.

## Rollback / Safety

- Revert the new backlog reference and any links to it together.
- If Report Schema Split has landed, retain the `harness_migration_candidates` report field even if backlog docs need rework.

## Progress Log (append-only)

- 2026-05-14 Plan drafted.
  - Summary: Added implementation plan for canonical `skill-candidates.md` and `skill-drafts` migration backlog format.
  - Validation evidence: Plan-format self-check.
  - Notes: Awaiting approval before execution.
- 2026-05-14 Waves 1-2 completed: [Task_1, Task_2, Task_3, Task_4]
  - Summary: Added canonical `skill-candidates.md` and skill-draft references, then linked them from rulebook and improvement-loop promotion guidance.
  - Validation evidence: Targeted `rg` confirmed `skill-candidates-file.md`, `skill-candidates.md`, and `skill-drafts` links are present.
  - Notes: The reference defines `HMC-*` ids, categories, backlog fields, and draft structure.
- 2026-05-14 Wave 3 completed: [Task_5]
  - Summary: Strict backlog format review completed by Orchestrator.
  - Validation evidence: `python plugins\coding-agent-orchestration-harness\scripts\validate_harness_package.py` passed; `git diff --check` passed.
  - Notes: Reviewer subagent was not used in this desktop session; review was performed directly against the plan acceptance criteria.

## Decision Log (append-only; re-plans and major discoveries)

- 2026-05-14 Decision: Rulebook owns the detailed backlog file-shape reference.
  - Trigger / new insight: Rulebook already owns repo governance file structures.
  - Plan delta (what changed): Improvement-loop links to the rulebook reference instead of owning a duplicate template.
  - Tradeoffs considered: Improvement-loop is closer to corrections, but duplicate file-shape templates would drift.
  - User approval: yes.

## Notes

- Risks:
  - Backlog docs could duplicate report contract fields too aggressively; keep one canonical description and cross-check it.
  - If a new reference is added, package validator may need to tolerate it without extra manifest changes.
- Edge cases:
  - A small candidate can have no draft; use an empty or omitted draft field according to the final documented format.
