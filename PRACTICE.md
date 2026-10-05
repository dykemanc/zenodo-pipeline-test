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
