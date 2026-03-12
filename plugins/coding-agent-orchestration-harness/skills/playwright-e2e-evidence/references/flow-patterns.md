# Flow Patterns and Interaction Conventions

Principles:
- Prefer snapshot-driven interaction (stable refs) over brittle CSS selectors.
- Validate key expectations at each step (page state, text, element presence).
- Capture screenshots at states that matter for acceptance criteria.

Common steps:
- navigate: go to a path relative to base_url
- snapshot: capture accessibility snapshot and identify elements by ref
- click/type/select: use snapshot refs or stable test ids
- resize: switch viewport and re-check critical UI

Evidence patterns:
- At least one screenshot per required state.
- Record console errors (minimum).
- Record failed network requests when the flow touches APIs.
