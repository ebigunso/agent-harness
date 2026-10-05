# Readings: Setup names what is missing

What the Orchestrator writes for the audit to compare. The auditor opens this file only after its grades are fixed.

## Readings

### `setup-names-what-is-missing-plan.md`, plan draft

Item | reading | statement relied on

- Definition of Done: every gives-statement and constraint carried by the plugin text; means built from | covered | brief, header: "It is passed verbatim; do not paraphrase it into a plan as if the paraphrase were the requirement."
- Definition of Done: scenarios 1 and 2 hold on a fixture repository, shown by a fresh agent following the setup text | covered | brief, Pass conditions: "scenarios 1 and 2 hold on a fixture repository"
- Definition of Done: no setup text drafts or templates a philosophy | covered | brief, Limits: "Setup never writes, drafts, starts or offers a form to fill in for a philosophy, and infers none from the repository's code or documents."
- Definition of Done: a run behaves as today while philosophies are missing | covered | brief, Limits: "A run in a repository whose philosophies are marked missing behaves exactly as a run does today in a repository without one."
- Definition of Done: a proposed record is accepted by name before text is built on it | extends | the earlier brief's amendment, "You still check a proposed decision record before anything is built on it."; this brief does not state it
- Definition of Done: validators and review | covered | brief, Pass conditions: "the package validators pass"
- Definition of Done: the run closes with its branch published and a pull request opened, nothing merged | covered | standing approval in `docs/coding-agent/rules/common.md` on publishing a finished, reviewed run
- Planner-added: setup looks among tracked files for a document that states which philosophy it is and carries a ratification record; with more than one it records none | extends | brief: "Where the repository already has a philosophy document, setup finds it, records the pointer to it, and says in its report that it did"; "A philosophy has no fixed path or name, so setup will sometimes list one as missing when it exists."
- Planner-added: the missing line cannot be read as a pointer and turns value-level operation neither on nor off | covered | brief, Limits: "behaves exactly as a run does today in a repository without one"
- Planner-added: the lines are derived again at every refresh, in earlier repositories too | extends | brief: "What is missing stays visible after the setup report is gone: the common rule file carries a line for each missing philosophy."
- Planner-added: this repository's own rule file refreshed under the built text | extends | brief: "Someone opens a repository and runs the harness setup once."
- Planner-added: one version bump | extends | brief: "the package validators pass"
- Non-goals | covered | brief, "Left out on purpose"; no script and no validator are asked for
- Design: one detection step in the rulebook, not "always missing until he names the file" | covered | brief: "setup finds it, records the pointer to it, and says in its report that it did"
- Compatibility stance: preserve | covered | brief, Limits: "behaves exactly as a run does today"
- A1: a gone pointer is flagged and left | covered | brief: "At refresh, a pointer to a file that is gone or moved is flagged, as it is for decision records."
- A2: Counsel mentions once per session and offers | extends | brief: "A Counsel session sees those lines when it opens and may offer to start on one."; "Nothing nags."
- A3: "a later run is kept to that product philosophy" shown on the fixture by a plan draft and its audit, not a whole run | extends | brief, scenario 2
- Task_1: one record, if the admission test passes, to the owner by name before text is built | extends | brief: "This changes a rule in force"
- Task_2: setup, the pointer rule, Counsel's opening | covered | brief, all sections
- Task_3: two fixture repositories and a fresh agent's setup on each | covered | brief, Pass conditions
- Task_4: land the record; refresh this repository's rule file; close and publish | covered | standing approval on publishing; brief on the rule files
- Decision Log: no script, no validator; two candidates recorded as neither; earlier repositories at refresh; Counsel once per session | extends | brief: "It states what and why. How is the Orchestrator's"

#### The audit's comparison, plan draft, first dispatch (2026-10-05), as returned

Reading compared (these two lines go in the readings file, not the plan):
- DoD 1: agrees
- DoD 2: diverges (Orchestrator: covered; audit: ask-now)
- DoD 3: agrees
- DoD 4: agrees
- DoD 5: diverges (Orchestrator: extends; audit: not audited, internal mechanics)
- DoD 6: agrees
- DoD 7: agrees
- Planner-added 1: agrees
- Planner-added 2: agrees
- Planner-added 3: agrees
- Planner-added 4: agrees
- Planner-added 5: diverges (Orchestrator: extends; audit: not audited)
- Non-goals, read as one item: agrees for "Left out on purpose" and for no change to how a philosophy is written; diverges for no script, no validator and the dispatch templates (Orchestrator: covered; audit: not audited)
- A1: agrees
- A2: agrees
- A3: diverges (Orchestrator: extends; audit: ask-now)
- Task_1: diverges (Orchestrator: extends; audit: not audited)
- Task_2: agrees
- Task_3: diverges (Orchestrator: covered; audit: ask-now)
- Task_4: agrees
- Decision Log 1: agrees
- Decision Log 2: unread
- The Orchestrator also read "Design" and "Compatibility stance"; the mandate lists neither as a plan item, so they carry no grade.

