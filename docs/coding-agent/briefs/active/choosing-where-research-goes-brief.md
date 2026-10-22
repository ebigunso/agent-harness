# Brief: Choosing where research goes

- status: ratified by ebigunso on 2026-10-22 ("I ratify the brief, hand it over now."). Asked before ratifying whether there is anything the work must not do or must ask before doing, he added nothing.
- handed to: agent-harness-orchestrator on 2026-10-22
- drafted by: agent-harness-counsel, from discussion with ebigunso on 2026-10-22
- product basis: the product owner's own words in this ratified brief. ebigunso owns the harness; no product philosophy and no engineering philosophy exist for this repository.
- provenance tags: *(told)* = ebigunso said it; *(agent-proposed)* = Counsel originated it and he accepted it. His quoted words with the date stand beside each.
- kind marks: **gives** (what the work must give him; it binds), **constraint** (fixed regardless), **means** (a way to get what a gives-statement asks for; the run builds from it and may better it).

This brief is the grounds for the work. It is passed verbatim; do not paraphrase it into a plan as if the paraphrase were the requirement. It states what and why. How is the Orchestrator's, except where a means is stated, and a means does not bind.

## Who it is for and why

- Someone runs the harness in a workspace with more than one way to do research, in-session subagents, peer seats on other models, or both, and research lands on the Researcher role on the option that suits it, not inside a Worker's task and not inside the dispatcher's own session by default. **gives** *(told 2026-10-22: "I'm feeling that the current harness uses researchers sub optimally, or sends work suited for researchers to other roles instead." and the two phenomena he saw: "Orchestrators send research tasks to workers, sometimes with implementation bundled with it." and "Orchestrators and Counsels spawn sub agent researchers within their own session, rather than sending it to a peer researcher which runs on a model family more suited to that research.")*
- What Counsel found on 2026-10-22 and he took as the cause: the routing reference routes by model strength and the Orchestrator's rule file lists only the worker and reviewer seats as registered peers, so research needing the Codex side goes to the worker seat bundled with its task, and other research stays in-session; Counsel's text names subagents as the only Researcher; the peer list lives in a file Counsel does not read. *(told, as the reality Counsel confirmed at his request: "I suspect this is because it doesn't explicitly state how to send tasks off to researchers versus another role, but I might be mistaken so you should confirm how the reality checks out and assess from there.")*

## What the plugin states

- The plugin states how a dispatcher chooses among the options a workspace has for research; it never assumes a seat, a peer, or a model exists. **constraint** *(told 2026-10-22: "Routing research to a peer seat by default I don't think is the right move. There's no guarantee that the plugin user has the exact peer session setup we use here. The harness should stay agnostic to the environment where it can be." and "The thing I feel needs to be spelled out is, how to choose between the available options.")*
- The choice rule, for the Orchestrator and for Counsel alike. **gives** *(agent-proposed 2026-10-22; he answered "That mostly reads right." with one correction, to the model below.)*
  1. Research is the Researcher role's work, whatever the environment; it is never part of a Worker's task.
  2. The dispatcher reads the workspace's record of options: each seat or subagent type, the role it can hold, its model, and the strengths that model has shown in this workspace.
  3. It picks by the strength the research needs: forensic research wants detail strength, exploratory research wants writing strength, a large corpus wants long-context reading, as the routing reference already states.
  4. Among options with that strength, it picks by what the owner has said of quality against cost for that kind of work (here: research takes the stronger option, cost notwithstanding) and by where the result should live: a peer keeps its own context and returns a report; a subagent returns into the dispatcher's context; bulk reading goes where it will not fill the dispatcher.
  5. Where nothing recorded has the strength, the dispatcher's own model as a subagent, and the observation is recorded with its date.
  6. Research may still be skipped where it may be today, but the record then says what was read instead, so a reviewer can judge whether reading was enough.
- Counsel follows the same rule from the same record; "a read-only Researcher" in Counsel's text means the Researcher role on whichever option the workspace records. **gives** *(agent-proposed; accepted with the above)*
- The workspace's record of options lives in the rule file both the Orchestrator and Counsel read. **means** *(agent-proposed 2026-10-22, put to him as the one item where what he experiences differs: with it, Counsel's check-ups come from the recorded researcher option as their own report; without it, Counsel keeps spawning a subagent whatever the rule says. He answered "That mostly reads right.")*
- Plan review flags research bundled inside an implementation task, as it flags an investigate-first plan since issue 86. **gives** *(agent-proposed; accepted with the above)*

## This repository, as the first application

- The researcher seat `agent-harness-researcher` is registered in the rule files beside the worker and reviewer seats, with its model, GPT-6 Astra. **gives** *(told 2026-10-22: "The rules file fixes should commence" and "the researcher peer is set up with GPT-6-Astra.")*
- The record of options moves from the Orchestrator's rule file into `common.md`, dated as the model observation is now. **means** *(agent-proposed; see above)*
- In this repository, research goes to the researcher seat whenever the strength matches, cost notwithstanding: research is where insight is valued, and a higher-quality outcome is preferred over a cheap one. The owner's cost setting of 2026-10-04 (Opus cheap; Fable and Astra expensive) stays for the other roles. **gives** *(told 2026-10-22, when Counsel put the cost setting against the seat: "I set them up that way since I thought research is the one place where insight is valued highly. Cost concerns are there, but I prefer higher quality outcomes more than cheap sloppy ones.")*

