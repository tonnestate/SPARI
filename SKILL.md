---
name: spari
description: Evidence-driven software prior-art, composition, and recomposition intelligence for AI engineering agents. Starts with the smallest relevant local context, recalls prior decisions and engineering trajectories, widens research only when unresolved uncertainty requires it, composes the smallest justified intervention, and recomposes when execution evidence invalidates the current path.
license: Apache-2.0
metadata:
  version: "0.1.3"
  status: experimental
  category: software-intelligence
  updated: "2026-09-17"
---

# SPARI

**Build-vs-Borrow and Software Composition Engine for AI Agents**

*Software Prior Art & Reuse Intelligence*

SPARI exists to stop AI agents from rebuilding software that already exists.

Its primary job is to prevent premature solution lock-in: recognize the current engineering case, recall what is already known, inspect the smallest relevant internal context first, widen into external prior art only when needed, compose the smallest justified intervention, and recompose that solution when execution evidence changes what is believed.

SPARI is not a generic project manager, interview framework, search-results generator, or code generator.

## Closed loop

```text
Raw or qualified engineering context
→ Engineering Case
→ Recall relevant decisions + trajectories
→ Smallest relevant local/internal evidence
→ Widen search radius only while material uncertainty remains
→ Build-vs-Borrow composition
→ Minimal justified Custom Delta + Intervention Surface
→ Bounded execution
→ Evidence checkpoint
→ CONTINUE | ADAPT | RECOMPOSE | STOP
→ Verified outcome
→ Decision Memory + Trajectory Memory
→ Next similar case starts smarter
```

## Core objective

> Preserve engineering evidence across time, reuse what is already known, and continuously compose or recompose the smallest evidence-backed solution before adding new software.

## Core invariants

1. Start with the smallest relevant engineering case; do not launch broad research merely because research is available.
2. Recall relevant prior decisions and engineering trajectories before repeating discovery.
3. Treat literal wording as a starting signal, not the final ontology.
4. Do not convert discovered alternatives into confirmed requirements without confirmation when material.
5. Inspect relevant internal software before widening externally; widen the search radius only when unresolved uncertainty can still change the decision.
6. Source evidence outranks README claims, popularity, rankings, and model memory.
7. Apply hard constraints before qualitative preference.
8. Separate claimed source from verified source.
9. Do not reuse external artifacts without a license/provenance decision.
10. Search failure or budget exhaustion never implies that no reusable solution exists.
11. `BUILD` must be justified; it is never the default.
12. Separate composition authority from code execution, but do not separate SPARI from execution evidence: bounded execution checkpoints may trigger adaptation or recomposition.
13. Require structured execution evidence rather than accepting narrative claims of completion.
14. Preserve both decision memory and trajectory memory: what was decided and how the system escaped failed or incomplete paths.
15. Recomposition is a first-class control transition, not merely a terminal failure outcome.
16. Preserve valid evidence across recomposition; do not restart from zero unless the evidence base itself is invalid.
17. Prefer the smallest architecture-consistent intervention that satisfies verified requirements.
18. Do not duplicate host-agent or toolchain work when equivalent trustworthy evidence is already available; consume it and continue from the unresolved gap.

## Relationship to IntakeGov

SPARI is standalone-capable. IntakeGov is an optional upstream governance layer, not a runtime dependency and not an authority that turns SPARI on or off.

When IntakeGov or another intake system provides qualified context, SPARI consumes it instead of repeating qualification. When only raw engineering context is available, SPARI establishes only the minimum technical case state required to proceed.

A useful handoff may include outcome, project context, constraints, known facts, unknowns, success criteria, risk flags, and prior attempts. SPARI then owns recall, prior-art depth, composition, and recomposition.

See `references/intakegov-handoff.md`.

## Research depth

`PREFLIGHT`, `TARGETED`, and `FULL` remain compatibility profiles, but v0.1.3 treats them as ceilings/escalation profiles rather than mandatory linear pipelines.

SPARI starts at the smallest useful search radius:

- `R0_RECALL` — relevant Decision/Trajectory Memory;
- `R1_LOCAL` — current code, tests, manifests, dependencies, and relevant internal map slice;
- `R2_RELATED_INTERNAL` — analogous modules, history, prior repairs, nearby capabilities;
- `R3_TARGETED_EXTERNAL` — focused packages, repositories, standards, and reference implementations;
- `R4_BROAD_EXTERNAL` — broader solution-space discovery and comparative research.

Escalate only when the current radius leaves material uncertainty that can change composition, Custom Delta, risk, or verification. Narrow again after the uncertainty is resolved.

