---
status: proposed
adr_type: design
date: 2026-10-29
deciders: ["ebigunso"]
consulted: []
informed: []
supersedes: ["ADR-D-0061-research-goes-to-the-researcher-role-on-an-option-chosen-from-the-workspaces-own-record.md"]
superseded_by: null
depends_on: ["ADR-D-0048-logical-roles-are-stable-and-each-runtime-names-its-agents-by-its-own-convention.md"]
---

# ADR-D-0068: Research is the Researcher role's work in every environment and never part of a Worker's task

Once accepted, this record, ADR-D-0067 and ADR-D-0069 together replace ADR-D-0061.

## Context and Problem Statement

Terms used here: an option is a way a workspace has to run a role: an in-session subagent or a peer seat, each on some model.

Research can be done by whoever needs its answer: a Worker before it implements, the dispatching session itself, or a Researcher dispatched for it. A workspace may have one way to run a Researcher or several, or none recorded that fits the research. The fork is whether research has a role of its own wherever it arises.

## Decision

- Research is the Researcher role's work in every environment; it is never part of a Worker's task.
- A workspace whose record holds no option fitting the research still has research done by a Researcher, on an option the dispatcher can always run itself; research never waits for, or goes without, a Researcher for want of a recorded option.

## Why

Research left inside a Worker's task or the dispatcher's own session runs on whatever model that work runs on, even where the workspace has an option better suited to it; made the Researcher role's work, it can go to the option that suits it in every setup. Because the harness cannot know what a workspace has, an option the dispatcher can always run holds the role where no recorded option fits.

## Rejected Alternatives

- A default route to a peer researcher: it lost because no workspace using the harness is guaranteed to have that peer set up; reopen if the harness itself provides a peer setup in every supported runtime.

## Decision Boundary

Invariant: research is the Researcher role's work in every environment and never part of a Worker's task; where no recorded option fits, a Researcher the dispatcher can always run itself holds the role.

Not covered: which of the dispatcher's own options holds the role where no recorded option fits, and what is recorded then; how plan review checks a plan for research bundled into another task; when research may be skipped and what a skip records.

## Validation

- Review of any change to research dispatch asks: does it let a Worker's task carry research?

## Revisit When

- On 2026-10-29 the harness provided no peer setup of its own, so whether a workspace has peers, and on which models, depended on that workspace alone; a peer setup the harness itself provides in every supported runtime reopens the rejected default route.

## More Information

Source of intent: `docs/coding-agent/briefs/completed/choosing-where-research-goes-brief.md`, "Who it is for and why", "What the plugin states" and "Limits". Replaces ADR-D-0061 once accepted, together with ADR-D-0067, which carries how a Researcher's option is chosen and that the harness assumes no seat, peer or model, and ADR-D-0069, which carries the one rule by which the Orchestrator and Counsel place a Researcher. Related: ADR-D-0048 (logical roles and physical names).
