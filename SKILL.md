---
name: spari
description: Evidence-driven software prior-art, composition, economy-gated reuse, and recomposition intelligence for AI engineering agents. Uses deterministic fast matching before inference, admits deeper research only when expected decision value or risk justifies it, reuses persistent repository intelligence, and recomposes when execution evidence invalidates the current path.
license: Apache-2.0
metadata:
  version: "0.1.4"
  status: experimental
  category: software-intelligence
  updated: "2026-09-28"
---

# SPARI

**Build-vs-Borrow, Economy-Gated Composition, and Recomposition for AI Agents**

*Software Prior Art & Reuse Intelligence*

SPARI exists to stop AI agents from rebuilding software that already exists without making the reuse check more expensive than the work it protects.

v0.1.4 adds an economy gate and persistent reuse index in front of the v0.1.3 small-first loop. The default is now: use deterministic evidence first, spend inference only when it can materially change the engineering decision, and preserve evidence-driven recomposition when execution disproves the current path.

SPARI is not a generic project manager, interview framework, search-results generator, code generator, or mandatory tax on every engineering task.

## Operating loop

```text
Raw or qualified engineering context
→ ECONOMY GATE
   → deterministic fast match / persistent index
   → risk override + break-even admission
   ├─ FAST_REUSE / DIRECT_EXECUTION
   └─ SPARI_ADMITTED
        → Engineering Case
        → R0 Recall
        → R1 Local
        → R2 Related Internal
        → R3 Targeted External
        → R4 Broad External
        → Build-vs-Borrow composition
        → Minimal justified Custom Delta + Intervention Surface
        → Bounded execution
        → Evidence checkpoint
        → CONTINUE | ADAPT | RECOMPOSE | STOP
        → Verified outcome
        → Decision + Trajectory Memory
        → Incremental index refresh
```

## Core objective

> Reuse existing engineering evidence and software with the least justified cognitive and execution cost, while preserving the ability to recompose when new evidence changes what is true.

## Core invariants

1. **Do not spend inference to decide whether inference is needed when deterministic evidence can decide first.**
2. Run deterministic fast matching before model-based prior-art analysis where the host can provide the required index/state.
3. Do not launch deep SPARI work when a bounded task can be safely resolved by an exact reusable match or direct execution.
4. Bypass is allowed only when explicit evidence shows that architecture, dependency, provenance, security, public-interface, and recovery risks do not require deeper decisioning.
5. Unknown admission state defaults to the smallest useful SPARI path, not to FULL research.
6. Recall relevant decisions and trajectories before rediscovering them.
7. Inspect the smallest relevant internal evidence before widening externally.
8. Widen search radius only when unresolved uncertainty can materially change composition, Custom Delta, intervention surface, hard-gate outcome, architecture risk, or verification strategy.
9. Source evidence outranks README claims, popularity, rankings, and model memory.
10. Apply hard constraints before qualitative preference.
11. Separate claimed source from verified source.
12. Do not reuse external artifacts without a license/provenance decision.
13. Search failure, index failure, or budget exhaustion never implies that no reusable solution exists.
14. `BUILD` must be justified; it is never the default consequence of missing evidence.
15. Separate composition authority from code execution while keeping execution evidence in the loop.
16. Require structured execution evidence for consequential work rather than accepting narrative claims of completion.
17. Preserve Decision Memory and Trajectory Memory: what was decided and how failed/incomplete paths were escaped.
18. Recomposition is a first-class transition and may override an earlier economy bypass when new execution evidence creates material uncertainty.
19. Preserve valid evidence across recomposition; reopen only the invalidated gap unless the evidence base itself is invalid.
20. Prefer the smallest architecture-consistent intervention that satisfies verified requirements.
21. Do not duplicate work already performed by the host agent, toolchain, IntakeGov, repository index, or prior validated SPARI evidence.
22. Do not publish quantitative savings claims without reproducible measurement.

## Relationship to IntakeGov

SPARI is standalone-capable. IntakeGov is an optional upstream governance layer.

When IntakeGov or another intake system provides qualified context, SPARI consumes it instead of repeating qualification. The Economy Gate should also consume upstream estimates, risk flags, known project boundaries, and prior-attempt evidence when available.

