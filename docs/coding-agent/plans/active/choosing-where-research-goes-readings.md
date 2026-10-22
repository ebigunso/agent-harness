# Readings: Choosing where research goes

Written by the Orchestrator for the value audit to compare after its grades are fixed. Not read by an auditor before grading.

## Readings

### `choosing-where-research-goes-plan.md`, plan draft

Item | reading | statement relied on

- DoD 1 (the choice rule once, in model-routing.md, read whenever a Researcher is dispatched; other texts point to it) | covered | brief, "What the plugin states", the choice rule (gives) and the pass condition "stated once in the plugin at the place where dispatch is decided"; the home is the reference item 3 names ("as the routing reference already states")
- DoD 2 (Counsel's Researcher is the role on the recorded option, same rule, same record, read before dispatch) | covered | brief, "Counsel follows the same rule from the same record" (gives)
- DoD 3 (the plugin names common.md as the record's place; no plugin text names a seat, peer or model) | covered | brief, the means "lives in the rule file both the Orchestrator and Counsel read"; constraints "never assumes a seat, a peer, or a model" and Limits; pass condition "no plugin text names a seat or a model"
- DoD 4 (a research task goes to the Researcher, never a Worker; plan review flags bundled research, not reading what the task changes) | covered | brief, choice rule item 1; "Plan review flags research bundled inside an implementation task" (gives); scenario 4
- DoD 5 (common.md record: three seats and models, dated observations, cost setting for other roles, research cost notwithstanding, Auditor line; nothing left in orchestrator.md) | covered | brief, "This repository" (gives and means); pass condition on common.md
- DoD 6 (scenarios 1, 3, 4 on a fixture, 5 on replays; 1 and 2 human-only at closeout) | covered | brief, pass conditions (agent-checkable and human-only)
- DoD 7 (version 1.1.0, last) | extends | no brief statement; the installed plugin refreshes only on a version change, so the rule reaches no installed workspace without it
- DoD 8 (validators, review, audits, reported ready, nothing merged) | covered as mechanics | brief: "Nothing merges without his acceptance" (Counsel's hand-over); standing approval of 2026-09-30 for publishing
- Planner-added 1 (the ordinary-reading control at scenario 4) | extends | brief, scenario 4 and the gives-statement on plan review, which asks to flag bundled research, not reading
- Planner-added 2 (scenario 3 on the same fixture) | extends | brief, scenario 3 and the constraint that no seat is assumed
- Planner-added 3 (version 1.1.0, last) | extends | as DoD 7
- Planner-added 4 (the owner's adjudication unlabelled by model) | extends | brief, "never by polish or by agreement with the Orchestrator"; the grades against what he would have decided
- A1 (runtime physical names and platform names are not seats or models) | inferred | brief, Limits: "what a workspace has is only ever read from its own record"; the names are the plugin's own runtime identities, not what a workspace has
- A2 (Counsel passes its observation on; the Orchestrator records it) | covered | counsel SKILL.md L22; common.md Repo Safety; brief item 5 does not say who records
- A3 (the 2026-09-15 observation covers Astra; re-observed for the Auditor by Task_5) | covered | orchestrator.md L25 and L28; brief, "The Auditor's model, compared before it moves"
- Non-goals (session models; cost classes; a default peer route; runtime names; Researcher adapters' descriptions; prose validators) | covered | brief, the Orchestrator and Counsel sessions "are not routed by this brief"; "Left out on purpose"; A1 for the runtime names
- Task_1 (the rule, pointers, Counsel texts, adr-template names, ADR if it passes) | covered | as DoD 1 to 3; the ADR by plan-format rule 11
- Task_2 (plan-review check; lifecycle-gates items 2 and 5) | covered | as DoD 4
- Task_3 (common.md record; orchestrator.md emptied; headless sessions as measurement instruments) | covered | as DoD 5; the brief's constraint that each replay runs "in a fresh subagent session or an ephemeral CLI session"
- Task_4 (fixture probes, reviewer answering the check as its own line) | covered | as DoD 6; lesson 2026-10-15 on controls
- Task_5 (five replays on two models, verbatim template, worktree as working directory, one adjudication over every item, Auditor line) | covered | brief, "The Auditor's model, compared before it moves" (gives and two constraints); the case set from R2; the 2026-10-15 case as availability only (the brief as corrected by Counsel)
- Task_6 (version) | extends | as DoD 7
- Routing line (Workers, reviews, audits; the closeout audit on the model the Auditor line names after Task_5) | covered | brief, "This repository" and "the Auditor moves or stays on that"; orchestrator.md L27 to L29

### `choosing-where-research-goes-plan.md`, plan draft, revision 1 (after the audit held Planner-added 1)

Every item not listed reads as above.

- DoD 4 (plan review flags the brief's own example, a task that says to read the module first and then change it; a task stating only the change is not flagged) | covered | brief, "Plan review flags research bundled inside an implementation task" (gives); scenario 4, its example quoted as the case to flag
- Planner-added 1 (the control: a task stating only the change, no step to read or find out first) | extends | brief, scenario 4; a check that flags every implementation task would show nothing
- Task_2 (the snippet flags a task that reads, investigates or finds out first and then changes; not one stating only the change) | covered | as DoD 4
- Task_4 (the bundled fixture worded in the brief's own words; the control a task stating only the change) | covered | brief, scenario 4; pass condition "scenarios 1, 4 and 5 are shown where one can be made"

### `choosing-where-research-goes-plan.md`, closeout

Every plan item reads as at plan draft, revision 1. The calls made during the run:

- Task_1: the rule's opening widened so the section is read at every Researcher dispatch, not only where models differ | covered | brief, "What the plugin states", the rule read "wherever the Orchestrator or Counsel decides where research goes"
- Task_1: pointers added at the gate, dispatch guidance, subagent-strategy, plan-format and both pairs of adapters, the rule stated once | covered | pass condition "stated once in the plugin at the place where dispatch is decided"
- Task_1: ADR-D-0061 proposed | extends | no brief statement; the admission test; proposal only, acceptance the owner's
- Task_1: adr-template's example model names made neutral | covered | pass condition "no plugin text names a seat or a model"
- Wave 1 ruling: `prompt-budgeting.md`:5 "GPT-Oriented" left as a platform label | covered | A1, as audited (inferred) at plan draft
- Task_2: the plan-review check answered as its own line | covered | brief, "Plan review flags research bundled inside an implementation task"; scenario 4
- Task_3: the record moved into common.md as one section before Standing Approvals, orchestrator.md left without it | covered | brief, "This repository", the means into `common.md`, dated
- Task_4: scenarios 1 and 3 dispatched to a fresh Claude subagent applying the written rule to two fixture workspaces; scenario 4 to the Codex reviewer seat | covered | brief pass condition "shown where one can be made"; scenario 1 on a fixture only as far as one can, human-only for the real run
- Task_5: the decision points for the owner drawn from R3 where sources differ on something that would have stopped work, reached him or changed what was built, the agreement blocks confirmed together | covered | brief, "adjudicated by him once"; the grades against what he would have decided
- Task_5: the key read as Counsel's answers as put to him, which he took ("your takes on each seems like the reasonable decision for the most part"), S1-d with his lean recorded | covered | his words as relayed, 2026-10-23
- Task_5: the first Fable set re-run in a clean context after the review found extra context; Astra kept, its setup already meeting the corrected construction | covered as mechanics | the plan's construction-defect rule (PR-F6); brief, "fresh subagent session or ephemeral CLI session"
- Task_5: Fable's outcome weighed on the kind of miss: an invented stop halts a run and reaches the owner, a read-order departure that opened no barred input changes no grade | extends | brief, the measures listed without weights; the owner's adjudication
- Task_5: the Auditor stays on Fable, recorded in common.md dated 2026-10-23 | covered | brief, "the Auditor moves or stays on that"
- Task_6: seven version fields in five files | covered | as DoD 7
- Run record scenario states left at the last audit-stated state | covered as mechanics | completion-closeout.md, the run record

### Closeout audit, 2026-10-23: the verdict's comparison lines, as returned

- Reading compared: `model-routing.md` rule and widened opening agrees; item 5's writer (A2) diverges (covered on non-value documents; audit: inferred); pointers in the gate, dispatch guidance, subagent-strategy, plan-format and both adapter pairs agrees; Counsel texts agrees; plan-review check agrees; the control (Planner-added 1) agrees; adr-template names agrees; `common.md` record (Task_3) agrees; handshake clause unread (audit: inferred); measurement-instrument line agrees; Auditor line agrees on the statement, the audit adding the case-set hold; `orchestrator.md` emptied agrees; ADR-D-0061 proposed agrees (extends; audit: inferred on the call, cited on the file); version (Task_6, DoD 7) agrees; comparison record agrees; Task_5 case set, the 2026-10-15 case as availability only, diverges (Orchestrator: covered by "the brief as corrected by Counsel"; audit: ask-now, the corrected clause carries no ratification record and the ratified words name the case); Wave 1 ruling on `prompt-budgeting.md` agrees; Task_4 ruling agrees; researcher seat compiling R3 unread (audit: cited); the decision points sent through Counsel agrees; the key read as Counsel's answers diverges (covered on his words; audit: inferred, "for the most part"); first Fable set re-run, Astra kept diverges in kind (covered as mechanics; audit: inferred, user-facing through the recorded outcome); elevated-sandbox stop unread (audit: cited); S3 adjusted unread (audit: inferred); outcome weighed by kind of miss agrees; A1-Astra read-order correction unread (audit: cited); run record states diverges in kind (covered as mechanics; audit: not audited); DoD 8 diverges (covered as mechanics, partly on Counsel's hand-over; audit: cited on the standing approval alone); the plan items as at revision 1 agree where they agreed then (DoD 8, Planner-added 2, A2, runtime names, adapter descriptions, prose validators diverging as logged at 2026-10-22).
- Findings compared: Fable's one-batch read of the plan and brief with the mandate, recorded as trivial: agrees (it changes nothing anyone experiences from the feature; no barred input opened, no grade rests on it; inferred, under the outcome-weighing call). Astra's holds on the closeout note to Counsel, recorded as trivial: agrees (the Auditor stays on Fable, so no audit the owner sees reads that way; cited under the outcome). Departures from a means: none noted on any item line (the record moved into `common.md` as the means states), so nothing further to compare.

## Findings

- Fable, in every replay, opened the plan and the brief in one batch with the mandate, which today's mandate's First Step forbids; no barred input was opened and no grade rests on it | trivial: it changes nothing anyone experiences while the void rule covers the readings and notes
- Astra held the closeout note to Counsel for approval in two cases, reading the standing approvals as not covering it | trivial: the Auditor stays on Fable, so no audit the owner sees reads this way
