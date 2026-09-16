# SPARI

<p align="center">
  <strong>Build-vs-Borrow</strong><br>
 SPARI is a Build-vs-Borrow engine for AI software development.
</p>

<p align="center">
  <img alt="License" src="https://img.shields.io/badge/license-Apache--2.0-blue">
  <img alt="Status" src="https://img.shields.io/badge/status-experimental-orange">
  <img alt="Version" src="https://img.shields.io/badge/version-0.1.2-green">
  <img alt="Agent Skill" src="https://img.shields.io/badge/agent-skill-purple">
</p>

---

**Build-vs-Borrow and Software Composition Engine for AI Agents**

*A Software Intelligence and Reuse Layer for AI Agents.*

> Research broadly. Reuse intelligently. Build only what is missing.

SPARI — **Software Prior Art & Reuse Intelligence** — makes existing software the starting point of AI engineering instead of an afterthought.

Its primary focus is simple:

> **Before substantial custom code is written, determine what already exists on GitHub, PyPI, and inside the current system — then compose the strongest reusable solution and justify whatever still needs to be built.**

SPARI is not a package recommender and not a link collector. It is a closed Build-vs-Borrow decision loop.

SPARI is not a universal package-registry search engine. In v0.x, GitHub, PyPI, and the existing internal codebase are the only first-class software sources; npm, crates.io, Maven, NuGet, Go modules, Hugging Face, OCI registries, and other ecosystems are explicitly out of scope for the current build.

---

## Why SPARI exists

AI coding agents are extremely good at producing code.

They are much worse at proving that the code should exist.

A request such as:

> “Build an Excel import.”

can quickly become:

```text
custom parser
+ validation helpers
+ database wrappers
+ mapping abstractions
+ retry logic
+ more patches
```

before anyone checks whether:

- the current project already contains most of the capability;
- a mature PyPI package solves the difficult part;
- a GitHub project already implements the larger system;
- a better adjacent solution class exists;
- several existing components can be composed;
- previous agents already evaluated the same software;
- the external code can legally be reused.

That creates duplicated code, fragmented architectures, repeated research, unnecessary maintenance, and large amounts of avoidable agent work.

SPARI reverses the default:

```text
NOT:

request
→ code
→ patches
→ more code
→ rediscover existing solution later
```

```text
INSTEAD:

raw intent
→ internal software map
→ broad GitHub/PyPI recon
→ solution-space map
→ a few qualified questions
→ confirmed intent
→ Golden Plan
→ deep GitHub/PyPI research
→ source inspection
→ Build-vs-Borrow decision
→ reuse composition
→ minimal custom delta
→ implementation
→ verified outcome
→ decision memory
→ smarter next run
```

**Custom code becomes the justified remainder, not the starting assumption.**

---

# What SPARI is

SPARI combines:

```text
Software Prior Art
+ Software Discovery
+ Source Intelligence
+ Build-vs-Borrow Decisioning
+ Software Composition
+ License & Provenance
+ Decision Memory
+ Outcome Learning
```

Its external research method is **GitHub-first and PyPI-first prior-art intelligence**. 

Its engineering decision is broader:

```text
ADOPT
ADAPT
COMPOSE
REFERENCE
REJECT
BUILD
```

The goal is not to maximize reuse at any cost.

The goal is to find the strongest existing foundation and build only the part that evidence shows is genuinely missing.

---

# Internal software is prior art too

v0.1.2 closes an important gap: SPARI must understand the software you already own before searching for more software.

The first question is no longer merely:

> What exists on GitHub or PyPI?

It is:

```text
What do we already own?
        +
What can we borrow externally?
        +
What should we compose?
        +
What genuinely remains to build?
```

SPARI therefore produces an `INTERNAL_SOFTWARE_MAP` before consequential external research.

It maps the relevant parts of the current system:

```text
repositories / workspaces
packages and modules
important symbols and interfaces
dependency relationships
installed dependencies
architectural boundaries
capability-to-code mappings
internal reuse candidates
```

The durable map may be rich.

The active model context should contain only the capability-relevant slice — not a dump of the whole repository.

This is inspired by a proven idea in coding systems such as Aider: repository context becomes more useful when important code relationships are mapped and the active representation is constrained to relevant context rather than blindly loading everything.

See [`references/internal-software-map.md`](references/internal-software-map.md).

---

# Broad Recon comes before requirement freeze

The user's first wording is useful evidence of intent.