No upstream flag may silently erase a hard safety, license, provenance, architecture, or recovery requirement. Conversely, SPARI must not repeat upstream work merely because it can.

See `references/intakegov-handoff.md`.

# Economy Gate

The Economy Gate runs before model-heavy prior-art reasoning.

Its purpose is not to decide the final architecture. It decides how much SPARI is justified for the current work slice.

## Gate inputs

Use deterministic/host-provided evidence where available:

- task/work-slice identity and scope;
- repository/base revision;
- touched or likely-touched capability/path;
- existing dependency and manifest evidence;
- exact symbol/export/type/interface matches;
- route/API/schema identifiers;
- tests and canonical authorities;
- structural fingerprints such as AST/signature hashes;
- prior Decision/Trajectory keys;
- prior failures/recomposition triggers;
- optional caller estimates of execution cost/time/tokens;
- configured risk and break-even policy.

Do not invent missing numeric estimates.

## Deterministic fast match

The first pass should require zero model inference when the host environment supports it.

Preferred evidence includes:

```text
exact capability key
exact symbol/export name
exact type/interface signature
manifest/lockfile dependency
route/API/schema key
AST/structural fingerprint
canonical authority mapping
validated Decision Memory key
validated Trajectory Memory key
```

Optional precomputed semantic/vector retrieval may be used as cached infrastructure, but its results are candidates, not final engineering judgements. The gate must not rebuild embeddings or repository semantics for every task.

## Gate outcomes

- `FAST_REUSE` — a fresh, compatible, validated reusable path is deterministically identified; use it with bounded verification.
- `DIRECT_EXECUTION` — the work is a bounded micro-task with no material reuse/architecture/dependency/provenance/security/recovery uncertainty.
- `SPARI_PREFLIGHT` — small uncertainty remains; admit the minimum R0/R1 path and escalate only if needed.
- `SPARI_TARGETED` — a known candidate/capability requires focused evaluation up to R3.
- `SPARI_FULL` — consequential or solution-family uncertainty justifies R4 and independent evaluation.
- `RECOMPOSE` — execution evidence has invalidated the current path; reopen only the relevant gap.

See `references/economy-gate.md` and `schemas/economy-gate.schema.json`.

## Risk overrides

Do not bypass merely because the patch is small when the task introduces or changes a material boundary, including:

- new dependency or externally sourced code;
- license/provenance uncertainty;
- security-sensitive behavior;
- public API/interface or schema change;
- data model or persistence authority change;
- new service/module/architecture authority;
- irreversible/destructive operation;
- repeated failed attempts;
- contradiction between current evidence and the active plan;
- unknown or stale exact-match evidence.

Risk override should normally route to the smallest adequate SPARI profile, not automatically to FULL.

## Break-even admission

Inference-based SPARI work is justified when at least one of these is true:

1. unresolved decision value can materially change composition or prevent meaningful rework;
2. a configured risk override requires evidence before execution;
3. prior failures or contradictory evidence require recomposition;
4. expected execution/rework burden exceeds the configured cost of the additional check.

There is no hard-coded universal token threshold in v0.1.4. Deployments may configure one, but public SPARI does not invent a number unsupported by evidence.

# Persistent Reuse Index

SPARI must prefer a persistent, incrementally refreshed index over reconstructing repository knowledge in model context for every intake.

The index may contain:

- repository/workspace revision;
- manifests and lockfiles;
- packages/modules/services;
- symbols, exports, types, interfaces, routes, schemas;
- dependency edges;
- architecture authorities/boundaries;
- capability-to-code mappings;
- test/evidence references;
- structural fingerprints;
- installed third-party dependencies;
- validated Decision/Trajectory references;
- optional cached embedding references.

The index stores evidence pointers and compact metadata. It is not a hidden reasoning transcript and not a substitute for source verification when freshness or compatibility is material.

Incrementally refresh affected entries when revisions, manifests, lockfiles, architecture boundaries, or indexed files change materially.

See `references/persistent-index.md` and `schemas/reuse-index.schema.json`.

# Research depth

The Economy Gate is admission control. Search radius begins only after SPARI is admitted.

