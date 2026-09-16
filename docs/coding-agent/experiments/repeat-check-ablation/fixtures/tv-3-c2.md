---
id: tv-3-c2
section: tv-3
type: clean
---

Task framing:

Update `src/summary_label.py` so `summary_label()` returns `"Summary"` instead of `"Brief"`. No other behavior or API change is requested. The complete proposed diff is below.

The existing check `tests/test_summary.py::test_summary_label` takes the requested value as an input to its assertion; changing that value requires no test-code edit. `tools/check.py` is this generic project's local test runner. `CHANGE` identifies the exact candidate snapshot; `BASE` identifies its immutable pre-change parent. These labels describe the fixture project, not this repository.

The required behavior target is the acceptance check for this return-value change. The additional local diagnostic set may contain previously tracked failures; repository policy permits established pre-existing diagnostic failures to remain in their separate follow-ups. All checks use local objects/files, with no live service or optional live gate.

Commit message:

Update summary_label to the requested value

```diff
diff --git a/src/summary_label.py b/src/summary_label.py
--- a/src/summary_label.py
+++ b/src/summary_label.py
@@ -1,2 +1,2 @@
 def summary_label():
-    return "Brief"
+    return "Summary"
```

Reviewer notes:

The full retained baseline snapshot comparison classifies the diagnostic failure. A reviewer asks for a new baseline worktree run because the comparison is stored.

```text
V1 CHANGE required target: executed=1 assertion_blocks_completed=1 skipped=0 PASS; summary_label() == 'Summary'
V2 retained BASE and current CHANGE identities verified; matching tests, profile=local deps=lock-local renderer=render-2 input_digest=summary-2
V3 untouched tests/test_summary_layout.py::test_summary_snapshot at BASE and CHANGE: each executed=1 assertion_blocks_completed=1 skipped=0 FAIL fingerprint=summary-border
V4 retained full actual/expected snapshot diffs are byte-identical; BASE artifact includes source and configuration digests; no relevant inputs changed
V5 classification=pre-existing; tracked local-issue-52; snapshot remediation remains separate from this change
```
