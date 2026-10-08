# Changes file: First use in a fresh repository

- Run record: `docs/coding-agent/plans/active/first-use-in-a-fresh-repository-run.md`. Readings file: `docs/coding-agent/plans/active/first-use-in-a-fresh-repository-readings.md`.
- Holds the trace of each small change of the run built without a plan; the Orchestrator's writing, not audit-stated. Created 2026-10-08 when the owner directed changes against the brief while the run was open for his judgement.

## Small change 1: a provisional mark lives in the companion, not in a philosophy's prose

- Directed by the owner while the run is open, on the closeout verdict's item C6. His words, relayed by Counsel on 2026-10-08 (admitted by the standing approval of 2026-10-01), quoted in full: "Both yes to 1 and 2." (to Counsel's two proposals; this is the first).
- Where the statement stands in the brief: `docs/coding-agent/briefs/active/first-use-in-a-fresh-repository-brief.md`, section "Directed after the run was reported ready", first statement (committed 106097c).
- Starts from revision: 106097c.
- The Orchestrator's call: small, no plan; one task, text only (value-documents' provisional line for a philosophy, the audit's reading of a provisional statement, Counsel's drafting line); his statement leaves no how-choice someone should see first. Built together with small change 2 by one Worker, reviewed once, audited once at the close of both.

## Small change 2: at open, Counsel takes its seat where it does not already hold it

- Directed by the owner while the run is open, on the run's observation that no open-time seat step exists. His words, relayed by Counsel on 2026-10-08, quoted in full: "Both yes to 1 and 2." (the second).
- Where the statement stands in the brief: the same section, second statement.
- Starts from revision: 106097c.
- The Orchestrator's call: small, no plan; one sentence in the Counsel skill's open-time steps, whether or not the Counsel line is present; the first-session reference's seat text then says the same once.

## Build and checks of small changes 1 and 2

- Worker report (one task, `done`, one YAML block, five files): a provisional mark stands in place in a brief only, a philosophy's going in its companion naming the statement, the prose unmarked, the companion's contents line now four things; the mandate, value-level-operation and Counsel's drafting read a philosophy's mark from the companion; one open-time seat step before the Counsel-line check, whether or not the line is there; first-session's seat paragraph refers to that step and keeps the move off the Orchestrator's seat. Word count 3518 to 3559 (+15 change 1, +26 change 2); the two lines unchanged. Worker validation: package validator pass, smoke tests pass, `git diff --check` clean, template block byte-identical, grep: no plugin text expects a provisional mark inside a philosophy's prose.
  - Judgement calls (Worker): the old-form line (a record inside the document) not extended to old in-prose provisional marks; the seat step reads "whether or not the line below is there"; first-session drops "before the first relay" and the runtime-claims sentence, the step's "where you do not already hold it" covering the runtime case.
  - Orchestrator ruling: first-session's opening sentence, "does nothing more", reworded by the Orchestrator to "does nothing beyond the open-time steps", since the seat step now runs at every open.
- Review (Codex reviewer, at 22aebba): APPROVED, no finding open.
- Closing audit, dispatch text (to a fresh Auditor dispatch on Fable):

  ```text
  You are the value auditor. Read references/value-audit-mandate.md of the orchestration-harness skill and follow it exactly. Position: closeout. Plan: docs/coding-agent/plans/active/first-use-in-a-fresh-repository-changes.md. Governing brief: docs/coding-agent/briefs/active/first-use-in-a-fresh-repository-brief.md. Changes since: 106097c.
  ```
