# SPARI v0.1.2 documentation update

This is intentionally **not** a v0.1.3 release.

The README patch targets the current public GitHub `main` README observed on 2026-09-16 (v0.1.2, 1307 lines). It does not replace the README with an older/local copy.

## Files

- `patches/README.patch`
  - fixes the IntakeGov-like header phrase;
  - clarifies that GitHub/PyPI are the external research focus;
  - explicitly states that other registries/ecosystems are not part of the current v0.x build;
  - adds evidence/measurement discipline without inventing a score;
  - strengthens the "What SPARI is not" and behavioral-test summaries.

- `references/closed-loop.md`
  - full replacement for the current file;
  - adds outcome evidence summaries and observed/estimated/unknown discipline.

- `references/evaluation-composition.md`
  - full replacement for the current file;
  - adds evidence-backed comparison without weighted synthetic rankings.

- `tests/adversarial-cases.append.md`
  - append tests 31–34 to the existing `tests/adversarial-cases.md`.

## Apply

From the repository root:

```bash
git apply patches/README.patch
cp references/closed-loop.md ./references/closed-loop.md
cp references/evaluation-composition.md ./references/evaluation-composition.md
cat tests/adversarial-cases.append.md >> ./tests/adversarial-cases.md
```

If you extract this archive into a separate directory, use the extracted paths as the source paths for the two `cp` commands.

No version badge, SKILL metadata, schemas, or changelog version is changed.
