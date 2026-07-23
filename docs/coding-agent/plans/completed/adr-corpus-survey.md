# ADR Corpus Survey (companion evidence for the ADR integration plan)

Codex researcher, 2026-07-23T13:14-13:16Z, three parts, verbatim (reformatted from agmsg).

1 new message(s):

  [2026-07-23T13:14:53Z] agent-harness-researcher: ADR corpus survey 1/3 — CharacterMemory 39 ADRs (read-only)

Legend: criterion a=contract/API/schema, b=rejected alternative likely to return, c=costly-to-reverse, d=cross-repo obligation, e=user ruling overriding defaults. Altitudes use requested vocabulary.

Design ADRs (17):
- ADR-D-0001 Episode-backed object model — a | architecture-contract — canonical object schema replaces flat-memory shape.
- ADR-D-0002 Derived-memory provenance — a | architecture-contract — behavior-influencing memory admission/provenance contract.
- ADR-D-0003 Soft memory threads — a | architecture-contract — optional many-to-many scored membership shape.
- ADR-D-0004 ContinuityContextPack — a | architecture-contract — public retrieval result/API shape instead of flat top-k.
- ADR-D-0005 DerivedMemory subtypes before belief ontology — b | architecture-contract — records and defers the likely-to-return normalized belief ontology alternative.
- ADR-D-0006 Supersession/suppression — a | architecture-contract — correction/forget lifecycle semantics and retrieval filtering contract (partially resolved later by D-0017).
- ADR-D-0007 Chat-native/transcript-compatible start — c | product-philosophy — foundational modality/capability boundary whose schema direction is costly to unwind.
- ADR-D-0008 Preserve source references — a | architecture-contract — raw_ref/source-reference contract and explicit non-resolution boundary.
- ADR-D-0009 Entity-neutral retrieval — b | product-philosophy — forbids the repeatedly tempting role/name-special-casing alternative.
- ADR-D-0010 Recurring entities are anchors — a | architecture-contract — durable retrieval/expansion semantics for high-degree entities.
- ADR-D-0011 Arbitrary ContinuityScope — a | product-philosophy — scope model and semantics across entity/pair/thread/project/custom contexts.
- ADR-D-0012 Candidates vs committed memory — a | architecture-contract — write-domain state boundary and candidate->plan->validation->commit contract.
- ADR-D-0013 Controlled serendipity without weak links — b | product-philosophy — rejects weak pairwise durable edges while preserving a future recall path.
- ADR-D-0014 Separate associative membership lifecycle — a | architecture-contract — two-level unit/membership schema and lifecycle.
- ADR-D-0015 Raw source storage outside core — b | architecture-contract — durable core/application responsibility boundary against a likely raw-storage proposal.
- ADR-D-0016 No generic MetaMemory plane — b | product-philosophy — explicitly rejects a cross-cutting metadata plane likely to reappear.
- ADR-D-0017 Append-only memory + out-of-band purge — c | product-philosophy — costly permanence/erasure boundary with operator/application implications.

