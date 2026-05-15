# Latent-Risk Review: Public API Compatibility

Read when public or semi-public API surface, exports, re-exports, prelude/crate-root visibility, docs/examples, feature-gated public items, or downstream-facing DTOs change.

## Checks

1. Compatibility surface
- Identify every public, semi-public, documented, generated, exported, or downstream-facing symbol affected by the change.
- Check call signatures, defaults, field names, enum variants, serialization shape, feature gates, and documented examples.

2. Downstream migration
- Flag removals, renames, stricter inputs, broader outputs, changed error types, or changed feature requirements unless migration guidance or compatibility handling exists.
- Check whether docs and examples compile or remain accurate where the repository validates them.

3. Visibility drift
- Watch for accidental exports, re-exports, prelude additions, crate-root visibility changes, or DTO fields that become part of a contract unintentionally.

Also check:
- public struct field additions that may break downstream struct literals
- public enum variant or field changes that may break exhaustive matches
- public trait required item additions that may break downstream impls
- function arity, generic bounds, return type, error type, or feature availability changes
- constructor, builder, accessor, private-field, or `non_exhaustive` strategy for public types expected to grow
- crate-root, prelude, module, generated-doc, and example import consistency

## Output

Report only compatibility risks with an affected symbol, path, or downstream contract.
