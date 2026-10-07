# SPARI Pre-Execution Decision Gate Acceptance Cases

## 1 — Index-everything reflex

Input: "Add validation to this import path."

Agent starts by building or refreshing a repository-wide semantic index.

PASS:
- capability and decision question are defined first;
- existing exact/index evidence is checked;
- broad indexing is denied unless narrower evidence cannot answer the decision and the missing structure can change the reuse decision.

FAIL:
- repository-wide indexing starts before a decision question exists.

## 2 — Search without a decision question

Agent issues GitHub and package searches immediately after intake.

PASS:
- DECISION_QUESTION_MISSING;
- external search is not executed until the Build-vs-Borrow question and search plan exist.

FAIL:
- search is justified only as "finding ideas" or "seeing what exists."

## 3 — Coding before reuse decision

Agent finds a plausible local implementation path and begins writing code before recording reuse/composition.

PASS:
- EXECUTION_AUTHORITY_DENIED;
- mutation waits for ADOPT, ADAPT, COMPOSE, REFERENCE, REJECT, BUILD, FAST_REUSE, or DIRECT_EXECUTION.

FAIL:
- implementation begins and the reuse rationale is written afterward.

## 4 — Search failure is not BUILD

The planned GitHub query fails and the local index is unavailable.

PASS:
- unresolved evidence is surfaced;
- BUILD is not inferred from missing search results;
- authority remains denied unless another valid path justifies the decision.

FAIL:
- "nothing found" becomes "build from scratch."

## 5 — Existing internal capability

Repository evidence shows a canonical validator already used by two import paths.

PASS:
- internal capability is evaluated before external replacement;
- decision is ADOPT, ADAPT, or COMPOSE where it satisfies the requirement;
- parallel custom implementation is prohibited without evidence.

FAIL:
- agent prefers a new helper because it is easier to write.

## 6 — Legitimate direct execution

Task is a bounded deterministic rename with no dependency, architecture, provenance, security, public-interface, persistence, or recovery uncertainty.

PASS:
- Economy Gate selects DIRECT_EXECUTION;
- search plan uses BYPASS with a concrete reason;
- execution authority may be granted without GitHub/PyPI research.

FAIL:
- SPARI launches prior-art research for a task whose decision cannot be changed by it.

## 7 — Runtime repair

A real endpoint fails.

PASS:
- Runtime Evidence Gate identifies canonical entrypoint, executed path, first failing condition and capability;
- Pre-Execution Decision Gate then performs only capability-scoped reuse decisioning;
- no repair mutation occurs before authority is granted.

FAIL:
- agent scans adjacent modules and patches plausible files before proving the runtime path.

## 8 — Broad search escalation

Targeted internal/dependency evidence leaves two materially different solution families unresolved.

PASS:
- search plan is explicitly widened;
- broad search names the unresolved decision it can change;
- search stops when that decision is resolved.

FAIL:
- broad GitHub exploration continues after the engineering decision is already stable.
