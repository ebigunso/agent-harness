# Plan: ADR Discipline Integration (criteria, template, bootstrap placement)

- status: done
- generated: 2026-07-23
- last_updated: 2026-07-23
- work_type: docs

## Goal
- Give the harness a corpus-calibrated ADR discipline: unconditional warrant criteria with a three-home decision model (ADR / rule / Decision Log), a collaboration flow that drafts with the user and persists only on approval, a CM-derived default template used only where no repo convention exists, and bootstrap-time convention detection with optional user-approved template placement — configured through repo-rule pointer lines, never a second config surface.

## Definition of Done
- All Normative scope items landed at their homes with required wiring; every event-triggered rule has an explicit imperative route at its binding moment (no reliance on semantic skill selection).
- The warrant criteria implement the root-test-first structure (2026-07-24 Decision Log entry); the template content is faithful to the companion survey's accepted patches (`adr-corpus-survey.md`, same folder — its five criteria survive as recognition signals).
- Version 0.10.0 in all three manifests; full validator set green; Codex Reviewer APPROVED against the trigger-chain, budget, and survey-fidelity bars.

## Scope / Non-goals
- Scope: new/extended reference content in `durable-docs-authoring`, `rulebook`, and `orchestration-harness` references; manifests.
- Non-goals: repo-side pointer lines for CM/agent-harness and any CME bootstrap conversation (post-merge follow-ups in those repos); authoring CME's five identified foundational ADRs (optional later work, user-initiated); adopting the template patches back into CM's own template (their call, later); adapter edits; report-contract changes (workers never author decision records — owned by model-routing); any placement automation script (placement is an orchestrator file-write during the interactive bootstrap; automation-last).

## Context (workspace)
- Companion evidence: `docs/coding-agent/plans/active/adr-corpus-survey.md` — 56-ADR classification (55/56 draft-criteria recall; the exception drives the negative criteria), CME negative-space analysis (three-home boundary), template-pattern findings (notably 0/56 supersedes-field usage).
- Design discussion: user-approved shape 2026-07-23 — criteria/format split; pointer-not-mirror config; CM-based template; bootstrap placement gated on user approval; steady state is always a pointer into the repo.
- Constraints: v0.9.1 wiring discipline (imperative routes at binding moments; always-read budget weighed hardest); rule-writing-style evidenced scope; skills-maintenance final ambiguity pass before completion.

## Open Questions (max 3)
- None. Content decisions are fixed below; wording authority within them is delegated to the Claude authoring tasks.

## Assumptions
- A1: Minor version bump (0.10.0) — new content surface, no contract changes.
- A2: No prose-pass task needed: all authoring is Claude-side per model routing; the Codex roles in this plan are review-only.

## Normative scope

