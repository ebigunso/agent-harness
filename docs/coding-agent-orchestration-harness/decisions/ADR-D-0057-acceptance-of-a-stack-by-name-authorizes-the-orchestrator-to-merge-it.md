---
status: proposed
adr_type: design
date: 2026-10-07
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1"]
informed: []
supersedes: []
superseded_by: null
depends_on: ["ADR-D-0038-the-word-of-the-person-directing-the-work-reaches-an-orchestrator-session-directly-or-by-quoted-relay.md", "ADR-D-0051-work-under-a-brief-is-a-run-of-one-or-more-units-that-closes-once.md", "ADR-D-0052-the-orchestrator-never-grades-its-own-run-and-its-reading-is-compared-only-after-the-grades-are-fixed.md"]
---

# ADR-D-0057: The acceptance of a stack by name by the person directing the work, reaching the Orchestrator session as that person's own statement or as Counsel's admitted relay, authorizes the Orchestrator to merge that stack, each pull request in it; the runtime's permission to merge is that person's to grant in the session, and no rule text stands in for it

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session the person directing the work opens for value discussion, separate from any Orchestrator session. The Orchestrator session is a session that holds the Orchestrator role (ADR-D-0020) and plans, dispatches and reports the work.

A run closes once, when the acceptance of its stack by the person directing the work reaches the session (ADR-D-0051), and that record leaves merge authorization not covered. This repository's rule asked for an instruction naming each pull request. In the first use of the plugin in a fresh repository, as the feedback report brought on 2026-10-07 records it, "merge" relayed by Counsel as that person's word was blocked by the Orchestrator session's tool permission layer, and that person had to approve in that session. The fork is what authorizes the Orchestrator to merge a stack, and what part the runtime's own permission plays in it.

## Decision

- The acceptance of a stack by name by the person directing the work authorizes the Orchestrator to merge that stack, each pull request in it.
- The acceptance counts when it reaches the Orchestrator session as that person's own statement there, or as Counsel's relay quoting that person, admitted as ADR-D-0038 states.
- The runtime's own tool permission for merging is that person's to grant in that session, once, as a standing matter. No rule text stands in for it.
- A standing approval still never covers a merge except as ADR-D-0052 allows.

## Why

A stack is the unit the person directing the work judges, and the run closes on that person's acceptance of it (ADR-D-0051), so the acceptance by name is the merge decision; asking again for each pull request would return that person to steering the work piece by piece, which the run exists to end. The permission layer belongs to the runtime, not to a rule, so a rule can neither grant it nor replace it.

## Rejected Alternatives

- An instruction naming each pull request, as this repository's rule asked: it lost because it asks that person the same thing once per pull request; reopen if a stack is found merged whose pull requests that person did not mean together.
- Rule text standing in for the runtime's permission to merge: rejected outright; a rule cannot grant what the runtime gates.

## Decision Boundary

Invariant: the acceptance of a stack by name by the person directing the work, as that person's own statement in the Orchestrator session or as Counsel's relay admitted under ADR-D-0038, authorizes the merge of that stack, each pull request in it; the runtime's permission to merge is that person's to grant in the session and no rule text stands in for it; a standing approval covers a merge only as ADR-D-0052 allows.

Not covered: how the merge is performed, which the git-workflow skill states; the merge method; what happens when a pull request of the stack cannot merge; the standing approval on publishing a branch and opening pull requests, which the repository's common rule file records; the wording that names a stack; how the word of the person directing the work reaches the session (ADR-D-0038).

## Validation

- The run's closeout text and the Orchestrator's merge rule state that the acceptance of a stack by name authorizes its merge, and that the runtime's permission to merge is the person's to grant in the session; no rule text claims to grant that permission.
- A merged stack's run record shows the acceptance by name: that person's statement in the session, or Counsel's relay with the quoted words and what admitted relays.

## Revisit When

- On 2026-10-07 no stack had been merged on an acceptance by name on any runtime; a stack found merged that the person directing the work did not accept by name reopens this record.

## More Information

Source of intent: `docs/coding-agent/briefs/active/first-use-in-a-fresh-repository-brief.md`, "Merging a stack". Related: ADR-D-0038 (the word of the person directing the work, whose example of what a quoted relay must name includes the stack), ADR-D-0051 (the run closes on the acceptance of its stack), ADR-D-0052 (standing approvals and merges).
