# PR Review Monitoring

Read this reference when waiting on PR review rounds or arming review monitoring.

## What the tool is

- `scripts/pr-comment-watch.sh` is a stateless PR activity checker: it fires when a PR's comment count OR review count changes (zero-comment review rounds fire too).
- There are no baseline files. The agent's thread context is the state store: counts ride in as arguments and ride out in printed lines.
- PR spec syntax: `OWNER/REPO:PR[:comments[:reviews]]` — supply the last-known counts as the baseline; multiple specs are supported in every mode.
- Every probe/wait result line prints current counts; that printed line is the baseline for the next invocation.

## Mode selection by runtime

- Monitor-capable runtimes (e.g. Claude Code): arm the watch mode (default, `-i SECONDS`) as a persistent monitor after opening a PR or pushing fixes. It stays silent until the first change, prints one `NEW_ACTIVITY` line, and exits 0 — exit-on-first-change wakes the agent, silence costs nothing.
- No-Monitor runtimes with concurrent work: run `--once` probes at natural checkpoints. Without counts it initializes (`BASELINE ...`, exit 0); with counts it compares (`NEW_ACTIVITY`, exit 0, or `NO_CHANGE ...`, exit 3). Carry the printed counts forward as the next call's baseline.
- No-Monitor runtimes that are only waiting: chain bounded `--wait SECONDS` calls (duration required, no default). Each wait must stay below the runtime's foreground command limit — GitHub Copilot auto-backgrounds long-running scripts after a fixed time and returns control, so keep waits under that threshold and re-invoke, feeding each round's printed counts to the next call.
- Exit codes: 0 activity/baseline, 2 usage error, 3 no-change/deadline, 4 API failure — do not record a baseline from a failed call.

## Operating semantics

- Arming is a deliberate act at PR-open and fix-push moments — there is no standing automation.
- Posting your own replies changes the counts and fires the watcher on your own activity (self-induced fire). After handling a review round, restart the watcher or re-baseline from fresh counts.
- Keep poll intervals at 30 seconds or more to respect GitHub API rate limits.

## Fire semantics boundary

- A fire may automatically drive the respond/fix/re-review loop — triage new comments, apply fixes, push, reply, re-arm.
- Merge is the hard stop: a fire, and in particular a zero-comment review round, is state to report to the user, never authorization to merge; merging waits for explicit user authorization.
