---
status: proposed
adr_type: design
date: 2026-11-24
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.2"]
informed: []
supersedes: ["ADR-D-0026-target-repository-work-never-edits-bundled-harness-files.md"]
superseded_by: null
---

# ADR-D-0127: Ordinary work in a target repository never edits bundled harness files

## Context and Problem Statement

Terms used here: a target repository is the repository a session works in, with the harness installed for that work. Bundled harness files are the harness as it is installed there: its skills, references, adapters, validators and other plugin files. The harness repository is the one in which the harness is maintained.

A change to the harness is to be reviewed and to last. Bundled harness files are present in a target repository's working tree, so a session can edit them as easily as any file of the project, and the target repository's diff never shows the change. The fork is whether ordinary work in a target repository may edit bundled harness files.

## Decision

- Ordinary work in a target repository never edits bundled harness files.
- The harness changes only through explicit harness-maintenance work, or when the target repository is the harness repository and the task is to modify the plugin.

## Why

An edit to a bundled harness file is invisible to the target repository's review and vanishes on the next update of the plugin, so it is both unreviewed and lost.

## Rejected Alternatives

- Sessions edit bundled harness files under a review flag: it lost because an edit under a flag is still an edit to a bundled harness file, which is invisible to the target repository's review and vanishes on the next update of the plugin; reopen if runtimes gain a first-class, audited channel for proposing plugin updates from target-repository work.
- A lesson's remedy names a bundled harness file as the place it goes: rejected outright; it points ordinary work at direct edits of bundled files.

## Decision Boundary

Not covered: what a session does about a defect of the harness that its work shows, which its own record states (ADR-D-0128); which files are bundled under each runtime; by what checks an edit is caught.

## Validation

The decision is broken where a bundled harness file differs from what was installed because of ordinary work in a target repository.

## Revisit When

- A runtime provides an audited mechanism for proposing plugin updates without editing bundled harness files during target-repository work. ADR-D-0026 records that there was none on 2026-09-07.

## More Information

Together with ADR-D-0128, replaces ADR-D-0026 in full; this record carries the part of ADR-D-0026 that stands unchanged. Source of intent: ADR-D-0026, and the brief "Lessons keep their purpose", "A lesson waits, and then leaves", which changes the other part.