Implementation ADRs (22):
- ADR-I-0001 Stable cross-store IDs/IRIs — a | architecture-contract — persisted identity/join scheme.
- ADR-I-0002 Natural-language embedding surfaces — b | architecture-contract — rejects structured metadata-template embeddings likely to recur.
- ADR-I-0003 Qdrant + Oxigraph defaults — c | technology-selection — two-store operational/storage commitment.
- ADR-I-0004 Typed MemoryLink records — a | architecture-contract — domain relationship schema and relation vocabulary.
- ADR-I-0005 Qdrant payload vs graph authority — a | architecture-contract — authoritative/duplicated-data boundary across stores.
- ADR-I-0006 Bounded graph expansion/rationale — a | architecture-contract — retrieval policy and diagnostic contract.
- ADR-I-0007 Schema versioning from first persistence — a | architecture-contract — stored-record migration/version contract.
- ADR-I-0008 Retrieval stats are derived metadata — a | architecture-contract — third-store authority boundary.
- ADR-I-0009 SQLite default stats store — c | technology-selection — persistent default with operational/migration consequences.
- ADR-I-0010 Continuous selectivity/smooth fanout — a | parameter-tuning — structural policy/formula contract qualifies, although exact alpha/gamma/budgets are over-detailed (see value-audit note).
- ADR-I-0011 Guard low-information co-occurrence links — b | architecture-contract — rejects easy pairwise-link creation likely to return.
- ADR-I-0012 Prepare/validate/commit workflow — a | architecture-contract — public write API and single-commit operation shape.
- ADR-I-0013 Deterministic helpers do not infer meaning — b | architecture-contract — prevents deterministic convenience from reintroducing high-level inference.
- ADR-I-0014 Graph-internal associative units — b | architecture-contract — rejects a separate weak-hint truth store.
- ADR-I-0015 Candidate producer/rationale provenance — a | architecture-contract — enum/field schema and provenance semantics.
- ADR-I-0016 RetrievalIntent as query-time policy — a | architecture-contract — public enum/API placement versus persisted eligibility.
- ADR-I-0017 Persist support, not derived association scores — a | architecture-contract — durable graph schema vs rebuildable policy values.
- ADR-I-0018 Responsibility modules/dependency direction — c | architecture-contract — broad crate reorganization and enforced layering, costly to reverse.
- ADR-I-0019 Continuity harness placement — d | architecture-contract — explicit CM/CME ownership and public-API obligation split.
- ADR-I-0020 Restart identity via caller IDs, no lookup API — a | architecture-contract — public API omission plus caller bookkeeping contract.
- ADR-I-0021 Persistent embedded Oxigraph, remove HTTP mode — b | technology-selection — supersedes service-default guidance and prevents casual service-mode resurrection.
- ADR-I-0022 Retain measured retrieval defaults — NONE-OF-THEM [FALSE NEGATIVE] | parameter-tuning — exact alpha/gamma/budgets/candidate limits are reversible measured defaults and scoped deferral, not a durable contract under the draft.

CM counts: a=22, b=10, c=5, d=1, e=0, NONE=1. Altitude: architecture-contract=28, product-philosophy=6, technology-selection=3, parameter-tuning=2.

False negative / criterion response:
- Only ADR-I-0022 is not triggered. A possible new criterion would be "(f) empirically calibrated defaults whose measurement basis and deferred scope boundary must outlive the plan." I recommend NOT adding it: it would admit routine tuning. Better negative rule: exact reversible defaults and their experiment corpus stay in config/docs + completed-plan Decision Log; an ADR may retain only the durable invariant (e.g. continuous selectivity and entity-root scope), with numbers linked as evidence.

Criteria-unwarranted in hindsight:
- Clear candidate: ADR-I-0022. Today's value-audit lens would call the values conditional synthetic-corpus tuning; future code/config is the authority and the plan should own the experiment.
- Scope-trim candidate, not wholesale removal: ADR-I-0010 is warranted for "persist counters; compute continuous selectivity; smooth rather than category cliffs," but its exact initial formula/alpha/gamma belongs in measured configuration evidence, not the durable decision body.
- No other CM ADR is clearly plan-scoped: even milestone-framed D-0005/D-0007 record durable exclusions/revisit boundaries and likely reproposals, so they still clear criterion b/c.


1 new message(s):

  [2026-07-23T13:15:13Z] agent-harness-researcher: ADR corpus survey 2/3 — agent-harness 17 ADRs (read-only)

