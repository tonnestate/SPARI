# SPARI

**Economy-Gated Prior-Art, Composition and Recomposition for AI Engineering Agents**

*Software Prior Art & Reuse Intelligence*

> Determinism before inference. Reuse before research. Recompose when evidence changes. Build only what is missing.

SPARI makes existing software and engineering evidence the starting point of AI engineering instead of an afterthought — without making the reuse check more expensive than the work it protects.

v0.1.4 adds an **Economy Gate** and **Persistent Reuse Index** in front of the v0.1.3 small-first loop.

The result is one adaptive system:

```text
small / known task
→ exact evidence
→ direct reuse or execution

uncertain / consequential task
→ progressively deeper SPARI

failed / contradicted path
→ evidence-driven recomposition
```

SPARI remains experimental. v0.1.4 does not claim a universal token-saving percentage or universal capability lift.

---

## Why SPARI exists

AI coding agents can produce code quickly. They are worse at proving that the code should exist, at reusing internal software consistently, and at abandoning a plausible solution after reality contradicts it.

Without explicit discipline, a request can become:

```text
request
→ custom code
→ helpers
→ parallel abstraction
→ patches
→ retries
→ rediscover existing solution later
```

SPARI changes the default:

```text
request
→ cheap exact evidence first
→ reuse/direct execution when justified
→ deeper prior-art reasoning only when decision value or risk justifies it
→ compose smallest justified intervention
→ execute with evidence checkpoints
→ recompose when evidence invalidates the path
→ remember the decision and recovery trajectory
```

Custom code is the justified remainder, not the starting assumption.

---

# v0.1.4: Economy before cognition

The main lesson from the v0.1.2/v0.1.3 evidence is not “research more”.

It is:

> **Pay for SPARI only when SPARI can plausibly change the engineering decision or prevent meaningful risk/rework.**

v0.1.4 therefore introduces a pre-inference admission layer.

```text
Raw / qualified work slice
        ↓
ECONOMY GATE
        ↓
Deterministic exact/index lookup
        ↓
Risk override + break-even admission
        ├── FAST_REUSE
        ├── DIRECT_EXECUTION
        ├── SPARI_PREFLIGHT
        ├── SPARI_TARGETED
        ├── SPARI_FULL
        └── RECOMPOSE
```

See [`references/economy-gate.md`](references/economy-gate.md).

---

# Deterministic Fast Path

Where the host environment supports it, SPARI checks structured evidence before model inference:

```text
capability key
symbol / export
function / class / type / interface signature
manifest / lockfile dependency
API route / schema identifier
canonical architecture authority
AST / structural fingerprint
validated decision-memory key
validated trajectory-memory key
```

No match is not proof that no reusable solution exists. It only means the cheap exact layer did not resolve the case.

Cached semantic/vector retrieval may help candidate recall, but it is not a final reuse decision and should not be regenerated for every intake.

---

# The Micro-Task Rule

A reuse engine must not spend more than the work it protects without a reason.

A bounded micro-task may bypass model-heavy SPARI when evidence shows:

- local scope is known;
- no new dependency/external code is introduced;
- no public interface/schema/data authority changes;
- no new architecture authority is created;
- no security/license/provenance decision is required;
- no repeated failure or contradictory evidence exists;
- no unresolved Build-vs-Borrow decision is likely to change the intervention.

Then the gate may return:

```text
FAST_REUSE
```

or:

```text
DIRECT_EXECUTION
```

This is not a universal “small patch = safe” rule. A two-line authentication-schema change can be more consequential than a hundred-line internal refactor.

---

# Risk overrides

A task cannot bypass required evidence merely because it is small.

Risk overrides include:

- new dependency or vendored external code;
- unclear license/provenance;
- security-sensitive behavior;
- public API/interface/schema changes;
- persistent data-model/authority changes;
- new architecture/service/module authority;
- destructive/irreversible operations;
- repeated failed attempts;
- contradiction between current evidence and the active plan;
- stale/unverified fast-match evidence.

Risk should route to the **smallest adequate SPARI profile**, not automatically to FULL.

---

# Break-even admission

SPARI does not hard-code a universal token threshold.

Model-based SPARI work is justified when:

