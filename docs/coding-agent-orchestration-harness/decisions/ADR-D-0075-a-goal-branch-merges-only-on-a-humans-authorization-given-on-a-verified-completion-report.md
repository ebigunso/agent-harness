---
status: accepted
adr_type: design
date: 2026-11-11
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "Claude Fable 5.2"]
informed: []
supersedes: ["superseded/ADR-D-0031-goal-completion-never-authorizes-merge--superseded-by-ADR-D-0075.md"]
superseded_by: null
---

# ADR-D-0075: A goal branch merges only on a human's authorization given on a verified completion report

## Context and Problem Statement

Terms used here: a goal run is a run in goal mode, in which a loop works toward a stated goal condition. The journal is the run's append-only record of its iterations and their evidence. The completion report is the loop's own concise account of how the goal condition was met and what the run did on the way. The assessor is the independent judgement of whether a goal loop continues (ADR-D-0080, ADR-D-0050).

Goal mode moves oversight from approval before the work to review after it, which only works if that review happens and is cheap enough to be done well. A raw journal is a pile of text, and requiring a human to mine it invites rubber-stamping. The fork is what stands between a loop that reports its goal satisfied and the merge of its branch.

## Decision

- A loop that reports its goal satisfied has authorized no merge. A goal branch merges only on a human's authorization.
- What the human acts on is a concise completion report written by the loop, whose assertions a reviewer other than the loop has verified against the journal.
- A report that has not been verified, or one with an assertion the verification does not bear out, supports no merge.

## Why

Oversight of a goal run comes after the work, which only works if the human's review happens and is cheap enough to be done well. The journal is complete but unreadable and the loop's own claim is readable but unverified, so a verified report is the one thing a human can act on without either mining the journal or trusting the party that wrote the claim.

## Rejected Alternatives

- A human review over the raw journal, with no report: it lost because an expensive review is skipped or done shallowly; rejected outright.
- A report whose contract a validator checks: it lost because the report is judgement-heavy prose, and validators enforce contracts, not such prose (ADR-I-0007); reopen if trials show recurring structural failures in reports that a narrow validator would catch honestly, the report's assertion about the assessor's dispatches being the one candidate.
- The assessor's dispatch texts reproduced verbatim in the report: it lost because it verifies the right thing in the wrong place and destroys the report's readability; rejected outright.

## Decision Boundary

Not covered: the report's sections and wording, how the human's review is conducted and how its outcomes feed the improvement loop, which goal mode's text states; which role verifies the report (ADR-D-0050); how a human's authorization to merge is given.

## Validation

The decision is broken where:

- a goal branch merged without a human's authorization, or a loop's report that its goal was satisfied was taken as authorization to merge;
- the assertions of the report a human acted on had not been verified against the journal by a reviewer other than the loop;
- a merge rested on a report that had not been verified, or on one with an assertion the verification did not bear out.

## Revisit When

- The premise that a concise, verified report makes the human's review cheap enough to happen no longer holds: reviews of goal runs are found skipped though the report was there. What then needs strengthening is the stop before the merge, not the report. The premise was held when the decision was recorded on 2026-09-08; the record of that date names no check of it.

## More Information

Replaces ADR-D-0031 in full, at the same decision; ADR-D-0031 had itself replaced ADR-D-0013. Related: ADR-I-0007 (validators enforce contracts, never prose), of which the report's verification by a reviewer and not by a validator is an application; ADR-D-0050 (the Auditor), which keeps the report's verification with the Reviewer and has the report assert the cadence of the assessor's dispatches; ADR-D-0080 (the assessor). Design: `docs/coding-agent-orchestration-harness/design/goal-mode-design.md`, the sections on the iteration journal and checkpoints and on the completion report and human retrospective.
