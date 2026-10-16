# Readings: Counsel's questions while drafting, and research before a plan

Written by the Orchestrator for the value audit to compare after its grades are fixed. Not read by an auditor before grading.

## Readings

### `counsel-questions-and-planning-research-plan.md`, plan draft

Item | reading | statement relied on

- DoD 1 (the framing test and the conflict rule, in "How a conversation goes") | covered | brief, issue 90 section, first and second gives-statements
- DoD 2 (ratification on framings; L54 and L56 reworded; tags stay) | covered | brief, third gives-statement and the means
- DoD 3 (unassisted path as default, backup named once) | covered | brief, fourth gives-statement
- DoD 4 (no rule file; value-documents definitions agree) | covered | brief, constraint of the issue 90 section; the means ("the tags stay in the brief for the audit")
- DoD 5 (the gate says what the research is for and when enough) | covered | brief, issue 86 section, first gives-statement; means: the gate is built on
- DoD 6 (the unknown's form; the research task's three statements) | covered | brief, issue 86 section, second gives-statement and the constraint
- DoD 7 (plan review flags the postponing task, not the legitimate one) | covered | brief, third gives-statement and the constraint
- DoD 8 (scenarios 3 and 4 on a fixture) | covered | brief, pass conditions, agent-checkable
- DoD 9 (version 1.0 as the last change) | covered | brief, Version
- DoD 10 (validators; review; reported ready) | covered as mechanics
- Planner-added 1 (control plan with a legitimate research task) | extends | brief, constraint of the issue 86 section (what the check must not flag)
- A1 (`1.0.0`; the marketplace plugin entries included) | extends | brief, Version: "becomes 1.0"; the entries state the plugin's version
- A2 (the closeout list of inferred lines is the lever replaced; the audit's marked-items list is not) | covered | brief, the means of the issue 90 section
- A3 (a record on the framing test if the admission test passes) | covered as mechanics | orchestrator rules; adr.md
- Non-goals (issues 87 to 89; the both-ways line) | covered | brief, Limits and Left out on purpose
- Design (tighten in place, no new reference) | covered | brief, the constraint "live in the Counsel skill" and the means "the gate is the place it builds on"

#### The audit's comparison, plan draft (2026-10-15), as returned

- Reading compared: DoD 1 agrees; DoD 2 agrees; DoD 3 agrees; DoD 4 diverges (Orchestrator: covered on the constraint and the means; audit: inferred, since no brief statement names the value-documents skill and the edit extends the gives and the means); DoD 5 agrees; DoD 6 agrees; DoD 7 agrees; DoD 8 agrees; DoD 9 agrees; DoD 10 diverges (Orchestrator: "covered as mechanics"; audit: cited on the publish standing approval, the item being outward-facing); Planner-added 1 diverges (Orchestrator: extends; audit: cited on the constraint, which the check enforces); A1 agrees; A2 diverges (Orchestrator: covered by the means; audit: inferred, the means does not name which closeout list); A3 diverges (Orchestrator: covered as mechanics on orchestrator rules and adr.md; audit: not audited, engineering side with no document); Non-goals 87-89 and the both-ways line agree; Non-goal rule files unread; Non-goal fixed audit dispatch template unread; Non-goal validators for prose unread; Non-goal run-time test unread; Non-goal ADR-D-0042 list unread; Task_1 unread; Task_2 unread; Task_3 unread; Task_4 unread; Decision Log entry unread. (The Orchestrator's "Design" line is not an item under this mandate and is not compared.)
- Findings compared: none found (the Findings section is empty; no departure from a means was noted on any item line)

Readings corrected after this comparison: the value-documents edit extends the brief, which names no such file; publication rests on the standing approval; the control plan enforces the brief's constraint; the means names no closeout list, so A2 extends it; A3 is engineering-side mechanics with no document.

### `counsel-questions-and-planning-research-plan.md`, plan draft revised (Task_5 added, 2026-10-15)

Written after the audit of the revised plan returned, not before it: the Orchestrator dispatched that audit without writing these, so its comparison reads these items as unread. They are the Orchestrator's readings as they stood at the dispatch, set down afterwards.

Item | reading | statement relied on

- DoD 1 as amended (the test applies any time Counsel puts a question to the owner; reserved acts reach the owner regardless) | covered | brief, issue 90 section, second gives-statement (amendment of 2026-10-15, the owner's words)
- Non-goal: the level test of what reaches the owner from a run stays, the framing test beside it | covered | the amendment's reserved-acts clause, marked as Counsel's reading
- Task_5 (the test governs every question; "Contacts with a run" points to it; ADR-D-0059 revised in place; ADR-D-0060's dependency follows) | covered | the amendment
- Decision Log: the owner's answer read as a change to the design; Task_5 added | covered | the amendment; Replan Procedure as mechanics
- Decision Log: ADR-D-0060 accepted; the ruling on kind marks told to the owner | extends | brief, third gives-statement and the means (the brief stays the record, the tags stay); the kind marks are not named by any statement

#### The audit's comparison, plan draft revised (2026-10-15), as returned

- Reading compared: the readings file carries one heading for this plan at plan draft (the first draft's readings, with the first audit's comparison and a correction line beneath); no readings were written for the revised plan. DoD 1 agrees; DoD 2 agrees; DoD 3 agrees; DoD 4 diverges (Orchestrator: covered on the constraint and the means; audit: inferred, no brief statement names the value-documents skill) though the correction line below the table concedes it extends; DoD 5 agrees; DoD 6 agrees; DoD 7 agrees; DoD 8 agrees; DoD 9 agrees; DoD 10 diverges (Orchestrator: "covered as mechanics"; audit: cited on the publish standing approval, the item being outward-facing), correction line concedes; Planner-added 1 diverges (Orchestrator: extends; audit: cited on the constraint), correction line concedes; A1 agrees; A2 diverges (Orchestrator: covered by the means; audit: inferred, the means names no closeout list), correction line concedes; A3 diverges (Orchestrator: covered as mechanics on orchestrator rules and adr.md; audit: not audited, engineering side with no document), correction line concedes; Non-goal issues 87-89 agrees; Non-goal both-ways line agrees; Non-goal rule files unread; Non-goal fixed audit dispatch template unread; Non-goal validators for prose unread; Non-goal level test stays unread; Non-goal ADR-D-0042 list unread; Task_1 unread; Task_2 unread; Task_3 unread; Task_4 unread; Task_5 unread; Decision Log relays admitted unread; Decision Log ADR-D-0059 proposal unread; Decision Log ADR-D-0060 proposal unread; Decision Log owner's answer and replan unread; Decision Log ADR-D-0060 accepted and the kind-marks ruling unread. (The "Design" line is not an item under this mandate and is not compared.)
- Findings compared: none found (the Findings section is empty; no departure from a means was noted on any item line)

Readings compared after this comparison: the audit grades the kind-marks ruling inferred and marks it direction, which the Orchestrator's "extends" reading agrees with in class; the owner sees it at closeout.

### `counsel-questions-and-planning-research-plan.md`, closeout (changes since 25f9831)

Written while the closeout audit was running, before its verdict returned.

Item | reading | statement relied on

- Counsel skill: the framing test at any question to the owner, drafting-time handling, conflict rule, reserved acts regardless (L29); run-contact clause pointing to it (L76) | covered | brief, issue 90, first and second gives-statements and the conflict gives-statement
- Counsel skill: ratification on framings; partial yes and closeout list reworded; unassisted default (L51, L56, L57, L59) | covered | brief, issue 90, third and fourth gives-statements and the means
- Value-documents skill: tag definitions and what ratification covers (L53, L65) | extends | brief, issue 90 means ("the tags stay in the brief for the audit"); the skill is not named
- Research Dispatch Gate, lifecycle-gates steps 4 and 5, dispatch-guidance, plan-format rule 10, template Assumptions line | covered | brief, issue 86, gives-statements, constraint and means
- Plan-review snippet check (prompt-snippets L75) | covered | brief, issue 86, third gives-statement and the constraint
- Orchestrator adapters, one line each | covered | brief, issue 86 means (the gate is built on)
- ADR-D-0059 (proposed, any time) | covered | brief, issue 90 amendment; returns to the owner by name
- ADR-D-0060 (accepted) and its post-acceptance wording change on ADR-D-0059's scope | covered as mechanics | the owner's acceptance; adr.md Reworded after acceptance
- Version 1.0.0 in five lines | covered | brief, Version
- Fixture outcomes, scenarios 3 and 4 and the control (Progress Log) | covered | brief, pass conditions
- Lessons entries (three) | covered as mechanics | orchestrator rules (lessons are repository working guidance)
- The ruling that kind marks are ratified with the brief on its framings | extends | brief, third gives-statement and the means; marked direction by the plan-draft audit

#### The audit's comparison, closeout (2026-10-15), as returned

- Reading compared:
- Counsel L29 test, drafting-time handling and conflict rule: agrees (covered / cited).
- Counsel L29 reserved-acts sentence: diverges. Orchestrator: covered on the issue 90 gives-statements. Audit: inferred, because the brief's reserved-acts clause carries no ratification and the sentence extends the owner's L21 words.
- Counsel L76: agrees.
- Counsel L51, L56, L57, L59: agree.
- value-documents L53 and L65: agree (extends / inferred); the audit adds the direction mark on L65.
- Gate, lifecycle-gates item 4, dispatch-guidance, rule 10, template: agree.
- lifecycle-gates item 5: diverges. Orchestrator: covered. Audit: inferred, because "only when" makes L33's cases an exclusive list.
- Plan-review snippet check: agrees.
- Adapters: agree.
- ADR-D-0059: agrees.
- ADR-D-0060 accepted: diverges. Orchestrator: covered as mechanics. Audit: cited on L23 and L26, with the acceptance carried under the relay entry.
- ADR-D-0060 wording after acceptance: diverges. Orchestrator: covered as mechanics. Audit: not audited, the changed words named.
- Version `1.0.0`: agrees.
- Version ordering: unread.
- Fixture outcomes: the control rewrite agrees. The scenario 3 dispatch rewording diverges: Orchestrator covered, audit inferred, because the wording points the agent at the gate.
- Lessons entries: diverges. Orchestrator: covered as mechanics on orchestrator rules. Audit: not audited, the engineering side having no document.
- Kind-marks ruling: agrees (extends / inferred, direction).
- Plan items (DoD 1-10, Planner-added 1, the non-goals, A1-A3, Task_1-Task_5, Decision Log entries) and the remaining judgement calls (snippet repetition, adapter length, the ADR split, the W1-F1 gloss, the L54 compatibility ruling, R-F1, FINAL-F1, the verdicts-count and re-dispatch rulings): unread under the closeout heading.
- Findings compared: none found. The Findings section is empty, and no item line notes a departure from a means.

Readings corrected after this comparison: the reserved-acts sentence extends the owner's words (the brief's clause on it is Counsel's reading, unratified); lifecycle-gates item 5's "only when" extends the constraint; ADR-D-0060's acceptance rests on the owner's quoted words; its wording after acceptance and the lessons entries are not audited, having no engineering document; the scenario 3 dispatch's rewording extends the pass condition, since it points the agent at the gate.

### `counsel-questions-and-planning-research-changes.md`, small change 1, closeout (changes since cf4d618)

Written before the closing audit was dispatched.

Item | reading | statement relied on

- Counsel SKILL.md L54, a brief's drops and departures as framings at ratification, only where they changed anything, no list | covered | brief, "Directed after the run was reported ready", first statement
- Counsel SKILL.md L54, "if no departure changed anything, say that the brief cannot decide anything" kept | extends | the same statement ("Counsel does not list the statements"): one remark, not a list
- Counsel SKILL.md L54, a philosophy's steps kept in their own sentence | covered as mechanics | the statement concerns a brief; L57 keeps a philosophy's full text
- value-documents SKILL.md L59, a recorded drop ratified with the brief, shown as a framing where it changed anything | extends | the same statement; L65 (ratification covers the whole brief)
- ADR-D-0059 accepted (owner's words relayed 2026-10-15) | covered as mechanics | the owner's acceptance by name
- No decision record for the change | covered as mechanics | ADR-D-0060 already decides ratification on framings

#### The audit's comparison, small change 1 closeout (2026-10-15), as returned

Reading compared: L54 brief framings: agrees (covered / cited). "Cannot decide anything" kept: agrees (extends / inferred; the audit adds the direction mark). Philosophy steps kept: diverges (Orchestrator: covered as mechanics; audit: inferred, a product-side choice about what a ratifier is shown, resting on reading "too" against L23). value-documents L59: diverges (Orchestrator: extends; audit: cited, since the directed statement says exactly what the line now says). ADR-D-0059 accepted: diverges (Orchestrator: covered as mechanics on the owner's acceptance; audit: not audited, engineering side with no document, the acceptance carried by the admitted relay). No decision record: diverges (Orchestrator: covered as mechanics; audit: not audited, no engineering document). Orchestrator ruling keeping the Worker's call: unread. Small, no plan, one task: unread. Branch and pull request 91 text update: unread. Record-keeping lines: unread.
Findings compared: none found (the Findings section is empty, and no item line notes a departure from a means).

Readings corrected after this comparison: keeping a philosophy's steps is a product-side choice of what a ratifier is shown, resting on the statement's "too" read against the brief's framings; the value-documents line says what the statement says; the ADR-D-0059 acceptance and the no-record call are engineering-side mechanics with no document.

## Findings

