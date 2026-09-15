---
id: tv-3-c1
section: tv-3
type: clean
---

Task framing:

Update `src/count_limit.py` so `count_limit()` returns `5` instead of `4`. No other behavior or API change is requested. The complete proposed diff is below.

The existing check `tests/test_count.py::test_count_limit` takes the requested value as an input to its assertion; changing that value requires no test-code edit. `tools/check.py` is this generic project's local test runner. `CHANGE` identifies the exact candidate snapshot; `BASE` identifies its immutable pre-change parent. These labels describe the fixture project, not this repository.

The required behavior target is the acceptance check for this return-value change. The additional local diagnostic set may contain previously tracked failures; repository policy permits established pre-existing diagnostic failures to remain in their separate follow-ups. All checks use local objects/files, with no live service or optional live gate.

Commit message:

Update count_limit to the requested value

```diff
diff --git a/src/count_limit.py b/src/count_limit.py
--- a/src/count_limit.py
+++ b/src/count_limit.py
@@ -1,2 +1,2 @@
 def count_limit():
-    return 4
+    return 5
```

Reviewer notes:

The untouched diagnostic failure has already been classified as pre-existing and filed in the existing follow-up. A reviewer suggests rerunning it at baseline again before accepting this scoped change.

```text
V1 CHANGE required target: executed=1 assertion_blocks_completed=1 skipped=0 PASS; count_limit() == 5
V2 BASE and CHANGE: same profile=local deps=lock-local input_digest=count-1 platform=local-a
V3 untouched tests/test_count_view.py::test_count_layout at BASE: executed=1 assertion_blocks_completed=1 skipped=0 FAIL fingerprint=count-spacing
V4 same target at CHANGE: executed=1 assertion_blocks_completed=1 skipped=0 FAIL fingerprint=count-spacing; full actual/expected output identical
V5 classification=pre-existing based on V2-V4; follow-up=local-issue-51; no remediation to that diagnostic check in this change
```
