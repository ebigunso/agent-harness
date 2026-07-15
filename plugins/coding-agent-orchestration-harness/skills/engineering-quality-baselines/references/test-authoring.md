# Test Authoring: Assert Behavior Contracts

Read when writing, modifying, or reviewing tests.

## Principle

- Tests assert behavior contracts that prove business-logic integrity.
- A test should fail only when behavior someone depends on breaks.

## Anchor Heuristic

- For each assertion, ask: "if this assertion failed, would it indicate a real defect or just a changed implementation detail?"
- Real defect: keep the assertion. Implementation detail: re-anchor it to the contract.

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

## Rationale

- Convenience-surface assertions punish refactoring and produce low-signal failures.
