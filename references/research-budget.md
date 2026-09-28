# Research Budget

SPARI v0.1.4 separates **admission cost control** from **research budgets**.

## 1. Admission control

Before model-heavy SPARI work, the Economy Gate asks whether additional decisioning is justified at all and what maximum profile is appropriate.

Admission may consider configured evidence such as:

- qualitative execution burden;
- optional caller-provided token/time/cost estimates;
- expected rework exposure;
- architecture/dependency/security/license risk;
- previous failed attempts;
- unresolved decision value.

Do not fabricate numeric estimates or a universal break-even threshold.

## 2. Research budget after admission

### QUALITY_STOP

Research converges because major solution families are stable, new searches mostly repeat known candidates, new candidates do not materially change the decision, and finalists have sufficient evidence.

### RESOURCE_STOP

A configured resource envelope is exhausted.

Possible controls:

- `max_scouts`
- `max_candidates_screened`
- `max_candidates_deep_inspected`
- `max_proofs_of_fit`
- `max_strong_model_escalations`
- optional `max_tokens`
- optional `max_cost`

## Cheap breadth, strong judgement

Prefer inexpensive collection for high recall. Reserve stronger models for finalist synthesis, difficult architecture comparisons, contradictory evidence, contrarian review, and high-impact judgement.

## Fail closed without over-escalating

If a research budget ends before sufficient evidence exists:

```text
RESEARCH_BUDGET_EXHAUSTED
→ RESEARCH_INCOMPLETE
```

Do not infer that no reusable solution exists and do not automatically route to `BUILD`.

If the Economy Gate itself is undecidable because its deterministic evidence is missing/stale, fall back to the smallest useful local inspection rather than FULL research.
