# Lessons Log (Coding Agent)

Purpose:
- capture recurring mistakes and the prevention mechanism
- enable "read once, don't repeat" improvements

## How to use
- Record a lesson after a missed hard gate, a review/CI/human finding the harness should have caught, or a correction that changed a durable default; low-signal corrections need no entry.
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
- adr
- assumptions
- audit
- contract
- correction
- documentation
- environment
- fixture
- gate-miss
- git-workflow
- input-boundary
- orchestration
- privacy
- runtime-adapters
- skills
- state
- troubleshooting
- worker
- workflow

## Entries

## 2026-04-26 - Keep Skill Content Version Agnostic  [tags: skill-maintenance, assumptions]

Context:
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
- Plan: docs/coding-agent/plans/completed/add-codex-runtime-support-plan.md
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

## 2026-05-09 - Preserve Exact ADR Consultation Provenance  [tags: documentation, assumptions]

Context:
- Plan: docs/coding-agent/plans/completed/architecture-rationale-and-shared-references-plan.md
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
- `docs/coding-agent/plans/completed/architecture-rationale-and-shared-references-plan.md` now specifies `GPT-5.5 Pro` in the open question resolution and assumptions.

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
- Plan: `docs/coding-agent/plans/completed/gh-stack-awareness-plan.md` (drafting, pre-approval).
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
- Plan: `docs/coding-agent/plans/completed/pr-watch-discoverability-plan.md`, Wave 1 dispatch.
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

## 2026-09-05 - Test Membership Removal When Emitted Tokens Are Re-Fed  [tags: validation, review, state]

Context:
- Plan: `docs/coding-agent/plans/completed/pr-watch-discoverability-plan.md`, Task_3 and Task_4.
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
- Codex plan review F3 and the Task_6 reachability dispatch, 2026-09-06; both recorded in the plan Decision Log.

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

## 2026-09-06 - Dispatch To Registered Peers, Never Spawn New Ones  [tags: orchestration, delegation, correction]

Context:
- Plan: `docs/coding-agent/plans/completed/frontier-model-guidance-refresh-plan.md` (audit probes and plan review).
- Roles involved: Orchestrator

Symptom:
- The Orchestrator spawned two new Codex peers (`astra-probe`, `plan-reviewer`) with `spawn.sh` for probe runs and plan review instead of sending the work to the registered `agent-harness-*` peers; the user deleted the extra roles afterwards.

Root cause:
- The registered peers had not answered an earlier ping, and the reflex was to create capacity rather than report the silence and ask.

Fix applied:
- Wave 1 work sent to `agent-harness-worker`; spawned roles torn down.

Prevention:
- Send agmsg work only to peers already registered and running in the agmsg app; automatic delivery works only for those sessions. If a registered peer is silent, tell the user and ask, rather than spawning or going headless.
- Sanctioned exception: a pure-baseline ablation probe may run as an ephemeral headless `codex exec` with skills and the user loader disabled, because it is a measurement instrument, not dispatch.
- Repo rule candidate:
  - audience: orchestrator
  - proposed rule: Route agmsg dispatch to the registered `agent-harness-*` peers only; never create new peers for a task.

Evidence:
- User correction 2026-09-06 ("send work towards already registered peers ... rather than spinning up new ones").

## 2026-09-06 - Dry-Check The Published Invocation And Every Exit Path  [tags: validation, tooling, review]

Context:
- Plan: `docs/coding-agent/plans/completed/frontier-model-guidance-refresh-plan.md`, Task_5 (probe runner archive).
- Roles involved: Orchestrator, Codex Reviewer

Symptom:
- The runner's stub dry check passed while the documented relative-root invocation was broken (paths resolved after `cd`), and a second pass passed while a setup failure exited 0 because the EXIT trap discarded the incoming status.

Root cause:
- The dry check asserted process exit only, from a shape that differed from the README command, and never drove the trap through a failing setup path.

Fix applied:
- Root resolved once; absolute prompt/output paths; EXIT handler preserves incoming status with restore failure taking precedence; dry check runs the exact README invocation under an isolated `CODEX_HOME` and covers normal, stale-backup, failing-stub, and setup-failure branches.

Prevention:
- A dry check runs the published invocation verbatim, asserts delivered content and outputs, and exercises every exit path through the real trap, not only the happy path.
- Restoration logic must preserve failure semantics as well as file contents.

Evidence:
- Codex Reviewer Task_5 findings 2026-09-06 13:26 and 13:47; runner commits a8fc57a78d6c and 4ace1fdf5eab.

## 2026-09-06 - ADRs Drifted Into Removal Ledgers Despite The Warrant Standard  [tags: documentation, skill-maintenance, review, correction]

