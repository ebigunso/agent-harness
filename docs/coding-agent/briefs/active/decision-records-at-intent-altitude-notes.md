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
