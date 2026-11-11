# Decision records at intent altitude: discussion notes

Counsel's notes for the discussion opened 2026-11-02, beside the brief of the same stem.

## What the owner saw, 2026-11-02

> The ADRs are saying the right things, but I'm starting to feel that the recent suite of ADRs, not limited to the ones proposed, are slightly too much into the details to be a good decision that is expected to hold through subsequent changes. I'm not sure if it's just my problem of comprehension, or if there's a real problem here.

Counsel's read, mine, given the same day and not contested: a real problem. The proposed records (ADR-D-0062 to 0065) restate the plugin's procedure, with titles of some sixty words, Decision lists of up to nine bullets, and cross-references to eight records; ADR-D-0040 and 0041 (2026-09-30), 0056 (2026-10-05) and 0061 (2026-10-22) were superseded within weeks with no decision reversing; the folder held 50 active and 23 retired records after two months. The standard (`durable-docs-authoring/references/adr.md`) already asks for intent altitude and one decision per record. One cause, mine: the Worker drafts from the brief's gives, which are themselves written as mechanism (Counsel's own writing), and the audit grades the record against the brief, so a record mirroring the brief passes; nothing asks whether it survives the next route change.

His direction on the proposed records: "Hold and rewrite before acceptance." Written into both running briefs. On the rest: "checks and rewrites of older ADRs to meet those same standards should happen as a parallel task." This brief.

## Ratification

Framings shown 2026-11-02: the reader after a later change; outcome untouched; a record that is really a rule retired; records of the two runs left alone; the standard itself not changed; acceptance by name. Asked whether there is anything the work must not do or must ask before doing: "Nothing to add, I ratify the brief, hand it over."

## Questions from the run

- 2026-11-11, before the run was planned: how 60 to 70 records for acceptance reach him; the three raised decisions (ADR-D-0016, ADR-D-0020, ADR-I-0007); whether an unread rewrite still waits for his naming it. His answers are in the brief with his words.
- 2026-11-11, with the first unit: whether four further places where the checker fails on prose are brought in line with ADR-I-0007; whether a repository-internal change made with its consumers unverified is reported in every kind of run. Brought to him with Counsel's advice.

## Counsel's read of the first unit, 2026-11-11

One read, of the two proposed records; the Orchestrator's report of 2026-11-10 22:16Z arrived with the outcomes in it (review approved at plan, wave and final after fixes; the value audits at plan draft and closeout held nothing). Pull request 96, nothing merged, nothing retired.

- ADR-D-0071 says what he decided on ADR-D-0016: protection needs a consumer that can be shown, and where one cannot be verified he is asked only about a surface that crosses the repository's boundary. Its Why is two sentences and cites no brief.
- Marked, mine: its title joins two clauses, and his own answer of 2026-11-11 changed the second (who is asked) while the first (the evidence requirement) held. By the test he applied to the record he read as ADR-D-0067, that reads as two decisions. The run read one. His to judge.
- The reopen condition on the rejected "ask in every case" was derived by the run and sets when that question returns to him; the audit marks it as direction. Counsel's framing: it returns when changes made on the evidence of no consumer found are seen to break something inside a repository, or it never returns. Brought to him.
- ADR-D-0072 says a loader-routed session holds the Orchestrator role and that the policy being in context confers nothing, leaving the other ways in to ADR-D-0037. One decision with its boundary. Nothing marked.
- The checker now warns where it failed on the Reviewer's prompt snippet; ADR-I-0007 is unchanged.

## Counsel's read of the goal-mode area's second unit, 2026-11-11

Not a full read. The Orchestrator's report of 2026-11-11 09:58Z arrived with the outcomes in it (the Codex review seat approved the plan, the wave and a final delta after findings in each; audits at plan draft and closeout held nothing). Pull request 98, stacked on 97; nothing accepted, retired or merged.

