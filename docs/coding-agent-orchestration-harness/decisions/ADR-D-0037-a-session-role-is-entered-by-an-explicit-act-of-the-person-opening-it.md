---
status: proposed
adr_type: design
date: 2026-09-30
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1"]
informed: []
supersedes: ["ADR-D-0023-the-harness-is-entered-by-selecting-the-orchestrator.md"]
superseded_by: null
depends_on: ["ADR-D-0020-loader-routed-sessions-assume-the-orchestrator-role.md", "ADR-D-0034-counsel-is-a-separate-session-at-the-level-of-behaviour-and-decisions.md"]
---

# ADR-D-0037: A session role (Orchestrator or Counsel) is entered by an explicit act of the person opening the session, using whatever the runtime offers for that session: an agent picker, a launch option or project setting that runs the role's agent, or an explicit invocation of the role's skill; a skill's activation by description match is never the way into one

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. The product owner is whoever is entitled to state the product's values and to answer product-level questions for that work; when the person directing the work owns the product, both are that person. Counsel is the session the person directing the work opens for value discussion, separate from any Orchestrator session. The Orchestrator session is a session that holds the Orchestrator role (ADR-D-0020) and plans, dispatches and reports the work.

Two harness roles are held by a session itself: the Orchestrator, whose plan gates and delegation rules apply only to the Orchestrator session, and Counsel, whose limits hold only in a session opened as Counsel by the person directing the work (ADR-D-0034). The runtimes differ in how a whole session can be made to run as a named agent, as checked on 2026-10-01: GitHub Copilot offers a per-session agent picker. Claude Code has no per-session agent picker; its documentation (https://code.claude.com/docs/en/sub-agents.md) states that a whole session runs as a custom agent by the launch flag `claude --agent <name>` or by the `agent` setting in `.claude/settings.json`, the flag being a CLI launch option and the setting applying to every session of that project, and it lists the CLI, the desktop app and the VS Code extension as surfaces; on the same date ebigunso observed that the desktop app did not run a custom agent as the main session. Codex offers none of these. Every one of these runtimes also discovers skills by description and may load one on its own when a request seems to match. The fork is whether a session comes to hold a role by an explicit act of the person opening it, whatever form the runtime gives that act, or by a skill's automatic activation.

## Decision

- A session takes a session role, Orchestrator or Counsel, by an explicit act of the person opening the session, in whatever form the runtime offers for the session being opened.
  - Where the runtime offers an agent picker for the session, the act is selecting the role's agent in it.
  - Where the runtime runs the whole session as a named agent by a launch option or a project setting, the act is launching the session as the role's agent by that option or setting.
  - Where neither applies to the session being opened, the act is explicitly invoking the role's skill, which holds the role's policy.
- A skill's activation by description match is never the way into a session role.
- The Orchestrator's route in a runtime that offers none of these acts stays the loader route, which ADR-D-0020 governs and this record does not.
- Support skills, meaning every skill other than the ones that hold a session role's policy, are capability modules whose descriptions serve discovery and assistance, and no support skill presents itself as the way into a session role.

## Why

A session that was supposed to run under a role but did not simply proceeds without that role's gates or limits, and nothing reports the omission; an explicit act fails visibly, an auto-trigger fails silently. The act is tied to what the runtime offers for the session being opened, not to a runtime as a whole, because one runtime offers it on some surfaces and not on others.

## Rejected Alternatives

- Rely on automatic skill discovery to start a role: reopen if a runtime documents deterministic activation for a named skill.
- Make every support skill self-sufficient as an entrypoint: rejected outright; it multiplies the workflow across skills against ADR-D-0022.
- One way in per runtime, chosen by whether the runtime offers agent selection: rejected outright; Claude Code runs the main session as a named agent on some surfaces and not on others, so a per-runtime rule leaves sessions on the other surfaces with no way in.

## Decision Boundary

Invariant: the only way into a session role that is relied on or documented is an explicit act of the person opening the session, in the form the Decision names for what that session offers; no automatic activation is one.

Not covered: what an adapter says once the role is entered; how skill descriptions are worded; the Orchestrator's loader route (ADR-D-0020); which surfaces of a runtime offer which act, which the runtime documentation and the adapters state; what each session role may do.

## Validation

- For each runtime and surface the harness supports, runtime documentation and adapters describe one explicit act as the way into each session role, chosen from the three the Decision names, and no automatic activation.
- Where the way in is invoking the role's skill, runtime documentation says so and the loader does not route to that skill.
- Support skill descriptions describe capabilities and do not present themselves as the way into a session role.

## Revisit When

- A runtime adds or removes a way to run the main session as a named agent (the facts in Context were checked on 2026-10-01).
- A runtime provides deterministic, documented activation of a named skill from a selected agent (neither GitHub Copilot nor Claude Code did on 2026-09-07).

## More Information

Replaces ADR-D-0023 in full: what it decided for the Orchestrator is carried, restated as an explicit act in the form the runtime offers, and the same rule is stated for Counsel, the second role a session itself holds. Loader-routed sessions: ADR-D-0020. Single home of workflow mechanics: ADR-D-0022. Counsel: the record on Counsel (ADR-D-0034).
