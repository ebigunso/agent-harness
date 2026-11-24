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

# ADR-D-0128: For anyone but the harness's maintainer, a defect of the harness that a lesson shows is met within their own repository, and nothing tells their sessions to stage a change to the harness

## Context and Problem Statement

Terms used here: a lesson is what a session records of a mistake so that the same mistake is not made twice. A target repository is the repository a session works in, with the harness installed for that work. The harness's maintainer is whoever changes the harness itself, and the harness repository is the one in which it is maintained. To stage a change is to write it up in a repository as something that waits for someone to act on it.

For someone who uses the harness and does not change what it says, a lesson has one purpose: the same mistake is not made twice. Some lessons show that the cause lies in the harness itself. For anyone but the harness's maintainer, staging such a lesson in their repository as a change proposed for the harness does not serve that purpose: nobody who works in their repository maintains the harness, so what is staged reads as though someone would act on it and nobody does. The fork is whether a defect of the harness found in the repository of anyone but the harness's maintainer is staged there for the harness, or met there.

## Decision

- For anyone but the harness's maintainer, a defect of the harness that a lesson shows is met within their own repository, by the same handling as any other lesson there.
- Nothing tells their sessions to stage a change to the harness as though someone would act on it.
- Taking a lesson into the harness itself is open only to the harness's maintainer, and is the exception.

## Why

For someone who uses the harness and does not change it, the whole purpose of a lesson is that the same mistake is not made twice, and a change staged where nobody acts on it is a pile that reads as though someone would. The product philosophy's "Who it is for" says "A design that works only if the person understands a role, a model or a step of the process is wrong", and staging works only where the person knows that what is staged has to be carried to the harness's maintainer.

## Rejected Alternatives

- For anyone but the harness's maintainer, a defect of the harness is staged in their repository, for later work on the harness: it lost because a candidate staged where nobody acts on it is a pile that reads as though someone would; reopen if what their sessions stage for the harness is shown to reach the harness's maintainer and to be acted on.
- Proposals for the harness are carried inside a target repository's rule files as a section of candidates: rejected outright; it makes rule files carry inactive proposals beside live policy and invites sessions to treat proposals as rules.

## Decision Boundary

Not covered: how a defect of the harness found in a target repository reaches the harness's maintainer; whether anything is staged in the harness repository; what meeting a defect within the repository consists of in a given case; that bundled harness files are never edited, which its own record states (ADR-D-0127); that nothing from a lesson binds before the person's yes, which its own record states (ADR-D-0129); the form of any report or file a lesson travels in.

## Validation

The decision is broken where the harness's text tells the sessions of anyone but the harness's maintainer to write up a change to the harness and leave it to wait; or where, for anyone but the harness's maintainer, a defect of the harness that a lesson shows is not met within their own repository.

## Revisit When

- The premise that what the sessions of anyone but the harness's maintainer stage for the harness reaches nobody who maintains it fails: what they stage is shown to reach the harness's maintainer and to be acted on.

## More Information

Together with ADR-D-0127, replaces ADR-D-0026 in full; this record carries the part the brief changes. Source of intent: the brief "Lessons keep their purpose", "Who it is for and why", "A lesson waits, and then leaves" and "Limits". ADR-D-0026's line that repository rule candidates never carry a global destination is held, for the sessions of anyone but the harness's maintainer, by the Decision's line that nothing tells their sessions to stage a change to the harness.
