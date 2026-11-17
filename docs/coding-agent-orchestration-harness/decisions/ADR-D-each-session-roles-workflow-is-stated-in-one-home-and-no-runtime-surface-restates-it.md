---
status: proposed
adr_type: design
date: 2026-11-17
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "Claude Fable 5.2"]
informed: []
supersedes: ["ADR-D-0049-each-session-roles-workflow-mechanics-have-one-home-and-every-runtime-surface-routes-to-it.md"]
superseded_by: null
---

# ADR-D (not yet numbered): The workflow of each session role is stated in one home, and no runtime surface restates it

## Context and Problem Statement

Terms used here: a session role is a role a session itself holds. A role's workflow is its gates, its rules and its formats. A runtime surface is anything a runtime reads to bring the harness to a session: an agent definition, a manifest, a block of installed instructions, a role template. A role's home is the one place its workflow is stated.

The runtimes the harness supports may consume it through different surfaces. Each surface is a place where the workflow could be written down again, and every copy is a place where it can go stale without anyone noticing. The fork is whether a runtime surface may carry workflow of its own or only route to a shared source.

## Decision

- The workflow of each session role is stated in one home.
- A runtime surface routes to the home of the role concerned and restates no role's workflow: none of its gates, its rules or its formats.
- A surface may name a session role: identifying a role, entering one and routing to its home cannot be said without the name. Naming a role restates nothing of its workflow.
- One copy outside a home is deliberate and bounded: what a runtime's own instruction block has to carry for a role to be held to its contract there. It is kept as one text across the runtimes.

## Why

An agent that follows a stale copy of the workflow reports gates as satisfied that the workflow no longer defines, and nothing in the copy tells it so; the person relying on that report then believes a check was made that was not. The engineering philosophy's "Where it goes" has each thing written once, in the place whose pace matches its reason: a surface changes with its runtime, the workflow with the harness.

## Rejected Alternatives

- Duplicate the workflow into every adapter: it lost because each copy can go stale unnoticed; reopen if a runtime refuses to read shared skills from an agent definition.
- Put the workflow in a repository-wide loader file: rejected outright; such a file reaches every platform that reads it, and a user-level one reaches every project.
- Force one identical prompt body on every runtime: it lost because the runtimes differ in what an agent definition may contain and how it is loaded, so one body fits none of them well; reopen if adapters come to be generated from one source in each runtime's own shape.
- Name the roles and their homes in this record: it lost because a new session role or a renamed home would leave the record stale for no change to the rule; reopen if the place that names them is found to drift from the homes with nothing catching it.

## Decision Boundary

Not covered: which session roles exist, which skill is the home of each, and their names in each runtime, which the role map states (ADR-D-0048); the length and wording of an adapter, which may differ between runtimes as long as its meaning comes from the home; the text of any installed block; what a surface says of which role a session holds and how a role is chosen (`ADR-D-a-session-opened-with-no-role-chosen-is-counsel.md`, `ADR-D-any-session-role-is-the-openers-to-choose.md`, `ADR-D-a-session-holds-a-role-only-by-its-openers-choice-or-the-default.md`); which home a session reads, and where what roles share is stated (`ADR-D-a-session-takes-its-workflow-only-from-its-own-roles-home-and-what-roles-share-is-in-no-roles-home.md`); where adapters live (ADR-I-0006).

## Validation

The decision is broken where a runtime surface carries a gate, a rule or a format of a role's workflow as its own text, the bounded copy excepted; where the bounded copy differs between runtimes; or where a session acted on a surface's statement of the workflow that the role's home does not make.

## Revisit When

- A runtime gains a first-class way to declare a dependency on shared instructions without installed text. None of GitHub Copilot, Claude Code or Codex had one on 2026-09-07.
- The premise that an agent routed to its role's home loads it and applies it fails.

## More Information

With `ADR-D-a-session-takes-its-workflow-only-from-its-own-roles-home-and-what-roles-share-is-in-no-roles-home.md`, replaces ADR-D-0049 in full. Carried unchanged: that each session role's workflow has one home, that a surface routes to it and restates none of its gates, rules or formats, and the one bounded copy. Changed in one respect: ADR-D-0049 forbade a surface to carry role names, and this record lets a surface name a session role, because a default role and the choice of a role cannot be stated by text that may not name a role. The source of that behaviour is the brief "One conversation with Counsel", "One conversation". Moved out: which document names the home of each role, and the checks a review makes of a surface, which the adapter text states. The loader check behind the second revisit condition is in git history at `2a5ebf9`, under `docs/coding-agent/experiments/frontier-guard-probes/`.
