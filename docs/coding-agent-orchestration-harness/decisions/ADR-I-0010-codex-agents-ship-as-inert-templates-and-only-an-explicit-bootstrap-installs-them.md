---
status: proposed
adr_type: implementation
date: 2026-11-24
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "Claude Opus 5.5"]
informed: []
supersedes: ["ADR-I-0006-runtime-adapters-live-outside-other-runtimes-discovery-scans.md"]
superseded_by: null
---

# ADR-I-0010: Codex agents ship as inert templates and only an explicit bootstrap installs them

## Context and Problem Statement

Codex reads custom agents only from its own agent directories after they are installed, so the harness's Codex agents reach Codex only by being installed into a Codex agent scope, and each is to register there once and in the form written for it. A duplicate or malformed registration appears at runtime in Codex, not in this repository's diff. The fork is in what form the plugin ships its Codex agents and how they come to be installed.

## Decision

Codex agents ship as inert templates that only an explicit bootstrap installs into a Codex agent scope.

## Why

Duplicate or malformed agent registrations surface only when a user opens Codex, so the way the Codex agents ship and are installed has to make them impossible rather than rely on review to notice them.

## Rejected Alternatives

- Live Codex agents inside the plugin tree, relying on Codex to ignore them until installed: rejected outright; Codex scanning behavior is not under this repository's control.
- Manual copy steps for Codex instead of a bootstrap: reopen if Codex ships plugin-installed custom agents directly.

## Decision Boundary

Not covered: the bootstrap's flags, the Codex agent scopes it installs into, and which files it copies, which change through the codex-harness-bootstrap skill; the specific directory names, which change through the runtime-adapter-contract skill; that nothing in the plugin source tree is a live Codex agent, which ADR-I-0009 states.

## Validation

The decision is broken where:

- the plugin ships a Codex agent in any form other than an inert template;
- a harness Codex agent is installed into a Codex agent scope by anything other than an explicit bootstrap.

## Revisit When

- Codex supports plugin-shipped custom agents without installation.

## More Information

With ADR-I-0008, ADR-I-0009 and ADR-I-0011, replaces ADR-I-0006 in full; the decision carried here is the same. Carried here from it: that Codex agents ship as inert templates that only an explicit bootstrap installs, with both rejected alternatives that bear on it and the revisit condition on Codex's support for plugin-shipped agents. It is a record of its own because it binds whether or not the plugin source tree may hold a live Codex agent: installation by anything other than an explicit bootstrap stays excluded either way.
