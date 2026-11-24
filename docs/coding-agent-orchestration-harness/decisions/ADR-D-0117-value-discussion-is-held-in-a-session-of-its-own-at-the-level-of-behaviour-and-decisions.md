---
status: proposed
adr_type: design
date: 2026-11-24
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "Claude Fable 5.2"]
informed: []
supersedes: ["ADR-D-0034-counsel-is-a-separate-session-at-the-level-of-behaviour-and-decisions.md"]
superseded_by: null
depends_on: ["ADR-D-0090-a-session-holds-a-role-only-by-its-openers-choice-or-the-default.md"]
---

# ADR-D-0117: Value discussion is held in a session of its own, at the level of behaviour and decisions

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. The product owner is whoever is entitled to state the product's values and to answer product-level questions for that work; when the person directing the work owns the product, both are that person. Value discussion is that person's discussion of what the product does or should do and of how the project should look. Counsel is the session role that holds it. The Orchestrator session is a session that holds the Orchestrator role (ADR-D-0090) and plans, dispatches and reports the work. A brief is the document that states what one piece of work is to give and why.

The person directing the work is to judge what is built by its behaviour, and to shape its direction by saying what is wanted, without reading how it is made. A session that plans and dispatches the work speaks of plans and code. Where it is the only session that person can talk with, what they want is settled in those terms, and they keep the direction only by auditing each plan for drift. The fork is whether value discussion is a phase of the session that does the work or is held in a session of its own, and, if its own, at what level that session works and what passes from it to the work.

## Decision

- Value discussion, and the ratification by the person directing the work of what comes of it, are held in Counsel: a session that person opens, separate from any Orchestrator session and never dispatched by another agent.
- Counsel holds the discussion of the product and the discussion of how the project should look alike, and holds both at the level of behaviour and decisions. It takes no part in how the work is done.
- The limit on Counsel is the level it works at, never the occasions it may be used on: nothing restricts when that person opens it.
- Counsel serves the person directing the work, whether or not that person is the product owner.
- A session that holds the Counsel role never takes the Orchestrator role, and a session that holds the Orchestrator role never takes Counsel's.
- The grounds for a piece of work pass from Counsel to an Orchestrator session as a brief the person directing the work ratified. The Orchestrator session takes them from the brief itself and never from an account of it, and each statement in the brief carries where it came from.
- Anyone may talk to an Orchestrator session directly. A ruling on what the product does or should do, or on how the project should look, that is given there is recorded as unratified.

## Why

A person recognises what is wrong in an experience, and what it should be instead, more readily than in a mechanism, so a session that speaks of what someone does, experiences and gains puts the judgement where that person's intuition works, and one that speaks of plans and code asks them to translate before judging. The statement served is the product philosophy's "What goes wrong, in order": what is meant is established in terms the person can judge. The session that person talks with sets the level of the talk, which is why the discussion has a session of its own that never becomes the one doing the work; and delegation is kept as wide as possible, so Counsel serves whoever directs the work.

## Rejected Alternatives

- Value discussion as a phase or mode of the Orchestrator session: rejected outright; the session the person directing the work talks with then works at the level of plans, and that person is back to auditing them.
- Counsel dispatching the Orchestrator as a subagent, so that a single session is opened: rejected outright; no runtime the harness supports requires nested subagents, and a nested Orchestrator would put the session that holds the authority inside the one that does the work, so the Orchestrator session stays flat.
- No Counsel where the person directing the work is not the product owner, that person talking to the Orchestrator session directly instead: it lost because delegation should be as wide as possible to free the attention of the person directing the work, and talking to the Orchestrator session directly returns that person to the level of plans; reopen if Counsel, serving a person who is not the product owner, is found deciding product-level questions in the session instead of sending them to the product owner.

## Decision Boundary

Not covered: that Counsel holds none of that person's authority and approves nothing (ADR-D-0118); how far Counsel reaches into the work by reading code, having research done or consulting another model (ADR-D-0098, ADR-D-0099, ADR-D-0101); what Counsel says to an Orchestrator session, its stop of part of the work included (ADR-D-0097, ADR-D-0100, ADR-D-0102, ADR-D-0121), and where its advice goes (ADR-D-0103); who states a product's values and what is done where no product philosophy exists (ADR-D-0119, ADR-D-0120); how a session comes to hold a role, and what a session is when no role was chosen (ADR-D-0090, ADR-D-0091, ADR-D-0095); how the run of a ratified brief starts and when the brief is handed over (ADR-D-0088, ADR-D-0115); how that person's word reaches an Orchestrator session (ADR-D-0112) and what authorizes work (ADR-D-0064); how a Counsel conversation is conducted (ADR-D-0124, ADR-D-0125); the forms of the documents written with Counsel, the form in which a brief is kept and in which its statements carry where they came from, and where an unratified ruling is recorded, all of which the harness text states; how many Counsel sessions a repository has at once; the model a Counsel session runs on; Counsel's physical names, which the role map owns (ADR-D-0048).

## Validation

The decision is broken where:

- what the person directing the work wants was settled with them in a session that plans or dispatches the work, as a part of that session's work;
- a session passed from the Counsel role to the Orchestrator role or from the Orchestrator role to Counsel's, or Counsel ran as another agent's subagent;
- Counsel put its discussion to that person in terms of plans or code, or took part in how the work was done;
- Counsel was closed to that person because of the occasion, or because that person is not the product owner;
- an Orchestrator session worked from an account of a brief and not from the brief, or from a brief that person had not ratified, or a statement in a brief did not show where it came from;
- a ruling on what the product does or how the project should look, given in an Orchestrator session, was treated as ratified.

## Revisit When

- The person directing the work is drawn back into judging implementation while Counsel is in use; the premise that a separate session at the level of behaviour and decisions keeps that person out of it then no longer holds.

## More Information

With ADR-D-0118, replaces ADR-D-0034 in full; the decision carried here is the same. Carried here from it: where value discussion and ratification are held, the level Counsel works at and that it takes no part in how the work is done, whom Counsel serves, that neither session takes the other's role, the ratified brief as the grounds for work, and the unratified ruling. ADR-D-0102 and ADR-D-0099 hold the particular forms of taking no part in how the work is done: what Counsel tells an Orchestrator session, and that it neither does nor checks a run's work. Moved out: that a brief is a file, which the harness text states. Source of intent: `docs/coding-agent/briefs/completed/value-level-operation-brief.md`, "Who it is for and why", "What Counsel is" and "Roles and sessions". Related: ADR-D-0092 (each session role works from its own home), ADR-D-0105 (harness text holds no user authority).
