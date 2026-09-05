# Plan: Plan Review Gate

- status: done
- generated: 2026-09-06
- last_updated: 2026-09-06
- work_type: docs

## Goal
- Draft plans get an independent review before user approval, using references the Reviewer already loads, with the plan-quality judgment lines that have no portable home today added where the plan author sees them.

## Definition of Done
- The Plan Gate states that plan-mode work is reviewed before user approval under the same waiver as the plan itself, and the lifecycle reference describes the review loop and its escalation by pointing at the existing delta-review condition, third-bounce detector, and Escalation Ruling.
- A plan-review prompt snippet exists in `subagent-strategy`. Reachability is proven in Task_6 by dispatching a Reviewer with the landed snippet, given only a plan file and Researcher output, and confirming it reached every reference it needed. The pre-approval live test on this plan exercised a draft packet, not the landed snippet, and is recorded as such.
- The plan template carries three new slots (assumption source, design-record acceptance, hypothesis and falsifier) and `validate_plan.py` still passes on the existing fixture unchanged.
- All three Reviewer adapters admit a draft plan as the review artifact and name the validator pass as its required evidence; instruction bodies diff clean outside runtime-specific blocks.
- Net added text across all files is at most thirty physical lines in the diff, counted after equal-length replacements; every added line passes the content test: the agent could not get it from tool help, plain knowledge, or a reference it already loads.
- This plan itself was reviewed before approval, and the Decision Log records what that review changed.

## Scope / Non-goals
- Scope: the twelve files listed under Tasks; the review loop text; the live plan-review test on this plan.
- Non-goals:
  - No new reference file. A `plan-format/references/plan-review.md` was considered and rejected: nothing in the Reviewer's load path would read it, and the snippet is the real entry point.
  - No validator change. Prose slots are not checked mechanically; the repo's own lesson says validators overfit prose.
  - No rule-file edits. Repo rules stay as they are; rule candidates from the reviews are recorded in the Decision Log for closeout.
  - No ADR. See A3.
  - No change to what the Worker-wave Reviewer does after implementation.
  - No direct route to `long-horizon-audit.md`. Its header forbids standard-flow loading, and the consumer-naming check it would add is already in core-principles.

## Compatibility stance
- surface: plan template slots; Reviewer adapter instruction bodies and description fields; `plan-format` core rules.
- stance: preserve
- justification: locatable consumers are the existing plans under `docs/coding-agent/plans/` in this and sibling repositories, and the three runtime adapters. New template slots are additive and unvalidated, so existing plans stay valid. Adapter changes add one sentence and one description clause and change no names, tools, or output format keys.

## Context (workspace)
- Related files/areas:
  - `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/SKILL.md` (Plan Gate, lines 33-42)
  - `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/lifecycle-gates.md` (Plan Gate Details, lines 19-41)
  - `plugins/coding-agent-orchestration-harness/skills/plan-format/SKILL.md` (design assumption "reviewed by humans", line 11; core rules)
  - `plugins/coding-agent-orchestration-harness/skills/plan-format/references/plan-template.md` (Context line 38 "Repo reference docs consulted", Assumptions line 46)
  - `plugins/coding-agent-orchestration-harness/skills/plan-format/references/execution-plan-lifecycle.md` (Create at line 13, Approve at line 22)
  - `plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/SKILL.md` (routing list, lines 33-39)
  - `plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/core-principles.md` (anti-pattern list, lines 136-145)
  - `plugins/coding-agent-orchestration-harness/skills/subagent-strategy/references/prompt-snippets.md` (Reviewer snippets from line 64)
  - `plugins/coding-agent-orchestration-harness/skills/subagent-strategy/references/dispatch-checklists.md` (Reviewer dispatch checklist, line 46; changed-files line 50)
  - `plugins/coding-agent-orchestration-harness/agents/Reviewer.md`, `claude/agents/harness-reviewer.md`, `codex/agent-templates/harness_reviewer.toml` (description line 3/3/2; opening paragraph line 12/13/8; validation evidence step 3 at `agents/Reviewer.md:81-82`)
