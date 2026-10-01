---
status: accepted
adr_type: design
date: 2026-09-30
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1"]
informed: []
supersedes: []
superseded_by: null
depends_on: ["ADR-D-0017-harness-text-holds-no-user-authority.md", "ADR-D-0034-counsel-is-a-separate-session-at-the-level-of-behaviour-and-decisions.md"]
---

# ADR-D-0038: The word of the person directing the work reaches an Orchestrator session as that person's own statement there or, once that person has admitted relays in that session or by a standing approval in the rule files, as Counsel's relay quoting that person

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. The product owner is whoever is entitled to state the product's values and to answer product-level questions for that work; when the person directing the work owns the product, both are that person. Counsel is the session the person directing the work opens for value discussion, separate from any Orchestrator session. The Orchestrator session is a session that holds the Orchestrator role (ADR-D-0020) and plans, dispatches and reports the work.

The relay decided here is how the word of the person directing the work arrives in an Orchestrator session when that person is not typing into it. Under value-level operation the person directing the work talks with Counsel, and the Orchestrator session's consent gates need that person's decision all the same: the ratification of a brief, the acceptance of a decision record or of a standing approval, the instruction to merge a named pull request, and the answers to questions a run brings back. An Orchestrator session cannot tell a faithful relay of that person's words from any other agent message, and harness text holds none of that person's authority (ADR-D-0017). The fork is what an Orchestrator session may treat as the word of the person directing the work when that person is not the one typing into it.

## Decision

- An Orchestrator session takes a decision of the person directing the work from that person's own statement in that session, or from a relay by Counsel that quotes that person's words.
- The relay counts only once admitted, in one of two ways: the person directing the work has told that Orchestrator session directly to accept Counsel's relays as that person's own; or a standing approval in the repository's rule files, accepted by the person directing the work, names Counsel's identity as the carrier of that person's decisions for the repository, and every Orchestrator session reads it at start. Without either, a relay is an agent's message and carries nothing, and the decision waits for that person's own statement.
- A relay carries exactly what the quoted words say.
- The terms of each gate are unchanged, and the quoted words must themselves meet them, such as naming the pull request or the record.
- Counsel's paraphrase, summary or own view, and any other agent's message, carry no decision of the person directing the work.
- A line in a file records an act and is not the act: a file line is never that person's answer to a question or consent at a gate in the session.
- Each relayed decision rests on Counsel quoting faithfully, which the Orchestrator cannot verify; that is the cost the person directing the work accepts in admitting relays, and it is why admission comes first. Under the standing approval one more risk remains: the Orchestrator cannot tell a message from the named Counsel identity from an impersonation of it, since the sender of an agent message can be forged; the person directing the work accepts that risk in accepting the entry.
- Approval or waiver of a plan is not carried by relay under this record: plans are presented only by the Orchestrator session, and the record on plan approval governs where approval comes from (ADR-D-0040).

## Why

The person directing the work should not need to type into the Orchestrator session: the Orchestrator escalates, Counsel brings the question to that person, and the answer has to be able to travel back. The session that acts on that person's authority cannot verify a relay, so an act of that person's own is what makes Counsel's quoting the chosen carrier instead of an agent's claim to speak for that person. The act names who may speak for that person and gives the session a reason to act on an agent's message. In the session, it is a statement; a per-session statement means typing it into every Orchestrator session after each restart, so the same act may be given once, as a standing approval that names Counsel's identity and is read at every session start. The risk of a relay misquoting is the same either way; the standing approval adds only the impersonation risk stated in the Decision.

## Rejected Alternatives

- The person directing the work states every decision in the Orchestrator session: it lost because that person should not need to type into that session, where the Orchestrator escalates and Counsel brings the question to that person; reopen if a supported runtime's instructions refuse every agent message as consent even after that person's statement in the session, or if a relayed quote is found to differ from what was said.
- Any message from Counsel counts as the word of the person directing the work: rejected outright; an agent's message would claim that person's authority (ADR-D-0017).
- A relay counts from the first message, with neither a statement from the person directing the work in the Orchestrator session nor a standing approval that person accepted: rejected outright; the Orchestrator would take on an agent's word the authority to take agents' words.
- Counsel relays the substance in its own words: rejected outright; a paraphrase is Counsel's statement, not that person's.
- A ratified status written in a brief file counts as ratification: rejected outright; ratifying is an act of the person directing the work, and a line in a file records the act and is not it.

## Decision Boundary

Invariant: a relay from Counsel counts as the decision of the person directing the work only once that person has admitted relays, by that person's own statement in the Orchestrator session or by an accepted standing approval in the rule files naming Counsel's identity, only as a quotation of that person's words, and only when those words meet the terms of the gate; plan approval and waiver are never carried by relay; the Decision list states the rest.

Not covered: statements of the person directing the work on channels other than the Orchestrator session and Counsel's relay, for example a pull-request comment from that person's account, which this record neither admits nor excludes; how the product owner's answer reaches the person directing the work, which precedes this relay; a standing approval in effect, which records an acceptance already given and is governed by the record on the value audit (ADR-D-0039), the file-line sentence being about answers and consents given in the session; how a relay or an escalation travels between sessions; the wording of the statement or entry admitting relays and the scope given to it; how a runtime identifies the sender of an agent message; how the Orchestrator records a relay; what each consent gate requires, which its own record or rule states; whether an audit's verdict can authorize a plan, which this record does not grant.

## Validation

- Each decision of the person directing the work recorded in a plan shows either that person's own statement in the Orchestrator session or Counsel's relay with the quoted words, and for a relay the plan also shows what admitted relays: the statement in that session, or the standing approval entry.
- A relay that arrives before relays are admitted, or without a quotation, is recorded as not acted on.
- Review of any consent-gate text asks: does it accept an agent's message as the word of the person directing the work in any form other than this relay?

## Revisit When

- On 2026-09-30 a Claude Code Orchestrator session running Claude Fable 5.1 honoured Counsel's relays for value rulings after the statement of the person directing the work in that session, and on 2026-10-01 the same session honoured relayed acceptances of decision records (ADR-D-0034 to ADR-D-0037). A relayed merge instruction, and a relay admitted by the standing approval alone in a fresh session, had not been exercised on any runtime on that date; a failure of either reopens this record.
- A runtime whose instructions refuse every agent message as consent, even after relays are admitted, makes the relay unusable there; the decision then waits for the person's own statement, and the alternative of stating every decision in the Orchestrator session is reopened for that runtime.
- A relayed quote is found to differ from what the person directing the work said, or a message is found to have carried the Counsel identity without coming from Counsel.
- A runtime offers a channel that delivers that person's own messages from one session to another, which makes the relay redundant.

## More Information

ADR-D-0033 says "the user" for the person present in the Orchestrator session; this record says the person directing the work. Source of intent: `docs/coding-agent/briefs/value-level-operation-brief.md`, "Roles and sessions" and "Limits on the run". Related: ADR-D-0017 (harness text holds no user authority), the record on plan approval (ADR-D-0040), the record on Counsel, which holds none of that person's authority (ADR-D-0034).
