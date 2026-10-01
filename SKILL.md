---
name: spari
description: Evidence-driven software prior-art, economy-gated reuse, runtime-path diagnosis, composition, and recomposition intelligence for AI engineering agents. Uses deterministic evidence before inference, traces the actual executed path before repairing observed failures, reuses persistent repository intelligence, builds only the smallest justified delta, and recomposes when execution evidence invalidates the current path.
license: Apache-2.0
metadata:
  version: "0.1.5"
  status: experimental
  category: software-intelligence
  updated: "2026-10-01"
---

# SPARI

**Build-vs-Borrow, Runtime-Evidence, Composition, and Recomposition for AI Agents**

*Software Prior Art & Reuse Intelligence*

SPARI exists to stop AI agents from rebuilding software that already exists, debugging code that does not actually run, and remaining trapped in solution paths contradicted by evidence.

SPARI is not a generic project manager, search-results generator, code generator, debugger, observability platform, or mandatory tax on every engineering task.

## Operating loop

```text
Raw or qualified engineering context
→ ECONOMY GATE
   → deterministic fast match / persistent index
   → risk override + break-even admission
   → observed failure?
      ├─ YES
      │   → RUNTIME EVIDENCE GATE
      │   → canonical entrypoint
      │   → reproduce
      │   → executed path
      │   → first concrete failure
      │   → capability-scoped reuse lookup
      │   → minimal Runtime Custom Delta
      │   → same-path retest
      │   → CONTINUE | ADAPT | RECOMPOSE | STOP
      └─ NO
          ├─ FAST_REUSE / DIRECT_EXECUTION
          └─ SPARI_ADMITTED
              → Engineering Case
              → R0 Recall
              → R1 Local
              → R2 Related Internal
              → R3 Targeted External
              → R4 Broad External
              → Build-vs-Borrow composition
              → Minimal Custom Delta + Intervention Surface
              → Bounded execution
              → Evidence checkpoint
              → CONTINUE | ADAPT | RECOMPOSE | STOP
→ Verified outcome
→ Decision + Trajectory Memory
→ Incremental index refresh
```

## Core objective

> Determine what actually runs, reuse what already works, and build only the smallest missing piece that evidence proves necessary.

## Core invariants

1. **Determinism before inference.**
2. **Runtime before repository speculation.**
3. **Trace before repair.**
4. **Reuse before research.**
5. **Build only what is missing.**
6. **Recompose when evidence changes.**
7. Do not spend model inference to decide whether inference is needed when deterministic evidence can decide first.
8. Do not launch deep SPARI work when a bounded task can be safely resolved by exact reuse or direct execution.
9. Bypass only when explicit evidence shows that architecture, dependency, provenance, security, public-interface, and recovery risks do not require deeper decisioning.
10. An observed failure activates Runtime Evidence Gate discipline before broad repository archaeology or architecture changes.
11. The actual executed path outranks repository proximity, naming similarity, legacy relevance, README claims, and model memory.
12. A file not shown to participate in the observed runtime path is out of repair scope unless evidence connects it to the root cause.
13. Identify the first concrete failing condition before widening the repair.
14. Additional diagnostic/research queries must be able to change the current technical decision.
15. Interesting inconsistencies that cannot change the current decision are `FUTURE_WORK`, not automatic scope.
16. Do not create a new service, adapter, contract, store, schema, CLI mode, rebuild path, or fallback architecture without evidence that the executed path cannot be repaired correctly without it.
17. Search failure, index failure, runtime-evidence failure, or budget exhaustion never implies that no reusable solution exists.
18. `BUILD` must be justified; it is never the default consequence of missing evidence.
19. Preserve valid evidence across recomposition; reopen only the invalidated gap unless the evidence base itself is invalid.
20. Prefer the smallest architecture-consistent intervention that satisfies verified requirements.
21. Re-run the identical canonical path after a repair when possible.
22. Do not duplicate work already performed by the host, IntakeGov, repository index, prior validated SPARI evidence, or runtime instrumentation.
23. Persist inspectable engineering evidence, not hidden chain-of-thought.
24. Do not publish quantitative savings or capability claims without reproducible measurement.

# Economy Gate

The Economy Gate runs before model-heavy prior-art reasoning.

Its job is to decide how much SPARI is justified for the current work slice.

## Inputs

Use host-provided deterministic evidence where available:

- task/work-slice identity and scope;
- repository/base revision;
- observed failure state;
- known canonical reproducer/entrypoint;
- affected capability/path;
- dependency/manifest evidence;
- exact symbol/export/type/interface matches;
- route/API/schema identifiers;
- tests and canonical authorities;
- structural fingerprints;
- prior Decision/Trajectory keys;
- prior failures/recomposition triggers;
- optional cost estimates;
- configured risk/break-even policy.

