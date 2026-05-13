# Plan: Lessons And Improvement Loop Promotion Model

- status: draft
- generated: 2026-05-14
- last_updated: 2026-05-14
- work_type: docs

## Goal

- Update the improvement loop so lessons promote to repo rules, lessons, troubleshooting notes, or staged harness migration candidates instead of direct bundled skill/reference edits during ordinary target-repo work.

## Definition of Done

- Improvement-loop guidance uses the new promotion targets.
- Promotion guidelines replace direct first-party skill/reference promotion with staged harness migration candidates.
- Entry and lessons templates expose repo rule, harness migration, dispatch/plan guardrail, troubleshooting, and residual-risk routes.
- A new tool-neutral `review-finding-triage.md` reference exists and classifies findings by durable destination.
- Ordinary runtime work is explicitly barred from editing bundled harness skills, references, agents, validators, or plugin files.

## Scope / Non-goals

- Scope:
  - Update improvement-loop skill guidance and references.
  - Add review finding triage reference.
  - Align lesson templates with the new report schema and staging model.
- Non-goals:
  - Do not change Worker report validator enums; that is covered by Report Schema Split.
  - Do not update runtime Reviewer adapters; that is covered by Runtime Agent Boundary And Adapter Updates.
  - Do not define full `skill-candidates.md` backlog format; that is covered by Harness Migration Backlog Format.

## Context (workspace)

- Related files/areas:
  - `plugins/coding-agent-orchestration-harness/skills/improvement-loop/SKILL.md`
  - `plugins/coding-agent-orchestration-harness/skills/improvement-loop/references/promotion-guidelines.md`
  - `plugins/coding-agent-orchestration-harness/skills/improvement-loop/references/entry-template.md`
  - `plugins/coding-agent-orchestration-harness/skills/improvement-loop/references/lessons-template.md`
  - `plugins/coding-agent-orchestration-harness/skills/improvement-loop/references/review-finding-triage.md`
- Existing patterns or references:
  - Improvement loop already owns post-correction workflow and lesson promotion guidance.
  - Promotion guidelines currently distinguish repo rules, first-party skill/reference updates, troubleshooting, and residual risk.
- Repo reference docs consulted:
  - `docs/coding-agent/plans/completed/integrate-latent-risk-review-routing-plan.md`

## Open Questions (max 3)

- Q1: resolved. Explicit harness-maintenance work may edit bundled harness files when the target repository is the harness repository itself or the user explicitly asks for harness-maintenance.

## Assumptions

- A1: This repository is the harness repository, but the guidance being authored is for ordinary runtime agents operating in target repositories.
- A2: "Troubleshooting notes under `docs/coding-agent/`" are repo-local unless later staged as a harness migration candidate.
- A3: Tool-neutral triage must name sources such as human reviewer, Copilot, CI, Reviewer, and other sources only as examples, not categories.

## Tasks

### Task_1: Update Improvement Loop Runtime Boundary And Promotion Targets

- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/improvement-loop/SKILL.md`
- depends_on: []
- description: |
  Replace direct first-party skill/reference promotion with the staged migration model and add the hard runtime boundary.
- acceptance:
  - Promotion targets are repo rules, repo lessons, harness migration candidates, harness migration drafts, and troubleshooting notes under `docs/coding-agent/`.
  - Ordinary target-repository work explicitly must not edit bundled/global harness skills, references, agents, validators, or plugin files.
  - The only exception is explicit harness-maintenance work where the target repo is the harness repository itself.
  - Any remaining direct first-party skill/reference update language is scoped only to explicit harness-maintenance work.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "Run targeted `rg` checks in improvement-loop/SKILL.md for stale direct-promotion phrases."
  - kind: review
    required: true
    owner: worker
    detail: "Confirm boundary wording does not block explicit harness-maintenance tasks."

### Task_2: Rewrite Promotion Guidelines

- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/improvement-loop/references/promotion-guidelines.md`
- depends_on: [Task_1]
- description: |
  Replace "Promote to first-party skill or reference" with "Stage as a harness migration candidate".
- acceptance:
  - Guidelines define when to stage a harness migration candidate.
  - Destination is `docs/coding-agent/skill-candidates.md` and optional `docs/coding-agent/skill-drafts/*.md`.
  - Direct bundled harness edits are allowed only during explicit harness-maintenance.
  - Guidelines preserve repo-rule, troubleshooting, and residual-risk routes.
  - The phrase "harness migration candidate" is present and central.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "Run `rg \"first-party skill|first-party reference|global-skill|references/\\*\" plugins/coding-agent-orchestration-harness/skills/improvement-loop/references/promotion-guidelines.md` and verify no stale direct-promotion target remains."

### Task_3: Update Lesson Entry Templates

- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/improvement-loop/references/entry-template.md`
  - `plugins/coding-agent-orchestration-harness/skills/improvement-loop/references/lessons-template.md`
- depends_on: [Task_2]
- description: |
  Update templates so future lessons ask for repo rule candidates, harness migration candidates, dispatch/plan guardrails, troubleshooting, and residual risk.
- acceptance:
  - Entry template lists rule audience as `common|worker|orchestrator|reviewer`.
  - Entry template includes a harness migration candidate block with `category`, `proposed_home`, `generalized_rule`, and `suggested_change`.
  - Entry template removes "First-party skill/reference update".
  - Lessons template says lessons promote into repo rules, harness migration candidates, troubleshooting notes, or residual risk records.
  - Templates align with the new lesson promotion target enum.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "Run targeted `rg` checks in improvement-loop references for `First-party skill/reference update`, `global-skill`, and `references/*`."

### Task_4: Add Tool-Neutral Review Finding Triage Reference

- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/improvement-loop/references/review-finding-triage.md`
- depends_on: [Task_2]
- description: |
  Add a source-neutral triage reference for findings from human reviewers, Copilot, CI, Reviewer, or other sources.
- acceptance:
  - Reference classifies findings by durable destination, not by source.
  - Destinations include repo-specific review behavior, repo-specific executable validation, proposed mechanical gate, cross-repo harness improvement, dispatch/packet issue, and accepted residual risk.
  - Destination paths match the hand-off document.
  - Guidance names `docs/coding-agent/rules/reviewer.md`, `docs/coding-agent/rules/worker.md`, `docs/coding-agent/skill-candidates.md`, `docs/coding-agent/skill-drafts/*.md`, and `docs/coding-agent/lessons.md`.
  - No Copilot-specific bucket is introduced.
- validation:
  - kind: review
    required: true
    owner: worker
    detail: "Review triage reference for tool-neutral language and destination clarity."

### Task_5: Wire New Reference Into Improvement Loop

- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/improvement-loop/SKILL.md`
  - `plugins/coding-agent-orchestration-harness/skills/improvement-loop/references/promotion-guidelines.md`
- depends_on: [Task_4]
- description: |
  Add a progressive-disclosure pointer to the new review finding triage reference where correction/review-miss handling is described.
- acceptance:
  - Improvement-loop guidance points to `review-finding-triage.md` when an external or later review finds an issue the harness should have caught.
  - The pointer remains compact and does not paste the full triage reference into `SKILL.md`.
  - Promotion guidelines and triage reference do not contradict each other.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Review improvement-loop routing for progressive-disclosure fit."

### Task_6: Final Improvement Loop Consistency Review

- type: review
- owns: []
- depends_on: [Task_1, Task_2, Task_3, Task_4, Task_5]
- description: |
  Confirm the improvement-loop documents consistently route ordinary runtime learning into repo-local files or staged harness migration candidates.
- acceptance:
  - No stale ordinary-runtime direct bundled edit instruction remains.
  - New promotion targets align with Report Schema Split.
  - Review finding triage is source-neutral.
  - Templates give future agents enough structure to record both repo-local and cross-repo lessons.
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
- Wave 2 (parallel): [Task_2]
- Wave 3 (parallel): [Task_3, Task_4]
- Wave 4 (parallel): [Task_5]
- Wave 5 (parallel): [Task_6]

## E2E / Visual Validation Spec

- Not applicable. This plan changes documentation and templates only.

## Rollback / Safety

- Revert improvement-loop SKILL and reference changes together.
- If Report Schema Split has already landed, do not restore old lesson promotion target names.

## Progress Log (append-only)

- 2026-05-14 Plan drafted.
  - Summary: Added implementation plan for updating lesson promotion and improvement-loop triage to staged harness migration candidates.
  - Validation evidence: Plan-format self-check.
  - Notes: Awaiting approval before execution.

## Decision Log (append-only; re-plans and major discoveries)

- 2026-05-14 Decision: Keep direct bundled edits available only for explicit harness-maintenance.
  - Trigger / new insight: The hand-off document asks runtime agents to stage cross-repo improvements rather than modify bundled harness content.
  - Plan delta (what changed): Runtime boundary is included in improvement-loop guidance and promotion guidelines.
  - Tradeoffs considered: Fully banning bundled edits would prevent this repository's own maintenance workflow.
  - User approval: yes.

## Notes

- Risks:
  - Wording must distinguish "ordinary target-repository work" from "this harness repo is the explicit target".
  - Package validation guards for stale direct-promotion wording are added in the final guard plan.
- Edge cases:
  - A finding can produce both a repo rule and a harness migration candidate when the repo needs immediate behavior and the harness should learn later.
