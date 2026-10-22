# Zenodo Sandbox practice: step-by-step

Goal: turn a GitHub release into a Zenodo Sandbox DOI, then publish the mock preprint and link the two records.
Everything here uses **sandbox.zenodo.org**, never zenodo.org. Sandbox DOIs start with `10.5072`, are not permanent, and the sandbox can be wiped at any time.

Items marked **[verify]** have not been confirmed by a real run; note what you actually see.

## Before you start (5 min)

- [ ] GitHub account `dykemanc` and a Zenodo **Sandbox** account (separate from real Zenodo; "Log in with GitHub" is easiest).
- [ ] `gh` is installed and logged in: `gh auth status`
- [ ] In the repo folder, the test passes: `python3 test_pipeline.py`
- [ ] `git log --format='%ae' | sort -u` shows only the GitHub noreply address. Never push the Outlook address.

## Part A: First release (code record)

**1. Push the repo, public.** Zenodo's GitHub integration can only read public repos. Pushing publishes the history, so check step 3 of "Before you start" first.

```bash
cd zenodo-pipeline-test
gh repo create zenodo-pipeline-test --public --source=. --remote=origin --push
git push origin --tags
```

**2. Switch the repo on in the sandbox.** Do this BEFORE the release, or no record is created.
Sandbox → your name (top right) → **Settings** → **GitHub** → **Sync now** → toggle `zenodo-pipeline-test` **ON**.

**3. Check the metadata.** `CITATION.cff` and `.zenodo.json` must agree (title, author, ORCID, license). If both exist, Zenodo uses `.zenodo.json` (confirmed; see Lessons learned).

**4. Create the release.**

```bash
gh release create v0.1.0 --title "v0.1.0 - Initial Pipeline Release Test" --notes "First practice release."
```

Wait 1 to 2 minutes **[verify]**, then open https://sandbox.zenodo.org/uploads. A record should appear.

**5. Copy both DOIs** from the record page:

| Name | What it is | Use it for |
|---|---|---|
| Version DOI | This release only | Pointing at exactly this code |
| Concept DOI | Always the latest version | Citing in papers |

## Part B: Put the DOI back (commits after the release)

**6.** Add the **concept DOI** and the DOI badge to `README.md`, and the DOI to `CITATION.cff` (`doi:` field). Badge URL format: **[verify]**, copy the snippet from the Zenodo record's sidebar.

**7.** In `scripts/make_mock_preprint.py`, replace `[SANDBOX DOI OF THE CODE RELEASE GOES HERE]` (page 3) with the code DOI, then rebuild:

```bash
python3 scripts/make_mock_preprint.py
git add -A && git commit -m "Add code DOI" && git push
```

Pushing a commit does not trigger a new record. Only a new release does.

## Part C: Preprint record and cross-links

**8. Upload the preprint.** sandbox.zenodo.org → **+** → **New upload** → upload `paper/mock_preprint.pdf`.
Resource type: **Publication → Preprint**. Title and author as in the PDF.

**9. Link to the code.** Under **Related works**, add the **code concept DOI** with relation **is supplemented by**.

**10. Publish, then link back.** Click **Publish** (files are locked afterwards). Open the **code** record → **Edit** → add the **preprint DOI** with relation **is supplement to** → publish. Editing metadata does not need a new release.

## Part D: Second release (versioning)

**11.** Make a small change, bump `version` and `date-released` in `CITATION.cff`, update `.zenodo.json` if it names a version, commit, push, then:

```bash
git tag v0.1.1 && git push origin v0.1.1
gh release create v0.1.1 --title "v0.1.1" --notes "Second practice release."
```

Check: the **concept DOI is unchanged** and a **new version DOI** appears.

## Part E: Large file (optional)

GitHub caps files at 100 MB; Zenodo allows up to 50 GB per record by direct upload. Upload `outputs/mock_dataset_5MB.csv` (kept outside the repo) as its own **Dataset** record, and link it to the other records with **is supplemented by**.

## Part F: Afterwards

Write down what confused you. Then repeat on real zenodo.org, which needs its own account, GitHub switch and token.

## If something goes wrong

| Symptom | Likely cause |
|---|---|
| No record after the release | Repo toggle was off, or the release was created before it was switched on. Toggle ON, then publish a new release. **[verify]** |
| Release is a draft or pre-release | May not archive **[verify]** |
| Commits not linked to your GitHub profile | Commit email not on the GitHub account |
| Record metadata is wrong | `.zenodo.json` overrides `CITATION.cff`; fix the file and release again |
| Can't change files in a published record | By design. Make a new version |

## Optional: API route

`scripts/zenodo_sandbox.sh` uploads a dummy file through the API. It is a contrast exercise, not part of this flow.

## Lessons learned (v0.1.0 to v0.1.3)

- **Two metadata files can disagree.** `.zenodo.json` said `cc-by-4.0` while `LICENSE` and
  `CITATION.cff` said MIT. Zenodo uses `.zenodo.json`, so the code record carried the wrong
  license until v0.1.2. `scripts/check_metadata.py` now fails CI if authors or license differ.
- **Licenses are per record and not retroactive.** v0.1.2 shows MIT; v0.1.0 and v0.1.1 keep
  `cc-by-4.0`. Fixing metadata means a new release. Code (MIT) and the preprint (CC-BY) are
  licensed separately, each in its own record.
- **The concept DOI is the stable one.** It stayed `10.5072/zenodo.614305` across every release
  while each version got a new DOI. Cite and link the concept DOI unless you mean one exact release.
- **The preprint shares the concept DOI** with the code versions in this sandbox run
  (`v0.1.0-preprint` appears in the same version list). Check how your real record groups them.
- **Release order matters.** A tag archives the repo as it was at that moment. The repo checklist
  merged after v0.1.2 and so only shipped in v0.1.3. Merge, then bump `CITATION.cff`, then tag.
- **Merge via PR so CI runs first.** CI caught nothing here, but the pre-commit step (gitleaks,
  large-file check) had never run anywhere before the first PR.
- **CI runs twice per push** when the workflow triggers on both `push` and `pull_request`.
  Harmless; restrict `push` to `master` if it bothers you.
- **API tokens stay with you.** Editing a published record (related identifiers) needs your
  sandbox token or the web UI. Don't hand a token to an assistant or paste it into a repo file.
- **Before the real run:** switch from `sandbox.zenodo.org` to `zenodo.org` deliberately (real DOIs
  are permanent), remove the "test / do not cite" banners and metadata, and re-check the license.
