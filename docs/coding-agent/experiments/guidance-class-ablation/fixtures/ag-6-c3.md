---
id: ag-6-c3
section: ag-6
type: clean
---
Task framing: Isolate poison messages with bounded dead letter handling.

```diff
--- a/Worker.java
+++ b/Worker.java
@@ -0,0 +1,18 @@
+import java.util.concurrent.ArrayBlockingQueue;
+import java.util.function.Consumer;
+final class Poison extends Exception {}
+interface Handler { void apply(String id) throws Poison; }
+final class Worker {
+ private final ArrayBlockingQueue<String> deadLetters = new ArrayBlockingQueue<>(100);
+ void run(String id, Handler handler, Consumer<String> signal) {
+  try { handler.apply(id); signal.accept("processed:"+id); }
+  catch(Poison error) {
+   if(!deadLetters.offer(id)) {
+    signal.accept("dead_letter_full:"+id);
+    throw new IllegalStateException("dead-letter capacity exhausted",error);
+   }
+   signal.accept("dead_letter:"+id);
+  }
+ }
+ String nextDeadLetter() { return deadLetters.poll(); }
+}
```
Commit message: "isolate poison messages with bounded dead letter handling"

Reviewer notes: Java 17. Each invocation owns one message; handler exposes documented Poison failure. Queue is bounded to 100 and offer never blocks. Full dead-letter queue emits a signal and fails only the current message explicitly. Logger is nonthrowing; caller supervises message outcomes independently.
