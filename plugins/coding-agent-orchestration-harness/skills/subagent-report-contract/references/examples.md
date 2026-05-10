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
    promotion_target: "troubleshooting/*"
```
