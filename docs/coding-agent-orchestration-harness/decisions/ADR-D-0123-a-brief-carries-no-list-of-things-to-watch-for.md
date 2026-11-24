---
status: proposed
adr_type: design
date: 2026-11-24
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1", "Claude Fable 5.2"]
informed: []
supersedes: ["ADR-D-0045-during-a-run-counsel-hears-from-the-audit-only-of-an-item-let-through-on-a-provisional-statement.md"]
superseded_by: null
---

# ADR-D-0123: A brief carries no list of things to watch for, and the value audit checks no item against one

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session role that person talks with about what the product does or should do. A brief is the document that person ratifies as the grounds for a run, and a run is the work done under one ratified brief. The value audit is the independent grading of a run's plan and result against the brief and the philosophies. A constraint is a statement of a brief that binds whatever else is true, and the audit holds an item that goes against one.

The person directing the work wants a matter they would have stopped, or decided differently, to come up while the run can still change course, and not only at closeout. One way to give that is a list in the brief of things to watch for, with the audit checking each item it grades against the list and each match reported to Counsel as the run goes. Such a list does not serve the want. What can be named ahead of the run can be written as a constraint, which stops the item where a match only reports it. What cannot be foreseen is on no list. What is left are matches on things that are fine. The fork is whether a brief carries such a list at all.

## Decision

- A brief carries no list of things to watch for, and the value audit checks no item against one.

## Why

A list of things to watch for is wrong in kind: what can be foreseen is a constraint written a second time with a weaker consequence, against the engineering philosophy's "Where it goes", which has each thing written once; what cannot be foreseen cannot be listed, as its "What to leave open" says of any list of cases; and what remains is being told of things that are fine, while a list worded poorly is reworded again and again for nothing.

## Rejected Alternatives

- The brief keeps a list of things to watch for, and the audit checks every item against it: it lost for the reason under Why; reopen if matters the person directing the work would have wanted to hear of at once are found to have reached that person only at closeout, with no constraint that could have named them.

## Decision Boundary

Not covered: what a brief carries in place of such a list, which is its constraints, and how Counsel draws them out before ratification; that the audit holds an item that goes against a constraint, and its grades, positions and dispatch (ADR-D-0052); what Counsel does hear from the audit during a run (ADR-D-0122); that Counsel's first read of a result is formed without what the audit marks, apart from what reached Counsel during the run (ADR-D-0126); what is shown at closeout (ADR-D-0042); the questions the Orchestrator session escalates and a finding that bears on the design (ADR-D-0053); the forms of a brief and of the audit's verdict, which the plugin's text states.

## Validation

The decision is broken where a brief carries a list of things to watch for, or where the value audit checked an item against such a list or reported a match with one.

## Revisit When

- The premise that a list of things to watch for gives nothing a brief's constraints do not, since what can be foreseen is a constraint written a second time and what cannot be foreseen cannot be listed, fails: matters the person directing the work would have wanted to hear of at once are found to have reached that person only at closeout, with no constraint that could have named them.

## More Information

With ADR-D-0122 and ADR-D-0126, replaces ADR-D-0045 in full. Related: ADR-D-0052 (the value audit), ADR-D-0054 (how a brief's statements bind). Source of intent: `docs/coding-agent/briefs/completed/design-led-long-runs-brief.md`, "Watch list" and "What reaches you, and what does not".
