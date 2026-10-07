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

## Findings

- The brief's means on a session-start hook claiming Counsel's seat is not taken: the plugin has no hook mechanism and names no channel tool; the seat is claimed by Counsel following the first-session reference, once per repository. Reading: trivial; it changes nothing the owner experiences beyond one claim per repository, which the brief's own text for runtimes without a hook already asks of Counsel.
