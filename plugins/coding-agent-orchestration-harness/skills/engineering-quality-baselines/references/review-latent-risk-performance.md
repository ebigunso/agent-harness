# Latent-Risk Review: Hot Path Cost

Read when loops touch potentially growing data, hot paths change, expensive work may repeat, locks are involved, async runtime compatibility may be affected, or network/database/API calls appear in iterative code.

## Checks

Inside loops over potentially growing data, flag:
- scans
- sorts
- allocations
- network calls
- database calls
- blocking calls
- async runtime blocking or executor starvation
- tracing/log payload construction when disabled
- lock-held expensive work

Check whether work can be moved out of the loop, cached safely, batched, streamed, indexed, guarded, made async-compatible, or moved outside lock-held sections.

## Output

Report only costs that scale with data size, call frequency, or contention.
