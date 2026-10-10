# Application Reconstruction (optional, evidence-first)

This bounded workflow adapts the publicly documented methodology of [Replica](https://github.com/Jakeschincariol/replica-skill) as **reference patterns**, not as a replacement controller. It does not install Replica, grant execution authority, promise a complete clone, or introduce another agent, storage service, or mandatory research stage.

## Admission and boundaries

Enter only when an approved engineering request explicitly needs to reconstruct a specific app's **observable functionality or user journeys**, or when observing that app can materially resolve the recorded Build-vs-Borrow decision. Normal runtime repair, feature requests without a reference product, and broad solution-family discovery must **not** trigger it.

1. Source Attestation and Economy Gate still run first. Pre-Execution Decision Gate records the exact target, platform, bounded user journey, required capabilities, constraints, decision question, evidence sources, and stop condition **before** consequential inspection.
2. Check relevant internal capabilities/Decision Memory and reusable host-native inspection, UI automation, screenshot diff, and testing tools first. Use DragonFruitMe or another existing approved observation provider only when justified. No parallel crawler, custom browser engine, agent, or repository-wide indexing.
3. Restrict observation to public material and access the owner is permitted to use. Never bypass authentication/paywalls/terms, invent access to other users' accounts, extract secrets, or assume a private API is reusable. User-provided screenshots and official documentation are legitimate evidence but not proof of hidden logic.
4. Set a bounded surface and stop once additional observations cannot change the decision, feature scope, or verification plan. Mark inaccessible surfaces **UNOBSERVED**, not absent.

## Observe: behavior inventory, not imagined implementation

Produce only when useful a compact `APPLICATION_BEHAVIOR_MAP` containing:

- target, platform and dated source references; stable screen IDs (`S01`) and flow IDs (`F01`);
- observed navigation, inputs, outputs, error/empty/loading/permissions/mobile states, and the core user journey;
- feature IDs (`C01`), evidence references and scope classification: `REQUIRED`, `OPTIONAL`, or `EXCLUDED_BY_OWNER`;
- each assertion's origin: `OBSERVED` (source or host), `DOCUMENTED` (official public documentation), `INFERRED`, or `UNKNOWN`.

Every `INFERRED` data entity, integration, backend behavior or mechanism remains a hypothesis and **cannot** satisfy coverage or authorize implementation. Do not treat matching screens or marketing claims as functional proof.

## Decide: existing SPARI composition remains authoritative

Map each **required** capability to the existing `REUSE_INDEX` / relevant `INTERNAL_SOFTWARE_MAP` slice and only then to targeted external prior art. Record `ADOPT`, `ADAPT`, `COMPOSE`, `REFERENCE`, `REJECT`, `BUILD` or `BLOCKED` under SPARI's existing decision rules.

The `CUSTOM_DELTA` is only behavior missing from proven reusable components. Observed similarity never grants `EXECUTION_AUTHORITY`. SPARI's pre-execution decision must be complete and `GRANTED` before the host executor can change source. BananaMe remains the repository observation/mutation/verification substrate where available. This method does not independently build, publish, deploy or rebrand applications.

## Verify: behavior parity with fail-closed denominators

If a comparison is material to the task, emit a small `BEHAVIOR_PARITY_MATRIX` for the scoped capabilities. Minimum fields per item: feature ID, scope/priority, target evidence ref, implementation ref, comparable observed test ref, result (`VERIFIED`, `PARTIAL`, `FAILED`, `UNVERIFIED`, `EXCLUDED_BY_OWNER`) and unresolved difference.

- Every `REQUIRED` feature **remains in the required denominator**, including missing, partial, untested, inaccessible and agent-marked `skip` rows. Only `VERIFIED` counts as completed; `PARTIAL` is not a pass.
- `EXCLUDED_BY_OWNER` is valid only for expressly owner-approved non-required scope; the agent may not silently reclassify a mandatory feature as excluded.
- Show `required_verified / required_total` as **counts**. An optional weighted or percentage diagnostic must expose its formula, denominator, exclusions and evidence; it never overrides a failed required capability.
- Run the same observable journey against the reference and implementation where legitimately accessible. Compare actions, state transitions, errors, persistence and outputs; screenshot/layout difference is supporting **structural** evidence only and cannot establish behavior parity.
- If the reference cannot be observed, label it `UNVERIFIED` / `UNOBSERVED`, never `VERIFIED`. A flow test absent from the evidence does not count as passed.
- Completion is refused if any required feature is not independently verified or a required hard gate fails. Do not present a cosmetic similarity score as release readiness.

Reuse an already available comparison utility if it meets these gates. Replica's `parity.py` is a **reference only**: its default `skip` logic removes a row from scoring, which is unsafe for required coverage.

## Optional sourced user-feedback signal

When user criticism could change the feature scope or composition, inspect only relevant, accessible feedback. Preserve exact review URL, date, excerpt, source and sampled denominator. Deterministic keyword/regex categorization may propose candidates, but is **not semantic verification** (negation such as "not expensive" is a counterexample). Treat low-sample, single-source, stale, promotional and contradictory feedback as qualified or unknown. No invented reviews, counts, scores or user demands. Never let sentiment silently override the owner's stated scope.

## Stop / failure handling

Use existing `BLOCKED`, research-incomplete and execution-denied rules. Unknown target access, missing feature evidence, contradictory observations and exhausted budgets do not become permission to BUILD or claims of 100% parity. Store only compact inspectable source references and decision results in existing SPARI outputs; do not add a permanent clone index or new governance authority.

Acceptance scenarios: `tests/application-reconstruction-cases.md`.