It is not necessarily the final search ontology.

If someone says:

> “I need a chair.”

searching only for chairs may miss that the real problem belongs to a broader seating or furniture solution space.

SPARI therefore expands the **research scope** before it freezes the **solution scope**:

```text
literal request
→ underlying capability
→ parent solution category
→ adjacent solution classes
→ complete systems solving the same outcome
```

Software example:

```text
"Excel import"
→ Excel parsing
→ tabular ingestion
→ validation + mapping
→ ETL / import frameworks
→ complete data-import systems
```

Another:

```text
"RAG"
→ vector retrieval
→ hybrid retrieval
→ GraphRAG
→ knowledge graphs
→ knowledge systems
→ agent memory / document intelligence
```

SPARI is allowed to discover a broader solution space.

It is **not** allowed to silently turn a discovered possibility into a confirmed user requirement.

---

# Fewer questions, better questions

SPARI does not start with a long interview.

It first learns what is possible.

Broad Recon should identify the real decision branches. Only then should SPARI ask a few high-information questions.

Bad:

> Which vector database do you want?

Better:

> The reconnaissance found that the strongest existing approaches split between retrieval-centric and graph-centric systems. Do explicit relationships between entities need to be persistent and directly queryable?

The second question is useful because evidence showed why it matters.

This is **evidence-informed clarification**, not requirements interrogation.

---

# IntakeGov + SPARI

