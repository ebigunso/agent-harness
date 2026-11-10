---
status: proposed
adr_type: design
date: 2026-10-29
deciders: ["ebigunso"]
consulted: []
informed: []
supersedes: ["ADR-D-0061-research-goes-to-the-researcher-role-on-an-option-chosen-from-the-workspaces-own-record.md"]
superseded_by: null
depends_on: ["ADR-D-0035-counsel-reaches-into-the-work-only-by-quick-reads-a-read-only-researcher-and-consulted-advice.md", "ADR-D-0048-logical-roles-are-stable-and-each-runtime-names-its-agents-by-its-own-convention.md"]
---

# ADR-D-0070: The Orchestrator and Counsel place a Researcher by one and the same rule

Once accepted, this record, ADR-D-0068 and ADR-D-0069 together replace ADR-D-0061.

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session that person opens for value discussion, separate from any Orchestrator session. An option is a way a workspace has to run a role: an in-session subagent or a peer seat, each on some model.

A workspace may have one way to run a Researcher or several, and both the Orchestrator and Counsel send research. The fork is whether each session places a Researcher by its own judgement or both by one rule.

## Decision

- The Orchestrator and Counsel place a Researcher by one and the same rule, which weighs what the research needs and how much cost may weigh in it (ADR-D-0068), and where its result is to be used.

## Why

Where each session places a Researcher by its own judgement, a session that no shared rule reaches places it its own way whatever the other does, even where the workspace has an option better suited to the research. Placed by one rule for both sessions, a Researcher goes to the option that suits the research whichever session sends it.

## Rejected Alternatives

- An in-session Researcher subagent named as the only option: it lost because research then stays in the dispatcher's session, or goes to a Worker on another model with its task, even where the workspace records an option that suits it better; reopen if workspaces are found to have no option beyond the in-session subagent.
- Each dispatcher left to choose without a stated rule: it lost because research then lands inside Workers' tasks and in the dispatcher's own session by default, for want of a stated way to choose; rejected outright.

## Decision Boundary

Invariant: one rule places a Researcher, for the Orchestrator and Counsel alike, by what the research needs, how much cost may weigh in it, and where its result is to be used.

Not covered: the rule's wording, its steps and where it is stated; how the rule weighs those things and in what order.

## Validation

- The harness texts that decide where research goes point to the one rule, and none restates a different one.
- Review of any change to research dispatch asks: does it give the Orchestrator and Counsel different ways to place research, or default research to one option?

## More Information

Source of intent: `docs/coding-agent/briefs/completed/choosing-where-research-goes-brief.md`, "Who it is for and why", "What the plugin states" and "Limits". Replaces ADR-D-0061 once accepted, together with ADR-D-0068, which carries how a Researcher's option is chosen and that the harness assumes no seat, peer or model, and ADR-D-0069, which carries that research is the Researcher role's work and never part of a Worker's task. Related: ADR-D-0035 (Counsel's read-only Researcher), ADR-D-0048 (logical roles and physical names).
