# Practice run: GitHub to Zenodo Sandbox

Work through this in order. Everything here uses **sandbox.zenodo.org**, never the real zenodo.org.
Sandbox DOIs start with `10.5072` and are not permanent.

## A. First release (code record)

1. Make the GitHub repo public (Zenodo's GitHub integration reads public repos only).
2. Sign in at sandbox.zenodo.org with GitHub. Open Account, GitHub, and switch this repo **on**.
   (The sandbox has its own switch, separate from the real Zenodo.)
3. Check `CITATION.cff` and `.zenodo.json` agree (title, author, ORCID, license). If both exist,
   Zenodo uses `.zenodo.json`.
4. On GitHub, create a release tagged `v0.1.0`. Zenodo mints a DOI within a minute or two.
5. Copy the two DOIs from the Zenodo record: the **version DOI** (this release) and the
   **concept DOI** (always the latest version; the one papers should cite).

## B. Put the DOI back

6. Add the concept DOI to `README.md` and `CITATION.cff` (`doi:` field), and the DOI badge to the README.
7. In `paper/make_mock_preprint.py`, replace the placeholder on page 3 with the code DOI and rebuild:
   `python3 paper/make_mock_preprint.py`.

## C. Preprint record and cross-links

8. At sandbox.zenodo.org choose New upload. Upload `paper/mock_preprint.pdf`.
   Resource type: Publication, then Preprint. Fill title and author as in the PDF.
9. Under related identifiers add the **code concept DOI**, relation **is supplemented by**.
10. Publish. Open the code record, edit it, and add the preprint DOI, relation **is supplement to**.
    (Editing metadata does not need a new release.)

## D. Second release (versioning)

11. Change something small, bump `version` and `date-released` in `CITATION.cff`, commit, tag `v0.1.1`,
    publish a release. Confirm the concept DOI is unchanged and a new version DOI appears.

## E. Large-file case (optional)

GitHub caps files at 100 MB; Zenodo takes up to 50 GB per record by direct upload. Large data should
go to Zenodo directly, not through the repo. Practice with the dummy file named `mock_dataset_5MB.csv`
kept **outside** this repository: upload it as its own Dataset record and link it to the others
(is supplemented by).

## F. Afterwards

12. Note what was confusing. Then redo the real thing on zenodo.org, not the sandbox.

## G. Lessons learned (v0.1.0 to v0.1.3)

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
- **Release order matters.** A tag archives the repo as it was at that moment. `REPO_CHECKLIST.md`
  merged after v0.1.2 and so only shipped in v0.1.3. Merge, then bump `CITATION.cff`, then tag.
- **Merge via PR so CI runs first.** CI caught nothing here, but the pre-commit step (gitleaks,
  large-file check) had never run anywhere before the first PR.
- **CI runs twice per push** when the workflow triggers on both `push` and `pull_request`.
  Harmless; restrict `push` to `master` if it bothers you.
- **API tokens stay with you.** Editing a published record (related identifiers) needs your
  sandbox token or the web UI. Don't hand a token to an assistant or paste it into a repo file.
- **Before the real run:** switch from `sandbox.zenodo.org` to `zenodo.org` deliberately (real DOIs
  are permanent), remove the "test / do not cite" banners and metadata, and re-check the license.