## The Auditor's model, compared before it moves

- Before the Auditor role is moved to another model, the two candidates are compared on real cases: a handful of past audits of this repository, the premature-read cases of 2026-10-04 and 2026-10-05 among them (Counsel first wrote "context-overflow" for the Fable dispatch of 2026-10-15 that was re-dispatched on Opus; the record shows a usage-limit failure, HTTP 429, not an overflow; asked on 2026-10-23 whether that dispatch counts among the audits to replay or stands aside as an availability case that weighs nothing in the choice, he said: "Set them aside."), replayed in fresh runs on each model with the same evidence and tools. The comparison is judged by the grades against what the owner would have decided (adjudicated by him once), by missed and invented issues, by source support, by read order and by completion; never by polish or by agreement with the Orchestrator. The record then states which model showed the strength, dated, and the Auditor moves or stays on that. **gives** *(told 2026-10-22, after the view from the other model family advised comparing before moving and Counsel recommended it: "Compare first, add it to the brief.")*
- Each replay runs in a fresh subagent session or an ephemeral CLI session, never inside a session that holds other context. **constraint** *(told 2026-10-22: "The comparison should run either in a fresh sub agent session, or an ephemeral CLI session.")*
- The researcher seat that gave the consulting view does not audit a run it helped shape; research and audit contexts stay separate. **constraint** *(agent-proposed, from the consulting view kept in the notes; accepted with the above)*
- The Orchestrator and Counsel sessions are not routed by this brief: which model opens them is the owner's choice at the time. The candidate noted for trial is Opus as the Orchestrator's default, Fable kept where planning is visibly better. *(told 2026-10-22, by taking Counsel's reading; nothing is built for it)*

## Directed after the run was reported ready

- A plan task of type research closes on the Researcher's report: its findings answer the task's acceptance, and closeout accepts that report for a research task as it accepts a Worker's for the rest; nothing else in the run changes. **gives** *(told 2026-10-23. The Copilot review of pull request 92 found that a research task, now never a Worker's, could not be closed, since a task closes only on a Worker's report; Counsel put the two ways to him (close on the Researcher's report; or research never a plan task) and recommended the first; his answer: "Go with A.")*

- A Researcher may gather evidence in line with its task, browser evidence included, and the task still closes on its report. What is prohibited for a read-only Researcher, which is the default, is modifying existing files outside the task's scope. The Orchestrator may grant permission to modify a named file, specifically, where touching it is necessary to complete the research objective. **gives** *(told 2026-10-23, asked whether a research task closes when its Researcher saved browser evidence (A) or only when it saved nothing (B): "Gathering evidence in line with the task at hand will be permitted for a researcher. Modifying existing files outside the task's scope is what should be prohibited for a read only research, which should be the default. But, permission to modify files can be granted specifically by the orchestrator, if touching said file is necessary to complete the research objective.")*

- The Copilot review comments on pull request 92 are checked and each is addressed, by fixing the problem or by dismissing it, and in either case the comment is resolved. **gives** *(told 2026-10-23: "Have it check copilot comments on the PR and address them by either fixing the problem, or dismissing it, in either case resolving the comment.")*

## Limits

- No seat, peer or model is assumed by the plugin; what a workspace has is only ever read from its own record. **constraint** *(told, see above)*
- The rule-file changes are this repository's and do not ship in the plugin. **constraint** *(agent-proposed; follows from the one above)*

## Core scenarios

Agent-proposed; ratified with the brief.

1. A plan in this repository needs a forensic census before drafting: the Orchestrator dispatches it to the Researcher role on the recorded detail-strength option, as its own dispatch with its own report; no Worker task carries it.
2. Counsel asks for a check-up on a project's state in this repository: it goes to the recorded researcher option, and the report arrives without filling Counsel's session.
3. The plugin in a workspace with no peers and one model: the same rule yields an in-session Researcher subagent, and nothing in the text asks for a seat that is not there.
4. A draft plan whose implementation task includes "read the module first and then change it": plan review flags the research bundled in.
5. The Auditor comparison: past audits replayed on both models in fresh sessions, the owner adjudicates the expected grades once, and the rule file records which model showed the strength with the date.

## Pass conditions

- Agent-checkable: the package validators pass; the choice rule is stated once in the plugin at the place where dispatch is decided, and Counsel's text refers to it rather than to a subagent; no plugin text names a seat or a model; this repository's `common.md` records the three Codex seats with their models and the dated strength observations, and the Orchestrator's rule file no longer carries a second copy; scenarios 1, 4 and 5 are shown where one can be made, and where one cannot the closeout says so plainly.
- Human-only: scenarios 1 and 2 in his next real run in this repository, and whether a session in another repository of his stops sending research to Workers.

## Left out on purpose

- A default route to a peer researcher. *(told 2026-10-22, see What the plugin states)*
- Any change to which models count as cheap or expensive. *(told 2026-10-04, standing)*
