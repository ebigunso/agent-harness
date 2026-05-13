# Worker Report Examples

## Example: done (with required validation)

```yaml
task_id: "Task_2"
status: done

summary: |-
  Implemented X and updated Y. Expected behavior matches acceptance criteria.

files_changed:
  - path: "src/foo/bar.ts"
    change: modified
    intent: "Add validation for input Z"

commands_run:
  - command: "npm run test:unit"
    result: pass
    notes: "All unit tests passed."

validation_results:
  - kind: command
    required: true
    owner: worker
    detail: "npm run test:unit"
    status: pass
    evidence: "Exit code 0."

tests:
  ran: true
  notes: "Unit tests executed."

blockers: []
questions_for_orchestrator: []
assumptions: []
rule_candidates: []
```

## Example: done with bounded Worker UI probe

```yaml
task_id: "Task_3"
status: done

summary: |-
  Updated the settings page dark-mode toggle and verified the local interaction with a bounded Worker UI probe.

files_changed:
  - path: "src/settings/DarkModeToggle.tsx"
    change: modified
    intent: "Wire the dark-mode toggle to persisted settings state"

commands_run:
  - command: "npm run test:unit"
    result: pass
    notes: "Unit tests passed."

validation_results:
  - kind: command
    required: true
    owner: worker
    detail: "npm run test:unit"
    status: pass
    evidence: "Exit code 0."

ui_probes:
  - base_url: "http://localhost:3000"
    flow: "Open settings page and toggle dark mode"
    result: pass
    evidence: ".playwright-cli/worker-probe-settings-dark-mode.png"
    notes: "No layout overlap after local CSS adjustment."

tests:
  ran: true
  notes: "Unit tests plus bounded Worker UI probe."

blockers: []
questions_for_orchestrator: []
assumptions: []
rule_candidates: []
```

## Example: blocked (cannot run required validation)

```yaml
task_id: "Task_2"
status: blocked

summary: |-
  Changes implemented, but required validation could not run.
  Expected: npm run test:unit passes. Actual: command fails due to missing dependency.

files_changed:
  - path: "src/foo/bar.ts"
    change: modified
    intent: "Add validation for input Z"

commands_run:
  - command: "npm run test:unit"
    result: fail
    notes: "Error: <short excerpt>"

validation_results:
  - kind: command
    required: true
    owner: worker
    detail: "npm run test:unit"
    status: fail
    evidence: "Exit code 1. Error: <excerpt>"

tests:
  ran: false
  notes: "Required unit test command failed."

blockers:
  - "Unit tests fail due to missing dependency <X>"

questions_for_orchestrator:
  - "Should I install dependency X (if allowed), or is there a repo-specific setup step?"

assumptions: []
rule_candidates: []
lesson_candidates:
  - id: "LESSON-CAND-missing-test-dependency"
    category: environment
    deviation: "Required validation could not complete because the documented test dependency was unavailable."
    root_cause: "The environment lacked a dependency that the task contract assumed was already installed."
    prevention: "Record prerequisite validation dependencies near the command or setup instructions before dispatch."
    promotion_target: troubleshooting
    suggested_destination: "docs/coding-agent/lessons.md"
```

## Example: done with harness migration candidate

```yaml
task_id: "Task_4"
status: done

summary: |-
  Updated repository review guidance and staged a reusable harness improvement idea.

files_changed:
  - path: "docs/coding-agent/rules/reviewer.md"
    change: modified
    intent: "Add repository-specific review heuristic"

commands_run:
  - command: "git diff --check"
    result: pass
    notes: "No whitespace errors."

validation_results:
  - kind: command
    required: true
    owner: worker
    detail: "git diff --check"
    status: pass
    evidence: "Exit code 0."

tests:
  ran: true
  notes: "Whitespace validation ran."

blockers: []
questions_for_orchestrator: []
assumptions: []
rule_candidates:
  - audience: reviewer
    id: "RB-CAND-review-public-api"
    rule: "Review public API changes for downstream compatibility before approval."
    rationale: "This prevents repository-specific public surface regressions."
    scope: "Reviewer-owned review of exported APIs in this repository."
    example: "A new public type should have an import/construction path checked."
harness_migration_candidates:
  - id: "HMC-review-public-api"
    category: review
    proposed_home: "engineering-quality-baselines/references/review-latent-risk-public-api.md"
    generalized_rule: "Public API changes should be reviewed for downstream compatibility."
    trigger: "Public structs, enums, functions, DTOs, exports, examples, or feature-gated public items change."
    evidence_from_repo: "A repository review found missing compatibility evidence for a public export."
    rationale: "Public API compatibility risk appears across many repositories."
    suggested_change: "Add a cross-repo public API compatibility review lens."
```
