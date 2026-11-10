---
status: proposed
adr_type: design
date: 2026-11-07
deciders: ["ebigunso"]
consulted: ["Claude Opus 5.5"]
informed: []
supersedes: ["ADR-D-0056-a-goal-mode-run-in-a-repository-with-a-philosophy-is-graded-by-the-value-audit-beside-the-assessor.md"]
superseded_by: null
depends_on: ["ADR-D-0063-a-goal-mode-run-under-a-brief-or-with-a-philosophy-is-graded-over-the-whole-run-by-the-value-audit-beside-the-assessor.md", "ADR-D-0066-a-goal-loops-forbidden-set-is-a-criterion-and-its-envelope-is-fixed-before-the-loop-and-never-changed-by-it.md"]
---

# ADR-D-0067: Under a brief a goal run carries out an already determined remedy without stopping the loop

Proposed to replace ADR-D-0056 together with ADR-D-0063 and ADR-D-0064; awaiting acceptance by the person directing the work, by name.

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. A brief is a ratified brief governing the run. The assessor is the independent judgement of whether a goal loop continues (ADR-D-0029, ADR-D-0050). The envelope is the boundary of a goal loop's autonomy, fixed before the loop starts (ADR-D-0066).

The value audit grades a goal run under a brief against the brief over the whole run, apart from the assessor, and an item it holds stops the loop (ADR-D-0063). Under a brief, a stop of the loop waits on the person directing the work, even for an item whose remedy leaves nothing to decide. The fork is whether, under a brief, such an item stops the loop or is remediated by the run, and how a remediation is kept from changing what the assessor reads.

## Decision

- Under a brief, an item the audit holds whose remedy is already determined within the run's authority, leaving no decision to make, is remediated by the run instead: the loop does not stop, the person directing the work is not reached, and what the remediation changed is graded again by the audit. Only an item that needs a decision above the run stops the loop.
- A remedy that would change the envelope is not within the run's authority (ADR-D-0066).
- A remediation reaches what the assessor reads only as a decision of the loop, without a grade or any other part of a verdict.
- The remedy carried out without a stop is limited to goal runs under a brief. Goal runs without a brief were not examined for it; in them an item the audit holds stops the loop as ADR-D-0063 states.

## Why

An item whose remedy is already determined within the run's authority leaves the person directing the work nothing to decide, so stopping the loop on it would only wait for an answer nobody has to give.

## Rejected Alternatives

- Under a brief, every held item stops the loop, remediable or not: it lost because an item whose remedy is already determined needs nothing from the person directing the work, so the stop only waits for an answer nobody has to give; reopen if remediations carried out by the run are found, when that person reads them afterwards, to have made a decision that was not already determined.
- A list of the findings the run may remedy itself: it lost because a list can admit a remedy that makes a decision, while the test whether a remedy is already determined is not outgrown by a new kind of finding; reopen if runs are found applying the test to remedies that made a decision, in a way a list would have kept out.

## Decision Boundary

Invariant: under a brief, an item the value audit holds in a goal run whose remedy is already determined within the run's authority is remediated by the run without stopping the loop or reaching the person directing the work, and what it changed is graded again; only an item that needs a decision above the run stops the loop; a remedy that would change the envelope is not within the run's authority; a remediation reaches what the assessor reads only as a decision of the loop, without any part of a verdict; a goal run without a brief is left as ADR-D-0063 states.

Not covered: how a goal run is graded against the value documents, and the stop on every other held item (ADR-D-0063); what an envelope consists of and that the loop never changes it (ADR-D-0066); how a remediation is carried out and which records it may touch, which the harness text states.

## Validation

- Review of any change to goal mode's text asks: under a brief, does the run remedy without stopping the loop only an item whose remedy is already determined within its authority, never one that would change the envelope, and is what it changed graded again; does a remediation reach what the assessor reads with a grade or any other part of a verdict; and is the remedy without a stop kept to goal runs under a brief?

## Revisit When

- On 2026-11-07 no goal run under a brief had run, so no remediation by the run had been exercised; a remediation found to have made a decision above the run reopens this record.

## More Information

Replaces ADR-D-0056 in full together with ADR-D-0063, which holds the value audit's grading of a goal run, and ADR-D-0064, which holds who authorizes the envelope. What this record changes from ADR-D-0056, which stopped the loop on every held item: under a brief an item whose remedy is already determined within the run's authority does not stop the loop. Source of intent: the brief "A quiet Orchestrator session under a brief" (`docs/coding-agent/briefs/active/quiet-orchestrator-session-brief.md`), "Directed during the run". Related: ADR-D-0063 (the value audit in a goal run), ADR-D-0066 (the envelope), ADR-D-0029 (the assessor), ADR-D-0062 (no question in the Orchestrator session under a brief), ADR-D-0064 (who authorizes non-trivial work). Design: `docs/coding-agent-orchestration-harness/design/goal-mode-design.md`.
