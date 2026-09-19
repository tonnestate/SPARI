# SPARI-CLAUDECODE-EXECUTION-ENTROPY-001

Bounded paired evaluation of **Claude Code** with and without **SPARI v0.1.3**, focused on externally observable execution discipline rather than raw task capability.

## Corrected Verdict

**EXECUTION_DISCIPLINE_LIFT_ONLY**

Both arms completed all six tasks. SPARI did not increase verified task completion, but it materially reduced unproductive execution churn on recovery tasks.

The original executor export reported `EXECUTION_ENTROPY_REDUCTION_SIGNAL`. Under the frozen contract, that verdict required a lower median paired EEI and improvement on at least 3 of 4 non-control tasks. The observed data do not satisfy those stricter conditions:

- median EEI: 0 vs. 0
- non-control tasks with lower EEI: 2 of 4

The supported bounded conclusion is therefore `EXECUTION_DISCIPLINE_LIFT_ONLY`.

## Design

- Executor: Claude Code
- Same model/runtime in both arms
- Treatment: SPARI v0.1.3 ON vs. OFF
- Tasks: 6
- Executions: 12 paired runs
- Reuse tasks: 2
- Recovery tasks: 2
- Straightforward controls: 2
- Completion criteria identical within each pair
- Entropy measured from externally observable execution behavior only

## Results

| Task | Class | Baseline | SPARI | EEI A | EEI B | Pair result |
|---|---|---:|---:|---:|---:|---|
| 1 | Reuse | PASS | PASS | 0 | 0 | TIE |
| 2 | Reuse | PASS | PASS | 0 | 0 | TIE |
| 3 | Recovery | PASS | PASS | 5 | 1 | SPARI_BETTER |
| 4 | Recovery | PASS | PASS | 3 | 1 | SPARI_BETTER |
| 5 | Control | PASS | PASS | 0 | 0 | TIE |
| 6 | Control | PASS | PASS | 0 | 0 | TIE |

## Completion

- Baseline: **6/6 PASS**
- SPARI: **6/6 PASS**
- Completion lift: **0**

SPARI preserved verified completion.

## Execution Entropy

### Aggregate EEI

- Baseline total EEI: **8**
- SPARI total EEI: **2**
- Aggregate reduction: **75%**

### Recovery tasks only

- Baseline: **8**
- SPARI: **2**
- Reduction: **75%**

### Reuse tasks

- Baseline: **0**
- SPARI: **0**

### Controls

- Baseline: **0**
- SPARI: **0**

No observable entropy overhead appeared on straightforward tasks.

## Raw Observed Components

| Component | Baseline | SPARI |
|---|---:|---:|
| Unjustified plan changes | 3 | 1 |
| Repeated analysis events | 1 | 0 |
| Abandoned implementations | 2 | 0 |
| Redundant tool calls | 0 | 0 |
| Unnecessary escalations | 0 | 0 |
| Unnecessary files | 0 | 0 |

The strongest observed effect was not fewer tool calls. It was less rework and less strategy churn after failure.

## Recovery Mechanism

### Task 3

Baseline:

`fail → strategy guess → retry → another strategy change → success`

SPARI:

`fail → diagnose constraint → one deliberate recomposition → success`

EEI:

- Baseline: 5
- SPARI: 1
- Reduction: 80%

### Task 4

Baseline:

`failure → speculative retry → another speculative retry`

SPARI:

`failure → identify specific logic error → one deliberate recomposition`

EEI:

- Baseline: 3
- SPARI: 1
- Reduction: 67%

## Key Interpretation

The bounded observation is:

> SPARI did not make Claude Code complete more tasks in this evaluation. It changed how Claude Code recovered from failure.

On the two recovery tasks, SPARI replaced retry-driven churn with more deliberate evidence-driven recomposition while preserving 100% completion.

This supports a recovery-time execution-stabilization hypothesis.

It does not establish that SPARI generally reduces all forms of agent activity or makes Claude Code universally more capable.

## Important Clarifications

### No owner-escalation effect was demonstrated

Both arms had zero recorded unnecessary owner escalations.

The original executor report states that owner escalation was reduced "implicitly." That claim is not supported by the recorded metric.

Correct interpretation:

> No owner-escalation difference was observed in this closed-scope evaluation.

### No tool-spam reduction was demonstrated

Both arms recorded the same tool-call volume in the evaluated tasks.

The observed effect was in:

- plan churn,
- repeated analysis,
- abandoned implementations,
- rework.

Therefore this evaluation does not support a claim that SPARI reduced tool-call count.

### Wall-clock and token savings were not measured

The original report suggests likely time/token savings.

Those remain hypotheses.

This evaluation supports cleaner recovery behavior, not measured cost reduction.

## Bounded Conclusion

> In this bounded six-task paired evaluation, SPARI v0.1.3 preserved 100% Claude Code task completion while reducing observed execution entropy from 8 to 2 events across the two recovery tasks. The observed effect consisted primarily of fewer unjustified strategy changes, less repeated analysis, and fewer abandoned implementations. No entropy overhead was observed on the straightforward control tasks.

## Limitations

- Six paired tasks only
- Entropy differences occurred only on two recovery tasks
- Median EEI across all tasks remained 0 in both arms
- No measured token savings
- No measured wall-clock savings
- No observed owner-escalation difference
- No observed redundant tool-call difference
- No general claim about Claude Code models or other task classes

## Provenance

- Evaluation ID: `SPARI-CLAUDECODE-EXECUTION-ENTROPY-001`
- Date: 2026-09-19
- Executor: Claude Code
- Treatment: SPARI v0.1.3 ON vs. OFF
- Total executions: 12
- Original exported Markdown and JSON are preserved unchanged under `raw/`.
