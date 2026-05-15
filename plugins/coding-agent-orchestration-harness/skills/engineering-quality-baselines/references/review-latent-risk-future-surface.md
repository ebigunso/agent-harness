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

3. Abstraction value and searchability
- Check whether a new abstraction removes real complexity or only hides simple logic behind a harder-to-search layer.
- Prefer names and locations that future maintainers can find from domain terms, public API names, errors, and call sites.

4. Canonical policy path

Identify the constructor, validator, helper, error builder, or policy function that owns the domain decision.

New code should route through that owner unless intentionally defining a new boundary.

Flag bypasses through:
- direct construction
- duplicated matching
- local constants
- parallel validation
- direct error construction that bypasses common metadata

Bypasses are acceptable only when the change documents why the existing owner is not appropriate.

## Output

Distinguish between harmless unused local code and production API surface that creates maintenance cost.
