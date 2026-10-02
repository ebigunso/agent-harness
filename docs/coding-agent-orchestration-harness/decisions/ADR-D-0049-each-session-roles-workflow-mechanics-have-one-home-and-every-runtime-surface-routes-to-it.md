---
status: proposed
adr_type: design
date: 2026-10-03
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1"]
informed: []
supersedes: ["ADR-D-0022-workflow-mechanics-have-one-home.md"]
superseded_by: null
depends_on: ["ADR-D-0034-counsel-is-a-separate-session-at-the-level-of-behaviour-and-decisions.md"]
---

# ADR-D-0049: The workflow mechanics of each session role have one home, a skill and its references, and every runtime surface routes to it instead of restating it

## Context and Problem Statement

Three runtimes (GitHub Copilot, Claude Code, Codex) consume the harness through different surfaces: agent definitions, plugin manifests, a Codex `AGENTS.md` loader block, and installed role templates. Each surface is a place where gates, rules and formats could be written down again, and every copy is a place where they can go stale without anyone noticing. A session holds one of two roles (ADR-D-0034): the Orchestrator, whose mechanics are planning gates, delegation, validation and reporting, or Counsel, whose mechanics are how a value discussion is held, drafted, ratified and handed over. The fork is whether a runtime surface may carry workflow content of its own or only route to a shared source, and what that source is now that there are two session roles.

## Decision

- The workflow mechanics of a session role have one home: the `orchestration-harness` skill and its references for the Orchestrator and the roles it dispatches, and the `counsel` skill and its references for Counsel.
- Every loader block, runtime adapter, snippet and README routes agents to the home of the role concerned and does not restate its gates, rules, role names or formats.
- A session reads the home of the role it holds and not the other's: a Counsel session never loads `orchestration-harness`, and an Orchestrator session does not take its mechanics from the `counsel` skill.
- What the two roles share (the forms of the value documents, the carrier between the sessions) is stated once, in the reference of the skill that owns it, and the other skill points to it.
- Adapters may differ from one another in length and wording as long as their meaning comes from the shared skill tree.
- One replication is deliberate and bounded: the role workflow and output contracts that runtime instruction blocks carry under `runtime-adapter-contract`, maintained as one text across all runtime copies.

## Why

An agent that follows a stale copy of the workflow reports gates as satisfied that the current workflow no longer defines, and nothing in the copy tells it so; the person relying on that report then believes a check was made that was not. One home per role keeps what a session is told true to what the harness now does, and keeps each session at its own level: a Counsel session that read the Orchestrator's mechanics would be drawn to the level of plans.

## Rejected Alternatives

- One home for both roles, the orchestration skill carrying Counsel's mechanics as well, as ADR-D-0022 was written before Counsel existed: it lost because a session would load the other role's mechanics with its own; reopen if the two skills are found restating each other's rules.
- Duplicate the workflow into every adapter: reopen if a runtime ever refuses to read shared skills from an agent definition.
- Put the workflow in `AGENTS.md`: rejected outright; a repository `AGENTS.md` reaches every platform, not only Codex, and a user one reaches every project.
- Force one identical prompt body on every runtime: reopen if a generated-adapter system can emit runtime-specific shapes from one source.

## Decision Boundary

Invariant: no surface other than the skill tree of the role concerned defines a gate, rule, role name or report format; each session reads its own role's home; the replicated role contract is the only exception and is kept in sync as one text; the Decision list states the rest.

Not covered: adapter length, kernel wording, which references an adapter names, and the loader block's exact text, all of which change through skill text and the runtime-adapter-contract checklist; what each role is responsible for (ADR-D-0034); how a session takes a role (ADR-D-0037); which skill owns a given shared statement.

## Validation

- Package validation confirms loader snippets are loader-only and rejects harness role names or gate wording in them.
- The adapter maintenance checklist diffs the replicated role contract across the runtime copies, for the Orchestrator's roles and for Counsel.
- Review of any new runtime surface asks: does this restate, or route, and to which role's home?

## Revisit When

- A runtime gains a first-class way to declare a dependency on shared instructions without loader text (none of Copilot, Claude Code, or Codex had one on 2026-09-07).
- Agents stop loading or applying their role's skill from loader-only routing; the live loader check recorded under `docs/coding-agent/experiments/frontier-guard-probes/` in git history at `2a5ebf9` is the evidence to consult for the Orchestrator.
- The two skills are found restating each other's rules.

## More Information

Replaces ADR-D-0022 in full: everything it decided for the orchestration skill is carried, and the rule is stated per session role now that Counsel is a second one. Related: ADR-D-0020 (loader-routed sessions assume the Orchestrator role), ADR-D-0034 (Counsel), ADR-D-0037 (entering a session role), ADR-I-0006 (adapter layout).
