# Examples (Task_X patterns)

These are examples of task definitions and waves. Adapt to your repo.

---

## Example: backend change with tests

Task:

    ### Task_2: Add endpoint validation
    - type: impl
    - owns:
      - src/api/**
    - depends_on: [Task_1]
    - acceptance:
      - "Endpoint returns 400 on invalid input"
      - "Error payload matches existing API format"
    - validation:
      - kind: command
        required: true
        owner: worker
        detail: "npm run test:unit -- <subset>"
      - kind: review
        required: true
        owner: reviewer
        detail: "Check error handling and consistency"

Waves:

- Wave 1 (parallel): [Task_1]
- Wave 2 (parallel): [Task_2]
- Wave 3 (parallel): [Task_3]

---

## Example: documentation update

Task:

    ### Task_2: Update docs for new behavior
    - type: docs
    - owns:
      - docs/**
    - depends_on: [Task_1]
    - acceptance:
      - "Docs reflect new behavior and examples"
    - validation:
      - kind: review
        required: true
        owner: reviewer
        detail: "Check clarity, consistency, and broken links"

Waves:

- Wave 1 (parallel): [Task_1]
- Wave 2 (parallel): [Task_2]
- Wave 3 (parallel): [Task_3]

---

## Example: UI change with E2E/visual evidence

Task:

    ### Task_3: E2E/visual verification
    - type: review
    - owns: []
    - depends_on: [Task_2]
    - acceptance:
      - "No console errors during flow"
      - "Screenshots captured for login + dashboard at mobile/desktop"
    - validation:
      - kind: e2e
        required: true
        owner: reviewer
        detail: "Run the UI evidence flow using the selected browser automation provider (artifacts under the provider-defined root)"

Waves:

- Wave 1 (parallel): [Task_1]
- Wave 2 (parallel): [Task_2]
- Wave 3 (parallel): [Task_3]

---

## Example: Non-trivial PR comment response (complexity-driven planning)

This is NOT a “special-case rule”. It is an example where complexity is typically high:
multiple comments often imply multiple steps, multiple files, and validation needs.

Task:

    ### Task_1: Triage comments and update the execution plan
    - type: design
    - owns:
      - docs/coding-agent/plans/active/**
    - depends_on: []
    - acceptance:
      - "Unresolved comments are listed and classified (must-fix vs optional)"
      - "Plan delta reflects required fixes and validation ownership"
    - validation:
      - kind: review
        required: true
        owner: orchestrator
        detail: "Plan updated + reflects comment classification"

    ### Task_2: Implement must-fix changes
    - type: impl
    - owns:
      - <affected module paths>
    - depends_on: [Task_1]
    - acceptance:
      - "Must-fix comments are addressed with minimal diffs"
    - validation:
      - kind: command
        required: true
        owner: worker
        detail: "<repo-required test/lint commands>"
      - kind: review
        required: true
        owner: reviewer
        detail: "Diff review vs must-fix comments"

    ### Task_3: Review gate
    - type: review
    - owns: []
    - depends_on: [Task_2]
    - acceptance:
      - "Reviewer status is APPROVED"
    - validation:
      - kind: review
        required: true
        owner: reviewer
        detail: "Verify must-fix comments satisfied; request revisions if evidence missing"

Waves:

- Wave 1 (parallel): [Task_1]
- Wave 2 (parallel): [Task_2]
- Wave 3 (parallel): [Task_3]

---

## Example: Progress Log entry

- 2026-02-20 14:10 Wave 2 completed: [Task_2, Task_4]
  - Summary: Implemented feature X and added unit tests
  - Validation evidence: npm run test:unit (pass), npm run lint (pass)
  - Notes: Deferred optional refactor (tracked as TD-002)
