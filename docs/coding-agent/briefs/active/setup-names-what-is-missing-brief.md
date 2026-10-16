# Brief: Setup names what is missing

- status: ratified by ebigunso on 2026-10-05 ("I ratify the brief, hand it over after the run closes."). Asked before ratifying whether there is anything the work must not do or must ask before doing, he added nothing.
- handed to: agent-harness-orchestrator on 2026-10-05, after the design-led long runs run closed. On his word it is taken up after the change to the audit positions: "Yes, do it first before the next one prepared." and again "Yes, do the small fixes first."
- drafted by: agent-harness-counsel, from discussion with ebigunso on 2026-10-05
- product basis: the product owner's own words in this ratified brief. ebigunso owns the harness; no product philosophy and no engineering philosophy exist for this repository.
- provenance tags: *(told)* = ebigunso said it; *(inferred)* = Counsel inferred it and he did not object; *(agent-proposed)* = Counsel originated it and he accepted it. For anything told or accepted, his quoted words with the date stand beside the statement.
- kind marks: **gives** (what the work must give him; it binds), **constraint** (fixed regardless), **means** (a way to get what a gives-statement asks for; the run builds from it and may better it).

This brief is the grounds for the work. It is passed verbatim; do not paraphrase it into a plan as if the paraphrase were the requirement. It states what and why. How is the Orchestrator's, except where a means is stated, and a means does not bind.

## Who it is for and why

- Someone opens a repository and runs the harness setup once. When it finishes, everything is in place except what that person has to discuss and define. Those things are clearly presented as missing, and the person is encouraged to start discussing them whenever they feel like it. **gives** *(told 2026-10-05: "The experience I'm looking for is, I'd open a repository and run setup, then everything is in place apart from things I have to discuss and define. Those things are clearly presented to me as missing, and are encouraged to start discussing them whenever I feel like it.")*
- Why: today setup handles decision records and says nothing of either philosophy, so a repository's values are kept in a run only if the person remembers, unprompted, to have a pointer recorded. **gives** *(told 2026-10-05: "I'm thinking that the repository setup procedure of the harness would need to be extended to include the new philosophy document writing or location.")*

## What setup marks as missing

- Only the two philosophy documents, the product philosophy and the engineering philosophy, are marked as missing by setup. **gives** *(told 2026-10-05, asked which things belong on the list, with standing approvals offered as a candidate: "I think only the philosophy documents would need to be marked as missing on setup.")*
- For each one that is missing, setup says what the person gains once it exists and how to start: open a Counsel session. **means** *(inferred)*

## A philosophy that already exists

- Where the repository already has a philosophy document, setup finds it, records the pointer to it, and says in its report that it did; the person objects only if it picked the wrong file. **gives** *(inferred, from "everything is in place"; put to him 2026-10-05 as a reading to confirm and listed to him again as Counsel's inference before he ratified)*
  - This changes a rule in force: the form of the value documents says a pointer line is added only on the owner's word. After this work, setup's report is where he hears of it, and his objection removes it.
  - A philosophy has no fixed path or name, so setup will sometimes list one as missing when it exists. A sentence from the person corrects it. **means** *(inferred)*
- Where the only document that fits looks as if it may belong to something else in the repository (a vendored project, an example, a test fixture), setup records nothing by itself and does not list the philosophy as simply missing: it holds the decision and brings what it found to the person for confirmation. Nothing obviously awkward passes quietly, and taking the document is one confirmation. **gives** *(told 2026-10-06. The Orchestrator asked whether setup should record such a document and report it, or record nothing and list the philosophy as missing; Counsel recommended the second. His answer: "I take neither. I think it is better if the setup procedure notices such a problem, it holds the decision and brings up the findings for confirmation. This way nothing obviously awkward quietly passes, and it is easier when you actually want to take that compared to just being reported that the philosophy is missing.")*
- At refresh, a pointer to a file that is gone or moved is flagged, as it is for decision records. **means** *(inferred)*

## After setup

- What is missing stays visible after the setup report is gone: the common rule file carries a line for each missing philosophy. **means** *(inferred; put to him 2026-10-05 as a reading to confirm and listed to him again as Counsel's inference before he ratified)*
- A Counsel session sees those lines when it opens and may offer to start on one. **means** *(inferred, same)*
- Nothing nags. Work runs as it does today while a philosophy is missing, and no run reminds the person of it. **gives** *(inferred, from "whenever I feel like it")*

## Limits

- Setup never writes, drafts, starts or offers a form to fill in for a philosophy, and infers none from the repository's code or documents. A philosophy comes only from discussion with the person entitled to state it. **constraint** *(agent-proposed; rests on the accepted record that a product philosophy is stated only by the product owner and none is inferred, ADR-D-0036)*
- A run in a repository whose philosophies are marked missing behaves exactly as a run does today in a repository without one. **constraint** *(inferred)*

## Core scenarios

All three are agent-proposed and are ratified with the brief.

1. A repository with no philosophy: after setup, the report and the common rule file each name both philosophies as missing, say what each gives and how to start; nothing else is listed as missing.
2. A repository that already has a product philosophy: after setup, the pointer to it is recorded and the report says so; only the engineering philosophy is listed as missing; a later run there is kept to that product philosophy.
3. A Counsel session opened in the repository of scenario 1 mentions what is missing and offers to start; an Orchestrator session there does not.

## Pass conditions

- Agent-checkable: the package validators pass; scenarios 1 and 2 hold on a fixture repository; no setup text drafts or templates a philosophy.
- Human-only: his first setup on a repository of his own, judged by whether what he was shown as missing was clear and whether anything pushed him.

## Left out on purpose

- Standing approvals as missing items. *(told 2026-10-05, the same words as under "What setup marks as missing")*
- Initiative briefs: they belong to a piece of work, not to the repository. *(agent-proposed)*
