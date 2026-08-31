Task framing: Tag each incoming log line with the product category it mentions.

```diff
--- a/pipeline/tagger.py
+++ b/pipeline/tagger.py
@@ def tag_lines(lines, catalog):
     out = []
     for line in lines:
+        pattern = re.compile("|".join(re.escape(p.name) for p in catalog))
+        ranked = sorted(catalog, key=lambda p: -len(p.name))
+        m = pattern.search(line)
+        if m:
+            out.append((line, next(p for p in ranked if p.name == m.group(0))))
+        else:
+            out.append((line, None))
     return out
```
Note: `lines` batches are ~1M entries; `catalog` is stable across a batch.
