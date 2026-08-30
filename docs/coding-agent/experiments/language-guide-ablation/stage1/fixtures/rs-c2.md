---
id: rs-c2
language: rust
type: clean
---
Task framing: Read the deploy target from the manifest and hand it to the rollout planner.

```diff
--- a/src/rollout/manifest.rs
+++ b/src/rollout/manifest.rs
@@ pub fn deploy_target(manifest: &Manifest) -> Result<Region, ManifestError> {
     manifest
         .metadata
         .get("region")
         .ok_or(ManifestError::MissingField("region"))
-        .and_then(|r| Region::parse(r))
+        .and_then(|r| Region::parse(r).map_err(ManifestError::BadRegion))
 }
```
