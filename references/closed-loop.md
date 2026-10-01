# Closed Loop

SPARI is incomplete unless execution evidence can change the active engineering strategy.

v0.1.5 has two entry shapes:

```text
NEW / CHANGED CAPABILITY
→ Economy Gate
→ deterministic reuse / admitted R0–R4
→ composition
→ execution
→ evidence checkpoint

OBSERVED FAILURE
→ Economy Gate
→ Runtime Evidence Gate
→ canonical entrypoint
→ reproduce
→ executed path
→ first failure
→ capability-scoped reuse
→ Runtime Custom Delta
→ same-path retest
```

Both converge on:

```text
CONTINUE | ADAPT | RECOMPOSE | STOP
→ VERIFY OUTCOME
→ UPDATE DECISION + TRAJECTORY MEMORY
→ INCREMENTALLY REFRESH REUSE INDEX
```

## Recomposition

Trigger recomposition when new evidence materially weakens or falsifies the current path, for example:

- runtime evidence proves a different component/authority is actually executed;
- verification contradicts the active hypothesis;
- dependency or integration assumptions fail;
- a previously unknown internal capability changes the solution;
- implementation begins creating parallel architecture or unjustified Custom Delta;
- repeated local repair attempts fail to address root cause;
- hard-gate evidence changes;
- a materially stronger composition becomes available.

A recomposition event preserves what remains valid.

Record:

- trigger/new evidence;
- invalidated hypotheses/assumptions;
- retained evidence/components;
- abandoned path;
- newly retrieved ingredients;
- previous/new composition reference;
- Custom Delta/intervention-surface change;
- required verification.

Do not restart all research from zero unless the evidence base itself is invalid.

## Runtime-path conflict

A specific recomposition trigger in v0.1.5 is:

```text
believed authority != actually executed authority
```

When runtime evidence proves the active composition targets the wrong code path:

```text
RECOMPOSE
```

Do not continue improving the unexecuted path.

## Outcome states

Final evidence states remain:

- `VALIDATED`;
- `VALIDATED_WITH_LIMITATIONS`;
- `REJECTED_AFTER_IMPLEMENTATION`;
- `UNKNOWN_OUTCOME`.

`REQUIRES_RECOMPOSITION` remains valid when execution cannot safely continue in the current context.

## Evidence summary

Preserve observed evidence for comparison across runs:

- capabilities required/covered;
- planned vs actual reuse;
- planned vs actual Custom Delta;
- intervention surface;
- canonical runtime path when relevant;
- first concrete failure;
- failed paths escaped;
- recomposition count/reasons;
- same-path retest result;
- verification outcome;
- revision/evidence references.

Label quantitative claims `OBSERVED`, `ESTIMATED`, or `UNKNOWN`.

Do not fabricate LOC/time/cost savings.
