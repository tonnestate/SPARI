# SPARI

<p align="center">
  <img src="docs/spari-banner.png" alt="SPARI — reuse-first and runtime-first engineering intelligence for AI agents" width="100%">
</p>

<p align="center">
  <strong>Build-vs-Borrow and Runtime-Evidence Intelligence for AI Engineering Agents.</strong><br>
  Reuse what exists. Trace what runs. Build only the missing delta.
</p>

<p align="center">
  <img alt="License" src="https://img.shields.io/badge/license-Apache--2.0-blue">
  <img alt="Status" src="https://img.shields.io/badge/status-experimental-orange">
  <img alt="Version" src="https://img.shields.io/badge/version-0.1.5-ff69b4">
  <img alt="Reuse First" src="https://img.shields.io/badge/reuse-first-c060ff">
  <img alt="Runtime First" src="https://img.shields.io/badge/runtime-first-ff69b4">
  <img alt="Agent Skill" src="https://img.shields.io/badge/agent-skill-purple">
  <img alt="Built-in LLM" src="https://img.shields.io/badge/built--in%20LLM-none-black">
</p>

---

## What SPARI is

SPARI — **Software Prior Art & Reuse Intelligence** — is an engineering decision layer for AI agents.

It addresses three recurring failure modes:

```text
REINVENTION
The agent builds something that already exists.

SOLUTION LOCK-IN
The agent keeps patching the first plausible approach after evidence contradicts it.

WRONG-PATH DEBUGGING
The agent audits, repairs or redesigns code that is not actually executed by the failing runtime path.
```

SPARI changes the default:

```text
deterministic evidence first
        ↓
reuse existing software where justified
        ↓
trace the real runtime path when behavior is broken
        ↓
build only the smallest missing delta
        ↓
verify the same path
        ↓
recompose when evidence changes
```

SPARI is not another coding agent. It does not contain a built-in LLM, code editor, deployment engine, project manager or mandatory research swarm.

> **Agents execute. SPARI constrains what should be reused, inspected, changed, or reconsidered.**

---

## What SPARI v0.1.5 can do today

v0.1.5 keeps the v0.1.4 Economy Gate and Persistent Reuse Index and adds a **Runtime Evidence Gate** for observed failures.

| Capability | v0.1.5 behavior |
|---|---|
| Economy admission | Decides how much SPARI is justified before model-heavy prior-art reasoning begins. |
| Deterministic fast reuse | Uses exact capability, symbol, interface, dependency, route/schema, structural and validated-memory evidence before inference where the host provides it. |
| Micro-task bypass | Allows `FAST_REUSE` or `DIRECT_EXECUTION` when bounded work has no material architecture, dependency, provenance, security, public-interface or recovery uncertainty. |
| Runtime Evidence Gate | Routes observed failures into a trace-first repair path instead of broad repository archaeology. |
| Canonical entrypoint | Requires the public command, API, UI action, MCP tool or library call that actually represents the failing behavior. |
| Reproduction | Requires a concrete, repeatable signal before repair when the failure is not already represented by a trustworthy failing check. |
| Executed-path evidence | Treats the code actually reached by the failing run as higher-value evidence than nearby or similarly named repository files. |
| First concrete failure | Narrows diagnosis to the earliest observed condition that materially breaks the canonical path. |
| Capability-scoped reuse | Queries the reuse index only for the failing capability before creating a new implementation. |
| Decision-changing evidence | Additional queries or audits must be able to change the current technical decision. Otherwise they are not justified. |
| Audit budget | Keeps diagnosis local to the current capability and immediate runtime dependencies unless evidence proves wider scope is necessary. |
| Minimal Runtime Custom Delta | Defines the smallest architecture-consistent change on the executed path that repairs the reproduced failure. |
| Same-path retest | Re-runs the same canonical path after the change instead of substituting a different proof. |
| Recomposition | If runtime evidence disproves the active authority, dependency or hypothesis, SPARI preserves valid evidence and reopens only the invalidated gap. |
| Decision + Trajectory Memory | Stores inspectable engineering decisions and recovery episodes without persisting hidden chain-of-thought. |
| Persistent Reuse Index | Reuses compact repository intelligence across tasks instead of reconstructing the codebase in every prompt. |
| Adaptive external research | Escalates through R0–R4 only while unresolved uncertainty can materially change the engineering decision. |
| Build-vs-Borrow composition | Produces `ADOPT`, `ADAPT`, `COMPOSE`, `REFERENCE`, `REJECT`, or justified `BUILD` decisions. |
| License/provenance discipline | Separates claimed source, verified source, license evidence and effective reuse permission. |

---

## The v0.1.5 operating model

