# Changelog

## Unreleased — 2026-10-10

- adds an optional evidence-first Application Reconstruction path to SPARI's existing decision gate for explicitly scoped external application behavior;
- extends the path with a machine-readable state-transition behavior model, independent execution-receipt boundary, SHA-256 model binding and deterministic required-feature conformance CLI;
- adds JSON Schema contracts for behavior, runs and receipts, plus 17 executable Python stdlib acceptance/negative-control tests;
- retains only observed-scope completeness claims: no full ioco equivalence, hidden-feature completeness or production readiness is inferred;
- adapts Replica-style screen/flow observation, required-feature functional parity, and sourced feedback signals without importing a second agent, execution layer or mandatory research stage;
- preserves all required capabilities in the acceptance denominator even when omitted or unverified; does not treat screenshots, inferred internals or regex review themes as verified functional evidence;
- adds behavioral acceptance cases; no universal reproduction, parity or productivity claims are asserted.

## 0.1.7 — 2026-10-07

Pre-execution decision-control and sparse-search release.

- adds a hard `PRE_EXECUTION_DECISION_GATE` between admission and consequential search/implementation;
- requires capability definition and one explicit Build-vs-Borrow decision question before broad discovery;
- requires a bounded search plan before non-trivial repository scans, index builds, repo-map generation, or external search;
- makes R0–R4 selectable evidence radii rather than a sequence an agent should mechanically traverse;
- explicitly prohibits reflexive repository-wide indexing when narrower or already-existing host evidence can answer the decision;
- reuses host-native skills, repo maps, symbol search, indexes, MCP tools, and search providers rather than duplicating them inside SPARI;
- adds `EXECUTION_AUTHORITY = DENIED|GRANTED` with DENIED as the default;
- requires a recorded reuse decision before consequential implementation;
- makes `BUILD` require explicit evidence-based justification and a bounded Custom Delta;
- extends the executor boundary so `EXECUTION_CONTRACT` requires both `pre_execution_decision_ref` and `execution_authority = GRANTED`;
- returns execution authority to DENIED when new evidence can materially change the active reuse decision;
- preserves deterministic `FAST_REUSE` and `DIRECT_EXECUTION` through an explicit BYPASS decision record so trivial work does not inherit research overhead;
- adds pre-execution decision schema, failure states, reference contract, and adversarial acceptance cases;
- preserves v0.1.6 source attestation, v0.1.5 runtime evidence, v0.1.4 economy/index behavior, and v0.1.3 recomposition.

## 0.1.6 — 2026-10-01

Source-attestation and authority-access release.

- added a `SOURCE_ATTESTATION_GATE` before Economy Gate and Runtime Evidence Gate so local SPARI copies cannot silently masquerade as current authoritative policy;
- declares `tonnestate/SPARI` branch `main` as SPARI's current authority and explicitly separates branch authority from optional release tags;
- adds `AUTHORITY_ACCESS_PLAN` so agents discover and reuse available source transports instead of repeatedly assuming shell `git` is the only GitHub path;
- makes `git ls-remote` failure a transport failure rather than automatic `GITHUB_UNAVAILABLE` when a GitHub connector/API or another approved route is available;
- prioritizes host-native GitHub connector/API and direct GitHub authority access over generic web-search snippets for current revision proof;
- adds current-source identity capture: repository, authoritative ref, resolved SHA, canonical Skill metadata/hash, transport, and evidence references;
- adds local active-surface attestation by exact Git revision where trustworthy or by canonical content/manifest hashes when the installed skill is a copied directory without valid Git metadata;
- adds explicit `CURRENT_ATTESTED`, `PINNED_ATTESTED`, `PARTIAL_ATTESTATION`, `STALE_LOCAL_COPY`, `INSTALLATION_UNATTESTED`, `SOURCE_UNRESOLVED`, and `SOURCE_CONFLICT` states;
- prevents cached/offline copies from being promoted to `current` when current authority cannot be resolved;
- adds evaluation-freeze rules so all comparable arms use the same attested SHA and one arm cannot silently refresh mid-experiment;
- adds an explicit bootstrap boundary: SPARI self-attestation can fail closed after invocation, while hard pre-load stale-skill prevention belongs to the host installer/skill loader;
- adds source-attestation schema, failure codes, adversarial cases, README capability/status updates, and release checksums;
- preserves v0.1.5 Runtime Evidence Gate, v0.1.4 Economy Gate/Persistent Reuse Index, and earlier Build-vs-Borrow/Recomposition behavior;
- makes no claim that v0.1.6 alone enforces freshness in hosts that load stale instructions before the gate can execute.

