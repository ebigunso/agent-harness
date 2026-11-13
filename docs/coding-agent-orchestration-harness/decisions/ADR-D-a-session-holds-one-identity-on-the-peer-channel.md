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

# ADR-D (not yet numbered): A session holds one identity on the peer channel, given when it is created and not changed after, and reads another session's messages without taking that session's identity

## Context and Problem Statement

Terms used here: a peer channel is a means by which sessions send each other messages under names. An identity is the name a session sends and receives under there.

Sessions on a peer channel are told apart only by their names, and other decisions rest on those names: a standing approval admits relays from Counsel by naming Counsel's identity (ADR-D-0038). A channel may let a session join under a further name, and the easy way for a session to see what another was sent is to join as that other. On 2026-11-11 the person directing the work described a session that "had many roles held". The fork is whether a name on the channel belongs to one session for its life, or is something a session takes up when it needs what the name gives access to.

## Decision

- A session holds one identity on the peer channel, given when it is created and not changed after.
- Reading what another session was sent never requires holding that session's identity.

## Why

A session that joins under another's name in order to read its messages then sends under a name that is not its own, and whoever receives the message cannot tell. Every decision that trusts a message by its sender's name, the admission of Counsel's relays among them, is only as sound as the rule that a name is held by one session.

## Rejected Alternatives

- A session takes whatever identities it needs, one for each seat or role whose messages it reads: it lost because its messages then carry names that say nothing about who sent them, and a reader of the channel's history cannot reconstruct who did what; rejected outright.
- A session may change its identity when its work changes: it lost because what was sent under the earlier name is then attributed to whoever holds that name next; reopen if a supported peer channel is found to record the session behind each message apart from the name.

## Decision Boundary

Not covered: which peer channel a workspace has, if any, and how an identity is given there, which the workspace's record states; the names themselves and their convention; how a session reads what another was sent, which depends on the channel; that a message's sender cannot be verified, the risk a standing approval that names an identity takes on (ADR-D-0038); whether two sessions may share a seat; a workspace with no peer channel, where nothing here applies.

## Validation

The decision is broken where one session has sent or received under two names on a peer channel; where a session's name there changed during its life; or where a session had to join as another in order to read what that other was sent.

## Revisit When

- A supported peer channel records the session behind each message apart from the name it was sent under, so that a name no longer carries who sent it.
- A peer channel in use is found to give a session no way to read what another was sent except under that other's name. Whether every peer channel a supported workspace may use offers such a read had not been checked on 2026-11-14.

## More Information

Source of intent: the brief "One conversation with Counsel", "Seats". Related: ADR-D-0038 (relays admitted by Counsel's identity), ADR-D-0068 (the harness assumes no seat or peer; what a workspace has is in its own record).
