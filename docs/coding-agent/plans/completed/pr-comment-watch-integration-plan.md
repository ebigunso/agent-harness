# Plan: Integrate The PR Comment Watch Script Into The Harness

- status: done (Reviewer APPROVED 2026-07-15)
- generated: 2026-07-15
- last_updated: 2026-07-15
- work_type: mixed

## Goal
- Ship the pr-comment-watch script as a harness-bundled tool with runtime-appropriate consumption modes, so agents on any platform can notice PR review activity without token-burning polling.

## Definition of Done
- Adapted script bundled under git-workflow with all three modes working (verified against a real PR); gated `pr-review-monitoring.md` reference with per-runtime guidance; routing in place; validators pass; Reviewer APPROVED.

## Scope / Non-goals
- Scope: `plugins/coding-agent-orchestration-harness/skills/git-workflow/**`; plugin manifests at closeout.
- Non-goals: global auto-arming or scheduling machinery; issue-comment watching and other extensions (future candidates); changes outside git-workflow; deleting the staged original in `~/staging` (user-owned, outside the repo).

## Design (converged with user, 2026-07-15 via agmsg)

Script (`skills/git-workflow/scripts/pr-comment-watch.sh`), adapted from the user's staged original. Fully stateless: the agent's thread context is the state store; no baseline files anywhere.

- PR spec syntax: `OWNER/REPO:PR[:comments[:reviews]]` — optional supplied baseline counts; multiple specs supported in every mode.
- Change detection: comments count OR reviews count differs (zero-comment review rounds must fire — they are the proceed-to-merge signal).
- Modes:
  - Watch (default, `-i SECONDS` interval, current behavior): in-memory baseline at startup (or supplied counts), silent until first change, one `NEW_ACTIVITY` line, exit 0. For Monitor-capable runtimes.
  - `--once`: single check. With supplied counts: compare and print `NEW_ACTIVITY ...` (exit 0) or `NO_CHANGE repo=... pr=... comments=N reviews=R` (exit 3). Without counts: initialization — print `BASELINE repo=... pr=... comments=N reviews=R`, exit 0. Probe/init output always includes current counts: that line is the next invocation's baseline.
  - `--wait SECONDS`: bounded foreground poll; duration is REQUIRED with no default (a wrong default fails silently and differently per runtime; a missing argument fails loudly). Supplied counts honored so between-round activity fires immediately; otherwise snapshot at start. Exit 0 with `NEW_ACTIVITY` on change; exit 3 with a final `NO_CHANGE` counts line on deadline.
- Exit codes: 0 activity/baseline-init; 2 usage error; 3 no-change/deadline; 4 API failure in `--once`/`--wait` when counts could not be fetched (so agents never record a bogus baseline). Watch mode keeps treating transient API failure as no-change.
- Preserved invariants (kept as maintainer comments in the script, no provenance narrative): `gh api --paginate` on every count; exit-on-first-change with no heartbeat in watch mode; self-induced fires after posting replies (restart/re-baseline after handling a round).

Reference (`skills/git-workflow/references/pr-review-monitoring.md`), gated: read when waiting on PR review rounds or arming review monitoring. Content: mode selection by runtime — Monitor-capable runtimes arm the persistent watcher after PR-open/fix-push; no-Monitor runtimes with concurrent work run `--once` probes at natural checkpoints, carrying counts forward in context; no-Monitor runtimes that are only waiting chain bounded `--wait` calls, keeping each below the runtime's foreground command limit (GitHub Copilot auto-backgrounds long-running scripts, so keep waits under its threshold and re-invoke). Arming is a deliberate act at PR-open/fix-push moments — no standing automation. Include the self-induced-fire and re-baseline-after-round semantics.

Routing: one line in `references/pr-authoring.md` (review-loop section) pointing at the new reference; SKILL.md already routes to pr-authoring for review loops — add a SKILL.md line only if the reference is otherwise unreachable.

Fire semantics (user directive 2026-07-15, refined): a watcher fire may automatically drive the respond/fix/re-review loop — triage the new comments, apply fixes, push, reply, re-arm. The merge boundary is the hard stop: a fire, and in particular a zero-comment review round, is state to report, never authorization to merge; merging waits for the user. The reference must state this boundary explicitly.

Dispatch split (user directive 2026-07-15): script implementation goes to the Codex worker (agent-harness-worker via agmsg — detail/shell strengths); reference/skill prose goes to a Claude worker (writing strengths). Owns are disjoint (scripts/ vs references/ + pr-authoring.md), so both dispatch in one parallel wave.

