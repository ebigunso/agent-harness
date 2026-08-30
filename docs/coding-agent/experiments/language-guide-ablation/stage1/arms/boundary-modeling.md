# Boundary modeling review checklist (arm D — cross-language)

Models reliably check language mechanics on their own. These are the checks they do not
make unprompted. Apply them to any non-trivial change, in any language.

- Domain rules stay out of transport handlers (HTTP routes, CLI entry points, message
  consumers). A handler parses, delegates to the domain layer, and renders — nothing else.
- Pure logic is separated from I/O so the logic is deterministically testable without
  fakes for the world.
- Domain concepts get domain types: no raw strings/ints for ids, money, quantities, or
  states, and no untyped dict/map/object bags crossing a layer boundary.
- Make invalid states unrepresentable: model multi-state results as closed unions/enums,
  not flat all-optional shapes; let the compiler or schema reject the impossible.
- State logic switches exhaustively over the closed set of variants — never through
  fall-through conditionals that silently absorb a future variant.
- Validate untrusted input at first entry and fail closed BEFORE any side effect runs;
  a write that precedes validation is a defect even when the happy path works.
- One executable source of truth per contract (schema, types package); a hand-copied
  duplicate with a "keep in sync" comment is a defect.
- Packages/modules stay cohesive with intentional, acyclic dependency direction; no
  utility dumping grounds, no reaching across boundaries.
