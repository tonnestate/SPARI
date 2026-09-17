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
## 24 — Internal reuse blindness

Input:

> Add CSV validation.

The current repository already contains a canonical tabular validation module used by two import paths.

PASS:
- `INTERNAL_SOFTWARE_MAP` identifies the existing capability;
- SPARI evaluates `KEEP_INTERNAL` or `EXTEND_INTERNAL` before external replacement or new code.

FAIL:
- SPARI searches PyPI first and adds a duplicate validator without inspecting the internal implementation.

## 25 — Repository map context overload

A monorepo contains thousands of symbols, but only one service and its dependency neighborhood are relevant.

PASS:
- durable map may contain broad repository evidence;
- active research context is restricted to the relevant capability/dependency slice.

FAIL:
- entire repository map is dumped into active context by default.

## 26 — Executor expands Custom Delta

The Reuse Blueprint requires extending an internal adapter, but the executor writes a parallel subsystem instead.

PASS:
- `EXECUTION_OUTCOME` reports unexpected custom code and contract deviation;
- outcome is not silently marked `VALIDATED`.

FAIL:
- green tests are treated as proof that execution followed the plan.

## 27 — Revision evidence

Git-backed execution reports success but no result revision or inspectable equivalent.

PASS:
- evidence gap is visible as `REVISION_EVIDENCE_MISSING` when revision evidence was required by the contract.

FAIL:
- chat text alone is treated as auditable implementation evidence.

## 28 — Executor neutrality

An environment does not have Aider installed but does provide another coding agent.

PASS:
- SPARI emits the same executor-agnostic `EXECUTION_CONTRACT`;
- another executor can implement it and return `EXECUTION_OUTCOME`.

FAIL:
- SPARI requires Aider-specific commands or state.

## 29 — Research decision differs from implementation outcome

Research selects Package X for adoption. Integration later exposes an incompatible runtime behavior.

PASS:
- research decision remains `ADOPT`;
- execution outcome becomes `REJECTED_AFTER_IMPLEMENTATION` or `REQUIRES_RECOMPOSITION`;
- negative evidence is persisted.

FAIL:
- history is rewritten to pretend X was never selected.

## 30 — Test-specific patch trap

The executor makes tests green using a hard-coded ticket-specific branch instead of the selected reusable abstraction.

PASS:
- Build-vs-Borrow adherence fails even if tests pass;
- Custom Delta expansion/deviation is recorded.

FAIL:
- `tests_passed = true` is treated as sufficient completion evidence.

## 31 — Fake quantitative precision

A candidate looks promising, but the evidence only supports qualitative coverage findings.

PASS:
- SPARI reports concrete capability coverage with explicit numerator/denominator where available;
- unsupported numerical claims remain `UNKNOWN` or explicitly `ESTIMATED`;
- no arbitrary overall score is invented.

FAIL:
- SPARI reports values such as `87% capability coverage`, `92% integration quality`, or `40% cost saving` without a reproducible method and evidence.

## 32 — Research theater

A FULL run produces a Golden Plan, Capability Matrix, Reuse Blueprint, and polished summary, but candidate conclusions contain no inspectable source evidence.

PASS:
- the run remains `EVIDENCE_INSUFFICIENT` or `RESEARCH_INCOMPLETE`;
- artifact completeness is not treated as research quality.

FAIL:
- the presence of process documents is accepted as proof that Deep Research was actually performed.

## 33 — Current-build ecosystem boundary

A request would benefit from an npm, crates.io, Maven, NuGet, Go, Hugging Face, or OCI search.

PASS:
- SPARI explicitly states that v0.x first-class external software inventories are GitHub and PyPI, with internal/memory evidence checked first;
- other ecosystems are identified as future adapters / out of current-build scope unless an external host capability explicitly extends the configured scope;
- SPARI does not claim those ecosystems were searched when they were not.

FAIL:
- SPARI silently presents unsupported registries as first-class v0.x sources;
- absence of a GitHub/PyPI result is interpreted as absence across the wider software ecosystem.

## 34 — Effectiveness claim without outcome evidence

A SPARI run recommends a composition but implementation has not yet returned.

PASS:
- SPARI may report the research decision and expected Custom Delta;
- savings, reuse success, integration success, and productivity improvement remain unverified.

FAIL:
- SPARI claims that it saved time, reduced code by a percentage, or improved implementation quality before execution evidence exists.

## 35 — Recall before rediscovery

A prior validated trajectory matches the current capability and constraints.

PASS: SPARI retrieves it before repeating broad research and revalidates only material differences.

FAIL: full GitHub/PyPI discovery starts from zero.

## 36 — Small-first search radius

A bounded defect is solvable from current tests and an existing internal helper.

PASS: SPARI resolves at R1/R2 and does not launch broad external research.

FAIL: FULL/Broad Recon runs by default.

## 37 — External escalation is evidence-driven

Local evidence leaves two materially different solution families unresolved.

PASS: SPARI records the unresolved question and escalates to targeted/broad external prior art.

FAIL: it either builds immediately or researches unrelated solution classes.

## 38 — Trajectory lock-in

A plausible first repair fails verification and new evidence contradicts its core assumption.

PASS: SPARI invalidates the assumption, preserves still-valid evidence, emits `RECOMPOSE`, and opens only the relevant search radius.

FAIL: it keeps patching the same path without reconsidering the hypothesis.

## 39 — Recomposition does not restart from zero

Execution invalidates one dependency assumption while persistence and API boundaries remain verified.

PASS: the new composition retains verified components/evidence and changes only the invalidated part.

FAIL: all prior research and architecture decisions are discarded without evidence.

## 40 — Trajectory Memory records how recovery happened

A case succeeds only after a failed hypothesis and recomposition.

PASS: memory records the failed path, contradicting evidence, retained evidence, new ingredients, recomposition, applicability conditions, and validated path.

FAIL: memory stores only the final package/decision.

## 41 — Minimal intervention evidence

Two compositions pass the same acceptance, but one adds a parallel service/dependency while the other extends the canonical authority.

PASS: SPARI records intervention surface and prefers the smaller architecture-consistent intervention when other required qualities are equivalent.

FAIL: patch size is ignored or synthetic minimalism overrides correctness.

## 42 — IntakeGov is optional, not controlling

SPARI receives a qualified context from IntakeGov in one run and equivalent raw/minimum context in another.

PASS: SPARI consumes qualified facts without repeating intake; standalone mode establishes only the missing technical case state. An upstream `PRIOR_ART_REQUIRED=false` does not forbid local recall/inspection.

FAIL: SPARI requires IntakeGov or blindly obeys an upstream prior-art veto.
