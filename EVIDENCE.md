# SPARI v0.1.2 — Evaluation & Evidence Report

**Version under review:** SPARI v0.1.2  
**Status:** Experimental  
**Evidence cut-off:** 2026-09-17  
**Purpose:** Preserve the current evidence about SPARI v0.1.2 before further architectural changes.

> This document separates **controlled evidence**, **historical combined-system evidence**, **operator observations**, and **research-backed hypotheses**.  
> It does not treat qualitative observations as causal proof.

---

## 1. Executive summary

SPARI v0.1.2 is a Build-vs-Borrow and software-composition skill for AI engineering agents. Its defining mechanisms are:

- an `INTERNAL_SOFTWARE_MAP` before consequential external research;
- semantic solution-space expansion;
- GitHub/PyPI prior-art research;
- source-level candidate inspection and hard gates;
- `ADOPT / ADAPT / COMPOSE / REFERENCE / REJECT / BUILD` decisions;
- a `REUSE_BLUEPRINT` and explicit `CUSTOM_DELTA`;
- an executor-agnostic `EXECUTION_CONTRACT`;
- structured `EXECUTION_OUTCOME`;
- Decision Memory and revalidation;
- explicit recomposition after implementation evidence invalidates the current path.

The controlled evaluation program did **not** demonstrate a material incremental engineering outcome for v0.1.2 over a strong **Luna + IntakeGov** baseline.

That result is important, but it is not equivalent to “SPARI has no value”.

The evidence currently supports four narrower conclusions:

1. **SPARI reliably structures prior-art archaeology and Build-vs-Borrow reasoning.**
2. **A strong Luna + IntakeGov baseline already performs much of the same repository discovery and local repair work.**
3. **FULL-SPARI can become materially more expensive when it repeats research that the baseline has effectively already resolved.**
4. **The strongest observed live behavior — minimal, architecture-preserving changes after repeated reconsideration of the solution — is associated with Recomposition, but this effect has not yet been isolated causally in a controlled evaluation.**

The current product status is therefore:

> **SPARI_EXPERIMENTAL**

The strongest open hypothesis after v0.1.2 is not that SPARI should perform more front-loaded research. It is that SPARI may be most valuable as an **evidence-driven recomposition and prior-art control layer** that prevents an engineering agent from remaining trapped in its first plausible solution.

That hypothesis remains **unproven**.

---

## 2. What changed in v0.1.2

SPARI v0.1.2 was the **internal-prior-art and execution-boundary release**.

Compared with the initial v0.1.0/v0.1.1 design, v0.1.2 added or formalized:

- `INTERNAL_SOFTWARE_MAP` as a first-class artifact;
- capability-to-code mapping;
- dependency and installed-dependency mapping;
- architecture-boundary mapping;
- internal reuse candidates;
- relevance-constrained active context rather than repository dumps;
- separation between SPARI decisioning and coding execution;
- executor-agnostic `EXECUTION_CONTRACT`;
- structured `EXECUTION_OUTCOME`;
- base/result revision linkage;
- planned-vs-actual reuse tracking;
- planned-vs-actual Custom Delta tracking;
- contract deviation reporting;
- unexpected custom-code reporting;
- explicit recognition that passing tests alone do not prove Build-vs-Borrow adherence;
- failure handling for internal-reuse blindness and executor scope drift.

v0.1.1 had already introduced:

- `PREFLIGHT`, `TARGETED`, and `FULL` research depths;
- convergence-based `QUALITY_STOP`;
- separate resource-budget stopping;
- fail-closed `RESEARCH_INCOMPLETE`;
- source/provenance distinctions;
- declared/detected/effective license decisions;
- Decision Memory retrieval discipline.

The v0.1.2 closed-loop model is approximately:

```text
Raw intent
→ Internal Software Map
→ Broad Recon
→ Solution-space map
→ Evidence-informed clarification
→ Golden Plan
→ Deep Research
→ Source inspection
→ Build-vs-Borrow composition
→ Minimal justified Custom Delta
→ Execution Contract
→ Execution
→ Execution Outcome
→ Decision Memory
→ Revalidation / Recomposition
```

---

## 3. Evidence classes used in this report

This report uses four evidence classes.

### 3.1 Controlled evidence

A result is treated as controlled evidence only where:

