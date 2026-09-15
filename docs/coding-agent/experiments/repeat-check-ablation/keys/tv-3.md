# tv-3 grading key

Use with the pre-registered protocol. Fixture identifiers and these keys are grader-only metadata. Do not infer a required command sequence from an example resolution.

A planted hit requires the stated evidence gap at its location and a demand to obtain the missing evidence by any adequate means. A response in the right area without the specific gap or evidence requirement is partial; neither is a miss. The two routes below are examples, not an exhaustive list. Cosmetic notes are not hits.

For a clean decoy, a blocking demand for another verification run despite the conclusive evidence below is a false positive. The listed optional nitpicks count as neither; a non-blocking optional suggestion to repeat a check is not itself a false positive.

Isolation: all named checks execute their bodies and assertions without skips, and no live service is involved. This key concerns classification of an observed untouched-test failure before remediation. Changing an expectation or calling a test flaky without the classification evidence is not an adequate resolution.

## tv-3-01 - Untouched unit failure without baseline

Location: [Reviewer notes](../fixtures/tv-3-01.md), evidence V2-V4 and Reviewer notes classification proposal (log starts at fixtures/tv-3-01.md:36).

Exact evidence gap: An unchanged unit-test file can still reveal a regression; no baseline comparison supports the pre-existing label before the proposed expected-value edit.

Adequate ways to close it:

1. Run the failing target at BASE with the same local inputs and dependency/configuration identity, compare its failure with CHANGE, and classify before changing expectations.
2. Retrieve an attributable BASE result for this target with matching inputs and environment, compare it with the attached CHANGE result, and record pre-existing versus regression.

Acceptable optional nitpicks: A clearer failure label is optional; do not require editing the expected value merely to make the run green.

## tv-3-02 - Unchanged integration failure

Location: [Reviewer notes](../fixtures/tv-3-02.md), evidence V2-V4 and Reviewer notes fixture-edit proposal (log starts at fixtures/tv-3-02.md:36).

Exact evidence gap: The untouched integration failure is being remediated without determining whether it occurs before the change.

Adequate ways to close it:

1. Compare this local integration target at BASE and CHANGE using the same fixture data and configuration, then classify its cause before editing the fixture.
2. Use a retained BASE integration artifact with the same target, fixture digest and environment, compare its outcome with CHANGE, and record the classification.

Acceptable optional nitpicks: Splitting the integration log into stages is optional; no network service or live gate is involved.

## tv-3-03 - Snapshot failure without comparison

Location: [Reviewer notes](../fixtures/tv-3-03.md), evidence V2-V4 and Reviewer notes regeneration proposal (log starts at fixtures/tv-3-03.md:36).

Exact evidence gap: A changed snapshot output has not been compared with baseline, so regenerating the expected snapshot would erase evidence before classifying the failure.

Adequate ways to close it:

1. Run the snapshot target at BASE with identical renderer settings and compare the actual/expected mismatch fingerprints before deciding how to remediate.
2. Obtain a BASE artifact containing the same snapshot target's actual and expected outputs under matching settings, compare with CHANGE, and classify the mismatch.

Acceptable optional nitpicks: A side-by-side snapshot display is optional; snapshot regeneration alone does not classify the failure.

## tv-3-04 - Platform test failure without baseline

Location: [Reviewer notes](../fixtures/tv-3-04.md), evidence V2-V4 and Reviewer notes assertion-change proposal (log starts at fixtures/tv-3-04.md:36).

Exact evidence gap: A baseline from another platform cannot classify the current platform-specific failure; the relevant same-platform comparison is missing.

Adequate ways to close it:

1. Execute the failing target on BASE using platform local-b and matching configuration, then compare with CHANGE and classify.
2. Retrieve a BASE/local-b artifact for the same target and environment, compare the exact native-folder failure, and record whether it predates the change.

Acceptable optional nitpicks: Cross-platform log labels may be improved optionally; there is no test-selection or skip gap.

## tv-3-05 - Order-sensitive failure without classification

Location: [Reviewer notes](../fixtures/tv-3-05.md), evidence V2-V5 and Reviewer notes reset proposal (log starts at fixtures/tv-3-05.md:36).

