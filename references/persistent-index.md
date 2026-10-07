# Persistent Reuse Index

The persistent reuse index is SPARI's cheap lookup surface.

Its purpose is to prevent repository understanding from being rebuilt in model context on every task.

## Content

A deployment may index compact evidence about:

- repositories/workspaces and base revisions;
- manifests and lockfiles;
- packages/modules/services;
- symbols, exports, classes, functions, types and interfaces;
- API routes, schemas and public contracts;
- dependency edges;
- architecture authorities/boundaries;
- capability-to-code mappings;
- tests and evidence references;
- structural/AST/signature fingerprints;
- installed third-party dependencies;
- validated Decision Memory references;
- validated Trajectory Memory references;
- optional cached embedding/vector references.

The index should store evidence pointers and compact metadata rather than large source dumps.

## No reflexive indexing

The existence of a repository is not a reason to build or refresh a broad index.

Before index construction or broad refresh, Pre-Execution Decision Gate must identify:

- the decision question;
- why the current/existing lookup surface is insufficient;
- what additional indexed structure can change the reuse decision;
- the smallest affected scope.

Prefer an existing host-native repo map, code index, symbol search, or cached SPARI index over reconstructing equivalent repository intelligence.

## Exact before semantic

Prefer exact and structural matches first:

```text
capability key
→ symbol/export/type/API key
→ dependency/manifest key
→ structural fingerprint
→ validated memory key
```

Cached semantic retrieval may widen candidate recall after deterministic matching, but it should not silently promote a candidate to a reuse decision.

## Freshness

Index entries are evidence about a specific repository state.

Invalidate or incrementally refresh affected entries when:

- indexed files change;
- manifests or lockfiles change;
- API/schema signatures change;
- architecture boundaries change;
- relevant generated artifacts change;
- the base revision moves across material changes.

Unrelated repository changes should not force a full rebuild when dependency/freshness evidence permits incremental refresh.

## Active context

The model should receive only the relevant result slice:

```text
query/capability
→ exact/index candidates
→ dependency neighborhood
→ architecture-boundary filter
→ evidence references
→ source inspection only where needed
```

Do not inject the whole index into active context.

## Embeddings

Embeddings are optional cached infrastructure, not a mandatory per-task operation.

If embeddings are used:

- compute/update them outside the critical path where possible;
- bind them to content/revision identity;
- retrieve compact candidate references;
- verify material decisions against source/structured evidence.

## Relationship to Internal Software Map

The index is the fast lookup layer.

`INTERNAL_SOFTWARE_MAP` is the richer engineering view used when a task requires capability/dependency/architecture reasoning.

A deterministic hit may avoid building a fresh map. A stale or ambiguous hit may cause SPARI to load or refresh only the relevant map slice.
