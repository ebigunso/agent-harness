# Brief: Decision records at intent altitude

- status: ratified by ebigunso on 2026-11-02 ("Nothing to add, I ratify the brief, hand it over."). Asked before ratifying whether there is anything the work must not do or must ask before doing, he added nothing.
- handed to: agent-harness-orchestrator on 2026-11-02
- drafted by: agent-harness-counsel, from discussion with ebigunso on 2026-11-02
- product basis: the product owner's own words in this brief. ebigunso owns the harness; no product philosophy and no engineering philosophy exist for this repository.
- provenance tags: *(told)* = ebigunso said it; *(inferred)* = Counsel read it from his words; *(agent-proposed)* = Counsel originated it and he accepted it. His quoted words with the date stand beside each.
- kind marks: **gives** (what the work must give him; it binds), **constraint** (fixed regardless), **means** (a way to get what a gives-statement asks for; the run builds from it and may better it).

This brief is the grounds for the work. It is passed verbatim; do not paraphrase it into a plan as if the paraphrase were the requirement. It states what and why. How is the Orchestrator's, except where a means is stated, and a means does not bind.

## Who it is for and why

- Someone who opens the decisions folder after the plugin has changed again finds, for each matter, one short record whose decision is still true, and can say what it decides from its title. Today the recent records restate the plugin's procedure, so a route change replaces them, and the reader gets the route of a given month. **gives** *(told 2026-11-02: "The ADRs are saying the right things, but I'm starting to feel that the recent suite of ADRs, not limited to the ones proposed, are slightly too much into the details to be a good decision that is expected to hold through subsequent changes.")*
- What Counsel found and he did not contest: ADR-D-0040 and 0041 (2026-09-30), 0056 (2026-10-05) and 0061 (2026-10-22) are superseded within weeks without any decision reversing; the folder holds 50 active and 23 retired records after two months; the standard (`durable-docs-authoring`, `references/adr.md`) already asks for intent altitude and one decision per record, and the records do not meet it. *(Counsel's read, 2026-11-02, mine)*

## What the work gives

- Every accepted record in `docs/coding-agent-orchestration-harness/decisions/` is checked against the standard the plugin already carries: one decision per record; the constraint stated so that any rewording of the plugin text that preserves it stays valid; the why in prose at intent altitude; exact mechanics (routes, moves, file names, admission of a relay, template fill-ins) not covered. **gives** *(told 2026-11-02: "checks and rewrites of older ADRs to meet those same standards should happen as a parallel task.")*
- The check also asks whether a record's wording names the thing it means rather than its position, order or relation to something else ("the second source"), so that the statement holds when that other thing changes. **gives** *(told 2026-11-07, reading a rewritten record of another run: "where it says 'the second source', I think should be reworded to point at what exactly it is, so that the statement holds even if it becomes the first or third or the likes. This is something to be wary of when writing documents in general. Choose wording that would be less likely to change meaning when something else changes.")*
- A record that fails the check is rewritten to meet it, under the standard's own lifecycle: a new complete record, the old one retired, accepted by name. A record found to be a bundle is split; a record found to carry only operational material is retired and its material placed in the rule or skill text that already states it, or added there. **gives** *(inferred 2026-11-02 from the above and the standard's lifecycle)*
- The decisions themselves do not change. The work moves altitude, not outcome; where a check finds a decision itself wrong, stale or contradicted, that is a value question for the owner through Counsel, not a rewrite. **constraint** *(inferred 2026-11-02; he asked for records that hold through changes, not for different decisions)*
- Records a run in progress proposes or supersedes are left to that run: on 2026-11-02 ADR-D-0040, 0041, 0056, 0061 to 0066. **constraint** *(agent-proposed 2026-11-02, so that two runs do not rewrite the same record)*
- Where the check finds that the standard's own form invites the detail (a section that asks for enumeration, a template that mirrors procedure), that is reported to the owner through Counsel as a value question; the standard is not changed by this work without his word. **constraint** *(agent-proposed 2026-11-02)*

## Directed before the run was planned, 2026-11-11

