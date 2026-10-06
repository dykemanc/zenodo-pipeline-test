# Repo structure and content checklist

Based on the prevalence data in Hora, Montandon & Costa, *What's Inside a GitHub Repository?* (arXiv 2605.16701, 2026) and on the practice run in this repo. Each tier is a rule for when to add things. Don't add a later tier's items until its trigger is true.

## Tier 1: every repo, day one

| Item | Why |
|---|---|
| `README.md` | What it is, how to run it, status. Present in 95% of repos in the paper. Add a "test / do not cite" banner if it applies. |
| `LICENSE` | Without one, others have no legal right to reuse your work. MIT for code, CC-BY for text and data. |
| `.gitignore` | Cover `.venv/`, `__pycache__/`, `.env`, `.DS_Store`, and any output or data directories. |
| `src/` (or the language's convention) | Keeps code separate from config and docs. |
| One runnable check | A single test or smoke script, e.g. `test_pipeline.py`. Non-trivial logic should have at least one. |
| `.pre-commit-config.yaml` with a secret scan and a large-file check | The cheapest protection against leaked keys and giant commits. Used here: gitleaks plus `check-added-large-files`. |

## Tier 2: once it is shared or reused

| Item | Trigger |
|---|---|
| `.github/workflows/ci.yml` | As soon as the repo is on GitHub. Keep it to checkout, install, run the check, and run pre-commit. Skip matrices and caching. |
| `tests/` directory | When you have a second test. One file at the root is fine until then. |
| `CHANGELOG.md` | When you cut tagged releases other people read. One line per release. |
| `CLAUDE.md` or `AGENTS.md` (one only) | When you use a coding agent. Rules and conventions only, no duplicated docs. |
| `docs/` | When the README gets too long. Until then, keep it in the README. |

## Tier 3: research or archival repos

| Item | Why |
|---|---|
| `CITATION.cff` | Machine-readable citation. Validate it in CI with `cffconvert --validate`. |
| `.zenodo.json` | Only if you need to override what Zenodo reads from the GitHub release. If both files exist, Zenodo uses this one. |
| A metadata consistency check in CI | `.zenodo.json` and `CITATION.cff` can drift apart, so check authors and license (see `scripts/check_metadata.py`). This repo caught a real MIT vs cc-by-4.0 mismatch that way. |
| DOI in the README and `CITATION.cff` | Use the concept DOI, which always points to the latest version. |
| A provenance log such as `GenAI_provenance/` | Only if you disclose AI use. Keep it short. |
| Large data stored outside the repo | GitHub caps files at 100 MB, so upload big files to Zenodo directly. |

## Tier 4: only with outside contributors or a public user base

- `CONTRIBUTING.md`, `CODE_OF_CONDUCT.md`, `SECURITY.md`
- `ISSUE_TEMPLATE/`, `PULL_REQUEST_TEMPLATE.md`, `CODEOWNERS`
- `.gitattributes`, `.editorconfig` (useful on teams and across operating systems)
- `pyproject.toml` or `package.json` if the code is installable. Use `pyproject.toml`, not `setup.py`.
- `Dockerfile` or `Makefile` if you have a real build or run recipe

## Release routine (any archived repo)

1. Merge through a PR and confirm CI is green.
2. Bump `version` and `date-released` in `CITATION.cff`.
3. Tag `vX.Y.Z` and create the release.
4. Verify the new version record, then check that the concept DOI is unchanged and the license and metadata are correct.
5. Add or update cross-links between code and paper records.

## Over-engineering signals

- Adding a file because it's common (`CODE_OF_CONDUCT.md` in a private test repo) instead of because someone needs it.
- Two files saying the same thing (`CLAUDE.md` plus `AGENTS.md`, or a `docs/` copy of the README).
- CI beyond what you'd run by hand: matrix builds, coverage uploads, auto-release.
- Packaging and dependency tooling for a single script.
- Templates for issue streams that don't exist.

## Minimal layout

```
repo/
├── README.md
├── LICENSE
├── .gitignore
├── .pre-commit-config.yaml
├── CLAUDE.md                  # if using an agent
├── CITATION.cff               # if citable
├── .zenodo.json               # only if overriding
├── .github/workflows/ci.yml
├── src/
├── tests/                     # or test_*.py until you have two
└── scripts/                   # small helpers, e.g. check_metadata.py
```

## Caveats

Prevalence isn't evidence of quality. The paper's sample is popular, actively maintained repos with 100 or more stars, so tier 4 reflects projects with contributors. Judge each item by who will use it.
