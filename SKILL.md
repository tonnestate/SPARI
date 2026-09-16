---
name: spari
description: Build-vs-Borrow and software composition intelligence for AI engineering agents. Broadly scouts GitHub, PyPI, and the current system before solution scope is frozen, asks only a few evidence-informed questions, then deeply evaluates source, compatibility, security, license, provenance, and reuse options before substantial custom code is written. Persists outcomes so future agents start from validated software intelligence instead of zero.
license: Apache-2.0
metadata:
  version: "0.1.2"
  status: experimental
  category: software-intelligence
  updated: "2026-09-16"
---

# SPARI

**Build-vs-Borrow and Software Composition Engine for AI Agents**

*Software Prior Art & Reuse Intelligence*

SPARI exists to stop AI agents from rebuilding software that already exists.

Its primary job is to map what the current system already contains, evaluate GitHub repositories and PyPI packages before substantial custom implementation begins, decide what should be adopted, adapted, composed, referenced, rejected, or built, hand only the justified delta to an execution agent, and feed machine-checkable implementation outcomes back into future decisions.

SPARI is not a generic project manager, interview framework, search-results generator, or code generator.

## Closed loop

```text
Raw intent
→ Internal Software Map
→ Broad GitHub/PyPI recon
→ Solution-space map
→ Few evidence-informed questions
→ Confirmed intent + Golden Plan
→ Deep GitHub/PyPI research
→ Source inspection + evaluation
→ Build-vs-Borrow composition
→ Minimal justified Custom Delta
→ Implementation handoff
→ Outcome verification
→ Decision memory
→ Revalidation
→ Next run starts smarter
```

## Core objective

> Explore existing software before freezing the solution, then compose the strongest reusable foundation and build only the part that evidence shows is genuinely missing.

## Core invariants

1. Do not freeze the solution before Broad Recon.
2. Do not make the user define a solution space the agent has not investigated.
3. Treat literal wording as a starting signal, not the final ontology.
4. Do not convert discovered alternatives into confirmed requirements without confirmation when material.
5. Map relevant internal software before external reuse research, then check GitHub and PyPI before substantial custom implementation.
6. Source evidence outranks README claims, popularity, rankings, and model memory.
7. Apply hard constraints before qualitative preference.
8. Separate claimed source from verified source.
9. Do not reuse external artifacts without a license/provenance decision.
10. Search failure or budget exhaustion never implies that no reusable solution exists.
11. `BUILD` must be justified; it is never the default.
12. Separate the Build-vs-Borrow decision from code execution.
13. Require structured execution evidence rather than accepting narrative claims of completion.
14. Feed implementation outcomes back into decision memory.

## Relationship to IntakeGov

SPARI works best after an intake layer such as IntakeGov has established `RECON_READY`.

```text
RAW
→ RECON_READY
→ SOLUTION_SPACE_MAPPED
→ DECISION_READY
→ EXECUTION_READY
```

`RECON_READY` means enough is known to search intelligently; full requirements do not yet need to exist.

SPARI may also run standalone when the caller supplies an equivalent minimum context.

See `references/intakegov-handoff.md`.

## Research depth

Choose proportionally:

- `PREFLIGHT` — local inspection plus focused GitHub/PyPI check for a small or obvious generic need.
- `TARGETED` — due diligence on a known capability or named candidate, with focused alternatives.
- `FULL` — Broad Recon, qualified questions, Golden Plan, research swarm, source inspection, independent evaluation, composition, and Custom Delta.

Research may escalate upward when evidence increases ambiguity, impact, or risk.

A lighter mode never bypasses required license, provenance, security, or compatibility gates.

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

## Phase 1 — Broad Recon

Broad Recon is deliberately broader than the user's literal request.

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

Goal: map the solution space cheaply and broadly, not choose the final implementation.

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

Deep Research compares concrete reusable software.

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


## Phase 18 — Decision Memory

Persist:

- capability;
- candidate;
- source/version/revision;
- evaluation;
- source verification;
- license/provenance;
- selected role;
- implementation outcome;
- limitations;
- revalidation triggers;
- last verified date.

Before fresh external research, query prior memory and determine whether revalidation is needed.

Retrieve only records relevant to the current capability, constraints, ecosystem, candidate family, and freshness. Do not inject the full historical store into active context.

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

Depending on research depth:

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
- `LICENSE_PROVENANCE_DECISIONS`
- `EXECUTION_CONTRACT`
- `EXECUTION_OUTCOME`
- `OUTCOME_RECORD`
- `DECISION_MEMORY_UPDATE`

## Failure handling

Use explicit failures rather than hallucinated completion.

See `references/failure-codes.md`.

## Guiding principle

> Explore existing software before you freeze the solution.  
> Decide Build-vs-Borrow with evidence, then compose the strongest reusable base before you write what is missing.  
> Feed the real implementation outcome back into the next decision.
