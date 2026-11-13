---
status: proposed
adr_type: design
date: 2026-11-14
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.2"]
informed: []
supersedes: []
superseded_by: null
---

# ADR-D (not yet numbered): A session Counsel started does not stop to ask the person directing the work for permission in its own window; input there is the backup, and no safety check is defeated to avoid it

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session role that person talks with about what the product does or should do. A session's window is where a person would type into that session. A permission check is a runtime's own check that asks a person, or refuses, before an act is performed.

A session that Counsel started has nobody at its window: the person directing the work is talking with Counsel (`ADR-D-a-ratified-briefs-run-starts-without-the-person-opening-anything.md`). A runtime's permission check that waits for input in that window therefore waits unseen, and the work stops without anything having failed. The two comfortable ways out are both wrong: leaving the session at the prompt until that person happens to look, and starting it so that the runtime's checks are switched off. The fork is where a permission that person has not already given is asked for, and what is done about a check that only input in the session's own window can satisfy.

## Decision

- A session started by Counsel does not stop to ask the person directing the work for permission in its own window. It works within what that person has already allowed for the repository, and anything outside that reaches that person as a question through Counsel.
- Where a runtime's own permission check can be satisfied only by input in that session's window, that input is the backup and not the default: it carries that person's word and nothing else, the work keeps such cases as few as the runtime allows, and the closeout says plainly which remain and what that person has to do for each.
- No check a runtime makes for safety is defeated to avoid such input.

## Why

That person accepted on 2026-11-12 that a started session asks for permission through Counsel and not in its own window, adding: "Yes, but the reality may be that other sessions would require manual input or "manual-ish" input directly in it's chat box to get around automatic permission checks." The product philosophy's "What goes wrong, in order" counts that person's attention spent on what could have been settled as a failure and has the harness ask only what only the person can answer; a prompt in a window nobody watches is asked of no one, and a person who must watch every started session is attending the machinery. What a runtime checks for safety is not the harness's to allow: harness text holds none of that person's authority (ADR-D-0017), so a check is satisfied by that person or it stands. Saying plainly which cases remain is the same section's remedy, that what was not done is said outright.

## Rejected Alternatives

- A started session waits at each permission prompt until that person attaches to it: it lost because that person would have to watch every started session to know that one is waiting; reopen if every supported runtime brings a waiting prompt to that person in the conversation they are already in.
- A started session runs with the runtime's checks switched off, or retries or reroutes an act a check refused until it passes: rejected outright; the check is that person's protection, and a session that removes it has decided on its own what that person allows.
- Window input is ruled out altogether, and work that would need it is not done: it lost because some runtimes can satisfy some checks in no other way, and that person accepted the input as a backup; reopen if every supported runtime lets all such checks be settled beforehand in that person's own settings.

## Decision Boundary

Not covered: what that person has allowed for a repository and where that is set, which is that person's own settings; which checks a runtime makes and which of them only window input satisfies, which changes with the runtime and its permission mode; how a session tells a check it can foresee from one it meets; how a question reaches that person through Counsel (ADR-D-0062); what a consent of that person's requires, which is separate from a runtime's permission and is not replaced by it; a session that person opened by their own choice, where that person is at the window.

## Validation

The decision is broken where a session Counsel started sits at a permission prompt that the person directing the work has not been told of; where such a session is started or run so that a runtime's safety check does not apply, or an act a check refused is tried again by another route; where window input is asked for something that person's settings could have allowed beforehand; or where a run closes and a case that still needs window input is not named with what that person has to do.

## Revisit When

- What was seen of the runtimes changes. On 2026-11-12 a background Claude Code session under a permission mode that asks stopped at the prompt and waited, listed from outside as blocked on a permission prompt, and a non-interactive Codex run under its read-only sandbox was refused without a prompt. On 2026-11-13 a started session's writes went through unasked under the automatic permission mode, and one write that the same mode's safety check refused was left refused. Whether a started session stops in its own window thus depended on the permission mode that person's settings name. A runtime that offers a way to carry that person's grant to a started session without its window reopens how many cases the backup has to cover.
- Cases that need window input are found to be so many that the person directing the work is in effect attending the started sessions; the premise that they can be kept few then no longer holds.

## More Information

Source of intent: the brief "One conversation with Counsel", "What reaches him". Related: ADR-D-0062 (under a brief the Orchestrator session asks that person nothing; it left an act only that person can perform in the session itself uncovered), ADR-D-0017 (harness text holds no user authority).
