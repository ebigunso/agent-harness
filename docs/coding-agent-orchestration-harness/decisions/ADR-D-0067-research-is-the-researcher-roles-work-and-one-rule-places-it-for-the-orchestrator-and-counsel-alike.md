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

# ADR-D-0067: Research is the Researcher role's work, never part of a Worker's task, and one rule places it for the Orchestrator and Counsel alike

Once accepted, this record and ADR-D-0066 together replace ADR-D-0061.

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session that person opens for value discussion, separate from any Orchestrator session. An option is a way a workspace has to run a role: an in-session subagent or a peer seat, each on some model.

Research can be done by whoever needs its answer: a Worker before it implements, the dispatching session itself, or a Researcher dispatched for it. A workspace may have one way to run a Researcher or several, and both the Orchestrator and Counsel send research. The fork is whether research has a role of its own wherever it arises, and whether each session places it by its own judgement or both by one rule.

## Decision

- Research is the Researcher role's work in every environment; it is never part of a Worker's task.
- The Orchestrator and Counsel place a Researcher by one and the same rule, which weighs what the research needs and how much cost may weigh in it (ADR-D-0066), and where its result is to be used.
- A workspace whose record holds no option fitting the research still has research done by a Researcher, on an option the dispatcher can always run itself; research never waits for, or goes without, a Researcher for want of a recorded option.

## Why

Research left inside a Worker's task or the dispatcher's own session runs on whatever model that work runs on, even where the workspace has an option better suited to it, and a session no shared rule reaches keeps it there whatever the other does. Made the Researcher role's work and placed by one rule for both sessions, research goes to the option that suits it in every setup; because the harness cannot know what a workspace has, an option the dispatcher can always run holds the role where no recorded option fits.

## Rejected Alternatives

- A default route to a peer researcher: it lost because no workspace using the harness is guaranteed to have that peer set up; reopen if the harness itself provides a peer setup in every supported runtime.
- An in-session Researcher subagent named as the only option: it lost because research then stays in the dispatcher's session, or goes to a Worker on another model with its task, even where the workspace records an option that suits it better; reopen if workspaces are found to have no option beyond the in-session subagent.
- Each dispatcher left to choose without a stated rule: it lost because research then lands inside Workers' tasks and in the dispatcher's own session by default, for want of a stated way to choose; rejected outright.

## Decision Boundary

Invariant: research is the Researcher role's work and never part of a Worker's task; one rule places a Researcher, for the Orchestrator and Counsel alike, by what the research needs, how much cost may weigh in it, and where its result is to be used; where no recorded option fits, a Researcher the dispatcher can always run itself holds the role.

Not covered: the rule's wording, its steps and where it is stated; how the rule weighs those things and in what order; which of the dispatcher's own options holds the role where no recorded option fits, and what is recorded then; how plan review checks a plan for research bundled into another task; when research may be skipped and what a skip records.

## Validation

- The harness texts that decide where research goes point to the one rule, and none restates a different one.
- Review of any change to research dispatch asks: does it let a Worker's task carry research, give the Orchestrator and Counsel different ways to place research, or default research to one option?

## Revisit When

- On 2026-10-29 the harness provided no peer setup of its own, so whether a workspace has peers, and on which models, depended on that workspace alone; a peer setup the harness itself provides in every supported runtime reopens the rejected default route.

## More Information

Source of intent: `docs/coding-agent/briefs/completed/choosing-where-research-goes-brief.md`, "Who it is for and why", "What the plugin states" and "Limits". Replaces ADR-D-0061 once accepted, together with ADR-D-0066, which carries how a Researcher's option is chosen and that the harness assumes no seat, peer or model. Related: ADR-D-0035 (Counsel's read-only Researcher), ADR-D-0048 (logical roles and physical names).
