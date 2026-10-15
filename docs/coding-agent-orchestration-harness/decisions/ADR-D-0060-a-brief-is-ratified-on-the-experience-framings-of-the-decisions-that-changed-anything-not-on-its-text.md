---
status: accepted
adr_type: design
date: 2026-10-15
deciders: ["ebigunso"]
consulted: []
informed: []
supersedes: []
superseded_by: null
depends_on: ["ADR-D-0046-value-discussion-is-conducted-from-the-viewpoint-of-a-persons-experience.md", "ADR-D-0059-while-a-brief-is-drafted-a-choice-reaches-the-person-directing-the-work-only-when-its-experience-framings-differ.md"]
---

# ADR-D-0060: A brief is ratified on the experience framings of the decisions in it that changed anything, not on its text, and the brief stays the record

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session the person directing the work opens for value discussion, separate from any Orchestrator session.

A brief is the grounds for a run and is ratified by the person directing the work before it is handed over. Having that person read the finished brief to ratify it costs the attention the separate Counsel session exists to save, and a list of the brief's tagged decisions is still text to read. The fork is what that person is shown to ratify.

## Decision

- At ratification the person directing the work is shown the experience framings for the decisions in the brief that changed anything, not the brief.
- The brief stays the record on disk for the run and the audit, and its tags stay in it. That person reads it only if that person wants to.

## Why

Reading a long brief to ratify it is the same burden as reading a plan: showing the decisions that changed anything as experience changes puts what that person ratifies in the terms that person judges in, and leaves the full text to the readers that rely on it.

## Rejected Alternatives

- A list of the brief's tagged decisions shown at ratification and again at closeout: it lost because a list of statements is the text-reading burden the framings remove; reopen if the framings are found to hide a decision that person would have objected to in the list.
- The person directing the work reads the whole brief to ratify it: it lost for the same reason as the list; reopen if ratifications on framings are found to miss statements that person later rejects.

## Decision Boundary

Invariant: a brief is ratified on the framings of the decisions in it that changed anything, not on its text; the brief stays the record for the run and the audit, with its tags; the Decision list states the rest.

Not covered: which choices reach that person while a brief is drafted, and which are Counsel's to decide (ADR-D-0059); the form of a framing, which ADR-D-0046 states; the kind of a statement and who may change it (ADR-D-0054); the tags' names and definitions, which the document forms state; the wording of a framing.

## Validation

- Counsel's policy states ratification on framings where a brief is drafted, and no sentence of it has that person read the brief to ratify it.
- The brief form gives a statement ratified on its framing the support a statement ratified with the brief has.
- Review of any change to Counsel's text asks: does the person directing the work still have to read the brief to ratify it?

## Revisit When

- On 2026-10-15 no brief had been ratified on framings on any runtime; a ratification that person later finds missed a statement they would have rejected reopens this record.

## More Information

Source of intent: `docs/coding-agent/briefs/active/counsel-questions-and-planning-research-brief.md`, "Counsel's questions while drafting (issue 90)". Related: ADR-D-0059 (which choices reach that person while drafting), ADR-D-0046 (the chain as the form of a framing), ADR-D-0054 (kinds of a brief's statements).
