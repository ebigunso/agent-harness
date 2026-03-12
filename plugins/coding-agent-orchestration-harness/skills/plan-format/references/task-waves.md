# Task Waves (Parallel Dispatch Semantics)

Waves make parallelism explicit and reviewable.

---

## Wave meaning

- A wave is a set of tasks intended to be executed in parallel (subject to constraints).
- Waves are executed sequentially.

Default semantics:
- Within a wave: dispatch tasks in parallel by default.
- Between waves: do not start wave N+1 until wave N tasks are done (or explicitly waived).

---

## When to keep tasks in the same wave

Put tasks in the same wave when:
- dependencies are satisfied
- `owns` are disjoint (no file/dir overlap)
- merge/conflict risk is low
- parallel execution materially reduces elapsed time

---

## When to separate into sequential waves

Use sequential waves when:
- one task produces inputs used by another (true dependency)
- parallelism would create known merge/conflict risk
- the plan calls for gating (e.g., review approval before proceeding)

Examples:
- Wave 1: design decision
- Wave 2: implementation tasks in parallel (disjoint owns)
- Wave 3: review gate (and E2E evidence if UI impacted)

---

## How to write waves

Preferred format:

- Wave 1 (parallel): [Task_1, Task_2]
- Wave 2 (parallel): [Task_3]
- Wave 3 (parallel): [Task_4, Task_5]

Add short labels when helpful:

- Wave 2 (parallel) — “backend implementation”: [Task_3, Task_4]

---

## “Maximize parallelism by default” note

Parallelism is the default, but not mandatory.
Use judgment when parallelism increases risk disproportionately.
