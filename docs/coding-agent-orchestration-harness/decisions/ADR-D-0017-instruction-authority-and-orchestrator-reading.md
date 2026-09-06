---
status: accepted
adr_type: design
date: 2026-09-06
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "GPT-6 Astra"]
informed: []
warrant:
  warranted_by: "without this record, future work would likely restore loader text that claims user authority, re-tighten the research gate to forbid the Orchestrator from reading code, and turn record-and-surface triggers back into pause-and-ask mandates, because each reads as the safer default in isolation"
  detected_signals: "cross-boundary authority shape (which instruction source outranks which); rejected alternatives likely to be re-proposed; premises likely to expire (the behavior profile of the daily-use models); a decider's ruling setting a durable governance default"
  cost_of_violation: "on a model that ranks conversation instructions above skill text and pauses whenever input could change the result, a loader that claims user authority makes every Orchestrator-to-subagent instruction lose to the loader, and pause mandates stack on the model's own asking bias; the failure is silent, it looks like caution"
  cost_of_wrong_preservation: "if a future daily-use model stops surfacing scope and contract impact on its own, record-and-surface without a pause becomes silent scope drift"
  cost_of_over_extension: "reading this as license to drop the three hard-stop cases, the plan-approval gate, or the research waiver record; those are consent and coordination contracts, not model-capability compensation"
supersedes: ["ADR-D-0008-codex-explicit-subagent-authorization-and-async-dispatch-lifecycle.md"]
superseded_by: null
supersession_scope: partial
depends_on: ["ADR-D-0018-evidence-tiers-for-removing-harness-content.md"]
---

# ADR-D-0017: Instruction authority and Orchestrator reading under frontier models

## Context and Problem Statement

Three harness rules compensated for older models: the Codex loader declared itself "explicit user direction" so the harness would be followed; the Research Dispatch Gate forbade the Orchestrator from reading implementation files before a Researcher returned; replan triggers and the drift tripwire mandated a pause for user confirmation on any material discovery. The daily-use fleet in September 2026 ranks the user's conversation instructions above skill text, reads and triages well, and pauses on its own whenever input could change the result. Each rule now inverts: the loader claim outranks Orchestrator-to-subagent instructions, the reading ban forces a dispatch round-trip to learn what a short read settles, and the pause mandate stacks on the model's own asking bias. What the fleet does not do unprompted is surface a public-contract change or name the cleaner alternative to a workaround; those obligations stay.

## Decision Drivers

- Harness text must be truthful about its authority: it is a skill, below the user's conversation.
- Surfacing scope and contract impact stays an obligation; pausing on every discovery does not.
- Consent and coordination contracts are unchanged.

## Decision

1. **Harness text holds no user authority.** Loader and adapter text never presents itself as the user's instruction. It states that the user installed the harness and that the harness is followed for coding tasks unless the user's conversation instructions say otherwise, so an instruction from any channel below the user (including the Orchestrator to a subagent) is weighed as such. This supersedes the ADR-D-0008 clause that made loader use "explicit user direction"; the rest of ADR-D-0008 stands.
2. **Reading is not gated behind a Researcher.** The Orchestrator may read the repository to decide triviality and scope; Researchers are dispatched for unfamiliar or cross-cutting areas. Non-trivial work that proceeds without a Researcher carries a recorded waiver with its reason, so the choice stays visible and reviewable.
3. **Discoveries are recorded and surfaced, and pause only for three cases.** A material discovery is written into the plan's decision record and surfaced at the next report or integration point rather than halting for confirmation. Confirmation is required only for a contract-shape change, an irreversible or outward-facing action, or a fix whose only path inside the Worker's scope is a workaround. Because the fleet does not volunteer the cleaner alternative to a workaround, the tripwire's scope includes shared types and boundaries outside the Worker's scope that the plan could change on request.

## Considered Options

1. Keep the three rules and override them per task in prompts.
2. Delete the loader, the research gate, and the replan triggers outright.
3. Reword: truthful authority, reading with a recorded waiver, record-and-surface with three hard stops and a widened tripwire scope.

## Decision Outcome

Chosen option: **Reword**. Option 1 keeps a silent failure on the model that most needs the fix, and per-task overrides travel through exactly the channel the loader claim defeats. Option 2 removes surfacing the fleet does not do natively. Option 3 keeps the obligations and the hard stops while removing the compensation.

### Rejected Alternatives

The "explicit user direction" wording is false on the fleet's instruction hierarchy and fails invisibly; it reopens only if a daily-use Codex model refuses subagent dispatch without an authority claim. Deleting the replan triggers reopens only if a fleet-wide probe shows unprompted surfacing of scope and contract impact.

## Consequences

- Positive: Orchestrator-to-subagent instructions are weighed on their merits on Codex; the Orchestrator triages by reading; routine discoveries no longer block on the user.
- Negative / tradeoffs: an Orchestrator that reads widely instead of dispatching trades context for round-trips and must still record the waiver; a discovery that should pause now depends on the three cases being recognized.

## Decision Boundary

Invariant: harness text never claims user authority; a pause mandate exists only for the three hard-stop cases; non-trivial work without a Researcher carries a recorded waiver; surfacing of scope and contract impact stays an obligation in Worker and Orchestrator text. Changing any of these requires a superseding ADR.

Not covered: the exact loader wording, the waiver's format and destination, Researcher dispatch heuristics, the tripwire's trip conditions, and which discoveries count as material; those are calibrated in skill text and plan records.

## Measurement Basis

Guard probes and verification cells under `docs/coding-agent/experiments/frontier-guard-probes/`, run under ADR-D-0018 class 3. What they demonstrate: with the old loader, a real peer-channel instruction to skip the harness was overridden; with nothing loaded, GPT-6 Astra widened a documented public contract silently and both models omitted the cleaner alternative to a workaround; with the modified harness loaded, both models surfaced the contract change and produced the design alert on the same fixtures. What they do not demonstrate: compliance with the new loader on a real peer channel. The post-change loader cell used an Orchestrator-framed instruction inside a user turn, a proxy; the live peer-channel check is a pending follow-up (`docs/coding-agent/plans/active/frontier-guidance-follow-ups-plan.md`, Task_4), and until it passes, decision 1 is a constraint, not a certified outcome.

## Validation

The Codex loader contains no authority claim; the Research Dispatch Gate and its reference agree; replan and tripwire text name the three hard-stop cases; the live peer-channel check passes, at which point this section is updated to cite it.

## Revisit When

A daily-use model changes: rerun fixtures A and C before keeping record-and-surface. A Codex model refuses subagent dispatch without an authority claim, or the live peer-channel check fails: reopen the loader wording with that evidence.

## More Information

Partially supersedes ADR-D-0008 (loader authority clause only). Evidence classes: ADR-D-0018. Implementing plan: `docs/coding-agent/plans/completed/frontier-model-guidance-refresh-plan.md`.
