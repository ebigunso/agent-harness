# Plan: PR Watcher Discoverability And Review-Round Steering

- status: in_progress
- generated: 2026-09-04
- last_updated: 2026-09-05
- work_type: mixed

## Goal
- Runtime agents find and run the bundled `pr-comment-watch.sh` at PR-open and fix-push moments instead of hand-rolling a poller, a broken watcher is distinguishable from a quiet one, and a review-round fire steers the agent to reconsider the design against the feature goal rather than only fix or defer.

## Definition of Done
- The git-workflow description names the script and its trigger moments; SKILL.md carries a no-hand-rolling core rule and a direct pointer to `pr-review-monitoring.md`; the entry skill's routing line names the moments.
- The script polls with one GraphQL call per spec, expands any member PR to its whole stack, prints one `ARMED` line per member once baselines exist, exits 4 when a watch-mode baseline cannot be established, and fires `TERMINAL` when a member is merged or closed.
- `pr-review-monitoring.md` documents the new output lines and carries a review-round handling section with four dispositions (fix, defer, decline, rethink) that routes rethink through the Replan Procedure, plus an extended stopping rubric.
- Validators green; Reviewer APPROVED.

## Scope / Non-goals
- Scope: `plugins/coding-agent-orchestration-harness/skills/git-workflow/**`, the routing line in `skills/orchestration-harness/SKILL.md`, plugin manifests at closeout.
- Non-goals (deferred, recorded here so they are not re-proposed as oversights): recording arming state in the plan Progress Log for compaction survival (background monitors survive compaction); a separate `--stack NUMBER` flag (superseded by automatic stack expansion, see Design); Windows hidden-console launcher or note (no reproduction; the single-call poll removes the multiplier anyway); Copilot-latency and self-fire operator observations; plugin hooks.

## Compatibility stance
- surface: `pr-comment-watch.sh` stdout contract and count semantics (watch mode gains `ARMED` and `TERMINAL` lines and exit 4; `comments` becomes GraphQL `totalCommentsCount` instead of the REST review-comment count; a spec expands to its whole stack).
- stance: break
- justification: the only locatable consumer is `pr-review-monitoring.md`, which is updated in the same change (Task_2). Counts are only ever compared against counts the script itself printed, so the semantic change cannot mix old and new baselines within one session. No target repository is known to parse the script's output beyond reading it as a Monitor event.

## Stack decision (2026-09-04)

GitHub stacks are a first-class object: REST `repos/O/R/stacks/N` and `repos/O/R/stacks` exist, the REST pull payload carries `.stack.{number,position,size}`, and GraphQL `PullRequest.stack` returns `PullRequestStack { number size baseRefName entries { position pullRequest {...} } }`. There is no GraphQL lookup by stack number; the stack is reached from any member PR. Stack and PR numbers never overlap.

Options weighed:
- A. Keep the REST per-PR poller and add `--stack N`, resolved once via REST `stacks/N`. Simple diff, but the agent must first discover the stack number, membership growth after arming is missed, and cost stays two REST endpoint processes per PR per poll plus a third for state, each paginating (a five-PR stack spawns fifteen or more subprocesses every interval).
- B. Move polling to one GraphQL query per spec that reads `pullRequest(number).stack.entries` and, for every member, `state`, `merged`, `reviews.totalCount`, and `totalCommentsCount`; fall back to the single PR when `stack` is null. One call per spec per poll at rate-limit cost 1 (overlapping specs cost one call each), membership growth picked up on every poll, terminal state included for free, and the agent passes the PR it just opened.
- C. REST `stacks/N` for expansion plus REST per-PR polling. Worse than B on every axis except familiarity.

Chosen: B. It is the smallest runtime burden (arm with any member PR, re-arm with the printed spec), the cheapest poll, and it deletes the `--paginate`/`wc -l` invariant rather than extending it. Verified on this repository: stack 52 (PRs 50, 51) resolves from either member in one query; PR 49 returns `stack: null`.

