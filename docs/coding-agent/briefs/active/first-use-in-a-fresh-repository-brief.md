# Brief: First use in a fresh repository

- status: ratified by ebigunso on 2026-10-07 ("Yes, go work on it."), after each statement below was put to him in discussion and answered as recorded beside it. Asked whether there is anything the work must not do or must ask before doing, he added nothing.
- drafted by: agent-harness-counsel, from discussion with ebigunso on 2026-10-07, over a feedback report he brought from the first use of the plugin (0.30.0) in a fresh repository: one Counsel session, one Orchestrator session, peer seats for the other roles; setup run, both philosophies drafted and ratified, shipped in three pull requests.
- handed to: agent-harness-orchestrator on 2026-10-07
- product basis: the product owner's own words in this ratified brief. ebigunso owns the harness; no product philosophy and no engineering philosophy exist for this repository.
- provenance tags: *(told)* = ebigunso said it; *(agent-proposed)* = Counsel originated it and he accepted it. His quoted words with the date stand beside each. His blanket acceptance of the proposals, "Everything except 6 seems good to me." (2026-10-07), covers each statement marked agent-proposed unless other words are quoted beside it.
- kind marks: **gives** (what the work must give him; it binds), **constraint** (fixed regardless), **means** (a way to get what a gives-statement asks for; the run builds from it and may better it).

This brief is the grounds for the work. It is passed verbatim; do not paraphrase it into a plan as if the paraphrase were the requirement. It states what and why. How is the Orchestrator's, except where a means is stated, and a means does not bind.

## Who it is for and why

- Someone opens the plugin in a repository that has never seen it, with a Counsel session and an Orchestrator session, and reaches a ratified philosophy and a first stack without working around the harness. The report named six places where the rules got in the way or had to be worked around; this brief answers each. **gives** *(told 2026-10-07: "I've tested it in a new project I've just started. This is the report of how it went. Read them, and let's discuss what needs to be changed to make the harness better represent the behavior I want.")*

## The philosophy as a human document

- A philosophy is pure prose. No provenance tag on its statements and no ratification record inside it. **gives** *(agent-proposed; the report records that he rejected per-line tags and in-document ratification as mechanical and unreadable and pointed at a prose philosophy of his as the model. Accepted 2026-10-07.)*
- Provenance and ratification live in a companion notes file beside each philosophy, named after it, with one ratification record per ratified version of the document, the owner's quoted words and the date. The Orchestrator and the Auditor look there for the ratification; the companion has a defined home so nobody invents one. **gives** *(agent-proposed; accepted 2026-10-07)*
  - What this gives up, said to him and accepted: the audit can no longer tell line by line which statements are his and which Counsel originated; he ratifies a philosophy whole. *(agent-proposed)*

## A reference for the philosophy

