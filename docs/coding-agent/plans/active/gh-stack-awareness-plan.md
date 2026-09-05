# Plan: Make Runtime Agents Aware Of GitHub Stacked PRs And gh stack

- status: in_progress
- generated: 2026-09-04
- last_updated: 2026-09-05
- work_type: docs

## Goal
- A runtime agent that is about to open a PR based on another unmerged feature branch, or to deliver work as more than one dependent PR, discovers that GitHub stacks exist, checks that the `gh stack` extension and the repository's stack support are available, and uses explicit, non-interactive, Orchestrator-controlled commands instead of hand-chaining base branches.

## Definition of Done
- `git-workflow` names stacked PRs and `gh stack` in its frontmatter description, carries a core rule that routes dependent PRs to the stack reference, and routes to a new gated reference `references/stacked-prs.md`.
- The reference is short: existence and availability with one escalation path, a pointer to the help text, when to stack, the traps that are unsafe to discover by trial, ownership, and the review-loop link to the watcher. Nothing the help text already teaches.
- `pr-authoring.md` routes to the reference at the moment a PR's base is an unmerged feature branch or work splits into dependent PRs.
- Validators green; Reviewer APPROVED.

## Scope / Non-goals
- Scope: `plugins/coding-agent-orchestration-harness/skills/git-workflow/**` (SKILL.md, `references/pr-authoring.md`, new `references/stacked-prs.md`), plugin manifests at closeout, this plan file and rule files at closeout.
- Non-goals: watcher script or `pr-review-monitoring.md` changes (owned by the pr-watch-discoverability plan); `orchestration-harness/SKILL.md` edits (its routing line already sends PR work to git-workflow, and the watcher branch edits that line); runtime adapter edits (adapters route to git-workflow already); plan-format template changes (a delivery-shape field was considered and cut, see Decision Log); auto-installing the extension; a lessons entry.

## Compatibility stance
- Not applicable: docs-only, no contract, interface, or persisted format changes.

## Design

### Why agents miss it, and the layers that fix it
- The feature is new and shipped as an extension, so neither model knowledge nor a default gh install surfaces it. Discovery has to come from the harness text visible at the moment of need.
- Layer 1, listing-visible trigger: the git-workflow frontmatter description gains "creating or updating stacked pull requests with the gh stack extension".
- Layer 2, always-on rule: git-workflow SKILL.md core rule 8: a PR based on another unmerged feature branch, or work delivered as dependent PRs, is a GitHub stack; read `references/stacked-prs.md`, which defines the availability check and the single fallback. Do not hand-chain base branches except through that fallback. Release, integration, or long-lived base branches are not in scope of this rule.
- Layer 3, gated procedure: `references/stacked-prs.md`, routed from SKILL.md ("If a PR will be based on an unmerged feature branch, or the work will land as more than one dependent PR: read `references/stacked-prs.md`") and from the top of pr-authoring.md.

### Reference content (`references/stacked-prs.md`)
Content test: a line earns its place only if an agent could not learn it from `gh stack --help` and `gh stack <cmd> --help`, or if learning it by trial is unsafe. Everything else (what a stack is, the command lifecycle, flags, navigation) is left to the help text, which the reference tells the agent to read.
- Existence and availability: GitHub stacks are managed by the `gh stack` extension (`github/gh-stack`), not core gh; check `gh extension list`, and repository support with `gh api repos/<o>/<r>/stacks` (a list, not 404). Ask the user before `gh extension install github/gh-stack`. If either check fails or the user declines, ask the user how to proceed; do not fall back silently.
- Read `gh stack --help` and the per-command help before first use; commands are non-interactive only when given explicit targets or `--auto`.
- When to stack: the base is an unmerged feature branch, or the work lands as dependent PRs. Independent changes stay separate PRs against trunk.
- Traps the help text does not make safe to discover by trial:
  - `submit --auto` creates drafts; add `--open` or mark each PR ready before arming review monitoring.
  - `link` creates no local tracking; run `checkout <member-pr>` before local stack commands.
  - argument-less `merge` in a non-interactive terminal merges the whole stack without prompting; merge waits for user authorization and always names a target, `--yes`, and a method.
  - `modify` and `switch` are interactive-only; `sync` aborts on divergence when unattended, so prefer `rebase` then `push`.
- Ownership: every `gh stack` command except `view` mutates branches or remote state and stays Orchestrator-controlled per core rule 3; `unstack` only on explicit user request.
- Review loop: arm monitoring with any member PR; the watcher covers the stack (pointer to `pr-review-monitoring.md`).
- Target length: about fifteen lines. Consumer-facing text only.

