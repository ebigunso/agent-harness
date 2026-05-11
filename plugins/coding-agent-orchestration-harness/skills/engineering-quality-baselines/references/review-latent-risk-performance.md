# Latent-Risk Review: Hot Path Cost

Read when loops touch potentially growing data, hot paths change, expensive work may repeat, locks are involved, or network/database/API calls appear in iterative code.

## Checks

Inside loops over potentially growing data, flag:
- scans
- sorts
- allocations
- network calls
- database calls
- blocking calls
- tracing/log payload construction when disabled
- lock-held expensive work

Check whether work can be moved out of the loop, cached safely, batched, streamed, indexed, or guarded.

## Output

Report only costs that scale with data size, call frequency, or contention.
