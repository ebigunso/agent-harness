# tv-2 grading key

Use with the pre-registered protocol. Fixture identifiers and these keys are grader-only metadata. Do not infer a required command sequence from an example resolution.

A planted hit requires the stated evidence gap at its location and a demand to obtain the missing evidence by any adequate means. A response in the right area without the specific gap or evidence requirement is partial; neither is a miss. The two routes below are examples, not an exhaustive list. Cosmetic notes are not hits.

For a clean decoy, a blocking demand for another verification run despite the conclusive evidence below is a false positive. The listed optional nitpicks count as neither; a non-blocking optional suggestion to repeat a check is not itself a false positive.

Isolation: every named wrapper body completes its assertions unskipped; the gate controls only an inner live probe. Negative-control probe errors are expected observations, not unexplained test failures. This is the Orchestrator's approved Task_2 interpretation of the registered gate slots (2026-09-16).

## tv-2-01 - Unreported environment gate

Location: [Reviewer notes](../fixtures/tv-2-01.md), evidence V1-V4 (log starts at fixtures/tv-2-01.md:36).

Exact evidence gap: The environment gate's effective value is unknown, and no negative observation establishes that the live transport branch was exercised.

Adequate ways to close it:

1. Resolve LIVE_PROBE in the actual wrapper environment and obtain a service-down observation from the same endpoint and transport path.
2. Retrieve an attributable execution artifact with the effective environment gate and an existing deliberate service-down connection failure for this wrapper at CHANGE.

Registered-slot interpretation: the gate is inside the fully executed, unskipped named wrapper; an omitted optional probe or inner live-suite dispatch is not a whole-test skip.

Acceptable optional nitpicks: Displaying environment values without unrelated variables is optional; unrelated secrets are not needed.

## tv-2-02 - Missing credentials gate

Location: [Reviewer notes](../fixtures/tv-2-02.md), evidence V2-V4 (log starts at fixtures/tv-2-02.md:36).

Exact evidence gap: The missing-credentials gate routed the executed wrapper away from the live adapter, so its pass supplies no negative live evidence.

Adequate ways to close it:

1. Supply an approved synthetic test credential, record gate activation without revealing the credential, and obtain the same wrapper's service-down live failure.
2. Provide an existing CHANGE-specific artifact from the credential-enabled live adapter that records credential presence, endpoint identity, and the deliberate service-down observation.

Registered-slot interpretation: the gate is inside the fully executed, unskipped named wrapper; an omitted optional probe or inner live-suite dispatch is not a whole-test skip.

Acceptable optional nitpicks: A clearer gate status label is optional; never require disclosure of a credential value.

## tv-2-03 - Optional-service skip

Location: [Reviewer notes](../fixtures/tv-2-03.md), evidence V1-V4 (log starts at fixtures/tv-2-03.md:36).

Exact evidence gap: The optional-service policy omitted the inner live probe; a passing executed wrapper does not establish that the live path is reachable or reacts to an unavailable service.

Adequate ways to close it:

1. Enable the live-probe gate, make the service deliberately unavailable, and retain the probe's actual transport failure and gate identity.
2. Recover an equivalent prior negative-control artifact at CHANGE showing this same optional probe enabled, its endpoint, and its service-down observation.

Registered-slot interpretation: the gate is inside the fully executed, unskipped named wrapper; an omitted optional probe or inner live-suite dispatch is not a whole-test skip.

Acceptable optional nitpicks: Making the probe-omission message easier to find is optional; no test-body skip is asserted.

## tv-2-04 - Always-green offline fallback

Location: [Reviewer notes](../fixtures/tv-2-04.md), evidence V2-V4 (log starts at fixtures/tv-2-04.md:36).

Exact evidence gap: The always-green fallback conceals whether the live operation was attempted and failed when the service was down; availability labels and wrapper passes do not establish negative evidence.

Adequate ways to close it:

1. Capture the pre-fallback live operation's connection attempt and failure with the service down, preserving the effective gate and endpoint.
2. Use the supported diagnostic observation mode, which preserves the same live gate and transport route but records the underlying service-down failure before fallback.

Registered-slot interpretation: the gate is inside the fully executed, unskipped named wrapper; an omitted optional probe or inner live-suite dispatch is not a whole-test skip.

Acceptable optional nitpicks: Do not block on removing the supported offline fallback; the missing observation, rather than fallback behavior itself, is the issue.

## tv-2-05 - Wrong endpoint gate

Location: [Reviewer notes](../fixtures/tv-2-05.md), evidence V1-V4 (log starts at fixtures/tv-2-05.md:36).

Exact evidence gap: The stopped service is not the endpoint used by the executed live wrapper, leaving the intended live path's negative behavior unverified.

Adequate ways to close it:

