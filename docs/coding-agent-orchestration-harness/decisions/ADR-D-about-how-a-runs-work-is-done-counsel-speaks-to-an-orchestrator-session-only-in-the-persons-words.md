---
status: proposed
adr_type: design
date: 2026-11-17
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "Claude Fable 5.2"]
informed: []
supersedes: ["ADR-D-0043-counsel-speaks-to-the-orchestrator-only-in-the-words-of-the-person-directing-the-work-and-its-advice-goes-to-that-person.md"]
superseded_by: null
depends_on: ["ADR-D-0034-counsel-is-a-separate-session-at-the-level-of-behaviour-and-decisions.md", "ADR-D-0038-the-word-of-the-person-directing-the-work-reaches-an-orchestrator-session-directly-or-by-quoted-relay.md"]
---

# ADR-D (not yet numbered): About what a run's work is to be and how it is done, Counsel speaks to an Orchestrator session only in the words of the person directing the work, and Counsel's own advice goes to that person

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session role that person talks with about what the product does or should do. The Orchestrator session is a session that holds the Orchestrator role and plans, dispatches and reports the work. A run is the work done under one ratified brief.

Counsel carries that person's decisions to an Orchestrator session by quoted relay (ADR-D-0038) and holds none of that person's authority (ADR-D-0034). Counsel also sees the run: its questions, where it stands, its result. A Counsel that answers those in its own words, tells the Orchestrator what to do next, or orders the work, is acting for that person and not advising. A Counsel that says nothing of its own to anyone loses the advice it exists to give. The fork is what Counsel may say to an Orchestrator session beyond a relay, and where its own advice goes.

## Decision

- About what a run's work is to be and how it is done, Counsel speaks to an Orchestrator session only in the words of the person directing the work, given for the matter at hand or standing from earlier. It gives no instruction of its own, no opinion on how the work is done, and no order in which to do it.
- Counsel answers from a statement of that person's only where the statement explicitly covers the question, and never extends one. What no statement covers Counsel brings to that person or returns undecided, and it never answers for an act that person reserved.
- Counsel's own advice, its read of a result included, goes to that person and is not held back to spare that person a decision. It reaches an Orchestrator session only as that person's direction.
- What falls under this is settled by what a message says and not by a list of messages: what Counsel sends in its own words that says nothing of what the work is to be or how it is done, and decides nothing in it, is outside the rule.
- The one exception is a stop of part of the work, which Counsel issues only as its own record provides (ADR-D-0044).

## Why

Counsel holds none of that person's authority, so anything it tells an Orchestrator session about the work in its own words is either an instruction with no authority behind it or advice addressed to the wrong party: advice that reaches the Orchestrator first becomes direction without that person having given it. The product philosophy's "The line" says a decision made for someone and never mentioned leaves them unable to correct it; sending the advice to that person keeps the direction theirs and keeps the advice.

## Rejected Alternatives

- Counsel answers the Orchestrator's questions with its own reading of what that person would want: it lost because an extended statement is Counsel's, not that person's, and the Orchestrator would act on it as if it were; reopen if questions that person's standing words plainly cover keep being brought to that person because no statement covers them explicitly.
- Counsel says nothing of its own to anyone, a carrier only: it lost because that person would then decide direction without the advice Counsel exists to give; reopen if Counsel's advice to that person is found to be about how the work is done.
- Counsel's advice goes to the Orchestrator as advice, marked as not binding: it lost because the Orchestrator cannot weigh advice on direction without deciding direction, which is that person's; reopen if an Orchestrator session is shown to carry such advice in its records without its plans changing on it.
- Counsel's read of a result goes to the Orchestrator as well as to that person: it lost for the same reason, the read being advice on direction; reopen on the same condition.
- The messages outside the rule are listed in this record: it lost because every new contact between Counsel and a run would leave the list short while the rule stood unchanged; reopen if messages are found passing as outside the rule that told an Orchestrator session how to do its work.

## Decision Boundary

Not covered: when a quoted relay counts as that person's decision and what admits relays (ADR-D-0038); what Counsel is responsible for (ADR-D-0034); how far Counsel reaches into the work (`ADR-D-counsel-reads-code-only-to-serve-a-discussion-and-takes-no-part-in-doing-or-checking-a-runs-work.md`); whether and when Counsel may stop work (ADR-D-0044); the ways Counsel answers what an Orchestrator session sends, and the note it keeps of what it answered from standing words, which Counsel's text states; what the Orchestrator escalates and at what level; which messages Counsel sends a run and what each contains; how a message travels between sessions.

## Validation

The decision is broken where an Orchestrator session received from Counsel, in Counsel's own words, an instruction, an opinion on how the work is done or an order in which to do it; where Counsel answered from a statement that did not explicitly cover the question; where Counsel's advice or its read of a result reached an Orchestrator session other than as that person's direction; where Counsel held advice back from that person; or where an Orchestrator session acted on Counsel's own words as direction or as that person's decision.

## Revisit When

- The premise that Counsel can tell a statement that explicitly covers a question from one it would be extending fails: Counsel is found to have answered from a standing statement that did not cover the question.
- A question Counsel returned as below the level that person wants to see is found to have been a decision of direction.

## More Information

Replaces ADR-D-0043 in full; the decision is the same. Changed in how it is stated: ADR-D-0043 listed two messages as outside the rule and gave the reason, that they say nothing about how the run's work is done; this record states the reason as the rule and lists none, and the last rejected alternative is new with it. Moved out: the three ways Counsel answers what an Orchestrator session sends, and the list Counsel keeps of answers from standing words, which Counsel's text states. Source of intent: `docs/coding-agent/briefs/completed/value-level-operation-brief.md`, "Roles and sessions".
