---
status: accepted
adr_type: design
date: 2026-10-03
deciders: ["ebigunso"]
consulted: ["Claude Fable 5.1"]
informed: []
supersedes: ["superseded/ADR-D-0022-workflow-mechanics-have-one-home--superseded-by-ADR-D-0049.md"]
superseded_by: null
---

# ADR-D-0049: The workflow mechanics of each session role have one home, and every runtime surface routes to it instead of restating it

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. The product owner is whoever is entitled to state the product's values and to answer product-level questions for that work; when the person directing the work owns the product, both are that person. Counsel is the session the person directing the work opens for value discussion, separate from any Orchestrator session. The Orchestrator session is a session that holds the Orchestrator role (ADR-D-0020) and plans, dispatches and reports the work.

The runtimes the harness supports consume it through different surfaces: agent definitions, plugin manifests, a loader block, installed role templates. Each surface is a place where gates, rules and formats could be written down again, and every copy is a place where they can go stale without anyone noticing. A session holds one role, and on 2026-10-03 there were two such roles, the Orchestrator and Counsel, each with mechanics of its own. The fork is whether a runtime surface may carry workflow content of its own or only route to a shared source, and what that source is when there is more than one session role.

## Decision

- The workflow mechanics of each session role have one home.
- Every loader, adapter, snippet and README routes to the home of the role concerned and does not restate its gates, rules, role names or formats.
- A session takes its mechanics from the home of the role it holds and never loads another role's home.
- What roles share is stated once, in a home of its own that is no role's home: both role homes point to it, it points to neither and names no role's procedure, so a procedure appearing in it is misuse. Where two roles each have a part in one exchange, each home states only its own role's part.
- Adapters may differ from one another in length and wording as long as their meaning comes from that home.
- One replication is deliberate and bounded: the role contracts that runtime instruction blocks must carry, kept as one text across the runtime copies.
- Which skill is the home of which role is stated in the role map (`plugins/coding-agent-orchestration-harness/skills/orchestration-harness/references/runtime-role-map.md`).

## Why

An agent that follows a stale copy of the workflow reports gates as satisfied that the current workflow no longer defines, and nothing in the copy tells it so; the person relying on that report then believes a check was made that was not. One home per role keeps what a session is told true to what the harness now does, and keeps each session at its own level: a session that read another role's mechanics would be drawn to that role's level of work.

## Rejected Alternatives

- One home for every session role, as ADR-D-0022 was written when there was one: it lost because a session would load another role's mechanics with its own; reopen if two homes are found restating each other's rules.
- The roles and their skills named in this record: it lost because a new session role or a renamed skill would leave the record stale for no change to the rule; reopen if the role map is found to drift from the skills with nothing catching it.
- Duplicate the workflow into every adapter: it lost because each copy can go stale unnoticed and an agent following one reports gates the workflow no longer defines; reopen if a runtime ever refuses to read shared skills from an agent definition.
- Put the workflow in a repository-wide loader file: rejected outright; such a file reaches every platform that reads it, and a user-level one reaches every project.
- Force one identical prompt body on every runtime: it lost because the runtimes differ in what an agent definition may contain and how it is loaded, so one body fits none of them well; reopen if a generated-adapter system can emit runtime-specific shapes from one source.

## Decision Boundary

Invariant: no surface other than the home of the role concerned defines that role's workflow mechanics, its gates, rules, role names and report formats; each session takes its mechanics from its own role's home; what roles share, the forms and ownership of the documents they both read, is stated once in a home of its own that names no role's procedure; the replicated role contract is the only copy of a role's mechanics outside its home and is kept in sync as one text; the Decision list states the rest.

Not covered: which roles exist, which skill is the home of each, and their physical names, which the role map states (ADR-D-0048); adapter length, kernel wording, which references an adapter names, and the loader block's exact text, all of which change through skill text and the adapter checklist; what each role is responsible for; how a session takes a role (ADR-D-0037).

## Validation

- Review of the loader snippet confirms it is loader-only, with no harness role names or gate wording in it; the package validator does not check this (ADR-D-0022 said it did), so it is a Reviewer and checklist check until a validator check exists.
- The adapter maintenance checklist diffs the replicated role contract across the runtime copies of each role.
- The role map states the home of every session role and the home of what they share.
- The shared home names no role's procedure; review of a change to it asks: does this say what a role does?
- Review of any new runtime surface asks: does this restate, or route, and to which role's home?

## Revisit When

- A runtime gains a first-class way to declare a dependency on shared instructions without loader text (none of Copilot, Claude Code, or Codex had one on 2026-09-07).
- Agents stop loading or applying their role's home from loader-only routing; the live loader check recorded under `docs/coding-agent/experiments/frontier-guard-probes/` in git history at `2a5ebf9` is the evidence to consult for the Orchestrator.
- Two homes are found restating each other's rules.

## More Information

Replaces ADR-D-0022 in full: everything it decided is carried, stated per session role instead of for one skill. New here: a session takes its mechanics only from its own role's home, and what roles share has a home of its own that names no role's procedure. Moved out: which skill is the home, which the role map now states. Corrected here: ADR-D-0022's Validation claimed a package-validator check of the loader snippet that the validator does not make. Related: ADR-D-0020 (loader-routed sessions assume the Orchestrator role), ADR-D-0034 (Counsel), ADR-D-0037 (entering a session role), ADR-D-0048 (role names and the role map), ADR-I-0006 (adapter layout).
