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
