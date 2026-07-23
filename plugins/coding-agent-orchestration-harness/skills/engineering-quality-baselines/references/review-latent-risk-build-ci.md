# Latent-Risk Review: Build, Features, and Strict CI

Read when the change touches cfgs, feature flags, test-only paths, platform-specific code, imports, lints, docs, examples, warning-sensitive code, or CI/build-sensitive behavior.

## Checks

1. Feature and cfg parity
- Check that feature-gated, platform-specific, and test-only paths compile or are intentionally excluded.
- Verify equivalent behavior across enabled/disabled features when the public contract claims parity.

2. Strict CI hygiene
- Look for unused imports, dead cfg branches, doc warnings, generated-code drift, examples that no longer compile, and warnings-as-errors failures.
- Confirm tests exercise the relevant feature/cfg combination when risk is meaningful.
- Resolve any moving external dependency (branch, tag, "latest") to one immutable revision before CI fan-out, so every job in the run builds against the same revision.

3. Build intent
- Distinguish intentional admission of a new entrypoint, feature, or target from accidental exposure through broad cfg or manifest changes.

Tests must exercise behavior that is compiled and reachable in the intended runtime configuration.

Watch for:
- `#[cfg(test)]` variants or branches that make rejection/fallback behavior test-only
- mock-only paths that do not exist in production
- debug-only behavior relied on by tests
- feature-gated public items that disappear under common feature combinations
- platform cfgs that make the tested path differ from the deployed path

## Output

Report build or CI risks with the affected feature, cfg, target, lint, doc, or example path.
