# Plan: Rulebook Rule-File Cleanup

- status: done
- generated: 2026-05-14
- last_updated: 2026-05-14
- work_type: docs

## Goal

- Make `docs/coding-agent/rules/*.md` live repository operating rules only, and route cross-repo harness ideas to harness migration staging instead of role rule files.

## Definition of Done

- Rulebook guidance says repo rule files are repo-specific source of truth, not global staging areas.
- `rules-files.md` no longer requires or routes `Global Migration Candidates`.
- `rule-suite-templates.md` removes `Global Migration Candidates` from role rule templates.
- Worker and Reviewer templates retain repo-local `Mechanical Gate Candidates` where appropriate.
- Reviewer template includes durable review category guidance from the hand-off document.

## Scope / Non-goals

- Scope:
  - Update rulebook core guidance, rule file reference, and rule suite templates.
  - Define routing from repo-local report candidates into role rule files.
- Non-goals:
  - Do not modify the Worker report schema or validator; that is covered by Report Schema Split.
  - Do not define the full `skill-candidates.md` file format; that is covered by Harness Migration Backlog Format.
  - Do not refresh any target repo rule suites in this plan.

## Context (workspace)

- Related files/areas:
  - `plugins/coding-agent-orchestration-harness/skills/rulebook/SKILL.md`
  - `plugins/coding-agent-orchestration-harness/skills/rulebook/references/rules-files.md`
  - `plugins/coding-agent-orchestration-harness/skills/rulebook/references/rule-suite-templates.md`
- Existing patterns or references:
  - Rulebook already owns rule bootstrap, repair, migration, and refresh guidance.
  - Existing templates define the required role rule file sections.
- Repo reference docs consulted:
  - `docs/coding-agent/plans/completed/rule-suite-bootstrap-lifecycle-plan.md`

## Open Questions (max 3)

- Q1: resolved. Existing target repos with `Global Migration Candidates` sections should not be migrated automatically by this harness update; they should migrate during a targeted rule refresh.

## Assumptions

- A1: `Mechanical Gate Candidates` remain repo-local and can stay in `worker.md` and `reviewer.md`.
- A2: `common.md`, `worker.md`, `orchestrator.md`, and `reviewer.md` templates should include only active repo behavior and repo-local candidates.
- A3: Cross-repo ideas are staged through `harness_migration_candidates` reports and `docs/coding-agent/skill-candidates.md`.

## Tasks

### Task_1: Update Rulebook Ownership Language

- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/rulebook/SKILL.md`
- depends_on: []
- description: |
  Replace language that treats rule files as global staging areas with language that makes them repo-specific operating rules.
- acceptance:
  - Rulebook describes `docs/coding-agent/rules/*.md` as repo-specific constraints and operating rules.
  - Cross-repo harness improvements are routed to `docs/coding-agent/skill-candidates.md` and `docs/coding-agent/skill-drafts/*.md`.
  - Guidance does not instruct ordinary runtime agents to edit bundled harness skills or references.
  - Existing rulebook ownership of rule files remains clear.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "Run targeted `rg` checks in rulebook SKILL.md for stale phrases implying rule files are a global staging area."
  - kind: review
    required: true
    owner: worker
    detail: "Confirm rulebook still owns repo rule bootstrap, repair, migration, and refresh."

### Task_2: Rewrite Rule Candidate Routing In Rules Reference

- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/rulebook/references/rules-files.md`
- depends_on: [Task_1]
- description: |
  Remove audience-plus-intended-home routing and document that `rule_candidates` are always repo-specific.
- acceptance:
  - `rules-files.md` routes `rule_candidates` by `audience` only.
  - `rules-files.md` says harness-global ideas must arrive as `harness_migration_candidates` or lesson candidates with `promotion_target: harness_migration`.
  - Required sections for role rule files do not include `Global Migration Candidates`.
  - The reference describes `skill-candidates.md` only as a staging backlog, not an active repo rule file.
  - The file contains no `global_candidate` or `intended_home`.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "Run `rg \"intended_home|global_candidate|Global Migration Candidates\" plugins/coding-agent-orchestration-harness/skills/rulebook/references/rules-files.md` and verify no stale routing remains."

### Task_3: Update Rule Suite Templates

- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/rulebook/references/rule-suite-templates.md`
- depends_on: [Task_2]
- description: |
  Remove global migration sections from role rule templates and add the requested durable Reviewer category guidance.
- acceptance:
  - `common.md` template sections are limited to repository references, validation commands, safety/boundaries, and naming/structure.
  - `worker.md` template includes repo-specific worker notes, CI/checks mapping, and `Mechanical Gate Candidates`.
  - `orchestrator.md` template includes repo-specific orchestrator policies, integration/git policy, and rule suite refresh notes.
  - `reviewer.md` template includes repo-specific reviewer notes, risk hotspots, required evidence, heuristics, recurring misses/prevention, and `Mechanical Gate Candidates`.
  - Reviewer template includes durable review categories listed in the hand-off document.
  - No role template includes `Global Migration Candidates`.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "Run targeted `rg` checks in rule-suite-templates.md for removed section `Global Migration Candidates`."
  - kind: review
    required: true
    owner: reviewer
    detail: "Review section changes for compatibility with existing rule bootstrap and refresh behavior."

### Task_4: Final Rulebook Consistency Review

- type: review
- owns: []
- depends_on: [Task_1, Task_2, Task_3]
- description: |
  Confirm the rulebook now cleanly separates active repo rules from harness migration staging.
- acceptance:
  - Rulebook core guidance, rules reference, and templates use the same routing model.
  - The role rule file shape matches the hand-off document.
  - Mechanical gate candidates remain explicitly repo-local.
  - No cross-repo migration backlog is placed inside role rule files.
- validation:
  - kind: command
    required: true
    owner: reviewer
    detail: "Run `python plugins/coding-agent-orchestration-harness/scripts/validate_harness_package.py` or review equivalent Worker evidence."
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review against this plan and the hand-off document."

## Task Waves (explicit parallel dispatch sets)

- Wave 1 (parallel): [Task_1]
- Wave 2 (parallel): [Task_2]
- Wave 3 (parallel): [Task_3]
- Wave 4 (parallel): [Task_4]

## E2E / Visual Validation Spec

- Not applicable. This plan changes harness rulebook documentation only.

## Rollback / Safety

- Revert rulebook documentation changes as a set.
- Do not execute this plan partially after Report Schema Split, because stale `intended_home` routing would conflict with the new report contract.

## Progress Log (append-only)

- 2026-05-14 Plan drafted.
  - Summary: Added implementation plan for removing global migration sections from repo rule files and rulebook routing.
  - Validation evidence: Plan-format self-check.
  - Notes: Awaiting approval before execution.
- 2026-05-14 Waves 1-3 completed: [Task_1, Task_2, Task_3]
  - Summary: Updated rulebook ownership language, rule candidate routing, rule templates, and stale rule-writing migration wording.
  - Validation evidence: `rg "intended_home|global_candidate|Global Migration Candidates" plugins\coding-agent-orchestration-harness\skills\rulebook` returned no matches after cleanup.
  - Notes: `Mechanical Gate Candidates` remains repo-local in Worker and Reviewer templates.
- 2026-05-14 Wave 4 completed: [Task_4]
  - Summary: Strict rulebook consistency review completed by Orchestrator.
  - Validation evidence: `python plugins\coding-agent-orchestration-harness\scripts\validate_harness_package.py` passed; `git diff --check` passed.
  - Notes: Reviewer subagent was not used in this desktop session; review was performed directly against the plan acceptance criteria.

## Decision Log (append-only; re-plans and major discoveries)

- 2026-05-14 Decision: Keep mechanical gate candidates in role rules.
  - Trigger / new insight: The hand-off document distinguishes repo-local mechanical gates from cross-repo harness ideas.
  - Plan delta (what changed): Worker and Reviewer templates retain mechanical gate sections.
  - Tradeoffs considered: Removing all candidate sections would lose useful repo-local validation backlog.
- 2026-05-14 Decision: Do not automatically migrate existing target repo rule files.
  - Trigger / new insight: Existing repos may contain context in old `Global Migration Candidates` sections that needs human/rule-refresh interpretation.
  - Plan delta (what changed): This plan updates harness templates and guidance only; target repo migrations are left to targeted rule refreshes.
  - Tradeoffs considered: Automatic migration is faster but risks moving context to the wrong destination.
  - User approval: yes.

## Notes

- Risks:
  - Existing lifecycle/bootstrap logic may assume old section names; implementation must search for those assumptions.
  - Package validation guards for this split are added later in the Package Validation Guards plan.
- Edge cases:
  - A repo-specific rule can be inspired by a cross-repo lesson, but once in a role rule file it must describe active behavior for that repo.
