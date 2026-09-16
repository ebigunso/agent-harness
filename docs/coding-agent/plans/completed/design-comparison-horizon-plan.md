# Plan: The design comparison weighs the whole lifecycle, not the diff

- status: done
- generated: 2026-09-16
- last_updated: 2026-09-16
- work_type: docs

## Goal
- A plan's `Design` section, and the Reviewer's check of it, compare designs on what they cost over the life of the code, not on the diff: the structure they leave, how they evolve, how they are verified, how they run, what they ask of the next reader, and what they expose. The three structural axes landed by `plan-requirement-provenance-plan.md` become one of six lens groups, each lens a short phrase the drafter walks once per design; where the harness already asks the question at post-Worker review, plan review may open that reference.

## Definition of Done
- `plan-format` rule 13 names six lens groups with their members from the fixed vocabulary (structure, evolution, verification, operation, human, safety); the template's `Design` section carries the six group labels; an alternative differs on at least one lens; consumers stay in the Compatibility stance; the proportional form stays, and its trigger gains "a trust boundary or a hot path" so the safety and operation groups can fire.
- A fit claim names the document where the repository states its direction (a decision record, roadmap, README or contributing guide, rule file, or a reference document the rule suite lists); without one the claim is not made.
- The plan-review snippet's design bullet points at the lens groups rule 13 names instead of enumerating members, adds the fit-claim check (a fit claim without a source, or one its source does not support, is a finding), adds the noise direction (a Design section that walks lenses on which its alternatives cannot differ is a finding), and names the latent-risk reference the Reviewer may open when a plan's Design section touches failure or degradation, runtime cost, or data exposure.
- The plan-review routing entry in `engineering-quality-baselines/SKILL.md` admits those named references as the one exception to "no latent-risk routing".
- No lens is a paragraph: every lens is its name, with at most one short parenthetical clause where the name alone is ambiguous, and no text the 2026-08-29 ablation deleted is restated.
- No validator, script, fixture, or manifest changes; the version stays 0.21.0, already bumped on this unmerged branch.
- Every added line passes the content test from lesson 2026-09-05 and stays within the length targets in the tasks.

## Scope / Non-goals
- Scope: `skills/plan-format/SKILL.md` rule 13, `skills/plan-format/references/plan-template.md` `Design` section, `skills/subagent-strategy/references/prompt-snippets.md` plan-review design bullet, `skills/engineering-quality-baselines/SKILL.md` plan-review routing entry.
- Non-goals: the Plan Gate sentence (it names no lenses); rule 12 and the enumeration bullet; the completed plan on this branch; any validator, fixture, or manifest change; a considerations reference file; the latent-risk references themselves and `architecture-gates.md` (its unrouted "How to Use in Planning" section is a separate observation, left alone).
- Research waived for the first draft (the Orchestrator wrote the three target lines in the previous plan on this branch); a Researcher mapped the seventeen lenses against the harness on 2026-09-16 before this revision (coverage table, routing lines, and ablation history in the Decision Log entry 3).

