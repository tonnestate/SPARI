# Decision Memory

Store:

- capability;
- Golden Plan version;
- candidate;
- source;
- version/commit;
- evidence;
- capability coverage;
- hard-gate results;
- solution decision;
- reuse mode;
- license decision;
- composition role;
- proof-of-fit;
- implementation outcome;
- limitations;
- last verified;
- revalidation triggers.

Research recommendation and implementation outcome are different facts.

Example:

```text
research_decision: ADOPT
implementation_outcome: REJECTED_AFTER_IMPLEMENTATION
```

Before new research:

1. query SPARI memory;
2. determine whether evidence is still valid;
3. revalidate only triggered areas;
4. research remaining gaps.


## Retrieval discipline

Durable memory may be rich. Active context should be selective.

Before injecting prior decisions into a new run:

1. match the current capability;
2. match relevant runtime/project constraints;
3. match ecosystem/source family;
4. check freshness;
5. check revalidation triggers;
6. retrieve only records that can materially affect the decision.

Do not dump the full SPARI history into every agent context.

This prevents institutional memory from becoming context rot.
