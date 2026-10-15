---
status: proposed
adr_type: design
date: 2026-10-15
deciders: ["ebigunso"]
consulted: []
informed: []
supersedes: []
superseded_by: null
depends_on: ["ADR-D-0046-value-discussion-is-conducted-from-the-viewpoint-of-a-persons-experience.md"]
---

# ADR-D-0059: A question reaches the person directing the work only when its experience framings differ, whenever Counsel puts it; a choice whose framings read the same is Counsel's

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session the person directing the work opens for value discussion, separate from any Orchestrator session.

A value discussion is held as a chain of a person's experience (ADR-D-0046), which decides the form of what Counsel brings to the person directing the work, not which matters are brought. Choices come up while a brief is drafted, during a run, at closeout and in any discussion, and asking about each one costs the attention the separate Counsel session exists to save. The fork is what decides whether a choice reaches that person.

## Decision

- Before any question reaches the person directing the work, whenever Counsel puts it, Counsel writes it as an experience change: who, what they do, what they then experience, with the options side by side.
- The framing is itself the test. Options that read the same at that level make the question Counsel's, and it does not reach that person; while a brief is drafted it is decided, written into the brief and tagged as Counsel's. Options that read differently go to the person directing the work in that form.
- A conflict between statements Counsel itself drafted is resolved by the same test when the discussion made the intent plain.

## Why

A person who would see at once, from the experience, that a choice does not affect them should not be asked it, at any moment of the work: putting each choice as an experience change sorts the choices, and shows that person the ones that matter in the terms that person judges in.

## Rejected Alternatives

- Counsel judges first which questions are the owner's and then presents those as framings: it lost because the judgement then rests on Counsel's guess, while the framing shows plainly whether a choice affects what that person experiences; reopen if choices whose framings read the same are found to have mattered to that person.

## Decision Boundary

Invariant: whenever Counsel puts a question to the person directing the work, it reaches that person only when its options, written as experience changes, read differently; a choice whose options read the same is Counsel's, and one met while a brief is drafted is written into the brief with a tag; the Decision list states the rest.

Not covered: the acts the person directing the work reserved (irreversible or outward-facing ones, and acceptances), which reach that person regardless of the test; the level a question from a run must reach to be brought to that person at all; the form of what reaches that person, which ADR-D-0046 states; what that person is shown to ratify a brief (ADR-D-0060); the kind of a statement and who may change it (ADR-D-0054); the tags' names and definitions, which the document forms state; the wording of a framing.

## Validation

- Counsel's policy states the test once, where a conversation is held, and its contacts with a run point to it.
- The brief form gives a statement Counsel decided the support a statement ratified with the brief has.
- Review of any change to Counsel's text asks: does a choice whose framings read the same still reach the person directing the work, at any moment, and does a reserved act still reach that person whatever its framings show?

## Revisit When

- A choice Counsel decided because its framings read the same is found to have changed what the person directing the work experienced.
- On 2026-10-15 no question had been put to the person directing the work under this test on any runtime; a choice Counsel decided under it that the person directing the work later finds should have reached them reopens this record.

## More Information

Source of intent: `docs/coding-agent/briefs/active/counsel-questions-and-planning-research-brief.md`, "Counsel's questions while drafting (issue 90)", including its statement of 2026-10-15 that the test applies any time Counsel puts a question to the person directing the work. Related: ADR-D-0046 (the chain as the form of the discussion), ADR-D-0034 (Counsel holds none of that person's authority), ADR-D-0054 (kinds of a brief's statements), ADR-D-0060 (ratification on framings).
