# SPARI Adversarial Acceptance Cases

## 1 — Literal-search trap

Input: "I want a Python library for an Excel import."

PASS: Broad Recon includes Excel parsing, tabular ingestion, validation, ETL/import frameworks, and complete import systems; GitHub and PyPI both searched.

FAIL: only searches `excel import python` and immediately recommends openpyxl.

## 2 — Chair problem

Input: "I need a chair."

PASS: Broadens to seating, furniture, adjacent sets, and complete seating-area solutions without silently changing the requirement.

FAIL: only searches chairs, or assumes a dining set without confirmation.

## 3 — RAG tunnel vision

Input: "Build a RAG over our company knowledge."

PASS: Recon includes conventional RAG, hybrid retrieval, GraphRAG, knowledge graphs, knowledge platforms, and related document/agent-memory systems.

FAIL: immediately chooses a vector database.

## 4 — Package-only blindness

Input: "We need agentic video production."

PASS: searches complete GitHub systems before composing packages.

FAIL: searches only PyPI and rebuilds the product.

## 5 — Repo-only blindness

Input: "We found a great GitHub project."

PASS: checks whether PyPI packages solve weak sub-capabilities better.

FAIL: adopts the repo all-or-nothing.

## 6 — README hallucination

README claims production-grade multi-tenancy.

PASS: source/tests are inspected.

FAIL: capability marked yes from README alone.

## 7 — Popularity bias

A has 50k stars but violates runtime constraints; B has 2k and fits.

PASS: A fails hard gate.

FAIL: A wins by popularity.

## 8 — Search outage

GitHub access fails.

PASS: GITHUB_UNAVAILABLE + RESEARCH_INCOMPLETE, no automatic BUILD.

FAIL: concludes no repo exists.

## 9 — Missing license

Best-fitting repo has no license.

PASS: REFERENCE_ONLY or REVIEW_REQUIRED.

FAIL: public visibility treated as permission.

## 10 — Best composition

Repo A covers 70%; PyPI B improves one subsystem; internal C already solves persistence; 20% remains custom.

PASS: BASE A + DEPENDENCY B + KEEP_INTERNAL C + explicit CUSTOM_DELTA.

FAIL: rebuilds everything or blindly adopts A.

## 11 — Cheap research, strong judgement

PASS: broad discovery may use cheap parallel agents; final synthesis uses independent evaluator and contrarian.

FAIL: scouts self-select winners without review.

## 12 — Closed-loop failure learning

Package X looked ideal but fails during integration.

PASS: outcome stored as REJECTED_AFTER_IMPLEMENTATION or REQUIRES_RECOMPOSITION; future runs see it first.

FAIL: X remains permanently "approved."

## 13 — Validated reusable base

Previously evaluated component is legally cleared and integration-validated.

PASS: memory is checked first and evidence reused unless revalidation triggers fire.

FAIL: full research starts from zero.

## 14 — Deep research before Golden Plan

PASS: Broad Recon → qualified questions → confirmed intent → Golden Plan → Deep Research.

FAIL: expensive deep evaluation against unconfirmed narrow assumptions.

## 15 — Scope refinement vs intent replacement

Confirmed intent requires explicit graph relationships.

PASS: vector-only RAG cannot silently replace this.

FAIL: requirement collapses because simpler code is easier.

## 16 — Build justification

No candidate fully fits.

PASS: reuseable parts identified and BUILD applies only to the justified remaining delta.

FAIL: "nothing perfect exists, so build everything."
## 17 — Research depth proportionality

Input:

> Add a mature UUID validation dependency to an existing Python service.

PASS:
- uses PREFLIGHT or TARGETED research;
- checks existing dependencies and focused PyPI/GitHub evidence;
- does not launch a full multi-agent swarm without material ambiguity.

FAIL:
- runs the complete FULL workflow by default.

## 18 — Consequential decision cannot hide behind PREFLIGHT

Input:

> Choose the core workflow engine for a new durable multi-tenant product.

PASS:
- escalates to FULL;
- evaluates whole-product/framework alternatives and lifecycle implications.

FAIL:
- selects the first plausible package after a quick registry lookup.

## 19 — Research budget exhaustion

Deep Research reaches its configured resource envelope before finalists have sufficient evidence.

PASS:
- `RESEARCH_BUDGET_EXHAUSTED`;
- `RESEARCH_INCOMPLETE`;
- no automatic `BUILD`.

FAIL:
- treats budget exhaustion as evidence that no reusable solution exists.

## 20 — Claimed source mismatch

PyPI metadata points to GitHub Repo A, but artifact/provenance evidence cannot confirm the link.

PASS:
- source remains `SOURCE_CLAIMED` or becomes `SOURCE_CONFLICT`;
- SPARI does not report `SOURCE_VERIFIED`.

FAIL:
- copies Repo A code as if it were proven to be the package source.

## 21 — Provenance is not trust

A package has strong provenance/attestation evidence but known critical unresolved vulnerabilities.

PASS:
- provenance remains verified;
- security gate can still fail independently.

FAIL:
- provenance is interpreted as proof that the package is trustworthy/safe.

## 22 — Memory without context rot

SPARI memory contains hundreds of decisions, but only three match the current capability/runtime.

PASS:
- retrieves the relevant records plus required evidence references;
- does not inject the entire historical store.

FAIL:
- loads all prior decisions into active context.

## 23 — Future ecosystem adapter does not expand current scope

A solution has an npm ecosystem equivalent.

PASS:
- SPARI may record the possibility if discovered;
- v0.x does not silently make npm a mandatory search source unless the configured research scope explicitly includes it.

FAIL:
- every run expands into all known package registries.
