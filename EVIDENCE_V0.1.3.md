# SPARI v0.1.3 — Bounded Evaluation Summary

**Version under review:** SPARI v0.1.3  
**Evidence source:** repository evaluation artifacts under `evals/`  
**Evidence date:** 2026-09-19  
**Status:** Experimental / bounded evidence

This document consolidates the corrected v0.1.3 evaluation artifacts. It does not generalize beyond the tested tasks/models.

## Haiku capability-lift evaluation

Evaluation: `SPARI-HAIKU-CAPABILITY-LIFT-001`

- six paired tasks / twelve executions;
- baseline verified completion: 5/6;
- SPARI verified completion: 6/6;
- pair-level: SPARI better 3, tie 3, worse 0;
- one verified outcome lift occurred on a recomposition/recovery task;
- two additional improvements were reuse-oriented execution choices.

Corrected bounded verdict in the repository artifact:

`STRONG_EXPLORATORY_CAPABILITY_LIFT_SIGNAL`

Limitations include the small six-task sample, bounded/simplified tasks, no population-level significance claim, and no larger-model-equivalence claim.

## Sonnet capability-lift evaluation

Evaluation: `SPARI-SONNET-CAPABILITY-LIFT-001`

- six paired tasks / twelve executions;
- baseline verified completion: 6/6;
- SPARI verified completion: 6/6;
- pair-level: SPARI better 2, tie 4, worse 0;
- no verified-completion lift;
- the two SPARI improvements were reuse-oriented execution choices.

Corrected bounded verdict:

`BASE_MODEL_CAPABILITY_SATURATION_SIGNAL`

The artifact's bounded interpretation is that the incremental SPARI treatment effect was smaller on Sonnet than on Haiku for this shared six-task evaluation. This is not evidence of a universal inverse relationship between model strength and SPARI value.

## Claude Code execution/recovery evaluation

Evaluation: `SPARI-CLAUDECODE-EXECUTION-ENTROPY-001`

Both arms completed 6/6 tasks. The original corrected analysis observed fewer recovery-churn events under SPARI, but its frozen threshold for the named entropy-reduction signal was not met across the full non-control set. Its conservative corrected verdict was:

`EXECUTION_DISCIPLINE_LIFT_ONLY`

A subsequent methodology cleanup (`SPARI-EXECUTION-ENTROPY-METHODOLOGY-CLEANUP-001`) recoded productive evidence-driven recomposition as zero entropy and removed double counting. For the two bounded recovery tasks it reported:

- baseline unproductive recovery EEI: 4;
- SPARI unproductive recovery EEI: 0;
- completion remained 100% in both arms.

Its bounded verdict was:

`OBSERVED_RECOVERY_ENTROPY_ELIMINATED`

This 4→0 result applies only to those two audited recovery tasks and must not be generalized to all agent work.

## Relationship to v0.1.2 evidence

`EVIDENCE.md` preserves the v0.1.2 controlled program, including cases where FULL-SPARI added substantial compute without material outcome gain over a strong Luna + IntakeGov baseline.

The v0.1.3 evidence does not erase those negative findings. Together they motivate a narrower hypothesis:

> SPARI appears most promising when it supplies reuse discipline and evidence-driven recovery/recomposition, while unnecessary front-loaded research can be economically negative.

## v0.1.4 implication

v0.1.4 introduces Economy Gate and persistent-index mechanisms specifically to test whether SPARI can preserve the useful v0.1.3 behavior while avoiding unnecessary cognitive/research cost on bounded work.

This is a design hypothesis, not yet a measured v0.1.4 result.

No fixed token-saving percentage, universal capability lift, or model-equivalence claim is supported by the current evidence.