- Existing patterns or references:
  - Third-bounce detector and delta-review condition: `skills/wave-integration/references/integration-checklist.md` lines 58 and 73.
  - Escalation ruling: `lifecycle-gates.md` line 67.
  - Same-wave conditions including producer/input dependencies: `skills/plan-format/references/task-waves.md` lines 20-31.
  - Model routing for detail versus design review tiers: `skills/subagent-strategy/references/model-routing.md` lines 14-15, 25-26.
  - Adapter replication rule: `skills/runtime-adapter-contract/SKILL.md` lines 21-23.
  - Existing local form of the mechanizing-judgment rule: `docs/coding-agent/rules/reviewer.md:13`, `docs/coding-agent/rules/orchestrator.md:15`, `docs/coding-agent/lessons.md` 2026-05-11. Task_3 promotes it to portable guidance; it is not new.
- Design record consulted and deviations from its acceptance: `docs/coding-agent/lessons.md` (plan-stage root causes 2026-04-28 through 2026-09-05); `CharacterMemory/docs/coding-agent/lessons.md` and `CharacterMemoryEvals/docs/coding-agent/lessons.md` (plan-stage root causes); `CharacterMemory/docs/coding-agent/skill-candidates.md` 2026-07-23 value-audit trigger entry; `CharacterMemoryEvals/docs/audits/2026-09-02-harness-design-value-audit.md` (strictness follows the claim). Deviation: none. The skill-candidates entry's "design review" trigger point was deliberately not promoted in v0.9.0 as duplicating Plan Gate text; this plan adds no audit route and no new trigger, so that disposition stands.

## Shared wording (Task_2 and Task_4 implement against this text, not against each other)
- Assumptions slot line: `- A1: <claim> — source: <file:line | design record path | unverified, checked by Task_N>`
- Context slot line (replaces "Repo reference docs consulted:"): `- Design record consulted and deviations from its acceptance:`
- Hypothesis slot line: `- Hypothesis (only for fix-shaped plans where the cause is not yet established): <cause> ; falsified by: <observation>`
- Plan-review snippet body (Task_4 lands this under a `## Reviewer snippet (plan review)` heading; `<plugin root>` and `<plan>` are filled by the Orchestrator):

```
Scope:
- Review the draft plan at <plan> before user approval. The artifact is the plan file, not a diff.
- Inputs: the plan; Researcher output at <path or "none">.

Procedure:
- Run `python <plugin root>/skills/plan-format/scripts/validate_plan.py --file <plan> --mode balanced` first. Its pass output is the required validation evidence; do not re-check by hand what it checks.
- Read `<plugin root>/skills/plan-format/SKILL.md` and `references/task-waves.md`; apply `<plugin root>/skills/engineering-quality-baselines/SKILL.md` per its plan-review routing entry.
- Open every source an Assumption or Context claim names and confirm it says what the plan says.

Deliverables:
- Each finding names the fact, record, or reference it contradicts.
- Your verdict is advisory to the Orchestrator. Question the decomposition given; do not propose another.
```

## Open Questions (max 3)
- (none; Q1 resolved in the Decision Log)

## Assumptions
- A1: The Claude Reviewer adapter preloads `engineering-quality-baselines`; the Copilot and Codex adapters load it only when prompted, which the snippet's routing line does — source: `claude/agents/harness-reviewer.md:6-8`; `agents/Reviewer.md:36`; `codex/agent-templates/harness_reviewer.toml:32`.
- A2: No current Reviewer adapter or dispatch reference routes to `plan-format` — source: the three adapters; `skills/orchestration-harness/references/dispatch-guidance.md` Reviewer Dispatch. Absence of an explicit route, not proof no custom dispatch could load it.
- A3: This decision does not warrant an ADR — source: `skills/durable-docs-authoring/references/adr.md` re-derivability negative at line 29, cheap-reversal severity conjunct at line 12, always-loaded enforcement text at line 26. The product-domain exception at line 28 applies to this repository, so the subject matter alone does not exclude an ADR; the re-derivability and severity tests are what exclude it. Confirmed by two reviewers.
- A4: `validate_plan.py` does not parse the Assumptions or Context section bodies — source: `skills/plan-format/scripts/validate_plan.py:13` and `:141` by inspection. The fixture run in Task_2 is the compatibility check, not the evidence for this claim.

