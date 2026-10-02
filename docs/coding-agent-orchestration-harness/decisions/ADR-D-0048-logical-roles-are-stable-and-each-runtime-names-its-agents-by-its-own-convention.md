---
status: proposed
adr_type: design
date: 2026-10-03
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1"]
informed: []
supersedes: ["ADR-D-0003-runtime-namespaced-role-identities.md"]
superseded_by: null
depends_on: ["ADR-D-0034-counsel-is-a-separate-session-at-the-level-of-behaviour-and-decisions.md"]
---

# ADR-D-0048: The harness has five stable logical roles, and each runtime names the agents that hold them by its own convention: namespaced where a generic name could collide, bare role names where the runtime's agents already use them

## Context and Problem Statement

Plans, skills and governance documents name roles; runtimes name agents. The harness has five logical roles: Orchestrator, Researcher, Worker and Reviewer, and Counsel, the session role for value discussion (ADR-D-0034). A runtime may ship built-in agents with generic names such as `worker`, so a physical name chosen carelessly can collide. The GitHub Copilot agents have been published under bare role names (`Orchestrator`, `Researcher`, `Reviewer`, `Worker`) since before namespacing was preferred. The fork is whether logical and physical names are one thing, and what rule a new physical name follows.

## Decision

- The logical roles are stable and are five: Orchestrator, Researcher, Worker, Reviewer and Counsel.
- Plans, shared skills and governance documents use logical role names, never a runtime's physical agent names.
- Physical agent names may differ by runtime, and the role map (`plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/runtime-role-map.md`) is the one place that states them.
- A new physical name is namespaced where a collision with a platform-provided or user agent is plausible; a generic name such as `worker` is not relied on in such a runtime.
- A runtime whose published agents already use bare role names keeps that convention for a new role, so that its agents read as one set: in Copilot the Counsel agent is `Counsel`, beside `Orchestrator`, `Researcher`, `Reviewer` and `Worker`.
- Published physical names are not changed without a migration plan.

## Why

Someone writing or reading a plan works with roles and should not have to know which runtime will run it; someone picking an agent in a runtime sees a list of names and should find the harness's agents as one recognisable set there. Namespacing protects that person from picking a platform agent that happens to share a generic name; where a runtime's set is already published under bare role names, a single namespaced newcomer would make the set harder to recognise, not safer.

## Rejected Alternatives

- One generic physical name per role on every runtime: it lost because a runtime's own `worker` or a user's agent can shadow it; reopen if every supported runtime gives plugin agents a namespace of their own.
- Rename every published agent to a namespaced name: it lost because people already select the Copilot agents by their published names; reopen if a release is planned that migrates them.
- Namespace every new physical name with no exception, as ADR-D-0003 preferred: it lost because the Copilot Counsel agent would be the one namespaced name in a set of bare ones; reopen if a bare role name in Copilot is found to collide with a platform or user agent.
- Four logical roles, Counsel treated as outside the role model: rejected outright; Counsel is a role a session holds, with a policy and adapters like the others (ADR-D-0034).

## Decision Boundary

Invariant: five logical roles, named the same in every plan and skill; physical names stated only in the role map; a new name is namespaced where a collision is plausible, and follows a runtime's published bare-name convention where one exists; the Decision list states the rest.

Not covered: what each role is responsible for (ADR-D-0034 for Counsel; the orchestration skill for the others); how a session takes a role (ADR-D-0037); where adapter files live (ADR-I-0006); dispatch profiles of a role, which are not roles (ADR-D-0030); the physical names themselves, which the role map owns.

## Validation

- The role map lists five logical roles and a physical name or entry route for each runtime, and matches the adapter files.
- Plans and shared skills use logical role names.
- Review of a new physical name asks: could this name collide in its runtime, and does the runtime's published set use bare role names?

## Revisit When

- A runtime gives plugin agents a namespace or a role binding independent of file names.
- A bare role name in Copilot is found to collide with a platform or user agent.
- A release is planned that migrates published physical names.

## More Information

Replaces ADR-D-0003 in full: its stable logical roles, runtime-specific physical names and role map are carried; Counsel is added as the fifth role, and the preference for namespaced new names gains the exception for a runtime whose published agents use bare role names. Related: ADR-D-0034 (Counsel), ADR-D-0037 (entering a session role), ADR-D-0030 (dispatch profiles), ADR-I-0006 (adapter layout).
