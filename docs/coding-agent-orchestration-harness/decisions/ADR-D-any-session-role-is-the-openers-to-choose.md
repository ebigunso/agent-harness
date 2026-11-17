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

# ADR-D (not yet numbered): Whoever opens a session can choose any session role, and every supported runtime offers a way into each

## Context and Problem Statement

Terms used here: a session role is a role a session itself holds. Counsel is the session role the person directing the work talks with about what the product does or should do.

A session opened with no role chosen is Counsel (`ADR-D-a-session-opened-with-no-role-chosen-is-counsel.md`). A default can be built so that it is the only thing a person can get: a runtime adapter that offers the default role and no way into another, or a default that a choice cannot override. Runtimes may differ in what they offer for opening a session as a named agent, and a runtime may offer it on some of its surfaces and not on others. The fork is whether the default replaces the opener's choice or stands only where no choice was made.

## Decision

- Whoever opens a session can choose any session role, by what the runtime offers for the session being opened.
- Every runtime the harness supports offers a way into each session role.
- A role chosen at opening is the role the session holds; the default applies only where nothing was chosen.

## Why

A default exists for the person who cannot tell the roles apart, and the product philosophy's "Who it is for" says that whoever does know the mechanics loses nothing by a choice being made for those who do not. A default that could not be chosen against would take from the opener who knows which role they want the choice they had before it.

## Rejected Alternatives

- Only the default role can be opened by a person, any other being reached only through it: it lost because someone who knows which role they want would be made to pass through a conversation they did not ask for; rejected outright.
- One way in per runtime, chosen by whether the runtime offers agent selection: it lost because a runtime may run the main session as a named agent on some surfaces and not on others, so a per-runtime rule leaves sessions on the other surfaces with no way in; rejected outright.

## Decision Boundary

Not covered: which session roles exist (ADR-D-0048), and which form the choice takes in each runtime and on each surface, which the role map states with the date each was seen; what a session with nothing chosen is (`ADR-D-a-session-opened-with-no-role-chosen-is-counsel.md`); what gives a session no role (`ADR-D-a-session-holds-a-role-only-by-its-openers-choice-or-the-default.md`); that a session holding one role never takes another (ADR-D-0034); the model a session runs on.

## Validation

The decision is broken where a supported runtime leaves a person who wants a session role with no way to open a session in it, or where a session whose opener chose one role holds another.

## Revisit When

- A runtime adds or removes a way to open a session in a named role. On 2026-11-12 each of GitHub Copilot, Claude Code and Codex offered a way into each session role; in Codex the choice was held by the conversation alone, and nothing in the runtime fixed it.
- A supported runtime is found in which a role chosen that way is not the role the session then holds.

## More Information

With `ADR-D-a-session-opened-with-no-role-chosen-is-counsel.md` and `ADR-D-a-session-holds-a-role-only-by-its-openers-choice-or-the-default.md`, replaces ADR-D-0037 in full. Carried here: that a person enters a role by what the runtime offers for the session being opened, and the rejected per-runtime rule. Moved out: the list of the forms the act takes, which the role map states. Source of intent: the brief "One conversation with Counsel", "One conversation". Related: ADR-D-0048 (role names and the role map).
