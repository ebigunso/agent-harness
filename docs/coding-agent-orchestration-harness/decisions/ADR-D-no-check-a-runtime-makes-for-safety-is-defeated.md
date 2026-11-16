---
status: proposed
adr_type: design
date: 2026-11-17
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.2"]
informed: []
supersedes: []
superseded_by: null
---

# ADR-D (not yet numbered): No check a runtime makes for safety is defeated: the person it protects satisfies it, or it stands

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. A check a runtime makes for safety is the runtime's own check that asks a person, or refuses, before an act is performed.

The harness has sessions working with nobody watching them (`ADR-D-a-ratified-briefs-run-starts-without-the-person-opening-anything.md`), and a runtime's check that waits or refuses there stops the work without anything having failed. The comfortable way out is to start the session so that the runtime's checks are switched off, or to make a refused act again by another route. The fork is whether the harness may get past a runtime's safety check to keep the work moving.

## Decision

- No check a runtime makes for safety is defeated. No session is started or run so that such a check does not apply, and an act a check refused is not repeated or made by another route until it passes.
- A check is satisfied by the person it protects, in that person's own settings beforehand or by that person's own input, or it stands. Nothing the harness writes or relays stands in for that, and no session changes a permission setting itself.
- What a standing check holds up is told to that person.

## Why

A check a runtime makes for safety is that person's protection, and a session that removes it or works round it has decided on its own what that person allows, with none of that person's authority to do so (`ADR-D-harness-text-holds-none-of-the-users-authority.md`). The statement served is the product philosophy's "The line": what cannot be undone, and what reaches outside the work, waits for the person's yes.

## Rejected Alternatives

- A session nobody watches runs with the runtime's checks switched off, so that the work never waits: rejected outright; the check is that person's protection.
- An act a check refused is tried again, or made by another route, until it passes: rejected outright; a session that does so has decided on its own what that person allows.

## Decision Boundary

Not covered: which checks a runtime makes, and which of them only input in a session can satisfy, which changes with the runtime; what that person has allowed for a repository and where that is set; where a permission not yet given is asked for by a session Counsel started (`ADR-D-a-session-counsel-started-does-not-stop-for-permission-in-its-own-window.md`); what follows where a check refuses to let the entry that admits Counsel's relays take effect (`ADR-D-the-persons-word-reaches-an-orchestrator-session-in-it-or-by-counsels-quoted-relay.md`); the harness's own consent gates, which are separate from a runtime's permission and are not replaced by it.

## Validation

The decision is broken where a session was started or run so that a runtime's safety check did not apply; where an act a check refused was made again or by another route; where a session changed a permission setting; where a check was taken as satisfied by anything other than that person's own setting or input; or where work stood held by a check and that person had not been told.

## Revisit When

- The premise that a check a runtime makes for safety can be satisfied by the person it protects fails: a supported runtime is found whose check no setting or input of that person's satisfies, so that the work it guards cannot be done there at all.

## More Information

Taken out of `ADR-D-a-session-counsel-started-does-not-stop-for-permission-in-its-own-window.md`, where it was the third line of the Decision: it would still bind if that record were retired, so it is a decision of its own. Source of intent: the brief "One conversation with Counsel", "What reaches him" ("No check a runtime makes for safety is defeated to avoid it."). Related: ADR-D-0062 (under a brief the Orchestrator session asks that person nothing).
