---
status: proposed
adr_type: design
date: 2026-11-14
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "Claude Fable 5.2"]
informed: []
supersedes: []
superseded_by: null
---

# ADR-D (not yet numbered): A session that holds its role by default says so in its first reply, with how another role is opened

## Context and Problem Statement

Terms used here: a session role is a role a session itself holds. The default is the role a session holds when its opener chose none (`ADR-D-a-session-opened-with-no-role-chosen-is-counsel.md`).

Whoever opens a session is to know which conversation they are in and that another can be had, the person who knows which role they want as much as the one who has never heard of roles. A role can still be chosen (`ADR-D-any-session-role-is-the-openers-to-choose.md`), and a default is given without anyone having chosen: nothing has told the opener that a role was given, or that there are others. The fork is whether the default is held silently or said.

## Decision

- A session that holds its role by default says so in its first reply, with how another role is opened.

## Why

The default is a choice made for the opener, and the product philosophy's "The line" has a decision made for someone told to them. Said with how another role is opened, it is what lets whoever knows the mechanics lose nothing by a choice made for those who do not ("Who it is for").

## Rejected Alternatives

- The default is held without being said: it lost because someone given a role they did not want would have nothing telling them that a choice was made or how to make another; reopen if every supported runtime itself shows the opener which role a session holds and how another is opened.

## Decision Boundary

Not covered: the wording of the first reply; which role the default is, and where it reaches (`ADR-D-a-session-opened-with-no-role-chosen-is-counsel.md`); the forms the choice of another role takes, which the role map states (`ADR-D-any-session-role-is-the-openers-to-choose.md`); a session whose opener chose its role.

## Validation

The decision is broken where a session holds its role by default and its first reply does not say so, or does not say how another role is opened.

## Revisit When

- The premise that a session holding the default is brought to say so by the text it reads fails. In trials on 2026-11-19 a session opened with no role chosen said so in its first reply where the first message was a plain wish, and did not where the first message was the ratification of a brief. Sessions regularly found not saying so reopen how the saying is carried, not the decision.

## More Information

Taken out of `ADR-D-a-session-opened-with-no-role-chosen-is-counsel.md`: the default could stand without being announced, and the announcement could be retired without touching the default. It stands in place of no accepted record. Source of intent: the brief "One conversation with Counsel", "One conversation" and "Core scenarios".
