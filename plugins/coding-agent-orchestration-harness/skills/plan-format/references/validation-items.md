# Validation Items Model

Validation must be explicit so it cannot be forgotten or treated as optional.

Each Task_X should include at least one validation item.
For implementation tasks, require at least one deterministic check when possible.

---

## Fields

- kind: command | manual | e2e | review
- required: true | false
- owner: worker | reviewer | orchestrator | user
- detail: a concrete command or checklist (be explicit)

---

## Guidance

- Use owner=worker for deterministic CLI checks (unit tests, lint, build).
- Use owner=reviewer for review gates and browser-based E2E/visual checks.
- Use owner=user only for validations that truly must be done by a human user (e.g., product sign-off).
- Use required=false only for “nice-to-have” checks.
- For non-trivial repository work, derive validation items from the repo rule suite when available:
  - `common.md`: repository validation contract and safety boundaries.
  - `worker.md`: Worker-owned check mapping.
  - `reviewer.md`: Reviewer-owned evidence requirements and review-risk hotspots.
- If rule files are missing or invalid and validation cannot be selected confidently, Orchestrator should run rulebook bootstrap/refresh/repair or explicitly record a waiver before dispatch.
- Trivial work does not require rule-suite bootstrap.

Rule of thumb:
- If required=true and owner is not user, someone in the system must produce evidence before the plan can be “done”.

---

## Examples

Example 1: unit tests

    validation:
      - kind: command
        required: true
        owner: worker
        detail: "npm run test:unit"

Example 2: manual sign-off

    validation:
      - kind: manual
        required: true
        owner: user
        detail: "Confirm layout looks correct on your device"

Example 3: browser-based E2E/visual

    validation:
      - kind: e2e
        required: true
        owner: reviewer
        detail: "Run the E2E spec in plan using the selected browser automation provider"

Example 4: optional cleanup pass

    validation:
      - kind: review
        required: false
        owner: reviewer
        detail: "Optional cleanup: readability polish"
