# Execution Boundary, Evidence Checkpoints, and Recomposition

SPARI owns Build-vs-Borrow composition and recomposition. It does not need to be the coding executor.

## Separation of responsibilities

```text
SPARI composition vN
        ↓
EXECUTION_CONTRACT vN
        ↓
coding executor
implements a bounded justified delta
        ↓
EVIDENCE CHECKPOINT / EXECUTION_OUTCOME
        ↓
SPARI
CONTINUE | ADAPT | RECOMPOSE | STOP
```

Possible executors include Aider, Claude Code, Codex, other coding agents, CI-assisted workflows, or humans. The contract is executor-agnostic.

## Why the boundary exists

Execution systems are optimized to modify software. SPARI preserves the prior-art/composition decision so execution cannot silently convert `reuse/extend existing component` into `write a parallel helper/subsystem because it is easier`.

The boundary is not a one-way handoff. New execution evidence may return control to SPARI before the whole task is finished.

## EXECUTION_CONTRACT

Identify where applicable:

- `engineering_case_ref`;
- `composition_version`;
- `golden_plan_ref`;
- `reuse_blueprint_ref`;
- `base_revision`;
- `planned_custom_delta`;
- `required_reuse`;
- `required_internal_components`;
- `allowed_substitutions`;
- `prohibited_scope_changes`;
- `hard_constraints`;
- `intervention_constraints`;
- `verification_requirements`;
- `evidence_requirements`;
- `checkpoint_conditions`.

Bounded adaptation is allowed. Scope or architecture expansion must be visible.

## Evidence checkpoint

A checkpoint may be requested after a meaningful implementation/test step, after contradictory evidence, or before a material architecture/dependency expansion. Return inspectable evidence rather than narrative confidence.

SPARI may respond:

- `CONTINUE` — current composition remains supported;
- `ADAPT` — bounded implementation detail changes without changing composition;
- `RECOMPOSE` — material evidence invalidated or materially improved the current composition;
- `STOP` — safety, hard gate, or unresolved evidence prevents continuation.

## Recomposition contract

`RECOMPOSE` must record:

- triggering evidence;
- invalidated assumptions/hypotheses;
- retained evidence and components;
- abandoned path;
- newly discovered/retrieved repair ingredients;
- previous composition version;
- new composition version;
- Custom Delta before/after;
- intervention surface before/after;
- verification required for the new path.

Do not erase the failed path from history. It becomes Trajectory Memory.

## Intervention surface

Where measurable, record the surface of the intervention:

- production files changed;
- symbols/classes/functions changed;
- public interfaces changed;
- dependencies added/removed;
- services/authorities introduced;
- persistence/schema changes;
- architecture boundaries crossed;
- abandoned code/components.

The objective is not synthetic minimalism. Prefer the smallest architecture-consistent intervention that satisfies verified requirements.
