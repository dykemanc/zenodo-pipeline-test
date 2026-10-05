"""Build paper/mock_preprint.pdf: a 3-page MOCK preprint (placeholder text) for practising
the Zenodo deposit. Needs only matplotlib. Run from the repository root:
    python3 paper/make_mock_preprint.py
"""
import textwrap
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

LOREM = ("Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut "
         "labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco "
         "laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in "
         "voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat "
         "non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.")
TITLE = "A Mock Preprint for Testing the Zenodo Pipeline"
BANNER = "MOCK PREPRINT - placeholder text, not real research, do not cite"

def page(pdf, n, blocks, figure=False):
    fig = plt.figure(figsize=(8.5, 11))
    fig.text(0.5, 0.965, BANNER, ha="center", va="top", fontsize=9, color="#b00020", weight="bold")
    fig.text(0.5, 0.03, f"Zenodo Sandbox practice record  -  page {n} of 3", ha="center", fontsize=8, color="#555")
    y = 0.93
    for kind, text in blocks:
        if kind == "title":
            fig.text(0.5, y, textwrap.fill(text, 55), ha="center", va="top", fontsize=17, weight="bold"); y -= 0.085
        elif kind == "author":
            fig.text(0.5, y, text, ha="center", va="top", fontsize=10); y -= 0.05
        elif kind == "h":
            y -= 0.012; fig.text(0.1, y, text, va="top", fontsize=12, weight="bold"); y -= 0.03
        else:
            w = textwrap.fill(text, 95); lines = w.count("\n") + 1
            fig.text(0.1, y, w, va="top", fontsize=9.5, linespacing=1.45); y -= 0.0165 * lines + 0.012
    if figure:
        import random
        random.seed(1)
        ax = fig.add_axes([0.15, 0.12, 0.7, 0.2])
        xs = list(range(1, 21)); ys = [i * 0.5 + random.uniform(-1, 1) for i in xs]
        ax.plot(xs, ys, marker="o"); ax.set_xlabel("x (synthetic)"); ax.set_ylabel("y (synthetic)")
        ax.set_title("Figure 1. Synthetic data, for layout only", fontsize=9)
    pdf.savefig(fig); plt.close(fig)

with PdfPages("paper/mock_preprint.pdf", metadata={"Title": TITLE, "Author": "Cass Dykeman",
        "Subject": "Mock preprint for Zenodo Sandbox practice"}) as pdf:
    page(pdf, 1, [("title", TITLE), ("author", "Cass Dykeman  |  Oregon State University  |  ORCID 0000-0001-7708-1409"),
        ("h", "Abstract"), ("p", LOREM), ("h", "Introduction"), ("p", LOREM), ("p", LOREM)])
    page(pdf, 2, [("h", "Methods"), ("p", LOREM), ("h", "Results"), ("p", LOREM), ("p", LOREM)], figure=True)
    page(pdf, 3, [("h", "Discussion"), ("p", LOREM), ("h", "Code and data availability"),
        ("p", "The code for this mock study is archived on the Zenodo Sandbox: 10.5072/zenodo.614305 (sandbox DOI, not a real DOI)."),
        ("h", "References"), ("p", "[1] Placeholder, A. (2026). Lorem ipsum. Journal of Test Records, 1(1), 1-3.")])
print("wrote paper/mock_preprint.pdf")
