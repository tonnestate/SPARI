# Closed Loop

SPARI is incomplete unless execution evidence can change the active engineering strategy. v0.1.3 therefore treats Recomposition as a first-class control transition, not merely an end-state label.

```text
ENGINEERING CASE
→ RECALL
→ RETRIEVE / INSPECT
→ DIAGNOSE
→ COMPOSE
→ BOUNDED EXECUTION
→ EVIDENCE CHECKPOINT
   ├─ CONTINUE
   ├─ ADAPT
   ├─ RECOMPOSE → update case → retrieve only the new gap → compose again
   └─ STOP
→ VERIFY OUTCOME
→ UPDATE DECISION + TRAJECTORY MEMORY
```

## Recomposition

Trigger recomposition when new evidence materially weakens or falsifies the current path, for example:

- verification contradicts the current hypothesis;
- a dependency or integration assumption fails;
- a previously unknown internal capability changes the solution;
- implementation starts creating parallel architecture or unjustified Custom Delta;
- repeated local repair attempts do not address the root cause;
- hard-gate evidence changes;
- a materially stronger composition becomes available.

A recomposition event must preserve what remains valid. Record:

- trigger/new evidence;
- invalidated hypotheses/assumptions;
- retained evidence/components;
- abandoned path;
- newly retrieved ingredients;
- previous and new composition reference;
- Custom Delta change;
- intervention-surface change;
- required verification.

Do not restart all research from zero unless the evidence base itself is invalid.

## Outcome states

Final/terminal evidence states remain:

- `VALIDATED`;
- `VALIDATED_WITH_LIMITATIONS`;
- `REJECTED_AFTER_IMPLEMENTATION`;
- `UNKNOWN_OUTCOME`.

`REQUIRES_RECOMPOSITION` remains valid for integrations that cannot continue in the current execution context, but active loops should prefer an explicit `RECOMPOSITION_EVENT` and continue when safe.

## Evidence summary

Preserve observed evidence for comparison across runs:

- capabilities required/covered;
- planned vs actual reuse;
- planned vs actual Custom Delta;
- intervention surface;
- failed paths escaped;
- recomposition count/reasons;
- verification outcome;
- revision/evidence references.

Label quantitative claims `OBSERVED`, `ESTIMATED`, or `UNKNOWN`. Do not fabricate LOC/time/cost savings.