- Closing audit, verdict as returned (machine paths redacted; the two comparison lines are logged in the readings file, not here):

  ## Value audit: Small changes 1 and 2, closeout

  Procedural note: the changes file and the brief were opened in the same call as the mandate, before the mandate was read to its end. Both are sanctioned inputs; no notes or readings file was opened before the grades were fixed, so the audit is not voided. Recorded here so the Orchestrator sees the deviation.

  - `Position: closeout`
  - `Documents read: docs/coding-agent/plans/active/first-use-in-a-fresh-repository-changes.md; docs/coding-agent/briefs/active/first-use-in-a-fresh-repository-brief.md; docs/coding-agent/plans/active/first-use-in-a-fresh-repository-run.md (Scenarios section for prior states); docs/coding-agent/rules/common.md (Repository Reference Documents, Standing Approvals, validation commands); git diff 106097c..working tree for: plugins/coding-agent-orchestration-harness/skills/value-documents/SKILL.md, skills/counsel/SKILL.md, skills/counsel/references/first-session.md, skills/orchestration-harness/references/value-audit-mandate.md, skills/orchestration-harness/references/value-level-operation.md, docs/coding-agent/plans/active/first-use-in-a-fresh-repository-run.md; after grading: docs/coding-agent/plans/active/first-use-in-a-fresh-repository-readings.md`
  - `Product basis: brief in the product owner's words (brief line 6: "ebigunso owns the harness; no product philosophy and no engineering philosophy exist for this repository"; ratified 2026-10-07 "Yes, go work on it."; the two statements under "Directed after the run was reported ready" each carry his words of 2026-10-08, "Both yes to 1 and 2.", and were committed in 106097c, the start revision, so they are support and not a change in range)`
  - `Not audited: engineering side, no engineering philosophy (common.md pointer line: "Engineering philosophy: none yet")`
  - `Missing inputs: none`
  - `Value documents changed in range: none committed. Working tree: docs/coding-agent/briefs/active/value-level-operation-notes.md is modified and uncommitted (a notes file, not opened, belongs to another initiative). No pointer line changed; both read "none yet" at 106097c and now.`

  Items (five fields):

  - C1 value-documents SKILL.md, "A statement in a brief that is not ready to settle is marked provisional where it stands. In a philosophy the prose stays unmarked: the mark is recorded in its companion, naming the statement." | maps to the brief | cited | brief, Directed after, first statement: "A provisional mark does not stand in a philosophy's prose either; a statement of a philosophy that is not ready to settle is marked provisional in the companion file, with the rest of the metadata." | -
  - C2 value-documents SKILL.md, companion holds "four things ... which statements are marked provisional, each named" | maps to the brief | cited | same statement, "in the companion file, with the rest of the metadata" | -
  - C3 counsel SKILL.md drafting line, "Mark a statement that is not ready to settle as provisional: in a brief where it stands, for a philosophy in its companion, the prose unmarked." | maps to the brief | cited | same statement | -
  - C4 value-audit-mandate.md grade 3, "a philosophy's statement is so marked in its companion, not in its prose" | maps to the brief | cited | same statement; brief, The philosophy as a human document: "The Orchestrator and the Auditor look there" | -
  - C5 value-level-operation.md, "for a philosophy a mark read from its companion" | maps to the brief | cited | same two statements | -
  - C6 counsel SKILL.md new open-time step, "Take your seat on the peer channel where you do not already hold it, `<repository>-counsel` by convention, whether or not the line below is there." | maps to the brief | cited | brief, Directed after, second statement: "At open, a Counsel session takes its seat on the peer channel where it does not already hold it, whether or not the Counsel line is present."; brief, The peer channel: "the Counsel text says so and names the convention". The two one-time lines ("if it is there, nothing more"; "If it is absent, read `references/first-session.md`") are unchanged in the diff, so the pass condition on the one-time procedure's word count is not loosened. | -
  - C7 first-session.md opening sentence, "does nothing beyond the open-time steps" (Orchestrator ruling, logged in the changes file) | maps to the brief | cited | second statement, as C6 | judgement call; not direction
  - C8 first-session.md, The seat: the seat "is taken at open by the step in the skill's open-time steps"; "Before the first relay" and "Take it by the channel's own means. Where the runtime claims the seat for Counsel when the session starts, there is nothing to do" dropped (Worker judgement call) | maps to the brief | cited | second statement, "where it does not already hold it", which covers a seat a runtime already claimed. Departure from the means (brief, One-time setup, sub-bullet: "the first-session reference says so for such runtimes") noted: no adapter in the plugin claims a seat from a hook (grep of claude/agents, agents/, scripts: none), so the dropped sentence described a mechanism that does not exist. | judgement call; not direction
  - C9 Worker judgement call: the old-form line ("A philosophy ratified before companions existed, with its ratification record and tags inside it, is read as ratified until Counsel moves its record into a companion") not extended to in-prose provisional marks | maps to the brief | inferred | extends the first statement and value-documents' old-form line. Cheap to undo (text). It does not loosen a stop: the provisional report to Counsel is an input, not a gate (value-level-operation: "Sending a report adds no gate and removes none"). Consequence: for a philosophy in the old form, which the owner's two real philosophies under 0.30.0 are, an in-prose provisional mark is one no reader now reads, until Counsel moves the record into a companion. | not direction; see Findings
  - C10 Worker judgement call: the seat step reads "whether or not the line below is there" | maps to the brief | cited | second statement, "whether or not the Counsel line is present" | judgement call; not direction
  - C11 Orchestrator's call: small, no plan, one Worker for both changes, one review, one audit | internal to the run's procedure, not a change to the product | not graded as a product item; the irreversible-or-outward-facing test passes (text in a branch, nothing published) | - | -
  - C12 run record: changes-file pointer added; two unit rows "in progress" | the run's own record, not a product change | not graded as a product item | - | -
  - W1 untracked in the working tree, not part of either change: `docs/coding-agent/plans/active/process-principles-in-the-plugin-plan.md`, `-run.md`, `-readings.md` (another run's drafts; commit c018e7f removed them from the index; the readings file was not opened), `.claude/pr67body.tmp`, `.claude/settings.local.json` | outside both statements; nothing ships them while untracked | not graded as a product item; named so the Orchestrator keeps them out of this stack | - | -

  - `Human-only conditions pending: "scenarios 2 and 3 in his next real use; whether the reference improved a philosophy's quality without shaping the discussion"`
  - `Scenarios: 1 demonstrated (prior state demonstrated; observe in the completed plan's Progress Log, fixture steps 1 to 3; the seat step added by the second statement was not shown on a fixture, and the scenario's clause "does nothing more at open" is superseded by that statement, which the owner ratified knowing it); 2 ready for the owner's judgement (unchanged); 3 ready for the owner's judgement (unchanged); 4 not yet (unchanged); getting closer: yes, because the range closes the two gaps the last closeout left open (the residual on the seat carried to the owner, and the provisional-mark form kept for all four documents) by text the owner directed, and no scenario moved backward.`

  Observations for the Orchestrator (no stop owed):
  - Brief wording now reads against the second statement in two places: One-time setup, "if it is present, nothing more", and Core scenario 1, "does nothing more at open". The later ratified statement decides it; Counsel may wish to amend those words at the next discussion so the brief does not say two things.
  - Validation evidence checked independently: `validate_harness_package.py` passed, `run_validation_smoke_tests.py` passed, `git diff --check` over the range clean.
  - The uncommitted modification to `value-level-operation-notes.md` and the untracked other-run files (W1) sit in the working tree; keep them out of this run's commits and stack.

  How the Orchestrator applied it: no item is `ask-now` and none is `ungraded`; nothing is marked `direction`; the verdict holds nothing, so both changes close. The comparison's `Findings compared:` line gives one finding as bearing on the design and not recorded, C9: for a philosophy in the old form (the owner's two real ones), an in-prose provisional mark is read by no reader until Counsel moves the record into a companion. As `references/value-level-operation.md` states for such a line, the finding is escalated to the owner through Counsel as a value question and the part it concerns is held: the old-form line's treatment of a provisional mark, which neither change touched and nothing built here rests on. Recorded under Findings in the readings file. The rest proceeds: the push onto PR #83's successor, #84, and the report that the run is ready again. The auditor's observation that the brief now says two things on "nothing more" at open goes to Counsel. The other run's untracked draft files stay out of this stack (c018e7f took them back out of the index).
