# Economy Gate

The Economy Gate is SPARI's pre-inference engineering admission layer. In v0.1.6 it runs only after Source Attestation Gate has produced an attestation state permitted by the current task/contract.

Its purpose is to prevent the reuse/control system from becoming more expensive than the bounded work it protects while still escalating when risk, uncertainty, failure evidence, or expected rework justifies deeper reasoning.

## Source-attestation precondition

Before Economy Gate:

```text
SOURCE_ATTESTATION_GATE
→ CURRENT_ATTESTED
```

or an explicitly contract-permitted:

```text
PINNED_ATTESTED
```

If source identity is stale, unresolved, conflicting, or unattested, do not silently continue as "current SPARI".

See `source-attestation-gate.md`.

## Outcomes

```text
FAST_REUSE
DIRECT_EXECUTION
SPARI_PREFLIGHT
SPARI_TARGETED
SPARI_FULL
RUNTIME_EVIDENCE_GATE
RECOMPOSE
```

## Deterministic first pass

Prefer zero-model evidence where the host provides it:

- capability keys;
- exact symbols/exports/types/interfaces;
- manifests and lockfiles;
- routes and schemas;
- structural fingerprints;
- architecture authorities;
- validated Decision/Trajectory keys;
- known task/repository revision;
- known failure/reproducer/entrypoint state.

Do not rebuild embeddings or repository semantics merely to make the admission decision.

## Observed failure routing

An observed failure changes the cheapest justified path.

When work starts from broken behavior, wrong output, an acceptance failure, performance regression, intermittent failure, or real end-to-end failure:

```text
ECONOMY_GATE
→ RUNTIME_EVIDENCE_GATE
```

unless a trustworthy canonical failing check already supplies the required runtime path evidence.

Runtime Evidence Gate is normally cheaper than broad prior-art research because it narrows the question to:

```text
what actually runs?
where does it first fail?
what existing implementation already solves that capability?
```

See `runtime-evidence-gate.md`.

## Micro-task bypass

`DIRECT_EXECUTION` or `FAST_REUSE` is appropriate only when deterministic evidence supports all material conditions:

- scope is bounded;
- no unresolved Build-vs-Borrow choice can materially change the intervention;
- no new dependency/external source is introduced;
- no material license/provenance uncertainty exists;
- no public API/schema/data authority changes;
- no new architecture authority;
- no security-sensitive uncertainty;
- no repeated failure/contradictory evidence;
- no observed failure requiring runtime-path diagnosis.

Patch size alone does not prove low risk.

## Risk overrides

Risk may admit the smallest adequate SPARI profile when the task changes or introduces:

- dependency/external code;
- license/provenance;
- security-sensitive behavior;
- public API/interface/schema;
- persistent data authority;
- architecture/service/module authority;
- destructive/irreversible behavior;
- repeated failed attempts;
- contradictory evidence;
- stale/unverified reuse evidence.

Do not route everything to FULL.

## Break-even rule

Model-based SPARI is justified when at least one is true:

1. unresolved decision value can materially change the composition, Custom Delta, intervention surface, hard-gate outcome, architecture risk, or verification plan;
2. configured risk policy requires evidence before execution;
3. observed failure requires Runtime Evidence Gate;
4. prior failures/contradictions require recomposition;
5. expected execution/rework burden exceeds a deployment's configured additional-check cost.

Public SPARI defines no universal token/time/currency threshold.

## Unknown gate state

When deterministic admission evidence is insufficient:

```text
ECONOMY_GATE_UNDECIDABLE
```

Fall back to the smallest useful source-backed inspection.

Do not:

```text
unknown
→ FULL
```

and never:

```text
unknown
→ BUILD
```

## Economy evidence

Where measurable record:

- exact/index hits;
- evidence freshness;
- risk flags;
- observed-failure flag;
- reproducer/entrypoint availability;
- admitted profile;
- inference admitted;
- optional execution/check cost estimate and provenance;
- reason codes.

See `../schemas/economy-gate.schema.json`.
