---
status: accepted
adr_type: design
date: 2026-09-30
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1"]
informed: []
supersedes: []
superseded_by: null
depends_on: ["ADR-D-0017-harness-text-holds-no-user-authority.md", "ADR-D-0020-loader-routed-sessions-assume-the-orchestrator-role.md"]
---

# ADR-D-0034: Value discussion with the person directing the work is held by Counsel, a session of its own that works at the level of behaviour and decisions and takes no part in how the work is done

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. The product owner is whoever is entitled to state the product's values and to answer product-level questions for that work; when the person directing the work owns the product, both are that person. Counsel is the session the person directing the work opens for value discussion, separate from any Orchestrator session. The Orchestrator session is a session that holds the Orchestrator role (ADR-D-0020) and plans, dispatches and reports the work.

The Orchestrator session works at the level of implementation, so when it is the only session the person directing the work can talk to, the product is shaped by auditing each plan for drift. The fork is whether value discussion is a phase of the Orchestrator session or a role of its own, and, if its own, what that role is responsible for.

## Decision

- Counsel serves the person directing the work, whether or not that person is the product owner.
- That person's discussion of what the product does or should do and of how the project should look, and that person's ratification of what comes of either, are held in Counsel.
- Counsel is a session the person directing the work opens, separate from any Orchestrator session and never dispatched by another agent.
- One Counsel holds both the product and the engineering discussion, and both are at the level of behaviour and decisions.
- Counsel holds none of that person's authority: it drafts and restates, and only that person's own act ratifies anything.
- Counsel approves nothing, whether a plan, a decision record or a merge.
- The grounds for a piece of work pass from Counsel to an Orchestrator session as a brief the person directing the work ratified, in a file the Orchestrator reads itself, each statement carrying its provenance.
- Counsel gives no direction on how the work is done.
- A Counsel session never takes the Orchestrator role, and an Orchestrator session never takes Counsel's.
- The limit is the level Counsel works at, not the occasions it may be used on: nothing restricts when the person directing the work opens it.
- Anyone may talk to an Orchestrator session directly, and a value-level ruling given there is recorded as unratified.

## Why

The person directing the work judges what is built by its behaviour and shapes direction by objecting at product level instead of auditing each plan, and the session that person opens sets the altitude; delegation is kept as wide as possible, so Counsel serves whoever directs the work.

## Rejected Alternatives

- Value discussion as a phase or mode of the Orchestrator session: rejected outright; the session the person directing the work talks with then works at the level of plans, and that person is back to auditing them.
- Counsel approving plans, decision records or merges on that person's behalf: rejected outright; an agent would hold that person's authority, against ADR-D-0017.
- Counsel dispatching the Orchestrator as a subagent, so that one session is opened: rejected outright; nested subagents are not required by any runtime the harness supports, and a nested Orchestrator would put the session that holds the authority inside the one that does the work, so the Orchestrator session stays flat.
- No Counsel where the person directing the work is not the product owner, that person talking to the Orchestrator session directly instead: it lost because delegation should be as wide as possible to free the attention of the person directing the work, and talking to the Orchestrator session directly returns that person to the level of plans; reopen if Counsel, serving a person who is not the product owner, is found deciding product-level questions in the session instead of sending them to the product owner.

## Decision Boundary

Invariant: value discussion and ratification are held in Counsel, a session the person directing the work opens, separate from the Orchestrator session, holding none of that person's authority and taking no part in how the work is done; the Decision list states the rest.

Not covered: how far Counsel reaches into the work by reading code, dispatching a Researcher or consulting another model, which ADR-D-0035 governs; how the philosophy documents are handled, what a brief traces to, and what is done where no product philosophy exists, which ADR-D-0036 governs; how a Counsel conversation is conducted; the forms of the documents written with it; where an unratified ruling is recorded; what else passes between the two sessions and how it travels; the model a Counsel session runs on, which the person opening it chooses; Counsel's physical names, which the role map owns (ADR-D-0003).

## Validation

- Counsel's adapters and policy state that Counsel approves nothing, that the grounds for work pass as a ratified brief in a file, and that Counsel gives no direction on how the work is done.
- Counsel's policy states that Counsel serves the person directing the work, whether or not that person is the product owner.
- Review of any change to Counsel's tools or text asks: does this let Counsel direct how the work is done, or decide anything for the person directing the work?
- A brief acted on by an Orchestrator session is a file that Orchestrator read itself.

## Revisit When

- The person directing the work is drawn back into judging implementation while Counsel is in use; the premise that a separate session at the level of behaviour and decisions keeps that person out of it then no longer holds.

## More Information

Source of intent: `docs/coding-agent/briefs/value-level-operation-brief.md`, "Who it is for and why", "What Counsel is" and "Roles and sessions". Related: ADR-D-0003 (role identities), ADR-D-0017 (harness text holds no user authority), ADR-D-0020 (a session that loads the orchestration workflow is the Orchestrator), the record on Counsel's reach into the work (ADR-D-0035), the record on the philosophy documents (ADR-D-0036), the record on how a session role is taken (ADR-D-0037), the record on how the word of the person directing the work reaches an Orchestrator session (ADR-D-0038).
