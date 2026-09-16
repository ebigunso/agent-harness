---
id: tv-1-c4
section: tv-1
type: clean
---

Task framing:

Update `src/footer_label.py` so `footer_label()` returns `"Done"` instead of `"End"`. No other behavior or API change is requested. The complete proposed diff is below.

The existing check `tests/test_footer.py::test_footer_label` takes the requested value as an input to its assertion; changing that value requires no test-code edit. `tools/check.py` is this generic project's local test runner. `CHANGE` identifies the exact candidate snapshot; `BASE` identifies its immutable pre-change parent. These labels describe the fixture project, not this repository.

All checks use local data only, with no live services or live-test gates and no failing test results. The runner may select, prepare or discover tests separately from executing them. Its logs distinguish runner stages from target-body and assertion-block events.

Commit message:

Update footer_label to the requested value

```diff
diff --git a/src/footer_label.py b/src/footer_label.py
--- a/src/footer_label.py
+++ b/src/footer_label.py
@@ -1,2 +1,2 @@
 def footer_label():
-    return "End"
+    return "Done"
```

Reviewer notes:

The validation artifact from an earlier run of this exact candidate is retained in full. A reviewer wants a fresh rerun because the artifact is stored.

```text
V1 retained command: python tools/check.py --select tests/test_footer.py::test_footer_label
V2 recorded revision=CHANGE current revision=CHANGE; recorded/current profile=local deps=lock-local; identical target file digest
V3 event: test_footer_label body_entered; asserted footer_label() == 'Done'; assertion_completed PASS
V4 recorded target executed=1 skipped=0 failed=0; no skipped tests
V5 source, test files, configuration and dependency lock have not changed since the recorded run
```
