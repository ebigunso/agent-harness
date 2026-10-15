# Run record: Counsel's questions while drafting, and research before a plan

- Governing brief: `docs/coding-agent/briefs/active/counsel-questions-and-planning-research-brief.md`
- Hand-over: Counsel's relay of 2026-10-15 (01:23Z), admitted by the standing approval of 2026-10-01, quoting the owner's ratification of 2026-10-14: "I ratify the brief, hand it over now."
- Run starts from revision: 25f9831 (the brief committed on the run's branch, on top of pull request 85's branch)
- Readings file: `docs/coding-agent/plans/active/counsel-questions-and-planning-research-readings.md`.
- State: open for the owner's judgement; a change he directed on 2026-10-15 is being built (reported ready 2026-10-15)
- Changes file: `docs/coding-agent/plans/active/counsel-questions-and-planning-research-changes.md`.

## Scenarios

State is one of: not yet; demonstrated (with how to observe); ready for the owner's judgement. States as the closeout audit stated them, 2026-10-15.

| Scenario | State |
| --- | --- |
| 1. A Counsel session drafting a brief meets a choice: framed as an experience change the options read the same, so Counsel decides it and tags it, and the owner is not asked; a choice whose framings differ reaches the owner as those two framings. | ready for the owner's judgement; the rules are at counsel SKILL.md L29 and L76; observe in his next Counsel discussion on the plugin as changed on this branch |
| 2. A brief is ready: the owner sees a handful of experience framings for what changed anything, ratifies on those, and does not read the brief; the unassisted path is the default, the backup named once. | ready for the owner's judgement; the rules are at counsel SKILL.md L51, L56, L57 and L59, with value-documents L65; observe at his next brief ratification |
| 3. A plan is drafted for a change in unfamiliar code: the research is done first, the tasks are concrete, no task says "investigate first" for what the plan needed to know. | demonstrated; observe at the fixture plan `fx/planrepo/docs/coding-agent/plans/active/currency-field-plan.md` in the Orchestrator's session scratchpad (outside the repository, may not persist): its tasks name `tallybook/monthly.py`'s three-field unpack and `sh scripts/precommit.sh`, with no investigate-first task; the agent's step-by-step report is in the plan's Progress Log |
| 4. A draft plan whose first task postpones the research the rest depends on: plan review flags it. | demonstrated; observe at the fixture `fx/plans/postponing-plan.md` in the same scratchpad; the reviewer's NEEDS_REVISION and the control's "Task_1 is not a finding" are in the plan's Progress Log; re-running the logged dispatch reproduces them |

## Units

| Unit | State | What its closeout audit found |
| --- | --- | --- |
| `docs/coding-agent/plans/completed/counsel-questions-and-planning-research-plan.md` | authorized under the ratified brief 2026-10-15; closed 2026-10-15 | Scenarios: 1 ready for the owner's judgement; 2 ready for the owner's judgement; 3 demonstrated; 4 demonstrated; getting closer: yes (closeout verdict logged in full in the plan) |
| Small change 1 (`counsel-questions-and-planning-research-changes.md`): drops and departures reach the owner as framings at ratification | directed 2026-10-15; in progress | - |
