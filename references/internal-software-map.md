# Internal Software Map

SPARI treats the current system as first-class prior art.

External reuse research is incomplete if the agent does not understand what the project already owns.

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
- packages/modules;
- services;
- public interfaces;
- important classes/functions/symbols;
- dependency relationships;
- architectural boundaries;
- runtime/deployment boundaries;
- capability-to-code mappings;
- existing third-party dependencies;
- likely internal-reuse candidates;
- unresolved areas.

## Relevant slice, not context dump

The durable map can be large.

The active research agent should receive only the subset relevant to the current capability, constraints, and dependency neighborhood.

A recommended pattern:

```text
full internal map
      ↓
capability relevance
      ↓
dependency neighborhood
      ↓
architectural boundary filter
      ↓
active context slice
```

This preserves internal awareness without consuming the entire model context.

## Evidence

Every material capability claim should point back to inspectable evidence where possible:

- file/module path;
- symbol;
- manifest entry;
- dependency edge;
- test;
- API/interface definition;
- runtime configuration.

## Internal reuse decisions

Internal candidates can receive:

- `KEEP_INTERNAL`
- `EXTEND_INTERNAL`
- `ADAPT_INTERNAL`
- `REPLACE_INTERNAL`
- `REFERENCE_INTERNAL`
- `NOT_RELEVANT`

Do not replace a functioning internal component merely because an external alternative is more popular.

## Freshness

Regenerate or incrementally refresh the relevant map when:

- the base revision changes materially;
- manifests/lockfiles change;
- architecture boundaries change;
- the requested capability touches previously unmapped areas.

The map is evidence about a specific system state, not timeless truth.
