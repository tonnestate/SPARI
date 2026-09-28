# Internal Software Map

SPARI treats the current system as first-class prior art.

v0.1.4 separates two layers:

1. `REUSE_INDEX` — persistent, compact, deterministic lookup surface;
2. `INTERNAL_SOFTWARE_MAP` — richer capability/dependency/architecture evidence used when the decision needs it.

External reuse research is incomplete when material internal prior art has not been checked, but a full map must not be rebuilt for every micro-task.

## Purpose

`INTERNAL_SOFTWARE_MAP` answers:

- Which relevant capabilities already exist?
- Where are they implemented?
- Which abstractions are canonical?
- Which dependencies are already present?
- Which modules/services/interfaces depend on one another?
- Which architecture boundaries constrain reuse or replacement?
- Which internal components should be retained, extended, adapted, or replaced?

## Not merely a file tree

A useful map may contain:

- repositories/workspaces;
- manifests and lockfiles;
- packages/modules/services;
- public interfaces;
- important classes/functions/symbols;
- dependency relationships;
- architectural and runtime boundaries;
- capability-to-code mappings;
- existing third-party dependencies;
- likely internal-reuse candidates;
- unresolved areas.

## Relevant slice, not context dump

The durable map can be large. Active context should contain only the subset relevant to the current capability, constraints, and dependency neighborhood.

```text
persistent reuse index
      ↓
capability/exact match
      ↓
relevant map slice (only if needed)
      ↓
dependency neighborhood
      ↓
architecture boundary filter
      ↓
active evidence context
```

## Evidence

Material capability claims should point to inspectable evidence where possible: file/module path, symbol, manifest entry, dependency edge, test, interface/API definition, runtime configuration, and base revision.

## Internal reuse decisions

Internal candidates can receive:

- `KEEP_INTERNAL`
- `EXTEND_INTERNAL`
- `ADAPT_INTERNAL`
- `REPLACE_INTERNAL`
- `REFERENCE_INTERNAL`
- `NOT_RELEVANT`

Do not replace functioning internal software merely because an external alternative is more popular.

## Freshness

Incrementally refresh the relevant index/map evidence when the base revision changes materially, manifests/lockfiles change, architecture boundaries change, or the requested capability touches previously unmapped areas.

Do not regenerate the complete map merely because an unrelated file changed.
