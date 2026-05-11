# Latent-Risk Review: Future-Edit Brittleness and Dead Surface

Read when the change adds public/internal API surface, abstractions, enum handling, positional lists, switch/default logic, test-only hooks, or speculative extension points.

## Checks

1. Brittleness against future edits
Look for:
- positional coupling
- duplicated lists
- tests coupled by index
- switch statements without future-proof defaults
- APIs relying on undocumented call ordering
- assumptions that only hold for today's enum variants, list lengths, call sites, or tests

2. Dead or aspirational code
Flag:
- unused abstractions
- unused public/internal APIs
- dead branches
- speculative extension points
- test-only production code

Allow these only when there is a current caller or explicit lifecycle/rationale.

## Output

Distinguish between harmless unused local code and production API surface that creates maintenance cost.