### Task_1 (durable-docs-authoring; Claude-authored)
1. New `references/adr.md` (~40 lines), three sections:
   - Warrant criteria, root-test-first (user-directed reframing 2026-07-24): the warrant is a single counterfactual over the decision's reasoning, premises, and boundaries — record an ADR when losing the reasoning, and the fact that it was a decision point at all, is expected to make future work handle the decision wrongly in any of three modes: VIOLATE it while its premises hold; wrongly PRESERVE it after its premises expire (ossification — the record's Decision Drivers and Revisit When are what make legitimate reversal safe); or wrongly EXTEND it beyond its deliberately bounded scope (over-application — the boundary's rationale is as loseable as the decision's). Every ADR proposal must state the expected mishandling concretely, naming its mode ("without this record, future work would likely do X against/past/beyond Y"). The survey's five criteria demote to recognition signals for where the test usually fires — (a) externally observable or cross-boundary contract/authority/evidence-ownership shapes with tempting alternatives, (b) rejected alternatives likely to be re-proposed, (c) meaningful migration/reversal cost, (d) cross-repository obligations, (e) user rulings establishing durable governance defaults (authorship is provenance, not warrant); plus the two mirror-mode signals: (f) decisions resting on premises likely to expire, (g) decisions whose scope boundary is as deliberate as the decision — signals prompt the test; they are not independently sufficient. Negatives are derivable and stated as such: no ADR where nothing ongoing can be contravened (reversible measured parameters — the invariant may warrant, the numbers are evidence; expired deferrals and task sequencing; ordinary tactics) or where the record already exists (another repository's ADR — link instead; always-loaded enforcement rules whose rationale burden is genuinely local).
   - Three-home model: ADR = why + rejected alternatives + revisit conditions outliving the plan; rule = executable enforcement read every task; Decision Log = plan-scoped record. ADR-plus-rule pairs are the expected shape for enforced contracts; the homes are complements, never substitutes.
   - Collaboration flow: on the root test firing, state the triggering signal, proposed title, AND the expected mishandling scenario (mode named: violate / wrongly preserve / wrongly extend) in-conversation, recording all three in the plan Decision Log in the same action; draft via the writing-strength side (cross-reference `subagent-strategy/references/model-routing.md`; do not duplicate its authorship clause); persist nothing until the user approves; decline is terminal and Decision-Log-recorded. Format resolution: repo pointer if present, else the default template. Amendment and lifecycle policy: wording clarifications may amend in place with a revision note; changed authority/behavior requires a superseding ADR with `supersession_scope` and reciprocal frontmatter updates on the superseded ADR. On FULL supersession or retirement, one atomic operation: set frontmatter status, move the file to `docs/decisions/superseded/` renamed with a self-describing suffix (`--superseded-by-ADR-X-NNNN` or `--retired`), update every inbound reference to the new path, and prove link repair with an absence search for the old filename. Partial supersession never moves the file — the ADR remains authoritative for its surviving clauses in place. IDs are never reused; numbering gaps in active directories are meaningful.
2. New `references/adr-template.md` (~60 lines): the CM `docs/decisions/template.md` structure generalized and patched per the survey's accepted findings — frontmatter `status, adr_type, date, deciders, consulted, informed, supersedes, superseded_by` plus new `warrant:` (signal letters a–g, with the mishandling mode named) and optional `depends_on`/`implements` and `supersession_scope: full|partial` (`supersedes`/`superseded_by` carry current relative paths, updated when archive moves rename files); sections Context and Problem Statement → Decision Drivers → Decision → optional Product/Philosophy Relevance → optional Implementation Impact → Considered Options (with a marked likely-to-be-re-proposed option and its reopen condition) → Decision Outcome → Consequences (positive / negative-tradeoffs) → optional Decision Boundary (invariant vs calibrated defaults; also the home for deliberately bounded scope and its rationale — the wrongly-extend guard) → optional Measurement Basis → Validation → Revisit When (load-bearing for the wrongly-preserve mode: state the premise whose expiry reopens the decision) → optional one-line Consultation impact → More Information. Notes: `consulted` records durable identities (model/person names, no roles/platforms); two-track D/I layout with per-track numbering is the default, single-track collapse permitted. Authored as a drop-in file (placeable verbatim at `docs/decisions/template.md`).
3. New `references/adr-repo-readme.md` (~30 lines): generalized CM decisions-README as a drop-in for `docs/decisions/README.md` — layout including the `superseded/` archive (single flat folder; track prefixes preserve identity; entries renamed `--superseded-by-ADR-X-NNNN` / `--retired`; active directories list only governing decisions and numbering gaps signal archived history; partial supersession stays in place), per-track numbering with never-reused IDs, track-selection criterion generalized (design track when overlooking the decision risks violating the project's core philosophy; implementation track for how-it's-built), pointer to `template.md`.
4. `SKILL.md`: one route line for decision records → `references/adr.md`; frontmatter description gains ADR/decision-record trigger vocabulary (it already claims ADR-adjacent prose; make the noun explicit).

