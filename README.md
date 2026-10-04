# Zenodo Pipeline Test Repository

> **This is a test repository. It is not research and it is not meant to be cited or reused.**
>
> It exists only to test the GitHub-to-Zenodo release pipeline (GitHub release, then DOI) against the **Zenodo Sandbox** (sandbox.zenodo.org), which is a throwaway test service. It has to be public because Zenodo's GitHub integration can only read public repositories.
>
> - Any DOI minted from it is a **sandbox DOI** and is not permanent or citable.
> - The code is a toy. The data and results are placeholders.
> - It holds no real credentials, no real data and no study material. Real projects are kept in separate repositories.
>
> Author: Cass Dykeman.

## What it does

Practice repo for testing pre-commit hooks and Zenodo Sandbox DOI minting.

## Files

- `src/analysis.py`, `test_pipeline.py`: the toy code and its test
- `paper/mock_preprint.pdf`: a 3-page mock preprint (placeholder text); `paper/make_mock_preprint.py` rebuilds it
- `CITATION.cff`, `.zenodo.json`: release metadata (keep the two in agreement)
- `PRACTICE.md`: the step-by-step practice checklist

## Usage

    python src/analysis.py
    python test_pipeline.py

## Status

Toy project for pipeline practice only.
