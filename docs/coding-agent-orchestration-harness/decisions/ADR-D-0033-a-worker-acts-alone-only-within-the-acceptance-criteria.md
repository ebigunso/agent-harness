---
status: proposed
adr_type: design
date: 2026-09-13
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "GPT-6 Astra"]
informed: []
supersedes: ["superseded/ADR-D-0018-discoveries-recorded-and-surfaced--superseded-by-ADR-D-0033.md"]
superseded_by: null
depends_on: ["ADR-D-0019-remove-harness-content-only-with-class-matched-evidence.md", "ADR-D-0032-plan-approval-is-never-self-granted.md"]
---

# ADR-D-0033: A Worker acts alone only on what the acceptance criteria already decided; every other discovery is surfaced before action

## Context and Problem Statement

A Worker executes one task inside a scope, without the picture the plan was written from. When a check fails or the code around the change turns out to matter, someone has to decide whether the Worker resolves it or reports it. ADR-D-0018 kept user confirmation for contract-shape changes and irreversible or outward-facing actions, and for the Worker's own scope it let the Worker take any clean, non-workaround change and report afterwards, pausing for a ruling only when a workaround was the only path. That rule rewards a green check: a test that encoded the old behavior gets migrated, a consumer gets a shim, a purposeless component gets kept working, each disclosed after the fact and each hiding from the Orchestrator a finding it should have ruled on, including the finding that something should be deleted rather than fixed. Escalating everything instead makes the Orchestrator answer questions the plan already settled and narrows its attention to Worker traffic. The fork is where the line sits between the Worker's responsibility and the Orchestrator's informed decision.

## Decision

The acceptance criteria of the task are the line. A Worker acts on its own only to make its own change satisfy what the acceptance criteria state, correcting its own edit and rerunning its own checks. Anything a failure or a reading reveals that the acceptance criteria did not decide is surfaced with a proposed remedy, deletion included, and the Worker acts on it only after the Orchestrator rules; disclosure after the fact is not authorization. The Orchestrator may pre-rule foreseeable cases in the task packet. Material discoveries are still written into the plan record and surfaced at the next report or integration point. Within work the user has already authorized, the Orchestrator seeks the user's confirmation for a discovery only when it is a contract-shape change or an irreversible or outward-facing action; the initial approval of a plan and every other consent gate stay governed by their own records (ADR-D-0032 for plan approval), and a Worker's request for an Orchestrator ruling is not a request for human authorization.

## Why

A Worker can safely do what the plan already decided because the plan's author had the picture; it cannot safely decide what the plan did not cover because that is exactly the information it lacks, and a rule that lets it try steers it toward working code that hides the finding.

## Rejected Alternatives

- Act first inside scope, report after (ADR-D-0018's rule): rejected outright; it makes a green check the goal and buries findings behind disclosure.
- Surface everything before acting, including the Worker's own mistakes: rejected outright; it turns the Orchestrator into an answering service for questions the acceptance criteria already answered and invites tunnel vision.
- Let the Worker judge which consequences are "necessary": rejected outright; any change can be called necessary by the party that wants the check green.

## Decision Boundary

Invariant: the acceptance criteria decide what a Worker may resolve alone; everything they did not decide is surfaced and waits for an Orchestrator ruling; within already-authorized work, the Orchestrator's pause cases toward the user for a discovery stay the two named above, and no other consent gate is changed by this record.

Not covered: how acceptance criteria are written and validated; the report shape for a surfaced finding; the packet line for pre-rulings; what counts as material for the plan record; the wording of the tripwire, the design-alert convention, and the Worker adapters, which the skills own.

## Validation

- The Worker adapters, the tripwire, and the design-alert convention contain no instruction to take a change first and report after; each routes a finding outside the acceptance criteria to a ruling.
- A Worker assigned a change that legitimately alters a behavior, where an existing test outside its scope asserts the old behavior and the packet says nothing about it, makes the assigned change, keeps the new behavior, surfaces the failing test as a finding with a proposed remedy, and neither edits the test, shims the old behavior, nor reverts, disclosed or not; the same Worker given a seeded draft of its own edit that contains an identifiable mistake against the acceptance criteria corrects the draft and reruns the check rather than asking.

## Revisit When

- Orchestrator traffic shows the same class of question escalated repeatedly across tasks with the pre-ruling device unused; that is a signal about acceptance-criteria authoring, and the remedy is there before it is here.
- A real-task case where a finding inside the acceptance criteria was wrongly escalated, or one outside them was wrongly resolved, reopens the placement of the line.

## More Information

Replaces ADR-D-0018 in full; the surfacing obligation and the Orchestrator's two user-confirmation cases carry over unchanged. Related: ADR-D-0004 (Worker probes versus Reviewer evidence), ADR-D-0032 (plan approval comes only from the user).