```text
Raw / qualified engineering context
                │
                ▼
          ECONOMY GATE
                │
        observed failure?
          /             \
        NO               YES
        │                 │
        ▼                 ▼
deterministic         RUNTIME
reuse lookup          EVIDENCE GATE
        │                 │
        │            canonical entrypoint
        │                 ↓
        │            reproduce failure
        │                 ↓
        │            actual executed path
        │                 ↓
        │            first concrete failure
        │                 ↓
        └──────────→ capability-scoped reuse
                          ↓
                     smallest delta
                          ↓
                    same-path retest
                          ↓
              CONTINUE / ADAPT / RECOMPOSE
                          ↓
                 verified outcome
                          ↓
            Decision + Trajectory Memory
                          ↓
             incremental index refresh
```

The Runtime Evidence Gate is deliberately **not** a second agent or a second workflow. It is an admission, scope and execution guard inside the existing SPARI loop.

---

## How SPARI solves the problem

### 1. Spend cognition only when it can change the decision

v0.1.4 introduced the Economy Gate:

```text
ECONOMY_GATE
    ├── FAST_REUSE
    ├── DIRECT_EXECUTION
    ├── SPARI_PREFLIGHT
    ├── SPARI_TARGETED
    ├── SPARI_FULL
    ├── RUNTIME_EVIDENCE_GATE
    └── RECOMPOSE
```

A reuse engine should not spend more reasoning than the work it protects without an evidence-backed reason.

There is no universal public token threshold. Deployments may configure cost policies, but SPARI does not invent a fixed break-even number.

See [`references/economy-gate.md`](references/economy-gate.md).

### 2. Trace before repair when behavior is broken

An observed failure changes the order of work.

Not:

```text
failure
→ search repository for plausible files
→ audit related modules
→ redesign architecture
→ eventually discover what really runs
```

Instead:

```text
failure
→ canonical entrypoint
→ reproduce
→ executed path
→ first concrete failing condition
→ capability-scoped reuse lookup
→ minimal correction
→ same-path retest
```

The governing rule is:

> **Runtime evidence outranks repository speculation.**

A file is not in repair scope merely because its name, folder or historical role looks relevant.

See [`references/runtime-evidence-gate.md`](references/runtime-evidence-gate.md) and [`schemas/runtime-evidence-gate.schema.json`](schemas/runtime-evidence-gate.schema.json).

### 3. Reuse after the failing capability is known

SPARI does not perform a repository-wide reuse hunt after every symptom.

Once the first failing capability is known:

```text
failing capability
→ exact capability key
→ symbol / interface / route / schema
→ installed dependency
→ architecture authority
→ prior Decision / Trajectory
→ relevant internal implementation
```

Only then does SPARI decide whether the executed path should be reused, adapted or minimally extended.

### 4. Build only the Runtime Custom Delta

The normal `CUSTOM_DELTA` remains the part not covered by reusable software.

For repair work v0.1.5 adds a stricter interpretation:

```text
RUNTIME_CUSTOM_DELTA =
the smallest change to the actually executed path
that repairs the reproduced failure
without inventing parallel architecture
```

New services, stores, adapters, schemas, contracts, modes or fallback systems require evidence that the real executed path cannot be repaired correctly without them.

### 5. Query only evidence that can change the decision

Before another diagnostic or research step:

```text
QUESTION:
What engineering decision can this evidence change?
```

If there is no concrete answer:

```text
DO_NOT_QUERY
```

Interesting inconsistencies may still be recorded as `FUTURE_WORK`, but they do not automatically become work inside a bounded repair.

### 6. Re-run the identical path

A different test or adjacent component is not a substitute for the original behavior.

After a repair:

```text
same canonical command / request / action
→ same runtime path
→ original failure absent
→ required acceptance evidence
```

If the original path cannot be re-run, the verification limitation remains explicit.

### 7. Recompose instead of perfecting the wrong path

Example:

```text
SPARI believes module A is the active authority
        ↓
runtime evidence shows module B is actually executed
        ↓
RECOMPOSE
        ↓
retain valid evidence
discard the wrong authority assumption
reopen only the affected capability
```

The correct action is not to keep improving module A.

---

## Runtime Evidence Gate

The minimal gate is:

```text
INPUT
observed failure
repository / system
canonical command, request, action or other public entrypoint when known

OUTPUT
canonical entrypoint
reproduction evidence
executed path
first failing component / condition
failing capability
reuse candidates
selected reusable component when present
minimal custom delta
same-path retest
non-blocking findings
status
```

Representative statuses:

```text
REPRODUCED
NOT_REPRODUCED
RUNTIME_EVIDENCE_INCOMPLETE
REUSE_FOUND
MINIMAL_REPAIR_REQUIRED
BLOCKED
RECOMPOSE
PASS
```

Before implementation changes, consequential repair work should know at least:

```text
canonical entrypoint
reproduction scenario
observed failure
actual executed component
first concrete failing condition
```

