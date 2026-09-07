---
status: proposed
adr_type: design
date: 2026-09-07
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1"]
informed: []
supersedes: ["ADR-D-0001-canonical-harness-workflow-location.md", "ADR-D-0005-runtime-prompt-budgeting.md", "ADR-I-0002-codex-bootstrap-and-loader-strategy.md"]
superseded_by: null
---

# ADR-D-0022: Workflow mechanics have one home, and every runtime surface routes to it

## Context and Problem Statement

Three runtimes (GitHub Copilot, Claude Code, Codex) consume the harness through different surfaces: agent definitions, plugin manifests, a Codex `AGENTS.md` loader block, and installed role templates. Each surface is a place where planning gates, delegation rules, validation rules, and reporting formats could be written down again, and every copy is a place where they can go stale without anyone noticing. The fork is whether those surfaces may carry workflow content of their own or only route to a shared source.

## Decision

The `orchestration-harness` skill and its references are the only home of harness workflow mechanics. Every loader block, runtime adapter, snippet, and README routes agents to that skill and does not restate its gates, rules, role names, or formats. Adapters may differ from one another in length and wording as long as their meaning comes from the shared skill tree. One replication is deliberate and bounded: the role workflow and output contracts that runtime instruction blocks carry under `runtime-adapter-contract`, maintained as one text across all runtime copies.

## Why

An agent that follows a stale copy of the workflow reports gates as satisfied that the current workflow no longer defines, and nothing in the copy tells it so.

## Rejected Alternatives

- Duplicate the workflow into every adapter: reopen if a runtime ever refuses to read shared skills from an agent definition.
- Put the workflow in `AGENTS.md`: rejected outright; a repository `AGENTS.md` reaches every platform, not only Codex, and a user one reaches every project.
- Force one identical prompt body on every runtime: reopen if a generated-adapter system can emit runtime-specific shapes from one source.

## Decision Boundary

Invariant: no surface other than the `orchestration-harness` skill tree defines a gate, rule, role name, or report format; the replicated role contract is the only exception and is kept in sync as one text.

Not covered: adapter length, kernel wording, which references an adapter names, and the loader block's exact text, all of which change through skill text and the runtime-adapter-contract checklist.

## Validation

- Package validation confirms loader snippets are loader-only and rejects harness role names or gate wording in them.
- The adapter maintenance checklist diffs the replicated role contract across the three runtime copies.
- Review of any new runtime surface asks: does this restate, or route?

## Revisit When

- A runtime gains a first-class way to declare a dependency on shared instructions without loader text (none of Copilot, Claude Code, or Codex had one on 2026-09-07).
- Agents stop loading or applying the orchestration skill from loader-only routing; the live loader check recorded under `docs/coding-agent/experiments/frontier-guard-probes/` is the evidence to consult.

## More Information

Replaces ADR-D-0001, ADR-D-0005, and the loader-only clause of ADR-I-0002 in full. Loader-routed sessions assuming the Orchestrator role: ADR-D-0020. Adapter layout: ADR-I-0006.
