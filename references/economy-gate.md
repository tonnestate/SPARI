# Economy Gate

SPARI v0.1.4 adds admission control before model-heavy prior-art reasoning.

The gate answers one question:

> How much SPARI is justified for this work slice before we pay for inference and research?

It does not choose the final architecture.

## 1. Deterministic first

Where the host environment supports it, run a zero-model-inference lookup against fresh structured evidence before any semantic reasoning.

Preferred keys include:

- exact capability identifiers;
- symbol/export names;
- type/interface signatures;
- manifest/lockfile dependencies;
- route/API/schema identifiers;
- canonical authority mappings;
- AST/structural fingerprints;
- validated Decision Memory keys;
- validated Trajectory Memory keys.

A cached semantic/vector index may retrieve candidates after or alongside exact matching, but retrieval is not a final engineering decision. Do not regenerate embeddings or repository semantics per task.

## 2. Admission outcomes

### FAST_REUSE

Use when a fresh, compatible, validated path is deterministically identified and no risk override requires deeper evaluation.

### DIRECT_EXECUTION

Use for a bounded micro-task when all of the following are supported by evidence:

- known local scope;
- no new dependency or external code;
- no public interface/schema/data-authority change;
- no architecture-boundary creation/replacement;
- no security/license/provenance decision;
- no repeated failure or contradictory evidence;
- no unresolved Build-vs-Borrow choice likely to change the intervention.

### SPARI_PREFLIGHT

Use when small uncertainty remains. Admit R0/R1 and escalate only if needed.

### SPARI_TARGETED

Use when a known candidate/capability requires focused due diligence, normally up to R3.

### SPARI_FULL

Use for consequential, ambiguous, cross-cutting, or solution-family decisions where R4/independent evaluation can materially change the outcome.

### RECOMPOSE

Use after execution evidence invalidates the current path. The Economy Gate does not suppress a legitimate recomposition trigger.

## 3. Break-even rule

Model-based SPARI work is admitted when one or more of these is true:

- unresolved decision value can materially change composition, Custom Delta, intervention surface, hard-gate result, or verification;
- configured risk policy requires evidence before execution;
- prior failures/contradictory evidence require strategy repair;
- expected rework/execution burden is greater than the configured cost of the check.

SPARI does not define a universal numeric token threshold in v0.1.4. Deployments may configure thresholds using their own measured workload economics.

If numeric cost estimates are unavailable, use explicit qualitative classes and reason codes. Do not manufacture precision.

## 4. Risk overrides

A small patch is not automatically a cheap decision. Escalate when material risk exists, including:

- new dependency or vendored external code;
- unclear license/provenance;
- security-sensitive behavior;
- public API/interface/schema change;
- persistent data-model/authority change;
- new architectural authority/service/module;
- irreversible/destructive operation;
- repeated failed attempts;
- active-plan contradiction;
- stale/unverified fast-match evidence.

Risk override should select the smallest sufficient profile, not automatically FULL.

## 5. Unknown state

If the gate cannot decide because structured evidence is missing or stale:

```text
ECONOMY_GATE_UNDECIDABLE
→ smallest useful local inspection (normally R1)
```

Do not:

```text
unknown
→ FULL
```

and do not:

```text
unknown
→ BUILD
```

## 6. Audit record

For consequential admission decisions preserve a compact `ECONOMY_GATE_DECISION`:

- repository/base revision;
- task/capability key when available;
- deterministic hits;
- freshness state;
- risk flags;
- optional execution/check cost estimates and their provenance;
- selected outcome/profile;
- reason codes;
- evidence references.

The gate record is engineering metadata, not chain-of-thought.