## Context (workspace)
- `plugins/coding-agent-orchestration-harness/skills/git-workflow/SKILL.md` and `references/pr-authoring.md`.
- `docs/coding-agent/plans/active/pr-watch-discoverability-plan.md`: sibling plan; this branch is stacked on its branch so the two git-workflow SKILL.md edits apply sequentially instead of conflicting.
- Research waived: `gh stack` help for every subcommand was captured in this session (gh 2.98.0, gh-stack v0.1.0) and cross-checked by the Codex reviewer against the v0.1.0 command sources; affected harness files were read in this session.

## Open Questions (max 3)
- None.

## Assumptions
- A1: This plan's branch is created as the second layer of a stack on `feature/2026-09-04/pr-watch-discoverability`, using `gh stack`, so the harness dogfoods the feature; the version bump is 0.14.1 on top of the watcher branch's 0.14.0 (patch, docs only).
- A2: Both implementation tasks go to Claude workers (prose); Task_1's command verification is read-only `gh stack <cmd> --help` and needs no repository mutation.

## Tasks

### Task_1: Write the stacked-prs reference
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/git-workflow/references/stacked-prs.md
- depends_on: []
- description: |
  Write `references/stacked-prs.md` per the "Reference content" design and its content test. Verify every named command and flag against the installed extension's `--help` output and capture that output in the report. No rationale, history, or provenance.
- acceptance:
  - Every bullet in the design is present and nothing else; each line passes the content test (not learnable from help, or unsafe to learn by trial).
  - Every named command and flag matches `gh stack <cmd> --help` output captured in the report.
  - The four traps and the merge authorization rule are stated; the reference is about fifteen lines.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "gh stack <cmd> --help for each documented subcommand; outputs captured in the report"
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py"
  - kind: review
    required: true
    owner: reviewer
    detail: "Docs review vs Design; consumer-facing text only per repo rules"

### Task_2: git-workflow trigger and routing
- type: docs
- owns:
  - plugins/coding-agent-orchestration-harness/skills/git-workflow/SKILL.md
  - plugins/coding-agent-orchestration-harness/skills/git-workflow/references/pr-authoring.md
- depends_on: []
- description: |
  Apply layers 1 to 3 of the design: frontmatter cue, core rule 8 with its scope limits and fallback pointer, the progressive-disclosure line to `references/stacked-prs.md`, and one routing line at the top of pr-authoring.md for the unmerged-feature-base or dependent-PR case. Change nothing else in either file; the watcher branch's edits to the same files are already in the base.
- acceptance:
  - Frontmatter description names stacked PRs and the gh stack extension, description-first per skills-maintenance.
  - Core rule 8 routes to the reference, names the fallback as the only exception, and excludes release or integration base branches; the disclosure line is present; pr-authoring.md routes to the reference.
  - No other lines change.
- validation:
  - kind: command
    required: true
    owner: worker
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py"
  - kind: review
    required: true
    owner: reviewer
    detail: "Diff review vs Design; SKILL.md stays routing and core rules only; core rule and reference fallback do not contradict"

### Task_3: Independent review
- type: review
- owns: []
- depends_on: [Task_1, Task_2]
- description: |
  Reviewer re-verifies the reference's commands against `gh stack --help` output, applies the content test line by line and flags anything the help text already teaches, checks that the trigger chain is complete (frontmatter, core rule, disclosure line, pr-authoring routing all point at the same reference), checks the traps and ownership against git-workflow core rules 3 to 5, confirms the core rule and the reference's escalation path agree, and checks for duplication with `pr-review-monitoring.md`.
- acceptance:
  - Reviewer status is APPROVED
- validation:
  - kind: review
    required: true
    owner: reviewer
    detail: "Full-diff review plus independent command verification"

