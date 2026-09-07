---
status: proposed
adr_type: design
date: 2026-09-07
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1"]
informed: []
supersedes: ["ADR-D-0013-completion-report-and-retrospective-merge-gate.md"]
superseded_by: null
---

# ADR-D-0031: Goal completion never authorizes merge; a human retrospective on a verified completion report does

## Context and Problem Statement

Goal mode moves oversight to review-after, which only works if the retrospective happens and is cheap enough to be done well. A raw iteration journal is a pile of text, and requiring a human to mine it invites rubber-stamping. The fork is what stands between a loop that reports its goal satisfied and the merge of its branch.

## Decision

Goal completion is not merge authorization. Before a goal branch may merge, the loop produces a concise self-asserted completion report: the satisfied goal condition with evidence, an assessment-cadence assertion, per-invariant integrity assertions with their proving checks, envelope compliance with every judgment call the loop was allowed to make surfaced, a trajectory summary, and a checkpoint index mapping commits to iterations. The report is reviewer-verified prose: before it is accepted, the pre-merge reviewer verifies its assertions against the journal, where the verbatim evidence lives, and a report whose assertions fail is invalid and cannot support merge. Merge stays behind the existing human hard stop, informed by the verified report.

## Why

The journal is complete but unreadable and the loop's own claim is readable but unverified; the verified report is the one artifact a human can act on without either mining the trail or trusting the party that wrote it.

## Rejected Alternatives

- A human retrospective over the raw journal with no report: rejected outright; expensive retrospectives are skipped or shallow.
- A validator-checked report contract: reopen if trials show recurring structural failures a narrow validator would catch honestly; the assessment-assertion section is the one candidate. Validators enforce contracts, not judgment-heavy prose (ADR-I-0007).
- Verbatim assessor dispatch texts inline in the report: rejected outright; it verifies the right thing in the wrong place and destroys readability.

## Decision Boundary

Invariant: no goal branch merges on an unverified or invalid report, and completion never bypasses the human merge stop.

Not covered: the report's section list and wording, the retrospective procedure, and how outcomes feed the improvement loop, which the goal-mode reference owns.

## Validation

- The pre-merge reviewer's verification of the report's assertions against the journal is itself recorded.
- Goal branches never merge on an unverified or invalid report.

## Revisit When

- Retrospectives are skipped despite the cheap-report design; then the gate, not the artifact, needs strengthening.

## More Information

Replaces ADR-D-0013 in full; its report-enforcement-level clause is an application of ADR-I-0007. Design: `docs/coding-agent-orchestration-harness/design/goal-mode-design.md`, pillars 2 and 6. Cadence verification: ADR-D-0030.
