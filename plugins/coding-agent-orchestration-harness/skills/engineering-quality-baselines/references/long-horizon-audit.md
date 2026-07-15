# Long-Horizon Audit (Five-Step Lens)

Read this only for: project/process health reviews, refactor scoping, retrospectives, explicit longer-horizon requests, or a tripped drift tripwire that looks systemic. Never load it as part of standard task flow.

Purpose: examine an existing system, process, or plan through five steps applied strictly in order. Each step gates the next; skipping ahead invalidates the result.

The order is the point. The canonical failure is running it backwards: automating, then accelerating, then optimizing a thing — and only afterwards discovering the thing should not exist at all.

## Step 1: Question the Requirements

- Identify requirements that no longer earn their existence: the consumer is gone, the risk it guarded against has changed, or nobody can name why it is there.
- Requirements from authoritative sources (senior engineers, official docs, long-standing policy) deserve extra suspicion, not less — authority makes stale requirements harder to challenge.
- Challenges are surfaced to the requirement owner. Never silently drop a requirement, and never silently obey one you believe is wrong.

Do not proceed to Step 2 for any item whose requirement question is unresolved.

## Step 2: Delete

- Enumerate deletion candidates across all layers: code, process steps, validations, and automation.
- "We might need it in case X" justifies almost anything; demand a concrete, current consumer or a named, plausible risk.
- Calibration signal: if nothing ever has to be added back, not enough is being deleted. Occasional re-adds are evidence of healthy pruning, not failure.

Only what survives Steps 1-2 is eligible for the remaining steps.

## Step 3: Simplify and Optimize

- Simplify or optimize only what survived questioning and deletion.
- The most common engineering error is optimizing a thing that should not exist. If Step 3 effort is being planned for an item that skipped Steps 1-2, stop and go back.

## Step 4: Accelerate

- Find feedback-loop and cycle-time friction: slow validations, long review round-trips, manual steps in the critical path.
- Prefer the fastest loop that still produces learning — speed without signal is churn.
- Accelerate only after Steps 1-3; speeding up work on the wrong thing compounds the waste.

## Step 5: Automate

- Automate last. Automation and validation gates are for what has stabilized and survived deletion.
- Premature automation freezes a process before it has earned permanence and makes later deletion harder.

## Output

- Findings are surfaced, not silently acted on: report them to the user, record decisions in the plan Decision Log, and file lesson/rule candidates through existing channels.
- Each finding names the item, the step that flagged it, and the proposed disposition (challenge, delete, simplify, accelerate, automate, or keep).
