# Sessions In This Workspace

How a session is started, messaged, watched and ended in this workspace. Only a session that does one of these reads it: Counsel and the Orchestrator. As of 2026-11-20. What was seen, how often, and what was not tried is kept with the evidence, in `docs/coding-agent/sessions-evidence.md`; an instruction here says what to do, not how well it is supported.

- To start a session in a role with a first message and without a person: use Claude Code's background option, naming the plugin's Orchestrator agent, with the message as its argument.
  - Only in a folder the owner has trusted once in Claude Code. Trust does not carry to a sibling folder or a new working tree; where the work is in such a place, start the session in a trusted working tree and name the other repository to it by path.
  - Only where the plugin is enabled.
  - There is no means here to start a session in Codex that outlives its turn. Trial runs in Codex are not kept, as this workspace's own restriction.
- To start it on a named model and at a named effort: give the same command its option naming the model and its option naming the effort level. Name both; a start that names neither runs on what the owner's settings give.
- To see what a session runs on: read the header of the runtime's log for it while it lives, or its transcript file, found by its full session id. Do not take it from the listing of sessions, which does not show it, nor from the session's own word.
- To see whether a session is alive, and working or waiting: read Claude Code's listing of sessions, which gives working, waiting with the kind of thing waited for, finished its turn, or stopped. Read what it waits for from what it last wrote. There is no means here to tell a session working long from one that is stuck.
- To give a session a further message:
  - While it works: over agmsg, where the session holds a seat in the team. A started session holds none unless it is given one.
  - Otherwise: by the runtime's continuation, only once the session has been stopped and is gone from the listing, naming it by its full session id and giving no option beyond the message. Continuing a live session, a short id or an added option starts a copy. Read the printed note, count the relay as sent only when the original was woken, and end any copy.
  - A session that a started session starts does not get a plugin that was loaded for one session only.
- To end a session: use Claude Code's stop for that session. Leave removing an ended session from the runtime's list to the owner.