Change-detection scope: `totalCommentsCount` is GitHub's aggregate of issue comments, review bodies, and inline comments, not the old inline-only REST count; `reviews.totalCount` counts review objects, and a reply posted into a thread arrives inside its own empty-body review, so both replies and zero-comment review rounds raise it (measured on PRs 36, 39, 47, 49). The watcher promises to fire on any change to either count. It does not detect count-preserving edits or a deletion offset by an addition, which the REST version did not detect either.

## Design

### Skill routing (Task_1)
- git-workflow frontmatter description: keep the existing scope sentence, then add the trigger: after opening a PR or pushing review fixes, arm review monitoring with the bundled `scripts/pr-comment-watch.sh` rather than an inline polling loop. The description is the only text visible from the skills listing; it must carry both the artifact name and the moment.
- git-workflow SKILL.md core rule 7: PR activity watching uses the bundled `scripts/pr-comment-watch.sh`; never compose an inline `gh` polling loop, even when a runtime tool's own example shows one.
- git-workflow SKILL.md progressive disclosure: add "If you are arming review monitoring after a PR open or fix push, or waiting on a review round: read `references/pr-review-monitoring.md`" as a sibling of the pr-authoring line, so the reference is one hop from SKILL.md.
- orchestration-harness SKILL.md routing table line: replace "Git safety, commit/PR workflow, and external review monitoring: `git-workflow`" with a line naming the moments (PR open, fix push, waiting on review rounds) and stating that git-workflow bundles the watcher. No script path in the entry skill; adapters and entry skill route to skills.

### Script (Task_3)
- Spec syntax gains an optional state: `OWNER/REPO:PR[:comments[:reviews[:state]]]`, `state` in `open|merged|closed`. An optional literal `spec=` prefix on any argument is stripped before parsing, so a printed token can be copied verbatim. Multiple specs in every mode. `comments` means GraphQL `totalCommentsCount`; `reviews` means `reviews.totalCount`.
- Baseline defaults, exactly: a bare `OWNER/REPO:PR` has no supplied baseline and takes fetched counts and fetched state; a spec with counts but no state has baseline state `open` (so old count-only inputs still detect a transition); an explicit state overrides. Supplied values win over fetched ones for that member.
- Re-feed contract: every printed line ends with `spec=OWNER/REPO:PR:comments:reviews:state`, one token per member, copied verbatim (prefix included) as the next invocation's argument. `ARMED`, `BASELINE`, `NO_CHANGE`, `NEW_ACTIVITY`, and `TERMINAL` all carry it (`TERMINAL` carries the current counts with the terminal state). A member whose baseline state is `merged` or `closed` is terminal at baseline and never fires, on counts or on state.
- Poll unit: one `gh api graphql` call per spec, no `--paginate`, no `wc -l`. Query selects `number state merged reviews{totalCount} totalCommentsCount` on the root PR and on every `stack.entries(first:100).nodes.pullRequest`, plus `stack.number`. If `stack` is null, the root PR is the only member. Parse with `gh api graphql --jq` into one `number stack comments reviews state` row per member; no separate `jq`.
- Member identity is `OWNER/REPO` plus PR number. When several specs resolve to the same member, a supplied baseline wins over a fetched one; two supplied baselines for the same member that differ are a usage error (exit 2); identical duplicates collapse.
- Startup, all modes: every spec is queried once. Watch mode exits 4 with `error: could not fetch counts for repo=<r> pr=<n>` on stderr if any spec's query fails, supplied counts or not, because membership comes only from the query. Members discovered on a later poll (stack grew) are baselined silently on that poll.
- `ARMED`: watch mode only, once, after startup: one line per member `ARMED repo=<r> pr=<n> stack=<s|none> comments=<c> reviews=<v> state=<state> spec=...`. Not a heartbeat; polls stay silent.
- `TERMINAL`: when a member whose baseline state is `open` is observed merged or closed, print `TERMINAL repo=<r> pr=<n> stack=<s|none> state=merged|closed spec=...`. Terminal takes precedence over a count change on the same member in the same poll. A member terminal at baseline never fires. Watch and wait modes exit 0 on the first line printed; `--once` prints every changed member and exits 0.
- Transient query failure after startup keeps the existing per-mode rule: no change in watch mode, exit 4 in probe modes.
- Replace the paginate invariant in the maintainer comment block with the single-query invariant; keep the no-heartbeat, self-induced-fire, and per-mode failure invariants; add ARMED-is-not-a-heartbeat and terminal-precedence.
- Bash and `gh` only; parse the response with `gh api graphql --jq`, no separate `jq` dependency.