## 0.1.5 — 2026-10-01

Runtime-evidence and trace-first repair release.

- added a `RUNTIME_EVIDENCE_GATE` for observed failures, broken behavior, wrong output, performance regressions, intermittent failures, failed acceptance gates, and real end-to-end failures;
- requires canonical entrypoint, reproduction, actual executed path, and first concrete failing condition before consequential speculative repair;
- makes runtime evidence outrank repository proximity, naming similarity, legacy relevance, and architecture speculation;
- adds capability-scoped reuse lookup after the failing runtime capability is known instead of defaulting to repository-wide archaeology;
- adds `RUNTIME_CUSTOM_DELTA`: the smallest architecture-consistent change on the actually executed path that repairs the reproduced failure;
- adds same-path retest discipline so repair evidence returns through the original canonical command/request/action;
- adds decision-changing-evidence and audit-budget rules to prevent thousands of low-value queries from becoming a substitute for diagnosis;
- routes unrelated inconsistencies to `FUTURE_WORK` unless they can change the active technical decision;
- adds a default three-cycle failed-hypothesis cap before feedback-loop/hypothesis re-evaluation or `RECOMPOSE`, while explicitly avoiding a universal optimality claim;
- extends Economy Gate outcomes with `RUNTIME_EVIDENCE_GATE`;
- adds runtime-specific failure states, schema, adversarial cases, and metrics including time-to-first-concrete-failure, runtime relevance ratio, and speculative intervention count;
- redesigns the README in the compact visual/project format used by BananaMe and adds a pink SPARI pig banner;
- preserves v0.1.4 Economy Gate, Persistent Reuse Index, adaptive R0–R4 research, Build-vs-Borrow composition, and v0.1.3 Recomposition;
- adds melodic-software/claude-code-plugins debugging skill as MIT-licensed conceptual prior art only; no source code or skill text is incorporated;
- makes no universal token, latency, request-count, or completion-lift claim for v0.1.5 before controlled evaluation.

## 0.1.4 — 2026-09-28

Economy-gate and persistent-reuse-index release.

- added a pre-inference `ECONOMY_GATE` so SPARI no longer acts as a mandatory cognitive tax on every engineering task;
- added deterministic fast matching before model-based prior-art reasoning where structured host evidence is available;
- added `FAST_REUSE`, `DIRECT_EXECUTION`, `SPARI_PREFLIGHT`, `SPARI_TARGETED`, `SPARI_FULL`, and `RECOMPOSE` admission outcomes;
- added explicit risk overrides so tiny patches that change dependencies, security, public interfaces, data/architecture authorities, provenance, or recovery state cannot bypass required reasoning;
- added break-even admission without inventing a universal token threshold;
- separated admission control from post-admission research budgets;
- added persistent/incremental `REUSE_INDEX` guidance for symbols, exports, types, dependencies, API/schema keys, architecture authorities, structural fingerprints, tests, and Decision/Trajectory references;
- made cached embeddings optional infrastructure rather than a per-task prerequisite and clarified that semantic retrieval is not a reuse verdict;
- changed `ENGINEERING_CASE` and heavier SPARI artifacts to conditional outputs rather than mandatory ceremony for deterministic micro-tasks;
- preserved v0.1.3 adaptive R0–R4 search radius and evidence-driven Recomposition;
- added schemas for Economy Gate decisions and the persistent reuse index;
- added adversarial economy-gate acceptance cases;
- consolidated corrected v0.1.3 bounded evaluation evidence in `EVIDENCE_V0.1.3.md`;
- explicitly marks v0.1.4 cost/capability effects as unproven until a dedicated controlled evaluation is run.

## 0.1.3 — 2026-09-17

Recomposition and trajectory-memory release.