Each entry is an amendment with its own ratification record. The Orchestrator reported the census of the 49 accepted records (4 meeting the standard, 21 needing a rewrite at the same decision, 20 holding more than one decision, 1 operational only, 3 whose decision looks stale or contradicted; its Researcher's classifications, not yet checked) and asked how 60 to 70 records for acceptance should reach him. His answer, quoted whole: "Go with your takes on all three. Rewrites can go in without me reading it, as long as it doesn't materially change what the decision is about."

- The records whose decision the check finds stale or contradicted reach him first, as value questions through Counsel, before the rest is rewritten, since his answers may change what the other records say. **gives** *(agent-proposed; Counsel's advice of 2026-11-11; accepted in the first sentence above)*
- The rest reaches him in batches by area, each batch its own pull request and its own acceptance, of about ten records. **gives** *(agent-proposed; Counsel's advice of 2026-11-11; accepted in the first sentence above)*
- A rewrite that does not materially change what its decision is about goes in without his reading it. **gives** *(told 2026-11-11: the second sentence above)* A record split in two or more, and a record the run cannot show to keep its decision, still reach him by name. *(inferred)* Such a rewrite does not wait for a statement of his naming it: it goes in once the closeout audit has confirmed, record by record, that its decision is unchanged, and he is given the list afterwards. This departs, for this run only, from the record standard's rule that every record is accepted by a statement naming it; the standard itself is not changed. **gives** *(agent-proposed; put to him 2026-11-11 as two experiences, each batch waiting for one sentence of his listing its records unread, or the records merging on the audit's confirmation with the list given to him afterwards; Counsel's advice was the second; accepted 2026-11-11: "Go with the second.")*
- The two runs whose records the constraint above left alone closed on 2026-11-11, so it now leaves no record out; and this work no longer runs beside them. *(inferred)*

## The three raised decisions, answered 2026-11-11

The Orchestrator brought the three records whose decision the check found at odds with the plugin's own text or checker, each as two experiences. Counsel put them to him with its own advice on each. His answer, quoted whole: "Go with your takes on all three."

- ADR-D-0016 (protection requires demonstrable consumers): his decision is what the plugin's text says. Where nobody can show who uses something, a run asks him only when the thing is visible outside the repository; inside the repository it goes ahead and says what it did. The record is behind the text and is rewritten to say this. **gives** *(agent-proposed; Counsel's advice, on the ground that only direction-level questions reach him; accepted 2026-11-11 in the words above)*
- Amended the same day, on reading the proposed ADR-D-0071: what decides whether he is asked is whether the information within reach settles the question, not whether the surface crosses the repository's boundary. He is asked only where no accessible source of information settles whether a consumer exists. **gives** *(told 2026-11-11: "71 should be widened, so that questions are raised only when any accessible information source does not settle the question, not at the moment it crosses repository boundaries.")* This replaces the boundary test in the entry above, in the record and in the plugin's text that states it. *(inferred)* Which sources count as accessible, and what it takes for them to settle the question, are the run's to word. *(inferred)*
- The proposed ADR-D-0071 is split in two records: that protection needs a consumer that can be shown, and when he is asked where a consumer cannot be verified. **gives** *(told 2026-11-11, after Counsel's read that the record's title joins two clauses and that his own answers had changed the second while the first held, and asked whether it stays one record or is split: "Probably it should be split too.")* He said "probably"; Counsel reads it as his direction, and the run splits unless the split shows the two cannot stand apart, in which case that returns to him. *(inferred)*
- ADR-D-0020 (loader-routed sessions assume the Orchestrator role): the record was overtaken by ADR-D-0037 and the plugin's text. A session becomes the Orchestrator only by the deliberate routes they name, not because the skill was loaded on a description match. The old sentence is corrected in the rewrite. **gives** *(agent-proposed; Counsel's advice; accepted 2026-11-11 in the words above)*
- ADR-I-0007 (validators never fail on exact prose): the record stands and the checker is brought in line with it. The check that requires exact phrases in the Reviewer's prompt snippet warns at most, and whether the snippet covers those risks is a reviewer's judgement. **gives** *(agent-proposed; Counsel's advice, on the ground that blocking an equivalent rewording is what the record forbids; accepted 2026-11-11 in the words above)* This changes a checker, which is plugin work this brief did not foresee; it is in the run by his word above. *(inferred)*
- The records rewritten for ADR-D-0016 and ADR-D-0020 state a decision other than the old record's wording, so they reach him by name and are not among the rewrites that go in unread. *(inferred)*

## Directed during the run

His answer of 2026-11-11 to two questions the Orchestrator raised with the first unit, each put to him as two experiences with Counsel's advice, quoted whole: "I'll take your advice on both questions."

- Every place where the package checker fails on wording that only people and models read is brought in line with ADR-I-0007: it warns, and a reviewer judges. The checker keeps failing only where a program reads the exact string, which is a contract in that record's own sense. **gives** *(agent-proposed; the Orchestrator's question on four further places, a required phrase in the two Orchestrator adapters, two forbidden phrases in the improvement-loop skill, a required phrase in its promotion guidelines and a forbidden heading in the rule-suite templates; Counsel's advice as stated here; accepted 2026-11-11 in the words above)* Which of the four a program reads is the run's to establish. *(inferred)*
- The plugin's text says that a change inside the repository made with its consumers unverified is reported in every kind of run, a goal-mode run and a small change without a plan included. **gives** *(agent-proposed; the Orchestrator's question after his answer on ADR-D-0016, since only a plan's compatibility stance says it today; Counsel's advice was yes, in this run, on the ground that being told is what makes going ahead without asking safe; accepted 2026-11-11 in the words above)*

## Limits

- The work runs beside the two runs in progress, as he asked, and lands by its own acceptance. **constraint** *(told 2026-11-02: "as a parallel task")*
- Acceptance is by name, as the standard says; one statement may accept several records when it names each. **constraint** *(the standard, Acceptance)*

## Core scenarios

Agent-proposed; ratified with the brief.

1. A record whose Decision lists the route a question travels and the moves when it fails: rewritten as one decision (who may be asked, by whom) with the route left to the plugin text; title short enough to state the decision.
2. A record deciding two things that could be retired separately: split into two, each accepted by name.
3. A record that is a rule with a status field (an exact string, a threshold, a dispatch template): retired; its material confirmed present in the rule or skill text, or placed there.
4. A record whose decision the check finds no longer true: not rewritten; brought to the owner through Counsel.

## Pass conditions

- For each active record, a reader can state what it decides in one sentence from its title, and no Decision section mirrors a passage of the plugin's procedure. *(agent-proposed)*
- The check's result for every record is recorded: meets, rewritten (to which), split (into which), retired (material where), or raised. *(agent-proposed)*

## Left out on purpose

- Changing any decision's outcome. Changing the record standard itself. Records belonging to runs in progress.