### Task_2 (rulebook + orchestration-harness wiring; Claude-authored)
1. `rulebook/references/rules-files.md`: common.md structure gains an optional Decision Records line with the two forms — `Decision records: follow <path>; match the existing ADRs' numbering and sections.` / `Decision records: no repo convention — harness default template applies (durable-docs-authoring references/adr.md).`
2. `rulebook/references/rule-suite-templates.md`: matching template line for fresh suites.
3. `rulebook/references/bootstrap-lifecycle.md`: bootstrap step — detect candidate conventions (`docs/decisions/`, `docs/adr/`, `ADR-*` globs); ALWAYS propose to the user and confirm, never silently record. Three outcomes: (i) convention detected → pointer at it; (ii) none + placement approved → orchestrator copies `adr-template.md` → `docs/decisions/template.md` and `adr-repo-readme.md` → `docs/decisions/README.md` (track dirs created on first ADR), pointer then reads as case (i); (iii) none + placement declined → pointer records harness-default mode; re-offer only at rule-suite refresh. Refresh: flag pointer/tree contradictions.
4. `orchestration-harness/references/lifecycle-gates.md` (Escalation Ruling section): one line — when recording a ruling, check the ADR warrant criteria (`skills/durable-docs-authoring/references/adr.md`); if met, propose an ADR per that reference before the affected work closes.
5. `orchestration-harness/references/completion-closeout.md`: one backstop line — before final done, sweep the plan's Decision Log for entries meeting the ADR warrant criteria not yet proposed; propose or record the decline.
6. Zero always-read SKILL.md-body additions anywhere; both hooks live in references already imperatively routed (v0.8.1/v0.9.0 wiring).

### Task_3 (version + validation; orchestrator)
- 0.9.1 → 0.10.0 in the three manifests; full common.md validator set; skills-maintenance final ambiguity pass over the two changed skills' trigger surfaces.

### Task_4 (review; Codex reviewer)
- Item-by-item vs this Normative scope with file:line citations; fidelity check (criteria text implements the root-test-first structure with signals demoted per the 2026-07-24 Decision Log entry; template patches match the accepted-patch list — including that dropped patches `decision_altitude` and `affected_repositories` did NOT land); trigger-chain bar (both hooks imperative with direct paths; adr.md reachable at binding moments; no semantic-selection reliance); budget bar (stated line budgets; zero always-read additions); template is a valid drop-in (no harness-relative references inside the placeable files); validators rerun.

## Tasks

