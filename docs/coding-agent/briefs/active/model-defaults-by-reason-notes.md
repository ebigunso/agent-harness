# Model defaults by reason: discussion notes

Counsel's notes for the discussion opened 2026-10-28. Brief not yet drafted; nothing here is ratified.

## The two observations that opened the discussion, 2026-10-28

The owner, on the harness at plugin 1.1.0:

> 1. Orchestrator session tends to ask questions within its own session unprompted, even under a brief and is handed instructions to load the orchestration-harness skill when being dispatched. The default behavior should be to route questions through Counsel.
> 2. Foregoing explicit default model selection in the harness has made use in multiple repositories a hassle, so I'd like to define a default, but which that doesn't pinpoint a model in a way that would become obsolete on every new model release.

On the first, after Counsel traced the plan-approval fallback in the lifecycle gates ("whenever it does not authorize, the paragraph above is the whole rule"):

> I did have a case where the Orchestrator asked for plan approval in its session even under a brief. This should be avoided rather than have that question brought anywhere. Keeping the behavior as is for a run without a Counsel is fine.

On the second, when Counsel proposed runtime family aliases as the stable name:

> Even those model aliases would grow old as capabilities advance, costs drop, and new even more powerful model classes arrive. I'd like to set a default by the reasons models are chosen, which is less likely to become obsolete.

## The owner's reasons for each role, 2026-10-28

Given in full so the default can be written from them:

> I choose what model to use on each role based on what they are good at.
>
> * Orchestrator: A model not prohibitively expensive to run long sessions, and a one that is good at keeping a high point of view, allowing it to make judgements that are good in the bigger picture without fixating on inconsequential minute details. Currently Claude models fit this criteria and GPT models fail it, and I choose Opus 5.5 for being cheap enough and having trustworthy judgement tendencies. Also the current Opus 5.5 beats even Fable 5.1 in long horizon coding tasks, so it's a win there too.
> * Auditor: The model that can give the best insight on open ended questions. Here also Claude models fit the bill, and Fable 5.1 is currently the best in this capability class so I have that used.
> * Researcher: Depends on work type, when insight and ideas are important, it should go to a model type that is good for that (i.e. Claude, Fable 5.1 now), and when rigor and assembling facts are important it should go to a model type good for that (i.e. GPT, 6 Astra now).
> * Worker: Design, writing and UI/UX work to Claude, and Coding work to GPT. Chosen mostly on what they are good at, Claude for design work that requires high point of view, human readable writing and human facing interface design, GPT for logic oriented work where avoiding subtle defects are valued. Use a model where its costs are not prohibitive, but the best model that meets that criteria. Claude Opus 5.5 and GPT 6.1 Sol at the moment, for me. Exact model choice would depend on budget allowance.
> * Reviewer: Mostly chosen on the same grounds as how I choose workers. There's value to running reviews on a model with a different capability suite as the worker that did the work too, but this part I haven't been exercising nearly enough right now.

Counsel's inference from these, put to the owner the same day and not contested: there is no single best model, since the owner's own list has Opus ahead of Fable on long-horizon coding and behind it on open-ended insight; every role's reason names a kind of capability plus a cost ceiling; the reasons use two capability families, wide view (big-picture judgement, open-ended insight, human-facing writing and design) and rigor (fact assembly, defect-averse logic), nearly the writing-strength and detail-strength vocabulary the routing reference already has; two roles split by work type (Researcher, Worker) rather than by role; and the cost ceiling has three settings (none; affordable for long sessions; best within the budget allowance).

Where the first mapping from capability family to actual model comes from in a fresh repository, three options were put: a dated seed observation in the plugin at the provider level, a setup question per family, or a record of the owner's outside any repository. The owner: "Go with the first option." And, before anything is written:

> But I'd like you to do research on what others say about a model family, Claude, GPT, and other model families too like Gemini, Grok, or even things like Qwen, DeepSeek, GLM and the sorts, to see if my personal observation holds, and if possible, more insight into the reasons, so that we can discuss further on what would be good to write and what wouldn't be.
> Doubling as a test run, try having both Claude and GPT model researchers go fetch those from online sources, and with two ways of task dispatch, research all in one run, and one researcher for each topic.

Then: "The test only matters if it's a fresh context, so Codex researcher dispatch for this should go to ephemeral CLI sessions."

