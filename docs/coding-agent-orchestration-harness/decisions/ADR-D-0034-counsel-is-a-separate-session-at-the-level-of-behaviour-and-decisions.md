---
status: proposed
adr_type: design
date: 2026-09-30
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1"]
informed: []
supersedes: []
superseded_by: null
depends_on: ["ADR-D-0017-harness-text-holds-no-user-authority.md", "ADR-D-0020-loader-routed-sessions-assume-the-orchestrator-role.md"]
---

# ADR-D-0034: Value discussion with the owner is held by Counsel, a session of its own that works at the level of behaviour and decisions and takes no part in how the work is done

## Context and Problem Statement

The owner, the person whose product the work serves, shapes the product by saying what it should do and how the project should look, and by judging what was built from its behaviour. The Orchestrator plans, dispatches and reports at the level of implementation, so when it is the only session the owner can talk to, the owner shapes the product by auditing each plan for drift. The fork is whether value discussion is a phase of the Orchestrator session or a role of its own, and, if its own, how far that role reaches into the work.

## Decision

The owner's discussion of what the product does or should do and of how the owner wants the project to look, and the owner's ratification of what comes of either, are held in a Counsel session: a session the owner opens, separate from any Orchestrator session and never dispatched by another agent. One Counsel holds both discussions, and both are at the level of behaviour and decisions. Counsel works at that level. It may do quick reads of code in service of a discussion with the owner; such a read informs the discussion and gives Counsel no part in how the work is done, no review of the work, and no direction to the Orchestrator, and it is never a check on a run's work. Grounding that needs bulk code reading is delegated to a read-only Researcher. Plans and diffs stay off limits to Counsel. Counsel dispatches no Worker, and the only agent it dispatches for facts about the project is a read-only Researcher. Counsel may ask another model for advice at the level of behaviour and decisions and bring it into the discussion marked with its source; that is consulting, not dispatching work: the adviser is given no part of the work to do and decides nothing, and what it says is an input to the discussion, never the owner's view. Counsel holds none of the owner's authority: it drafts and restates, only the owner's own act ratifies anything, and Counsel approves nothing, whether a plan, a decision record or a merge. The grounds for a piece of work pass from Counsel to an Orchestrator as a brief the owner ratified, a file the Orchestrator reads itself, and Counsel gives no direction on how the work is done. A Counsel session never takes the Orchestrator role, and an Orchestrator session never takes Counsel's. The limit is the level Counsel works at, not the occasions it may be used on: nothing restricts when the owner opens it. Where the person directing a piece of work is not the owner of the product, there is no Counsel for that work: that person talks to the Orchestrator session directly under plan mode as it stands, a value-level ruling given there is recorded as unratified, and nothing in this record stops an Orchestrator session from discussing the work with that person.

## Why

The owner judges what is built by its behaviour and shapes direction by objecting at product level instead of auditing each plan, and the session the owner opens sets the altitude. A discussion partner that reviews a run's work or reads its plans draws the owner back into judging implementation; a quick look at code to make an engineering discussion concrete does not.

## Rejected Alternatives

- Value discussion as a phase or mode of the Orchestrator session: rejected outright; the session the owner talks with then works at the level of plans, and the owner is back to auditing them.
- Counsel never reading code at all: rejected outright; the owner judged that boundary to go too far, since the engineering discussion may be better handled when Counsel can do quick reads.
- Counsel reading plans and diffs: rejected outright; the owner kept them off limits.
- Counsel reading code as a check on a run's work: rejected outright; it would make Counsel a reviewer of the work, and a quick read serves a discussion with the owner.
- Counsel doing bulk grounding in the code itself: rejected outright; the owner delegates grounding that needs bulk code reads to a Researcher.
- Counsel approving plans, decision records or merges on the owner's behalf: rejected outright; an agent would hold the owner's authority, against ADR-D-0017.
- Counsel dispatching the Orchestrator as a subagent, so that the owner opens one session: rejected outright; the owner left nested orchestration out on purpose, nested subagents are not required, and the Orchestrator session stays flat.

## Decision Boundary

Invariant: the owner's discussion of what the product does or should do and of how the owner wants the project to look, and the owner's ratification of either, are held in Counsel, a session the owner opens, separate from the Orchestrator and never dispatched by another agent; it works at the level of behaviour and decisions; it may do quick reads of code in service of a discussion with the owner, which inform the discussion and give it no part in how the work is done, no review of the work and no direction to the Orchestrator, and are never a check on a run's work; grounding that needs bulk code reading is delegated to a read-only Researcher; plans and diffs stay off limits to it; it dispatches no Worker, and the only agent it dispatches for facts about the project is a read-only Researcher; advice it asks of another model is at that level, marked with its source, given no part of the work and no decision, and never the owner's view; it holds no approval authority; the grounds for work pass from it as a brief the owner ratified, in a file, and it gives no direction on how the work is done; neither session takes the other's role; the limit is the level Counsel works at, and nothing restricts when the owner opens it.

Not covered: work directed by someone who is not the owner of the product, which has no Counsel; where a quick read ends and bulk reading begins; any account of which files Counsel read, which this record neither requires nor asks for; how a Counsel conversation is conducted; how advice from another model is obtained; the forms of the documents the owner writes with it; what else passes between the two sessions and how it travels; the model a Counsel session runs on, which the owner chooses when opening it; Counsel's physical names, which the role map owns (ADR-D-0003); its tool configuration in each runtime, which the adapters and the capability matrix own.

## Validation

- Counsel's adapters and policy forbid Worker dispatch, keep plans and diffs off limits, and state that a read of code serves a discussion with the owner and is never a check on a run's work; a Researcher dispatched by Counsel is read-only.
- Review of any change to Counsel's tools or text asks: does this let Counsel review or direct how the work is done, read a plan or a diff, or decide anything for the owner?
- A brief acted on by an Orchestrator is a file that Orchestrator read itself.

## Revisit When

- Use on real initiatives, the first being Character Memory, shows Counsel's reads of code turning into a check on a run's work, or the owner being drawn back into judging implementation.
- In the Counsel agent definitions for GitHub Copilot and Claude Code as written on 2026-09-30, the limits on reading (plans and diffs off limits, and no read of code as a check on a run's work) are stated rules and no tool configuration enforces them. Evidence that a Counsel session read a plan or a diff, or checked a run's work by reading code, reopens how the limits are held, not the limits.

## More Information

Source of intent: `docs/coding-agent/briefs/value-level-operation-brief.md`. Related: ADR-D-0003 (role identities), ADR-D-0017 (harness text holds no user authority), ADR-D-0020 (a session that loads the orchestration workflow is the Orchestrator), the record on how a session role is taken (ADR-D-0035), the record on how the owner's word reaches an Orchestrator session (ADR-D-0037).
