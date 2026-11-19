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

# ADR-D (not yet numbered): In a session Counsel started, the answer of the person directing the work to the entry that admits relays is itself carried by Counsel

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session role that person talks with about what the product does or should do. The Orchestrator session is a session that holds the Orchestrator role and plans, dispatches and reports the work. A relay is Counsel's message to an Orchestrator session that quotes that person's words. The admitting entry is the standing approval that names Counsel's identity as the carrier of that person's decisions for the repository.

The person directing the work has one conversation, with Counsel, and is never to open a second session, the first time in a repository included, because the harness is for someone who does not know its roles and sessions. A relay counts in an Orchestrator session only once that person has admitted Counsel's relays, by a statement of their own in that session or by accepting the admitting entry (`ADR-D-the-persons-word-reaches-an-orchestrator-session-in-it-or-by-counsels-quoted-relay.md`). Accepting the entry is then itself an act nothing has yet admitted a relay of, so once in every repository that person had to open an Orchestrator session to give it. The fork is whether that person's answer to the admitting entry is waited for in a session that person did not open, or is carried there by Counsel before anything has admitted Counsel's relays.

## Decision

- In a session Counsel started, the answer of the person directing the work to the admitting entry itself, yes or no, may be carried by Counsel as a relay quoting that person's words, and is taken on Counsel's word that that person said it.
- Nothing else is admitted before the entry is in effect: no other decision, no answer without that person's quoted words, and nothing in a session that does not know Counsel started it.
- The relay that carries the answer rests, like every relay, on the word of whoever writes as Counsel, and that is named to that person with the entry.
- Where a runtime's own check refuses to let the entry be put in effect on a relayed word, the check stands (`ADR-D-no-check-a-runtime-makes-for-safety-is-defeated.md`): the entry is not in effect, Counsel is told, and that person's own word in that session is what remains. That word satisfies the runtime's check and is no part of what this record decides the harness should do: what is decided is that the answer travels by Counsel, and wherever a runtime does not require that person's word in the session, none is asked for.

## Why

Opening an Orchestrator session once per repository, to type an acceptance into it, is a step of the process that the product philosophy's "Who it is for" says a design must not need the person to understand, and that act verified no later relay: it protected the first step only. With the answer carried, the same unverifiable word is relied on one step earlier, which is why the risk is named to that person and the exception is limited to the one answer.

## Rejected Alternatives

- That person's answer to the admitting entry is always given in the Orchestrator session, the first time in a repository: it lost because it asks of that person once per repository the knowledge of roles and sessions the harness exists to spare them, and the statement so given verifies no later relay; reopen if a relay carrying an answer to the entry is found to have carried words that person did not say.
- In a session Counsel started, every relay counts from the first message, the admitting entry or not: rejected outright; the entry is where that person is shown what relays rest on and takes it on, and a session that acted on relays without it would have nothing of that person's to point to.
- A session that does not know Counsel started it takes the answer to the entry by relay as well: it lost because such a session may have a person in it, who can be asked there; reopen if sessions are found waiting for an answer nobody is there to give.

## Decision Boundary

Not covered: what carries a decision of that person's once relays are admitted, and what admits them (`ADR-D-the-persons-word-reaches-an-orchestrator-session-in-it-or-by-counsels-quoted-relay.md`); how a session knows that Counsel started it; the wording of the admitting entry, its scope, what puts it in effect, and what a session does with it on a declined answer; which checks a runtime makes (`ADR-D-no-check-a-runtime-makes-for-safety-is-defeated.md`, `ADR-D-a-session-counsel-started-does-not-stop-for-permission-in-its-own-window.md`); who starts a session and when (`ADR-D-a-ratified-briefs-run-starts-without-the-person-opening-anything.md`); a session that person opened by their own choice, where that person's own statement is available as before.

## Validation

The decision is broken where, before the entry is in effect, a session acts on anything relayed but that person's answer to the entry in that person's quoted words; where a session that does not know Counsel started it takes that answer by relay; where the entry is in effect although a runtime's check refused it and that person gave no word in that session; where that person is asked for a word in a session that no runtime's check required; or where, the first time in a repository, that person had to open a session in order to answer the entry.

## Revisit When

- The premise that the answer to the entry can be carried by relay in a session Counsel started fails. On 2026-11-13 it had been carried only in trials in Claude Code, with stand-ins for Counsel and for that person; no session started for a ratified brief, no relay over a peer channel and no other runtime had been tried. An answer that cannot be carried so in a supported runtime, or one acted on that this record does not admit, reopens it.
- A runtime's check is found always to refuse putting the entry in effect on a relayed word. That person's own word in the session is then the rule there and not what remains, and the first rejected alternative is what happens in fact. On 2026-11-13, in Claude Code, the check let it through once and refused it once.

## More Information

With `ADR-D-the-persons-word-reaches-an-orchestrator-session-in-it-or-by-counsels-quoted-relay.md`, replaces ADR-D-0038 in full. Changed here: ADR-D-0038 let a relay count only after an act of that person's own in the Orchestrator session or an accepted admitting entry, the acceptance being itself such an act; this record lets Counsel carry that one answer in a session it started. Source of intent: the brief "One conversation with Counsel", "What reaches him", "Directed during the run" and "Limits". Related: ADR-D-0017 (harness text holds no user authority), ADR-D-0034 (Counsel, which holds none of that person's authority), ADR-D-0062 (under a brief the Orchestrator session asks that person nothing).
