---
status: proposed
adr_type: design
date: 2026-11-24
deciders: ["ebigunso"]
consulted: ["Claude Opus 5.5"]
informed: []
supersedes: ["ADR-D-0065-a-ratified-brief-authorizes-a-plan-or-a-goal-envelope-only-on-a-closed-review-and-a-value-audit-that-holds-nothing.md"]
superseded_by: null
depends_on: ["ADR-D-0139-non-trivial-work-is-authorized-only-by-the-person-directing-the-work.md"]
---

# ADR-D-0142: What is added to or changed in a plan or a goal envelope after its execution starts needs fresh authorization from the same authority before it is built or acted on

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. The Orchestrator session is a session that holds the Orchestrator role (ADR-D-0090) and plans, dispatches and reports the work. A unit here is a plan, or the envelope of a goal-mode run together with its goal condition.

A plan or a goal envelope is authorized before anything of it executes: under a ratified brief by the ratification, on a review and a value audit of that unit (ADR-D-0141); without one, by the person directing the work's own approval or waiver (ADR-D-0139). The authority is to stand behind what is built. What a unit decides changes as the work goes, and a change made after execution starts is in no unit that authority judged; were the authorization to follow the unit through its changes, the Orchestrator, which makes them, would decide which of them it still covers. The fork is what an authorization covers once execution has started, and what a change after that needs.

## Decision

- An authorization of a plan or a goal envelope covers the unit as it stands when execution starts.
- What is added to or changed in what a plan decides, or in a goal envelope, afterwards is not authorized by it and needs fresh authorization before it is built or acted on, from the same authority on that authority's own terms: under a ratified brief, the conditions on which the ratification authorizes such a unit (ADR-D-0141), on the unit as it then stands; without one, the person directing the work's own approval or waiver.
- A repeated judgement on unchanged inputs is not fresh authorization.

## Why

The ratification carries the authority of the person directing the work only for the unit the verdict judged, and an authorization that followed the unit through later changes would leave the party that makes them to decide which of them need no new judgement, which the product philosophy's "What it must not be" refuses: "Not its own judge. A builder's confidence in its own work is not evidence, and a longer list of rules does not make it so."

## Rejected Alternatives

- The verdict follows the unit through later changes: rejected outright; the Orchestrator would decide which changes need no new audit, which is the judgement ADR-D-0134 keeps from it.

## Decision Boundary

Not covered: the authorities themselves and the forms an authorization takes (ADR-D-0139); the conditions on which a ratified brief authorizes a plan or a goal envelope (ADR-D-0141); which brief governs the work and what counts as its ratification having reached the session (ADR-D-0112 and the harness text); how a revision is reviewed and audited and at which position, and what the Orchestrator does while a change awaits authorization or when it is not authorized, which the harness text states; what an envelope consists of and that the loop never changes it (ADR-D-0084, ADR-D-0086); how a goal run is graded once its loop starts, and what the run does with an item held during it (ADR-D-0082, ADR-D-0067); how the unit records an authorization; the wording of the harness text that states this.

## Validation

The decision is broken where:

- a change to what a plan decides, or to a goal envelope, made after execution started was built or acted on by the authorization given before it;
- a change was taken as authorized afresh on a judgement repeated on unchanged inputs;
- a change was authorized afresh by an authority other than the one that authorized the unit, or not on that authority's own terms.

## Revisit When

- The premise that the party that makes a change cannot be the one to say that the authorization already given still covers it no longer holds.

## More Information

With ADR-D-0141 and ADR-D-0143, replaces ADR-D-0065 in full; the decision carried here is the same. Carried here from it: what an authorization covers once execution starts and what a change after that needs, a goal envelope included. It is a record of its own because it binds whichever authority authorized the unit, the person directing the work's own approval or waiver included. ADR-D-0086 leaves to this decision that a changed envelope is authorized afresh. Source of intent: `docs/coding-agent/briefs/completed/value-level-operation-brief.md`, "Who it is for and why", "Stops during a run", "Value audit" and "Lifecycle"; the brief "A quiet Orchestrator session under a brief" (`docs/coding-agent/briefs/completed/quiet-orchestrator-session-brief.md`), "What the plugin states" and "Directed during the run". Related records: ADR-D-0139 (who authorizes non-trivial work), ADR-D-0086 (the loop never changes its envelope), ADR-D-0084 (the envelope), ADR-D-0134 (the value audit in a plan-mode run), ADR-D-0082 (the value audit in a goal run), ADR-D-0067 (a determined remedy carried out without a stop under a brief).