## Planner-added requirements
- The landed three axes fold into the `structure` group rather than standing beside the six groups ebigunso named. Needed because: they are structural lenses by content, and a seventh group for three of them would be the flat-list shape the grouping avoids.
- A fit claim names its source, and the admitted sources are the documents where a repository states its direction (decision record, roadmap, README or contributing guide, rule file, or a reference document the rule suite lists). Needed because: an unsourced "aligns with the roadmap" is the hollow-reason failure the enumeration bullet exists to catch, relocated into the Design section; naming the source lets the Reviewer's existing "open every source a claim names" step cover it; the list is wide enough that a repository's philosophy in a README counts and narrow enough that a merged PR or a chat message does not.
- Lens members live in rule 13 only; the template carries the group labels and the snippet points at rule 13. Needed because: ADR-D-0022 has snippets route to the owning skill without restating its formats, and a second copy of the member list is one the final Reviewer would otherwise have to police verbatim.
- A lens carries at most one short parenthetical clause, and only where its name alone is ambiguous (which direction of coupling; which seams; what "determinism" must keep injectable). Needed because: a bare name like "coupling direction" does not say which direction is the cost, so the drafter would have to guess; a clause is the smallest addition that fixes the question, and the one-clause bound is what keeps it from becoming the deleted paragraph.
- The proportionality trigger gains "a trust boundary or a hot path". Needed because: the landed trigger (responsibility, contract, persisted state, new component) was written for three structural axes; a change that adds a hot loop or a new untrusted input touches none of the four and would take the one-line form, so the operation and safety groups would never be walked for the changes they exist for.
- The Reviewer's design bullet gains the noise direction: a Design section that walks lenses on which its alternatives cannot differ is a finding. Needed because: the trigger widens with this plan, and a symmetric check is how the harness keeps a widened obligation from becoming ritual; the review rubric's Symmetric checks are the precedent.
- Folded into the open PR on the same branch, with no further version bump. Needed because: shipping 0.21.0 with three axes and replacing them in 0.22.0 is churn for installed copies; the branch is unmerged and the manifests already read 0.21.0.
- Not planner-added, stated for the record: the six groups and their members (ebigunso's selection of 2026-09-16); phrases not paragraphs, nothing the ablation deleted restated as a paragraph, and one exception clause on the routing line admitting only the references the snippet names (ebigunso accepted these as presented, 2026-09-16); length targets and the content test (lesson 2026-09-05); validators and `git diff --check` (rules `common.md`, `worker.md`).

## Design
- Chosen: rule 13 carries the six groups and their members; the template's `Chosen:` and `Alternative:` lines carry the group labels; the snippet's design bullet points at the groups rule 13 names and names three latent-risk references the Reviewer may open; the routing entry admits those three. Structure: no new dependency (the snippet already has the Reviewer read `plan-format/SKILL.md`); one copy of the member list; the pointer to the three references lives in the snippet and the routing entry admits it by reference, not by restating. Evolution: a lens change touches one line; fits ADR-D-0022 (`docs/coding-agent-orchestration-harness/decisions/ADR-D-0022-workflow-mechanics-have-one-home.md`) in the one respect claimed: a snippet routes to the owning skill and does not restate its formats; the ADR's invariant addresses runtime surfaces (loaders, adapters, snippets, READMEs), and `plan-format` and `subagent-strategy` are the skills the `orchestration-harness` skill routes to for plan format and dispatch, which the ADR leaves as they were and ADR-D-0019 (`docs/coding-agent-orchestration-harness/decisions/ADR-D-0019-remove-harness-content-only-with-class-matched-evidence.md`: evidence is matched to "its own subject matter", and the ablated subject was code-review defect detection, not plan-time design comparison). Verification: the plan validator is presence-only and unaffected; the only check on the three reference paths is the Reviewer opening them (Task_2); `validate_harness_package.py` does open `prompt-snippets.md` (its operational-routing check reads the latent-risk routing snippet's labels; the router-name check is on the reviewer packet template) but validates none of the three paths named here. Operation: every plan loads rule 13; the member list adds about a hundred words to a file already loaded on every plan, and no other cost. Human: a drafter sees six labels and walks the members from one rule. Safety: none of the lenses widens any permission or surface.
- Alternative: the landed arrangement extended, with the snippet enumerating the members. Structure: three copies of the member list to keep verbatim. Evolution: a lens change touches three lines, and the arrangement is the restatement ADR-D-0022 rules out. Verification, operation, human, safety: same. Rejected.
- Alternative: a separate reference listing the lenses with a paragraph each, routed from rule 13. Structure: one new file and a routing entry every plan loads. Evolution: paragraphs are the form the #70 ablation outcome (`docs/coding-agent/plans/completed/repeat-check-ablation-plan.md`, a reference document per `common.md`) removed, and nine of them would restate deleted text, which ADR-D-0019 forbids without new evidence. Verification, operation, human, safety: same. Rejected.
- Alternative: keep the latent-risk exclusion absolute and carry the four latent-risk-only lenses as phrases only. Structure: no routing change. Evolution: the Reviewer's check of failure, cost, and exposure at plan time stays a phrase with nothing behind it, while the same question has a worked reference two skills away. Verification: same. Operation: same. Human: same. Safety: the data-exposure lens has no reference behind it at plan time. Rejected by ebigunso's ruling.
- Alternative: leave the proportionality trigger as landed. Structure: two fewer lines change. Evolution: the trigger and the groups it guards drift apart on the first edit. Verification: same. Operation: a change adding a hot loop takes the one-line form. Human: same. Safety: a change adding an untrusted input takes the one-line form, so the safety group never fires on its own subject. Rejected.
- Why chosen: one home for the members, the existing post-Worker references reused by pointer rather than paraphrased, and no paragraph reintroduced, reached before any installed copy sees the narrower version.

