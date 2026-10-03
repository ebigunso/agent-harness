---
name: value-documents
description: The forms of the value documents a target repository carries (product philosophy, engineering philosophy, initiative brief with its watch list, discussion notes), what each means, where each lives, and who may write or change each. Use when drafting, changing, locating, handing over, reading or grading against one of them. It is the home of no session role and holds no role's procedure; any procedure of a role appearing in it is misuse.
---

# Value Documents

Four document types in the target repository carry what the person directing the work wants; this skill calls that person the owner. The product owner is whoever is entitled to state the product values and answer product-level questions for that work; the owner takes product-level questions to the product owner, and when one person is both, nothing here is special. Counsel writes these documents; the Orchestrator and the value auditor read them. This skill states their forms, meaning, locations and ownership only: any procedure of a role appearing in it is misuse. Decision records are not defined here and keep their own form and process.

## Rules for all four

- Only what the owner ratified counts. Ratification is the owner's act; a status line in a file records it and is not it.
- The owner's reading surface is three kinds of document: decision records, the product philosophy and the engineering philosophy. They shape later implementation decisions, so the owner reads them and objects to anything even slightly off.
- Both philosophies sit above decision records. A conflict between the two philosophies is never inferred; the owner settles it, and the ruling is written into the engineering philosophy.
- Neither philosophy need be complete up front. They grow from what each initiative forces into words and from verdicts on results, and are revised by discussion after implementation and measurement shed new light.
- A statement that is not ready to settle is marked provisional where it stands.
- None of these documents is required to take the form of the experience chain (a person with a given persona, does something, experiences something as a result, and so gains certain values). A document may use that framing where it helps communicate, and each states the concept the discussion settled on in whatever terms state it best. A product persona is the product owner's to state; Counsel supplies none and no values for one.

## Where each is, who changes it, who reads it

| Document | Located by | Changed by | Read by |
|---|---|---|---|
| Product philosophy | pointer line in `common.md` | the product owner only | Counsel, Orchestrator, auditor |
| Engineering philosophy | pointer line in `common.md` | the owner only | Counsel, Orchestrator, auditor |
| Initiative brief | `docs/coding-agent/briefs/active/<initiative>-brief.md` | Counsel, on the owner's ratification | Counsel, Orchestrator, auditor |
| Discussion notes | `<initiative>-notes.md`, in the same folder as its brief | Counsel; the Orchestrator for three kinds of entry | Counsel, Orchestrator; never the auditor |

- The two philosophies have no fixed path. Each is located only by a pointer line in the target repository's `docs/coding-agent/rules/common.md`, section "Repository Reference Documents". That pointer line is the only location there is.
- A pointer line is added, removed or repointed by the Orchestrator only, and only on the owner's word. Counsel never edits rule files.
- "Only" in the Changed by column means the text changes only on that person's ratification, and Counsel writes what was ratified. The Orchestrator, its subagents and the auditor never edit either philosophy.
- Briefs have the lifecycle plans have. A brief is written under `docs/coding-agent/briefs/active/` and is under `docs/coding-agent/briefs/completed/` once the owner has accepted its final stack of pull requests; its discussion notes are in the same folder as the brief in either state.
- A completed brief authorizes nothing: only a brief under `active/` can govern a run.

## Product philosophy

- Standing. Only the product owner writes or amends it, and it may exist whoever directs the work. It states the behaviour the product owner wants from using the product, what the product owner wants out of it, and what the product owner does not want it to be.
- Product values are the product owner's: a product-level judgement the request does not explicitly cover, and any amendment to a product philosophy, is the product owner's to state and nobody else's. The engineering philosophy is unchanged by this.
- Form: prose that gives a view to reason from, with success written as observable behaviour. No fixed fields and no length limit.
- Its statements keep the product owner's wording. It never refers to the engineering philosophy.

## Engineering philosophy

- A separate document, complete without the product philosophy. It says how the owner wants the project to look, which is broader than trade-off stances and can include things like data model expectations.
- It works at mostly the same level as the product philosophy and may refer to it.

## Initiative brief

- One initiative's acceptance. It states what and why, and contains no how.
- Each statement carries a tag, told (someone said it), inferred (Counsel inferred it and nobody objected), or agent-proposed (Counsel originated it and it was accepted), and, for anything told or accepted, the quoted words of the person who said it with the date.
- It traces to statements in the product philosophy where there is one, and to the request as received where there is not. It states which of three it is, so the auditor and the Orchestrator can tell without asking: it traces to a product philosophy; or it is ratified in the owner's words where the owner is the product owner; or it carries the request as received from a product owner who is not the owner, in which case the product owner's words are kept as received and Counsel adds nothing to them as product value.
- Each pass condition is marked agent-checkable or human-only. A human-only condition passes only by the owner's judgement of the result.
- It may carry a watch list: a short list, a handful of entries, of the things the owner would want to hear about at once if they came up during the run. The owner writes it with Counsel and it is ratified with the brief. Each entry names the thing watched for in its own words. A brief with no watch list has none; nobody writes one for the owner.
- It records its ratification by quoting the owner's words with the date.
- The file on disk is the requirement, verbatim. A paraphrase of it in a plan or a message is not.
- An amendment is ratified like the brief, and the file on disk governs.
- An amendment to a brief or to either philosophy carries its own ratification record, the owner's quoted words with the date, beside the statement it adds or changes.

## Discussion notes

- Unratified. One file per initiative, with typed entries: facts, assumptions, decisions, open questions.
- The Orchestrator writes three kinds of entry: an open question for Counsel when the setup has no peer channel; an exception report for Counsel (a watch hit or a provisional-statement item, as the audit's verdict states it) when the setup has no peer channel; and a value-level ruling given in the Orchestrator session, recorded as unratified.
- No entry is grounds for a plan or a grade, and no entry is the owner's answer.
- The auditor never reads them.
