# Closed Loop

SPARI v0.1.4 adds an economy gate before the v0.1.3 evidence/recomposition loop.

```text
RAW / QUALIFIED CONTEXT
→ ECONOMY GATE
   ├─ FAST_REUSE / DIRECT_EXECUTION → bounded verification → outcome/index update
   └─ SPARI ADMITTED
        → ENGINEERING CASE
        → RECALL
        → RETRIEVE / INSPECT
        → DIAGNOSE
        → COMPOSE
        → BOUNDED EXECUTION
        → EVIDENCE CHECKPOINT
           ├─ CONTINUE
           ├─ ADAPT
           ├─ RECOMPOSE → update case → retrieve only new gap → compose again
           └─ STOP
        → VERIFY OUTCOME
        → UPDATE DECISION + TRAJECTORY MEMORY
        → INCREMENTAL REUSE-INDEX REFRESH
```

## Fast path is not permanent permission

A task may begin as `FAST_REUSE` or `DIRECT_EXECUTION` and later produce evidence that invalidates the cheap path.

Examples:

- verification contradicts the expected behavior;
- a supposedly local change exposes an architecture boundary;
- a dependency/provenance issue appears;
- repeated repair attempts fail;
- the intervention starts creating parallel authority.

At that point, emit `RECOMPOSE` or admit the smallest adequate SPARI profile. Economy gating must not suppress new evidence.

## Recomposition

Trigger recomposition when new evidence materially weakens or falsifies the current path.

Record:

- trigger/new evidence;
- invalidated hypotheses/assumptions;
- retained evidence/components;
- abandoned path;
- newly retrieved ingredients;
- previous/new composition reference;
- Custom Delta change;
- intervention-surface change;
- required verification.

Do not restart all research from zero unless the evidence base itself is invalid.

## Outcome states

- `VALIDATED`
- `VALIDATED_WITH_LIMITATIONS`
- `REJECTED_AFTER_IMPLEMENTATION`
- `UNKNOWN_OUTCOME`

`REQUIRES_RECOMPOSITION` remains valid for integrations that cannot continue in the current execution context, but active loops should prefer an explicit `RECOMPOSITION_EVENT` and continue when safe.

## Evidence summary

Preserve observed evidence for comparison across runs:

- economy-gate outcome/reason codes;
- capabilities required/covered;
- planned vs actual reuse;
- planned vs actual Custom Delta;
- intervention surface;
- failed paths escaped;
- recomposition count/reasons;
- verification outcome;
- revision/evidence references;
- observed token/time/cost only when actually measured.

Label quantitative claims `OBSERVED`, `ESTIMATED`, or `UNKNOWN`.
