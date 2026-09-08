### Gate 2: Correct Dependency Direction

**Expectation**
- Dependencies point from outer layers toward stable inner abstractions.
- Core behavior does not depend directly on volatile delivery or storage details.

**Evidence expectations**
- Plan documents dependency direction for touched components.
- Review verifies new imports/calls do not invert boundaries.
- Abstraction seams are explicit where external systems are involved.

**Anti-patterns**
- Domain logic directly calling framework, transport, or vendor clients.
- Circular dependencies between modules.
- Feature code bypassing interfaces to reach lower-level internals.
