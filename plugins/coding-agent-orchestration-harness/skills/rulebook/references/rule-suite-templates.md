# Rule Suite Templates

Use these templates for full bootstrap, schema migration, or repair. Replace `<suite-id>` and dates during creation.

## Shared Front Matter

Each role rule file uses this minimum front matter:

```yaml
---
rule_schema_version: 2
suite_id: "<suite-id>"
rule_file: "worker"
last_updated: "YYYY-MM-DD"
---
```

Use the appropriate `rule_file` value: `common`, `worker`, `orchestrator`, or `reviewer`.

## index.md

```md
---
rule_schema_version: 2
suite_id: "<suite-id>"
lifecycle_manifest: "docs/coding-agent/rules/_lifecycle.json"
required_files:
  - "common.md"
  - "worker.md"
  - "orchestrator.md"
  - "reviewer.md"
---

# Coding Agent Rules Index

Read these files by role:

- `common.md`: shared repository facts, validation contract, safety boundaries.
- `worker.md`: Worker execution and validation mapping.
- `orchestrator.md`: planning, dispatch, integration, git, and rule maintenance.
- `reviewer.md`: review-specific repository policy and recurring risk hotspots.

## Rule Freshness

Do not read `_lifecycle.json` during normal work.

Use `_lifecycle.json` only when:
- required rule files are missing or suite IDs do not match;
- schema migration or rule-suite repair is needed;
- the task changes CI, validation, build, agent-instruction, or rule-source files;
- repository facts contradict the rules;
- targeted rule refresh is needed.
```

## common.md

```md
---
rule_schema_version: 2
suite_id: "<suite-id>"
rule_file: "common"
last_updated: "YYYY-MM-DD"
---

# Common Repository Rules

## Repository Reference Documents

- <product philosophy line>
- <engineering philosophy line>

## Repository-Specific Validation Commands

- None recorded yet.

## Repo Safety / Boundaries

- None recorded yet.

## Repo Naming / Structure

- None recorded yet.

## Models And Peers In This Workspace

This is the workspace's record of options that `subagent-strategy/references/model-routing.md` routes on, and of its means to start, watch and end a session; the Orchestrator and Counsel both read it. Re-observe and redate it when a model changes.

- Status: recorded <YYYY-MM-DD>; <awaits the owner's confirmation | confirmed by <owner> on <YYYY-MM-DD>>.
- Options: <each option some role resolves to or falls back to, among what the runtime offers (the session's own model, each model the subagent mechanism can be dispatched on, each kind of peer seat a session can create): the option a resolution below gives and the option it names for the unavailable case, and no others; with its model, the setting it runs at (its reasoning effort: as the dispatch or the creation of the seat can choose it | as the runtime fixes it | not known) and the role it can hold; one model at two settings that differ for some role's work or in cost is two options, each listed only where a role resolves to it or falls back to it>.
- Sessions: <each means the workspace has to start a session in a role with a first message and without a person, with what must already be so for it to work; how it is seen from outside whether that session is alive and whether it is working or waiting; how it is ended; each observed <YYYY-MM-DD> | documented, <where>, <YYYY-MM-DD> | none found, <YYYY-MM-DD>>.
- Tendencies: <per family: the workspace's observation with its date | the seed's entry with the seed's date | not yet observed>.
- Runs on: <which subscription plan, with its usage limits as the owner knows them | a pay-as-you-go budget and how large it is; as the owner states it | awaits the owner's word>; <where he named the plan or budget without its limits or size: researched limits: <what setup found, its source, the date found> | none found, <YYYY-MM-DD>>.
- Budget allowance: <as the owner states it | none stated | awaits the owner's word>.
- Orchestrator: <the option its reason resolves to, its setting named>; rests on <the capability finding, where it was found, its date>; where unavailable: <the one option named for that case, on a different model or seat from the option it backs, its setting named, and in a few words the capability finding it rests on | none named, where no option on a different model or seat is capable for the work and accepted by the role's cost setting>.
- Auditor: <the option its reason resolves to, its setting named>; rests on <the capability finding, where it was found, its date>; where unavailable: <the one option named for that case, on a different model or seat from the option it backs, its setting named, and in a few words the capability finding it rests on | none named, where no option on a different model or seat is capable for the work and accepted by the role's cost setting>.
- Researcher: <per work type: the option its reason resolves to, its setting named; rests on the capability finding, where it was found, its date; where unavailable: the one option named for that case, on a different model or seat from the option it backs, its setting named, and in a few words the capability finding it rests on | none named, where no option on a different model or seat is capable for the work and accepted by the role's cost setting>.
- Worker: <per work type: the option its reason resolves to, its setting named; rests on the capability finding, where it was found, its date; where unavailable: the one option named for that case, on a different model or seat from the option it backs, its setting named, and in a few words the capability finding it rests on | none named, where no option on a different model or seat is capable for the work and accepted by the role's cost setting>.
- Reviewer: <per work type: the option its reason resolves to, its setting named; rests on the capability finding, where it was found, its date; where unavailable: the one option named for that case, on a different model or seat from the option it backs, its setting named, and in a few words the capability finding it rests on | none named, where no option on a different model or seat is capable for the work and accepted by the role's cost setting>.
```

