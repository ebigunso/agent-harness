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

# ADR-D-0011: Progress Is The Goal Read As A Gap, Not A Second Object

## Context and Problem Statement

Stall detection needs a working notion of progress, but "demonstrable movement" resists general definition: useful measures depend on the task type, and the task type may be unknown when a goal starts. An early design draft introduced a separately named, separately maintained "movement definition" instantiated per goal. That construction was challenged as inventing the same thing twice — and a movement definition that can diverge from the goal is itself a failure mode: a loop can be "moving" by its own definition while not approaching the goal.

## Decision Drivers

- One authoritative object per concept; a second definable object is a second Goodhart surface.
- Genuine plateau progress (diagnosis, harness-building, mid-refactor regressions) must not be flagged as stall.
- The definition must work when the task type is unknown at the start.
- Loosening any progress standard mid-run must be visible and gated.

## Decision

There is one object: the goal condition. Progress is reduction in expected distance to the goal, measured two ways:

- directly, when the goal condition yields a countable gap (failing tests, lint errors, files remaining, benchmark delta) — an executable condition usually provides this for free;
- epistemically, on plateaus: the journal must argue that what was learned credibly reduces the remaining distance or uncertainty toward this goal. A falsified hypothesis is progress when that linkage holds.

Stall is the conjunction of: gap unchanged, no credible goal-linkage argument, and attempts circling previously failed approaches. The gap reading — the chosen way of measuring the goal condition as a number mid-run — and the credibility bar for epistemic linkage are part of the goal condition: tightening either mid-run is free, loosening either is treated like pressure on a protected invariant and forces an ask-now escalation (the loop stops and waits for the user). Proxy metrics may inform the journal but are never load-bearing. Early assessments choose how to read the gap for the specific goal — a measurement refinement of the one object, not a second object.

## Considered Options

1. Fixed, globally defined movement metrics for all goals.
2. A per-goal "movement definition" instantiated and maintained as its own named instrument.
3. Progress as distance-to-goal on the single goal object, with direct and epistemic readings and a guarded gap reading.

## Decision Outcome

Chosen option: **Option 3**.

Option 1 fails task-type diversity. Option 2 duplicates the goal into a second Goodhartable, maintainable, divergence-capable object. Option 3 keeps the goal authoritative, handles unknown task types (the reading is refined as the task's nature emerges), and moves the plateau problem to where it is solvable: an explicit linkage argument judged by an independent assessor.

## Consequences

### Positive

- No second definition to maintain, game, or watch for divergence.
- Plateau work (bisection, instrumentation, temporary regressions) is legitimized through explicit goal-linkage rather than exempted by a looser standard.
- The Goodhart guard concentrates on one object with clear tighten-free/loosen-escalates semantics.

### Negative / Tradeoffs

- Epistemic linkage credibility is a judgment call; it requires the independent assessor (ADR-D-0012) rather than self-grading.
- Goals whose conditions yield no countable gap lean entirely on epistemic reading, which is weaker; condition construction should prefer countable forms.

## Validation

- Goal files name the gap reading; journal plateau entries contain explicit goal-linkage arguments.
- Any mid-run change to the gap reading or credibility bar appears as a journaled escalation, never a silent edit.
- Completion reports show gap trajectory from the condition's own measurements.

## Revisit When

- A recurring goal class has no workable gap reading and epistemic-only assessment proves too weak.
- Trials show the three-signal stall conjunction misfires systematically.

## More Information

- `docs/coding-agent-orchestration-harness/design/goal-mode-design.md` (pillars 1 and 3)
- ADR-D-0010 (progress obligation), ADR-D-0012 (who judges linkage credibility)
