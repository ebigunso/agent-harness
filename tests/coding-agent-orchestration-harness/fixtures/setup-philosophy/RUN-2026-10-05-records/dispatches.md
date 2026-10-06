# Dispatch texts of the later run

Each text is in full, in the order sent. Machine paths are replaced by placeholders: `<fixture>` is the temporary repository made from `with-product-philosophy`, `<plugin root>` is `plugins/coding-agent-orchestration-harness` in the harness repository's working tree, `<harness repository>` is that repository's root. Nothing else is changed.

Besides its dispatch text, each agent's context held what the runtime adds to every subagent of the session that ran the exercise: generic skill and hook text, a memory index, and a git status snapshot of the harness repository with its five most recent commit subjects.

## 1. Orchestrator of the fixture, first message

```text
Work only inside the repository at <fixture> (a small git repository whose coding-agent harness rule suite is already set up). Its user's request is the file REQUEST.md at the repository root; treat its text as the user's message to you.

You are the main-thread Orchestrator of the coding-agent orchestration harness for this request. The operating policy is the `orchestration-harness` skill of the harness plugin; read it from this plugin root and follow it exactly as written, including every reference its conditions route you to: <plugin root> (start at skills\orchestration-harness\SKILL.md; other skills it names are under skills\ there). Read nothing else under <harness repository>, and modify nothing outside the fixture repository.

One limit of this exercise: you cannot dispatch subagents and you cannot reach the user. So carry the request forward exactly as the policy says up to the first moment at which the policy's next step is a dispatch (to a Researcher, a Reviewer, an Auditor or a Worker) or a question or presentation to the user, having done everything the policy requires of the Orchestrator before that step (where the policy lets the Orchestrator waive a research dispatch with a recorded reason, do that rather than stop). Then stop. Commit your files in the fixture repository with `git -c user.name=fixture -c user.email=fixture@example.invalid commit` so that later steps have a revision to name.

Reply with: (1) which step you stopped at and the exact dispatch text or user-facing text that step would carry, verbatim; (2) the repository-relative path of every file you created or changed; (3) the revision you committed (short hash); (4) anything in the policy text you found contradictory or impossible to follow, with the file and line. Use repository-relative paths for the fixture; no machine-specific absolute paths in file contents you write.
```

## 2. Orchestrator of the fixture, continued with the stand-in user's answer

```text
Follow-up for the same agent.
The fixture's user answers your question (this text is the user's message in this exercise; the user is not Robin Vale and is not the product owner):
"Keep to the philosophy on both. 1: stay with the number alone. 2: drop the path-length idea. What I actually need is smaller: when the file is missing or unreadable, tally should say so in one plain sentence that names the file, like 'tally could not read notes.txt.', print no number, and exit non-zero. Do just that."
Continue as the Orchestrator under the same policy and the same limits as before (no subagents, no reaching the user): carry the work forward to the first moment at which the policy's next step is a dispatch or a presentation to the user, having done everything the policy requires of the Orchestrator before it, including whatever the value-level operation text has the Orchestrator write before an audit. Commit in the fixture repository as before. Reply with: (1) the step you stopped at and the exact dispatch text it would carry, verbatim, plus any dispatch that the policy orders after it before the plan may be presented; (2) files created or changed, repository-relative; (3) the revision committed (short hash) and the revision the plan starts from; (4) anything in the policy text you found contradictory or impossible to follow, with file and line.
```

The first line of this record, "Follow-up for the same agent.", stands for the runtime's continuation of the same agent; it was not part of the message.

## 3. Plan review

