---
status: proposed
adr_type: implementation
date: 2026-09-07
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1"]
informed: []
supersedes: ["ADR-I-0001-runtime-adapter-layout.md", "ADR-I-0002-codex-bootstrap-and-loader-strategy.md"]
superseded_by: null
---

# ADR-I-0006: Each runtime's adapters live outside every other runtime's discovery scan

## Context and Problem Statement

Copilot discovers agent files under the plugin's `agents/` directory, Claude Code discovers the files its plugin manifest lists, and Codex reads custom agents only from its own agent directories after they are installed. A file that two runtimes both scan registers twice or with the wrong frontmatter, and the failure appears at runtime in one of those tools, not in this repository's diff. The fork is whether adapters share one discovery path or are isolated per runtime.

## Decision

Each runtime's adapter files live in a path that no other runtime scans for agents. Codex agents ship as inert templates that only an explicit bootstrap installs into a Codex agent scope; nothing in the plugin source tree is a live Codex agent. All skills live in one shared tree that every runtime's manifest points at.

## Why

Duplicate or malformed agent registrations surface only when a user opens that runtime, so the layout has to make them impossible rather than rely on review to notice them.

## Rejected Alternatives

- One `agents/` directory for every runtime: reopen if all three runtimes adopt one agent format with compatible frontmatter.
- Live Codex agents inside the plugin tree, relying on Codex to ignore them until installed: rejected outright; Codex scanning behavior is not under this repository's control.
- Manual copy steps for Codex instead of a bootstrap: reopen if Codex ships plugin-installed custom agents directly.

## Decision Boundary

Invariant: no adapter path is inside another runtime's discovery scan, and no live Codex agent exists in the source tree.

Not covered: the specific directory names, manifest formats, bootstrap flags, and which files the bootstrap copies; those change through the runtime-adapter-contract and codex-harness-bootstrap skills.

## Validation

- Package validation parses every plugin manifest and checks that referenced paths exist and that no Codex agent directory exists in the source tree.
- Bootstrap smoke tests install the templates into a temporary Codex home and verify the result.

## Revisit When

- Copilot is verified to discover nested agent directories in this plugin (unverified on 2026-09-07).
- Codex supports plugin-shipped custom agents without installation.

## More Information

Replaces ADR-I-0001 in full and the template clause of ADR-I-0002; ADR-I-0002's loader-only clause is carried by ADR-D-0022.
