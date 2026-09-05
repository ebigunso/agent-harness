# PR Review Monitoring

Read this reference when arming review monitoring after a PR open or fix push, or when waiting on and handling a review round.

## What the tool is

- `scripts/pr-comment-watch.sh` is a stateless PR activity checker: it fires when a PR's comment count or review count changes, or when an open PR becomes merged or closed.
- Poll unit: one `gh api graphql` call per spec per poll. A spec names any PR; the watcher expands it to that PR's whole stack and tracks every member (`stack=none` when the PR is not stacked). Arm with the PR you just opened; the whole stack is watched. Stack authoring: `stacked-prs.md`.
- Count semantics: `comments` is GitHub's `totalCommentsCount` (issue comments, review bodies, and inline comments together); `reviews` is `reviews.totalCount`. A reply posted into a thread arrives as its own review, so replies and zero-comment review rounds both raise `reviews`. Count-preserving edits are not detected.
- There are no baseline files. The agent's thread context is the state store: baselines ride in as arguments and ride out in printed lines.
- Spec syntax: `OWNER/REPO:PR[:comments[:reviews[:state]]]`, `state` in `open|merged|closed`; a leading `spec=` on any argument is stripped. Multiple specs in every mode. Defaults: a bare `OWNER/REPO:PR` takes fetched counts and fetched state; counts given without a state are baselined as `open`; an explicit state overrides. Supplied values win over fetched ones for that member; two supplied baselines for one member that differ are a usage error.
- Re-feed contract: every printed line ends with `spec=OWNER/REPO:PR:comments:reviews:state`, one line per member. Copy each token verbatim, prefix included, as the next invocation's argument. A member whose baseline state is `merged` or `closed` is terminal at baseline and never fires, on counts or on state.

## Output lines

- `BASELINE` (`--once` only): a member without a supplied baseline, including a stack sibling discovered by expansion. It carries the token to feed forward.
- `ARMED`: watch mode only, once per member after startup, carrying the baseline counts and state. It is not a heartbeat; polls stay silent. A Monitor that never printed `ARMED` is dead, not quiet: check the runtime and the spec before assuming a slow reviewer.
- `NEW_ACTIVITY`: a count changed on a member whose baseline state is `open`.
- `TERMINAL ... state=merged|closed`: an `open` member was observed merged or closed. It takes precedence over a count change on the same member in the same poll.
- `NO_CHANGE` (probe modes): no triggering event for that member (a terminal baseline with different counts is still `NO_CHANGE`). `--wait` prints one per current member at the deadline.
- Exit code is decided per command, not per line: 0 if any `NEW_ACTIVITY` or `TERMINAL` was printed, or (`--once`) if any input spec was bare; otherwise 3.
- Members that join the stack after arming are baselined silently on the poll that first sees them; members that leave the stack disappear from the output. Result tokens describe the latest successful poll; `ARMED` reports the armed baseline.
- The script needs Bash 4 or later.

## Mode selection by runtime

- Monitor-capable runtimes (e.g. Claude Code): arm the watch mode (the default; `-i SECONDS` optionally overrides the 120s poll interval) as a persistent monitor after opening a PR or pushing fixes. It prints `ARMED` per member, stays silent until the first change, prints one `NEW_ACTIVITY` or `TERMINAL` line, and exits 0; exit-on-first-change wakes the agent, silence costs nothing.
- No-Monitor runtimes with concurrent work: run `--once` probes at natural checkpoints. Without counts it initializes (`BASELINE`, exit 0); with counts it compares (`NEW_ACTIVITY` or `TERMINAL`, exit 0; `NO_CHANGE`, exit 3), printing every changed member. Carry the printed `spec=` tokens forward as the next call's arguments.
- No-Monitor runtimes that are only waiting: chain bounded `--wait SECONDS` calls (duration required, no default). Each wait must stay below the runtime's foreground command limit; GitHub Copilot auto-backgrounds long-running scripts after a fixed time and returns control, so keep waits under that threshold and re-invoke, feeding each round's printed tokens to the next call.
- Exit codes: 0 activity/baseline/terminal, 2 usage error (malformed spec, bad state word, conflicting baselines, missing wait duration), 3 no-change/deadline, 4 API failure. Watch mode exits 4 at startup when any spec cannot be fetched, supplied counts or not, because stack membership comes only from the query. After startup a transient failure is no change in watch mode and exit 4 in probe modes. Do not record a baseline from a failed call.

## Operating semantics

- Arming is a deliberate act at PR-open and fix-push moments; there is no standing automation.
- Posting your own replies changes the counts and fires the watcher on your own activity (self-induced fire). After handling a review round, re-arm with the `spec=` tokens from the line that fired, or from a fresh `--once` probe if you posted afterwards.
- Keep poll intervals at 30 seconds or more to respect GitHub API rate limits.

## Review-round handling

- Read the whole round before fixing anything. Then re-read the plan Goal and Definition of Done and ask what the round says about the feature, not only about the lines it points at.
- Give each comment one disposition:
  - fix: apply locally.
  - defer: record the reason.
  - decline: a judgment call, with the reason stated in the thread.
  - rethink: the comment reveals that the implementation, or the requirement behind it, may not earn its place, or that a different shape serves the goal better.
- Rethink routes to the orchestration-harness Replan Procedure: record it in the plan Decision Log and propose it to the user as a plan delta. A redesign is never executed silently on a fire.
- Repeated rounds on one area are a churn signal: at that event, apply the value-audit verdicts in `engineering-quality-baselines/references/long-horizon-audit.md` to the area. Not continuously.
- Merge is the hard stop: a fire, and in particular a zero-comment review round or a `TERMINAL` line, is state to report to the user, never authorization to merge; merging waits for explicit user authorization.
- After the round: push, reply, re-arm.

## Stopping rubric

Stop re-requesting external review only when all hold: the latest round produced zero new substantive comments; every prior thread is resolved or explicitly deferred with a recorded reason; any remaining disagreement is a judgment call already ruled on, not an unanswered correctness claim; and any redesign question surfaced by a round has been ruled on by the user. Do not stop on fatigue or round count alone.
