---
name: spari
description: Source-attested software prior-art and reuse control for AI engineering agents. Requires a decision question before broad search, a Build-vs-Borrow decision before consequential implementation, deterministic evidence before inference, runtime-path diagnosis before repair, and the smallest justified custom delta.
license: Apache-2.0
metadata:
  version: "0.1.7"
  status: experimental
  category: software-intelligence
  updated: "2026-10-07"
---

# SPARI

**Build-vs-Borrow, Runtime-Evidence, Composition, and Recomposition for AI Agents**

*Software Prior Art & Reuse Intelligence*

SPARI exists to stop AI agents from rebuilding software that already exists, debugging code that does not actually run, remaining trapped in contradicted solution paths, and executing stale local SPARI policy while claiming current authoritative source.

SPARI is not a generic project manager, search-results generator, code generator, debugger, observability platform, or mandatory tax on every engineering task.

## Operating loop

~~~text
SPARI invoked
→ AUTHORITY ACCESS PLAN
→ SOURCE ATTESTATION GATE
   ├─ CURRENT_ATTESTED / permitted PINNED_ATTESTED
   └─ stale / unresolved / conflict → stop current-version-sensitive work
→ Raw or qualified engineering context
→ ECONOMY GATE
   ├─ FAST_REUSE / DIRECT_EXECUTION
   │    → minimal BYPASS decision record
   │    → EXECUTION_AUTHORITY = GRANTED
   └─ consequential decisioning
        → PRE-EXECUTION DECISION GATE
        → DEFINE capability + material constraints
        → DECISION QUESTION
        → SEARCH PLAN
        → observed failure?
           ├─ YES → RUNTIME EVIDENCE GATE
           │        → canonical entrypoint
           │        → reproduce
           │        → executed path
           │        → first concrete failure
           │        → failing capability
           └─ NO  → continue planned retrieval
        → targeted deterministic/internal retrieval first
        → external search only when the decision still requires it
        → COMPARE
        → ADOPT | ADAPT | COMPOSE | REFERENCE | REJECT | BUILD | BLOCKED
        → BUILD requires explicit justification + bounded Custom Delta
        → EXECUTION_AUTHORITY = GRANTED
        → bounded execution
        → same-path / required verification
        → CONTINUE | ADAPT | RECOMPOSE | STOP
→ Decision + Trajectory Memory
→ incremental index refresh only where justified
~~~

The controller is intentionally sparse. SPARI should reuse host-native repo maps, symbol search, skills, MCP tools, indexes, and search providers instead of rebuilding them inside the decision layer.

## Core objective

> Determine what actually runs, reuse what already works, and build only the smallest missing piece that evidence proves necessary.

## Core invariants

1. **Source authority before local cache.**
2. **Determinism before inference.**
3. **Think/define before broad search.**
4. **No broad search or indexing without a named decision question.**
5. **No consequential implementation before a recorded reuse decision.**
6. **Execution authority is denied by default.**
7. **BUILD is a justified decision, never the fallback for missing evidence.**
8. **Runtime before repository speculation.**
9. **Trace before repair.**
10. **Reuse before external research.**
11. **Recompose when evidence changes.**
12. A local SPARI copy is a cache, not current truth, until attested against the configured authority.
13. For SPARI itself, tonnestate/SPARI branch main is the current authority; a release tag is optional metadata, not a prerequisite.
14. Do not claim or evaluate a SPARI version without evidence of the exact authoritative revision/instruction surface actually in use.
15. Do not spend model inference to decide whether inference is needed when deterministic evidence can decide first.
16. Do not launch deep SPARI work when a bounded task can be safely resolved by FAST_REUSE or DIRECT_EXECUTION.
17. DIRECT_EXECUTION and FAST_REUSE still produce a compact BYPASS decision record stating why deeper prior-art work cannot change the bounded intervention.
18. A non-trivial search plan must name the evidence source, query/lookup, decision impact, and stop condition before retrieval.
19. R0–R4 are selectable search radii, not a mandatory pipeline.
20. Do not build or refresh a broad repository index merely because a repository exists.
21. Reuse host-provided repo maps, indexes, skills, symbol search, MCP tools, and search capabilities when they already provide the needed evidence.
22. An observed failure activates Runtime Evidence Gate discipline before repair mutation.
23. The actual executed path outranks repository proximity, naming similarity, legacy relevance, README claims, and model memory.
24. A file not shown to participate in the observed runtime path is out of repair scope unless evidence connects it to the root cause.
25. Identify the first concrete failing condition before widening the repair.
26. Every additional diagnostic/research query must be able to change the current technical decision.
27. Interesting inconsistencies that cannot change the current decision are FUTURE_WORK, not automatic scope.
28. Do not create a new service, adapter, contract, store, schema, CLI mode, rebuild path, or fallback architecture without evidence that the required capability cannot be satisfied by the supported composition.
29. Search failure, index failure, runtime-evidence failure, or budget exhaustion never implies that no reusable solution exists.
30. Preserve valid evidence across recomposition; reopen only the invalidated gap unless the evidence base itself is invalid.
31. Prefer the smallest architecture-consistent intervention that satisfies verified requirements.
32. Re-run the identical canonical path after a repair when possible.
33. Do not duplicate work already performed by the host, IntakeGov, repository index, prior validated SPARI evidence, or runtime instrumentation.
34. Persist inspectable engineering evidence and decision summaries, not hidden chain-of-thought.
35. Do not publish quantitative savings or capability claims without reproducible measurement.
36. Reconstruct external application behavior only for a bounded named decision and permitted observation surface; evidence of UI similarity is not evidence of hidden implementations.
37. Do not exclude unverified, skipped, inaccessible, inferred, or partial REQUIRED behavior from parity denominators or acceptance gates.

