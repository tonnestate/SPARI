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
