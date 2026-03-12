# Provenance Governance

Use this when deciding whether a skill is safe and in scope to edit directly.

## Default edit policy

- First-party skills in this repository may be maintained directly when they are inside task scope.
- Third-party, upstream, vendored, or unknown-provenance skills are read-only by default.
- Edit those skills only when the user explicitly approves that exact change target.
- If governance is needed without approval, create or update a first-party wrapper skill instead of mutating the original.

## Unknown-provenance signals

- External license files or upstream packaging metadata indicate the skill may be imported or mirrored.
- Directory layout or bundled assets look copied from an upstream source.
- Repository ownership history for the skill is unclear.
- The skill is treated operationally like a dependency rather than a maintained first-party asset.

## Response pattern when provenance blocks direct edits

1. State that the skill is read-only by default.
2. Propose a first-party wrapper skill or local rule as the landing spot.
3. Escalate only if the user wants direct edits and explicitly approves that scope.
