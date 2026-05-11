# Plan: Integrate Latent-Risk Review Routing

- status: done
- generated: 2026-05-11
- last_updated: 2026-05-11
- work_type: docs

## Goal

- Integrate latent-risk review criteria into the harness review mechanism through progressive-disclosure plugin skills and references, without expanding Reviewer agent prompts with the full checklist.

## Definition of Done

- `engineering-quality-baselines` owns the latent-risk review router and conditional criteria references.
- Reviewer runtime adapters route reviewers to the plugin skill, not to repo-relative paths in the target project.
- Orchestrator dispatch guidance and Reviewer packet templates can pass applicable latent-risk hints without sending a wall of irrelevant checklist items.
- Review rubric makes applicable latent-risk failures blocking unless waived or recorded as accepted residual risk.
- Review confirms shared criteria are not duplicated across runtime adapter bodies and existing package validation remains valid.

## Scope / Non-goals

- Scope:
  - Add latent-risk review references under `plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/`.
  - Update `engineering-quality-baselines` routing and review rubric.
  - Add compact plugin-skill routing hooks to Reviewer adapters for Copilot, Claude, and Codex.
  - Update Orchestrator-facing Reviewer packet, dispatch checklist, and prompt snippets to carry applicable routing hints.
  - Run existing package/static validation; add new validation only for manifest/bootstrap/package-structure requirements, not for skill prose internals.
- Non-goals:
  - Do not create a new skill unless implementation discovers `engineering-quality-baselines` cannot cleanly own this behavior.
  - Do not paste the full latent-risk checklist into runtime agent files.
  - Do not rename runtime agents or alter runtime role identities.
  - Do not change Reviewer role authority; Reviewer remains review-only.
  - Do not require runtime agents to resolve plugin source paths relative to the target project working directory.

## Context (workspace)

- Related files/areas:
  - `plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/SKILL.md`
  - `plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/review-rubric.md`
  - `plugins/coding-agent-orchestration-harness/agents/Reviewer.md`
  - `plugins/coding-agent-orchestration-harness/claude/agents/harness-reviewer.md`
  - `plugins/coding-agent-orchestration-harness/codex/agent-templates/harness_reviewer.toml`
  - `plugins/coding-agent-orchestration-harness/skills/wave-integration/references/reviewer-packet-template.md`
  - `plugins/coding-agent-orchestration-harness/skills/subagent-strategy/references/dispatch-checklists.md`
  - `plugins/coding-agent-orchestration-harness/skills/subagent-strategy/references/prompt-snippets.md`
  - `plugins/coding-agent-orchestration-harness/skills/runtime-adapter-contract/references/prompt-budgeting.md`
  - `plugins/coding-agent-orchestration-harness/scripts/validate_harness_package.py`
- Existing patterns or references:
  - `engineering-quality-baselines` already uses risk triage and progressive-disclosure references.
  - `skills-maintenance` says `SKILL.md` should keep routing/core rules while procedures and checklists live in `references/*`.
  - `runtime-adapter-contract` says shared semantics live in shared skills/references, while runtime adapters stay short and mechanics-specific.
  - `wave-integration` owns the Reviewer packet shape.
  - `subagent-strategy` owns dispatch checklists and prompt snippets.
- Repo reference docs consulted:
  - `docs/coding-agent/rules/common.md`
  - `docs/coding-agent/rules/orchestrator.md`
  - `docs/coding-agent/lessons.md`

## Open Questions (max 3)

- Q1: resolved. Do not add strict validators for skill/reference internals; keep prose and prompt-bloat checks in human/Reviewer review unless a package-structure issue is discovered.
- Q2: resolved. Do not add a permanent `Latent-Risk Findings` output section; report applicable latent-risk issues under the existing review findings and recommendations.

## Assumptions

- A1: `engineering-quality-baselines` is the correct owner because latent-risk review is a quality/review-depth concern, not a new subagent role.
- A2: Runtime agents should be instructed to use the plugin skill, not target-project-relative paths, because agents run in their own project directories after taking the plugin.
- A3: Orchestrator-prepared packets may name plugin skill/reference files as routing hints when the context is explicitly plugin-owned.
- A4: The latent-risk files should be durable and version-agnostic.

## Tasks

### Task_1: Verify Current Review Integration Surface

