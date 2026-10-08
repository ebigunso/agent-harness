---
name: value-documents
description: The forms of the value documents a target repository carries (product philosophy, engineering philosophy, initiative brief, discussion notes) and the companion beside each philosophy, what each means, where each lives, and who may write or change each. Use when drafting, changing, locating, handing over, reading or grading against one of them. It is the home of no session role and holds no role's procedure; any procedure of a role appearing in it is misuse.
---

# Value Documents

Four document types in the target repository carry what the person directing the work wants; this skill calls that person the owner. The product owner is whoever is entitled to state the product values and answer product-level questions for that work; the owner takes product-level questions to the product owner, and when one person is both, nothing here is special. A companion beside each philosophy records its provenance and ratification. Counsel writes these documents; the Orchestrator and the value auditor read them. This skill states their forms, meaning, locations and ownership only: any procedure of a role appearing in it is misuse. Decision records are not defined here and keep their own form and process.

## Rules for all four

- Only what the person entitled to ratify a document ratified counts: the product owner for a product philosophy, the owner for a brief and the engineering philosophy. Ratification is that person's act; a record in a file records it and is not it.
- The owner's reading surface is three kinds of document: decision records, the product philosophy and the engineering philosophy. They shape later implementation decisions, so the owner reads them and objects to anything even slightly off.
- Both philosophies sit above decision records. A conflict between the two philosophies is never inferred; the owner settles it, and the ruling is written into the engineering philosophy.
- Neither philosophy need be complete up front. They grow from what each initiative forces into words and from verdicts on results, and are revised by discussion after implementation and measurement shed new light.
- A philosophy says what the person who may change it ratified; it need not be in that person's wording. It is prose: no statement in it carries a provenance tag and no ratification record sits inside it. Which statements Counsel originated, and the ratification, are in its companion.
- A date in a value document or a companion is the owner's local calendar date, since the owner is the one ratifying; the peer channel's timestamps are left as the channel gives them.
- A statement in a brief that is not ready to settle is marked provisional where it stands. In a philosophy the prose stays unmarked: the mark is recorded in its companion, naming the statement.
- None of these documents is required to take the form of the experience chain (a person with a given persona, does something, experiences something as a result, and so gains certain values). A document may use that framing where it helps communicate, and each states the concept the discussion settled on in whatever terms state it best. A product persona is the product owner's to state; Counsel supplies none and no values for one.

## Where each is, who changes it, who reads it

| Document | Located by | Changed by | Read by |
|---|---|---|---|
| Product philosophy | pointer line in `common.md` | the product owner only | Counsel, Orchestrator, auditor |
| Engineering philosophy | pointer line in `common.md` | the owner only | Counsel, Orchestrator, auditor |
| Initiative brief | `docs/coding-agent/briefs/active/<initiative>-brief.md` | Counsel, on the owner's ratification | Counsel, Orchestrator, auditor |
| Philosophy companion | `<philosophy-stem>-companion.md`, in the same folder as its philosophy | Counsel, on the ratifier's word | Counsel, Orchestrator, auditor |
| Discussion notes | `<initiative>-notes.md`, in the same folder as its brief; for a philosophy's discussion, which has no brief, `<philosophy-stem>-notes.md` beside that philosophy | Counsel; the Orchestrator for three kinds of entry | Counsel, Orchestrator; never the auditor |

- The two philosophies have no fixed path. Each is located only by a pointer line in the target repository's `docs/coding-agent/rules/common.md`, section "Repository Reference Documents". That pointer line is the only location there is; a philosophy's companion and notes are found beside the file it names.
- A pointer line is added, removed or repointed by the Orchestrator only, and only on the owner's word, with one exception: setup, the `rulebook` skill's bootstrap and refresh, records a pointer line itself for a document as that skill states (`skills/rulebook/references/bootstrap-lifecycle.md`, Philosophy Lines), the person hears of it in the setup report, and the person's objection removes it. Counsel never edits rule files.
- "Only" in the Changed by column means the text changes only on that person's ratification, and Counsel writes what was ratified. The Orchestrator, its subagents and the auditor never edit either philosophy or its companion.
- Briefs have the lifecycle plans have. A brief is written under `docs/coding-agent/briefs/active/` and is under `docs/coding-agent/briefs/completed/` once the owner has accepted its final stack of pull requests; its discussion notes are in the same folder as the brief in either state.
- A completed brief authorizes nothing: only a brief under `active/` can govern a run.

## Product philosophy