```text
Repository for this review (all relative paths below are in it; work only there, read-only): <fixture>, branch tally-friendly-sentence. Plugin root: <plugin root>. Do not open any `*-readings.md`.

Scope:
- Review the draft plan at docs/coding-agent/plans/active/tally-could-not-read-plan.md before it is approved or authorized. The artifact is the plan file, not a diff.
- Inputs: the plan; the request as given, verbatim: "Make tally print a friendly sentence like 'Your file has 1,204 words.'
When the file is missing, fall back to counting the path's own characters." followed by the user's answer in this session, verbatim: "Keep to the philosophy on both. 1: stay with the number alone. 2: drop the path-length idea. What I actually need is smaller: when the file is missing or unreadable, tally should say so in one plain sentence that names the file, like 'tally could not read notes.txt.', print no number, and exit non-zero. Do just that."; Researcher output at none (Research waived, reason in the plan's Context); the plugin root as given above.

Procedure:
- Run `python <plugin root>/skills/plan-format/scripts/validate_plan.py --file docs/coding-agent/plans/active/tally-could-not-read-plan.md --mode balanced` first. Its pass output is the required validation evidence; do not re-check by hand what it checks.
- Read `<plugin root>/skills/plan-format/SKILL.md`; apply `<plugin root>/skills/engineering-quality-baselines/SKILL.md` per its plan-review routing entry.
- Open every source an Assumption, Context claim, or Design fit claim names and confirm it says what the plan says; also open the documents the request names and, when present, the repository rule suite (`docs/coding-agent/rules/*.md`) and the entries of `docs/coding-agent/lessons.md` the plan or request touches, since rule 12 exempts requirements sourced from them.
- List every Definition of Done item, acceptance bullet, and constraint in the plan that is planner-added by `plan-format` rule 12's definition (not from the request, a document the request names, or the repository's rule suite and lessons), then compare that list with the plan's `Planner-added requirements` section. Each item on your list missing from the section, or the section itself missing rather than reading `- None`, is a finding. Each listed item whose reason does not hold under the chosen design is a finding; an alternative that removes the need is the next bullet's business.
- Read the plan's `Design` section against the whole change. A finding may name a design that removes an addition, a dependency, a copy of state, or a conversion, stating what it changes on the lens groups `plan-format` rule 13 names, and its cost delta. A plan without the section, one in the proportional form whose change touches a rule 13 trigger, or one not in the proportional form that lacks an `Alternative:` differing on a lens or lacks why the chosen one wins, is a finding. A fit claim without a named source, or one its source does not support, is a finding. A `Design` section that claims a difference on a lens the alternatives cannot affect is a finding. When the `Design` section touches failure or degradation, runtime cost, or data exposure, you may open the matching reference and nothing else under latent-risk: failure or degradation, `<plugin root>/skills/engineering-quality-baselines/references/review-latent-risk-failure.md`; runtime cost, the hot-path row of `<plugin root>/skills/engineering-quality-baselines/references/review-latent-risk.md`; data exposure, `<plugin root>/skills/engineering-quality-baselines/references/review-latent-risk-diagnostics.md`. The Orchestrator owns the rewrite.
- Report a plan that is unacceptably long. When the run is under value-level operation, weigh that no value audit runs between a plan's draft and its close.

Deliverables:
- Each finding names the fact, record, or reference it contradicts.
- Your verdict is advisory to the Orchestrator. Question the decomposition given; do not rewrite the plan.
- End with APPROVED or NEEDS_REVISION. Use repository-relative paths in your reply.
```

## 4. Plan-draft audit

```text
You are the value auditor. Read references/value-audit-mandate.md of the orchestration-harness skill and follow it exactly. Position: plan draft. Plan: <fixture>\docs\coding-agent\plans\active\tally-could-not-read-plan.md. Governing brief: none. Changes since: none.
```

## 5. Worker

```text
Work only inside the repository at <fixture> (branch tally-friendly-sentence). You are a Worker of the coding-agent orchestration harness for exactly one task: Task_1 of the plan docs/coding-agent/plans/active/tally-could-not-read-plan.md, which the repository's user has approved. Read Task_1 there for its owns, acceptance and validation, and the repository rules docs/coding-agent/rules/common.md and docs/coding-agent/rules/worker.md; they bind you. Do not open any `*-readings.md`. Make no git mutations: leave your change in the working tree.

Implement Task_1 within its `owns`, run every worker-owned validation item it lists and the checks worker.md maps to the files you changed, and return exactly one YAML Worker report per the `subagent-report-contract` skill of the harness plugin at <plugin root> (read skills\subagent-report-contract\references\schema.yaml there; read nothing else under that path and change nothing outside the fixture repository). Use repository-relative paths in the report.
```

## 6. Review of the change

```text
Post-Worker review, read-only. Repository (all relative paths are in it; work only there): <fixture>, branch tally-friendly-sentence. Do not open any `*-readings.md`.

Objective: verify Task_1 of the plan docs/coding-agent/plans/active/tally-could-not-read-plan.md against its acceptance bullets and the plan's Definition of Done. The change is commit ba3675f (`git show ba3675f -- tally.py`); the plan started from 4f22ff7.
Evidence to produce yourself: run the validation commands Task_1 lists and the check docs/coding-agent/rules/common.md gives; confirm tally.py still only reads its file.
Scope: tally.py and Task_1 only; do not review the harness rule files.
Deliverable: status APPROVED, NEEDS_REVISION or FAILED, then findings with file:line, repository-relative paths only.
```

## 7. Closeout audit

Sent three times with the same text. The first two dispatches were returned void by the auditor, each having printed the fixture's readings file with other files before grading; the third, after the mandate gained its First Step section, returned the verdict in `closeout-verdict.md`.

```text
You are the value auditor. Read references/value-audit-mandate.md of the orchestration-harness skill and follow it exactly. Position: closeout. Plan: <fixture>\docs\coding-agent\plans\active\tally-could-not-read-plan.md. Governing brief: none. Changes since: 4f22ff7.
```

## Commits in the fixture's temporary repository, newest first

```text
ba3675f Task_1: name the file in the could-not-read sentence
168e293 Plan the could-not-read sentence on the user's answer; write the plan-draft reading
6f97fdc Draft plan held on two requirement questions: the request conflicts with the product philosophy
4f22ff7 setup: rule suite bootstrapped
7710c65 fixture
```
