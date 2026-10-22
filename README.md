> [!WARNING]
> **DRY RUN / PIPELINE TEST ONLY — DO NOT CITE OR USE**
> This repository (`zenodo-pipeline-test`) is a temporary test environment created solely to validate automated Git-to-Zenodo release workflows. All code, datasets, and preprints in this repository are synthetic mocks and must not be cited, reproduced, or relied upon for research.

# Zenodo Pipeline Test

This repository contains mock research files, scripts, and preprints used to test automated archival pipelines.

Sandbox concept DOI (all versions, not a real DOI): [10.5072/zenodo.614305](https://sandbox.zenodo.org/doi/10.5072/zenodo.614305)

## What's where

| Folder | Contents |
|---|---|
| [`manuscript/`](manuscript/) | The manuscript. Co-authors: start with [`CONTRIBUTING.md`](CONTRIBUTING.md). |
| [`tables/`](tables/), [`figures/`](figures/) | Tables (HTML in Markdown) and figure images linked from the manuscript |
| [`genai-logs/`](genai-logs/) | GenAI use logs, one file per session |
| [`paper/`](paper/) | The mock preprint PDF archived on Zenodo |
| [`src/`](src/), [`scripts/`](scripts/) | Analysis code and helper scripts |
| [`docs/`](docs/) | Zenodo practice guide and repo checklist |

Run the checks: `python3 test_pipeline.py` and `python3 scripts/check_links.py`.
