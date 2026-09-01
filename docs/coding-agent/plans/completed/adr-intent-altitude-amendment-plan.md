# Plan: ADR Intent-Altitude Amendment

- status: done
- generated: 2026-09-01
- last_updated: 2026-09-01
- work_type: docs

## Goal

- The shipped ADR discipline (`durable-docs-authoring`) states what an ADR's content is: design intent, recorded self-containedly at intent altitude, never mirroring implementation wording — closing the gap that allowed an ADR proposal to be drafted as a norm restatement or as a deferral to implementation text.

## Definition of Done

- `durable-docs-authoring` carries the intent-altitude content principle in one compact addition (target: one to two sentences, placed where drafting guidance already lives).
- The amendment contains no mention of implementation pointers/side notes (deliberate omission: naming them nudges models toward writing them).
- The amendment reads as a drafting rule for new records, not a retroactive defect-finding over the existing ADR corpus.
- No change to warrant criteria: whether to record stays governed solely by the existing root test.
- Package validators pass; plugin version bumped per release convention.

## Scope / Non-goals

- Scope: `durable-docs-authoring` skill prose (amendment + consistency pass over its references), package validation, version bump.
- Branch: work on a new branch (`adr-intent-altitude-amendment`), separate from the compat-and-test-scope-guidance work.
- Non-goals:
  - No addition to the warrant criteria's existing-records negatives (shipped prose is implementation, never a substitute record for intent — earlier idea withdrawn).
  - No pointer/side-note clause in the amendment.
  - No rewrite or audit of existing ADRs in this repo's corpus.
  - No changes to other skills; the intent-altitude principle applied to the compat/test ADR itself is owned by the compat-and-test-scope-guidance plan (Task_1 there).

## Context (workspace)

- Related files/areas:
  - `plugins/coding-agent-orchestration-harness/skills/durable-docs-authoring/references/adr.md` (primary target — warrant, homes, collaboration flow)
  - `plugins/coding-agent-orchestration-harness/skills/durable-docs-authoring/references/adr-template.md` and `references/authoring-rules.md` (consistency check only)
- Existing patterns or references:
  - `adr.md` "Three homes" already implies the division (ADR = why/alternatives/revisit conditions); the amendment makes the content principle explicit.
  - Origin: discussion 2026-09-01, logged in `docs/coding-agent/plans/active/compat-and-test-scope-guidance-plan.md` Decision Log ("ADR content principle — intent altitude, not norm deferral").
- Repo reference docs consulted: `docs/coding-agent/rules/common.md`, `plugins/coding-agent-orchestration-harness/README.md`.

## Design summary (agreed in discussion)

- Principle to encode: ADRs record design intent self-containedly at intent altitude; they do not mirror implementation wording, whether that implementation is code or normative prose. Intent, stated well, remains valid under any implementation rewording that preserves it.
- Asymmetry retained from the discussion: the record must be complete on intent, premises, rejected alternatives, and revisit conditions — brevity never trims the why.
- Deliberate omissions: no pointer/side-note allowance (attractor risk: naming pointers invites writing them); no new warrant negatives.

## Open Questions (max 3)

- Q1: Exact placement — extend "Three homes" (content division already lives there) or the collaboration flow's drafting step? Proposed: Three homes; Worker confirms against the file's flow and states the choice in the report.

## Assumptions

- A1: One to two sentences suffice; if drafting pressure pushes beyond that, the addition is over-scoped — stop and re-check against the design summary rather than expanding.
- A2: Version bump is a patch-level release per the existing `vX.Y.Z` convention (single-skill prose clarification); adjust if release convention says otherwise.

## Tasks

### Task_1: Amend durable-docs-authoring with the intent-altitude content principle

- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/durable-docs-authoring/
- depends_on: []
- description: |
  Add the content principle to `references/adr.md` per the design summary (placement per Q1 resolution).
  Consistency pass over `adr-template.md` and `authoring-rules.md`: reword only if a passage actively invites norm restatement or deferral-to-implementation; otherwise leave untouched.
  Keep the amendment free of pointer/side-note language and free of any retroactive judgment on the existing corpus.
- acceptance:
  - Amendment states: intent altitude, self-contained, no mirroring of implementation wording (code or prose alike); completeness on intent/premises/alternatives/revisit conditions is preserved or restated.
  - No pointer/side-note clause anywhere in the diff.
  - Warrant criteria section unchanged.
  - Diff outside `adr.md` is minimal or empty.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "python scripts/validate_harness_package.py (from plugins/coding-agent-orchestration-harness/)"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review vs acceptance; adversarial read: does any added sentence nudge toward writing pointers, restating norms, or auditing old ADRs?"

