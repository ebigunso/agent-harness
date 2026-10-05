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

## Findings

- None yet.