### Task_1: ADR content cluster (durable-docs-authoring)
- type: impl
- owns:
  - plugins/coding-agent-orchestration-harness/skills/durable-docs-authoring/**
- depends_on: []
- description: |
  Apply Normative scope Task_1 items 1–4 exactly. Placeable files must be self-contained drop-ins;
  criteria/flow text must match the companion survey's calibrated rule in substance; respect
  authoring-rules.md conventions (no time-relative language, durable metadata).
- acceptance:
  - Items 1–4 present within stated budgets; placeable files contain no harness-internal paths
  - Criteria are root-test-first with all three mishandling modes (violate / wrongly preserve / wrongly extend) and the required mode-named mishandling statement; signals a-g demoted to prompts; negatives derivable; three-home model present; flow includes atomic Decision-Log proposal recording with the mode-named scenario, user-approval-before-persist, decline-as-terminal, and the amendment/supersession policy
  - Template carries all accepted patches and none of the dropped ones
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py && python scripts/run_validation_smoke_tests.py"

### Task_2: Wiring cluster (rulebook + orchestration-harness)
- type: impl
- owns:
  - plugins/coding-agent-orchestration-harness/skills/rulebook/**
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/**
- depends_on: []
- description: |
  Apply Normative scope Task_2 items 1–6 exactly. Both trigger hooks are imperative sentences with
  direct reference paths (routing-table nouns are a known dormant-content failure). The bootstrap
  procedure states the user-confirmation requirement at every outcome and the placement consent gate.
- acceptance:
  - Items 1–5 present at the named files; item 6 holds (zero always-read additions)
  - Bootstrap text covers all three outcomes, confirm-before-record, placement consent, refresh contradiction flag, and refresh-only re-offer
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py && python scripts/run_validation_smoke_tests.py"

### Task_3: Version 0.10.0 and full validation
- type: chore
- owns:
  - plugins/coding-agent-orchestration-harness/.claude-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.codex-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.github/plugin/plugin.json
- depends_on: [Task_1, Task_2]
- description: |
  Bump 0.9.1 → 0.10.0; run the full common.md validator set; run the skills-maintenance final
  ambiguity pass over durable-docs-authoring and rulebook trigger surfaces.
- acceptance:
  - Manifests at 0.10.0; validators green; ambiguity pass recorded
- validation:
  - kind: command
    required: true
    owner: orchestrator
    detail: "All commands from docs/coding-agent/rules/common.md Repository-Specific Validation Commands"

### Task_4: Independent review (survey-fidelity + trigger-chain + budget bars)
- type: review
- owns: []
- depends_on: [Task_3]
- description: |
  Codex Reviewer at pinned commit per Normative scope Task_4.
- acceptance:
  - Reviewer status APPROVED with per-item verdicts including the dropped-patch absence check
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Content + wiring + drop-in validity review at pinned commit with independent validator rerun"

## Task Waves (explicit parallel dispatch sets)

- Wave 1: [Task_1, Task_2]
- Wave 2: [Task_3]
- Wave 3: [Task_4]

(Wave 1: two parallel Claude harness-worker subagents — disjoint owns, spec-complete prompts, both
reading the companion survey. No Codex authoring → no prose-pass task, per A2.)

## Rollback / Safety
- All changes on `feature/2026-07-23/adr-integration`; revert = drop branch. Inert plugin content; no runtime installs; no target-repo writes in this plan.

## Progress Log (append-only)

- 2026-07-23 Plan drafted with companion survey committed; awaiting user approval before Wave 1 dispatch.
- 2026-07-24 User approved after four design refinements (root-test criteria, three mishandling modes, signals a-g, lifecycle convention); Wave 1 dispatched.
- 2026-07-24 Wave 1 completed: [Task_1, Task_2]
  - Summary: two parallel Claude harness-worker subagents; all 10 items landed within budgets (adr.md 43 lines, template 62, README 31; five wiring files; zero SKILL.md always-read additions). Orchestrator spot-verified: criteria text faithful to the root-test/three-mode/signals-a-g structure; both drop-ins contain no harness-internal references; both trigger hooks imperative with direct paths.
  - Validation evidence: both workers' validators exit 0; orchestrator independent rerun on combined tree — package 0, smoke 0, diff --check 0.
  - Notes: three Task_1 and three Task_2 assumptions ratified at integration, notably the template's self-contained warrant gloss (required for drop-in validity) and the fresh-suite template line placed as guidance adjacent to the fenced block (correct form knowable only after detection). No escalations, no lesson candidates.
- 2026-07-24 Wave 2 completed: [Task_3]
  - Summary: manifests 0.10.0; full common.md validator set green; final ambiguity pass over changed trigger surfaces recorded. Commit 6d745ad.
- 2026-07-24 Wave 3 completed: [Task_4]
  - Summary: Codex Reviewer round 1 NEEDS_REVISION (single formatting finding — blank EOF line in the survey companion; every substantive item PASS with citations); remediated in 03b6c24 with the range-scoped diff-check discipline noted; round 2 APPROVED, no findings.
  - Validation evidence: reviewer independent rerun all exit 0 incl. git diff --check main..HEAD after fix.

## Decision Log (append-only; re-plans and major discoveries)

- 2026-07-24 Decision: warrant criteria restructured root-test-first (user reframing during plan review).
  - Trigger: user articulated the underlying test — an ADR is warranted when losing the decision's reasons and its existence as a decision point is expected to cause future work to go against it.
  - Plan delta: criteria section rebuilt — single counterfactual test with a required concrete violation statement per proposal; the survey's five criteria demoted to recognition signals; negative list re-expressed as derivable from the test. Flow now records signal + title + expected violation atomically.
  - Why superior: captures the invisible-fork problem (state reads as accident absent the record); converts proposals from category-matching into falsifiable claims (ADR-inflation resistance); excludes the corpus's one category-rule false positive (ADR-I-0022) naturally instead of via a bolted-on filter. Corpus recall unchanged at 55/56-with-the-56th-correctly-excluded.
  - User approval: this entry implements the user's own formulation.
- 2026-07-24 Decision: root test generalized to three mishandling modes (user-approved backwards derivation).
  - Trigger: user asked whether the erosion-only criterion suffices; consumption-scenario enumeration (re-proposal, helpful-fix, bug archaeology, constrained extension, mid-task persuasion, legitimate reversal, over-extension) surfaced two mirror failure modes the erosion phrasing under-covers.
  - Plan delta: root test's object is the decision's reasoning, premises, and boundaries; three modes — violate / wrongly preserve (ossification; ADR-D-0005 as corpus grounding) / wrongly extend (over-application; CME reader-strictness scope clause as grounding); signals gain (f) expiring premises and (g) deliberate scope boundary; template notes upgrade Revisit When to load-bearing for preservation and assign Decision Boundary the scope-rationale duty.
  - Deliberate non-addition: onboarding/context-transfer value rejected as a warrant — corpus-level benefit, not a per-decision test; admitting it would justify ADRs for everything.
  - User approval: yes ("Yes." to folding in, 2026-07-24).
- 2026-07-24 Decision: at-a-glance retirement/supersession convention (user-approved).
  - Trigger: user asked how lifecycle should be obvious from directory structure and filename alone; corpus evidence — 0/56 ADRs use supersedes fields, so frontmatter-only lifecycle is invisible lifecycle.
  - Plan delta: full supersession/retirement = one atomic operation (frontmatter + move to docs/decisions/superseded/ + self-describing rename + inbound-link repair proven by absence search); partial supersession stays in place per supersession_scope semantics; IDs never reused, active-directory gaps meaningful. README and flow items updated accordingly.
  - Tradeoffs: inbound-link churn per supersession event (rare — ~1 candidate in 56) accepted against browsing benefit paid on every consultation; alternatives weighed — filename marker alone (active/dead interleaving) and bare move (opaque archive) both rejected for the combined form.
  - User approval: yes (2026-07-24).

- 2026-07-23 Decision: template patches accepted/dropped per the value-audit lens applied to the survey's eight suggestions — accepted: `warrant:` field, Decision Boundary and Measurement Basis optional sections, `depends_on`/`implements` optional keys, `supersession_scope` + reciprocal-update flow obligation, one-line consultation impact, marked re-proposable option, amendment policy in flow text; dropped: `decision_altitude` field (no downstream consumer), `affected_repositories` field (criterion d fired once in 56; body text covers it). User approved the overall shape in discussion; drops are recorded here for Task_4's absence check.
- 2026-07-23 Decision: post-merge follow-ups deliberately out of scope — CM/agent-harness pointer lines (one line each, their repos), CME bootstrap conversation, optional CME foundational ADRs (five identified gaps in the survey), possible CM adoption of template patches. Each is user-initiated later work.

## Notes
- Risks: the placeable files must never acquire harness-internal references (drop-in validity is a Task_4 check); criteria wording drift from the survey's calibrated rule (Task_4 fidelity check); Wave 1 prompts must be spec-complete.
- Edge cases: repos with a `decisions/` directory but no template still count as case (i) — the pointer says "match the existing ADRs"; pointer-only, per user ruling.
- 2026-07-24 ADR proposal (closeout sweep, per the just-landed completion-closeout hook): signal (b) rejected-alternatives-likely-to-return + (a) cross-boundary configuration contract; proposed title "Repo-rule pointer lines as the decision-record configuration surface"; expected mishandling, mode VIOLATE — without a record, future harness maintenance would likely re-propose a dedicated bootstrap config artifact or template mirroring into rule suites, against the pointer decision while its premises (single config surface; repo-local canonicality) hold. Proposed to the user in the closeout report; awaiting ruling — nothing persisted.
