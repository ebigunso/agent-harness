---
status: accepted
adr_type: design
date: 2026-11-11
deciders: ["ebigunso"]
consulted: ["Claude Opus 5.5", "Claude Fable 5.2"]
informed: []
supersedes: ["superseded/ADR-D-0063-a-goal-mode-run-is-graded-over-the-whole-run-by-the-value-audit-beside-the-assessor--superseded-by-ADR-D-0082.md"]
superseded_by: null
depends_on: ["ADR-D-0080-whether-a-goal-loop-continues-is-judged-by-a-party-other-than-the-optimizer.md", "ADR-D-0081-a-goal-loop-whose-continuation-the-evidence-does-not-justify-stops-and-escalates.md", "ADR-D-0052-the-orchestrator-never-grades-its-own-run-and-its-reading-is-compared-only-after-the-grades-are-fixed.md", "ADR-D-0050-independent-judgement-of-the-orchestrators-work-is-held-by-a-role-of-its-own-the-auditor.md"]
---

# ADR-D-0083: Nothing of a value audit reaches what a goal loop's assessor reads but a stop and its question

## Context and Problem Statement

Terms used here: a goal run is a run in goal mode, in which a loop works toward a stated goal condition. The assessor is the independent judgement of whether a goal loop continues (ADR-D-0080). The value audit is the independent judgement of how a run's items stand against the value documents, the governing brief and the repository's philosophies (ADR-D-0052). A verdict is what an audit returns.

A goal run can have two independent judgements made of it: the assessor's, on whether the loop continues, and the value audit's, on whether the work fits the value documents (ADR-D-0082, and ADR-D-0065 for the envelope under a brief). The assessor judges from the run's own evidence, and continuation bears the burden of proof (ADR-D-0081). The fork is whether the two are one judgement or two, and whether what the audit finds may enter the evidence the assessor reads.

## Decision

- The value audit of a goal run and the assessor's judgement of its continuation are two judgements, never one judgement carrying both mandates.
- Nothing of an audit, neither a grade nor its support nor any other part of a verdict, enters the evidence the assessor reads. The assessor sees of an audit only that the loop stopped and the question that was put.

## Why

The two judge different things, the assessor whether the loop is still closing its gap and the audit whether the work fits the value documents. Continuation bears the burden of proof (ADR-D-0081), so a favourable grade among the assessor's inputs would argue for continuing.

## Rejected Alternatives

- A record of each value audit kept where the assessor reads it, so that their number can be checked before merge: rejected outright; it puts audit material into the assessor's evidence.
- One judgement carrying both the assessor's mandate and the audit's: rejected outright; it puts the audit's grade among the assessor's inputs, where a favourable grade would argue for continuing a loop whose continuation bears the burden of proof (ADR-D-0081).

## Decision Boundary

Not covered: which goal runs the audit grades, how much of the run, and what an item it holds does to the loop (ADR-D-0082); who the assessor is and what it reads (ADR-D-0080) and which way its uncertainty resolves (ADR-D-0081); how a remediation carried out under a brief reaches what the assessor reads (ADR-D-0067); how the audit is packaged and asked (ADR-D-0050, ADR-D-0052); where an audit's verdicts and the Orchestrator's readings are kept and what the run's journal records of a stop, which goal mode's text states.

## Validation

The decision is broken where:

- a grade, its support or any other part of a verdict stood in the evidence an assessor read;
- one judgement was asked both whether a loop continues and how the run stands against the value documents.

## Revisit When

- The premise that continuation of a goal loop bears the burden of proof, so that a favourable grade among the assessor's inputs would argue for continuing, no longer holds: the record that states it (ADR-D-0081) is retired without a replacement that keeps it.
- On 2026-11-07 no goal run under a brief had run, and on 2026-10-05 the repository that holds the harness had no philosophy, so no goal run had had both an assessor and a value audit and nothing had exercised this separation.

## More Information

Replaces ADR-D-0063 at the separation of the audit from the assessor's evidence; ADR-D-0082 replaces it at the audit's coverage of a goal run and the stop on a held item. Related: ADR-D-0080 (the assessor), ADR-D-0081 (uncertainty resolves against continuing), ADR-D-0052 (the value audit), ADR-D-0050 (the Auditor), ADR-D-0065 (the audit of a goal envelope under a brief), ADR-D-0067 (a remediation reaches the assessor only as a decision of the loop). Design: `docs/coding-agent-orchestration-harness/design/goal-mode-design.md`.