# Source Attestation Gate

Source Attestation Gate runs before Economy Gate.

For SPARI itself:

```text
AUTHORITY_REPOSITORY = https://github.com/tonnestate/SPARI
AUTHORITY_REF        = refs/heads/main
```

`main` is the current source of truth.

## Authority Access Plan

Do not equate a tool/transport with the authority.

On first source resolution in a session, identify the available approved routes and choose the strongest working route without repeatedly retrying known-dead transports.

Preferred route classes:

1. host-native GitHub connector/API;
2. direct GitHub API/fetch capability;
3. shell Git remote access;
4. direct GitHub page/fetch only when it exposes an exact commit identity.

Search-engine snippets are discovery evidence, not authoritative current-main proof.

If `git ls-remote` fails but a GitHub connector/API is available:

```text
GIT_REMOTE_TRANSPORT_FAILED
```

not:

```text
GITHUB_UNAVAILABLE
```

`GITHUB_UNAVAILABLE` or `SOURCE_UNRESOLVED` requires that all approved authority-resolution routes are unavailable or unable to resolve the required authority state.

Cache the resulting route as `AUTHORITY_ACCESS_PLAN` for the session and reuse it until evidence invalidates it.

## Resolve current main

Record:

- repository;
- authoritative ref;
- resolved main SHA;
- transport used;
- canonical `SKILL.md` metadata version;
- canonical `SKILL.md` content hash when available;
- canonical release manifest/hash evidence when available;
- resolution timestamp/evidence refs.

Do not require a version tag when branch `main` is configured as authority.

A missing `refs/tags/vX.Y.Z` is not a source-resolution failure when `refs/heads/main` resolves successfully.

## Attest the installed surface

The installed/local SPARI directory is evidence about what is loaded, not evidence about what is current.

Preferred attestation:

```text
valid installed Git revision == resolved main SHA
```

If the installed skill is a copied directory without trustworthy Git metadata, use content evidence:

```text
installed SKILL.md hash
+
installed referenced active files / release-manifest checks
+
canonical hashes from resolved main
```

A missing, broken, or empty local `.git` directory must not be promoted to a revision claim.

Attestation states:

- `CURRENT_ATTESTED` — installed active surface matches resolved current main under the declared method;
- `PINNED_ATTESTED` — installed surface matches an exact previously/explicitly frozen SHA permitted by the task/eval contract;
- `PARTIAL_ATTESTATION` — only part of the active surface could be compared;
- `STALE_LOCAL_COPY` — installed surface is proven older/different from required authority state;
- `INSTALLATION_UNATTESTED` — authority is known but installed active surface cannot be proven;
- `SOURCE_UNRESOLVED` — current authority state cannot be resolved;
- `SOURCE_CONFLICT` — authoritative evidence routes disagree and cannot be reconciled.

Only the states permitted by the current task/contract may proceed.

Normal "use current SPARI" requires `CURRENT_ATTESTED`.

A version-sensitive evaluation may use `PINNED_ATTESTED` only if its contract explicitly froze that exact SHA.

## Offline/failure behavior

If current GitHub `main` cannot be resolved:

- do not promote a cached copy to current;
- report its exact known/pinned identity if attested;
- do not invent freshness;
- stop work whose contract requires current main;
- continue only work explicitly permitted against the known pinned revision.

## Evaluation freeze

For controlled evaluation:

1. resolve current main at evaluation start;
2. attest the evaluation surface;
3. freeze that exact SHA in the manifest;
4. run comparable arms against that same frozen revision.

Do not silently refresh one arm mid-experiment.

If policy requires continuously-current main rather than a frozen evaluation revision, a main change invalidates the comparable run set.

## Bootstrap boundary

Self-attestation begins after some SPARI instructions have already been loaded.

Therefore:

```text
SPARI_SELF_ATTEST
!=
HOST_LOADER_ATTEST
```

A hard guarantee that stale SPARI can never be activated requires host/installer/skill-loader enforcement before skill activation.

v0.1.7 preserves the source/transport/attestation contract and fails closed once invoked; it does not claim to control every host loader.

