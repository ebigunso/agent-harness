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

## Findings

- None yet.
