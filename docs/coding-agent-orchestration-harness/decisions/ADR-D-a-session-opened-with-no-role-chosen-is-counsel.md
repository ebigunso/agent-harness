---
status: proposed
adr_type: design
date: 2026-11-14
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "Claude Fable 5.2"]
informed: []
supersedes: ["ADR-D-0037-a-session-role-is-entered-by-an-explicit-act-of-the-person-opening-it.md"]
superseded_by: null
---

# ADR-D (not yet numbered): A session opened with no role chosen is Counsel, and says so in its first reply

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session role that person talks with about what the product does or should do. The Orchestrator is the session role that plans, dispatches and reports the work.

ADR-D-0037 held that a session takes a role only by an explicit act of the person opening it. Someone who installs the harness, opens a session and types what they want has performed no such act: they may not know that there are two roles, and under that record their session held no role of the harness at all. The fork is what a session is when its opener chose nothing: nothing, the Orchestrator, or Counsel.

## Decision

- A session opened with no role chosen is Counsel, in every runtime the harness supports and for everyone who installs it.
- A session that holds the role by default says so in its first reply, with how the other role is opened.
- Where a runtime does not let an installed harness give a session a role, the default holds in each repository where the harness's setup has run. A repository where setup has not run has no default in such a runtime.
- Nothing describes a runtime, a surface or a repository the default does not reach as having it.

## Why

The product philosophy's "Who it is for" calls wrong any design that works only if the person understands a role, and has a choice between things a person cannot tell apart made for them; the person directing the work put it on 2026-11-11 as "We shouldn't assume everyone would know the difference between the two roles enough to make an informed decision", and, of a session with nothing chosen, "the harness still needs to take some kind of role or else there wouldn't be a harness there." The role is Counsel ("I think we should have Counsel as the default, and ship it for everyone", 2026-11-11) because Counsel is the one conversation from which a run can be started for that person, so someone who never chooses a role still never has to open a second session. For the runtimes where an install gives no role, a default in each repository where setup has run was put to that person beside being told what to type and beside not counting those runtimes as delivered, and accepted on 2026-11-13.

## Rejected Alternatives

- A session with nothing chosen holds no role, as ADR-D-0037 had it: it lost because the person the harness is for then meets no harness at all until they learn what a role is; reopen if the default is found to give people a role they did not want more often than it spares them the choice.
- The Orchestrator as the default: it lost because the person would then be talking at the level of plans, which ADR-D-0034 keeps away from them, and would need a second session for the conversation about what is wanted; rejected outright while Counsel is the role that starts a run.
- In a runtime where an install cannot give a role, no default, the person being told what to type instead: it lost because it asks of that person the knowledge the default exists to spare them; reopen if repository instructions are found not to be followed in such a runtime.

## Decision Boundary

Not covered: how each runtime carries the default and on which of its surfaces, and what setup writes into a repository to carry it, which the role map and the setup text state with the date each was seen; the wording of the first reply; that either role can still be chosen (`ADR-D-either-session-role-is-the-openers-to-choose.md`); what gives a session no role (`ADR-D-a-session-holds-a-role-only-by-its-openers-choice-or-the-default.md`); how a run is started from the default conversation (`ADR-D-a-ratified-briefs-run-starts-without-the-person-opening-anything.md`).

## Validation

The decision is broken where someone opens a session in a supported runtime with the default in place, chooses nothing, and is talking to a session that holds no role or the Orchestrator's; where such a session is Counsel and does not say so, or does not say how the other role is opened; or where a runtime or a repository that the default does not reach is described as having it.

## Revisit When

- The premise that the people the harness is for do not know the two roles well enough to choose between them no longer holds.
- What was seen of the default's reach changes. On 2026-11-12 the default given by the install was seen in the Claude Code terminal CLI, and by that runtime's documentation does not reach its cloud sessions. On 2026-11-13 the default carried by repository instructions was seen followed in Codex in non-interactive runs only, held by instruction text alone, and had not been tried in GitHub Copilot. A trial in which a session opened with nothing chosen does not come out as Counsel reopens how the default is carried there, and, where no way is found, the reach this record states.

## More Information

With `ADR-D-either-session-role-is-the-openers-to-choose.md` and `ADR-D-a-session-holds-a-role-only-by-its-openers-choice-or-the-default.md`, replaces ADR-D-0037 in full. Changed here: ADR-D-0037 allowed no way into a role but an explicit act, and this record gives a session with nothing chosen the Counsel role. Source of intent: the brief "One conversation with Counsel", "Who it is for and why", "One conversation" and "Directed during the run". Related: ADR-D-0034 (Counsel), ADR-D-0048 (role names and the role map).