1. unresolved decision value can materially change composition, Custom Delta, intervention surface, hard-gate outcome, architecture risk, or verification;
2. configured risk policy requires evidence before execution;
3. prior failures or contradictory evidence require recomposition;
4. expected execution/rework burden exceeds a deployment's configured cost of the additional check.

When cost estimates exist, preserve their provenance. When they do not, use explicit qualitative classes instead of invented precision.

This distinction matters because the historical evidence contains both expensive no-uplift runs and bounded positive recovery/reuse signals.

---

# Persistent Reuse Index

SPARI should not reconstruct repository knowledge inside an LLM prompt on every task.

v0.1.4 defines a persistent, incrementally refreshed `REUSE_INDEX` that can contain compact evidence about:

- repositories and revisions;
- manifests/lockfiles;
- modules/services;
- symbols/exports/types/interfaces;
- API routes and schemas;
- dependency edges;
- architecture authorities/boundaries;
- capability-to-code mappings;
- tests/evidence references;
- structural fingerprints;
- installed dependencies;
- Decision/Trajectory references;
- optional cached embedding references.

The model receives only the relevant result slice, not the full index.

See [`references/persistent-index.md`](references/persistent-index.md) and [`schemas/reuse-index.schema.json`](schemas/reuse-index.schema.json).

---

# Internal software is prior art

SPARI keeps the v0.1.2/v0.1.3 principle that software you already own is first-class prior art.

v0.1.4 distinguishes:

```text
REUSE_INDEX
cheap persistent lookup
        ↓
INTERNAL_SOFTWARE_MAP
richer capability / dependency / architecture evidence when needed
```

A full map is no longer implied for every task. Exact evidence can resolve cheap cases; ambiguous/stale cases load or refresh only the relevant map slice.

See [`references/internal-software-map.md`](references/internal-software-map.md).

---

# Adaptive search radius

Admission and research depth are different decisions.

After SPARI is admitted:

```text
R0_RECALL
relevant Decision + Trajectory Memory

R1_LOCAL
code, tests, manifests, dependencies, relevant indexed/map slice

R2_RELATED_INTERNAL
analogous modules, history, previous fixes, internal repair ingredients

R3_TARGETED_EXTERNAL
focused GitHub / PyPI / standards / references

R4_BROAD_EXTERNAL
broader solution-space discovery + comparative research
```

`PREFLIGHT`, `TARGETED`, and `FULL` are ceilings/operating ranges rather than mandatory workflows.

Move outward only while unresolved uncertainty can materially change the decision.

See [`references/research-depth.md`](references/research-depth.md).

---

# IntakeGov + SPARI

SPARI is standalone-capable. IntakeGov is an optional upstream governance layer.

When IntakeGov provides qualified context, SPARI consumes it instead of repeating qualification. The Economy Gate should also consume known project boundaries, risk flags, prior-attempt evidence, and cost estimates when supplied.

A useful combined flow is now:

```text
IntakeGov / equivalent context
        ↓
SPARI Economy Gate
        ├── bypass / fast reuse
        └── admitted SPARI
              ↓
        adaptive R0–R4
```

This prevents a cheap upstream intake from being followed automatically by expensive prior-art ceremony.

---

# Broad Recon is an escalation, not a reflex

If local/internal/targeted evidence leaves material solution-family uncertainty, SPARI can widen semantic scope:

```text
literal request
→ underlying capability
→ parent solution category
→ adjacent solution classes
→ complete systems solving the same outcome
```

It may discover broader alternatives, but it may not silently convert them into confirmed user requirements.

Broad Recon is useful when the solution family is genuinely uncertain. It is wasteful when an exact validated local path already solves the case.

---

# Fewer questions, better questions

SPARI does not start with a long interview.

Questions are justified only when answers can materially distinguish evidence-backed solution paths.

This remains **evidence-informed clarification**, not generic requirements interrogation.

---

# GitHub and PyPI

SPARI v0.x deliberately prioritizes:

```text
existing internal software
GitHub
PyPI
```

Serious external candidates should be linked where possible across exact package/version, artifact/hash, claimed source, verified source, release/tag/commit, compatibility, dependencies, license, and provenance.

`CLAIMED_SOURCE` is not `VERIFIED_SOURCE`.

`PROVENANCE_VERIFIED` does not mean secure or suitable.