## The research run, 2026-10-28 to 29

Sixteen dispatches of one shared prompt (eight roles as dimensions; claims with URL, source kind and date; reasons offered; list prices; thin or contradictory evidence; a closing section on the hypothesis "Claude models show wide-view judgement, open-ended insight and human-facing writing and design; GPT models show rigor, fact assembly and defect-averse logic"; about 900 words per family). Two models, Claude Fable 5.1 as subagents of the Counsel session and GPT-6 Astra in fresh `codex exec` sessions with web search, each in two shapes: all seven families in one task, and one task per family.

| Side | Shape | Outcome | Wall clock | Words | Unique URLs | Tokens |
|---|---|---|---|---|---|---|
| Fable | one task per family (7) | 7 of 7 reports | 8 to 12 min each, in parallel | 1,230 to 1,610 | 18 to 27 | 100k to 200k each |
| Fable | all families in one | 1 report | 30 min | 4,975 | 57 | 200k |
| Astra | one task per family (7) | 7 of 7 reports | 2.5 to 12 min each, in parallel | 850 to 960 | 12 to 18 | 88k to 119k each |
| Astra | all families in one | failed twice, same way | 9.6 and 12.5 min | 19 and 20 | 0 | 254k and 278k |

The two failed Astra runs share one mechanism, read from their logs. The task did not fit one context window: after about 250k tokens the session compacted, and on compaction the user-level session-start hook fired a second time and re-injected its instruction text (the harness loader block). The model's final message then answered that re-injected text ("Understood. I'll follow the repository's orchestration harness...") instead of delivering the report, and the last-message capture held nothing. Backend request failures clustered around the same minutes in both runs. The seven per-family Astra sessions never compacted and all delivered. The first run's working directory also held sibling reports being written, and its log shows it read three of them; the rerun was in an empty directory and failed the same way, so that was not the cause. Nothing was retried a third time: two failures by one mechanism is the result.

