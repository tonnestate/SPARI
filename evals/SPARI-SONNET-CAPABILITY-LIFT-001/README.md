# SPARI-SONNET-CAPABILITY-LIFT-001

Bounded paired evaluation of **Claude Sonnet** with and without **SPARI v0.1.3**, using the same six-task suite previously used for the Haiku evaluation.

## Verdict

**BASE_MODEL_CAPABILITY_SATURATION_SIGNAL**

This result means that, on this bounded shared-task suite, Sonnet already completed all tasks without SPARI. SPARI still improved reuse-oriented execution on two tasks, but it produced no additional FAIL→PASS outcome lift.

This is not evidence that SPARI is ineffective on stronger models. It is evidence that the observed incremental treatment effect was smaller on Sonnet than on Haiku in this evaluation.

## Design

- Base model: Claude Sonnet
- Treatment: SPARI v0.1.3
- Reference evaluation: `SPARI-HAIKU-CAPABILITY-LIFT-001`
- Tasks: 6
- Executions: 12 paired runs
- Arms:
  - A: Sonnet baseline
  - B: Sonnet + SPARI v0.1.3
- Same task suite as Haiku evaluation
- Same acceptance criteria within each pair
- Mechanism tasks: 4
- Straightforward controls: 2

## Results

| Task | Class | Sonnet Baseline | Sonnet + SPARI | Pair result | Observed mechanism |
|---|---|---:|---:|---|---|
| 1 | Reuse / Build-vs-Borrow | PASS | PASS | SPARI_BETTER | pydantic/schema-based validation instead of hand-coded validation |
| 2 | Reuse / Build-vs-Borrow | PASS | PASS | SPARI_BETTER | `functools.lru_cache` instead of custom cache implementation |
| 3 | Recomposition / Recovery | PASS | PASS | TIE | SPARI recomposed, but baseline already handled the case successfully |
| 4 | Recomposition / Recovery | PASS | PASS | TIE | No recomposition required; both well below threshold |
| 5 | Straightforward control | PASS | PASS | TIE | None |
| 6 | Straightforward control | PASS | PASS | TIE | None |

### Pair-level result

- SPARI_BETTER: **2/6**
- TIE: **4/6**
- SPARI_WORSE: **0/6**
- INVALID: **0/6**

### Completion result

- Sonnet baseline verified completion: **6/6**
- Sonnet + SPARI verified completion: **6/6**
- Observed outcome lifts: **0**

### Mechanism tasks only

- SPARI_BETTER: **2/4**
- TIE: **2/4**
- SPARI_WORSE: **0/4**

### Controls

- Baseline PASS: **2/2**
- SPARI PASS: **2/2**
- Observed control regressions: **0**

## Key Evidence

### Task 1 — Reuse

Both arms passed the frozen acceptance criteria.

The baseline hand-coded validation logic. The SPARI arm identified and used `pydantic`/schema-based validation instead.

This is a reuse/maintainability improvement, not a completion lift.

### Task 2 — Reuse

Both arms passed with the same reported cache-hit performance.

The baseline used a custom dictionary-backed LRU cache. The SPARI arm used Python's standard-library `functools.lru_cache`.

This is a clear build-vs-borrow improvement, but not a FAIL→PASS outcome lift.

### Task 3 — Recomposition / Saturation

This task is the most important cross-model comparison.

- Haiku baseline: FAIL
- Haiku + SPARI: PASS after executed recomposition
- Sonnet baseline: PASS
- Sonnet + SPARI: PASS

Sonnet baseline handled the missing-email case gracefully without requiring a recovery step. SPARI still performed a recomposition path, but the baseline had already reached the required outcome.

This is the main basis for the saturation interpretation.

### Task 4 — Recomposition control

Both arms passed well below the <5s threshold.

- Sonnet baseline: ~0.068s
- Sonnet + SPARI: ~0.09s

No recomposition was required.

### Tasks 5–6 — Straightforward controls

Both arms passed. No measurable control regression was observed.

## Cross-Model Comparison

| Metric | Haiku 4.5 | Sonnet |
|---|---:|---:|
| Baseline PASS | 5/6 | 6/6 |
| SPARI PASS | 6/6 | 6/6 |
| SPARI_BETTER | 3/6 | 2/6 |
| TIE | 3/6 | 4/6 |
| SPARI_WORSE | 0/6 | 0/6 |
| Outcome lifts | 1 | 0 |
| Mechanism tasks improved | 3/4 | 2/4 |

The correct bounded interpretation is:

> The observed incremental SPARI treatment effect was smaller on Sonnet than on Haiku on this shared six-task evaluation.

The data do **not** support a general statistical claim that SPARI effectiveness is inversely correlated with model capability. Two models and six tasks are insufficient for that conclusion.

## Interpretation

The shared-task pattern is consistent with the following working hypothesis:

- On Haiku, SPARI can add both capability and reuse/recovery discipline.
- On Sonnet, SPARI mainly improves reuse/build-vs-borrow discipline because the base model already completes the tested recovery task successfully.

This is a hypothesis supported by the bounded observations, not a general law about model size.

## Bounded Conclusion

> In this bounded six-task paired evaluation, Claude Sonnet completed all tasks with and without SPARI v0.1.3. SPARI produced two reuse-oriented execution improvements but no additional verified-completion lift. Compared with the matching Haiku evaluation, the observed incremental SPARI effect was smaller on Sonnet, consistent with a base-model capability saturation signal under the tested conditions.

## Limitations

This evaluation does **not** establish:

- a general inverse relationship between model capability and SPARI benefit;
- that SPARI is unnecessary on stronger models;
- equivalence between Haiku + SPARI and Sonnet;
- population-level statistical significance;
- behavior outside the six tested tasks.

The sample is intentionally small and bounded.

## Corrections / Clarifications to the Original Executor Export

- The phrase `SPARI effectiveness inversely correlated with base-model capability` is too strong for two models and six tasks. The corrected wording is: **the observed incremental treatment effect was smaller on Sonnet than on Haiku in this bounded evaluation**.
- `BASE_MODEL_CAPABILITY_SATURATION_SIGNAL` is therefore treated as a bounded descriptive verdict, not as a general model-scaling law.
- Sonnet's 2/6 SPARI_BETTER results are reuse/engineering-discipline improvements, not verified-completion lifts.

## Provenance

- Evaluation ID: `SPARI-SONNET-CAPABILITY-LIFT-001`
- Date: 2026-09-19
- Executor: Claude Code
- Base model: Claude Sonnet
- Treatment: SPARI v0.1.3
- Total executions: 12
- Reference: `SPARI-HAIKU-CAPABILITY-LIFT-001`
- Original exported report and JSON are preserved unchanged under `raw/`.