## Compatibility stance
- surface: the `Design` section shape, rule 13, and the plan-review routing entry, read by Orchestrators and the plan-review Reviewer.
- stance: migrate
- justification: consumers are this repository's future plans and the one plan on this branch that already carries a `Design` section (`plan-requirement-provenance-plan.md`, completed; its section stays as written, since a completed plan is history).

## Context (workspace)
- Related files/areas: `skills/plan-format/SKILL.md` rule 13 (line 75); `references/plan-template.md` `## Design` (lines 33 to 37); `skills/subagent-strategy/references/prompt-snippets.md` plan-review design bullet (line 73); all three landed by `docs/coding-agent/plans/completed/plan-requirement-provenance-plan.md` on this branch, unmerged, PR #71. `skills/engineering-quality-baselines/SKILL.md` line 39, the plan-review routing entry ("core-principles.md and the Symmetric checks section of review-rubric.md only ... no latent-risk routing"). Latent-risk references the snippet will name: `references/review-latent-risk-failure.md` (degradation and what the operator sees), `references/review-latent-risk.md` (the hot-path row for runtime cost), `references/review-latent-risk-diagnostics.md` (sensitive data in diagnostics).
- Existing patterns or references: `engineering-quality-baselines/references/core-principles.md` principle 3 (build for testability and verifiability), principle 2 (safe revert), and the anti-patterns list carry several lenses as review concerns but not as design-comparison questions; `review-rubric.md` Symmetric checks already load at plan review and cover the test-to-contract lens; `long-horizon-audit.md` is the value-audit lens for churn, not a plan-time comparison; decision records under `docs/coding-agent-orchestration-harness/decisions/` are this repository's stated direction, and a target repository's are whatever its `common.md` reference documents list.
- Design record consulted and deviations from its acceptance: ADR-D-0022 (snippets route to the owning skill and do not restate formats): the landed snippet bullet restates rule 13's axes; this plan corrects that to a pointer. ADR-D-0019 (removed content returns only with evidence of the same class): nine lenses name concepts whose review-guidance paragraphs the 2026-08-29 ablation deleted (readability, trust-boundary validation, cognitive load, dependency direction, failure modes, leave-easier-to-change, data ownership, failure containment, sensitive data in logs); this plan adds them as plan-time phrases on the reading that the ablation's subject was code-review defect detection, ruled by ebigunso on 2026-09-16 without a probe. No clause of ADR-D-0019 covers added content that later misbehaves (its revisit clause covers model replacement and restoring a removal); recorded here for a future reader. No other deviation.

## Fixed vocabulary (Workers use these exactly)
- Lens groups and members:
  - `structure`: dependencies; duplicated state; conversions; one owner per piece of state; coupling direction (volatile depends on stable); boundary crossings (representation, process, trust level).
  - `evolution`: technical debt; blast radius of the next change; fit with the project's stated direction; concept count (abstractions, knobs, vocabulary); deletion path.
  - `verification`: test seam (clear of network, clock, filesystem, UI); cost to run the tests; cost to change the tests when the design changes; tests pin the contract, not the implementation; determinism (randomness, time, ordering, concurrency injectable); failure observability.
  - `operation`: runtime cost and how it scales; degradation when a dependency is slow, down, or wrong.
  - `human`: cognitive load (names predict behavior); debuggability (reproducible locally).
  - `safety`: trust boundary handling; least privilege (permissions, secrets, reach); data exposure (logs, caches, errors).
- Fit claim: a statement that a design fits or conflicts with the project's stated direction; it names the document where the repository states that direction: a decision record, roadmap, README or contributing guide, rule file, or a reference document the rule suite lists.
- Template `Design` lines: `- Chosen: <design>. Structure: <...>. Evolution: <...>. Verification: <...>. Operation: <...>. Human: <...>. Safety: <...>. (consumers: see the Compatibility stance)`; `- Alternative: <design differing on at least one lens>. Structure: <...>. Evolution: <...>. Verification: <...>. Operation: <...>. Human: <...>. Safety: <...>.`; `- Why chosen: <...>`; the proportional form with its trigger extended: `Proportional form when the change touches no responsibility, contract, persisted state, new component, trust boundary, or hot path: ...`.
- Latent-risk references the snippet names, by trigger: failure or degradation, `engineering-quality-baselines/references/review-latent-risk-failure.md`; runtime cost, the hot-path row of `engineering-quality-baselines/references/review-latent-risk.md`; data exposure, `engineering-quality-baselines/references/review-latent-risk-diagnostics.md`.