- changed SPARI from a primarily front-loaded research pipeline to a small-first evidence-driven engineering loop;
- added compact `ENGINEERING_CASE` working state to bridge raw/qualified context into recall and technical evidence without duplicating intake governance;
- added Decision Memory + Trajectory Memory separation (`what was decided` vs `how the problem was escaped/solved`);
- made Recomposition a first-class control transition during execution rather than only a post-execution outcome;
- added bounded execution checkpoints with `CONTINUE / ADAPT / RECOMPOSE / STOP`;
- added adaptive search radius `R0_RECALL` through `R4_BROAD_EXTERNAL`;
- preserved `PREFLIGHT / TARGETED / FULL` as compatibility profiles/ceilings rather than mandatory linear workflows;
- changed Broad Recon and Deep Research from default sequencing to uncertainty-driven escalation;
- added intervention-surface evidence for minimal architecture-consistent changes;
- made IntakeGov explicitly optional: qualified context is consumed when available, but SPARI remains standalone-capable;
- added schemas for `ENGINEERING_CASE` and `TRAJECTORY_RECORD`;
- extended execution/memory schemas with composition version, trajectory references, checkpoints, and intervention evidence;
- added adversarial cases for recall-first behavior, trajectory lock-in, recomposition, small-first research, and minimal intervention;
- preserved v0.1.2 evidence as `EVIDENCE.md`; v0.1.3 hypotheses remain experimental until separately evaluated.

## 0.1.2 — 2026-09-16

Internal-prior-art and execution-boundary release.

- added `INTERNAL_SOFTWARE_MAP` as a first-class artifact before consequential external research;
- added capability-to-code, dependency, architecture-boundary, installed-dependency, and internal-reuse mapping;
- made active internal context relevance-constrained rather than a full repository dump;
- formalized the separation between SPARI decisioning and coding execution;
- added executor-agnostic `EXECUTION_CONTRACT`;
- added structured `EXECUTION_OUTCOME`;
- added base/result revision linkage for auditable implementation evidence;
- added planned-vs-actual reuse tracking;
- added planned-vs-actual Custom Delta tracking;
- added contract-deviation and unexpected-custom-code reporting;
- clarified that passing tests do not prove Build-vs-Borrow adherence;
- added Aider as conceptual prior art for repository mapping and execution-boundary design;
- added schemas for internal software maps, execution contracts, and execution outcomes;
- expanded failure codes and adversarial tests for internal-reuse blindness and executor scope drift.

## 0.1.1 — 2026-09-16

Build-vs-Borrow clarification and research-governance release.

- repositioned SPARI as a Build-vs-Borrow and Software Composition Engine;
- kept GitHub, PyPI, and internal software as the primary v0.x research scope;
- added proportional `PREFLIGHT`, `TARGETED`, and `FULL` research depths;
- separated convergence-based quality stopping from resource-budget stopping;
- added explicit research budgets for scouts, candidates, proof-of-fit work, strong-model escalation, tokens, and cost;
- made budget exhaustion fail closed as `RESEARCH_INCOMPLETE`;
- introduced ecosystem-neutral source-artifact modelling without expanding mandatory v0.x ecosystems;
- separated claimed source from verified source;
- separated declared license, detected license, and effective reuse decision;
- added memory retrieval discipline to avoid context rot;
- added source and research-profile schemas;
- expanded adversarial tests for research depth, budget exhaustion, source-link verification, and memory retrieval;
- added `search-first` and Microsoft Agent Governance Toolkit to conceptual prior-art notices.

## 0.1.0 — 2026-09-16

Initial public draft.

- Broad Recon before requirement freeze.
- GitHub and PyPI as primary software inventories.
- Semantic scope expansion.
- Few evidence-informed questions instead of generic interviews.
- Golden Plan handoff.
- Capability decomposition and source-level Deep Research.
- Parallel low-cost research swarm with independent evaluator and contrarian.
- Hard-gate-first evaluation.
- Reuse Blueprint and Custom Delta.
- License/provenance gate.
- Research convergence.
- Explicit failure states.
- Closed implementation-outcome feedback loop.
- Decision memory and revalidation triggers.
- Adversarial acceptance cases.
