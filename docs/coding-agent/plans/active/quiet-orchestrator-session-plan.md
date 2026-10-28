# Plan: A quiet Orchestrator session under a brief

- status: draft
- generated: 2026-10-28
- last_updated: 2026-10-28
- work_type: docs

## Goal
- The harness gives what the governing brief `docs/coding-agent/briefs/active/quiet-orchestrator-session-brief.md` states: while a run under a ratified brief is in progress, the owner never needs to look at the Orchestrator's session; whatever needs him reaches him through Counsel, a plan under a brief is never presented for approval, and the final response names what is with Counsel and what the turn ended blocked on instead of asking.
- The brief is the requirement and is not restated here; where this plan and the brief differ, the brief governs and the difference is a plan defect.
- This is the first plan of the run recorded in `docs/coding-agent/plans/active/quiet-orchestrator-session-run.md`.

## Definition of Done
- The default is stated once, in `value-level-operation.md` The Carrier: under a brief every question that needs the owner, whatever its kind, travels by the Carrier, the session puts no question to the owner, and a line elsewhere in the plugin that asks the user is read under a brief as pointing at the Carrier or at the blocked report; a brief, hand-over or dispatch arriving as a message does not make the owner present for questions, while anyone may still talk to the session and a question is answered where it was asked (brief, "What the plugin states", items 2 to 4).
- Under a brief a plan is never presented for approval, in the session or through Counsel; the three moves when the brief route does not authorize are stated once, where the route is (`lifecycle-gates.md` Plan Gate Details), and every fallback that today sends a plan under a brief to the plan-mode rule's approval or its asking (R1 part 5: `SKILL.md`:41-42, `lifecycle-gates.md`:17, :19, :25, :57, `value-level-operation.md`:97, both Orchestrator adapters' Plan Gate) no longer does; the plan-mode rule's asking is scoped to work no brief governs (brief, item 1).
- The lines the brief names read under a brief as the Carrier or the blocked report, each at its own place: the Orchestrator's ownership of user questions (`SKILL.md`:24); the replan procedure's confirmation (`lifecycle-gates.md`:56); the final-response slot for questions (`final-response-contract.md` item 8 and its Under a brief carry-over, `SKILL.md` Final Response Summary, both Orchestrator adapters); the Carrier's list of consent gates (`value-level-operation.md`:95) no longer reads as the only kinds that go to Counsel. Counsel's own statement that plans are presented only by the Orchestrator session (`counsel/SKILL.md`:22) says that under a brief no plan is presented at all.
- Counsel's receiving side matches the sending side (`counsel/SKILL.md`:73 and :77, which today hand back everything below the direction level): what only the owner can give, an act, a permission or an input that no statement of his covers and no one else can supply, is brought to him and not handed back; a question of judgement below the direction level still goes back to the Orchestrator to settle, and Counsel decides no implementation and uses none of the owner's authority (brief, "Who it is for and why": "Whatever needs him, of any kind, reaches him through Counsel").
- A run without a brief, on a philosophy alone or with no value document, is unchanged (brief, constraint): its plan is presented and its user asked in the session.
- Goal mode under a brief: held for the owner's answer to the value question of 2026-10-28 (Decision Log D1); built only after the plan is revised for that answer and passes its gate again (Replan Procedure step 4).
- Scenarios 1, 2 and 5 are shown on a fixture with the outcome in the Progress Log, and scenario 4 as the control; scenario 3 is shown on the same fixture where one can be made; the human-only pass condition stays pending and the closeout says so.
- The plugin's version is 1.2.0 in every file that states it, made as the last change before the run is reported ready.
- Package validators and smoke tests pass; the branch has Reviewer `APPROVED`; value audits at plan draft and closeout are logged; the plan closes and the run is reported ready: branch published, pull request opened under the standing approval, note to Counsel, nothing merged.