- `R0_RECALL` — relevant Decision/Trajectory Memory;
- `R1_LOCAL` — current code/tests/manifests/dependencies and relevant indexed slice;
- `R2_RELATED_INTERNAL` — analogous modules/history/previous fixes/internal repair ingredients;
- `R3_TARGETED_EXTERNAL` — focused GitHub/PyPI/standards/reference search;
- `R4_BROAD_EXTERNAL` — broader solution-space discovery, research swarm, comparative evaluation.

`PREFLIGHT`, `TARGETED`, and `FULL` remain ceilings/operating ranges, not mandatory pipelines.

Escalate only when the unresolved question can materially change the decision. Narrow again after it is resolved.

See `references/research-depth.md`.

# Research budget

SPARI has two different cost controls:

1. `ADMISSION_CONTROL` — should model-based SPARI work run at all, and at what maximum profile?
2. `RESEARCH_BUDGET` — once admitted, how much research resource may be consumed?

`QUALITY_STOP` remains evidence convergence. `RESOURCE_STOP` remains configured exhaustion.

Possible research controls include:

- `max_scouts`;
- `max_candidates_screened`;
- `max_candidates_deep_inspected`;
- `max_proofs_of_fit`;
- `max_strong_model_escalations`;
- optional `max_tokens`;
- optional `max_cost`.

Budget exhaustion yields `RESEARCH_BUDGET_EXHAUSTED` + `RESEARCH_INCOMPLETE`, never automatic `BUILD`.

See `references/research-budget.md`.

# Engineering Case and recall

Create a compact `ENGINEERING_CASE` only after SPARI is admitted or a recomposition trigger requires it. Do not force a full case artifact for a deterministic fast reuse/direct-execution bypass.

Where applicable preserve:

- outcome / affected capability;
- observed signal/failure;
- known evidence and constraints;
- material unknowns;
- current hypotheses;
- current composition;
- prior attempts and contradicting evidence.

Before fresh discovery, query only relevant Decision Memory and Trajectory Memory. Do not inject the full historical store.

See `references/memory-schema.md`.

# Internal Software Map

Internal software is first-class prior art.

The persistent reuse index provides the cheap lookup surface. The `INTERNAL_SOFTWARE_MAP` provides the richer capability/dependency/architecture evidence when the task needs it.

Do not rebuild the full map for every task. Retrieve the smallest relevant slice and inspect source only where the evidence must be refreshed or deepened.

See `references/internal-software-map.md`.

# External prior art

SPARI v0.x prioritizes:

1. existing internal software;
2. GitHub;
3. PyPI.

External research is not a reflex. Use R3/R4 only after deterministic/indexed/internal evidence leaves a material gap.

For serious package candidates resolve where possible:

- exact package/version;
- distribution artifact/hash;
- claimed source;
- verified source where possible;
- release/tag/commit;
- runtime compatibility;
- dependencies;
- provenance/attestation.

Do not collapse `CLAIMED_SOURCE` into `VERIFIED_SOURCE`.

# Broad Recon and clarification

Broad Recon is an escalation for solution-family uncertainty, not a mandatory first step.

When needed, expand semantically:

```text
literal request
→ underlying capability
→ parent solution category
→ adjacent solution classes
→ complete systems solving the same outcome
```

After recon, ask only questions whose answers materially distinguish discovered solution families. Do not conduct a generic interview.

See `references/broad-recon.md`.

# Golden Plan and capability map

For consequential work, establish the confirmed goal, scope, non-goals, capabilities, constraints, environment, success criteria, known facts, unknowns, and allowed scope refinement.

Deep Research may refine technical shape but may not silently replace confirmed intent.

Capabilities remain the unit of discovery, comparison, composition, and Custom Delta accounting.

See `references/golden-plan.md`.

# Deep Research and evaluation

Deep Research compares concrete reusable software only when consequential uncertainty remains.

Prefer cheap breadth and strong judgement. Scouts collect evidence; they do not independently finalize architecture.

Shortlisted candidates should be inspected beyond README claims where access permits. Apply hard gates before preferences. Use technical evaluation and contrarian review for consequential decisions.

See `references/deep-research.md`, `references/research-swarm.md`, and `references/evaluation-composition.md`.

# Build-vs-Borrow composition

Serious candidates may receive:

- `ADOPT`
- `ADAPT`
- `COMPOSE`
- `REFERENCE`
- `REJECT`
- `BUILD`

