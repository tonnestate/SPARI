# Failure Codes

## Admission / index

- `ECONOMY_GATE_UNDECIDABLE`
- `REUSE_INDEX_UNAVAILABLE`
- `REUSE_INDEX_STALE`
- `FAST_MATCH_STALE`
- `FAST_MATCH_CONFLICT`
- `BYPASS_UNSAFE`

An admission/index failure should normally fall back to the smallest useful source-backed local inspection. It does not imply FULL research and never implies permission to `BUILD`.

## Research / source

- `NOT_RECON_READY`
- `GITHUB_UNAVAILABLE`
- `PYPI_UNAVAILABLE`
- `INTERNAL_CONTEXT_UNAVAILABLE`
- `RESEARCH_INCOMPLETE`
- `RESEARCH_BUDGET_EXHAUSTED`
- `NO_LICENSE`
- `LICENSE_SCOPE_UNCLEAR`
- `PROVENANCE_UNRESOLVED`
- `SECURITY_GATE_FAILED`
- `RUNTIME_INCOMPATIBLE`
- `NO_VIABLE_BASE`
- `NO_VIABLE_COMPONENT`
- `CONSTRAINT_CONFLICT`
- `EVIDENCE_INSUFFICIENT`
- `SOURCE_INSPECTION_INCOMPLETE`
- `JUDGE_DISAGREEMENT_UNRESOLVED`
- `CUSTOM_DELTA_UNJUSTIFIED`
- `OUTCOME_NOT_VERIFIED`

Discovery failure never implies permission to build from scratch.

## Internal map / execution

- `INTERNAL_MAP_INCOMPLETE`
- `EXECUTION_CONTRACT_MISSING`
- `EXECUTION_OUTCOME_MISSING`
- `EXECUTION_SCOPE_DRIFT`
- `CUSTOM_DELTA_EXPANDED_UNJUSTIFIED`
- `REVISION_EVIDENCE_MISSING`

## Recomposition / trajectory

- `ENGINEERING_CASE_INSUFFICIENT`
- `TRAJECTORY_EVIDENCE_MISSING`
- `RECOMPOSITION_UNJUSTIFIED`
- `RECOMPOSITION_EVIDENCE_MISSING`
- `INTERVENTION_SURFACE_UNKNOWN`

Recomposition failure never implies permission to continue blind trial-and-error. Preserve the last supported composition and surface the unresolved evidence gap.