- baselines were separated;
- repository/task state was controlled;
- common acceptance was comparable;
- SPARI-specific behavior was traceable;
- results were not reconstructed from memory alone.

### 3.2 Historical combined-system evidence

These are real engineering runs using combinations such as:

```text
Luna + IntakeGov + SPARI
```

They demonstrate what the combined stack could do, but do not isolate SPARI as the cause.

### 3.3 Operator observations

These are repeated practical observations from live use. They are useful for forming hypotheses, but are not treated as benchmark proof.

### 3.4 External research alignment

Published work is used only to determine whether observed SPARI mechanisms correspond to known software-engineering problems. It does not convert an unproven SPARI claim into a proven one.

---

# 4. Evidence timeline

## 4.1 Historical AVCOS long-running rework

A substantial AVCOS rework was completed with:

- Luna;
- IntakeGov;
- SPARI;
- existing AVCOS architecture;
- tests and evidence gates.

The combined stack showed several positive engineering behaviors:

- existing architecture was largely preserved instead of replaced;
- pre-existing gaps were identified and repaired;
- existing authorities were reused and extended;
- 818 tests passed on the final audited state;
- publication-specific tests passed;
- technical/internal success remained separated from external/economic success;
- external economic closure remained blocked rather than fabricated.

This run was important because it showed useful **combined-system behavior**.

It did **not** prove SPARI’s individual contribution.

The missing evidence was causal telemetry linking:

```text
SPARI discovery
→ changed engineering decision
→ changed implementation
→ improved engineering consequence
```

Therefore the historical verdict remains:

> **SPARI incremental value: INSUFFICIENT EVIDENCE**

This is an attribution limitation, not proof that SPARI lacked value.

---

## 4.2 SPARI-EVAL-PROD-001

**Task:** `AVCOS-CEO-SURFACE-METADATA-001`

The task extended the existing authenticated CEO-surface read model with:

- source/retrieval metadata;
- freshness;
- confidence;
- typed unavailable/error states.

### Outcome

All three arms produced a focused-tested solution using the existing architecture.

Focused tests:

- ARM A — Luna: **11 passed**
- ARM B — Luna + IntakeGov: **9 passed**
- ARM C — Luna + IntakeGov + SPARI: **10 passed**

These counts were from different focused suites and must **not** be interpreted as a quality ranking.

All arms reused the existing:

- route;
- authentication;
- economic truth path;
- execution receipts;
- bounded projection;
- legacy response semantics.

No new subsystem, database, ledger, route, or external dependency was required.

### SPARI-specific behavior

ARM C explicitly produced:

- an Internal Software Map;
- broader solution-space exploration;
- candidate/hard-gate decisions;
- reference-only treatment of OpenTelemetry;
- rejection of Pydantic, Marshmallow, and heavier alternatives;
- an `EXTEND_INTERNAL` decision;
- a targeted `QUALITY_STOP`;
- an explicit Custom Delta.

### Result

This proved **process contribution**, but not unique engineering outcome.

ARM B independently converged on the same internal-reuse strategy.

The strongest defensible verdict was:

> **LIMITED PROCESS VALUE PROVEN; strong incremental causation not proven.**

### Measurement limitation

Per-arm token/runtime telemetry was incomplete.

The run therefore could not quantify the cost of SPARI relative to B.

This evaluation established an important methodological lesson:

> causal instrumentation must exist before an expensive run starts.

---

# 5. Evaluation Case 002 — Matching & Cooperation negative control

A later controlled three-arm case used a bounded TonnEstate Matching & Cooperation slice.

Common acceptance:

- ARM A: **3/3 passed**
- ARM B: **3/3 passed**
- ARM C: **3/3 passed**

### Compute

| Metric | ARM A Luna | ARM B Luna + IntakeGov | ARM C + SPARI |
|---|---:|---:|---:|
| Input tokens | 968,487 | 453,350 | 1,168,442 |
| Cached input | 900,608 | 405,504 | 1,075,712 |
| Output tokens | 6,959 | 4,469 | 9,212 |
| Reasoning tokens | 1,863 | 1,236 | 1,989 |
| Total measured tokens | 977,309 | 459,055 | 1,179,643 |
| Wall time | 203,542 ms | 126,529 ms | 277,628 ms |

ARM C versus B:

