# SPARI

<p align="center">
  <strong>Classify before you execute.</strong><br>
  An Software Intelligence and Reuse Layer for AI Agents
</p>

<p align="center">
  <img alt="License" src="https://img.shields.io/badge/license-Apache--2.0-blue">
  <img alt="Status" src="https://img.shields.io/badge/status-experimental-orange">
  <img alt="Version" src="https://img.shields.io/badge/version-0.1.0-green">
  <img alt="Agent Skill" src="https://img.shields.io/badge/agent-skill-purple">
</p>

---
**Software Prior Art & Reuse Intelligence**

> Before AI agents write more code, make them discover what already exists.

SPARI is an Agent Skill for **GitHub-first and PyPI-first software reuse intelligence**.

It changes the normal agent order from:

```text
request → code → patches → more code → rediscover existing solution
```

to:

```text
raw intent
→ broad GitHub/PyPI recon
→ solution-space map
→ a few qualified questions
→ Golden Plan
→ deep GitHub/PyPI research
→ source inspection
→ reuse composition
→ minimal custom delta
→ implementation
→ outcome feedback
→ reusable decision memory
```

## Why Broad Recon comes first

Users often know the problem better than the software landscape.

If a user asks for a "chair", searching only for chairs can fail when the real need is a complete seating area. SPARI therefore broadens the first search semantically without silently changing the user's requirement.

```text
literal request
→ underlying capability
→ parent category
→ adjacent solution classes
→ complete systems solving the same outcome
```

Only after seeing what actually exists does SPARI ask a few evidence-informed questions.

## GitHub and PyPI are software inventories

SPARI asks:

- Which GitHub repository is the best existing base?
- Which PyPI packages solve individual capabilities better?
- What should remain from the current system?
- What can be reused directly?
- What is reference-only?
- What must actually be built?
- Did the selected software work after implementation?

The output is a composition, not a link list.

## The closed loop

SPARI is not finished when it recommends a repository.

```text
DISCOVER
→ EVALUATE
→ COMPOSE
→ HAND OFF
→ IMPLEMENT
→ VERIFY OUTCOME
→ STORE DECISION
→ REVALIDATE WHEN NEEDED
→ DISCOVER SMARTER NEXT TIME
```

Without that loop, the next agent burns the same tokens again.

## Relationship to IntakeGov

[IntakeGov](https://github.com/tonnestate/IntakeGov) decides what kind of work this is and whether enough is known to begin useful reconnaissance.

SPARI deliberately starts at `RECON_READY`, before the full technical solution is frozen.

## Broad Recon vs Deep Research

**Broad Recon** is cheap, broad, and fast. It maps solution families and discovers the few questions that matter.

**Deep Research** is focused, comparative, and source-level. It links packages to repositories, inspects finalists, applies hard gates, checks license/provenance, and determines the best composition.

## Research swarm

SPARI is designed for parallel low-cost discovery with stronger synthesis:

```text
Research Coordinator
├── GitHub whole-product scout
├── GitHub framework scout
├── GitHub implementation scout
├── PyPI primary-package scout
├── PyPI alternative-package scout
├── internal-reuse scout
├── security/maintenance scout
└── license/provenance scout
             ↓
      Technical Evaluator
             ↓
       Contrarian Review
```

## Reuse decisions

```text
ADOPT
ADAPT
COMPOSE
REFERENCE
REJECT
BUILD
```

`BUILD` is not the default.

## Example Reuse Blueprint

```text
BASE
GitHub Repo A

KEEP_INTERNAL
existing persistence layer

DEPENDENCY
PyPI Package B

REPLACE
Repo A module C with PyPI Package D

REFERENCE_ONLY
Repo E architecture pattern

CUSTOM
adapter F
```

## License and provenance

Every selected external artifact must resolve to:

```text
REFERENCE_ONLY
PATTERN_ONLY
DEPENDENCY_ALLOWED
CODE_REUSE_ALLOWED
REVIEW_REQUIRED
DENIED
```

Public does not mean reusable.

## Status

`v0.1.0` — experimental.

## License

Apache License 2.0.

See `THIRD_PARTY_NOTICES.md` for conceptual prior art.

---

**SPARI — research broadly, reuse intelligently, build only what is missing.**
