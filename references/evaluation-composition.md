# Evaluation & Composition

SPARI seeks the strongest composition, not one universal winner.

## Hard gates first

Eliminate candidates violating mandatory constraints before trade-off comparison.

## Questions

- What is the best overall base?
- Which internal components should remain?
- Which PyPI package solves a capability better than the base?
- Which repository is reference-only?
- Which capability still lacks a reusable solution?
- What integration code is unavoidable?

## Decisions

ADOPT / ADAPT / COMPOSE / REFERENCE / REJECT / BUILD

## Artifact roles

PRODUCT_BASE / DEPENDENCY / SOURCE_COMPONENT / REFERENCE_PATTERN / API_INTEGRATION / VENDORED_COMPONENT / CUSTOM_IMPLEMENTATION

## Custom Delta

Every custom item must state why existing internal, GitHub, and PyPI options are insufficient.

## Evidence-backed comparison

Candidate comparison should be quantitative where the underlying evidence is actually measurable, and qualitative where it is not.

Useful fields can include:

| Field | Preferred representation |
| --- | --- |
| Capability coverage | explicit capability count / total required |
| Integration effort | observed or estimated, with evidence/assumptions |
| Maintenance | dated repository/release evidence |
| Dependency risk | concrete dependency findings |
| Security | concrete findings / advisory state |
| License | declared, detected, and effective reuse decision |
| Test evidence | inspectable tests / CI evidence |
| Production evidence | cited evidence or `UNKNOWN` |
| Custom work required | explicit Custom Delta items |
| Migration / exit effort | observed, estimated, or `UNKNOWN` |

Do not turn these fields into an arbitrary weighted winner score.

A candidate with a higher synthetic score must not override:

- a failed hard gate;
- a material architecture mismatch;
- a license/provenance restriction;
- stronger source evidence for another composition.

## Measurement discipline

Every numerical claim should be traceable to an explicit denominator, method, or execution observation.

Example:

```text
required_capabilities: 12
covered_internal: 3
covered_external: 6
custom_required: 3
```

This can support a transparent reuse calculation.

By contrast:

```text
Capability Coverage: 87%
Integration Quality: 92%
```

is invalid unless SPARI can show exactly how those numbers were produced.

Use:

- `OBSERVED`
- `ESTIMATED`
- `UNKNOWN`

when the evidence state matters.

The purpose of measurement is to make Build-vs-Borrow decisions auditable and comparable over time, not to create false precision.

## Intervention Surface (v0.1.3)

Composition quality is not only capability coverage or Custom Delta. For existing systems, also preserve the intervention surface where measurable: files/symbols/interfaces/dependencies/authorities/persistence/boundaries changed.

Prefer the smallest architecture-consistent composition that satisfies verified requirements. Do not minimize patch size at the expense of correctness, maintainability, safety, or explicit requirements.

When execution evidence invalidates a composition, do not patch indefinitely inside the same assumption set. Emit a recomposition event, retain still-valid evidence, reopen only the relevant search radius, and version the new composition.
