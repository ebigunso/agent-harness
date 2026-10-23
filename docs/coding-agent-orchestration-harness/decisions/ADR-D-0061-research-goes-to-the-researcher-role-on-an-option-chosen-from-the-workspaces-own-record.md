---
status: accepted
adr_type: design
date: 2026-10-22
deciders: ["ebigunso"]
consulted: []
informed: []
supersedes: []
superseded_by: null
depends_on: ["ADR-D-0035-counsel-reaches-into-the-work-only-by-quick-reads-a-read-only-researcher-and-consulted-advice.md", "ADR-D-0048-logical-roles-are-stable-and-each-runtime-names-its-agents-by-its-own-convention.md"]
---

# ADR-D-0061: Research goes to the Researcher role, never into a Worker's task, on the option the workspace's own record shows suits it, chosen by one rule for the Orchestrator and Counsel alike; the harness assumes no seat, peer or model

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session that person opens for value discussion, separate from any Orchestrator session. An option for research is a way a workspace has to run a Researcher: an in-session subagent, or a peer seat, each on some model.

A workspace may have one way to do research or several, in-session subagents, peer seats on other models, or both, and the harness runs in workspaces whose setups differ. The fork is whether the harness names where research goes, leaves it to each dispatcher, or states how a dispatcher chooses among the options the workspace itself records.

## Decision

- Research is the Researcher role's work in every environment; it is never part of a Worker's task.
- The Orchestrator and Counsel choose where a Researcher runs by one rule, from one record of options kept by the workspace.
- The choice is by the strength the research needs, then by what the person directing the work has said of quality against cost for that kind of work and by where the result should live.
- Where nothing recorded has the strength, the dispatcher's own model runs the Researcher as a subagent, and the observation is recorded with its date.
- The harness assumes no seat, peer or model; what a workspace has is read only from its own record.

## Why

The harness runs where it cannot know the setup, so naming a seat or defaulting to a peer breaks wherever that setup is absent, while naming only a subagent keeps research in the dispatcher's session or sends it to a Worker with its task when the workspace has a better option; a rule that reads the workspace's own record serves every setup with the same text.

## Rejected Alternatives

- A default route to a peer researcher: it lost because no workspace using the harness is guaranteed to have that peer set up; reopen if the harness itself provides a peer setup in every supported runtime.
- An in-session Researcher subagent named as the only option: it lost because research then stays in the dispatcher's session, or goes to a Worker on another model with its task, even where the workspace records an option that suits it better; reopen if workspaces are found to have no option beyond the in-session subagent.
- Each dispatcher left to choose without a stated rule: it lost because research then lands inside Workers' tasks and in the dispatcher's own session by default, for want of a stated way to choose; rejected outright.

## Decision Boundary

Invariant: research is the Researcher role's work and never part of a Worker's task; one rule chooses where a Researcher runs, for the Orchestrator and Counsel alike, from the workspace's own record of options; the harness assumes no seat, peer or model, and falls back to the dispatcher's own model as a subagent where nothing recorded has the strength.

Not covered: the rule's wording and where it is stated; the strengths routed on and which research wants which; where the record of options is kept and its form; which options and models a workspace has, and what its person directing the work has said of quality against cost; how plan review checks a plan for research bundled into another task; when research may be skipped.

## Validation

- The harness texts that decide where research goes point to the one rule, and none restates a different one.
- No harness text names a seat, a peer or a model as something a workspace has.
- Review of any change to research dispatch asks: does this name an option the workspace has not recorded, default research to one option, or let a Worker's task carry research?

## Revisit When

- On 2026-10-22 the harness provided no peer setup of its own, so whether a workspace has peers, and on which models, depended on that workspace alone; a peer setup the harness itself provides in every supported runtime reopens the rejected default route.
- On 2026-10-22 no run had yet chosen research by this rule; a dispatcher found reaching a worse option than its workspace's record shows, with the rule followed, reopens how the choice is stated, not the decision.

## More Information

Source of intent: `docs/coding-agent/briefs/completed/choosing-where-research-goes-brief.md`, "What the plugin states" and "Limits". Related: ADR-D-0035 (Counsel's read-only Researcher), ADR-D-0048 (logical roles and physical names).
