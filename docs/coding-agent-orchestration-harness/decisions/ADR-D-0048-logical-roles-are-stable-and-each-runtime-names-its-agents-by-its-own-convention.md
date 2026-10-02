---
status: proposed
adr_type: design
date: 2026-10-03
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1"]
informed: []
supersedes: ["ADR-D-0003-runtime-namespaced-role-identities.md"]
superseded_by: null
---

# ADR-D-0048: Roles are referred to by stable logical names, each runtime gives its agents physical names by that runtime's own convention, and the role map is the canonical statement of which roles exist and which physical name holds each

## Context and Problem Statement

Plans, skills and governance documents name roles; runtimes name agents. The same role is held by differently named agents in different runtimes, and the set of roles grows over time. The fork is whether logical and physical names are one thing, and where the list of roles and the mapping between the two kinds of name is stated.

## Decision

- Plans, shared skills and governance documents refer to roles by their logical names, and those names are stable.
- Each runtime gives its agents physical names following that runtime's own convention.
- The role map (`plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/runtime-role-map.md`) is the canonical statement of which roles exist and which physical name holds each role in each runtime.
- Published physical names do not change without a migration plan.

## Why

Someone writing or reading a plan works with roles and should not have to know which runtime will run it, so the names in plans must not move when a runtime's do. Someone picking an agent in a runtime sees that runtime's list and should find the harness's agents named the way that runtime's agents are named. Which roles exist and what each runtime calls them changes more often than this rule does, so it is stated in one place that is edited when a role or a runtime is added, and this record does not have to be.

## Rejected Alternatives

- One physical name per role, the same on every runtime: it lost because runtimes differ in how agents are named and listed, so one name fits some and reads as foreign in others; reopen if every supported runtime adopts one naming scheme for plugin agents.
- The list of roles stated in this record: it lost because the record would have to be replaced each time a role is added, for no change to the rule; reopen if the role map is found to drift from the adapters with nothing catching it.
- A collision-avoidance rule in this record, namespacing new physical names wherever a clash with a platform or user agent is plausible, as ADR-D-0003 had: it lost because no such collision had been observed on Copilot, Claude Code or Codex on 2026-10-03, and a naming convention is a runtime's matter that a reviewer checks on the diff that adds an agent; reopen if a harness agent's name is found to collide with a platform or user agent.
- Renaming published agents to a common scheme: it lost because people already select the published agents by name; reopen if a release is planned that migrates them.

## Decision Boundary

Invariant: roles are referred to by stable logical names; physical names follow each runtime's convention; the role map says which roles exist and which physical name holds each; published names change only with a migration plan.

Not covered: which roles exist and what each is responsible for; each runtime's naming convention and any guidance on choosing a new name, which the role map and the adapter checklist state; how a session takes a role (ADR-D-0037); where adapter files live (ADR-I-0006); dispatch profiles of a role, which are not roles (ADR-D-0030).

## Validation

- The role map lists every role with a physical name or entry route for each runtime, and matches the adapter files.
- Plans and shared skills refer to roles by logical names.
- Review of a change that adds or renames an agent asks: is the role map updated, and does the name follow its runtime's convention?

## Revisit When

- A harness agent's name is found to collide with a platform or user agent; none had been observed on Copilot, Claude Code or Codex on 2026-10-03.
- The role map is found to drift from the adapters with nothing catching it.
- A release is planned that migrates published physical names.

## More Information

Replaces ADR-D-0003 in full. Carried: stable logical role names, runtime-specific physical names, the role map as their canonical statement, and published names kept. Dropped: the list of four roles, which the role map now owns, and the preference for namespaced new names where a collision is plausible, which is no longer a decision of record. Related: ADR-D-0037 (entering a session role), ADR-D-0030 (dispatch profiles), ADR-I-0006 (adapter layout).
