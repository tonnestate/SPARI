---
name: spari
description: Software Prior Art & Reuse Intelligence for AI engineering agents. Broadly scouts GitHub and PyPI before solution scope is frozen, asks only a few evidence-informed questions, then performs deep source-level research to compose the strongest reusable solution before custom development begins. Persists decisions and outcomes so future agents start from accumulated software intelligence instead of zero.
license: Apache-2.0
metadata:
  version: "0.1.0"
  status: experimental
  category: software-intelligence
  updated: "2026-09-16"
---

# SPARI

**Software Prior Art & Reuse Intelligence**

SPARI exists to stop AI agents from rebuilding software that already exists.

Its primary job is to evaluate GitHub repositories and PyPI packages before substantial custom implementation begins, then preserve what was learned so future agents do not repeat the same discovery work.

SPARI is not a generic project manager, not an interview framework, and not a search-results generator.

It is a closed software-reuse intelligence loop:

```text
Raw intent
   ↓
Broad GitHub/PyPI recon
   ↓
Solution-space map
   ↓
Few evidence-informed questions
   ↓
Confirmed intent + Golden Plan
   ↓
Deep GitHub/PyPI research
   ↓
Source inspection + candidate evaluation
   ↓
Reuse composition
   ↓
Minimal justified custom delta
   ↓
Implementation handoff
   ↓
Outcome + verification feedback
   ↓
Decision memory + revalidation triggers
   ↓
Next SPARI run starts smarter
```

## Core objective

Given a technical or product request:

> Discover what already exists, understand the broader solution space before narrowing it, identify the best GitHub codebases and PyPI packages, determine what can legally and technically be reused, compose the strongest existing foundation, and minimize unnecessary new code.

## Core invariants

1. Do not freeze the solution before Broad Recon.
2. Do not ask the user to define a solution space the agent has not yet investigated.
3. Do not interpret the user's literal wording as the final ontology.
4. Do not turn discovered alternatives into confirmed requirements without confirmation when the distinction is material.
5. Do not begin substantial custom implementation before internal, GitHub, and PyPI prior art has been evaluated.
6. Do not treat README claims, popularity, or passing tests as sufficient evidence.
7. Do not reuse external artifacts without a license/provenance decision.
8. Do not end at recommendation time. Feed implementation outcome back into SPARI memory.
9. Search failure is not evidence that no reusable solution exists.
10. BUILD must be justified; it is never the default.

## Relationship to IntakeGov

SPARI expects an upstream intake layer such as IntakeGov to decide whether work is a project/change/investigation and whether enough is known to begin reconnaissance.

SPARI can start at `RECON_READY`, intentionally earlier than full requirement completion.

Suggested maturity:

```text
RAW
→ RECON_READY
→ SOLUTION_SPACE_MAPPED
→ DECISION_READY
→ EXECUTION_READY
```

SPARI normally starts at `RECON_READY`.

See `references/intakegov-handoff.md`.

## Phase 1 — Broad Recon

Broad Recon is deliberately broader than the user's literal request.

Treat the literal wording as a starting signal.

Expand only along meaningful semantic relationships:

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
→ schema validation / mapping
→ ETL / import frameworks
→ complete data-import systems
```

Example:

```text
"RAG"
→ vector retrieval
→ hybrid retrieval
→ GraphRAG
→ knowledge graphs
→ knowledge systems
→ agent memory / document intelligence
```

Broad Recon must prioritize:

1. GitHub
2. PyPI
3. existing internal code and dependencies

It may use structured supporting sources such as deps.dev, OSV, OpenSSF, package metadata, and official documentation.

Broad Recon is not Deep Research. Its goal is to map the solution space cheaply and broadly.

Output: `SOLUTION_SPACE_BRIEF`.

See `references/broad-recon.md`.

## Phase 2 — Evidence-informed clarification

After Broad Recon, ask only a few questions that materially distinguish between real solution families already discovered.

Do not perform a generic interview.

Good:

> The recon found that the strongest existing systems split between a graph-centric and a retrieval-centric architecture. Do explicit entity relationships need to be first-class and queryable?

Bad:

> Which vector database do you want?

unless the user has already constrained that choice.

## Phase 3 — Confirmed intent and Golden Plan

After Broad Recon and any necessary clarification, establish the Golden Plan.

Required fields:

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

Deep Research may refine the solution shape. It may not silently replace confirmed intent because an easier implementation exists.

See `references/golden-plan.md`.

## Phase 4 — Capability map

Translate the Golden Plan into a capability map. Capabilities are the unit of research and composition.

## Phase 5 — Deep Research

Deep Research compares concrete reusable software.

Prefer parallel low-cost research agents for breadth and stronger evaluators for synthesis and judgement.

Recommended scouts:

- GitHub whole-product scout
- GitHub framework scout
- GitHub implementation scout
- PyPI primary-package scout
- PyPI alternative-package scout
- internal-reuse scout
- security/maintenance scout
- license/provenance scout

Scouts gather evidence. They do not make the final composition decision.

See `references/research-swarm.md`.

## Phase 6 — Candidate linking

For serious PyPI candidates, resolve where possible:

- package name;
- exact version;
- canonical source repository;
- release/tag;
- commit;
- hashes;
- Python compatibility;
- dependencies;
- provenance/attestation.

Treat package metadata and source code as one evidence chain.

## Phase 7 — Source inspection

Shortlisted candidates must be inspected beyond README-level claims.

Inspect as relevant:

- source tree;
- architecture;
- relevant modules;
- APIs;
- extension points;
- tests;
- release history;
- maintenance;
- dependency footprint;
- integration complexity;
- migration burden;
- issue quality;
- security posture;
- license scope;
- provenance.

Source evidence outranks marketing claims.

## Phase 8 — Capability coverage

Build a capability coverage matrix and identify:

- strongest whole-product base;
- strongest component libraries;
- internal components worth keeping;
- gaps that genuinely remain.

## Phase 9 — Hard gates

Apply non-negotiable constraints before trade-off comparison.

Examples:

- runtime incompatibility;
- Python-version incompatibility;
- unsupported deployment environment;
- unacceptable license;
- unresolved provenance;
- critical known vulnerability without acceptable mitigation;
- architectural conflict with mandatory constraints.

Popularity does not compensate for a failed hard gate.

## Phase 10 — Independent evaluation

Evaluate surviving candidates in two passes:

1. technical evaluator;
2. contrarian reviewer.

Resolve disagreement using evidence. Run a proof-of-fit when material uncertainty remains.

The evaluation must answer:

- Which GitHub repository is the best overall base?
- Which PyPI packages are better than the base implementation for specific capabilities?
- Which internal components should remain?
- Which repositories are useful only as references?
- Which custom capabilities remain unavoidable?

## Phase 11 — Reuse decisions

Assign each serious candidate one solution decision:

- `ADOPT`
- `ADAPT`
- `COMPOSE`
- `REFERENCE`
- `REJECT`
- `BUILD`

`BUILD` requires explicit evidence that viable existing options are insufficient.

Assign selected artifacts one role:

- `PRODUCT_BASE`
- `DEPENDENCY`
- `SOURCE_COMPONENT`
- `REFERENCE_PATTERN`
- `API_INTEGRATION`
- `VENDORED_COMPONENT`
- `CUSTOM_IMPLEMENTATION`

## Phase 12 — License and provenance

Before incorporation, resolve one legal reuse state:

- `REFERENCE_ONLY`
- `PATTERN_ONLY`
- `DEPENDENCY_ALLOWED`
- `CODE_REUSE_ALLOWED`
- `REVIEW_REQUIRED`
- `DENIED`

No reuse decision means no reuse.

See `references/license-provenance.md`.

## Phase 13 — Reuse Blueprint

Produce a concrete composition:

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
Repo E architecture pattern

CUSTOM
adapter F
```