### Reference (Task_2)
- Update "What the tool is" and "Mode selection by runtime" for the single-query poll, stack expansion (arm with any member PR; the whole stack is watched; re-arm with the same spec after handling a round), the new count semantics, `ARMED`, exit 4 at watch startup, and `TERMINAL`; state that a Monitor that never printed `ARMED` is dead, not quiet.
- Stack authoring guidance is out of scope here; it lives in the gh-stack-awareness plan's `references/stacked-prs.md`. This reference only states that any member PR arms the whole stack.
- Replace the one-clause fire handling in "Fire semantics boundary" with a "Review-round handling" section:
  - Read the whole round before fixing anything, then re-read the plan Goal and Definition of Done and ask what the round says about the feature, not only the lines it points at.
  - Four dispositions per comment: fix locally; defer with a recorded reason; decline as a judgment call with the reason in the thread; rethink, when the comment reveals that the implementation or the requirement behind it may not earn its place, or that a different shape serves the goal better.
  - Rethink routes to the orchestration-harness Replan Procedure: recorded in the plan Decision Log and proposed to the user as a plan delta; never executed silently on a fire. Merge remains the hard stop.
  - Repeated rounds on one area are a churn signal: apply the value-audit verdicts in `engineering-quality-baselines/references/long-horizon-audit.md` at that event, not continuously.
- Stopping rubric: add a fourth condition, that any redesign question surfaced by a round has been ruled on by the user.
- Keep the reference free of provenance or session narrative per `skills-maintenance` rule 3.

## Context (workspace)
- `plugins/coding-agent-orchestration-harness/skills/git-workflow/SKILL.md`, `references/pr-authoring.md`, `references/pr-review-monitoring.md`, `scripts/pr-comment-watch.sh`.
- `plugins/coding-agent-orchestration-harness/skills/orchestration-harness/SKILL.md` routing table (line 114) and Replan Triggers / Procedure.
- `docs/coding-agent/plans/completed/pr-comment-watch-integration-plan.md`: original design, invariants, and the same parallel docs/script dispatch split.
- Research waived: the brief supplied the failure trace, and every affected file was read in this session; scope is four files.

## Open Questions (max 3)
- None.

## Assumptions
- A1: Version bump to 0.14.0 at closeout, since the script's output contract changes; flag in the PR if a patch bump is preferred.
- A2: Script verification uses read-only `gh api` calls against real merged and open PRs in ebigunso repositories; `TERMINAL` is verified against a merged PR and a closed-unmerged PR.
- A3: Per the model-routing convention, the script task goes to a Codex worker via agmsg and the prose tasks to Claude workers; owns are disjoint so both dispatch in one wave.

## Tasks

### Task_1: Skill routing edits
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/git-workflow/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/orchestration-harness/SKILL.md
- depends_on: []
- description: |
  Apply the "Skill routing" design: frontmatter description, core rule 7, the direct progressive-disclosure line, and the entry-skill routing line. Keep SKILL.md to routing and core rules; no procedure text.