Do not invent missing numeric estimates.

## Gate outcomes

- `FAST_REUSE`
- `DIRECT_EXECUTION`
- `SPARI_PREFLIGHT`
- `SPARI_TARGETED`
- `SPARI_FULL`
- `RUNTIME_EVIDENCE_GATE`
- `RECOMPOSE`

An observed failure normally routes to `RUNTIME_EVIDENCE_GATE` unless a trustworthy canonical failing check already supplies the required runtime evidence. That check may itself serve as the reproducer.

Risk override should route to the smallest adequate profile, not automatically to FULL.

See `references/economy-gate.md` and `schemas/economy-gate.schema.json`.

# Runtime Evidence Gate

Use when work starts from:

- `OBSERVED_FAILURE`
- `BROKEN_BEHAVIOR`
- `WRONG_OUTPUT`
- `PERFORMANCE_REGRESSION`
- `INTERMITTENT_FAILURE`
- `FAILED_ACCEPTANCE_GATE`
- `REAL_E2E_FAILURE`

The Runtime Evidence Gate is an admission/scope/execution guard, not a new autonomous agent.

## Required sequence

### 1. Canonical entrypoint

Identify the public path representing the real behavior:

```text
CLI command
HTTP/API endpoint
UI action
MCP tool
library function
scheduled/runtime entrypoint
trusted failing test when it faithfully exercises the real path
```

If unknown, record `CANONICAL_ENTRYPOINT_UNKNOWN` and obtain the smallest evidence needed to resolve it.

### 2. Reproduce

Create or use a fast enough, deterministic enough signal that shows:

```text
failure present
failure absent
```

The reproducer must represent the user's reported failure, not an adjacent failure that happens to be easy to trigger.

If the failure cannot be reproduced, do not perform speculative implementation repair. Record `NOT_REPRODUCED` or `RUNTIME_EVIDENCE_INCOMPLETE` with the missing evidence.

### 3. Trace the executed path

Follow only the path needed to locate the first material failure:

```text
entrypoint
→ actual functions/modules/services
→ actual data access/dependency calls
→ first concrete failing condition
```

Use stack/call/test traces, structured logs, targeted instrumentation, debugger/REPL observations, coverage slices, request traces, or equivalent host evidence.

`looks relevant` is not runtime evidence.

### 4. First concrete failure

Stop broadening when the earliest material failing condition is found.

Do not simultaneously fix later symptoms.

Record the failing component, condition and evidence reference.

### 5. Capability-scoped reuse lookup

Query the Persistent Reuse Index for the failing capability:

```text
capability
→ symbol / interface / route / schema
→ installed dependency
→ architecture authority
→ prior Decision / Trajectory
→ related internal implementation
```

Do not convert one runtime failure into a full repository reuse audit by default.

### 6. Minimal Runtime Custom Delta

Prefer:

- `KEEP_INTERNAL`
- `REUSE`
- `ADAPT`
- `EXTEND_INTERNAL`

before new architecture.

`RUNTIME_CUSTOM_DELTA` is the smallest change to the executed path that repairs the reproduced failure and satisfies required constraints.

### 7. Same-path retest

Re-run the same canonical command/request/action or equivalent faithful reproducer.

A different adjacent test is not sufficient evidence for the original failure unless equivalence is explicitly demonstrated.

### 8. Close or recompose

- `PASS` when required evidence shows the original path works.
- `ADAPT` when a bounded local adjustment remains.
- `RECOMPOSE` when runtime evidence invalidates the active authority, dependency, composition, or hypothesis.
- `BLOCKED` when evidence needed to proceed cannot be obtained safely.

See `references/runtime-evidence-gate.md` and `schemas/runtime-evidence-gate.schema.json`.

## Executed code outranks nearby code

If a module is not executed by the observed path:

```text
NOT_IN_RUNTIME_PATH
```

Default action:

```text
do not repair
do not refactor
do not redesign around it
```

Exception: evidence demonstrates that it participates in the root cause despite not appearing in the direct trace.

## Decision-changing evidence rule

Before an additional diagnostic or research action:

```text
What engineering decision can this evidence change?
```

If there is no concrete answer:

```text
DO_NOT_QUERY
```

This rule applies to repository audits, historical scans, broad store/database scans, external searches, new instrumentation and speculative comparisons.

## Audit budget

Default diagnosis scope:

