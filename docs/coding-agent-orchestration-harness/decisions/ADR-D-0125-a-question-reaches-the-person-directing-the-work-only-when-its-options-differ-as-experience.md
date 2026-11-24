---
status: proposed
adr_type: design
date: 2026-11-24
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.2"]
informed: []
supersedes: ["ADR-D-0059-a-question-reaches-the-person-directing-the-work-only-when-its-experience-framings-differ.md"]
superseded_by: null
---

# ADR-D-0125: A question reaches the person directing the work only when its options, written as what a person would experience, read differently; one whose options read the same is Counsel's and does not reach them

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session role that person talks with about what the product does or should do. The Orchestrator session is a session that holds the Orchestrator role and plans, dispatches and reports the work.

The attention of the person directing the work is to go to the choices that change something for them, and to no others. Choices come up at every point of the work at which Counsel and that person talk, and asking about each one spends that attention. Holding the discussion as a person's experience (ADR-D-0124) does not serve this by itself: it decides the form of what Counsel brings to that person, not which matters are brought. The fork is what decides whether a choice reaches that person.

## Decision

- Before a question reaches the person directing the work, at whatever point of the work Counsel would put it, Counsel writes it as what a person would experience under each option, with the options beside each other.
- That writing is itself the test, and no judgement of whose question it is comes before it. Options that read differently go to that person in that form. Options that read the same make the question Counsel's, and it does not reach that person.
- A question that is Counsel's by the test and arises while a brief is drafted is decided by Counsel and written into the brief, marked as Counsel's own. In the ratified brief it has the support that a statement ratified with the brief has.
- A conflict between statements Counsel itself drafted is resolved by the same test where the discussion made the intent plain.

## Why

The product philosophy's "Who it is for" has a choice between things the person cannot tell apart made for them, and its "What goes wrong, in order" has them asked only what only they can answer. A person who would see at once, from the experience, that a choice does not affect them should not be asked it, at any point of the work: writing each choice as what someone would experience sorts the choices, and shows that person the ones that matter in the terms that person judges in.

## Rejected Alternatives

- Counsel judges first which questions are that person's and then writes those as experiences: it lost because the judgement then rests on Counsel's guess, while the writing shows plainly whether a choice affects what that person experiences; reopen if choices whose options read the same are found to have mattered to that person.

## Decision Boundary

Not covered: the acts the person directing the work reserved, which reach that person whatever the test shows; the level a question from a run must reach to be brought to that person at all; what Counsel does with a question an Orchestrator session sent it whose options read the same, where the call is that session's own and Counsel gives no answer on the matter (ADR-D-0097); the form in which an experience is told (ADR-D-0124); what that person is shown to ratify a brief (ADR-D-0060); the kind of a statement in a brief and who may change it (ADR-D-0054); how many matters are put to that person at a time (ADR-D-0106); how a brief marks whose a statement is; how a question is worded.

## Validation

The decision is broken where:

- a question reached the person directing the work without having been written as what a person would experience under each option, or its options, so written, read the same;
- a choice whose options read differently was settled without that person;
- a choice Counsel decided while drafting a brief stands in the brief with nothing to tell it from what that person said;
- a statement Counsel so decided, in a ratified brief, was refused the support that a statement ratified with the brief has.

## Revisit When

- The premise that a choice whose options read the same, written as what a person would experience, does not affect that person fails: a choice Counsel decided because its options read the same is found to have changed what the person directing the work experienced, or is one that person finds should have reached them. On 2026-10-15 no question had been put to that person under this test on any runtime.

## More Information

Replaces ADR-D-0059 whole. What ADR-D-0059 stated under Validation of the support of a statement Counsel decided is stated here under Decision. For a question an Orchestrator session sends whose options read the same, ADR-D-0097 has the call be that session's own and Counsel give no answer on the matter, and this record leaves that question to ADR-D-0097. Source of intent: `docs/coding-agent/briefs/completed/counsel-questions-and-planning-research-brief.md`, "Counsel's questions while drafting (issue 90)". Related: ADR-D-0124 (the experience as the form of the discussion), ADR-D-0118 (Counsel holds none of that person's authority), ADR-D-0054 (kinds of a brief's statements), ADR-D-0060 (ratification of a brief), ADR-D-0097 (what Counsel may answer an Orchestrator session), ADR-D-0109 (only what needs that person reaches them).
