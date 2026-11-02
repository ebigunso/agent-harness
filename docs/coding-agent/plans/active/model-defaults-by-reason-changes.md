# Changes: Model defaults by reason

- Run record: `docs/coding-agent/plans/active/model-defaults-by-reason-run.md`.

## The proposed record rewritten to intent altitude

- The owner's statement: the governing brief `docs/coding-agent/briefs/active/model-defaults-by-reason-brief.md`, Directed during the run, the last entry (**gives**, told 2026-11-02). As it reached this session, Counsel's relay of 2026-11-02 (10:57Z), admitted by the standing approval of 2026-10-01, quoting the owner: "The ADRs are saying the right things, but I'm starting to feel that the recent suite of ADRs, not limited to the ones proposed, are slightly too much into the details to be a good decision that is expected to hold through subsequent changes." and, put to him as hold-and-rewrite against accept-now, "Hold and rewrite before acceptance."
- Built as a small change without a plan: one task, and the statement settles how (the record standard's altitude). It goes on top of the run's branch, `feature/2026-10-29/model-defaults-by-reason`, and pull request 94's text is brought up to date.
- The change starts from revision: 61aaf49 (the brief entry committed on the run's branch).
- The owner's separate direction that older records be checked and rewritten to the same standard is a separate initiative, not this change.
- 2026-11-02 11:00Z Worker dispatched (Claude subagent `harness-worker` on Opus), text verbatim (checkout paths shortened):

  Worker dispatch: the small change "The proposed record rewritten to intent altitude" of the run in docs/coding-agent/plans/active/model-defaults-by-reason-changes.md (built without a plan; the owner's statement in the brief is the requirement). Role: Worker. Return one YAML report per the subagent-report-contract skill as your final message.

  Where to work: the worktree <worktree> (branch feature/2026-10-29/model-defaults-by-reason); every path is relative to it. Do not touch <main checkout>, where another Worker rewrites other records.

  Why: the owner held the proposed record ADR-D-0066 before acceptance. It says the right things but sits too close to the plugin's procedure, so it would need replacing whenever that procedure changes. He wants it rewritten to the altitude the record standard already states, so that it is a decision that holds through later rewording of the plugin text.

  Owns
  - docs/coding-agent-orchestration-harness/decisions/ADR-D-0066-*.md (rename it if its title changes; nothing else in decisions/)

  Acceptance
  - The record states one decision at intent altitude, as durable-docs-authoring/references/adr.md Form states. Its constraint is worded so that any rewording of the plugin text that preserves it stays valid. Mechanism stays in the plugin text and out of the record: how a reason is read, the fit ranking and walk-down steps, how cost is judged, what setup researches and in what order, the Models Record's lines, plugin file names, line references, exact strings. A record may name the role or document a decision is about (the workspace's record of models, setup) but not the steps taken through them.
  - Should the rewrite leave more than one decision, the one-decision test ("could this be retired on its own without touching another decision?") decides: a decision that can be retired apart becomes its own record, numbered 0067; otherwise it stays one.
  - Nothing is decided that the draft does not decide, and nothing it decides is dropped except mechanism moved out. The draft replaces the accepted ADR-D-0061: the result still names it as replaced, and carries whatever of ADR-D-0061 still binds as a decision, because retiring it would otherwise drop it. No file outside owns moves; the retirement waits for acceptance.
  - The form follows adr.md and the repository's decision-record convention: status proposed; the why is prose of a sentence or two and names the statement it serves, in the brief or in a philosophy the rules' Repository Reference Documents point to; each rejected alternative says why it lost and carries its reopen condition or "rejected outright"; Revisit When names a premise, not an occasion (a measured fact names the models and the date of the check); no time-relative wording; the owner is never quoted and no ruling is a reason; no model, provider, plan or price named in the decision itself.

  Sources: the brief docs/coding-agent/briefs/active/model-defaults-by-reason-brief.md (whole, and the last entry under Directed during the run); plugins/coding-agent-orchestration-harness/skills/durable-docs-authoring/references/adr.md and the template and convention it points to; docs/coding-agent/rules/common.md (Repository Reference Documents); the draft as it stands; ADR-D-0061 in decisions/; the Decision Log of docs/coding-agent/plans/completed/model-defaults-by-reason-plan.md for the reasons. Where a reason is not written down in these, put the gap in questions_for_orchestrator and invent nothing. The plugin text under plugins/ is where the mechanism lives; read it to check that what you move out is stated there. Do not open any *-notes.md or *-readings.md file.

  Constraints: edit only owns; no Git commits or other shared-state Git mutations, `git add -N` included. No machine-specific user names or paths in anything you write.

  Validation (required, worker-owned): from plugins/coding-agent-orchestration-harness/: py scripts/validate_harness_package.py and py scripts/run_validation_smoke_tests.py pass; git diff --check on the decisions/ directory.

  Report: the YAML report. In summary, for each resulting record: its ID and title, the decision in one line, the constraint, the why, and what it replaces. In assumptions, each piece of mechanism removed, with where in the plugin text it is stated (path and section), so the review can check that nothing was lost.
- 2026-11-02 11:05Z Worker report: done. ADR-D-0066 rewritten (filename unchanged) and ADR-D-0067 created; both proposed; package validator, smoke tests and `git diff --check` pass. A `git add -N --dry-run` was chained into a validation command by mistake; it changed no index state (the new file still untracked), disclosed in the report.
- Judgement calls:
  - The draft held two decisions that the one-decision test separates: how each role's option is chosen (by a stated reason resolved against the workspace's record, never by a name), kept in ADR-D-0066; and that research is the Researcher role's work, never part of a Worker's task, placed by one rule for the Orchestrator and Counsel alike, with the dispatcher's own model holding the role where no recorded option fits, moved to ADR-D-0067. Both name ADR-D-0061 as replaced.
  - When research may be skipped, and what a skip records, read as mechanism (the draft and ADR-D-0061 both listed it as not covered); stated in the plugin text.
  - The dated seed of tendencies kept inside ADR-D-0066, since the exception that only the seed names providers rests on it.
  - Mechanism removed, each stated in the plugin text: a reason's parts and each work type's tendencies; each role's cost setting; how the Researcher's option is picked; the fallback's recording; the skip and its waiver; the seed's level, families and date; the record's contents and where it is kept.
- Rulings: ADR-D-0061 is replaced jointly; both records list it, and its retirement, applied when both are accepted, reads "Replaced by ADR-D-0066 and ADR-D-0067." with the superseded/ filename settled then as D7 of the run-1 plan settled lengths. `adr.md`'s "no partial supersession" holds, since ADR-D-0061 retires whole. The skip reading and the seed's place stand as the Worker made them.
- ADR-D-0067's filename shortened to 113 characters by the Orchestrator (`docs/coding-agent/lessons.md`: a record's filename at or under 135 characters, for the smoke test's copied tree on Windows); the heading keeps the full title.
- 2026-11-02 11:05Z Review dispatched to the Codex reviewer seat over agmsg (range 61aaf49..1d9a1b4; the change against the brief's last Directed during the run entry and `adr.md`; nothing lost or added against the draft and ADR-D-0061; the joint replacement; privacy; validators).
- 2026-11-02 11:11Z Review: CHANGES_REQUESTED, one minor finding. IR-F1: ADR-D-0067 still fixed a fallback route (the dispatcher's own model holds the Researcher role where no recorded option fits), which can change apart from the decision. The split, nothing lost or added, the removed mechanism's presence in the plugin text, the form, the joint replacement, privacy and the validators: confirmed.
- Ruling on IR-F1, fixed by the Orchestrator (three phrases in ADR-D-0067): where no recorded option fits, research is still a Researcher's; which option holds the role then, and what is recorded, moved to Not covered. The judgement call above that kept the fallback as decision is revised accordingly: the decision kept is that research stays a Researcher's even then; the fallback's choice of model is mechanism.
