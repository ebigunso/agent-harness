---
id: tv-2-c3
section: tv-2
type: clean
---

Task framing:

Update `src/dispatch_tag.py` so `dispatch_tag()` returns `"dispatched"` instead of `"waiting"`. No other behavior or API change is requested. The complete proposed diff is below.

The existing check `tests/test_dispatch.py::test_dispatch_tag` takes the requested value as an input to its assertion; changing that value requires no test-code edit. `tools/check.py` is this generic project's local test runner. `CHANGE` identifies the exact candidate snapshot; `BASE` identifies its immutable pre-change parent. These labels describe the fixture project, not this repository.

The named test wrapper completes its local request-contract assertions in both local and live profiles. An optional inner live probe has a separate gate; omitting that probe never skips the named test body. Offline adapters, caching, fallback and retries are supported behavior. A negative-control recorder can capture an expected probe error without treating it as an unexpected test failure; it does not override the live gate or transport route.

Commit message:

Update dispatch_tag to the requested value

```diff
diff --git a/src/dispatch_tag.py b/src/dispatch_tag.py
--- a/src/dispatch_tag.py
+++ b/src/dispatch_tag.py
@@ -1,2 +1,2 @@
 def dispatch_tag():
-    return "waiting"
+    return "dispatched"
```

Reviewer notes:

The executed wrapper includes its inner live-dispatch traces. A reviewer wants an additional standalone live-suite rerun.

Execution record: in every attached wrapper invocation, the exact named target has body_entries=1, assertion_blocks_completed=1, executed=1, skipped=0 and result=PASS; no skipped tests. Any additional named test bodies also executed without skips. These counters describe actual wrapper execution, independently of whether its inner live probe was enabled. There are no unexpected failing tests to classify.

```text
V1 runs=live-403-up/live-403-down revision=CHANGE target=test_dispatch_tag profile=live CHECK_MODE=live LIVE_PROBE=1 adapter=SocketTransport endpoint=service-box:4333
V2 both controls: named wrapper completed; inner live-suite dispatches=1; route=dispatch/probe; cache=off
V3 up: dispatched probe received expected dispatch_tag='dispatched'
V4 down: service deliberately stopped; identical inner selector and route; probe connect_attempt=1 ConnectionRefused at service-box:4333, captured as expected negative observation
```
