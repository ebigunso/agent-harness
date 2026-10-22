# Changes file: Choosing where research goes

- Run record: `docs/coding-agent/plans/active/choosing-where-research-goes-run.md`. Readings file: `docs/coding-agent/plans/active/choosing-where-research-goes-readings.md`.
- Holds the trace of each small change of the run built without a plan; the Orchestrator's writing, not audit-stated. Created 2026-10-23 when the owner directed a change against the brief while the run was open for his judgement.

## Small change 1: a research task closes on the Researcher's report

- Directed by the owner while the run is open, on a finding from the Copilot review of #92 (plan-format/SKILL.md:27): a task of type `research` now goes to the Researcher role, never a Worker, but a Task_X closes only on a Worker report with `status: done`, so a plan carrying a legitimate research task could not close. Read as bearing on the design and escalated; Counsel put two ways to him (close on the Researcher's report; or research never a plan task) and recommended the first. His words, relayed by Counsel on 2026-10-23 (admitted by the standing approval of 2026-10-01), quoted in full: "Go with A."
- Where the statement stands in the brief: `docs/coding-agent/briefs/active/choosing-where-research-goes-brief.md`, section "Directed after the run was reported ready", first statement (committed b6d967f).
- Starts from revision: b6d967f.
- The Orchestrator's call: small, no plan; one task, plugin text only, built on the run's branch (#92). A research task's report is the Researcher's: its findings answer the task's acceptance and carry its required validation; closeout and wave integration accept that report for a research task as they accept a Worker's for the rest; nothing else changes. Research waived for the build: the gap and the texts that state it are named in the finding (completion-closeout.md Task_X Done Criteria, wave-integration contract, the Researcher's Orchestrator-dispatch output). Routed as skill prose to a Claude Worker on Opus (common.md); review by the Codex reviewer seat; closing audit on Fable.
