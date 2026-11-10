---
status: accepted
adr_type: design
date: 2026-10-29
deciders: ["ebigunso"]
consulted: []
informed: []
supersedes: ["superseded/ADR-D-0061-research-goes-to-the-researcher-role-on-an-option-chosen-from-the-workspaces-own-record--superseded-by-ADR-D-0068.md"]
superseded_by: null
depends_on: ["ADR-D-0048-logical-roles-are-stable-and-each-runtime-names-its-agents-by-its-own-convention.md"]
---

# ADR-D-0068: Each role's model is chosen by a stated reason resolved against the workspace's record, never by a named model

## Context and Problem Statement

An option is a way a workspace has to run a role: an in-session subagent or a peer seat, each on some model. The workspace's record is its own dated account of the options it has, what it has observed of them, and what it may spend.

The harness runs in workspaces whose setups differ, and the models on offer change with every release. A repository that sets up the harness and says nothing about models still needs its dispatches to go to fitting options at once. The fork is whether the harness names where each role runs (a model, a family alias, a tier, or a default seat), leaves each workspace to state its models from nothing, or states why an option is chosen for each role and lets that reason find its option in what the workspace itself records.

## Decision

- Each role's option is chosen by a reason the harness states for that role: what the role's work needs, and how much cost may weigh in it. No role's option is chosen by the name of a model, family, tier or seat.
- No option is held best overall; options are compared for each kind of work.
- The reasons resolve against the workspace's own record. Where the workspace has observed nothing of a family, a dated seed observation the harness ships stands in for it until the workspace's own dated observation replaces it. An observation of a family records what it tends to do, never what it can or cannot do.
- The harness assumes no seat, peer or model: what a workspace has, and what it may spend, is read only from its own record. The harness's rules name no model, family alias, provider, seat or price; only the seed names providers and families, as dated observations.

## Why

A default that names a model, an alias or a seat goes out of date as new models arrive and breaks wherever that setup is absent. A reason that says what a role's work needs, resolved against the workspace's own record, holds across every setup and release, so someone who sets up the harness in a new repository and says nothing about models has fitting dispatches at once.

## Rejected Alternatives

- A default written as runtime family aliases or tiers: it lost because an alias grows old as capabilities advance, costs drop and new classes arrive, the same as a model name; reopen if an alias is found to keep naming the fitting option across model releases with no edit.
- No default, each workspace stating its models from nothing: it lost because using the harness in several repositories then means stating models again in each before the first dispatch goes where it should; rejected outright.
- One ranking of models applied to every role: it lost because an option ahead on one kind of work falls behind on another, so a single order sends some work to an option that fits it poorly; reopen if an option is observed ahead on every kind of work the reasons name.

## Decision Boundary

Invariant: each role's option is chosen by a stated reason of what its work needs and how much cost may weigh, never by a name; options are compared per kind of work, never ranked overall; the reasons resolve against the workspace's own record, with a dated seed of tendencies standing in for a family the workspace has not observed until its own observation replaces it; the harness assumes no seat, peer or model, its rules name no model, family alias, provider, seat or price, and only the seed names providers and families.

Not covered: each reason's wording and parts, and where the reasons are stated; how a reason is read, including how options are ordered for a kind of work and how cost bounds the choice; what setup finds out about the options and how it fills and holds the record; the record's form and where it is kept; the seed's families, entries, level and date; which options, models and allowance a workspace has.

## Validation

- A search of the harness's rules, the seed excluded, finds no model name, family alias, provider, seat or price, and no harness text names a seat, a peer or a model as something a workspace has.
- Review of any change to model routing asks: does it name a model, alias, tier or seat as a default, rank options across kinds of work, write an observation as what a family can or cannot do, or read what a workspace has from anywhere but its own record?

## Revisit When

- On 2026-10-28 each model release was changing which model fit a role and at what cost; if releases stop changing that, a default by name stops going out of date, and the rejected alias alternative reopens.
- On 2026-10-29 no setup had yet resolved the reasons against a lineup; a setup found unable to fill a usable record from the reasons and the seed, or a dispatcher found reaching a worse option than its workspace's record shows with the reasons followed, reopens how the reasons are stated, not the decision.

## More Information

Source of intent: `docs/coding-agent/briefs/completed/model-defaults-by-reason-brief.md`, "Who it is for and why", "What the plugin states" and "Limits". Replaces ADR-D-0061, together with ADR-D-0069 and ADR-D-0070, which carry its research decisions. Related: ADR-D-0048 (logical roles and physical names), ADR-D-0050 (the Auditor role).