### Task_4: Closeout
- type: chore
- owns:
  - plugins/coding-agent-orchestration-harness/.claude-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.codex-plugin/plugin.json
  - plugins/coding-agent-orchestration-harness/.github/plugin/plugin.json
  - docs/coding-agent/plans/active/gh-stack-awareness-plan.md
  - docs/coding-agent/rules/*.md
- depends_on: [Task_3]
- description: |
  Orchestrator-owned: version bump per A1; full validators; targeted rule freshness check because the change touches rule-source patterns in `docs/coding-agent/rules/_lifecycle.json` (update the affected rule file or record an explicit waiver with reason in the Decision Log; no full bootstrap); logical commits (reference, routing); publish this branch as the second PR of the stack with `gh stack submit --auto --open` then `gh pr edit <number>` per the reference; arm the watcher with this PR's number; append the final Progress Log entry, set status done, and move this plan to `docs/coding-agent/plans/completed/`.
- acceptance:
  - Version bumped in all three manifests; validators green.
  - Rule freshness resolved: rule file updated or waiver recorded.
  - PR open, not draft, as a member of the same stack as the watcher PR, evidenced by `.stack.number` and `isDraft` from the PR payload, and the watcher's ARMED lines listing both PRs, recorded in the Progress Log.
  - Plan status done and file moved to completed.
- validation:
  - kind: command
    required: true
    owner: orchestrator
    detail: "From plugins/coding-agent-orchestration-harness/: python scripts/validate_harness_package.py && python scripts/run_validation_smoke_tests.py; from repo root: git diff --check"
  - kind: review
    required: true
    owner: orchestrator
    detail: "Progress Log carries PR URL, stack number, isDraft=false, ARMED output, and the rule-freshness decision before the plan is moved"

## Task Waves (explicit parallel dispatch sets)

- Wave 1 (parallel): [Task_1, Task_2]
- Wave 2: [Task_3]
- Wave 3: [Task_4]

## Rollback / Safety
- Docs only, on a branch stacked above the watcher branch; revert by dropping the branch. Command verification is read-only.

## Progress Log (append-only)

Append-only editing rule (applies to both logs below): when appending an entry, anchor the edit on the previous entry and reproduce it (or anchor on the section's tail marker) so the edit inserts rather than replaces, and verify afterward that the log grew.

- (none yet)

## Decision Log (append-only; re-plans and major discoveries)

- 2026-09-04 Decision: separate plan and branch from the watcher work, stacked on it.
  - Trigger / new insight: user asked for gh stack awareness as its own plan and branch; both plans edit git-workflow SKILL.md and pr-authoring.md.
  - Plan delta (what changed): the Stacked PRs section originally assigned to the watcher plan's Task_2 moves here as the full reference; this branch bases on the watcher branch so the shared-file edits are sequential.
  - Tradeoffs considered: an independent branch off main would conflict on SKILL.md; a single combined plan would mix a script rewrite with a docs rollout.
  - User approval: pending.
- 2026-09-05 Decision: Codex reviewer round applied; plan-template task cut.
  - Trigger / new insight: reviewer findings P2-1 to P2-5: `submit --auto` creates drafts unless `--open`; `link` creates no local tracking; argument-less `merge` merges the whole stack without prompting in non-interactive terminals; the absolute no-hand-chaining core rule contradicted the reference's fallback; forcing wave boundaries onto PR boundaries conflates dispatch batches with delivery units.
  - Plan delta (what changed): reference design now handles draft-versus-ready and per-PR edits, link-then-checkout, explicit merge targets with `--yes` and a method, modify and switch forbidden, navigation commands classed as mutations, two availability checks with one escalation path, and the core rule scoped to unmerged feature bases with the fallback as its named exception. The plan-template Delivery shape task is cut: the frontmatter cue plus the pr-authoring route already cover discovery and no planning failure justified a template field. Tasks renumbered; closeout now includes plan lifecycle and rule freshness.
  - Tradeoffs considered: keeping the template line as optional metadata was possible but had no named consumer.
  - User approval: pending.
- 2026-09-05 Decision: reference content trimmed to what the help text cannot teach.
  - Trigger / new insight: user ruled that skill content stays minimal; concept explanations and command lifecycles are rediscoverable from `gh stack --help` or are everyday knowledge, and only content that prevents repeated exploration or unsafe trial earns a line.
  - Plan delta (what changed): the reference design drops the concept paragraph, the command-per-moment list, navigation and inspect bullets, and REST field details; it keeps existence and availability, a pointer to the help text, when to stack, four traps, ownership, and the watcher pointer, with a content test and a length target the Reviewer applies line by line.
  - Tradeoffs considered: a per-moment command list would save one help read per moment but freezes flag details of a v0.1.0 extension into the skill.
  - User approval: yes (this conversation).

## Notes
- Risks: the extension is at v0.1.0 and its flags may change; the reference names commands by moment so a flag rename is a one-line fix. Interactive forms hang or, for merge, act without prompting; the reference forbids them explicitly.
- Edge cases: an agent on a machine without the extension, or in a repository without stack support, escalates to the user rather than choosing a fallback silently.
