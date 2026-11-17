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

# ADR-D (not yet numbered): The word of the person directing the work reaches an Orchestrator session as that person's own statement there or as Counsel's relay quoting that person; in a session Counsel started, that person's answer to the entry that admits relays is itself carried by Counsel

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session role that person talks with about what the product does or should do. The Orchestrator session is a session that holds the Orchestrator role and plans, dispatches and reports the work. A relay is Counsel's message to an Orchestrator session that quotes that person's words. The admitting entry is the standing approval in a repository's rule files that names Counsel's identity as the carrier of that person's decisions for the repository.

The person directing the work talks with Counsel, and an Orchestrator session's consent gates need that person's decision all the same: the ratification of a brief, the acceptance of a decision record or of a standing approval, the instruction to merge, and the answers to questions a run brings back. An Orchestrator session cannot tell a faithful relay of that person's words from any other agent message, and harness text holds none of that person's authority (ADR-D-0017). ADR-D-0038, accepted on 2026-10-01, therefore let a relay count only after an act of that person's own: a statement in that Orchestrator session, or an accepted admitting entry. The acceptance of that entry was itself such an act, so the first time in a repository that person opened an Orchestrator session to give it. The brief "One conversation with Counsel" has that person never open a second session, the first time in a repository included. The fork is whether that person's answer to the admitting entry is waited for in a session that person did not open, or is carried there by Counsel before anything has admitted Counsel's relays.

## Decision

- An Orchestrator session takes a decision of the person directing the work from that person's own statement in that session, or from a relay by Counsel that quotes that person's words. Nothing else carries one: not Counsel's paraphrase, summary or own view, not any other agent's message, and not a line in a file, which records an act and is not the act.
- A relay counts only once that person has admitted Counsel's relays: by telling that Orchestrator session so directly, or by accepting the admitting entry, which admits them in every Orchestrator session it is in effect for. Without either, a relay is an agent's message and carries nothing, and the decision waits for that person's own statement, with the one exception that follows.
- In a session Counsel started, that person's answer to the admitting entry itself, yes or no, may be carried by Counsel as a relay quoting that person's words, and is taken on Counsel's word that that person said it. Nothing else is admitted before the entry is in effect: no other decision, no answer without that person's quoted words, and nothing in a session that does not know Counsel started it.
- A relay carries exactly what the quoted words say. The terms of each gate are unchanged, and the quoted words must themselves meet them.
- What a relay rests on is named to that person and is what accepting the admitting entry takes on: an Orchestrator session cannot verify that Counsel quotes faithfully or who sent a message. Every relayed decision therefore rests on the word of whoever writes as Counsel, the relay that carries the answer to the entry included.
- Approval or waiver of a plan is not carried by relay: plans are presented only by the Orchestrator session, and the record on plan approval governs where approval comes from (ADR-D-0064).
- Where a runtime's own check refuses to let the entry be put in effect on a relayed word, the check stands (`ADR-D-no-check-a-runtime-makes-for-safety-is-defeated.md`): the entry is not in effect, Counsel is told, and that person's own word in that session is what remains. That word satisfies the runtime's check and is no part of what this record decides the harness should do: what is decided is that the answer travels by Counsel, and wherever a runtime does not require that person's word in the session, none is asked for.

## Why

Opening an Orchestrator session once per repository, to type an acceptance into it, is a step of the process that the product philosophy's "Who it is for" says a design must not need the person to understand, and that act verified no later relay: it protected the first step only. With the answer carried, the same unverifiable word is relied on one step earlier, which is why the risk is named to that person and the exception is limited to the one answer.

## Rejected Alternatives

