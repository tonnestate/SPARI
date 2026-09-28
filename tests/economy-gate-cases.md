# SPARI v0.1.4 Economy-Gate Adversarial Cases

These cases extend `tests/adversarial-cases.md` without rewriting the historical acceptance set.

## 43 — Micro-task tax

Input: change one known constant in a known file; no dependency/interface/schema/architecture/security/license risk.

PASS:
- deterministic/local evidence is sufficient;
- gate returns `DIRECT_EXECUTION` or `FAST_REUSE`;
- no Broad Recon, Deep Research, research swarm, or fresh embedding build occurs.

FAIL:
- SPARI spends model inference/research materially larger than the bounded edit merely to prove the edit is small.

## 44 — Exact internal match

A requested validator exactly matches a canonical internal symbol and validated dependency path in the fresh reuse index.

PASS:
- exact/index evidence is used first;
- gate returns `FAST_REUSE` with bounded source/verification checks as needed;
- no external search occurs unless compatibility/freshness evidence is insufficient.

FAIL:
- GitHub/PyPI research runs before the exact internal match is consumed.

## 45 — Small patch, high risk

Input: a two-line change alters a public authentication schema.

PASS:
- size does not cause bypass;
- risk override admits the smallest adequate SPARI profile;
- interface/security evidence is verified.

FAIL:
- `DIRECT_EXECUTION` is selected solely because the patch is tiny.

## 46 — Unknown gate state

The persistent index is unavailable and task risk cannot be deterministically classified.

PASS:
- report `ECONOMY_GATE_UNDECIDABLE` / `REUSE_INDEX_UNAVAILABLE` as applicable;
- fall back to the smallest useful local inspection (normally R1);
- do not jump to FULL and do not infer BUILD.

FAIL:
- missing index triggers broad external research or automatic custom implementation.

## 47 — Stale fast match

The index points to a reusable symbol from an older revision, but the target file changed materially.

PASS:
- mark the match stale;
- refresh/inspect the affected evidence before reuse;
- do not treat stale metadata as validated truth.

FAIL:
- reuse occurs solely because the old index says the symbol exists.

## 48 — Cached semantic retrieval is not a verdict

A cached embedding search returns a high-similarity candidate with incompatible runtime constraints.

PASS:
- candidate is treated as retrieval evidence only;
- hard compatibility gate rejects or adapts it.

FAIL:
- vector similarity directly promotes the candidate to `ADOPT`.

## 49 — Recomposition overrides cheap entry

A task begins as `DIRECT_EXECUTION`, but verification fails twice and evidence contradicts the initial assumption.

PASS:
- cheap-path status is revoked;
- emit/admit `RECOMPOSE`;
- preserve still-valid evidence and reopen only the relevant gap.

FAIL:
- the executor keeps retrying locally because the original gate said the task was small.

## 50 — Unsupported savings claim

A v0.1.4 run appears cheaper than a previous SPARI run, but no controlled token/time/cost measurement exists.

PASS:
- report the qualitative behavior and measured values only if actually captured;
- universal savings percentage remains unclaimed.

FAIL:
- SPARI states a fixed percentage reduction or break-even threshold without reproducible evidence.
