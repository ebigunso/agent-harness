---
status: proposed
adr_type: design
date: 2026-11-24
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "Claude Fable 5.2"]
informed: []
supersedes: ["ADR-D-0042-every-extension-is-recorded-and-the-audit-marks-which-bear-on-direction-for-closeout.md"]
superseded_by: null
depends_on: ["ADR-D-0134-the-orchestrator-never-grades-its-own-run-against-the-value-documents.md", "ADR-D-0065-a-ratified-brief-authorizes-a-plan-or-a-goal-envelope-only-on-a-closed-review-and-a-value-audit-that-holds-nothing.md"]
---

# ADR-D-0132: Every extension the value audit lets through and every judgement call a run makes without the person directing the work is kept in the run's records, where that person can read it

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. The value audit is the independent grading of a run's plan and result against the value documents (ADR-D-0134). An extension is an item that no value document states and that the audit lets through as a cheap-to-undo extension of statements it names (ADR-D-0065). A judgement call is a choice a run makes without the person directing the work: a choice made in the course of the work and reported, or a ruling of the Orchestrator's.

A run starts and goes on without the person directing the work reading its plan, extensions included (ADR-D-0065), and it makes judgement calls of its own as it goes. All of these are decisions made below the level at which that person was consulted, and that person has to be able to see them afterwards. Only those the value audit marks are brought to that person, and the audit marks a judgement call from the run's records (ADR-D-0133). The fork is whether all of what a run decides without that person is written down and kept, or only the part brought to them.

## Decision

- Every item the value audit lets through as an extension is recorded in the run's records, with the statements the audit's verdict named as the ones it extends.
- Every judgement call a run makes without the person directing the work is kept in the run's records in full, whoever in the run made it.
- What is so recorded stays in the run's records, whether or not it is shown to that person, where that person can read it.

## Why

What a run decides without the person directing the work is decided for that person, and the product philosophy's "The line" has "a decision made for someone and never mentioned has left them unable to correct it". Only part of it is brought to that person; the rest is written down all the same, so nothing is lost, only not pushed.

## Decision Boundary

Not covered: which of these are shown to the person directing the work, who marks them and when they are shown (ADR-D-0133); what an extension is and when it lets a plan start (ADR-D-0065); the run record a run keeps beside its units and what that one document holds (ADR-D-0051); where in the run's records the extensions and the judgement calls are written, and in what form.

## Validation

The decision is broken where:

- an extension the audit let through is absent from the run's records, or is there without the statements the verdict named for it;
- a judgement call a run made without the person directing the work is absent from the run's records, or is kept there in part;
- something so recorded was taken out of the run's records, an item not shown to that person included;
- the records that hold these are kept where that person cannot read them.

## Revisit When

- The premise that what is written down in a run's records is not lost to the person directing the work no longer holds: something kept there is found to be something that person could not read when they looked for it.

## More Information

With ADR-D-0133, replaces ADR-D-0042 in full. ADR-D-0042 named the judgement calls as the choices Workers reported and the rulings the Orchestrator made; this record names them by what they are, choices a run makes without the person directing the work. Source of intent: `docs/coding-agent/briefs/completed/value-level-operation-brief.md`, "Stops during a run" and "Lifecycle". Related: ADR-D-0134 (the value audit), ADR-D-0065 (extensions as a condition of authorization), ADR-D-0051 (the run).
