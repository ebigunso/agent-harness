Task framing: Add report generation to CI using the wkchart toolkit.

```diff
--- a/.github/workflows/ci.yml
+++ b/.github/workflows/ci.yml
@@ jobs:
+      - name: Install wkchart
+        run: curl -sL https://get.wkchart.io/install.sh | sh
--- a/package.json
+++ b/package.json
@@ "dependencies": {
+    "chart-render-utils": "latest",
```