- current failing capability;
- canonical executed path;
- immediately dependent components;
- the smallest evidence needed to distinguish live hypotheses.

Do not run full-store, full-history or repository-wide completeness audits for a local repair unless the current decision depends on them.

Record unrelated findings as `FUTURE_WORK`.

## Failed-cycle cap

Do not retry blindly.

After three falsified hypothesis-test cycles by default:

1. re-check the reproduction loop;
2. re-check the canonical entrypoint/path;
3. reconsider hypothesis ranking;
4. `RECOMPOSE` or `BLOCKED` when appropriate.

A deployment may configure another cap. The public release does not claim that three is universally optimal.

# Persistent Reuse Index

SPARI prefers a persistent, incrementally refreshed index over reconstructing repository knowledge in model context for every intake.

The index may contain:

- repository/workspace revision;
- manifests/lockfiles;
- packages/modules/services;
- symbols, exports, types, interfaces, routes, schemas;
- dependency edges;
- architecture authorities/boundaries;
- capability-to-code mappings;
- test/evidence references;
- structural fingerprints;
- installed dependencies;
- validated Decision/Trajectory references;
- optional cached embedding references.

Optional semantic/vector retrieval returns candidates, not final engineering judgements.

Refresh only affected entries when relevant repository state changes.

See `references/persistent-index.md` and `schemas/reuse-index.schema.json`.

# Research depth

Economy Gate is admission control. Runtime Evidence Gate is repair scoping. Search radius is a separate escalation dimension.

- `R0_RECALL` — relevant Decision/Trajectory Memory.
- `R1_LOCAL` — current code/tests/manifests/dependencies and relevant indexed slice.
- `R2_RELATED_INTERNAL` — analogous modules/history/previous fixes/internal repair ingredients.
- `R3_TARGETED_EXTERNAL` — focused GitHub/PyPI/standards/reference search.
- `R4_BROAD_EXTERNAL` — broader solution-family discovery and comparative evaluation.

For observed failures, remain capability-scoped around the executed failing path until evidence justifies widening.

`PREFLIGHT`, `TARGETED`, and `FULL` are ceilings/operating ranges, not mandatory pipelines.

See `references/research-depth.md`.

# Engineering Case and recall

Create a compact `ENGINEERING_CASE` only when admitted work or recomposition requires it.

Where applicable preserve:

- outcome / affected capability;
- observed signal/failure;
- known evidence and constraints;
- material unknowns;
- current hypotheses;
- current composition;
- prior attempts;
- contradicting runtime evidence.

Before fresh discovery, retrieve only relevant Decision and Trajectory Memory.

# Internal Software Map

Internal software is first-class prior art.

`REUSE_INDEX` is the cheap lookup surface. `INTERNAL_SOFTWARE_MAP` is the richer capability/dependency/architecture view when needed.

Do not rebuild the full map for every task. Runtime failures should normally inspect only the relevant executed path and capability neighborhood.

See `references/internal-software-map.md`.

# External prior art

SPARI v0.x prioritizes:

1. existing internal software;
2. GitHub;
3. PyPI.

Use R3/R4 only when internal/runtime evidence leaves a material gap.

For serious external candidates resolve where possible exact version/artifact/source/revision, compatibility, dependencies, license and provenance.

`CLAIMED_SOURCE` is not `VERIFIED_SOURCE`.

# Broad Recon and clarification

Broad Recon is for real solution-family uncertainty.

Do not use it merely because a runtime failure exposed an interesting adjacent architecture question.

Ask only questions whose answers can materially distinguish evidence-backed solution paths.

# Build-vs-Borrow composition

Candidate decisions:

- `ADOPT`
- `ADAPT`
- `COMPOSE`
- `REFERENCE`
- `REJECT`
- `BUILD`

Produce a concrete `REUSE_BLUEPRINT`, not a winner list.

`CUSTOM_DELTA` is only the capability still requiring custom implementation.

For observed failures, `RUNTIME_CUSTOM_DELTA` is narrower: the smallest necessary change on the executed path.

# License and provenance

Track declared/detected license, effective reuse permission, and source verification separately.

Before incorporating external material, resolve one of:

- `REFERENCE_ONLY`
- `PATTERN_ONLY`
- `DEPENDENCY_ALLOWED`
- `CODE_REUSE_ALLOWED`
- `REVIEW_REQUIRED`
- `DENIED`

No reuse decision means no reuse.

# Execution boundary

SPARI decides what should exist; a coding agent performs source changes.

For consequential admitted work, emit an executor-agnostic `EXECUTION_CONTRACT`.

Fast-path/runtime-gate repairs may use reduced bounded instructions when a full contract would cost more than the task and no risk override requires it.

