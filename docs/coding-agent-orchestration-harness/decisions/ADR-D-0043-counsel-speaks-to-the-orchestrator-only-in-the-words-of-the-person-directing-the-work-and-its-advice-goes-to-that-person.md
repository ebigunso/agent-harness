---
status: proposed
adr_type: design
date: 2026-10-02
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1"]
informed: []
supersedes: []
superseded_by: null
depends_on: ["ADR-D-0034-counsel-is-a-separate-session-at-the-level-of-behaviour-and-decisions.md", "ADR-D-0038-the-word-of-the-person-directing-the-work-reaches-an-orchestrator-session-directly-or-by-quoted-relay.md"]
---

# ADR-D-0043: About the run's work, Counsel speaks to an Orchestrator session only in the words of the person directing the work, and Counsel's own advice goes to that person, never to the Orchestrator

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. The product owner is whoever is entitled to state the product's values and to answer product-level questions for that work; when the person directing the work owns the product, both are that person. Counsel is the session the person directing the work opens for value discussion, separate from any Orchestrator session. The Orchestrator session is a session that holds the Orchestrator role (ADR-D-0020) and plans, dispatches and reports the work.

Counsel carries that person's decisions to an Orchestrator session by quoted relay (ADR-D-0038) and holds none of that person's authority (ADR-D-0034). Between relays Counsel also sees the run: its questions, its note at closeout, what is being decided. A Counsel that answers those in its own words, tells the Orchestrator what to do next, or orders the work, is acting for that person and not advising. A Counsel that says nothing of its own to anyone loses the advice it exists to give. The fork is what Counsel may say to an Orchestrator session about the run's work beyond a relay, and where its own advice goes.

## Decision

- About the run's work, Counsel speaks to an Orchestrator session only in the words of the person directing the work, given for the matter at hand or standing from earlier.
- For anything an Orchestrator session sends, Counsel does one of three things:
  - answers by quoting a statement of that person that explicitly covers the question, never extending one; such an answer is a relay and counts on a relay's terms (ADR-D-0038), and it never stands in for an act that person reserved, which is brought to that person;
  - hands it back as below the level that person wants to see, citing that person's rule that only direction-level decisions reach them; a hand-back decides nothing and returns the question to the Orchestrator to settle;
  - or brings it to that person.
- Counsel gives an Orchestrator session no instruction of its own, no opinion on how the work is done, and no order in which to do it; it may say that a question on a matter is with that person, which stops nothing.
- Counsel's advice within its own responsibility (the direction of the product and of its engineering, the documents that state them, whether what is being decided fits what that person has said) goes to that person and is not held back to spare that person a decision; it never goes to the Orchestrator session, and reaches the Orchestrator only as that person's direction.
- Counsel's read of a result at closeout is such advice and goes to that person; a copy may go to the Orchestrator session only to be shown to that person with the closeout, and the Orchestrator does not act on it.
- Counsel keeps a list of what it answered from that person's standing words and gives it to that person with its read at closeout.
- Two messages are outside this rule because they say nothing about how the run's work is done: the hand-over of a ratified brief, and Counsel's request, after its first read at closeout, for material it needs to finish that read. A stop of work is the one exception to the rule, and Counsel may issue one only as its own record provides.

## Why

Counsel holds none of that person's authority, so anything it tells the Orchestrator about the work in its own words is either an instruction with no authority behind it or advice addressed to the wrong party: the one who decides direction is that person, and advice that reaches the Orchestrator first becomes direction without that person having given it. Sending the advice to that person keeps the split of responsibility and keeps the advice.

## Rejected Alternatives

- Counsel answers the Orchestrator's questions with its own reading of what that person would want: it lost because an extended statement is Counsel's, not that person's, and the Orchestrator would act on it as if it were; reopen if questions that person's standing words plainly cover keep being brought to that person because no statement covers them explicitly.
- Counsel says nothing of its own to anyone, a carrier only: it lost because that person would then decide direction without the advice Counsel was opened to give; reopen if Counsel's advice to that person is found to be about how the work is done.
- Counsel's advice goes to the Orchestrator as advice, marked as not binding: it lost because the Orchestrator cannot weigh direction-level advice without deciding direction, which is that person's; reopen if an Orchestrator session is shown to carry such advice in its records without its plans changing on it.
- Counsel's read of a result goes to the Orchestrator as input to the run: it lost for the same reason, the read being advice on direction; reopen on the same condition.

## Decision Boundary

Invariant: about the run's work, Counsel sends an Orchestrator session only that person's quoted words, a hand-back citing that person's rule, or notice that a question is with that person; Counsel's own advice, its read of a result included, goes to that person, a copy of the read reaching the Orchestrator only for display; the hand-over, a request for closeout material and a stop provided by its own record are outside the rule; the Decision list states the rest.

Not covered: when a quoted relay counts as that person's decision and what admits relays (ADR-D-0038); what Counsel is responsible for (ADR-D-0034); how far Counsel reaches into the work (ADR-D-0035); whether and when Counsel may stop work (ADR-D-0044); what the Orchestrator escalates and at what level; what the hand-over and the closeout exchange contain; how a message travels between sessions.

## Validation

- Counsel's policy states the three answers, that Counsel gives the Orchestrator no instruction, opinion or sequencing of its own, that its advice and its read go to that person, and the list it keeps.
- The Orchestrator's run-side text states that a hand-back returns the question to the Orchestrator, that a notice stops nothing, and that nothing Counsel says in its own words is acted on as direction or as that person's decision.
- Review of any change to Counsel's text asks: does this let Counsel tell the Orchestrator what to do, or let its advice reach the run before that person?

## Revisit When

- Counsel is found answering from a standing statement that did not explicitly cover the question.
- A question handed back as below that person's level is later found to have been a direction-level decision.
- On 2026-10-02 no question had been handed back and no answer given from standing words under this rule on any runtime; either failure above, at first occurrence, reopens this record.

## More Information

Source of intent: `docs/coding-agent/briefs/active/value-level-operation-brief.md`, "Roles and sessions". Related: ADR-D-0034 (Counsel's role), ADR-D-0038 (the relay), ADR-D-0044 (the pause), ADR-D-0035 (Counsel's reach).
