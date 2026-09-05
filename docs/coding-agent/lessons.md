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

## 2026-09-05 - Skill Content Carries Only What The Tool Cannot Teach  [tags: skill-maintenance, planning, review]

Context:
- Plan: `docs/coding-agent/plans/active/gh-stack-awareness-plan.md` (drafting, pre-approval).
- Roles involved: Orchestrator, Codex Reviewer (plan review)

Symptom:
- The reference design for `git-workflow/references/stacked-prs.md` spelled out what a stack is, a command-per-moment lifecycle, navigation commands, and REST field details.
- The user flagged it as overkill: most of it is rediscoverable from `gh stack --help` or is everyday knowledge, and every loaded line costs context on each task.

Root cause:
- Writing the reference as a tutorial for the tool instead of as the delta between what an agent already knows or can cheaply discover and what it must know before acting.

Fix applied:
- Cut the concept and lifecycle material; kept existence and availability checks, a pointer to the help text, the when-to-stack judgment, the four traps that are unsafe to learn by trial, ownership, and the watcher pointer; added a content test and a length target to the plan so the Reviewer applies it line by line.

Prevention:
- Every skill or reference line must pass: "could the agent learn this from the tool's `--help` or from plain knowledge?" If yes, cut it. Lines that earn their place: that a tool exists and how to check availability, judgment rules for when to use it, traps that are unsafe or expensive to discover by trial, ownership and safety mappings, and pointers.
- When a plan specifies new skill content, include the content test and an approximate length in the task acceptance so review is mechanical rather than taste.
- Repo rule candidate:
  - audience: orchestrator
  - proposed rule: Skill and reference content states only what an agent cannot learn from the tool's help or plain knowledge; concept explanations and command lifecycles are cut.
- Residual risk / waiver:
  - A v0.1.0 extension's flags may change; pointing at help text instead of freezing flags into the skill is the intended mitigation.

Evidence:
- Plan Decision Log entry 2026-09-05 in `gh-stack-awareness-plan.md`; `gh stack <cmd> --help` captures reviewed in session.

## 2026-09-05 - Use The Bundled Watcher, Never A Hand-Rolled Poll  [tags: orchestration, tooling, correction]

Context:
- Plan: `docs/coding-agent/plans/active/pr-watch-discoverability-plan.md`, Wave 1 dispatch.
- Roles involved: Orchestrator

Symptom:
- While waiting on Codex peer replies over agmsg, the Orchestrator wrote inline bash polling loops against `inbox.sh` instead of running the bundled `agmsg` `watch.sh`. One loop exited on a false match ("No new messages" contains "new message"); a later `watch.sh | head -1` pipeline never terminated, so a delivered report went unnoticed until the user pointed at the inbox.

Root cause:
- The Monitor tool was unavailable after a session resume, and the reflex was to improvise a poller rather than run the bundled script through the shell. This is the same failure the plan under execution exists to prevent for the PR watcher.

Fix applied:
- Run `watch.sh` in the background writing to a file, poll that file for the awaited sender, and kill the watcher once the message lands. Hand-rolled loops removed.

Prevention:
- When a bundled watcher exists (agmsg `watch.sh`, `pr-comment-watch.sh`), run it even when the Monitor tool is missing; a shell-backgrounded bundled script beats an inline loop every time.
- A watcher that must wake the session on one event needs an explicit termination path (kill after first match); a pipe through `head` does not end the producer.
- Repo rule candidate:
  - audience: orchestrator
  - proposed rule: Never hand-roll a polling loop for a channel that ships a watcher script; background the script and give it an explicit exit condition.

Evidence:
- Session 2026-09-05; user correction "Use the bundled monitor script from agmsg".

## 2026-09-05 - No Version Numbers In PR Titles  [tags: git-workflow, correction]

