---
id: cp-9-c3
section: cp-9
type: clean
---
Task framing: Let an optional thumbnail fail visibly while a successfully stored upload remains usable.

```diff
--- a/src/upload.rs
+++ b/src/upload.rs
@@ -1,5 +1,11 @@
 fn upload(file: &File, store: &Store) -> Result<UploadResult, StoreError> {
     let id = store.save(file)?;
-    let thumbnail = thumbnails::create(file)?;
-    Ok(UploadResult { id, thumbnail: Some(thumbnail), warning: None })
+    let (thumbnail, warning) = match thumbnails::create(file) {
+        Ok(image) => (Some(image), None),
+        Err(error) => {
+            log::warn!("thumbnail unavailable for {}: {}", id, error);
+            (None, Some(UploadWarning::ThumbnailUnavailable))
+        }
+    };
+    Ok(UploadResult { id, thumbnail, warning })
 }
```
Commit message: "report optional thumbnail degradation"

Reviewer notes: UploadResult includes Option<Thumbnail> and Option<UploadWarning>; this is the published contract. thumbnails::create returns StoreError, is bounded to 2 seconds, cleans up temporary files and logs no secrets. File scanning/validation precedes upload and remains mandatory. Clients display the warning and original file; upload errors still propagate.