## Context (workspace)
- Original script + README: `~/staging/pr-comment-watch/` (read this session; design notes incorporated).
- Live usage evidence: two rounds on agent-harness PR #35 (comment-count fire) and the zero-comment round on PR #34 (the missed-signal case motivating review-count detection).
- Research waived: design converged with user over three agmsg rounds; script and packaging targets fully inspected this session.

## Open Questions (max 3)
- None; design converged.

## Assumptions
- A1: Version bump to 0.6.1 at closeout; flag to user in the PR if they prefer a minor bump for the new bundled tool.
- A2: Script behavioral verification may use read-only `gh api` calls against real merged PRs in ebigunso repos (no mutations).

## Tasks

### Task_1: Adapt and bundle the script (Codex worker)
- type: impl
- owns:
  - plugins/coding-agent-orchestration-harness/skills/git-workflow/scripts/**
- depends_on: []
- description: |
  Implement the script per Design: stateless, three modes, spec syntax with optional counts, review-count firing, exit codes 0/2/3/4. Bash only, no new dependencies beyond gh (keep the wc -l counting pattern). Behavioral verification against a real merged PR (read-only): --once init prints BASELINE with correct counts; --once with matching counts exits 3 with NO_CHANGE; --once with mismatched counts exits 0 with NEW_ACTIVITY showing was/now; --wait 5 with matching counts exits 3 after the deadline; --wait with mismatched counts exits 0 immediately; missing --wait duration and malformed specs exit 2; watch mode still takes a startup baseline and stays silent (bounded manual check).
- acceptance:
  - All three modes and exit codes behave per Design, evidenced by captured command outputs.
  - Script retains the paginate/no-heartbeat/self-fire invariants as maintainer comments.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "Behavioral mode/exit-code matrix against a real merged PR (read-only gh api), outputs captured in the report"
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py"
  - kind: review
    required: true
    owner: reviewer
    detail: "Line-by-line shell review vs Design"

### Task_2: Write the gated pr-review-monitoring reference (Claude worker)
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/git-workflow/references/**
- depends_on: []
- description: |
  Write references/pr-review-monitoring.md per Design (mode selection by runtime, Copilot auto-background constraint, re-baseline-after-round and self-fire semantics, arming as a deliberate act) with the fire-semantics boundary stated explicitly: a fire may automatically drive the respond/fix/re-review loop, but merge is the hard stop — a fire, including a zero-comment review round, is reported state and never merge authorization. Add one routing line in pr-authoring.md. Write against the plan's CLI spec (not the script file), so it can run parallel to Task_1.
- acceptance:
  - Reference gated with its condition at top; fire-semantics boundary explicit (automated comment handling allowed, merge waits for the user); routing line in place; no duplication with pr-authoring.md.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py"
  - kind: review
    required: true
    owner: reviewer
    detail: "Docs review vs Design, including CLI-spec consistency with the landed script"

### Task_3: Independent review
- type: review
- owns: []
- depends_on: [Task_1, Task_2]
- description: |
  Reviewer scrutinizes the script line by line (quoting, pagination, arg parsing, exit-code paths, multi-spec loops, API-failure handling), reruns the behavioral matrix independently, and checks the reference against the Design and against the script's actual CLI (spec drift between parallel tasks), including the notify-only rule.
- acceptance:
  - Reviewer status is APPROVED
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Full-diff review plus independent rerun of the behavioral matrix"

### Task_4: Closeout
- type: chore
- owns:
  - plugins/coding-agent-orchestration-harness/.claude-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.codex-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.github/plugin/plugin.json
- depends_on: [Task_3]
- description: |
  Orchestrator-owned: version bump per A1, full validators, logical commits, PR.
- acceptance:
  - Version bumped; validators green; PR open.
- validation:
  - kind: command
    required: true
    owner: orchestrator
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py && python scripts/run_validation_smoke_tests.py; from repo root: git diff --check"

## Task Waves (explicit parallel dispatch sets)

- Wave 1 (parallel): [Task_1, Task_2]
- Wave 2: [Task_3]
- Wave 3: [Task_4]

## Rollback / Safety
- New files plus one routing line on `feature/2026-07-15/pr-comment-watch-integration`; revert by dropping the branch. Script verification is read-only against GitHub.

## Progress Log (append-only)

- 2026-07-15 Wave 1 partial: [Task_2 done; Task_1 in progress]
  - Summary: Task_2 (Claude) delivered pr-review-monitoring.md + one routing line, validator green. Task_1 (codex) started after a delivery nudge; its real-PR gh validation is blocked by invalid gh auth in the codex terminal (no token override attempted).
  - Validation evidence: Task_2 validate_harness_package.py pass.
  - Notes: validation ownership for the Task_1 real-PR behavioral matrix reassigned Worker -> Orchestrator (Orchestrator session has working gh auth); Worker delivers local checks + validator + strict YAML with matrix items marked blocked. Reassignment recorded per Validation Gate rules.

- 2026-07-15 Wave 1 completed: [Task_1, Task_2]
  - Summary: Task_1 (codex) delivered the script with a passing mock-gh matrix, bash -n, and package validator; Orchestrator executed the reassigned real-PR matrix against merged PR #35 — all nine cases pass (BASELINE/0; matching NO_CHANGE/3; comment-mismatch and review-only-mismatch NEW_ACTIVITY/0 with was/now for both counts; --wait 5 matching deadline/3; --wait mismatched immediate/0; missing --wait duration and malformed spec /2; 8s watch-mode run silent until timeout 124; --once against a nonexistent repo /4 with error to stderr).
  - Validation evidence: real counts comments=4 reviews=5 fetched independently via gh api --paginate and used as the matching baseline; command outputs captured in conversation.
  - Notes: Worker lesson candidate recorded (gh-auth preflight before assigning real-GitHub validation -> workspace-troubleshooting candidate, deferred to a future batch).

- 2026-07-15 Wave 2 completed: [Task_3]
  - Summary: Reviewer (codex) APPROVED, no blocking findings. Its gh auth was also invalid, so it validated the recorded real-PR matrix plus an independent static line-by-line review and an in-memory mock-gh suite (incl. cases beyond the original matrix: multi-spec mixed fire, watch skip-failed-spec, permanent-failure silence, conflicting-mode usage errors). Reference verified against the script's actual CLI — no spec drift; merge hard-stop wording confirmed.
  - Validation evidence: reviewer reran bash -n, package validator, targeted git diff --check; mock suite all pass.
  - Notes: non-blocking closeout note handled — script staged with mode 100755 via git update-index --chmod=+x (core.fileMode=false on this checkout).

- 2026-07-15 Wave 3 completed: [Task_4]
  - Summary: version bumped to 0.6.1 in all three manifests; package validator, smoke tests, and git diff --check green; committed in logical chunks and PR opened.
  - Validation evidence: validate_harness_package.py pass; run_validation_smoke_tests.py pass; git diff --check clean; staged script mode 100755 confirmed via git ls-files -s.
  - Notes: targeted repo-rule refresh waived — no repository facts in docs/coding-agent/rules/*.md changed.

## Decision Log (append-only; re-plans and major discoveries)

- 2026-07-15 Decision: stateless three-mode design converged over three agmsg rounds.
  - Trigger / new insight: user rejections — persisted baseline files (repo-state pollution vs gitignore cost) and default --wait durations (runtime-specific silent failure, Copilot auto-backgrounding).
  - Plan delta (what changed): baselines move to agent thread context via supplied-count arguments and always-printed count lines in probe/wait modes; --wait duration made mandatory with per-runtime guidance in the gated reference.
  - Tradeoffs considered: state files (rejected); hardcoded per-runtime defaults (rejected — drift with platform updates).
  - User approval: design yes ("Seems good enough"); execution approval pending.

- 2026-07-15 Decision: implementation split by agent strengths; notify-only fire semantics added.
  - Trigger / new insight: user directives — script and skill writing handed to different workers (Codex: shell detail; Claude: prose), and a watcher fire must never auto-advance to merge.
  - Plan delta (what changed): Task_1 split into Task_1 (script, Codex via agmsg) and Task_2 (reference, Claude), parallel with disjoint owns; notify-only rule added to Design and Task_2 acceptance; review/closeout renumbered to Task_3/Task_4.
  - Tradeoffs considered: single worker (simpler, but ignores strength matching); sequential tasks (unneeded — reference writes against the plan's CLI spec, reviewer checks spec drift).
  - User approval: refinement yes; execution approval pending.

## Notes
- Risks: shell portability (git-bash on Windows vs Linux) — mitigated by keeping to the original's POSIX-ish constructs and Reviewer scrutiny; GitHub API rate limits under chained --wait calls — reference advises 30s+ poll intervals (script keeps -i style interval inside --wait loops).
