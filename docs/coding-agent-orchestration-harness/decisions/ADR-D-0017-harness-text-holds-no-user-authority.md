---
status: accepted
adr_type: design
date: 2026-09-06
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "GPT-6 Astra"]
informed: []
supersedes: ["superseded/ADR-D-0008-codex-explicit-subagent-authorization-and-async-dispatch-lifecycle--superseded-by-ADR-D-0020.md"]
superseded_by: null
---

# ADR-D-0017: Harness text holds no user authority

## Context and Problem Statement

The Codex loader block declared that using it was "explicit user direction" to follow the harness (ADR-D-0008), so that GPT-5.5, the consulted model of that record, would follow the harness at all. Claude Fable 5.1 and GPT-6 Astra rank the user's conversation above skill text, so a skill that claims user rank outranks every instruction that arrives below the user, including an Orchestrator instructing a subagent.

## Decision

Loader and adapter text never presents itself as the user's instruction. The loader states that the user installed the harness and that it is followed for coding tasks unless the user's conversation says otherwise. An instruction from below the user is weighed as such. ADR-D-0008, which carried the "explicit user direction" clause, was retired on 2026-09-06; this record replaces that clause.

## Why

A skill is not the user, and a model that knows the difference obeys whichever text claims the higher rank; the claim was false and its failure invisible.

## Rejected Alternatives

- Keep the claim and override per task: the override travels through the channel the claim defeats.

## Decision Boundary

Invariant: harness text never claims user authority.

Not covered: the loader's wording; it lives in the Codex snippet.

## Validation

The Codex loader snippet contains no authority claim.

## Revisit When

Checked on 2026-09-06 against Claude Fable 5.1 and GPT-6 Astra. Replacing either model with another reopens this record. A Codex model that refuses subagent dispatch without an authority claim reopens it. As of 2026-09-06 the reworded loader had not been verified on a real peer channel; that check is the live loader follow-up listed in PR #57, and a failure there reopens this record.