- acceptance:
  - git-workflow description names `pr-comment-watch.sh` and the PR-open / fix-push moments.
  - SKILL.md has the no-hand-rolling core rule and a direct pointer to `references/pr-review-monitoring.md`.
  - orchestration-harness routing line names the moments and the bundled watcher without a script path.
  - No other lines in either file change.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review vs Design; frontmatter reads description-first per skills-maintenance"

### Task_2: Reference update and review-round handling
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/git-workflow/references/pr-review-monitoring.md
- depends_on: []
- description: |
  Apply the "Reference" design: document the single-query poll, stack expansion, count semantics, ARMED, watch-mode exit 4, and TERMINAL; replace fire handling with the review-round handling section; extend the stopping rubric. Write against the plan's script spec, not the script file, so it runs parallel to Task_3.
- acceptance:
  - Stack expansion, new output lines, and exit code documented with the dead-versus-quiet distinction.
  - Review-round handling section present with the four dispositions, rethink routed to the Replan Procedure, churn routed to the value audit, and merge kept as the hard stop.
  - Stopping rubric has the fourth condition.
  - No provenance or session narrative.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py"
  - kind: review
    required: true
    owner: reviewer
    detail: "Docs review vs Design, including consistency with the landed script's actual output lines and exit codes"

### Task_3: Script single-query poll, stack expansion, ARMED, dead-baseline exit, and TERMINAL
- type: impl
- owns:
  - plugins/coding-agent-orchestration-harness/skills/git-workflow/scripts/pr-comment-watch.sh
  - plugins/coding-agent-orchestration-harness/skills/git-workflow/scripts/pr-comment-watch-selfcheck.sh
- depends_on: []
- description: |
  Apply the "Script" design. Bash and gh only. Two evidence layers:
  Live smoke (read-only, ebigunso/agent-harness, every PR there is merged): --once on bare PR 50 (stack 52) prints BASELINE lines for 50 and 51 with stack=52, fetched state=merged, and a spec= token each, exit 0; --once on bare PR 49 prints one BASELINE line with stack=none; --once with specs 50 and 51 together tracks each member once; copying a printed `spec=...` token verbatim into argv and running --once exits 3 with NO_CHANGE; the same token with lower counts still exits 3 (terminal baseline never fires on counts); supplying `:c:r:open` against merged PR 49 fires TERMINAL state=merged, and copying that line's token verbatim then exits 3; supplying `:c:r` with no state against PR 49 also fires TERMINAL (omitted state defaults to open); watch mode on a nonexistent PR exits 4 with a stderr error even with counts supplied; missing --wait duration and malformed specs (including a bad state word) exit 2.
  Deterministic self-check (`pr-comment-watch-selfcheck.sh`): creates a temp dir with a fake `gh` first on PATH that replays scripted GraphQL responses in sequence, then asserts exit codes and stdout for, on OPEN fixtures unless stated: watch mode ARMED then silence then NEW_ACTIVITY on a reviews-only increment with comments unchanged (zero-comment review round); NEW_ACTIVITY on a comments-only increment with reviews unchanged; stack growth baselined silently; transient failure treated as no change in watch mode and exit 4 in --once; terminal and count change on the same member in one poll printing TERMINAL only; state=closed transition; bare merged member initializes as BASELINE state=merged with no fire; explicit `:merged` baseline never fires; same PR number in two repositories tracked as two members; overlapping specs where one member is supplied explicitly and also fetched as a stack member of another spec, in both argument orders, with the supplied baseline winning; identical supplied duplicates collapsing and differing ones exiting 2 in both orders; a `spec=`-prefixed argv token parsing identically to the bare form; --wait exiting 0 on an initial change, exiting 3 with NO_CHANGE at the deadline, and exiting 4 on API failure; exactly one gh invocation per spec per poll. Plain bash, no framework; a failing assertion prints the case name and exits 1.
