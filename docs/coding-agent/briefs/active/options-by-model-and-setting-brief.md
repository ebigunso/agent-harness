# Brief: An option is a model at the setting it runs at

- status: ratified by ebigunso on 2026-11-11. Drafted on his request of that day ("Draft a small brief for the option-and-setting change."), shown to him as the experience framings of its four decisions, its limits and its three core scenarios, and after his answers on reasoning effort, the fallback statement and what the work must not do, asked whether he ratified it, he said: "I ratify it."
- drafted by: agent-harness-counsel, from discussion with ebigunso on 2026-11-11
- handed to: agent-harness-orchestrator on 2026-11-11
- product basis: the product owner's own words in this brief once ratified. ebigunso owns the harness; no product philosophy and no engineering philosophy exist for this repository.
- provenance tags: *(told)* = ebigunso said it; *(agent-proposed)* = Counsel originated it and he accepted it; *(inferred)* = Counsel inferred it. His quoted words with the date stand beside each told statement. The agent-proposed statements were accepted with the ratification.
- kind marks: **gives** (what the work must give; it binds), **constraint** (fixed regardless), **means** (a way to get what a gives-statement asks for; the run builds from it and may better it).

This brief is the grounds for the work. It is passed verbatim; do not paraphrase it into a plan as if the paraphrase were the requirement. It states what and why. How is the Orchestrator's, except where a means is stated, and a means does not bind.

It changes text the run "Model defaults by reason" introduced. That run's brief is context for this one, not authority.

## Who it is for and why

- Someone who sets up the harness in a repository, or refreshes its record when a model changes, gets a record that tells apart the settings a model can run at wherever they differ in what the model can do for a role's work or in what it costs. Each role then lands on the fitting setting of the fitting model, without that person naming either. **gives** *(agent-proposed 2026-11-11)*
- Why: on 2026-11-11 he routed this repository's roles by model and setting together. *(told 2026-11-11: "the spot previously occupied by Opus 5.5 should rather be routed to Fable 5.2 with low reasoning effort, and only when Fable 5.2 is unavailable, should fall back to Opus 5.5 with high effort."; and of the Auditor and the Researcher's insight work: "Yes, move to Fable 5.2 with high effort.")* The figures he named showed one model at two settings eight index points and about three times the cost per task apart, with the lower setting matching a different model's cost. The plugin's text speaks of an option's model only, so a setup that follows it records one option per model, judges that model's cost once, and cannot find a stronger model's lower setting as the fit a cost-bounded role can afford. *(agent-proposed 2026-11-11; the figures are in the notes beside the completed brief `model-defaults-by-reason`)*

## What the plugin states

A setting, here, is anything about how a model runs that the dispatcher or the person who set up a seat can choose, and that changes what the model can do for a role's work or what it costs. *(agent-proposed 2026-11-11)* The plugin's text names reasoning effort as the setting it means. **gives** *(told 2026-11-11, on the draft's limit that no setting be named: "I think \"reasoning effort\" is now wide spread enough in text generation models that are released from anywhere, that it's safe to write into the harness.")* The same statements hold of any other setting a runtime offers that changes what a model can do or what it costs; the text says so without naming one. *(inferred)*

- An option is a way to run a role: a seat or a subagent, on a model, at a setting. Two settings of one model that differ for some role's work, or in cost, are two options in the workspace's record. **gives** *(agent-proposed 2026-11-11)*
- Everything the plugin already says of options holds of options so understood: the capability finding is made for the option, its cost is judged for the option, the fit ranking orders options, and the cost-bounded walk goes down that ranking. **gives** *(agent-proposed 2026-11-11)*
- A resolution names its option's setting, and a dispatch on that resolution runs at it wherever the runtime lets the dispatch choose. Where the runtime gives no such choice, or a seat's setting was fixed by whoever set it up, the record states the setting the option runs at, and what the plugin says of best effort applies. **gives** *(agent-proposed 2026-11-11)*
- Setup records the settings worth telling apart, not every setting a model offers, and shows them for confirmation with the rest of the record. **means** *(agent-proposed 2026-11-11; a model may offer many settings, most of them no role's fit)*
- Where the option a role resolves to is unavailable when a dispatch is due, the role goes to what its resolution names for that case; where the resolution names nothing, to the next option in the fit ranking for that work that the role's cost setting accepts. The dispatcher says which option it used and why. **gives** *(agent-proposed 2026-11-11; the plugin states this today for research only. He named the option-and-setting change when asking for this brief; this statement is Counsel's addition, and asked whether it stays in the brief or comes out he said 2026-11-11: "Stay.")*

## Limits

- No model name, family alias, provider, seat or price enters the plugin's rules; the seed names providers only, as observations with dates. **constraint** *(told, in the completed brief `model-defaults-by-reason`)* Reasoning effort is named as a kind of setting; no level of it is named, since levels belong to a workspace's record like the models they are set on. **constraint** *(inferred, from his words of 2026-11-11 above and the limit before this sentence)*
- His words are not carried into the plugin's text as quotations, and are not read to the letter. **constraint** *(told, a standing direction: "Don't carry my word directly in the plugin text quoted, or take it literally.")*
- The reasons by role do not change, and no resolution in this repository's record changes; that record has named settings since 2026-11-11. **constraint** *(inferred)*
- The decision records ADR-D-0068, ADR-D-0069 and ADR-D-0070, accepted 2026-11-11, are not contradicted by this. If the run finds that a decision record is needed or that an accepted one must be reworded, that record returns to him for acceptance by name. **constraint** *(inferred for the first sentence; told, a standing direction, for the second)*

- Asked whether there is anything this work must not do, or must ask him before doing, beyond the limits above: nothing. *(told 2026-11-11: "None.")*

## Core scenarios

Agent-proposed 2026-11-11; shown to him before ratification and ratified with the brief.

1. Setup runs in a fresh repository whose runtime offers one model at more than one setting. The record lists the settings that differ as options of their own, each with its finding and its cost, and a cost-bounded role resolves to the stronger model's lower setting where that is the fit its cost setting accepts.
2. In this repository, a run opens after the change. Each dispatch runs at the setting its resolution names: the Auditor's at the one recorded for it, a design-writing Worker's at the one recorded for it.
3. The option a Worker's writing task resolves to is unavailable when the dispatch is due. The task goes to what the resolution names for that case, and the dispatcher's report says which option ran it and why.

## Pass conditions

- Agent-checkable: the package validators pass; the plugin's rules name no model and no level of reasoning effort; the text that defines the record of options, and the text setup follows to fill it, speak of an option's reasoning effort as well as its model.
- Human-only: the next time a model arrives with more than one setting, he judges whether the refreshed record found the fitting setting for each role without his naming it.

## Left out on purpose

- Reopening pull request 94 for this. *(agent-proposed 2026-11-11: he had accepted it and it was being merged)*
- Recording every setting of every model at setup. *(agent-proposed 2026-11-11: see the means above)*