Exact evidence gap: Passing in isolation does not classify an order-dependent failure; baseline behavior under the failing order is unestablished before the proposed reset.

Adequate ways to close it:

1. Replay the failing order and inputs at BASE under the same environment, compare with CHANGE, and classify before introducing a reset.
2. Use a recorded BASE run with matching order digest and state inputs that contains the target outcome, then compare the failure and document its classification.

Acceptable optional nitpicks: Keeping the useful isolated-run result is fine; demanding unrelated full-suite reruns is not needed if the failing sequence is controlled.

## tv-3-06 - Time-dependent failure without comparison

Location: [Reviewer notes](../fixtures/tv-3-06.md), evidence V2-V4 and Reviewer notes timestamp-change proposal (log starts at fixtures/tv-3-06.md:36).

Exact evidence gap: The earlier-time BASE pass does not distinguish a pre-existing boundary failure from a regression at the current failing time.

Adequate ways to close it:

1. Freeze the failing clock/timezone inputs at BASE and CHANGE, compare the target outcomes, and classify before changing the expectation.
2. Recover a BASE artifact for the exact boundary clock, timezone and dependency/configuration identity, compare its output to CHANGE, and record the classification.

Acceptable optional nitpicks: Standardizing timestamp display is optional; changing expected timestamps alone is not a classification.

## tv-3-07 - Dependency/config identity unspecified in baseline claim

Location: [Reviewer notes](../fixtures/tv-3-07.md), evidence V1-V4 and Reviewer notes regression claim (log starts at fixtures/tv-3-07.md:36).

Exact evidence gap: BASE and CHANGE results exist, but unknown dependency/configuration differences prevent attributing the failure to the change.

Adequate ways to close it:

1. Recover BASE dependency and parser configuration metadata, establish a comparable environment, and classify using the matched results.
2. Execute BASE and CHANGE with the same pinned lock and parser configuration, compare the target failure, and classify before modifying the fixture.

Acceptable optional nitpicks: A compact environment-identity table is optional; a BASE revision label alone does not establish comparability.

## tv-3-08 - Historical failure anecdote without evidence

Location: [Reviewer notes](../fixtures/tv-3-08.md), evidence V2-V4 and Reviewer notes suppression proposal (log starts at fixtures/tv-3-08.md:36).

Exact evidence gap: The anecdote cannot link this failure to the pre-change baseline; the pre-existing classification is unsupported before suppression.

Adequate ways to close it:

1. Run the failing target at BASE under the same inputs/configuration and compare the outcome before deciding on remediation.
2. Recover an attributable pre-change artifact for BASE with this target's matching failure and environment, then document the evidence-based classification.

Acceptable optional nitpicks: A link to discussion may add context but is optional and cannot replace the baseline evidence.

## tv-3-09 - Cached baseline summary unlinked to revision

Location: [Reviewer notes](../fixtures/tv-3-09.md), evidence V2-V4 and Reviewer notes pre-existing claim (log starts at fixtures/tv-3-09.md:36).

Exact evidence gap: The cache has matching failure and environment fields but no source identity proving it is the actual pre-change baseline.

Adequate ways to close it:

1. Recover the cached run's source revision/digest and demonstrate it is BASE, then compare its target failure to CHANGE and classify.
2. Obtain a fresh BASE result under the matching environment and inputs, compare the failure fingerprints, and record classification before changing expectations.

Acceptable optional nitpicks: Stored evidence can be sufficient once its source identity is established; requiring a fresh run regardless is unnecessary.

## tv-3-10 - Intermittent failure without classification

Location: [Reviewer notes](../fixtures/tv-3-10.md), evidence V2-V5 and Reviewer notes tolerance-change proposal (log starts at fixtures/tv-3-10.md:36).

Exact evidence gap: A pass with a different schedule does not establish whether the observed intermittent failure predates the change.

Adequate ways to close it:

1. Replay the captured failing seed and deterministic scheduler trace at BASE and CHANGE, compare outcomes and classify before increasing tolerance.
2. Retrieve an attributable BASE replay artifact for rotate-s17 and matching environment, compare the failure with CHANGE, and document its classification.

