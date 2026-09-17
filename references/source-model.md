# Source Model

SPARI v0.x uses an ecosystem-neutral evidence model and a small-first source strategy. Internal evidence and relevant memory are checked before external expansion. GitHub and PyPI remain the primary external software inventories in v0.x.

## Primary source classes

- `MEMORY` — relevant prior decisions/trajectories;
- `INTERNAL` — current system, history, dependencies, repair ingredients;
- `GITHUB` — primary external repository inventory;
- `PYPI` — primary Python package inventory.

Source order is governed by the current search radius, not by a requirement to query every source on every run.

## Supporting evidence sources

Examples:

- official documentation;
- deps.dev;
- OSV;
- OpenSSF;
- attestations;
- release metadata;
- local lockfiles/manifests.

## Generic artifact identity

A source artifact may contain:

- `source_type`
- `ecosystem`
- `namespace`
- `name`
- `version`
- `revision`
- `distribution_hash`
- `claimed_source`
- `verified_source`
- `provenance_state`
- `evidence_refs`

## Source verification

Use distinct states:

- `SOURCE_UNKNOWN`
- `SOURCE_CLAIMED`
- `SOURCE_VERIFIED`
- `SOURCE_CONFLICT`

A package metadata link is normally `SOURCE_CLAIMED` until stronger evidence connects the distribution to that source.

## Provenance

Provenance can establish origin/integrity evidence.

It does not by itself establish:

- security;
- suitability;
- maintenance quality;
- license compatibility;
- trust.

## Future adapters

The generic model may support future adapters such as:

- npm;
- crates.io;
- Go modules;
- Maven;
- NuGet;
- Hugging Face;
- OCI registries.

These are not required search sources in v0.x.

Adding an adapter must not silently broaden SPARI's mandatory research scope.
