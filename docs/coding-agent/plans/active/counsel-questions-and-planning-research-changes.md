# Changes file: Counsel's questions while drafting, and research before a plan

- Run record: `docs/coding-agent/plans/active/counsel-questions-and-planning-research-run.md`. Readings file: `docs/coding-agent/plans/active/counsel-questions-and-planning-research-readings.md`.
- Holds the trace of each small change of the run built without a plan; the Orchestrator's writing, not audit-stated. Created 2026-10-15 when the owner directed a change against the brief while the run was open for his judgement.

## Small change 1: drops and departures reach the owner as framings at ratification

- Directed by the owner while the run is open, on the closeout verdict's second marked item (Counsel SKILL.md L54 still has Counsel list the statements dropped or departed from before ratification). His words, relayed by Counsel on 2026-10-15 (admitted by the standing approval of 2026-10-01), quoted in full: "Yes, change it." Counsel's question to him, as relayed: left as it is, he sees the framings plus a list of statements at ratification; changed, drops and departures reach him as framings too, only where they changed anything, so ratification is one short read.
- Where the statement stands in the brief: `docs/coding-agent/briefs/active/counsel-questions-and-planning-research-brief.md`, section "Directed after the run was reported ready", first statement (committed cf4d618).
- Starts from revision: cf4d618.
- The Orchestrator's call: small, no plan; one task, text only. The Counsel skill's pre-ratification step (L54) for a brief: drops and departures reach the owner as experience framings, only where they changed anything, and Counsel does not list the statements; the value-documents line that a brief's drops are each confirmed by the owner (L59) made to agree, the ratification on framings covering the whole brief as L65 already states. A philosophy's ratification is untouched: the statement and its section concern a brief, and the skill already keeps a philosophy's full text (L57). No decision record: ADR-D-0060 (accepted) already decides that at ratification the owner sees the framings of what changed anything and not the brief's text; the change brings L54 into line with it and changes none of its decision, boundary, reasons or reopen conditions. Built on the run's branch, on top of stack 74, in pull request 91, whose text is brought up to date.

## Build and checks of small change 1

- Worker report (one task, `done`, one YAML block, two files) at a1627a2: Counsel SKILL.md L54 now opens with a brief's drops and departures reaching the owner at ratification as experience framings beside the brief's other decisions, only where they changed anything, with no list of statements; a philosophy keeps its steps in a sentence of its own (drops listed with why and confirmed, departures listed); the question on what the work must not do or must ask before doing is unchanged, now opening "Before asking for ratification, ask". value-documents L59: a drop recorded in a brief is ratified with the brief and shown to the owner as a framing where it changed anything. Counsel skill 3834 to 3898 words. Worker validation: package validator pass, smoke tests pass, `git diff --check` clean; no rule file and no decision record touched.
  - Judgement calls (Worker): "cannot decide anything" kept for a brief, adapted to the framings: if no departure changed anything, Counsel says the brief cannot decide anything (one remark, not a list), so a brief that only restates the conventional answer still warns the owner.
  - Orchestrator ruling: the call kept, for the review to judge against the statement's "Counsel does not list the statements".
- Review (Codex reviewer, range 56673b5..a1627a2): APPROVED, no finding open.
- Closing audit, dispatch text (to a fresh Auditor dispatch on Opus; Fable was at the account's usage limit earlier the same day, so the run's closeout audit also ran on Opus):

  ```text
  You are the value auditor. Read references/value-audit-mandate.md of the orchestration-harness skill and follow it exactly. Position: closeout. Plan: docs/coding-agent/plans/active/counsel-questions-and-planning-research-changes.md. Governing brief: docs/coding-agent/briefs/active/counsel-questions-and-planning-research-brief.md. Changes since: cf4d618.
  ```
