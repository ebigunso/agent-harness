---
status: proposed
adr_type: design
date: 2026-11-24
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.2", "GPT-6 Astra"]
informed: []
supersedes: []
superseded_by: null
---

# ADR-D-0129: Nothing from a lesson becomes a new obligation on later sessions until the person has said yes, and until then a lesson informs and requires nothing

## Context and Problem Statement

Terms used here: a lesson is what a session records of a mistake so that the same mistake is not made twice. The person is whoever directs the work and whose the repository's rules are to decide. An obligation is anything every later session must follow: a rule of the repository, or a setting in the person's own scope. A lesson waits while it has neither left the record of lessons nor been made an obligation.

A mistake is not to be made twice, and what binds every later session is to be well framed, because a badly framed rule is costly. A rule made from a lesson is prone to being badly framed. A lesson that a session makes a rule on its own, when it is written or when the mistake comes again, binds every later session unasked; one that waits but is held as a requirement by a plan or an audit does the work of a rule without being one. The fork is whether a session makes a lesson binding and tells the person, as it does with other things that can be undone, or the lesson waits for the person's yes.

## Decision

- Nothing from a lesson becomes a new obligation on later sessions, as a rule of the repository or as a setting in the person's own scope, until the person has said yes. There is no exception for a context held to be well known.
- Until then a lesson informs the next judgement and requires nothing: a session takes it into account and says that it did. It is no source of a plan's requirement and nothing an audit holds the work to.
- Where a remedy adds no new obligation and only makes something the person already accepted take effect, it is done and the person is told.
- The work does not wait for the person's answer; the lesson waits.

## Why

A rule binds every later session, so a badly framed one is costly, and a rule made from a lesson is prone to being badly framed. That is why it waits although a rule can be undone: the product philosophy's "The line" says "The line is drawn by whether a thing can be taken back and how far it reaches, never by whose decision it could be called", and a rule reaches every later run. A remedy that adds no obligation is what "What goes wrong, in order" speaks of in "If a decision can be undone and stays inside the work, it is made and reported, and not asked."

## Rejected Alternatives

- The session that writes a lesson makes it a rule and tells the person: it lost because a rule binds every later session, so a badly framed one is costly, and a rule made from a lesson is prone to being badly framed; reopen if a session can be shown to hold enough context about the person and the situation they are in to decide this with high enough precision.
- A lesson becomes a rule when the mistake occurs a second time: it lost for the same reason, so a second occurrence that no existing rule covers produces a proposal and not a rule; reopen on the same condition.
- A lesson that still waits is held as a requirement by a plan or an audit: rejected outright; it lets a waiting lesson do the work of a rule, and only the person's yes gives anything from a lesson that force.

## Decision Boundary

The decision holds where the lessons are one person's to decide. In a repository several people work in, what would bind the others goes by whatever way that repository changes its rules.

Not covered: how a proposal is worked through, what it shows and which answers are offered; that lessons sharing a cause reach the person as one decision; how many matters are put to the person at a time, in what order and when (ADR-D-0106, ADR-D-0110, ADR-D-0116); how the yes is kept with the rule made on it; which lessons a session removes without asking, and on what grounds; a statement of fact about the repository that is not the prevention of a mistake; whether the person is asked before a fact of their machine is recorded; where the person's own scope is.

## Validation

The decision is broken where a rule of a repository or a setting in the person's own scope that adds an obligation came from a lesson with no yes of the person's; where a plan or an audit holds work to a lesson that still waits; where the person is asked about a remedy that adds no obligation and only makes something they already accepted take effect; or where work waited for the answer to a proposal.

## Revisit When

- The premise that no session can tell whether a context is well enough known to make something binding unasked fails. It was held on 2026-11-21 as a judgement; a session shown to hold enough context about the person and the situation they are in to decide this with high enough precision reopens whether everything from a lesson waits for the yes.

## More Information

Source of intent: the brief "Lessons keep their purpose", "Who it is for and why", "A lesson waits, and then leaves", "What is asked, and what is not", "Limits" and "Left out on purpose". Related: ADR-D-0105 (harness text holds none of the user's authority), ADR-D-0109 (only what needs the person reaches them).
