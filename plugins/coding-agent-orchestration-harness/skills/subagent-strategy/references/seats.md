# Seats

Read this reference when a dispatch goes to a seat: a session that another session creates to do work for it and reaches over a peer channel. A subagent the runtime starts and ends inside one dispatch is not a seat.

## A seat belongs to the session that uses it

- The session that uses a seat creates it when the work needs one and ends it when the work does not. It may keep a seat while the seat is useful and may end one at any time. Why: work that waits for a seat somebody else must start, or for the one seat to come free, waits on the machinery and not on the person.
- Nothing depends on a seat surviving. A seat may be gone when the next dispatch is due, and whether a seat that is still there holds what it saw cannot be read from outside it. Instinct goes wrong by keeping a seat for what it has seen and writing the next dispatch short on the strength of it. A kept seat may save reading; no result rests on it, and what a dispatch needs is in the dispatch and the files it names (`dispatch-checklists.md`, Every dispatch).
- Two Orchestrators never share a peer seat in the middle of a run. Why: a seat that serves two runs mixes their scope and decisions, and neither run can end it.
- How a seat is started, watched and ended is the workspace's record to say (`docs/coding-agent/rules/common.md`, Models And Peers In This Workspace, Sessions). Nothing here rests on a particular tool.

## Delivery

- A successful send is not delivery. Before work goes over a peer channel, the seat's delivery path is seen to be live. Where it cannot be seen so, the work goes to a seat whose path is live, a new one if need be; the person is not asked to wake a seat.
- A hand-off counts as delivered when it is visible in the store the receiver reads, never before.
- Never redirect a hand-off to another store to get round a write restriction.
