---
status: accepted
adr_type: design
date: 2026-10-04
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1"]
informed: []
supersedes: ["superseded/ADR-D-0030-the-assessor-is-a-reviewer-dispatch-profile-not-a-fourth-role--superseded-by-ADR-D-0050.md"]
superseded_by: null
depends_on: ["ADR-D-0029-the-optimizer-never-judges-its-own-continuation.md", "ADR-D-0052-the-orchestrator-never-grades-its-own-run-and-its-reading-is-compared-only-after-the-grades-are-fixed.md", "ADR-D-0048-logical-roles-are-stable-and-each-runtime-names-its-agents-by-its-own-convention.md"]
---

# ADR-D-0050: Independent judgement of the Orchestrator's work (the value audit and the in-loop goal assessment) is held by a role of its own, the Auditor, apart from the Reviewer that checks the work for the Orchestrator

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. The Orchestrator session is a session that holds the Orchestrator role (ADR-D-0020) and plans, dispatches and reports the work.

Two judgements of the Orchestrator's own work are made by a dispatch with fresh context that the Orchestrator cannot frame: the in-loop assessment of a goal run (ADR-D-0029) and the value audit (ADR-D-0052). Both were packaged as dispatch profiles of the Reviewer role, so in every runtime they run on the Reviewer's agent, with the Reviewer's model. The Reviewer also checks the work for the Orchestrator: plan review, wave and final review, evidence. The two kinds of work differ in nature: one checks work against a packet the Orchestrator wrote, the other judges the Orchestrator from the documents alone. Sharing an agent ties them to one model, so whoever chooses models must put the strongest one on all review work because the judgement needs it. The fork is whether independent judgement stays a dispatch profile of the Reviewer or becomes a role of its own.

## Decision

- Independent judgement of the Orchestrator's work is held by a logical role of its own, the Auditor.
- The Auditor holds the value audit and the in-loop assessment of a goal run. Each keeps its mandate in its reference and its fixed dispatch template, unchanged by this record.
- A dispatch to the Auditor carries locations only: the fixed template with its fill-ins, logged verbatim where its mandate says. An account of the work in a dispatch is misuse on sight.
- The Auditor is read-only, is dispatched only by the Orchestrator session, and dispatches nothing.
- Its adapter in each runtime carries no procedure of its own: it points at the mandate named in the dispatch and restates none of it.
- The Reviewer keeps checking the work for the Orchestrator: plan review, wave and final review, and its evidence duties. In goal mode the Reviewer keeps the pre-loop check of the goal condition and the pre-merge check of the completion report against the journal, which are checks of work done for the Orchestrator.
- Cadence compliance of the in-loop assessment is still asserted in the completion report and verified before merge against the journal, so a starved Auditor invalidates the report.
- Which model runs each role is chosen per role by whoever configures the runtime; the harness fixes none.

## Why

Someone who sets up the harness can put a model suited to each kind of work on it only if the kinds of work are separate roles: with judgement and checking on one agent, the capability one of them needs is paid for on both, and checking, the larger volume, runs on the strongest model for no gain. The mandate, the fixed template and the journal stay what protect the judgement from the dispatcher's framing; the separate role adds the choice of model and removes nothing.

## Rejected Alternatives

- Independent judgement stays a dispatch profile of the Reviewer role, the decision of ADR-D-0030: it lost because it binds two kinds of work to one model, so the choice of a model per kind of work cannot be made; that record weighed the added role only against framing effects, which the fixed template already exposes, and did not weigh model choice. Reopen if the runtimes come to let one agent run different dispatches on different models chosen by the person configuring them.
- The Auditor also takes the pre-loop check of the goal condition and the pre-merge check of the completion report: it lost because those check work for the Orchestrator against a packet, the Reviewer's kind of work, and moving them would change who checks a goal run before merge with no gain in model choice; reopen if those checks are found to need judgement independent of the Orchestrator's framing.
- The Auditor's mandate written into its adapter in each runtime: rejected outright; three replicated copies of a procedure that has one home (ADR-D-0049).
- A model fixed per role by the harness: rejected outright; which models exist and what each is good at changes with the runtime and over time, and is the choice of the person configuring it.

## Decision Boundary

Invariant: the value audit and the in-loop goal assessment are dispatched to the Auditor, a read-only role apart from the Reviewer, by a fixed location-only template logged verbatim; the Auditor's adapters restate no mandate; cadence of the in-loop assessment is verified before merge; the harness fixes no model for any role; the Decision list states the rest.

Not covered: what the value audit grades and against what (ADR-D-0052 and its mandate); what the in-loop assessment judges (ADR-D-0029 and its mandate); the cadence schedule and the template texts, which their references own; the Auditor's physical names, which the role map states by each runtime's convention (ADR-D-0048); how a runtime lets a model be chosen for an agent; goal mode's admission, loop, stall rule and completion report, which are unchanged.

## Validation

- The role map states the Auditor and its home; an adapter exists for it in each runtime, read-only, with no mandate text in it.
- No plugin text routes the value audit or the in-loop goal assessment to the Reviewer.
- Both fixed dispatch templates are byte-identical to what they were before this record.
- Journaled and logged dispatch texts match the fixed templates across a run.
- The pre-merge check of a goal run verifies the cadence assertion against the journal.

## Revisit When

- Runtimes come to let one agent run different dispatches on different models chosen by the person configuring them.
- Retrospectives find the Auditor's judgement framed by the dispatcher despite the fixed template.
- The pre-loop or pre-merge checks kept with the Reviewer are found to need independent judgement.
- On 2026-10-04 no run had dispatched the Auditor's adapter in any runtime; a run in which the Reviewer and the Auditor on different models does not work as it did on one model reopens this record.

## More Information

Replaces ADR-D-0030 in full: its invariant (the mandate in the reference, the dispatch text fixed and journaled, cadence verified at the merge gate) is carried, and its decision that the assessor is not a role of its own is reversed; the fourth role it named as an upgrade path is taken here for a different reason, model choice. Settles what the record ADR-D-0052 replaced left open, whether the audit is a dispatch profile of another role or a role of its own. Source of intent: `docs/coding-agent/briefs/active/design-led-long-runs-brief.md`, "Roles and models". Design: `docs/coding-agent-orchestration-harness/design/goal-mode-design.md`, pillar 4. Related: ADR-D-0029 (the independent assessor), ADR-D-0031 (the merge gate), ADR-D-0052 (the value audit), ADR-D-0048 (role identities), ADR-D-0049 (one home per role's mechanics).