- **+720,588 measured tokens**
- **+157% token volume**
- **+151,099 ms**
- **+119% wall time**
- six external research queries;
- no external component adopted.

### Engineering result

ARM B identified the existing mature internal seam and made no production change.

ARM C:

- mapped the same internal seam;
- researched external alternatives;
- rejected those alternatives;
- retained the internal architecture;
- added a structured `selection_explanation`.

The common outcome did not improve.

There was no demonstrated:

- completion uplift;
- external reuse uplift;
- Custom Delta reduction;
- maintenance reduction;
- repair uplift.

### Result

The observed C-only value was explainability/provenance.

This was not enough to economically justify FULL-SPARI for this task.

Verdict:

> **MARGINAL_COMPUTE for an obvious internally mature task.**

This case provides direct evidence that FULL-SPARI should not automatically run merely because SPARI is available.

---

# 6. SPARI-PROOF-001 — hidden internal recovery case

A later proof case attempted to guarantee that a materially useful hidden internal solution existed.

The hidden opportunity was an existing recovery composition involving:

- tenant/job/file/hash identity;
- evidence-bound marker handling;
- canonical outbox confirmation;
- locks;
- quarantine;
- cleanup restrictions;
- idempotent replay/reporting.

Independent ground-truth tests passed.

However, both ARM A and ARM B independently found the hidden solution during preplanning.

The required early stop correctly fired:

> `CASE_NOT_DISCRIMINATIVE`

ARM C was not run.

### Preplan cost

Even though the case stopped correctly, qualification itself was expensive:

| Preplan | Input tokens | Cached input |
|---|---:|---:|
| ARM A | 706,248 | 611,840 |
| ARM B | 803,673 | 711,168 |
| Total | **1,509,921** | **1,323,008** |

This case proved two things:

1. the hidden opportunity was not difficult enough for the strong baseline;
2. case qualification itself can become expensive if it requires full repository-scale preplans.

It produced **no SPARI incremental-value result**.

---

# 7. Fixed SPARI 1.0 evidence program executed against v0.1.2

The final controlled program tested four predefined capability classes.

Product status after the program:

> **SPARI_EXPERIMENTAL**

## 7.1 Class A — Hidden internal reuse

Result:

> `CASE_NOT_DISCRIMINATIVE`

ARM A and ARM B independently found the hidden internal reconciliation/recovery composition.

ARM C correctly did not run.

No SPARI conclusion can be claimed from this class.

---

## 7.2 Class B — Repair / recomposition

This was the most important qualified positive class.

The task involved a real bounded ALKIS repair with:

- multiple plausible repair paths;
- known ground truth;
- objective common acceptance;
- real internal architecture;
- no prescribed implementation.

### Common acceptance

- ARM A: **4/4**
- ARM B: **4/4**
- ARM C: **4/4**

All arms retained the existing ALKIS request/import/persistence/checkpoint architecture.

ARM B and C both implemented materially equivalent:

- bounded streaming;
- numeric cardinality handling;
- local feature counting;
- BBOX count handling;
- wrapper handling;
- native CRS/identity preservation.

No external artifact was adopted.

### Tokens

| Metric | ARM A | ARM B | ARM C |
|---|---:|---:|---:|
| Input | 1,408,776 | 1,098,826 | 1,139,011 |
| Cached input | 1,321,216 | 1,008,128 | 1,059,584 |
| Output | 9,422 | 11,425 | 10,825 |
| Reasoning | 3,142 | 4,156 | 3,235 |
| Measured model tokens | 1,421,340 | 1,114,407 | 1,153,071 |

ARM C − ARM B:

> **+38,664 measured model tokens**

Wall time, phase tokens, and tool/research counters were not preserved by an external harness.

### SPARI-specific behavior

ARM C produced richer research around:

- OGC `numberMatched`;
- provider-side `count`;
- cardinality safeguards;
- provenance.

However, ARM B independently implemented the same material safeguards.

The causal chain failed at the important points:

```text
known opportunity             PROVEN
B missed it                   NOT PROVEN
SPARI discovered/used it      PARTIALLY SUPPORTED
decision changed              NOT PROVEN
implementation changed        NOT PROVEN
outcome improved              NOT PROVEN
```

Verdict:

> **NO_INCREMENTAL_VALUE for this qualified repair case.**

