# Value Documents

Four document types in the target repository carry what the person directing the work wants; this reference calls that person the owner. The product owner is whoever is entitled to state the product values and answer product-level questions for that work; the owner takes product-level questions to the product owner, and when one person is both, nothing here is special. This reference is read by Counsel, which writes them; by the Orchestrator, which takes them as the grounds of a run; and by the value auditor, which grades against them. Decision records are not defined here and keep their own form and process.

## Rules for all four

- Only what the owner ratified counts. Ratification is the owner's act; a status line in a file records it and is not it.
- The owner's reading surface is three kinds of document: decision records, the product philosophy and the engineering philosophy. They shape later implementation decisions, so the owner reads them and objects to anything even slightly off. A change to any of them reaches the owner through Counsel with the path to the document itself. A change that adds a standing approval reaches the owner the same way.
- An irreversible or outward-facing action comes back to the owner through Counsel even when the brief or a philosophy covers it; a brief covers the intent, not the moment. The exception is a standing approval: one of the approvals given for all future runs. Standing approvals live under the heading "Standing Approvals" in the target repository's `docs/coding-agent/rules/common.md`, written by the Orchestrator and never by Counsel. One takes effect only after the owner accepts it, and an accepted one applies from the run after the one that adds it; in the run that adds it the action still comes to the owner. A standing approval is given by whoever holds the authority for that action in that repository, and the entry records who gave it; the owner may grant one only within their own authority. Ordinary rule changes do not go to the owner this way.
- Both philosophies sit above decision records. A conflict between the two philosophies is never inferred; it is asked, and the ruling is written into the engineering philosophy.
- Neither philosophy need be complete up front. They grow from what each initiative forces into words and from verdicts on results, and are revised by discussion after implementation and measurement shed new light.
- A statement that is not ready to settle is marked provisional where it stands.
- Value statements are written from the viewpoint of a person's experience, as a chain: a person with a given persona, does something, experiences something as a result, and so gains certain values. The third part is an experience, not an abstract state. This holds for the statements of both philosophies and, in a brief, for its value statements, its human-only pass conditions and its watch list. A part that cannot yet be filled is named as missing, not left out silently, and the statement is marked provisional where the missing part bears on what it decides. A product persona is the product owner's to state, in the philosophy or when a discussion needs one; Counsel supplies none and no values for one. For the engineering philosophy the persona is whoever works on the project later. What the product owner has ratified, and a request as received, keep their wording: they are never recast into chains, an existing philosophy is not rewritten into the form, and a part they leave out is asked through the owner.

## Where each is, who changes it, who reads it

| Document | Located by | Changed by | Read by |
|---|---|---|---|
| Product philosophy | pointer line in `common.md` | the product owner only | Counsel, Orchestrator, auditor |
| Engineering philosophy | pointer line in `common.md` | the owner only | Counsel, Orchestrator, auditor |
| Initiative brief | `docs/coding-agent/briefs/active/<initiative>-brief.md` | Counsel, on the owner's ratification | Counsel, Orchestrator, auditor |
| Discussion notes | `<initiative>-notes.md`, in the same folder as its brief | Counsel; the Orchestrator for three kinds of entry | Counsel, Orchestrator; never the auditor |

- The two philosophies have no fixed path. Each is located only by a pointer line in the target repository's `docs/coding-agent/rules/common.md`, section "Repository Reference Documents". Do not probe paths for one.
- The Orchestrator adds, removes or repoints a pointer line only on the owner's word: the owner's own statement in the Orchestrator session, or Counsel's relay quoting the owner naming the document and its path. Counsel never edits rule files, and Counsel's own statement of a path is not enough.
- "Only" in the Changed by column means the text changes only on that person's ratification, which reaches Counsel through the person directing the work where the two differ, and Counsel writes what was ratified. The Orchestrator, its subagents and the auditor never edit either philosophy.
- Briefs have the lifecycle plans have. A brief is written under `docs/coding-agent/briefs/active/` and moves to `docs/coding-agent/briefs/completed/` when the owner accepts its final stack of pull requests; its discussion notes move with it. The Orchestrator makes the move.
- A completed brief authorizes nothing: only a brief under `active/` can govern a run. The brief that governs a run is the one named in the hand-over, never one chosen by looking in the directory.

## Product philosophy

- Standing. Only the product owner writes or amends it, and it may exist whoever directs the work. It states the behaviour the product owner wants from using the product, what the product owner wants out of it, and what the product owner does not want it to be.
- Counsel never infers product values on the product owner's behalf. Where there is no product philosophy and the owner is not the product owner, product-level judgements the request does not explicitly cover go to the product owner through the owner. Any amendment to a product philosophy goes to the product owner through the owner. The engineering philosophy is unchanged by this.
- Form: prose that gives a view to reason from, with success written as what a person experiences and gains. No fixed fields and no length limit.
- Its statements keep the product owner's wording. It never refers to the engineering philosophy.

## Engineering philosophy

- A separate document, complete without the product philosophy. It says how the owner wants the project to look, which is broader than trade-off stances and can include things like data model expectations.
- It works at mostly the same level as the product philosophy and may refer to it.

## Initiative brief

- One initiative's acceptance. It states what and why; how is the Orchestrator's.
- Each statement carries a tag, told (someone said it), inferred (Counsel inferred it and nobody objected), or agent-proposed (Counsel originated it and it was accepted), and, for anything told or accepted, the quoted words of the person who said it with the date. Counsel writes a brief this way while drafting, not when an audit asks.
- It traces to statements in the product philosophy where there is one, and to the request as received where there is not. It states which of three it is, so the auditor and the Orchestrator can tell without asking: it traces to a product philosophy; or it is ratified in the owner's words where the owner is the product owner; or it carries the request as received from a product owner who is not the owner, in which case the product owner's words are kept as received and Counsel adds nothing to them as product value.
- Each pass condition is marked agent-checkable or human-only. A human-only condition passes only by the owner's judgement of the result.
- It may carry a watch list: a short list, a handful of entries, of the things the owner would want to hear about at once if they came up during the run. The owner writes it with Counsel at the closing pass of the discussion and it is ratified with the brief. The auditor checks every item it grades against it; a hit is reported to Counsel during the run and is neither a grade nor a stop. Each entry names the thing watched for in its own words, inside its chain, so the auditor matches what the entry says. A brief with no watch list has none; nobody writes one for the owner.
- It records its ratification by quoting the owner's words with the date.
- The Orchestrator and the auditor read it from disk, verbatim. A paraphrase of it in a plan or a message is not the requirement.
- An amendment is ratified like the brief. The file on disk governs, and it reaches the Orchestrator as the hand-over did: a relay quoting the owner's ratifying words and naming the brief's path.
- An amendment to a brief or to either philosophy carries its own ratification record, the owner's quoted words with the date, beside the statement it adds or changes. The auditor counts a statement changed during a run as support only when that record is there.

## Discussion notes

- Unratified. One file per initiative, with typed entries: facts, assumptions, decisions, open questions.
- The Orchestrator writes three kinds of entry: an open question for Counsel when the setup has no peer channel; an exception report for Counsel (a watch hit or a provisional-statement item, as the audit's verdict states it) when the setup has no peer channel; and a value-level ruling given in the Orchestrator session, recorded as unratified.
- No entry is grounds for a plan or a grade, and no entry is the owner's answer.
- The auditor never reads them.
