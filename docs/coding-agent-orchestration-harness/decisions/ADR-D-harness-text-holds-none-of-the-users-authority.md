---
status: proposed
adr_type: design
date: 2026-11-17
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "GPT-6 Astra", "Claude Fable 5.2"]
informed: []
supersedes: ["ADR-D-0017-harness-text-holds-no-user-authority.md"]
superseded_by: null
---

# ADR-D (not yet numbered): Harness text holds none of the user's authority

## Context and Problem Statement

Terms used here: harness text is whatever the harness installs or loads into a session: a loader, an adapter, a skill. The user is the person whose conversation the session is.

A harness reaches a session only as text, and such text can say of itself that following it is the user's direction. An earlier loader said so, in order that a model would follow the harness at all (ADR-D-0008, retired on 2026-09-06). A model that weighs an instruction by who gave it then puts that text above everything that arrives below the user, an Orchestrator's instruction to a subagent included. The fork is whether harness text may claim the user's rank in order to be followed, or is weighed as what it is.

## Decision

- No harness text presents itself as the user's instruction or claims the user's authority.
- What harness text says is weighed as an instruction from below the user, and the user's own conversation outranks it.

## Why

A model that ranks the user's conversation above skill text obeys whichever text claims the higher rank, so a false claim of that rank overrides everything honestly ranked below the user, and nothing shows that it happened. The statement served is the product philosophy's "The line": what waits for the person's yes waits for the person, and text that could claim that yes for itself would leave nothing waiting.

## Rejected Alternatives

- Keep the claim and override it for each task where it does harm: it lost because the override travels through the channel the claim defeats; rejected outright.

## Decision Boundary

Not covered: what a loader or an adapter says of who installed the harness and of when it is followed, and all of its wording, which the loader's own text states; which role a session holds and how it comes to hold it (`ADR-D-a-session-holds-a-role-only-by-its-openers-choice-or-the-default.md`); how the user's decisions reach a session the user is not in (ADR-D-0038); what a runtime's own checks allow (`ADR-D-no-check-a-runtime-makes-for-safety-is-defeated.md`).

## Validation

The decision is broken where harness text states or implies that following it is the user's direction; or where a session puts an instruction from installed text or from another agent above what the user said in the conversation because that instruction claimed the user's rank.

## Revisit When

- The premise that the models the harness runs on rank the user's conversation above skill text, and follow harness text that claims no such rank, fails. It was checked on 2026-09-06 against Claude Fable 5.1 and GPT-6 Astra. A model that follows the harness only where its text claims the user's authority, a Codex model that refuses subagent dispatch without the claim for one, reopens this record.

## More Information

Replaces ADR-D-0017 in full; the decision is the same. Moved out: what the Codex loader states about who installed it and what it is followed for, which is the loader's wording and no decision of record. Related: ADR-D-0034 (Counsel holds none of the authority of the person directing the work), ADR-D-0038 (how that person's word reaches an Orchestrator session).
