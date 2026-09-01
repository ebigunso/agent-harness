# Test Authoring: Assert Behavior Contracts

Read when writing, modifying, or reviewing tests.

## Selection Principle

- A test earns its place when it would detect a plausible defect in behavior someone depends on, at the cheapest boundary that observes it.
- All three parts must hold: a plausible defect (not a hypothetical one), depended-on behavior (an observable contract, not an implementation choice), and the cheapest observing boundary (not the most convenient seam).

## What Earns a Test

- Contract boundaries: behavior promised to a consumer, exercised through the public interface.
- Decision logic and edge values: branches, empty/zero/max/off-by-one; representative cases per equivalence class, not exhaustive matrices sharing one code path.
- Invariants and failure paths: bad input, partial failure, round-trip properties.
- Fixed bugs, generalized to the violated contract (see Regression Discipline).

## Non-Earners

- Branchless glue and delegation.
- Framework/stdlib behavior.
- Config plumbing.
- Contracts already guarded at a higher-value boundary.

## Necessity Gate

- Before writing a test, ask: "would anything other than this test observe the difference if this behavior changed?" — a boundary consumer, a documented contract, a user-visible outcome.
- If the only observer is the test itself, the test pins implementation, not a contract. Do not write it; the test suite is not its own consumer.

## Anchor Heuristic

- For each assertion, ask: "if this assertion failed, would it indicate a real defect or just a changed implementation detail?"
- Real defect: keep the assertion. Implementation detail: re-anchor it to the contract.

## Placement

- One contract, one boundary: test each contract once, at the level that observes it.
- Do not re-assert the same contract at multiple levels; pick the cheapest boundary where a violation is observable.

## Regression Discipline

- Derive the general contract the bug violated and test that, not the incident's specific trajectory.
- One test per violated contract, not one per symptom.

## Low-Signal Surfaces (with the correct alternative)

- Log output/format: test the behavior that emits it, not the message.
- Exact error-message prose: assert error types/codes/classification instead.
- Over-specified mock interactions (call counts, ordering not in the contract): assert outcomes and contract-relevant interactions.
- Snapshot tests of incidental formatting: snapshot only contract-stable output.

## Contract Exception

- Logs/diagnostics that are themselves contracts are tested at that contract boundary:
  - audit trails
  - compliance events
  - telemetry consumed by alerting
  - documented operator diagnostics

## Completeness Check

- Completeness is not line coverage; invert the question: "which plausible defect would ship undetected?"
- For each contract the change touches, there should be a test that fails if it breaks. A changed contract with no failing observer is the gap to close.

## Rationale

- Convenience-surface assertions punish refactoring and produce low-signal failures.
- Tests justified only by themselves constrain legitimate change without protecting any consumer.
