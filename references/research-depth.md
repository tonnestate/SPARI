# Research Depth and Search Radius

SPARI v0.1.7 separates **admission**, **decision formation**, and **research depth**.

## G0 — Economy Gate

Before model-heavy research, use deterministic/indexed evidence to select one of:

- `FAST_REUSE`
- `DIRECT_EXECUTION`
- `SPARI_PREFLIGHT`
- `SPARI_TARGETED`
- `SPARI_FULL`
- `RECOMPOSE`

See `economy-gate.md`.

The search radius below applies only when SPARI is admitted or recomposition requires it.

## Decision-question prerequisite

For consequential work, Pre-Execution Decision Gate defines the current engineering decision before selecting a search radius.

R0–R4 are not steps that must be walked in order. The search plan selects the cheapest radius/source that can change the active decision, and may jump directly to a targeted source when justified.

No broad search is permitted merely to "understand everything" or "see what exists."

## Search radius

### R0_RECALL
Retrieve relevant Decision Memory and Trajectory Memory.

### R1_LOCAL
Inspect the current code, tests, manifests, dependencies, and relevant reuse-index/internal-map slice.

### R2_RELATED_INTERNAL
Inspect analogous modules, repository history, previous fixes, nearby capabilities, and internal repair ingredients.

### R3_TARGETED_EXTERNAL
Use focused GitHub/PyPI/standards/reference searches for a specific unresolved capability, pattern, candidate, or design question.

### R4_BROAD_EXTERNAL
Use semantic solution-space expansion, broader candidate discovery, research swarm, and comparative evaluation when the solution family itself remains uncertain.

## Escalation rule

Move outward only when evidence at the current radius leaves material uncertainty that can change:

- selected composition;
- Custom Delta;
- intervention surface;
- hard-gate outcome;
- architecture risk;
- verification strategy.

Do not escalate merely because another search could be performed.

## Compatibility profiles

- `PREFLIGHT` normally uses R0–R1 and may escalate;
- `TARGETED` normally uses R0–R3 around a known capability/candidate;
- `FULL` permits R0–R4 and independent evaluation for consequential or ambiguous decisions.

Profiles are ceilings/expected operating ranges, not mandatory linear pipelines.

## Stop rule

`QUALITY_STOP` when additional search no longer materially changes the candidate frontier, composition, Custom Delta, intervention surface, hard-gate outcome, or verification plan.

`RESOURCE_STOP` remains separate. Budget exhaustion never means `BUILD`.