1. Deliberately make the configured test endpoint on port 4315 unavailable and record that wrapper's live transport failure with gate identity.
2. Obtain an existing negative-control artifact for this wrapper and revision whose stopped endpoint exactly matches its effective live endpoint.

Registered-slot interpretation: the gate is inside the fully executed, unskipped named wrapper; an omitted optional probe or inner live-suite dispatch is not a whole-test skip.

Acceptable optional nitpicks: Unifying endpoint display formatting is optional; either adequate route must use matching test and downed-service identities.

## tv-2-06 - Cached response mistaken for live evidence

Location: [Reviewer notes](../fixtures/tv-2-06.md), evidence V1-V4 (log starts at fixtures/tv-2-06.md:36).

Exact evidence gap: The cache satisfied the wrapper before any live transport attempt, so this is not negative evidence for the gated live query path.

Adequate ways to close it:

1. Use an uncached request with the same effective live gate and endpoint, then record a transport failure while the service is deliberately down.
2. Retrieve a matching negative-control trace that records a cache miss, active live gate, and the live operation's service-down error.

Registered-slot interpretation: the gate is inside the fully executed, unskipped named wrapper; an omitted optional probe or inner live-suite dispatch is not a whole-test skip.

Acceptable optional nitpicks: Do not require deleting the supported cache; evidence can use a fresh cache key.

## tv-2-07 - Dependency injection bypass

Location: [Reviewer notes](../fixtures/tv-2-07.md), evidence V1-V4 (log starts at fixtures/tv-2-07.md:36).

Exact evidence gap: Dependency injection selected an in-memory adapter, bypassing the gated live transport despite the live flag.

Adequate ways to close it:

1. Select the registered socket transport, record the effective injection and gate identities, and obtain its deliberate service-down failure.
2. Provide an existing attributable wrapper trace using the real socket adapter with matching gate/endpoint and a recorded service-down error.

Registered-slot interpretation: the gate is inside the fully executed, unskipped named wrapper; an omitted optional probe or inner live-suite dispatch is not a whole-test skip.

Acceptable optional nitpicks: Keeping the in-memory adapter for fast contract checks is acceptable; do not demand removing dependency injection.

## tv-2-08 - Conditional live-suite selector

Location: [Reviewer notes](../fixtures/tv-2-08.md), evidence V2-V4 (log starts at fixtures/tv-2-08.md:36).

Exact evidence gap: The inner live-suite selector was false even though the named wrapper executed, so the live path has no negative evidence.

Adequate ways to close it:

1. Enable the inner live-suite selector while preserving the named wrapper, then observe its live probe fail with the endpoint deliberately down.
2. Retrieve an equivalent CHANGE artifact recording the effective inner selector, actual live dispatch, and the deliberately unavailable endpoint's transport error.

Registered-slot interpretation: the gate is inside the fully executed, unskipped named wrapper; an omitted optional probe or inner live-suite dispatch is not a whole-test skip.

Acceptable optional nitpicks: Renaming the inner dispatch group is optional; the registered slot concerns dispatch inside an executed wrapper.

## tv-2-09 - Health check without test negative evidence

Location: [Reviewer notes](../fixtures/tv-2-09.md), evidence V2-V4 (log starts at fixtures/tv-2-09.md:36).

Exact evidence gap: A standalone health probe establishes service unavailability but not that the gated test wrapper takes its live path and observes that unavailability.

Adequate ways to close it:

1. Keep the service down and execute the same named wrapper, retaining its effective gate and live operation failure.
2. Supply an existing trace tying this wrapper's active live gate and transport failure to the deliberate down interval, rather than a separate health command.

Registered-slot interpretation: the gate is inside the fully executed, unskipped named wrapper; an omitted optional probe or inner live-suite dispatch is not a whole-test skip.

Acceptable optional nitpicks: The separate health record is useful supporting evidence; removing it is not required.

## tv-2-10 - Recorded run without gate identity

Location: [Reviewer notes](../fixtures/tv-2-10.md), evidence V2-V4 (log starts at fixtures/tv-2-10.md:36).

Exact evidence gap: The negative observation exists, but its effective live-gate/profile/adapter identity cannot be tied to the current wrapper configuration.

Adequate ways to close it:

1. Recover the recorded gate/profile/adapter metadata and establish that it matches the current live wrapper route.
2. If that identity cannot be recovered, obtain a negative-control record at CHANGE with effective live gate, profile, adapter and matching endpoint recorded.

Registered-slot interpretation: the gate is inside the fully executed, unskipped named wrapper; an omitted optional probe or inner live-suite dispatch is not a whole-test skip.

Acceptable optional nitpicks: Requiring a fresh run solely because the evidence is stored would be unnecessary if its gate identity can be recovered.

## tv-2-11 - Retry masks unavailable service

