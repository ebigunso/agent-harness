---
status: accepted
adr_type: design
date: 2026-10-01
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1"]
informed: []
supersedes: []
superseded_by: null
depends_on: ["ADR-D-0034-counsel-is-a-separate-session-at-the-level-of-behaviour-and-decisions.md"]
---

# ADR-D-0035: Counsel reaches into the work only by quick reads of code in service of a discussion, by a read-only Researcher for bulk grounding, and by advice it consults; plans, diffs and Worker dispatch stay off limits

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. The product owner is whoever is entitled to state the product's values and to answer product-level questions for that work; when the person directing the work owns the product, both are that person. Counsel is the session the person directing the work opens for value discussion, separate from any Orchestrator session. The Orchestrator session is a session that holds the Orchestrator role (ADR-D-0020) and plans, dispatches and reports the work.

Counsel works at the level of behaviour and decisions and takes no part in how the work is done (ADR-D-0034), yet the engineering discussion is sometimes better with the code in front of it, a check-up on the project needs facts about the project's state, and the engineering discussion gains from a second model's advice. The fork is how far Counsel reaches into the work for these without becoming a reviewer or a director of it.

## Decision

- Counsel may do quick reads of code in service of a discussion with the person directing the work.
- A quick read informs the discussion and gives Counsel no part in how the work is done, no review of the work and no direction to the Orchestrator session.
- A read of code is never a check on a run's work.
- Grounding that needs bulk code reading is delegated to a read-only Researcher.
- Plans and diffs stay off limits to Counsel.
- Counsel dispatches no Worker.
- The only agent Counsel dispatches for facts about the project is a read-only Researcher.
- Counsel may ask another model for advice at the level of behaviour and decisions; that is consulting, not dispatching work.
  - The adviser is given no part of the work to do and decides nothing.
  - The advice enters the discussion marked with its source, as an input and never as the view of the person directing the work.
- Counsel gives no list of the files it read.

## Why

A discussion partner that reviews a run's work or reads its plans draws the person directing the work back into judging implementation; a quick look at code to make an engineering discussion concrete does not, and what needs more than a look comes from a Researcher reporting at the level of the discussion.

## Rejected Alternatives

- Counsel never reading code at all: rejected outright; the engineering discussion is better handled with the code in front of it, and a Researcher's summary loses the wording that matters where the code is the prose.
- Counsel reading plans and diffs: rejected outright; they are a run's work in progress, and reading them puts Counsel back into auditing the run.
- Counsel reading code as a check on a run's work: rejected outright; it would make Counsel a reviewer of the work, and a quick read serves a discussion with the person directing the work.
- Counsel doing bulk grounding in the code itself: rejected outright; bulk reading would quickly fill the Counsel session's context, so vital information not yet documented could be lost at session compaction, and code in the context would pull Counsel away from the high level of abstraction it is meant to hold.
- Counsel dispatching a Worker to act on what a discussion settled: rejected outright; Counsel would then direct how the work is done, which ADR-D-0034 forbids.
- Counsel listing the files it read in the conversation: rejected outright; the list does not serve the discussion at hand, which is about behaviour and decisions and not about where facts were found.
- Advice from another model taken as a decision, or the adviser given part of the work: rejected outright; the adviser is a consultant, and a decision is the act of the person directing the work.

## Decision Boundary

Invariant: Counsel's reach into the work is a quick read of code in service of a discussion, a read-only Researcher for what needs more, and consulted advice marked with its source; it never reads a plan or a diff, checks a run's work, or dispatches a Worker.

Not covered: where a quick read ends and bulk reading begins; how advice from another model is obtained and from which model; the shape of a Researcher's report to Counsel; Counsel's tool configuration in each runtime, which the adapters and the capability matrix own; what Counsel is and whom it serves, which ADR-D-0034 governs.

## Validation

- Counsel's adapters and policy forbid Worker dispatch, keep plans and diffs off limits, and state that a read of code serves a discussion with the person directing the work and is never a check on a run's work; a Researcher dispatched by Counsel is read-only.
- Counsel's policy states that advice from another model is brought into the discussion marked with its source and that the adviser is given no part of the work.
- Review of any change to Counsel's tools or text asks: does this let Counsel review the work, read a plan or a diff, dispatch a Worker, or give an adviser part of the work?

## Revisit When

- Counsel's reads of code turn into a check on a run's work; the premise that a quick read serves the discussion without making Counsel a reviewer then no longer holds.
- In the Counsel agent definitions for GitHub Copilot and Claude Code as written on 2026-09-30, the limits on reading (plans and diffs off limits, and no read of code as a check on a run's work) are stated rules and no tool configuration enforces them. Evidence that a Counsel session read a plan or a diff, or checked a run's work by reading code, reopens how the limits are held, not the limits.

## More Information

Builds on ADR-D-0034, which decides what Counsel is and whom it serves; this record decides only how far it reaches into the work. Source of intent: `docs/coding-agent/briefs/value-level-operation-brief.md`, "What Counsel is" and "Roles and sessions".
