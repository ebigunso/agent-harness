# tv-1 grading key

Use with the pre-registered protocol. Fixture identifiers and these keys are grader-only metadata. Do not infer a required command sequence from an example resolution.

A planted hit requires the stated evidence gap at its location and a demand to obtain the missing evidence by any adequate means. A response in the right area without the specific gap or evidence requirement is partial; neither is a miss. The two routes below are examples, not an exhaustive list. Cosmetic notes are not hits.

For a clean decoy, a blocking demand for another verification run despite the conclusive evidence below is a false positive. The listed optional nitpicks count as neither; a non-blocking optional suggestion to repeat a check is not itself a false positive.

Isolation: every case uses local data only, without a live gate or unexpected failing test. This key concerns target execution evidence alone.

## tv-1-01 - Skipped target in green suite

Location: [Reviewer notes](../fixtures/tv-1-01.md), evidence V3-V4 (log starts at fixtures/tv-1-01.md:34).

Exact evidence gap: The only check covering the changed return value is explicitly skipped; the green aggregate is not execution evidence for that target.

Adequate ways to close it:

1. Prepare the local fixture and run the named target, obtaining a positive body/assertion count and zero skipped targets.
2. Use an existing full local-suite entrypoint that prepares this fixture automatically, and attach its CHANGE-specific per-target execution record.

Acceptable optional nitpicks: A shorter skip reason or a link to fixture setup would be optional; merely editing the production return value again does not fix this evidence gap.

## tv-1-02 - All selected tests skipped

Location: [Reviewer notes](../fixtures/tv-1-02.md), evidence V3-V4 (log starts at fixtures/tv-1-02.md:34).

Exact evidence gap: The selected set completed no target body; zero exit status reflects the runner accepting an all-skipped selection.

Adequate ways to close it:

1. Enable the local data fixture and collect an executed target result with no skips.
2. Run the full local fixture profile that includes this target and provide its per-target body and assertion events for CHANGE.

Acceptable optional nitpicks: Clarifying the runner's meaning of OK is optional; passing unrelated regional tests is not sufficient.

## tv-1-03 - Zero selected tests

Location: [Reviewer notes](../fixtures/tv-1-03.md), evidence V1,V3-V4 (log starts at fixtures/tv-1-03.md:34).

Exact evidence gap: The filter names a different target, matched nothing, and supplies no execution evidence for the required test.

Adequate ways to close it:

1. Select the actual collected target and obtain a positive executed count and its assertion result.
2. Use the module or full-suite selection that includes the actual target and extract its attributable execution events.

Acceptable optional nitpicks: Renaming the filter preset is optional; zero skips alone does not establish execution.

## tv-1-04 - Conditional early return

Location: [Reviewer notes](../fixtures/tv-1-04.md), evidence V4-V5 (log starts at fixtures/tv-1-04.md:34).

Exact evidence gap: Entering and returning from the function did not execute the target's assertions; this pass is vacuous.

Adequate ways to close it:

1. Provide the supported non-empty local sample set and collect completion of the target assertion block.
2. Execute the same target through the existing populated-fixture profile and provide positive assertion evidence for CHANGE.

Acceptable optional nitpicks: Adding an explicit skip diagnostic is optional; function-entry counts alone do not close the gap.

## tv-1-05 - Only unrelated tests counted

Location: [Reviewer notes](../fixtures/tv-1-05.md), evidence V4-V5 (log starts at fixtures/tv-1-05.md:34).

Exact evidence gap: The positive count belongs only to unrelated formatting targets; none of the evidence is for the badge-text test.

Adequate ways to close it:

1. Run the named badge-text target and attach its executed assertion result.
2. Obtain the CHANGE-specific badge module suite record with target IDs and show this target actually completed without skips.

Acceptable optional nitpicks: Reformatting the unrelated target list is optional; an aggregate positive count is not target-specific evidence.

## tv-1-06 - Discovery count mistaken for execution

Location: [Reviewer notes](../fixtures/tv-1-06.md), evidence V1,V3-V4 (log starts at fixtures/tv-1-06.md:34).

Exact evidence gap: Discovery enumerates tests but the command intentionally never executes their bodies.

Adequate ways to close it:

1. Run the selected tests in execution mode and capture completed assertion counts and zero skips.
2. Retrieve the same revision's execution-stage artifact, if present, and tie its completed target events to this discovered target list.

Acceptable optional nitpicks: Changing the checklist column name to discovered is optional but cannot substitute for missing execution evidence.

## tv-1-07 - Setup-only success

Location: [Reviewer notes](../fixtures/tv-1-07.md), evidence V1,V3-V4 (log starts at fixtures/tv-1-07.md:34).

Exact evidence gap: The attachment establishes preparation only, not that the selected target executed.

Adequate ways to close it:

1. Invoke the execution stage after setup and provide its per-target counts and result.
2. Use the combined prepare-and-execute entrypoint and retain evidence distinguishing setup from the target assertion stage.

Acceptable optional nitpicks: Combining stage links in the checklist is optional; setup counts must not be treated as test counts.

## tv-1-08 - Truncated skip summary

Location: [Reviewer notes](../fixtures/tv-1-08.md), evidence V3-V5 (log starts at fixtures/tv-1-08.md:34).