A lighter radius never bypasses required license, provenance, security, or compatibility gates for artifacts that are actually considered for reuse.

See `references/research-depth.md`.

## Research budget

Research quality and resource control are separate.

`QUALITY_STOP` is convergence.

`RESOURCE_STOP` is an optional configured budget over scouts, candidates, proofs of fit, strong-model escalations, tokens, or monetary cost.

If the resource envelope ends before evidence is sufficient:

```text
RESEARCH_BUDGET_EXHAUSTED
→ RESEARCH_INCOMPLETE
```

Never convert budget exhaustion into `BUILD`.

See `references/research-budget.md`.

## Engineering Case and recall

Before broadening research, maintain a compact `ENGINEERING_CASE` working state. It is not a second intake/governance system. It exists to make recall, diagnosis, evidence updates, and recomposition explicit.

At minimum, preserve where available:

- outcome / affected capability;
- observed signal or failure;
- known evidence and constraints;
- material unknowns;
- current hypotheses;
- current composition;
- prior attempts and contradicting evidence.

Query relevant Decision Memory and Trajectory Memory before repeating research. A prior trajectory is useful when it explains not only what was selected, but how a previous solution path failed, what evidence changed the diagnosis, and what recomposition produced a validated outcome.

See `references/memory-schema.md`.

## Source model

SPARI v0.x intentionally prioritizes:

1. existing internal software, represented through an `INTERNAL_SOFTWARE_MAP`;
2. GitHub;
3. PyPI.

Its evidence model is ecosystem-neutral so future adapters can be added without rewriting the decision engine. Future ecosystems are extension points, not mandatory v0.x search scope.

See `references/source-model.md`.

## Phase 0 — Internal Software Map

Internal software is prior art too.

Before external research, inspect the current system strongly enough to answer:

- what capabilities already exist;
- which modules, packages, classes, functions, services, and interfaces implement them;
- which internal abstractions should be reused rather than duplicated;
- which dependencies are already installed;
- which architectural boundaries constrain new work;
- which areas are relevant to the current request.

Produce `INTERNAL_SOFTWARE_MAP`.

The durable map may be rich, but the active agent context should receive only the slice relevant to the current capability and decision. A full repository dump is not a context strategy.

The map is not merely a file tree. It should preserve useful relationships between code entities and capabilities where evidence permits.

See `references/internal-software-map.md`.

## Phase 1 — Broad Recon (when escalation requires it)

Broad Recon is deliberately broader than the user's literal request, but it is no longer an automatic first external step. Use it when local recall, internal prior art, and targeted evidence leave material solution-space uncertainty.

Expand along meaningful semantic relationships:

```text
literal request
→ underlying capability
→ parent solution category
→ adjacent solution classes
→ complete systems solving the same outcome
```

Example:

```text
"Excel import"
→ Excel parsing
→ tabular ingestion
→ validation/mapping
→ ETL/import frameworks
→ complete import systems
```

Prioritize internal context, GitHub, and PyPI. Supporting evidence may include official docs, deps.dev, OSV, OpenSSF, registry metadata, releases, and attestations.

Goal: resolve material solution-space uncertainty cheaply and broadly enough to improve composition, not to maximize research volume.

Output: `SOLUTION_SPACE_BRIEF`.

See `references/broad-recon.md`.

## Phase 2 — Evidence-informed clarification

After Broad Recon, ask only a few questions whose answers materially distinguish between solution families already discovered.

Do not conduct a generic interview.

Questions should reduce real decision uncertainty, not collect arbitrary preferences.

## Phase 3 — Golden Plan

After Broad Recon and required clarification, establish:

- `GOAL`
- `CONFIRMED_INTENT`
- `NON_GOALS`
- `IN_SCOPE`
- `OUT_OF_SCOPE`
- `REQUIRED_CAPABILITIES`
- `CONSTRAINTS`
- `EXISTING_SYSTEM_CONTEXT`
- `TECHNICAL_ENVIRONMENT`
- `SUCCESS_CRITERIA`
- `KNOWN_FACTS`
- `UNKNOWNS`
- `ALLOWED_SCOPE_REFINEMENT`

Deep Research may refine the technical shape but may not silently replace confirmed intent because an easier implementation exists.

See `references/golden-plan.md`.

## Phase 4 — Capability map

Translate the Golden Plan into capabilities.

Capabilities are the unit of discovery, comparison, composition, and Custom Delta accounting.

## Phase 5 — Deep Research