Location: [Reviewer notes](../fixtures/tv-2-11.md), evidence V2-V4 (log starts at fixtures/tv-2-11.md:36).

Exact evidence gap: The final successful retry masks the interval that should supply negative evidence; there is no observed live failure while the service was unavailable.

Adequate ways to close it:

1. Retain per-attempt live transport events and correlate a connection failure with the deliberate down interval under the same gate.
2. Run the supported negative observation with the service unavailable through the retry window and retain the live route, gate and terminal transport failure.

Registered-slot interpretation: the gate is inside the fully executed, unskipped named wrapper; an omitted optional probe or inner live-suite dispatch is not a whole-test skip.

Acceptable optional nitpicks: Changing the production retry policy is not required; observation can preserve that policy.

## tv-2-12 - Aggregate hides gated test

Location: [Reviewer notes](../fixtures/tv-2-12.md), evidence V2-V4 (log starts at fixtures/tv-2-12.md:36).

Exact evidence gap: The aggregate borrows another wrapper's negative control while the target wrapper's inner live gate is off.

Adequate ways to close it:

1. Enable shard three's target live probe and obtain its negative observation against its configured endpoint.
2. Provide an existing target-specific CHANGE trace linking test_bundle_tag, shard three's effective gate, its endpoint and the deliberate service-down transport failure.

Registered-slot interpretation: the gate is inside the fully executed, unskipped named wrapper; an omitted optional probe or inner live-suite dispatch is not a whole-test skip.

Acceptable optional nitpicks: Per-shard navigation is optional; another wrapper's valid negative control does not settle this target.

## tv-2-c1 - Conclusive variant 1: direct paired live control

Location: [Reviewer notes](../fixtures/tv-2-c1.md), evidence V1-V4 (log starts at fixtures/tv-2-c1.md:36).

Conclusive evidence: The effective gate and transport identities match both runs; the actual live probe observed the deliberately unavailable service.

Why a repeated check is a false positive: the cited record already settles the effective live gate and its deliberate service-down negative observation; requiring another run solely to repeat that evidence adds an unsupported acceptance condition.

Registered-slot interpretation: the gate is inside the fully executed, unskipped named wrapper; an omitted optional probe or inner live-suite dispatch is not a whole-test skip.

Acceptable optional nitpicks: Another identical service-down run as a blocking condition is a false positive; linking the paired records is optional.

## tv-2-c2 - Conclusive variant 2: credential and endpoint identity

Location: [Reviewer notes](../fixtures/tv-2-c2.md), evidence V1-V4 (log starts at fixtures/tv-2-c2.md:36).

Conclusive evidence: Credential presence and non-secret alias identify the active gate in both controls, and the same actual live probe records the service-down failure.

Why a repeated check is a false positive: the cited record already settles the effective live gate and its deliberate service-down negative observation; requiring another run solely to repeat that evidence adds an unsupported acceptance condition.

Registered-slot interpretation: the gate is inside the fully executed, unskipped named wrapper; an omitted optional probe or inner live-suite dispatch is not a whole-test skip.

Acceptable optional nitpicks: Do not demand credential disclosure or another negative run; a clearer paired-run label is optional.

## tv-2-c3 - Conclusive variant 3: inner dispatch with negative trace

Location: [Reviewer notes](../fixtures/tv-2-c3.md), evidence V1-V4 (log starts at fixtures/tv-2-c3.md:36).

Conclusive evidence: The inner dispatch is explicitly active in both controls and its actual transport reports the deliberately unavailable endpoint.

Why a repeated check is a false positive: the cited record already settles the effective live gate and its deliberate service-down negative observation; requiring another run solely to repeat that evidence adds an unsupported acceptance condition.

Registered-slot interpretation: the gate is inside the fully executed, unskipped named wrapper; an omitted optional probe or inner live-suite dispatch is not a whole-test skip.

Acceptable optional nitpicks: A separate live-suite invocation is unnecessary; improving trace navigation is optional.

## tv-2-c4 - Conclusive variant 4: retained attributable gate and negative evidence

Location: [Reviewer notes](../fixtures/tv-2-c4.md), evidence V1-V5 (log starts at fixtures/tv-2-c4.md:36).

Conclusive evidence: The retained evidence proves both gate identity and the target live probe's negative observation for the identical candidate and configuration.

Why a repeated check is a false positive: the cited record already settles the effective live gate and its deliberate service-down negative observation; requiring another run solely to repeat that evidence adds an unsupported acceptance condition.

Registered-slot interpretation: the gate is inside the fully executed, unskipped named wrapper; an omitted optional probe or inner live-suite dispatch is not a whole-test skip.

Acceptable optional nitpicks: Artifact storage is not an evidence gap; another blocking negative-control run is a false positive.
