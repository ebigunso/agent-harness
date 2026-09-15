# Repeat-check fixture authoring plan

Frozen revision: 76434f6e0b45360412c073d8fd02eb86161dcffe

Author exactly one diff and validation-summary fixture for each slot below. Each fixture has YAML frontmatter id, section, type; Task framing:, Commit message:, Reviewer notes:, and a syntactically valid fenced diff. Keys name the exact evidence gap, its location, at least two adequate ways to obtain the missing evidence, and acceptable optional nitpicks. A plant targets exactly one section; decoys explicitly settle that section and invite a redundant rerun. Follow protocol.md for grading and immutable arm texts. No actual fixture or key is authored in this task.

## tv-1

Invariant: - Specific-test evidence must show executed, unskipped tests.

Exact source check: - Skip-capable tests can report green with unexecuted bodies: when specific-test evidence matters, rerun it targeted and confirm no skip message

| Fixture | Type | Registered evidence scenario |
|---|---|---|
| tv-1-01 | planted | Skipped target in green suite; evidence is inconclusive, and the key requires closing that gap by adequate means. |
| tv-1-02 | planted | All selected tests skipped; evidence is inconclusive, and the key requires closing that gap by adequate means. |
| tv-1-03 | planted | Zero selected tests; evidence is inconclusive, and the key requires closing that gap by adequate means. |
| tv-1-04 | planted | Conditional early return; evidence is inconclusive, and the key requires closing that gap by adequate means. |
| tv-1-05 | planted | Only unrelated tests counted; evidence is inconclusive, and the key requires closing that gap by adequate means. |
| tv-1-06 | planted | Discovery count mistaken for execution; evidence is inconclusive, and the key requires closing that gap by adequate means. |
| tv-1-07 | planted | Setup-only success; evidence is inconclusive, and the key requires closing that gap by adequate means. |
| tv-1-08 | planted | Truncated skip summary; evidence is inconclusive, and the key requires closing that gap by adequate means. |
| tv-1-09 | planted | Cached green summary without execution counts; evidence is inconclusive, and the key requires closing that gap by adequate means. |
| tv-1-10 | planted | Platform exclusion of target; evidence is inconclusive, and the key requires closing that gap by adequate means. |
| tv-1-11 | planted | Disabled parameterized target; evidence is inconclusive, and the key requires closing that gap by adequate means. |
| tv-1-12 | planted | Aggregate hides target skip; evidence is inconclusive, and the key requires closing that gap by adequate means. |
| tv-1-c1 | clean | Conclusive variant 1: positive executed-test counts and no-skip output for the target; another run is unnecessary. |
| tv-1-c2 | clean | Conclusive variant 2: positive executed-test counts and no-skip output for the target; another run is unnecessary. |
| tv-1-c3 | clean | Conclusive variant 3: positive executed-test counts and no-skip output for the target; another run is unnecessary. |
| tv-1-c4 | clean | Conclusive variant 4: positive executed-test counts and no-skip output for the target; another run is unnecessary. |

## tv-2

Invariant: - Gated live tests require negative evidence when the gate could be off.

Exact source check: verify gated live tests once with the service deliberately down.