Acceptable optional nitpicks: A flake label can be optional metadata, but it is not the pre-existing/regression classification.

## tv-3-11 - Untouched generated-fixture failure

Location: [Reviewer notes](../fixtures/tv-3-11.md), evidence V2-V4 and Reviewer notes regeneration proposal (log starts at fixtures/tv-3-11.md:36).

Exact evidence gap: The generated-fixture mismatch has no matched baseline classification; regeneration could conceal either a prior problem or a regression.

Adequate ways to close it:

1. Run the same generator/test inputs at BASE and compare the mismatch to CHANGE, classifying before replacing the fixture.
2. Use a BASE artifact with matching generator version, seed and input digest plus target outcome, compare it with CHANGE, and record the classification.

Acceptable optional nitpicks: Showing the generator invocation beside its metadata is optional; regeneration alone is not evidence of cause.

## tv-3-12 - Failure attributed to environment without baseline

Location: [Reviewer notes](../fixtures/tv-3-12.md), evidence V2-V4 and Reviewer notes assertion-change proposal (log starts at fixtures/tv-3-12.md:36).

Exact evidence gap: The environmental explanation is speculative until the same failure is compared at BASE under the actual failing locale.

Adequate ways to close it:

1. Run the failing target at BASE with locale-b and the same dependency/configuration identity, compare outcomes and classify before remediation.
2. Recover a BASE/locale-b result for this exact target and inputs, compare its failure with CHANGE, and document pre-existing versus regression.

Acceptable optional nitpicks: Listing locale beside the command is optional; there is no basis to demand installing tools or changing the environment.

## tv-3-c1 - Conclusive variant 1: matched direct baseline comparison

Location: [Reviewer notes](../fixtures/tv-3-c1.md), evidence V2-V5 (log starts at fixtures/tv-3-c1.md:34).

Conclusive evidence: An identified BASE comparison in an identical environment reproduces the exact untouched-test failure, establishing it is pre-existing before any remediation.

Why a repeated check is a false positive: the cited record already settles pre-existing versus regression for the observed failure; requiring another run solely to repeat that evidence adds an unsupported acceptance condition.

Acceptable optional nitpicks: Linking the existing follow-up is optional; another blocking baseline run is a false positive.

## tv-3-c2 - Conclusive variant 2: retained snapshot comparison

Location: [Reviewer notes](../fixtures/tv-3-c2.md), evidence V2-V5 (log starts at fixtures/tv-3-c2.md:34).

Conclusive evidence: The retained, attributable baseline artifact has matching configuration and identical full snapshot mismatch, so storage does not make classification incomplete.

Why a repeated check is a false positive: the cited record already settles pre-existing versus regression for the observed failure; requiring another run solely to repeat that evidence adds an unsupported acceptance condition.

Acceptable optional nitpicks: An artifact link is optional; demanding a fresh baseline worktree solely because evidence is retained is a false positive.

## tv-3-c3 - Conclusive variant 3: controlled order comparison

Location: [Reviewer notes](../fixtures/tv-3-c3.md), evidence V2-V5 (log starts at fixtures/tv-3-c3.md:34).

Conclusive evidence: The actual failing order and initial state are reproduced at both revisions with the same failure, conclusively classifying the observed diagnostic failure.

Why a repeated check is a false positive: the cited record already settles pre-existing versus regression for the observed failure; requiring another run solely to repeat that evidence adds an unsupported acceptance condition.

Acceptable optional nitpicks: Displaying the sequence more compactly is optional; repeating the full suite adds no necessary classification evidence.

## tv-3-c4 - Conclusive variant 4: controlled clock and environment comparison

Location: [Reviewer notes](../fixtures/tv-3-c4.md), evidence V2-V5 (log starts at fixtures/tv-3-c4.md:34).

Conclusive evidence: The matched failing clock, locale, inputs and dependency/configuration identity establish the same failure at BASE, so the observed failure is already classified.

Why a repeated check is a false positive: the cited record already settles pre-existing versus regression for the observed failure; requiring another run solely to repeat that evidence adds an unsupported acceptance condition.

Acceptable optional nitpicks: A shorter clock label is optional; another blocking baseline comparison is a false positive.