Context:
- Plan: `docs/coding-agent/plans/completed/frontier-model-guidance-refresh-plan.md`, Tasks 4 and 5 (the first ADR-D-0017 and a removal-ledger record, both since replaced; see that plan's Decision Log).
- Roles involved: Orchestrator (author), Codex Reviewer

Symptom:
- ADR-I-0006 was a per-file deletion table with a warrant written around it; ADR-D-0017 bundled three decisions and mirrored skill wording. The user found both failed the lens: ADRs carry high-impact decisions and their constraints forward, not history.

Root cause:
- An older ADR (ADR-D-0015) directed "an implementation ADR per removal", and two precedents (ADR-I-0004, ADR-I-0005) had that shape; the directive and the precedent outranked the standard in practice.
- The plan pre-committed the ADRs as task deliverables with ledger-shaped acceptance, so review checked plan compliance, not the standard.
- The template's Implementation Impact and Measurement Basis sections invited inventories; a filled template read as complete.
- The collaboration flow (state the proposal in conversation before drafting) was skipped; the ADRs were written at closeout as summaries.
- Reviewer packets asked for "warrant and structure", which the reviewer verified as field presence.
- Plan approval was treated as acceptance of the records it named.

Fix applied:
- PR #57: ledger record replaced, bundled record split, records rewritten at decision altitude, retirements instead of in-place amendment; each record accepted by the user on its own. Standard rewritten in `durable-docs-authoring/references/adr.md` (admission test, one decision per record, prose why, no relative time, proposed/accepted/superseded lifecycle with immutability at merge, standalone acceptance).

Prevention:
- Run the admission test in `adr.md` on every proposed record, including one a plan or an older record told you to write; a directive or a precedent admits nothing.
- A plan task may propose a record only if the test passes; acceptance criteria never enumerate a record's contents.
- Present every record to the human on its own (title, decision, constraint, why) and land it only on an explicit yes; plan approval and merge do not accept.
- Reviewer packets for records ask the admission questions and whether a maintainer can act on the Decision alone, not whether fields are present.
- Repo rule added to `docs/coding-agent/rules/orchestrator.md` on 2026-09-06.

Evidence:
- User corrections 2026-09-06; ADR review rounds on PR #57; Task_1 review of the standard revision plan.

## 2026-09-10 - A Measurement Runner Publishes Its Evidence Only After The Containment Snapshot  [tags: validation, tooling, review]

Context:
- Plan: `docs/coding-agent/plans/completed/plan-gate-waiver-boundary-plan.md`
- Task/Wave: Task_4, run 1
- Roles involved: Orchestrator (runner author), Codex Reviewer

Symptom:
- The probe runner wrote its per-cell evidence files into the authoritative checkout while the cell ran, so the before/after content manifests of that checkout differed on exactly those files and the plan's identical-manifest criterion failed. A follow-up edit excluded the whole output directory from the manifest, which the Reviewer rejected as a blind spot for future edits there.

Root cause:
- Output location was chosen for convenience (next to the prompts) without asking whether the runner itself was inside the measured set.

Fix applied:
- Cell output stays under the scratch root until the cell's after-snapshot, then is copied into the checkout; nothing is excluded from the manifest. Run 1 preserved as a containment FAIL; run 2 accepted.

Prevention:
- Repo rule candidate:
  - audience: orchestrator
  - proposed rule: A runner that measures a worktree writes nothing into that worktree until its after-snapshot is taken; exclusions from a containment manifest are never used to make the runner's own writes disappear.
- Residual risk / waiver:
  - none

Evidence:
- Codex Reviewer Task_4 round 1 (2026-09-10); `frontier-guard-probes/live-loader/boundary/run1/` versus run 2.

## 2026-09-10 - Proposal Logging In A Plan Is Not ADR Derivability  [tags: documentation, review, adr]

Context:
- Plan: `docs/coding-agent/plans/completed/plan-gate-waiver-boundary-plan.md`
- Task/Wave: Task_2
- Roles involved: Orchestrator, Codex Reviewer

Symptom:
- The Reviewer's first round rejected ADR-D-0032 as re-derivable because the plan and the Task_1 research already stated the boundary and its rationale.

Root cause:
- The admission test's negative ("re-derivable from git history or from a plan") was read against the proposal's own drafting history, which adr.md's acceptance step 1 requires the plan to carry; every record proposed through a plan would fail that reading.

Fix applied:
- Admission re-run with the distinction recorded in the Decision Log; the Reviewer withdrew the finding and stated the corrected test: judge whether the substance merely reconstructs existing facts or carries an independent future constraint.

Prevention:
- Dispatch/plan guardrail (optional):
  - Reviewer packets for a proposed record say that the plan's Decision Log entry and the research it cites are the proposal's own drafting history; derivability is judged against the artifact the record constrains and against history whose substance is history (ledgers, evidence tables, investigation summaries).
- Residual risk / waiver:
  - none

Evidence:
- Codex Reviewer Task_2 rounds 1 and 2 (2026-09-10), the second carrying the corrected rule as a lesson candidate.

## 2026-09-10 - Codex Worker Sandbox May Not Resolve The Installed Python  [tags: troubleshooting, environment, worker]

Context:
- Plan: `docs/coding-agent/plans/completed/plan-gate-waiver-boundary-plan.md`
- Task/Wave: Task_3
- Roles involved: Codex Worker

Symptom:
- `python scripts/validate_harness_package.py` failed in the Worker's sandbox because the interpreter was not on the sandbox PATH; the same command passed with the installed executable's full path under approved escalation.

Root cause:
- The restricted sandbox environment does not expose the user-installed Python alias.

Fix applied:
- The Worker reran with the full path of a locally installed Python and reported both attempts.

Prevention:
- Troubleshooting note/candidate:
  - symptom: `python` not found inside a Codex Worker sandbox on this machine
  - cause: sandbox PATH lacks the user-level Python install
  - safe steps: rerun the required check with the installed interpreter's full path; report both the failed and the passing invocation, never mark the check skipped.
- Residual risk / waiver:
  - none

Evidence:
- Codex Worker Task_3 report (2026-09-10), commands_run.

## 2026-09-15 - A Step Sequence Rewritten As A Contract Needs Each Item Tagged Gate Or Input  [tags: skill-maintenance, review, documentation]

Context:
- Plan: `docs/coding-agent/plans/completed/skill-loading-and-description-trim-plan.md`
- Task/Wave: Task_3, Wave 1
- Roles involved: Claude Worker, Codex Reviewer

Symptom:
- Merging wave-integration's ten-step root checklist and nine-section reference into one contract produced an opener that required every contract item to hold before any follow-up dispatch. A blocked report whose required validation had not run failed the evidence item, so the opener forbade the very follow-up Worker the checklist dispatches to obtain that evidence.

Root cause:
- The numbered sequence was rewritten as a precondition set without deciding which steps were gates (evidence before Reviewer dispatch) and which were triage inputs (every report, including malformed and blocked ones).

Fix applied:
- Every returned report enters triage and corrective follow-up; pass-or-waiver evidence gates only Reviewer dispatch and closeout; the Worker traced a blocked and a malformed report through the result before reporting.

Prevention:
- Harness migration candidate:
  - category: review
  - proposed_home: skills-maintenance/references/final-ambiguity-pass.md
  - generalized_rule: When converting a step list into a contract or precondition set, tag each item as gate or triage input, write the opener from those tags, and trace one failing and one malformed case through the result before reporting.
  - suggested_change: add the tag-and-trace check to the final ambiguity pass for checklist consolidations.
- Residual risk / waiver:
  - none

Evidence:
- Codex Reviewer Task_3 finding (2026-09-15, 3877bd9); rework 727d7a4 approved.

## 2026-09-15 - The Package Validator Reads The First audience Line Literally  [tags: troubleshooting, validation]

Context:
- Plan: `docs/coding-agent/plans/completed/skill-loading-and-description-trim-plan.md`
- Task/Wave: Task_4, Wave 1
- Roles involved: Claude Worker

Symptom:
- `validate_harness_package.py` failed with "Worker report audience line must allow common/worker/orchestrator/reviewer" after the audience enum was folded into a prose bullet of `subagent-report-contract/SKILL.md`.

Root cause:
- The validator takes the first `audience:` occurrence in that file and splits the rest of the line on `|`; trailing prose or backticks on that line break the check.

Fix applied:
- The root keeps a line whose text after `audience:` is exactly `common | worker | orchestrator | reviewer`, placed before any `audience: reviewer` guidance.

Prevention:
- Troubleshooting note/candidate:
  - symptom: package validator rejects the Worker report audience line after a SKILL.md edit
  - cause: the first `audience:` line is parsed as the enum
  - safe steps: keep an enum-only `audience:` line first; rerun the validator.
- Residual risk / waiver:
  - none

Evidence:
- Task_4 Worker report (2026-09-15), commands_run.

## 2026-09-15 - Parallel Wave Workers Share One Tree, So Repo-Wide Validators See Peer Edits  [tags: troubleshooting, validation, orchestration]

Context:
- Plan: `docs/coding-agent/plans/completed/skill-loading-and-description-trim-plan.md`
- Task/Wave: Task_5, Wave 1
- Roles involved: Claude Workers in parallel

Symptom:
- Task_5's required package validator failed on `subagent-report-contract/SKILL.md`, a file owned by the parallel Task_4 and mid-edit at that moment; a rerun after the peer's edit settled passed.

Root cause:
- Parallel Wave tasks run in one working tree, so a repository-wide validator observes other tasks' unfinished edits.

Fix applied:
- The Worker classified the failure by diffing the failing file against HEAD and rerunning once it was consistent, reporting both runs.

Prevention:
- Troubleshooting note/candidate:
  - symptom: a repo-wide required validator fails on a file outside the Worker's owns during a parallel wave
  - cause: a peer Worker's in-progress edit in the shared tree
  - safe steps: diff the failing file against HEAD, confirm it is outside owns, rerun after the peer settles, report both runs; never edit the peer's file.
- Residual risk / waiver:
  - none

Evidence:
- Task_5 Worker report (2026-09-15), commands_run.

## 2026-09-16 - A Documented, Gitignored Setup Step Reads As Pre-Authorized Unless The Text Says Otherwise  [tags: orchestration, delegation, review]

Context:
- Plan: `docs/coding-agent/plans/completed/harness-contradictions-and-persistence-plan.md`
- Task/Wave: Task_7 probe round 1, fixture F2
- Roles involved: Orchestrator, Codex Reviewer, headless Worker sessions on Claude Fable 5.1 and GPT-6 Astra

Symptom:
- With the first ADR-D-0033 adapter text, which listed "a missing prerequisite" among findings to surface, the Fable modified-arm cell ran the fixture's README-documented generator on its own and argued that a documented, gitignored setup step "is not scope expansion". The Astra cell under the same text asked first.

Root cause:
- The text named the category but not the two arguments a capable model reaches for: that documentation implies permission and that an untracked output leaves no change worth asking about.

Fix applied:
- One sentence in Workflow step 5 of the three Worker adapters: a missing prerequisite or setup step waits for a ruling even when documented and even when its output is untracked or gitignored; only the acceptance criteria or a packet pre-ruling authorize it. Round 2: both models asked and left the file absent.

Prevention:
- Harness migration candidate:
  - category: delegation
  - proposed_home: skills-maintenance/references/final-ambiguity-pass.md
  - generalized_rule: When a boundary text names a category of thing not to do, also name the readings a capable model will use to place its case outside the category, and probe one such case before shipping.
  - suggested_change: add "name the escape readings" to the final ambiguity pass for boundary and permission text.
- Residual risk / waiver:
  - none

Evidence:
- Codex Reviewer Task_7 round 1 (2026-09-16) disposition (6) on F2-M-fable; round 2 APPROVED after 1384aa2.

## 2026-09-16 - Headless Claude CLI Sessions Carry Plugin SessionStart Hooks Unless Settings Are Excluded  [tags: troubleshooting, tooling]

Context:
- Plan: `docs/coding-agent/plans/completed/harness-contradictions-and-persistence-plan.md`
- Task/Wave: Task_7 probe round 1
- Roles involved: Orchestrator, Codex Reviewer

Symptom:
- A pure-baseline Fable cell reported "loaded instructions: none" for files but disclosed a persona banner injected by this host's enabled plugin (a SessionStart hook), so the baseline was not instruction-free.

Root cause:
- `claude -p` loads user settings, including enabled plugins and their hooks, even with an explicit system prompt, restricted tools, and an empty MCP config.

Fix applied:
- The runner passes `--setting-sources ""` to Fable cells; a dry check showed the session then reports no injected text. Round-1 baseline cells were kept with the qualification recorded.

Prevention:
- Troubleshooting note/candidate:
  - symptom: a headless Claude CLI cell shows text you did not pass (a persona, a mode banner)
  - cause: user settings load enabled plugins and their SessionStart hooks
  - safe steps: add `--setting-sources ""` (and keep `--strict-mcp-config` with an empty MCP config); ask the session to report injected text in a dry check before counting cells.
- Residual risk / waiver:
  - none

Evidence:
- Codex Reviewer Task_7 round 1 protocol note; dry check 2026-09-16.

## 2026-09-16 - Gitignored Outputs Are Invisible To git status In Probe Evidence  [tags: troubleshooting, validation]

Context:
- Plan: `docs/coding-agent/plans/completed/harness-contradictions-and-persistence-plan.md`
- Task/Wave: Task_7
- Roles involved: Orchestrator

Symptom:
- The F2 fixture gitignores its generated `schema.json`, so the per-cell status and created-file lists could not show whether a cell had run the setup step; the answer had to come from inspecting the clone directory.

Root cause:
- The runner collected `git status --porcelain --untracked-files=all`, which honors `.gitignore`.

Fix applied:
- The Orchestrator checked each clone directory directly and told the Reviewer; future runners record ignored files too (`git status --ignored` or a direct listing of the paths the fixture ignores).

Prevention:
- Troubleshooting note/candidate:
  - symptom: a probe's created-file evidence misses a file the session wrote
  - cause: the file matches `.gitignore`
  - safe steps: collect `git status --ignored --porcelain` alongside the untracked list, or list the ignored paths the fixture declares.
- Residual risk / waiver:
  - none

Evidence:
- Task_7 round 1 addendum to the Reviewer packet (2026-09-16).

## 2026-09-16 - A Frozen Revision Taken On A Stacked Branch Leaves The Branch Ancestry At Every Rebase  [tags: planning, validation, tooling]

Context:
- Plan: `docs/coding-agent/plans/completed/repeat-check-ablation-plan.md`
- Task/Wave: Task_1 and Task_2
- Roles involved: Orchestrator, Reviewer

Symptom:
- The protocol recorded the part-3 branch base as its frozen revision; two rebases of the stack in one day replaced that commit with a new one and moved the branch, so the recorded SHA was no longer in the branch's ancestry (the object still existed locally but was unreachable from any branch and would not survive a fresh clone or garbage collection).

Root cause:
- A rebase creates replacement commits and moves branch references; the old commit is left outside the new ancestry. A stacked branch's base commits belong to the lower branches, which change under review, so a SHA taken there has no durable reachability until the stack merges.

Fix applied:
- The frozen revision was pinned to the `main` tip the stack is based on, after checking the file under test is byte-identical from there to the branch; a Decision Log entry records the repoint and the new protocol hash.

Prevention:
- Troubleshooting note/candidate:
  - symptom: a pre-registered SHA in an experiment record is no longer an ancestor of the branch (and may not resolve at all in a fresh clone)
  - cause: the SHA was a stacked-branch commit that a rebase replaced, leaving it unreachable
  - safe steps: freeze on a commit that no open review rewrites (the trunk tip the stack is based on, or a tag pushed for the purpose); verify the frozen content is identical to the branch head before pinning.
- Residual risk / waiver:
  - none

## 2026-09-16 - A Grader Can Relax The Pre-Registered Hit Condition After Reading The Responses  [tags: validation, review, orchestration]

Context:
- Plan: `docs/coding-agent/plans/completed/repeat-check-ablation-plan.md`
- Task/Wave: Task_3
- Roles involved: Orchestrator, Reviewer, Claude grader subagents

Symptom:
- One blinded grader scored seven responses as hits under a condition it stated in its own summary ("evidence required only for the claim as made"), while the pre-registered rule required the response to require obtaining the missing evidence. The Reviewer's sensitivity copy showed the reading flipped that section's verdict.

Root cause:
- The grader packet restated the rule but did not name the tempting relaxation; the responses offered the author a way out (retract the claim), and the grader resolved the ambiguity in the responses' favor after seeing them.

Fix applied:
- The section was regraded on both models by fresh blinded graders with the rule's condition stated literally, including the alternative that does not count; round-1 grade files were preserved beside the regrade, and the adjudication is in the Decision Log and `outcome.md`. Applied consistently, the other model showed the same pattern in most responses, and the worst-model verdict did not change.

Prevention:
- Troubleshooting note/candidate:
  - symptom: a grader's summary adds a condition or reading the rubric does not contain
  - cause: the rubric left a plausible relaxation unnamed and the grader chose it post hoc
  - safe steps: when a grader reports a "judgment worth noting", treat it as a rubric deviation until checked; have the Reviewer recompute a sensitivity copy; regrade the affected unit on every model with the condition stated literally rather than adjudicating only the records found.
- Residual risk / waiver:
  - the corrected condition is now in the grader packet for this experiment only; a future protocol should carry it in the grading rule text.

## 2026-09-16 - Requirements Added During Drafting Passed As The User's  [tags: planning, review, scope-owns, correction]

Context:
- Plan: none in this repository; reported by ebigunso from a target-repository session run on the installed harness (GPT-family Orchestrator and Reviewer).
- Task/Wave: plan draft and plan review
- Roles involved: Orchestrator, Reviewer, user

Symptom:
- The drafting Orchestrator decided extra things were necessary to meet the request and wrote them into acceptance bullets next to the requested ones, without challenging their necessity.
- A scan of the plan by the user and the Reviewer's plan review both passed them; the additions surfaced only later as the source of an error.

Root cause:
- The Plan Gate's existence challenge runs on the request before decomposition; additions made during decomposition never face it.
- The plan template has no place where added requirements are visible as additions, so an added bullet is indistinguishable from a requested one on a scan.
- The plan-review snippet asks the Reviewer to verify sourced claims and question the decomposition, never to enumerate what the plan requires that the request did not; a Reviewer of the same model family passes a plausible-looking addition.

Fix applied:
- Plan `docs/coding-agent/plans/completed/plan-requirement-provenance-plan.md`: planner-added requirements are listed in one section of the plan with the reason the request cannot be met without each under the chosen design; the plan states the chosen design against at least one alternative on the whole-change cost axes; the Plan Gate re-runs the existence challenge and the design comparison before the plan is presented; the plan-review Reviewer enumerates the plan's unrequested requirements independently, tests each reason against the design, and may name a design that removes an addition with its cost delta (ebigunso's correction on the first presented plan: surfacing and justifying additions is not enough; the plan must land on the best design for the instance).

