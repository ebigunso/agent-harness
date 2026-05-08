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
