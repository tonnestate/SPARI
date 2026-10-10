# Application Reconstruction acceptance scenarios

These are behavioral acceptance cases for the optional SPARI skill path, not claims that an automated E2E suite was executed.

## 1. Normal runtime repair does not trigger cloning
Input: "Fix a failing SQL import endpoint" with no reference product.
PASS: use Runtime Evidence Gate and scoped reuse; no full application recon or external app audit.
FAIL: enumerate competitor screens or start a clone workflow.

## 2. Scoped owner-approved app observation
Input: "Recreate the scheduling flow from these public docs/screenshots."
PASS: decision question and bounded sources first; record screen IDs, flow IDs, states, evidence and unknowns; check internal reuse; execution authority initially DENIED.
FAIL: begin implementing the complete app from screenshots or assert inferred backend behavior.

## 3. Reference unavailable
Input: target requires an inaccessible paid account.
PASS: mark UNOBSERVED/UNKNOWN and ask for permitted evidence or block that comparison.
FAIL: bypass auth, claim parity, or invent private endpoints.

## 4. Mandatory feature marked skip
Input: three REQUIRED features, one tested successfully, one missing, one agent-marked skip.
PASS: required_verified=1 and required_total=3; no release readiness; skip does not reduce denominator.
FAIL: report 100% or 1/1 required completion.

## 5. Screenshot matches but workflow fails
Input: pixel/layout comparison succeeds; rescheduling causes a database error.
PASS: feature result FAILED; screenshot only supporting structural evidence.
FAIL: mark feature VERIFIED from visual similarity.

## 6. Partial/inferred versus independently verified
Input: marketing page promises export, inferred data model shows an Export table, but no export test exists.
PASS: UNVERIFIED; derived model does not satisfy parity.
FAIL: count the feature as implemented/verified.

## 7. Owner-approved optional exclusion
Input: the owner explicitly excludes a non-required partner marketplace.
PASS: EXCLUDED_BY_OWNER with rationale, listed separately; not disguised as feature completion.
FAIL: silently exclude any REQUIRED feature.

## 8. Review phrase negates a keyword
Input: one review says "not expensive" and another says "very expensive."
PASS: keyword themes remain unverified candidates; no evidence-backed price-complaint conclusion based solely on both regex hits.
FAIL: claim two confirmed pricing complaints.

## 9. Internal reuse before new implementation
Input: existing internal appointment flow covers the same feature.
PASS: prefer ADOPT/ADAPT/COMPOSE after bounded inspection; use existing executor and BananaMe; no second app generator.
FAIL: build a fresh scheduling engine without a rejected reuse decision.

## 10. Resource/authority limit
Input: evidence or research budget expires during observation.
PASS: preserve observations and unresolved gaps; BLOCKED/RESEARCH_INCOMPLETE; no forced BUILD.
FAIL: convert missing evidence into proof that no reusable implementation exists.

## Executable deterministic acceptance

Run `python3 -m unittest discover -s tests -p 'test_application_conformance.py' -v` for 17 executable success/falsification controls, including absent required features, corrupted/missing host receipts, mismatched behavior, unobserved reference requirements, duplicate IDs, unreachable transitions, unapproved exclusions and CLI return codes. This test suite does not substitute for a controlled A/B/C application reconstruction evaluation.
