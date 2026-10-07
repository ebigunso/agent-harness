# Brief: Process principles in the plugin

- status: ratified by ebigunso on 2026-10-07 ("I ratify the brief, hand it over after the current run closes."). Asked before ratifying whether there is anything the work must not do or must ask before doing, he added nothing.
- handed to: agent-harness-orchestrator on 2026-10-08, after the run under first-use-in-a-fresh-repository-brief.md was reported ready (pull request 84), as he directed: "hand it over after the current run closes."
- drafted by: agent-harness-counsel, from discussion with ebigunso on 2026-10-07
- product basis: the product owner's own words in this ratified brief. ebigunso owns the harness; no product philosophy and no engineering philosophy exist for this repository.
- provenance tags: *(told)* = ebigunso said it; *(agent-proposed)* = Counsel originated it and he accepted it. His quoted words with the date stand beside each.
- kind marks: **gives** (what the work must give him; it binds), **constraint** (fixed regardless), **means** (a way to get what a gives-statement asks for; the run builds from it and may better it).

This brief is the grounds for the work. It is passed verbatim; do not paraphrase it into a plan as if the paraphrase were the requirement. It states what and why. How is the Orchestrator's, except where a means is stated, and a means does not bind.

## Who it is for and why

- Someone runs the harness in any repository, owned or not, and the agents working there ask the questions that keep agent-written code from accumulating the debt agents produce when nobody pushes back, without the harness imposing any stance on what the code should look like. **gives** *(told 2026-10-07, project name redacted by Counsel under his standing privacy rule: "I want to discuss if parts of the engineering philosophy I arrived at in the [other project] repository should be incorporated into the harness itself. I think the things stated there are applicable to any repository I own, but for those I don't own some of the principles may conflict with the repository's norm." and, of Counsel's split between process principles and code norms: "incorporating the process principles seems like a good idea")*
- The distinction, as Counsel put it and he took it: a process principle changes what the agent asks, not what the code is, and conflicts with no repository's norms; a code norm (what the code should be) is a repository's own, stated in its engineering philosophy, and the plugin stays neutral on it so that the audit grades against whatever document the repository has. **constraint** *(agent-proposed; accepted 2026-10-07 with the words above)*

## The process principles

Each is drawn from an engineering philosophy of his, ratified in another repository of his on 2026-10-07; the lines quoted are from that document and are his. Each is stated here as what the agent does, not as what the code must be.

- Before a design is accepted, each piece of it is reassessed against the goal that was actually given with two questions: what is it for (name the thing in the goal the piece serves; if it prevents something, say what situation that arises in and how likely it is in everyday use), and what does it cost (debt, operational complexity, effect on future change, blast radius relative to the task). A piece that exists only to prevent something is the exception and has to make its case; when the questions pull a draft toward a smaller design, the smaller design is the right one. **gives** *(told, from the document: "Before a design is accepted, each piece of it is reassessed against the goal that was actually given." Where the plugin already asks part of this at plan review, the change is to ask all of it.)*
- A discovered issue reopens the design; it does not slip in. When something arises mid-implementation, it is weighed against the task's scope, what it implies for the shape of the implementation and how it sits under the repository's philosophies, and the question is put whether the original design is still the right one; it is either noted for its own task or the design changes, and it is never absorbed into the current change as if it had been part of the task. **gives** *(told, from the document: "A discovered issue reopens the design; it does not slip in." The plugin's existing record on discoveries within authorized work is checked against this and brought in line where it differs.)*
  - "Its own task" does not mean its own plan. The Orchestrator reads a discovered issue as one of three: within the task as given, which is fixed in place because it was always part of it; a change to the design, which revises or extends the current plan; or a matter for later, noted for its own task. Revising or extending the plan is fine as long as the whole is still kept in line with every criterion set for the work. **gives** *(told 2026-10-07: "It might be too much to have every finding be put aside for its own task, if that is interpreted to mean its own plan. Revising a plan, or extending it is fine, as long as the whole is still kept in line with all of the criteria we have set.")*
  - The guard: a plan revised or extended mid-run goes back through the same gate that admitted it, for what changed, before any of the change is built: the plan review and the value audit on the plan as it now stands, graded as a whole against the brief and the philosophies and not against the issue that prompted it. No extension is built on the Orchestrator's own judgement alone, and the audit's existing scope test, which escalates expansion beyond the brief, applies to the revision as to a draft. The two questions apply to each piece the revision adds. **means** *(agent-proposed, answering his caution: "But this if executed poorly, is a vulnerability where scope creep and tunnel vision can slip in, so we have to be careful on how we design it.")*
- A report says what was left out and why, what was not verified, and scopes down out loud rather than quietly building more to be safe; it does not describe what was done in a way that cannot be faulted. **gives** *(told, from the document: "say what was left out and why, say what was not verified, and scope down out loud rather than quietly building more to be safe." The plugin's report contracts are checked against this.)*
- Evidence has served once its claim is recorded: test output, probe results, captured samples and the like do not go into what is merged and do not lie around the working tree; the default is overruled only when an artifact carries more meaning than evidence and future work rests on it, with the case made rather than assumed. **gives** *(told 2026-10-06: "Test artifacts that doesn't serve a purpose after they are used while building a feature, should be removed rather than left in place. Those are different from test code that catches regressions."; and from the document: "Evidence has served once its claim is recorded." On 2026-10-06 he said no recorded rule was required yet; incorporating it as a plugin default is part of this brief's ask of 2026-10-07.)*
- What is added carries its reason: a guard, a limit, a compromise states in place what it is for and when it could go, so the next agent can remove it when the need lapses. **gives** *(told, from the document: "What is added carries its reason.")*

## Limits

- No stance on what code should be enters the plugin: nothing on compatibility, on smallness of design as a target, on refactoring, on what is irreversible. Those remain a repository's to state in its own engineering philosophy. **constraint** *(told 2026-10-07: "for those I don't own some of the principles may conflict with the repository's norm."; the line between the kinds is Counsel's and he took it)*
- No mechanism for carrying an owner's engineering philosophy between repositories is built. **constraint** *(told 2026-10-07: "a way to port my own stance between repositories doesn't have to be built. It's just an occasional thing so I can handle it myself without introducing mechanisms into the harness.")*
- Where a repository's engineering philosophy or rules say otherwise on any of these, the repository's text is the legible authority and wins. **constraint** *(agent-proposed, from the document's own "Real authority must be legible")*
- Where a principle is already in the plugin in part, the work tightens the existing text rather than adding a second statement of it. **means** *(agent-proposed)*

## Core scenarios

Agent-proposed; ratified with the brief.

1. A plan review in a repository with no engineering philosophy: the Reviewer asks of each piece what it is for and what it costs, and a piece that only prevents an unlikely situation is named as such.
2. A Worker notices an issue mid-task: it is reported as reopening the design or noted for its own task, and the change does not grow to absorb it.
3. A final report lists what was left out and what was not verified.
4. A run's closing review names any evidence artifact left in the change.

## Pass conditions

- Agent-checkable: the package validators pass; each principle is present once in the plugin text at the place where it acts; no new text states a code norm; the existing record on discoveries is consistent with the second principle, revised and returned to him by name where its decision changes.
- Human-only: whether, in his next real run, the questions were asked without the harness pushing a stance of its own.

## Left out on purpose

- The three principles of the document themselves, what it aims for, and what it must not become: a repository's own. *(told, see Limits)*
- Carrying his standing engineering philosophy into new repositories by setup. *(told, see Limits)*
