# Execution Plan Lifecycle (Active → Completed)

This reference describes how execution plans are maintained over time.

---

## 0) Roadmaps vs execution plans

- Roadmaps stay at high-level chunk granularity; add concrete Task_X detail only for the next executable chunk.
- Keep roadmaps and concrete execution plans in separate files with independent lifecycles.
- Name plans by the outcome they achieve, not by sequence number.

## 1) Create

- Create under `docs/coding-agent/plans/active/`.
- Use the plan template and fill:
  - tasks
  - validation ownership
  - task waves
  - initial assumptions

## 2) Approve

- status: `draft` → `approved`
- Record key approvals/constraints in Decision Log if needed.

## 3) Execute

- status: `in_progress`
- Execute wave-by-wave.
- After each wave:
  - append a Progress Log entry (what completed + validation evidence)

### Deviations mid-execution (mandatory interrupt)

If a deviation occurs mid-execution (unexpected outcome, blocked/failed, reviewer revision, waiver needed, new insight):
1) Pause dispatch and stop edits.
2) Run the improvement loop checklist:
   - `docs/coding-agent/references/improvement-loop.md`
3) Record a Decision Log entry:
   - trigger/new insight
   - plan delta
   - tradeoffs
   - approval status
4) Update tasks/waves/validation as needed.
5) Continue only after the plan delta is approved (when non-trivial).

## 4) Close

Before closing:
- ensure required validations are evidenced (or waived)
- ensure review gate is satisfied (or waived)

Then:
- status: `done`
- move file to `docs/coding-agent/plans/completed/`

## 5) Post-mortem improvements (recommended)

If a deviation occurred:
- add a repo-local lesson entry (atomic)
- add/update reference docs (how-to-run / validation / ui-e2e / troubleshooting)
- stage migration candidates for cross-repo improvements
