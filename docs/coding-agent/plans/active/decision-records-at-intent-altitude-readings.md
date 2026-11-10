# Readings: Decision records at intent altitude

The Orchestrator's readings, each written before the audit dispatch it is compared with, and the findings of the run. The Auditor opens this file only after its grades are fixed.

## Readings

### The raised plan (decision-records-at-intent-altitude-raised-plan.md), plan draft

Item | reading | statement relied on

- A proposed record replaces ADR-D-0016 with the surface split for an unverifiable consumer; it reaches him by name | covered for the decision (brief, the answers' section, the first answer); extends for reaching him by name, which the section's sentence tagged inferred says and his direction on rewrites supports (a change to what a decision says is not an unread rewrite)
- A proposed record replaces ADR-D-0020 without the overtaken sentence, agreeing with ADR-D-0037; its procedure left to the plugin's text and confirmed there | covered | the second answer, and the brief's statement that exact mechanics are not covered and operational material is placed in the text that already states it
- If nothing of ADR-D-0020 is left as a decision of its own, no record is written and its retirement returns to him | extends | the brief's scenario 3 and its constraint that the decisions do not change
- The checker does not fail on the snippet's wording, its heading included, and warns at most | covered | the third answer
- ADR-I-0007 unchanged by this plan; its own check against the standard waits for its batch | extends | the run's ordering, his direction that the raised decisions come first
- Nothing retired before acceptance; references repaired at acceptance | covered | the brief ("a new complete record, the old one retired, accepted by name")
- Planner-added: the warning kept in place of the failure | extends | the third answer sets an upper bound ("it warns at most") and does not ask for a warning; keeping one is the plan's choice
- Planner-added: ADR-D-0020's procedure confirmed present in the plugin's text | covered | the brief (operational material is placed in the rule or skill text that already states it)
- Planner-added: the version | extends | the work reaching whoever installs the plugin
- Design: keeping the topics as a warning, against removing the check | not audited | internal mechanics; no engineering philosophy
- Compatibility: break, for one checker behaviour | extends | the third answer
- The run's layout: five units by area, each its own pull request | covered | his direction of 2026-11-11 (the raised decisions first, then batches by area of about ten)
- Built by a writing Worker and a coding Worker with the review seat; published as a branch and a pull request when ready; no merge | covered for publication (common.md Standing Approvals); not audited for the rest

### The raised plan (decision-records-at-intent-altitude-raised-plan.md), plan draft, 2026-11-10 by the channel clock: the verdict's comparison lines, as returned

- Reading compared: ADR-D-0016 record, the decision: agrees (covered / cited). ADR-D-0016 record, reaching him by name: diverges. Orchestrator: extends, on the answers' section's inferred sentence and his direction on rewrites. Auditor: cited, on Limits "Acceptance is by name, as the standard says"; the inferred sentence is no support and is not needed. ADR-D-0020 record: agrees. No record written if nothing of ADR-D-0020 survives: diverges. Orchestrator: extends, on scenario 3 and the constraint. Auditor: cited, on the constraint's own words and scenario 4. The checker, heading included: agrees. ADR-I-0007 unchanged, its own check waiting for its batch: diverges. Orchestrator: extends. Auditor: cited ("the record stands"; the batches statement). Nothing retired before acceptance: agrees. Planner-added, the warning kept: diverges. Orchestrator: extends (the bound does not ask for a warning). Auditor: cited (a warning sits inside "warns at most"). Planner-added, the procedure confirmed present: agrees. Planner-added, the version: agrees (extends / inferred). Design, the topics kept as a warning against removing the check: no separate item, since the mandate's item list has none for the Design section. Its internal part (a second place that knows the topics) is not audited, which agrees; its observable part is the planner-added warning item above. Compatibility, break for one checker behaviour: diverges. Orchestrator: extends. Auditor: cited under the checker item; the third answer itself turns the failure into a warning at most. The run's layout: agrees. Built, published, no merge: agrees (the standing approval for publication; not audited for the rest). Unread by the Orchestrator: the DoD entry that the decisions do not change and no other checker behaviour changes; the non-goal on the standard and its template; the assumption; Decision Log RAI-P3; the Decision Log note on recounting an area.
- Findings compared: none found (the readings file records no findings, and no item line notes a departure from a means).

### The raised plan (decision-records-at-intent-altitude-raised-plan.md), closeout

Item | reading | statement relied on

- ADR-D-0071, proposed, replaces ADR-D-0016: a protection needs a consumer that can be shown; where one cannot be verified, the question goes to the person directing the work only for a surface that crosses the repository's boundary, and inside the repository the change goes ahead and is reported | covered | brief, "The three raised decisions, answered 2026-11-11", the first answer
- Everything else ADR-D-0016 decided is kept, and what was only mechanics is left to the plugin's text that states it | covered | the brief ("The decisions themselves do not change"; exact mechanics not covered)
- ADR-D-0071 kept as one record, the unverifiable case read as the edge of the evidence requirement | extends | the brief's one-decision test; the reading is the run's and the review's
- ADR-D-0071's rejected all-cases alternative carries a reopen condition the run derived from its reason; two alternatives the old records left without a disposition are written as rejected outright; its Revisit When says the old record names no models checked | extends | the brief (the standard's form); none is his statement, and each is shown to him with the record
- ADR-D-0072, proposed, replaces ADR-D-0020: a session routed by the installed loader holds the Orchestrator role; the overtaken sentence is gone; the rule-load procedure is left to the plugin's text, which states it | covered | the second answer; the brief on operational material
- A decision of ADR-D-0020's own survives beside ADR-D-0037, which leaves the loader route to it | covered | the second answer ("The old sentence is corrected in the rewrite")
- Both records reach him by name; neither old record is retired or changed | covered | Limits (acceptance by name); the brief ("a new complete record, the old one retired, accepted by name")
- The checker does not fail on the Reviewer snippet's wording, heading included; it warns; the smoke cases use their own text so that the suite does not fail on it either (RAI-W1-F1) | covered | the third answer
- Four other places where the checker fails on prose are left as they are and put to him | covered | the brief (a contradicted decision is a question for the owner, not a rewrite); his answer named one check
- ADR-I-0007 unchanged | covered | the third answer ("the record stands")
- Finding: no sentence in the plugin's text that a change inside the repository is reported where there is no plan; read trivial | covered | the first answer; the plan's stance and the closing message already report
- The check's result for the three records is recorded in the run record | covered | the brief's pass condition
- The version, 1.4.0 | extends | the third answer reaching whoever installs the plugin
- Built by a writing Worker on Fable 5.2 at low reasoning effort and the Codex worker seat, with the review seat | not audited | internal mechanics; no engineering philosophy
- The branch published and a pull request opened at this close, a note to Counsel, nothing merged | covered | common.md Standing Approvals

## Findings

- 2026-11-11, from Task_1 of the raised plan: the owner's answer on ADR-D-0016 has a change inside the repository go ahead and be reported; the plugin's text has the default (migrate or break) and the plan's compatibility stance, and no sentence that the change is reported where there is no plan | trivial: under a plan the stance is the report, and a change small enough to have no plan is reported in the run's closing message as any change is; adding the sentence would change no one's experience. Not escalated; told to Counsel with the unit's report.
- 2026-11-11, from Task_2 of the raised plan: the package checker fails on prose in four more places than the one his answer named | bears on the design: each blocks an equivalent rewording as the named one did, which ADR-I-0007 forbids. Escalated to Counsel with the unit's report as a question for the owner (bring all four in line, or say which are contracts). Part held: none; the named check is changed and the four are left as they are.