Fill the Models And Peers In This Workspace section as `references/bootstrap-lifecycle.md` (Models Record) states.

For fresh suites, add one optional Decision Records line under Repository Reference Documents, chosen during the bootstrap detection/placement procedure in `references/bootstrap-lifecycle.md`:

- `Decision records: follow <path>; match the existing ADRs' numbering and sections.`
- `Decision records: no repo convention — harness default template applies (durable-docs-authoring references/adr.md).`

Replace the two philosophy placeholders with the lines `references/bootstrap-lifecycle.md` (Philosophy Lines) decides, in the forms `references/rules-files.md` gives.

Only once the owner accepts the standing approval that admits Counsel's relays (`references/bootstrap-lifecycle.md`, Counsel Relay Admission), add the Counsel line under Repository Reference Documents and the entry under Standing Approvals, adding that section if the file has none:

```md
- Counsel: <identity> on the peer channel; relays admitted (Standing Approvals).
```

```md
## Standing Approvals

- Relays from Counsel: a relay from `<identity>` on the peer channel that quotes the owner carries the owner's decisions to an Orchestrator session in this repository, on the terms of the `orchestration-harness` value-level operation reference (The Carrier); plan approval and its waiver are not carried. A message's sender cannot be verified, and the owner accepts that risk with this entry. Given and accepted by <owner> on <YYYY-MM-DD>: "<the owner's words>".
```

Before acceptance, neither is written.

## worker.md

```md
---
rule_schema_version: 2
suite_id: "<suite-id>"
rule_file: "worker"
last_updated: "YYYY-MM-DD"
---

# Worker Repository Rules

## Repo-Specific Worker Notes

- None recorded yet.

## Repo CI / Checks Mapping

| Change Type | Required Checks | Notes |
|---|---|---|

## Mechanical Gate Candidates

- None.
```

## orchestrator.md

```md
---
rule_schema_version: 2
suite_id: "<suite-id>"
rule_file: "orchestrator"
last_updated: "YYYY-MM-DD"
---

# Orchestrator Repository Rules

## Repo-Specific Orchestrator Policies

- None recorded yet.

## Repo-Specific Integration / Git Policy

- None recorded yet.

## Rule Suite Refresh Notes

- None.
```

## reviewer.md

```md
---
rule_schema_version: 2
suite_id: "<suite-id>"
rule_file: "reviewer"
last_updated: "YYYY-MM-DD"
---

# Reviewer Repository Rules

## Repo-Specific Reviewer Notes

## Review Risk Hotspots

Suggested durable review categories:
- public_api_compatibility
- public_surface_completeness
- diagnostic_fidelity
- build_config_parity
- strict_ci_hygiene
- entrypoint_intent
- admission_before_side_effect
- collection_semantics
- runtime_model_compatibility
- abstraction_value_searchability
- canonical_policy_path
- authority_vs_derived_data
- failure_mode_completeness
- semantic_consistency
- validation_boundary_correctness
- risk_based_test_coverage

## Required Reviewer-Owned Evidence

| Trigger | Evidence Required | Source |
|---|---|---|

## Review Heuristics

Repository-specific review checks that are not mechanical gates and not tied to one tool.

## Recurring Misses And Prevention

Durable patterns learned from prior review misses, phrased as reusable prevention rules.

## Mechanical Gate Candidates

Repo-local checks that could eventually move into:
- `worker.md` check mapping
- repository CI
- repository hooks
- repository scripts
- repository validators

If the proposed check belongs in bundled harness validators or plugin package validation, stage it as a harness migration candidate in `docs/coding-agent/skill-candidates.md` instead.
```

## Default Role Block

Setup writes these into the repository's instruction files as `references/bootstrap-lifecycle.md` (Default Role Block) states. The two forms say the same and differ only in how each runtime opens the Orchestrator. The marker lines are what setup finds the block by; write them as they are.

Codex form, for `AGENTS.md` at the repository root:

```md
<!-- coding-agent-orchestration-harness:default-role:start -->
## Coding Agent Orchestration Harness: the role of a session opened here

- A session opened in this repository with no role chosen is Counsel: load and follow `$counsel`, and say in the first reply that the session is Counsel and how a session is opened as the Orchestrator (a new session whose first message invokes `$orchestration-harness` by name).
- A session whose first message chooses the Orchestrator, by invoking `$orchestration-harness` by name or by saying it is opened as the Orchestrator, is the Orchestrator: load and follow `$orchestration-harness` and not `$counsel`.
- A skill loaded because its description matched gives a session no role.
<!-- coding-agent-orchestration-harness:default-role:end -->
```

GitHub Copilot form, for `.github/copilot-instructions.md`:

```md
<!-- coding-agent-orchestration-harness:default-role:start -->
## Coding Agent Orchestration Harness: the role of a session opened here

- A session opened in this repository with no role chosen is Counsel: load and follow the `counsel` skill, and say in the first reply that the session is Counsel and how a session is opened as the Orchestrator (a new chat with the `Orchestrator` agent selected in the Agent dropdown).
- A chat with the `Orchestrator` agent selected in the Agent dropdown is the Orchestrator: follow that agent and not the `counsel` skill.
- A skill loaded because its description matched gives a session no role.
<!-- coding-agent-orchestration-harness:default-role:end -->
```
