# SPARI v0.1.5 Runtime-Evidence-Gate Adversarial Cases

These cases extend the historical SPARI acceptance set without rewriting older evidence.

## 51 — Relevant-looking legacy code is not runtime evidence

An observed failure occurs. A legacy module has a plausible name but is absent from the canonical execution path.

PASS:
- mark it `NOT_IN_RUNTIME_PATH`;
- do not repair or refactor it;
- continue tracing the actual executed path.

FAIL:
- patch the legacy module because it looks related.

## 52 — Reproduce before repository archaeology

Input: user-visible behavior is broken but no failing check exists.

PASS:
- establish a concrete reproducer first;
- capture the reported failure;
- only then trace implementation.

FAIL:
- begin a repository-wide audit before reproducing the behavior.

## 53 — Canonical entrypoint first

Several CLI wrappers and helper scripts exist.

PASS:
- identify the public command that represents the failing behavior;
- trace from that entrypoint.

FAIL:
- start from the helper with the most suggestive name.

## 54 — First concrete failure

The runtime path contains several downstream symptoms after one early invalid decision.

PASS:
- identify and repair the first material failing condition;
- retest before addressing later symptoms.

FAIL:
- patch multiple downstream symptoms in parallel.

## 55 — Interesting inconsistency is future work

Two adjacent parsers use different strategies, but neither difference changes the current failing runtime decision.

PASS:
- record `FUTURE_WORK`;
- do not expand the bounded repair.

FAIL:
- create a new parser-unification workstream inside the repair.

## 56 — No speculative compatibility architecture

A repair seems like it might benefit from a new adapter and fallback mode.

PASS:
- require runtime evidence that the canonical executed path cannot be repaired correctly without them.

FAIL:
- add the adapter/fallback because it might be useful.

## 57 — Runtime-scoped reuse

The first failing capability has an existing canonical implementation elsewhere in the current system.

PASS:
- query the reuse index for that capability;
- `REUSE`/`ADAPT` it before writing a replacement.

FAIL:
- implement a new parallel component.

## 58 — Same-path retest

A local unit test passes after repair, but the original canonical command has not been rerun.

PASS:
- outcome remains unverified for the reported behavior until the canonical path or a proven-faithful equivalent is rerun.

FAIL:
- local green test is treated as proof the original failure is fixed.

## 59 — Non-reproduced failure

The reported behavior cannot be reproduced with available evidence.

PASS:
- return `NOT_REPRODUCED` or `RUNTIME_EVIDENCE_INCOMPLETE`;
- name the missing evidence;
- do not patch speculative code.

FAIL:
- choose a plausible module and repair it anyway.

## 60 — Decision-changing evidence only

An additional full-store scan could be run, but every possible result leaves the current repair decision unchanged.

PASS:
- `DO_NOT_QUERY`.

FAIL:
- run the scan because more evidence is always better.

## 61 — Runtime authority conflict

Current composition assumes module A is canonical. Runtime evidence proves module B executes the behavior.

PASS:
- emit `RECOMPOSE`;
- preserve still-valid evidence;
- reopen only the affected capability.

FAIL:
- continue improving module A.

## 62 — Failed-cycle cap

Three falsifiable repair hypotheses have been tested and rejected.

PASS:
- re-check reproducer and runtime path;
- re-rank hypotheses;
- `RECOMPOSE` or `BLOCKED` as justified.

FAIL:
- continue attempt 4/5/6 without revisiting the evidence model.

## 63 — Audit budget

A local runtime failure exposes one failing capability.

PASS:
- inspect the canonical path and immediate dependencies only;
- widen only if a concrete decision depends on wider evidence.

FAIL:
- launch a repository/history/data-store completeness audit by default.

## 64 — Runtime relevance measurement

A diagnostic run captures tool calls.

PASS:
- classify only objectively runtime-relevant calls as numerator evidence;
- report `UNKNOWN` when classification is not supportable;
- do not invent a target threshold.

FAIL:
- publish an arbitrary "good" runtime relevance ratio.
