---
status: accepted
adr_type: design
date: 2026-11-14
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.2"]
informed: []
supersedes: []
superseded_by: null
---

# ADR-D-0089: A session Counsel started does not stop to ask the person directing the work for permission in its own window; input there is the backup

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session role that person talks with about what the product does or should do. A session's window is where a person would type into that session. A permission check is a runtime's own check that asks a person, or refuses, before an act is performed.

The person directing the work is to be asked only what only they can answer, and asked it where they are. A session that Counsel started has nobody at its window: the person directing the work is talking with Counsel (ADR-D-0088). A runtime's permission check that waits for input in that window therefore waits unseen, and the work stops without anything having failed. The comfortable way out is to leave the session at the prompt until that person happens to look. The fork is where a permission that person has not already given is asked for, and what is done about a check that only input in the session's own window can satisfy.

## Decision

- A session started by Counsel does not stop to ask the person directing the work for permission in its own window. It works within what that person has already allowed for the repository, and anything outside that reaches that person as a question through Counsel.
- Where a runtime's own permission check can be satisfied only by input in that session's window, that input is the backup and not the default: it carries that person's word and nothing else, the work keeps such cases as few as the runtime allows, and the closeout says plainly which remain and what that person has to do for each.

## Why

A prompt in a window nobody watches is asked of no one, and a person who must watch every started session to see whether one waits is attending the machinery; the product philosophy's "What goes wrong, in order" has the harness ask only what only the person can answer, where that person is. Some checks a runtime can satisfy in no other way than by input in the window, so that input is kept as the backup, and saying plainly which cases remain is the same section's remedy that what was not done is said outright.

## Rejected Alternatives

- A started session waits at each permission prompt until that person attaches to it: it lost because that person would have to watch every started session to know that one is waiting; reopen if every supported runtime brings a waiting prompt to that person in the conversation they are already in.
- Window input is ruled out altogether, and work that would need it is not done: it lost because some runtimes can satisfy some checks in no other way; reopen if every supported runtime lets all such checks be settled beforehand in that person's own settings.

## Decision Boundary

Not covered: what that person has allowed for a repository and where that is set, which is that person's own settings; which checks a runtime makes and which of them only window input satisfies, which changes with the runtime and its permission mode; that no check a runtime makes for safety is defeated to avoid input in a window (ADR-D-0107); how a session tells a check it can foresee from one it meets; how a question reaches that person through Counsel (ADR-D-0062); what a consent of that person's requires, which is separate from a runtime's permission and is not replaced by it; a session that person opened by their own choice, where that person is at the window.

## Validation

The decision is broken where a session Counsel started sits at a permission prompt that the person directing the work has not been told of; where window input is asked for something that person's settings could have allowed beforehand; or where a run closes and a case that still needs window input is not named with what that person has to do.

## Revisit When

- What was seen of the runtimes changes. On 2026-11-12 and 2026-11-13, in Claude Code and Codex, whether a started session stopped in its own window depended on what that person's own settings allowed. A runtime that offers a way to carry that person's grant to a started session without its window reopens how many cases the backup has to cover.
- Cases that need window input are found to be so many that the person directing the work is in effect attending the started sessions; the premise that they can be kept few then no longer holds.

## More Information

Source of intent: the brief "One conversation with Counsel", "What reaches him". Related: ADR-D-0062 (under a brief the Orchestrator session asks that person nothing; it left an act only that person can perform in the session itself uncovered), ADR-D-0105 (harness text holds no user authority).