- Closed 2026-10-08, both changes: built on top of the stack's last branch with no branch or pull request of their own; pushed onto PR #84, its text brought up to date; the run reported ready again; one value question with Counsel.

## Small change 3: the old-form reading of a philosophy is dropped

- The owner's answer to the value question of 2026-10-08 on in-prose provisional marks in an old-form philosophy, relayed by Counsel (admitted by the standing approval of 2026-10-01), quoted in full: "This case doesn't need to be explicitly mentioned. Old form philosophies currently doesn't exist anywhere and it never will," Counsel's fact beside it, not his word: his two real philosophies are prose with their provenance in notes files beside them, not the tagged in-document form. The part held for the finding is released.
- Where the statement stands: his words answer a value question; the brief carries no statement on the old form, and the run's own planner-added requirement 2 (old-form philosophies read as ratified until moved) was the run's addition. The Orchestrator reads his words as directing that the addition go: a small change under the brief, graded against his words and the brief's "A philosophy is pure prose" statement.
- Starts from revision: 876bee4.
- The Orchestrator's call: small, no plan; the removal of one reading from four texts (value-documents, the mandate's inputs and Missing inputs, value-level-operation's Documents step, setup's detection), with no how-choice.
- Worker report (one task, `done`, one YAML block, four files): the old-form reading removed from value-documents, the mandate (inputs, Missing inputs, the support sentence now "the brief, or for a philosophy its companion"), value-level-operation's Documents step and setup's detection; a philosophy's ratification is read from its companion only. Worker validation: package validator pass, smoke tests pass, `git diff --check` clean, template block byte-identical, grep finds no trace.
- Review (Codex reviewer, at 4d3cb63): APPROVED, no finding.
- Closing audit, dispatch text (to a fresh Auditor dispatch on Fable):

  ```text
  You are the value auditor. Read references/value-audit-mandate.md of the orchestration-harness skill and follow it exactly. Position: closeout. Plan: docs/coding-agent/plans/active/first-use-in-a-fresh-repository-changes.md. Governing brief: docs/coding-agent/briefs/active/first-use-in-a-fresh-repository-brief.md. Changes since: 876bee4.
  ```
