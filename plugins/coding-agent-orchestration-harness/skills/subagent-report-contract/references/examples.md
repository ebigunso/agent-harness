# Worker Report Examples

Field meanings and filling notes: `schema.yaml`.

## Example: done (own-edit correction, then rerun)

```yaml
task_id: "Task_2"
status: done

summary: |-
  Implemented X and updated Y. The first unit run failed on an off-by-one in my own edit against the acceptance criterion (upper bound is inclusive); corrected the bound and reran. Nothing else changed.

files_changed:
  - path: "src/foo/bar.ts"
    change: modified
    intent: "Add validation for input Z"

commands_run:
  - command: "npm run test:unit"
    result: fail
    notes: "1 failed: input-Z upper bound rejected the inclusive maximum; mistake in my own edit against the criterion."
  - command: "npm run test:unit"
    result: pass
    notes: "Rerun after correcting the bound in src/foo/bar.ts."

validation_results:
  - kind: command
    required: true
    owner: worker
    detail: "npm run test:unit"
    status: pass
    evidence: "Rerun exit code 0; 42 tests passed, 0 failed, including the new input-Z validation cases."

tests:
  ran: true
  notes: "Unit tests executed."

blockers: []
questions_for_orchestrator: []
assumptions: []
rule_candidates: []
lesson_candidates:
  - id: "LESSON-CAND-inclusive-bound-off-by-one"
    category: validation
    deviation: "The first unit run failed on an off-by-one in my own edit against the inclusive upper bound the acceptance criterion names."
    root_cause: "The bound was implemented as exclusive; the criterion was not reread before the first run."
    prevention: "Reread the acceptance criterion's stated bounds against the edit before the first validation run."
    promotion_target: residual_risk
    suggested_destination: "docs/coding-agent/lessons.md"
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
    evidence: "Exit code 0; 18 tests passed, 0 failed, including DarkModeToggle persistence cases."

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
  Expected: npm run test:unit passes. Actual: the command fails because dependency <X> is missing; the README's setup step (npm install) has not been run in this checkout. No setup was performed.

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
  - "Unit tests fail because dependency <X> is missing. Proposed remedy: run the README's setup step (npm install) in this checkout, either pre-authorized in a redispatch or done by the Orchestrator; then rerun npm run test:unit. Not done: setup is outside the acceptance criteria."

questions_for_orchestrator: []

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

## Example: blocked (a failing test that encoded the old behavior, surfaced with a remedy)

The assigned change is complete and the new behavior is present; the test that asserted the old behavior is outside `owns` and the packet says nothing about it. The Worker neither edits the test, shims the old behavior, nor narrows the change; it surfaces the finding as a design alert with a proposed remedy and waits.

```yaml
task_id: "Task_5"
status: blocked

summary: |-
  Changed price rounding to round-half-even per the acceptance criterion; the new behavior is in place.
  Expected: npm run test:unit passes. Actual: 1 test fails: tests/pricing/rounding.test.ts asserts the old round-half-up result. The test is outside owns and the packet does not rule on it; no change was made to it.

files_changed:
  - path: "src/pricing/round.ts"
    change: modified
    intent: "Round half to even, per the acceptance criterion"

commands_run:
  - command: "npm run test:unit"
    result: fail
    notes: "40 passed, 1 failed: rounding.test.ts 'rounds 2.5 up to 3' expects the pre-change behavior."

validation_results:
  - kind: command
    required: true
    owner: worker
    detail: "npm run test:unit"
    status: fail
    evidence: "Exit code 1; 40 passed, 1 failed. The failing assertion encodes the old rounding; the assigned behavior is correct against the criterion."

tests:
  ran: true
  notes: "Unit tests ran; the single failure is the old-behavior assertion, left untouched."

blockers:
  - "Design alert. Boundary: tests/pricing/rounding.test.ts (outside owns) asserts round-half-up, which the criterion replaces. Cleaner alternative: update the assertion to the round-half-even result (2.5 -> 2), or delete the case if the round-half-up guarantee has no remaining consumer. Cost delta: one assertion line versus keeping a second rounding path for the test. Proposed remedy: authorize updating the assertion; no change made pending the ruling."

questions_for_orchestrator: []
assumptions: []
rule_candidates: []
lesson_candidates:
  - id: "LESSON-CAND-old-behavior-test-unruled"
    category: planning
    deviation: "A test outside owns encoded the behavior the acceptance criterion replaces, and the packet did not rule on it, so the task blocked on a ruling."
    root_cause: "The plan changed a behavior without listing the tests that asserted the old one or pre-ruling their update."
    prevention: "When a task changes a behavior, name the tests that assert the old behavior in the packet and pre-rule whether they are to be updated."
    promotion_target: repo_rule
    suggested_destination: "docs/coding-agent/rules/orchestrator.md"
```

## Example: done with rule candidate and harness migration candidate

Only the Orchestrator edits `docs/coding-agent/rules/*.md`; a Worker proposes a rule through `rule_candidates` instead.

```yaml
task_id: "Task_4"
status: done

summary: |-
  Added the public export for the new settings type and staged a reusable harness improvement idea.

files_changed:
  - path: "src/api/index.ts"
    change: modified
    intent: "Export the SettingsSnapshot type from the public API"

commands_run:
  - command: "npm run test:unit"
    result: pass
    notes: "All unit tests passed."
  - command: "git diff --check"
    result: pass
    notes: "No whitespace errors."

validation_results:
  - kind: command
    required: true
    owner: worker
    detail: "npm run test:unit"
    status: pass
    evidence: "Exit code 0; 27 tests passed, 0 failed, including the public-export import test."
  - kind: command
    required: true
    owner: worker
    detail: "git diff --check"
    status: pass
    evidence: "Exit code 0; no whitespace errors reported."

tests:
  ran: true
  notes: "Unit tests and whitespace validation ran."

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
