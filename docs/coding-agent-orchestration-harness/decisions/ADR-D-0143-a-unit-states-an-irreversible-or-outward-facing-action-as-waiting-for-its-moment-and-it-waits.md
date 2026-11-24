---
status: proposed
adr_type: design
date: 2026-11-24
deciders: ["ebigunso"]
consulted: ["Claude Opus 5.5"]
informed: []
supersedes: ["ADR-D-0065-a-ratified-brief-authorizes-a-plan-or-a-goal-envelope-only-on-a-closed-review-and-a-value-audit-that-holds-nothing.md"]
superseded_by: null
depends_on: ["ADR-D-0139-non-trivial-work-is-authorized-only-by-the-person-directing-the-work.md", "ADR-D-0136-a-standing-approval-is-given-only-by-whoever-holds-the-authority-for-the-action.md"]
---

# ADR-D-0143: A ratified brief authorizes a unit containing an irreversible or outward-facing action that no standing approval in effect covers only when the unit states the action as waiting for its moment, and the action waits in every case

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. A unit here is a plan, or the envelope of a goal-mode run together with its goal condition.

Under a ratified brief a unit starts without the person directing the work reading it, only when the value audit holds none of its items for a decision above the run (ADR-D-0141). An action that cannot be undone or that reaches outside the work is one the audit tests for on every item, and it is to be taken on the decision of whoever holds the authority for it; a standing approval in effect is that decision given once beforehand by the one entitled to give it (ADR-D-0136). Kept from starting until that person had read it, every plan with a publish or a merge in it would be one that person must read; authorized like any other item, the action would go ahead with the unit and not on that decision. The fork is whether a unit containing such an action can start on the ratification, and what becomes of the action.

## Decision

- A unit containing an irreversible or outward-facing action that no standing approval in effect covers (ADR-D-0136) is authorized only when the unit states the action as taken on the decision of whoever holds the authority for it, at its moment and not before; an action so stated does not count as an item held above the run; otherwise the ratification does not authorize the unit.
- Such an action itself waits for that decision in every case, its unit authorized or not: authorizing a unit lets no item go ahead that the value audit holds for a decision above the run. An action a standing approval in effect covers has that decision already, given once beforehand (ADR-D-0136).

## Why

What cannot be undone or reaches outside the work is taken on the decision of whoever holds the authority for it, which serves the product philosophy's "The line": "What cannot be undone, and what reaches outside the work, waits for the person's yes". A unit that states such an action as waiting for that decision can start on the ratification all the same, since keeping every such unit from starting until the person directing the work has read it makes every plan with a publish or a merge in it one that person must read.

## Rejected Alternatives

- An irreversible action in a unit always keeps the unit from starting until the person directing the work has read it: it makes every plan with a publish or a merge in it one that person must read; reopen if an action stated as waiting for its decision is found executed before that decision.

## Decision Boundary

Not covered: what a standing approval is, who may give one and when its entry counts (ADR-D-0136); the other conditions on which a ratified brief authorizes a plan or a goal envelope (ADR-D-0141); the grade names and their definitions, which no record states and the audit's mandate owns (ADR-D-0134 leaves them uncovered); how a question the audit holds reaches the person directing the work or the product owner (ADR-D-0062); what the Orchestrator does when the ratification does not authorize a unit, which the harness text states; merge authorization; how the unit states the action; the wording of the harness text that states this.

## Validation

The decision is broken where:

- a unit containing an irreversible or outward-facing action that no standing approval in effect covered was authorized by the ratification without stating the action as taken on the decision of whoever holds the authority for it, at its moment;
- such an action was taken before that decision, in a unit the ratification authorized or not.

## Revisit When

- An action a unit stated as waiting for its decision is found executed before that decision.

## More Information

With ADR-D-0141 and ADR-D-0142, replaces ADR-D-0065 in full; the decision carried here is the same. Carried here from it: which actions a unit must state as waiting for their moment, what it must state of them, and that the action waits in every case. It is a record of its own because the action's waiting binds whatever conditions authorize the unit that contains it. ADR-D-0136 points here for which actions wait for a decision at their moment and what a plan that contains one must state, and for what a standing approval in effect does for such an action in a unit being authorized. Source of intent: `docs/coding-agent/briefs/completed/value-level-operation-brief.md`, "Who it is for and why", "Stops during a run", "Value audit" and "Lifecycle"; the brief "A quiet Orchestrator session under a brief" (`docs/coding-agent/briefs/completed/quiet-orchestrator-session-brief.md`), "What the plugin states" and "Directed during the run". Related records: ADR-D-0136 (standing approvals), ADR-D-0139 (who authorizes non-trivial work), ADR-D-0134 (the value audit in a plan-mode run), ADR-D-0082 (the value audit in a goal run), ADR-D-0062 (no question in the Orchestrator session under a brief).
