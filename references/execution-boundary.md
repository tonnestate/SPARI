# Execution Boundary and Outcome Contract

SPARI is a Build-vs-Borrow decision and composition layer.

It does not need to be the coding executor.

## Separation of responsibilities

```text
SPARI
decides what should be reused/composed/built
        ↓
EXECUTION_CONTRACT
        ↓
coding executor
implements the justified delta
        ↓
EXECUTION_OUTCOME
        ↓
SPARI
verifies decision adherence and learns
```

Possible executors include Aider, Claude Code, Codex, other coding agents, CI-assisted workflows, or humans.

The contract is executor-agnostic.

## Why this boundary exists

A coding system is optimized to modify software.

That creates a natural bias toward producing code.

SPARI exists to preserve the prior Build-vs-Borrow decision so execution cannot silently convert:

```text
reuse existing component
```

into:

```text
write a new helper because it is easier
```

## EXECUTION_CONTRACT

The handoff should identify:

- `golden_plan_ref`
- `reuse_blueprint_ref`
- `base_revision`
- `planned_custom_delta`
- `required_reuse`
- `required_internal_components`
- `allowed_substitutions`
- `prohibited_scope_changes`
- `hard_constraints`
- `verification_requirements`
- `evidence_requirements`

The contract can allow bounded adaptation, but scope expansion must be visible.

## EXECUTION_OUTCOME

The executor returns structured evidence such as:

- executor/type;
- repository;
- base/result revision;
- actual reused components;
- dependencies added/removed;
- files changed;
- actual custom delta;
- tests/verification executed;
- lint/static-analysis results;
- integration failures;
- abandoned components;
- unexpected custom code;
- contract deviations;
- evidence references.

## Revision linkage

When Git or another revision system is available, record the before/after revisions.

This makes the execution result auditable and lets later systems inspect the real implementation instead of trusting a chat summary.

## Test success is not enough

A test can pass while the system-level decision was violated.

Examples:

- a test-specific hard-coded route;
- duplicated helper instead of the required internal abstraction;
- replaced dependency despite a reuse decision;
- larger Custom Delta than approved.

Therefore SPARI checks both:

```text
behavioral verification
+
Build-vs-Borrow adherence
```

## Feedback

The structured result updates Decision Memory.

Research selection and implementation outcome remain separate fields.

A candidate can be:

```text
research_decision: ADOPT
implementation_outcome: REJECTED_AFTER_IMPLEMENTATION
```

This negative evidence is valuable future prior art.
