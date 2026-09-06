---
status: accepted
adr_type: design
date: 2026-09-06
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "GPT-6 Astra"]
informed: []
warrant:
  warranted_by: "without this record, future work would likely restore loader text that claims user authority, forbid the Orchestrator from reading before research, and turn record-and-surface back into pause-and-ask, because each reads as the safer default"
  detected_signals: "cross-boundary authority shape; rejected alternatives likely to be re-proposed; premises tied to the current fleet"
  cost_of_violation: "silent: harness text that claims user authority outranks every Orchestrator-to-subagent instruction, and pause mandates stack on a model that already pauses; both look like caution"
  cost_of_over_extension: "dropping the three hard-stop cases, the plan-approval gate, or the research waiver record; those are consent and coordination contracts, not model compensation"
supersedes: ["ADR-D-0008-codex-explicit-subagent-authorization-and-async-dispatch-lifecycle.md"]
superseded_by: null
supersession_scope: partial
depends_on: ["ADR-D-0018-evidence-tiers-for-removing-harness-content.md"]
---

# ADR-D-0017: Instruction authority and Orchestrator reading for Claude Fable 5.1 and GPT-6 Astra

## Context and Problem Statement

Three rules compensated for the models the harness was written against, GPT-5.5 and Claude Fable 5 (the consulted models of ADR-D-0008 and ADR-I-0004): the Codex loader called itself "explicit user direction", the Orchestrator was forbidden to read code before a Researcher returned, and every material discovery paused for user confirmation. Claude Fable 5.1 and GPT-6 Astra rank the user's conversation above skill text, triage by reading, and pause on their own when input could change the result, so each rule works against them. What those two models do not do on their own is surface a public-contract change or name the cleaner alternative to a workaround.

## Decision

1. **Harness text never claims user authority.** The loader says the user installed the harness and that it is followed unless the user's conversation says otherwise. An instruction from below the user, including Orchestrator to subagent, is weighed as such. This supersedes the ADR-D-0008 clause that made loader use "explicit user direction"; the rest of ADR-D-0008 stands.
2. **The Orchestrator may read to triage.** Researchers are for unfamiliar or cross-cutting areas. Non-trivial work done without one carries a recorded waiver with its reason.
3. **Discoveries are recorded and surfaced; only three cases pause.** A material discovery goes into the plan record and the next report. Confirmation is required only for a contract-shape change, an irreversible or outward-facing action, or a fix whose only path inside the Worker's scope is a workaround. Because Claude Fable 5.1 and GPT-6 Astra do not volunteer the cleaner alternative, the tripwire covers shared types and boundaries outside the Worker's scope that the plan could change.

## Why

A skill is not the user, and a model that knows the difference will obey whichever text claims the higher rank; the claim was false and its failure invisible. Reading is cheaper than a dispatch round-trip, and Claude Fable 5.1 and GPT-6 Astra read well. Surfacing is the part that protects the plan; the pause only protected against models that would not surface.

## Rejected Alternatives

- Keep the rules and override per task: the override travels through the channel the loader claim defeats.
- Delete the loader, the research gate, and the replan triggers: removes surfacing that Claude Fable 5.1 and GPT-6 Astra do not do natively; reopens when a probe shows unprompted surfacing of scope and contract impact on every model used for dispatch, each named and dated in the reopening record.

## Decision Boundary

Invariant: harness text never claims user authority; a pause mandate exists only for the three cases above; work without a Researcher carries a recorded waiver; surfacing of scope and contract impact stays an obligation in Worker and Orchestrator text.

Not covered: loader wording, waiver format, Researcher heuristics, the tripwire's exact conditions, and what counts as material; those live in skill text.

## Validation

The Codex loader contains no authority claim; the Research Dispatch Gate and its reference agree; replan and tripwire text name the three cases.

## Revisit When

Checked on 2026-09-06 against Claude Fable 5.1 and GPT-6 Astra. Replacing either model with another reopens all three items. A Codex model that refuses subagent dispatch without an authority claim reopens item 1. As of 2026-09-06, item 1 had not been verified on a real peer channel with the reworded loader; that check is Task_4 of `docs/coding-agent/plans/active/frontier-guidance-follow-ups-plan.md`, and a failure there reopens item 1.
