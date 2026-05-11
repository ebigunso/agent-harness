# Latent-Risk Review: Contract Consistency and Scope Boundaries

Read when two or more paths claim to implement the same contract, or logic depends on user/request/tenant/root/config/cache scope.

## Checks

1. Semantic consistency across implementations
Compare edge-case behavior, not just type signatures, across:
- fake vs production
- client vs server validation
- sync vs async
- batch vs single-item
- cache vs database
- old API vs new API
- fallback vs primary path

2. Scope leakage
For every policy, config, cache, authorization decision, or derived rule:
- identify its intended scope
- verify it is not applied outside that scope
- check user-specific rules, tenant-specific config, request-local cache, root-node policy, and test-only assumptions.

## Output

Report any divergence in behavior or scope as a concrete contract/scope issue.
