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

# ADR-D-0037: The owner's word reaches an Orchestrator session as the owner's own statement there or, once the owner has said so in that session, as Counsel's relay quoting the owner

## Context and Problem Statement

The owner is the person whose product the work serves. When the owner is present in an Orchestrator session, the owner is its user in the sense of ADR-D-0032 and ADR-D-0033; the relay decided here is how the owner's word arrives when the owner is not. Under value-level operation the owner talks with Counsel, and the Orchestrator's consent gates need the owner's decision all the same: the ratification of a brief, the acceptance of a decision record or of a standing approval, the instruction to merge a named pull request, and the answers to questions a run brings to the owner. An Orchestrator session cannot tell a faithful relay of the owner's words from any other agent message, and harness text holds none of the owner's authority (ADR-D-0017). The fork is what an Orchestrator session may treat as the owner's word when the owner is not the one typing into it.

## Decision

An Orchestrator session takes the owner's decision from the owner's own statement in that session, or from a relay by Counsel that quotes the owner's words. The relay counts only after the owner has told that Orchestrator session directly to accept Counsel's relays as the owner's; without that statement a relay is an agent's message and carries nothing, and the decision waits for the owner's own statement. A relay carries exactly what the quoted words say. The terms of each gate are unchanged, and the quoted words must themselves meet them, such as naming the pull request or the record. Counsel's paraphrase, summary or own view, and any other agent's message, carry no decision of the owner's. A line in a file records an act of the owner and is not the act: a file line is never the owner's answer to a question or the owner's consent at a gate in the session. Each relayed decision rests on Counsel quoting the owner faithfully, which the Orchestrator cannot verify; that is the cost the owner accepts in making the statement, and it is why the statement comes first. Approval or waiver of a plan is not carried by relay under this record: plans are presented only by the Orchestrator session, and the record on plan approval (ADR-D-0032) governs where approval comes from.

## Why

The owner should not need to type into the Orchestrator session: the Orchestrator escalates, Counsel brings the question to the owner, and the answer has to be able to travel back. The session that acts on the owner's authority cannot verify a relay, so one act of the owner's own in that session is what makes Counsel's quoting the owner's chosen carrier instead of an agent's claim to speak for the owner.

## Rejected Alternatives

- The owner states every decision in the Orchestrator session: it lost because the owner should not need to type into that session, where the Orchestrator escalates and Counsel brings the question to the owner; reopen if a supported runtime's instructions refuse every agent message as consent even after the owner's statement in the session, or if a relayed quote is found to differ from what the owner said.
- Any message from Counsel counts as the owner's: rejected outright; an agent's message would claim the owner's authority (ADR-D-0017).
- A relay counts from the first message, with no statement from the owner in the Orchestrator session: rejected outright; the Orchestrator would take on an agent's word the authority to take agents' words.
- Counsel relays the substance in its own words: rejected outright; a paraphrase is Counsel's statement, not the owner's.
- A ratified status written in a brief file counts as ratification: rejected outright; ratifying is an act of the owner, and a line in a file records the act and is not it.

## Decision Boundary

Invariant: a relay from Counsel counts as the owner's decision only after the owner's own statement in that Orchestrator session, only as a quotation of the owner's words, and only when those words meet the terms of the gate; a line in a file is never the owner's answer or consent in the session, and an agent's unquoted account never stands for the owner; plan approval and waiver are not carried by relay under this record.

Not covered: the owner's statements on channels other than the Orchestrator session and Counsel's relay, for example a pull-request comment from the owner's account, which this record neither admits nor excludes; a standing approval in effect, which records an acceptance the owner already gave and is governed by the record on the value audit (ADR-D-0036), the file-line sentence being about answers and consents given in the session; how a relay or an escalation travels between sessions; the wording of the owner's statement and the scope the owner gives it; how the Orchestrator records a relay; what each consent gate requires, which its own record or rule states; whether an audit's verdict can authorize a plan, which this record does not grant.

## Validation

- Each owner decision recorded in a plan shows either the owner's own statement in the Orchestrator session or Counsel's relay with the quoted words, and for a relay the plan also shows the owner's earlier statement in that session.
- A relay that arrives before that statement, or without a quotation, is recorded as not acted on.
- Review of any consent-gate text asks: does it accept an agent's message as the owner's word in any form other than this relay?

## Revisit When

- On 2026-09-30 a Claude Code Orchestrator session running Claude Fable 5.1 honoured Counsel's relays for value rulings after the owner's own statement in that session. A relayed acceptance of a decision record and a relayed merge instruction had not been exercised on any runtime on that date; a failure of either reopens this record.
- A runtime whose instructions refuse every agent message as consent, even after the owner's statement in the session, makes the relay unusable there; the decision then waits for the owner's own statement, and the alternative of stating every decision in the Orchestrator session is reopened for that runtime.
- A relayed quote is found to differ from what the owner said.
- A runtime offers a channel that delivers the owner's own messages from one session to another, which makes the relay redundant.

## More Information

Source of intent: `docs/coding-agent/briefs/value-level-operation-brief.md`, "Roles and sessions" and "Limits on the run". Related: ADR-D-0017 (harness text holds no user authority), the record on plan approval (ADR-D-0032), the record on Counsel, which holds none of the owner's authority (ADR-D-0034).