Context:
- Plan: pr-watch-discoverability and gh-stack-awareness closeouts (PRs #53, #54).
- Roles involved: Orchestrator

Symptom:
- PR titles carried a trailing "(v0.14.0)" / "(v0.14.1)", copied from older PR titles in the log.

Root cause:
- Pattern-matched the historical title style instead of asking what the title is for; the version already lives in the manifests and the PR body.

Fix applied:
- Titles rewritten without the version suffix.

Prevention:
- PR titles describe the change; version numbers stay in manifests and the PR body.
- Repo rule candidate:
  - audience: orchestrator
  - proposed rule: Do not put plugin version numbers in PR titles.

Evidence:
- User correction 2026-09-05.

## 2026-09-05 - Test Membership Removal When Emitted Tokens Are Re-Fed  [tags: validation, review, state]

Context:
- Plan: `docs/coding-agent/plans/active/pr-watch-discoverability-plan.md`, Task_3 and Task_4.
- Roles involved: Worker (Codex), Reviewer (Codex), Orchestrator

Symptom:
- `pr-comment-watch.sh --wait` printed deadline tokens from the accumulated member list, so a stack member removed mid-wait was emitted with stale values and re-admitted on re-feed. The self-check covered membership growth but not removal.

Root cause:
- The plan's self-check list named growth cases only; when emitted output becomes the next invocation's input, every lifecycle transition of a member is a serialization boundary, and removal was the untested one.

Fix applied:
- Deadline output now uses the latest successful poll's membership; two regressions added (removed sibling absent from output and re-feed set; failed final poll exits 4 with no tokens).

Prevention:
- When a tool's printed output is its own next input, test add, change, and remove for every tracked entity, not only add and change.
- Repo rule candidate:
  - audience: reviewer
  - proposed rule: For stateless tools whose printed tokens are re-fed as arguments, require a removal regression alongside growth in the self-check.

Evidence:
- Reviewer finding 2026-09-05 (Task_4, MAJOR issue 1) and its delta approval.

## 2026-09-06 - A Pointer's Source Check Covers The Target's Admission Clause  [tags: planning, review]

Context:
- Plan: `docs/coding-agent/plans/completed/plan-review-gate-plan.md` (pre-approval plan review).
- Roles involved: Orchestrator, Claude Reviewer and Codex Reviewer (plan review)

Symptom:
- The draft plan routed standard-flow plan review into `long-horizon-audit.md`, whose own header says never to load it in standard task flow, and no task owned that file.

Root cause:
- References were chosen by their content without re-reading the target's admission or usage clause, and without checking the target sat in some task's `owns` or was unchanged.

Fix applied:
- Route dropped; the consumer-naming check it would have added already lives in core-principles.

Prevention:
- When a plan adds a routing entry or pointer, the source check includes the target's admission clause and confirms the target is in an `owns` set or unchanged.
- Repo rule candidate:
  - audience: orchestrator
  - proposed rule: A plan that adds a pointer or routing entry verifies the target's own load or usage restriction and lists the target in `owns` when that restriction must change.

Evidence:
- Both plan reviews, MAJOR F1, 2026-09-06; plan Decision Log.

## 2026-09-06 - Claim Only The Reachability Actually Exercised  [tags: validation, review]

Context:
- Plan: `docs/coding-agent/plans/completed/plan-review-gate-plan.md` (pre-approval plan review).
- Roles involved: Orchestrator, Codex Reviewer (plan review)

Symptom:
- The live-test dispatch packet supplied plugin and repository roots, a working directory, and an explicit reference list that the bare snippet under review did not, so the test proved the packet worked, not the snippet the DoD claimed.

Root cause:
- The dispatched artifact and the artifact whose contract was claimed were different, and the plan did not say so.

Fix applied:
- DoD reworded to name the draft-packet test as such; a separate Task_6 dispatch with only the landed snippet became the reachability evidence, and it surfaced one real gap (the quality-baselines reference had no path).

Prevention:
- Record the exact text that was dispatched and any extra context the packet added; claim only the reachability that dispatch exercised. Test the landed artifact, not its draft.

Evidence:
- Codex plan review F3 and reachability report `.agent-work/reviewer/plan-review-gate-reachability.md`, 2026-09-06.

## 2026-09-06 - A Ruling That Changes An Acceptance Bullet Amends It In The Same Edit  [tags: planning, scope-owns]

Context:
- Plan: `docs/coding-agent/plans/completed/plan-review-gate-plan.md`, Wave 1 integration.
- Roles involved: Orchestrator, Claude Reviewer (reachability test)

Symptom:
- A Worker asked whether to exceed its six-line cap by one blank line for style consistency. The Orchestrator allowed it and logged the ruling in the Progress Log, but left the acceptance bullet at six, so the final Reviewer scored against a superseded number.

Root cause:
- Rulings are logged as narrative; nothing prompts an edit to the acceptance line the ruling overrides.

Fix applied:
- Acceptance bullet amended to seven, citing the ruling.

Prevention:
- When a ruling changes an acceptance bullet, amend the bullet in place and cite the ruling, in the same edit that logs it.
- Repo rule candidate:
  - audience: orchestrator
  - proposed rule: A ruling that changes a task's acceptance edits that acceptance bullet in the same action as the log entry.

Evidence:
- Reachability report finding 1, 2026-09-06; plan Progress Log Wave 1 and Task_2 acceptance.