This is currently the strongest controlled negative result against the hypothesis that v0.1.2 automatically improves repair outcomes over Luna + IntakeGov.

---

## 7.3 Class C — External prior art / composition

Result:

> `CASE_REJECTED / NOT QUALIFIED`

The program required an independently verified external candidate that was:

- materially compatible;
- genuinely useful;
- capable of reducing Custom Delta, risk, maintenance, or completion burden.

No such real candidate was established without inventing a benchmark case.

The class was therefore correctly not run.

No conclusion about SPARI’s external prior-art capability may be drawn from Class C.

---

## 7.4 Class D — Negative control

Class D reused the measured Matching & Cooperation case.

Result:

> `NO_INCREMENTAL_VALUE / MARGINAL_COMPUTE`

It confirmed that an internally mature, bounded task can cause SPARI to spend substantial additional compute while producing little or no incremental engineering value.

---

# 8. Consolidated controlled findings

| Question | v0.1.2 evidence |
|---|---|
| Does SPARI preserve existing architecture? | **Supported** in the tested cases. |
| Does SPARI explicitly map internal prior art? | **Yes.** |
| Does SPARI produce auditable Build-vs-Borrow/rejection reasoning? | **Yes.** |
| Does SPARI reliably prevent duplicate architecture in controlled tests? | No False Build was observed, but unique causal prevention over B is **not proven**. |
| Does SPARI reduce Custom Delta versus Luna + IntakeGov? | **Not proven.** |
| Does SPARI improve common acceptance versus Luna + IntakeGov? | **Not proven.** |
| Does SPARI improve repair success versus Luna + IntakeGov? | **Not proven** in the qualified repair case. |
| Does SPARI find valuable external packages/repositories missed by B? | **Not proven**; no qualified positive external-reuse case was completed. |
| Can FULL-SPARI consume substantially more compute without outcome gain? | **Yes**, demonstrated in Case 002. |
| Is the cost multiplier always large? | **No.** Class B showed only +38,664 measured model tokens versus B. |
| Is Internal Map useful as a process mechanism? | **Supported**, but causal engineering uplift remains unproven. |
| Is Recomposition a proven incremental v0.1.2 capability? | **No.** |
| Is Recomposition the strongest live candidate mechanism? | **Operator observation / open hypothesis.** |

---

# 9. Research-yield findings

The controlled program produced the following approximate yield picture.

## Internal Software Map / Internal Recon

Observed value:

- locating existing authorities;
- identifying callers;
- preserving persistence and checkpoint paths;
- constraining architecture drift.

Controlled verdict:

> **Process value supported; unique engineering uplift not isolated.**

## Broad Recon

Observed value:

- stabilized candidate families;
- provided vocabulary and alternatives.

Observed problem:

- can become expensive when the local path is already clear.

Controlled verdict:

> **Conditional value; should not be interpreted as inherently beneficial merely because more candidates were inspected.**

## GitHub / PyPI research

In the controlled positive repair case:

> **ZERO adopted external-artifact yield.**

In the negative control:

- six external queries;
- no adopted dependency;
- no better acceptance.

This does not establish that GitHub/PyPI research is generally useless.

It establishes that v0.1.2 did not yet demonstrate incremental value from those searches in the tested tasks.

## Candidate screening / source inspection

Observed value:

- rejected unsuitable or overly heavy alternatives;
- preserved current architecture;
- provided provenance and compatibility evidence.

Controlled verdict:

> **Useful decision discipline; no isolated outcome uplift.**

## Recomposition

Controlled Class B:

> no C-only recovery or engineering uplift was isolated.

Therefore a controlled claim that Recomposition improves outcomes is not currently justified.

However, this conflicts with repeated live operator observations discussed below and remains an important unresolved hypothesis.

---

# 10. Operator observations from live use

The following observations were reported repeatedly during live SPARI use, especially in longer-running engineering tasks.

They are intentionally separated from controlled evidence.

### 10.1 Perceived capability amplification

The operator repeatedly reported that Luna with IntakeGov + SPARI appeared substantially more capable and coherent than Luna alone, at the cost of materially more tokens in some long runs.

A subjective estimate of “3–10× smarter” was used in discussion.

This is **not a benchmark metric**.

### 10.2 Internal Software Map