Missing runtime evidence is not permission to build.

---

## Runtime evidence

Useful evidence can include:

```text
CLI invocation
failing test
HTTP/API request
UI action
MCP tool invocation
stack trace
call trace
structured logs
targeted instrumentation
coverage slice
debugger observation
import/call graph tied to the observed execution
```

Insufficient by itself:

```text
"this file looks relevant"
"the name matches"
"the module is nearby"
"the old implementation used to do this"
```

Repository archaeology is justified only when the runtime path exposes a capability gap, an existing implementation must be located, or concrete runtime evidence is missing.

---

## Failed-cycle cap

SPARI should not convert debugging into endless speculative retries.

After repeated falsified repair hypotheses, stop opening another local patch by default. Re-check the reproduction loop, the canonical path and the hypothesis basis, then either:

```text
ADAPT
RECOMPOSE
BLOCKED
```

The public v0.1.5 contract does not claim that a universal retry count is optimal. A host may configure one; the default guidance is to escalate after three failed hypothesis-test cycles rather than push through attempt five or six.

---

## Persistent Reuse Index

SPARI should not reconstruct repository knowledge inside a model prompt on every task.

The `REUSE_INDEX` can preserve compact evidence about:

```text
repositories / revisions
manifests / lockfiles
modules / services
symbols / exports / types / interfaces
routes / schemas
dependency edges
architecture authorities
capability-to-code mappings
tests / evidence references
structural fingerprints
installed dependencies
Decision Memory references
Trajectory Memory references
optional cached embedding references
```

The model receives only the relevant slice.

Semantic similarity can retrieve candidates. It cannot by itself promote a candidate to reuse.

See [`references/persistent-index.md`](references/persistent-index.md).

---

## Adaptive search radius

After SPARI is admitted:

```text
R0_RECALL
relevant Decision + Trajectory Memory

R1_LOCAL
code, tests, manifests, dependencies, relevant indexed/map slice

R2_RELATED_INTERNAL
analogous modules, history, previous fixes, internal repair ingredients

R3_TARGETED_EXTERNAL
focused GitHub / PyPI / standards / reference search

R4_BROAD_EXTERNAL
solution-family discovery + comparative research
```

For observed failures, the Runtime Evidence Gate narrows the R0–R2 question around the **executed failing capability** before any broadening is considered.

`PREFLIGHT`, `TARGETED`, and `FULL` remain ceilings, not mandatory pipelines.

---

## Build-vs-Borrow is composition

SPARI does not exist to produce recommendation lists.

A useful result looks like:

```text
KEEP_INTERNAL
existing persistence authority

DEPENDENCY
already-installed package

ADAPT
canonical internal implementation

REFERENCE_ONLY
external architecture pattern

CUSTOM
only the unavoidable missing adapter
```

Candidate decisions are:

```text
ADOPT
ADAPT
COMPOSE
REFERENCE
REJECT
BUILD
```

`BUILD` is never the automatic result of missing evidence.

---

## Execution boundary

SPARI decides what should exist and which path is justified. Coding agents execute.

```text
SPARI
  │
  ├─ Economy Gate
  ├─ Runtime Evidence Gate
  ├─ Reuse / composition decision
  ├─ Custom Delta
  └─ Recomposition
        │
        ▼
Coding Agent
Claude / Codex / Aider / other executor
        │
        ▼
execution evidence
        │
        └────────────→ SPARI
```

For consequential work SPARI can emit an executor-agnostic `EXECUTION_CONTRACT`.

Fast-path work may use reduced bounded instructions when a full contract would cost more than the work and no risk override requires it.

---

## Relationship to BananaMe, MangoMe and IntakeGov

The repositories remain independent.

```text
IntakeGov
qualification / routing
        │
        ▼
SPARI
what exists?
what actually runs?
what should be reused or changed?
        │
        ▼
Coding Agent
        │
        ├──────── BananaMe
        │         understand / mutate / verify repository state
        │
        └──────── MangoMe
                  optional governance / work / evidence substrate
```

SPARI may identify the exact failing block or capability. BananaMe can provide guarded repository mechanics for changing it. MangoMe can consume SPARI decisions as governance evidence. None is a runtime dependency of SPARI.

---

## Safety and scope invariants

```text
DETERMINISM BEFORE INFERENCE
RUNTIME BEFORE REPOSITORY SPECULATION
TRACE BEFORE REPAIR
REUSE BEFORE RESEARCH
BUILD ONLY THE MISSING DELTA
EXECUTED CODE OUTRANKS NEARBY CODE
MISSING EVIDENCE != BUILD
INTERESTING INCONSISTENCY != CURRENT WORK
RECOMPOSE WHEN EVIDENCE INVALIDATES THE PATH
```

Additional boundaries:

