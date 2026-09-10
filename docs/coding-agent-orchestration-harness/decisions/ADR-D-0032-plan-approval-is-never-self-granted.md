---
status: accepted
adr_type: design
date: 2026-09-10
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "GPT-6 Astra"]
informed: []
supersedes: []
superseded_by: null
depends_on: ["ADR-D-0017-harness-text-holds-no-user-authority.md", "ADR-D-0020-loader-routed-sessions-assume-the-orchestrator-role.md"]
---

# ADR-D-0032: Approval of a non-trivial plan comes only from the user, never from the Orchestrator or from the request that produced the plan

## Context and Problem Statement

A session that assumes the Orchestrator role (ADR-D-0020) plans non-trivial work and then needs authorization to execute it. Two readings of the Plan Gate let execution start without any human seeing the plan: the Orchestrator waives approval on its own authority with a recorded reason, or the ordinary task request ("add X") is taken as approval of whatever plan results from it. On 2026-09-08 a headless GPT-6 Astra session under the installed loader took both readings, implemented the work, and no human had seen the plan. The fork is whether approval attaches to the request or to the presented plan, and who may grant it.

## Decision

In plan mode, execution of non-trivial work is authorized only by the user: either an explicit approval of the plan that was presented, or an explicit waiver from the user that names the approval step. The Orchestrator never waives that approval on its own authority; it may reclassify work as trivial under the Plan Gate's tripwires, and that classification is reviewable. A task request authorizes planning, not execution: it is not approval of the plan it produces. When no applicable approval or waiver from the user exists and no user can answer, the Orchestrator presents the plan and ends the turn; elapsed time, silence, and the absence of a human channel confer no new authorization and revoke none already given.

## Why

The party that would benefit from skipping approval cannot grant it to itself, and a request describes a goal, not a plan, so it cannot approve a plan that did not exist when it was made; a presented plan awaiting a human is the correct resting state for a session nobody is watching.

## Rejected Alternatives

- Orchestrator self-waiver with a recorded reason and evidence: rejected outright; the record is written by the party the waiver benefits, so it constrains nothing.
- A task request counts as approval of the resulting plan: reopen only if plan review moves entirely to a runtime mechanism that shows the plan to the user before any execution step in every runtime the harness supports.
- A headless fallback that proceeds after a timeout: rejected outright; silence carries no authority.

## Decision Boundary

Invariant: approval or waiver of a non-trivial plan comes from the user, addressed to the presented plan or to the approval step itself; the Orchestrator and the originating request are never sources of it.

Not covered: the trivial/non-trivial tripwires and who applies them; the wording of the Plan Gate, the lifecycle reference, and the runtime entry points; how the presented plan is surfaced in each runtime; goal mode, whose envelope ratification is governed by ADR-D-0027.

## Validation

- The Plan Gate, its lifecycle reference, and every runtime entry point that restates the approval condition name the user as the only source of approval or waiver.
- A loader probe given an ordinary non-trivial request presents a plan and ends the turn with only planning artifacts written; the same request with an explicit user waiver proceeds past the Plan Gate.

## Revisit When

- A supported runtime gains a native plan-approval step that the harness can bind to, so that the request-as-approval alternative can be re-examined.
- The premise that a session under the installed loader will take a self-waiver or request-as-approval path when the text allows it was observed in a GPT-6 Astra session on 2026-09-08; the decision does not rest on that premise, so a model change reopens the probe, not the decision.

## More Information

Probe method and evidence: `docs/coding-agent/experiments/frontier-guard-probes/` in git history at `2a5ebf9`. Related records: ADR-D-0017 (harness text holds no user authority), ADR-D-0020 (loader-routed sessions assume the Orchestrator role), ADR-D-0027 (goal-mode envelope ratification).