SPARI is designed to work with [IntakeGov](https://github.com/tonnestate/IntakeGov).

IntakeGov answers:

```text
What kind of work is this?
Does it belong to an existing project?
Is there enough information to begin useful reconnaissance?
Which delivery process should own the work?
```

SPARI answers:

```text
What already exists?
Which solution families are relevant?
Which GitHub repository is the strongest base?
Which PyPI packages solve capabilities better?
What should remain from the current system?
What can be reused legally and technically?
What must actually be built?
```

The handoff intentionally happens before full technical specification:

```text
IntakeGov
   ↓
RECON_READY
   ↓
SPARI Broad Recon
   ↓
Solution-space map
   ↓
few evidence-informed questions
   ↓
Confirmed Intent
   ↓
Golden Plan
   ↓
SPARI Deep Research
```

`RECON_READY` means enough is known to search intelligently.

It does **not** mean the solution has already been decided.

SPARI can also be used standalone when the caller supplies an equivalent minimum recon-ready context.

---

# Research depth is adaptive

SPARI should be rigorous without becoming bureaucratic.

v0.1.2 defines three research depths:

## PREFLIGHT

For a small or obvious generic mechanism.

```text
existing project check
→ focused GitHub/PyPI check
→ reuse/build verdict
```

No large swarm unless uncertainty appears.

## TARGETED

For a known capability or named candidate that needs due diligence.

```text
candidate/source verification
→ focused alternatives
→ compatibility
→ maintenance
→ security
→ license/provenance
→ decision
```

## FULL

For consequential, ambiguous, cross-cutting, or project-level Build-vs-Borrow decisions.

```text
Broad Recon
→ qualified questions
→ Golden Plan
→ research swarm
→ source inspection
→ capability coverage
→ hard gates
→ evaluator
→ contrarian
→ composition
→ Custom Delta
```

Research depth can escalate when new evidence increases uncertainty or impact.

A lighter mode may never bypass required legal, security, provenance, or compatibility gates.

See [`references/research-depth.md`](references/research-depth.md).

---

# Research budget: control cost without faking certainty

SPARI is explicitly designed to use cheap parallel agents for high-recall discovery and stronger models for a smaller number of judgement-heavy decisions.

But Deep Research must not become uncontrolled token consumption.

SPARI therefore separates:

```text
QUALITY STOP
research convergence
```

from:

```text
RESOURCE STOP
research budget
```

A research profile may constrain:

```text
max_scouts
max_candidates_screened
max_candidates_deep_inspected
max_proofs_of_fit
max_strong_model_escalations

optional:
max_tokens
max_cost
```

The normal quality stop is **convergence**, not an arbitrary token number.

If the resource envelope is exhausted before sufficient evidence exists:

```text
RESEARCH_BUDGET_EXHAUSTED
→ RESEARCH_INCOMPLETE
```

Never:

```text
budget exhausted
→ nothing found
→ BUILD
```

See [`references/research-budget.md`](references/research-budget.md).

---

# GitHub and PyPI are primary software inventories

SPARI v0.x deliberately focuses on:

```text
PRIMARY SOFTWARE SOURCES

GitHub
PyPI
existing internal codebase
```

GitHub provides:

- complete products;
- frameworks;
- reference architectures;
- implementation patterns;
- source code;
- tests;
- releases;
- issues and maintenance evidence.

PyPI provides:

- packages;
- versions;
- Python compatibility;
- distribution artifacts;
- hashes;
- dependencies;
- project/source links;
- package metadata.

SPARI does not treat these sources as independent worlds.

For a serious package candidate, it should construct the strongest available chain:

```text
PyPI package
→ exact version
→ distribution artifact
→ hash
→ claimed source repository
→ verified source repository where possible
→ release/tag/commit
→ source inspection
→ license/provenance
```

---

# Source model: focused today, extensible tomorrow

GitHub and PyPI remain SPARI's primary external sources.

v0.1.2 does **not** expand the research scope to every package ecosystem.

Instead, the data model becomes ecosystem-neutral so future adapters can be added without rewriting the decision engine.

Possible future adapters include:

```text
npm
crates.io
Go modules
Maven Central
NuGet
Hugging Face
OCI registries
```

These are future extension points, not v0.1.2 research requirements.

See [`references/source-model.md`](references/source-model.md).

---

# Claimed source is not verified source

A registry link to a repository is useful evidence.

It is not automatically verified provenance.

SPARI distinguishes:

```text
CLAIMED_SOURCE
VERIFIED_SOURCE
```

Likewise:

```text
PROVENANCE_VERIFIED
```

does not imply:

```text
TRUSTED_SOFTWARE
```

Provenance can establish where an artifact came from.

It cannot prove that the artifact is secure, maintained, suitable, or safe.

That requires separate evaluation.

---

# Broad Recon vs Deep Research

Broad Recon asks:

> **What kinds of existing solutions should we know about before we narrow the problem?**

It is:

```text
cheap
broad
parallel
high-recall
semantically wider than the literal request
```

Deep Research asks:

> **Which concrete existing software should actually form the solution?**

It is:

```text
focused
comparative
source-level
evidence-heavy
```

The distinction prevents two common failures:

```text
too narrow too early
```

and:

```text
expensive deep research against the wrong interpretation
```

---

# The Golden Plan

Broad Recon happens before the final technical solution is frozen.

After the solution space is understood and the few material questions are resolved, SPARI works against a Golden Plan.

It contains:

```text
GOAL
CONFIRMED_INTENT
NON_GOALS
IN_SCOPE
OUT_OF_SCOPE
REQUIRED_CAPABILITIES
CONSTRAINTS
EXISTING_SYSTEM_CONTEXT
TECHNICAL_ENVIRONMENT
SUCCESS_CRITERIA
KNOWN_FACTS
UNKNOWNS
ALLOWED_SCOPE_REFINEMENT
```

Deep Research may improve the technical shape.

It may not silently replace the confirmed intent because an easier implementation exists.

---

# Parallel research, independent judgement

SPARI is designed for **cheap breadth and strong synthesis**.

A FULL research run may use:

```text
Research Coordinator
│
├── GitHub Whole-Product Scout
├── GitHub Framework Scout
├── GitHub Implementation Scout
├── PyPI Primary Package Scout
├── PyPI Alternative Package Scout
├── Internal Reuse Scout
├── Security / Maintenance Scout
└── License / Provenance Scout
             ↓
      Technical Evaluator
             ↓
      Contrarian Reviewer
             ↓
      Composition Decision
```

Scouts collect evidence.

They do not individually choose the final architecture.

This concentrates expensive judgement where it matters most.

---

# Source beats README

README claims, stars, download counts, rankings, and marketing pages are useful discovery signals.

They are not proof.

A serious finalist should be inspected at the source level where access permits:

```text
source tree
architecture
relevant modules
APIs
extension points
tests
release history
maintenance
dependency footprint
integration complexity
issue quality
security posture
license scope
provenance
```

---

# Capability Coverage

SPARI evaluates candidates against the Golden Plan's required capabilities.

Example:

```text
                         Repo A   Repo B   PyPI X   PyPI Y
----------------------------------------------------------
ingestion                  yes      yes      yes
OCR                         no      yes               yes
retrieval                  yes      partial
graph relationships        partial  yes
API                        yes      yes
```

The purpose is not to crown one universal winner.

It is to identify:

- the strongest overall base;
- the strongest component libraries;
- internal components worth keeping;
- useful reference implementations;
- capabilities that genuinely remain custom.

---

# Build-vs-Borrow is a composition decision

SPARI's output should not be:

> Here are five interesting repositories.

A useful output looks more like:

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

This is why SPARI is more than a prior-art search skill.

It is a **software composition decision engine**.

---

# Reuse decisions

Every serious candidate receives a solution decision:

```text
ADOPT
ADAPT
COMPOSE
REFERENCE
REJECT
BUILD
```

`BUILD` is not the default.

It means:

> Existing internal software, GitHub repositories, PyPI packages, and viable compositions were investigated, and evidence still shows that this remaining capability is best implemented as custom code.

---

# The Custom Delta

SPARI explicitly identifies:

```text
CUSTOM_DELTA
```

Everything outside that delta should already be covered by:

```text
existing internal code
GitHub base
PyPI dependency
reused source component
API integration
reference pattern
```

A large Custom Delta is acceptable when justified.

The goal is not maximal reuse.

The goal is to prevent accidental reinvention.

---

# Hard gates before preferences

A popular project can still be the wrong project.

SPARI applies mandatory constraints before qualitative comparison.

Examples:

```text
runtime compatibility
Python version
deployment constraints
architecture constraints
security
license
provenance
```

A candidate that fails a hard gate does not win because it has more stars or downloads.

---

# License and provenance

Public code is not automatically reusable code.

SPARI separates three layers of license evidence:

```text
DECLARED_LICENSE
what metadata/upstream declares

DETECTED_LICENSE
what inspection identifies in relevant artifacts

EFFECTIVE_REUSE_DECISION
what the intended use is actually allowed to do
```

Before an external artifact enters a reusable deliverable, it must resolve to:

```text
REFERENCE_ONLY
PATTERN_ONLY
DEPENDENCY_ALLOWED
CODE_REUSE_ALLOWED
REVIEW_REQUIRED
DENIED
```

Unknown, conflicting, or scope-unclear licensing fails closed.

See [`references/license-provenance.md`](references/license-provenance.md).

---

# Research convergence

Deep Research does not stop because a fixed number of repositories were found.

It converges when:

- major solution families are stable;
- repeated searches mostly return known candidates;
- new candidates no longer materially change the shortlist or composition;
- finalists have sufficient source evidence;
- unresolved uncertainty is explicit.

If a required source is unavailable:

```text
RESEARCH_INCOMPLETE
```

not:

```text
no solution exists
```

---

# SPARI decides. Coding agents execute.

SPARI is deliberately not another coding agent.

Execution systems such as Aider, Claude Code, Codex, and other engineering agents are good at changing code.

SPARI answers a different question first:

> **Which code should exist at all?**

The boundary is explicit:

```text
SPARI
Build-vs-Borrow decision
        ↓
Reuse Blueprint
        ↓
Custom Delta
        ↓
EXECUTION_CONTRACT
        ↓
Aider / Claude Code / Codex / other executor
        ↓
EXECUTION_OUTCOME
        ↓
SPARI verification + Decision Memory
```

This prevents the execution layer from silently replacing a reuse decision with more custom code simply because generating code is easier.

The contract is executor-agnostic.

It records what must be reused, what may change, what custom work is allowed, what must be verified, and what evidence has to come back.

The result is also structured: repository revisions, actual dependencies, files changed, verification results, abandoned components, integration failures, actual Custom Delta, and contract deviations.

A green test suite is useful evidence.

It is **not** sufficient evidence that the Build-vs-Borrow decision was respected.

See [`references/execution-boundary.md`](references/execution-boundary.md).

---

# The closed loop

SPARI is not finished when it recommends software.

The full loop is:

```text
DISCOVER
→ EVALUATE
→ COMPOSE
→ HAND OFF
→ IMPLEMENT
→ VERIFY OUTCOME
→ RECORD RESULT
→ UPDATE DECISION MEMORY
→ REVALIDATE WHEN REQUIRED
→ DISCOVER SMARTER NEXT TIME
```

Without outcome feedback, research remains theoretical.

A package may look ideal and fail during integration.

A repository may expose hidden architectural limitations.

A less obvious candidate may outperform the research favorite in the real environment.

SPARI must remember that.

---

# Research decision ≠ implementation outcome

These are different facts:

```text
research_decision:
ADOPT

implementation_outcome:
REJECTED_AFTER_IMPLEMENTATION
```

Future agents must see both.

Otherwise the same bad recommendation can be rediscovered forever.

---

# Decision Memory without context rot

SPARI stores rich evidence, but future agents should not receive the entire history on every run.

Decision Memory is retrieved by relevance:

```text
current capability
+ project/runtime constraints
+ ecosystem
+ candidate family
+ freshness/revalidation status
```

The durable store can contain full evidence references.

The active context should contain only the records that materially bind the current decision.

This preserves institutional learning without turning memory into a new source of context noise.

---

# Revalidation

Previous decisions can be reopened when evidence changes:

```text
major release
security advisory
license change
provenance change
maintenance decline
breaking dependency change
runtime change
integration failure
materially stronger alternative
```

Revalidation returns to the same Build-vs-Borrow loop.

---

# Failure remains visible

SPARI fails explicitly instead of manufacturing confidence.

Examples:

```text
NOT_RECON_READY
GITHUB_UNAVAILABLE
PYPI_UNAVAILABLE
RESEARCH_INCOMPLETE
RESEARCH_BUDGET_EXHAUSTED
SOURCE_LINK_UNVERIFIED
NO_LICENSE
LICENSE_SCOPE_UNCLEAR
PROVENANCE_UNRESOLVED
SECURITY_GATE_FAILED
RUNTIME_INCOMPATIBLE
NO_VIABLE_BASE
NO_VIABLE_COMPONENT
EVIDENCE_INSUFFICIENT
SOURCE_INSPECTION_INCOMPLETE
CUSTOM_DELTA_UNJUSTIFIED
OUTCOME_NOT_VERIFIED
```

Missing evidence is not negative evidence.

---

# What SPARI is not

SPARI is not:

- a generic web-search skill;
- a GitHub link collector;
- a PyPI recommendation list;
- a long requirements interview;
- a project-management replacement;
- a code generator;
- a numeric popularity ranking;
- a mandate to always add dependencies;
- a mandate to always avoid custom code.

SPARI is the intelligence layer between:

```text
"What might we need?"
```

and:

```text
"Start writing substantial custom code."
```

---

# Repository structure

```text
SPARI/
├── SKILL.md
├── README.md
├── LICENSE
├── NOTICE
├── THIRD_PARTY_NOTICES.md
├── CHANGELOG.md
│
├── references/
│   ├── broad-recon.md
│   ├── closed-loop.md
│   ├── deep-research.md
│   ├── evaluation-composition.md
│   ├── failure-codes.md
│   ├── golden-plan.md
│   ├── intakegov-handoff.md
│   ├── internal-software-map.md
│   ├── execution-boundary.md
│   ├── license-provenance.md
│   ├── memory-schema.md
│   ├── research-budget.md
│   ├── research-depth.md
│   ├── research-swarm.md
│   └── source-model.md
│
├── schemas/
│   ├── decision-memory.schema.json
│   ├── execution-contract.schema.json
│   ├── execution-outcome.schema.json
│   ├── golden-plan.schema.json
│   ├── internal-software-map.schema.json
│   ├── research-profile.schema.json
│   └── source-artifact.schema.json
│
└── tests/
    └── adversarial-cases.md
```

---

# Behavioral testing

SPARI is tested against the failure modes it exists to prevent:

- literal-search tunnel vision;
- package-only blindness;
- repo-only blindness;
- README hallucination;
- popularity bias;
- search outages treated as absence;
- missing-license reuse;
- incorrect package-to-repository linking;
- unnecessary full research for trivial work;
- insufficient research for consequential work;
- budget exhaustion converted into fake certainty;
- repeated research despite validated memory;
- failed implementation outcomes forgotten by later agents;
- ecosystem expansion that accidentally changes SPARI's v0.x scope.

See [`tests/adversarial-cases.md`](tests/adversarial-cases.md).

---

# Design principles

```text
Explore before you narrow.

Research before you rebuild.

Search broader than the literal wording.

Ask only questions that evidence makes useful.

Use cheap breadth and strong judgement.

Inspect source, not just descriptions.

Treat claimed source and verified source differently.

Use hard constraints before popularity.

Compose before creating.

Treat custom code as the justified remainder.

Control research cost without turning budget limits into fake certainty.

Verify licensing before reuse.

Remember outcomes, including failures.

Retrieve only the memory relevant to the current decision.

Never turn missing evidence into certainty.
```

---

# References and conceptual prior art

SPARI is independently written.

Its design was informed by public work in software reuse, agent workflows, software selection, cost governance, source intelligence, and project governance.

The following projects are conceptual references, not bundled dependencies.

## IntakeGov

https://github.com/tonnestate/IntakeGov

**License:** Apache-2.0

Relevant concepts:

- project/product intake;
- recon readiness;
- work classification;
- routing;
- reuse governance.

## evaluate-existing-solutions

https://github.com/citypaul/.dotfiles

**Repository license:** MIT, subject to any more specific nested license or notice applying to individual paths.

Relevant concepts:

- proportionate evaluation depth;
- hard gates before trade-offs;
- total lifecycle ownership;
- proof-of-fit;
- explicit bespoke baseline.

## search-first

https://github.com/shimo4228/search-first

**License:** MIT

Relevant concepts:

- research-before-coding discipline;
- quick vs full research modes;
- repo/registry/tool search order;
- explicit Adopt / Extend / Compose / Build verdicts.

## reduce-reinvention

https://github.com/JUNERDD/skills

**License:** MIT

Relevant concepts:

- institutional software reuse;
- reuse catalogs;
- lifecycle and ownership.

## repo-to-skill

https://github.com/zhangguiping-xydt/repo-to-skill

**License:** Apache-2.0

Relevant concepts:

- source-level capability extraction;
- provenance-preserving reuse artifacts.

## skill-mining

https://github.com/voodootikigod/skill-mining

**License:** MIT

Relevant concepts:

- reusable knowledge extraction;
- gap discovery;
- persistent organizational learning.

## project-state-governor

https://github.com/Ghost011118/project-state-governor

**License:** Apache-2.0

Relevant concepts:

- durable project truth;
- evidence states;
- resistance to conversational drift.

## Microsoft Agent Governance Toolkit

https://github.com/microsoft/agent-governance-toolkit

**License:** MIT

Relevant concepts:

- agent resource/cost governance;
- budget enforcement;
- separating resource control from agent autonomy.

## BMAD Method

https://github.com/bmad-code-org/BMAD-METHOD

**License:** MIT

Relevant concepts:

- adaptive planning depth;
- structured project delivery.

## Superpowers

https://github.com/obra/superpowers

**License:** MIT

Relevant concepts:

- disciplined engineering;
- behavioral skill testing.

## GitHub Spec Kit

https://github.com/github/spec-kit

**License:** MIT

Relevant concepts:

- specification-driven development;
- clarification and planning.

## GitHub awesome-copilot

https://github.com/github/awesome-copilot

**License:** MIT

Relevant concepts:

- codebase knowledge;
- architecture and quality workflows.

## Product on Purpose PM Skills

https://github.com/product-on-purpose/pm-skills

**License:** Apache-2.0

Relevant concepts:

- product discovery;
- problem framing;
- build-risk analysis.

## tomzx/agents

https://github.com/tomzx/agents

Used as **conceptual research only** in SPARI v0.1.2 unless a concrete applicable license is separately verified for a specific reuse.

Relevant concepts:

- existing-solution review;
- SDLC traceability;
- independent verification.

---

## Aider

https://github.com/Aider-AI/aider

**License:** Apache-2.0

Relevant concepts:

- repository-wide code mapping;
- selecting relevant repository context within a token budget;
- using code relationships to preserve existing abstractions;
- separating architectural reasoning from file editing;
- Git-native execution evidence.

Aider is not a SPARI dependency and solves a different problem. It is useful prior art for SPARI's internal software mapping and executor boundary.

# External software-intelligence infrastructure

SPARI is designed to use structured software sources before resorting to generic scraping.

Relevant infrastructure includes:

- GitHub / GitHub MCP Server
- PyPI APIs and attestations
- deps.dev / Open Source Insights
- OSV
- OpenSSF Scorecard
- Chroma Package Search
- OSS Review Toolkit

These are infrastructure candidates, not mandatory bundled dependencies.

---

# Status

```text
v0.1.2
Experimental
```

v0.1.2 makes internal software first-class prior art and formalizes the boundary between Build-vs-Borrow intelligence and code execution through `INTERNAL_SOFTWARE_MAP`, `EXECUTION_CONTRACT`, and `EXECUTION_OUTCOME`.

---

# License

Apache License 2.0.

See [`LICENSE`](LICENSE), [`NOTICE`](NOTICE), and [`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md).

---

# Existing software first. Custom code only where evidence earns it.

**SPARI — Build vs Borrow, then compose.**
