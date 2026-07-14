# Async Dispatch Lifecycle

Use this reference only for runtimes that launch Researcher, Worker, or Reviewer agents asynchronously or as background processes.

This is Orchestrator-owned lifecycle guidance. It does not change subagent role behavior or report contracts.

If the runtime setup uses multiple long-lived agents that stay alive across dispatches and communicate over an external channel, also read references/persistent-peer-dispatch.md.

## Parent-Owned Lifecycle

1. Dispatch the child agent with one bounded objective.
2. Track the active child process in Orchestrator state.
3. Wait at dependency boundaries.
4. Validate and integrate the final report.
5. Close or terminate the completed child process when the runtime supports it.

## Active Dispatch State

Track enough state to avoid losing, duplicating, or misrouting background work:

- logical role: Researcher, Worker, or Reviewer;
- runtime physical agent name;
- assigned objective or `Task_X`;
- `owns` / scope boundaries;
- expected output contract;
- status: `dispatched | running | reported | integrated | closed | cancelled | blocked`;
- cleanup status: `pending | done | unavailable`.

## Waiting Behavior

- No report yet means `running`, not failed.
- Do not prompt for an immediate final report right after dispatch.
- Poll only when the runtime requires polling or when a dependency boundary is reached.
- Do not duplicate active child work on the main thread unless the dispatch is cancelled, blocked, or explicitly reassigned.
- If a child is blocked, record the blocker before deciding whether to reassign the work.
- Wait substantially longer before force-closing background agents unless they are clearly blocked, conflicting with newer direction, or unsafe.
- Use checkpoint prompts to redirect or narrow work, not as a prelude to termination.

## Report Integration

- A final report means the assigned work is complete.
- Validate the report against the expected output contract.
- Integrate findings, changed-file summaries, validation evidence, blockers, and candidates into the plan or wave state.
- Do not treat an idle-open runtime process as evidence that the subagent assignment is unfinished.

## Cleanup Behavior

- After report validation and integration, close or terminate the runtime child process when the platform exposes that action.
- If no close or terminate action exists, record cleanup as `unavailable`.
- Do not reuse a completed process for unrelated work.
- Keep cleanup status separate from task status: a task may be integrated while process cleanup is still `pending` or `unavailable`.
