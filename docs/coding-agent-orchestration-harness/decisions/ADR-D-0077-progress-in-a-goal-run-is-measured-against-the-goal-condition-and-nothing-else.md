---
status: proposed
adr_type: design
date: 2026-11-11
deciders: ["ebigunso"]
consulted: ["Claude Fable 5", "Claude Fable 5.2"]
informed: []
supersedes: ["ADR-D-0011-single-object-progress-definition.md"]
superseded_by: null
---

# ADR-D-0077: Progress in a goal run is measured against the goal condition and nothing else

## Context and Problem Statement

Terms used here: a goal run is a run in goal mode, in which a loop works toward a stated goal condition. The journal is the run's append-only record of its iterations and their evidence. The gap is the distance left to the goal condition, where the condition yields one that can be counted. A plateau is a stretch of the run in which that count does not move.

A goal loop continues only while it progresses (ADR-D-0074), so the run needs a working notion of progress. Useful measures of movement depend on the type of task, and the type may be unknown when the goal starts. The fork is whether progress is defined by something written beside the goal, for all goals or for each, or by the goal condition itself.

## Decision

- Progress in a goal run is reduction in the expected distance to the goal condition. Nothing other than the goal condition defines it: no measure of movement is defined or maintained beside the goal, for all goals or for one.
- Where the goal condition yields a gap that can be counted, progress is read from that count. On a plateau, progress is what the run learned, and it counts only where the journal argues that what was learned credibly reduces the remaining distance or uncertainty toward this goal. A falsified hypothesis is progress on that argument.
- How the gap is read is settled for the particular goal before its loop starts, so that the loop cannot shape the reading to flatter its own progress. A reading is a way of measuring the goal condition, never a definition of progress in its own right.
- A cheaper intermediate signal may inform the journal. No judgement of progress rests on one.

## Why

A measure of movement defined apart from the goal can diverge from it, so that a loop is moving by its own definition while not approaching the goal, and it is one more thing to game, maintain and watch. Measuring against the goal condition alone keeps the goal authoritative and needs no measure fixed in advance for a type of task that may be unknown when the goal starts.

## Rejected Alternatives

- Movement metrics fixed for all goals: they lost because useful measures depend on the type of task, and the type may be unknown when a goal starts; reopen if goal runs turn out to be of so few kinds that one fixed set of measures fits them all.
- A definition of movement written for each goal and maintained as an instrument of its own: it lost because it duplicates the goal in a form that can be gamed, has to be maintained and can diverge from the goal; rejected outright.

## Decision Boundary

Not covered: what counts as a stall (ADR-D-0078); a change during the run to how the gap is read or to the bar a plateau argument must clear, tightened freely and loosened only with the owner's word (ADR-D-0079); that the loop never changes its goal (ADR-D-0087); that a loop continues only while it progresses, and what a stall triggers (ADR-D-0074); who judges whether a plateau argument is credible (ADR-D-0080) and which way doubt resolves (ADR-D-0081); the examples of gaps that can be counted, the form of the journal, how a goal with no countable gap is marked and that goal construction prefers conditions that can be counted, all of which goal mode's text states.

## Validation

The decision is broken where:

- progress was judged from a measure defined apart from the goal condition;
- a plateau was counted as progress with no argument in the journal linking what was learned to the goal;
- a judgement of progress rested on an intermediate signal;
- a loop started with no reading of its gap settled, and chose one while it ran.

## Revisit When

- The premise that the goal condition, read as a count or by argument, measures progress well enough for every class of goal no longer holds: a recurring class of goal has no workable reading of its gap, and assessment by argument alone proves too weak. ADR-D-0011, dated 2026-07-16, names no trial of this premise.

## More Information

Replaces ADR-D-0011 at what progress is measured against; ADR-D-0078 and ADR-D-0079 replace the rest of it. On when the reading of the gap is settled, this record states goal mode's text and not ADR-D-0011's wording, which had early assessments choose it. Design: `docs/coding-agent-orchestration-harness/design/goal-mode-design.md`.
