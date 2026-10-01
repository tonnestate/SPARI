# Runtime Evidence Gate

SPARI v0.1.5 adds Runtime Evidence Gate for bounded engineering work that begins with an observed failure.

The gate prevents a common agent failure mode:

```text
symptom
→ broad repository audit
→ plausible legacy/adjacent code
→ speculative repair/redesign
→ real executed path still unknown
```

The replacement is:

```text
symptom
→ canonical entrypoint
→ reproduce
→ actual executed path
→ first concrete failing condition
→ capability-scoped reuse lookup
→ minimal repair
→ same-path retest
```

## Governing rule

> Runtime evidence outranks repository speculation.

Repository structure is evidence about what exists.

Runtime evidence is evidence about what actually participated in the observed behavior.

The two must not be conflated.

## Triggers

Use Runtime Evidence Gate for:

- `OBSERVED_FAILURE`;
- `BROKEN_BEHAVIOR`;
- `WRONG_OUTPUT`;
- `PERFORMANCE_REGRESSION`;
- `INTERMITTENT_FAILURE`;
- `FAILED_ACCEPTANCE_GATE`;
- `REAL_E2E_FAILURE`.

It is not mandatory for greenfield feature design without an observed failure.

## Gate 1 — Canonical entrypoint

Identify the public/operational entrypoint:

- CLI command;
- HTTP/API endpoint;
- UI action;
- MCP tool;
- library call;
- scheduled/background entry;
- trustworthy failing check that faithfully exercises the same runtime path.

Do not start from a file name.

If the entrypoint is unknown:

```text
CANONICAL_ENTRYPOINT_UNKNOWN
```

Obtain only the smallest evidence required to resolve it.

## Gate 2 — Reproduction

Create or use a concrete signal for the reported failure.

A valid reproducer should make it possible to distinguish:

```text
BUG_PRESENT
BUG_ABSENT
```

It may be a test, command, API request, UI automation, replayed trace, bounded harness, performance measurement, or other faithful host-provided signal.

If reproduction fails:

```text
NOT_REPRODUCED
```

or:

```text
RUNTIME_EVIDENCE_INCOMPLETE
```

Do not compensate by guessing which implementation to patch.

## Gate 3 — Executed path

Trace only enough of the real execution to locate the first material failing condition.

Useful evidence:

- stack/call trace;
- failing test trace;
- structured logs;
- request trace;
- targeted instrumentation;
- debugger/REPL observation;
- coverage slice;
- import/call graph tied to the execution;
- concrete data-access/dependency events.

Insufficient by itself:

- repository proximity;
- file/module naming similarity;
- historical importance;
- old/legacy resolver presence;
- README description;
- "could be related".

Code not shown to participate is:

```text
NOT_IN_RUNTIME_PATH
```

Default:

```text
DO_NOT_REPAIR
DO_NOT_REFACTOR
```

unless root-cause evidence points to it.

## Gate 4 — First concrete failure

Find the earliest concrete condition that materially breaks the canonical run.

Examples:

- wrong branch selected;
- expected authority not called;
- actual authority returns invalid state;
- dependency call fails;
- data lookup violates a verified invariant;
- output diverges at a known boundary.

Fix one root-cause condition at a time.

Do not jump from one local failure into repository-wide completeness work unless that completeness decision is required to fix the current failure.

## Gate 5 — Capability-scoped reuse

Translate the first failure into a capability query:

```text
failing capability
→ Persistent Reuse Index
→ exact symbol/interface/route/schema
→ canonical internal implementation
→ installed dependency
→ prior Decision/Trajectory
```

The lookup asks:

> Does a working implementation or previously validated repair ingredient already exist for this failing capability?

It does not ask:

> What else in the repository might be interesting?

## Gate 6 — Runtime Custom Delta

Prefer existing/canonical components.

Only the remaining repair becomes:

```text
RUNTIME_CUSTOM_DELTA
```

Definition:

> The smallest architecture-consistent change on the actually executed path that repairs the reproduced failure under the verified constraints.

A new service, adapter, contract, store, schema, mode, fallback, rebuild path or compatibility layer requires evidence that the canonical path cannot be repaired correctly without it.

## Gate 7 — Same-path retest

After repair, run the same canonical path or a proven-faithful equivalent.

Required question:

```text
Does the original failing behavior now pass?
```

A different adjacent test may add evidence but does not replace the canonical retest.

## Gate 8 — Close / adapt / recompose

- `PASS`: original path passes required evidence.
- `ADAPT`: bounded local adjustment remains.
- `RECOMPOSE`: runtime evidence invalidates active composition/hypothesis/authority.
- `BLOCKED`: required evidence cannot be obtained.
- `RUNTIME_EVIDENCE_INCOMPLETE`: runtime path remains insufficiently evidenced.

## Decision-changing evidence only

Before another query, scan, file read or research branch:

```text
What technical decision can this result change?
```

If there is no concrete answer:

```text
DO_NOT_QUERY
```

This is especially important for:

- full-store scans;
- full-history scans;
- broad code search;
- alternative parser/adapter comparisons;
- external research;
- adding instrumentation.

## Audit budget

Default scope:

1. canonical entrypoint;
2. executed path;
3. current failing capability;
4. immediate runtime dependencies;
5. smallest evidence required to distinguish live hypotheses.

Non-blocking findings:

```text
FUTURE_WORK
```

They may be recorded without expanding the current repair.

## Falsifiable hypotheses

A hypothesis should make a prediction that a bounded observation can falsify.

Use targeted instrumentation.

Prefer one probe mapped to one prediction over logging everything and searching afterward.

## Failed-cycle cap

After three falsified hypothesis-test cycles by default:

- re-evaluate the reproduction loop;
- re-evaluate the canonical path;
- re-rank hypotheses;
- `RECOMPOSE` or `BLOCKED` when appropriate.

Deployments may configure another cap. Three is a practical default, not a universal optimum claim.

## Evidence record

A `RUNTIME_GATE_RESULT` may contain:

```text
task_id
repository
base_revision
entrypoint
reproduction_status
observed_failure
execution_path
first_failure
failing_capability
reuse_candidates
selected_existing_component
runtime_custom_delta
nonblocking_findings
retest
metrics
status
evidence_refs
```

See `../schemas/runtime-evidence-gate.schema.json`.

## Metrics

When captured:

```text
request_count
tool_call_count
files_inspected
irrelevant_files_inspected
stores_scanned
queries_executed
runtime_relevant_tool_calls
runtime_relevance_ratio
time_to_first_concrete_failure
speculative_intervention_count
failed_hypothesis_cycles
```

Do not create a universal threshold before evaluation supports one.

## Privacy of reasoning

Persist:

- commands/actions;
- observations;
- execution path;
- evidence references;
- failing condition;
- hypothesis summary;
- test result;
- reuse decision;
- repair outcome.

Do not persist hidden chain-of-thought.