## Planner-added requirements
- Scenario 4 is shown on the same fixture as scenarios 1, 2 and 5, as a control. Needed because: a text that stops every question everywhere would pass 1, 2 and 5 and break the brief's constraint that a run without a brief is unchanged.
- The fixtures and probe outputs live in the Orchestrator's scratchpad, not in the repository. Needed because: they are one-off measurements of how a fresh agent reads the text, not checks a validator runs again; `tests/` holds what the validators run (`common.md`, validation commands), and a fixture kept there would need upkeep with no consumer.
- The plugin's version becomes 1.2.0, as the last change before the run is reported ready. Needed because: an installed plugin is refreshed only when its version changes, so no workspace receives the change otherwise; minor, since behaviour changes and nothing a consumer relies on breaks; last, so a later fix in the run does not ship under a version already published.

## Scope / Non-goals
- Scope: the plugin texts in R1's census that, under a brief, ask the user in the session or present a plan there: `skills/orchestration-harness/SKILL.md` (Stable Role Model, Plan Gate, Final Response Summary); `references/value-level-operation.md` (The Carrier); `references/lifecycle-gates.md` (Plan Gate Details, Replan Procedure); `references/final-response-contract.md`; `agents/Orchestrator.md`, `claude/agents/harness-orchestrator.md` where they restate those; `skills/counsel/SKILL.md`:22, :73 and :77 (Counsel's receiving side); `skills/git-workflow/references/pr-review-monitoring.md`:46 (a redesign proposed "to the user as a plan delta"); the version files. A decision record if the admission test passes.
- Non-goals: what the audit grades and what authorizes a plan under a brief (brief, Limits); any new carrier or kind of message (brief, Limits); runs without Counsel (brief, Left out); the generic operational asks R1 lists in other skills (troubleshooting, setup, git stacking, peer nudging, improvement-loop), which the default's reading rule covers without editing each; the Researcher, Worker, Reviewer and Auditor texts, which already put no question to the user (R1 part 4).

## Design
- Chosen: state the default once, at the head of The Carrier in `value-level-operation.md`, where the brief's means puts the root cause ("the fix belongs where the default is stated"); state the three moves once in `lifecycle-gates.md` Plan Gate Details, beside the route's conditions; then change only the lines that, read with the default, still contradict it, because they say "in this session" or send a plan under a brief back to approval (R1 parts 1, 2 and 5). Every other line that says "ask the user" is left as it is and read through the default.
  - structure: one owner of the rule, the Carrier; the fallbacks point to it; no line restates it. evolution: a new "ask the user" line elsewhere needs no edit to be right under a brief; deletion path is the one paragraph. verification: the census lines are checked by search; the behaviour on a fixture. operation: none. human: a reader of the Plan Gate meets the brief case where the fallback is. safety: no consent gate is lowered; each keeps its rule and gains only the carrier.
- Alternative: edit each of the about thirty lines R1 lists to add "under a brief, by the Carrier".
  - structure: thirty restatements of one rule. evolution: every future ask line must remember the clause, and the census goes stale. verification: the same search, more places to miss. operation: none. human: a reader sees the clause everywhere and the default nowhere. safety: the same.
- Why chosen: the brief locates the defect in the rule being an exception list rather than a default; the alternative keeps it an exception list, only a longer one.
- Ruling R1 (merge permission): under a brief, the runtime's own permission to merge (`value-level-operation.md`:96 and its four copies) is not a question the Orchestrator asks. When a merge waits for it, the turn ends blocked naming it, and Counsel is told in the same message that reports the run's state; nothing in the session is phrased as a question. The permission itself stays the owner's to grant in the session, once and as a standing matter, as written; the plugin cannot carry a runtime grant.

## Compatibility stance
- surface: the Plan Gate's sources of authorization and the final response's question slot, as an Orchestrator reads them under a brief.
- stance: break
- justification: the consumers are the Orchestrator sessions that read the plugin, and the owner, who is the one the brief changes it for; under a brief the old behaviour (a plan presented for approval, questions in the session) is what the brief removes. A run without a brief keeps the old behaviour unchanged.

