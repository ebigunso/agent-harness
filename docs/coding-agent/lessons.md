# Lessons Log (Coding Agent)

Purpose:
- capture recurring mistakes and the prevention mechanism
- enable "read once, don't repeat" improvements

## How to use
- Append a new entry after any user correction or significant miss.
- Keep entries short and actionable.
- Promote repeated/high-severity lessons into repo rules, first-party skills/references, or troubleshooting knowledge.

## Tags
- planning
- validation
- delegation
- review
- tooling
- scope-owns
- skill-maintenance

## Entries

## 2026-05-13 - Avoid Tool-Specific Catch-All Rule Sections  [tags: assumptions, review, skill-maintenance]

Context:
- Task: refine reviewer rule suite bootstrap template and bootstrapped repository reviewer rules.
- Roles involved: Orchestrator

Symptom:
- The reviewer rule template used `Copilot Finding Prevention` as a durable section heading.

Root cause:
- A design-time review source was promoted into the durable repository rule taxonomy, creating a broad tool-specific bucket that could collect unrelated memos instead of routing them to better sections.

Fix applied:
- Replaced the section with `Review Heuristics` and `Recurring Misses And Prevention`, and updated lifecycle sidecar section identifiers accordingly.

Prevention:
- Durable rule sections should describe the repository convention or review semantics, not the tool or reviewer that surfaced the issue.
- Use `Recurring Misses And Prevention` only for generalized reusable prevention rules; route mechanical checks, risk taxonomy, evidence requirements, and global candidates to their own sections.

## 2026-05-13 - Validate Exact Enum Sources, Not Broad Tokens  [tags: validation, review, tooling]

Context:
- Plan: docs/coding-agent/plans/completed/rule-suite-bootstrap-lifecycle-plan.md
- Task/Wave: Reviewer closeout for Task_10 package validation
- Roles involved: Orchestrator, Reviewer

Symptom:
- Package validation claimed to verify `rule_candidates[].audience: reviewer`, but only checked that contract files contained the broad string `reviewer`.

Root cause:
- The structural validator used substring presence as a proxy for the exact enum source, so it could pass from unrelated `reviewer` tokens such as validation owners.

Fix applied:
- Tightened `validate_harness_package.py` to inspect the exact `ALLOWED_AUDIENCE` set and the explicit schema/contract audience line.

Prevention:
- For enum or schema expansion checks, validate the exact enum source or contract field instead of broad token presence.
- Repo rule candidate:
  - audience: orchestrator
  - proposed rule: When adding package validation for enum/schema changes, check the exact enum owner or contract field rather than a broad substring.
  - scope: harness package validators and contract fixtures.

## 2026-05-13 - Use Feature Branch Naming And Escalate Nested Ref Creation  [tags: tooling, git, workflow]

Context:
- Task: create a branch for rule-suite bootstrap lifecycle work.
- Roles involved: Orchestrator

Symptom:
- Creating `codex/rule-suite-bootstrap-lifecycle` failed in the sandbox with `unable to create directory for .git/refs/heads/...`; creating `feature/2026-05-13/rule-suite-bootstrap-lifecycle` failed the same way until the Git command was rerun with approved filesystem access.

Root cause:
- The branch names were valid. The failure came from sandboxed writes to nested Git ref paths under `.git/refs/heads/`, not from a naming conflict or invalid branch format.

Fix applied:
- Verified no loose or packed `codex` ref existed, reran nested branch creation with approval, and switched to `feature/2026-05-13/rule-suite-bootstrap-lifecycle`.

Prevention:
- Prefer `feature/YYYY-MM-DD/<feature-name>` branch names in this repository unless the user requests another convention.
- When a nested branch name fails with `unable to create directory for .git/refs/heads/...`, inspect refs briefly, then rerun the Git branch/switch command with filesystem approval instead of changing naming conventions.
- Do not manually edit `.git` internals to work around nested ref creation failures.

## 2026-04-26 - Keep Skill Content Version Agnostic  [tags: skill-maintenance, assumptions]

Context:
- Plan: docs/coding-agent/plans/completed/add-review-remediation-loop-skill-plan.md
- Task/Wave: follow-up correction
- Roles involved: Orchestrator

Symptom:
- The review-remediation-loop skill embedded version-specific and test-phase phrasing.

Root cause:
- The hand-off's version labels were carried into durable skill content instead of being treated as external rollout context.

