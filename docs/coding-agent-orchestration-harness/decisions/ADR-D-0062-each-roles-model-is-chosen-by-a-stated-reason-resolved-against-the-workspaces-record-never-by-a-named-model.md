---
status: proposed
adr_type: design
date: 2026-10-29
deciders: ["ebigunso"]
consulted: []
informed: []
supersedes: ["ADR-D-0061-research-goes-to-the-researcher-role-on-an-option-chosen-from-the-workspaces-own-record.md"]
superseded_by: null
depends_on: ["ADR-D-0035-counsel-reaches-into-the-work-only-by-quick-reads-a-read-only-researcher-and-consulted-advice.md", "ADR-D-0048-logical-roles-are-stable-and-each-runtime-names-its-agents-by-its-own-convention.md"]
---

# ADR-D-0062: Each role's option is chosen by a stated reason, resolved against the workspace's own dated record and, for a family the workspace has not observed, a dated seed of tendencies; research goes to the Researcher role, never into a Worker's task, by one rule for the Orchestrator and Counsel alike; the harness assumes no seat, peer or model and its rules name none

Once accepted, this record replaces ADR-D-0061 in full.

## Context and Problem Statement

Terms used here: the person directing the work is the one who says what the work should do and how the project should look, and judges what is built from its behaviour. Counsel is the session that person opens for value discussion, separate from any Orchestrator session. An option is a way a workspace has to run a role: an in-session subagent or a peer seat, each on some model. The record of options is the workspace's own dated record of the options it has and of what it has observed of them.

The harness runs in workspaces whose setups differ, and the models on offer change with every release. A repository that sets up the harness and says nothing about models still needs its dispatches to go to fitting options at once. The fork is whether the harness names where each role runs (a model, a family alias, a tier, or a default seat), leaves the choice to each dispatcher, or states why an option is chosen for each role and how a dispatcher resolves that reason against what the workspace itself records.

## Decision

- Each role's option is chosen by a reason the harness states: the kind of capability the role needs, a split by work type where the work types want different things, and a cost setting; for each work type, the tendency that serves the work, the tendency that harms it, and why.
- No option is ranked best overall; options are compared per kind of capability.
- The reasons resolve against the workspace's dated record of options. For a family the workspace has observed nothing of, they resolve against a seed the harness ships, dated, at the provider level, written as tendencies and never as what a family can or cannot do; a workspace's own dated observation of a family replaces the seed for that family.
- Research is the Researcher role's work in every environment; it is never part of a Worker's task.
- The Orchestrator and Counsel choose where a Researcher runs by one rule, from the one record of options: by the Researcher's reason for the research's work type, under the Researcher's own cost setting, then by where the result should live.
- Where no recorded option fits the research's work type, the dispatcher's own model runs the Researcher as a subagent, and what it showed is recorded with its date.
- Research may be skipped only where the harness allows a skip, and the waiver then says what was read instead.
- The harness assumes no seat, peer or model; what a workspace has is read only from its own record. The harness's rules name no model, family alias, provider, seat or price; only the seed names providers and families, as dated observations.

## Why

The harness runs where it cannot know the setup, and a default that names a model, an alias or a seat goes out of date as capabilities advance, costs drop and new model classes arrive, or breaks wherever that setup is absent; a reason that says what the work needs, resolved against the workspace's own record, serves every setup with the same text and does not expire with a release.

## Rejected Alternatives

- A default written as runtime family aliases or tiers: it lost because an alias grows old as capabilities advance, costs drop and new classes arrive, the same as a model name; reopen if an alias is found to keep naming the fitting option across model releases with no edit.
- No default, each workspace stating its models from nothing: it lost because using the harness in several repositories then means stating models again in each before the first dispatch goes where it should; rejected outright.
- One ranking of models applied to every role: it lost because an option ahead on one kind of work falls behind on another, so a single order sends some work to an option that fits it poorly; reopen if an option is observed ahead on every kind of capability the reasons name.
- A default route to a peer researcher: it lost because no workspace using the harness is guaranteed to have that peer set up; reopen if the harness itself provides a peer setup in every supported runtime.
- An in-session Researcher subagent named as the only option: it lost because research then stays in the dispatcher's session, or goes to a Worker on another model with its task, even where the workspace records an option that suits it better; reopen if workspaces are found to have no option beyond the in-session subagent.
- Each dispatcher left to choose without a stated rule: it lost because research then lands inside Workers' tasks and in the dispatcher's own session by default, for want of a stated way to choose; rejected outright.

## Decision Boundary

Invariant: a role's option is chosen by a stated reason in three parts, with the tendency that serves and the tendency that harms each work type; the reasons resolve against the workspace's dated record and, for an unobserved family, a dated seed of tendencies that a workspace observation replaces; no ordering of options across kinds of capability; research is the Researcher role's work and never part of a Worker's task; one rule chooses where a Researcher runs, for the Orchestrator and Counsel alike, by the Researcher's reason and its cost setting; the dispatcher's own model as a subagent where no recorded option fits; the harness assumes no seat, peer or model, its rules name no model, family alias, provider, seat or price, and only the seed names providers and families.

Not covered: the wording of each reason and of the research rule, and where they are stated; which work types split; each role's cost setting and how a cost-bounded option is found when no allowance is stated; the seed's entries, families and date; the record's form, where it is kept, and how setup fills it and holds it for confirmation; which options, models and allowance a workspace has; how plan review checks a plan for research bundled into another task; when research may be skipped.

## Validation

- A search of the harness's rules, the seed excluded, finds no model name, family alias, provider, seat or price, and no harness text names a seat, a peer or a model as something a workspace has.
- Each role's reason is stated once, where routing is decided, with the tendency that serves and the tendency that harms each work type and why.
- The harness texts that decide where research goes point to the one rule, and none restates a different one.
- Review of any change to model routing or research dispatch asks: does this name a model, alias, tier or seat as a default, rank options across kinds of capability, write a tendency as what a family can or cannot do, default research to one option, or let a Worker's task carry research?

## Revisit When

- On 2026-10-28 each model release was changing which model fit a role and at what cost; if releases stop changing that, a default by name stops going out of date, and the rejected alias and no-default alternatives reopen.
- On 2026-10-29 the harness provided no peer setup of its own, so whether a workspace has peers, and on which models, depended on that workspace alone; a peer setup the harness itself provides in every supported runtime reopens the rejected default route.
- On 2026-10-29 no setup had yet resolved the reasons against a lineup; a setup found unable to fill a usable record from the reasons and the seed, or a dispatcher found reaching a worse option than its workspace's record shows, with the rule followed, reopens how the reasons and the rule are stated, not the decision.

## More Information

Source of intent: `docs/coding-agent/briefs/active/model-defaults-by-reason-brief.md`, "Who it is for and why", "What the plugin states" and "Limits"; for the research rule, `docs/coding-agent/briefs/completed/choosing-where-research-goes-brief.md`, "What the plugin states" and "Limits". Replaces ADR-D-0061 once accepted. Related: ADR-D-0035 (Counsel's read-only Researcher), ADR-D-0048 (logical roles and physical names), ADR-D-0050 (the Auditor role).
