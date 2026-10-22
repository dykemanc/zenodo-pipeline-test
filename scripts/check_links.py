"""Fail if a Markdown file links to a repo file that doesn't exist (e.g. a mistyped ../tables/table-3.md)."""
import pathlib
import re
import subprocess
import sys
from urllib.parse import unquote

errors = []
for name in subprocess.run(["git", "ls-files", "*.md"], capture_output=True, text=True, check=True).stdout.split():
    md = pathlib.Path(name)
    text = re.sub(r"```.*?```|`[^`\n]*`", "", md.read_text(), flags=re.S)  # snippets in code are examples, not links
    for target in re.findall(r"\]\(\s*([^)\s]+)", text):
        path = unquote(target.split("#")[0])
        if not path or re.match(r"[a-z]+:", path):  # same-page anchor, or http:/mailto:
            continue
        if not (md.parent / path).exists():
            errors.append(f"{md}: broken link {target}")

if errors:
    sys.exit("\n".join(errors))
print("links OK")