- Standing. Only the product owner writes or amends it, and it may exist whoever directs the work. It states the behaviour the product owner wants from using the product, what the product owner wants out of it, and what the product owner does not want it to be.
- Product values are the product owner's. Any amendment to a product philosophy is the product owner's to state. Where there is no product philosophy and the owner is not the product owner, a product-level judgement the request does not explicitly cover is likewise the product owner's and nobody else's; where a product philosophy exists, it is reasoned from. The engineering philosophy is unchanged by this.
- Form: prose that gives a view to reason from, with success written as observable behaviour. No fixed fields, no length limit, no tags and no ratification record; those are in its companion.
- It never refers to the engineering philosophy.

## Engineering philosophy

- A separate document, complete without the product philosophy. It says how the owner wants the project to look, which is broader than trade-off stances and can include things like data model expectations.
- It works at mostly the same level as the product philosophy and may refer to it. Its form is the product philosophy's.

## Initiative brief

- One initiative's acceptance. It states what and why. How is the Orchestrator's, except where the brief states a means, or a mechanism that is itself what the owner cares about.
- It holds the design: the experience someone gains from the feature. A design may be only a desired behaviour, which is open-ended, and may include a UI design. The design lives in the brief; no formal design document is written before the work.
- Each statement carries a tag, told (someone said it), inferred (Counsel inferred it and nobody objected), or agent-proposed (Counsel originated it and it was accepted), and, for anything told or accepted, the quoted words of the person who said it with the date.
- Each statement may also carry a kind mark: gives (what the work must give), constraint (fixed regardless), or means (a way, settled in discussion, to get what a gives-statement asks for). Gives and constraints bind. A means is ratified with the brief like any other statement and does not bind: the run builds from it. The mark is on the statement, not a layout: a brief keeps whatever sections state its concept best, and a means stays beside the thing it serves. A statement with no kind mark binds, so a brief with none is read with every statement binding.
- It traces to statements in the product philosophy where there is one, and to the request as received where there is not. It states which of three it is, so the auditor and the Orchestrator can tell without asking: it traces to a product philosophy; or it is ratified in the owner's words where the owner is the product owner; or it carries the request as received from a product owner who is not the owner, in which case the product owner's words are kept as received and Counsel adds nothing to them as product value.
- Each pass condition is marked agent-checkable or human-only. A human-only condition passes only by the owner's judgement of the result.
- What the owner says the work must not do, or must ask before doing, is written into it as constraints and ratified with the brief.
- It may carry core scenarios: a few scenarios the owner defines with Counsel beforehand, ratified with the brief. They are evidence of the experience, not its definition: a run that satisfies every one and misses the experience has not delivered the design. A run may add scenarios of its own; those are its reading of the design. A brief with no core scenarios has none; nobody writes them for the owner.
- It may list what was discussed and left out on purpose, with why, each drop confirmed by the owner.
- It records its ratification by quoting the owner's words with the date.
- The file on disk is the requirement, verbatim. A paraphrase of it in a plan or a message is not.
- An amendment is ratified like the brief, and the file on disk governs.
- An amendment to a brief carries its own ratification record, the owner's quoted words with the date, beside the statement it adds or changes. A philosophy's ratification, new or amended, is recorded in its companion.
- Wording that restates an answer of the owner's is ratified by that answer, which is its ratification record, and needs no second yes. What Counsel infers beyond an answer is tagged inferred and has no ratification record of its own, so it is no support for the audit. A statement tagged inferred that the owner ratified with the brief keeps its support.

## Philosophy companion

- One file beside each philosophy, named after it: `<philosophy-stem>-companion.md`, the stem being the philosophy's file name without its extension.
- It holds four things and nothing of the discussion: which statements Counsel originated, each accepted by the person entitled to ratify the philosophy; one ratification record per ratified version of the philosophy, that person's quoted words with the date; which statements are marked provisional, each named; and the gaps against the `counsel` skill's philosophy reference that that person left out, so they are not raised again.
- That person ratifies the philosophy whole: every statement in a ratified version counts on that version's record, whoever originated it.
- It is not a notes file. The Orchestrator and the auditor read it for a philosophy's ratification.

## Discussion notes

- Unratified. One file per initiative, and one beside a philosophy for its discussion, with typed entries: facts, assumptions, decisions, open questions.
- The Orchestrator writes three kinds of entry: an open question for Counsel when the setup has no peer channel; an exception report for Counsel (an item let through on a statement marked provisional, as the audit's verdict states it) when the setup has no peer channel; and a value-level ruling given in the Orchestrator session, recorded as unratified.
- No entry is grounds for a plan or a grade, and no entry is the owner's answer.
- The auditor never reads them.
