# Research Budget

Research budgets control resource use. They do not define truth.

## Two independent stop conditions

### QUALITY_STOP

Research converges because:

- major solution families are stable;
- new searches mostly repeat known candidates;
- new candidates do not materially change the decision;
- finalists have sufficient evidence.

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

Prefer inexpensive parallel agents for high-recall collection.

Reserve stronger models for:

- finalist synthesis;
- difficult architecture comparisons;
- contradictory evidence;
- contrarian review;
- high-impact judgement.

## Fail closed

If the resource budget ends before sufficient evidence exists:

`RESEARCH_BUDGET_EXHAUSTED`

and:

`RESEARCH_INCOMPLETE`

Do not infer that no reusable solution exists.

Do not automatically route to `BUILD`.

The caller may increase the budget, accept a provisional decision, narrow the scope, or defer the decision.
