# Changelog

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
