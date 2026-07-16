# Goal Engines (Runtime Mapping)
Read this only when running a goal loop on a runtime with a native goal/autopilot engine. The manual loop needs no engine — skip this reference entirely in that case.

## Shared rule (applies to every engine)

- The harness goal condition always includes the escalation clause: reaching an ask-now or abort state is a successful termination of the loop, not a failure to grind through.
- Engine mechanisms (evaluators, continuation nudges, tracked state) never override an escalation state. Governance lives in harness content; engines only supply continuity.

## Claude Code `/goal`

- Evaluator-gated turn continuation: an independent fast model checks the goal condition after each turn and decides whether the loop continues.
- Goals survive `--resume` — the loop can be interrupted and picked up without losing the goal.
- Give the harness goal condition (target + invariants + escalation clause) verbatim as the `/goal` condition.
- The platform evaluator's judgment is advisory. The harness's evidence rules and independent assessment decide completion — never the evaluator alone.

## Codex goals

- Behind the `features.goals` opt-in; without it there is no engine and the engine-less baseline below applies.
- Goals are thread-attached tracked state with pause/resume/clear.
- Continuation is semi-manual: the engine tracks the goal but does not drive turns. The harness cadence drives the loop, with the goal held as tracked state.

## GitHub Copilot Autopilot

- `task_complete`-gated: the loop ends when the agent calls `task_complete`.
- The CLI injects a synthetic "you aren't done" continuation nudge when a loop ends without `task_complete`. The nudge must NEVER override an ask-now/abort state — the escalation clause is part of task completion, so an escalated stop IS done.
- Set `--max-autopilot-continues` as a coarse backstop, consistent with the envelope's iteration budget. It is a safety cap, never a load-bearing control.

## Engine-less baseline

- With no engine, the loop runs manually: each iteration is a prompted turn.
- Governance is identical — same condition, envelope, journal, escalation, and assessment rules.
- Engines add continuity, never authority.