- never repair a legacy implementation merely because it looks relevant;
- never use repository inventory as a substitute for reproduction;
- never create compatibility architecture before proving the executed path needs it;
- never let a small patch bypass material security, license, public-interface or architecture risk;
- never treat cached semantic similarity as a final reuse verdict;
- never persist hidden chain-of-thought;
- never publish savings or capability percentages without controlled measurement.

---

## Evidence

SPARI separates design from demonstrated effect.

[`EVIDENCE.md`](EVIDENCE.md) preserves the v0.1.2 controlled program, including expensive no-uplift cases.

[`EVIDENCE_V0.1.3.md`](EVIDENCE_V0.1.3.md) consolidates corrected bounded v0.1.3 evidence, including:

```text
Haiku:
baseline 5/6
SPARI    6/6

Sonnet:
baseline 6/6
SPARI    6/6
with two reuse-oriented pair improvements

bounded recovery cleanup:
4 → 0 measured unproductive recovery EEI
across two recovery tasks
```

These are bounded observations, not universal claims.

v0.1.4 Economy Gate and v0.1.5 Runtime Evidence Gate effects are **not yet validated by dedicated controlled evaluations**.

---

## v0.1.5 evaluation target

The next runtime-first evaluation should compare at least:

```text
A — base executor
B — executor + SPARI v0.1.4
C — executor + SPARI v0.1.5
D — optional Runtime Evidence Gate only
```

Measure:

```text
completion
acceptance
time to first concrete runtime failure
time to correct fix
request count
tool-call count
token / time / cost where available
files inspected
irrelevant files inspected
stores / datasets scanned
queries executed
existing components reused
new components proposed
new components actually required
speculative intervention count
scope-expansion events
failed repair cycles
runtime relevance ratio
```

No universal threshold or savings percentage should be claimed before those measurements exist.

---

## Repository structure

```text
SPARI/
├── README.md
├── SKILL.md
├── CHANGELOG.md
├── EVIDENCE.md
├── EVIDENCE_V0.1.3.md
├── LICENSE
├── NOTICE
├── THIRD_PARTY_NOTICES.md
│
├── docs/
│   └── spari-banner.png
│
├── references/
│   ├── economy-gate.md
│   ├── runtime-evidence-gate.md
│   ├── persistent-index.md
│   ├── internal-software-map.md
│   ├── closed-loop.md
│   └── ...
│
├── schemas/
│   ├── economy-gate.schema.json
│   ├── runtime-evidence-gate.schema.json
│   ├── reuse-index.schema.json
│   └── ...
│
├── tests/
│   ├── adversarial-cases.md
│   ├── economy-gate-cases.md
│   └── runtime-evidence-gate-cases.md
│
└── evals/
    └── preserved historical evaluation evidence
```

---

## Behavioral testing

SPARI keeps historical acceptance cases separate from release-specific additions:

- [`tests/adversarial-cases.md`](tests/adversarial-cases.md) — historical Build-vs-Borrow, research, execution and recomposition cases;
- [`tests/economy-gate-cases.md`](tests/economy-gate-cases.md) — v0.1.4 admission/economy cases;
- [`tests/runtime-evidence-gate-cases.md`](tests/runtime-evidence-gate-cases.md) — v0.1.5 runtime-path, trace-first, audit-budget and same-path-retest cases.

The runtime cases are behavioral contracts. They do not by themselves prove a measured v0.1.5 performance effect.

---

## Conceptual prior art

SPARI is independently written.

v0.1.5's Runtime Evidence Gate was informed conceptually by disciplined debugging work that emphasizes a tight feedback loop, reproduction, falsifiable hypotheses, targeted instrumentation, minimal root-cause repair and retesting. No third-party source code or skill text is incorporated.

See [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md).

---

## Current limitations

v0.1.5 defines an engineering contract and guardrails. It does **not** ship:

- a universal runtime tracing engine;
- a debugger;
- an observability platform;
- a call-graph server;
- a new graph database;
- a mandatory agent swarm;
- automatic proof that a discovered path is complete.

Host tools provide tests, traces, logs, debuggers, coverage, CLI execution and runtime instrumentation.

The Runtime Evidence Gate consumes that evidence and constrains the next engineering decision.

---

## Status

SPARI v0.1.5 is an **experimental runtime-evidence release**.

The release extends v0.1.4 rather than replacing it:

```text
v0.1.4
economy before cognition

        ↓

v0.1.5
runtime before repair
```

The governing sequence is now:

```text
Determinism before inference.
Runtime before speculation.
Reuse before research.
Build only what is missing.
Recompose when evidence changes.
```

---

## License

Apache License 2.0.

See [`LICENSE`](LICENSE), [`NOTICE`](NOTICE), and [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md).

---

# Trace what runs. Reuse what exists. Build only the delta.

**SPARI — Build vs Borrow, then compose; recompose when reality changes.**