Observations on the two sides, Counsel's: Astra kept to the length asked and found a different stratum of sources (METR's September 2026 assessment, SlopCodeBench, Big-Big-SycoBench, CRUX, Sonar's and Endor's evaluations, a 116-task review study) with a steady "what this does not establish" discipline; Fable overran the length by half, cited more practitioner write-ups and leaderboards, and gave more texture per claim. The two sides overlapped little in sources, so running both widened coverage rather than duplicating it. Per-family dispatch gave more sources per family than the all-in-one on either side; the all-in-one gave the only cross-family comparison with one consistent grading legend (Fable's), and was the one shape that failed on the Codex side. The Codex side's research unit has to fit in one context window; compaction in an ephemeral session loses the task.

## What the fifteen reports say about the hypothesis

Every report on both sides reached the same shape of verdict: the hypothesis describes real stylistic tendencies and overstates them as capability gaps. Fable on GPT: "the hypothesis describes real stylistic tendencies (breadth, polish, verbosity vs depth, terseness) but overstates them as capability gaps." Astra on GPT: "a useful provisional workflow preference, not an established family distinction."

Best supported:

- Claude: UI and design structure (Subframe October 2026, Kilo April 2026, GenDesigns, LH-Bench); sustained scope and context across long sessions (Vals Terminal-Bench 4.0, two dual-use practitioner write-ups); review that "goes broad" with more findings and more false positives (Greptile, 1,000 pull requests, July 2026).
- GPT: literal, in-bounds spec-following, the best-replicated qualitative finding across sources, though a September 2026 thread on Astra in Codex reports the opposite; browsing-style fact retrieval (BrowseComp, vendor-reported); token economy and lower cost per task; review that favours precision over recall.
- Harness and version effects are as large as family effects: the same DeepSeek checkpoint scores 42 in one harness and 32 in another on the same suite; Anthropic's own postmortem traced a two-month quality dip to harness bugs; nearly every head-to-head used a model two releases old.

Not supported:

- "GPT is defect-averse": evidence splits by test. SlopCodeBench favours GPT-5.5; a 50-seeded-bug test favours Claude; a 116-task study found GPT-5.5 reviewing Opus 4.7 lowered correctness while Opus reviewing GPT raised it. GPT-5.5's 86% hallucination rate on AA-Omniscience (it abstains less) is the opposite of rigor as calibration; Astra improved it to 51%, and Gemini 4 Argon sits at 15%.
- "Claude writes better": the one blind prose evaluation had GPT-5 ahead; Every's panel prefers Astra for technical writing; Fable 5 prose was judged dense.
- "Open-ended insight": no independent measurement on either side. METR (September 2026) saw no large advance in researcher judgement for Opus 5.5; CRUX had expert reviewers reject papers from both Astra and Fable.

Reasons offered in the sources: Anthropic's stated move from rule lists to a constitution so the model exercises judgement in novel situations, and its character training; OpenAI's reinforcement learning on execution feedback with verification, and its targeted training for structured artifacts; token economy (Astra about 27k output tokens per task against 78k for Fable); context handling in the harness (file-saved tool outputs and compaction recall on one side, middle-truncation of outputs on the other). All are plausible mechanisms; none is causal evidence of a family trait.

Where the other families sit: Gemini, a high-context reasoner with the lowest measured hallucination rate and the weakest session discipline (loops, over-eager edits); Grok, knowledge-work first and a cheap executor, mid-pack on coding; Qwen, DeepSeek and GLM, cheap execution-focused models that invent APIs on unfamiliar libraries and misread vague prompts, with GLM strong on web-design preference arenas and security finding. None occupies either pole.

On the Reviewer's cross-family preference the owner has not exercised: three sources support it (a practitioner's "the model that wrote the code is the worst possible judge of it", Greptile's finding that each model is blind to the bug classes it introduces, and the 116-task study), with the 116-task study adding that direction matters.

## The owner's words after the research, 2026-10-29

On the Worker's coding reason: "'literal and in-bounds' seems more appropriate. Matches what I feel too."

> And, one thing you might want to look at is the recent Frontier Code 2.0 benchmark, that shows how models do in situations where initial task prompts are intentionally vague. I feel this represents real life workflows better than anything else, and it supported Opus 5.5 being the best choice. Fable 5.1 being behind I feel is the execution side lacking, not insight.

Looked up the same day in one fresh Astra session (145 seconds). FrontierCode 2.0 is Cognition's, released 2026-10-27: 132 repository tasks with "humanlike and deliberately concise" descriptions, judged on mergeability (correctness, interpretation of the incomplete request, design, scope, integration) by hidden tests and maintainer-authored rubrics; a failed blocker scores zero. Cognition's own snapshot, best effort per model: Opus 5.5 45.5%, GPT-6 Astra 42.8%, Sonnet 5.5 41.0%, GPT-6.1 Sol 39.0%, Fable 5.1 32.4%, Grok 4.7 28.6%, Gemini 4 Argon 26.3%. Artificial Analysis reproduced it independently with its own scaffold and judge and found the same order: Opus 46.4%, Astra 42.4%, Fable 35.7%. The one mechanism Cognition names is "outright overthinking, where a model talks itself into implementing a misreading of the requested change", and across four models higher effort reduced thoroughness failures but increased scope failures. Fable's score falls from 32.4% at xhigh to 31.7% at max while its cost rises. No source attributes Fable's gap to execution or to judgement; the researcher marked both readings unsourced.

Counsel's read, mine: this is the closest measurement found to the Orchestrator's reason (judgement of an under-specified ask that stays in scope), and it supports Opus 5.5 for that role on independent as well as vendor data. It does not support "GPT models fail it": Astra is second, three points behind. On the owner's reading of Fable's gap, the evidence is silent; the only mechanism the publisher names is a judgement one, and Fable's score falling as effort rises is consistent with it, so the gap is better recorded as unexplained than as execution.

## The owner's own account of the GPT tendency, 2026-10-29

Asked to say what the "high point of view" criterion rests on, as his own observation:

> Well, being put that way, I think what I'm most feeling about the GPT family models are, that it gets fixated on minute details that is inconsequential when considering the bigger picture, and holds back work or pulls designs towards "safe" alternatives without considering what would be best for the overall experience or aim, when left to its own devices.
> This tendency spirals into self invented work of hardening and test building that in many cases are overly constraining or covers risks that have very low probability to occur in real life settings, and overall less progress in the same amount of time. Putting it back on track was observed possible by human redirection or judgement by Claude models without its context poisoned by repeated requests by GPT, as my own account.

This is the observation the seed records for the GPT family, dated and as his. It is consistent with what the sources circled without naming: GPT-5.5 "defaulting to conventional choices"; the October 2026 user thread on Codex reporting "fast progress initially" then prolonged fixing and polishing; the Astra thread where a five-line script became a configuration system; and the Astra researcher's own note that "pedantry results from rewarding work rather than completion" was a causal explanation no source had made. His account also states the remedy the sources do not: redirection by a person, or by a Claude model whose context the GPT model's repeated requests have not shaped, which is the Orchestrator-over-Worker arrangement the default already has.

## His corrections to the first draft of the brief, 2026-10-29

> Don't carry my word directly in the plugin text quoted, or take it literally.
> The reasoning stated for the defaults should cover what the preferred tendency to have is on a kind of work, and what tendency is detrimental and the whys.
> The two observations you named to record in this repository, I think is not worth keeping so can be kept out.
>
> The first version having observed tendencies written only for Claude and GPT is fine.
> The cross family review should actually take a different shape than what you described. Different model families do find things one missed, but it depends on the situation if the expected type of findings are what you want in the first place. For example, you don't want to be pointed out about edge case breakages when you're still working out a design, or to have one skim over a code and say OK for what needs to work precisely in production environments.

Applied: the plugin's reasons are its own prose in the form preferred tendency, detrimental tendency, why; his words stay in the brief as provenance only; the two test-run observations are left out; the Reviewer is chosen by the kind of finding the stage wants, and a different family follows from that, not from the difference itself.

## Questions from the run

- 2026-10-29, the plan-draft audit held as ask-now, the plan not authorized until the brief carries the answer. The verdict's question, verbatim: "When the owner confirms the record without naming an allowance, does the Worker go to the best fitting option regardless of cost, or does setup keep holding until an allowance is stated?" The Orchestrator also reported that a second question of the audit, on research's cost, came from a line of its own that had left the brief and was put back to the brief's words (research to the stronger option cost notwithstanding, in every repository); nothing of it comes to him. Brought to him as an experience framing the same day, with Counsel's third shape (no allowance: the cheapest option with the needed capability). His answer in two parts, 2026-10-29: "I'd lean towards your proposal, but only if the best option would be considered expensive by what budget the environment runs on. Today that is mostly true for any setup since the best models are expensive even on the biggest budget plan available, but this may change, so it should be checked against how expensive a model is compared to whatever subscription plan or pay as you go budget." Then, on the fallback: "the fall back should be the second best model, also judged for its cost, and so on until it lands on something acceptable." Written into the brief under Directed during the run and relayed.

- 2026-10-29, a finding during the run that bears on the design, the part held: a probe of setup in a fresh repository with three models of one family found every role tied, since the observations describe how a family tends to behave and not how its models differ, and the agent picked on its own judgement. The Orchestrator's question: which model should a role get in such a repository, without his being asked about models? Options put: (a) rank the family's models by the capability the runtime itself states for each; no-cost-limit roles take the most capable, the others walk down with the cost check he directed; (b) the session's own model for every role until a difference is observed; (c) show the tie and let him pick at confirmation. Brought to him as an experience framing the same day, with Counsel's recommendation of (a). His answer, 2026-10-29: "When there are only one provider to choose models from, using the cost walk-down only is the sensible choice. Basically, the plugin should name the base thought process for the ideal case, and where some environment restrictions prevent some parts to be fully applied, it should be applied in a best effort manner for anything that still is possible to apply." Written into the brief under Directed during the run and relayed.

- 2026-10-29, the Orchestrator's inferred call in the revised plan (D9): with no fit order, the walk's order taken from cost, most costly first. Passed to him for information; he corrected it: "The most costly is not the right way to put it. It would be what is most capable for the job. Model cost and capabilities sometimes doesn't pair up, like in the case of Opus 5.5 and Fable 5.1 in it's long horizon execution case." Written into the brief under Directed during the run and relayed. He then added, on where the capability baseline comes from: "The baseline for what the model capabilities are and if they are fitting, should be researched if not readily available at setup time, so that it can choose whatever is most fitting in the situation regardless of what models are the frontier, or what models are allowed in the environment the harness runs on." Written into the brief the same way and relayed.

- 2026-10-29, the plan-draft audit of 05:10Z held one clause as ask-now: when he names only the kind of plan or budget, which model a Worker gets. The Orchestrator's three shapes: (a) as the text stands, the least costly model and a note that the limits are missing, work going ahead; (b) hold until the limits or size are stated; (c) the kind read as room for the most capable, stepping down when usage shows strain. Counsel added a fourth, mine: research the named plan's limits as the capability baseline is researched, falling to (a) only where they cannot be found. His answer: "I think researching where things are ambiguous is the right way to go." Written into the brief under Directed during the run and relayed.

## Counsel's first read of the result, 2026-10-29

Written before any part of the closeout audit's verdict was seen; facts from the Orchestrator's note reporting pull request 94 ready.

- The note states the human-only pass condition as the brief states it: setup in another repository of his yields a usable record without his stating a model. Matches.
- The note says nothing of what the result does beyond that; the plugin's content against the brief's gives (reasons per role in three parts, the two capability families, the seed as dated tendencies for Claude and GPT only, setup filling and showing the record, the cost walk-down ordered by capability, research of the baseline and of a named plan's limits) is to be read from the audit's marks, which were asked for.
- One decision record, ADR-D-0066, replacing ADR-D-0061, goes to him for acceptance by name with its path.
- Value documents changed during the run: the brief's section Directed during the run, every entry Counsel's, each carrying his words; no change by the run itself was reported.

Finished after the closeout audit's material arrived (verdict of 2026-10-29 05:49, as the Orchestrator sent it):

- Nothing marked as bearing on direction; nothing let through on a provisional statement; the run wrote no value document; the five entries under Directed during the run confirmed as Counsel's.
- Seven inferred items, each cheap to undo, each a mechanism the brief left open: the cost measure as the share of the plan or budget the role's work would take (and the Orchestrator judged by it); a Researcher tie-break for a large corpus in one pass; setup's own research running on the session's model at first setup; the research kept on dated resolution lines and the Runs on line; a refresh keeping the confirmed record until he confirms the new; this repository's record showing the environment as not recorded with his 2026-10-04 cost setting standing. Counsel's read, mine: none changes what he experiences at setup beyond what he said, so none goes to him as a question; told to him as the list, for information.
- The version bump to 1.2.0 was not graded; run 1 bumps to the same version. Counsel's observation, mine, passed to him: the two pull requests cannot both land as 1.2.0, so whichever merges second carries a further bump, which is the Orchestrator's to handle.
- ADR-D-0066 goes to him with its path, as recorded above.

From the Copilot review of pull request 94, 2026-10-29, one finding, for information: at a refresh, setup's own research goes by the confirmed record, so if a model change removed the Researcher option that record names, the research is sent to a model no longer offered and the refresh cannot show its new record. It sits in the Orchestrator's inferred route (item d). The fix is one clause: where the confirmed Researcher option is no longer offered, the research runs on the session's own model, and the new record is not used before he confirms it. Nothing changed without his direction; whether to build it and what to do with the thread are his. Brought to him the same day. A second finding the same day: the Worker's fallback for an unknown budget is worded for "the kind of budget but not which plan or how large", so a plan he names whose limits are neither stated nor found falls outside it, though setup sends that case there; his answer of 2026-10-29 ("only where they cannot be found") already decides it, and the fix is one clause keying the fallback to limits or size missing, plan named or not. Both findings, the Orchestrator says, are small fixes it can build together if he directs it, each reviewed and audited, the threads resolved. He asked Counsel to inspect whether the findings matter, since the harness runs on a capable model and not inert code. Counsel's read from the text, mine: neither needs patching. The second finding's case is already covered by the same sentence it cites ("Only where none could be found does it fall back") and by the setup text, which names the fallback for a named plan whose limits cannot be found. The first finding's case falls through the research route's own rule that research goes to the session's model where no recorded option fits, and a refresh re-reads the options from the runtime, so a model no longer offered is known as such; a capable reader reroutes. His direction: "Dismiss the five threads with a line each, nothing patched." Written into both briefs and relayed.

## Counsel's first read of the result after the rewrite, 2026-11-02

Written before any part of the closing audit's verdict was seen; facts from the Orchestrator's note reporting pull request 94 ready again, and from a quick read of the two records.

- Against his direction of 2026-11-02 (one decision per record, stated to survive rewording of the plugin text, mechanism out): the held draft is now two records. ADR-D-0066 decides that a role's option is chosen by a stated reason against the workspace's record, never by a name; ADR-D-0067 that research is the Researcher's work, placed by one rule for the Orchestrator and Counsel alike. Each title states its decision in a line; each Decision is three or four bullets; routes, the record's form, the walk's order and the seed's entries are all under Not covered. Matches.
- The Orchestrator reports a lesson it drew: the first rewrite dropped, with the route, the commitment behind it (research never goes without a Researcher), caught and kept at decision level. Counsel's read, mine: that is the failure the older-records run should watch for, and it goes into that run's notes as an observation for the owner's next contact.
- Together the two replace ADR-D-0061, which retires only when both are accepted. Both go to him by name with their paths.
- Value documents changed: the brief's Directed during the run, the entry of 2026-11-02 included, all Counsel's. The plugin text is unchanged by the rewrite.

Finished after the closing audit's material arrived (second closeout audit of 2026-11-02, held nothing):

- One item marked direction, inferred: ADR-D-0067 rewords ADR-D-0061's fallback commitment from "the dispatcher's own model as a subagent" to "a Researcher the dispatcher can always run itself"; the specific option, the order of weighing and what is recorded move to Not covered, stated in the plugin text. Counsel's framing test, mine: in a workspace whose record names nothing fitting, research still goes to a Researcher either way, and the two wordings read the same at the level of what anyone experiences; the generalization is the altitude he asked for. Not a question for him; named to him as the line to look at when he reads 0067, since the audit asked that he see it.
- Two further inferred items, cheap to undo: the research-skip clause moved to Not covered (0061 listed it there too); ADR-D-0061's retirement line names both replacing records, a two-record form the standard's single "Replaced by" does not name.
- The first closeout dispatch had marked two items direction (the fallback's option and the research rule's factors left to plugin text); both were restored at decision level before the second dispatch. Recorded as the failure mode for the older-records run.
- The run itself changed no value document.

## His direction on the Why sections, 2026-11-08

- On reading ADR-D-0066: "66 needs to stop citing the brief as authority in the why section. ADRs needs to state reasons beyond that." Asked whether the second sentence reaches ADR-D-0067 and the five records on pull request 93: "Yes, apply it to 67 and the five on 93 as well." Written into the brief under Directed during the run, relayed in his words.

## Counsel's read of the result after the Why rewrite, 2026-11-08

First read, before the audit's summary was read: ADR-D-0066's Why states that a named default goes out of date and breaks where the setup is absent, while a reason resolved against the workspace's record holds across setups and releases; ADR-D-0067's Why states that research left inside a Worker's task or the dispatcher's session runs on whatever model that work runs on, and that one rule for both sessions places it where it suits, with an option the dispatcher can always run holding the role where none fits. Neither cites the brief. Nothing marked.

Finished after the audit's material: review approved after two rounds; the closeout audit held nothing and every reading agreed. One item inferred: the reasons a Why leaves to the Decision and Rejected Alternatives, since the brief does not say whether every clause needs its reason in the Why. Counsel's framing test, mine: a reader finds the reason for each clause in the record either way; the two read the same, not a question for him. The run changed no value document.

## His directions of 2026-11-11

- On reading the proposed records: "67 has two decisions in one. Split them. Also, renumber the ADRs so the numbering skip within one PR is not there anymore." Written into the brief, relayed in his words.
- On the model routing: "A new model, Fable 5.2 has come out and has changed the landscape slightly. Now, the spot previously occupied by Opus 5.5 should rather be routed to Fable 5.2 with low reasoning effort, and only when Fable 5.2 is unavailable, should fall back to Opus 5.5 with high effort." Written into the brief, relayed in his words. Put to him and open: whether the resolutions that name Fable 5.1 (the Auditor; the Researcher's insight and ideas) move as well.

## Counsel's read of the result after the split, 2026-11-11

The Orchestrator's report of 2026-11-10 16:48Z arrived with the review's and the audit's outcome in it, so this read was not formed before that material; it is one read, of the records themselves.

- The record he read as ADR-D-0067 is now ADR-D-0069 (research is the Researcher role's work in every environment and never part of a Worker's task) and ADR-D-0070 (the Orchestrator and Counsel place a Researcher by one and the same rule). The record he read as ADR-D-0066 is ADR-D-0068. No Why cites a brief.
- ADR-D-0069 keeps a second bullet: where no recorded option fits, a Researcher the dispatcher can always run holds the role. Counsel's reading, mine: it is what "in every environment" requires and not a second decision; his to judge when he reads the record.
- ADR-D-0070, marked, mine: its second rejected alternative loses "because research then lands inside Workers' tasks", which is ADR-D-0069's matter, the same slip the review corrected in its Why; and its Decision lists what the rule weighs, one item of which ("where its result is to be used") has no reason in the Why. What the rule weighs is the rule's content, and the record's own Not covered leaves how it weighs to the plugin text.
- Review approved after one correction; the closeout audit held nothing. The six things the run settled without his word are graded as extending his statements. The run changed no value document.
- Pull request 94 is not at its final state: his direction on Fable 5.2 reached the Orchestrator after this report and changes the workspace's record on the same branch.

## Artificial Analysis figures for the cost line, read 2026-11-11

Why: asked whether the record's cost line still holds with Fable 5.2 at low reasoning effort in the place Opus 5.5 held, he said: "the cost argument can be settled if you search for the cost vs intelligence and time vs intelligence benchmark results on Artificial Analysis." He also answered that day: "Yes, move to Fable 5.2 with high effort." (the Auditor and the Researcher's insight work) and "Move the Auditor now, no comparison needed."

Who read them: the Researcher role on the peer seat `agent-harness-researcher` (GPT-6 Astra), dispatched by Counsel over the peer channel, read-only. Source: artificialanalysis.ai only, each model's own page, read 2026-11-11 (Asia/Tokyo). The pages identify Intelligence Index v5.0.1. Intelligence, cost per task, token prices, time per task, output speed and time to first answer token are the figures the pages display. Total index cost and end-to-end time are the unrounded values of the datasets embedded in the same pages. USD throughout.

| ID | Label on the site | Page | Intelligence Index | Cost per task | Total index cost | Input / output per 1M tokens |
|---|---|---|---:|---:|---:|---:|
| A | Claude Fable 5.2 (Low, Default Fallback) | /models/claude-fable-5-2-low | 54 | 3.10 | 2861.7798750438624 | 8.00 / 40.00 |
| B | Claude Fable 5.2 (High, Default Fallback) | /models/claude-fable-5-2-high | 62 | 9.08 | 7105.770618708859 | 8.00 / 40.00 |
| C | Claude Opus 5.5 (High, Default Fallback) | /models/claude-opus-5-5-high | 52 | 3.46 | 2715.9800012757146 | 4.00 / 20.00 |
| D | Claude Fable 5.1 (Low, Default Fallback) | /models/claude-fable-5-1-low | 39 | 4.47 | 3885.935028642357 | 10.00 / 50.00 |
| E | Claude Fable 5.1 (Medium, Default Fallback) | /models/claude-fable-5-1-medium | 43 | 5.56 | 4896.576659417077 | 10.00 / 50.00 |
| F | Claude Fable 5.1 (High, Default Fallback) | /models/claude-fable-5-1-high | 47 | 7.54 | 6617.890073737758 | 10.00 / 50.00 |
| G | Claude Fable 5.1 (Xhigh, Default Fallback) | /models/claude-fable-5-1-xhigh | 50 | 10.85 | 10096.622784971296 | 10.00 / 50.00 |
| H | Claude Fable 5.1 (Max, Default Fallback) | /models/claude-fable-5-1 | 49 | 12.99 | 13326.778522254179 | 10.00 / 50.00 |
| I | GPT-6 Astra (Low) | /models/gpt-6-astra-low | 43 | 1.42 | 1650.7484149542447 | 10.00 / 50.00 |
| J | GPT-6 Astra (Medium) | /models/gpt-6-astra-medium | 52 | 2.73 | 2638.289263719404 | 10.00 / 50.00 |
| K | GPT-6 Astra (High) | /models/gpt-6-astra-high | 55 | 3.24 | 3203.9990980989687 | 10.00 / 50.00 |
| L | GPT-6 Astra (Xhigh) | /models/gpt-6-astra-xhigh | 55 | 3.66 | 3746.2153585654264 | 10.00 / 50.00 |
| M | GPT-6 Astra (Max) | /models/gpt-6-astra | 57 | 6.24 | 5661.179482563332 | 10.00 / 50.00 |
| N | GPT-6.1 Sol (Low) | /models/gpt-6-1-sol-low | 35 | 0.16 | 237.90799854181154 | 2.00 / 10.00 |
| O | GPT-6.1 Sol (Medium) | /models/gpt-6-1-sol-medium | 46 | 0.36 | 388.5687768506756 | 2.00 / 10.00 |
| P | GPT-6.1 Sol (High) | /models/gpt-6-1-sol-high | 50 | 0.59 | 573.1677910130082 | 2.00 / 10.00 |
| Q | GPT-6.1 Sol (Xhigh) | /models/gpt-6-1-sol-xhigh | 52 | 0.76 | 717.7081569486036 | 2.00 / 10.00 |
| R | GPT-6.1 Sol (Max) | /models/gpt-6-1-sol | 55 | 1.27 | 1123.9739209537065 | 2.00 / 10.00 |

| ID | Time per index task, min | Output speed, tok/s | Time to first answer token, s | End-to-end time, s |
|---|---:|---:|---:|---:|
| A | 6.5 | 92 | 8.73 | 66.75418154858342 |
| B | 17.5 | 93 | 30.79 | 109.92921746225001 |
| C | 9.5 | 105 | 24.49 | 106.7747722015722 |
| D | 7.6 | 83 | 5.24 | 56.36778648528129 |
| E | 9.9 | 81 | 8.24 | 72.84260559095836 |
| F | 13.3 | 83 | 13.58 | 83.10333854023953 |
| G | 19.4 | 83 | 58.37 | 188.562859202125 |
| H | 22.5 | 87 | 166.95 | 391.68471855832286 |
| I | 3.8 | 40 | 3.29 | 99.87419650091665 |
| J | 6.9 | 43 | 5.69 | 112.56847905461113 |
| K | 9.7 | 40 | 61.10 | 239.27059205539445 |
| L | 11.4 | 39 | 107.70 | 318.39662489568144 |
| M | 23.1 | 37 | 239.21 | 560.2278735114118 |
| N | 1.8 | 55 | 2.52 | 63.104844797083274 |
| O | 3.8 | 59 | 4.10 | 72.62337346045187 |
| P | 6.5 | 58 | 32.53 | 134.3396866699982 |
| Q | 9.3 | 54 | 62.08 | 192.99467906013896 |
| R | 20.1 | 56 | 150.99 | 364.9323790487797 |

What the site's measures are, as the Researcher reports its definitions:

- Cost per task is an evaluation-weighted average after dividing each evaluation's cost by its task count. Total index cost sums the evaluations' token costs, cache and reasoning included, repeats excluded. The two can rank models differently.
- Time per index task is modelled (task output tokens divided by end-to-end output speed, weighted over the evaluations), not a stopwatch measurement. No total time to run the whole index is published. End-to-end time is the site's mean over single-request workloads. Performance figures average the preceding five days.
- No separately titled coding or agentic index is on the model pages; nothing was substituted for one. The Fable 5.1 pages mark that release deprecated.
- How it was read: direct reads of the public model pages and the chart datasets embedded in them; no other source, no estimate, no interpolation.

The Researcher's reading, its words: "Fable 5.2 Low costs less per weighted index task than Opus 5.5 High ($3.10 versus $3.46), but its total index-run cost is higher and its input/output token rates are $8/$40 versus $4/$20 per million. Its Intelligence Index score is higher, 54 versus 52, which does not imply a win on every individual coding task. Its listed time per index task is shorter (6.5 versus 9.5 minutes), its first-answer latency is lower (8.73 versus 24.49 seconds), and its published end-to-end value is also lower. Opus 5.5 High has the higher output speed, 105 versus 92 tokens per second. These figures support Fable 5.2 Low as a candidate for the former Opus role on weighted task cost, time and aggregate intelligence, while the total-run and token-price measures do not support calling it universally cheaper."

## Counsel's reads for the writing, 2026-10-29

Mine, for discussion:

- The owner's reasons hold as tendencies and as a routing rule for his work; the sources do not license writing them as capability facts. A seed observation should say what the families tend toward and who observed it when, not what they can and cannot do.
- "Defect-averse logic" is the one phrase in the owner's reasons the evidence contradicts most directly; "literal, in-bounds execution with precision-leaning review" is what the sources support for GPT.
- Harness and version effects argue for the record's observations being dated and redone on a model change, which the record already requires.
