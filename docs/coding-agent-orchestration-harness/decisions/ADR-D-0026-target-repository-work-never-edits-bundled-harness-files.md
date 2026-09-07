---
status: proposed
adr_type: design
date: 2026-09-07
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1"]
informed: []
supersedes: ["ADR-D-0007-repo-rules-vs-harness-migration-candidates.md"]
superseded_by: null
---

# ADR-D-0026: Target-repository work stages harness improvements locally and never edits bundled harness files

## Context and Problem Statement

Agents working in a target repository find two kinds of durable lessons: operating rules for that repository, and improvements that belong to the harness every repository shares. The harness files are present in the working tree as an installed plugin, so an agent can edit them as easily as any project file, and the target repository's diff never shows the change. The fork is whether ordinary target-repository work may touch bundled harness files or must stage cross-repository improvements locally for later harness-maintenance work.

## Decision

Ordinary target-repository work never edits bundled harness skills, references, adapters, validators, or plugin files. Repository rule candidates are always repo-local and route to that repository's rule files. Cross-repository improvements are staged in the target repository as harness migration candidates (`docs/coding-agent/skill-candidates.md`, with drafts under `docs/coding-agent/skill-drafts/`) and migrate into the plugin only through explicit harness-maintenance work, or when the target repository is the harness repository and the task is to modify the plugin.

## Why

An edit to an installed harness file is invisible to the target repository's review and vanishes on the next plugin update, so it is both unreviewed and lost; staging keeps the idea where its provenance is and lets the harness change once, on purpose.

## Rejected Alternatives

- Carry harness-global proposals inside role rule files as a candidates section: rejected outright; it makes rule files carry inactive proposals beside live policy and invites agents to treat proposals as rules.
- Route harness improvements through lesson promotion targets that point at bundled files: rejected outright; it points ordinary work at direct bundled edits.
- Let agents edit bundled files under a review flag: reopen if runtimes gain a first-class, audited channel for proposing plugin updates from target-repository work.

## Decision Boundary

Invariant: outside explicit harness-maintenance work, no bundled harness file changes from a target-repository task; repository rule candidates never carry a global destination.

Not covered: the report field names and validator shapes that enforce the split, the candidates file format, and the rejected legacy field names, all of which validators and the `rulebook` and `subagent-report-contract` skills own.

## Validation

- Worker report validation rejects a global destination on a repository rule candidate and validates harness migration candidates separately.
- Package validation guards the current rule templates and rulebook references against a global-candidates section or global routing of rule candidates.

## Revisit When

- A runtime provides an audited mechanism for proposing plugin updates without editing bundled files during target-repository work (none on 2026-09-07).
- The harness gains a dedicated migration workflow that consumes the candidates file, which may change where staging lives but not the boundary.

## More Information

Replaces ADR-D-0007 in full. Rule-suite placement and freshness: ADR-D-0024, ADR-D-0025.
