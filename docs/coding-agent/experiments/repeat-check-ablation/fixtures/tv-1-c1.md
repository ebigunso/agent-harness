---
id: tv-1-c1
section: tv-1
type: clean
---

Task framing:

Update `src/option_label.py` so `option_label()` returns `"on"` instead of `"off"`. No other behavior or API change is requested. The complete proposed diff is below.

The existing check `tests/test_option.py::test_option_label` takes the requested value as an input to its assertion; changing that value requires no test-code edit. `tools/check.py` is this generic project's local test runner. `CHANGE` identifies the exact candidate snapshot; `BASE` identifies its immutable pre-change parent. These labels describe the fixture project, not this repository.

All checks use local data only, with no live services or live-test gates and no failing test results. The runner may select, prepare or discover tests separately from executing them. Its logs distinguish runner stages from target-body and assertion-block events.

Commit message:

Update option_label to the requested value

```diff
diff --git a/src/option_label.py b/src/option_label.py
--- a/src/option_label.py
+++ b/src/option_label.py
@@ -1,2 +1,2 @@
 def option_label():
-    return "off"
+    return "on"
```

Reviewer notes:

The author attached the targeted execution record. A reviewer asks whether an additional targeted rerun is still needed simply to be safe.

```text
V1 $ python tools/check.py --select tests/test_option.py::test_option_label
V2 revision=CHANGE profile=local deps=lock-local exit=0
V3 target body_entries=1 assertion_blocks_completed=1 executed=1 skipped=0 failed=0
V4 assertion: option_label() == 'on' PASS; final: no skipped tests
```
