---
id: tv-1-c2
section: tv-1
type: clean
---

Task framing:

Update `src/header_label.py` so `header_label()` returns `"Begin"` instead of `"Start"`. No other behavior or API change is requested. The complete proposed diff is below.

The existing check `tests/test_header.py::test_header_label` takes the requested value as an input to its assertion; changing that value requires no test-code edit. `tools/check.py` is this generic project's local test runner. `CHANGE` identifies the exact candidate snapshot; `BASE` identifies its immutable pre-change parent. These labels describe the fixture project, not this repository.

All checks use local data only, with no live services or live-test gates and no failing test results. The runner may select, prepare or discover tests separately from executing them. Its logs distinguish runner stages from target-body and assertion-block events.

Commit message:

Update header_label to the requested value

```diff
diff --git a/src/header_label.py b/src/header_label.py
--- a/src/header_label.py
+++ b/src/header_label.py
@@ -1,2 +1,2 @@
 def header_label():
-    return "Start"
+    return "Begin"
```

Reviewer notes:

The author used a full local suite. A reviewer asks to rerun the target separately even though the per-target record is included.

```text
V1 $ python tools/check.py --suite local --events events-202.log
V2 revision=CHANGE profile=local deps=lock-local exit=0
V3 suite executed=14 skipped=0 failed=0
V4 events-202.log: tests/test_header.py::test_header_label body_entries=1 assertion_blocks_completed=1 PASS
V5 asserted header_label() == 'Begin'; target skipped=0
```
