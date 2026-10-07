# Pre-Execution Decision Gate

SPARI v0.1.7 adds a small control gate between task intake and consequential search or implementation.

Its purpose is to stop a coding agent from entering an unconstrained explore-and-build loop before it has established what technical decision it is trying to make.

The gate is a controller, not another research pipeline.

## Governing rules

~~~text
NO BROAD SEARCH WITHOUT A DECISION QUESTION.
NO BUILD WITHOUT A REUSE DECISION.
NO CONSEQUENTIAL IMPLEMENTATION WITHOUT EXECUTION AUTHORITY.
~~~

A search, index build, repository map, external query, or source inspection is justified only when its result can change a named engineering decision.

A missing result, failed search, unavailable index, or imperfect candidate never means BUILD.

## Position in the loop

~~~text
SOURCE ATTESTATION
        ↓
ECONOMY GATE
        ↓
FAST_REUSE / DIRECT_EXECUTION?
   ├─ YES → bounded fast path
   └─ NO
        ↓
PRE-EXECUTION DECISION GATE
        ↓
DEFINE
        ↓
PLAN SEARCH
        ↓
TARGETED RETRIEVAL
        ↓
COMPARE
        ↓
REUSE DECISION
        ↓
EXECUTION AUTHORITY
~~~

Observed failures still use Runtime Evidence Gate to establish the canonical failing capability and executed path. Runtime evidence may inform the pre-execution decision, but repair mutation remains denied until execution authority is granted.

## 1. DEFINE before search

Produce a compact, inspectable decision state:

- required capability;
- material constraints;
- what is already known;
- what remains unknown;
- the single current Build-vs-Borrow decision question.

Do not persist hidden chain-of-thought. Persist only the decision-relevant summary and evidence references.

A valid decision question is specific enough that evidence can change the answer.

Good:

~~~text
Does the repository or an already-installed dependency provide the canonical
CSV validation capability required by this import path, or is a custom delta needed?
~~~

Bad:

~~~text
What should I build?
~~~

## 2. PLAN search before retrieval

Before non-trivial discovery, declare the smallest search plan that can answer the decision question.

The plan records:

- search mode: BYPASS, TARGETED, or BROAD;
- evidence sources to inspect;
- concrete queries/lookups;
- the decision each query can change;
- stop condition.

Prefer deterministic and already-available evidence:

~~~text
exact capability / symbol / interface
→ installed dependency / manifest
→ relevant Persistent Reuse Index slice
→ relevant Decision / Trajectory Memory
→ targeted local source
→ targeted external prior art
→ broad external discovery only when material solution-family uncertainty remains
~~~

R0–R4 are search radii, not a mandatory sequence.

## 3. Do not index by reflex

Do not build, refresh, or inject a broad repository index merely because a repository exists.

Broad indexing is justified only when:

1. the decision question cannot be answered from an existing index or narrower evidence;
2. the missing structural knowledge can materially change the reuse decision;
3. the planned scope is bounded to the smallest useful repository region where possible.

If a host already provides a repo map, code index, symbol search, skill, MCP tool, or equivalent capability, reuse it instead of rebuilding the same facility inside SPARI.

## 4. TARGETED RETRIEVAL

Execute only the planned lookups.

For every additional lookup ask:

~~~text
What current engineering decision can this result change?
~~~

If there is no concrete answer:

~~~text
DO_NOT_QUERY
~~~

New evidence may revise the search plan, but the revision must be explicit and evidence-driven.

## 5. COMPARE before BUILD

Classify the available path as one of:

- ADOPT
- ADAPT
- COMPOSE
- REFERENCE
- REJECT
- BUILD
- FAST_REUSE
- DIRECT_EXECUTION
- BLOCKED

BUILD is valid only when the decision record states why the known internal, installed, remembered, or searched candidates do not satisfy the required capability and why the remaining custom delta is necessary.

The absence of a perfect candidate is not sufficient.

## 6. EXECUTION AUTHORITY

Default:

~~~text
EXECUTION_AUTHORITY = DENIED
~~~

Grant:

~~~text
EXECUTION_AUTHORITY = GRANTED
~~~

only when the applicable path is decision-complete.

For consequential Build-vs-Borrow work, that means:

- capability defined;
- decision question defined;
- search plan completed or validly bypassed;
- relevant candidates/evidence evaluated;
- reuse decision recorded;
- Custom Delta bounded;
- hard constraints preserved.

For DIRECT_EXECUTION or FAST_REUSE, Economy Gate may authorize a BYPASS search plan when deterministic evidence proves that deeper prior-art decisioning cannot materially change the bounded intervention.

## 7. Executor boundary

An executor must not receive consequential mutation authority from SPARI without a decision reference whose authority state is GRANTED.

The execution contract carries:

- pre_execution_decision_ref;
- execution_authority;
- selected reuse/composition;
- bounded Custom Delta;
- prohibited scope changes;
- verification requirements.

If the executor discovers evidence that would change the reuse decision, authority returns to DENIED for the affected scope and SPARI enters ADAPT or RECOMPOSE.

## Failure behavior

Use explicit states:

- CAPABILITY_UNDEFINED
- DECISION_QUESTION_MISSING
- SEARCH_PLAN_MISSING
- BROAD_SEARCH_UNJUSTIFIED
- REUSE_DECISION_MISSING
- BUILD_JUSTIFICATION_MISSING
- EXECUTION_AUTHORITY_DENIED

Failure of this gate blocks consequential implementation. It does not authorize a fallback build.