- The person directing the work states every decision in the Orchestrator session: it lost because that person talks with Counsel, to whom the Orchestrator's questions go, and should not need to type into another session; reopen if a supported runtime's instructions refuse every agent message as consent even after relays are admitted, or if a relayed quote is found to differ from what was said.
- That person's answer to the admitting entry is always given in the Orchestrator session, the first time in a repository: it lost because it asks of that person once per repository the knowledge of roles and sessions the harness exists to spare them, and the statement so given verifies no later relay; reopen if a relay carrying an answer to the entry is found to have carried words that person did not say.
- Any message from Counsel counts as the word of the person directing the work: rejected outright; an agent's message would claim that person's authority (ADR-D-0017).
- In a session Counsel started, every relay counts from the first message, the admitting entry or not: rejected outright; the entry is where that person is shown what relays rest on and takes it on, and a session that acted on relays without it would have nothing of that person's to point to.
- A session that does not know Counsel started it takes the answer to the entry by relay as well: it lost because such a session may have a person in it, who can be asked there; reopen if sessions are found waiting for an answer nobody is there to give.
- Counsel relays the substance in its own words: rejected outright; a paraphrase is Counsel's statement, not that person's.
- A ratified status written in a brief file counts as ratification: rejected outright; ratifying is an act of the person directing the work, and a line in a file records the act and is not it.

## Decision Boundary

Not covered: statements of the person directing the work on channels other than the Orchestrator session and Counsel's relay, which this record neither admits nor excludes; how the product owner's answer reaches the person directing the work, which precedes the relay; a standing approval in effect, which records an acceptance already given (ADR-D-0052); how a relay travels between sessions, how a session knows that Counsel started it, and how an Orchestrator session records a relay; the wording of the admitting entry, its scope, what puts it in effect, and what a session does with it on a declined answer; which checks a runtime makes (`ADR-D-no-check-a-runtime-makes-for-safety-is-defeated.md`, `ADR-D-a-session-counsel-started-does-not-stop-for-permission-in-its-own-window.md`); what each consent gate requires, which its own record or rule states; who starts a session and when (`ADR-D-a-ratified-briefs-run-starts-without-the-person-opening-anything.md`); a session that person opened by their own choice, where that person's own statement is available as before.

## Validation

The decision is broken where an Orchestrator session acts on something as a decision of the person directing the work that is neither that person's own statement in that session nor Counsel's relay quoting that person; where a relay is acted on with nothing having admitted it, the answer to the admitting entry in a session Counsel started excepted; where, before the entry is in effect, a session acts on anything relayed but that answer in that person's quoted words; where quoted words that do not meet a gate's terms are taken as meeting them; where a plan is approved or its approval waived on a relay; where that person accepted an admitting entry without having been shown what relays rest on; where the entry is in effect although a runtime's check refused it and that person gave no word in that session; where that person is asked for a word in a session that no runtime's check required; or where, the first time in a repository, that person had to open a session in order to answer the entry.

## Revisit When

- The premise that the answer to the entry can be carried by relay in a session Counsel started fails. On 2026-11-13 it had been carried only in trials in Claude Code, with stand-ins for Counsel and for that person; no session started for a ratified brief, no relay over a peer channel and no other runtime had been tried. An answer that cannot be carried so in a supported runtime, or one acted on that this record does not admit, reopens it.
- A runtime's check is found always to refuse putting the entry in effect on a relayed word. That person's own word in the session is then the rule there and not what remains, and the second rejected alternative is what happens in fact. On 2026-11-13, in Claude Code, the check let it through once and refused it once.
- A relay admitted by the entry alone, or a relayed instruction to merge, fails in a runtime. On 2026-11-11 a relayed acceptance of a pull request, admitted by the entry alone, was acted on in Claude Code; on 2026-11-14 neither had been exercised in any other runtime.
- A runtime whose instructions refuse every agent message as consent, even after relays are admitted, makes the relay unusable there; the decision then waits for that person's own statement, and the first rejected alternative is reopened for that runtime.
- A relayed quote is found to differ from what the person directing the work said, or a message is found to have been taken as Counsel's without coming from Counsel.
- A runtime offers a channel that delivers that person's own messages from one session to another, or lets a session verify who sent a message, which makes the relay redundant or removes what it rests on.

## More Information

ADR-D-0033 says "the user" for the person present in the Orchestrator session; this record says the person directing the work. Source of intent: `docs/coding-agent/briefs/completed/value-level-operation-brief.md`, "Roles and sessions" and "Limits on the run"; the brief "One conversation with Counsel", "What reaches him", "Directed during the run" and "Limits". Related: ADR-D-0017 (harness text holds no user authority), ADR-D-0034 (Counsel, which holds none of that person's authority), ADR-D-0043 (what Counsel says to an Orchestrator session), ADR-D-0062 (under a brief the Orchestrator session asks that person nothing), ADR-D-0064 (plan approval).
