---
status: proposed
adr_type: design
date: 2026-10-05
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1"]
informed: []
supersedes: []
superseded_by: null
depends_on: ["ADR-D-0036-a-product-philosophy-is-stated-only-by-the-product-owner-and-no-product-value-is-inferred-without-one.md"]
---

# ADR-D-0057: Setup records a philosophy's pointer line itself, only for a tracked document that states which philosophy it is and carries a ratification record and only where one document fits, and the person hears of it in the setup report and removes it by objecting, the objection holding at every later refresh

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Setup is the rulebook's bootstrap and refresh of a repository's rule files. A pointer line is the line in the "Repository Reference Documents" section of the repository's common rule file that names the path of the product philosophy or of the engineering philosophy and says which it is; it is the only location a philosophy has, and value-level operation finds a philosophy through it.

Before this record, a pointer line was added only on the word of the person directing the work, never by looking for a philosophy at any path, and setup said nothing of either philosophy. A person who already had a philosophy had it kept in a run only by remembering, unprompted, to have a pointer recorded. The fork is whether setup may record a pointer line itself, and if so for which document and how the person undoes a wrong pick.

## Decision

- Where a repository already has a philosophy document, setup finds it, records the pointer line to it without asking first, and says in its report that it did.
- Setup records a pointer only for a tracked document that states, in whatever words, that it is the repository's product philosophy or its engineering philosophy, and that carries a ratification record. This is how setup looks, not a form a philosophy must take.
- Where more than one document fits one philosophy, setup records none for it, names them in its report, and leaves that philosophy listed as missing.
- The person hears of a recorded pointer in the setup report and removes it by objecting. The objection is kept in the line that replaces the pointer, which names the file that is not the philosophy in a form that is not a pointer, so that a later refresh does not record that file again.
- Apart from setup's recording, a pointer line is added, removed or repointed only on the word of the person directing the work.

## Why

Someone who already has a philosophy should find it in force once setup finishes, not be told it is missing every time and have it kept in a run only if that person remembers to ask; a wrong pick costs that person one objection. A document that says which philosophy it is and carries a ratification record is the one kind setup can tell from any other document and place as one of the two, and where two fit setup cannot know which the person means, while a philosophy left unfound is corrected by a sentence from the person. The objection is kept because the lines are derived again at every refresh, and without it the next refresh would undo it.

## Rejected Alternatives

- Setup records no pointer by itself; it lists every philosophy as missing unless a pointer already exists, and the person names the file: it lost because a person who already has a philosophy is then told it is missing every time; reopen if setup is found recording documents the person did not mean as a philosophy, objection after objection.
- Detecting a philosophy by file name alone: rejected outright; it would record documents nobody ratified.
- An objection that removes the pointer and leaves no line behind: it lost because the lines are derived again at every refresh, and the next refresh would find the same file and record it again; reopen if refresh stops deriving the lines from the repository.

## Decision Boundary

Invariant: setup records a pointer line only for a single tracked document per philosophy that states which philosophy it is and carries a ratification record, and always says so in its report; the person's objection removes it and holds across refreshes; every other addition, removal or repointing of a pointer line is on the word of the person directing the work; the Decision list states the rest.

Not covered: the wording of the pointer line, of the line that lists a philosophy as missing and of the line that keeps an objection, which the rulebook text owns; that a line listing a philosophy as missing is not a pointer and turns value-level operation neither on nor off; what setup and a Counsel session say about a missing philosophy; a pointer whose file is gone or moved, which refresh flags and leaves as it is; that setup writes, drafts, templates or infers no philosophy, which the governing brief states as a constraint and the rulebook text carries, and which for the product side rests on ADR-D-0036; the form and ratification of a philosophy, which the value-documents reference owns.

## Validation

- The rulebook's bootstrap and refresh text records a pointer only as the Decision states, names the file in the report, and keeps an objection in the line that replaces the pointer.
- The value-document form and the run-side reference state setup's recording as the one exception to a pointer line changing only on the word of the person directing the work.
- On a fixture repository that has a ratified product philosophy under a path and name of its own, a fresh agent following the setup text records the pointer and its report says so, and a later run there is graded against that philosophy.

## Revisit When

- Setup is found recording documents the person did not mean as a philosophy, objection after objection.
- Philosophies that exist are found listed as missing again and again because they do not say which philosophy they are.
- Refresh stops deriving the lines from the repository.
- On 2026-10-05 setup had recorded a pointer only on fixtures; a pointer recorded in a person's own repository for a document that person had not ratified reopens this record.

## More Information

Source of intent: `docs/coding-agent/briefs/active/setup-names-what-is-missing-brief.md`, "Who it is for and why" and "A philosophy that already exists", and the plan `docs/coding-agent/plans/active/setup-names-what-is-missing-plan.md`, its planner-added requirements, Design and Decision Log. This record fixes nothing the brief states as a means. That setup finds an existing philosophy, records its pointer, says so in its report, and that the person's objection removes it are what the brief states the work must give; the test of a tracked document that states which philosophy it is and carries a ratification record, the rule that two fitting documents give no pointer, and the objection kept in the line that replaces the pointer are the run's own design. Related: ADR-D-0036 (who states a philosophy; nothing inferred where none exists), ADR-D-0024 and ADR-D-0025 (the rule files and their refresh, derived from repository facts).
