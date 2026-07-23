# Latent-Risk Review: Information Conservation

Read when the change serializes, converts, aggregates, wraps, or falls back across a boundary that carries structured data.

## Checks

1. Per-boundary conservation audit
- Every consumed field reaches the output or has a recorded intentional drop with a reason.
- Classifications retain their discriminant; collapsing distinct cases into one output value is a finding unless the collapse is contracted.

2. Reconstruction
- Breakdowns reconstruct their totals: parts must sum back to the whole they were derived from.
- Multi-failure paths capture all contributing causes order-independently, not only the first or last failure observed.

3. Fallback parity
- Fallback arms carry no less data than the primary path; a degraded arm that silently narrows the payload is a finding.

## Output

Report each lossy boundary with the dropped or collapsed data and the missing conservation evidence or intentional-drop record.
