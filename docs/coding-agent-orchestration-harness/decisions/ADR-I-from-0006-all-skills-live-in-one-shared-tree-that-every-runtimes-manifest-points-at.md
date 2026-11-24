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

# ADR-I-XXXX: All skills live in one shared tree that every runtime's manifest points at

## Context and Problem Statement

Each runtime the harness supports reads the harness's skills from where its manifest points. The fork is whether all skills live in one tree that every runtime's manifest points at, or skills are kept apart by runtime.

## Decision

All skills live in one shared tree that every runtime's manifest points at.

## Why

## Decision Boundary

Not covered: the tree's directory name and the manifest formats, which change through the runtime-adapter-contract skill; where each runtime's adapter files live, which the record "Each runtime's adapter files live in a path that no other runtime scans for agents" states.

## Validation

The decision is broken where:

- a skill lives outside the shared tree;
- a runtime's manifest points at a skills tree other than the shared one, or at none.

## Revisit When

## More Information

With the records "Each runtime's adapter files live in a path that no other runtime scans for agents", "Nothing in the plugin source tree is a live Codex agent" and "Codex agents ship as inert templates and only an explicit bootstrap installs them", replaces ADR-I-0006 in full; the decision carried here is the same. Carried here from it: that all skills live in one shared tree that every runtime's manifest points at. It is a record of its own because it binds wherever the adapters live and however Codex agents are installed.
