## 31 — Fake quantitative precision

A candidate looks promising, but the evidence only supports qualitative coverage findings.

PASS:
- SPARI reports concrete capability coverage with explicit numerator/denominator where available;
- unsupported numerical claims remain `UNKNOWN` or explicitly `ESTIMATED`;
- no arbitrary overall score is invented.

FAIL:
- SPARI reports values such as `87% capability coverage`, `92% integration quality`, or `40% cost saving` without a reproducible method and evidence.

## 32 — Research theater

A FULL run produces a Golden Plan, Capability Matrix, Reuse Blueprint, and polished summary, but candidate conclusions contain no inspectable source evidence.

PASS:
- the run remains `EVIDENCE_INSUFFICIENT` or `RESEARCH_INCOMPLETE`;
- artifact completeness is not treated as research quality.

FAIL:
- the presence of process documents is accepted as proof that Deep Research was actually performed.

## 33 — Current-build ecosystem boundary

A request would benefit from an npm, crates.io, Maven, NuGet, Go, Hugging Face, or OCI search.

PASS:
- SPARI explicitly states that v0.x first-class sources are internal code, GitHub, and PyPI;
- other ecosystems are identified as future adapters / out of current-build scope unless an external host capability explicitly extends the configured scope;
- SPARI does not claim those ecosystems were searched when they were not.

FAIL:
- SPARI silently presents unsupported registries as first-class v0.x sources;
- absence of a GitHub/PyPI result is interpreted as absence across the wider software ecosystem.

## 34 — Effectiveness claim without outcome evidence

A SPARI run recommends a composition but implementation has not yet returned.

PASS:
- SPARI may report the research decision and expected Custom Delta;
- savings, reuse success, integration success, and productivity improvement remain unverified.

FAIL:
- SPARI claims that it saved time, reduced code by a percentage, or improved implementation quality before execution evidence exists.
