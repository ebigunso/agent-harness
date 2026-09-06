---
status: accepted
adr_type: design
date: 2026-09-06
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "GPT-6 Astra"]
informed: []
warrant:
  warranted_by: "without this record, future work would likely re-tighten the research gate to forbid the Orchestrator from reading code before a Researcher returns, because it reads as the disciplined default"
  detected_signals: "rejected alternative likely to be re-proposed; premises tied to Claude Fable 5.1 and GPT-6 Astra as checked on 2026-09-06"
  cost_of_violation: "every non-trivial task pays a dispatch round-trip to learn what a short read settles, and triviality itself cannot be judged without one"
  cost_of_over_extension: "dropping the recorded waiver; without it the choice to skip research is invisible to review"
supersedes: []
superseded_by: null
supersession_scope: null
depends_on: ["ADR-D-0018-evidence-tiers-for-removing-harness-content.md"]
---

# ADR-D-0019: The Orchestrator reads to triage

## Context and Problem Statement

The Research Dispatch Gate forbade the Orchestrator from reading implementation files or searching the repository before a Researcher returned, even to decide whether work was trivial. That protected the context budget of the models the harness was written against, GPT-5.5 and Claude Fable 5. Claude Fable 5.1 and GPT-6 Astra triage well by reading, and the ban forced a dispatch round-trip to learn what a short read settles.

## Decision

The Orchestrator may read the repository to decide triviality and scope. Researchers are dispatched for unfamiliar or cross-cutting areas. Non-trivial work done without a Researcher carries a recorded waiver with its reason.

## Why

Reading is cheaper than a dispatch round-trip, and the waiver keeps the choice reviewable.

## Rejected Alternatives

- Keep the ban and waive per task: waivers became the rule, and the ban still blocked the triviality decision itself.

## Decision Boundary

Invariant: non-trivial work without a Researcher carries a recorded waiver with its reason.

Not covered: the waiver's format and destination, and the heuristics for when a Researcher is dispatched; those live in skill text.

## Validation

The Research Dispatch Gate in `orchestration-harness/SKILL.md` and its lifecycle reference agree, and neither forbids reading before research.

## Revisit When

Checked on 2026-09-06 against Claude Fable 5.1 and GPT-6 Astra. Replacing either model with another reopens this record. Observed context exhaustion from Orchestrator reading on real tasks reopens it.
