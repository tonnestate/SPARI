# Source Attestation Gate

SPARI v0.1.6 adds a control-plane gate for a failure mode that ordinary repository reasoning cannot solve:

```text
authoritative source changed
+
local installed skill stayed stale
+
agent executed local copy
+
agent claimed current behavior
```

The Source Attestation Gate separates:

```text
SOURCE AUTHORITY
TRANSPORT / TOOL
CURRENT REVISION
INSTALLED SURFACE
ATTESTATION STATE
```

These are not interchangeable.

## SPARI authority

For SPARI itself:

```text
repository = https://github.com/tonnestate/SPARI
ref        = refs/heads/main
```

`main` is the current source of truth.

Tags/releases may describe releases but do not replace branch authority.

A missing version tag is therefore not a failure to resolve current SPARI when `main` is successfully resolved.

## Authority Access Plan

A failed transport does not prove the authority is unavailable.

At first source resolution in a session, inspect the host's available source-access capabilities and select an approved route.

Recommended classes, strongest practical route first:

1. host-native GitHub connector/API;
2. direct GitHub REST/GraphQL/fetch capability;
3. shell Git remote access;
4. direct GitHub page/fetch only when exact commit identity is exposed.

Search-engine snippets and cached search results are not sufficient to prove the current `main` SHA.

Record the route:

```text
AUTHORITY_ACCESS_PLAN
```

and reuse it until the route fails or stronger contradictory evidence appears.

Do not repeatedly retry one known-dead route while ignoring another already-available authority route.

## Transport semantics

Examples:

```text
git ls-remote fails
+
GitHub connector resolves main
=
GIT_REMOTE_TRANSPORT_FAILED
+
AUTHORITY_RESOLVED
```

Not:

```text
GITHUB_UNAVAILABLE
```

Only emit:

```text
SOURCE_UNRESOLVED
```

when every approved route is unavailable or unable to resolve the required authority state.

If two authority routes return incompatible current-main identity and the conflict cannot be reconciled:

```text
SOURCE_CONFLICT
```

Fail closed for version-sensitive use.

## Current-source evidence

Capture at minimum:

```text
repository
authoritative_ref
resolved_main_sha
authority_transport
canonical_skill_version
canonical_skill_sha256
attested_at
evidence_refs
```

When available also capture the canonical release-manifest identity.

## Installed-surface evidence

An installed SPARI copy may be:

- a valid Git clone;
- a copied skill directory;
- a packaged skill;
- a directory with missing/broken/empty `.git`;
- a partial active instruction surface.

Never invent an installed revision.

### Git revision attestation

When trustworthy Git metadata exists:

```text
installed HEAD == required SHA
```

is strong revision evidence.

### Content/manifest attestation

When the installed skill is not a valid Git checkout, compare canonical file hashes.

At minimum, attest every local file that can materially affect the active SPARI behavior required by the task.

For full-release attestation, compare the canonical release manifest/surface.

Matching only `metadata.version` is insufficient.

```text
version string == 0.1.6
```

does not prove:

```text
installed instructions == authoritative v0.1.6
```

## Attestation states

### CURRENT_ATTESTED

Current authority resolved and installed required active surface matches it.

Normal "use current SPARI" may proceed.

### PINNED_ATTESTED

Installed surface matches an exact non-current or frozen SHA explicitly permitted by the current contract.

Appropriate for a preregistered evaluation frozen to that SHA.

Must not be called `current`.

### PARTIAL_ATTESTATION

Some but not all required active files were verified.

Proceed only if the task contract explicitly permits that reduced surface.

### STALE_LOCAL_COPY

Current authority is resolved and installed surface is proven different/older.

Do not use the local copy as current SPARI.

### INSTALLATION_UNATTESTED

Current authority is resolved but the installed active surface cannot be proven to match it.

Do not claim current SPARI.

### SOURCE_UNRESOLVED

Current authority cannot be resolved through any approved available route.

A previously attested local copy may be named by its exact known identity but not promoted to current.

### SOURCE_CONFLICT

Authority-resolution evidence conflicts.

Do not guess.

## Evaluation freeze

Controlled evaluations require reproducibility.

At evaluation start:

```text
resolve current main
→ attest active evaluation surface
→ record exact SHA
→ freeze exact SHA for all comparable arms
```

A tag is not required unless the evaluation contract explicitly requires one.

Do not refresh only one experimental arm.

If the evaluation contract requires current-main freshness continuously rather than a start-time freeze, any main movement must be handled consistently across all comparable arms.

## Source-sensitive operations

Require an allowed attestation state before:

- claiming a SPARI version as current;
- running a version-sensitive SPARI evaluation;
- publishing results attributed to current SPARI;
- comparing local SPARI behavior to GitHub current behavior;
- executing a contract that explicitly names the current SPARI revision.

## Tool-routing failure as evidence

Tool routing itself is measurable.

Record:

```text
available authority route classes
route selected
failed routes
fallback route
resolution result
retries
latency/cost where available
```

A false statement of `GITHUB_UNAVAILABLE` while an approved GitHub connector could resolve the source is a Tool Routing / Authority Resolution violation.

## Bootstrap boundary

A stale v0.1.5 skill cannot obey v0.1.6 instructions it has never loaded.

Therefore v0.1.6 provides:

```text
SELF_ATTESTATION_CONTRACT
```

but hard pre-activation prevention requires:

```text
HOST_LOADER_ATTESTATION
```

A robust host should resolve/attest the skill before activation.

SPARI must not claim that a self-check can retroactively prevent stale instructions from being read.

## Minimal principle

```text
local copy = cache
transport = route
GitHub main = authority
attestation = proof
```
