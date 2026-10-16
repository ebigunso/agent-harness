# Readings: Value-level operation of the harness

Written by the Orchestrator for the value audit to compare after its grades are fixed. Not read by an auditor before grading. Created 2026-10-06 with the run's first small change.

## Readings

### Small change 1 (the Copilot comments of the stack), closeout

Item | reading | statement relied on

- The assessment: 30 addressed, 16 declined, 2 declined against the triage, 3 to Counsel, 15 fixed (16 lines) | covered | brief: "checked and assessed; those that need a fix are applied, the rest not"
- Fix 1, a philosophy amendment quoted from whoever ratifies the document (value-documents, value-level-operation, counsel, three Counsel lines) | covered | brief, Roles and sessions: only the product owner writes or amends a product philosophy; mechanics of the existing authority
- Fix 2, the Orchestrator role entered by an opened session, the managed loader or explicit invocation | covered | ADR-D-0037 as accepted; the brief's "Roles and sessions"
- Fixes 3, 6, 8 (records' Validation and Not covered wording) | covered as mechanics; wording that changes no decision (the reviewer's and the Orchestrator's reading)
- Fixes 4, 5, 7, 9, the rule file's push line and date, goal-mode's one sentence | covered as mechanics; no statement needed
- The declines against the triage (the closed plan's A1 and its audit range) | extends | brief: "the rest not"; ADR-D-0051: a closed unit is not reopened
- The routing of three comments to Counsel | covered | the brief is Counsel's document; "the Orchestrator and its subagents never edit a philosophy or a brief"
- The Orchestrator's call: small, no plan | covered | small-change brief: "The Orchestrator chooses, per change"; the fixes each specified, no open how-choice
- ADR-D-0020's broader wording left as an observation | extends | brief: "the rest not"; a record's decision is the owner's
- Scenario: the brief states no numbered scenarios; nothing to move.

#### The audit's comparison, small change 1 closeout (2026-10-06), as returned

- `Reading compared:` the assessment: agrees (covered / cited); fix 1: agrees; fix 2: agrees; fixes 3, 6, 8 (the records' wording): diverges, Orchestrator "covered as mechanics", auditor "not audited" as decision records changed after acceptance that did not alter the decision (items 10 to 13); fixes 4, 5, 7, 9 and the rule-file line and goal-mode sentence: agrees on the grade (covered / cited), though the auditor places the Counsel contact line, the goal-mode sentence and the push rule on the product side, not as mechanics; the declines against the triage: diverges, Orchestrator "extends", auditor "cited" on the brief's "the rest not"; the routing to Counsel: agrees; the call small, no plan: agrees (the Orchestrator relied on the small-change brief, which does not govern this run; the auditor cites this brief's "How is the Orchestrator's"); ADR-D-0020 left as an observation: diverges, Orchestrator "extends", auditor "cited" on "Each decision record is still accepted on its own"; unread: the closed middle-size plan's DoD edit (item 14), the setup run record's Scenarios cells (item 15), the planned push and PR body edits (item 17), the run record and changes file (item 16), the three Worker judgement calls (items 26 to 28)
- `Findings compared:` none recorded ("None yet"); departures noted on item lines: item 15 (Orchestrator words in audit-stated cells) changes nothing anyone experiences, agrees, cited; item 14 (closed plan edited while two other closed-record comments were declined as not reopened) changes nothing anyone experiences, agrees, cited

Readings corrected after this comparison: the records' wording changes are decision records changed after acceptance, not mechanics; the declines and the ADR-D-0020 observation rest on this brief's "the rest not" and "Each decision record is still accepted on its own"; the small-change call rests on this brief's "How is the Orchestrator's", not on the small-change brief, which does not govern this run.

### Directed change: a standing approval for rebasing unmerged pull requests, closeout

Item | reading | statement relied on

- The common.md entry: unmerged pull requests' branches may be rebased and force-pushed without asking first; merges not covered | covered | brief, "Directed while the stack was open for his judgement", last statement: "The branches of unmerged pull requests may be rebased and force-pushed without asking him; they are not final until merged. A standing approval records it."; "Merges are not covered" repeats the first entry, and "Delivery and judgement" keeps merging on his acceptance
- The entry's acceptance taken in the Orchestrator session ("Accept the entry"), since the relayed words grant the approval but do not accept an entry's wording | covered | common.md, Standing Approvals: an entry is in effect only once it records the giver's acceptance of the entry, quoted with the date, and is committed
- The Orchestrator writing the entry itself | not a product item | only the Orchestrator edits rule files (common.md, Repo Safety / Boundaries)
- `last_updated` moved | not a product item | the rule suite's metadata
- Scenarios expected: none of the run's scenarios is touched; getting closer: unchanged

#### The audit's comparison, standing-approval entry closeout (2026-10-15), as returned

- `Reading compared:` item 1 (the entry's content): agrees (covered / cited, same statement); item 2 (the acceptance taken in the Orchestrator session): diverges, Orchestrator "covered" on common.md's Standing Approvals paragraph (an ordinary rule, which is not support for a product-side item and does not speak to the route), auditor "ask-now" on brief lines 52 and 123 (the entry reaches him through Counsel with a link; an Orchestrator-session ruling is unratified); item 10 (the Orchestrator writing the entry): diverges on class, Orchestrator "not a product item" on a common.md rule, auditor "cited" on brief lines 49 and 193 (no stop either way); item 3 (`last_updated`): agrees (not a product item / not audited); unread: item 5 (C6 closed in the first-use changes file), item 6 (first-use run record), item 7 (readings file), item 8 (untracked files), item 9 (a push, if any), rulings 12, 13, 14. On scenarios: Orchestrator "getting closer: unchanged", auditor "yes" with the reason above.
- `Findings compared:` none found (the Findings section reads "None yet"; no means statement bears on this change, so no departure from a means is noted on any item line)

Readings corrected after this comparison: the route by which a standing approval takes effect is the brief's (through Counsel, with a link to the file), not the rule section's form alone; an acceptance in the Orchestrator session does not meet it.

### Small change 2: the codebase checked for leftovers and clean-up candidates, closeout

Item | reading | statement relied on

- The sweep of the whole tracked tree, split in two, read-only | covered | brief, "Directed while the stack was open for his judgement", last statement: "Before the stack is merged, the codebase is checked for leftovers and clean-up candidates that should be deleted or handled, and they are dealt with, so that the stack can be called clean and done."
- Each candidate judged by the Orchestrator against his standing words (evidence removed once its claim is recorded; nothing kept because deleting felt wrong; additions carry their reason) | covered | the same statement; Counsel's relay of 2026-10-16: what is a leftover is the Orchestrator's to judge against his standing words
- Taken: the plugin README's pointer to `docs/` paths absent from the package (A1) | covered | the statement; common.md, Boundaries: content under `plugins/` carries no references to `docs/` paths absent from the plugin package
- Taken: stale paths, status lines and metadata corrected (D1 to D4, D6, D7, D9, D16) | covered | the statement ("handled")
- Taken: orchestrator.md's interim sentence for an installed plugin without the Auditor agent dropped (D8) | covered | the statement; the sentence's own condition no longer holds once the stack ships the Auditor agent
- Taken: lessons whose every prevention line is held by a rule or skill removed with a drain note (D10, D13; ten after SC2-F1), a lesson cut to the part that still holds (D11), the Tags header matched (D14) | covered | the statement; lessons.md's own drain convention ("Promotion drain note (2026-07-23)")
- Taken: three raw survey, triage and audit outputs deleted, their citing plans naming the commit that last holds each (D15) | covered | his standing words: evidence is removed once its claim is recorded
- Not taken: A2 (bytecode in ignored folders), D17 (a run record's note that a fixture may not persist) | covered | the statement asks for leftovers in the codebase; neither is one
- Not taken: five open candidate blocks in lessons.md (three repository rule candidates, one harness migration candidate, the 2026-10-01 one whose prevention has no full home) | covered | each carries its reason; promoting a rule is not a clean-up; they reach him in the ready note, through Counsel, so he can say if he wants them handled now
- Deferred to the merge step: D5 and the moves of three briefs of runs whose records are completed | covered | plan-format: a finished plan moves to `plans/completed/`; brief, "Delivery and judgement": merging waits for his acceptance, so the move is done with it
- The rule-file items built by the Orchestrator, the rest by a Worker | not a product item | only the Orchestrator edits rule files (common.md, Boundaries); a Worker for the rest (lessons.md, 2026-10-15)
- Two lessons recorded (every prevention sentence has a home; the validator writes bytecode) | not a product item | lessons.md, How to use
- Scenarios expected: none of the run's scenarios is touched; getting closer: yes, the stack can be judged clean, which is what he asked before giving the go-ahead to merge

#### The audit's comparison, small change 2 closeout (2026-10-16), as returned

- `Reading compared:` the sweep (item 18): agrees (covered / cited, same statement); each candidate judged against "his standing words" (item 19): agrees on the grade, diverges on the basis, Orchestrator "covered" on the statement plus Counsel's relay about his standing words, auditor "cited" on brief lines 194 and 8 alone, the standing words being in no document the dispatch names; A1 (item 1): agrees (the Orchestrator adds common.md's boundary rule, which is read to understand and is not support for a product-side item); stale paths, status lines, metadata (items 3, 4, 5, 6, 7, 12): agrees on cited for items 3, 4, 5, 7, 12, diverges on class for item 6, Orchestrator "covered" as a handled path, auditor "not audited" as decision records (superseded) changed after acceptance without altering the decision; D8 (item 2): agrees; the lessons drain, D11 and D14 (items 8, 9, 7): agrees (the Orchestrator's second source, the log's own drain convention, is a repository file and not support; the grade rests on the brief); D15 (item 11): diverges on the basis, Orchestrator "covered" on "his standing words: evidence is removed once its claim is recorded", auditor "cited" on brief line 194 ("deleted"); A2 and D17 not taken (item 20): agrees; the five open candidate blocks (item 21): agrees (the Orchestrator reads "they reach him in the ready note, through Counsel"; auditor adds brief line 168); deferred to the merge step (item 28): agrees on cited, diverges on the statement, Orchestrator plan-format and "Delivery and judgement", auditor brief line 96 (a brief moves on his acceptance of its final stack), with the condition noted on the item; rule-file items by the Orchestrator, the rest by a Worker (item 25): diverges on class, Orchestrator "not a product item", auditor "cited" on brief line 8 (no stop either way); the two lessons recorded (item 10): diverges on class, Orchestrator "not a product item" on lessons.md's How to use, auditor "cited" on brief line 8 (no stop either way); unread: items 13, 14, 15, 16, 17 (the changes file, readings file, notes file, untracked files, a push if any), rulings 22 (D12 corrected), 23 (D16 rest), 24 (SC2-F1), 26 (open product choices to Counsel), 27 (D18), Worker calls 29 and 30. On scenarios: agrees (Orchestrator "getting closer: yes, the stack can be judged clean", auditor "yes" with the reason above).
- `Findings compared:` none found (the Findings section reads "None yet"; no means statement bears on this change, so no departure from a means is noted on any item line)

Readings corrected after this comparison: "his standing words" are in no document the audit is given, so a reading resting on them rests on the brief's statement and "How is the Orchestrator's"; a superseded decision record's link repair is a decision record changed after acceptance, not a handled path.

## Findings

- None yet.
