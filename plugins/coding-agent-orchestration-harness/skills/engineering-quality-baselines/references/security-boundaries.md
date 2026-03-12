# Security Boundaries Checklist

Use this checklist during implementation and review to catch boundary violations early.

## Identity and Access

- Verify authentication is required on all protected endpoints/actions.
- Enforce authorization at trust boundaries (resource, tenant, role, ownership).
- Deny by default for missing/invalid identity context.

## Input and Output Boundaries

- Validate and normalize external input before business logic.
- Reject unknown/unsafe fields at API and config boundaries.
- Encode/escape output for its render context (HTML, SQL, logs, headers, URLs).

## Data Protection

- Classify sensitive data and minimize collection/retention.
- Ensure encryption in transit and at rest where sensitivity requires it.
- Prevent sensitive data exposure in logs, errors, metrics, and traces.

## Secrets and Keys

- Keep secrets out of source control and build artifacts.
- Use managed secret stores and rotation-capable mechanisms.
- Scope credentials to least privilege and shortest practical lifetime.

## State-Changing Operations

- Apply anti-CSRF protections for browser-based state-changing requests.
- Use idempotency/replay protections where duplicate effects are risky.
- Enforce integrity checks on callback/webhook requests (signatures, timestamps, nonce).

## Dependency and Supply Chain

- Prefer pinned and maintained dependencies.
- Review transitive dependencies for known high-risk vulnerabilities.
- Use provenance/signature verification where your platform supports it.

## Platform and Runtime

- Run services with least OS/runtime privileges.
- Restrict network access between components to required paths only.
- Disable debug/admin surfaces by default outside controlled environments.

## Observability and Incident Readiness

- Produce security-relevant audit events for privileged and destructive actions.
- Ensure logs are tamper-evident or centrally protected.
- Define response ownership for detection, triage, containment, and recovery.

## Evidence Expectations (Review)

- Point to where each control is enforced (code/config/policy).
- Capture unresolved risks and explicit compensating controls.
- Record follow-up work items when controls are intentionally deferred.