Findings compared: none found (the readings file exists and records no finding; no item line notes a departure from a means)

### `setup-names-what-is-missing-plan.md`, plan draft, second dispatch

Item | reading | statement relied on

- Every item read under the plan-draft heading above keeps that reading, with these changes.
- Definition of Done: scenarios 1 and 2 on a fixture, the later run of scenario 2 carried from plan to close and audited at both ends | covered | brief, Pass conditions: "scenarios 1 and 2 hold on a fixture repository"; scenario 2: "a later run there is kept to that product philosophy"
- Definition of Done: a proposed record accepted by name before text is built on it; Task_1; the version bump; no script, no validator, the templates untouched | covered as mechanics; no statement needed
- A3: the later run is a whole small run on the fixture, its agents fresh, dispatched by this run's Orchestrator | covered | brief, scenario 2
- Task_3 | covered | brief, Pass conditions
- Planner-added: an objection is kept in the line that replaces the pointer, in a form that is not a pointer | extends | brief: "his objection removes it"
- Task_2: the setup report is where an Orchestrator session tells the person what is missing | covered | brief: "Those things are clearly presented as missing"; "no run reminds the person of it"
- Task_3: the fixture's later run passes the built text's own gates, this run's Orchestrator standing in for the fixture's user | extends | brief, scenario 2
- Decision Log: the line redone after the first verdict, nothing asked of the owner | covered | the earlier brief's amendment: "A line the Orchestrator adds to its own plan that your documents do not support is the Orchestrator's to drop or redo so that the plan follows the brief." (not this brief; this brief is silent on it)

#### The audit's comparison, plan draft, second dispatch (2026-10-05), as returned

Reading compared (heading "plan draft, second dispatch", which keeps the first heading's readings except where it changes them):
- DoD 1: agrees
- DoD 2: agrees
- DoD 3: agrees
- DoD 4: agrees
- DoD 5: diverges (Orchestrator: covered as mechanics; audit: not audited, internal mechanics on a side with no document)
- DoD 6: agrees
- DoD 7: agrees
- Planner-added 1: agrees
- Planner-added 2: agrees
- Planner-added 3 (objection line): agrees
- Planner-added 4 (refresh): agrees
- Planner-added 5 (this repository's rule file): agrees
- Planner-added 6 (version bump): diverges (Orchestrator: covered as mechanics; audit: not audited)
- Non-goals, read as one item: agrees for "Left out on purpose" and for no change to how a philosophy is written; diverges for no script, no validator and the dispatch templates (Orchestrator: covered; audit: not audited)
- A1: agrees
- A2: agrees
- A3: diverges (Orchestrator: covered; audit: inferred, the brief does not state the run's size or who dispatches it)
- Task_1: diverges (Orchestrator: covered as mechanics; audit: not audited)
- Task_2: agrees
- Task_3: read twice. Agrees with the reading of the stand-in (extends); diverges from the reading of the task as a whole (Orchestrator: covered; audit: inferred)
- Task_4: agrees
- Decision Log 1: agrees
- Decision Log 2: unread
- Decision Log 3: agrees on the grade (the statement the reading relies on is from another brief, as the reading itself says; the audit's support is this brief's scenario 2)
- Decision Log 4: unread as an entry (its two parts are read under Planner-added 3 and Task_3)
- The Orchestrator also read "Design" and "Compatibility stance"; the mandate lists neither as a plan item, so they carry no grade.

Findings compared: none found (the readings file records no finding; no item line notes a departure from a means)

Readings corrected after this comparison: A3 and Task_3 as a whole are extensions (the brief does not state the run's size or who dispatches it); the acceptance of a record by name, the version bump, Task_1, no script, no validator and the templates are mechanics the audit does not grade.

## Findings

- Four Auditor dispatches in two days opened a readings file before grading, two of them running on this run's fixture; the mandate's instruction did not hold. Reading: trivial as to what he experiences (no grade was given on a seen reading), but it blocked this run's evidence; built here as the mandate's First Step, the Orchestrator's addition.
- A repository that tracks another project's ratified philosophy (a vendored project, or a test fixture, as this repository's own fixture was) gets that file recorded as its philosophy by setup. Reading: trivial; the brief leaves a wrong pick to one objection, and the objection holds across refreshes. This repository's fixture was changed so that it is not one.
- The built text does not say which comes first when a request itself contradicts a philosophy: the question before planning, or the plan-draft audit; nor what "search the documents before escalating" means when the documents answer against the user's explicit request (the fixture's Orchestrator asked first). Reading: bears on the design, as it decides whether a person is asked or planned against; outside this brief, which is about setup; no part of this plan is held by it.
- In a run on a philosophy alone whose user is not the product owner, no text names a route to the product owner. Reading: bears on the design; outside this brief; nothing here is held by it.
- The reading is written before the plan review and can go stale when the review changes the plan; the reading's three values have none for an item the audit will not grade; a plan file has to exist half-made to hold the research waiver and start revision before requirement questions are settled. Reading: trivial; mechanics.
