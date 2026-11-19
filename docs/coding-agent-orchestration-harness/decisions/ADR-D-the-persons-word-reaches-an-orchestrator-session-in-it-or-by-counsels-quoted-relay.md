---
status: proposed
adr_type: design
date: 2026-11-14
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "Claude Fable 5.2"]
informed: []
supersedes: ["ADR-D-0038-the-word-of-the-person-directing-the-work-reaches-an-orchestrator-session-directly-or-by-quoted-relay.md"]
superseded_by: null
depends_on: ["ADR-D-0017-harness-text-holds-no-user-authority.md", "ADR-D-0034-counsel-is-a-separate-session-at-the-level-of-behaviour-and-decisions.md"]
---

# ADR-D (not yet numbered): The word of the person directing the work reaches an Orchestrator session as that person's own statement there or, once that person has admitted relays, as Counsel's relay quoting that person

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session role that person talks with about what the product does or should do. The Orchestrator session is a session that holds the Orchestrator role and plans, dispatches and reports the work. A relay is Counsel's message to an Orchestrator session that quotes that person's words. The admitting entry is the standing approval that names Counsel's identity as the carrier of that person's decisions for the repository.

Two things are wanted together. The person directing the work talks with Counsel and is not to need to type into an Orchestrator session. And nothing passes an Orchestrator session's consent gates but that person's own decision: the ratification of a brief, the acceptance of a decision record or of a standing approval, the instruction to merge, and the answers to questions a run brings back. An Orchestrator session cannot tell a faithful relay of that person's words from any other agent message, and harness text holds none of that person's authority (ADR-D-0017). Requiring every decision to be stated in the Orchestrator session serves the second and fails the first; letting whatever Counsel says count serves the first and fails the second. The fork is what an Orchestrator session may treat as the word of that person when that person is not the one typing into it.

## Decision

- An Orchestrator session takes a decision of the person directing the work from that person's own statement in that session, or from a relay by Counsel that quotes that person's words. Nothing else carries one: not Counsel's paraphrase, summary or own view, not any other agent's message, and not a line in a file, which records an act and is not the act.
- A relay counts only once that person has admitted Counsel's relays: by telling that Orchestrator session so directly, or by accepting the admitting entry, which admits them in every Orchestrator session it is in effect for. Without either, a relay is an agent's message and carries nothing, and the decision waits for that person's own statement.
- A relay carries exactly what the quoted words say. The terms of each gate are unchanged, and the quoted words must themselves meet them.
- What a relay rests on is named to that person and is what accepting the admitting entry takes on: an Orchestrator session cannot verify that Counsel quotes faithfully or who sent a message. Every relayed decision therefore rests on the word of whoever writes as Counsel.
- Approval or waiver of a plan is not carried by relay: plans are presented only by the Orchestrator session, and the record on plan approval governs where approval comes from (ADR-D-0064).

## Why

The product philosophy's "Who it is for" asks of that person what they want and their judgement of what they got, so their answer to what Counsel brings them has to be able to travel to the session that acts on it. That session cannot verify a relay, so an act of that person's own, admitting relays with what they rest on named, is what makes Counsel's quoting the chosen carrier and not an agent's claim to speak for them.

## Rejected Alternatives

- The person directing the work states every decision in the Orchestrator session: it lost because that person talks with Counsel, to whom the Orchestrator's questions go, and should not need to type into another session; reopen if a supported runtime's instructions refuse every agent message as consent even after relays are admitted, or if a relayed quote is found to differ from what was said.
- Any message from Counsel counts as the word of the person directing the work: rejected outright; an agent's message would claim that person's authority (ADR-D-0017).
- Counsel relays the substance in its own words: rejected outright; a paraphrase is Counsel's statement, not that person's.
- A ratified status written in a brief file counts as ratification: rejected outright; ratifying is an act of the person directing the work, and a line in a file records the act and is not it.

## Decision Boundary

Not covered: how that person's answer to the admitting entry itself arrives in a session Counsel started, which is the one thing a relay carries before relays are admitted (`ADR-D-the-persons-answer-to-the-entry-that-admits-relays-is-carried-by-counsel-in-a-session-counsel-started.md`); statements of the person directing the work on channels other than the Orchestrator session and Counsel's relay, which this record neither admits nor excludes; how the product owner's answer reaches the person directing the work, which precedes the relay; a standing approval in effect, which records an acceptance already given (ADR-D-0052); how a relay travels between sessions and how an Orchestrator session records one; the wording of the admitting entry, its scope and what puts it in effect; what each consent gate requires, which its own record or rule states; who starts a session and when (`ADR-D-a-ratified-briefs-run-starts-without-the-person-opening-anything.md`); a session that person opened by their own choice, where that person's own statement is available as before.

## Validation

The decision is broken where an Orchestrator session acts on something as a decision of the person directing the work that is neither that person's own statement in that session nor Counsel's relay quoting that person; where a relay is acted on with nothing having admitted it, the one answer its own record admits excepted; where quoted words that do not meet a gate's terms are taken as meeting them; where a plan is approved or its approval waived on a relay; or where that person accepted an admitting entry without having been shown what relays rest on.

## Revisit When

- A relay admitted by the entry alone, or a relayed instruction to merge, fails in a runtime. On 2026-11-11 a relayed acceptance of a pull request, admitted by the entry alone, was acted on in Claude Code; on 2026-11-14 neither had been exercised in any other runtime.
- A runtime whose instructions refuse every agent message as consent, even after relays are admitted, makes the relay unusable there; the decision then waits for that person's own statement, and the first rejected alternative is reopened for that runtime.
- A relayed quote is found to differ from what the person directing the work said, or a message is found to have been taken as Counsel's without coming from Counsel.
- A runtime offers a channel that delivers that person's own messages from one session to another, or lets a session verify who sent a message, which makes the relay redundant or removes what it rests on.

## More Information

With `ADR-D-the-persons-answer-to-the-entry-that-admits-relays-is-carried-by-counsel-in-a-session-counsel-started.md`, replaces ADR-D-0038 in full; the decision carried here is the same. Source of intent: `docs/coding-agent/briefs/completed/value-level-operation-brief.md`, "Roles and sessions" and "Limits on the run"; the brief "One conversation with Counsel", "What reaches him" and "Limits". Related: ADR-D-0017 (harness text holds no user authority), ADR-D-0034 (Counsel, which holds none of that person's authority), ADR-D-0043 (what Counsel says to an Orchestrator session), ADR-D-0062 (under a brief the Orchestrator session asks that person nothing), ADR-D-0064 (plan approval).
