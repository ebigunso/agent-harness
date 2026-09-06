---
status: accepted
adr_type: design
date: 2026-09-06
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "GPT-6 Astra"]
informed: []
warrant:
  warranted_by: "without this record, future work would likely restore loader text that claims user authority, re-tighten the research gate to forbid the Orchestrator from reading code, and turn record-and-surface triggers back into pause-and-ask mandates, because each of those reads as the safer default in isolation"
  detected_signals: "cross-boundary authority shape (which instruction source outranks which); rejected alternatives likely to be re-proposed; premises likely to expire (the behavior profile of the daily-use models); a decider's ruling setting a durable governance default"
  cost_of_violation: "on models that rank conversation instructions above skill text and pause whenever input could change the result, a loader that claims user authority makes every Orchestrator-to-subagent instruction lose to the loader, and pause mandates stack on the model's own asking bias; the failure is silent, it looks like caution"
  cost_of_wrong_preservation: "if a future daily-use model stops surfacing scope and contract impact on its own, record-and-surface without a pause becomes silent scope drift; the probe protocol in ADR-I-0006 is the check that detects this"
  cost_of_over_extension: "reading this as license to drop the three hard-stop cases, the plan-approval gate, or the Research waived record; those are consent and coordination contracts, not model-capability compensation"
supersedes: ["ADR-D-0008-codex-explicit-subagent-authorization-and-async-dispatch-lifecycle.md"]
superseded_by: null
supersession_scope: partial
depends_on: ["ADR-D-0015-remove-obsolete-guidance-as-models-improve.md"]
---

# ADR-D-0017: Instruction authority and Orchestrator reading under frontier models

## Context and Problem Statement

Three harness rules were written for models that needed to be pushed to follow skills, kept from reading too much, and stopped before acting on a discovery. The daily-use fleet in September 2026 (Claude Fable 5.1, GPT-6 Astra) behaves differently in ways that invert the effect of those rules.

- The Codex loader block declared that using it was "explicit user direction" to follow the harness (ADR-D-0008). GPT-6 Astra ranks instructions from the user's conversation above skill and `AGENTS.md` text. The loader's claim promotes the harness to user authority, so an instruction arriving through any other channel loses to it. In a 2026-09-06 probe, a peer-channel instruction to skip the harness for a bounded task was overridden with "Harness loaded under the user AGENTS.md instruction"; the same instruction given in the user turn was honored.
- The Research Dispatch Gate forbade the Orchestrator from reading implementation files or running repo-wide search before a Researcher returned, even to decide whether work was trivial. That protected a weak main thread's context budget; on the current fleet it forces a dispatch round-trip to learn what a two-minute read would settle.
- Replan triggers and the drift tripwire mandated a pause for user confirmation on any material discovery. GPT-6 Astra's own documented default is to pause and ask whenever input could change the result. Stacking a mandate on that bias produced approval-seeking on routine discoveries, while the guard's real value, surfacing the discovery at all, was not native for that model: with nothing loaded, it widened a documented public API contract without a question.

## Decision Drivers

- Instruction authority must be truthful: harness text is a skill, and skills rank below the user's conversation instructions on the fleet in use.
- The Orchestrator's context budget is a calibration, not an invariant; the fleet's context windows and judgment make "read nothing until Researcher returns" a net cost.
- Surfacing scope and contract impact must stay mandated; pausing on every discovery must not.
- Consent and coordination contracts (plan approval, hard-stop cases, `Research waived` record) are unchanged.

## Decision

1. Loader and adapter text never claims user authority. The Codex loader states that the user installed it and that the harness is followed for coding tasks unless the user's instructions in the conversation say otherwise. This partially supersedes the ADR-D-0008 clause that made loader use "explicit user direction"; the rest of ADR-D-0008 (Orchestrator identity on loader routing, minimal rule load, async child lifecycle) stands.
2. The Research Dispatch Gate becomes: dispatch Researchers for unfamiliar or cross-cutting areas; the Orchestrator may read repository files directly to decide triviality and scope, and records `Research waived: <reason>` whenever non-trivial work proceeds without a Researcher.
3. Replan triggers and the drift tripwire are record-and-surface: the Orchestrator logs the insight in the plan Decision Log and surfaces it in the next report or wave integration. A pause for confirmation applies only to the three hard-stop cases: a contract-shape change (routed through Escalation Ruling), an irreversible or outward-facing action, or a fix whose only path inside `owns` is a workaround.

## Considered Options

1. Keep all three rules as written and rely on prompt-level overrides per task.
2. Delete the loader, the research gate, and the replan triggers outright.
3. Reword: truthful authority, reading allowed with a waiver record, record-and-surface with three hard stops.

## Decision Outcome

Chosen option: **Reword**. Option 1 keeps a silent failure on the model that most needs the fix, and per-task overrides are exactly the channel the loader claim defeats. Option 2 removes guards the 2026-09-06 probes showed are not native: with no harness text, GPT-6 Astra did not surface a public-contract change, and neither model named the cleaner boundary change or its cost delta when a workaround was available. Option 3 keeps the surfacing obligation and the three hard stops while removing the parts that only compensated for older models.

### Rejected Alternatives

Keeping the "explicit user direction" wording was rejected because it is false on the fleet's instruction hierarchy and its failure mode is invisible; it would legitimately reopen only if a daily-use Codex model again refused subagent dispatch without an authority claim, which the Task_6 regression cell in the implementing plan checks. Deleting the replan triggers outright was rejected because the surfacing behavior is not native to GPT-6 Astra; it would reopen if a fleet-wide probe showed unprompted surfacing of scope and contract impact.

## Consequences

- Positive: Orchestrator-to-subagent instructions work on Codex; the Orchestrator can triage by reading; routine discoveries no longer block on the user.
- Negative / tradeoffs: an Orchestrator that reads widely instead of dispatching a Researcher trades context for round-trips and must still record the waiver; a discovery that should have paused now depends on the three hard-stop cases being recognized.

## Decision Boundary

Invariant: harness text never claims to be the user; a pause mandate exists only for the three hard-stop cases; non-trivial work without a Researcher carries a `Research waived: <reason>` record. Changing any of these requires a superseding ADR.

Not covered: the wording of the loader block, the Researcher dispatch heuristics, and which discoveries count as material; those are calibrated in skill text and plan Decision Logs.

## Measurement Basis

Probe fixtures A-D run 2026-09-06 across Claude Fable 5.1 (subagent, no harness), GPT-6 Astra pure baseline (ephemeral, no instructions loaded), GPT-6 Astra with the harness on, and the peer-channel loader override; recorded by ADR-I-0006 under `docs/coding-agent/experiments/frontier-guard-probes/`. Single run per cell; enough to show which behaviors are and are not native, not to size effects.

## Validation

`codex/snippets/AGENTS.md` contains no authority claim; `orchestration-harness/SKILL.md` Research Dispatch Gate and `references/lifecycle-gates.md` agree; Replan Triggers and Drift Tripwires name the three hard-stop cases; the implementing plan's Task_6 cells (peer-channel compliance, subagent-dispatch regression, public-contract surfacing) pass.

## Revisit When

A daily-use model changes. Weaker instruction hierarchy or a model that stops surfacing contract impact: rerun the fixture A and C cells before keeping record-and-surface. A Codex model that refuses subagent dispatch without an authority claim: reopen the loader wording with that evidence.

## More Information

Implementing plan: `docs/coding-agent/plans/completed/frontier-model-guidance-refresh-plan.md` after closeout. Evidence record: ADR-I-0006. Partially supersedes ADR-D-0008 (loader authority clause only).