The output is not "Repo A wins." It is the smallest strong composition of existing software.

## Phase 14 — Custom Delta

Produce `CUSTOM_DELTA`: only what still needs to be implemented after reuse.

A large custom delta is acceptable when justified. The purpose is to avoid unnecessary reinvention, not force reuse.

## Phase 15 — Research convergence

Deep Research is converged when:

- major solution families are stable;
- repeated searches mostly return known candidates;
- new candidates no longer materially change the comparison;
- finalists have enough source evidence for a decision;
- unresolved uncertainty is explicit.

If GitHub, PyPI, or another required source is unavailable, mark research incomplete.

Never convert source unavailability into permission to `BUILD`.

## Phase 16 — Implementation handoff

Hand downstream engineering:

- Golden Plan;
- capability map;
- candidate evidence;
- Reuse Blueprint;
- Custom Delta;
- license/provenance decisions;
- rejected alternatives and reasons;
- proof-of-fit evidence;
- known risks.

SPARI does not need to own implementation.

## Phase 17 — Outcome feedback

The loop is incomplete until implementation results return.

Record:

- what was actually implemented;
- which selected components were used;
- which were abandoned;
- integration failures;
- unexpected incompatibilities;
- tests/evidence;
- operational limitations;
- user/system outcome;
- custom code actually required;
- whether the reuse decision held up.

Outcome states:

- `VALIDATED`
- `VALIDATED_WITH_LIMITATIONS`
- `REQUIRES_RECOMPOSITION`
- `REJECTED_AFTER_IMPLEMENTATION`
- `UNKNOWN_OUTCOME`

## Phase 18 — Decision Memory

Persist software intelligence so future runs do not start from zero.

Store:

- capability;
- candidate;
- source;
- version/commit;
- evaluation;
- license/provenance;
- selected role;
- implementation outcome;
- limitations;
- revalidation triggers;
- last verified date.

A future SPARI run must query existing decision memory before repeating external research.

See `references/closed-loop.md` and `references/memory-schema.md`.

## Phase 19 — Revalidation

Re-open a previous decision when triggered by:

- major version change;
- repository maintenance collapse;
- new security advisory;
- license change;
- provenance change;
- breaking dependency change;
- materially better alternative;
- previous integration failure;
- target runtime/environment change.

Revalidation feeds back into the same research loop.

## Required outputs

- `SOLUTION_SPACE_BRIEF`
- `GOLDEN_PLAN`
- `CAPABILITY_MAP`
- `CANDIDATE_SET`
- `CAPABILITY_COVERAGE_MATRIX`
- `CANDIDATE_EVALUATIONS`
- `REUSE_BLUEPRINT`
- `CUSTOM_DELTA`
- `LICENSE_PROVENANCE_DECISIONS`
- `OUTCOME_RECORD`
- `DECISION_MEMORY_UPDATE`

## Failure handling

Use explicit failure states instead of hallucinating completion.

See `references/failure-codes.md`.

## Guiding principle

> Explore existing software before you freeze the solution.  
> Deeply evaluate and compose the strongest reusable base before you write what is missing.  
> Feed the real implementation outcome back into the next decision.
