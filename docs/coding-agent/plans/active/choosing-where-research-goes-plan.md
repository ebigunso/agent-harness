# Plan: Choosing where research goes

- status: draft
- generated: 2026-10-22
- last_updated: 2026-10-22
- work_type: docs

## Goal
- The harness gives what the governing brief `docs/coding-agent/briefs/active/choosing-where-research-goes-brief.md` states: one choice rule in the plugin, for the Orchestrator and Counsel alike, for where research goes among the options a workspace records, never assuming a seat, peer or model, research never inside a Worker's task; plan review flags research bundled into an implementation task; this repository's record of options in `common.md` with the researcher seat registered; and the Auditor's model compared on replayed past audits before it moves.
- The brief is the requirement and is not restated here; where this plan and the brief differ, the brief governs and the difference is a plan defect.
- This is the first plan of the run recorded in `docs/coding-agent/plans/active/choosing-where-research-goes-run.md`.

## Definition of Done
- The choice rule of the brief ("What the plugin states", items 1 to 6) is stated once in the plugin, in `skills/subagent-strategy/references/model-routing.md` under one heading of its own, and that reference is read whenever a Researcher is dispatched, a single-model workspace included; every other plugin text that decides or states where research goes points to it instead of saying "subagent".
- Counsel's text (the `counsel` skill and the two Counsel adapters) says its read-only Researcher is the Researcher role on whichever option the workspace records, chosen by the same rule from the same record, and Counsel reads that record before it dispatches research.
- The plugin names the record's place as `docs/coding-agent/rules/common.md`, the rule file both sessions read; no plugin text names a seat, a peer or a model.
- A research task of a plan is dispatched to the Researcher role, never to a Worker; the plan-review snippet flags an implementation task that bundles the research its own scope or acceptance depends on, its example the brief's own (a task that says to read the module first and then change it), and does not flag a task whose description states only the change.
- This repository's `common.md` carries the record of options, dated: the three Codex seats with their models (`agent-harness-researcher` on GPT-6 Astra; `agent-harness-worker` and `agent-harness-reviewer` on GPT-6.1-Sol), the dated strength observations, the owner's cost setting of 2026-10-04 for the roles other than research, research to the strongest option with the strength cost notwithstanding (brief, "This repository"), the Auditor's model and the comparison's outcome; `orchestrator.md` no longer carries the section or a second copy of any line of it.
- Scenarios 1, 3 and 4 are shown on a fixture and scenario 5 on replayed past audits, each outcome in the Progress Log; scenarios 1 and 2 stay human-only for the owner's next real run in this repository (brief, Pass conditions), the fixture showing scenario 1 only as far as a fixture can, and the closeout says so.
- The plugin's version is 1.1.0 in every file that states it, made as the last change before the run is reported ready.
- Package validators and smoke tests pass; the branch has Reviewer `APPROVED`; value audits at plan draft and closeout are logged; the plan closes and the run is reported ready: branch published, pull request opened under the standing approval, note to Counsel, nothing merged.