## Tasks

### Task_1: Plan Gate and review loop text
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/lifecycle-gates.md
- depends_on: []
- description: |
  In SKILL.md Plan Gate, add one bullet: plan-mode work is reviewed by a Reviewer before user approval, under the same waiver as the plan, using the `subagent-strategy` plan-review snippet.
  In lifecycle-gates.md Plan Gate Details, add one short paragraph: the Orchestrator triages each finding as fix, research-and-rewrite, or dispute; re-review is delta-scoped only when the delta-review condition in `wave-integration/references/integration-checklist.md` holds, otherwise full; a third round on the same seam applies the third-bounce detector; a finding that needs a ruling follows the Escalation Ruling procedure.
- acceptance:
  - SKILL.md Plan Gate gains exactly one bullet and no other section changes.
  - lifecycle-gates.md gains one paragraph under Plan Gate Details that names the delta-review condition, third-bounce detector, and Escalation Ruling by reference, not by restating them.
  - No sentence restates content already in `wave-integration`, `engineering-quality-baselines`, or the Escalation Ruling section.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness: python scripts/validate_harness_package.py; from repo root: git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "Content test per line; pointer-not-restatement check"

### Task_2: plan-format slots and rules
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/plan-format/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/plan-format/references/plan-template.md
  - plugins/coding-agent-orchestration-harness/skills/plan-format/references/execution-plan-lifecycle.md
- depends_on: []
- description: |
  SKILL.md: replace the design assumption "reviewed by humans" with "reviewed by a Reviewer, then approved by the user"; add one core rule: a plan states what, why, and constraints, and leaves how to the Worker; it does not restate what the Worker can discover cheaply. This does not override user-requested decomposition depth (existing rule 9).
  plan-template.md: replace the Assumptions example line and the "Repo reference docs consulted:" line with the Shared-wording slot lines; add the Hypothesis slot with its condition stated inline.
  execution-plan-lifecycle.md: insert a "Review" step between Create and Approve: Reviewer per the plan-review snippet; Decision Log records what the review changed.
- acceptance:
  - The three slot lines match the Shared wording section verbatim, including the Hypothesis condition.
  - The existing fixture still validates.
  - Net additions across the three files are at most seven physical lines (raised from six by the Wave 1 ruling in the Progress Log).
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness: python skills/plan-format/scripts/validate_plan.py --file tests/fixtures/valid-plan.md --mode balanced; python scripts/validate_harness_package.py; git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "Slot wording verbatim against this plan; content test per added line"

### Task_3: quality-baselines routing and anti-patterns
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/references/core-principles.md
- depends_on: []
- description: |
  SKILL.md routing list: add one entry: plan review reads `core-principles.md` and the review-rubric 30-second pass only; no scorecard, no latent-risk routing.
  core-principles.md anti-pattern list: add two bullets: enumeration from the ticket (case lists, vocabularies, or validation matrices built from the finding's citations instead of the producer's full branch set); mechanizing judgment (validators or gates for prose quality, design taste, or other properties that need a reader).
- acceptance:
  - One routing entry and two anti-pattern bullets, matching the surrounding list style.
  - No other section changes.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness: python scripts/validate_harness_package.py; git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "Bullets are generalized, not repo-specific; content test per line"

### Task_4: plan-review snippet and packet line
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/subagent-strategy/references/prompt-snippets.md
  - plugins/coding-agent-orchestration-harness/skills/subagent-strategy/references/dispatch-checklists.md
- depends_on: []
- description: |
  prompt-snippets.md: add `## Reviewer snippet (plan review)` with the Shared-wording snippet body verbatim, placed before the existing Reviewer snippets, in the same heading style (no code fence).
  dispatch-checklists.md Reviewer dispatch checklist: add one line: for plan review, the packet is the plan path, the Researcher output path, and the plugin root; no changed-files list.
- acceptance:
  - Snippet body matches the Shared wording section verbatim.
  - Checklist line added; nothing else in the file changes.
  - Package validator still finds the latent-risk snippet.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness: python scripts/validate_harness_package.py; git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "Nothing restated that adapters or loaded references already say"

