---
status: accepted
adr_type: design
date: 2026-09-06
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "GPT-6 Astra"]
informed: []
supersedes: []
superseded_by: null
---

# ADR-D-0022: Decision records carry active decisions, one each, immutable once merged, and accepted on their own

## Context and Problem Statement

On 2026-09-06 the records written for PR #57 came out as a removal ledger, a bundled record holding three decisions, and a partial supersession that left two files authoritative for one decision, and they were treated as accepted because a plan naming them had been approved. The standard in force asked for a warrant and allowed in-place amendment, and each of those shapes passed it. The fork is what a record is for: a chronicle of how a decision was reached, or a statement of what binds now.

## Decision

A decision record states one decision that binds future work, with its constraint and its why, and nothing else. It is immutable from the moment it lands on `main`; a changed decision is a new complete record and the old one is retired, never amended or partially superseded. A human accepts each record on its own, presented as title, decision, constraint, and why; plan approval and pull-request merge do not accept a record.

## Why

A record is read by someone building later who needs to know what is decided and why, and that reader is served by one complete file; history is served by git and the plan's Decision Log, and mixing the two lets ledgers pass as decisions and lets a decision hide in a plan approval.

## Rejected Alternatives

- In-place revision with a dated note: rejected because a revised record either falsifies the reasons that landed the original decision or accretes a chronicle; reopens only if retirement and replacement prove unworkable for a class of small records.
- Partial supersession: rejected outright; it forces readers to hold two files.
- Acceptance by plan approval: rejected outright; a decision that binds future work must be seen as a decision, not as one line in a plan.

## Decision Boundary

Invariant: one decision per record; immutable once merged; retire and replace; standalone acceptance.

Not covered: the admission criteria, template, and retirement mechanics, which live in `durable-docs-authoring/references/adr.md`.

## Validation

The skill reference states the four rules; the package validator rejects a live record with `supersession_scope`; every record in a pull request is listed under its own heading with its acceptance state.

## Revisit When

A record class appears for which retire-and-replace costs more than it protects, or a repository cannot present records to a human before merge.
