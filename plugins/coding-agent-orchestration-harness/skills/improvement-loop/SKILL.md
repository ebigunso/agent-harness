---
name: improvement-loop
description: Lessons for Orchestrator-driven workflows, so that the same mistake is not made twice. Use when a hard gate was missed (required validation or evidence skipped, a wrong done/blocked state, a safety or policy gate miss), when a run audited against the owner's value documents made a wrong stop or skipped a decision that needed the owner, when a review, CI, or human finding arrives that the harness should have caught, when a user correction changes a durable default (workflow, validation, scope), when the owner says what they want for one case of a kind that may come again, or when a mistake broke output or cost significant time; and when lessons are looked up for the work in hand, or a lesson is to be removed, proposed to the person as a rule, or made one on their yes. Records the lesson and states the durable default change before ending the turn; low-signal corrections (tone, wording, a one-off format) are applied without a lessons entry.
---

# Skill: improvement-loop

A lesson exists so that the same mistake is not made twice. This skill says when a lesson is written; `references/settling-lessons.md` says everything that follows.

The Lessons Log is repo-local: `docs/coding-agent/lessons.md`.

---

## Core rules (always apply)

1) Close the correction loop
Before ending the turn, write the lesson for each capture trigger in rule 2 that occurred, and state any durable default change.

2) One capture rule
- Record a lesson before ending the turn when any of these occurred:
  - a hard gate was missed (required validation or evidence skipped, a wrong done/blocked state, a safety or policy gate miss)
  - in a run audited against the owner's value documents: a wrong stop (the run stopped on something the documents already answered, for a decision that can be undone) or a skipped decision (something that needed the owner went ahead)
  - a review, CI, or human finding arrived that the harness should have caught
  - a correction changed a durable default (workflow, validation, scope)
  - the owner said what they want for one case of a kind that may come again (`references/settling-lessons.md`, An answer the owner gave for one case)
  - a mistake broke output or cost significant time
- A miss of a rule that already exists is settled as `references/settling-lessons.md` (The four questions, 1) states and leaves no entry to wait: the session makes the remedy in the same turn, asks nothing and tells the person in a line, the remedy holding work only to what the existing rule already says; anything further is a proposal that waits for the person's yes, and the reference says the rest, the case where the remedy cannot be made in the work in hand included.
- Low-signal corrections (tone, wording, a one-off format) are applied in the current task without a lessons entry.
- If the lessons file does not exist, create it using the template in references/lessons-template.md.

3) A lesson keeps its account
- Write the entry in the form of references/entry-template.md, newest at the top. A mistake already in the log is added to its entry, one entry for one cause.
- The account of what produced the lesson stays with it, concrete and specific to what happened, because the later decision to make it a rule or drop it is checked against the account.

4) Record durable default changes only when the correction changes future behavior
- If the user approves a new persistent default, workflow default, or other future-behavior change, state it back in the same turn as the correction handling.
- Do not treat ordinary plan refinements, one-off task tactics, or local execution adjustments as persistent defaults.
- If the user explicitly says the change is one-time only, record it as a one-time exception instead of a new default. What the owner wants for one case of a kind that may come again is no new default either; it is kept as a lesson (rule 2).

5) Writing a lesson settles nothing
Read `references/settling-lessons.md` before acting on one in any way: it is the one statement of what a waiting lesson may and may not do, and of what waits for the person's yes.

---

## Progressive disclosure (read only what you need)

`references/settling-lessons.md`, by heading:
- Looking up lessons, at the start of work and partway through: Finding and applying lessons; A waiting lesson informs and requires nothing.
- Whether and when a lesson leaves the log: How a lesson leaves; When its leaving is decided; What is removed without asking.
- Before anything from a lesson, a review finding or a rule candidate goes into a rule file or becomes a setting in the person's own scope: What waits for the person's yes; The four questions; Putting a proposal to the person.
- The owner answered for one case: An answer the owner gave for one case.
- The log is too long to read whole: A log grown too large.
- Several people work in the repository: A repository several people work in.
- The mistake was the harness's own: A defect of the harness.
- The log has entries or a header in an older form: Older entries and headers.

If you need a lessons file template:
- Read references/lessons-template.md

If you need a single lesson entry template:
- Read references/entry-template.md