- The plugin carries a reference for what a philosophy states, so that the quality of the final document is consistent across repositories. **gives** *(told 2026-10-07: "The philosophy document could have some reference template though, which would make the final document's quality consistent, just with some considerations into how to have the Counsel not drive discussions to follow that template.")*
- Counsel reads the reference only after the discussion has produced a draft, never before or during; the discussion runs as the person's experience chain and the draft comes out in whatever shape the discussion gave it. Counsel then lists what the reference covers that the draft does not, as gaps for the owner to fill or to leave out; a gap left out is recorded in the companion notes so it is not raised again. The reference never supplies wording: if a gap is real, the words come from another round of discussion. **constraint** *(agent-proposed, as the consideration he asked for; accepted 2026-10-07: "Yes, go work on it.")*
- What the reference states was derived by Counsel from three philosophies of his, two of them written with this plugin, and put to him on 2026-10-07; he said to go ahead with it. The reference states, in this order, what a philosophy holds: a one-sentence thesis; the scene and the measure (who, in what situation, experiences what; the single measure of success and the failure that counts whatever else is right); the core distinction or principles, few and named, each with its reason, and where two goods conflict which wins and why; how it behaves, stated as what someone experiences, by analogy to a person where it helps; what it aspires to, the legitimate future that extension is measured against, and the honest fallback until then; what it must not be, as refusals each countering a comfortable default; success as observable behaviour, a short list one could watch for; a north star, one question every decision is held to, and the tie-break when in doubt; and what is left out on purpose and why. It states what is not in a philosophy and where it goes instead: architecture and the list of the system's parts, named patterns or methods, metrics, backend or vendor choices, and open design questions belong in decision records with their context. It states the qualities Counsel checks for: prose that gives a view to reason from; every principle cutting both ways, what it refuses and what it demands; conflicts between goods settled in the text; reasons present on every line; the comfortable defaults the document exists to counter named as such. It carries one short example in prose, invented, so that no real document of anyone's is in the plugin. **means** *(agent-proposed; told 2026-10-07: "what to put in the philosophy reference, you should use the [one project] philosophy and the newly set up [other project] philosophies as an example here too, deriving what should be stated in the reference." (project names redacted by Counsel under his standing privacy rule) The derivation is Counsel's and he accepted it.)*

## Merging a stack

- The owner's acceptance of a stack by name, reaching the Orchestrator session as his own statement or as Counsel's quoted relay, is enough for the Orchestrator to merge it. The text says so plainly, so that nobody relays "merge" expecting it to act on its own. The runtime's own tool permission for merging is the owner's to grant in that session once, as a standing matter, and no rule text stands in for it. **gives** *(agent-proposed; the report records that "merge" relayed as the owner's word was blocked by the Orchestrator's permission layer and the owner had to approve in that session. Accepted 2026-10-07.)*

## The peer channel

- No acknowledgement rule is added for relays. A lost or truncated message is the delivery mechanism's to fix, not the harness's; Counsel reads the channel's history rather than trusting the inbox until it is fixed. **constraint** *(told 2026-10-02, of the same failure: "this is just a delivery failure and that should better be handled by the delivery mechanism"; put to him again 2026-10-07 after the report asked for a relay contract, and his view had not changed: "Everything except 6 seems good to me.")*
- Counsel takes a seat of its own on the peer channel, distinct from the Orchestrator's, before its first relay; the Counsel text says so and names the convention. **gives** *(agent-proposed; the report records that the Counsel session inherited the Orchestrator's seat and the owner had to reassign it by hand. Accepted 2026-10-07.)*

## Relay admission before setup

- Setup's report offers the standing approval that admits Counsel's relays, so that one acceptance by the owner covers admission from the start. Admission is recorded in the common rule file and nowhere else; a note the Orchestrator keeps for itself is not a place the harness reads. The first request, setup itself, the owner gives to the Orchestrator session directly. **gives** *(agent-proposed; the report records that before setup there is no rule file to hold the approval, so the owner had to type into both sessions, and that the Orchestrator then recorded the admission in its own memory. Accepted 2026-10-07.)*

## One-time setup without a cost on every Counsel session

- Nothing that is done once per repository lives in the Counsel skill that loads on every session. The skill carries two lines: at open, read the Repository Reference Documents section of the common rule file, which Counsel reads anyway, and look for one line there that records Counsel's seat and that relays are admitted; if it is present, nothing more; if it is absent, read a first-session reference and follow it once. The first-session reference holds the one-time procedure: take the seat, offer setup if it has not run, have the standing approval recorded. Setup writes that line in the same section when it records the approval. The philosophy reference is read only when a draft is being checked, never at open. **gives** *(told 2026-10-07: "I'd like to discuss how this one time setup procedure can be introduced without incurring a token cost on every Counsel call."; the shape is Counsel's, put to him and accepted with "Yes, go work on it.")*
  - Where a runtime offers a session-start hook, the plugin's adapter for that runtime claims Counsel's seat from the hook, at no token cost, and the first-session reference says so for such runtimes; where there is none, the reference tells Counsel to claim it. **means** *(agent-proposed)*

