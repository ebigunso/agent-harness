# Plan: Value-level operation of the harness

- status: in_progress
- generated: 2026-09-30
- last_updated: 2026-09-30
- work_type: mixed

## Goal
- The harness can be operated at value level as `docs/coding-agent/briefs/active/value-level-operation-brief.md` describes: the owner talks with a Counsel session about what the product should do, a ratified brief is the grounds for a run, a value audit grades the run against the documents that exist, and the run stops only where those documents do not decide.
- The brief is the requirement and is not restated here; where this plan and the brief differ, the brief governs and the difference is a plan defect.

## Definition of Done
- A Counsel session can be opened in each of the three runtimes and behaves as the brief's sections "What Counsel is", "How a conversation with Counsel should go", "Roles and sessions" and "Counsel as contributor" state.
- The four document types of the brief's "Documents, in the target repository" have one stated form, location and reading rule each, in one place.
- An Orchestrator session that finds value documents in a repository reads them, runs the value audit at plan draft, each wave boundary and closeout, handles the three grades as the brief states, under a ratified brief brings what needs the owner to Counsel instead of asking in its own session, and closes out as "candidate ready" leading with behaviour.
- With a brief the owner ratified, a citing audit authorizes plan execution; without one, plan approval is unchanged. This item lands only after the owner accepts its decision record on its own.
- A repository with no value documents behaves exactly as before this work.
- Every decision record this work contradicts is replaced through the record process, each accepted by the owner on its own; none is accepted by plan approval or merge. A replacement that fails the admission test or is declined means the part of the work that contradicts the standing record does not land, and that part returns to the owner as a value question.
- Package validators pass; each pull request has Reviewer `APPROVED`; nothing is merged without the owner's instruction naming that pull request.

## Planner-added requirements
- Delivery as two stacked pull requests, the plan-approval change second and alone. Needed because: the brief requires the change to plan approval to have its own decision record, accepted separately, so the authority change must be separable from, and later than, the audit it relies on. (Reworded 2026-09-30: the brief line first quoted here was replaced when the owner waived plan approval for this initiative.)
- Decision records beyond the one the brief names (plan approval): a replacement for ADR-D-0023 (the harness is entered only by selecting the Orchestrator), and new records for the Counsel role, for the value audit, and for the owner's word reaching the Orchestrator as Counsel's relay. Needed because: ADR-D-0023 states the opposite of what the brief asks and `durable-docs-authoring/references/adr.md` allows no partial supersession, and the three new decisions constrain later work in ways the text alone would not show; the relay record must be accepted before the first pull request, because that pull request routes the owner's decisions through Counsel. (Corrected 2026-09-30: ADR-D-0003, ADR-D-0022 and ADR-D-0033 were found to stand; see the Decision Log.)
- The value audit has one fixed dispatch template whose fill-ins are disk locations only, and each dispatch is logged verbatim in the plan. Needed because: the brief requires inputs "never the Orchestrator's summary", and free dispatch prose is the one place a summary could enter; the log is what lets a Reviewer check it.
- A run under a brief records the brief's path in its plan, and every audit dispatch names that path. Needed because: briefs accumulate in one directory, and once the audit can authorize a plan the choice of brief decides authority.
- The existing term "value audit" in plugin text (the keep/oversized/delete verdicts in `long-horizon-audit.md` and its three callers) is renamed "existence audit". Needed because: the brief gives "value audit" a second meaning, and the wave-integration and closeout texts would otherwise use one name for two procedures in the same file.
- The Researcher contract in its three runtime copies names the dispatching session instead of "the parent Orchestrator" and states a behaviour-level report for a Counsel dispatch. Needed because: the brief has Counsel learn the project's state through a Researcher reporting at that level, and today's contract returns plan-fill inputs to an Orchestrator.
- The product philosophy and the engineering philosophy are located only by pointer lines in `common.md` Repository Reference Documents, which the Orchestrator adds when it is handed a brief in a repository that has them or when the user tells it of one; briefs and their notes live together under `docs/coding-agent/briefs/`, and the governing brief is named in the hand-over. Value-level operation is on for a run when a governing brief was handed over or `common.md` points to a standing document, and off otherwise. Needed because: the auditor and the Orchestrator must find the documents without probing paths, the brief names none, and `common.md` is already read on every task, so a repository without the documents takes no new step and an unrelated file cannot switch the audit on.
- How an escalation travels from the Orchestrator session to Counsel: over a peer channel when the setup has one; otherwise written as an open question in the initiative's discussion notes, and the Orchestrator ends its turn naming that entry. The owner's answer returns as Counsel's relay quoting him over that channel, or as the owner's own statement in the Orchestrator session; a line in a file is never his answer. Needed because: the brief has the Orchestrator escalate to Counsel and names no transport, the harness cannot assume a messaging tool, and the owner ruled that ratification is an act and not a file line.
- A live dispatch of the landed value-audit template against this plan and this brief, at the plan-draft and closeout positions, as closeout evidence; the reachability claimed is limited to the positions exercised. Needed because: it is the only evidence that the fixed template works with nothing but disk inputs, and lessons 2026-09-06 "Claim Only The Reachability Actually Exercised" allows that claim only if it was exercised; it is not a trial of the product.
- One plugin version bump per pull request. Needed because: the package validator requires the three manifests to agree, and installed copies are keyed by version.
- A missing, malformed or partly graded audit verdict authorizes nothing. Needed because: ADR-D-0032 states that silence confers no authorization, and the conditional must fail closed.

## Scope / Non-goals
- Scope: plugin text, adapters, manifests, package validator, READMEs and decision records of this repository; the brief file itself is committed with the first pull request as the grounds of the work.
- Non-goals: persona voices, nested orchestration, a directory-structured discussion memory (brief, "Left out on purpose").
- Non-goals: writing a product philosophy or an engineering philosophy for this repository or for Character Memory; those come from the owner's conversations with Counsel.
- Non-goals: probes or trials of Counsel's conversation before shipping (brief: "No trial on a development build is required first").
- Non-goals: validators for grades, citations, conversation conduct or closeout wording (ADR-I-0007); new Worker report fields; changes to `validate_closeout.py`; a Counsel rule file; document template files; a Codex agent template or loader change for Counsel.
- Non-goals: tool-level enforcement of Counsel's reading limit (no plans or diffs; quick reads of code only in service of a discussion with the owner, never as a check on a run) and of a Codex Counsel session not drifting into Orchestrator work; no runtime offers it, so both are stated rules in this version. (Reading limit reworded 2026-09-30 after the owner's ruling on ADR-D-0034.)

## Design
- Chosen: Counsel is its own skill (`counsel`: conduct and boundaries in `SKILL.md`, the four document forms and reading rules in one reference that also admits the Orchestrator and the auditor as readers) with thin agents for the two runtimes that offer agent selection and explicit invocation of the skill in Codex; the standing documents are found through `common.md` pointer lines; the value audit is a mandate reference with a fixed dispatch template in the `orchestration-harness` tree; delivery is two stacked pull requests with the authority change second. Structure: one owner per piece of state (document forms in `counsel`, locations in `common.md`, audit procedure in the mandate, lifecycle positions in `orchestration-harness`); the audit depends on the documents, never the reverse; one new skill, one new agent per selectable runtime. Evolution: a repository without value documents takes none of the new paths; the authority change can be reverted alone; two new concepts (Counsel, value audit) and four document types, all from the brief; two standing records are replaced (ADR-D-0023, and ADR-D-0032 in the second pull request) and three added. Verification: the audit reads only files and git, so a dispatch is reproducible; structure is checked by the package validator, wording by Reviewer. Operation: one extra Reviewer-profile dispatch at plan draft, per wave and at closeout when value documents exist, none otherwise. Human: the session the owner opens sets the altitude; a Counsel session never sees gate text. Safety: Counsel holds no approval authority and no Worker dispatch; the owner's word reaches the Orchestrator only directly or as Counsel's relay quoting it; plan approval stays with the user until the separately accepted record lands. (consumers: see the Compatibility stance)
- Alternative: one home: Counsel's conduct as a reference inside the `orchestration-harness` tree behind a role switch at the top of its `SKILL.md`, document forms under `durable-docs-authoring`, the standing documents probed at fixed default paths, one pull request. Structure: no new skill and ADR-D-0022 stands, but `SKILL.md` gains a branch every Orchestrator session reads, location has two owners (default path and pointer), and `durable-docs-authoring` would own unratified notes its description excludes. Evolution: three fewer record replacements; the approval change cannot be reverted apart from the rest; a fixed path becomes a contract with every target repository. Verification: the same. Operation: a path probe on every run, including where no documents exist. Human: a Counsel session loads the Orchestrator's gate text and must ignore it, and a loaded `orchestration-harness` is what ADR-D-0020 treats as making a session the Orchestrator. Safety: an unrelated file at a default path switches the audit on; the role switch is the only thing keeping Counsel out of the Orchestrator role.
- Why chosen: the brief separates the two sessions by altitude, and the alternative puts both in one text where a misread switch gives Counsel the Orchestrator's reach; the fit claim rests on ADR-D-0020 (role follows the policy in context). The price is more record replacements, which are one-time, against an always-read branch and a per-run probe, which are permanent.

## Compatibility stance (required if a contract/interface/persisted format is touched)
- surface: the role map and agent names; the Researcher contract; the Plan Gate; the final-response contract.
- stance: preserve
- justification: the locatable consumers are repositories with the plugin installed (Character Memory, and this repository). Existing role names, the Worker report contract, the Codex loader block and the `done`/`blocked` outcomes are unchanged; every new behaviour is conditional on value documents existing in the repository.

## Context (workspace)
- Related files/areas: `plugins/coding-agent-orchestration-harness/` (skills `orchestration-harness`, `plan-format`, `wave-integration`, `subagent-strategy`, `improvement-loop`, `runtime-adapter-contract`, `engineering-quality-baselines`, `git-workflow`, `durable-docs-authoring`; `agents/`, `claude/agents/`, `codex/`; the three manifests; `scripts/validate_harness_package.py`), `README.md`, `docs/coding-agent-orchestration-harness/decisions/`.
- Existing patterns or references: the goal assessor (`orchestration-harness/references/goal-assessor-mandate.md`) is the precedent for a Reviewer dispatch profile with a disk-only input boundary and a fixed dispatch template; a repository's decision records are located by a pointer line in `common.md` (`rulebook/references/bootstrap-lifecycle.md:42-46`), and listed reference documents are read for the purpose `common.md` states (`orchestration-harness/SKILL.md:14`).
- Research: three Researcher reports (role surfaces; lifecycle seams; value documents and the third-party reference set the brief names), received in session on 2026-09-30.
- Governing brief: `docs/coding-agent/briefs/active/value-level-operation-brief.md`; ratification relayed by Counsel on 2026-09-30 quoting the owner: "That looks reasonable enough. You can now start delegating work to the orchestrator."
- Design record consulted and deviations from its acceptance: ADR-D-0003, D-0017, D-0020, D-0022, D-0023, D-0029, D-0030, D-0031, D-0032, D-0033, ADR-I-0006, I-0007. Contradicted: D-0023 and D-0032. D-0003, D-0022 and D-0033 stand (determined in Task_3 and its review; see the Decision Log).

## Open Questions (max 3)
- None open. Q1 to Q3 of the draft were answered on 2026-09-30; see the Decision Log.

## Assumptions
- A1: "The owner is the product owner" is decided per run by whether a ratified brief governs it: under one, the owner's decisions travel through Counsel; without one, he talks to the Orchestrator session as today. source: brief, "Roles and sessions", last three bullets (inferred).
- A2: Worker judgement calls are choices the acceptance criteria left open, reported in the existing `assumptions` field; a Worker still stops on anything the criteria did not decide. source: brief, "Lifecycle" ("Workers make choices within the bounds of their task, and the Orchestrator settles what falls outside them ... No act-then-report."); ADR-D-0033 Decision; `subagent-report-contract/references/schema.yaml:54`.
- A3: "Candidate ready" is the closeout outcome of a run under a brief: the plan is done, human-only conditions are listed as pending, and a rejected result returns as a new correction. source: brief, "Delivery and judgement" and "Lifecycle" (inferred).
- A4: With no value documents in a repository the audit does not run. source: brief, "Value audit": "It audits against whichever documents exist" (inferred).
- A5: At plan draft, a plan whose items are all graded cited or inferred, with none ask-now, counts as the brief's "citing audit"; the inferred items are journaled and shown at closeout. source: brief, "Stops during a run" ("Where a direction can be reasonably inferred from standing values, the run keeps going and reports it afterwards") and the grade definitions in "Value audit" (inferred).
- A6: A rejected result or a confirmed inferred call yields a candidate amendment that Counsel takes to the owner; the Orchestrator supplies the list at closeout and writes to neither philosophy. source: brief, "Documents, in the target repository" (standing documents changed only by the owner) and "Roles and sessions" (the owner does not type into the Orchestrator session) (inferred).
- A7: A Worker sees tenets only through its task packet. source: unverified; the brief states no Worker reading rule, and no task changes what a Worker reads.
- A8: The Reviewer's plan review still runs before the audit at plan draft when the audit can authorize the plan. source: brief, "Limits on the run" keeps it for this initiative; `orchestration-harness/SKILL.md:39` (inferred for the general case).
- A9: The registered Codex peers `agent-harness-worker` and `agent-harness-reviewer` are reachable. source: unverified; checked at first dispatch, and a silent peer is reported, never replaced by a spawned one.

## Tasks

