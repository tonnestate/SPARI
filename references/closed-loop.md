# Closed Loop

SPARI is incomplete unless real implementation outcomes return to the software-intelligence layer.

```text
DISCOVER
→ EVALUATE
→ COMPOSE
→ HAND OFF
→ IMPLEMENT
→ VERIFY
→ RECORD OUTCOME
→ UPDATE MEMORY
→ REVALIDATE
→ DISCOVER SMARTER
```

## Outcome states

- VALIDATED
- VALIDATED_WITH_LIMITATIONS
- REQUIRES_RECOMPOSITION
- REJECTED_AFTER_IMPLEMENTATION
- UNKNOWN_OUTCOME

## Outcome record

Capture:

- planned base vs actual base;
- planned packages vs actual packages;
- abandoned candidates;
- actual custom delta;
- integration defects;
- verification evidence;
- operational limitations;
- user/system outcome;
- lessons for future selection.

A candidate becomes a trusted reusable base only after source/version, legal state, real implementation outcome, limitations, and revalidation triggers are known.

Negative outcomes are valuable memory. Do not rediscover and retry them without new evidence.


## Execution evidence

Prefer a structured `EXECUTION_OUTCOME` over a prose completion claim.

When revision control is available, link the researched decision to:

- base revision;
- result revision;
- planned vs actual reuse;
- planned vs actual Custom Delta;
- verification evidence;
- deviations.

This lets future revalidation inspect the implementation state that produced the recorded outcome.