### Task_2: Release pass

- type: review
- owns:
  - plugins/coding-agent-orchestration-harness/.claude-plugin/
  - plugins/coding-agent-orchestration-harness/README.md
- depends_on: [Task_1]
- description: |
  Run full package validators; bump plugin version per release convention (A2); update README only if it enumerates the changed sections.
- acceptance:
  - Reviewer status is APPROVED on the combined diff.
  - All package validators pass; version bumped consistently with convention.
- validation:
  - kind: command
    required: true
    owner: reviewer
    detail: "python scripts/validate_harness_package.py && python scripts/run_validation_smoke_tests.py (from plugins/coding-agent-orchestration-harness/)"
  - kind: review
    required: true
    owner: reviewer
    detail: "Combined diff review."

## Task Waves (explicit parallel dispatch sets)

Interpretation:

- Tasks listed in the same wave are intended to be dispatched in parallel by default, when `owns` are disjoint and dependencies are met.
- Waves are executed sequentially.

- Wave 1 (parallel): [Task_1]
- Wave 2 (parallel): [Task_2]

## Rollback / Safety

- Docs-only change on its own branch; revert is dropping/reverting the branch before merge, or a clean `git revert` after.

## Progress Log (append-only)

- 2026-09-01 Wave 1 completed: [Task_1]
  - Summary: Two-sentence intent-altitude principle added to references/adr.md in "Three homes", after the home bullets (Q1 resolved there: that section owns the content division; the collaboration flow delegates authorship, not content). adr-template.md and authoring-rules.md checked, deliberately untouched (nothing invites norm restatement or deferral-to-implementation). Diff: 3 inserted lines; warrant criteria unchanged; no pointer/side-note language; drafting-rule register.
  - Validation evidence: validate_harness_package.py pass (worker).
  - Notes: A1 size guard held — exactly two sentences, one per line.

- 2026-09-01 Wave 2 completed: [Task_2]
  - Summary: Reviewer APPROVED with zero findings; adversarial read confirmed no pointer nudges, no norm-restatement nudges, no retroactive-audit register, coherence with homes-as-complements, and correct Q1 placement. Version bumped 0.12.0 -> 0.12.1 across all three runtime manifests; README re-confirmed to need no update.
  - Validation evidence: validate_harness_package.py pass (pre- and post-bump), run_validation_smoke_tests.py exit 0, git diff --check clean.
  - Notes: none.

## Decision Log (append-only; re-plans and major discoveries)

- 2026-09-01 Decision: Split the amendment out of the compat-and-test-scope-guidance plan onto its own branch.
  - Trigger / new insight: user ruling — separate plan, new branch; and the pointer/side-note clause is dropped from the amendment (naming pointers would nudge models toward writing them when unneeded).
  - Plan delta (what changed): this plan created; pointer clause moved from amendment content to an explicit non-goal.
  - Tradeoffs considered: folding into the other plan (rejected: unrelated owns, independent release).
  - User approval: yes (discussion, 2026-09-01)

- 2026-09-01 Decision: Stack this branch on compat-and-test-scope-guidance for PR submission; version becomes 0.13.1.
  - Trigger / new insight: user requested PRs for both plans via gh stack; stacking amendment on top of compat resolves the forecast manifest conflict at restack time instead of merge time.
  - Plan delta (what changed): branch rebuilt on top of the compat branch; version bump re-resolved 0.12.1 -> 0.13.1 (patch on top of compat's 0.13.0) across all three manifests; Wave 2 progress entry's "0.12.0 -> 0.12.1" reflects the pre-stack state.
  - Tradeoffs considered: independent PRs from main (rejected: guaranteed manifest merge conflict for whichever lands second).
  - User approval: yes (user message requesting stacked PRs, 2026-09-01)

## Notes

- Risks:
  - Over-writing: the principle is one idea; the main failure mode for this change is expanding it into a section. A1 is the guard.
  - The two active plans both bump the plugin version on separate branches; whichever merges second resolves the version/README conflict at merge time (mechanical).
- Edge cases:
  - `adr-template.md` has a Decision section; the consistency pass must not weaken it — under the intent principle the Decision section states the decision fully at intent altitude, which is not norm-mirroring.