- type: research
- owns: []
- depends_on: []
- description: |
  Confirm the exact current Review workflow, runtime adapter wording, packet template, dispatch checklist, prompt snippet shape, and package validation behavior before editing.
- acceptance:
  - Exact insertion points are identified for `engineering-quality-baselines`, review rubric, Reviewer adapters, packet template, dispatch checklist, and prompt snippets.
  - Research confirms whether package validation needs updates for manifest, bootstrap, or package-structure reasons only.
  - Research explicitly notes any runtime-specific constraints for Copilot, Claude, and Codex wording.
- validation:
  - kind: review
    required: true
    owner: orchestrator
    detail: "Verify Researcher returned concise findings with file paths, relevant existing sections, and implementation cautions; no file edits."

### Task_2: Add Latent-Risk Reference Tree

- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/review-latent-risk.md`
  - `plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/review-latent-risk-state.md`
  - `plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/review-latent-risk-failure.md`
  - `plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/review-latent-risk-contract-scope.md`
  - `plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/review-latent-risk-performance.md`
  - `plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/review-latent-risk-future-surface.md`
  - `plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/review-latent-risk-validation-tests.md`
- depends_on: [Task_1]
- description: |
  Add a short latent-risk router plus conditional reference files. Keep the router compact and make each deeper file self-contained with clear "read when" triggers and output expectations.
- acceptance:
  - Router asks the core latent-risk question and lists the short first-pass risk shapes.
  - Router points reviewers to conditional references only when triggers match the changed code.
  - Conditional files cover state/invariants, failure/degradation, contract/scope, performance, future surface, and validation/tests.
  - Reporting guidance requires applicable criteria only and blocks approval on unwaived applicable FAIL items.
  - Files avoid target-project-relative runtime assumptions and version/rollout language.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "Search new latent-risk references for version/rollout wording and for accidental instructions to paste full checklists into runtime agents."
  - kind: review
    required: true
    owner: worker
    detail: "Review that each conditional file is independently useful and not required for unrelated reviews."

### Task_3: Wire Latent-Risk Routing Into Engineering Quality Baselines

- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/SKILL.md`
  - `plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/review-rubric.md`
- depends_on: [Task_2]
- description: |
  Add the minimal always-on routing pointer to the skill and a compact companion check to the review rubric.
- acceptance:
  - `SKILL.md` adds a single progressive-disclosure entry for latent-risk review routing.
  - `SKILL.md` does not list every conditional latent-risk subfile.
  - `review-rubric.md` adds a small companion check that points to the router through the skill/reference structure.
  - Review rubric states applicable latent-risk FAIL blocks approval unless waived or recorded as accepted residual risk.
- validation:
  - kind: review
    required: true
    owner: worker
    detail: "Confirm `SKILL.md` remains lean and the full checklist lives only in references."

### Task_4: Update Reviewer Runtime Adapters With Plugin-Skill Routing

- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/agents/Reviewer.md`
  - `plugins/coding-agent-orchestration-harness/claude/agents/harness-reviewer.md`
  - `plugins/coding-agent-orchestration-harness/codex/agent-templates/harness_reviewer.toml`
- depends_on: [Task_3]
- description: |
  Add compact latent-risk routing hooks to Reviewer adapters. Word runtime instructions as plugin-skill routing, not target-project path routing.
- acceptance:
  - Copilot Reviewer receives a short trigger to use the plugin's `engineering-quality-baselines` latent-risk routing when change shape warrants it.
  - Claude Reviewer remains especially short and reference-driven.
  - Codex Reviewer TOML uses plugin-skill phrasing and does not assume the target project contains plugin source paths.
  - No runtime adapter contains the full latent-risk checklist or conditional reference content.
  - Existing review-only boundaries and validation evidence rules remain unchanged.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "Search Reviewer adapters for duplicated latent-risk checklist phrases and for target-project-relative references to new latent-risk files."
  - kind: review
    required: true
    owner: worker
    detail: "Check adapter wording against runtime-adapter-contract prompt budgeting guidance."

### Task_5: Update Orchestrator Dispatch And Reviewer Packet Guidance

- type: docs
- owns:
  - `plugins/coding-agent-orchestration-harness/skills/wave-integration/references/reviewer-packet-template.md`
  - `plugins/coding-agent-orchestration-harness/skills/subagent-strategy/references/dispatch-checklists.md`
  - `plugins/coding-agent-orchestration-harness/skills/subagent-strategy/references/prompt-snippets.md`
- depends_on: [Task_2]
- description: |
  Give Orchestrator-facing guidance for sending only applicable latent-risk routing hints to Reviewer.
- acceptance:
  - Reviewer packet template replaces generic risk-area ambiguity with optional latent-risk routing hints.
  - Packet guidance says to omit irrelevant categories rather than sending `N/A` lists.
  - Dispatch checklist adds optional latent-risk routing hints with category, plugin skill/reference, and one-sentence reason.
  - Prompt snippets add a concise latent-risk Reviewer snippet that uses plugin-skill routing and forbids printing irrelevant checklist items.
  - Guidance preserves single-scope prompt-snippet style.
- validation:
  - kind: review
    required: true
    owner: worker
    detail: "Confirm Orchestrator guidance helps route review depth without duplicating criteria."

### Task_6: Run Existing Package Validation And Avoid Overfitting Validators

- type: test
- owns:
  - `plugins/coding-agent-orchestration-harness/scripts/validate_harness_package.py`
  - `plugins/coding-agent-orchestration-harness/scripts/run_validation_smoke_tests.py`
- depends_on: [Task_4, Task_5]
- description: |
  Run existing package validation and update validators only if implementation discovers a manifest, bootstrap, path, or package-structure requirement. Do not validate the inner workings of skill prose or conditional criteria, because that makes skill content harder to evolve.
- acceptance:
  - Existing package validation passes after the documentation and adapter changes.
  - No new validator is added for latent-risk reference content, checklist phrasing, or adapter prose duplication.
  - Validator changes are made only if needed for manifest, bootstrap, path, or package-structure correctness.
  - If validator files are unchanged, record the reason in the plan progress log and rely on Task_7 for prompt-bloat/prose review.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "Run `python plugins/coding-agent-orchestration-harness/scripts/validate_harness_package.py`."
  - kind: command
    required: false
    owner: worker
    detail: "Run `python plugins/coding-agent-orchestration-harness/scripts/run_validation_smoke_tests.py` only if validator or smoke-test files change."

### Task_7: Final Governance And Review Gate

- type: review
- owns: []
- depends_on: [Task_3, Task_4, Task_5, Task_6]
- description: |
  Review the full diff for skill-maintenance fit, runtime-adapter fit, internal consistency, and validation evidence.
- acceptance:
  - Reviewer confirms the criteria are integrated through plugin skills/references and not copied into runtime adapters.
  - Reviewer confirms `engineering-quality-baselines` remains the correct owner and no new skill is needed.
  - Reviewer confirms runtime adapter wording works for agents operating in target project directories after taking the plugin.
  - Reviewer confirms validation evidence is present or explicitly waived.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Review final diff against this plan, skills-maintenance guidance, runtime-adapter-contract guidance, and validation evidence."

## Task Waves (explicit parallel dispatch sets)

Interpretation:
- Tasks listed in the same wave are intended to be dispatched in parallel by default,
  when `owns` are disjoint and dependencies are met.
- Waves are executed sequentially.

- Wave 1 (parallel): [Task_1]
- Wave 2 (parallel): [Task_2]
- Wave 3 (parallel): [Task_3, Task_5]
- Wave 4 (parallel): [Task_4]
- Wave 5 (parallel): [Task_6]
- Wave 6 (parallel): [Task_7]

## E2E / Visual Validation Spec

- Not applicable. This plan changes harness documentation, skill references, runtime adapter text, and existing package validation only if needed for structure.

## Rollback / Safety

- Revert the latent-risk reference files and remove routing hooks from `engineering-quality-baselines`, Reviewer adapters, Reviewer packet guidance, dispatch checklist, and prompt snippets.
- If validator changes are made for package-structure reasons, revert them with the related smoke-test updates.
- Because this is documentation and static validation work, rollback should not require migration steps.

## Progress Log (append-only)

- 2026-05-11 Plan drafted.
  - Summary: Added draft plan for progressive-disclosure latent-risk review routing.
  - Validation evidence: Manual plan-format check; no implementation executed.
  - Notes: Awaiting user approval before implementation.
- 2026-05-11 Wave 1 completed: [Task_1]
  - Summary: Verified existing integration surfaces for quality routing, review rubric, Reviewer adapters, packet template, dispatch checklist, prompt snippets, and package validation.
  - Validation evidence: Manual file inspection and targeted `rg` checks.
  - Notes: No manifest/bootstrap/package-structure validator update needed.
- 2026-05-11 Wave 2 completed: [Task_2]
  - Summary: Added latent-risk router and six conditional review references under `engineering-quality-baselines/references/`.
  - Validation evidence: Targeted `rg` check for rollout/version/prompt-bloat wording; hits were expected semantic wording only.
  - Notes: Criteria live in references, not runtime adapters.
- 2026-05-11 Wave 3 completed: [Task_3, Task_5]
  - Summary: Wired latent-risk routing into `engineering-quality-baselines`, review rubric, Reviewer packet guidance, dispatch checklist, and prompt snippets.
  - Validation evidence: Manual review of SKILL.md lean routing and Orchestrator-facing prompt guidance.
  - Notes: Packet guidance says to omit irrelevant categories.
- 2026-05-11 Wave 4 completed: [Task_4]
  - Summary: Added compact plugin-skill routing hooks to Copilot, Claude, and Codex Reviewer adapters.
  - Validation evidence: `rg` confirmed no conditional latent-risk reference paths or distinctive checklist headings were copied into adapters; `rg` confirmed no target-project path routing wording was introduced.
  - Notes: Claude hook remains shorter than Copilot/Codex wording.
- 2026-05-11 Wave 5 completed: [Task_6]
  - Summary: Ran existing package validation; no validator changes were made because there was no manifest, bootstrap, path, or package-structure change.
  - Validation evidence: `python plugins/coding-agent-orchestration-harness/scripts/validate_harness_package.py` passed; plan validation also passed.
  - Notes: Smoke tests were skipped because validator and smoke-test files were unchanged.
- 2026-05-11 Wave 6 completed: [Task_7]
  - Summary: Final governance review completed by Orchestrator due runtime subagent restrictions in this session.
  - Validation evidence: `git diff --check` passed; conflict-marker search returned no matches; targeted searches confirmed runtime adapters did not copy conditional checklist headings or target-project path routing.
  - Notes: Reviewer approval was not collected from a separate subagent in this session.

## Decision Log (append-only; re-plans and major discoveries)

- 2026-05-11 Decision: Use `engineering-quality-baselines` as the owning skill.
  - Trigger / new insight: Latent-risk criteria are review-depth and quality-gate concerns.
  - Plan delta (what changed): No new skill proposed by default.
  - Tradeoffs considered: New dedicated skill would increase routing surface and overlap with existing quality baseline ownership.
  - User approval: pending.
- 2026-05-11 Decision: Runtime adapters route through plugin skills, not target-project-relative paths.
  - Trigger / new insight: Runtime agents take the plugin and work inside their own project directories.
  - Plan delta (what changed): Adapter task acceptance requires plugin-skill wording.
  - Tradeoffs considered: Direct file paths remain useful inside plugin references and Orchestrator packets when plugin context is explicit.
  - User approval: pending.
- 2026-05-11 Decision: Do not strictly validate skill internals.
  - Trigger / new insight: Strict validators for each skill's internal prose make skill evolution harder.
  - Plan delta (what changed): Task_6 now runs existing package validation and only updates validators for manifest/bootstrap/path/package-structure needs.
  - Tradeoffs considered: Human/Reviewer review is better suited for prompt-bloat and prose-quality checks than brittle static validators.
  - User approval: yes.
- 2026-05-11 Decision: Keep latent-risk reporting in existing review sections.
  - Trigger / new insight: A permanent latent-risk output section would invite empty boilerplate.
  - Plan delta (what changed): Q2 resolved in favor of reporting applicable latent-risk issues under existing `Issues Found` and `Recommendations`.
  - Tradeoffs considered: Optional issue-shape guidance preserves evidence quality without growing every review report.
  - User approval: inferred from prior discussion; no separate output-section request was made.

## Notes

- Risks:
  - Adapter prompts could drift into duplicating the new checklist unless validation catches bloat.
  - Review output could become noisy if packet guidance does not clearly say to omit irrelevant categories.
  - Codex template wording must not assume plugin source paths exist in the target project.
- Edge cases:
  - Reviews with multiple risk categories should load only matching conditional references.
  - A severe latent-risk FAIL with missing test coverage should block approval unless explicitly waived or recorded as accepted residual risk.
