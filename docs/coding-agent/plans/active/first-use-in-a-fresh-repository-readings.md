# Readings: First use in a fresh repository

Written by the Orchestrator for the value audit to compare after its grades are fixed. Not read by an auditor before grading.

## Readings

### `first-use-in-a-fresh-repository-plan.md`, plan draft

Item | reading | statement relied on

- DoD 1 (prose philosophy; companion with records; readers look there) | covered | brief, The philosophy as a human document, both statements
- DoD 2 (the reference; read after the draft; gaps; no wording; gaps left out recorded) | covered | brief, A reference for the philosophy, gives and constraint; its contents the means
- DoD 3 (acceptance of a stack by name merges; permission the owner's once) | covered | brief, Merging a stack
- DoD 4 (Counsel's seat; no acknowledgement rule) | covered | brief, The peer channel
- DoD 5 (setup offers the approval; the line; recorded in common.md and nowhere else) | covered | brief, Relay admission before setup
- DoD 6 (two lines; first-session reference; reference read only at a draft check; word count) | covered | brief, One-time setup without a cost; pass condition on the word count
- DoD 7 (the outside view, route-neutral, verbatim, no-route escape) | covered | brief, A view from a model of another family
- DoD 8 (before setup; dates) | covered | brief, Smaller frictions
- DoD 9 (records return by name) | covered | brief, Limits, first constraint
- DoD 10 (privacy and other repositories' names) | covered | brief, Limits, second constraint
- DoD 11 (validators; review; scenario 1 and the fixture part of scenario 2 on a fixture, the rest said plainly) | covered | brief, Pass conditions: "where one can be made, and where one cannot the closeout says so plainly"
- DoD 12 (the plan closes, the run reported ready) | covered as mechanics; the standing approval covers publication
- Planner-added 1 (companion `-companion.md`, metadata only, an input; discussion stays in notes) | extends | brief: "a companion notes file beside each philosophy, named after it"; "The Orchestrator and the Auditor look there"
- Planner-added 2 (old-form philosophies read as ratified until moved) | extends | brief: "the companion has a defined home"; the owner's two philosophies in the old form exist
- Planner-added 3 (the engineering discussion's notes in a notes file beside the philosophy) | extends | brief: "the reply is kept verbatim in the discussion notes"
- Planner-added 4 (version 0.31.0) | extends | the brief answers a report on 0.30.0 in use; the cache installs by version
- Non-goals (acknowledgement contract; named route; trivial work) | covered | brief, Left out on purpose
- Non-goals (template; grades; goal mode; rewriting other repositories' philosophies) | covered as mechanics
- Design: no hook built, the seat claimed by Counsel once per repository | extends | a departure from a means, recorded as a finding; brief: "where there is none, the reference tells Counsel to claim it"
- Design: the Counsel line beside the Standing Approvals entry | extends | brief: "Admission is recorded in the common rule file"; "one line there that records Counsel's seat and that relays are admitted"
- Design: a record proposed for the merge; ADR-D-0035 revised; ADR-D-0038 wording | covered | brief, Limits: "Where it changes what an accepted decision record decides, that record returns to him"
- A1 (a stack by name covers each pull request in it) | extends | brief: "acceptance of a stack by name"
- A2 (nowhere else excludes runtime memory, not the in-session statement) | extends | brief: "a note the Orchestrator keeps for itself is not a place the harness reads"; ADR-D-0038
- A3 (the identity convention `<repository>-counsel`; the owner may correct it) | extends | brief: "names the convention"
- Task_1 to Task_5 | covered, as the Definition of Done items they carry
- Decision Log 1 (no hook) | as the Design line
- Decision Log 2 (companion name; old form) | as Planner-added 1 and 2
- Scenarios, the Orchestrator's expectation only: all four not yet at plan draft.

#### The audit's comparison, plan draft (2026-10-07), as returned

- `Reading compared: DoD 1-11 agrees; DoD 12 agrees (covered); Planner-added 1 diverges: Orchestrator "extends", audit "cited" (the brief's statement covers the companion's home, purpose and readers whole; only the filename is a how); Planner-added 2 agrees; Planner-added 3 agrees; Planner-added 4 agrees; Non-goals (ack contract; route; trivial work) agrees; Non-goals (template; grades; goal mode; other repositories' philosophies) agrees (covered); Design: no hook agrees in grade (Orchestrator "extends" for the departure, audit cited on the gives-statement it serves; the departure is compared below); Design: Counsel line beside the Standing Approvals entry agrees in substance (read under DoD 5, cited); Design: records agrees; A1 diverges: Orchestrator "extends", audit "cited" (brief 30 says "a stack by name"); A2 agrees; A3 agrees; Task_1-5 agrees; Decision Log 1 agrees as the Design line; Decision Log 2 agrees; Decision Log 3 unread.`
- `Findings compared: Finding (hook means not taken): agrees, trivial. The owner experiences the same outcome, a seat taken before the first relay, and the brief's own text for runtimes without a hook already has Counsel claim it; a hook would have fired in Orchestrator sessions too. Ends cited.`

Readings corrected after this comparison: the companion's home, purpose and readers are what the brief states and only the filename is a how; "a stack by name" is the brief's own phrase.

### `first-use-in-a-fresh-repository-plan.md`, closeout

Item | reading | statement relied on

- Every item read under the plan-draft heading keeps its reading as corrected after that comparison, with these additions.
- The text as built, Counsel's side: prose philosophy, companion, notes file, dates, the two open-time lines, the two references, the outside view, the seat, before-setup | covered | the brief's sections as the plan-draft readings cite them
- The text as built, the Orchestrator's side: the companion read by the Orchestrator, the Auditor and setup; the offer and the Counsel line; the merge on acceptance of a stack; 0.31.0 | covered | the brief's sections; Planner-added 4 for the version
- Records: ADR-D-0035 revised and accepted by name; ADR-D-0038 wording only; ADR-D-0057 proposed then withdrawn on his question | covered | brief, Limits; his words of 2026-10-07
- This repository's rule files: the Counsel line; the merge rule | covered | brief, Relay admission and Merging a stack; the identity the standing approval of 2026-10-01 names
- The fixture: scenario 1 and the fixture part of scenario 2 shown, the rest said plainly | covered | brief, Pass conditions
- Worker judgement calls (Task_2): the notes file for either philosophy's discussion; `provisional` kept as a status; the two lines placed after the open-time bullet; "For facts, dispatch only" | extends | brief: "the reply is kept verbatim in the discussion notes"; ADR-D-0035
- Worker judgement calls (Task_3): the stub's wording; the offer at bootstrap and at a targeted refresh; the yes as his own statement unless already admitted; the repository-wide notes exclusion | extends | brief, Relay admission before setup; the mandate's boundary
- Orchestrator rulings: the wide notes exclusion kept; the Copilot adapter's agent list left; the history sentence added; the first-request scoping (review); the companion metadata-only (review); withdrawal of ADR-D-0057 on his question | covered | brief, The peer channel; A view from a model of another family; Limits; his words
- Departure from the means: no hook | extends | the finding below, trivial
- Observations for the owner: no open-time seat step in a later session; `<repository>` from the folder name where no remote exists | extends | brief: "names the convention"
- Scenarios, the Orchestrator's expectation only: 1 demonstrated on the fixture; 2 demonstrated in its checkable part, the discussion his; 3 not yet; 4 not yet.

#### The audit's comparison, closeout (2026-10-07), as returned

- `Reading compared: C1, C2, C5, C7-C12, C14-C19, C21 (companion part), C24, C26, C27: agrees (covered / cited). C3 (notes file for either philosophy): agrees (extends / inferred). C4 and C21 (old form): agrees (extends / inferred). C6 (provisional kept): agrees in grade (extends / inferred); the direction mark is the audit's. C13 (first-session reference) and J9 (no hook): agrees in grade, as at plan draft (Orchestrator "extends" for the departure; audit cited on the gives-statements it serves). C20 (repository-wide notes exclusion): diverges: the Orchestrator reads it both "extends" (Task_3 judgement calls) and "covered" (Orchestrator rulings line, "the mandate's boundary"); audit inferred, since no statement of the brief places a notes file outside the briefs folder. C22 (refresh offer, ask-again terms) and C23 (stub wording): agrees (extends / inferred); their cited parts agree (covered / cited). C25 (0.31.0): agrees (extends / inferred). C28 (ADR-D-0035): diverges: Orchestrator "covered ... accepted by name; his words of 2026-10-07"; audit ask-now under the mandate's rule for a record whose decision changed in range, the logged acceptance being a claim the Orchestrator applies, not support the audit may take. C29 (ADR-D-0038): diverges in class: Orchestrator "covered"; audit not audited, wording only. C30 and J13 (ADR-D-0057 withdrawn): agrees (covered / cited). J1 (the Orchestrator's reason marked for the owner): unread as a reading; graded with C28. J2, J3 (Task_1 rulings 2 and 3): unread. J4: agrees as on C20, C22, C23 and the "yes in the session" clause (covered / cited). J5 (pr-review-monitoring left): unread; not audited. J6: agrees per part. J7 (Copilot adapter list left): agrees (covered / cited). J8 (history sentence): agrees. J10, J11, J12: agrees (covered / cited). J14 (fixture, rule files): agrees (covered / cited). J15 (observations for the owner): Orchestrator "extends"; audit cited on brief 72, 73 and 35; diverges in class, nothing to redo. J16: unread; not audited. Scenarios, the Orchestrator's expectation against the audit's states: 1 agrees (demonstrated); 2 the Orchestrator "demonstrated in its checkable part, the discussion his", the audit ready for the owner's judgement with the checkable part demonstrated, the same substance in the mandate's three-state form; 3 the Orchestrator not yet, the audit ready for the owner's judgement (the text is built and only his real use can show it); 4 agrees (not yet).`
- `Findings compared: Finding (the hook means not taken; the seat claimed by Counsel following the first-session reference): agrees, trivial. The owner experiences a seat taken before the first relay either way; the brief's own means text for runtimes without a hook already has Counsel claim it, and the reference leaves room for a runtime that claims it at start. Its trivial reading rests on the seat persisting per repository, which the report's "inherited the Orchestrator's seat" (brief 35) suggests, and the Orchestrator's first observation to the owner (no open-time seat step in a later session) carries the residual to him. Ends cited. The departure noted on C13 is the same departure: agrees, trivial, ends cited.`

Readings corrected after this comparison: the widened notes exclusion extends the brief (no statement places a notes file outside the briefs folder); ADR-D-0038's change is wording only; the observations for the owner rest on the brief's pass conditions and "names the convention"; the owner's acceptance of ADR-D-0035 lives in the plan's Decision Log, a claim to the audit, and the readings now say so.

### Small changes 1 and 2 (provisional mark to the companion; seat at open), closeout

Item | reading | statement relied on

- The text as built, change 1: a philosophy's provisional mark in its companion, prose unmarked, readers adjusted | covered | brief, Directed after the run was reported ready, first statement
- The text as built, change 2: one open-time seat step whether or not the Counsel line is present; first-session refers to it | covered | brief, second statement
- The Orchestrator's calls: small, no plan, built together, reviewed once, audited once | covered | small-change brief: "The Orchestrator chooses, per change"; the statements leave no how-choice
- Worker judgement calls (old-form line not extended to in-prose provisional marks; first-session's dropped sentences) | covered as mechanics; nothing beyond the statements
- Orchestrator ruling: first-session's "does nothing more" reworded to "nothing beyond the open-time steps" | covered | the second statement makes the seat step run at every open
- Scenario 1 (the next Counsel session "does nothing more"): the Orchestrator's expectation, demonstrated as before; the seat step now runs at every open as he directed.

#### The audit's comparison, small changes 1 and 2 closeout (2026-10-08), as returned

- `Reading compared: C1-C5 agrees (covered / cited). C6, C10 agrees (covered / cited). C7 agrees (covered / cited). C8 agrees in grade (Orchestrator "covered as mechanics"; audit cited on the second statement with the means departure noted). C9 diverges: Orchestrator "covered as mechanics; nothing beyond the statements"; audit inferred, since no statement of the brief says what becomes of an in-prose provisional mark in an old-form philosophy. C11 unread as to grade (the Orchestrator cites a small-change brief this audit was not pointed to; not graded as a product item). C12, W1 unread. Scenario 1: the Orchestrator "demonstrated as before"; audit demonstrated with the new seat step not shown on a fixture, the same state.`
- `Findings compared: Finding (hook means not taken): agrees, trivial; in this range first-session.md drops the hook sentence altogether, and nothing anyone experiences changes since no adapter ever claimed a seat. The departure noted on C8 is that same departure: agrees, trivial, ends cited. C9 (old-form in-prose provisional marks unread): bears on the design and not recorded; an owner whose old-form philosophy carries a provisional mark in its prose would no longer have an inferred item resting on it reported to Counsel, until the record is moved. Ends inferred.`

Readings corrected after this comparison: the Worker's old-form call extends the statements (no statement says what becomes of an in-prose mark in an old-form philosophy) and is a finding, recorded below.

## Findings

- The brief's means on a session-start hook claiming Counsel's seat is not taken: the plugin has no hook mechanism and names no channel tool; the seat is claimed by Counsel following the first-session reference, once per repository. Reading: trivial; it changes nothing the owner experiences beyond one claim per repository, which the brief's own text for runtimes without a hook already asks of Counsel.
- For a philosophy in the old form (its record and marks inside the document), an in-prose provisional mark is read by no reader once the mark is defined as living in the companion, until Counsel moves the record (noticed by the closeout audit of small changes 1 and 2, 2026-10-08, from the Worker's call not to extend the old-form line). Reading: bears on the design, since an inferred item resting on such a mark would no longer be reported to Counsel for an old-form philosophy. Escalated to the owner through Counsel on 2026-10-08 as a value question; the part held: the old-form line's treatment of a provisional mark. Answered 2026-10-08: "This case doesn't need to be explicitly mentioned. Old form philosophies currently doesn't exist anywhere and it never will,"; the part released and the old-form reading dropped (small change 3).
