### 9) Make Failure Modes Explicit and Safe

- Handle errors at appropriate boundaries with useful context.
- Avoid swallowing failures or converting them into ambiguous states.
- Design fallback behavior to be safe, observable, and bounded.

Review checks:
- Are failure paths visible and diagnosable?
- Do fallbacks preserve safety and correctness expectations?
