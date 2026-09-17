# Intake / Qualified-Context Handoff

SPARI is standalone-capable. IntakeGov is an optional upstream provider of qualified work context, not a runtime dependency and not a gate that decides whether SPARI may reason about prior art.

## Accepted entry states

SPARI may receive either:

- `RAW_CASE` — enough engineering context to establish a minimal technical case; or
- `QUALIFIED_CASE` — an upstream system already established the work type, outcome, constraints, context, and success criteria.

When a `QUALIFIED_CASE` is available, do not repeat intake qualification unless contradictory evidence requires clarification.

## Preferred qualified handoff

- raw intent;
- qualified outcome;
- project relation/context;
- known facts and non-goals;
- constraints and risk flags;
- success criteria;
- technical environment;
- material unknowns;
- previous attempts/evidence when available.

SPARI then creates or updates its compact `ENGINEERING_CASE`, performs recall, starts at the smallest relevant search radius, and owns composition/recomposition decisions.

An upstream field such as `PRIOR_ART_REQUIRED` may be treated as a useful signal, but it must not be interpreted as a prohibition on SPARI recall or local prior-art inspection.