Selected roles may include:

- `PRODUCT_BASE`
- `DEPENDENCY`
- `SOURCE_COMPONENT`
- `REFERENCE_PATTERN`
- `API_INTEGRATION`
- `VENDORED_COMPONENT`
- `CUSTOM_IMPLEMENTATION`

Produce a concrete `REUSE_BLUEPRINT`, not a winner list.

`CUSTOM_DELTA` is only the capability that still requires custom implementation after internal/external composition. Each item should explain why existing evidence is insufficient.

# License and provenance

Track declared/detected license and effective reuse decision separately from source verification.

Before incorporation, resolve reuse to one of:

- `REFERENCE_ONLY`
- `PATTERN_ONLY`
- `DEPENDENCY_ALLOWED`
- `CODE_REUSE_ALLOWED`
- `REVIEW_REQUIRED`
- `DENIED`

No reuse decision means no reuse.

See `references/license-provenance.md`.

# Execution boundary

SPARI decides what should exist; an execution agent performs the code changes.

For consequential admitted work, emit an executor-agnostic `EXECUTION_CONTRACT` with composition reference, planned Custom Delta, required reuse/retention, allowed substitutions, prohibited scope changes, hard constraints, verification requirements, evidence expectations, and base revision where available.

Fast-path/direct-execution cases may use a reduced bounded instruction if a full contract would cost more than the task and no risk override requires it.

Execution evidence may trigger:

- `CONTINUE`
- `ADAPT`
- `RECOMPOSE`
- `STOP`

See `references/execution-boundary.md`.

# Recomposition

Recompose when new evidence materially weakens or falsifies the current path, for example:

- verification contradicts the active hypothesis;
- dependency/integration assumptions fail;
- a previously unknown internal capability changes the solution;
- implementation starts creating parallel architecture or unjustified Custom Delta;
- repeated local repairs do not address root cause;
- hard-gate evidence changes;
- a materially stronger composition becomes available.

A recomposition event must record the trigger, invalidated assumptions, retained evidence, abandoned path, newly retrieved ingredients, composition change, Custom Delta/intervention change, and required verification.

Do not restart all research from zero unless the evidence base itself is invalid.

See `references/closed-loop.md`.

# Structured execution outcome

For consequential work, require `EXECUTION_OUTCOME` rather than prose-only completion.

Where applicable record executor, repository, base/result revision, planned vs actual reuse, dependencies, files changed, intervention surface, recomposition evidence, planned vs actual Custom Delta, verification results, abandoned components, unexpected custom code, deviations, and evidence references.

Outcome states:

- `VALIDATED`
- `VALIDATED_WITH_LIMITATIONS`
- `REQUIRES_RECOMPOSITION`
- `REJECTED_AFTER_IMPLEMENTATION`
- `UNKNOWN_OUTCOME`

A green test suite alone does not prove Build-vs-Borrow adherence.

# Memory and index update

Decision Memory answers what was decided and what happened.

Trajectory Memory answers how the system escaped or failed to escape the problem.

After validated work, update only the relevant memory/index records. Do not rebuild the entire store/index unless invalidation requires it.

# Required outputs

Outputs are conditional, not mandatory ceremony.

Fast path may emit only:

- `ECONOMY_GATE_DECISION`
- deterministic evidence references;
- bounded execution/verification evidence;
- optional memory/index update.

Admitted work may additionally require:

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

Use explicit failures rather than hallucinated completion. An unavailable/stale index falls back to the smallest source-backed local inspection; it does not force FULL research and does not justify `BUILD`.

See `references/failure-codes.md`.

# Evidence status

v0.1.4 is an experimental design release. Its Economy Gate and persistent-index cost claims have not yet been validated by a dedicated controlled evaluation.

The repository preserves v0.1.2 controlled evidence in `EVIDENCE.md` and v0.1.3 bounded capability/recovery evidence in `EVIDENCE_V0.1.3.md` and `evals/`.

Do not claim a universal token-saving percentage, universal capability lift, or model-equivalence effect.

## Guiding principle

> Determinism before inference.  
> Reuse before research.  
> Research only while decision value exceeds its cost or risk requires it.  
> Compose the smallest evidence-backed solution.  
> Recompose when reality invalidates the path.
