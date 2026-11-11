---
status: proposed
adr_type: design
date: 2026-11-11
deciders: ["ebigunso"]
consulted: []
informed: []
supersedes: ["ADR-D-0016-protection-requires-demonstrable-consumers.md"]
superseded_by: null
---

# ADR-D-0073: The person directing the work is asked whether a consumer exists only where no accessible source settles it

## Context and Problem Statement

Terms used here: protection is anything a change adds or keeps so that existing behaviour stays as it is, a compatibility layer or a test assertion. A consumer is whoever or whatever relies on that behaviour. The person directing the work is the one who says what the work should do and judges what is built from its behaviour. A source is accessible when the run making the change can read it with the access it has. It settles whether a consumer exists when it shows one, or gives real evidence that there is none.

ADR-D-0071 holds that protection is owed only to a consumer that can be shown. A run that changes a surface and has no consumer to show still has to act: go ahead without the protection, or ask. ADR-D-0016, accepted on 2026-09-01, sent every such case to the person directing the work. The guidance written under it then drew the line at the repository's boundary: a surface that crosses it was a question for the person, and a surface inside it was changed and reported. The fork is what decides whether the person is asked: where the surface sits, or whether what the run can read answers the question.

## Decision

- Where no consumer of a changed surface has been shown, the person directing the work is asked whether one exists only where no accessible source settles it; the surface is then neither kept nor broken without an answer.
- Where accessible sources settle that there is none, the change goes ahead without the protection and without asking, and is reported to that person.
- Where the surface sits, inside the repository or across its boundary, does not decide which of the two applies.

## Why

Asking whether a consumer exists where the run can answer by reading spends the person's attention on something that was within reach, while where nothing the run can read answers it the person is the only source left and acting without an answer is a guess either way. Being told of a change made on evidence that there is no consumer is what makes going ahead without asking safe, because the person can still correct it.

## Rejected Alternatives

- The repository's boundary as the test, the person asked about a surface that crosses it and a surface inside it changed and reported: it lost because where a surface sits is only a proxy for whether accessible sources settle the question, and it asks about a boundary-crossing surface whose consumers the run can read. Reopen if changes to surfaces that cross a repository's boundary, made on sources taken to settle the question, are found to break consumers.
- Asking the person whenever no consumer has been found, whatever the sources show about there being none: it lost because where the sources give real evidence that there is none the question is already answered; reopen if changes made on that evidence are found to break consumers on either side of a repository's boundary.

## Decision Boundary

Invariant: the person directing the work is asked whether a consumer exists only where no accessible source settles it, and the surface is then neither kept nor broken without an answer; where the sources settle that there is none, the change goes ahead and is reported; where the surface sits never decides.

Not covered: that protection needs a consumer that can be shown (ADR-D-0071); what counts as showing a consumer or as real evidence that there is none; which sources a run can reach; what is done about a consumer that is found; how and where the question is put and the change is reported; the wording and location of the guidance.

## Validation

- Review of a change to a surface with no consumer shown asks: did accessible sources settle whether one exists? If they did not, was the person directing the work asked before the surface was kept or broken? If they settled that there is none, was the change reported?
- Review of an edit to the guidance in this area checks the direction of drift: an edit that makes where the surface sits decide whether the person is asked, drops the question where no source settles it, or drops the report of a change that went ahead needs a record replacing this one, not a prose fix.

## Revisit When

- The premise that a run judges soundly whether the sources it can read settle that a surface has no consumer no longer holds. Nothing had exercised it on 2026-11-11; a change that went ahead on sources taken to settle the question and broke a consumer those sources did not show reopens the record.

## More Information

With ADR-D-0071, replaces ADR-D-0016 in full. ADR-D-0016 sent the person directing the work every case in which a consumer could not be verified; this record sends only the case that no accessible source settles. Related: ADR-D-0071 (protection is owed only to a consumer that can be shown).
