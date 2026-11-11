---
status: proposed
adr_type: design
date: 2026-11-11
deciders: ["ebigunso"]
consulted: ["Claude Fable 5", "Claude Fable 5.2"]
informed: []
supersedes: ["ADR-D-0014-assessor-goal-validity-re-examination.md"]
superseded_by: null
---

# ADR-D-0076: An independent assessor asks whether a goal is still worth pursuing

## Context and Problem Statement

Terms used here: a goal run is a run in goal mode, in which a loop works toward a stated goal condition. The optimizer is the agent pursuing the goal. The journal is the run's append-only record of its iterations and their evidence. The assessor is the independent judgement of whether a goal loop continues (ADR-D-0080). The goal's owner is the person whose goal it is.

A goal loop can make perfect progress toward a goal that should no longer be pursued: requirements shift, evidence gathered during the run shows the goal was framed on a wrong assumption, or the stated condition turns out to reward an outcome nobody wants. Efficient pursuit of a wrong goal is a worse failure than a stall and harder to notice from inside the loop. The fork is whether anyone examines the goal itself while the loop runs, and if so who examines it and where what is found goes.

The examination improves the odds and guarantees nothing: a wrong goal whose evidence never reaches the journal stays undetected until the human's retrospective.

## Decision

- Whether the goal is still worth pursuing is examined by the independent assessor, from the run's own evidence, at every assessment. No assessment judges progress and leaves the goal unexamined.
- Where the examination fails, the loop stops and the challenge goes to the goal's owner with the evidence that prompted it. Stopping there is a successful termination.

## Why

Goal mode removes the human touchpoints at which direction is otherwise re-checked, so nothing questions the goal unless the question is given to someone. It goes to the assessor because the assessor has no stake in the goal and already reads the run's evidence, and a failed examination goes to the goal's owner because what follows from it is a change of direction, which only the owner is entitled to make.

## Rejected Alternatives

- The assessor judges progress only, a goal that has gone stale being left to the human's retrospective: it lost because the retrospective finds a wrong goal after the run's cost is sunk, and it can revert changes but not spent effort; reopen if, run after run, the examination finds no goal to question.
- The optimizer examines its own goal: it lost because it gives the question to the party motivated to answer that the run should continue; rejected outright, on the ground on which ADR-D-0080 rejects the optimizer judging its own continuation, that the conflicted party would sit in the judge's seat.

## Decision Boundary

Not covered: that the loop never re-scopes, reframes or abandons its goal and that a change of goal is the owner's, which would bind with this examination gone and is held by ADR-D-0087; the questions the examination asks, the form of the assessor's verdict, the escalation level at which the loop stops and how the challenge reaches the owner, all of which goal mode's text states; who the assessor is and what it reads (ADR-D-0080), and which way its ties break (ADR-D-0081); how the assessor is packaged (ADR-D-0050); the protection of the goal's measures against being loosened during a run (ADR-D-0079), which is a different case from a condition that is intact and no longer measures what its owner meant.

## Validation

The decision is broken where:

- an assessment judged progress and left the goal unexamined;
- a loop continued past a failed examination, or a challenge reached the owner without the run's evidence for it.

## Revisit When

- The premise that a goal run has no human moment between its start and its retrospective at which direction is re-checked no longer holds.
- The premise that goals do go stale or prove wrongly framed during a run, often enough to be worth an examination at every assessment, no longer holds: run after run, the examination finds no goal to question. ADR-D-0014, dated 2026-07-16, names no trial of this premise.
- Challenges so frequent that they show goals are being constructed weakly do not reopen this record; they reopen how a goal is constructed before its loop starts, which goal mode's text states.
- Wrong goals reaching the retrospective although the examination was made do not reopen this record; they reopen the examination's questions and the assessor's cadence, which goal mode's text states.

## More Information

Replaces ADR-D-0014 at the assessor's examination and what follows its failure; ADR-D-0087 replaces the rest of it, that the loop never re-scopes, reframes or abandons a goal on its own. Related: ADR-D-0080 (the assessor), ADR-D-0074 (the stall rule), ADR-D-0073 (the goal lifecycle). Design: `docs/coding-agent-orchestration-harness/design/goal-mode-design.md`, the section on independent in-loop assessment.