Fix applied:
- Removed version-specific and evolution-planning wording from the skill and references while preserving the bounded behavior.

Prevention:
- Repo rule candidate:
  - audience: common
  - proposed rule: Keep first-party skill content version agnostic; track rollout phase and evolution plans outside the skill unless the version is part of a public compatibility contract.
- First-party skill/reference update:
  - owner: skills-maintenance
  - target: frontmatter-and-structure guidance
  - change: Consider adding a future guardrail for separating durable skill behavior from rollout/version context.
- Dispatch/plan guardrail:
  - During final ambiguity pass, check for temporary rollout/version labels embedded in durable skill text.

Evidence:
- Search for version-specific and evolution-planning wording in the review-remediation-loop skill folder returned no matches after the fix.

## 2026-04-28 - Keep Runtime Agent Templates Out of Live Discovery Paths  [tags: planning, validation, tooling]

Context:
- Plan: docs/coding-agent/plans/active/add-codex-runtime-support-plan.md
- Task/Wave: multi-runtime plugin restructure follow-up correction
- Roles involved: Orchestrator

Symptom:
- VS Code recognized and listed Codex-style agent TOML files under the plugin repo, while other runtime adapter files did not register; fixing all runtime registrations would risk duplicate role agents appearing in the same VS Code environment.

Root cause:
- The plan placed installable Codex profiles as real `.toml` files under a live discovery-shaped `codex/agents/` path inside the plugin source tree, mixing runtime payload templates with active workspace agent discovery surfaces.

Fix applied:
- Proposed a replan: keep Codex profiles as inert bootstrap-owned templates outside active discovery paths, and materialize real `.toml` files only into a target repository's `.codex/agents/` directory during bootstrap.

Prevention:
- Before adding runtime agent files, classify each path as active-discovered, plugin-packaged, or inert template storage.
- Do not place templates in known live agent discovery paths unless the goal is for the current workspace to expose those agents immediately.
- Add validation that plugin source templates do not appear in VS Code-visible discovery paths when they are intended only for bootstrap installation.

## 2026-05-08 - Do Not Assume Copilot Agent Filename Suffix Requirements  [tags: planning, tooling, assumptions]

Context:
- Plan: multi-runtime coding-agent-orchestration-harness plugin integration
- Task/Wave: planning correction
- Roles involved: Orchestrator

Symptom:
- The integration plan proposed renaming Copilot agent files to `*.agent.md` even though the user confirmed the current names remain discoverable.

Root cause:
- The plan treated the hand-off filename convention as a discovery requirement instead of checking it against the current tested local behavior.

Fix applied:
- Keep the current Copilot agent filenames and remove the rename task from the implementation plan.

Prevention:
- When adapting hand-off documents, distinguish normative requirements from examples or stale assumptions.
- Preserve locally verified runtime behavior unless a change is required by acceptance criteria or new validation evidence.

## 2026-05-09 - Avoid Compatibility Wrappers Without Clear Need  [tags: planning, scope-owns, skill-maintenance]

Context:
- Plan: docs/coding-agent/plans/completed/add-codex-runtime-support-plan.md
- Task/Wave: post-implementation correction
- Roles involved: Orchestrator

Symptom:
- The bootstrap update kept `install_codex_agents.py` as a compatibility wrapper even though the canonical `install_codex_harness.py` entrypoint was sufficient.

Root cause:
- The plan preserved backward compatibility by default without confirming there was an actual supported external contract for the older script name.

Fix applied:
- Removed the extra wrapper and updated docs/plan references to use only the canonical script.

Prevention:
- Before adding or retaining compatibility shims, verify a concrete compatibility requirement exists. If not, prefer one canonical entrypoint and document it clearly.

## 2026-05-09 - Keep Maintainer Rationale Out Of Runtime Skill Instructions  [tags: skill-maintenance, assumptions, documentation]

Context:
- File: plugins/coding-agent-orchestration-harness/skills/orchestration-harness/SKILL.md
- Task/Wave: post-implementation correction
- Roles involved: Orchestrator

Symptom:
- A source-of-truth section added to `SKILL.md` read like implementation/maintenance rationale rather than runtime instructions an agent should follow when invoking the skill.

Root cause:
- The change mixed architectural documentation with always-on agent operating policy.

