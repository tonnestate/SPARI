# Decision Memory and Trajectory Memory

SPARI persists two complementary forms of reusable engineering intelligence.

## 1. Decision Memory

Decision Memory answers: **What did we decide, under what evidence and constraints, and what happened after implementation?**

Store where applicable:

- capability;
- Golden Plan / Engineering Case reference;
- candidate and source/version/commit;
- evidence and capability coverage;
- hard-gate results;
- solution decision and reuse mode;
- license/provenance state;
- composition role;
- proof-of-fit;
- implementation outcome;
- limitations;
- base/result revision;
- revalidation triggers;
- linked trajectory records;
- last verified.

Research recommendation and implementation outcome are different facts.

```text
research_decision: ADOPT
implementation_outcome: REJECTED_AFTER_IMPLEMENTATION
```

## 2. Trajectory Memory

Trajectory Memory answers: **How did we get out of this problem?**

Persist material engineering episodes rather than every token or thought. A useful trajectory can include:

- case signature / affected capability / observed signal;
- constraints and success criteria;
- hypotheses considered;
- attempted solution paths;
- evidence produced by each attempt;
- contradicting evidence;
- invalidated assumptions;
- evidence retained as still valid;
- repair ingredients discovered;
- recomposition events and reasons;
- composition versions;
- Custom Delta / intervention-surface changes;
- final validated or failed path;
- applicability conditions;
- evidence/revision references.

Trajectory Memory is not a hidden chain-of-thought archive. Store inspectable engineering state, decisions, evidence, actions, failures, and transitions that are useful to future work.

## Retrieval discipline

Before repeating research:

1. match the current capability/problem pattern;
2. match relevant runtime/project constraints;
3. retrieve relevant prior decisions;
4. retrieve relevant prior trajectories;
5. check freshness/applicability/revalidation triggers;
6. inject only records that can materially affect the current case.

Do not dump the full SPARI history into every agent context. Durable memory may be rich; active context must remain selective.
