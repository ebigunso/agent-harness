---
rule_schema_version: 2
suite_id: "rules-20260513-b80f05e"
rule_file: "orchestrator"
last_updated: "2026-10-02"
---

# Orchestrator Repository Rules

## Repo-Specific Orchestrator Policies

- Keep first-party skill procedures in `references/` when they are not always-on routing rules.
- For first-party skills, keep `SKILL.md` limited to trigger/scope boundaries, core runtime rules, and progressive-disclosure pointers; put design rationale, history, and maintenance decisions in ADRs or maintainer references.
- Preserve exact user-provided ADR consultation provenance unless the user explicitly asks to normalize it.
- Before adding validators for skill changes, distinguish objective package integrity from editable skill prose. Prefer Reviewer checks for wording, criteria quality, and prompt-bloat concerns unless a structural packaging contract is at risk.
- When adding package validation for enum/schema changes, check the exact enum owner or contract field rather than a broad substring.
- Use `rulebook` for full rule-suite bootstrap, schema migration, targeted refresh, and repair. Do not run full bootstrap as a per-task ritual.
- Propose a decision record only after the admission test in `durable-docs-authoring/references/adr.md` passes, present it for acceptance on its own, and never count plan approval or a merge as acceptance.
- Keep implementation-time artifacts (self-tests, fixtures, dry checks) out of `skills/`; every file there is one a session reads or runs at runtime, and a Reviewer packet for a skill change asks what runtime text invokes each added non-Markdown file.

## Models And Peers In This Workspace

The routing principle is in `subagent-strategy/references/model-routing.md`; this section is the dated observation it routes on. Re-observe and redate it when a model changes.

- Observation, dated 2026-09-15: the Claude models have shown the writing strength and the Codex (GPT) models the detail-scrutiny strength. Nothing is recorded for long-context reading; route on it only after observing it.
- What this workspace has: Claude subagents dispatched from the Orchestrator session, and the registered Codex peers `agent-harness-worker` and `agent-harness-reviewer`, reached over agmsg in team `AgentHarness`.
- So, by default: correctness-tier review, forensic research, checks and scripts whose acceptance is mechanical precision go to the Codex peers; delegated prose implementation (skill text, references, READMEs) and design-tier review go to Claude subagents. Model choice never moves role ownership: plans and decision records stay with the Orchestrator. Prose a Codex peer authored is finalized under the Prose quality rules of `subagent-strategy/references/model-routing.md`.
- Cost, the owner's setting, stated 2026-10-04 and his to change: Opus is an acceptable cheap model; Fable and Astra count as expensive. The registered Codex peers run GPT-6.1-Sol (set by the owner on 2026-10-04 in place of Astra) and may be dispatched freely. So checking work (plan, wave and final review) and Worker tasks go to the Codex peers or to Opus by the kind of work, and Fable is kept for what needs it: independent judgement of the Orchestrator's work.
- The Auditor (the value audit and the in-loop goal assessment) is held here by a Claude subagent on Fable, apart from whoever holds the Reviewer; this too is the owner's setting to change. Until the installed plugin carries the Auditor agent, an Auditor dispatch from this workspace runs on the Reviewer's agent type with the fixed template as its whole prompt.
- Before the first dispatch of a run, send each registered peer the run needs a message and confirm it answers. A peer that stays silent is reported to the user, with what was sent and when; its work is not given to a Claude subagent without saying so in the plan and to the user, and the peer is tried again at the next dispatch that suits it.
- Route agmsg dispatch only to the registered `agent-harness-*` peers; never spawn new peers or run headless Codex for dispatch. Ephemeral headless `codex exec` is allowed only as a measurement instrument for ablation probes.

## Repo-Specific Integration / Git Policy

- Shared-state Git mutations remain Orchestrator-controlled unless explicitly delegated.
- Prefer `feature/YYYY-MM-DD/<feature-name>` branch names in this repository unless the user requests another convention.
- If nested branch creation fails with `unable to create directory for .git/refs/heads/...`, verify there is no conflicting loose or packed ref, then rerun the Git branch/switch command with filesystem approval; do not change naming conventions or edit `.git` internals as a workaround.
- Stage only intended files when the worktree is mixed; never include unrelated untracked files silently.
- A change reaches the remote only after it has been reviewed, an open pull request included: commit locally, get the review, apply its findings, then push. Log the validator result and the review for each change in the plan before the push.
- Merge a pull request only on an explicit user instruction that names that pull request; a conditional or standing authorization given for one pull request never extends to another, ask again for each one.
- PR titles describe the change; plugin version numbers stay in the manifests and the PR body, never in the title.
