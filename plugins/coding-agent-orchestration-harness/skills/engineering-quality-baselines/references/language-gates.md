# Language and Technology Gates (Routing + Shared Template)

## Purpose

Use this reference to decide which language/technology guidance to load, in what order, and at what depth.

This document is intentionally routing-focused:
- It does not define repository-canonical commands.
- It does not require reading every language/tech document.
- It emphasizes progressive disclosure so review effort stays proportional to risk.

## Progressive Disclosure Model

Use the smallest sufficient depth first, then expand only when risk or uncertainty remains.

### Level 0 — Route First (always)

Identify what is actually in scope:
- Primary language(s) changed.
- Runtime/framework(s) touched.
- Nature of change (new behavior, refactor, bug fix, review-only).
- Risk profile (security, data integrity, concurrency, performance, migration impact).

Output of Level 0:
- A short list of relevant language/tech docs to read now.
- A short list of docs explicitly out of scope for this task.

### Level 1 — Core Applicable Gates (default)

Read only language/tech docs directly tied to changed code paths.

Typical minimum:
- One language gate for each language edited.
- One framework/technology gate for each framework meaningfully touched.

Stop here when:
- Acceptance criteria are fully covered.
- No unresolved high-risk area remains.

### Level 2 — Extended Gates (conditional)

Add adjacent language/tech docs only if one or more is true:
- Cross-language boundary behavior changed.
- New integration point introduced.
- Prior incidents indicate hidden risk in neighboring layers.
- Review identifies unresolved concerns after Level 1.

### Level 3 — Full Sweep (rare)

Use broad language/tech coverage only for high-impact migrations, platform changes, or systemic quality incidents.

## How to Choose Relevant Language/Tech Documents

Apply this filter sequence in order:

1. Direct modification filter
- Include docs for languages/frameworks with modified files.

2. Execution-path filter
- Include docs for languages/frameworks that execute the changed behavior, even if not directly edited.

3. Boundary filter
- Include docs for serialization, API contracts, persistence, async/job systems, auth/security, and observability when those boundaries are touched.

4. Risk amplifier filter
- Expand coverage if the change affects correctness-critical or failure-amplifying paths.

5. Exclusion declaration
- Explicitly note major language/tech docs not read and why they are out of scope.

If uncertain between two scopes, choose the smaller scope first and escalate only if evidence is insufficient.

## Shared Template for Language/Tech-Specific Docs

Use this same structure for each language or technology reference to keep navigation consistent.

### 1) Scope and Applicability
- What this doc applies to.
- What it does not cover.
- Typical triggers for loading this doc.

### 2) Core Quality Gates
- Correctness and behavior-preservation checks.
- Maintainability and complexity constraints.
- Reliability/performance expectations relevant to the language/tech.

### 3) Safety and Failure Boundaries
- Input/state boundary checks.
- Security-sensitive patterns to verify.
- Failure modes and containment expectations.

### 4) Validation Expectations (Generic)
- What to validate conceptually for this language/tech.
- What evidence is expected to show confidence.
- Explicit reminder that repository-local docs define canonical required commands.

### 5) Review Prompts
- Short prompts that help reviewers detect common regressions quickly.
- Escalation prompts for high-risk findings.

### 6) Common Anti-Patterns
- Frequent mistakes that lower quality or create hidden risk.
- What to do instead.

## Routing Output Format (Recommended)

For each task, produce a small routing note:
- In-scope language/tech docs.
- Out-of-scope docs with reasons.
- Progressive disclosure level selected (0/1/2/3).
- Escalation trigger(s) that would require moving to the next level.

This keeps routing decisions explicit, reviewable, and proportional.

## Neutrality and Precedence

- This reference defines selection logic and structure, not repository policy.
- Repository-local documents remain canonical for required validations and exact command-level gates.