Design ADRs (14):
- ADR-D-0001 Canonical workflow location — b | process-governance — rejects duplicated workflow mechanics across loaders/adapters, a repeatedly tempting shape.
- ADR-D-0002 Explicit Orchestrator entrypoint — b | process-governance — rejects reliance on exact support-skill auto-triggering and protects explicit invocation.
- ADR-D-0003 Runtime-namespaced role identities — a | process-governance — logical/physical role identity contract across runtimes.
- ADR-D-0004 Worker UI probes vs Reviewer evidence — a | process-governance — validation ownership/independence contract.
- ADR-D-0005 Runtime prompt budgeting — b | process-governance — records why uniform prompts are rejected and runtime divergence is intentional.
- ADR-D-0006 Full rule suite + low-token index/lifecycle sidecar — a | process-governance — repository rule schema, file set, bootstrap order, and lifecycle contract.
- ADR-D-0007 Repo rules vs harness migration candidates — a | process-governance — durable ownership/routing boundary and candidate schema.
- ADR-D-0008 Codex authorization/Orchestrator/async lifecycle — e | process-governance — explicit-user-direction interpretation overrides duplicate-authorization caution and defines loader-routed authority.
- ADR-D-0009 Goal mode as second mode — c | process-governance — costly new operating lifecycle with human-oversight relocation.
- ADR-D-0010 Authority envelope/progress obligation — a | process-governance — formal authority, forbidden-action, and escalation contract.
- ADR-D-0011 Progress is goal-gap, not second object — a | process-governance — formal progress/stall/Goodhart contract.
- ADR-D-0012 Independent in-loop assessor — a | process-governance — assessment role, context, cadence, and burden-of-proof contract.
- ADR-D-0013 Completion report + retrospective merge gate — a | process-governance — completion/merge authorization and evidence-report contract.
- ADR-D-0014 Assessor re-examines goal validity — a | process-governance — co-equal validity duty and user-only direction-change boundary.

Implementation ADRs (3):
- ADR-I-0001 Runtime adapter layout — a | technology-selection — runtime-specific discovery/layout contract with shared skill ownership.
- ADR-I-0002 Codex bootstrap/loader strategy — c | technology-selection — installation/update mechanism and managed-loader boundary with stale-install consequences.
- ADR-I-0003 Contract-first balanced validation — a | process-governance — strict-vs-advisory validator contract.

Harness counts: a=11, b=3, c=2, d=0, e=1, NONE=0. Altitude: process-governance=15, technology-selection=2.

Combined 56-ADR counts:
- Criteria: a=33 (58.9%), b=13 (23.2%), c=7 (12.5%), d=1 (1.8%), e=1 (1.8%), NONE=1 (1.8%).
- Altitude: architecture-contract=28 (50.0%), process-governance=15 (26.8%), product-philosophy=6 (10.7%), technology-selection=5 (8.9%), parameter-tuning=2 (3.6%), other=0.
- Draft recall against the historical corpus: 55/56 (98.2%); after applying the recommended negative filter to I-0022, effective desirable recall is 55/55.

Value-audit notes:
- No harness ADR is clearly unwarranted. D-0005 is the closest borderline: prompt length itself is implementation detail, but the durable decision is that semantic equivalence does NOT require textual equality and uniform-prompt proposals are expected to recur, so criterion b justifies it.
- I-0001 looks like folder layout at first glance, but runtime discovery/collision behavior makes the layout a multi-runtime contract, not routine file placement.
- The goal-mode ADRs D-0009..D-0014 form a deliberately decomposed cluster: root mode decision plus separate authority, progress, assessor, completion, and validity contracts. Their separation is useful because each has an independent invariant/revisit trigger; collapsing them would make one mega-ADR.

Calibration implication:
- Criterion (a) should say "externally observable or cross-boundary contract/API/schema/authority/evidence-ownership shape" so harness governance contracts are unmistakably included; do not broaden it to every internal type.
- Criterion (e) should be narrowed: user authorship is provenance, not by itself warrant. Trigger only when the ruling establishes a durable product/architecture/cross-boundary governance default likely to survive the task. Otherwise CME shows it would over-admit PR titles, push sequencing, artifact placement, and similar repo operating rules.


1 new message(s):

  [2026-07-23T13:16:04Z] agent-harness-researcher: ADR corpus survey 3/3 — CME negative space, rule/ADR boundary, template patterns

CME evidence inspected: all current rules plus Decision Logs in the three largest completed plans by line count: character-memory-public-api-eval-adapter-plan (360), eval-harness-architecture-revision-plan (348), metric-registry-runtime-readiness-plan (335).

