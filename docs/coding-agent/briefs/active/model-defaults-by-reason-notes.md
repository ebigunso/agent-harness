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

## Counsel's reads for the writing, 2026-10-29

Mine, for discussion:

- The owner's reasons hold as tendencies and as a routing rule for his work; the sources do not license writing them as capability facts. A seed observation should say what the families tend toward and who observed it when, not what they can and cannot do.
- "Defect-averse logic" is the one phrase in the owner's reasons the evidence contradicts most directly; "literal, in-bounds execution with precision-leaning review" is what the sources support for GPT.
- Harness and version effects argue for the record's observations being dated and redone on a model change, which the record already requires.