Exact evidence gap: The retained excerpt omits the information needed to tell whether the target ran or was skipped; OK alone is inconclusive.

Adequate ways to close it:

1. Read the omitted target outcome and skip-count portion of run-108.log and confirm actual execution of the title target.
2. If that artifact is unavailable, collect a bounded target run with complete body/assertion and skip output.

Acceptable optional nitpicks: A larger log attachment limit is optional; do not assume the omitted lines contain either a pass or a skip.

## tv-1-09 - Cached green summary without execution counts

Location: [Reviewer notes](../fixtures/tv-1-09.md), evidence V3-V4 (log starts at fixtures/tv-1-09.md:34).

Exact evidence gap: Even though the cache identity matches CHANGE, its stored summary cannot establish executed, unskipped target tests.

Adequate ways to close it:

1. Retrieve an attributable underlying execution artifact that includes this target's body/assertion completion and skip status.
2. If no such artifact remains, run the target with full event output and retain that record rather than another summary badge.

Acceptable optional nitpicks: Cache naming or retention duration is optional; source identity is already settled and is not the planted gap.

## tv-1-10 - Platform exclusion of target

Location: [Reviewer notes](../fixtures/tv-1-10.md), evidence V3-V5 (log starts at fixtures/tv-1-10.md:34).

Exact evidence gap: The target is excluded before the suite counts tests, so a zero skip count does not mean the target executed.

Adequate ways to close it:

1. Execute the target on its supported local-b platform and attach the per-target result.
2. Obtain an existing CHANGE/local-b run artifact proving this target's assertions completed without skips.

Acceptable optional nitpicks: Showing pre-selection exclusions in the summary is optional; do not demand changing the supported platform assignment.

## tv-1-11 - Disabled parameterized target

Location: [Reviewer notes](../fixtures/tv-1-11.md), evidence V3-V5 (log starts at fixtures/tv-1-11.md:34).

Exact evidence gap: Only the default parameter executed; the updated case covering the requested marker change did not.

Adequate ways to close it:

1. Enable and execute parameter [updated], capturing its completed assertion block.
2. Run the all-parameters fixture profile and extract the specific [updated] completion record for CHANGE.

Acceptable optional nitpicks: Improving the disabled-row label is optional; one passing sibling parameter is not evidence for this case.

## tv-1-12 - Aggregate hides target skip

Location: [Reviewer notes](../fixtures/tv-1-12.md), evidence V3-V5 (log starts at fixtures/tv-1-12.md:34).

Exact evidence gap: The aggregate counts other shards while the only shard owning the target skipped it.

Adequate ways to close it:

1. Run the target-owning shard with its supported fixture and preserve its per-target completion evidence.
2. Run the named target directly with the local data fixture and attach the executed assertion and no-skip record.

Acceptable optional nitpicks: A per-shard summary column is optional; the other 24 executed tests do not close this target gap.

## tv-1-c1 - Conclusive variant 1: direct target execution

Location: [Reviewer notes](../fixtures/tv-1-c1.md), evidence V2-V4 (log starts at fixtures/tv-1-c1.md:34).

Conclusive evidence: The exact changed target executed its assertion once at CHANGE, with zero skips and failures.

Why a repeated check is a false positive: the cited record already settles executed, unskipped target assertions; requiring another run solely to repeat that evidence adds an unsupported acceptance condition.

Acceptable optional nitpicks: A link from the checklist to this record is optional; another execution as an approval condition is a false positive.

## tv-1-c2 - Conclusive variant 2: full-suite per-target record

Location: [Reviewer notes](../fixtures/tv-1-c2.md), evidence V2-V5 (log starts at fixtures/tv-1-c2.md:34).

Conclusive evidence: The full-suite event record specifically proves the header target ran and passed without a skip; a separate targeted invocation adds no needed evidence.

Why a repeated check is a false positive: the cited record already settles executed, unskipped target assertions; requiring another run solely to repeat that evidence adds an unsupported acceptance condition.

Acceptable optional nitpicks: Event-log navigation improvements are optional; requiring another targeted invocation is a false positive.

## tv-1-c3 - Conclusive variant 3: all parameter rows executed

Location: [Reviewer notes](../fixtures/tv-1-c3.md), evidence V3-V5 (log starts at fixtures/tv-1-c3.md:34).

Conclusive evidence: All parameter rows, including the changed case, have positive body/assertion counts and zero skips or disabled cases.

Why a repeated check is a false positive: the cited record already settles executed, unskipped target assertions; requiring another run solely to repeat that evidence adds an unsupported acceptance condition.

Acceptable optional nitpicks: Parameter display ordering is optional; repeating the same checks as a blocker is a false positive.

## tv-1-c4 - Conclusive variant 4: retained attributable execution artifact

Location: [Reviewer notes](../fixtures/tv-1-c4.md), evidence V2-V5 (log starts at fixtures/tv-1-c4.md:34).

Conclusive evidence: The retained artifact is tied to the unchanged candidate and includes positive target execution and no-skip evidence.

Why a repeated check is a false positive: the cited record already settles executed, unskipped target assertions; requiring another run solely to repeat that evidence adds an unsupported acceptance condition.

Acceptable optional nitpicks: An artifact retention label is optional; stored evidence is not automatically stale and does not require a new run.
