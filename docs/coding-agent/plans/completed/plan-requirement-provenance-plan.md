# Plan: Plan drafting and review land on the best design, not the first

- status: done
- generated: 2026-09-16
- last_updated: 2026-09-16
- work_type: docs

## Goal
- A plan presented for approval carries the design judged best for the instance, not the first design reached: every requirement that entered during drafting is visible as an addition with its reason, each reason has been tested against the whole change, the chosen design has been set against at least one alternative, and the plan-review Reviewer independently enumerates the additions, tests their reasons against the design, and questions the design itself, so an unchallenged addition or an unexamined design is caught at plan review instead of surfacing later as an error.

## Definition of Done
- `plan-format` defines `planner-added requirement` and carries the obligation: every Definition of Done item, acceptance bullet, or constraint the request did not state is listed in one `Planner-added requirements` section with the reason the request cannot be met without it under the chosen design.
- `plan-format` carries a design obligation: the plan states the design chosen and at least one alternative that differs from it on a cost axis, what each changes across dependencies, duplicated state, and conversions (consumers stay in the Compatibility stance), and why the chosen one wins; proportional, so a change that touches no responsibility, contract, persisted state, or new component states it in one line.
- The `orchestration-harness` Plan Gate states that, after drafting and before the plan is presented, the existence challenge re-runs on planner-added requirements and the chosen design is set against its alternatives.
- The plan-review Reviewer snippet in `subagent-strategy` carries the review obligation: the Reviewer lists the plan's unrequested requirements itself and reports each mismatch with the plan's section; for each listed addition, tests whether the reason holds under the chosen design or whether another design removes the need; questions the design, and a finding may name a design that removes an addition, a dependency, a copy of state, or a conversion, with its cost delta; the Orchestrator owns the rewrite. The plan-review packet includes the request as given, and every place that defines the plan-review inputs agrees.
- No validator, script, or fixture changes. Reviewer judgment is the only check (ebigunso, 2026-09-16: automation comes last).
- Every added line passes the content test from the 2026-09-05 lesson (not learnable from plain knowledge or a tool's help) and stays within the length targets in the tasks.
- Package validators pass; plugin manifests bumped 0.20.0 to 0.21.0.

## Scope / Non-goals
- Scope: `skills/plan-format/SKILL.md`, `skills/plan-format/references/plan-template.md`, `skills/orchestration-harness/SKILL.md` (Plan Gate only), `skills/subagent-strategy/references/prompt-snippets.md` (plan-review snippet only), `skills/subagent-strategy/references/dispatch-checklists.md` (plan-review packet line only), `skills/wave-integration/SKILL.md` (draft-plan review route line only), the three plugin manifests.
- Non-goals: any validator or fixture change; architecture-gates; runtime adapters and the Codex loader; existing plans under `completed/`; post-Worker review (the design question is asked at plan review, where a rewrite is cheap).

## Planner-added requirements
- The obligations live in `plan-format` core rules, not only in template sections. Needed because: an Orchestrator that loads `SKILL.md` and reuses an older plan's structure never opens the template; a rule is read on every plan, a template section only when copied.
- An addition found anywhere in the plan but absent from the section is a plan defect. Needed because: without a consequence a drafter can list some additions and omit the rest; the section only catches what the defect clause makes it cover.
- A fixed item shape (`Needed because:`) and an explicit `- None` form. Needed because: the Reviewer compares its own list against the section item by item, which needs one shape; `- None` distinguishes "nothing was added" from "the section was skipped".
- The design obligation takes the shape of a named comparison: chosen design, at least one alternative that differs on a cost axis, what each changes, why. Needed because: "question the design" has no check without a second design to hold it against; the comparison is the artifact the Reviewer can test, and the three cost axes (dependencies, duplicated state, conversions) are what distinguishes a whole-change comparison from a diff-size one. Consumers are not a fourth axis: rule 8's Compatibility stance already carries them, and a second home would diverge.
- The design obligation is proportional: full comparison when the change touches a responsibility, contract, persisted state, or new component; one line otherwise. Needed because: a comparison on a one-file fix is noise on every plan, and `plan-format` rule 10 (plan altitude) already forbids restating what is cheap to see.
- The Reviewer obligation has two failure directions for additions (missing from the section; listed with a reason the design does not support) and a third for the design (an alternative that removes an addition, a dependency, a copy of state, or a conversion, named with its cost delta). Needed because: with only the first direction a drafter satisfies the check by listing every addition with a hollow reason, which is the incident's behavior relocated into a section; the design direction is what ebigunso's correction of 2026-09-16 asks for, and it is the Worker design-alert shape (cleaner alternative plus cost delta) already in the harness.
- The plan-review snippet's closing line changes from "do not propose another" to "do not rewrite the plan". Needed because: the existing line forbids the design finding outright; the intent it protects (the Orchestrator owns the rewrite) survives in the new wording.
- Every place that defines the plan-review inputs agrees, with the snippet as the one home. Needed because: a restated copy in `wave-integration/SKILL.md` had already diverged from the packet line, and the Reviewer obligations depend on the request reaching every dispatch route.
- The plan-review packet includes the request as given. Needed because: the Reviewer cannot enumerate unrequested requirements without the request; the current packet carries only the plan path, Researcher output, and plugin root.
- The terms `planner-added requirement` and the section headings are fixed in this plan. Needed because: three Workers edit three skills in parallel and the Reviewer matches the names across them.
- Not planner-added, stated for the record: the content test and length targets come from lesson 2026-09-05 (a repository lesson); "obligations, no mechanics, no checklist of design questions" in the review details comes from the ablation outcome merged in #70 (`repeat-check-ablation-plan.md`, keep the obligations, delete the prescribed mechanics); the validators, smoke tests, and `git diff --check` come from `docs/coding-agent/rules/common.md` and `worker.md`; the compatibility stance from `plan-format` rule 8.

## Design
- Chosen: obligations as `plan-format` rules 12 and 13 with two template sections, one Plan Gate sentence, and the plan-review snippet doing the checking. Dependencies: none added; the snippet already routes to `plan-format` and `engineering-quality-baselines`. Duplicated state: one copy removed (the restated plan-review inputs in `wave-integration`); the section headings and term must match across three skills, fixed by vocabulary. Conversions: none.
- Alternative: a standalone design-review reference under `engineering-quality-baselines`, the placement proposed in ebigunso's opening message of 2026-09-16 (`architecture-gates.md`). Dependencies: one new file and a routing entry every plan loads; the file's sibling gates were removed by the ablation in #61 for no measured lift. Duplicated state: the obligation lives apart from the plan format that carries its artifact, so the section shape and the rule that demands it sit in two skills. Conversions: none.
- Alternative: obligations only in the plan-review snippet, the drafter not asked. Dependencies: none. Duplicated state: none. Conversions: none. Removes rules 12 and 13 and both sections, so it is the cheapest; rejected because the drafter never faces the question, every plan reaches review with the first design, and a same-family Reviewer shares the blind spot, which is the incident's mechanism.
- Why chosen: the drafter is asked first and the Reviewer checks second, the shape of every other gate in the harness; the cost is prose in files already loaded on every plan, and the only state it adds is the vocabulary match across three skills.
- Not a design: a validator for the sections is the scope ruling in Decision Log entry 1, not an alternative design.

## Compatibility stance
- surface: the plan template and Plan Gate text read by Orchestrators, and the plan-review snippet and its input definitions read at Reviewer dispatch.
- stance: migrate
- justification: consumers are the three runtime adapters and future plans in this repository; no validator changes, so plans without the new sections remain structurally valid; the version bump in Task_4 carries the change to installed copies.

## Context (workspace)
- Related files/areas: `plugins/coding-agent-orchestration-harness/skills/plan-format/SKILL.md` (core rules 1 to 11; rule 10 plan altitude), `references/plan-template.md` (Definition of Done, Scope / Non-goals, Assumptions with `source:` convention; Decision Log "Tradeoffs considered" is the only place alternatives appear today, at replan time), `skills/orchestration-harness/SKILL.md` Plan Gate second bullet ("question the requirements themselves"), `skills/subagent-strategy/references/prompt-snippets.md` "Reviewer snippet (plan review)" (closing line "Question the decomposition given; do not propose another", introduced in #56 with no recorded rationale beyond keeping the rewrite with the Orchestrator), `references/dispatch-checklists.md` Reviewer checklist line "For plan review, the packet is...", `skills/wave-integration/SKILL.md` Routes "Draft-plan review" line (restates the inputs and says "No packet").
- Origin of the placement alternative: ebigunso's opening message of 2026-09-16 pasted a recommendation (Japanese, six design-check sections) proposing `engineering-quality-baselines/references/architecture-gates.md` as the home; this plan's Design section names it as the first alternative.
- Proportionality ladders: rule 13's trigger (responsibility, contract, persisted state, new component) decides whether a design comparison is meaningful; `architecture-gates.md` Decision Guidance grades gate-evidence rigor by change risk. They coexist and key on different questions; this plan does not merge them.
- Existing patterns or references: the Assumptions `source:` convention; the Symmetric checks pattern in `engineering-quality-baselines/references/review-rubric.md`; the Worker design-alert shape (what is worked around, the cleaner alternative, the cost delta) in `subagent-report-contract` and `wave-integration/references/integration-checklist.md`; lesson 2026-09-16 "A Grader Can Relax The Pre-Registered Hit Condition" motivates literal enumeration over judgment prompts.
- Design record consulted and deviations from its acceptance: ADR-D-0019 governs removal and relaxation of harness content; this plan adds, and reworded one Reviewer line whose intent survives, which is outside its scope. ADR-D-0032 (plan approval is never self-granted) unchanged. No deviation.
- Research waived: the Orchestrator read every target file and the repo rules directly in this session; the change is confined to six prose files whose current text is quoted above.

## Fixed vocabulary (Workers use these exactly)
- `planner-added requirement`: a Definition of Done item, acceptance bullet, or constraint that entered the plan during drafting rather than from the request, a document the request names, or the repository's rule suite and lessons.
- Section heading: `## Planner-added requirements`; item shape: `- <requirement>. Needed because: <why the request cannot be met without it under the chosen design>`; empty section reads `- None`.
- Section heading: `## Design`; lines: `Chosen:` with what it changes on each axis; one or more `Alternative:` lines, each differing from the chosen design on at least one axis, with what each changes across dependencies, duplicated state, and conversions (consumers: see the Compatibility stance); `Why chosen:`. Proportional form when the change touches no responsibility, contract, persisted state, or new component: `- Chosen: <one line>; no alternative changes the cost axes.`

## Open Questions (max 3)
- Q1: resolved 2026-09-16 by ebigunso: version bump to 0.21.0.

## Assumptions
- A1: The validator's section check is presence-only over seven fixed headings, so new optional sections need no validator or fixture change — source: `skills/plan-format/scripts/validate_plan.py` `REQUIRED_SECTIONS` (lines 13 to 21) and `validate()`.
- A2: The plan-review inputs are defined in exactly three places, all in scope — source: `rg -i "plan.review|plan-review|draft-plan" plugins/coding-agent-orchestration-harness/skills/` returns seven files; `prompt-snippets.md` (snippet), `dispatch-checklists.md` (packet line), and `wave-integration/SKILL.md:27` (route line) define the inputs, while `orchestration-harness/SKILL.md:39`, `lifecycle-gates.md:19`, `execution-plan-lifecycle.md:24`, and `engineering-quality-baselines/SKILL.md:39` only route to the snippet; the Reviewer adapters defer to the snippet and restate no inputs (Reviewer plan review, 2026-09-16).
- A3: The Reviewer line "do not propose another" has no incident or ADR behind it — source: `git log -S"do not propose another"` shows it entering in #56 (`e136397`); `docs/coding-agent/plans/completed/plan-review-gate-plan.md` carries the snippet text with no rationale for the clause; no lesson cites it.

## Tasks

### Task_1: plan-format carries the two obligations and the two sections
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/plan-format/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/plan-format/references/plan-template.md
- depends_on: []
- description: |
  Add core rule 12 to `SKILL.md` (at most three sentences): the definition of `planner-added requirement` from the fixed vocabulary; every such requirement is listed in the plan's `Planner-added requirements` section with the reason the request cannot be met without it under the chosen design; an addition found anywhere else in the plan but not in that section is a plan defect.
  Add core rule 13 (at most three sentences): the plan's `Design` section states the design chosen and at least one alternative that differs from it on a cost axis, with what each changes across dependencies, duplicated state, and conversions, consumers staying in the Compatibility stance, and why the chosen one wins; when the change touches no responsibility, contract, persisted state, or new component, the section is the one-line proportional form.
  Add both sections to `plan-template.md` (at most four lines for `Planner-added requirements` and six for `Design`, headings included), using the shapes from the fixed vocabulary and showing the `- None` and proportional forms; place them where the Worker judges they read best among the front sections.
- acceptance:
  - `SKILL.md` has rules 12 and 13 as described, each within three sentences, using the fixed vocabulary verbatim, and rule 13 names the three cost axes, the pointer to the Compatibility stance for consumers, and the proportionality trigger.
  - `plan-template.md` has both sections in the stated shapes and within the stated lengths.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python skills/plan-format/scripts/validate_plan.py --file ../../tests/coding-agent-orchestration-harness/fixtures/valid-plan.md --mode balanced; from repo root: git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review vs acceptance; content test per lesson 2026-09-05 on each added line; length targets met; rule 13 states an obligation and the comparison's axes, no checklist of design questions"

### Task_2: Plan Gate re-runs the existence challenge and sets the design against its alternatives
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/SKILL.md
- depends_on: []
- description: |
  In the Plan Gate, extend the second bullet ("Before decomposing non-trivial work, question the requirements themselves...") with at most two sentences: after drafting and before the plan is presented, the same challenge runs on every planner-added requirement and the plan lists each with its reason; the chosen design is set against at least one alternative and the plan records why it wins, so the plan presented is the best design found, not the first.
- acceptance:
  - The Plan Gate second bullet gains at most two sentences stating the re-run, the listing, and the design comparison.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From repo root: git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review vs acceptance; the sentences add obligations and no mechanics; content test per lesson 2026-09-05"

### Task_3: Plan-review Reviewer enumerates additions, tests their reasons, and questions the design
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/subagent-strategy/references/prompt-snippets.md
  - plugins/coding-agent-orchestration-harness/skills/subagent-strategy/references/dispatch-checklists.md
  - plugins/coding-agent-orchestration-harness/skills/wave-integration/SKILL.md
- depends_on: []
- description: |
  In `prompt-snippets.md` "Reviewer snippet (plan review)": add the request as given to Inputs. Add two Procedure bullets, each at most three sentences. First, the enumeration: list every Definition of Done item, acceptance bullet, and constraint in the plan that the request does not state; compare with the plan's `Planner-added requirements` section; each item on the Reviewer's list missing from the section is a finding, and each listed item whose reason does not hold under the chosen design, or whose need another design removes, is a finding. Second, the design: read the `Design` section against the whole change; a finding may name a design that removes an addition, a dependency, a copy of state, or a conversion, with what it changes on the three cost axes and its cost delta; the Orchestrator owns the rewrite. Replace the closing line "Question the decomposition given; do not propose another." with "Your verdict is advisory to the Orchestrator; do not rewrite the plan."
  In `dispatch-checklists.md`, extend the plan-review packet line so the packet includes the request as given.
  In `wave-integration/SKILL.md`, the "Draft-plan review" route line points at the snippet for the inputs instead of restating them, so the inputs have one home.
- acceptance:
  - The plan-review snippet's Inputs name the request as given; the Procedure has the enumeration bullet with both failure directions and the design bullet with the cost-delta finding shape, each within three sentences; the closing line no longer forbids naming an alternative and still keeps the rewrite with the Orchestrator.
  - The dispatch checklist's plan-review packet line includes the request as given.
  - The wave-integration route line no longer restates the inputs or says "No packet"; it names the snippet as their home.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From repo root: git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review vs acceptance; the obligations are enumeration and comparison tasks with named failure directions, not judgment prompts; the three input definitions agree; content test per lesson 2026-09-05"

### Task_4: Version bump and package validation
- type: chore
- owns:
  - plugins/coding-agent-orchestration-harness/.claude-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.codex-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.github/plugin/plugin.json
- depends_on: [Task_1, Task_2, Task_3]
- description: |
  Bump `version` from 0.20.0 to 0.21.0 in the three manifests and run the package validators over the completed tree.
- acceptance:
  - All three manifests read 0.21.0.
  - Package validation and the smoke tests pass on the tree containing Tasks 1 to 3.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py; python scripts/run_validation_smoke_tests.py; from repo root: git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "Final review of the whole diff against the Definition of Done, including the cross-file vocabulary match (section headings, term, and cost axes identical across the three skills; the Compatibility-stance pointer present)"

## Task Waves (explicit parallel dispatch sets)

Interpretation:
- Tasks listed in the same wave are intended to be dispatched in parallel by default, when `owns` are disjoint and dependencies are met.
- Waves are executed sequentially.

- Wave 1 (parallel): [Task_1, Task_2, Task_3]
- Wave 2 (parallel): [Task_4]

## Rollback / Safety
- Prose-only change on a feature branch; revert the branch. No data, scripts, or fixtures touched.

## Progress Log (append-only)

Append-only editing rule (applies to both logs below): when appending an entry, anchor the edit on the previous entry and reproduce it (or anchor on the section's tail marker) so the edit inserts rather than replaces, and verify afterward that the log grew.

- 2026-09-16 Plan drafted; lessons entry appended ("Requirements Added During Drafting Passed As The User's").
- 2026-09-16 Plan review round 1 (Claude Reviewer): NEEDS_REVISION; revised per Decision Log entry 2; delta re-review requested.
- 2026-09-16 Plan review round 2 (delta): APPROVED with one minor (the single-home consolidation was itself an unlisted planner-added requirement); folded in.
- 2026-09-16 Presented; ebigunso's correction (Decision Log entry 3) replans; full re-review requested.
- 2026-09-16 Plan review round 3 (full): NEEDS_REVISION, three majors; revised per Decision Log entry 4; delta re-review requested.
- 2026-09-16 Plan review round 4 (delta): APPROVED; one advisory design finding (refer to the section by rule instead of restating the heading in the Gate and snippet) declined for readability.
- 2026-09-16 Plan approved by ebigunso ("Approved, go ahead with Wave 1. Version bump can go to 0.21.0."); Wave 1 dispatched: [Task_1, Task_2, Task_3].
- 2026-09-16 Wave 1 completed: [Task_1, Task_2, Task_3], all done (Claude Workers).
  - Summary: rules 12 (3 sentences) and 13 (2 sentences) and both template sections (3 and 5 lines) in `plan-format`; two sentences on the Plan Gate bullet; the plan-review snippet gains the request input, the enumeration and design bullets (3 sentences each), and the new closing line; the dispatch-checklists packet line and the wave-integration route line agree with the snippet as the one home.
  - Validation evidence: Task_1 validate_plan.py on the fixture pass; all three `git diff --check` pass (the only warning is the pre-existing LF/CRLF notice on lessons.md).
  - Blockers/questions: none blocking. Task_1 asked whether the template's `- None` form should be a bare line; ruled: keep the instruction form, a bare line would copy as an already-empty section. Task_2 flagged lifecycle-gates.md; checked, it points at the SKILL.md bullet and restates nothing. Task_3 dropped "no changed-files list" from the route line since the packet line carries it; accepted.
  - Candidates: Task_3 lesson candidate (CRLF line endings defeat LF-pattern replacement in this repo): low-signal environment note, not promoted.
  - Follow-up decision: dispatch Wave 2 (Task_4 version bump and package validation), then final Reviewer over the whole diff.
- 2026-09-16 Wave 2 completed: [Task_4] done. Manifests 0.20.0 to 0.21.0; validate_harness_package.py pass; run_validation_smoke_tests.py pass; git diff --check pass. No blockers or questions. Follow-up: final Reviewer over the whole diff.
- 2026-09-16 Final review (fresh Claude Reviewer, whole diff): APPROVED. All required checks rerun independently and pass. One pre-existing minor: the snippet's Inputs line lacked the plugin root the packet line names; fixed by the Orchestrator in one phrase (within Task_3's file, completing the Definition of Done bullet that every input definition agrees). Closeout: plan moved to completed/, lessons path updated, committed on the feature branch, PR opened.

## Decision Log (append-only; re-plans and major discoveries)

- 2026-09-16 Decision: no validator for the new section.
  - Trigger / new insight: ebigunso's ruling, "automation comes last, per the discipline"; a tag a model writes is as easy to fake as the addition itself, so the Reviewer's independent enumeration is the check that carries weight.
  - Plan delta (what changed): Task list holds no validator or fixture task; Non-goals record it.
  - Tradeoffs considered: a structural check that each acceptance bullet carries a source tag (rejected: gives the Reviewer something to contradict but adds a tagging burden to every bullet of every plan).
  - User approval: yes (in session).
  - Record proposed: none (a scope ruling for this plan, not a durable design decision; the admission test in `durable-docs-authoring/references/adr.md` does not pass).
- 2026-09-16 Decision: revisions from plan review round 1.
  - Trigger / new insight: the Reviewer's enumeration found nine additions the plan's own `Planner-added requirements` section omitted, a third plan-review input definition in `wave-integration/SKILL.md:27` outside every `owns`, and a definition under which every rule-suite check reads as planner-added.
  - Plan delta (what changed): the section now lists each addition with its reason, and three additions were dropped rather than justified (a fixed template position, naming `plan-format` in the Plan Gate sentence, and "change nothing else" bullets already covered by the Worker contract); the definition excludes the repository's rule suite and lessons; Task_3 owns the wave-integration route line and makes the snippet the one home for the inputs; A1 and A2 corrected with the grep pattern named; ADR-D-0019 restated as scope; the lesson citation date corrected.
  - Tradeoffs considered: keeping the wave-integration line as a restatement and editing it in step (rejected: a second copy is the divergence that produced the finding).
  - User approval: pending with the plan.
  - Record proposed: none.
- 2026-09-16 Decision: the design question is in scope, not deferred.
  - Trigger / new insight: ebigunso, on the presented plan: the review and rewrite should not only surface additions and justify them, but verify the justifications against the bigger picture and question the design choices themselves, so the plan lands on the design thought best for the instance. The presented plan stopped at surfacing and justifying; a justified addition under the wrong design is still the wrong design.
  - Plan delta (what changed): Goal and Definition of Done extended; `plan-format` gains a design obligation (rule 13, `Design` section) with proportionality; the Plan Gate sentence covers the design comparison; the Reviewer snippet gains a design bullet with the cost-delta finding shape and its closing line changes from "do not propose another" to "do not rewrite the plan"; the alternatives-comparison item leaves Non-goals; this plan carries its own `Design` section as the first instance.
  - Tradeoffs considered: keeping "do not propose another" and asking the Reviewer only to test reasons (rejected: forbids the finding the correction asks for); a full checklist of design questions in a reference (rejected: the recommendation's shape, mechanics over obligation, and the file it names was thinned by ablation); the design obligation on every plan without proportionality (rejected: noise on one-file fixes, against rule 10).
  - User approval: pending with the plan.
  - Record proposed: none yet; if the Reviewer or ebigunso judges "plans land on the best design, not the first" a durable design decision, run the admission test in `durable-docs-authoring/references/adr.md` at closeout.
- 2026-09-16 Decision: no ADR.
  - Trigger / new insight: the final Reviewer ran the admission test on "a plan lands on the best design found, not the first": a plan that skips the comparison is caught by the next plan review, so the constraint belongs in a rule; the why is re-derivable from rules 12 and 13, the Plan Gate sentence, the lessons entry, and this Decision Log.
  - Plan delta (what changed): none.
  - Tradeoffs considered: none; the decision already sits at its home (rule plus lesson).
  - User approval: not needed (declining a record).
  - Record proposed: none.
- 2026-09-16 Decision: revisions from plan review round 3, and the Design D ruling.
  - Trigger / new insight: the Reviewer found the "fix-in-place and structural at minimum" pairing unlisted and unfit (a docs-only change has no structural design, so it forces a straw alternative); the plan's own Design section not in the shape it prescribes; and "consumers to migrate" duplicating rule 8's Compatibility stance. It also named Design D under the new obligation: carry the comparison in the existing Decision Log `Tradeoffs considered` field instead of a `Design` section.
  - Plan delta (what changed): the pairing is replaced by "at least one alternative that differs on a cost axis"; the axes are three, with consumers pointed at the Compatibility stance; the Design section rewritten in the fixed shape with the validator moved to a note; the recommendation's origin named in Context; the two proportionality ladders stated as coexisting; the wrong-proportional-line case routed to the design bullet; the "no mechanics" constraint sourced to #70.
  - Tradeoffs considered: Design D (rejected: the Decision Log is append-only replan history at the bottom of the plan, and the incident was a scan miss; the comparison must sit where the user's scan lands, beside the additions it justifies; its saving is one heading and two template lines); keying rule 13's trigger on architecture-gates' rigor tiers (rejected: different question, and it would couple plan-format to a file thinned by ablation).
  - User approval: pending with the plan.
  - Record proposed: none.

## Notes
- Risks: a drafting model tags nothing and names a straw alternative, and the Reviewer's enumeration and design check also miss; mitigation is the user's scan of two sections, and a second occurrence promotes the validator question (lessons entry residual risk). A same-family Reviewer may share the drafter's design blind spot; the cost-delta shape forces a concrete comparison rather than an opinion, and cross-family review remains the Orchestrator's dispatch choice.
- Edge cases: a requirement that comes from a document the request names, or from the rule suite or lessons, is not planner-added; the definition says so. A change whose proportional `Design` line is wrong (it does touch a contract) is a Reviewer finding under the design bullet: the design was not compared.
