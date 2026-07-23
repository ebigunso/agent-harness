# Durable-docs authoring rules

Rules for writing and restructuring durable documentation: product/strategy/policy/roadmap docs, philosophy or capability-boundary write-ups, and ADR-adjacent prose intended to stay accurate over time.

## Before drafting

1) Freeze capability-class terminology
- Define the capability-class terminology explicitly before writing (e.g., LLM-driven behavior vs deterministic automation vs internal agent workflow).
- Avoid ambiguous umbrella terms ("assistant", "automation", "the system") unless they are defined near the top of the document; otherwise use the specific term.
- Make the boundary between nearby capability classes explicit wherever the document depends on it.

2) Assign document roles before writing
- Decide which document owns philosophy/aspirations, which owns milestone sequencing, and which owns capability boundaries — before drafting prose.
- Do not let large abstraction jumps collapse into one memo; if aspirations, milestones, and boundary rules all need expression, split the documents first.

3) Identify the governing claim and top ideas first
- For each document, identify the one governing claim and the two or three highest-priority ideas a skimming reader must retain.
- Structure the document so those appear before peer lists, support tables, or companion-routing detail.

## While writing

4) Freshness semantics for time-relative language
- Durable docs that use time-relative language ("today", "current", "now") must carry explicit freshness metadata (e.g., last-updated) or dated snapshot framing.
- Remove or date-anchor any unqualified time-relative wording; readers must be able to distinguish durable principles from dated state observations.

5) Durable actors, not session-relative ones
- Persisted documents speak in durable roles (deciders, reviewers, maintainers) or named people, never session-relative vocabulary — "the user" assumes a single human authoring via an agent and turns ambiguous the moment more people are involved.

6) Tier support material; no flat peer lists
- Do not give every idea equal visual and rhetorical weight. Section structure should mirror message priority, not topic inventory.
- Group long lists (roughly 5+ items) into tiers — foundational / supporting / later-stage — or subordinate them under the primary idea; move second-order detail to companion docs.

7) Fix misleading names instead of disclaiming them
- If a document needs a sentence explaining why its filename or title should not be taken literally, treat that as a defect signal: rename or restructure instead of preserving the mismatch with disclaimer prose.
- When renaming, update live and historical references to the canonical path and remove the defensive disclaimer.

## Before finalizing

8) Coherence and emphasis check
- First screen: does the opening screen show the main story (governing claim plus top ideas), not a flat inventory?
- Agreement: do title, filename, metadata role, and opening paragraph all describe the same document role? If they disagree, resolve the mismatch — do not document around it.
- Sweep for time-relative words and session-relative actor words ("the user") and confirm each is durable by role, named, or explicitly date-anchored.