- What Counsel did: a mechanical check of the twelve proposed records (ADR-D-0076 to ADR-D-0087), and a reading of the Decision of ADR-D-0077 and of ADR-D-0087 and the Why of ADR-D-0082. It did not read the other nine in full, and said so to him.
- The check: every Why is one or two sentences; none cites a brief as its authority (ADR-D-0082's Why names the brief as what a goal run may drift from, which is its subject); none has an Invariant prompt; each `consulted` field names the old record's entries and Claude Fable 5.2.
- ADR-D-0087 carries the line taken out of ADR-D-0076, the named invariants, and that what a run learns against its goal is surfaced. ADR-D-0077 has the reading of the gap settled before the loop starts. Both as he decided.
- Brought to him: the audit's matter of direction on a Revisit When premise that the run words from an old record's reason, for rewrites he does not read; and the Orchestrator's report that it built an extended plan without a fresh plan review and plan-draft audit.

## Counsel's read of the goal-mode area's first unit, 2026-11-11

One read, of the proposed ADR-D-0076; the Orchestrator's report of 2026-11-11 08:09Z arrived with the outcomes in it (plan review passed after eight findings; the wave's review, by a Claude reviewer after the two Codex seats left the roster, passed after seven; audits at plan draft and both closeouts held nothing). Pull request 97, nothing merged.

- Three rewrites went in unread on the route he chose, the closeout audit confirming each keeps its decision: ADR-D-0073 for ADR-D-0009, ADR-D-0074 for ADR-D-0028, ADR-D-0075 for ADR-D-0031. Counsel did not read them; that is the route.
- ADR-D-0076 (for ADR-D-0014) carries what he settled on its two rejected alternatives, in the new template's form. Its Why is two sentences and cites no brief.
- Marked, mine: its Decision has three lines. The second (a failed examination stops the loop and goes to the goal's owner) is the first's own failing case and could not stand with the first retired. The third (the loop never changes its goal; a change of goal is the owner's) would still bind with the examination gone, and it sits beside ADR-D-0011's protection of the goal condition, which the next unit splits. By that test the record holds two decisions, and the third line belongs with the goal's protection. The run read one. His to judge; the test, if he takes it, is the line for the twenty records the census classed as holding more than one decision.
- The Orchestrator's ruling that a clause of an old record's Decision which a rewrite does not carry must be held by a named accepted record: Counsel's view, its own, is that this is right; every constraint he once decided stays where he can point at it. Brought to him.
- Found and not built: a repository that already has its own copy of the record template keeps the old prompts. Brought to him.

## Counsel's read after his widening and split of ADR-D-0071, 2026-11-11

He said of the proposed ADR-D-0071: "71 should be widened, so that questions are raised only when any accessible information source does not settle the question, not at the moment it crosses repository boundaries." and, asked whether it stays one record: "Probably it should be split too." One read, of ADR-D-0073; the Orchestrator's report of 2026-11-11 05:57Z arrived with the outcomes in it (review approved after two findings in ADR-D-0073 were fixed; the closeout audit held nothing).

- ADR-D-0071 is reduced to the evidence requirement. ADR-D-0073 is new and carries when he is asked: only where no accessible source settles whether a consumer exists; where sources settle that there is none the change goes ahead and is reported; where the surface sits never decides. It says what he said. Its Why is two sentences and cites no brief. The run, the review and the audit each found the two records stand apart.
- The audit marks as direction the run's wording of "accessible" (the run can read it with the access it has) and "settles" (it shows a consumer, or gives real evidence that there is none, which a search does only where the sources searched would show one). Counsel's framing test, mine: a run that reads a registry's dependents and finds none goes ahead and reports, or asks him first; the two read differently, so it goes to him.
- Its second Decision line carries his "goes ahead and says what it did", which he said of a change inside the repository, to any surface the sources settle. That follows from his widening; pointed out to him.
- The two reopen conditions and the Revisit When are derived by the run; pointed out to him.