### Task_5: Reviewer adapters admit a draft plan
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/agents/Reviewer.md
  - plugins/coding-agent-orchestration-harness/claude/agents/harness-reviewer.md
  - plugins/coding-agent-orchestration-harness/codex/agent-templates/harness_reviewer.toml
- depends_on: []
- description: |
  In each adapter's opening paragraph append one sentence: the review artifact may also be a draft plan before approval; then diff-first steps do not apply, the dispatch snippet governs, and the plan validator's pass output is the required validation evidence for step 3. Extend the description field's first sentence with "or a draft plan before approval". Keep the three copies identical outside runtime-specific blocks per `runtime-adapter-contract`.
- acceptance:
  - One sentence and one description clause per adapter, same wording in all three.
  - Instruction bodies diff clean outside intentional runtime-specific blocks.
  - No tool list or output-format key changes.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness: python scripts/validate_harness_package.py; diff of the three instruction bodies recorded in the report; git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "Three-copy sync confirmed per runtime-adapter-contract"

### Task_6: Final review and snippet reachability test
- type: review
- owns: []
- depends_on: [Task_1, Task_2, Task_3, Task_4, Task_5]
- description: |
  Review the whole diff against the Definition of Done, including the line budget and the content test across all files.
  Reachability test: the Orchestrator dispatches a Reviewer with the landed snippet only (plugin root and this plan's path filled in, Researcher output "none") and the Reviewer reports which references it loaded and whether any needed reference was unreachable.
- acceptance:
  - Reviewer status APPROVED.
  - Net added lines across all files at most thirty physical lines; each line passes the content test.
  - Reachability test report lists every loaded reference and no unreachable one.
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review vs Definition of Done; line count, content test, and reachability report recorded"

## Task Waves (explicit parallel dispatch sets)

Interpretation:
- Tasks listed in the same wave are intended to be dispatched in parallel by default, when `owns` are disjoint and dependencies are met.
- Waves are executed sequentially.

- Wave 1 (parallel): [Task_1, Task_2, Task_3, Task_4, Task_5]
  - Parallelism discharged: `owns` are disjoint, and no task consumes another task's output; all cross-task wording is pinned in the Shared wording section above.
- Wave 2 (parallel): [Task_6]

## Rollback / Safety
- All changes are text in tracked files; revert the commit.

## Progress Log (append-only)

Append-only editing rule (applies to both logs below): when appending an entry, anchor the edit on the previous entry and reproduce it (or anchor on the section's tail marker) so the edit inserts rather than replaces, and verify afterward that the log grew.

- 2026-09-06 Wave 1 completed: [Task_1, Task_2, Task_3, Task_4, Task_5]
  - Summary: five Claude Workers in parallel; all status done. Orchestrator ruling on Task_2's question: blank line after the "## 1b) Review" heading allowed for style consistency (applied by Orchestrator).
  - Validation evidence: validate_harness_package.py pass; run_validation_smoke_tests.py pass; validate_plan.py on tests/fixtures/valid-plan.md pass; git diff --check clean; git diff --numstat added 38 deleted 9 net 29 across 12 files (thirteenth file, task-waves.md, unchanged by design).
  - Notes: Reviewer-owned content-test items pending Task_6.
- 2026-09-06 Wave 2 completed: [Task_6]
  - Summary: two dispatches. Reachability test (Claude harness-reviewer, landed snippet only): APPROVED, nothing unreachable, one wasted latent-risk read, four minor plan-doc findings fixed in place; report at `.agent-work/reviewer/plan-review-gate-reachability.md`. Final diff review (Codex agent-harness-reviewer over agmsg): APPROVED, no findings; report at `.agent-work/reviewer/plan-review-gate-final-review.md`.
  - Validation evidence: Codex independently reran validate_harness_package.py, run_validation_smoke_tests.py, fixture validate_plan.py, git diff --check (all pass); exact-string comparison of snippet and slot lines against Shared wording; three-adapter body and description equality; net 29 lines measured by numstat; content test recorded per added line.
  - Notes: Task_2 landed at seven lines under the Wave 1 ruling; acceptance amended to match.

## Decision Log (append-only; re-plans and major discoveries)

- 2026-09-06 Decision: no new reference file; distribute across existing load paths.
  - Trigger / new insight: tracing the Reviewer load path showed nothing reads `plan-format/references`; the dispatch snippet is the entry point and the quality-baselines routing list is the existing mechanism for "which reference for which review kind".
  - Plan delta (what changed): the earlier proposal of `plan-format/references/plan-review.md` with pointer lines is dropped; the new judgment lines land as template slots and core rules where the plan author sees them.
  - Tradeoffs considered: a single checklist file is easier to find by a human but adds a second hop for the agent and duplicates prose that drifts.
  - User approval: yes (chat, 2026-09-06, "Seems good. Draft the plan.").
- 2026-09-06 Decision: Research waived: context gathered in-session during the assessment turns at user direction across this repo and the two CharacterMemory repos; no Researcher dispatched.
- 2026-09-06 Decision: pre-approval plan review, two dispatches (Q1 resolved by user direction): Claude `harness-reviewer` subagent and Codex `agent-harness-reviewer` over agmsg, both NEEDS_REVISION. Reports: Claude in session transcript; Codex at `.agent-work/reviewer/plan-review-gate-review.md`.
  - Trigger / new insight: both reviews independently found the same three majors: the routing entry sent standard-flow review into `long-horizon-audit.md` against that file's own header; the snippet's validator command assumed this repository's layout; the line budget could not be met and the DoD claimed reachability the live packet did not test. Codex additionally found that unconditional delta re-review dropped the existing applicability condition. Both flagged six restated lines under the content test, the template slot that should replace rather than add, the adapter evidence gap for step 3, and line-number nits. Codex noted the task-waves addition duplicated the existing producer-dependency rule at line 31 and that the mechanizing-judgment bullet is a promotion of a local rule, not new.
  - Plan delta (what changed): long-horizon route dropped and recorded as a non-goal; delta re-review now conditional on the existing condition; snippet cut to nine lines with `<plugin root>` placeholders and a pointer to task-waves instead of a restated rule; task-waves.md removed from Task_2 owns; Context slot is a replacement; Hypothesis condition narrowed to fixes without an established cause; Task_5 names step 3 evidence and may edit the description field; Task_6 gains the reachability test as the evidence for DoD line 2; budget convention fixed at thirty physical lines; file count corrected to thirteen; A1, A3, A4 re-scoped; line citations corrected.
  - Disputed: none. Accepted with amendment: Codex's point that Task_5 could be zero net lines by appending to paragraphs is adopted as the counting convention.
  - Rule and lesson candidates carried to closeout: (1) when a plan adds a pointer or routing entry, the source check covers the target's admission clause and confirms the target is in some task's `owns` or unchanged (Claude); (2) a live test proves only the packet actually dispatched; record the tested text and claim only the reachability exercised (Codex).
  - User approval: yes (chat, 2026-09-06, "Looks good. Get to work.").
- 2026-09-06 Decision: Task_6 review round, fix-class only, no re-review needed (delta-review condition holds: plan-doc and one snippet-line edits, no new contracts or surfaces).
  - Trigger / new insight: the reachability test found the snippet's `engineering-quality-baselines` reference carried no path, so Copilot and Codex Reviewers would have to derive it; and four plan-doc mismatches (Task_2 cap not amended after the ruling, Hypothesis line not the landed form, one line citation, an overclaimed non-goal).
  - Plan delta (what changed): snippet line now names `<plugin root>/skills/engineering-quality-baselines/SKILL.md` in both Shared wording and prompt-snippets.md; Task_2 acceptance raised to seven citing the ruling; Hypothesis line replaced with the landed form; citation fixed; non-goal softened to "no direct route"; Scope corrected to twelve files.
  - Lesson candidates carried to lessons.md at closeout: (1) pointer targets' admission clauses are part of the source check (Claude, plan review); (2) claim only the reachability actually exercised (Codex, plan review); (3) a ruling that changes an acceptance bullet amends the bullet in the same edit (Claude, reachability test).
  - User approval: not required (fix-class within approved scope).

## Notes
- Risks: the added template slots could be filled ritually; the reviewer's source check is what keeps them honest.
- Edge cases: the Hypothesis slot applies only to fix-shaped plans without an established cause; the template states the condition inline so other plans do not grow an empty slot.
