---
id: py-c1
language: python
type: clean
---
Task framing: Translate storage-layer errors into domain errors at the repository boundary.

```diff
--- a/repo/documents.py
+++ b/repo/documents.py
@@ def load(self, doc_id: DocumentId) -> Document:
     try:
         raw = self._bucket.get(str(doc_id))
-    except StorageError as err:
-        raise err
+    except StorageError as err:
+        raise DocumentUnavailable(doc_id) from err
     return Document.parse(raw)
```
