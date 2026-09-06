# Validation Strictness

The harness validates contracts and completion state strictly while keeping execution strategy and prose flexible.

Default runtime-facing mode is `balanced`.

## Hard rules

Block progression.

Examples:

- malformed plan/task contract;
- missing validation owner;
- any `SKILL.md` Validation Gate or Completion Closeout Gate condition unmet at the point of marking `done`;
- malformed Worker YAML report;
- unsafe shared-state Git mutation;
- waiver evidence that does not follow the Canonical Required-Check Waiver Template in `engineering-quality-baselines/references/testing-validation.md`.

## Soft rules

Require explanation, waiver, or follow-up.

Examples:

- Worker touched files outside `owns` but reported and justified it;
- optional validation was skipped with a reason;
- plan decomposition changed during execution and needs a Decision Log entry;
- Reviewer found non-blocking maintainability concerns that should be tracked.

## Advisory rules

Warn only.

Examples:

- exact prose style;
- task decomposition aesthetics;
- prompt wording;
- non-critical optional validations;
- adapter wording differences that preserve shared semantics.

## Mode Guidance

- `strict`: hard-fail hard rules and elevate selected soft rules when release or governance risk is high.
- `balanced`: hard-fail malformed contracts and missing required evidence; warn on subjective quality or uncertain heuristics.
- `relaxed`: report issues without blocking except for unsafe or clearly malformed critical contracts.