See `references/source-attestation-gate.md` and `schemas/source-attestation.schema.json`.

# Economy Gate

The Economy Gate runs after Source Attestation Gate has produced an attestation state permitted by the current task/contract and before model-heavy prior-art reasoning.

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

Any path other than a deterministically justified FAST_REUSE or DIRECT_EXECUTION enters Pre-Execution Decision Gate before non-trivial retrieval or consequential mutation. Observed failures use Runtime Evidence Gate to establish the failing capability/path, but repair mutation remains denied until the reuse decision grants execution authority.

See `references/economy-gate.md` and `schemas/economy-gate.schema.json`.

# Pre-Execution Decision Gate

Any consequential Build-vs-Borrow task enters this gate before broad search or implementation.

The gate exists to prevent the common agent trajectory:

~~~text
intake
→ index everything
→ search widely
→ consolidate unrelated context
→ prefer a fresh implementation
→ justify BUILD afterward
~~~

The required trajectory is:

~~~text
DEFINE
→ DECISION QUESTION
→ SEARCH PLAN
→ TARGETED RETRIEVAL
→ COMPARE
→ REUSE DECISION
→ EXECUTION AUTHORITY
→ IMPLEMENT
~~~

## Required decision state

Record only the compact, inspectable decision state:

- required capability;
- material constraints;
- known state;
- material unknowns;
- one current decision question;
- planned evidence sources/lookups;
- stop condition.

Do not persist hidden chain-of-thought.

## Search permission

Before a non-trivial search, index build, repo-map generation, source scan, or external query:

~~~text
What engineering decision can this operation change?
~~~

If there is no concrete answer:

~~~text
DO_NOT_QUERY
~~~

Broad search or broad indexing additionally requires evidence that narrower/existing sources cannot resolve a material solution-family uncertainty.

## Reuse decision

Before consequential mutation choose:

- ADOPT
- ADAPT
- COMPOSE
- REFERENCE
- REJECT
- BUILD
- FAST_REUSE
- DIRECT_EXECUTION
- BLOCKED

BUILD requires explicit evidence-based justification plus a bounded Custom Delta. "Nothing perfect found" is not sufficient.

## Execution authority

Default:

~~~text
EXECUTION_AUTHORITY = DENIED
~~~

Grant only when the applicable decision is complete.

For consequential work this requires:

- capability defined;
- decision question defined;
- search plan completed or validly bypassed;
- relevant candidates/evidence evaluated;
- reuse decision recorded;
- Custom Delta bounded where custom work remains;
- hard constraints preserved.

If later evidence can materially change the reuse decision, authority returns to DENIED for the affected scope and control returns to ADAPT or RECOMPOSE.

See references/pre-execution-decision-gate.md and schemas/pre-execution-decision.schema.json.

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

`PREFLIGHT`, `TARGETED`, and `FULL` are ceilings/operating ranges, not mandatory pipelines. R0–R4 are selectable evidence radii chosen by the current decision question; do not walk them sequentially by default.

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

# Application Reconstruction (optional)

When the named engineering decision depends on reconstructing a specific application's observable workflows, use `references/application-reconstruction.md` **after** the normal Source Attestation, Economy and Pre-Execution Decision gates. Scope public/permitted observations to the decision, inventory screens/flows/features with provenance, and reuse the existing SPARI Build-vs-Borrow controller and host executor. This is not a mandatory phase for normal coding or repair.

Behavior-parity evidence must keep every REQUIRED feature in the denominator; missing, skipped, inferred, inaccessible and untested items cannot be counted as verified. Structural screenshot similarity and regex-classified reviews are supporting signals only. Do not introduce a parallel builder, deployer, policy controller, or index.

For significant behavior-parity claims, use `references/application-conformance.md`: a scoped state-transition model, evidence-linked requirements, the deterministic `tools/application_conformance.py` gate and host-controlled execution receipts. An unverified or unobserved requirement never becomes PASS. Its machine result does not override SPARI execution authority or other hard gates.

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
- scoped `APPLICATION_BEHAVIOR_MAP` / `BEHAVIOR_PARITY_MATRIX` only when an external application's observable behavior materially informs the decision
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

Source-resolution/attestation failure is not permission to treat a stale local skill as current. Runtime evidence failure is not permission to repair speculative code or to `BUILD`.

See `references/failure-codes.md`.

# Evidence status

v0.1.6 is an experimental design release.

The repository preserves:

- v0.1.2 controlled evidence in `EVIDENCE.md`;
- corrected bounded v0.1.3 capability/recovery evidence in `EVIDENCE_V0.1.3.md` and `evals/`.

v0.1.4 Economy Gate, v0.1.5 Runtime Evidence Gate, and v0.1.6 Source Attestation/Authority Access have not yet earned universal cost or outcome claims.

## Guiding principle

> Source authority before local cache.  
> Determinism before inference.  
> Runtime before speculation.  
> Reuse before research.  
> Build only what is missing.  
> Recompose when evidence changes.