Strongest CME decisions that never became a CME ADR:
1. Workspace/module ownership: backend-neutral contracts in core; live CM adapter in its crate; each dataset owns loader/mapper/scorer/history/config/metric family; adding a dataset must not edit core (common.md:46-49, architecture-revision Q2). Verdict: SHOULD HAVE ADR (a/c), likely one "evaluation architecture and extension boundary" ADR. It constrains every future dataset/adapter and alternatives (core dispatch, extension trait, main-trait contract) need rationale/revisit context; the rule should remain as enforcement.
2. Live adapter is benchmark default; mock requires explicit opt-in and visible mock/smoke labeling (public-api plan Decision Log + common.md:26-27). Verdict: SHOULD HAVE ADR (a/e). It is user-facing CLI/default behavior chosen against a plausible accidental-mock alternative; the rule alone states what, not why failing loudly is preferred.
3. Artifact contract: schema 2.0.0 on rows/traces/summaries/reports; strict fail-closed readers; exactly bounded legacy 1.0 readers for sealed register-cited evidence; latency/embedding binding/typed-null semantics (architecture-revision Q3 + common.md:50-52). Verdict: SHOULD HAVE ADR (a/b/c), strongest true gap. It is a multi-artifact schema/migration contract with a deliberately rejected broad compatibility mode and an exception that future authors will re-litigate.
4. Reader strictness is a trust-boundary property independent of producer Deserialize permissiveness, scoped only to hash-cited evidence readers; manual Deserialize belongs on mirrored type, not scattered fields (common.md:51, consult-ruled). Verdict: SHOULD HAVE ADR, probably a section/paired ADR with #3 (a/b). The unusually specific scope and rejected generalization need durable rationale; keep the rule as executable enforcement.
5. No backwards compatibility while no external consumers, BUT frozen stores/hashes/evidence are sealed and exempt (common.md:41-42). Verdict: SHOULD HAVE ADR or be folded into #3 (b/e/c). This is not merely coding style: it governs removal/migration and a costly immutable-artifact exception.
6. Character-Memory-shaped main MemoryAdapter trait with staged writes, no extension-trait split (architecture-revision Q2). Verdict: SHOULD HAVE ADR (a/b), naturally part of #1. It is the central adapter API shape and records a rejected alternative.
7. Restart identity uses caller-supplied deterministic IDs + harness-persisted registry; store rediscovery verifies only; no facade change (architecture-revision Decision Log). Verdict: NO duplicate CME ADR. Cross-repo criterion d is already canonically satisfied by CM ADR-I-0020; CME should link to that ADR and keep implementation-specific evidence in plan/rules. This is the "another repo already owns the ADR" negative rule.
8. Drop the adapter feature gate after workspace membership made it ineffective (architecture-revision Q1). Verdict: Decision Log was right. Reversible build-organization tactic tied to current Cargo topology; no durable alternatives burden.
9. Public sibling checkout + full fmt/clippy/test/mock CI without credentials (architecture-revision 2026-07-11). Verdict: rule/CI config + Decision Log was right. Repository fact and validation procedure, not architecture.
10. Use heuristic token estimates now; defer exact tokenization/readers/judges (metric-registry plan). Verdict: Decision Log was right. Explicitly plan-scoped sequencing/deferral.
11. Gold labels only in scoring, never model/adapter inputs (common.md:25). Verdict: rule home is right. It is a direct, testable benchmark-safety invariant with little alternatives/rationale burden; always-loaded enforcement is more valuable than an ADR.
12. Internal Tier-D approval before external-review-triggering push; isolated review worktrees; design-consult threshold; validation evidence matrices (orchestrator/reviewer rules). Verdict: rule home is right. These are agent operating/verification procedures that must be read every task and can evolve with harness capability; an ADR would add historical rationale but not change future product architecture.

