# SPARI-HAIKU-CAPABILITY-LIFT-001

Bounded paired evaluation of **Claude Haiku 4.5** with and without **SPARI v0.1.3**.

## Verdict

**STRONG_EXPLORATORY_CAPABILITY_LIFT_SIGNAL**

This is a small, bounded engineering evaluation. It is evidence of a capability-lift signal under the tested conditions, not evidence that SPARI makes Haiku universally smarter or equivalent to larger models.

## Design

- Base model: Claude Haiku 4.5
- Treatment: SPARI v0.1.3
- Tasks: 6
- Executions: 12 paired runs
- Arms:
  - A: Haiku 4.5 baseline
  - B: Haiku 4.5 + SPARI v0.1.3
- Execution order: alternating
- Acceptance criteria: frozen before execution and identical within each pair
- Mechanism tasks: 4
- Straightforward controls: 2

The test was designed to distinguish better execution from merely better analysis. A SPARI mechanism counted only when it changed actual execution.

## Corrected Results

| Task | Class | Baseline | SPARI | Pair result | Observed mechanism |
|---|---|---:|---:|---|---|
| 1 | Reuse / Build-vs-Borrow | PASS | PASS | SPARI_BETTER | Existing `jsonschema` dependency/pattern used instead of hand-coded validation |
| 2 | Reuse / Build-vs-Borrow | PASS | PASS | SPARI_BETTER | `functools.lru_cache` used instead of custom cache implementation |
| 3 | Recomposition / Recovery | FAIL | PASS | SPARI_BETTER | Plan change and recomposition actually executed |
| 4 | Recomposition / Recovery | PASS | PASS | TIE | Recomposition threshold detected but not triggered |
| 5 | Straightforward control | PASS | PASS | TIE | None |
| 6 | Straightforward control | PASS | PASS | TIE | None |

### Pair-level result

- SPARI_BETTER: **3/6**
- TIE: **3/6**
- SPARI_WORSE: **0/6**
- INVALID: **0/6**

### Completion result

- Baseline verified completion: **5/6**
- SPARI verified completion: **6/6**
- Observed outcome lift: **1 task** — Task 3, FAIL → PASS

### Mechanism tasks only

- SPARI_BETTER: **3/4**
- TIE: **1/4**
- SPARI_WORSE: **0/4**

### Controls

- PASS under baseline: **2/2**
- PASS under SPARI: **2/2**
- Observed control regressions: **0**

## Key Evidence

### Task 1 — Reuse

Both arms passed the frozen validator acceptance. The baseline implemented approximately 50 lines of custom validation logic. The SPARI arm identified and used the existing `jsonschema` library/pattern and implemented the solution in approximately 20 lines.

**Correction to the original executor report:** `jsonschema` is a third-party Python package, not part of the Python standard library. The reuse finding remains relevant; only the original classification was incorrect.

### Task 2 — Reuse

Both arms met the reported latency criterion. The baseline implemented a custom cache class (~15 lines); the SPARI arm used Python's standard-library `functools.lru_cache` (~3 lines).

The original acceptance criterion also required no memory leak. The exported report states the task passed but does not contain a separate memory-leak measurement. Therefore the reuse/code-size finding is supported by the exported evidence, while that sub-criterion should be treated as incompletely documented unless the underlying run evidence is published.

### Task 3 — Recomposition

This is the strongest result.

The baseline followed automatic column detection, encountered a row with missing email data, and failed without recovery.

The SPARI arm detected the failed execution path, changed strategy, executed a manual-mapping fallback, and then passed the frozen acceptance criterion.

This is an observed **execution lift**, not merely a planning or diagnostic difference.

### Task 4 — Recomposition control

Both arms passed the <5s performance criterion. The naive implementation completed fast enough, so actual recomposition was unnecessary. The pair is correctly classified as a tie.

### Tasks 5–6 — Straightforward controls

Both arms passed. No benefit and no degradation was observed from SPARI.

## Decision Rule

The preregistered bounded decision rule required:

1. at least 2 of 4 mechanism tasks classified SPARI_BETTER;
2. zero SPARI_WORSE results on mechanism tasks;
3. actual execution of at least one reuse/build-vs-borrow improvement and one recomposition/recovery improvement;
4. both control tasks remain PASS;
5. no material control regression;
6. winning claims tied to frozen acceptance or observable execution evidence.

Observed:

- 3/4 mechanism tasks SPARI_BETTER
- 0/4 mechanism tasks SPARI_WORSE
- reuse executed on Tasks 1–2
- recomposition executed on Task 3
- controls 2/2 PASS
- no observed control regression

Result: **STRONG_EXPLORATORY_CAPABILITY_LIFT_SIGNAL**

## Bounded Conclusion

> In this bounded six-task paired evaluation, Claude Haiku 4.5 with SPARI v0.1.3 demonstrated measurable engineering capability lift over the same Haiku baseline on tasks requiring reuse and/or execution-time recomposition, without observed degradation on the straightforward control tasks.

## Limitations

This evaluation is intentionally small and exploratory.

It does **not** establish:

- general intelligence improvement;
- universal SPARI benefit;
- equivalence to larger models;
- performance outside the tested engineering conditions;
- population-level statistical significance.

The tasks were bounded and simplified. The result should be replicated on additional real engineering tasks before broader claims are made.

## Corrections to the original executor export

- `jsonschema` was incorrectly described as Python stdlib; it is third-party.
- Completion counts were reported as baseline 4/6 and SPARI 5/6. The task-level table supports **baseline 5/6 and SPARI 6/6**.
- `TIE` is a pair-level comparison result, not an execution outcome, and should not be mixed into PASS counts.
- Task 2's exported evidence does not separately document the memory-leak sub-criterion.

## Provenance

- Evaluation ID: `SPARI-HAIKU-CAPABILITY-LIFT-001`
- Evaluation date: 2026-09-19
- Executor: Claude Code / Claude Haiku 4.5
- Treatment: SPARI v0.1.3
- Total paired executions: 12
- Publication package: corrected from the original exported Markdown and JSON artifacts while preserving both originals under `raw/`.
