# Seats

Read this reference when the relay a dispatch goes by is a peer channel: the work goes to a session, here called a seat, that is reached by messages in a store both sides read. What holds for a dispatch by any relay is in `SKILL.md` (Core rule 6) and `dispatch-checklists.md` (Every dispatch); this reference holds only what the channel adds. How a seat is started, watched and ended is the workspace's record to say (`docs/coding-agent/rules/common.md`, Models And Peers In This Workspace, Sessions), and nothing here rests on a particular tool.

## Delivery

- A successful send is not delivery. Before work goes over a peer channel, the seat's delivery path is seen to be live. Where it cannot be seen so, the work goes by a relay whose path is live; the person is not asked to wake a seat.
- A hand-off counts as delivered when it is visible in the store the receiver reads, never before.
- Never redirect a hand-off to another store to get round a write restriction.

## One identity

- A session holds one identity on a peer channel and reads what another session was sent without taking that session's identity; a dispatch that asks for such a read says how. Why: a session that joins under another's name to see its inbox sends under a name that is not its own.