### Task_1: Counsel skill and the value-document forms
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/counsel/**
- depends_on: []
- description: |
  Write the `counsel` skill: `SKILL.md` for what a Counsel session is, its limits, how a conversation goes, ratification and its relay to the Orchestrator quoting the owner's words, the hand-over, bringing the Orchestrator's escalations to the owner, its two later contacts with a run, how verdicts grow the documents, and check-ups through a read-only Researcher; one reference, `references/value-documents.md`, for the four document types (form, how each is located, who may change each, who reads and who never reads each).
  A session opened as Counsel stays Counsel: it does not load `orchestration-harness`, including in Codex when its own work could read as a coding task to the loader.
  The reference is read by Counsel, by the Orchestrator and by the value auditor, and says so.
  The brief is the requirement; carry its meaning, keep the owner's wording for anything tagged told, and write for the agent at task time. The brief's "Documents, in the target repository" section was amended on 2026-09-30 (prose philosophies with no fixed fields and no length limit; the owner's reading surface; candidate amendments); the amended text governs. One Counsel holds both the product and the engineering discussion (amended in the brief after a first ruling that left a second Counsel open).
- acceptance:
  - Every statement in the brief sections "What Counsel is", "How a conversation with Counsel should go", "Roles and sessions", "Counsel as contributor" and "Documents, in the target repository" is carried by the skill, or listed in the Worker report as not carried with the reason.
  - Each line passes the content test of lessons 2026-09-05 (an agent could not learn it from plain knowledge); `SKILL.md` is about 60 lines and the reference about 50.
  - Consumer-facing text only: no history, no decision-record or `docs/` references, no version labels, no persona voices, no template files.
  - The skill description states that it is for a session opened as Counsel and does not present itself as a way into the orchestration workflow; the skill text is what keeps a Codex Counsel session from taking the Orchestrator role.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py"
  - kind: review
    required: true
    owner: reviewer
    detail: "Line-by-line check of the skill against the named brief sections and the content test; final ambiguity pass per skills-maintenance"

### Task_2: Counsel agents and role registration
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/agents/harness-counsel.md
  - plugins/coding-agent-orchestration-harness/agents/Orchestrator.md
  - plugins/coding-agent-orchestration-harness/agents/Researcher.md
  - plugins/coding-agent-orchestration-harness/claude/agents/harness-counsel.md
  - plugins/coding-agent-orchestration-harness/claude/agents/harness-researcher.md
  - plugins/coding-agent-orchestration-harness/codex/agent-templates/harness_researcher.toml
  - plugins/coding-agent-orchestration-harness/.claude-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.codex-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.github/plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/README.md
  - README.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/runtime-role-map.md
  - plugins/coding-agent-orchestration-harness/skills/runtime-adapter-contract/references/tool-capability-matrix.md
  - plugins/coding-agent-orchestration-harness/skills/runtime-adapter-contract/references/adapter-maintenance-checklist.md
  - plugins/coding-agent-orchestration-harness/skills/runtime-adapter-contract/SKILL.md (added by ruling 2026-09-30: the Counsel two-copy qualification only)
  - plugins/coding-agent-orchestration-harness/skills/runtime-adapter-contract/references/prompt-budgeting.md (added by the same ruling)
  - plugins/coding-agent-orchestration-harness/skills/improvement-loop/references/entry-template.md
- depends_on: []
- description: |
  Make Counsel a selectable session role: a Copilot agent and a Claude agent, both with the physical name `harness-counsel`, that route to the `counsel` skill (skill name and reference path as in Task_1); in Codex a Counsel session is entered by the owner invoking the `counsel` skill, documented in the READMEs, with no loader or template change. Register the role wherever the role set is listed.
  Counsel may dispatch only the Researcher and is never dispatched. Express that in tool configuration where the runtime demonstrably supports it and as a stated rule elsewhere.
  Generalize the Researcher contract in its three copies to the dispatching session, with a behaviour-level report when Counsel dispatches it.
  Bump the plugin version in the three manifests.
- acceptance:
  - A Counsel agent exists for Copilot and Claude and neither loads `orchestration-harness`; the Codex entry is documented in the READMEs.
  - The role map, both READMEs, the Stable Role Model, the capability matrix, the maintenance checklist and the lessons entry template list Counsel consistently; existing physical names are unchanged.
  - The three Researcher copies carry the same meaning, and an Orchestrator dispatch of a Researcher reads as before.
  - The agents route to the skill and restate no conduct beyond the replicated role contract `runtime-adapter-contract` allows.
  - The three manifests carry the same new version.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py and python scripts/run_validation_smoke_tests.py"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review vs acceptance; docs/coding-agent/rules/reviewer.md hotspots for agent names, role maps and three-copy sync; adapter-maintenance-checklist"

### Task_3: Decision record drafts for Counsel and the value audit
- type: docs
- owns:
  - docs/coding-agent-orchestration-harness/decisions/*.md
- depends_on: []
- description: |
  A Worker on the writing side runs the admission test of `durable-docs-authoring/references/adr.md` and, where it passes, drafts a record with `status: proposed` for each of: Counsel as a separate-session role at value altitude; the replacement of ADR-D-0023 (replacements of ADR-D-0003 and ADR-D-0022 were also tested and not admitted; see the Decision Log); the value audit as a stateless Reviewer profile whose ask-now grade stops a run; the owner's word reaching the Orchestrator directly or as Counsel's relay quoting it. It determines whether ADR-D-0033's pause-case invariant can stand beside that grade and, if not, drafts its replacement as a record of its own; and whether the relay record can stand beside ADR-D-0032 and ADR-D-0017 for every consent other than plan approval.
  The brief and the proposals in this plan's Decision Log are the inputs; the records need nothing from the implementation. No standing record is edited or moved in this task.
- acceptance:
  - The Worker report gives the admission-test result for each proposal, including any that fail, and the stand-beside determinations for ADR-D-0033, ADR-D-0032 and ADR-D-0017 with their reasons.
  - Each draft holds one decision and is actionable from its Decision alone.
  - No existing record file is changed.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "ADR review snippet in subagent-strategy prompt-snippets, one record at a time; each replacement checked against the record it replaces"
  - kind: review
    required: true
    owner: user
    detail: "Accepts or declines each proposed record on its own, each brought to the owner after its Reviewer check, by the path Q1 and Q2 settle"
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py; from the repository root: git diff --check"

### Task_4: Value-audit mandate and the existence-audit rename
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/value-audit-mandate.md
  - plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/long-horizon-audit.md
  - plugins/coding-agent-orchestration-harness/skills/git-workflow/references/pr-review-monitoring.md
- depends_on: []
- description: |
  Write the mandate for the value audit as a Reviewer dispatch profile, after the goal-assessor mandate's pattern: input boundary, what is graded, the three grades, the scope test, the proxy rule, auditing whichever documents exist, the verdict record, and one fixed dispatch template. It refers to `counsel/references/value-documents.md` for document forms and locations and does not restate them.
  Rename the older "value audit" (keep/oversized/delete verdicts) to "existence audit" in the two other owned files.
  In this task the verdict at plan draft is advisory; plan approval is unchanged.
- acceptance:
  - The mandate carries every statement of the brief's "Value audit" section and the grade consequences of "Stops during a run".
  - Inputs are the value documents that exist and the artifact under review, read from disk; the Orchestrator's summary and the discussion notes are excluded by name.
  - The dispatch template is fixed text whose fill-ins are disk locations, a git revision and the position only, the governing brief among them; it admits no prose. For each of the three positions the mandate says what the artifact is, as something the auditor obtains itself from disk or git.
  - An inferred grade that rests on a tenet marked provisional says so in the verdict.
  - An irreversible or outward-facing item is ask-now even when a document covers it (ruling 2026-09-30, the literal reading of the brief; the owner has the question).
  - "Value audit" names only the new profile in the owned files; about 60 lines; content test as in Task_1.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py"
  - kind: review
    required: true
    owner: reviewer
    detail: "Check against the brief sections named; final ambiguity pass, naming the escape readings for the input boundary (lessons 2026-09-16)"

### Task_5: Package validator covers the Counsel agents
- type: impl
- owns:
  - plugins/coding-agent-orchestration-harness/scripts/validate_harness_package.py
  - plugins/coding-agent-orchestration-harness/scripts/run_validation_smoke_tests.py
  - tests/coding-agent-orchestration-harness/**
- depends_on: [Task_2]
- description: |
  Extend the package validator's role-map check so the Counsel agent paths and role-map entries are required like the other roles', as `docs/coding-agent/rules/reviewer.md` asks of role maps and expected file lists. Structure only: no check on Counsel's wording or conduct.
- acceptance:
  - The validator fails when a Counsel agent file or its role-map entry is missing, and passes on the tree Task_2 produced.
  - No check asserts prose, and no existing check is loosened.
  - The smoke tests change only if the installed-file set changed.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py; python scripts/run_validation_smoke_tests.py; the plan and worker-report fixture validators in docs/coding-agent/rules/common.md; a run with one Counsel agent path temporarily absent showing the failure"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review; exact-source checks per lessons 2026-05-13, within ADR-I-0007"

### Task_6: The audit in the run: reading, positions, grades, escalation
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/lifecycle-gates.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/dispatch-guidance.md
  - plugins/coding-agent-orchestration-harness/skills/wave-integration/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/wave-integration/references/**
  - plugins/coding-agent-orchestration-harness/skills/subagent-strategy/references/prompt-snippets.md
  - plugins/coding-agent-orchestration-harness/skills/subagent-strategy/references/dispatch-checklists.md
- depends_on: [Task_2, Task_4]
- description: |
  Wire the audit into an Orchestrator run, conditional on a governing brief having been handed over or `common.md` pointing to a standing document: the standing documents are found through `common.md` pointer lines, which the Orchestrator adds when handed a brief or told of a document by the user, and are read when non-trivial work starts; a run under a brief records the brief's path in its plan; the audit (mandate at `orchestration-harness/references/value-audit-mandate.md`, grades cited / inferred / ask-now) is dispatched at plan draft and at each wave boundary with the mandate's fixed template, naming at a wave boundary the revision the wave started from, and with its dispatch text and verdict logged verbatim; cited proceeds; inferred proceeds and is journaled for closeout; ask-now stops.
  In a run under a ratified brief, whatever needs the owner's authority or judgement is escalated to Counsel, over a peer channel when the setup has one and otherwise as an open question in the initiative's discussion notes with the turn ended. His answer counts when it is his own statement in the Orchestrator session or Counsel's relay quoting his words; the consent gates this reaches (record acceptance, merge, the two confirmation cases for discoveries) keep their rules and only the carrier is added; plan approval is not touched by this task and stays as ADR-D-0032 states it until Task_10. Without a ratified brief, today's plan mode applies, and a value-level ruling given in the Orchestrator session is recorded to the discussion notes as unratified.
  Before escalating anything, the run checks whether the documents already answer it. A review loop that does not converge becomes a value question. Worker `assumptions` are collected across the run at wave integration.
  Wherever `SKILL.md` names the outcomes, add `candidate ready` as the outcome of a run under a brief, in exactly those two words. Use "existence audit" for the older procedure in the owned files. Plan approval text is not changed by this task.
- acceptance:
  - Each behaviour above is stated once, in the file that owns that moment of the run, and the routing table points to the mandate.
  - A run with no governing brief, in a repository whose `common.md` points to no standing document, takes no new step: no dispatch, no read, no probe, no changed stop. A run under a brief in a repository with no standing documents is audited against the brief alone.
  - Every statement of the brief's "Stops during a run"; the ratification, escalation, relay-exception and not-the-product-owner statements of "Roles and sessions"; and these "Lifecycle" statements are carried: a review loop that does not converge becomes a value question; Workers choose within the bounds of their task and the Orchestrator settles what falls outside; what comes to the owner is limited to decisions at the level of the product or engineering philosophy; the acts the owner reserved still come to him. (Amended 2026-09-30 to name the statements instead of their positions, after the live audit found the brief had gained bullets.)
  - The plan-review snippet and existing Reviewer packets are unchanged except for the rename.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review vs acceptance; trace one run with value documents and one without through the changed text; gate-or-input tagging per lessons 2026-09-15"

### Task_7: Closeout as candidate ready, and what verdicts feed back
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/completion-closeout.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/final-response-contract.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/status-model.md
  - plugins/coding-agent-orchestration-harness/skills/improvement-loop/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/improvement-loop/references/promotion-guidelines.md
  - plugins/coding-agent-orchestration-harness/skills/durable-docs-authoring/references/adr.md
  - plugins/coding-agent-orchestration-harness/agents/Orchestrator.md
  - plugins/coding-agent-orchestration-harness/claude/agents/harness-orchestrator.md
- depends_on: [Task_2, Task_4]
- description: |
  For a run under a brief: the audit runs at closeout; the final response reports the outcome `candidate ready`, leads with behaviour, gives implementation detail only with its reason stated, and lists evidence for agent-checkable conditions, human-only conditions as pending, the judgement calls and inferred items that bear on the product's direction, with those resting on a provisional statement flagged, and where the full list is kept, what was learned that the philosophies do not account for, and Counsel's read or that it is pending. A proxy never stands in for a human-only condition. The closeout audit names the revision the run started from.
  The note that tells Counsel a candidate is ready carries the judgement calls and inferred items that bear on direction and the value documents changed during the run, and never the auditor's verdict.
  A wrong stop or a skipped decision is an improvement-loop trigger. Where a repository has a product philosophy or an engineering philosophy, a decision record's why names the tenet served.
  Use "existence audit" for the older procedure in the owned files. The Claude Orchestrator agent also says, as the Copilot one does, that Counsel is a separate session role the Orchestrator never dispatches.
- acceptance:
  - Every statement of the brief's "Closeout" section; the "Lifecycle" statements that a closeout shows the owner only the choices and rulings that bear on direction while the rest stay in the run's records, and that closeout reports "candidate ready" with its contents; the closeout clause of the provisional-tenet bullet in "Counsel as contributor"; (amended 2026-09-30 to name the statements) and the decision-record bullet of "Documents, in the target repository" is carried.
  - A run without a brief closes out as before: `done` or `blocked`, same items.
  - The two Orchestrator agents carry the same final-response meaning as the contract.
  - No validator or report schema is changed.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py and python scripts/run_validation_smoke_tests.py"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review vs acceptance; adapter sync per runtime-adapter-contract"

### Task_8: Live audit dispatch, and landing the accepted records
- type: test
- owns:
  - docs/coding-agent-orchestration-harness/decisions/**
  - docs/coding-agent/lessons.md
  - docs/coding-agent/plans/completed/**
- depends_on: [Task_3, Task_5, Task_6, Task_7]
- description: |
  Executed by the Orchestrator. Dispatch the landed fixed template, with nothing added, against this plan and the brief at the plan-draft and closeout positions, and log each dispatch text and verdict in the Progress Log; an ask-now item in a verdict goes to the owner through Counsel before the pull request opens. For each record the owner accepted, set it accepted and carry out the retirement it requires as the one atomic operation the record process defines; a declined or unadmitted record is logged and triggers a replan of the work that depended on it.
- acceptance:
  - Each dispatch text logged is the template verbatim, and each verdict grades this plan's user-facing items against the brief; reachability is claimed for the two positions exercised and no other.
  - Any gap the dispatch exposes in the template or mandate is fixed by a follow-up Worker on Task_4's files, not by adding context to the dispatch.
  - No record is accepted or retired without the owner's explicit yes for that record; after each retirement an absence search for the old filename is clean.
- validation:
  - kind: review
    required: true
    owner: orchestrator
    detail: "Dispatch text and verdict recorded in the Progress Log; record outcomes recorded in the Decision Log"
  - kind: command
    required: true
    owner: orchestrator
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py (supersession check); from the repository root: git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "Final review of the first pull request's whole diff; each retirement checked for repaired inbound references"

### Task_9: Decision record for plan approval by a citing audit
- type: docs
- owns:
  - docs/coding-agent-orchestration-harness/decisions/**
  - docs/coding-agent/lessons.md
  - docs/coding-agent/plans/completed/**
- depends_on: [Task_8]
- description: |
  Propose the replacement of ADR-D-0032 if the admission test passes: a plan is authorized by the user, or by a value audit against a brief the owner ratified in which every item is graded cited or inferred and none ask-now. The draft states that reading of "citing" in its Decision so the owner accepts or corrects it there, and the Worker reports what the retirement leaves stale in ADR-D-0033's reference to ADR-D-0032. Drafted by a Worker on the writing side, presented alone, and landed with the retirement of ADR-D-0032 by the Orchestrator only on the owner's yes for this record.
- acceptance:
  - The admission-test result is in the Worker report and logged in the Decision Log by the Orchestrator.
  - The record lands, and ADR-D-0032 is retired, only on the owner's explicit yes for this record.
  - After retirement an absence search for the old filename is clean.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "ADR review snippet"
  - kind: review
    required: true
    owner: user
    detail: "Accepts or declines this record on its own"
  - kind: command
    required: true
    owner: orchestrator
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py; from the repository root: git diff --check"

### Task_10: The plan-approval conditional
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/lifecycle-gates.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/status-model.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/value-audit-mandate.md
  - plugins/coding-agent-orchestration-harness/skills/plan-format/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/plan-format/references/**
  - plugins/coding-agent-orchestration-harness/skills/wave-integration/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/subagent-strategy/references/prompt-snippets.md
  - plugins/coding-agent-orchestration-harness/agents/Orchestrator.md
  - plugins/coding-agent-orchestration-harness/claude/agents/harness-orchestrator.md
  - plugins/coding-agent-orchestration-harness/.claude-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.codex-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.github/plugin/plugin.json
- depends_on: [Task_9]
- description: |
  Dispatched only after the owner has accepted Task_9's record. State the one conditional inside plan mode: with a brief the owner ratified (his own statement in the Orchestrator session, or Counsel's relay quoting him), after the Reviewer's plan review, an audit at plan draft that grades every item cited or inferred authorizes execution, and the relay, the verdict and the dispatch text are recorded in the plan; any ask-now item means the plan is not approved and the item goes to the owner as a value question; with no ratified brief, or with only an engineering philosophy, the user approves as before. Bump the plugin version.
- acceptance:
  - The conditional is stated once in the Plan Gate, and every other entry point that states plan approval agrees with it, the two Orchestrator agents included.
  - The text does not present the audit's verdict as the user's approval; the authority named is the owner's ratification of the brief, and a brief file's own status line is not that ratification.
  - A missing, malformed or partly graded verdict authorizes nothing.
  - Without a ratified brief the approval text reads as it did before this task; goal mode, merge authorization and the trivial-work tripwires are unchanged.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py; python scripts/run_validation_smoke_tests.py; the plan fixture validator in docs/coding-agent/rules/common.md"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review vs acceptance and vs the accepted record; escape readings for 'ratified' and 'cited' named and closed (lessons 2026-09-16)"

## Task Waves (explicit parallel dispatch sets)

- Wave 1 (parallel): [Task_1, Task_2, Task_3, Task_4]
- Wave 2 (parallel): [Task_5, Task_6, Task_7]
- Wave 3 (parallel): [Task_8]
- Wave 4 (parallel): [Task_9]
- Wave 5 (parallel): [Task_10]

Pull requests: the first after Wave 3 (Counsel, the documents, and the value audit in the run), the second after Wave 5 (plan approval), stacked on the first. Each is reviewed before it opens. By the owner's ruling of 2026-09-30 the two are brought to him as one stack through Counsel, with each number and link, what the stack ships at behaviour level and how he can observe it; nothing merges before his acceptance names the stack and its pull requests.

## Rollback / Safety
- Each pull request reverts on its own in reverse order; reverting the second restores user-only plan approval without touching Counsel or the audit.
- Until the second pull request merges, every plan is approved by the user as today.
- A retired decision record is restored only by a new record; retirements therefore happen only after the owner's acceptance.
- The untracked `.claude/` directory is not staged.

## Progress Log (append-only)

Append-only editing rule (applies to both logs below): when appending an entry, anchor the edit on the previous entry and reproduce it (or anchor on the section's tail marker) so the edit inserts rather than replaces, and verify afterward that the log grew.

- 2026-09-30 Plan drafted from the brief handed over by Counsel; three Researcher reports received.
- 2026-09-30 Plan review round 1: NEEDS_REVISION, five MAJOR and twelve MINOR findings; all accepted and applied in this revision (see Decision Log). Full re-review requested because tasks were renumbered and the delivery changed from three pull requests to two.
- 2026-09-30 Plan review round 2: NEEDS_REVISION, two MAJOR and nine MINOR findings, round-1 findings confirmed resolved; the hold on the relayed waiver judged required under ADR-D-0032. All findings applied; numbering and waves unchanged, delta re-review requested.
- 2026-09-30 Plan review round 3 (delta): NEEDS_REVISION, round-2 findings resolved, one new MAJOR (the pointer-only off-condition excluded brief-only repositories) and three MINOR; all applied as wording changes and confirmed by the Orchestrator against the four findings; the validator passes. Execution remains held on Q1.
- 2026-09-30 Execution authorized by the owner's statement in the Orchestrator session (Decision Log). Branch `feature/2026-09-30/value-level-operation` created from `main` at 9172590. Wave 1 dispatched: Task_1, Task_2, Task_3, Task_4 to Claude Workers in parallel.
- 2026-09-30 Wave 1, Tasks 1, 2 and 4 returned done (Task_3 still running).
  - Summary: `counsel` skill (SKILL.md 61 lines, reference 53); Counsel agents for Copilot and Claude, role registered, Researcher contract generalized in three copies, manifests at 0.22.0; value-audit mandate (71 lines) and the existence-audit rename in two files.
  - Validation evidence: each Worker reported `validate_harness_package.py` passing on the finished tree; Task_2 also `run_validation_smoke_tests.py`, `git diff --check`, and identical hashes of the three Researcher bodies.
  - Notes: follow-ups applied by the same Workers after rulings (Decision Log): Task_4 grade order; Task_1 second brief amendment; Task_2 Researcher report wording and the two-copy qualification. Lesson candidate from Task_2: validators do not parse agent frontmatter as YAML. Reviewer dispatched on Tasks 1, 2 and 4.
- 2026-09-30 Wave 1 review (Tasks 1, 2, 4): Task_1 and Task_2 APPROVED with minor findings, Task_4 NEEDS_REVISION (three MAJOR: verdict shape for a side with no document; discussion notes reachable through the diff; no statement that a verdict approves nothing). All findings and the owner's standing-approval rulings applied by the same Workers; validators pass after each delta. Task_3 returned six drafts; ADR review returned NEEDS_REVISION with two drafts to drop; revision is with the Worker.
- 2026-09-30 Wave 2 dispatched early for Task_5 (depends only on Task_2) and, once the mandate's contract was stable, Task_6 and Task_7. Task_5 done (validator requires the Counsel agent files, role-map tokens and the `counsel` skill; negative runs on a temporary copy fail with the exact path or token). Task_7 done (closeout, final response, improvement-loop trigger, adr.md line, two Orchestrator agents; validators pass). Task_6 running.
- 2026-09-30 Wave 2 completed: [Task_5, Task_6, Task_7].
  - Summary: Task_6 put the run-side procedure in `orchestration-harness/references/value-level-operation.md` (75 lines) with the on-condition and pointer in `SKILL.md` (151 lines, was 148) and one to three lines in the files that own each moment.
  - Validation evidence: every Worker reported `validate_harness_package.py` passing on the finished tree after each delta; Tasks 5 and 7 also the smoke tests; Task_5 negative runs on a temporary copy; Task_6 four traced runs.
  - Review: Wave 2 review with Wave 1 delta re-review: Task_5 APPROVED, Task_7 APPROVED with minors, Task_6 and the mandate NEEDS_REVISION (four MAJOR: value documents changed in range; an answered ask-now; scope expansion missing from the ordered test; pointer lines). All findings applied by the owning Workers; the final review of the whole diff is Task_8's.
  - Records: ADR re-review found all four admitted and needing wording fixes; revision is with the Worker.
  - Judgement calls (Worker choices the acceptance criteria left open, kept in full here): Task_1 kept the provenance tags in the reference and added "A question below that level goes back to the Orchestrator to settle"; Task_2 configured no Claude tool restriction for Counsel and kept terminal tools on the Copilot Counsel; Task_4 made an item covered by a standing approval `cited` on that approval, defined sides by the internal-mechanics test, and treats a reworded statement as a new statement; Task_5 added `counsel` to the required skills; Task_6 gates the position on `ungraded`, missing inputs and absent or malformed verdicts, and put the ask-for-ratification trigger in `SKILL.md`; Task_7 placed the closeout audit after the gates are confirmed and before the plan moves.
- 2026-09-30 Task_8, live audit dispatch 1 (plan draft position). Dispatch text, verbatim: "You are the value auditor. Read references/value-audit-mandate.md of the orchestration-harness skill and follow it exactly. Position: plan draft. Plan: docs/coding-agent/plans/active/value-level-operation-plan.md. Governing brief: docs/coding-agent/briefs/value-level-operation-brief.md. Changes since: none." Dispatched to a fresh Reviewer-profile subagent with nothing added.
  - Verdict as returned (verdict record; the auditor's surrounding remarks are summarized after it):
    - `Position: plan draft`
    - `Documents read: docs/coding-agent/briefs/value-level-operation-brief.md; docs/coding-agent/rules/common.md (pointer lines and Standing Approvals only; neither present, working tree and HEAD 9172590)`
    - `Not audited: engineering side, no engineering philosophy (no pointer line in common.md)`
    - `Missing inputs: none`
    - `Value documents changed in range: none (no range at plan draft)`
    - DoD1 Counsel session in three runtimes | maps to the brief | cited | brief: "The role is named Counsel; runtime name `harness-counsel`."; "Counsel and the Orchestrator are separate sessions." | -
    - DoD2 four document types, one form, location and reading rule | maps | cited | brief, "Documents, in the target repository" (the four types) | -
    - DoD3 Orchestrator reads documents, audits at three positions, escalates to Counsel, closes "candidate ready" | maps | cited | "It runs by position: plan draft, each wave boundary, closeout."; "it escalates to Counsel, and Counsel brings it to him"; "Closeout reports \"candidate ready\""; "It leads with behaviour." | -
    - DoD4 citing audit authorizes plans only after its record is accepted | maps | cited | "With a ratified brief, a citing audit approves plans; without one, ebigunso approves as today."; "The change to plan approval needs its own decision record, accepted by you separately." | -
    - DoD5 no value documents, behaviour as before | maps | inferred | extends "It audits against whichever documents exist."; "without one, ebigunso approves as today" | -
    - DoD6 contradicted records replaced, each accepted on its own | maps | cited | "Each decision record is still accepted on its own."; "A change to any of them reaches him through Counsel with a link to the document itself" | -
    - DoD7 validators, Reviewer approval, no merge without instruction | maps | cited | "Merges happen only on your explicit instruction for each pull request." | -
    - P1 delivery as two stacked pull requests | maps | ask-now | brief: "An irreversible or outward-facing action stops and comes back to him through Counsel even when the brief or a philosophy covers it"; "Two checkpoints stay with ebigunso ... accepting the decision record that changes plan approval, and each merge." | Reason: pushing the branch and opening a pull request writes to an external service, and no standing approval is in effect. Question: when a run's work has passed review, should it publish the branch and open the pull request on its own, with only the merge waiting for you, or come to you before anything leaves the machine? If on its own, do you approve that for all future runs?
    - P2 four decision records beyond the one the brief names | maps | inferred | extends "Decision records (ADRs) stay for architectural forks"; "Each decision record is still accepted on its own." | -
    - P3 fixed dispatch template, logged verbatim | internal mechanics | not audited | - | -
    - P4 brief path recorded in the plan and named in each dispatch | internal mechanics | not audited | - | -
    - P5 older "value audit" renamed "existence audit" | maps | inferred | extends brief, "Value audit" (the name takes a new meaning) | -
    - P6 Researcher contract names the dispatching session; behaviour-level report for Counsel | maps | cited | "For a check-up it learns the project's state through a read-only Researcher reporting at that level." | -
    - P7 philosophies found only by `common.md` pointer lines; on/off condition | maps | inferred | extends "It audits against whichever documents exist." A philosophy with no pointer line is not audited until the Orchestrator is told of it. | -
    - P8 escalation transport; a file line is never his answer | maps | inferred | extends "it escalates to Counsel, and Counsel brings it to him"; "Ratifying a brief takes an act of the owner, not a line in a file." With no peer channel, escalations wait until he next opens Counsel. | -
    - P9 live dispatch of the template as closeout evidence | internal mechanics | not audited | - | -
    - P10 one version bump per pull request | internal mechanics | not audited | - | -
    - P11 missing, malformed or partly graded verdict authorizes nothing | maps | cited | "With a ratified brief, a citing audit approves plans; without one, ebigunso approves as today." | -
    - N1 persona voices, nested orchestration, directory memory | maps | cited | brief, "Left out on purpose" | -
    - N2 no philosophy written for this repository or Character Memory | maps | cited | "Product philosophy: standing, changed only by the owner."; "No engineering guidelines exist for the harness yet." | -
    - N3 no trial of Counsel before shipping | maps | cited | "It ships as a first version. No trial on a development build is required first." | -
    - N4 no grade validators, report fields, rule file, templates, Codex loader change | internal mechanics | not audited | - | -
    - N5 "Counsel never reads plans, diffs or code" is a stated rule, not tool-enforced | maps | inferred | extends "Counsel never reads plans, diffs or code, never dispatches Workers"; "It ships as a first version." | -
    - A1 product-owner mode decided per run by a ratified brief | maps | inferred | extends "When ebigunso is not the product owner, today's plan mode applies and ebigunso talks to the Orchestrator session directly." | -
    - A2 Worker judgement calls are choices inside the task | maps | cited | "Workers make choices within the bounds of their task, and the Orchestrator settles what falls outside them ... No act-then-report." | -
    - A3 "candidate ready" is the closeout outcome under a brief | maps | cited | "Closeout reports \"candidate ready\""; "what proves off comes back as corrections" | -
    - A4 no documents, no audit | maps | inferred | extends "It audits against whichever documents exist." | -
    - A5 all cited-or-inferred counts as a "citing audit" | maps | inferred | extends "inferred (extends named tenets and is cheap to undo; proceed, journal, show at closeout)"; "a citing audit approves plans". Task_9's record puts this reading to the owner. | -
    - A6 candidate amendments go through Counsel; Orchestrator writes to neither philosophy | maps | cited | "A result ebigunso rejects, or an inferred call he confirms, yields a candidate amendment that he accepts or not in discussion." | -
    - A7 Worker sees tenets only through its packet | internal mechanics | not audited | - | -
    - A8 Reviewer's plan review runs before the audit | maps | inferred | extends "The Reviewer's plan review still runs" (stated for this initiative only) | -
    - A9 Codex peers reachable | internal mechanics | not audited | - | -
    - T1 Counsel skill and document forms | maps | cited | brief sections "What Counsel is", "How a conversation with Counsel should go", "Roles and sessions", "Counsel as contributor", "Documents, in the target repository" | -
    - T2a Counsel agents for Copilot and Claude, role registered, Researcher-only dispatch | maps | cited | "runtime name `harness-counsel`"; "may dispatch read-only Researchers for facts" | -
    - T2b Codex Counsel entered by invoking the skill, no agent | maps | inferred | extends "The session you open sets the altitude." | -
    - T3 record drafts, each accepted by the owner on its own | maps | inferred | as P2; "Each decision record is still accepted on its own." | -
    - T4 value-audit mandate and the rename | maps | cited | brief, "Value audit"; "An irreversible or outward-facing action stops ... even when the brief or a philosophy covers it" | -
    - T5 package validator covers Counsel agents | internal mechanics | not audited | - | -
    - T6 audit in the run, escalation, standing approvals | maps | cited | "cited (... proceed); inferred (... proceed, journal, show at closeout); ask-now"; "Stopping on something the documents already answer is also a defect."; "A review loop that does not converge ... becomes a value question."; "its home is the repository rule files" | -
    - T7a closeout as candidate ready: behaviour first, reasoned detail, what was learned, pending human-only conditions, Counsel's read | maps | cited | "It leads with behaviour."; "with the reason stated"; "It also reports what was learned that the philosophies don't account for."; "A proxy never stands in for a human-only condition."; "formed before seeing the auditor's verdict" | -
    - T7b closeout and the note to Counsel list the collected judgement calls, unfiltered | maps | ask-now | brief line 128: "the collected judgement calls"; brief line 126: "a closeout shows him only those that bear on direction" (tagged inferred, no quoted words) | Reason: the two statements bear on the item differently and the plan follows the older. Question: at the end of a run, do you want to see every choice the Workers made and every ruling the Orchestrator made, or only the ones that bear on the product's direction? Note: read together, the brief already answers "only those that bear on direction"; correcting T7 and the T6/T7 acceptance to brief lines 125-126 removes this item without asking him.
    - T8 live dispatch; landing accepted records | maps | cited | "Each decision record is still accepted on its own." | -
    - T9 record for plan approval by a citing audit | maps | cited | "The change to plan approval needs its own decision record, accepted by you separately." | -
    - T10 the plan-approval conditional | maps | cited | "One conditional inside plan mode, not a third lifecycle."; "With only engineering guidelines, it audits that side and plans are approved by ebigunso as today."; "Ratifying a brief takes an act of the owner, not a line in a file." | -
    - DL1 requirement challenge, cuts | internal mechanics | not audited | - | -
    - DL2 record proposals 1 to 7 | maps | inferred | as P2 | -
    - DL3 ratification reaches the Orchestrator by quoted relay | maps | cited | "The act happens in Counsel's session, and Counsel relays it to the Orchestrator quoting the owner's words." | -
    - DL4 plan review round 1 applied | internal mechanics | not audited | - (pull-request delivery is graded at P1) | -
    - DL5 relayed waiver held until the owner confirms in the Orchestrator session | maps | cited | "Counsel's relay carries his decisions to an Orchestrator session only after he has himself told that Orchestrator to accept Counsel's relays as his." | -
    - DL6 round 2 applied: relay record, pointer location | maps | inferred | as P7 and P2 | -
    - DL7 round 3 applied: Proposal 7 tightened | maps | cited | brief line 82, as DL5 | -
    - DL8 execution authorized; Counsel as carrier | maps | cited | "Plan approval is waived for this initiative only."; "Two checkpoints stay with ebigunso". The owner's statement in the Orchestrator session is the plan's claim and is in no document; the grade rests on the brief alone. | -
    - DL9 Wave 1 rulings | maps | inferred | extends "it's advisable to get advice from GPT models" (generalized to a model of another family); "Which model Counsel runs on is the owner's choice"; Copilot Counsel keeping terminal tools as N5 | -
    - DL10 proposals 2, 6, 8 not admitted; standing approvals; Wave 2 rulings | maps | inferred | extends "Decision records (ADRs) stay for architectural forks"; "its home is the repository rule files". Leaves ADR-D-0003 and ADR-D-0022 "slightly stale" on a surface where he "objects to anything even slightly off"; show at closeout. | -
    - `Human-only conditions pending: "You judge it through first real use on Character Memory, and what proves off comes back as corrections."` The brief marks no pass condition agent-checkable or human-only; this is the one statement that reads as his judgement of the result.
  - Auditor's remarks outside the record: 27 cited, 15 inferred, 2 ask-now, 12 not audited, none ungraded. The dispatch matched the fixed template and the auditor found the repository copy of the mandate by itself. Plan-hygiene findings: Task_7's description and the Task_6/Task_7 acceptance cite brief bullets by position and miss the two Lifecycle bullets the brief gained; the open value question and A2's note are stale; Task_1 and Task_3 descriptions are stale; owner quotations in the plan differ from the brief in contractions. For later positions: the brief is untracked and will be in range as new; brief statements amended on 2026-09-30 that say "told" without quoted words, or are tagged inferred, will not count as support at a wave boundary or closeout until each carries the owner's quoted words.
  - Acting on the verdict: P1 (ask-now, gate on the item): nothing is pushed and no pull request is opened until the owner answers; the value question went to Counsel. T7b (ask-now): met by changing the artifact, not by asking: the brief already says closeout shows only what bears on direction, the landed text follows it, and this plan's Task_6 and Task_7 text is corrected below to name the brief statements; the closeout-position audit regrades it. The 15 inferred items are journaled here in full; at closeout only those that bear on direction are shown. Reachability claimed: the plan-draft position only, so far.
- 2026-09-30 Final review of the first pull request's whole diff: NEEDS_REVISION, two MAJOR (a machine-specific path in the committed plan and in the brief; the pointer-line rule not carried to the Counsel-side text) and eight MINOR (standing-approval wording in three files and two records; one mandate sentence behind the owner's closeout ruling; a recording line the relay record's validation relies on; "four things" in the value-documents reference; ADR-D-0034's condition differing from the brief's). All six required validations passed on the Reviewer's rerun; the earlier MAJOR fixes were confirmed resolved. Every finding was applied by the owning Worker and each delta passed the package validator; the Counsel session replaced the path in the brief. ADR-D-0034 was revised before the owner answered it (the engineering discussion named; advice from another model stated as consulting, not dispatch; the brief's not-the-product-owner condition). The three local commits were rebuilt so the path is in no commit; nothing had been pushed.
- 2026-09-30 Lessons recorded in `docs/coding-agent/lessons.md` (four entries dated 2026-09-30).
- 2026-09-30 Task_8, live audit dispatch 2 (closeout position), after the first pull request's content was committed locally at 972793b. Dispatch text, verbatim: "You are the value auditor. Read references/value-audit-mandate.md of the orchestration-harness skill and follow it exactly. Position: closeout. Plan: docs/coding-agent/plans/active/value-level-operation-plan.md. Governing brief: docs/coding-agent/briefs/value-level-operation-brief.md. Changes since: 9172590." Dispatched to a fresh Reviewer-profile subagent with nothing added.
  - Verdict as returned (verdict record; the auditor's remarks outside the record are summarized after it):
    - `Position: closeout`
    - `Documents read: docs/coding-agent/briefs/value-level-operation-brief.md; docs/coding-agent/rules/common.md ("Repository Reference Documents" pointer lines and "Standing Approvals" only: no philosophy pointer and no Standing Approvals section, at HEAD 972793b and in the working tree)`
    - `Not audited: engineering side, no engineering philosophy (no pointer line in common.md). Product side audited against the brief alone (no product philosophy pointer).`
    - `Missing inputs: none` (the brief carries its ratification record at line 3, the owner's quoted words with the date; revision 9172590 resolves)
    - `Value documents changed in range: docs/coding-agent/briefs/value-level-operation-brief.md (new in range, added whole by commit 21ba7b6; 9172590 is main, before the brief was committed). No pointer line added, removed or changed; common.md unchanged in range.` Counted as support: statements under the line-3 ratification, and amendments carrying the owner's quoted words with a date. Not counted: line 129, which says it replaces an earlier line, is tagged inferred and has no quoted words. Not relied on alone: the unquoted tails of lines 37, 59, 60 and 63, and line 130.
    - DoD1 Counsel session in three runtimes | maps to the brief | cited | "The role is named Counsel; runtime name `harness-counsel`."; "Counsel and the Orchestrator are separate sessions. The session you open sets the altitude." | -
    - DoD2 four document types, one form, location and reading rule | maps | cited | "Documents, in the target repository" (product philosophy, engineering philosophy, initiative brief, discussion notes) | -
    - DoD3 Orchestrator reads documents, audits at three positions, escalates to Counsel, closes "candidate ready" | maps | cited | "It runs by position: plan draft, each wave boundary, closeout."; "When the Orchestrator needs his authority or judgement it escalates to Counsel, and Counsel brings it to him."; "Closeout reports \"candidate ready\""; "It leads with behaviour." | -
    - DoD4 citing audit authorizes plans only after its record is accepted (not yet landed; Tasks 9 and 10) | maps | cited | "With a ratified brief, a citing audit approves plans; without one, ebigunso approves as today."; "The change to plan approval needs its own decision record, accepted by you separately." | -
    - DoD5 no value documents, behaviour as before | maps | inferred | extends "It audits against whichever documents exist."; "without one, ebigunso approves as today" | -
    - DoD6 contradicted records replaced, each accepted on its own | maps | cited | "Each decision record is still accepted on its own." | -
    - DoD7 validators, Reviewer approval, no merge without instruction | maps | cited | "Merges happen only on your explicit instruction for each pull request." | -
    - P1 delivery as two stacked pull requests (push the branch, open the pull requests) | maps | ask-now | "An irreversible or outward-facing action stops and comes back to him through Counsel even when the brief or a philosophy covers it; a brief covers the intent, not the moment."; "The unit he accepts is a stack of pull requests that together ship something he can judge" covers the intent only | Reason: pushing a branch and opening a pull request write to an external service; no standing approval is in effect; neither the brief nor the Decision Log carries the owner's answer to the question raised at plan draft. Nothing has been published: the branch is not on the remote and no pull request exists for it. Question: when a run's work has passed review, should it publish the branch and open the pull requests on its own, with only the merge waiting for you, or come to you before anything leaves the machine? If on its own, is that for this stack only or an approval for all future runs?
    - P2 four decision records beyond the one the brief names | maps | inferred | extends "Decision records (ADRs) stay for architectural forks"; "Each decision record is still accepted on its own." | -
    - P3 fixed dispatch template, logged verbatim | internal mechanics | not audited | - | -
    - P4 brief path recorded in the plan and named in each dispatch | internal mechanics | not audited | - | -
    - P5 older "value audit" renamed "existence audit" | maps | inferred | extends the brief's "Value audit" section, which gives the name a new meaning | -
    - P6 Researcher contract names the dispatching session; behaviour-level report for Counsel | maps | cited | "For a check-up it learns the project's state through a read-only Researcher reporting at that level." | -
    - P7 philosophies found only by `common.md` pointer lines; on/off condition | maps | inferred | extends "It audits against whichever documents exist."; "Product philosophy: standing, changed only by the owner." | -
    - P8 escalation transport; a file line is never his answer | maps | inferred | extends "it escalates to Counsel, and Counsel brings it to him"; "Ratifying a brief takes an act of the owner, not a line in a file."; "only after he has himself told that Orchestrator to accept Counsel's relays as his" | -
    - P9 live dispatch of the template as closeout evidence | internal mechanics | not audited | - | -
    - P10 one version bump per pull request | internal mechanics | not audited | - | -
    - P11 missing, malformed or partly graded verdict authorizes nothing | maps | inferred | extends "With a ratified brief, a citing audit approves plans"; "Skipping a decision that needed to reach you is a harness failure to be fixed." | -
    - N1 persona voices, nested orchestration, directory memory left out | maps | cited | "Left out on purpose" (all three named) | -
    - N2 no philosophy written for this repository or Character Memory | maps | cited | "Product philosophy: standing, changed only by the owner."; "No engineering guidelines exist for the harness yet." (provisional) | -
    - N3 no trial of Counsel before shipping | maps | cited | "It ships as a first version. No trial on a development build is required first." | -
    - N4 no grade validators, report fields, rule file, templates, Codex loader change | internal mechanics | not audited | - | -
    - N5 "Counsel never reads plans, diffs or code" is a stated rule, not tool-enforced | maps | inferred | extends "Counsel never reads plans, diffs or code, never dispatches Workers, and may dispatch read-only Researchers for facts."; "It ships as a first version." | -
    - A1 product-owner mode decided per run by a ratified brief | maps | inferred | extends "When ebigunso is not the product owner, today's plan mode applies and ebigunso talks to the Orchestrator session directly." | -
    - A2 Worker judgement calls are choices inside the task | maps | cited | "Workers make choices within the bounds of their task, and the Orchestrator settles what falls outside them; that is unchanged from the accepted harness rule. No act-then-report." | -
    - A3 "candidate ready" is the closeout outcome under a brief | maps | cited | "Closeout reports \"candidate ready\": evidence for agent-checkable conditions, human-only conditions pending, the collected judgement calls, and Counsel's read."; "what proves off comes back as corrections" | -
    - A4 no documents, no audit | maps | inferred | extends "It audits against whichever documents exist." | -
    - A5 all cited-or-inferred counts as a "citing audit" | maps | inferred | extends "inferred (extends named tenets and is cheap to undo; proceed, journal, show at closeout)"; "a citing audit approves plans" | -
    - A6 candidate amendments go through Counsel; Orchestrator writes to neither philosophy | maps | cited | "Product philosophy: standing, changed only by the owner."; "A result ebigunso rejects, or an inferred call he confirms, yields a candidate amendment that he accepts or not in discussion." | -
    - A7 Worker sees tenets only through its packet | internal mechanics | not audited | - | -
    - A8 Reviewer's plan review runs before the audit | maps | inferred | extends "without one, ebigunso approves as today"; the brief's "The Reviewer's plan review still runs" is an unquoted tail and stated for this initiative only | -
    - A9 Codex peers reachable | internal mechanics | not audited | - | -
    - T1 Counsel skill and document forms | maps | cited | sections "What Counsel is", "How a conversation with Counsel should go", "Roles and sessions", "Counsel as contributor", "Documents, in the target repository" | -
    - T2a Counsel agents for Copilot and Claude, role registered, Researcher-only dispatch | maps | cited | "runtime name `harness-counsel`"; "may dispatch read-only Researchers for facts" | -
    - T2b Codex Counsel entered by invoking the skill, no agent | maps | inferred | extends "The session you open sets the altitude." | -
    - T3 record drafts, each accepted by the owner on its own | maps | inferred | as P2 | -
    - T4 value-audit mandate and the rename | maps | cited | "Value audit" section; "An irreversible or outward-facing action stops and comes back to him through Counsel even when the brief or a philosophy covers it" | -
    - T5 package validator covers Counsel agents | internal mechanics | not audited | - | -
    - T6 audit in the run, escalation, standing approvals | maps | cited | "cited (a tenet or the brief covers it; proceed); inferred (...; proceed, journal, show at closeout); ask-now"; "Stopping on something the documents already answer is also a defect."; "A review loop that does not converge is treated as evidence against the brief and becomes a value question."; "its home is the repository rule files" | -
    - T7a closeout as candidate ready: behaviour first, reasoned detail, what was learned, pending human-only conditions, Counsel's read | maps | cited | "It leads with behaviour."; "Implementation detail is allowed when your judgement needs it, with the reason stated."; "It also reports what was learned that the philosophies don't account for."; "A proxy never stands in for a human-only condition."; "formed before seeing the auditor's verdict" | -
    - T7b closeout and the note to Counsel show only the judgement calls and inferred items that bear on direction; the full list stays in the plan | maps | inferred | extends "What comes to ebigunso is limited to what needs a decision at the level of the product or engineering philosophy" and "the collected judgement calls". Line 129 states it directly but has no ratification record in range. | -
    - T8 live dispatch; landing accepted records only on the owner's yes for each | maps | cited | "Each decision record is still accepted on its own." | -
    - T9 record for plan approval by a citing audit | maps | cited | "The change to plan approval needs its own decision record, accepted by you separately." | -
    - T10 the plan-approval conditional | maps | cited | "One conditional inside plan mode, not a third lifecycle."; "With only engineering guidelines, it audits that side and plans are approved by ebigunso as today."; "Ratifying a brief takes an act of the owner, not a line in a file." | -
    - DL1 requirement challenge, cuts | internal mechanics | not audited | - | -
    - DL2 record proposals 1 to 7 | maps | inferred | as P2 | -
    - DL3 ratification reaches the Orchestrator by quoted relay | maps | cited | "The act happens in Counsel's session, and Counsel relays it to the Orchestrator quoting the owner's words." | -
    - DL4 plan review round 1 applied | internal mechanics | not audited | - (pull-request delivery is graded at P1) | -
    - DL5 relayed waiver held until the owner confirms in the Orchestrator session | maps | cited | "Counsel's relay carries his decisions to an Orchestrator session only after he has himself told that Orchestrator to accept Counsel's relays as his." | -
    - DL6 round 2 applied: relay record, pointer location | maps | inferred | as P7 and P2 | -
    - DL7 round 3 applied: Proposal 7 tightened | maps | cited | as DL5 | -
    - DL8 execution authorized; Counsel as carrier | maps | cited | "Plan approval is waived for this initiative only."; "Two checkpoints stay with ebigunso and reach him through Counsel". The owner's statement in the Orchestrator session is the plan's claim; the grade rests on the brief. | -
    - DL9 Wave 1 rulings | maps | inferred | extends "it is advisable to get advice from GPT models as well" (generalized to a model of another family); "Which model Counsel runs on is the owner's choice" | -
    - DL10 proposals 2, 6 and 8 not admitted; standing-approval home; Wave 2 rulings | maps | inferred | extends "Decision records (ADRs) stay for architectural forks"; "its home is the repository rule files" | -
    - DL11 second-review rulings and the narrowing of what reaches the owner | maps | inferred | the narrowing is covered by "What comes to ebigunso is limited to what needs a decision at the level of the product or engineering philosophy"; the Orchestrator rulings extend "he accepts it himself before it takes effect"; "One conditional inside plan mode" | -
    - DL12 verdict acted on: push and pull request held; stack brought to the owner as one | maps | cited | "An irreversible or outward-facing action stops and comes back to him through Counsel"; "The unit he accepts is a stack of pull requests that together ship something he can judge, not each pull request on its own." | -
    - C1 `counsel` skill; `harness-counsel` agents for Copilot and Claude; Codex by explicit skill invocation | maps | cited | "The role is named Counsel; runtime name `harness-counsel`."; "Counsel and the Orchestrator are separate sessions."; "Its limit is the level it works at, behaviour and decisions, not the occasions it may be used on." | -
    - C2 Copilot Counsel holds terminal and file-edit tools; the reading limit is a stated rule in every runtime | maps | inferred | as N5 | -
    - C3 Counsel takes engineering advice from "a model of another family" | maps | inferred | extends "it is advisable to get advice from GPT models as well, brought into the discussion marked with its source"; the owner's wording is generalized | -
    - C4 Counsel's read of a result takes its facts from the Orchestrator's note and, where needed, a Researcher; it goes to the owner and the Orchestrator | maps | inferred | extends "an independent read when a result is presented for human judgement, formed before seeing the auditor's verdict. That read is advisory and quotes its source."; "Counsel never reads plans, diffs or code" | -
    - C5 with no peer channel, the hand-over and every answer reach the Orchestrator as the owner's own statement in its session | maps | inferred | extends "Ratifying a brief takes an act of the owner, not a line in a file."; "only after he has himself told that Orchestrator to accept Counsel's relays as his". In that setup it sits against "As owner, ebigunso does not need to type into the Orchestrator session." | -
    - C6 `counsel/references/value-documents.md`: forms, locations, who changes and reads each, ratification record beside each amendment | maps | cited | "Documents, in the target repository"; "The auditor never reads them."; "A change to any of them reaches him through Counsel with a link to the document itself" | -
    - C7 Researcher contract in three copies: dispatching session named, Counsel report at behaviour and decision level | maps | cited | as P6 | -
    - C8 on-condition in `orchestration-harness/SKILL.md`: plan-mode runs only; a file merely present turns nothing on; an unratified hand-over turns nothing on | maps | inferred | extends "One conditional inside plan mode, not a third lifecycle."; "Ratifying a brief takes an act of the owner, not a line in a file." | -
    - C9 audit positions, template-only dispatch, acting on each grade, never altering a grade | maps | cited | "Fresh context each time; inputs are the documents that exist and the artifact under review, read from disk, never the Orchestrator's summary."; "It runs by position"; the three grade definitions; "called by the closeout value audit, not by the Orchestrator about its own work" | -
    - C10 an answered ask-now returns as an amendment Counsel writes; plan approval never answers an ask-now | maps | inferred | extends "They grow from what each initiative forces into words and from verdicts on results."; "Cementing is ebigunso's act." | -
    - C11 asking the owner: direction-level questions only, reserved acts still reach him, documents searched first, no judgement of product phase | maps | cited | "What comes to ebigunso is limited to..."; "Stopping on something the documents already answer is also a defect."; "Skipping a decision that needed to reach you is a harness failure to be fixed."; "Autonomy comes from the decisions documented; where none is documented, that is the gap. No separate judgement of product phase sets it." | -
    - C12 the carrier: escalation to Counsel, relay admitted only after the owner's statement, consent gates keep their terms, plan approval not carried by relay | maps | cited | "it escalates to Counsel, and Counsel brings it to him"; "only after he has himself told that Orchestrator to accept Counsel's relays as his"; "Plans are presented only by the Orchestrator session, never relayed by Counsel."; "Counsel relays a merge only with his exact words naming that pull request" | -
    - C13a standing approvals live in `common.md`, reach the owner with the file path, take effect on his acceptance | maps | cited | "what I approve for all future runs should probably hold, and that I think the home would be the repository rule files."; "he accepts it himself before it takes effect" | -
    - C13b a standing approval never discharges a merge, a record acceptance, a philosophy change, plan approval or another standing approval | maps | inferred | extends "Merges happen only on your explicit instruction for each pull request."; "Each decision record is still accepted on its own."; "changed only by the owner". Read beside "How loose merging may be is a per-repository matter for that repository's rule files." | -
    - C13c a standing approval is not in effect in the run that adds it | maps | inferred | extends "what I approve for all future runs"; "he accepts it himself before it takes effect" | -
    - C14a mandate: three grades, scope test, proxy rule, audit on whichever side has a document | maps | cited | "Three grades: ..."; "Scope test: each user-facing item maps to the brief, is internal mechanics, or is scope expansion that escalates."; "A proxy never stands in for a human-only condition."; "It audits against whichever documents exist." | -
    - C14b mandate: the "nobody using the product could observe" test for sides; a standing-approval item graded cited on the approval | maps | inferred | extends the scope test and "That standing approval holds" | -
    - C15a closeout under a brief: candidate ready, behaviour first, evidence, pending human-only conditions, what was learned | maps | cited | as T7a | -
    - C15b Counsel's read may be reported as pending without holding back candidate ready; the plan's own status stays `done` | maps | inferred | extends "Closeout reports \"candidate ready\": ... and Counsel's read."; "an independent read when a result is presented for human judgement" | -
    - C16 the note to Counsel never carries the verdict | maps | cited | "formed before seeing the auditor's verdict" | -
    - C17 a run audited on a philosophy alone keeps done or blocked and lists its direction-bearing inferred items | maps | inferred | extends "With only engineering guidelines, it audits that side and plans are approved by ebigunso as today." | -
    - C18 wrong stop or skipped decision triggers the improvement loop | maps | cited | "Skipping a decision that needed to reach you is a harness failure to be fixed."; "Stopping on something the documents already answer is also a defect." | -
    - C19 a decision record's why names the statement served | maps | cited | "Decision records (ADRs) stay for architectural forks; the why names the tenet served." | -
    - C20 a rejected result or confirmed inferred call goes to Counsel as a candidate amendment, never into a repo rule | maps | cited | "yields a candidate amendment that he accepts or not in discussion" | -
    - C21 a review loop at its third bounce under a brief becomes a value question | maps | cited | "A review loop that does not converge is treated as evidence against the brief and becomes a value question." | -
    - C22 "existence audit" rename in five files | maps | inferred | as P5 | -
    - C23 ADR-D-0034 to ADR-D-0037 added with `status: proposed`; ADR-D-0023 and ADR-D-0032 still in place, nothing retired | maps | cited | "Each decision record is still accepted on its own."; "A change to any of them reaches him through Counsel with a link to the document itself" | -
    - C24 package validator entries, manifests at 0.22.0, adapter-sync and checklist lines, four lessons entries, the "decision records proposed" line synced into the two Orchestrator agents | internal mechanics | not audited | - | -
    - `Human-only conditions pending: "You judge it through first real use on Character Memory, and what proves off comes back as corrections."; "He checks behaviour before anything ships. The unit he accepts is a stack of pull requests that together ship something he can judge, not each pull request on its own."` The brief marks no pass condition agent-checkable or human-only; these are the two statements that read as his judgement of the result. No plan item or change lets a proxy settle either.
  - Auditor's remarks outside the record: 41 cited, 31 inferred, 1 ask-now, 11 not audited, none ungraded; the irreversible-or-outward-facing test ran on every item and caught only P1. Still needing the owner for this stack, as reserved acts under their own gates and so listed and not graded: acceptance of each of ADR-D-0034 to ADR-D-0037, the Task_9 record and the retirement of ADR-D-0032, the merge instruction naming the stack's pull requests, and the two human-only judgements. Inferred items the auditor thinks bear on direction: C5 (without a peer channel the owner types in the Orchestrator session), C13b (a standing approval can never cover a merge), C13c (a standing approval does not apply in the run that adds it), C4 (Counsel's read rests on the Orchestrator's note unless a Researcher is dispatched), C3 ("GPT models" became "a model of another family"), C8 (goal-mode runs are never audited), A5 (inferred grades count toward a citing audit), C15b (candidate ready may be reported before Counsel's read exists). `Changes since` named main, so the whole brief was in range; the landed procedure commits the brief before recording the start revision, which this run predates. The plan's P1 reason quoted a brief line that the brief no longer contains, and several owner quotations in this plan are as Counsel relayed them and differ from the brief in contractions; the brief carries his exact words. The brief marks no pass condition agent-checkable or human-only and traces to no product statement, which the value-documents reference asks of a brief; that is Counsel's and the owner's. The installed plugin (0.21.0) has no mandate file; the dispatch resolved because this repository's working tree carries the skill.
  - Acting on the verdict: P1 (ask-now) holds the push and the pull requests until the owner answers; the question is with him through Counsel. The 31 inferred items are journaled here; the eight above are the ones shown at closeout. Reachability claimed: the plan-draft and closeout positions, with the fixed template and nothing added; the wave-boundary position was not exercised.

- 2026-09-30 Wave 3 (Task_8), first pull request opened: https://github.com/ebigunso/agent-harness/pull/72, branch `feature/2026-09-30/value-level-operation` at the commit that moved proposed ADR-D-0038 to the second pull request's branch. Opened on the owner's answer logged in the Decision Log against item P1; no merge is requested. Validation on the pushed head: `validate_harness_package.py` passed, `run_validation_smoke_tests.py` exit 0, plan validator passed, `git diff --check` clean, no machine-specific path in any commit of the branch. Review monitoring armed with the bundled watcher. Still open in Task_8: the owner's acceptance of ADR-D-0034 to ADR-D-0037 and the retirement of ADR-D-0023 if ADR-D-0035 is accepted. The second pull request needs the `gh stack` extension, which is not installed on this machine; permission to install it was asked of the owner through Counsel.
- 2026-10-02 Closeout audit of the run (live audit dispatch 3, closeout position), after the second pull request's content was committed locally at 2eb21b6. Dispatch text, verbatim: "You are the value auditor. Read references/value-audit-mandate.md of the orchestration-harness skill and follow it exactly. Position: closeout. Plan: docs/coding-agent/plans/active/value-level-operation-plan.md. Governing brief: docs/coding-agent/briefs/value-level-operation-brief.md. Changes since: 972793b." Dispatched to a Claude Reviewer-profile subagent with fresh context. Verdict as returned:

  ## Value audit verdict: closeout, value-level-operation plan

  The dispatch matched the fixed template with nothing added, so the audit was graded. Two items are `ask-now`; nothing is `ungraded`. A value audit verdict grades and approves nothing.

  ### Verdict record

  - `Position: closeout`
  - `Documents read: docs/coding-agent/briefs/value-level-operation-brief.md; docs/coding-agent/rules/common.md ("Repository Reference Documents" pointer lines and "Standing Approvals" only)`. Instructions read: the mandate and `counsel/references/value-documents.md`. Artifact read: the plan file whole, and `git diff 972793b` to the working tree with the notes exclude pathspec on every content command. HEAD is 2eb21b6, the tree is clean, and the only untracked path is `.claude/`, which predates the range and was not opened.
  - `Product basis: brief in the product owner's words`. No product philosophy pointer exists in `common.md`. The brief has no labelled basis line; I read the basis from line 3 ("ratified by ebigunso on 2026-09-30 (...)") and line 12 ("You (ebigunso), as owner of a product built with agents.").
  - `Not audited: engineering side, no engineering philosophy (no pointer line in common.md)`
  - `Missing inputs: none`. Revision 972793b resolves; the brief carries its ratification record at line 3.
  - `Value documents changed in range: docs/coding-agent/briefs/value-level-operation-brief.md. No pointer line added, removed or changed.`
  - Counted as support, each carrying quoted words with a date: lines 40, 63, 64, 65, 66, 85, 86, 87, 88, 95, 98, 121, 133, 139, and lines 143 and 144, which gained their confirmation quotes in range.
  - Not relied on alone: line 84 (reworded by deletion, no record), line 99 (reworded, no record) and the unquoted tail of line 66.
  - `common.md` is not a value document, but its whole "Standing Approvals" section, both entries, was added inside the range. By the mandate neither entry is in effect for this audit.

  Item lines use the mandate's five fields. "Lnn" is the brief's line number.

  **Plan: Definition of Done**
  - DoD1 Counsel session in three runtimes | maps to the brief | cited | L82 "The role is named Counsel; runtime name `harness-counsel`."; L83 "Counsel and the Orchestrator are separate sessions. The session you open sets the altitude." | -
  - DoD2 four document types, one form, location and reading rule each | maps | cited | "Documents, in the target repository" L113-119 | -
  - DoD3 Orchestrator reads documents, audits at three positions, escalates to Counsel, closes "candidate ready" | maps | cited | L128 "It runs by position: plan draft, each wave boundary, closeout."; L93 "it escalates to Counsel, and Counsel brings it to him"; L145 "Closeout reports \"candidate ready\""; L46 "It leads with behaviour." | -
  - DoD4 a citing audit authorizes plan execution only after its record is accepted | maps | cited | L138 "With a ratified brief, a citing audit approves plans; without one, ebigunso approves as today."; L59 "The change to plan approval needs its own decision record, accepted by you separately." | -
  - DoD5 no value documents, behaviour as before | maps | inferred | extends L132 "It audits against whichever documents exist."; L138 "without one, ebigunso approves as today" | -
  - DoD6 contradicted records replaced, each accepted on its own | maps | cited | L116 "Each decision record is still accepted on its own." | -
  - DoD7 validators, Reviewer approval, no merge without instruction | maps | cited | L58 "Merges happen only on your explicit instruction for each pull request." | -

  **Plan: planner-added requirements**
  - P1 delivery as two stacked pull requests: publishing the branches and opening the pull requests | maps | ask-now | L38 "An irreversible or outward-facing action stops and comes back to him through Counsel even when the brief or a philosophy covers it; a brief covers the intent, not the moment."; L66 "A finished, reviewed run may publish its branch and open the pull request before his approval; the merge still waits for him." covers the intent | Reason: outward-facing, and no standing approval is in effect because the `common.md` entry was added inside the audited range. That test is the only reason. State found: the first branch is on the remote at f0bc8a0; the second branch `feature/2026-10-02/plan-authorized-by-ratified-brief` (2eb21b6) is not on the remote. Question: your answer of 2026-09-30 let a finished, reviewed run publish its branch and open the pull request before your approval. Does it cover publishing the second branch of this stack and opening its pull request now, or do you want to be asked at that moment?
  - P2 decision records beyond the one the brief names (nine in all) | maps | inferred | extends L120 "Decision records (ADRs) stay for architectural forks"; L116 | -
  - P3 fixed dispatch template, logged verbatim | internal mechanics | not audited | - | -
  - P4 brief path recorded in the plan and named in each dispatch | internal mechanics | not audited | - | -
  - P5 older "value audit" renamed "existence audit" | maps | inferred | extends the "Value audit" section L125-134 | -
  - P6 Researcher contract names the dispatching session; behaviour-level report for Counsel | maps | cited | L21 "For a check-up it learns the project's state through a read-only Researcher reporting at that level." | -
  - P7 philosophies found only by `common.md` pointer lines; on/off condition | maps | inferred | extends L132; L113 "Product philosophy: standing, changed only by the owner." | -
  - P8 escalation transport; a file line is never his answer; without a peer channel the answer is his own statement in the Orchestrator session | maps | inferred | extends L93; L92 "Ratifying a brief takes an act of the owner, not a line in a file."; sits against L93 "ebigunso does not need to type into the Orchestrator session" | direction
  - P9 live dispatch as closeout evidence | internal mechanics | not audited | - | -
  - P10 one version bump per pull request | internal mechanics | not audited | - | -
  - P11 missing, malformed or partly graded verdict authorizes nothing | maps | inferred | extends L138; L36 "Skipping a decision that needed to reach you is a harness failure to be fixed." | -

  **Plan: non-goals**
  - N1 persona voices, nested orchestration, directory memory | maps | cited | "Left out on purpose" L149-151 | -
  - N2 no philosophy written for this repository or Character Memory | maps | cited | L113; L73 "No engineering guidelines exist for the harness yet." (provisional) | -
  - N3 no trial of Counsel before shipping | maps | cited | L52 "It ships as a first version. No trial on a development build is required first." | -
  - N4 no grade validators, report fields, rule file, templates, Codex loader change | internal mechanics | not audited | - | -
  - N5 Counsel's reading limit is a stated rule, not tool-enforced | maps | inferred | extends L85, L86 "Plans and diffs stay off limits to Counsel."; L52 | -

  **Plan: assumptions**
  - A1 under a ratified brief the owner's decisions travel through Counsel; without one he talks to the Orchestrator | maps | inferred | extends L93; L99 "anyone may talk to the Orchestrator session directly" (reworded in range, no record; not relied on alone) | -
  - A2 Worker judgement calls are choices inside the task | maps | cited | L141 "Workers make choices within the bounds of their task, and the Orchestrator settles what falls outside them ... No act-then-report." | -
  - A3 "candidate ready" is the closeout outcome under a brief | maps | cited | L145; L53 "what proves off comes back as corrections" | -
  - A4 no documents, no audit | maps | inferred | extends L132 | -
  - A5 all cited-or-inferred counts as a "citing audit" | maps | inferred | extends L129 "inferred (extends named tenets and is cheap to undo; proceed, journal, show at closeout)"; L138; L35 "Where a direction can be reasonably inferred from standing values, the run keeps going and reports it afterwards." | direction
  - A6 candidate amendments go through Counsel; the Orchestrator writes to neither philosophy | maps | cited | L113; L122 "yields a candidate amendment that he accepts or not in discussion" | -
  - A7 Worker sees tenets only through its packet | internal mechanics | not audited | - | -
  - A8 the Reviewer's plan review runs before the audit | maps | inferred | extends L60 "The Reviewer's plan review still runs" (stated for this initiative only); L140 | -
  - A9 Codex peers reachable | internal mechanics | not audited | - | -

  **Plan: tasks and the pull-request paragraph**
  - T1 Counsel skill and document forms | maps | cited | sections "What Counsel is", "How a conversation with Counsel should go", "Roles and sessions", "Counsel as contributor", "Documents, in the target repository" | -
  - T2a Counsel agents for Copilot and Claude, role registered, Researcher-only dispatch | maps | cited | L82; L84 "Counsel never dispatches Workers, and may dispatch read-only Researchers for facts." | -
  - T2b Codex Counsel entered by invoking the skill | maps | inferred | extends L83 | -
  - T3 record drafts, each accepted on its own | maps | inferred | as P2 | -
  - T4 value-audit mandate and the rename | maps | cited | "Value audit" section; L38 | -
  - T5 package validator covers Counsel agents | internal mechanics | not audited | - | -
  - T6 audit in the run, escalation, standing approvals | maps | cited | L129; L37 "Stopping on something the documents already answer is also a defect."; L140; L39 "its home is the repository rule files" | -
  - T7 closeout as candidate ready, showing only what bears on direction | maps | cited | L46; L47; L48; L131; L143 "a closeout shows him only those that bear on direction" (confirmed "Looks good.") | -
  - T8 live dispatch; landing accepted records only on the owner's yes for each | maps | cited | L116 | -
  - T9 record for plan approval by a citing audit | maps | cited | L59 | -
  - T10 the plan-approval conditional | maps | cited | L138 "One conditional inside plan mode, not a third lifecycle."; L92 | -
  - PR merge of the stack, stated as waiting for his acceptance naming the stack and each pull request | maps | ask-now | L58; L62 "The unit he accepts is a stack of pull requests that together ship something he can judge"; L63 | Reason: outward-facing, and no standing approval covers a merge here. That test is the only reason, and the plan states the action as waiting for the owner. Question: having seen what this stack does, do you accept it and instruct the merge, naming each pull request?

  **Plan: Decision Log**
  - DL1 requirement challenge, cuts | internal mechanics | not audited | - | -
  - DL2 record proposals 1 to 7 | maps | inferred | as P2 | -
  - DL3 ratification reaches the Orchestrator by quoted relay | maps | cited | L92 | -
  - DL4 plan review round 1 applied | internal mechanics | not audited | - | -
  - DL5 relayed waiver held until the owner confirms in the Orchestrator session | maps | cited | L94 | -
  - DL6 round 2 applied: relay record, pointer location | maps | inferred | as P7, P2 | -
  - DL7 round 3 applied: Proposal 7 tightened | maps | cited | L94 | -
  - DL8 execution authorized; Counsel as carrier | maps | cited | L60 "Plan approval is waived for this initiative only."; L69. The owner's statement in the Orchestrator session is the plan's claim; the grade rests on the brief. | -
  - DL9 Wave 1 rulings ("a model of another family" for "GPT models") | maps | inferred | extends L96 "it is advisable to get advice from GPT models as well"; L97 | -
  - DL10 proposals 2, 6 and 8 not admitted; standing-approval home; Wave 2 rulings | maps | inferred | extends L120; L39 | -
  - DL11 second-review rulings; narrowing of what reaches the owner | maps | cited | L142; L41 "he accepts it himself before it takes effect" | -
  - DL12 verdict acted on; stack brought as one; records sent | maps | cited | L38; L62 | -
  - DL13 reading limit changed; Counsel on any runtime; plan-approval record drafted | maps | cited | L85; L86; L87; L88; L59 | -
  - DL14 owner's answer to P1; pending standing-approval entry; what a standing approval never discharges | maps | cited | L66; L41; L63; L64; L65 | -
  - DL15 standing approval accepted; local install of the stack extension | maps | cited | L41. The install is local tooling and not outward-facing. | -
  - DL16 Counsel serves the person directing the work; ADR-D-0034 split; three product bases | maps | cited | L98; L133 | -
  - DL17 further directions (one product-owner role, standing-approval authority, four terms, brief tagging, reading order), renumbering | maps | cited | L98; L40; L133. The brief-tagging rule is graded at C8. | -
  - DL18 a standing approval may cover a merge where the rule files allow it and the product owner gave it | maps | cited | L40 "a standing approval to merge in a repository they do not own is the product owner's to give"; L68 "How loose merging may be is a per-repository matter for that repository's rule files." | -
  - DL19 acceptances of ADR-D-0034 to ADR-D-0042 recorded one by one from Counsel's relays (ten entries) | maps | cited | L116; L94; L95. That each relay occurred and what it quoted is the plan's claim; no document carries it. | -
  - DL20 records do not quote the owner; reasons replace rulings; ADR-D-0034 back to proposed | maps | cited | L121 | -
  - DL21 ADR-D-0037 restated as an explicit act per runtime | maps | inferred | extends L83 "The session you open sets the altitude." | -
  - DL22 relays admitted by a standing approval naming Counsel's identity | maps | cited | L95 | -
  - DL23 plan-approval record split into three; sources stated for any mode; the audit marks direction | maps | cited | L139; L59. The marking is graded at C14. | -
  - DL24 two sources apply to any unit of work, goal-mode envelope included | maps | cited | L139 | -
  - DL25 second branch cut as a stack; ADR-D-0040 and ADR-D-0041 landed; ADR-D-0032 retired | maps | cited | L59; L62. A retirement is undone by reverting. | -
  - DL26 Task_10 done with the text of ADR-D-0040 to ADR-D-0042 | maps | cited | L138; conditions graded at C10 to C13 | -

  **Changes since 972793b**
  - C1 Counsel may do quick reads of code; plans and diffs off limits; a read is never a check on a run; no file list (skill, both agents, READMEs, matrix, checklist, ADR-D-0035) | maps | cited | L85; L86; L87; L88 | -
  - C2 a session role is entered by an explicit act per runtime: picker, `claude --agent` or project setting, or explicit skill invocation (READMEs, agents, SKILL.md, ADR-D-0037; ADR-D-0023 retired) | maps | inferred | extends L83; L82 | -
  - C3 Counsel serves the person directing the work; product owner defined; no product value inferred for an absent owner (skill, value-documents, run-side reference, ADR-D-0034, ADR-D-0036) | maps | cited | L98 | -
  - C4 three product bases; request as received graded cited only, never inferred; `Product basis` verdict line (mandate, value-documents) | maps | cited | L133 | -
  - C5 relays admitted by the owner's statement in the session or by a Standing Approvals entry naming Counsel's identity (skill, run-side reference, ADR-D-0038, `common.md` entry) | maps | cited | L95; L94 | -
  - C6 standing approvals: given by whoever holds the authority, entry records who gave it; may cover a merge only where the rule files allow it and the product owner gave it (mandate, run-side reference, value-documents, ADR-D-0039) | maps | cited | L40; L68 | -
  - C7 an accepted standing approval applies from the run after the one that adds it; in the adding run the action still comes to the owner | maps | inferred | extends L39 "what I approve for all future runs"; L41 | direction
  - C8 each brief statement tagged, with quoted words and date for anything told or accepted, written while drafting | maps | inferred | extends L6 (provenance tags); L92 | -
  - C9 two Standing Approvals entries added to `common.md` (publish and open pull requests; Counsel's identity as carrier) | maps | cited | L66; L95; L41 | -
  - C10 second source in the Plan Gate: under a ratified brief, after a closed plan review, a plan-draft verdict with every graded item cited or inferred authorizes execution without the owner reading the plan; the verdict is never presented as approval (SKILL.md, lifecycle-gates, both Orchestrator agents, status-model, plan-format, ADR-D-0040, ADR-D-0041; ADR-D-0032 retired) | maps | cited | L138; L59; L92. The inferred-counts reading is A5. | -
  - C11 a side with no document is not audited and does not block authorization, so internal mechanics start with no person and no audit having seen them | maps | inferred | extends L132; L73 "No engineering guidelines exist for the harness yet." (provisional) | direction
  - C12 an irreversible or outward-facing action the plan states as waiting for its decision does not count against authorization; the action still waits | maps | inferred | extends L38; L138 | direction
  - C13 the verdict covers the plan as it stands; later changes to what the plan decides need a later audit or the owner's approval; a non-converging review is not a closed review | maps | inferred | extends L127; L140 | -
  - C14 the auditor, not the Orchestrator, marks which inferred items bear on direction; the closeout shows those and no others, as the verdict states them (mandate, final-response contract, closeout, ADR-D-0042) | maps | inferred | extends L143; L67 "called by the closeout value audit, not by the Orchestrator about its own work" | direction
  - C15 the Orchestrator still selects which Worker choices and its own rulings bear on direction for the closeout; a direction it inferred at run time is reported as its ruling, never as an audit-graded item | maps | inferred | extends L143; L142 | direction
  - C16 the note to Counsel carries the audit's direction-marked items as the verdict states them, grade and statements included ("the one part of a verdict the note carries") | maps | ask-now | L91 "an independent read when a result is presented for human judgement, formed before seeing the auditor's verdict"; against L122 and L143, which need those items to reach him | Reason: the statements that bear on it conflict; Counsel now sees part of the verdict before forming its read. Question: when a run finishes, should Counsel form its read of the result before seeing any part of the audit's verdict, including the list of extensions the audit marked as bearing on direction, or may it see that list first?
  - C17 Counsel's read takes its facts from the Orchestrator's note and a Researcher, never from Counsel's own read of code | maps | inferred | extends L87 "never a check on a run's work"; L91 | direction
  - C18 the two sources apply to any unit of work; with no per-mode record the second source authorizes nothing in goal mode; value-level operation stays plan-mode only | maps | cited | L139 "apply to any unit of work the harness authorizes, a goal-mode envelope included ... Redefining goal mode as a longer-horizon mode stays a later initiative." | -
  - C19 `adr.md`: a rejected alternative states why it lost and never quotes the person; Revisit When names the premise, not the occasion | maps | cited | L121 | -
  - C20 `adr.md`: the form for a premise not yet exercised | maps | inferred | extends L121 | -
  - C21 nine records set accepted (ADR-D-0034 to ADR-D-0042), renumbered and split; pointer repairs in ADR-D-0033, ADR-D-0002 and two completed plans | maps | cited | L116; L120 | -
  - C22 manifests at 0.23.0, status-model and plan-format wording, three lessons entries, checklist and matrix sync lines | internal mechanics | not audited | - | -

  - `Human-only conditions pending: "You judge it through first real use on Character Memory, and what proves off comes back as corrections."; "He checks behaviour before anything ships. The unit he accepts is a stack of pull requests that together ship something he can judge, not each pull request on its own."` The brief marks no pass condition agent-checkable or human-only; these two read as his judgement of the result. No item lets a proxy settle either.

  ### Remarks outside the record

  - **Totals:** 44 cited, 27 inferred (8 marked `direction`), 3 ask-now, 12 not audited, none ungraded. The irreversible-or-outward-facing test ran on every item and caught P1 and the merge.
  - **P1 and the merge:** each is `ask-now` only on the outward-facing test. The plan's Decision Log carries a quoted answer against P1, and the plan states the merge as waiting. Whether that Decision Log entry meets the repeated `ask-now` for the second, unpublished branch is the Orchestrator's to apply under the run-side procedure, not mine.
  - **C16 is the one new stop.** The text before this range already had the note carry inferred items; the change in range makes it explicit that verdict item lines reach Counsel before its read. The brief answers neither way.
  - **Marked `direction` for the closeout:** P8, A5, C7, C11, C12, C14, C15, C17. C11 rests on a statement the brief marks provisional (L73).
  - **Brief form gaps, for Counsel and the owner:** the brief has no labelled product-basis line, marks no pass condition agent-checkable or human-only, and traces to no product statement. `value-documents.md` asks for all three. I could determine the basis from lines 3 and 12, so I did not report it as a missing input.
  - **Stale plan text:** A1's source ("last three bullets") and its not-the-product-owner framing predate L98. The plan header still reads `last_updated: 2026-09-30`. The task text names ADR-D-0032 and ADR-D-0023 by their pre-retirement state.
  - **Not verifiable from documents:** every relayed acceptance (records, standing approvals) and the owner's session statement admitting relays are the plan's claims. The grades rest on the brief only.
  - **Installed plugin:** the cached plugin is 0.21.0 and has no mandate file; the dispatch resolved only because this repository's working tree carries the skill.

  ### Lesson candidate

  - category: value documents
  - deviation: the governing brief lacks a labelled product-basis line and agent-checkable/human-only marks, so each auditor has to derive them.
  - root_cause: the brief was ratified before `value-documents.md` required them, and was amended without adding them.
  - prevention: Counsel adds the basis line and the marks as a ratified amendment before the next run under this brief.
  - promotion_target: residual_risk

  How the Orchestrator applied it: (P1) `ask-now` on the outward-facing test alone; the owner's answer of 2026-09-30 to this same item, recorded in the Decision Log ("Yes, pull requests can be opened before approval."), was given for this plan's delivery as two stacked pull requests, so the second branch is published and its pull request opened on that answer; nothing merges. (Merge) waits for the owner's acceptance naming the stack and each pull request. (C16) a new stop: sent to Counsel as a value question; the text stays as committed and unmerged until answered. The eight `direction` items go in the closeout note as the verdict states them. The remarks on the brief's form go to Counsel.

## Decision Log (append-only; re-plans and major discoveries)

- 2026-09-30 Decision: requirement challenge on the brief before decomposition.
  - Trigger / new insight: Plan Gate existence challenge.
  - Plan delta (what changed): kept every brief item; cut from the first draft of scope a Counsel rule file, document template files, a new Worker report field, a `validate_closeout.py` change, validators for grades, and conversation probes (see Non-goals).
  - Tradeoffs considered: the wave-boundary and closeout audits double the Reviewer-profile dispatches under a brief; kept because the brief fixes the positions and the audit must not share the Reviewer's packet.
  - User approval: no (pending plan approval)
  - Record proposed: none
- 2026-09-30 Decision: decision-record proposals stated at plan time; each is drafted only if its admission test passes and is presented to the owner on its own.
  - Trigger / new insight: the brief contradicts accepted records.
  - Plan delta (what changed): Task_3, Task_8, Task_9.
  - Proposal 1: Counsel is a separate-session role at value altitude. Decision: value discussion is held by its own session, which never reads plans, diffs or code, never dispatches Workers and approves nothing. Constraint: no later change may give Counsel implementation reach or fold it into the Orchestrator session. Why: the session that settles what is wanted must not be the one that benefits from a convenient answer about how.
  - Proposal 2: replacement of ADR-D-0003. Decision: logical roles are stable and physical names namespaced, with the role set owned by the role map. Constraint: as ADR-D-0003, without fixing the set at four. Why: the accepted record enumerates four roles.
  - Proposal 3: replacement of ADR-D-0023. Decision: a session takes a harness role by the user explicitly selecting that role, never by automatic skill activation. Constraint: no support skill becomes an entry. Why: the accepted record allows no entry other than the Orchestrator.
  - Proposal 4: the value audit is a stateless Reviewer profile whose ask-now stops a run. Decision: it reads only the documents and the artifact from disk. Constraint: no later change may feed it the Orchestrator's account. Why: a verdict the audited party framed cannot release that party. May replace ADR-D-0033.
  - Proposal 5: replacement of ADR-D-0032. Decision: a plan is authorized by the user, or by a value audit against a brief the owner ratified in which every item is graded cited or inferred and none ask-now. Constraint: the Orchestrator, the request and a brief file's own text remain never a source of approval. Why: the owner's ratified grounds, checked by a party the Orchestrator cannot frame, carry the owner's authority to the plan.
  - Proposal 6: replacement of ADR-D-0022. Decision: the orchestration workflow's mechanics have one home, and Counsel's conduct has its own, neither restating the other. Constraint: no third home, and no adapter restating either. Why: the accepted record routes every adapter to `orchestration-harness`, which a Counsel session must not load.
  - Proposal 7 (added after plan review round 2): the owner's word reaches the Orchestrator directly or as Counsel's relay quoting it. Decision: a relay that quotes the owner carries his decision; Counsel's paraphrase, Counsel's own view and a file's text carry none. Constraint: no consent gate is loosened, only its carrier is added, and no later change may let an agent's unquoted account stand for the owner. Why: the owner works at value level in one session, and the session that needs his decision must be able to tell his words from an agent's.
  - User approval: no
  - Record proposed: seven proposals as above; all unaccepted
- 2026-09-30 Decision: owner ruling relayed by Counsel on how a brief's ratification reaches the Orchestrator.
  - Trigger / new insight: value question sent to Counsel; ruling quoted by Counsel: "Come back to me, but I should not need to type into the Orchestrator session directly. It should escalate, and the Counsel should bring it to me." The brief's "Roles and sessions" was amended by Counsel with two bullets.
  - Plan delta (what changed): ratification is the owner's act in the Counsel session, relayed quoting his words (Task_1, Task_9, Task_10); escalations go to Counsel, not to the owner in the Orchestrator session (Task_6); the growth loop is written by Counsel (A6, Task_1); escalation transport added to Planner-added requirements.
  - Tradeoffs considered: the relay-with-quote form is Counsel's reading and not yet confirmed by the owner; it is cheap to change until Task_9's record is accepted.
  - User approval: no (the ruling is on the brief, not on this plan)
  - Record proposed: none beyond Proposal 5
- 2026-09-30 Decision: plan review round 1 findings applied.
  - Trigger / new insight: Reviewer findings.
  - Plan delta (what changed): fixed template and verbatim logging, the two new records, and fail-closed listed as planner-added; the Codex loader line dropped in favour of explicit skill invocation and ADR-D-0022 moved from "stands" to contradicted with Proposal 6; `SKILL.md` outcome wording given to Task_6; "cited or inferred" stated as assumption A5; template fill-ins loosened to disk locations including the governing brief; record drafting moved to Wave 1 with retirements after acceptance; delivery reduced from three pull requests to two; `owns` entries made paths; brief items on decision records, Counsel's closeout note and decided cases given to tasks; the guideline-versus-rule assumption removed as unrequested.
  - Tradeoffs considered: two pull requests make the first one larger to review and save one version bump and one merge stop.
  - User approval: no
  - Record proposed: none
- 2026-09-30 Decision: a waiver of plan approval relayed by Counsel is not acted on until the owner confirms it in the Orchestrator session.
  - Trigger / new insight: Counsel relayed, quoting the owner: "Lets try going with the first option. I will then retroactively look at the plan and see if something was still off, and then I will discuss its implications."; the brief's "Limits on the run" was amended to say plan approval is waived for this initiative only.
  - Plan delta (what changed): none to tasks; execution is held (Open Questions Q1, Q2). Plan review continues.
  - Tradeoffs considered: acting on the relay would be the Orchestrator accepting, on another agent's word, the authority change this plan itself treats as needing a separately accepted record; holding costs the owner one line in this session.
  - User approval: no
  - Record proposed: none
- 2026-09-30 Decision: plan review round 2 findings applied.
  - Trigger / new insight: Reviewer findings; the hold on one relayed consent exposed that the plan routed the other consents (record acceptances, merges) through the same relay without saying so.
  - Plan delta (what changed): Proposal 7 added and drafted in Task_3, to be accepted before the first pull request; Q1 widened to ask the owner once, in the Orchestrator session, for the waiver and for relay as the carrier of his decisions in this initiative; Task_6 adds a carrier and changes no consent gate; the cited-or-inferred reading put into Proposal 5 and Task_9; standing documents located by `common.md` pointers instead of probed default paths; the Design alternative replaced by one the brief does not exclude; the audit artifact defined per position; provisional-tenet flag, plan review before the audit, and the Codex guard given to tasks; the engineering-guidelines drafter turned from an assumption into Q3.
  - Tradeoffs considered: pointer-only location means a repository without a rule suite gets no value-level operation until it has one.
  - User approval: no
  - Record proposed: Proposal 7, unaccepted
- 2026-09-30 Decision: plan review round 3 findings applied; Proposal 7 tightened; Proposal 8 stated; document forms wait on the brief.
  - Trigger / new insight: Reviewer delta findings; the Reviewer's observation that a runtime may refuse to treat any agent message as the user's consent; Counsel's heads-up that the brief's lines on the form of the product philosophy and the content of the engineering philosophy are under revision with the owner.
  - Plan delta (what changed): value-level operation is on when a governing brief was handed over or `common.md` points to a standing document; plan approval removed from the consents Task_6 gives the relay carrier; Task_3 also determines whether the relay record stands beside ADR-D-0032 and ADR-D-0017; Task_1 is dispatched only after Counsel amends the brief, and Task_4 takes document forms from Task_1's reference, so its form-dependent lines wait with it.
  - Proposal 7, as now proposed (replaces the wording in the entry above): Counsel's relay quoting the owner carries his decision to an Orchestrator session only after the owner has, in that session, named Counsel as his carrier for the initiative; without that statement a relay is an agent's message and carries nothing. Constraint and why as before, with this added why: the session relying on the owner's authority must have seen one act of his own.
  - Proposal 8 (conditional): replacement of ADR-D-0033, proposed only if Task_3 determines its pause-case invariant cannot stand beside the ask-now grade. Decision: within authorized work the Orchestrator pauses for the owner on the two cases ADR-D-0033 names and on an ask-now grade. Constraint: no other pause case is added without a record. Why: the accepted record fixes the pause cases at two. Proposal 4 does not itself replace ADR-D-0033.
  - Tradeoffs considered: the tightened Proposal 7 costs the owner one line per initiative in the Orchestrator session, against his wish not to type there; taken to Counsel as a value consequence.
  - User approval: no
  - Record proposed: Proposals 7 (amended) and 8 (conditional), unaccepted
- 2026-09-30 Decision: execution authorized; Counsel is the owner's carrier for this initiative; open questions closed.
  - Trigger / new insight: the owner's own statement in the Orchestrator session: "I confirm the decisions relayed to you through the Counsel, I'll interact with the Counsel and it will relay you what you need to know." The decisions relayed before it include the waiver of plan approval for this initiative ("Lets try going with the first option. I will then retroactively look at the plan and see if something was still off, and then I will discuss its implications.").
  - Plan delta (what changed): status in_progress. Q1 closed by that statement. Q2 closed by relay: "You bring it to me, but with a link to the document itself so I can actually read them, and not take your word for granted. I think ADRs, product philosophy, and the engineering philosophy, are the three things that I need to keep track of and object to if there is anything even slightly off."; each record goes to him on its own through Counsel with its path. Q3 closed by relay: "Counsel, most likely."; a second Counsel for engineering is undecided and not foreclosed. The brief's document section was amended (tenet form and one-page limit withdrawn; "engineering philosophy" replaces "engineering guidelines"); Task_1 is unblocked and the plan's wording follows.
  - Tradeoffs considered: none.
  - User approval: waived for this initiative by the owner (statement above); the two checkpoints, record acceptance and each merge, stay his.
  - Record proposed: none new
- 2026-09-30 Decision: Wave 1 rulings and the second brief amendment.
  - Trigger / new insight: Worker questions from Tasks 1, 2 and 4; Counsel's relay of the owner's rulings: on a closeout also reporting what was learned that the philosophies do not account for, "This seems like a good idea."; on the model Counsel runs on, "This is just me switching out models so it does not have to go into the harness."; "I will take your case and stay with one counsel. Engineering could still use help from GPT models so it is advisable to get advice from them too for that."; review occasions proposed by Counsel and accepted.
  - Plan delta (what changed): Task_1 keeps the hand-over content, the two recipients of Counsel's read and the amendment bullet, and carries one Counsel for both discussions with advice from a model of another family (no vendor named in harness text; inferred from "GPT models", shown at closeout). Task_2 owns extended to two `runtime-adapter-contract` files for the two-copy qualification; Copilot Counsel keeps terminal tools; the Researcher's Counsel report gains "what is open". Task_4 grades an irreversible or outward-facing item ask-now even when a document covers it (value question with the owner through Counsel); the mandate's length of 71 lines is accepted. Task_6 and Task_7 name the revisions the audit is given. Task_7 adds what was learned to the closeout and the never-dispatches-Counsel sentence to the Claude Orchestrator agent.
  - Tradeoffs considered: keeping terminal tools on the Copilot Counsel leaves "never reads plans, diffs or code" a stated rule there.
  - User approval: waived for this initiative
  - Record proposed: none new
- 2026-09-30 Decision: outcome of the record proposals; owner rulings on stops; Wave 2 rulings.
  - Trigger / new insight: Task_3 admission tests and the ADR review; Counsel's relays of the owner's rulings.
  - Plan delta (what changed): Proposal 2 (replace ADR-D-0003) not admitted: its role list is not closed and its decision is about naming. Proposal 6 (replace ADR-D-0022) not admitted: under the reading already in force (the orchestration-harness skill and what it routes to) a `counsel` skill that the Stable Role Model routes to is inside it. Proposal 8 (replace ADR-D-0033) not admitted: its invariant covers the Orchestrator's own pauses for a discovery and leaves other consent gates to their records. Records going forward, once revised and re-reviewed: ADR-D-0034 (Counsel), ADR-D-0035 (role by explicit choice, replaces ADR-D-0023), ADR-D-0036 (value audit), ADR-D-0037 (relay). Each goes to the owner on its own through Counsel with its path.
  - Owner rulings relayed by Counsel, quoted: on an irreversible or outward-facing action that a document covers, "Yeah I agree with your assessment. Critical decisions should come back to me through the Counsel. But not for everything, what I approve for all future runs should probably hold, and that I think the home would be the repository rule files."; on a change that adds a standing approval reaching him with a link and taking effect on his acceptance, "Yes, I think that is sound."; on decision records, "You bring it to me, but with a link to the document itself so I can actually read them, and not take your word for granted."
  - Orchestrator rulings: standing approvals live under the heading "Standing Approvals" in `docs/coding-agent/rules/common.md`; the auditor's irreversible-or-outward-facing test runs on every item, including on a side with no document; an uncommitted or in-range standing approval is not in effect. Task_6 owns extended to a new reference `orchestration-harness/references/value-level-operation.md` (the run-side procedure, so `SKILL.md` carries only the condition and a pointer) and one line in `rulebook/references/rules-files.md`. Task_5: no role-map table parser and no new smoke test (neither is needed for this change). Task_7: a run audited without a brief lists its inferred items in the final response; an unanswered ask-now at closeout ends the turn blocked. Task_5 was given to a Claude Worker because the registered Codex peers show no placement record and their delivery could not be confirmed without the owner.
  - Tradeoffs considered: fewer records for the owner to read, against three standing records whose wording now reads slightly stale beside Counsel (a stale Context line in ADR-D-0003; "routes agents to that skill" in ADR-D-0022).
  - Value question put to the owner through Counsel: whether "judgement calls Workers made under ambiguity" means choices inside what the task decided (assumption A2, as built) or acting on undecided things and reporting afterwards, which would replace ADR-D-0033. (Answered later the same day for the first reading; see the next entry.)
  - User approval: waived for this initiative
  - Record proposed: ADR-D-0034, ADR-D-0035, ADR-D-0036, ADR-D-0037 proposed, unaccepted; Proposals 2, 6 and 8 not admitted
- 2026-09-30 Decision: second-review rulings and the owner's narrowing of what reaches him.
  - Trigger / new insight: Wave 2 review findings; ADR re-review findings; Counsel's relay of the owner's answer on Worker judgement calls: "Yeah I agree. Workers make choices within its bounds, and the Orchestrator settles things that fall out of them, that is unchanged. What should come to me is now more limited, only something that needs decisions on the product or engineering philosophy level that defines the direction of the product."
  - Plan delta (what changed): assumption A2 is confirmed by the owner and ADR-D-0033 stands. Closeout and the note to Counsel show only judgement calls and inferred items that bear on direction; the full list stays in this plan. Escalation to the owner is limited to direction-level questions and the acts he reserved.
  - Orchestrator rulings: a statement changed during a run counts as support only with the owner's ratification record beside it, and the run commits the brief before recording its start revision; the owner's answer to an ask-now comes back as a ratified amendment written by Counsel, and until then a repeated ask-now is met only by his answer quoted in the Decision Log against that item; plan approval never answers an ask-now; a pointer line changes only on the owner's word and a missing target is escalated; a standing approval covers only actions with no consent gate of their own and applies from the run after the one that adds it; value-level operation applies to plan-mode runs only; an unratified hand-over does not turn it on. Records: ADR-D-0035 and ADR-D-0037 declare their dependency on ADR-D-0034 and are presented only if it is accepted.
  - Tradeoffs considered: under the mandate's definition, opening a pull request is outward-facing, so a run under a brief asks before it unless a standing approval exists; left as the owner's rule says, and expected to surface in the live audit of this plan.
  - User approval: waived for this initiative
  - Record proposed: unchanged (ADR-D-0034 to ADR-D-0037, in revision)
- 2026-09-30 Decision: live audit verdict acted on; the owner's ruling on merges; records sent for acceptance.
  - Trigger / new insight: the plan-draft value audit of this plan (Progress Log) returned two ask-now items and showed that this plan's task text had not been amended when the brief was; Counsel's relay of the owner's ruling on merges: "I would want to check the behavior before things get shipped. Then it is probably better off to have me check before merge, but not in the form of approving every individual PR, rather as an accepted stack that ships something I can decide to accept or not."
  - Plan delta (what changed): pushing and opening a pull request wait for the owner's answer to the audit's value question (sent to Counsel). Task_1, Task_3, Task_6 and Task_7 text corrected to the amended brief, with acceptance naming brief statements instead of their positions. The two pull requests are brought to the owner as one stack. The four proposed records were sent to the owner through Counsel, each with its path, ADR-D-0034 first and ADR-D-0035 and ADR-D-0037 conditional on it.
  - Tradeoffs considered: asking before every pull request costs a stop per run in a repository where opening one is routine; a standing approval is the owner's instrument for that and the question offers it.
  - User approval: waived for this initiative
  - Record proposed: ADR-D-0034, ADR-D-0035, ADR-D-0036, ADR-D-0037 with the owner, unaccepted
- 2026-09-30 Decision: the owner changed Counsel's reading limit on reading ADR-D-0034; Counsel on any runtime; ADR-D-0038 drafted.
  - Trigger / new insight: Counsel's relays, quoting the owner: on ADR-D-0034, "Probably the boundary about you never reading code has gone too far. The engineering discussion may be better handled if the Counsel can do quick reads too. But grounding work that requires bulk code reads should still be delegated to a researcher."; asked whether plans and diffs stay off limits, "Yes."; on a quick read serving a discussion with him and never being a check on a run, "This one is reasonable."; declining a list of files read, "This one probably is just too much to bring up. I do not want to look at a list of files you read. That does not serve the discussion at hand."; and on runtimes, "Make it work both ways, if the Counsel session is with Claude or with Codex, or anything else for that matter. If it already reads that way then it is fine."
  - Plan delta (what changed): ADR-D-0034, the `counsel` skill, both Counsel agents, the READMEs and the capability matrix are revised to the new limit by their Workers (Task_1, Task_2, Task_3 deltas); the record goes back to the owner after the revision. Counsel already reads the same on every runtime; what differs by runtime (how the session is opened; the limits being stated rules) was sent to Counsel for the owner. Task_9's record is drafted as ADR-D-0038 and in review; it states the reading of "citing", that an unaudited side does not block, and that a plan containing an irreversible or outward-facing action is authorized by the user or states that action as waiting for the owner. Task_10 carries into the mandate that an action a plan states as waiting for the owner's decision does not block the audit's authority.
  - Tradeoffs considered: "quick" is left undefined beyond the owner's contrast with bulk grounding.
  - User approval: waived for this initiative
  - Record proposed: ADR-D-0034 in revision; ADR-D-0035, ADR-D-0036, ADR-D-0037 with the owner; ADR-D-0038 drafted, in review
- 2026-09-30 Decision: the owner's answer to the P1 ask-now (publishing the branch and opening pull requests); further answers; records.
  - Trigger / new insight: Counsel's relay of 2026-09-30, quoting the owner, after the owner's own statement in this session on 2026-09-30 to accept Counsel's relays ("I confirm the decisions relayed to you through the Counsel, I'll interact with the Counsel and it will relay you what you need to know.").
  - Against item P1 (ask-now at the plan-draft and closeout audits): asked whether a finished, reviewed run may publish its branch and open the pull request on its own in this repository as a standing approval, the owner answered on 2026-09-30: "Yes, pull requests can be opened before approval." P1 is released for this run: the branch is published and the pull requests are opened without asking again; merges are not covered and wait for the owner's acceptance of the stack.
  - Standing approval: an entry for later runs is written under "Standing Approvals" in `docs/coding-agent/rules/common.md` (commit b4fb8d1), marked pending and not in effect; it reaches the owner through Counsel with its path and takes effect for later runs only on his acceptance of the entry.
  - The owner's other answers, quoted: that a closeout shows only the Worker choices and Orchestrator rulings that bear on direction, "Looks good."; that his limit is about questions of judgement and the reserved acts still reach him, "Yes."; that stack acceptance applies in this repository with every pull request named in his acceptance, "Yes."; that a stack arrives with a way to run or observe it before merge, "Preferably yes, but it might not be possible every time, so I am not sure if you should state it that way." (a preference, not a gate); on how a rejected stack is fixed, "This is really just implementation details, and anything reasonable will work. I am not going to restrict how to handle things."
  - Plan delta (what changed): ADR-D-0038 was reviewed (NEEDS_REVISION, four MAJOR on its Decision wording) and revised on every finding; it is committed as proposed and goes to the owner after ADR-D-0036 and ADR-D-0037. The earlier ruling in this log that "a standing approval covers only actions with no consent gate of their own" is replaced by: a standing approval never discharges a merge, acceptance of a decision record, a change to a philosophy, plan approval, or acceptance of another standing approval. A delta re-review of the last fixes before the pull request opens returned NEEDS_REVISION with one MAJOR (this entry was missing) and small wording items in ADR-D-0038, the run-side reference and the Counsel skill, all applied. The closeout-position audit logged above ran at 972793b as the reachability exercise; the run's own closeout audit runs again when the second pull request is complete.
  - Tradeoffs considered: none.
  - User approval: waived for this initiative
  - Record proposed: ADR-D-0034 (final revision), ADR-D-0035, ADR-D-0036, ADR-D-0037, ADR-D-0038 with the owner, unaccepted
- 2026-09-30 Decision: the owner accepted the standing approval and allowed the stack extension.
  - Trigger / new insight: Counsel's relay of 2026-09-30, quoting the owner in reply to a message listing the gh-stack install, ADR-D-0034 and the standing-approval entry: "The common rule proposed, accepted. The gh-stack can be installed. I am still looking at the ADR. Await on that."
  - Plan delta (what changed): the entry under "Standing Approvals" in `docs/coding-agent/rules/common.md` records the acceptance with those words and the date; by the landed rule it applies from the run after this one. The `gh stack` extension is installed for the second pull request. ADR-D-0034 is unanswered; the records and the second pull request wait.
  - Tradeoffs considered: none.
  - User approval: waived for this initiative
  - Record proposed: unchanged
- 2026-10-01 Decision: the owner generalised whom Counsel serves, split ADR-D-0034, and ruled the audit's product basis.
  - Trigger / new insight: Counsel's relays of 2026-10-01 quoting the owner: "Yes, generalize it and have the Orchestrator revise 0034." (Counsel serves the person directing the work, whether or not that person owns the product; a product philosophy only where that person owns it; the brief traces to the philosophy where there is one and to the request as received where there is not; no product values inferred for an absent owner; product-level judgements go to that person to take to the requester; the engineering side unchanged; his reason: "it's still good to have as much delegation as possible to free up my attention."); on the shape of 0034: "in the current form the decision section has too little structure that it is hard to read." and "Yes, do the split and the list form."; on the audit's product basis, to the Orchestrator's question with Counsel's refinement: "Yes to the split, and take the refinement too." (a brief in the product owner's own words stands in for their values, graded including `inferred`; a request as received is `cited` only when it explicitly covers an item, never `inferred`, the rest goes to that person to take to the requester). None of these is an acceptance of a record.
  - Plan delta (what changed): ADR-D-0034 split into the core (0034) and ADR-D-0039 (Counsel's reach: quick reads, a read-only Researcher for bulk grounding, plans and diffs off limits, no Worker dispatch, consulted advice); all six proposed records (0034, 0039, 0035, 0036, 0037, 0038) use a Decision list of constraints and a short Invariant; "the person directing the work" replaces "the owner" wherever a record means that person; 0037 and 0038 renamed to match. The Counsel skill, the value-documents reference, the run-side reference and the mandate carry the generalisation with one convention (the person directing the work is called the owner in the text, the product owner where ownership is the point) and the three product bases, with a `Product basis` verdict line. Reviewed once with three small findings, all applied.
  - Tradeoffs considered: the brief's "Roles and sessions" line says "where there is no product philosophy" while its "Value audit" bullet refines that to "where that person does not own the product"; the landed text follows the refinement, and Counsel is asked to align the earlier line.
  - User approval: waived for this initiative
  - Record proposed: ADR-D-0034, ADR-D-0039, ADR-D-0035, ADR-D-0036, ADR-D-0037 (first pull request) and ADR-D-0038 (second), all proposed, unaccepted; to be brought to the owner in that order
- 2026-10-01 Decision: the owner's further directions on the records (second split, one role for product values, standing-approval authority, four terms, brief tagging, reading order) and the renumbering.
  - Trigger / new insight: Counsel's relays of 2026-10-01 quoting the owner: "I think we should split it further. A decision to introduce the Counsel role and what it is responsible for, and how philosophy documents should be handled are probably different decisions. Also, a product philosophy might be pre-existing even when the person directing the work is not the product owner themselves, so the wording about that part should probably be revised to match the reality as well."; on grading against a pre-existing philosophy the owner wrote, "Yes, I agree."; on five further points (one role for the product values, "the product owner", with "requester" dropped; standing approvals given by whoever holds the authority for the action, the entry recording who gave it, the person directing the work granting only within their own authority; the philosophy record independent of the Counsel record; four terms defined identically in each record and "user" replaced by "the person directing the work"; each brief statement tagged with the quoted words and date, written while drafting), "I think all five needs addressing." and "Go, send all five as my direction."; on order, "reorder the proposed ADRs so that a reader would encounter related content smoothly when reading one sequentially."; and on the renumbering after the Worker's script was refused by the permission check, "Go ahead with the renumbering." None is an acceptance of a record.
  - Plan delta (what changed): seven proposed records, renumbered in reading order and renamed with git by the Orchestrator: ADR-D-0034 the Counsel role and its responsibilities; ADR-D-0035 Counsel's reach into the work; ADR-D-0036 how the philosophy documents are handled (new; no dependency on 0034; 0039 depends on it); ADR-D-0037 how a session role is entered (supersedes ADR-D-0023); ADR-D-0038 how the word of the person directing the work reaches an Orchestrator session; ADR-D-0039 the Orchestrator never grades its own run (carries the standing-approval authority rule); ADR-D-0040 plan approval (supersedes ADR-D-0032; second pull request). The Counsel skill, the value-documents reference, the run-side reference, the audit mandate and `common.md` carry the product-owner role, pre-existing philosophies, the three product bases, the tagging rule and the standing-approval authority rule; the accepted standing-approval entry records that the repository's owner gave it. Reviewed once (one MAJOR: this entry was missing; three wording MINORs, applied).
  - Tradeoffs considered: "the owner" stays the short name for the person directing the work in the plugin text, with "the product owner" defined beside it, instead of renaming forty occurrences; the records use the full phrases.
  - User approval: waived for this initiative
  - Record proposed: ADR-D-0034, ADR-D-0035, ADR-D-0036, ADR-D-0037, ADR-D-0038, ADR-D-0039 (first pull request) and ADR-D-0040 (second), all proposed, unaccepted; brought to the owner in numerical order
- 2026-10-01 Decision: a standing approval may cover a merge where the repository's rule files allow it and the product owner gave it.
  - Trigger / new insight: the brief's "Stops during a run", amended with the owner's direction on who gives a standing approval, says a standing approval to merge in a repository the person directing the work does not own is the product owner's to give; the owner had already made merge looseness a per-repository matter for that repository's rule files. The Orchestrator's earlier ruling that a standing approval never discharges a merge over-reached.
  - Plan delta (what changed): the mandate, the run-side reference and ADR-D-0039 now say a standing approval never discharges acceptance of a decision record, a change to a philosophy, plan approval or acceptance of another standing approval, and may cover a merge only where that repository's rule files allow it and only when given by its product owner. In this repository none does: the owner withdrew free merging here.
  - Tradeoffs considered: none.
  - User approval: waived for this initiative
  - Record proposed: unchanged
- 2026-10-01 Decision: ADR-D-0034 accepted by the owner.
  - Trigger / new insight: Counsel's relay of 2026-10-01 quoting the owner: "I accept ADR-D-0034." (the record as announced final at 06:30 UTC).
  - Plan delta (what changed): ADR-D-0034's status set to accepted; it is the first record acceptance carried by relay on any runtime. ADR-D-0035 is with the owner next.
  - User approval: waived for this initiative
  - Record proposed: ADR-D-0034 accepted; ADR-D-0035 to ADR-D-0040 proposed
- 2026-10-01 Decision: records do not quote the owner; reasons replace rulings; ADR-D-0034 back to proposed for re-acceptance.
  - Trigger / new insight: the owner's corrections relayed by Counsel on 2026-10-01: a decline or ruling is not itself the reason for a decision, a reason behind it is always present; records do not quote his words, the reasons clearly stated are enough; the reason bulk code reading by Counsel was rejected (context filling, loss at compaction, pull away from the level of abstraction); the initiative name does not belong in a Revisit When.
  - Plan delta (what changed): all seven records revised; `durable-docs-authoring/references/adr.md` Form gains two rules (a ruling or decline is never the reason and the record does not quote the person; Revisit When names the premise, never the occasion); ADR-D-0034 returned to `status: proposed` and goes back to the owner first, then ADR-D-0035. Two reasons in ADR-D-0034 are the record's own rather than the owner's stated ones (nested orchestration: the authority-holding session would sit inside the working one; the non-owner alternative's second clause: direct talk returns that person to the level of plans) and are named to the owner with the record. Lesson recorded in `docs/coding-agent/lessons.md`.
  - User approval: waived for this initiative
  - Record proposed: ADR-D-0034 to ADR-D-0040 all proposed, unaccepted
- 2026-10-01 Decision: ADR-D-0034 re-accepted by the owner in its revised form.
  - Trigger / new insight: Counsel's relay quoting the owner: "I accept ADR-D-0034." (the revised record, reasons stated without quotes; the two record-own reasons were named to him and accepted with that known).
  - Plan delta (what changed): ADR-D-0034 status accepted. ADR-D-0035 is with the owner next.
  - User approval: waived for this initiative
  - Record proposed: ADR-D-0034 accepted; ADR-D-0035 to ADR-D-0040 proposed
- 2026-10-01 Decision: ADR-D-0035 accepted by the owner.
  - Trigger / new insight: Counsel's relay quoting the owner: "I accept ADR-D-0035."
  - Plan delta (what changed): ADR-D-0035 status accepted. ADR-D-0036 is with the owner next.
  - User approval: waived for this initiative
  - Record proposed: ADR-D-0034, ADR-D-0035 accepted; ADR-D-0036 to ADR-D-0040 proposed
- 2026-10-01 Decision: ADR-D-0036 accepted by the owner.
  - Trigger / new insight: Counsel's relay quoting the owner: "I accept ADR-D-0036." Accepted as written; Counsel had noted that its brief-traces-to line names two grounds (a product philosophy; the request as received) and not the third (the product owner's own ratified brief where no philosophy exists), and the owner asked for no change.
  - Plan delta (what changed): ADR-D-0036 status accepted. ADR-D-0037 is with the owner next.
  - User approval: waived for this initiative
  - Record proposed: ADR-D-0034 to ADR-D-0036 accepted; ADR-D-0037 to ADR-D-0040 proposed
- 2026-10-01 Decision: ADR-D-0037 revised after the owner found its runtime premise false.
  - Trigger / new insight: the owner, relayed by Counsel: "I have found out that Claude Code only accepts custom agent definitions as main session, when using the CLI and launching with a specific option. Claude Code Desktop app does not support this. The grounds this ADR stands on has been proven false, so it needs revision." Checked against the Claude Code documentation on 2026-10-01: a whole session runs as a custom agent by `claude --agent <name>` or the `agent` project setting; the docs list the desktop app as a surface for the setting, the owner observed the desktop app did not honour it; Claude Code has no per-session agent picker.
  - Plan delta (what changed): ADR-D-0037 restated as "a session role is entered by an explicit act of the person opening the session" (an agent picker; a launch option or project setting that runs the role's agent; or explicit invocation of the role's skill), file renamed; both READMEs and the Claude agent files state the act per runtime with the exact commands and the skill fallback; `orchestration-harness/SKILL.md` says "selecting or launching". The Orchestrator on a surface with no launch option enters by explicitly loading the `orchestration-harness` skill, which ADR-D-0020 already governs; no new record.
  - User approval: waived for this initiative
  - Record proposed: ADR-D-0034 to ADR-D-0036 accepted; ADR-D-0037 revised, with the owner next; ADR-D-0038 to ADR-D-0040 proposed
- 2026-10-01 Decision: ADR-D-0037 accepted; ADR-D-0023 retired.
  - Trigger / new insight: Counsel's relay of 2026-10-01 quoting the owner: "I accept ADR-D-0037." Counsel added that the project `agent` setting pins every session to one role and that the owner asked for no change there.
  - Plan delta (what changed): `ADR-D-0037-a-session-role-is-entered-by-an-explicit-act-of-the-person-opening-it.md` set to `status: accepted`; ADR-D-0023 set to `status: superseded`, given the retirement header line, and moved to `superseded/ADR-D-0023-the-harness-is-entered-by-selecting-the-orchestrator--superseded-by-ADR-D-0037.md`; the `supersedes` pointer in ADR-D-0037 and the `superseded_by` pointer in the retired ADR-D-0002 repaired; absence search for the old filename clean; the stray pre-revision file `ADR-D-0037-a-session-role-is-entered-by-selecting-its-agent.md`, left tracked by the rename at 31c2fe2, removed. Validator passed.
  - Tradeoffs considered: none.
  - User approval: the owner's acceptance of the record, relayed by Counsel
  - Record proposed: ADR-D-0037 accepted; ADR-D-0038, ADR-D-0039 and ADR-D-0040 still proposed
- 2026-10-01 Decision: relays may be admitted by a standing approval naming Counsel's identity, not only by a statement in each session.
  - Trigger / new insight: Counsel's relay of 2026-10-01 quoting the owner on ADR-D-0038, not an acceptance: "Go with the standing approval, send it to the Orchestrator." The owner found the per-session statement means typing into every Orchestrator session after a restart, and noted the misquoting risk is the same with or without it; Counsel proposed keeping what the statement buys (naming who may speak for the owner; a reason for the runtime to act on an agent message) through a standing approval in the rule files that names the Counsel identity and is read at every session start.
  - Plan delta (what changed): ADR-D-0038 revised in its Decision (two ways to admit relays; the impersonation risk under the standing approval stated and accepted by the person directing the work), Why, the rejected alternative on counting from the first message, Decision Boundary, Validation and Revisit When (relayed acceptances exercised 2026-10-01 on ADR-D-0034 to ADR-D-0037; a relayed merge and a standing-approval-only admission not yet). A pending Standing Approvals entry added to `docs/coding-agent/rules/common.md`: relays from the agmsg identity `agent-harness-counsel` quoting the person directing the work carry that person's decisions to an Orchestrator session; given by ebigunso; pending acceptance. The Counsel skill and the run-side reference (The Carrier) say relays are admitted either way. ADR-D-0039 and ADR-D-0040 carry no per-session statement wording (checked). The brief's new line under Stops during a run is Counsel's.
  - Tradeoffs considered: the entry is not in effect for this run (added during it), and this session already holds the owner's statement, so nothing changes for the run in progress.
  - User approval: waived for this initiative; the entry itself waits for the owner's acceptance
  - Record proposed: ADR-D-0038 revised, proposed, unaccepted
- 2026-10-01 Decision: ADR-D-0038 and the relay standing approval accepted.
  - Trigger / new insight: Counsel's relay of 2026-10-01 quoting the owner: "I accept ADR-D-0038 and the standing approval entry." The record is ADR-D-0038 as revised in 7383168; the entry is the Standing Approvals bullet in `docs/coding-agent/rules/common.md` naming `agent-harness-counsel` as carrier.
  - Plan delta (what changed): ADR-D-0038 set to `status: accepted`; the entry now records the giver, the quoted words and the date. The entry is not in effect for this run, which already holds the owner's statement in this session.
  - Tradeoffs considered: none.
  - User approval: the owner's acceptance of the record and the entry, relayed by Counsel
  - Record proposed: ADR-D-0038 accepted; ADR-D-0039 and ADR-D-0040 still proposed
- 2026-10-01 Decision: ADR-D-0039 accepted.
  - Trigger / new insight: Counsel's relay of 2026-10-01 quoting the owner: "ADR-D-0039 is accepted." The record as pushed in d881563.
  - Plan delta (what changed): `ADR-D-0039-the-orchestrator-never-grades-its-own-run-against-the-value-documents.md` set to `status: accepted`. The six records of the first pull request are now all accepted; ADR-D-0040 is brought to the owner next.
  - Tradeoffs considered: none.
  - User approval: the owner's acceptance of the record, relayed by Counsel
  - Record proposed: ADR-D-0039 accepted; ADR-D-0040 still proposed
- 2026-10-01 Decision: ADR-D-0040 split into three records; the sources of authorization stated mode-neutrally.
  - Trigger / new insight: Counsel's relay of 2026-10-01 quoting the owner on ADR-D-0040, not an acceptance: "This probably should be split into multiple ADRs. And, the case about goal mode applies here too." Counsel proposed a split by the retirability test (sources; plan-mode conditions; extensions at closeout) and, on its own point not yet answered by the owner, that the audit rather than the Orchestrator marks which extensions bear on direction; Counsel's reading of the goal-mode remark, unconfirmed, is that the sources record covers any unit of work the harness authorizes, goal-mode envelope ratification included, while goal mode's redefinition stays a later initiative.
  - Plan delta (what changed): three proposed records replace the draft, all untracked on this machine until accepted and destined for the second pull request: ADR-D-0040 the two sources of authorization and what is never one, for a non-trivial unit of work in any mode (supersedes ADR-D-0032; per-mode conditions left to their own records; where none states them for a mode the second source authorizes nothing there); ADR-D-0041 the conditions under which a ratified brief authorizes a plan in plan mode (governing brief and ratification reached; review closed; audit grades all and holds nothing; two sides; side without a document; irreversible test; verdict binds the plan as it stands; missing or partial verdict authorizes nothing; held items wait; an action stated as waiting for its decision); ADR-D-0042 every extension recorded, the audit marks which bear on direction, closeout shows only those. ADR-D-0027 and the goal-mode text untouched pending the owner's confirmation. Task_10's text changes will follow the three records.
  - Tradeoffs considered: the "philosophy alone" exclusion sits in ADR-D-0040 (it is about whether a second source exists) rather than ADR-D-0041 (how it carries).
  - User approval: waived for this initiative
  - Record proposed: ADR-D-0040, ADR-D-0041, ADR-D-0042 proposed, unaccepted; brought to the owner in that order
- 2026-10-01 Decision: the two sources of authorization apply to any unit of work the harness authorizes, a goal-mode envelope included.
  - Trigger / new insight: Counsel's relay of 2026-10-01 quoting the owner on Counsel's reading of his goal-mode remark: "That reading is right, go with it." The reading: the sources record covers any unit of work the harness authorizes, so goal-mode envelope ratification is covered by the same two sources; redefining goal mode as a longer-horizon mode stays a later initiative. Counsel added the line to the brief.
  - Plan delta (what changed): ADR-D-0040 as split is already mode-neutral and needs no change; it leaves ADR-D-0027 in force and names that a future goal-mode record stating second-source conditions would supersede it. The goal-mode reference and ADR-D-0027 stay untouched in this initiative; Task_10's Plan Gate text names the two sources for a unit of work. Counsel's brief line and notes file committed on the branch at Counsel's word.
  - Tradeoffs considered: none.
  - User approval: waived for this initiative
  - Record proposed: unchanged (ADR-D-0040 to ADR-D-0042 proposed)
- 2026-10-02 Decision: ADR-D-0040 accepted.
  - Trigger / new insight: Counsel's relay quoting the owner, 2026-10-02: "I accept ADR-D-0040." The record is `ADR-D-0040-non-trivial-work-is-authorized-only-by-the-person-directing-the-work-or-by-that-persons-ratified-brief.md` as announced final on 2026-10-01.
  - Plan delta (what changed): the record's file set to `status: accepted`; it stays untracked on this branch and is committed on the second pull request's branch, where ADR-D-0032 is retired in the same commit with its inbound pointers repaired. That branch is cut once ADR-D-0041 and ADR-D-0042 have the owner's word, since the Plan Gate text follows from them.
  - Tradeoffs considered: none.
  - User approval: the owner's acceptance of the record, relayed by Counsel
  - Record proposed: ADR-D-0040 accepted; ADR-D-0041 and ADR-D-0042 still proposed
- 2026-10-02 Decision: ADR-D-0041 accepted.
  - Trigger / new insight: Counsel's relay quoting the owner, 2026-10-02: "I accept ADR-D-0041."
  - Plan delta (what changed): the record's file set to `status: accepted`; untracked on this branch, committed on the second pull request's branch.
  - Tradeoffs considered: none.
  - User approval: the owner's acceptance of the record, relayed by Counsel
  - Record proposed: ADR-D-0041 accepted; ADR-D-0042 still proposed
- 2026-10-02 Decision: the second pull request's branch cut as a stack on the first; ADR-D-0040 and ADR-D-0041 landed there and ADR-D-0032 retired.
  - Trigger / new insight: the owner's acceptances of ADR-D-0040 and ADR-D-0041 (entries above).
  - Plan delta (what changed): `gh stack init` adopted `feature/2026-09-30/value-level-operation` and created `feature/2026-10-02/plan-authorized-by-ratified-brief` on top. On the new branch: ADR-D-0040 and ADR-D-0041 committed as accepted; ADR-D-0032 set to `status: superseded`, given the retirement line, and moved to `superseded/ADR-D-0032-plan-approval-is-never-self-granted--superseded-by-ADR-D-0040.md`; pointers repaired in ADR-D-0033 (depends_on and two glosses), ADR-D-0038 and ADR-D-0039 (the plan-approval pointer now names ADR-D-0040) and two completed plans' paths; absence search for the old filename clean; validator passed. ADR-D-0042 stays untracked until the owner's word.
  - Tradeoffs considered: pointer repairs in accepted records change no decision (adr.md allows pointer repair).
  - User approval: waived for this initiative
  - Record proposed: unchanged
- 2026-10-02 Decision: ADR-D-0042 accepted; Task_10 done with the text of ADR-D-0040 to ADR-D-0042.
  - Trigger / new insight: Counsel's relay quoting the owner, 2026-10-02: "I accept ADR-D-0042." All nine records (ADR-D-0034 to ADR-D-0042) and both standing-approval entries are accepted.
  - Plan delta (what changed): ADR-D-0042 set to `status: accepted` and committed on the second pull request's branch. Task_10 (Worker, then Reviewer NEEDS_REVISION with one MAJOR, fixed, then delta review APPROVED with four wording MINORs, applied): the second source of authorization stated once in the Plan Gate with its conditions in `lifecycle-gates.md` Plan Gate Details; Replan Procedure step 4 holds changed items for a later audit or approval; the mandate's `ask-now` on an action stated as waiting does not count against authorization when that test is the only reason; the auditor marks `inferred` items `direction` and the closeout, the final response, the note to Counsel, both Orchestrator agents and the Counsel skill show only the marked ones as the verdict states them; one line of `value-level-operation.md` outside Task_10's owns corrected by the Orchestrator (it said a plan-draft verdict authorizes nothing); manifests at 0.23.0. Validators and smoke tests pass. Reviewer wording "draft plan before approval" in the Reviewer agents left as is (not contradictory).
  - Tradeoffs considered: the "only reason" qualifier is narrower than ADR-D-0041's words, in the safe direction.
  - User approval: the owner's acceptance of the record, relayed by Counsel; plan approval waived for this initiative
  - Record proposed: none outstanding
- 2026-10-02 Decision: the stack published on the owner's statement in this session.
  - Trigger / new insight: the permission check in this session refused `gh stack submit --auto --open` as an external write; the refusal was brought to the owner here and through Counsel and not worked around. The owner's own statement in this session, 2026-10-02: "You can push the stack and open PRs."
  - Plan delta (what changed): `gh stack submit --auto --open` pushed both branches, opened pull request #73 (https://github.com/ebigunso/agent-harness/pull/73) on top of #72 (https://github.com/ebigunso/agent-harness/pull/72) and created the stack on GitHub. Nothing is merged; the merge waits for the owner's acceptance naming the stack and each pull request. The closeout audit's question on whether Counsel sees the audit's direction-marked items before its own read is with Counsel, unanswered.
  - Tradeoffs considered: none.
  - User approval: the owner's statement in this session
  - Record proposed: none outstanding
- 2026-10-02 Decision: Counsel forms a first read before seeing any part of the verdict, then reads what it needs and brings the finished read.
  - Trigger / new insight: the closeout audit's held item on the note to Counsel carrying the audit's direction-marked items. Counsel's relay quoting the owner, 2026-10-02: "Do an independent read first, but do not make that final. Read whatever you need to next, and bring me the finalized read." Also relayed, on the brief amendments Counsel drafted at the audit's request (product-basis line, pass conditions marked, provenance on two reworded lines): "The brief amendments are OK as well."
  - Plan delta (what changed): `completion-closeout.md` Note to Counsel no longer carries the marked items; after Counsel says its first read is written down, the Orchestrator sends what Counsel asks for, the marked items as the verdict states them included, as text. The Counsel skill says the same from its side. ADR-D-0042 is unaffected: what the owner is shown at closeout is unchanged. The marked items of this run's closeout audit sent to Counsel after its first read. Counsel's brief amendments and notes committed on the branch.
  - Tradeoffs considered: none.
  - User approval: the owner's answer to the held item, relayed by Counsel
  - Record proposed: none
- 2026-10-02 Decision: briefs get the lifecycle plans have; the Copilot Counsel agent is named Counsel; machine user names and paths are redacted before push.
  - Trigger / new insight: Counsel's relay quoting the owner, 2026-10-02, from looking at the structure of the pull requests; not an acceptance of the stack: "Do the briefs split, and rename the Copilot agent to Counsel. The wording cleanup is not necessary, but the usual privacy protection of no machine specific user names and paths leaking applies here too. If that sort of thing is quoted, it should be redacted before they ever reach the remote." Counsel amended the brief accordingly.
  - Plan delta (what changed): (1) target-repository layout `docs/coding-agent/briefs/active/` and `completed/`, notes travelling with the brief; a brief moves to `completed/` when the owner's acceptance of its final stack has reached the Orchestrator session; only a brief under `active/` can govern a run, and the audit reports one named elsewhere as a missing input; stated once in the brief form (`counsel/references/value-documents.md`) and carried in the Counsel skill, the Repository Rule Entry, the run-side reference, the mandate and the closeout. This repository's brief and notes moved to `docs/coding-agent/briefs/active/`; live pointers repaired in this plan's header lines and in the eight records' source-of-intent lines (path only). Verbatim history in the Progress Log keeps the old path. (2) `agents/harness-counsel.md` renamed `agents/Counsel.md` for Copilot, Claude keeps `harness-counsel`; role map, both READMEs, adapter checklist and validator repaired; the role map's Counsel row says the person directing the work; its naming rule gains the Copilot exception. Task text above that names `agents/harness-counsel.md` and "the physical name harness-counsel" is left as written; this entry supersedes it. (3) Scan of both published branches: the stack introduced no machine user name or path; three lines already on main (two in lessons, one in a completed plan) redacted. Worker Task_11, Reviewer NEEDS_REVISION (one MAJOR: the mandate's notes-exclusion pathspec had been narrowed and no longer covered a notes file directly under `briefs/`; restored), validators pass. Plugin stays at 0.23.0: unmerged.
  - Tradeoffs considered: main's history keeps the three old lines; no history rewrite proposed.
  - User approval: the owner's directions, relayed by Counsel; plan approval waived for this initiative
  - Record proposed: none
- 2026-10-02 Decision: what Counsel may say to the Orchestrator, and the binding pause, proposed as ADR-D-0043 and ADR-D-0044; the pre-push privacy sweep broadened.
  - Trigger / new insight: Counsel's relays quoting the owner, 2026-10-02. On Counsel's messages and the pause: "Mostly good. But I feel that structure suppresses the Counsel session advisory role too much. The split between what Orchestrator and Counsel is each responsible for should be honored, but for something that falls in the Counsel responsibility, I would like genuine advice to reach me. If such advice warrants stopping a work probably rests on how severe the effects would be if continued without a decision." and, to the revised structure, "Make the pause binding, go with it." On the privacy check: "Have the Orchestrator check what the pre-push privacy check covers. How to deal with it I will leave it to you or the Orchestrator, whichever is appropriate, to decide. Come back to me if something is lacking for operations to continue in this way, so I may discuss how to deal with the situation."
  - Plan delta (what changed): two proposed records on the second pull request's branch. ADR-D-0043: about the run's work Counsel speaks to the Orchestrator only in the owner's words (quote a statement that explicitly covers the question; hand back as below the owner's level; or bring it to the owner), gives no instruction, opinion or sequencing of its own, and its advice, the closeout read included, goes to the owner; a copy of the read reaches the Orchestrator only for display, which keeps the brief's line that closeout reports Counsel's read. ADR-D-0044: three severities; at high severity Counsel pauses the affected part with a stated reason and raises the matter with the owner at once; the Orchestrator holds that part until the owner answers and does not judge the pause; a pause is no decision of the owner and directs nothing. The Counsel skill, the brief form and the run-side carrier text carry both. Orchestrator's addition, not in the owner's words: the Orchestrator names every pause in force in its next report to the owner, so a pause the owner never heard of cannot hold work unseen. Review: first draft NEEDS_REVISION (four MAJORs: closed lists contradicted the closeout exchange; hand-back wording; one record bundled two decisions; the reconciliation with ADR-D-0034 belonged in the Decision), split and fixed; second round MINORs applied. Privacy sweep: the existing check covered only four Windows path forms and only documentation-heavy pushes, so it missed a display name, a path in a quoted command and Unix-style paths; `git-workflow/references/pre-commit-gate.md` now sweeps every commit a push publishes, patch and message, case-insensitively, for home paths in any form, the local account name and the host name, with quoted material not exempt, and escalates where only a history rewrite would remove a hit. Nothing is lacking for operations to continue this way.
  - Tradeoffs considered: Counsel's read to the owner only (no copy to the Orchestrator) would be simpler but contradicts the brief's closeout line; left for the owner if he wants it.
  - User approval: the owner's directions, relayed by Counsel; plan approval waived for this initiative
  - Record proposed: ADR-D-0043 and ADR-D-0044, proposed, unaccepted
- 2026-10-02 Decision: the dated model-routing observation moves from the plugin into this repository's rule files; a third pull request on the stack.
  - Trigger / new insight: the owner noticed the Orchestrator used no agmsg Codex teammate in this run. Fact: every dispatch went to Claude subagents; the one recorded reason (Task_5: peer delivery could not be confirmed) was never retried or reported to the owner, which the repository rule required; the routing text existed, so the continuing cause was the Orchestrator's omission. Counsel's relay quoting the owner, 2026-10-02: "Right. I think that is a good direction to go towards. Let us do that. Stack on the current PRs." What that answered: the plugin keeps the durable routing principle; the dated observation of which models have shown which strength, and which models and peers the workspace has, moves into the repository rule files that every session reads at start; a model upgrade is an occasion to re-observe.
  - Plan delta (what changed): on a new branch stacked on the second pull request: `subagent-strategy/references/model-routing.md` drops its dated illustration and points to `docs/coding-agent/rules/orchestrator.md`; that rule file gains "Models And Peers In This Workspace" (the observation dated 2026-09-15, the Claude subagents and the two registered Codex peers, the default split, the agmsg dispatch rule moved there, and a liveness check before the first dispatch of a run with a silent peer reported and never silently replaced); plugin 0.24.0. The privacy sweep scrutiny was dispatched to `agent-harness-reviewer` over agmsg.
  - Tradeoffs considered: the liveness check lives in this repository's rule file, not the plugin; whether the plugin should carry such a step was put to Counsel for the owner.
  - User approval: the owner's direction, relayed by Counsel; plan approval waived for this initiative
  - Record proposed: none
- 2026-10-02 Decision: ADR-D-0043 accepted with the copy of Counsel's read removed.
  - Trigger / new insight: Counsel's relay quoting the owner, 2026-10-02: "I accept ADR-D-0043, keep the copy out." What that answered: Counsel had told him the record let a copy of Counsel's closeout read go to the Orchestrator session only to be shown with the closeout, that this was not in his words, and that removing it was a one-line change.
  - Plan delta (what changed): ADR-D-0043 set to `status: accepted` with the read going to the owner only (Decision line, the rejected alternative and the invariant). The Counsel skill, `completion-closeout.md`, `final-response-contract.md` and both Orchestrator agents no longer have the Orchestrator show or report Counsel's read; `candidate ready` does not depend on it. The brief's closeout line naming Counsel's read is Counsel's to amend.
  - Tradeoffs considered: none.
  - User approval: the owner's acceptance of the record, relayed by Counsel
  - Record proposed: ADR-D-0043 accepted; ADR-D-0044 proposed, unaccepted
- 2026-10-02 Decision: the pre-push privacy sweep is a read-only helper script, built and reviewed by the Codex peers.
  - Trigger / new insight: the Codex reviewer peer (`agent-harness-reviewer`), given the prose sweep written earlier today, returned five MAJORs (the configured upstream is not the push destination; a patch listing is not a full publication inventory; other refs, tags and notes; "any form" was not a reproducible matching rule; a hit in an outgoing commit cannot be fixed in the working tree) and recommended a small Git-specific helper.
  - Plan delta (what changed): Task_12, Codex worker peer (`agent-harness-worker`): `skills/git-workflow/scripts/privacy-sweep.sh` (reads the destination's advertised refs, scans every commit a push would newly publish: messages, author and committer, added lines, paths, merge diffs; identities collected from the machine at run time; candidates, inspection items and a clean result kept apart; writes nothing but scratch files), the corrected step 7 bullet in `pre-commit-gate.md`, and `tests/coding-agent-orchestration-harness/privacy-sweep-selfcheck.sh` (30 cases). Orchestrator integration rulings: an advertised ref whose object is missing locally (GitHub pull-request merge refs) is not used for exclusion and is noted, with fail-closed kept for the destination tip and shallow clones; valid UTF-8 is scanned as text and only invalid or binary content needs inspection. Codex review: NEEDS_REVISION once (a one-letter Unix account produced a false clean), fixed, delta APPROVED. `common.md` gains the self-check as a validation command and narrows the watcher self-check to its own script. The watcher self-check timed out on Windows at its 12-second guard in the peers' runs; unchanged script, waived for this task. Also from the Codex review of the routing change: the workspace routing line keeps plans and decision records with the Orchestrator.
  - Tradeoffs considered: a script under `skills/` is runtime text invoked by `pre-commit-gate.md`, and it is Git-specific, so it is not the universal quality-gate runner the repository rules forbid.
  - User approval: the owner left how to deal with the privacy check to the Orchestrator (relay of 2026-10-02); plan approval waived for this initiative
  - Record proposed: none

## Notes
- Risks: a Codex session opened as Counsel may drift into Orchestrator work when the talk turns to code; a stated rule in the skill is the only guard. Claude lists plugin agents as dispatchable subagents, so "Counsel is never dispatched" is a stated rule there. Up to nine record acceptances are nine decisions for the owner (Q2); they are required by the repository rule on records. The Orchestrator cannot verify a relayed quote; the design accepts Counsel as the carrier of the owner's word only after the owner has named Counsel as his carrier in that Orchestrator session, and the relay record (Proposal 7) must say so plainly.
- Edge cases: a repository with an engineering philosophy only (audit runs on that side; user approves plans); a brief with no human-only conditions (closeout is still "candidate ready" under a brief); a setup with no peer channel (escalations wait in the discussion notes until the owner next opens Counsel).