## Open Questions (max 3)
- None; the two rulings (no probe; plan review may open the named references) are ebigunso's of 2026-09-16.

## Assumptions
- A1: The three target files are the only places that name the axes — source: `rg -n -i "duplicated state" plugins/coding-agent-orchestration-harness/` returns `plan-format/SKILL.md:75`, `plan-template.md:34-35` (capitalized `Duplicated state:`), `prompt-snippets.md:73`, and nothing else (the completed plan under `docs/` is history and is not edited).
- A2: The plan-review routing entry is the only line excluding latent-risk from plan review — source: `engineering-quality-baselines/SKILL.md:39`; the Researcher's sweep of 2026-09-16 found the snippet applies it "per its plan-review routing entry" (`prompt-snippets.md:70`) and no other file restates the exclusion.
- A3: No validator checks that the three paths the snippet names resolve; the Reviewer opening them (Task_2 validation) is the only check of the snippet's paths — source: `scripts/validate_harness_package.py` lines 252 to 273 check that a fixed list of latent-risk files exists (`review-latent-risk-diagnostics.md` among them) and that the backticked names inside `review-latent-risk.md` resolve (`review-latent-risk-failure.md` among those), which covers the files' existence but reads no path from the snippet (corrected 2026-09-16 after Copilot's third round; the earlier wording said no validator reads the paths at all). The `worker.md` row wording "latent-risk reference links" is broader than the script; corrected at closeout as a targeted rule refresh.

## Tasks

### Task_1: plan-format rule 13 and the template Design lines carry the six groups
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/plan-format/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/plan-format/references/plan-template.md
- depends_on: []
- description: |
  Rewrite rule 13 (at most six sentences) so the comparison names the six lens groups with their members verbatim from the fixed vocabulary (parenthetical clauses included, nothing added to them), keeps "at least one alternative that differs from it on a lens", the Compatibility-stance pointer for consumers, and "why the chosen one wins", extends the proportional form's trigger to "no responsibility, contract, persisted state, new component, trust boundary, or hot path", and adds that a fit claim names the document where the repository states its direction (decision record, roadmap, README or contributing guide, rule file, or a reference document the rule suite lists). The member list may be one sentence per group or one sentence with the six groups in parentheses.
  Rewrite the template's `Chosen:` and `Alternative:` lines to the fixed-vocabulary shape (the six group labels in place of the three axis names) and the proportional line's trigger to the extended form; leave `Why chosen:` as it is. The section stays at most six lines including the heading.
- acceptance:
  - Rule 13 names the six groups and their members verbatim from the fixed vocabulary, the extended proportionality trigger, the fit-claim source requirement, and everything it named before, within six sentences, with no clause beyond those the vocabulary carries.
  - The template's `Design` section uses the fixed-vocabulary `Chosen:` and `Alternative:` shapes and the extended trigger, and is within six lines including the heading.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python skills/plan-format/scripts/validate_plan.py --file ../../tests/coding-agent-orchestration-harness/fixtures/valid-plan.md --mode balanced; from repo root: git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review vs acceptance; content test per lesson 2026-09-05; rule 13 stays an obligation with named lenses, no paragraph per lens and no checklist of design questions"

### Task_2: the plan-review design bullet points at the groups, checks fit claims, and names the references
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/subagent-strategy/references/prompt-snippets.md
- depends_on: []
- description: |
  In the plan-review snippet's design bullet (at most six sentences after the edit): the finding shape states what the named design changes on the lens groups `plan-format` rule 13 names, in place of the enumerated axis names; add that a fit claim without a named source, or one its source does not support, is a finding; add that a Design section walking lenses on which its alternatives cannot differ is a finding; add that when the plan's Design section touches failure or degradation, runtime cost, or data exposure, the Reviewer may open the matching reference from the fixed vocabulary (the three paths, by trigger) and nothing else under latent-risk.
- acceptance:
  - The design bullet points at the lens groups rule 13 names and enumerates no members, keeps the cost-delta finding shape and "The Orchestrator owns the rewrite", adds the fit-claim and noise failure directions, and names the three references by trigger with the "nothing else under latent-risk" bound, within six sentences.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From repo root: git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review vs acceptance; the bullet stays an enumeration and comparison task with named failure directions; the three paths resolve; content test per lesson 2026-09-05"

### Task_3: the plan-review routing entry admits the named references
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/engineering-quality-baselines/SKILL.md
- depends_on: []
- description: |
  Amend the plan-review routing entry (the "Plan review:" bullet under Routing Decision) with one clause: the latent-risk references the plan-review snippet names for the Design section are the one exception to "no latent-risk routing". Do not list the three files here; the snippet is their home.
- acceptance:
  - The plan-review routing entry keeps its current reads and its "no latent-risk routing" wording and gains one clause admitting the references the plan-review snippet names for the Design section, without naming them.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py; from repo root: git diff --check"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review vs acceptance; the entry stays a routing line; content test per lesson 2026-09-05"

### Task_4: package validation over the completed tree
- type: chore
- owns: []
- depends_on: [Task_1, Task_2, Task_3]
- description: |
  Orchestrator runs the package validators and the final Reviewer reviews the delta against the Definition of Done.
- acceptance:
  - `validate_harness_package.py`, `run_validation_smoke_tests.py`, and `git diff --check` pass; the manifests still read 0.21.0.
- validation:
  - kind: command
    required: true
    owner: orchestrator
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py; python scripts/run_validation_smoke_tests.py; from repo root: git diff --check; grep for 0.21.0 in the three manifests"
  - kind: review
    required: true
    owner: reviewer
    detail: "Delta review of the four files against the Definition of Done, including that the members appear in rule 13 only, the template carries the six labels, the snippet points at rule 13 and names the three references, the routing entry admits them without naming them, the trigger is extended in both rule 13 and the template, and no lens exceeds its name plus one clause"

## Task Waves (explicit parallel dispatch sets)

Interpretation:
- Tasks listed in the same wave are intended to be dispatched in parallel by default, when `owns` are disjoint and dependencies are met.
- Waves are executed sequentially.

- Wave 1 (parallel): [Task_1, Task_2, Task_3]
- Wave 2 (parallel): [Task_4]

## Rollback / Safety
- Prose-only on the open feature branch; revert the commit.

## Progress Log (append-only)

Append-only editing rule (applies to both logs below): when appending an entry, anchor the edit on the previous entry and reproduce it (or anchor on the section's tail marker) so the edit inserts rather than replaces, and verify afterward that the log grew.

- 2026-09-16 Plan drafted after ebigunso's correction on PR #71 (the comparison must weigh the bigger picture: technical debt, fit with the project's philosophy or roadmap, testability, the cost to run tests and to change them when the design changes); lessons entry extended.
- 2026-09-16 Plan review round 1: NEEDS_REVISION (both fit claims in the plan's own Design section failed the check it installs; the pointer design named); revised per Decision Log entry 2; delta re-review requested.
- 2026-09-16 Plan review round 2 (delta): APPROVED, no findings. Presented.
- 2026-09-16 ebigunso selected seventeen further lenses before approval; Researcher mapped them against the harness; ebigunso ruled on the two open questions; plan extended per Decision Log entry 3; full re-review requested.
- 2026-09-16 Plan review round 3 (full): NEEDS_REVISION, three majors (a Verification claim naming a validator check that does not exist; glosses contradicting Task_1; a proportionality trigger that cannot fire for the new groups); revised per Decision Log entry 4; delta re-review requested.
- 2026-09-16 Plan review round 4 (delta): APPROVED; one advisory (some glosses sit on names that are not strictly ambiguous), left as is.
- 2026-09-16 Plan approved by ebigunso ("Good. Proceed with the plan."), trigger extension included; Wave 1 dispatched: [Task_1, Task_2, Task_3].
- 2026-09-16 Wave 1 completed: [Task_1, Task_2, Task_3], all done (Claude Workers).
  - Summary: rule 13 is four sentences with the six groups and members verbatim, the fit-claim source sentence, and the extended trigger; the template's Design section is five lines with the six labels and the extended trigger; the snippet's design bullet is six sentences pointing at rule 13, with the fit-claim and noise directions and the three references by trigger; the routing entry gains the one exception clause.
  - Validation evidence: Task_1 validate_plan.py on the fixture pass; Task_3 validate_harness_package.py pass; all `git diff --check` pass. Task_4 (Orchestrator): validate_harness_package.py pass, run_validation_smoke_tests.py pass, git diff --check pass, three manifests read 0.21.0.
  - Blockers/questions: none blocking. Task_1 changed the proportional line's tail from "no alternative changes the cost axes" to "no alternative differs on a lens" since the axes no longer exist; accepted. The two plan-format files now carry LF in the working copy (autocrlf notice); the repository stores LF, so the commit is unaffected.
  - Follow-up decision: final delta Reviewer over the four files.
- 2026-09-16 Final delta review (Claude Reviewer): APPROVED; all required checks rerun independently and pass. One minor: the lessons follow-up line still named three groups; corrected at closeout with the completed plan path. Closeout: `worker.md` row narrowed to what the package validator reads (targeted rule refresh); `reviewer.md` gains the closeout re-read of lessons entries (the Reviewer's lesson candidate, promoted as a repo rule); plan moved to completed/; committed on the feature branch; PR #71 updated.
- 2026-09-16 Copilot round 4 (reviewed at badf522, before ab743b8; zero new inline comments, ten suppressed notes): rule 13's proportional bullet now says no alternative is required (fix); the enumeration bullet treats a missing section, as opposed to `- None`, as a finding (fix); reviewer.md's example reads "three axes became six lens groups" (fix); the Design line's description of the operational-routing check corrected once more (the router-name check is on the packet template, the snippet check is on the latent-risk snippet's labels). Declined as history: rewording A1's citation, A3's read-versus-validate phrasing, Task_1's sentence count (the count predates the layout change), and the completed provenance plan's Definition of Done and A2. Stopping rubric met after this push: zero new substantive comments in the latest round, every thread resolved, the remaining notes are judgment calls on completed records; no further Copilot review requested.
- 2026-09-16 Copilot round 3 (reviewed at e3c05cb, before badf522): the `<request>` placeholder added to the snippet's Inputs (fix); rule 12 now requires the section on every plan with `- None` when empty (fix); A3 and the Design line's ADR-D-0022 clause sharpened (fix: the validator does check the three files exist, through its list and the router's links, but reads no path from the snippet; the ADR's invariant is about runtime surfaces, and the one respect claimed is the snippet routing to the owning skill). Declined: the note that the completed provenance plan should list the version bump as planner-added; its number was an open question ebigunso resolved before approval, and the plan is history.
- 2026-09-16 Correction: the Design section's Verification clause and A3 said the package validator does not read `prompt-snippets.md`; Copilot's second round showed `check_operational_routing_surfaces()` opens it, so the clause now says the validator reads the snippet but validates none of the three named paths. A3's line citation stands for the latent-risk check it names; the "not the snippet" inference was wrong and was missed by the plan Reviewer as well.
- 2026-09-16 Copilot review round on PR #71 (two reviews, four threads, two suppressed comments), handled as trivial consistency fixes: the enumeration bullet now uses rule 12's definition instead of "the request does not state" (fix); the dispatch-checklists packet line points at the snippet instead of restating the inputs (fix); the noise direction narrowed to "claims a difference on a lens the alternatives cannot affect", since the template requires all six groups on every line (fix); the Plan Gate sentence admits the proportional form rule 13 allows (fix, suppressed comment); reviewer.md `last_updated` corrected to 2026-09-16 (fix). The suppressed comment on the completed provenance plan's Definition of Done is declined: a completed plan is history, and the landed rule 12 carries the definition.

## Decision Log (append-only; re-plans and major discoveries)

- 2026-09-16 Decision: three named groups, not a flat list, and fold into PR #71.
  - Trigger / new insight: ebigunso's correction after the PR opened.
  - Plan delta (what changed): new plan on the same branch; the previous plan stays completed and unedited.
  - Tradeoffs considered: see the Design section (a separate considerations reference; a later release).
  - User approval: pending with the plan.
  - Record proposed: none.
- 2026-09-16 Decision: the snippet points at rule 13; the fit-claim source list widens.
  - Trigger / new insight: the Reviewer found the plan's own fit claims cited a PR (not an admitted source) and ADR-D-0022 (which rules against the arrangement claimed to fit it), and named the pointer design, which removes a copy of the member list and is what the ADR asks for.
  - Plan delta (what changed): chosen design is the pointer form; the source list admits README or contributing guides and the rule suite's reference documents; the two "cost to change" members are distinguished as code and tests; Task_2's "nothing else changes" constraint dropped as covered by the Worker contract.
  - Tradeoffs considered: the landed enumerating arrangement (rejected, recorded in the Design section).
  - User approval: pending with the plan.
  - Record proposed: none.
- 2026-09-16 Decision: six lens groups, phrases only, and plan review may open three named latent-risk references.
  - Trigger / new insight: ebigunso selected seventeen lenses (evolution: blast radius, concept count, deletion path; verification: test seam, failure observability, determinism, test-to-contract; structure: ownership, coupling direction, boundary crossings; operation: runtime cost and scaling, degradation; human: cognitive load, debuggability; safety: trust boundary, least privilege, data exposure) and asked for a coverage check first. The Researcher found one already at plan review (test-to-contract), four present only in latent-risk references that plan review is told not to load (failure observability, runtime cost, degradation, data exposure), two absent everywhere (least privilege, debuggability), and nine naming concepts whose review-guidance paragraphs the 2026-08-29 ablation deleted under ADR-D-0019. Two questions were put to ebigunso: whether ADR-D-0019's same-class evidence rule bars plan-time phrases for those nine without a probe, and whether plan review may open a latent-risk reference for the Design section.
  - Plan delta (what changed): ebigunso ruled no probe (the ablated subject was code-review defect detection; plan-time design comparison is a different subject) and allowed plan review to open the named references. The fixed vocabulary grows to six groups; Task_2 names the three references by trigger; Task_3 adds the routing exception in `engineering-quality-baselines/SKILL.md`; the Definition of Done forbids any lens being a paragraph or restating deleted text; the Context records the ADR-D-0019 reading so its revisit clause can find it.
  - Tradeoffs considered: a probe before landing (rejected by ebigunso: a day of work for a different-subject question); keeping the latent-risk exclusion absolute (rejected by ebigunso; recorded as an alternative in the Design section); a separate lens reference with a paragraph each (rejected: the deleted form).
  - User approval: the two rulings yes; the plan as a whole pending.
  - Record proposed: none now. The ADR-D-0019 reading is recorded in Context; no clause of the ADR covers added content that later misbehaves, so a future reader finds the reading there.
- 2026-09-16 Decision: revisions from plan review round 3.
  - Trigger / new insight: the plan's own Verification claim cited a validator check on the snippet's reference paths that `validate_harness_package.py` does not perform; the vocabulary's glosses contradicted Task_1's "no explanation"; and the proportionality trigger, kept unchanged, could not fire for a change adding a hot loop or an untrusted input, so the operation and safety groups would never be walked where they matter.
  - Plan delta (what changed): the Verification claim and A3 now say the Reviewer opening the paths is the only check, and the `worker.md` row is queued for a targeted rule refresh at closeout; glosses are bounded to one short clause where the name is ambiguous, trimmed, and listed as planner-added; the trigger gains "trust boundary or hot path" in rule 13 and the template; the Reviewer's design bullet gains the noise direction; the ADR-D-0019 wording no longer borrows the revisit clause; the planner-added section separates what the planner added from what ebigunso selected or accepted.
  - Tradeoffs considered: no glosses at all (rejected: "coupling direction" and "determinism" do not say which way or what to inject, and the Reviewer would have nothing to hold the drafter to); the trigger unchanged (rejected, recorded as an alternative in the Design section); the noise direction in Notes only (rejected: an obligation nobody owns is not one).
  - User approval: pending with the plan. The trigger extension changes a detail ebigunso accepted as presented ("proportionality stays the guard"); the Orchestrator reads the acceptance as the guard staying functional, and flags it at presentation.
  - Record proposed: none.

## Notes
- Risks: the evolution group's "fit with the project's stated direction" depends on the target repository having a stated direction; where none exists the fit claim is simply not made, which the Definition of Done says. Twenty-one lenses in rule 13 cost roughly a hundred words on every plan; proportionality (the one-line form for changes touching no responsibility, contract, persisted state, new component, trust boundary, or hot path) is the guard, and the noise direction in Task_2 is its symmetric check.
- Edge cases: the completed `plan-requirement-provenance-plan.md` on this branch carries the old three-axis `Design` section; it is history and stays.