Other ecosystems remain extension points unless a host explicitly extends configured scope.

---

# Build-vs-Borrow is composition

SPARI does not exist to produce recommendation lists.

A useful result is a composition:

```text
KEEP_INTERNAL
existing persistence authority

BASE
existing internal/GitHub component

DEPENDENCY
specific package

REFERENCE_ONLY
useful architecture pattern

CUSTOM
only the unavoidable adapter/gap
```

Candidate decisions include:

```text
ADOPT
ADAPT
COMPOSE
REFERENCE
REJECT
BUILD
```

`BUILD` is never the default result of missing evidence.

---

# Custom Delta and Intervention Surface

`CUSTOM_DELTA` identifies only the capabilities still requiring custom implementation after reuse composition.

`INTERVENTION_SURFACE` records how much of the existing system must actually change.

SPARI prefers the smallest architecture-consistent intervention when required qualities are otherwise equivalent. It does not optimize for fewest lines at the expense of correctness.

---

# Source beats README

README claims, stars, download counts, rankings, and marketing pages are discovery signals, not proof.

Consequential finalists should be inspected at the source/evidence level where access permits: architecture, relevant modules/APIs, extension points, tests, maintenance, dependencies, integration burden, security, license scope, and provenance.

---

# Hard gates before preference

Mandatory constraints such as runtime, deployment, architecture, security, license, and provenance are applied before popularity or qualitative preference.

A popular candidate that violates a hard constraint does not win.

---

# License and provenance

SPARI separates:

```text
DECLARED_LICENSE
DETECTED_LICENSE
EFFECTIVE_REUSE_DECISION
```

and source state:

```text
SOURCE_UNKNOWN
SOURCE_CLAIMED
SOURCE_VERIFIED
SOURCE_CONFLICT
```

Before incorporation, external reuse resolves to one of:

```text
REFERENCE_ONLY
PATTERN_ONLY
DEPENDENCY_ALLOWED
CODE_REUSE_ALLOWED
REVIEW_REQUIRED
DENIED
```

Unknown or conflicting permission fails closed.

---

# Research budget

v0.1.4 has two resource controls:

```text
ADMISSION CONTROL
Should model-heavy SPARI run at all?
```

and:

```text
RESEARCH BUDGET
Once admitted, how much research may it consume?
```

Research still separates `QUALITY_STOP` from `RESOURCE_STOP`.

Budget exhaustion yields:

```text
RESEARCH_BUDGET_EXHAUSTED
→ RESEARCH_INCOMPLETE
```

Never:

```text
budget exhausted
→ nothing exists
→ BUILD
```

See [`references/research-budget.md`](references/research-budget.md).

---

# SPARI decides; coding agents execute

SPARI is not another coding agent.

For consequential admitted work:

```text
SPARI composition
→ Reuse Blueprint + Custom Delta
→ executor-agnostic EXECUTION_CONTRACT
→ Claude Code / Codex / Aider / other executor
→ evidence checkpoint
→ CONTINUE | ADAPT | RECOMPOSE | STOP
→ EXECUTION_OUTCOME
```

Fast-path micro-tasks may use reduced bounded execution instructions when a full contract would cost more than the work and no risk override requires it.

A green test suite is useful evidence, but it does not by itself prove Build-vs-Borrow adherence.

---

# Recomposition: strategy repair

Recomposition is the central v0.1.3 mechanism preserved by v0.1.4.

When execution evidence invalidates the current path, SPARI should not blindly retry and should not restart all research from zero.

```text
active hypothesis
→ execution / inspection
→ contradictory evidence
→ invalidate only what failed
→ retain still-valid evidence
→ retrieve only the new gap
→ recompose
→ verify again
```

A task that entered through `DIRECT_EXECUTION` can still escalate to `RECOMPOSE` if reality changes.

See [`references/closed-loop.md`](references/closed-loop.md).

---

# Decision + Trajectory Memory

Decision Memory answers:

> What did we decide, under what evidence/constraints, and what happened after implementation?

Trajectory Memory answers:

> How did we get out of the problem?

SPARI stores inspectable engineering state and evidence — not hidden chain-of-thought.

Future runs retrieve only relevant memory, then revalidate triggered areas.

---

