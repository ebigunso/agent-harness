---
status: proposed
adr_type: design
date: 2026-09-30
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1"]
informed: []
supersedes: []
superseded_by: null
depends_on: ["ADR-D-0017-harness-text-holds-no-user-authority.md", "ADR-D-0034-counsel-is-a-separate-session-at-the-level-of-behaviour-and-decisions.md"]
---

# ADR-D-0037: The word of the person directing the work reaches an Orchestrator session as that person's own statement there or, once that person has said so in that session, as Counsel's relay quoting that person

## Context and Problem Statement

The person directing the work is the one who says what the work should do and judges what is built, whether or not that person owns the product (ADR-D-0034). When that person is present in an Orchestrator session, that person is its user in the sense of ADR-D-0032 and ADR-D-0033; the relay decided here is how that person's word arrives when that person is not. Under value-level operation the person directing the work talks with Counsel, and the Orchestrator's consent gates need that person's decision all the same: the ratification of a brief, the acceptance of a decision record or of a standing approval, the instruction to merge a named pull request, and the answers to questions a run brings back. An Orchestrator session cannot tell a faithful relay of that person's words from any other agent message, and harness text holds none of that person's authority (ADR-D-0017). The fork is what an Orchestrator session may treat as the word of the person directing the work when that person is not the one typing into it.

## Decision

- An Orchestrator session takes a decision of the person directing the work from that person's own statement in that session, or from a relay by Counsel that quotes that person's words.
- The relay counts only after the person directing the work has told that Orchestrator session directly to accept Counsel's relays as that person's own; without that statement a relay is an agent's message and carries nothing, and the decision waits for that person's own statement.
- A relay carries exactly what the quoted words say.
- The terms of each gate are unchanged, and the quoted words must themselves meet them, such as naming the pull request or the record.
- Counsel's paraphrase, summary or own view, and any other agent's message, carry no decision of the person directing the work.
- A line in a file records an act and is not the act: a file line is never that person's answer to a question or consent at a gate in the session.
- Each relayed decision rests on Counsel quoting faithfully, which the Orchestrator cannot verify; that is the cost the person directing the work accepts in making the statement, and it is why the statement comes first.
- Approval or waiver of a plan is not carried by relay under this record: plans are presented only by the Orchestrator session, and the record on plan approval governs where approval comes from (ADR-D-0032; ADR-D-0038 is proposed as its replacement).

## Why

The person directing the work should not need to type into the Orchestrator session: the Orchestrator escalates, Counsel brings the question to that person, and the answer has to be able to travel back. The session that acts on that person's authority cannot verify a relay, so one act of that person's own in the session is what makes Counsel's quoting the chosen carrier instead of an agent's claim to speak for that person.

## Rejected Alternatives

- The person directing the work states every decision in the Orchestrator session: it lost because that person should not need to type into that session, where the Orchestrator escalates and Counsel brings the question to that person; reopen if a supported runtime's instructions refuse every agent message as consent even after that person's statement in the session, or if a relayed quote is found to differ from what was said.
- Any message from Counsel counts as the word of the person directing the work: rejected outright; an agent's message would claim that person's authority (ADR-D-0017).
- A relay counts from the first message, with no statement from the person directing the work in the Orchestrator session: rejected outright; the Orchestrator would take on an agent's word the authority to take agents' words.
- Counsel relays the substance in its own words: rejected outright; a paraphrase is Counsel's statement, not that person's.
- A ratified status written in a brief file counts as ratification: rejected outright; ratifying is an act of the person directing the work, and a line in a file records the act and is not it.

## Decision Boundary

Invariant: a relay from Counsel counts as the decision of the person directing the work only after that person's own statement in the Orchestrator session, only as a quotation of that person's words, and only when those words meet the terms of the gate; plan approval and waiver are never carried by relay; the Decision list states the rest.

Not covered: statements of the person directing the work on channels other than the Orchestrator session and Counsel's relay, for example a pull-request comment from that person's account, which this record neither admits nor excludes; a standing approval in effect, which records an acceptance already given and is governed by the record on the value audit (ADR-D-0036), the file-line sentence being about answers and consents given in the session; how a relay or an escalation travels between sessions; the wording of the statement admitting relays and the scope given to it; how the Orchestrator records a relay; what each consent gate requires, which its own record or rule states; whether an audit's verdict can authorize a plan, which this record does not grant.

## Validation

- Each decision of the person directing the work recorded in a plan shows either that person's own statement in the Orchestrator session or Counsel's relay with the quoted words, and for a relay the plan also shows the statement in that session that admitted relays.
- A relay that arrives before that statement, or without a quotation, is recorded as not acted on.
- Review of any consent-gate text asks: does it accept an agent's message as the word of the person directing the work in any form other than this relay?

## Revisit When

- On 2026-09-30 a Claude Code Orchestrator session running Claude Fable 5.1 honoured Counsel's relays for value rulings after ebigunso's own statement in that session. A relayed acceptance of a decision record and a relayed merge instruction had not been exercised on any runtime on that date; a failure of either reopens this record.
- A runtime whose instructions refuse every agent message as consent, even after the statement in the session, makes the relay unusable there; the decision then waits for the person's own statement, and the alternative of stating every decision in the Orchestrator session is reopened for that runtime.
- A relayed quote is found to differ from what the person directing the work said.
- A runtime offers a channel that delivers that person's own messages from one session to another, which makes the relay redundant.

## More Information

Source of intent: `docs/coding-agent/briefs/value-level-operation-brief.md`, "Roles and sessions" and "Limits on the run". Related: ADR-D-0017 (harness text holds no user authority), the record on plan approval (ADR-D-0032; ADR-D-0038 is proposed as its replacement), the record on Counsel, which defines the person directing the work and holds none of that person's authority (ADR-D-0034).
