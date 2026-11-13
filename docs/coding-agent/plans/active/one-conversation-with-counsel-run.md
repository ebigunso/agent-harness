# Run record: One conversation with Counsel

- Governing brief: `docs/coding-agent/briefs/active/one-conversation-with-counsel-brief.md`
- Hand-over: Counsel's relay of 2026-11-12, admitted by the standing approval in `docs/coding-agent/rules/common.md`, quoting the owner's ratification of that day: "I ratify the "One conversation with Counsel" brief."
- Run starts from revision: a295f45 (the brief and Counsel's notes, on top of main 0930756).
- Readings file: `docs/coding-agent/plans/active/one-conversation-with-counsel-readings.md`.
- State: one unit, closed 2026-11-13 by the channel clock; the run is reported ready (candidate ready) and stays open for the owner's judgement: his acceptance of the pull request, of the twelve proposed decision records by name and of the reworded entry admitting Counsel's relays, and his confirmation of this workspace's Sessions record.
- What this run touches, told to Counsel on taking the brief: the plugin's text on how a session gets its role, on Counsel's conduct and on seats and dispatch; the runtime adapter files and loaders; the rule files; proposed decision records replacing ADR-D-0037 and ADR-D-0020.

## Scenarios

State is one of: not yet; demonstrated (with how to observe); ready for the owner's judgement. States are the Auditor's, copied from the closeout verdict of 2026-11-13 by the channel clock.

| Scenario | State |
| --- | --- |
| 1 | not yet. In part: with no role chosen the session is Counsel and says so with how to open the other role. Observe in Claude Code by a non-interactive run with this branch's plugin and no agent named; in Codex by a run in a repository whose `AGENTS.md` holds the block. "Never open another session" is not shown. |
| 2 | not yet. In part: on a stand-in ratification Counsel started an Orchestrator session and carried the words. Observe by ratifying in a session with no agent named, then listing sessions. He "goes on talking to Counsel" was not tried, and the started session ran on the installed plugin 1.5.0, not the branch's. |
| 3 | not yet. In part: the second brief's session was started at once. Its ratification reached a copy that never took a turn; no work began. |
| 4 | not yet. Not tried. |
| 5 | not yet. In part: Workers that took over part-way finished from the hand-off, and first dispatches carried the machine's entries. All were subagents; no peer seat. |
| 6 | not yet. Not tried. |
| 7 | not yet. Not tried. |
| 8 | not yet. In part: Counsel held the brief and said what it waits for, once. Observe by ratifying a brief that names an unfinished run's change. The later hand-over was not reached. |
| 9 | not yet. The text says it has not been shown. |

## Units

| Unit | State | Result |
| --- | --- | --- |
| The whole brief, one plan (`docs/coding-agent/plans/completed/one-conversation-with-counsel-plan.md`) | done 2026-11-13 by the channel clock (final review APPROVED; closeout audit holds nothing) | Scenarios: prior state of each, not yet; no scenario demonstrated whole. Getting closer: yes. Before this unit nothing of any scenario had been observed; the range holds a first observation of parts of 1, 2, 3, 5 and 8, and text for every statement of the brief, with the validators and the census passing. No scenario is demonstrated whole, and what was seen rests on stand-ins and single runs. |