| Fixture | Type | Registered evidence scenario |
|---|---|---|
| tv-2-01 | planted | Unreported environment gate; evidence is inconclusive, and the key requires closing that gap by adequate means. |
| tv-2-02 | planted | Missing credentials gate; evidence is inconclusive, and the key requires closing that gap by adequate means. |
| tv-2-03 | planted | Optional-service skip; evidence is inconclusive, and the key requires closing that gap by adequate means. |
| tv-2-04 | planted | Always-green offline fallback; evidence is inconclusive, and the key requires closing that gap by adequate means. |
| tv-2-05 | planted | Wrong endpoint gate; evidence is inconclusive, and the key requires closing that gap by adequate means. |
| tv-2-06 | planted | Cached response mistaken for live evidence; evidence is inconclusive, and the key requires closing that gap by adequate means. |
| tv-2-07 | planted | Dependency injection bypass; evidence is inconclusive, and the key requires closing that gap by adequate means. |
| tv-2-08 | planted | Conditional live-suite selector; evidence is inconclusive, and the key requires closing that gap by adequate means. |
| tv-2-09 | planted | Health check without test negative evidence; evidence is inconclusive, and the key requires closing that gap by adequate means. |
| tv-2-10 | planted | Recorded run without gate identity; evidence is inconclusive, and the key requires closing that gap by adequate means. |
| tv-2-11 | planted | Retry masks unavailable service; evidence is inconclusive, and the key requires closing that gap by adequate means. |
| tv-2-12 | planted | Aggregate hides gated test; evidence is inconclusive, and the key requires closing that gap by adequate means. |
| tv-2-c1 | clean | Conclusive variant 1: gate identity and negative evidence proving the live test executes with the service down; another run is unnecessary. |
| tv-2-c2 | clean | Conclusive variant 2: gate identity and negative evidence proving the live test executes with the service down; another run is unnecessary. |
| tv-2-c3 | clean | Conclusive variant 3: gate identity and negative evidence proving the live test executes with the service down; another run is unnecessary. |
| tv-2-c4 | clean | Conclusive variant 4: gate identity and negative evidence proving the live test executes with the service down; another run is unnecessary. |

## tv-3

Invariant: - Classify failures in untouched tests as pre-existing or regression before remediation.

Exact source check: - When validation fails in tests the change did not touch, rerun against baseline HEAD (stash/worktree) to classify pre-existing vs regression before remediating.

| Fixture | Type | Registered evidence scenario |
|---|---|---|
| tv-3-01 | planted | Untouched unit failure without baseline; evidence is inconclusive, and the key requires closing that gap by adequate means. |
| tv-3-02 | planted | Unchanged integration failure; evidence is inconclusive, and the key requires closing that gap by adequate means. |
| tv-3-03 | planted | Snapshot failure without comparison; evidence is inconclusive, and the key requires closing that gap by adequate means. |
| tv-3-04 | planted | Platform test failure without baseline; evidence is inconclusive, and the key requires closing that gap by adequate means. |
| tv-3-05 | planted | Order-sensitive failure without classification; evidence is inconclusive, and the key requires closing that gap by adequate means. |
| tv-3-06 | planted | Time-dependent failure without comparison; evidence is inconclusive, and the key requires closing that gap by adequate means. |
| tv-3-07 | planted | Dependency/config identity unspecified in baseline claim; evidence is inconclusive, and the key requires closing that gap by adequate means. |
| tv-3-08 | planted | Historical failure anecdote without evidence; evidence is inconclusive, and the key requires closing that gap by adequate means. |
| tv-3-09 | planted | Cached baseline summary unlinked to revision; evidence is inconclusive, and the key requires closing that gap by adequate means. |
| tv-3-10 | planted | Intermittent failure without classification; evidence is inconclusive, and the key requires closing that gap by adequate means. |
| tv-3-11 | planted | Untouched generated-fixture failure; evidence is inconclusive, and the key requires closing that gap by adequate means. |
| tv-3-12 | planted | Failure attributed to environment without baseline; evidence is inconclusive, and the key requires closing that gap by adequate means. |
| tv-3-c1 | clean | Conclusive variant 1: baseline comparison identifying pre-existing failure or regression before remediation; another run is unnecessary. |
| tv-3-c2 | clean | Conclusive variant 2: baseline comparison identifying pre-existing failure or regression before remediation; another run is unnecessary. |
| tv-3-c3 | clean | Conclusive variant 3: baseline comparison identifying pre-existing failure or regression before remediation; another run is unnecessary. |
| tv-3-c4 | clean | Conclusive variant 4: baseline comparison identifying pre-existing failure or regression before remediation; another run is unnecessary. |
