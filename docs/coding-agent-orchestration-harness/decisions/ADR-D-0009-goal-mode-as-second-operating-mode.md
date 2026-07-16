---
status: accepted
adr_type: design
date: 2026-07-16
deciders:
  - ebigunso
consulted:
  - Claude Fable 5
informed: []
supersedes: []
superseded_by: null
---

# ADR-D-0009: Goal Mode As A Second Operating Mode

## Context and Problem Statement

Coding-agent platforms ship goal engines — turn-continuation loops that keep an agent working until a stated condition is met (`/goal` in Claude Code and Codex CLI, Autopilot in GitHub Copilot CLI) — but none ship governance for the decisions those loops delegate away from humans. The harness's plan mode assumes work is decomposable before execution and protects that contract with per-decision human gates. Search-shaped work (iterate/measure/revise toward an objectively checkable end state, with task structure unknown at the start) does not fit that assumption: forcing it through plan mode produces stale plans and permission-pumping, while running it on a bare platform goal engine produces ungoverned autonomy.

## Decision Drivers

- Extend agentic coding to long-horizon, search-shaped work without abandoning the harness's safety properties.
- Keep one shared substrate (roles, validation, evidence integrity, lessons, skills) rather than forking the harness identity.
- Replace per-decision human gates with structural governance where gates cannot exist.
- Prevent goal mode from becoming an escape hatch around planning for decomposable work.

## Decision

The harness defines goal mode as a second operating mode alongside plan mode. The goal is the invariant and structure is discovered (attempt, observe, revise). Human oversight relocates from gate-before-each-decision to four structural mechanisms: a negotiated authority envelope, an append-only iteration journal with per-iteration checkpoint commits (rollback as the safety property), independent in-loop assessment, and a completion report gated by human retrospective before merge.

Mode selection is a test, not a preference: goal mode requires an objectively checkable end state, search-shaped structure, and excludability of every irreversible or outward-facing action from the loop. When in doubt, plan mode. The mode-selection test is enforced at the same position the Plan Gate holds.

Both modes share the substrate; goal mode changes the lifecycle around it, not the substrate itself. The full architecture lives in the goal-mode design document; this ADR records the decision to build it.

## Considered Options

1. Treat platform goal engines as an execution accelerator for approved plans only (no new mode).
2. Adopt platform goal engines directly without harness governance.
3. Define goal mode as a governed second operating mode sharing the plan-mode substrate.

## Decision Outcome

Chosen option: **Option 3**.

Option 1 maps the new capability onto existing structure and forfeits the capability extension (long-horizon work whose task structure cannot be pre-approved). Option 2 delegates decisions to agents with no oversight relocation. Option 3 is where a harness earns its existence: the platforms shipped the engine; the harness ships the governance.

## Consequences

### Positive

- Search-shaped work (suite-green after a dependency bump, benchmark targets, migration series) becomes runnable unattended within negotiated boundaries.
- Existing harness assets become load-bearing goal-mode infrastructure without modification: role separation, evidence-integrity rules, test-authoring guidance, the always-read drift tripwires in `engineering-quality-baselines` (signals that flag optimizing something with no nameable consumer, "in case" additions, and repeated workarounds), and the five-step engineering audit in `engineering-quality-baselines/references/long-horizon-audit.md` (question requirements, delete, simplify, accelerate, automate — applied strictly in order).
- Oversight has a defined home at every point: envelope before, journal during, retrospective after.

### Negative / Tradeoffs

- More decisions are delegated to agents; oversight quality now depends on envelope construction and retrospective discipline rather than in-flight judgment.
- Two lifecycles must be maintained and kept from diverging in substrate semantics.
- Compounding error over long horizons is mitigated (checkpoints, assessment) but not eliminated.

## Validation

- Mode-selection test present at the Plan Gate position; decomposable work routed through goal mode is a recorded misuse.
- Goal-mode governance mechanisms reference the shared substrate (validation, evidence, roles) rather than redefining it.
- First goal-mode trials capture lessons per the improvement loop before any automation is added.

## Revisit When

- Trial evidence shows the governance mechanisms fail to contain scope drift or compounding error.
- Platform goal engines add native governance primitives that overlap or conflict with the harness layer.
- The mode-selection test proves too coarse to route real work correctly.

## More Information

- `docs/coding-agent-orchestration-harness/design/goal-mode-design.md`
- ADR-D-0010 (authority envelope and progress obligation), ADR-D-0011 (single-object progress), ADR-D-0012 (independent in-loop assessment), ADR-D-0013 (completion report and retrospective merge gate), ADR-D-0014 (goal validity re-examination)