# Evidence

SPARI's evidence is deliberately split by version.

[`EVIDENCE.md`](EVIDENCE.md) preserves the v0.1.2 controlled program. It includes negative/no-uplift cases and documents that FULL-SPARI can add substantial compute when the baseline already has a sufficient solution.

[`EVIDENCE_V0.1.3.md`](EVIDENCE_V0.1.3.md) consolidates the corrected bounded v0.1.3 repository evaluations:

- Haiku: baseline 5/6 vs SPARI 6/6 verified completion; 3 pair-level improvements, 3 ties, 0 worse;
- Sonnet: both 6/6; 2 pair-level reuse improvements, 4 ties, no completion lift;
- Claude Code recovery methodology cleanup: 4→0 measured unproductive recovery EEI across two bounded recovery tasks, with 100% completion in both arms.

These are bounded signals, not universal performance claims.

v0.1.4 Economy Gate/persistent-index effects are **not yet evaluated**. The release exists to make that hypothesis testable.

Raw/corrected evaluation artifacts remain under [`evals/`](evals/).

---

# v0.1.4 evaluation target

The next controlled evaluation should compare at least:

```text
A — base model / executor
B — existing intake/context baseline
C — B + SPARI v0.1.4
```

and separately capture:

- gate decision accuracy;
- false bypasses / unnecessary admissions;
- token/time/cost by phase;
- first and last material discovery;
- exact/index hit rate;
- external research avoided;
- completion and acceptance;
- reuse decisions changed;
- Custom Delta/intervention surface;
- recomposition/recovery events;
- recovery entropy;
- regressions on control tasks.

The key question is no longer simply “Does SPARI research better?”

It is:

> **Can SPARI retain useful reuse/recomposition behavior while becoming nearly free when its deeper intelligence is unnecessary?**

---

# Repository structure

```text
SPARI/
├── SKILL.md
├── README.md
├── CHANGELOG.md
├── EVIDENCE.md
├── EVIDENCE_V0.1.3.md
├── LICENSE
├── NOTICE
├── THIRD_PARTY_NOTICES.md
│
├── references/
│   ├── economy-gate.md
│   ├── persistent-index.md
│   ├── internal-software-map.md
│   ├── research-depth.md
│   ├── research-budget.md
│   ├── closed-loop.md
│   └── ...
│
├── schemas/
│   ├── economy-gate.schema.json
│   ├── reuse-index.schema.json
│   └── ...
│
├── tests/
│   ├── adversarial-cases.md
│   └── economy-gate-cases.md
│
└── evals/
    └── preserved evaluation evidence
```

Historical patch/apply scratch files are not part of the canonical release surface.

---

# Behavioral principles

```text
Determinism before inference.

Reuse before research.

Use the persistent index before rebuilding repository understanding.

Do not make a 50-token task pay a 2,000-token reuse tax without evidence-backed reason.

Do not let small patch size hide high architectural/security/license risk.

Escalate research only while it can change the decision.

Inspect source, not just descriptions.

Treat claimed source and verified source differently.

Use hard constraints before popularity.

Compose before creating.

Treat custom code as the justified remainder.

Preserve successful and failed trajectories.

Recompose when evidence invalidates the active path.

Never turn missing evidence into certainty.

Never invent savings percentages.
```

---

# Conceptual prior art and notices

SPARI is independently written. Its design has been informed by public work in software reuse, agent workflows, source intelligence, repository mapping, program repair, specification/planning, cost governance, and software-selection discipline.

The repository's conceptual references and license/provenance notices remain documented in [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md) and the historical README/evidence lineage. Referenced projects are conceptual prior art unless explicitly incorporated as a dependency.

---

# Status

```text
v0.1.4
Experimental
```

v0.1.4 keeps v0.1.3's evidence-driven recomposition and adaptive search radius, but adds an economy gate so model-heavy SPARI is conditional rather than automatic and a persistent reuse index so repository knowledge can be reused without repeated prompt reconstruction.

---

# License

Apache License 2.0.

See [`LICENSE`](LICENSE), [`NOTICE`](NOTICE), and [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md).

---

# Existing software first. Expensive reasoning only where evidence earns it.

**SPARI — Build vs Borrow, then compose; recompose when reality changes.**