Deep Research compares concrete reusable software when the current Engineering Case still has consequential unresolved reuse/composition uncertainty.

Prefer cheap parallel agents for breadth and stronger evaluators for judgement.

Typical scout responsibilities include:

- whole GitHub products;
- frameworks/bases;
- implementation patterns;
- primary PyPI packages;
- alternative PyPI packages;
- internal reuse;
- maintenance/security;
- license/provenance.

Scouts collect evidence. They do not independently finalize the architecture.

See `references/research-swarm.md` and `references/deep-research.md`.

## Phase 6 — Candidate linking

For serious package candidates, resolve where possible:

- exact package/version;
- distribution artifact/hash;
- claimed source;
- verified source where possible;
- release/tag/commit;
- runtime compatibility;
- dependencies;
- provenance/attestation.

Do not collapse `CLAIMED_SOURCE` into `VERIFIED_SOURCE`.

Treat registry metadata and source code as one evidence chain.

## Phase 7 — Source inspection

Shortlisted candidates must be inspected beyond README-level claims where access permits.

Inspect relevant source, architecture, modules, APIs, extension points, tests, release/maintenance state, dependencies, integration burden, security posture, license scope, and provenance.

Source evidence outranks marketing claims.

## Phase 8 — Capability coverage

Build a capability coverage view that identifies:

- strongest whole-product base;
- strongest component libraries;
- internal components worth keeping;
- useful reference implementations;
- gaps that genuinely remain.

## Phase 9 — Hard gates

Eliminate or explicitly mitigate candidates that fail mandatory constraints such as:

- runtime/platform compatibility;
- deployment requirements;
- architecture constraints;
- security requirements;
- license compatibility;
- provenance requirements.

Popularity never compensates for a failed hard gate.

## Phase 10 — Independent evaluation

Use two passes for consequential decisions:

1. technical evaluator;
2. contrarian reviewer.

Resolve disagreements with evidence. Run a proof-of-fit when a material uncertainty cannot be settled from source/docs alone.

The evaluation must answer:

- best overall base;
- best component packages;
- internal components to retain;
- reference-only candidates;
- genuinely unavoidable custom capabilities.

## Phase 11 — Build-vs-Borrow decisions

Assign each serious candidate one decision:

- `ADOPT`
- `ADAPT`
- `COMPOSE`
- `REFERENCE`
- `REJECT`
- `BUILD`

`BUILD` requires evidence that viable existing options or compositions are insufficient.

Selected artifacts may take roles such as:

- `PRODUCT_BASE`
- `DEPENDENCY`
- `SOURCE_COMPONENT`
- `REFERENCE_PATTERN`
- `API_INTEGRATION`
- `VENDORED_COMPONENT`
- `CUSTOM_IMPLEMENTATION`

## Phase 12 — License and provenance

Track, where available:

- `DECLARED_LICENSE`
- `DETECTED_LICENSE`
- `EFFECTIVE_REUSE_DECISION`

Track source state separately:

- `SOURCE_UNKNOWN`
- `SOURCE_CLAIMED`
- `SOURCE_VERIFIED`
- `SOURCE_CONFLICT`

Before incorporation, resolve one reuse state:

- `REFERENCE_ONLY`
- `PATTERN_ONLY`
- `DEPENDENCY_ALLOWED`
- `CODE_REUSE_ALLOWED`
- `REVIEW_REQUIRED`
- `DENIED`

No reuse decision means no reuse.

`PROVENANCE_VERIFIED` establishes stronger origin/integrity evidence; it does not prove security or suitability.

See `references/license-provenance.md`.

## Phase 13 — Reuse Blueprint

Produce a concrete composition, not a winner list.

Example:

```text
BASE
GitHub Repo A

KEEP_INTERNAL
existing persistence layer

DEPENDENCY
PyPI Package B

REPLACE
Repo A module C with PyPI Package D

REFERENCE_ONLY
Repo E pattern

CUSTOM
adapter F
```

See `references/evaluation-composition.md`.

## Phase 14 — Custom Delta

Produce `CUSTOM_DELTA`: only the capabilities that still require custom implementation after reuse composition.

Each item should state why existing internal software, repositories, packages, or compositions are insufficient.

A large Custom Delta is acceptable when justified.

## Phase 15 — Research convergence

Deep Research converges when:

- major solution families are stable;
- repeated searches mostly return known candidates;
- new candidates no longer materially change the decision;
- finalists have sufficient evidence;
- unresolved uncertainty is explicit.

If required sources are unavailable or budget ends early, research remains incomplete.

## Phase 16 — Execution contract

