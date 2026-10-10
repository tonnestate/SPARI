# Application Conformance: scoped, executable extension

This is an optional verification adjunct to `references/application-reconstruction.md`. SPARI's existing Source Attestation, Economy Gate, Pre-Execution Decision Gate, Build-vs-Borrow composition and execution authority remain authoritative. It is not a clone engine, second executor, or release authority.

## Model and deterministic oracle

- `schemas/application-behavior.schema.json`: bounded reference behavior, source references, requirements, states and expected transitions.
- `schemas/application-runs.schema.json`: execution observations without worker-declared PASS or success fields.
- `schemas/application-receipts.schema.json`: execution digests held by the host-controlled independent test harness.
- `tools/application_conformance.py`: stdlib-only validator and deterministic conformance evaluator. It enforces additional cross-reference, duplicate-ID, reachability, source-kind and owner-exclusion rules beyond JSON Schema.

Use an existing host observation tool to populate the behavior model. `OBSERVED` sources must correspond to independently inspectable reference observations; `DOCUMENTED` and `INFERRED` alone never establish behavioral parity. An `OWNER_APPROVAL` source permits excluding only non-required features. Before accepting a feature as required or excluded, the owner-approved **scope itself** must be established through SPARI's normal intake/authority process; a label inside model JSON cannot prove that scope was authorized.

A transition records `from_state`, `action`, expected `to_state`, `expected_output` and its requirement and reference evidence. Failure and permission states are ordinary modeled states, not exceptions. An externally observed output is compared for exact canonical JSON equality; no semantic equivalence, hidden API inference or nondeterministic timing tolerance is assumed. Complex or nondeterministic outputs require host normalization defined and independently verified *before* comparison; this tool does not infer it.

## Traceability and assurance boundary

For a declared requirement, the auditable chain is:

`source ID / locator -> requirement ID -> transition ID -> modeled oracle -> host run ID -> host receipt -> deterministic verdict -> SPARI execution decision`

The host computes each execution receipt as the SHA-256 of canonical UTF-8 JSON (`sort_keys=True`, compact separators, `ensure_ascii=False`) over:

```
{
  "model_sha256": "SHA-256 of canonical model JSON",
  "transition_id": "T1",
  "from_state": "FREE",
  "action": "book",
  "to_state": "BOOKED",
  "output": {"result": "confirmed"}
}
```

The harness provides the receipt file from a **separate, host-controlled trust boundary**. Do not let a worker create, overwrite or choose its own trusted receipt store. The digest detects mismatches and binds observed execution to the exact model; a hash is **not** a signature or independent evidence that the harness really ran. This tool cannot cryptographically authenticate the host, independently authenticate the reference application, or prevent reuse of a legitimate old receipt for an identically hashed model. Such identity, freshness, recording and write permissions belong to the host. Unknown receipt IDs, changed payloads or mixed trusted/untrusted attempts fail closed.

## Execute

```
python3 tools/application_conformance.py \
  --model model.json \
  --observations harness-runs.json \
  --trusted-receipts /host/protected/receipts.json

python3 -m unittest discover -s tests -p 'test_application_conformance.py' -v
```

Exit codes: `0` all *declared REQUIRED* behavior independently attested and matched; `1` one or more required transitions blocked/failed; `2` invalid contract/JSON. The output is JSON, including per-feature and per-transition reasons. `VERIFIED` does **not** mean production-ready: security, performance, usability, applicable regulations and SPARI's existing hard gates still apply.

`required_verified / required_total` is the definitive required-feature fraction. A required feature with zero transitions, missing evidence, skipped tests or inaccessible oracle remains in the denominator and **UNVERIFIED**. No percentage or layout similarity substitutes for that gate. Optional/owner-excluded features are reported separately. Completion always bears `DECLARED_OBSERVED_SCOPE_ONLY`; undiscovered functionality is an explicit completeness limitation. Observed transition conformance does not establish equivalence of unobserved traces or satisfy full ioco/conformance testing.

## Controlled assessment, not a success claim

For an A/B/C comparison freeze comparable target scopes and sources, model version, task and agent budgets and independently scored ground truth: A = SPARI without the reconstruction path; B = preceding markdown-only reconstruction; C = behavior model + deterministic gate. Evaluate required-feature omissions, false VERIFIED decisions, observed transition mismatches, relevant test coverage, intervention size, elapsed time and tokens/compute. Predefine stop criteria and failure handling, run independent negative controls, and report all arms, sample sizes and uncertainty. This release adds executable deterministic controls and unit cases; **it does not claim improved agent performance or full application equivalence** without the controlled study.