## A view from a model of another family

- For the engineering discussion, Counsel obtains a view from a model of a different family than its own. How it gets one is whatever the environment provides, a peer seat, a subagent on another model, or the owner pasting one in, and Counsel says which route it used. The question is put as the discussion put it, and the reply is kept verbatim in the discussion notes with the model and the route named. Where the environment provides no such route, Counsel says so and the owner decides whether to go on without it. **gives** *(told 2026-10-07, of Counsel's first proposal, which named one peer seat: "For 6, I think your proposal is too specific to the environment I operate in. The harness needs to support many environments, where the platform used could be different, and what model the Counsel session operates on could differ." The environment-neutral form is Counsel's, put to him and accepted with "Yes, go work on it.")*

## Smaller frictions

- When a Counsel session opens before setup has run, there is no reference-documents section to read; the Counsel text says what to do then: say that setup has not run, and offer it. **gives** *(agent-proposed; accepted 2026-10-07)*
- Dates in value documents are the owner's local calendar date, since the owner is the one ratifying; the channel's timestamps, which are in UTC, are left alone. **gives** *(agent-proposed; accepted 2026-10-07)*
- The 30-minute expiry of the watch is the runtime's, not the harness's; re-arming it before a relay is the workaround until delivery is fixed, and nothing in the harness changes for it. *(agent-proposed; accepted 2026-10-07)*

## Limits

- This brief changes the forms in the value-documents skill, the Counsel skill, the setup procedure and the Orchestrator's run-side text. Where it changes what an accepted decision record decides, that record returns to him for acceptance by name. **constraint** *(agent-proposed)*
- Machine-specific user names and paths, and the names of his other repositories, do not reach the remote in any file this work touches. **constraint** *(told 2026-10-03, standing: "the usual privacy protection of no machine specific user names and paths leaking applies here too"; and 2026-10-02, that the mention of his other project is removed from durable documents)*

## Core scenarios

Agent-proposed, restating the report's cases; ratified with the brief.

1. A fresh repository, two sessions. The owner gives setup to the Orchestrator directly; the setup report offers the relay approval and one yes records it with Counsel's seat line. The next Counsel session finds the line and does nothing more at open.
2. The owner and Counsel write a product philosophy through discussion. The document is prose; after the draft, Counsel lists the gaps against the reference and the owner fills or drops each; the ratification is recorded in the companion file; the Orchestrator and the Auditor raise no missing-ratification flag.
3. The owner accepts a stack by name through Counsel; the Orchestrator merges it without the owner typing into its session, beyond the tool permission granted once.
4. The engineering discussion in an environment with no second model family: Counsel says so, and the owner decides.

## Pass conditions

- Agent-checkable: the package validators pass; the Counsel skill's word count does not grow for the one-time procedure beyond the two lines; no value-documents text asks for a tag or a ratification record inside a philosophy; the philosophy reference exists with its invented example and names no real project; scenarios 1 and 2 are shown on a fixture repository where one can be made, and where one cannot the closeout says so plainly.
- Human-only: scenarios 2 and 3 in his next real use; whether the reference improved a philosophy's quality without shaping the discussion.

## Left out on purpose

- A relay acknowledgement contract, as the report suggested. *(told, see The peer channel)*
- A named route for the outside-model view. *(told, see A view from a model of another family)*
- Any change to what counts as trivial work. *(told 2026-10-06: "keep the definition of trivial work as is.")*

## Kept from the report as evidence for this repository's own philosophies

The Orchestrator caught a real conflict between the design document and the first draft of the philosophy; it refused to act on an unadmitted relay and flagged a missing ratification record; and the experience-chain framing and the "departs from the conventional answer" test turned a list of agent failure modes into principles the owner recognised as his own. Counsel keeps these in its notes as candidates.
