---
status: proposed
adr_type: design
date: 2026-09-07
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1"]
informed: []
supersedes: ["ADR-D-0006-repository-rule-suite-bootstrap-lifecycle.md"]
superseded_by: null
---

# ADR-D-0024: Rule-suite lifecycle metadata lives in a sidecar read only for lifecycle work

## Context and Problem Statement

A repository's rule suite under `docs/coding-agent/rules/` is read on most non-trivial tasks, and its index is read most often of all. The same suite also needs machine-oriented lifecycle data (required files, bootstrap context, refresh groups, source evidence, source-to-section mappings) for repair, schema migration, targeted refresh, and contradiction handling. The fork is whether that data rides in the files agents read every task or in a file they open only when doing lifecycle work.

## Decision

Lifecycle metadata lives in a sidecar (`_lifecycle.json`) that agents read only for bootstrap, repair, schema migration, targeted refresh, source-drift diagnosis, or contradiction handling. The index stays a low-token routing file and bootstrap success marker, written last so an interrupted bootstrap leaves no installed suite. Role rule files carry operating policy only.

## Why

Every byte in the index is paid on every task that reads it, while lifecycle data is needed on a few; putting the two together taxes the common path to serve the rare one, and the tax grows silently as the metadata grows.

## Rejected Alternatives

- Keep all lifecycle metadata in the index: reopen if runtimes gain a way to load rule files lazily by section so index size stops costing context.
- Keep only skeleton rule files and rediscover repository truth each task: rejected outright; it removes the durable operating contract the suite exists to provide.

## Decision Boundary

Invariant: no lifecycle data (source snapshots, fingerprints, refresh groups, mappings) in the index or the role rule files; the index is written last.

Not covered: the sidecar's schema, the set of role files, write order beyond "index last", and read triggers, which live in the `rulebook` skill.

## Validation

- Package validation checks that the index template stays compact and points at the sidecar.
- Rulebook bootstrap writes the index last; smoke tests verify the write order.

## Revisit When

- Runtimes gain portable lifecycle hooks that maintain rule freshness without prompt-token cost (none of Copilot, Claude Code, or Codex had them on 2026-09-07).
- Rule files become loadable by section on demand.

## More Information

Replaces ADR-D-0006 together with ADR-D-0025; the file list, write order, read triggers, and refresh triggers ADR-D-0006 enumerated are `rulebook` skill text. Freshness derivation: ADR-D-0025. Validators enforce contracts, not prose: ADR-I-0003.
