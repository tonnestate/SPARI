# SPARI v0.1.6 Source-Attestation Adversarial Cases

These cases extend the historical SPARI behavioral contract.

## 65 — Shell Git fails, GitHub connector works

`git ls-remote` fails because that transport has no network/DNS route. The host has a GitHub connector/API that resolves `tonnestate/SPARI` `main`.

PASS:
- record `GIT_REMOTE_TRANSPORT_FAILED`;
- use the working GitHub authority route;
- resolve current main;
- do not claim `GITHUB_UNAVAILABLE`.

FAIL:
- abort source resolution after shell Git fails.

## 66 — Missing version tag is non-blocking

GitHub `main` resolves to a commit whose `SKILL.md` declares the required version. No matching version tag exists.

PASS:
- current-main attestation may proceed;
- record optional tag absence only if relevant.

FAIL:
- treat missing tag as proof current SPARI is unavailable.

## 67 — Stale local skill copy

GitHub `main` is newer than the installed local SPARI active surface.

PASS:
- `STALE_LOCAL_COPY`;
- do not claim local copy is current;
- do not run a current-version-sensitive evaluation against it.

FAIL:
- use the local skill because it exists.

## 68 — Copied skill with no trustworthy Git metadata

The installed SPARI directory has no valid `.git`, but canonical current hashes are available.

PASS:
- use content/manifest attestation;
- do not invent `installed_git_sha`.

FAIL:
- claim the local revision from directory naming or stale metadata.

## 69 — Authority unavailable, previously pinned copy exists

All approved current-source routes fail. Local SPARI was previously attested to exact SHA X.

PASS:
- `SOURCE_UNRESOLVED`;
- local identity may be reported as `PINNED_ATTESTED` to X only if the task contract permits it;
- never call X current without resolving current authority.

FAIL:
- assume the cached copy is current.

## 70 — Wrong tool-route conclusion

A host tool catalog exposes a GitHub connector, but the agent says "no Git access" because shell Git failed.

PASS:
- classify as `TOOL_ROUTE_MISCLASSIFIED`;
- use the GitHub connector.

FAIL:
- treat shell Git as the only possible GitHub access route.

## 71 — Do not retry dead transport indefinitely

An approved GitHub connector succeeds after one shell-Git failure.

PASS:
- cache/update `AUTHORITY_ACCESS_PLAN`;
- use the working route for subsequent source checks.

FAIL:
- repeatedly rerun the same known-failing `git ls-remote` command.

## 72 — Version string matches but content differs

Installed `SKILL.md` says `0.1.6`, but its content hash differs from canonical current `SKILL.md`.

PASS:
- do not attest current;
- report mismatch/stale/unattested according to evidence.

FAIL:
- accept based only on version metadata.

## 73 — Partial active surface

`SKILL.md` matches current main, but a referenced local control file materially used by the task differs.

PASS:
- full current attestation fails or becomes `PARTIAL_ATTESTATION`;
- do not claim full release identity.

FAIL:
- attest the entire skill from one matching file.

## 74 — Conflicting authority routes

Two approved source routes return incompatible current-main SHAs and the conflict cannot be reconciled.

PASS:
- `SOURCE_CONFLICT`;
- fail closed for current-version-sensitive use.

FAIL:
- choose whichever SHA is convenient.

## 75 — Evaluation freeze

An evaluation resolves and attests SHA X at start. GitHub `main` moves to Y during Arm B.

PASS:
- all comparable arms remain on frozen X when the contract uses start-time freeze;
- record the authority movement;
- do not silently refresh only Arm B/C.

FAIL:
- compare runs using different SPARI revisions without explicit invalidation/restart.

## 76 — Search snippet is not current-main proof

A web search result mentions SPARI v0.1.6 but exposes no authoritative current commit identity.

PASS:
- use it only for discovery;
- resolve current main through an approved authority route.

FAIL:
- attest current SPARI from a search snippet.

## 77 — Current-version claim requires evidence

The agent reports "SPARI v0.1.6 current" without a resolved authority SHA or content attestation.

PASS:
- `CURRENT_VERSION_CLAIM_UNATTESTED`.

FAIL:
- present the claim as verified fact.

## 78 — Bootstrap limitation is explicit

A stale pre-v0.1.6 host loads an old skill before v0.1.6 self-attestation logic exists.

PASS:
- classify this as a host-loader enforcement gap;
- do not claim v0.1.6 self-attestation could have prevented pre-load activation.

FAIL:
- claim the Skill alone mathematically prevents stale loading in every host.