Fix applied:
- Proposed moving the design rationale into ADR-style documentation and keeping only concise runtime-relevant routing/precedence language in `SKILL.md`.

Prevention:
- For first-party skills, keep `SKILL.md` limited to trigger/scope boundaries, core runtime rules, and progressive-disclosure pointers. Put design rationale, history, and maintenance decisions in ADRs or maintainer references.

## 2026-05-09 - Keep ADR Metadata And Language Durable  [tags: documentation, assumptions]

Context:
- Files: docs/coding-agent-orchestration-harness/decisions/*.md
- Task/Wave: ADR correction
- Roles involved: Orchestrator

Symptom:
- ADRs used the personal display name `Kohta`, generic `Codex` for the consulted agent, and context-sensitive terms such as `current`.

Root cause:
- ADRs were written from the immediate chat context instead of as durable project records.

Fix applied:
- Updated ADR metadata to use `ebigunso` as decider and `GPT-5.5` as consulted model, and replaced context-sensitive wording with durable path/filename descriptions.

Prevention:
- For ADRs, use stable actor identifiers, explicit model names when AI consultation is recorded, and avoid time-relative language unless the decision depends on a dated state.

## 2026-05-09 - Preserve Exact ADR Consultation Provenance  [tags: documentation, assumptions]

Context:
- Plan: docs/coding-agent/plans/active/architecture-rationale-and-shared-references-plan.md
- Task/Wave: planning correction
- Roles involved: Orchestrator

Symptom:
- The ADR plan recommendation shortened the consulted entity from the user's intended `GPT-5.5 Pro` to `GPT-5.5`.

Root cause:
- The recommendation generalized the model name from existing ADR style instead of preserving the provenance detail provided by the user.

Fix applied:
- Updated the ADR plan open question and assumptions to specify `GPT-5.5 Pro` as the consulted entity for this ADR batch.

Prevention:
- Repo rule candidate:
  - audience: orchestrator
  - proposed rule: Record the actual consulted entity for each ADR or ADR batch; preserve exact user-provided provenance names unless the user explicitly asks to normalize them.
- Dispatch/plan guardrail:
  - When answering ADR metadata questions, verify the real consulted model/person for that decision instead of carrying forward a previous ADR's consulted value.

Evidence:
- `docs/coding-agent/plans/active/architecture-rationale-and-shared-references-plan.md` now specifies `GPT-5.5 Pro` in the open question resolution and assumptions.

## 2026-05-11 - Route Runtime Agents Through Plugin Skills  [tags: assumptions, runtime-adapters, skill-maintenance]

Context:
- Topic: latent-risk review routing assessment
- Roles involved: Orchestrator

Symptom:
- The assessment treated repo-relative reference paths as potentially usable by Codex runtime agents, even though runtime agents take the plugin and operate inside their own project directories.

Root cause:
- The distinction between plugin-packaged skill references and the target project working directory was not made explicit when evaluating adapter wording.

Fix applied:
- Treat runtime agent routing as skill-based plugin routing, not direct repo-relative path routing from the target project.

Prevention:
- When editing runtime agent prompts, word shared review/checklist routing as “use/read the relevant plugin skill/reference” rather than assuming repository-relative paths are available from the runtime agent's project directory.
- Keep direct file-path references primarily inside plugin skills/references and Orchestrator dispatch packets that are known to be interpreted in the plugin context.

## 2026-05-11 - Avoid Overfitting Validators To Skill Prose  [tags: validation, skill-maintenance, planning]

Context:
- Plan: docs/coding-agent/plans/active/integrate-latent-risk-review-routing-plan.md
- Roles involved: Orchestrator

Symptom:
- The plan considered adding static validation for latent-risk skill/reference internals and prompt-bloat heuristics.

Root cause:
- The validation scope mixed package-structure checks with prose-quality and skill-internal checks that are better handled through review.

Fix applied:
- Updated the plan so validators are added only for manifest, bootstrap, path, or package-structure requirements; skill prose and adapter prompt-bloat checks stay in human/Reviewer review.

Prevention:
- Before adding validators for skill changes, distinguish objective package integrity from editable skill prose. Prefer Reviewer checks for wording, criteria quality, and prompt-bloat concerns unless a structural packaging contract is at risk.

## 2026-05-17 - Discuss Worker Dispatch Waivers Before Self-Implementation  [tags: workflow, delegation, orchestration, correction]

Context:
- Plan: docs/coding-agent/plans/completed/codex-async-subagent-lifecycle-plan.md
- Task/Wave: harness implementation
- Roles involved: Orchestrator

Symptom:
- The Orchestrator implemented planned documentation changes directly after the user said to implement according to the plan, even though the plan defined Worker-style task ownership and the harness workflow expected subagent dispatch discussion for non-trivial work.

Root cause:
- The Orchestrator treated a runtime-level tool instruction limiting subagent spawning as sufficient reason to self-implement, but did not pause to discuss the conflict with the user before proceeding.

Fix:
- Pause implementation and discuss the dispatch constraint before moving further. Treat the current edits as unreviewed work until the user chooses whether to keep, revert, or re-run through Worker dispatch.

Prevention:
- Before self-implementing a non-trivial harness plan that calls for Worker/Reviewer roles, explicitly state any reason Worker dispatch is not being used and get user direction before editing implementation files.
- If runtime instructions conflict with the planned harness dispatch model, surface the conflict as blocked or needs-decision instead of silently waiving dispatch.

## 2026-07-16 - Verify Catalog-Provided Skill Paths Before Reading  [tags: environment, tooling, skills]

Context:
- Plan: goal-mode implementation, Task_2 (codex worker)
- Roles involved: Worker (codex)

Symptom:
- The session skill catalog pointed at a cached orchestration-harness SKILL.md path that no longer existed on disk.

Root cause:
- The catalog locator was stale relative to the plugin-cache filesystem state (plugin version had advanced).

Fix applied:
- The Worker fell back to the verified repository-local first-party copy and reported the mismatch.

Prevention:
- Verify a catalog-provided skill path exists before reading it; when maintaining this harness repository, use the repository first-party copy as the documented fallback and report the mismatch.

Evidence:
- Task_2 Worker report (agmsg, 2026-07-16).

## Promotion drain note (2026-07-23)

Promoted into harness skills by the v0.9.0 skill-promotion PR and removed from this log:
- "Complete Contract Specs Before Parallel Authoring" → subagent-strategy `dispatch-checklists.md`
- "Record Mid-Wave Rulings In The Decision Log At Ruling Time" → orchestration-harness `lifecycle-gates.md` (Escalation Ruling)
- Wiring-remediation worker batch → engineering-quality-baselines `testing-validation.md` (owning-surface line); runtime-adapter-contract `adapter-maintenance-checklist.md` (baseline/normalization/hash lines)
- "Promotion Triage Requires A Per-Item Existing-Text Diff" → improvement-loop `promotion-guidelines.md` (Existing-text check)
- "Re-Baseline Audit Tables Against The Current Tree Before Dispatch" → subagent-strategy `dispatch-checklists.md`

Appended 2026-07-23 (second drain): "Assert Postconditions On Scripted Text Mutations" promoted to engineering-quality-baselines testing-validation.md Evidence Integrity after a third occurrence (drain-note deletion caught by CME delta review) made promotion mandatory under the repeats rule.

## 2026-09-01 - Bundled Skill Content Is Consumer-Facing Only  [tags: skill-maintenance, review]

Context:
- Task: remove ablation-obsoleted guidance references from `engineering-quality-baselines` (ADR-I-0005, PR #47).
- Roles involved: Orchestrator

Symptom:
- Removal-history narration, tombstone annotations, and ADR-referencing reintroduction guards were embedded in bundled skill content (`SKILL.md`, reference files, a reviewer-packet template).

Root cause:
- Maintainer-perspective breadcrumb habit: writing for the editor of the repo rather than the consumer of the plugin. Plugin consumers only use skills — they cannot edit them and their package does not include `docs/` (ADRs, decisions, plans), so maintainer guards are inert and ADR references dangle.

Fix applied:
- Stripped all removal history, tombstones, and ADR references from `plugins/` content; kept maintainer invariants solely in the decision records; repointed template slots to plain current-state references.

Prevention:
- Content under `plugins/` is written purely for the consumer's agent at task time: current-state operating text only. Test each sentence with "does the consumer's agent act differently because of this?"
- Maintainer-facing material (change history, reintroduction guards, decision rationale) lives in `docs/coding-agent-orchestration-harness/decisions/` and this lessons log, never in bundled skill content.
- Templates deserve extra scrutiny: their text propagates into every generated artifact.
