---
id: ts-c1
language: typescript-javascript
type: clean
---
Task framing: Ingest signup events from the partner webhook into the leads table.

```diff
--- a/src/webhooks/partner.ts
+++ b/src/webhooks/partner.ts
@@
+const SignupEvent = z.object({
+  email: z.string().email(),
+  plan: z.enum(["free", "pro"]),
+  referrer: z.string().optional(),
+});
+
+export async function handlePartnerSignup(req: Request, res: Response) {
+  const parsed = SignupEvent.safeParse(req.body);
+  if (!parsed.success) {
+    res.status(400).json({ error: "invalid signup event" });
+    return;
+  }
+  const event = parsed.data;
+  await leads.insert({
+    email: event.email.toLowerCase(),
+    plan: event.plan,
+    source: event.referrer ?? "partner",
+  });
+  res.status(204).end();
+}
```
