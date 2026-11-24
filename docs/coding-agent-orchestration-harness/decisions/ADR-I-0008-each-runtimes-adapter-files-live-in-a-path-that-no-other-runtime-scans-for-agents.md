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

# ADR-I-0008: Each runtime's adapter files live in a path that no other runtime scans for agents

## Context and Problem Statement

The runtimes the harness supports each discover agent files in a way of their own and read an agent format of their own, and each adapter written for a runtime is to be registered by that runtime once, from that file. A file that two runtimes both scan registers twice or with the wrong frontmatter, and the failure appears at runtime in one of those tools, not in this repository's diff. The fork is whether adapters share one discovery path or are isolated per runtime.

## Decision

Each runtime's adapter files live in a path that no other runtime scans for agents.

## Why

Duplicate or malformed agent registrations surface only when a user opens that runtime, so the layout has to make them impossible rather than rely on review to notice them.

## Rejected Alternatives

- One agent directory for every runtime: reopen if Copilot, Claude Code and Codex all adopt one agent format with compatible frontmatter.

## Decision Boundary

Not covered: the specific directory names and manifest formats, which change through the runtime-adapter-contract skill; whether a live Codex agent may be in the plugin source tree, and how Codex agents ship and are installed, which ADR-I-0009 and ADR-I-0010 state; where skills live, which ADR-I-0011 states.

## Validation

The decision is broken where:

- an adapter file of one runtime lies in a path that another runtime scans for agents;
- a runtime registers an agent from an adapter file written for another runtime.

## Revisit When

- Copilot is verified to discover nested agent directories in this plugin (unverified on 2026-09-07).

## More Information

With ADR-I-0009, ADR-I-0010 and ADR-I-0011, replaces ADR-I-0006 in full; the decision carried here is the same. Carried here from it: that each runtime's adapter files live outside every other runtime's discovery scan, with its reason, its rejected alternative and the revisit condition on Copilot's discovery of nested directories. It is a record of its own because it binds however Codex agents are installed and wherever skills live. Related: ADR-D-0104 (no runtime surface restates a role's workflow).
