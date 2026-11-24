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

# ADR-I-0009: Nothing in the plugin source tree is a live Codex agent

## Context and Problem Statement

Codex reads custom agents only from its own agent directories after they are installed, and each harness agent is to register in Codex once and in the form written for it. A Codex agent file kept live in the plugin's source tree would register or not as Codex's scanning decides, and a duplicate or malformed registration appears at runtime in Codex, not in this repository's diff. The fork is whether the plugin source tree may hold live Codex agents.

## Decision

Nothing in the plugin source tree is a live Codex agent.

## Why

Codex scanning behavior is not under this repository's control, and duplicate or malformed agent registrations surface only when a user opens Codex, so the layout has to make them impossible rather than rely on review to notice them.

## Rejected Alternatives

- Live Codex agents inside the plugin tree, relying on Codex to ignore them until installed: rejected outright; Codex scanning behavior is not under this repository's control.

## Decision Boundary

Not covered: the specific directory names, which change through the runtime-adapter-contract skill; how Codex agents ship and are installed, which ADR-I-0010 states; where other runtimes' adapter files live, which ADR-I-0008 states.

## Validation

The decision is broken where the plugin source tree holds a live Codex agent: a Codex agent directory, or any file Codex registers as an agent from the source tree.

## Revisit When

- Codex supports plugin-shipped custom agents without installation.

## More Information

With ADR-I-0008, ADR-I-0010 and ADR-I-0011, replaces ADR-I-0006 in full; the decision carried here is the same. Carried here from it: that nothing in the plugin source tree is a live Codex agent, with its rejected alternative and the revisit condition on Codex's support for plugin-shipped agents. It is a record of its own because it binds however the Codex agents come to be installed, and whatever other runtimes scan.