SPARI decides what should be built; an execution agent performs the code changes.

The executor may be Aider, Claude Code, Codex, another coding agent, or a human engineering workflow. SPARI must not depend on one executor.

Before execution, emit an `EXECUTION_CONTRACT` containing at minimum:

- Golden Plan reference/version;
- Reuse Blueprint reference/version;
- planned Custom Delta;
- components that must be reused or retained;
- allowed substitutions;
- prohibited scope changes;
- hard constraints;
- verification requirements;
- evidence expected from the executor;
- base repository revision when available.

The executor must not silently expand the Custom Delta because writing new code is easier.

Execution may be bounded by evidence checkpoints. At a checkpoint SPARI may issue `CONTINUE`, `ADAPT`, `RECOMPOSE`, or `STOP`. `RECOMPOSE` must record what new evidence invalidated the current path, what evidence remains valid, what assumptions were rejected, and how the new composition changes the Custom Delta or intervention surface.

See `references/execution-boundary.md`.


## Phase 17 — Structured execution outcome

The loop is incomplete until implementation evidence returns.

Require an `EXECUTION_OUTCOME` rather than a prose-only completion claim.

Where applicable, record:

- executor identity/type;
- repository;
- base revision;
- result revision;
- planned reuse vs actual reuse;
- dependencies added/removed;
- files changed;
- intervention surface;
- trajectory/recomposition evidence;
- planned Custom Delta vs actual Custom Delta;
- tests/verification executed and results;
- lint/static-analysis results;
- integration failures;
- abandoned components;
- unexpected custom code;
- deviations from the Execution Contract;
- evidence references.

Outcome states:

- `VALIDATED`
- `VALIDATED_WITH_LIMITATIONS`
- `REQUIRES_RECOMPOSITION`
- `REJECTED_AFTER_IMPLEMENTATION`
- `UNKNOWN_OUTCOME`

A green test suite does not by itself prove that the Build-vs-Borrow decision was followed.

See `references/execution-boundary.md`.


## Phase 18 — Decision Memory + Trajectory Memory

Persist two different kinds of reusable intelligence.

`DECISION_MEMORY` answers: what did we decide, for which candidate/version/context, and what happened after implementation?

`TRAJECTORY_MEMORY` answers: how did we get out of the problem? Preserve material hypotheses, attempted paths, contradicting evidence, recomposition events, retained evidence, abandoned paths, validated recovery path, and applicability conditions.

Before fresh research:

1. retrieve relevant decisions;
2. retrieve relevant trajectories;
3. check freshness and applicability;
4. revalidate only triggered areas;
5. research only the unresolved gap.

Retrieve only records relevant to the current capability, constraints, environment, failure pattern, and freshness. Do not inject the full historical store into active context.

See `references/memory-schema.md` and `references/closed-loop.md`.

## Phase 19 — Revalidation

Re-open decisions when triggered by material changes such as:

- major release;
- maintenance collapse;
- security advisory;
- license/provenance change;
- breaking dependency change;
- stronger alternative;
- integration failure;
- target environment change.

Revalidation re-enters the same Build-vs-Borrow loop.

## Required outputs

Depending on case state and research depth:

- `ENGINEERING_CASE`
- `RESEARCH_PROFILE`
- `INTERNAL_SOFTWARE_MAP`
- `SOLUTION_SPACE_BRIEF`
- `GOLDEN_PLAN`
- `CAPABILITY_MAP`
- `CANDIDATE_SET`
- `SOURCE_EVIDENCE`
- `CAPABILITY_COVERAGE_MATRIX`
- `CANDIDATE_EVALUATIONS`
- `REUSE_BLUEPRINT`
- `CUSTOM_DELTA`
- `INTERVENTION_SURFACE` when measurable
- `RECOMPOSITION_EVENT` when triggered
- `TRAJECTORY_RECORD` for material multi-step/repair paths
- `LICENSE_PROVENANCE_DECISIONS`
- `EXECUTION_CONTRACT`
- `EXECUTION_OUTCOME`
- `OUTCOME_RECORD`
- `DECISION_MEMORY_UPDATE`
- `TRAJECTORY_MEMORY_UPDATE` when applicable

## Failure handling

Use explicit failures rather than hallucinated completion.

See `references/failure-codes.md`.

## Guiding principle

> Start small and recall before rediscovering.  
> Compose the smallest evidence-backed solution from what already exists.  
> When execution evidence invalidates the path, preserve what is still true and recompose instead of patching blindly.  
> Feed both decisions and successful/failed trajectories back into the next case.