## Planner-added requirements
- The plan-review fixture for scenario 4 holds a control: an implementation task whose description states only the change, with no step to read or find anything out first, and the review must not flag it. Needed because: a check that flags every implementation task, whatever it says, would meet scenario 4 while showing nothing about bundled research.
- Scenario 3 is shown on the same fixture as scenario 1 (one probe, two records: this repository's and a workspace with no record and one model). Needed because: the brief's constraint that no seat is assumed is otherwise checked only by reading, and a rule that silently needs a recorded seat would pass scenario 1 and break scenario 3.
- The plugin's version becomes 1.1.0, as the last change before the run is reported ready. Needed because: an installed plugin is refreshed only when its version changes, so without it no workspace that has the plugin installed receives the rule; 1.1.0 because the change adds behaviour and breaks nothing; last, so that a later fix in the run does not ship under a version already published.
- In the owner's adjudication (Task_5) the verdict items are shown without the model that gave them. Needed because: the brief judges the comparison by the grades against what he would have decided, never by agreement; a label invites judging the model rather than the grade.

## Scope / Non-goals
- Scope: plugin text where research dispatch is decided or stated (R1 census, Context below): `skills/subagent-strategy/references/model-routing.md` and `SKILL.md`; `skills/orchestration-harness/SKILL.md` (Research Dispatch Gate), `references/dispatch-guidance.md`, `references/lifecycle-gates.md` (Research Dispatch Details); `skills/subagent-strategy/references/prompt-snippets.md` (plan-review snippet); `skills/plan-format/SKILL.md` (a research task's dispatch); `skills/counsel/SKILL.md`; `agents/Counsel.md`, `claude/agents/harness-counsel.md`; `agents/Orchestrator.md`, `claude/agents/harness-orchestrator.md` where they restate the gate; `skills/durable-docs-authoring/references/adr-template.md` (its example model names); the version files. This repository's `docs/coding-agent/rules/common.md`, `orchestrator.md` and `_lifecycle.json` if a source pattern changes. A decision record if the admission test passes. Fixtures in the Orchestrator's scratchpad.
- Non-goals: which model opens the Orchestrator or Counsel session (brief: not routed by this brief); any change to which models count as cheap or expensive; a default route to a peer researcher; runtime adapter physical names (`harness-researcher`, `harness_researcher`, `Researcher`), which are runtime identities, not workspace seats (Assumption A1); the Researcher adapters' own descriptions as a research-only subagent, which define the subagent option and stay true of it; validators for prose.

## Design
- Chosen: the rule lives in `model-routing.md`, which already holds the research routing by strength the rule's item 3 points to; a new first section states the rule, the reference's opening and its routing condition in `subagent-strategy/SKILL.md` widen from "more than one model" to "whenever a Researcher is dispatched", and the record's place moves from `orchestrator.md` to `common.md`. The other texts get a pointer at the place where each decides: the Research Dispatch Gate, the Researcher Dispatch section, Counsel's two research lines and its two adapters. The plan-review check gains one case beside the investigate-first check. Structure: one owner of the rule; Counsel reads a reference of `subagent-strategy` by path, as it already reads `value-documents`, without loading `orchestration-harness`. Evolution: a later change to the rule is one edit; concept count unchanged (the routing reference already exists). Verification: read-checkable against the brief; the fixture probes show the rule applied by a fresh agent. Operation: one more read at research dispatch, which already reads the routing reference in multi-model workspaces. Human: a dispatcher meets the rule where it chooses. Safety: no trust boundary moves.
- Alternative: a new reference `skills/subagent-strategy/references/research-routing.md` holding only the choice rule, with `model-routing.md` left as it is and pointers from the same places. Structure: two references state research routing (strength in one, choice in the other), and the rule's item 3 points across files. Evolution: a strength change touches two files. Verification, operation, human, safety: as the chosen one, plus a second read at dispatch.
- Why chosen: the brief's item 3 already defers to the routing reference; putting the rule there keeps one home for where research goes.

## Compatibility stance
- surface: the plan-review snippet's checks; the place a workspace records its options (`orchestrator.md` to `common.md`); `model-routing.md`'s routing condition.
- stance: migrate
- justification: the consumers are locatable: this repository's rule files, moved in this run (Task_3); the plugin's own texts that read the record (`model-routing.md`:13, the routing condition in `subagent-strategy/SKILL.md`:59); other workspaces that recorded options in `orchestrator.md` keep working as before until they move it, since the rule reads the record from rule files the Orchestrator reads anyway; the plugin says where it now belongs.

## Context (workspace)
- Related files/areas: R1 census of 2026-10-22 by the researcher seat (agmsg history, 10:52Z to 10:53Z; recorded in this plan's Progress Log), path:line for every statement above.
- Existing patterns or references: `model-routing.md` "Routing by work type" (research items at :19 to :21); `lifecycle-gates.md` Research Dispatch Details items 3 and 5 (waiver names what was read instead; legitimate research tasks); plan-review snippet `prompt-snippets.md`:75 (investigate-first check, issue 86); lessons 2026-10-15 "A Control For 'Research Stays Legitimate' Asks What The Repository Cannot Answer" and "A Dispatch That Opens By Casting The Agent As A Session Failed Before It Began"; 2026-10-05 "An Auditor Told What Not To Read Still Reads It When It Works From A Listing".
- Design record consulted and deviations from its acceptance: none found that governs where research goes.

## Open Questions (max 3)
- None.

## Assumptions
- A1: "no plugin text names a seat or a model" (brief, Pass conditions) covers workspace seats, peers and model names; the runtime adapters' physical agent names and platform names (Claude, Codex, Copilot) are the plugin's own runtime identities, kept — source: R1 Appendix B (no plugin hit for `agmsg` or `agent-harness-`; the only model names are the examples at `adr-template.md`:6); the brief's constraint is about what a workspace has, "only ever read from its own record".
- A2: Counsel never edits rule files (`counsel/SKILL.md`:22), so where the rule's item 5 says the observation is recorded, Counsel passes its observation to the Orchestrator, who records it — source: `counsel/SKILL.md`:22; `common.md` Repo Safety ("Only the Orchestrator edits").
- A3: in this repository the strength observation of 2026-09-15 (Codex models: detail; Claude models: writing) covers GPT-6 Astra, the peers' model before 2026-10-04 — source: `orchestrator.md`:25 and :28; it is re-observed for the Auditor role by Task_5, not assumed there.

## Tasks

### Task_1: The choice rule, and pointers to it
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/subagent-strategy/references/model-routing.md
  - plugins/coding-agent-orchestration-harness/skills/subagent-strategy/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/dispatch-guidance.md
  - plugins/coding-agent-orchestration-harness/skills/plan-format/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/counsel/SKILL.md
  - plugins/coding-agent-orchestration-harness/agents/Counsel.md
  - plugins/coding-agent-orchestration-harness/claude/agents/harness-counsel.md
  - plugins/coding-agent-orchestration-harness/agents/Orchestrator.md
  - plugins/coding-agent-orchestration-harness/claude/agents/harness-orchestrator.md
  - plugins/coding-agent-orchestration-harness/skills/durable-docs-authoring/references/adr-template.md
  - docs/coding-agent-orchestration-harness/decisions/ (a new record only)
- depends_on: []
- description: |
  State the brief's choice rule once, in model-routing.md under one heading of its own (its wording the Worker's; named in the Worker's report so Task_2's pointer uses it), and point to it from every place that decides where research goes. The brief's six items are the content; how they are worded is the Worker's, within the brief's words.
- acceptance:
  - model-routing.md carries the rule under that heading; its opening and the routing condition in subagent-strategy/SKILL.md make it read whenever a Researcher is dispatched, one model included; its record sentence names `docs/coding-agent/rules/common.md` as the file both the Orchestrator and Counsel read; item 5's recording is the Orchestrator's, Counsel passing its observation on (A2).
  - The Research Dispatch Gate (orchestration-harness SKILL.md and both Orchestrator adapters, kept in sync), dispatch-guidance.md Researcher Dispatch, subagent-strategy SKILL.md Core rule 1, and plan-format's rule on task types point to the rule; a plan task of type research is dispatched to the Researcher role, never a Worker.
  - The counsel skill's lines on Researchers and check-ups (now L19, L85) and both Counsel adapters say the Researcher is the role on whichever option the workspace records, chosen by the same rule from the same record, which Counsel reads before it dispatches research; the subagent physical name stays only as the subagent option.
  - No plugin text names a seat, peer or model; adr-template.md's example model names are replaced by a neutral form.
  - A decision record is proposed if the admission test in `durable-docs-authoring/references/adr.md` passes, filename at or under 135 characters.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py and python scripts/run_validation_smoke_tests.py pass; git diff --check clean on owned paths"
  - kind: command
    required: true
    owner: worker
    detail: "Adapter sync: diff the instruction bodies of the two Orchestrator adapters and the two Counsel adapters outside runtime-specific blocks (runtime-adapter-contract SKILL.md:23)"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review against the brief's 'What the plugin states' and Limits; zero-hit search for seat, peer and model names in plugins/"

### Task_2: Plan review flags research bundled into an implementation task
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/subagent-strategy/references/prompt-snippets.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/lifecycle-gates.md
- depends_on: []
- description: |
  Extend the plan-review snippet's investigation check (prompt-snippets.md:75) to an implementation task that carries the research its own scope, acceptance or validation depends on; Research Dispatch Details item 5 says research is never part of an implementation task, and item 2 points to the rule's section in model-routing.md (the two Workers are told the same working heading, `## Choosing where research goes`, and Task_1 keeps it unless its report says why not) for which option a Researcher runs on.
- acceptance:
  - The snippet flags an implementation task (any type other than research) whose description has it read, investigate or find out something first and then make the change (the brief's example: "read the module first and then change it"), and does not flag a task whose description states only the change; the reviewer answers this check as its own line.
  - lifecycle-gates.md items 2 and 5 carry the two statements above; nothing else in the file changes.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "Package validator and smoke tests pass; git diff --check clean on owned paths"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review against the brief's plan-review statement and scenario 4"

### Task_3: This repository's record of options
- type: docs
- owns:
  - docs/coding-agent/rules/common.md
  - docs/coding-agent/rules/orchestrator.md
  - docs/coding-agent/rules/_lifecycle.json
- depends_on: []
- description: |
  The Orchestrator moves `## Models And Peers In This Workspace` from orchestrator.md into common.md and brings it up to the brief's "This repository" section (rule files are the Orchestrator's to edit, common.md Repo Safety).
- acceptance:
  - common.md carries every item the Definition of Done lists for the record, dated; research goes to the researcher seat when the research wants detail strength and to a Claude subagent on the stronger model when it wants writing strength, cost notwithstanding; the handshake and registered-peers rules apply to any session that dispatches to a seat; ephemeral headless `codex exec` and `claude -p` sessions are allowed as measurement instruments, the Auditor comparison's replays included.
  - orchestrator.md no longer carries the section; `last_updated` is 2026-10-22 in each file changed; `_lifecycle.json` changes only if a source pattern names the moved text.
- validation:
  - kind: command
    required: true
    owner: orchestrator
    detail: "Package validator and smoke tests pass; git diff --check clean"
  - kind: review
    required: true
    owner: reviewer
    detail: "Every line of the old section has one home in common.md or is reported dropped with a reason; nothing left in orchestrator.md"

### Task_4: Scenarios 1, 3 and 4 on a fixture
- type: test
- owns: []
- depends_on: [Task_1, Task_2, Task_3]
- description: |
  In the Orchestrator's scratchpad, outside the repository. Scenario 1 and 3: a fresh Claude subagent, given the plugin root at this branch and a planning request that needs a census of a small fixture repository, says where it sends the research and why, once with this repository's common.md record and once with a fixture workspace with no record and one model; the dispatch names the agent's task, not a session role. Scenario 4: the Codex reviewer, with the plan-review snippet, reviews a fixture plan whose implementation task bundles its own research, in the brief's own words ("read the module first and then change it"), and a control plan whose implementation task states only the change; it answers the bundled-research check as its own line for each.
- acceptance:
  - Scenario 1: the research goes to the Researcher role on the recorded detail-strength option as its own dispatch; no Worker task carries it. Scenario 3: an in-session Researcher subagent on the dispatcher's own model, and no seat asked for.
  - Scenario 4: the bundled plan is flagged; the control is not.
  - Dispatch texts and outcomes are in the Progress Log; a failed probe sends the text back to Task_1 or Task_2 and is re-run.
- validation:
  - kind: review
    required: true
    owner: orchestrator
    detail: "Outcomes logged against each scenario; the control result answered as its own line"

### Task_5: The Auditor's model, compared before it moves
- type: test
- owns:
  - docs/coding-agent/plans/active/choosing-where-research-goes-auditor-comparison.md
  - docs/coding-agent/rules/common.md (the Auditor line only)
- depends_on: [Task_3]
- description: |
  Run by the Orchestrator (dispatch is its own; no nested subagents). The question it answers: which of Fable and GPT-6 Astra shows the strength the Auditor role needs here. Evidence: five past audit positions replayed on each model; its outcome sets the Auditor line of common.md.
  Cases (R2 report of 2026-10-22, its recommended set; dispatch snapshot and Changes since as R2 gives them, paths at the snapshot's active locations):
  - S1 setup plan draft #1, 38a08712, Changes since none: a supported hold on a weakened pass condition.
  - S2 setup plan draft #2, e8c46882, none: the repaired plan, a clean pass (correlated with S1).
  - R2 run-across-plans closeout #2, f8f381b5, c329ac42: a premature-read case (readings opened before any grade).
  - A1 audit-at-plan-draft-and-close closeout #1, 1327baa8, 2e237902: a premature-read case through a range diff.
  - S3 setup closeout #1, deaf3ac0, 6935b2c3: a clean grade table beside a design-bearing finding that held work; untracked inputs of the time are omitted and the case labelled adjusted.
  - The 2026-10-15 Fable dispatch (Q, 7017fbee) is recorded as an availability case only (HTTP 429): no replay recreates a quota.
  Each replay: a detached worktree at the snapshot in the Orchestrator's scratchpad, which is the session's working directory, so the repository and its plugin are found from where the session runs; the dispatch text is the historical fixed template verbatim with only its sanctioned fill-ins (the snapshot's mandate refuses anything more, 38a08712 `value-audit-mandate.md`:16 and :108); the role instructions are each runtime's own Auditor adapter at that snapshot, given as the session's role instructions; Fable as an ephemeral headless `claude -p` session, Astra as an ephemeral read-only `codex exec` session, both started in the worktree with nothing else in their context (the repository carries no loader file at the root). The researcher seat runs no replay (brief constraint). Read order is taken from each session's own event record.
  The key: one adjudication by the owner, through Counsel, covering every case, after the replays: for each case a neutral list of the items and issues at stake (every item either verdict or the historical verdict raised, and what the record shows happened later), each without its source, with room to name what all of them missed; he says for each what he would have decided. His answer is the key for both models.
- acceptance:
  - Ten replays run, or each that could not run is recorded with why; Fable and Astra had the same tree, dispatch text and tools in each case, any difference disclosed.
  - Each replay's dispatch text is byte-identical to the historical template with its fill-ins; a replay is re-run only when its recorded payload or runtime setup shows a construction defect, the corrected setup then applied to both models; a refusal to grade on a setup verified valid is that model's result and is scored.
  - The comparison record scores each replay on the brief's measures only, against the owner's key for every item of every case, shared omissions included: grades, missed and invented issues, source support, read order, completion; never polish or agreement with the Orchestrator.
  - The owner's adjudication is quoted in the record; common.md's Auditor line states which model showed the strength, dated 2026-10-22 or the date of his answer, and the Auditor moves or stays on that.
  - Worktrees removed after the replays.
- validation:
  - kind: review
    required: true
    owner: orchestrator
    detail: "Each replay's dispatch text, tree and session record logged; scores traceable to the owner's key and to the verdict text"
  - kind: review
    required: true
    owner: reviewer
    detail: "The comparison record checked against the brief's measures and constraints (fresh sessions; same evidence and tools; the researcher seat not auditing)"

### Task_6: Version 1.1.0
- type: chore
- owns:
  - every file that states the plugin's version (the plugin manifests and the marketplace entries)
- depends_on: [Task_1, Task_2, Task_3, Task_4, Task_5]
- description: |
  The last change before the run is reported ready.
- acceptance:
  - Every file that stated 1.0.0 as the plugin's version states 1.1.0; nothing else changes.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "Package validator and smoke tests pass; a search for 1.0.0 in version-bearing files finds none"

## Task Waves (explicit parallel dispatch sets)

- Wave 1 (parallel): [Task_1, Task_2, Task_3]; wave review.
- Wave 2 (parallel): [Task_4, Task_5]
- Wave 3: [Task_6]; final review; closeout audit.

Routing (common.md record, as moved by Task_3): Task_1 and Task_2 are skill prose, to Claude Workers on Opus; Task_3 is the Orchestrator's; Task_6 is mechanical, to the Codex worker seat; plan, wave and final review to the Codex reviewer seat; the value audit at plan draft to the Auditor on Fable (the record as it stands); the closeout audit to the Auditor on the model common.md's Auditor line names after Task_5.

## Rollback / Safety
- Every change is text on one branch; revert the branch. Task_5's replays run in worktrees and ephemeral sessions and change nothing in the repository but the comparison record and common.md.

## Progress Log (append-only)

Append-only editing rule (applies to both logs below): when appending an entry, anchor the edit on the previous entry and reproduce it (or anchor on the section's tail marker) so the edit inserts rather than replaces, and verify afterward that the log grew.

- 2026-10-22 10:52 Research before drafting: R1, a forensic census, dispatched to the Researcher role on the researcher seat `agent-harness-researcher` (detail strength), its own dispatch and report over agmsg; no Worker task carried it.
  - Summary: three layers of research statements (environment-agnostic role; subagent-worded dispatch defaults; a workspace record listing only the worker and reviewer seats); the candidate home `model-routing.md`; no Worker text forbids research; the investigate-first check lives only in the plan-review snippet; no plugin hit for seats, peers or agmsg, the only model names at `adr-template.md`:6; no validator pins the text to be changed.
- 2026-10-22 10:55 R2 (past audits for the Auditor comparison) dispatched to the same seat; on the context-overflow case, Counsel corrected its own wording in the brief (81fe274): no audit overflowed its context; the 2026-10-15 usage-limit case is one of availability.
- 2026-10-22 11:13 Plan review (Codex reviewer seat), round 1: NEEDS_REVISION, five findings, all taken: PR-F1 the replays keep the historical template verbatim and set the repository through the working directory; PR-F2 the owner's key covers every item of every case, shared omissions included; PR-F3 no audit at the wave boundary; PR-F4 the version and the unlabelled adjudication listed as planner-added, the rule's heading left to the Worker; PR-F5 the closeout audit follows the Auditor line as Task_5 leaves it. From its part 2: scenarios 1 and 2 kept human-only at closeout.
- 2026-10-22 11:18 Plan review round 2 (delta f8996e8..12217d7): PR-F1 to PR-F5 closed; NEEDS_REVISION on one new finding, taken: PR-F6, a refusal to grade on a verified valid setup is scored, and only a shown construction defect is re-run, for both models.
- 2026-10-22 11:21 Plan review round 3 (delta 12217d7..4496a75): APPROVED, no finding open. Readings written first (db52dff). Plan-draft audit, dispatch text (to a fresh Auditor dispatch on Fable):

  You are the value auditor. Read references/value-audit-mandate.md of the orchestration-harness skill and follow it exactly. Position: plan draft. Plan: docs/coding-agent/plans/active/choosing-where-research-goes-plan.md. Governing brief: docs/coding-agent/briefs/active/choosing-where-research-goes-brief.md. Changes since: none.
- 2026-10-22 Plan-draft audit verdict (Fable), as returned (absolute paths shortened to repository-relative):
  - Procedural disclosure: the first tool batch opened the plan and brief alongside the mandate rather than after it; neither is a notes or readings file, so the voiding condition is not met. Paths written down before grading and not opened before grades were fixed: the run's notes file, two completed briefs' notes files, the run's readings file (opened once after grading), and the nine readings files under `docs/coding-agent/plans/completed/`.
  - Position: plan draft
  - Documents read: `value-audit-mandate.md`; the plan; the brief; `value-documents/SKILL.md`; `common.md` at HEAD (Repository Reference Documents pointer lines and Standing Approvals); for understanding only, never as support: `orchestrator.md` (Models And Peers), `model-routing.md`, `prompt-snippets.md` (L65-89); after grading: the readings file
  - Product basis: brief in the product owner's words (brief L6; ratification L3, "I ratify the brief, hand it over now.", 2026-10-22)
  - Not audited: engineering side, no engineering philosophy ("none yet"); product philosophy likewise "none yet", so the product side is graded on the brief alone
  - Missing inputs: none
  - Value documents changed in range: none
  - Items:
  - DoD 1 | maps to the brief | cited | the choice rule (gives) with item 3; pass condition "stated once in the plugin at the place where dispatch is decided"; constraint "never assumes a seat, a peer, or a model exists"; scenario 3 | -
  - DoD 2 | maps to the brief | cited | "Counsel follows the same rule from the same record" (gives) | -
  - DoD 3 | maps to the brief | cited | means "lives in the rule file both the Orchestrator and Counsel read"; Limits constraint; pass condition "no plugin text names a seat or a model" | -
  - DoD 4, first two clauses | maps to the brief | cited | rule item 1; "Plan review flags research bundled inside an implementation task" (gives); scenario 4; the third clause graded as Planner-added 1 | -
  - DoD 5 | maps to the brief | cited | the researcher seat registered (gives); means "moves ... into `common.md`, dated"; research cost notwithstanding, the 2026-10-04 setting for the other roles (gives); the pass condition on common.md; "The record then states which model showed the strength, dated" (gives) | -
  - DoD 6 | maps to the brief | cited | pass conditions agent-checkable and human-only; scenario 3; no proxy settles a human-only condition; the plan keeps 1 and 2 pending | -
  - DoD 7 (version 1.1.0, last) | maps to the brief | inferred | no brief statement; extends the human-only pass condition on another repository and "Someone runs the harness in a workspace ..." (gives), which need the installed plugin refreshed; cheap to undo | -
  - DoD 8 | maps to the brief | cited | publish and pull request passed on the standing approval of 2026-09-30 in common.md Standing Approvals; the plan merges nothing; the note to Counsel is the run's report to the session that handed the brief over | -
  - Planner-added 1 (the control at scenario 4: a task that reads the module it changes, the change decided in the plan, not flagged; also DoD 4 third clause, Task_2 acceptance, Task_4's control) | maps to the brief | ask-now | scenario 4 "A draft plan whose implementation task includes 'read the module first and then change it': plan review flags the research bundled in" against the gives "Plan review flags research bundled inside an implementation task" and rule item 6 | Reasons: (1) it changes how a pass condition is checked and narrows it: scenario 4's own example is a task that reads the module first and then changes it, and the control says exactly such a task is not flagged once the plan states the change, so the probe would show scenario 4 only on a fixture worded more strongly than the owner's example; (2) the statements conflict as written, scenario 4's literal example on one side, the gives-statement's "research" and item 6's reading-versus-research distinction on the other, and the auditor does not resolve it. Value question: when a plan's implementation task says "read the module first and then change it" and the plan already states what the change is, is that research bundled into the task, which plan review must flag, or ordinary reading, which it must not? Where does he want the line between reading and research drawn for plan review?
  - Planner-added 2 | maps to the brief | cited | scenario 3; the constraint | -
  - Planner-added 3 | maps to the brief | inferred | as DoD 7 | -
  - Planner-added 4 (unlabelled adjudication) | maps to the brief | inferred | extends "judged by the grades against what the owner would have decided ... never by polish or by agreement"; cheap to undo | -
  - Non-goal: session models | maps to the brief | cited | "not routed by this brief" | -
  - Non-goal: cost classes | maps to the brief | cited | Left out on purpose | -
  - Non-goal: a default peer route | maps to the brief | cited | Left out on purpose; the constraint | -
  - Non-goal: runtime names kept (same as A1) | maps to the brief | inferred | extends the Limits constraint and the pass condition by reading "seat" and "model" as a workspace's; cheap to undo | -
  - Non-goal: Researcher adapters' descriptions stay | maps to the brief | inferred | extends the pass condition "Counsel's text refers to it rather than to a subagent", the subagent adapter being the subagent option; cheap to undo | -
  - Non-goal: validators for prose | internal mechanics | not audited | - | -
  - A1 | maps to the brief | inferred | as the runtime-names non-goal | -
  - A2 | maps to the brief | inferred | extends rule item 5 and "Counsel follows the same rule from the same record", which say nothing of who writes; cheap to undo | -
  - A3 | maps to the brief | cited | the researcher seat on GPT-6 Astra (gives); "research goes to the researcher seat whenever the strength matches" (gives); the comparison before the Auditor moves (gives); fact checked at orchestrator.md L25 and L28 | -
  - Task_1 | maps to the brief | cited | as DoD 1 to 3; the pass condition for adr-template | -
  - Task_1 acceptance, a decision record if the admission test passes | maps to the brief | inferred | no brief statement; extends the gives on where the rule lives; proposal only; cheap to undo | -
  - Task_2 | maps to the brief | cited | the plan-review gives; rule item 1; its control clause held under Planner-added 1 | -
  - Task_3 | maps to the brief | cited | as DoD 5; rule item 4; Counsel same record; the replay constraint | -
  - Task_4 | maps to the brief | cited | scenarios 1, 3, 4; the pass condition; the control held under Planner-added 1 | -
  - Task_5 | maps to the brief | cited | "The Auditor's model, compared before it moves" (gives, quoted in full) and its two constraints; the two premature-read cases both dated 2026-10-05 on R2's claim satisfy "among them" | -
  - Task_6 | maps to the brief | inferred | as DoD 7 | -
  - Routing line | maps to the brief | cited | the 2026-10-04 setting for the other roles; "the Auditor moves or stays on that" | -
  - Decision Log: no entries | - | - | - | -
  - Human-only conditions pending: "scenarios 1 and 2 in his next real run in this repository, and whether a session in another repository of his stops sending research to Workers"
  - Scenarios: none
  - Reading compared: DoD 1 to 7 agree; DoD 8 diverges (Orchestrator: covered as mechanics, relying in part on Counsel's hand-over, not the brief; audit: cited on the standing approval alone, outward-facing); Planner-added 1 diverges (extends; audit: ask-now); Planner-added 2 diverges (extends; audit: cited); Planner-added 3 and 4 agree; A1 agrees; A2 diverges (covered on non-value documents; audit: inferred); A3 agrees; Non-goals: session models, cost classes, default peer route agree; runtime names diverges (covered; audit: inferred); Researcher adapters' descriptions diverges (covered; audit: inferred); prose validators diverges in kind (covered; audit: not audited); Task_1 agrees; Task_1's decision-record clause unread (audit: inferred); Task_2 to Task_6 agree; Routing line agrees
  - Findings compared: none found
- 2026-10-22 Audit held Planner-added 1 as ask-now: the control said a task reading the module first and then changing it is not flagged once the plan states the change, narrowing scenario 4 against its own example. Handled by revision, not by a question to the owner: the check now flags the brief's own example as written, and the control is a task that states only the change, so the line between reading and research is the brief's example and nothing the plan draws. DoD 4, Planner-added 1, Task_2 and Task_4 revised; delta re-review and a plan-draft audit of the revision follow.
- 2026-10-22 11:28 Plan review round 4 (delta 25d69c5..1f7c4c4): APPROVED, no finding open. Plan-draft audit of the revised plan, dispatch text (to a fresh Auditor dispatch on Fable):

  You are the value auditor. Read references/value-audit-mandate.md of the orchestration-harness skill and follow it exactly. Position: plan draft. Plan: docs/coding-agent/plans/active/choosing-where-research-goes-plan.md. Governing brief: docs/coding-agent/briefs/active/choosing-where-research-goes-brief.md. Changes since: none.
- 2026-10-22 11:04 R2 report received: eleven candidate positions with dispatch snapshots, Changes-since revisions and fidelity limits; the mandate's history per snapshot; the four premature-read dispatches (all 2026-10-05); the Q case's original objects reachable only by reflog; a recommended set of five replay cases plus the availability record, taken as Task_5's cases.

## Decision Log (append-only; re-plans and major discoveries)

- (none yet)

## Notes (Risks / Edge cases)
- Risks: Counsel's dispatch by the rule needs a way to reach a seat; where the workspace records none, it falls to a subagent (scenario 3). The replays (Task_5) are expensive on both models; the brief accepts the cost.