## Context (workspace)
- Governing brief: `docs/coding-agent/briefs/active/quiet-orchestrator-session-brief.md`. Ratification as it reached this session: Counsel's relay of 2026-10-28 (16:17Z), quoting the owner on 2026-10-29: "I ratify both briefs, hand them over now." Relays are admitted by the Standing Approvals entry of 2026-10-01 in `common.md`.
- Run record: `docs/coding-agent/plans/active/quiet-orchestrator-session-run.md`. Readings file: `docs/coding-agent/plans/active/quiet-orchestrator-session-readings.md`.
- Related files/areas: R1 census of 2026-10-28 by the researcher seat (agmsg history, 16:38Z to 16:40Z), path:line for each line named above.
- Existing patterns or references: ADR-D-0038 (the owner's word reaches the session directly or by quoted relay), ADR-D-0051 (work under a brief is a run), ADR-D-0034 (Counsel is a separate session).
- Design record consulted and deviations from its acceptance: ADR-D-0038 and ADR-D-0051 state that plan approval is not carried by relay; this plan keeps that (no plan is carried) and removes plan approval under a brief altogether, which a new record states if the admission test passes.

## Open Questions (max 3)
- None in this session; the one value question is with Counsel (D1).

## Assumptions
- A1: the generic "ask the user" lines in other skills (R1 part 3) are covered by the default's reading rule and need no edit; the reviewer checks that none of them says "in this session" or otherwise defeats the reading — source: R1 parts 3 and 6 C; brief, item 3 (means).
- A2: the runtime's merge permission is the runtime's, not a question the plugin can route; Ruling R1 stands until the closeout audit grades it — source: R1 part 2 and part 7 E; `value-level-operation.md`:96.

## Tasks

### Task_1: The default, the three moves, and the lines that contradict them
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/value-level-operation.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/lifecycle-gates.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/final-response-contract.md
  - plugins/coding-agent-orchestration-harness/agents/Orchestrator.md
  - plugins/coding-agent-orchestration-harness/claude/agents/harness-orchestrator.md
  - plugins/coding-agent-orchestration-harness/skills/counsel/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/git-workflow/references/pr-review-monitoring.md
  - docs/coding-agent-orchestration-harness/decisions/ (a new record only)
- depends_on: []
- description: |
  Make the plugin say what the brief's "What the plugin states" says, by the Design above: the default once in The Carrier, the three moves once in Plan Gate Details, and the contradicting lines changed at their own places. Wording is the Worker's, within the brief's words. Goal-mode texts are out of this task (D1).
- acceptance:
  - The Carrier opens with the default (brief items 2 to 4), including the message-arrival line; its consent-gate list keeps each gate's own rule and reads as gates the carrier reaches, not as the only kinds of question that go to Counsel; `value-level-operation.md`:97 no longer locates a plan under a brief in the session; Ruling R1 is stated where :96 is.
  - Plan Gate Details states the three moves once, beside the route's conditions; `SKILL.md` Plan Gate and `lifecycle-gates.md`:17, :19, :25 and :57 send a plan under a brief to no approval, waiver or asking, and the plan-mode rule's asking reads as for work no brief governs; both Orchestrator adapters' Plan Gate lines match.
  - `SKILL.md`:24, `lifecycle-gates.md`:56, `final-response-contract.md` item 8 and its Under a brief carry-over, `SKILL.md` Final Response Summary and both adapters' final-response lines read under a brief as the Carrier or the blocked report; `counsel/SKILL.md`:22 and `pr-review-monitoring.md`:46 agree.
  - `counsel/SKILL.md`:73 and :77 bring to the owner what only he can give (an act, a permission or an input no statement of his covers and no one else can supply) and still hand back a question of judgement below the direction level; Counsel decides no implementation and uses none of the owner's authority. The Orchestrator's side (`value-level-operation.md` Asking The Owner and the Carrier) names the same three kinds of what needs the owner: direction-level questions, the reserved acts, and what only he can give.
  - A run without a brief reads exactly as before.
  - A decision record is proposed if the admission test in `durable-docs-authoring/references/adr.md` passes, filename at or under 135 characters.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: py scripts/validate_harness_package.py and py scripts/run_validation_smoke_tests.py pass; git diff --check clean on owned paths"
  - kind: command
    required: true
    owner: worker
    detail: "Adapter sync: the two Orchestrator adapters' instruction bodies agree outside runtime-specific blocks (runtime-adapter-contract SKILL.md:23)"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review against the brief; a search of plugins/ for lines that, under a brief, ask the user in the session or present a plan there, R1's census lines included, finds none outside the held goal-mode texts"

### Task_2: Scenarios on a fixture
- type: test
- owns:
  - the Orchestrator's scratchpad (fixtures and probe outputs; nothing in the repository)
- depends_on: [Task_1]
- description: |
  Show scenarios 1, 2 and 5, and 4 as the control, by giving a fresh agent the plugin text at the branch head and a fixture state for each, and recording what it does. Scenario 3 on the same fixture where one can be made.
- acceptance:
  - For 1 (review left a finding open), 2 (an ask-now) and 3 (an outward-facing change at replan), the agent under a fixture brief takes one of the brief's moves and puts no question in the session and presents no plan; for 5 its final response names what is with Counsel and phrases nothing as a question to the reader.
  - For 4 (no brief, a philosophy alone) it presents the plan and asks in the session.
  - A fresh agent given Counsel's text and an Orchestrator message asking for something only the owner can give (for example a credential the run needs) brings it to the owner and does not hand it back; given a question of judgement below the direction level, it hands it back.
  - The dispatch texts and outcomes are logged in the Progress Log; a scenario that cannot be made on a fixture is said so plainly.
- validation:
  - kind: manual
    required: true
    owner: orchestrator
    detail: "Each probe a new session with no context beyond the plugin text and the fixture; each outcome recorded in the Progress Log with the part of the response that shows it"

### Task_3: Version 1.2.0
- type: chore
- owns:
  - plugins/coding-agent-orchestration-harness/.claude-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.codex-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.github/plugin/plugin.json
  - .claude-plugin/marketplace.json
  - .github/plugin/marketplace.json
- depends_on: [Task_1, Task_2]
- description: |
  Set the plugin's version to 1.2.0 everywhere it is stated, as the last change before the run is reported ready.
- acceptance:
  - Every file that states the plugin's version says 1.2.0 and none says 1.1.0.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "py scripts/validate_harness_package.py passes; a search for 1.1.0 in the version files finds none"

## Task Waves (explicit parallel dispatch sets)
- Wave 1: Task_1
- Wave 2: Task_2
- Wave 3: Task_3

## Rollback / Safety
- Each task's commits are its own; reverting them restores the prior text. Nothing reaches the remote before review, and nothing is merged without the owner's acceptance naming the pull request.

## Progress Log (append-only)
- 2026-10-28 16:21 Research before drafting: R1, a forensic census, dispatched to the Researcher role on the researcher seat `agent-harness-researcher` (detail strength), its own dispatch and report over agmsg; no Worker task carried it. The seat disclosed that it opened this run's notes file and the then-empty readings file, against the dispatch's exclusion, and the other brief; directed to quote and cite nothing from the notes, which its report states it did not.
- 2026-10-28 16:43 Finding escalated to Counsel (readings file, Findings): goal mode under a brief. Part held: the goal-mode texts.
- Run starts from revision: 55c08a4.
- 2026-10-28 16:45 Plan review dispatched to the reviewer seat `agent-harness-reviewer` with the plan-review snippet, at cb25c26. 16:56 to 16:57 NEEDS_REVISION, two findings: QPR-F1 (major) Counsel's receiving side (`counsel/SKILL.md`:73, :77) hands back everything below the direction level, so an owner-only question that is no judgement call would come back instead of reaching him; QPR-F2 (minor) three drafting constraints unlisted (fixtures only in the scratchpad, outcomes copied verbatim, one commit per task). Triage: QPR-F1 fix (a DoD item, Task_1 acceptance and a Counsel probe in Task_2); QPR-F2 fix (the scratchpad listed with its reason; "verbatim" and the commit count dropped). Validator: pass.

## Decision Log (append-only; re-plans and major discoveries)
- D1, 2026-10-28: goal mode under a brief is held for the owner's answer to the value question sent to Counsel at 16:43:07Z (options: plan mode under a brief; goal mode with its envelope agreed in the session; the envelope through Counsel). Plan revised for the answer when it arrives.

## Notes (Risks / Edge cases)
- A fixture probe shows what a fresh agent does with the text, not what a long session does; the human-only pass condition covers the latter.
