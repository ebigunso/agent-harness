---
status: accepted
adr_type: design
date: 2026-11-17
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "Claude Fable 5.2"]
informed: []
supersedes: ["superseded/ADR-D-0035-counsel-reaches-into-the-work-only-by-quick-reads-a-read-only-researcher-and-consulted-advice--superseded-by-ADR-D-0098.md"]
superseded_by: null
depends_on: ["ADR-D-0034-counsel-is-a-separate-session-at-the-level-of-behaviour-and-decisions.md"]
---

# ADR-D-0099: Counsel reads a project's code only to serve a discussion, and takes no part in doing or checking a run's work

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session role that person talks with about what the product does or should do. A run is the work done under one ratified brief.

The person directing the work is to judge the work from its behaviour and never from how it was made, so the session that person talks with works at the level of behaviour and decisions and takes no part in how the work is done (ADR-D-0034). Yet an engineering discussion is sometimes better with the code in front of it, a check-up on the project needs facts about its state, and Counsel is in contact with the runs it starts. Each of these is a way for the session that person talks with to slide into reviewing the work or directing it. The fork is how far Counsel reaches into the work without becoming a reviewer or a director of it.

## Decision

- Counsel reads a project's code only in service of a discussion with the person directing the work. A read gives Counsel no part in how the work is done and is never a check on a run's work.
- A run's plans and diffs are off limits to Counsel.
- Counsel dispatches no Worker. A model Counsel asks for advice is consulted: it is given no part of the work and decides nothing.
- What a discussion needs beyond a quick look at the code reaches Counsel as a report at the level of the discussion, from a role that only reads.

## Why

A discussion partner that reviews a run's work or reads its plans draws the person directing the work back into judging implementation; a quick look at code to make a discussion concrete does not, and what needs more than a look comes as a report at the level of the discussion. The statement served is the product philosophy's "Who it is for": what that person wants and whether what they got is it are the only two things asked of them.

## Rejected Alternatives

- Counsel never reads code at all: rejected outright; the engineering discussion is better held with the code in front of it, and a summary loses the wording that matters where the code is the prose.
- Counsel reads plans and diffs: rejected outright; they are a run's work in progress, and reading them puts Counsel back into auditing the run.
- Counsel reads code as a check on a run's work: rejected outright; it would make Counsel a reviewer of the work.
- Counsel does bulk reading of the code itself: rejected outright; it fills the session that person talks with, so that what was said and not yet written down can be lost, and it pulls Counsel away from the level it is meant to hold.
- Counsel dispatches a Worker to act on what a discussion settled: rejected outright; Counsel would then direct how the work is done, which ADR-D-0034 forbids.
- Advice from another model is taken as a decision, or the adviser is given part of the work: rejected outright; the adviser is a consultant, and a decision is the act of the person directing the work.

## Decision Boundary

Not covered: where a quick look ends and bulk reading begins; which role reports to Counsel, on which option, and the shape of its report (ADR-D-0069, ADR-D-0070); whether Counsel says which files it read, and how advice is marked with its source, which Counsel's text states; how each runtime configures Counsel's tools; when Counsel may take a view from another model and when it has to (ADR-D-0098, ADR-D-0101); that Counsel starts the run of a ratified brief and learns where it stands, which give it no part in the run's work (ADR-D-0088, ADR-D-0093); what Counsel says to an Orchestrator session (ADR-D-0100, ADR-D-0097, ADR-D-0102); what Counsel is and whom it serves (ADR-D-0034).

## Validation

The decision is broken where Counsel has read a run's plan or diff; where Counsel judged a run's work from its own read of code; where Counsel dispatched a Worker or gave an adviser part of the work; or where an adviser's word was taken as a decision.

## Revisit When

- The premise that a quick read serves a discussion without making Counsel a reviewer fails: Counsel's reads of code are found to have turned into a check on a run's work.
- On 2026-09-30 the limits on what Counsel reads were held by stated rules, and no tool configuration enforced them in GitHub Copilot or Claude Code. A Counsel session found to have read a plan or a diff, or to have checked a run's work by reading code, reopens how the limits are held, not the limits.

## More Information

With ADR-D-0098 and ADR-D-0101, replaces ADR-D-0035 in full; the decision carried here is the same. Changed in how it is stated: ADR-D-0035 named the only ways Counsel reaches into the work, and this record names what Counsel never does there, so that a contact with a run that is no part of its work does not contradict it. Moved out: that Counsel gives no list of the files it read, and that advice enters a discussion marked with its source, which Counsel's text states. Source of intent: `docs/coding-agent/briefs/completed/value-level-operation-brief.md`, "What Counsel is" and "Roles and sessions".