Boundary synthesis (the prize):
- ADR home = durable semantic/authority/ownership decision whose rejected alternatives, migration/reversal cost, or cross-boundary obligations must survive the implementing plan; future humans need WHY + revisit conditions. The ADR may have an always-loaded rule that enforces it.
- Rule home = concise imperative or evidence trigger that agents must execute on every applicable task; rationale is local/short, change follows repo facts or harness capability, and no alternative/migration history is needed to apply it.
- Decision Log home = task-specific sequencing, temporary deferral, exact current parameters, reversible implementation tactic, or a choice canonically owned by another repo ADR.
- Therefore rules and ADRs are not substitutes: for #1-#5, ADR owns rationale/contract and rules own enforcement. For #8-#12, adding ADRs would be documentation inflation.

Recurring corpus/template patterns not already captured by the CM template:
1. Warrant + altitude metadata. Add `warrant: [a|b|c|d|e]` and `decision_altitude:` (or an equivalent short "Why ADR, not Decision Log/rule?" field). This forces the value audit at creation time and catches parameter-tuning leakage.
2. Durable invariant vs calibrated defaults. Add an optional "Decision Boundary" subsection: invariant that requires ADR change vs current defaults/parameters that may change through measured config/Decision Log. I-0010/I-0022 demonstrate the need.
3. Explicit ADR graph. Add `implements`, `implemented_by`, `depends_on`, and `affected_repositories/authority_owner` metadata. Corpus clusters are common: CM D-0012 -> I-0012/I-0015; D-0013/D-0014 -> I-0014/I-0017; retrieval philosophy D-0009/D-0010 -> I-0008..I-0011; harness goal-mode root D-0009 -> D-0010..D-0014. `More Information` links do not express relationship type.
4. Partial supersession semantics + reciprocal maintenance. Existing template already has supersedes/superseded_by, but all 56 ADRs leave both empty/non-null despite D-0006 explicitly saying D-0017 resolved its deletion question. Add `supersession_scope: full|partial` (or amendments list), require the old ADR's status/frontmatter update, and say which clauses remain authoritative.
5. Consultation impact, not just names. All 56 ADRs have non-empty `consulted`, but metadata records only model/person identity. Add one concise optional "Consultation impact" line: question asked, ruling adopted/rejected, and any unresolved dissent. This is especially valuable for contract-shape consults; do not copy chat transcripts.
6. Evidence basis for empirically grounded ADRs. I-0022 had to invent `## Measurement Basis`; add optional template support with corpus/config/provenance, scope limits, and reproducibility pointer. Crucially, evidence does not automatically warrant an ADR.
7. Amendment policy. Only one ADR has Revision History, while later decisions often clarify older ones inline. Define when a wording clarification may amend in place versus when changed authority/behavior requires a new superseding ADR; prefer reciprocal ADR links over silent historical rewrites.
8. Guarded rejected alternatives. `Considered Options` exists already, but add a small flag/phrase for the specific rejected alternative likely to be re-proposed and the evidence/revisit condition that would reopen it. This makes criterion b operational without bloating every option.

Corpus structure counts: 56/56 accepted; 56/56 have Decision/Context/Consequences/Validation; 53 have Decision Drivers; 52 have Considered Options, Decision Outcome, and Revisit When; 36 Implementation Impact; 19 Character Memory Relevance. All 56 record consultation provenance, but 0/56 use `supersedes` and 0/56 use non-null `superseded_by`. Special one-offs: one Revision History, one Measurement Basis, one Rejected Legacy Shapes section.

Recommended calibrated warrant rule:
"Create an ADR when a decision must constrain future work beyond its implementing plan because it establishes (a) an externally observable or cross-boundary contract/API/schema/authority/evidence-ownership shape; (b) rejects an alternative likely to be re-proposed; (c) creates meaningful migration/reversal cost; (d) assigns cross-repository obligations; or (e) records a user ruling that establishes a durable product/architecture/cross-boundary governance default. Do not create an ADR for reversible parameters, task sequencing, temporary deferrals, ordinary implementation tactics, always-loaded enforcement rules with no durable rationale burden, or a decision canonically owned by another repository's ADR."

No files edited.
