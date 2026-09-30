# Value Documents

Four document types in the target repository carry what the person directing the work wants; this reference calls that person the owner, and says "product owner" where owning the product is the point. It is read by Counsel, which writes them; by the Orchestrator, which takes them as the grounds of a run; and by the value auditor, which grades against them. Decision records are not defined here and keep their own form and process.

## Rules for all four

- Only what the owner ratified counts. Ratification is the owner's act; a status line in a file records it and is not it.
- The owner's reading surface is three kinds of document: decision records, the product philosophy and the engineering philosophy. They shape later implementation decisions, so the owner reads them and objects to anything even slightly off. A change to any of them reaches the owner through Counsel with the path to the document itself. A change that adds a standing approval reaches the owner the same way.
- An irreversible or outward-facing action comes back to the owner through Counsel even when the brief or a philosophy covers it; a brief covers the intent, not the moment. The exception is a standing approval: what the owner approved for all future runs. Standing approvals live under the heading "Standing Approvals" in the target repository's `docs/coding-agent/rules/common.md`, written by the Orchestrator and never by Counsel. One takes effect only after the owner accepts it, and an accepted one applies from the run after the one that adds it; in the run that adds it the action still comes to the owner. Ordinary rule changes do not go to the owner this way.
- Both philosophies sit above decision records. A conflict between the two philosophies is never inferred; it is asked, and the ruling is written into the engineering philosophy.
- Neither philosophy need be complete up front. They grow from what each initiative forces into words and from verdicts on results, and are revised by discussion after implementation and measurement shed new light.
- A statement that is not ready to settle is marked provisional where it stands.

## Where each is, who changes it, who reads it

| Document | Located by | Changed by | Read by |
|---|---|---|---|
| Product philosophy | pointer line in `common.md` | the owner only | Counsel, Orchestrator, auditor |
| Engineering philosophy | pointer line in `common.md` | the owner only | Counsel, Orchestrator, auditor |
| Initiative brief | `docs/coding-agent/briefs/<initiative>-brief.md` | Counsel, on the owner's ratification | Counsel, Orchestrator, auditor |
| Discussion notes | `docs/coding-agent/briefs/<initiative>-notes.md` | Counsel; the Orchestrator for two kinds of entry | Counsel, Orchestrator; never the auditor |

- The two philosophies have no fixed path. Each is located only by a pointer line in the target repository's `docs/coding-agent/rules/common.md`, section "Repository Reference Documents". Do not probe paths for one.
- The Orchestrator adds, removes or repoints a pointer line only on the owner's word: the owner's own statement in the Orchestrator session, or Counsel's relay quoting the owner naming the document and its path. Counsel never edits rule files, and Counsel's own statement of a path is not enough.
- "The owner only" means the text changes only by the owner's ratification in a Counsel session, and Counsel writes what was ratified. The Orchestrator, its subagents and the auditor never edit either philosophy.
- Briefs accumulate in one directory. The brief that governs a run is the one named in the hand-over, never one chosen by looking in the directory.

## Product philosophy

- Standing. It exists only where the person directing the work owns the product. It states the behaviour the product owner wants from using the product, what the product owner wants out of it, and what the product owner does not want it to be.
- Counsel never infers product values on behalf of an absent product owner. Where the person directing the work does not own the product, product-level judgements go to that person, who takes them to the requester; the engineering philosophy and the engineering side are unchanged by this.
- Form: prose that gives a view to reason from, with success written as observable behaviour. No fixed fields and no length limit.
- Its statements keep the owner's wording. It never refers to the engineering philosophy.

## Engineering philosophy

- A separate document, complete without the product philosophy. It says how the owner wants the project to look, which is broader than trade-off stances and can include things like data model expectations.
- It works at mostly the same level as the product philosophy and may refer to it.

## Initiative brief

- One initiative's acceptance. It states what and why; how is the Orchestrator's.
- Each statement carries its provenance: told (the owner said it), inferred (Counsel inferred it and the owner did not object), or agent-proposed (Counsel originated it and the owner accepted it).
- It traces to statements in the product philosophy where there is one, and to the request as received where there is not. It states which of three it is, so the auditor and the Orchestrator can tell without asking: it traces to a product philosophy; or it is ratified in the words of the person directing the work, who owns the product; or it carries the request as received from a requester who is not that person, in which case the requester's words are kept as received and Counsel adds nothing to them as product value.
- Each pass condition is marked agent-checkable or human-only. A human-only condition passes only by the owner's judgement of the result.
- It records its ratification by quoting the owner's words with the date.
- The Orchestrator and the auditor read it from disk, verbatim. A paraphrase of it in a plan or a message is not the requirement.
- An amendment is ratified like the brief. The file on disk governs, and Counsel tells the Orchestrator that it changed.
- An amendment to a brief or to either philosophy carries its own ratification record, the owner's quoted words with the date, beside the statement it adds or changes. The auditor counts a statement changed during a run as support only when that record is there.

## Discussion notes

- Unratified. One file per initiative, with typed entries: facts, assumptions, decisions, open questions.
- The Orchestrator writes two kinds of entry: an open question for Counsel when the setup has no peer channel, and a value-level ruling given in the Orchestrator session, recorded as unratified.
- No entry is grounds for a plan or a grade, and no entry is the owner's answer.
- The auditor never reads them.
