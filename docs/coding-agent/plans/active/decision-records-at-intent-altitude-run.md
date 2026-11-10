# Run record: Decision records at intent altitude

- Governing brief: `docs/coding-agent/briefs/active/decision-records-at-intent-altitude-brief.md`
- Hand-over: Counsel's relay of 2026-11-02, admitted by the standing approval of 2026-10-01, quoting the owner's ratification of that day: "Nothing to add, I ratify the brief, hand it over." Not started until 2026-11-11; his word on the order of the waiting runs, relayed 2026-11-10 18:46Z by the channel clock: "Do the settings work first, then the decision records cleanup."
- Run starts from revision: a54b7a9 (the brief with his directions and answers of 2026-11-11, on top of main 8d5f390).
- Readings file: `docs/coding-agent/plans/active/decision-records-at-intent-altitude-readings.md`.
- State: the first unit (the three raised decisions) is done and reported 2026-11-11; its two proposed records await the owner's acceptance by name. The four units by area are not started.

## How the work reaches the owner

His directions of 2026-11-11, in the brief: the three raised decisions first, then batches by area of about ten. A rewrite that does not materially change what its decision is about goes in without his reading; the closeout audit confirms record by record that the decision is unchanged, and he gets the list afterwards. A split record, and a record the run cannot show to keep its decision, reach him by name.

## The census

The Researcher seat's census of 2026-11-10 (49 accepted records, at a2877d6) classed 4 as meeting the standard, 21 as rewrite, 20 as split, 1 as retire and 3 as raise. These are its classifications; each unit checks its own records again before acting on them.

Units planned, by area, each its own plan, pull request and closeout:

| Unit | Records |
| --- | --- |
| The three raised decisions | ADR-D-0016, ADR-D-0020, and the checker for ADR-I-0007 |
| Goal mode | ADR-D-0009, 0011, 0014, 0028, 0029, 0031, 0063, 0066, 0067 |
| Counsel and the value discussion | ADR-D-0034, 0035, 0036, 0037, 0043, 0044, 0045, 0046, 0047, 0059, 0060 |
| Authority, the audit and the run | ADR-D-0017, 0038, 0042, 0051, 0052, 0053, 0054, 0055, 0057, 0058, 0062, 0064, 0065 |
| Roles, routing, runtimes and rules | ADR-D-0004, 0019, 0021, 0024, 0025, 0026, 0048, 0049, 0050, 0068, 0069, 0070, ADR-I-0006, ADR-I-0007 |

## The check's result, record by record

| Record | Result |
| --- | --- |
| ADR-D-0016 | raised; answered by the owner 2026-11-11; rewritten to ADR-D-0071 (proposed, awaiting his acceptance by name) |
| ADR-D-0020 | raised; answered by the owner 2026-11-11; rewritten to ADR-D-0072 (proposed, awaiting his acceptance by name) |
| ADR-I-0007 | raised; answered by the owner 2026-11-11: the record stands and the checker is brought in line with it; the record's own check against the standard follows in its area's unit |

## Scenarios

State is one of: not yet; demonstrated (with how to observe); ready for the owner's judgement. States are the Auditor's, copied from the closing verdict: the raised plan's closeout audit of 2026-11-11.

| Scenario | State |
| --- | --- |
| 1. A record whose Decision lists the route a question travels and the moves when it fails: rewritten as one decision (who may be asked, by whom) with the route left to the plugin text; title short enough to state the decision. | not yet |
| 2. A record deciding two things that could be retired separately: split into two, each accepted by name. | not yet |
| 3. A record that is a rule with a status field (an exact string, a threshold, a dispatch template): retired; its material confirmed present in the rule or skill text, or placed there. | not yet |
| 4. A record whose decision the check finds no longer true: not rewritten; brought to the owner through Counsel. | demonstrated: read the brief's section "The three raised decisions, answered 2026-11-11" beside ADR-D-0016 and ADR-D-0020, both still accepted and unchanged, and the result table above, 2026-11-11 |

## Units

| Unit | State | What its closeout audit found |
| --- | --- | --- |
| `docs/coding-agent/plans/completed/decision-records-at-intent-altitude-raised-plan.md` | done 2026-11-11 (final review APPROVED; closeout audit holds nothing) | Scenarios: 1 (a Decision that lists a route, rewritten as one decision): not yet. 2 (a record deciding two things, split): not yet. 3 (a rule with a status field, retired, its material confirmed in the text): not yet. 4 (a decision the check finds no longer true: not rewritten, brought to the owner through Counsel): demonstrated. To observe: read the brief's section "The three raised decisions, answered 2026-11-11" beside ADR-D-0016 and ADR-D-0020 at HEAD, both still `accepted` and unchanged since a54b7a9, and the run record's result table ("raised; answered by the owner 2026-11-11"). The raising itself predates the start revision, so it is seen in the brief, not in the range. Prior state of all four: not yet (no unit of the run has closed). Getting closer: yes. The brief puts the stale or contradicted records first because his answers may change what the others say. This unit turns his three answers into two proposed records and one checker change that the tree shows, changes nothing else, and records the check's result for 3 of the 49 records. It exercises none of scenarios 1 to 3, which cover the other 46 records, and neither proposed record is accepted yet. |