Prevention:
- Harness migration candidate:
  - category: skill
  - proposed_home: `plan-format`, `orchestration-harness` Plan Gate, `subagent-strategy` plan-review snippet (this repository is the harness; the plan above edits them directly)
  - generalized_rule: A requirement that entered a plan during drafting is listed as planner-added with the reason it must exist under the chosen design; the plan sets that design against an alternative; plan review enumerates the additions independently, tests their reasons against the design, and questions the design against the alternative rule 13 requires of every plan outside the proportional form, naming a better one with its cost delta where it exists.
  - suggested_change: per the plan above; no validator, per ebigunso's ruling that automation comes last.
  - follow-up (2026-09-16, ebigunso, after PR #71 opened): the comparison's axes were the diff-sized slice (dependencies, duplicated state, conversions). The mindset for writing and reviewing plans is the bigger picture: technical debt, fit with the project's philosophy or roadmap direction, testability where feasible, the cost of running the tests, and the cost of changing them when the design changes. Durable default: the design comparison walks the six lens groups `plan-format` rule 13 names (structure, evolution, verification, operation, human, safety), each lens a name with at most one clause; a fit claim names its source; plan review may open the three latent-risk references the snippet names for the Design section. Plan: `docs/coding-agent/plans/completed/design-comparison-horizon-plan.md`.
- Residual risk / waiver:
  - A drafting model may still leave an addition untagged; the Reviewer's independent enumeration is the catch, and the user's scan of one section is the backstop. If an untagged addition passes both, the second occurrence promotes to a validator question.

Evidence:
- ebigunso's account in session on 2026-09-16; the files named above read in that session (no draft-time alternatives or provenance obligation found in `plan-format`, `orchestration-harness`, or `subagent-strategy`).

## 2026-09-16 - Hold Fixes Until The Review Round On The Current Head Lands  [tags: git-workflow, review, correction]

Context:
- Plan: `docs/coding-agent/plans/completed/design-comparison-horizon-plan.md` (Copilot review loop on PR #71)
- Task/Wave: review-round handling after PR open
- Roles involved: Orchestrator

Symptom:
- Seven Copilot rounds each reviewed the commit before the latest push, so every round re-reported findings already fixed, and the Orchestrator triaged stale notes against the current head each time.

Root cause:
- Copilot auto-reviews every push. The Orchestrator pushed each round's fixes as soon as they were ready, while the review of the previous push was still running, so the next review always started from a superseded commit.

Fix applied:
- ebigunso's correction: await the push until the round on the current head has landed.

Prevention:
- Dispatch/plan guardrail:
  - After a push that triggers an automatic review, hold further fixes locally (commit without pushing) until the watcher reports that round; then push once with everything batched. A round whose commit is not the current head is triaged by first marking which notes are already fixed.
- Repo rule candidate:
  - audience: orchestrator
  - proposed rule: When a PR has automatic review on push, push fix rounds only after the review of the current head has landed; batch fixes locally in between.
- Residual risk / waiver:
  - none.

Evidence:
- PR #71 review commits: ab257e3, e3c05cb, badf522, ab743b8, b430246, 11bd23b, each one push behind the head at review time.

## 2026-09-30 - A Plan That Cites An Amendable Requirement By Position Drifts When It Is Amended  [tags: planning, review, scope-owns]

Context:
- Plan: `docs/coding-agent/plans/completed/value-level-operation-plan.md`
- Task/Wave: Task_6 and Task_7 acceptance; found by the first live value audit
- Roles involved: Orchestrator, Counsel (brief author), value auditor

Symptom:
- Task acceptance named the brief's statements by position ("the first three bullets", "the last two bullets"). The brief was amended several times during the run, gained bullets, and two statements were then carried by no task's acceptance; two task descriptions still stated what an amendment had replaced.

Root cause:
- Positional references to a document another session amends; and rulings that followed each amendment were sent to Workers without amending the plan text in the same edit (the 2026-09-06 lesson on acceptance bullets, repeated).

Fix applied:
- Acceptance now names the statements it carries; stale descriptions corrected; the audit is re-dispatched at the closeout position.

Prevention:
- Acceptance criteria name or quote the requirement statements they carry, never their position.
- After each amendment of the requirement document, re-read the plan's task text against it before sending the delta to a Worker.
- Repo rule candidate:
  - audience: orchestrator
  - proposed rule: A ruling or requirement amendment that changes what a task must do amends that task's description and acceptance in the plan in the same action that dispatches the change.

Evidence:
- Plan-draft value audit verdict, plan Progress Log, 2026-09-30.

## 2026-09-30 - A Standing Record Is Contradicted Only When Its Closure Words Are Broken  [tags: planning, documentation, adr]

Context:
- Plan: `docs/coding-agent/plans/completed/value-level-operation-plan.md`
- Task/Wave: plan draft and Task_3
- Roles involved: Orchestrator, Researchers, Worker, Reviewer

Symptom:
- The plan listed ADR-D-0003, ADR-D-0022 and ADR-D-0033 as contradicted and scheduled replacements; the admission test and the record review found all three stand, and two drafted replacements were dropped.

Root cause:
- "Contradicted" was judged on literal wording (a list of four roles; "routes agents to that skill"; "the two cases") and not on the reading already in force or on the record's own scoping clauses.

Fix applied:
- Replacements dropped; the plan's Decision Log records the three as not admitted.

Prevention:
- When a plan marks a standing record as contradicted, it cites the closure words in the Decision or Invariant ("only", "no other", "every") that the design breaks, under the reading existing text already applies; a bare enumeration is not one. A replacement whose own text says the decision is unchanged fails admission.
- Repo rule candidate:
  - audience: orchestrator
  - proposed rule: as the first prevention line.

Evidence:
- Task_3 Worker report and ADR review, 2026-09-30.

## 2026-09-30 - A Fix That Changes Who May Do Something Is Applied On Both Sides Of The Hand-Off  [tags: review, skill-maintenance]

Context:
- Plan: `docs/coding-agent/plans/completed/value-level-operation-plan.md`
- Task/Wave: second wave review fixes; final review
- Roles involved: Orchestrator, Workers, Reviewer

Symptom:
- A review fix (a philosophy's pointer line is added only on the owner's word) landed in the Orchestrator-side reference but not in the Counsel-side skill that tells Counsel what to send, so the two sides of the hand-off disagreed. Separately, one ruling on how a relayed consent may arrive was applied to the gate that raised it and not to the other gates the plan routed the same way.

Root cause:
- Fixes and rulings were scoped to the file or the gate the finding named, not to every place that states the same fact.

Fix applied:
- The Counsel skill now relays the location as the owner's quoted words; the plan states one carrier rule for every consent gate.

Prevention:
- When a fix or ruling changes who may do or authorize something, search the fact across the plugin and the plan, and apply it to both the producer and the consumer in the same delta.
- When several records are proposed together, the review packet asks for a pairwise read of their Decisions and Invariants.
- Harness migration candidate:
  - category: review
  - proposed_home: skills-maintenance/references/final-ambiguity-pass.md
  - generalized_rule: a change to a permission or hand-off rule is checked at every file that states either side of it.

Evidence:
- Final review of the first pull request, 2026-09-30; plan review round 2.

## 2026-09-30 - Whitespace And Frontmatter Checks Miss New Files  [tags: troubleshooting, validation]

Context:
- Plan: `docs/coding-agent/plans/completed/value-level-operation-plan.md`
- Roles involved: Workers, Reviewer

Symptom:
- `git diff --check` passed while the only files a task edited were untracked; a Worker's first agent description held a colon-space in an unquoted YAML scalar and both validators passed.

Root cause:
- `git diff --check` reads tracked content only; the package validator checks that frontmatter exists, not that it parses.

Fix applied:
- Workers checked new files by path and parsed agent frontmatter with a YAML loader.

Prevention:
- Troubleshooting note/candidate:
  - symptom: a whitespace or frontmatter defect in a new file passes the required checks
  - cause: the file is untracked, or the frontmatter is never parsed
  - safe steps: search the new file for trailing whitespace by path; parse agent and skill frontmatter with a YAML loader after editing a description.

Evidence:
- Task_2 and Task_6 Worker reports, 2026-09-30.

## 2026-09-30 - Record The Owner's Answer Against The Held Item Before Acting On It  [tags: orchestration, validation, correction]

Context:
- Plan: `docs/coding-agent/plans/completed/value-level-operation-plan.md`
- Task/Wave: Task_8, before the first pull request opened
- Roles involved: Orchestrator, Reviewer

Symptom:
- A value audit held the push and the pull request for the owner. The owner's answer arrived by relay and was written into the brief by the Counsel session, and the Orchestrator queued the push while the plan's Decision Log still said the item was held.

Root cause:
- The answer was acted on from the message that carried it; the step that records it against the item was skipped because the commit that followed touched the brief and a rule file only.

Fix applied:
- The answer is logged in the Decision Log against the item with its date and the owner's statement admitting relays; the delta review caught it before anything was pushed.

Prevention:
- Before acting on a released hold, check that the plan's Decision Log carries the owner's quoted answer against that item; the record comes before the act.
- Repo rule candidate:
  - audience: orchestrator
  - proposed rule: as the prevention line.

Evidence:
- Delta re-review before the first pull request, 2026-09-30.

## 2026-10-01 - A Ruling Is Provenance, Never The Reason  [tags: documentation, adr, correction]

Context:
- Plan: `docs/coding-agent/plans/completed/value-level-operation-plan.md`
- Task/Wave: the proposed decision records read by the owner
- Roles involved: Orchestrator, Worker (records), owner

Symptom:
- Rejected alternatives in a proposed record gave the owner's ruling as the reason they lost ("the owner kept them off limits", "the owner declined"). The owner's correction, quoted: "Me declining or ruling, in itself should not be treated as the reason for a decision. A reason behind it should always be present."

Root cause:
- Rulings arrived by relay with the decision but without the reasoning behind it, and the drafting instruction said to give only reasons on disk; the ruling was the only thing on disk.

Fix applied:
- The reasons as the owner gave them in discussion were written into the alternatives, with the ruling kept as provenance; `durable-docs-authoring/references/adr.md` gains the rule under Form.

Prevention:
- A rejected alternative states why it lost; a person's ruling or decline is provenance (who, quoted, when), never the reason. When a ruling arrives without its reason, ask for the reason before writing the record.
- Repo rule candidate:
  - audience: orchestrator
  - proposed rule: as the prevention line; the Counsel skill's relay carries the reason with the ruling where one was given.

Evidence:
- Owner correction relayed by Counsel, 2026-10-01, on ADR-D-0035.

## 2026-10-01 - Revisit When Names The Unexercised Premise, Not The First Use  [tags: documentation, adr, review]

Context:
- Plan: `docs/coding-agent/plans/completed/value-level-operation-plan.md`
- Task/Wave: the three records split from the plan-approval draft (ADR-D-0040 to ADR-D-0042)
- Roles involved: Orchestrator (author), Reviewer

Symptom:
- Two drafts wrote "the first use on a real initiative is the check of this record" under Revisit When. That names the occasion on which the record will be checked, which the record standard forbids, not the premise whose failure reopens it.

Root cause:
- `durable-docs-authoring/references/adr.md` stated the rule and gave the expiring-fact form, but no form for a premise nothing has exercised yet; the accepted ADR-D-0038 had the right shape (the date on which nothing had exercised it, and what failure reopens) and was not consulted.

Fix applied:
- Both lines restated as the unexercised premise and what reopens; `adr.md` Form now gives that case with the forbidden phrase as the counter-example.

Prevention:
- For a premise not yet exercised, write the date on which nothing had exercised it and what failure reopens the record; never the occasion. Before drafting a Revisit When, read the newest accepted record's for the shape.

Evidence:
- Reviewer findings on the split records, 2026-10-01; `adr.md` Form, Revisit When rule.

## 2026-10-04 - A Verdict Logged Verbatim Is Swept For Machine Paths Before It Is Committed  [tags: privacy, validation, orchestration]

Context:
- Plan: `docs/coding-agent/plans/completed/design-led-long-runs-plan.md`
- Task/Wave: the audit verdicts logged in the Progress Log
- Roles involved: Orchestrator, Auditor, Reviewer

Symptom:
- Seven audit verdicts were logged verbatim into the plan and committed locally. Each said where the auditor had read its mandate, as an absolute path under the machine's home directory with the user name in it. The final review caught it before anything was pushed.

Root cause:
- "Logged verbatim" was applied without the privacy sweep, which ran only on text the Orchestrator wrote. A subagent's output is text from the same machine and names the same paths.

Fix applied:
- The paths were replaced in the plan by an explicit redaction mark and a note saying what was changed; the unpushed commits that still hold the original are rebuilt before publication, on the owner's go.

Prevention:
- Before committing any text returned by a subagent or a peer (a verdict, a report, a review), run the same sweep as for one's own text, and redact with an explicit mark rather than silently. A local commit counts: what is committed is what gets pushed.

Evidence:
- Final review by the Codex reviewer peer, 2026-10-04, on the range from the run's start revision.

## 2026-10-04 - A Changed Label Is Traced Through Its Producer, Its Consumer And The Record's Validation  [tags: review, contract, orchestration]

Context:
- The audit's comparison line had an outcome renamed when a brief amendment changed which departures from a means are raised.

Symptom:
- The mandate could still emit a design-bearing departure as not recorded, while the run-side text held only on the other label, so that case would have passed with no escalation and no hold.

Fix applied:
- The comparison has three named outcomes, and the run side holds on each design-bearing one.

Prevention:
- When an emitted label or outcome changes, list every case the producer can emit and check each against the consumer's branches and the decision record's Validation lines, in the same change.

Evidence:
- Second-round Wave 2 review by the Codex reviewer peer, 2026-10-04.

## 2026-10-05 - A New Branch Is Traced Through Every Special Case And Every Stop And Release  [tags: review, contract, orchestration]

Context:
- A comparison gained a second direction and a stop gained a second mode (a goal loop) in one wave.

Symptom:
- The ordinary case was right, but a special branch written earlier (a departure from a means) still returned the old outcome, and a mapping of "every gate stops the loop" swept in gates that wait for no decision and gave them no way to resume.

Fix applied:
- The special branch names both directions; a gate the Orchestrator clears itself suspends without asking.

Prevention:
- When adding an outcome or a stop, list every existing branch that produces that kind of outcome and every transition into and out of a stopped state (held, corrected, answered, archived), and check each against the new rule in the same change.

Evidence:
- Combined review of two tasks by the Codex reviewer peer, 2026-10-05.

## 2026-10-05 - The Wave-Boundary Audit Is Dispatched Before The Next Wave, Not Remembered After  [tags: validation, orchestration, gate-miss]

Context:
- A plan under a brief with five waves, reordered mid-run when records were accepted at different times.

Symptom:
- Three wave boundaries passed with no value audit: each time the Orchestrator went from the wave's review straight to the next dispatch, because the next task was already unblocked by an acceptance that had just arrived.

Fix applied:
- The closeout audit covers the plan's whole range; the miss is recorded in the plan.

Prevention:
- A required gate is written into the order of work when the order changes, not left to memory.

Evidence:
- Third plan of the design-led long runs brief, 2026-10-05, found by the Orchestrator when reaching the closeout.

## 2026-10-05 - An Auditor Told What Not To Read Still Reads It When It Works From A Listing  [tags: validation, audit, input-boundary]

Context:
- The value audit keeps one file, the run's readings file, unread until its grades are fixed. The mandate said so, and gave the pattern to exclude.

Symptom:
- Four Auditor dispatches in two days opened a readings file before grading and had to return void, two of them one after the other on the same position. Each had printed several files in one command, taken from a file listing, before applying the boundary.

Fix applied:
- The mandate opens with a First Step: read the mandate alone, write down the paths not to open from name-only listings, open one named path at a time, and copy the exact exclude pathspecs.

Prevention:
- When an instruction forbids reading something that sits beside the things to read, put the instruction first, make the reader list what it will not open before it opens anything, and give the exact command form. A sentence inside a longer list of rules does not hold against a batch read.
- A position that returns void twice for the same cause is not cleared by a third dispatch on the same text; change the text or the input.

Evidence:
- The closeout audits of the design-led long runs run, the audit-positions run and the fixture run of the setup plan, 2026-10-04 and 2026-10-05; the first verdict after the change opened the file once, after grading.

## 2026-10-15 - A Decision Record's Filename Is Also A Path The Smoke Test Copies  [tags: documentation, adr, troubleshooting]

Context:
- Plan: `docs/coding-agent/plans/completed/counsel-questions-and-planning-research-plan.md`, Task_1, Wave 1.
- A record is named by its title in kebab case, and the title states the decision as a sentence.

Symptom:
- The package smoke test, which copies the repository into the system temporary directory, failed on Windows for a new record whose filename was over about 135 characters: the copied path crossed the platform's path length limit. The validators on the repository itself passed.

Fix applied:
- The Worker shortened the filename, keeping the title in the heading in full.

Prevention:
- Keep a record's filename at or under 135 characters; the heading carries the full title. A validator that copies the tree runs against the longest path it will create, not the longest path in place.

Evidence:
- Task_1 Worker report, 2026-10-15; ADR-D-0059's filename.

## 2026-10-15 - A Control For "Research Stays Legitimate" Asks What The Repository Cannot Answer  [tags: validation, planning, fixture]

Context:
- A fixture checked that plan review flags a plan whose first task postpones research the rest of the plan needs, and does not flag a research task that is a legitimate deliverable.

Symptom:
- The first control plan's research task measured a timing bound the README promised. The review did not flag it as postponement, but flagged it on necessity: the measurement served nothing in the request, so the control did not show the constraint either way.

Fix applied:
- The control's research task became a check whose answer is not in the repository (whether an outside reader named in the request accepts the new line), with the request extended to name that reader, the unknown stated in Assumptions in the form the gate asks, and the dependent task written as conditional on it. The review then answered the investigation check explicitly: not a finding, and said why.

Prevention:
- A control for this check needs a question that no reading before drafting could settle, that the request itself raises, and that later work is written as conditional on. A task that is merely bounded and well stated is judged on necessity first, and a control that fails on necessity shows nothing about postponement.
- Ask the reviewer to answer the check under test as its own line; a verdict on the whole plan does not separate the check from the rest.

Evidence:
- The plan's Progress Log, Task_3, 2026-10-15: two control reviews.

## 2026-10-15 - A Dispatch That Opens By Casting The Agent As A Session Failed Before It Began  [tags: troubleshooting, delegation, tooling]

Context:
- A fixture scenario needed a fresh agent to draft a plan the way an Orchestrator session would, with the plugin's policy read by path.

Symptom:
- Three dispatches that opened with "You are the Orchestrator session of the repository at ..." ended in request-side failures before any tool call, on two models. The Orchestrator's own messages that quoted the dispatch were stopped the same way.

Fix applied:
- The dispatch was reworded as a plain task: what to draft, where, which policy files to read first and by path, what not to do, and what to report in what order. The same inputs ran at the first attempt and gave the record the scenario needed.

Prevention:
- For a fixture or scenario dispatch the Orchestrator writes itself, where casting the agent as a session has failed before any tool call: word it as a task with inputs, procedure and a report shape. A scenario that needs "what a session would do" is shown by having the agent follow the session's policy by path and report its steps in order.
- When such a dispatch fails the same way twice before any work, change the wording, not the model.
- This does not reach a dispatch whose text a rule fixes, such as the Auditor's Fixed Dispatch Template, which is sent verbatim as its own rules state.

Evidence:
- The plan's Progress Log, Task_3, 2026-10-15, scenario 3.

## 2026-10-15 - A Small Change That Changes What The Product Does Still Goes To A Worker  [tags: workflow, delegation, orchestration, correction]

Context:
- A change the owner directed while a run was open for his judgement: remove one clause from a reference Counsel checks a philosophy's draft against, in words his direction gave.

Symptom:
- The Orchestrator classed the build as trivial because it was one clause with no how-choice, and made the edit itself. The review found that the edit changes which gaps Counsel puts to the owner, a meaningful behaviour change, so the Plan Gate's trivial criteria did not hold.

Root cause:
- Two separate calls were run together: small (no plan needed) and trivial (no Worker needed). A short, fully specified edit satisfies the first; the second asks whether the behaviour or design changes, and the length of the diff does not answer that.

Fix applied:
- The changes file's account was corrected and the finding logged; the edit was kept, since it was correct and rebuilding it through a Worker would add nothing.

Prevention:
- For a small change under a brief, decide "small" and "trivial" separately. A change directed because it alters what the product does is not trivial however short it is: dispatch a Worker, unless the owner has said to do it as trivial work.
- This repeats the 2026-05-17 lesson on self-implementation in a smaller form; read the two together.

Evidence:
- `docs/coding-agent/plans/active/first-use-in-a-fresh-repository-changes.md`, Small change 4, review finding FU4-F1.

## 2026-10-16 - A Lesson Is Applied Only When Every Prevention Sentence Has A Home  [tags: review, documentation, correction]

Context:
- A clean-up before a stack's merge: lessons and candidate blocks whose rule is already in a rule file or a plugin reference are removed under the log's drain convention.

Symptom:
- The Orchestrator ruled a candidate block and two lessons already applied at one line of `adr.md`. The Worker, checking each sentence, found that line holds only the first sentence; the second ("ask for the reason before writing the record") and the Counsel-relay half have no home.

Root cause:
- The home was matched against the headline sentence of the prevention, not every sentence.

Fix applied:
- The block and both lessons kept; the ruling corrected in the run's changes file.

Prevention:
- Before ruling that a lesson or candidate is already applied, quote the line that holds each of its prevention sentences; remove it only when every sentence has one.

Evidence:
- `docs/coding-agent/plans/active/value-level-operation-changes.md`, Small change 2, D12 and D13.

## 2026-10-16 - The Package Validator Writes Bytecode, So A Run Of It Is Not Read-Only  [tags: validation, tooling, delegation]

Context:
- A read-only sweep dispatched to the Codex worker ran `validate_harness_package.py` for a baseline.

Symptom:
- The run refreshed an ignored `__pycache__` file beside the plugin's scripts, though the dispatch was read-only and `PYTHONDONTWRITEBYTECODE=1` was set.

Root cause:
- The validator calls `py_compile.compile`, and the smoke runner compiles five scripts the same way; an explicit compile writes bytecode whatever the environment says.

Fix applied:
- None to the tools: the files are ignored and never ship. The worker reported it and ran the smoke tests in a disposable copy.

Prevention:
- A dispatch that must leave the tree untouched runs the validator and the smoke tests in a disposable copy, or says that ignored bytecode may be written.

Evidence:
- `docs/coding-agent/plans/active/value-level-operation-changes.md`, Small change 2, A2.

## Promotion drain note (2026-10-16)

Removed from this log on 2026-10-16, each prevention line already held by a rule or a plugin skill:
- "Avoid Tool-Specific Catch-All Rule Sections" (2026-05-13) → docs/coding-agent/rules/reviewer.md Recurring Misses And Prevention ("Durable rule sections should describe repository convention or review semantics"); rulebook `rule-suite-templates.md` reviewer section descriptions and `rules-files.md` (harness-global ideas go out as migration candidates)
- "Validate Exact Enum Sources, Not Broad Tokens" (2026-05-13) → docs/coding-agent/rules/orchestrator.md Repo-Specific Orchestrator Policies; docs/coding-agent/rules/reviewer.md Recurring Misses And Prevention
- "Use Feature Branch Naming And Escalate Nested Ref Creation" (2026-05-13) → docs/coding-agent/rules/orchestrator.md Repo-Specific Integration / Git Policy (branch naming; nested ref creation, `.git` internals)
- "Avoid Compatibility Wrappers Without Clear Need" (2026-05-09) → docs/coding-agent/rules/reviewer.md Review Risk Hotspots (entrypoint intent and admission); engineering-quality-baselines `SKILL.md` Drift Tripwires (compatibility shim)
- "Keep Maintainer Rationale Out Of Runtime Skill Instructions" (2026-05-09) → docs/coding-agent/rules/orchestrator.md Repo-Specific Orchestrator Policies
- "Keep ADR Metadata And Language Durable" (2026-05-09) → durable-docs-authoring `adr.md` Form (no time-relative wording), `adr-template.md` (`consulted` as durable identities), `authoring-rules.md` (durable roles or named people)
- "Avoid Overfitting Validators To Skill Prose" (2026-05-11) → docs/coding-agent/rules/orchestrator.md Repo-Specific Orchestrator Policies
- "No Version Numbers In PR Titles" (2026-09-05) → docs/coding-agent/rules/orchestrator.md Repo-Specific Integration / Git Policy
- "Merge Authorization Is Per Pull Request, Never A Standing Condition" (2026-09-10) → docs/coding-agent/rules/orchestrator.md Repo-Specific Integration / Git Policy (merge only on the owner's word naming what is merged)
- "Implementation-Time Artifacts Must Not Ship Inside Skill Contents" (2026-09-10) → docs/coding-agent/rules/orchestrator.md Repo-Specific Orchestrator Policies (rule and Reviewer-packet question)