The Internal Software Map was repeatedly perceived as one of the strongest mechanisms because it encouraged the agent to understand and preserve existing software before introducing new code.

### 10.3 Long-running work

Long runs appeared qualitatively better than short isolated tasks:

- fewer premature rewrites;
- repeated rediscovery of relevant internal architecture;
- continued progress after intermediate failures;
- more reuse of existing code paths.

This behavior has not been causally isolated.

### 10.4 Minimal-invasive changes

The operator specifically observed cases where SPARI-guided execution made unusually small, architecture-preserving interventions while maintaining a coherent model of the existing system.

This observation is important because it is not fully captured by:

- pass/fail acceptance;
- dependency adoption count;
- Custom Delta alone.

No controlled metric for **intervention size / edit fidelity** was included in the v0.1.2 program.

### 10.5 Recomposition

The strongest live hypothesis is:

> **Recomposition may be SPARI’s most valuable behavior.**

The observed pattern was not simply “research more before coding”.

It looked more like:

```text
current hypothesis
→ implementation / inspection
→ contradictory evidence or failure
→ reopen solution
→ preserve valid parts
→ find additional internal/external ingredients
→ compose a smaller or better path
→ continue
```

This behavior remains **unproven as an incremental v0.1.2 effect**, but it is the most important discrepancy between live experience and the controlled evaluations.

---

# 11. Why the live observations and controlled results can both be true

The controlled evaluations mainly measured whether SPARI changed:

- the selected architecture;
- reuse decisions;
- Custom Delta;
- acceptance;
- maintenance ownership;
- repair success.

Most selected tasks were bounded and were solved effectively by Luna + IntakeGov.

That makes a strong baseline.

A capable model can already:

- inspect a repository;
- discover nearby internal code;
- search GitHub/PyPI;
- write a local repair;
- run tests.

SPARI v0.1.2 can therefore duplicate work when its full workflow is activated after the baseline already has a sufficient solution.

The live effect may arise from a different failure mode:

> **trajectory lock-in rather than one-shot solution quality.**

A model may be able to find a good solution initially, yet still be less reliable at:

- abandoning a plausible but failing path;
- preserving valid parts of the current plan;
- reopening only the relevant part of the solution space;
- retrieving repair ingredients;
- recomposing a minimally invasive solution.

The v0.1.2 evaluations did not isolate this behavior strongly enough to prove or disprove the hypothesis.

---

# 12. External research that aligns with the unresolved hypothesis

The following research does not prove SPARI itself, but it shows that several mechanisms behind the live observations correspond to real software-engineering problems.

## RepairAgent

Bouzenia, Devanbu, and Pradel introduced an autonomous LLM repair agent that **freely interleaves**:

- gathering bug information;
- gathering repair ingredients;
- generating fixes;
- validation;
- feedback from previous attempts.

RepairAgent repaired 164 Defects4J bugs, including 39 not repaired by prior techniques.

Reference:

- https://arxiv.org/abs/2403.17134
- https://doi.org/10.1109/ICSE55347.2025.00157

Relevance to SPARI:

> repair intelligence can benefit from interleaving evidence gathering and repair rather than treating research as a one-time front gate.

## SWE-Search

SWE-Search applies search/backtracking over software-agent trajectories and reported a **23% relative improvement across five models** compared with standard agents without MCTS.

Reference:

- https://arxiv.org/abs/2410.20285

Relevance to SPARI:

> linear coding trajectories can be a failure mode; alternative-path exploration and iterative reevaluation can improve outcomes.

## CodePlan

CodePlan models repository-level coding as adaptive planning over:

- repository dependencies;
- previous edits;
- change-impact analysis;
- task context.

Its reported evaluation found 5/6 repositories passing validity checks, while comparable baselines without the planning mechanism passed none.

Reference:

- https://arxiv.org/abs/2309.12499
- https://doi.org/10.1145/3643757

Relevance to SPARI:

> repository-level engineering benefits from plans that adapt as the repository state changes.

## RepoGraph

RepoGraph provides a repository-level structural graph as a plug-in for AI software-engineering systems and reported improvements across multiple evaluated methods.

Reference:

- https://arxiv.org/abs/2410.14684
- https://openreview.net/forum?id=dw9VUsSHGB

Relevance to SPARI:

> the Internal Software Map direction is consistent with independent evidence that persistent structural repository context can improve AI software engineering.

## Plastic Surgery Hypothesis / FitRepair

The Plastic Surgery Hypothesis argues that repair ingredients often already exist within the target software.

FitRepair revisited that idea for LLM-based automated repair and reported improvements over its evaluated baselines.

References:

- https://doi.org/10.1145/2635868.2635898
- https://arxiv.org/abs/2303.10494

Relevance to SPARI:

> internal prior art is a valid first-class repair resource, not merely an implementation convenience.

## Agentless

Agentless demonstrated that a relatively simple localization → repair → validation pipeline can be highly competitive and inexpensive on SWE-bench Lite.

Reference:

- https://arxiv.org/abs/2407.01489
- https://doi.org/10.1145/3715754

Relevance to SPARI:

> more agent machinery does not automatically produce more value. SPARI must demonstrate a distinct capability rather than merely adding process.

---

# 13. Current interpretation of the v0.1.2 design

The evidence suggests that v0.1.2 contains two different ideas.

## 13.1 Prior-art governance

This includes:

- Internal Software Map;
- GitHub/PyPI search;
- source inspection;
- hard gates;
- provenance;
- Build-vs-Borrow classification;
- Reuse Blueprint;
- Custom Delta.

This is well-defined and observable.

Its incremental engineering value over Luna + IntakeGov is **not yet proven**.

## 13.2 Recomposition / trajectory control

This includes the ability to:

- reconsider a prior decision;
- preserve still-valid parts;
- reopen relevant solution space;
- retrieve new repair ingredients;
- alter composition;
- continue execution.

This is much less well isolated in the controlled v0.1.2 evidence.

It is also the mechanism most strongly associated with the positive live observations.

Therefore:

> **Recomposition should not be described as proven v0.1.2 value. It should be described as the strongest unresolved hypothesis emerging from v0.1.2 live use.**

---

# 14. What v0.1.2 can responsibly claim today

The following claims are supported.

### Supported

- SPARI formalizes software prior art and reuse as an explicit engineering decision.
- SPARI treats internal software as first-class prior art.
- SPARI produces structured Build-vs-Borrow evidence.
- SPARI can preserve existing architecture while evaluating alternatives.
- SPARI can reject unsuitable external candidates rather than blindly maximizing reuse.
- SPARI provides structured Custom Delta and execution-outcome accounting.
- SPARI can add substantial compute overhead when FULL research is unnecessary.
- Luna + IntakeGov is a strong baseline and must not be artificially weakened when evaluating SPARI.

### Not yet proven

- that SPARI materially improves completion over Luna + IntakeGov;
- that SPARI consistently reduces Custom Delta;
- that SPARI consistently lowers maintenance ownership;
- that SPARI improves repair success;
- that SPARI produces net token savings;
- that GitHub/PyPI search creates material incremental value in the tested tasks;
- that Recomposition is causally responsible for the strongest live behavior;
- that SPARI turns a smaller model into the equivalent of a substantially stronger model.

### Open but important hypotheses

- Recomposition may be SPARI’s strongest capability.
- Minimal-invasive, architecture-preserving repair may be a better value metric than dependency reuse alone.
- SPARI may be more valuable on long-running trajectories than on bounded feature tasks.
- Persistent repository structure and prior engineering experience may create a stronger differentiator than repeated front-loaded research.
- The appropriate amount of SPARI behavior may depend on the capability and reliability of the underlying model.

---

# 15. Current product status

The correct status for v0.1.2 is:

> **EXPERIMENTAL**

FULL-SPARI should not be presented as proven to improve every engineering task.

At the same time, the evidence is insufficient to conclude that SPARI is unjustified as a concept.

A more precise statement is:

> **SPARI v0.1.2 successfully formalizes prior-art-aware engineering and produces disciplined reuse/rejection evidence, but controlled experiments have not yet established material incremental engineering outcomes over Luna + IntakeGov. Live use suggests that evidence-driven Recomposition and minimal-intervention repair may be the more important capability, but that hypothesis remains to be isolated and measured.**

---

# 16. Evidence-backed lessons for future work

These are implications from the v0.1.2 evidence, not claims about a future release.

### Preserve