Execution evidence may trigger:

- `CONTINUE`
- `ADAPT`
- `RECOMPOSE`
- `STOP`

# Recomposition

Recompose when new evidence materially weakens or falsifies the current path, including when:

- runtime evidence shows a different canonical authority is executed;
- verification contradicts the active hypothesis;
- dependency/integration assumptions fail;
- a previously unknown internal capability changes the composition;
- implementation starts creating parallel architecture or unjustified Custom Delta;
- repeated local repairs do not address the root cause;
- hard-gate evidence changes.

A recomposition event preserves valid evidence and records:

- trigger/new evidence;
- invalidated assumptions;
- retained evidence/components;
- abandoned path;
- new capability/reuse evidence;
- composition change;
- Custom Delta/intervention change;
- required verification.

Do not restart from zero unless the evidence base itself is invalid.

# Structured execution outcome

For consequential work, require `EXECUTION_OUTCOME` rather than prose-only completion.

Where applicable record:

- executor;
- repository;
- base/result revision;
- planned vs actual reuse;
- files/dependencies changed;
- intervention surface;
- runtime/recomposition evidence;
- planned vs actual Custom Delta;
- verification results;
- abandoned components;
- unexpected custom code;
- deviations;
- evidence references.

A green test suite alone does not prove Build-vs-Borrow or runtime-path adherence.

# Memory and index update

Decision Memory answers what was decided and what happened.

Trajectory Memory answers how the system escaped or failed to escape the problem.

Persist inspectable state:

```text
commands / actions
observations
execution path
evidence references
failing condition
hypothesis summary
test result
reuse decision
repair outcome
```

Do not persist hidden reasoning transcripts.

Update only relevant memory/index records after validated work.

# Metrics

When measurable, runtime-focused evaluations should capture:

- request count;
- tool-call count;
- files inspected;
- irrelevant files inspected;
- stores/datasets scanned;
- queries executed;
- runtime-relevant diagnostic calls;
- time to first concrete runtime failure;
- speculative intervention count;
- failed repair cycles;
- completion/acceptance;
- token/time/cost.

`RUNTIME_RELEVANCE_RATIO` may be measured as:

```text
runtime-relevant diagnostic tool calls
--------------------------------------
all diagnostic tool calls
```

Do not publish a universal threshold before evidence supports one.

# Required outputs

Outputs are conditional, not mandatory ceremony.

Fast path may emit:

- `ECONOMY_GATE_DECISION`
- deterministic evidence refs
- bounded execution/verification evidence

Runtime failure path may emit:

- `RUNTIME_GATE_RESULT`
- canonical entrypoint
- reproduction evidence
- executed path
- first failure
- failing capability
- reuse decision
- Runtime Custom Delta
- non-blocking findings
- same-path retest
- status

Admitted consequential work may additionally require:

- `ENGINEERING_CASE`
- `RESEARCH_PROFILE`
- relevant `INTERNAL_SOFTWARE_MAP` slice
- `SOLUTION_SPACE_BRIEF`
- `GOLDEN_PLAN`
- `CAPABILITY_MAP`
- `CANDIDATE_SET`
- `SOURCE_EVIDENCE`
- `CAPABILITY_COVERAGE_MATRIX`
- `CANDIDATE_EVALUATIONS`
- `REUSE_BLUEPRINT`
- `CUSTOM_DELTA`
- `INTERVENTION_SURFACE`
- `LICENSE_PROVENANCE_DECISIONS`
- `EXECUTION_CONTRACT`
- `EXECUTION_OUTCOME`
- `RECOMPOSITION_EVENT`
- `DECISION_MEMORY_UPDATE`
- `TRAJECTORY_MEMORY_UPDATE`
- `REUSE_INDEX_UPDATE`

Do not generate artifacts that do not materially help the current decision.

# Failure handling

Use explicit failures rather than hallucinated completion.

Runtime evidence failure is not permission to repair speculative code or to `BUILD`.

See `references/failure-codes.md`.

# Evidence status

v0.1.5 is an experimental design release.

The repository preserves:

- v0.1.2 controlled evidence in `EVIDENCE.md`;
- corrected bounded v0.1.3 capability/recovery evidence in `EVIDENCE_V0.1.3.md` and `evals/`.

v0.1.4 Economy Gate and v0.1.5 Runtime Evidence Gate have not yet earned universal cost or outcome claims.

## Guiding principle

> Determinism before inference.  
> Runtime before speculation.  
> Reuse before research.  
> Build only what is missing.  
> Recompose when evidence changes.