- acceptance:
  - Single-query poll, stack expansion, ARMED, exit 4 at watch startup, and TERMINAL behave per Design, evidenced by live smoke output and a passing self-check.
  - No `--paginate` or `wc -l` remains; invariant comment block updated per Design.
  - Poll-time silence preserved: no output line other than NEW_ACTIVITY or TERMINAL after ARMED.
  - Every printed line carries a spec= token that is valid re-feed input, and the merged and terminal round trips show no repeat fire.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "Live smoke list above against real PRs (read-only gh api), outputs captured in the report"
  - kind: command
    required: true
    owner: worker
    detail: "bash skills/git-workflow/scripts/pr-comment-watch-selfcheck.sh exits 0; output captured in the report"
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py"
  - kind: review
    required: true
    owner: reviewer
    detail: "Line-by-line shell review vs Design: query shape, member dedupe, baseline precedence, TERMINAL over counts, per-mode failure handling, quoting"

### Task_4: Independent review
- type: review
- owns: []
- depends_on: [Task_1, Task_2, Task_3]
- description: |
  Reviewer checks the script line by line, reruns the live smoke list and the self-check independently, and checks the self-check's fake responses against the real query shape; checks the reference against the landed script (spec drift between parallel tasks); checks the routing edits for trigger precision and SKILL.md leanness; confirms the review-round section routes rethink to the Replan Procedure rather than authorizing silent redesign.
- acceptance:
  - Reviewer status is APPROVED
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Full-diff review plus independent rerun of the live smoke list and the self-check"