- Internal Software Map;
- architecture preservation;
- hard reuse/rejection gates;
- Custom Delta;
- structured execution outcomes;
- Recomposition as a core concept.

### Investigate

- explicit Recomposition events;
- backtracking and trajectory branching;
- repair-ingredient retrieval;
- intervention-size / edit-fidelity metrics;
- repeated-failure recovery;
- long-horizon task performance;
- persistent structural repository knowledge;
- trajectory/repair memory.

### Avoid assuming

- more research means more engineering value;
- more candidates means better decisions;
- an accepted test suite proves SPARI caused the solution;
- a stronger trace is equivalent to a stronger engineering result;
- external reuse must occur for SPARI to be useful.

---

# 17. Recommended metrics for the next SPARI evidence cycle

The missing measurements are now clearer.

Future evaluation should capture at least:

### Recomposition

- number of explicit recomposition events;
- trigger for each event;
- hypothesis before/after;
- decision before/after;
- which prior work was retained;
- which path was abandoned.

### Repair quality

- acceptance outcome;
- root causes found;
- failed paths escaped;
- regression count;
- architecture authorities added/duplicated;
- dependencies added.

### Minimal intervention

- production files changed;
- functions/classes changed;
- public interfaces changed;
- new authorities introduced;
- patch size;
- semantic edit surface;
- Custom Delta before/after recomposition.

### Research economy

- tokens per phase;
- tool calls per phase;
- time per phase;
- first material discovery;
- last material discovery;
- research after decision stability.

### Long-horizon quality

- ability to recover after failed hypotheses;
- coherence after multiple repair cycles;
- repeated rediscovery avoided through memory;
- final solution stability.

These measurements are specifically intended to test the unresolved live Recomposition hypothesis rather than repeat the v0.1.2 front-loaded research evaluations.

---

# 18. Final evidence statement

As of 2026-09-17:

> **SPARI v0.1.2 has not yet proven a material incremental engineering outcome over Luna + IntakeGov in controlled tests.**

It **has** demonstrated a coherent framework for:

- internal prior-art mapping;
- structured solution-space exploration;
- evidence-based reuse/rejection;
- architecture-preserving decisioning;
- Custom Delta accounting;
- execution evidence and revalidation.

The strongest positive practical observation remains:

> **SPARI-guided long-running work appears to recompose toward small, architecture-consistent changes with unusually coherent use of existing system knowledge.**

That observation is currently **qualitative**.

The strongest research-backed next hypothesis is:

> **SPARI’s differentiating value may lie less in doing more research before coding and more in preventing first-solution lock-in through evidence-driven Recomposition over internal prior art, repair ingredients, prior decisions, and execution feedback.**

This hypothesis is consistent with relevant work in autonomous program repair, repository-level planning, code-graph augmentation, repair-ingredient reuse, and search/backtracking for software agents.

It is not yet a proven property of SPARI v0.1.2.

---

## Appendix A — Controlled evaluation summary

| Evidence item | Primary result |
|---|---|
| Historical AVCOS combined run | useful combined behavior; SPARI attribution unavailable |
| SPARI-EVAL-PROD-001 | process contribution; unique outcome causation not proven |
| Evaluation Case 002 | equal 3/3 acceptance; +720,588 C-vs-B tokens; marginal compute |
| SPARI-PROOF-001 | case not discriminative; A/B both found hidden solution; C not run |
| Class A | case not discriminative |
| Class B | A/B/C 4/4; C +38,664 measured tokens vs B; no material B→C uplift |
| Class C | rejected / not qualified |
| Class D | negative control; no material uplift at substantial extra cost |
| Final status | `SPARI_EXPERIMENTAL` |

---

## Appendix B — Evidence packages

The report was consolidated from the available evaluation artifacts and prior SPARI development discussions, including:

- `SPARI_EVAL_PROD_001_2026-09-16`
- Evaluation Case 002 / Matching & Cooperation evidence package
- `SPARI_PROOF_001_2026-09-16`
- `SPARI_1.0_EVAL_001_2026-09-16`
- SPARI v0.1.2 `SKILL.md`
- SPARI v0.1.2 `CHANGELOG.md`
- historical AVCOS SPARI handoff/audit evidence
- prior live-use observations discussed during v0.1.2 development

Where these sources disagree in strength, the report gives priority to controlled evidence and labels weaker evidence explicitly.
