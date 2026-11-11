# Run record: Decision records at intent altitude

- Governing brief: `docs/coding-agent/briefs/active/decision-records-at-intent-altitude-brief.md`
- Hand-over: Counsel's relay of 2026-11-02, admitted by the standing approval of 2026-10-01, quoting the owner's ratification of that day: "Nothing to add, I ratify the brief, hand it over." Not started until 2026-11-11; his word on the order of the waiting runs, relayed 2026-11-10 18:46Z by the channel clock: "Do the settings work first, then the decision records cleanup."
- Run starts from revision: a54b7a9 (the brief with his directions and answers of 2026-11-11, on top of main 8d5f390).
- Readings file: `docs/coding-agent/plans/active/decision-records-at-intent-altitude-readings.md`.
- State: the first unit (the three raised decisions) is merged (pull request 96, 2026-11-11). The goal-mode area is two units. Its first is built and reported 2026-11-11: ADR-D-0073, 0074 and 0075 went in on the closeout audit's confirmation that each keeps its old record's decision, and ADR-D-0009, 0028 and 0031 are retired; ADR-D-0067 meets the standard; ADR-D-0076, proposed for one of ADR-D-0014's two decisions, awaits his acceptance by name; the record template changed on his word, and a refresh now brings a repository's placed copy of it up to date. The second goal-mode unit (the four bundles) and the three other areas are not started.

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
| ADR-D-0016 | raised; answered by the owner 2026-11-11 and amended by him the same day; rewritten to ADR-D-0071 and ADR-D-0072, both accepted by name 2026-11-11; retired |
| ADR-D-0020 | raised; answered by the owner 2026-11-11; its proposed rewrite was taken out of this run on his word the same day: a decision of another initiative will replace the record, which stands accepted and unchanged until then, its overtaken sentence included. That rewrite was numbered ADR-D-0072 while it was proposed; the number now belongs to the record split from ADR-D-0071. |
| ADR-I-0007 | raised; answered by the owner 2026-11-11: the record stands and the checker is brought in line with it; the record's own check against the standard follows in its area's unit |
| ADR-D-0009 | rewritten at the same decision to ADR-D-0073 (work that passes a test of its shape, and only that, may run under a governed goal lifecycle), accepted 2026-11-11 on the closeout audit's confirmation that the decision is unchanged; retired |
| ADR-D-0014 | holds two decisions by the owner's test of 2026-11-11. The assessor's examination and what follows its failure: rewritten to ADR-D-0076 (an independent assessor asks whether a goal is still worth pursuing), proposed, awaiting his acceptance by name. That the loop never changes its goal, a change of goal being the owner's: waits for the record on the protection of the goal condition, which the area's second unit splits from ADR-D-0011. ADR-D-0014 is retired when both are accepted. |
| ADR-D-0028 | rewritten at the same decision to ADR-D-0074 (a goal loop is stopped by its failure to progress; a resource ceiling is only a backstop), accepted 2026-11-11 on the closeout audit's confirmation; retired |
| ADR-D-0031 | rewritten at the same decision to ADR-D-0075 (a goal branch merges only on a human's authorization given on a verified completion report), accepted 2026-11-11 on the closeout audit's confirmation, read together with ADR-D-0050; retired |
| ADR-D-0067 | meets the standard (the Worker's check, agreed by the review, against the census's "rewrite"); nothing written |

## Scenarios

State is one of: not yet; demonstrated (with how to observe); ready for the owner's judgement. In this record ADR-D-0072 names the record split from ADR-D-0071 (numbered ADR-D-0073 until 2026-11-11, and so called in the changes and readings files before that date). States are the Auditor's, copied from the closing verdict of the unit that last moved each: scenario 2 from the goal-mode plan's closeout audit, the others from the raised plan's, both of 2026-11-11.

| Scenario | State |
| --- | --- |
| 1. A record whose Decision lists the route a question travels and the moves when it fails: rewritten as one decision (who may be asked, by whom) with the route left to the plugin text; title short enough to state the decision. | not yet |
| 2. A record deciding two things that could be retired separately: split into two, each accepted by name. | demonstrated, for one instance only (the run's own proposed record, split on his word; no accepted record holding two decisions has been split yet): read ADR-D-0071 and ADR-D-0072, both accepted, with ADR-D-0016 under `superseded/`, beside the brief's "I accept ADR-D-0071 and ADR-D-0072, and pull request 96.", 2026-11-11 |
| 3. A record that is a rule with a status field (an exact string, a threshold, a dispatch template): retired; its material confirmed present in the rule or skill text, or placed there. | not yet |
| 4. A record whose decision the check finds no longer true: not rewritten; brought to the owner through Counsel. | demonstrated: read the brief's section "The three raised decisions, answered 2026-11-11" beside ADR-D-0020, still accepted and unchanged, and the result table above, 2026-11-11 |

## Units

| Unit | State | What its closeout audit found |
| --- | --- | --- |
| `docs/coding-agent/plans/completed/decision-records-at-intent-altitude-raised-plan.md` | done 2026-11-11 (final review APPROVED; closeout audit holds nothing) | Scenarios: 1 (a Decision that lists a route, rewritten as one decision): not yet. 2 (a record deciding two things, split): not yet. 3 (a rule with a status field, retired, its material confirmed in the text): not yet. 4 (a decision the check finds no longer true: not rewritten, brought to the owner through Counsel): demonstrated. To observe: read the brief's section "The three raised decisions, answered 2026-11-11" beside ADR-D-0016 and ADR-D-0020 at HEAD, both still `accepted` and unchanged since a54b7a9, and the run record's result table ("raised; answered by the owner 2026-11-11"). The raising itself predates the start revision, so it is seen in the brief, not in the range. Prior state of all four: not yet (no unit of the run has closed). Getting closer: yes. The brief puts the stale or contradicted records first because his answers may change what the others say. This unit turns his three answers into two proposed records and one checker change that the tree shows, changes nothing else, and records the check's result for 3 of the 49 records. It exercises none of scenarios 1 to 3, which cover the other 46 records, and neither proposed record is accepted yet. |
| Small change, in `docs/coding-agent/plans/active/decision-records-at-intent-altitude-changes.md`: the checker's four other places, and reporting an internal change in every kind of run | done 2026-11-11 (review APPROVED; closeout audit holds nothing) | Scenarios: 1 to 3 not yet, 4 demonstrated; no state moved. Getting closer: yes. One judgement call marked direction: the checks kept failing require or forbid a token inside documents only people and models read. |
| Small change, in the same file: ADR-D-0071 widened and split | done 2026-11-11 (review APPROVED after two findings fixed; closeout audit holds nothing) | Scenarios: 2 moved to ready for the owner's judgement, for one instance; 1 and 3 not yet; 4 demonstrated. Getting closer: yes. One judgement call marked direction: what makes a source accessible and what settles the question. |
| `docs/coding-agent/plans/completed/decision-records-at-intent-altitude-goal-mode-plan.md` | done 2026-11-11 (review APPROVED after five findings fixed; closeout audit holds nothing and confirms each of the three decisions unchanged) | Scenarios: 1 not yet; 2 demonstrated for one instance, outside this unit; 3 not yet; 4 demonstrated. Getting closer: yes; the check now covers 8 of 49 records. One ruling marked direction: a Decision clause a rewrite does not carry must be held by a named active record. |
| Small changes, in `docs/coding-agent/plans/active/decision-records-at-intent-altitude-changes.md`: the three goal-mode rewrites accepted and their old records retired; the template's two prompts; ADR-D-0014 rewritten | done 2026-11-11 (review APPROVED, two wordings fixed; closeout audit holds nothing and confirms the three decisions again) | Scenarios: no state moved. Getting closer: yes; for three matters the folder holds one accepted record at intent altitude with the old one retired. One judgement call marked direction: ADR-D-0014 read as one decision under a two-clause title. |
| Small changes, in the same file: ADR-D-0076 narrowed to the examination; setup's refresh updates a repository's copy of the template | done 2026-11-11 (review APPROVED after one finding fixed; closeout audit holds nothing) | Scenarios: no state moved; a second instance of scenario 2 is half built (ADR-D-0076 holds one of ADR-D-0014's two decisions). Getting closer: yes. Two judgement calls marked direction: ADR-D-0014 staying in force past ADR-D-0076's acceptance; an edited template copy left until its user says otherwise. |
