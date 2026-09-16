diff --git a/README.md b/README.md
--- a/README.md
+++ b/README.md
@@
 <p align="center">
-  <strong>Classify before you execute.</strong><br>
+  <strong>Reuse before you rebuild.</strong><br>
  SPARI is a Build-vs-Borrow engine for AI software development.
 </p>
@@
-Its technical method is **GitHub-first and PyPI-first prior-art intelligence**.
+Its external research method is **GitHub- and PyPI-centered prior-art intelligence**.
@@
 These are future extension points, not v0.1.2 research requirements.
+
+**SPARI is not a universal software-registry crawler. v0.x is intentionally limited to the existing internal codebase, GitHub, and PyPI; npm, crates.io, Go modules, Maven Central, NuGet, Hugging Face, OCI registries, and other ecosystems are future adapters, not part of the current build.**
+
 See [`references/source-model.md`](references/source-model.md).
@@
 SPARI must remember that.

 ---
+# Evidence without false precision
+
+SPARI should make Build-vs-Borrow outcomes measurable where the evidence supports it.
+
+Useful evidence includes:
+
+```text
+capabilities_total
+capabilities_covered_internal
+capabilities_covered_external
+capabilities_custom_required
+
+candidates_discovered
+candidates_failed_hard_gates
+candidates_deep_inspected
+
+planned_reuse
+actual_reuse
+
+planned_custom_delta
+actual_custom_delta
+
+verification_outcome
+```
+
+Derived measures such as reuse yield are allowed only when the underlying capability units are explicitly defined and comparable.
+
+SPARI must distinguish:
+
+```text
+OBSERVED
+ESTIMATED
+UNKNOWN
+```
+
+Do not manufacture percentages, scores, LOC savings, cost reductions, or productivity claims merely to make a decision look quantitative.
+
+Measurement exists to make the decision auditable and empirically testable — not to replace engineering judgement with a synthetic score.
+
+See [`references/evaluation-composition.md`](references/evaluation-composition.md) and [`references/closed-loop.md`](references/closed-loop.md).
+
+---
 # Research decision ≠ implementation outcome
@@
 SPARI is not:

 - a generic web-search skill;
+- a universal software-registry crawler;
 - a GitHub link collector;
 - a PyPI recommendation list;
@@
 - failed implementation outcomes forgotten by later agents;
-- ecosystem expansion that accidentally changes SPARI's v0.x scope.
+- ecosystem expansion that accidentally changes SPARI's v0.x scope;
+- fake quantitative precision without inspectable evidence;
+- research artifacts being mistaken for evidence of research quality.
 See [`tests/adversarial-cases.md`](tests/adversarial-cases.md).
