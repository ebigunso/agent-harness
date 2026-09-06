---
status: accepted
adr_type: design
date: 2026-09-06
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "GPT-6 Astra"]
informed: []
warrant:
  warranted_by: "without this record, future work would likely turn record-and-surface back into pause-and-ask on every discovery, because a pause reads as the safer default"
  detected_signals: "rejected alternative likely to be re-proposed; premises tied to Claude Fable 5.1 and GPT-6 Astra as checked on 2026-09-06"
  cost_of_violation: "pause mandates stack on a model that already pauses when input could change the result, and the surplus asking looks like caution"
  cost_of_over_extension: "dropping the three pause cases or the surfacing obligation; the cases are consent contracts and the surfacing is the part Claude Fable 5.1 and GPT-6 Astra do not do unprompted"
supersedes: []
superseded_by: null
supersession_scope: null
depends_on: ["ADR-D-0020-remove-harness-content-only-with-class-matched-evidence.md"]
---

# ADR-D-0019: Discoveries are recorded and surfaced; three cases pause

## Context and Problem Statement

Replan triggers and the drift tripwire paused for user confirmation on every material discovery. Claude Fable 5.1 and GPT-6 Astra already pause on their own when input could change the result, so the mandate stacked on that bias. What those two models do not do on their own is surface a public-contract change or name the cleaner alternative to a workaround; the surfacing was the part worth keeping, not the pause.

## Decision

A material discovery is written into the plan record and surfaced at the next report or integration point. Confirmation is required only for a contract-shape change, an irreversible or outward-facing action, or a fix whose only path inside the Worker's scope is a workaround.

## Why

Surfacing is what protects the plan; the pause only protected against models that would not surface.

## Rejected Alternatives

- Delete the replan triggers and the tripwire: removes surfacing that Claude Fable 5.1 and GPT-6 Astra do not do natively; reopens when a probe shows unprompted surfacing of scope and contract impact on every model used for dispatch, each named and dated in the reopening record.

## Decision Boundary

Invariant: a pause mandate exists only for the three cases above; surfacing of scope and contract impact stays an obligation in Worker and Orchestrator text.

Not covered: the tripwire's exact conditions (including that it reaches shared types and boundaries outside the Worker's scope, because Claude Fable 5.1 and GPT-6 Astra do not volunteer the cleaner alternative) and what counts as material; those live in skill text.

## Validation

Replan Triggers in `orchestration-harness/SKILL.md` and Drift Tripwires in `engineering-quality-baselines/SKILL.md` name the three cases.

## Revisit When

Checked on 2026-09-06 against Claude Fable 5.1 and GPT-6 Astra. Replacing either model with another reopens this record. A real-task miss where a contract change or a workaround went unsurfaced reopens it.
