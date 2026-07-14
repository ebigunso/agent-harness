# Persistent-Peer Dispatch (Long-Lived Agents Over an External Channel)

Read this reference ONLY when the runtime setup uses multiple long-lived agents that stay alive across dispatches and communicate over an external channel (team messaging, shared inbox). It does not apply to subagents spawned and cleaned up within a single dispatch.

## Delivery-Path Verification

- Verify the peer's delivery path is live before dispatching work over an external channel — a successful send is not delivery.
- If automatic delivery cannot be confirmed, ask the user to nudge the peer or hold the dispatch.

## Parallel-Wave Capacity

- Before dispatching a parallel wave, count live workers and spawn/request the shortfall first.

## Report Handoffs

- Verify critical report handoffs are visible in the registered store/channel the receiver actually reads before treating delivery as complete.
- Never redirect a handoff to an alternate store to bypass a write restriction.
