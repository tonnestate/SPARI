# Research Depth

SPARI research depth is proportional to impact, ambiguity, irreversibility, integration cost, and lifecycle ownership.

## PREFLIGHT

Use when:

- the capability is narrow;
- the target environment is already known;
- one or two obvious reuse candidates are likely;
- the decision is cheap to reverse.

Minimum:

1. inspect local code/dependencies;
2. focused GitHub/PyPI search;
3. verify obvious candidate facts;
4. issue a reuse/build verdict.

Escalate if the search reveals multiple credible solution families or material risk.

## TARGETED

Use when:

- the user names a specific package/repository;
- a capability is known but the dependency choice is unresolved;
- the main need is due diligence rather than solution-space discovery.

Check:

- exact version/revision;
- source linkage;
- compatibility;
- maintenance;
- security;
- license/provenance;
- focused alternatives;
- integration/exit cost.

## FULL

Use when:

- the request is consequential or architectural;
- the solution space is unclear;
- whole products and component libraries may compete;
- several capabilities need composition;
- the result will become a durable base.

FULL includes Broad Recon, evidence-informed clarification, Golden Plan, Deep Research, source inspection, independent evaluation, contrarian review, composition, and Custom Delta.

## Escalation

Research can move upward:

`PREFLIGHT → TARGETED → FULL`

when evidence shows higher ambiguity or impact.

Do not silently downgrade mandatory hard gates because a lighter research mode was selected.
