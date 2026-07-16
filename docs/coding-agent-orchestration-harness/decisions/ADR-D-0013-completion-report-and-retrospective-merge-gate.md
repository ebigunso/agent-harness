---
status: accepted
adr_type: design
date: 2026-07-16
deciders:
  - ebigunso
consulted:
  - Claude Fable 5
informed: []
supersedes: []
superseded_by: null
---

# ADR-D-0013: Self-Asserted Completion Report Behind A Human Retrospective Merge Gate

## Context and Problem Statement

Goal mode relocates oversight to review-after, which only works if retrospectives actually happen and are cheap enough to be done well. A raw iteration journal is a pile of text; requiring humans to mine it invites rubber-stamping. Separately, the report's enforcement level needed a decision: a validator-checked contract (like the Worker report) or reviewer-verified prose. An early draft also required verbatim assessor dispatch texts and verdicts inline in the report, which was rejected as hurting readability — that verification belongs to an agent, not the report body.

## Decision Drivers

- Merge must remain a human decision, informed rather than burdened.
- The loop should pre-assert everything a retrospective would otherwise dig for.
- Reports are judgment-heavy prose; validators check shape, not truth (the harness rule against overfitting validators to prose applies).
- Readability of the human-facing artifact is a design property, not a nicety.

## Decision

Goal completion is not merge authorization. Before the goal branch may merge, the loop produces a self-asserted completion report — concise and contract-shaped — containing: the satisfied goal condition with evidence inline; a one-line assessment assertion (assessor dispatches occurred at the required cadence and complied with the fixed template); per-invariant integrity assertions with their proving checks; envelope compliance with every decide-and-journal item surfaced (autonomous judgment-heavy calls the loop was allowed to make but flagged for retrospective review); a trajectory summary (pivots, stalls, abandonments); and a checkpoint index mapping commits to iterations.

The report is reviewer-verified prose, not a validator-checked contract. Before the report is accepted, the pre-merge reviewer autonomously verifies its assertions — assessment cadence and template compliance, invariant integrity, envelope compliance — against the journal, where the verbatim evidence lives. A report whose assertions fail verification is invalid and cannot support merge. The journal remains the backing audit trail; the report is the human interface to it. Merge stays behind the existing human hard stop, informed by the verified report.

## Considered Options

1. Human retrospective reads the raw journal; no report artifact.
2. Validator-checked report contract mirroring the Worker report schema.
3. Self-asserted concise report with verbatim evidence inline (including assessor dispatch texts).
4. Self-asserted concise report, reviewer-verified against the journal, verbatim evidence staying in the journal.

## Decision Outcome

Chosen option: **Option 4**.

Option 1 makes retrospectives expensive and therefore skipped or shallow. Option 2 checks shape rather than truth for a judgment-heavy artifact. Option 3 verifies the right things in the wrong place, trading readability for inline evidence a reviewer agent can check at its source. Option 4 keeps each artifact in its role: journal as complete trail, report as readable interface, reviewer as independent verifier, human as merge authority.

## Consequences

### Positive

- Retrospectives become cheap: the human reads a verified report, not a pile of text, and can drill into the journal via the checkpoint index when warranted.
- Assessor starvation and envelope violations surface mechanically at the strongest existing gate (merge).
- The merge hard stop is preserved unchanged from plan mode.

### Negative / Tradeoffs

- Verification quality depends on the pre-merge reviewer's diligence; the report's assertion structure is designed to make that check enumerable.
- No validator means report-shape drift is possible; if trials show recurring structural failures, the assessment-assertion section is the one narrowly checkable candidate.

## Validation

- Completion reports contain all six sections; the pre-merge reviewer's verification of assertions against the journal is itself recorded.
- Goal branches never merge on an unverified or invalid report.
- Retrospective outcomes (accepted, reverted iterations, lessons) are captured per the improvement loop.

## Revisit When

- Trials show recurring report failures of a structural kind a narrow validator would catch honestly.
- Retrospectives are being skipped despite the cheap-report design (then the gate, not the artifact, needs strengthening).

## More Information

- `docs/coding-agent-orchestration-harness/design/goal-mode-design.md` (pillars 2 and 6)
- ADR-D-0012 (assessment cadence enforcement), ADR-I-0003 (contract-first validation strategy — the contrast case)