### Task_5: Closeout
- type: chore
- owns:
  - plugins/coding-agent-orchestration-harness/.claude-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.codex-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.github/plugin/plugin.json
  - docs/coding-agent/plans/active/pr-watch-discoverability-plan.md
  - docs/coding-agent/rules/*.md
- depends_on: [Task_4]
- description: |
  Orchestrator-owned: version bump per A1; full validators; targeted rule freshness check because the change touches rule-source patterns in `docs/coding-agent/rules/_lifecycle.json` (update the affected rule file or record an explicit waiver with reason in the Decision Log; no full bootstrap); logical commits (routing, reference, script plus self-check as separate commits); open the PR; arm the bundled watcher on it; append the final Progress Log entry, set status done, and move this plan to `docs/coding-agent/plans/completed/`.
- acceptance:
  - Version bumped in all three manifests; validators green.
  - Rule freshness resolved: rule file updated or waiver recorded.
  - PR open with the watcher armed, evidenced by the PR URL and the ARMED lines in the Progress Log.
  - Plan status done and file moved to completed.
- validation:
  - kind: command
    required: true
    owner: orchestrator
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py && python scripts/run_validation_smoke_tests.py; from repo root: git diff --check"
  - kind: review
    required: true
    owner: orchestrator
    detail: "Progress Log carries PR URL, ARMED output, and the rule-freshness decision before the plan is moved"

## Task Waves (explicit parallel dispatch sets)

- Wave 1 (parallel): [Task_1, Task_2, Task_3]
- Wave 2: [Task_4]
- Wave 3: [Task_5]

## Rollback / Safety
- All changes on `feature/2026-09-04/pr-watch-discoverability`; revert by dropping the branch. Script verification is read-only against GitHub.

## Progress Log (append-only)

Append-only editing rule (applies to both logs below): when appending an entry, anchor the edit on the previous entry and reproduce it (or anchor on the section's tail marker) so the edit inserts rather than replaces, and verify afterward that the log grew.

- (none yet)

## Decision Log (append-only; re-plans and major discoveries)

- 2026-09-04 Decision: scope cut from the assessment.
  - Trigger / new insight: user ruled that compaction-survival logging, the Windows console note, and the operator observations are not needed now; background monitors survive compaction, and better skill routing is sufficient.
  - Plan delta (what changed): those items and `--stack` are listed as non-goals rather than tasks.
  - Tradeoffs considered: none deferred item blocks the discoverability goal.
  - User approval: yes (this conversation).
- 2026-09-04 Decision: stack support via automatic expansion on a GraphQL poll, not a `--stack` flag.
  - Trigger / new insight: user ruled that stacked PRs use `gh stack` from now on and asked for the watcher's shape to be decided on simplicity, runtime burden, and script cost. API probing confirmed `PullRequest.stack` in GraphQL and REST `stacks/N`.
  - Plan delta (what changed): Task_3 becomes a poll rewrite (one GraphQL call per spec, stack expansion, new count semantics); Task_2 gains pr-authoring.md and a Stacked PRs section; compatibility stance widened; `--stack` and the GraphQL-folding item leave the non-goals.
  - Tradeoffs considered: options A/B/C in the Stack decision section; B chosen for one call per stack per poll and no new agent-side inputs, at the cost of a larger script diff and a count-semantics break.
  - User approval: pending (this revision).
- 2026-09-04 Decision: stacked-PR authoring guidance moves to the gh-stack-awareness plan.
  - Trigger / new insight: user asked for gh stack awareness as a separate plan and branch.
  - Plan delta (what changed): Task_2 drops pr-authoring.md from owns and the Stacked PRs section from its description; the sibling plan's branch will be stacked on this one.
  - Tradeoffs considered: keeping a short section here would create two owners for the same topic across two branches.
  - User approval: yes (this conversation).
- 2026-09-05 Decision: Codex reviewer round applied.
  - Trigger / new insight: reviewer findings P1-1 to P1-7 plus a shared closeout gap: count-only specs could not round-trip terminal state; the query omitted root-PR counts; members keyed by PR number collide across repositories; supplied counts exempted the startup query so ARMED could be printed for a dead watcher; the all-real-PR matrix was not reproducible because every PR in this repository is merged; the change-detection claim overreached; the cost wording misstated the current script; closeout omitted plan lifecycle and rule freshness.
  - Plan delta (what changed): spec syntax gains an optional state and every printed line carries a re-feedable spec= token; root counts added to the query; member identity is repo plus PR with conflicting supplied baselines rejected; startup query is mandatory in watch mode; evidence split into a live smoke list and a deterministic fake-gh self-check script added to Task_3 owns; change-detection scope and cost wording corrected; Task_5 owns and acceptance extended to plan lifecycle, rule freshness, and PR/ARMED evidence.
  - Tradeoffs considered: scoping terminal detection to in-process observations only was the alternative for P1-1; carrying state in the spec keeps the stateless re-feed model intact for no-Monitor runtimes.
  - User approval: pending.
- 2026-09-05 Decision: delta re-review findings D1 to D4 applied.
  - Trigger / new insight: the `spec=` token was outside the declared argument grammar; the live smoke expected NEW_ACTIVITY on a terminal baseline; the state default was ambiguous for bare versus count-only specs; the self-check did not separate review-only from comment-only detection or test supplied-over-fetched precedence.
  - Plan delta (what changed): parser strips an optional literal `spec=` prefix; baseline defaults defined exactly (bare takes fetched state, counts-only defaults to open, explicit overrides); live smoke expects NO_CHANGE on terminal baselines and moves count-change firing to open fixtures in the self-check; self-check gains reviews-only, comments-only, bare-merged, explicit-merged, counts-without-state, supplied-over-fetched in both orders, and prefixed-token cases.
  - Tradeoffs considered: none; all four were contract contradictions.
  - User approval: pending.

## Notes
- Risks: Task_2 and Task_3 run in parallel against the plan spec; Reviewer owns the drift check. The script diff is larger than the first draft; the behavioral matrix and a Codex worker's shell scrutiny are the controls.
- Edge cases: a PR that is merged before the watcher's first poll is terminal at baseline and never fires; a member removed from a stack disappears from the query and is dropped silently; a supplied-baseline spec still gets an ARMED line using the supplied counts and state; stacks larger than 100 entries are not handled; a closed-unmerged test PR must exist in an ebigunso repository for the state=closed case, or that case is waived with a note.
