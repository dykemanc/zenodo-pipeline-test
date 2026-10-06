"""Fail if .zenodo.json and CITATION.cff disagree. Zenodo uses .zenodo.json when both exist."""
import json
import sys

import yaml

z = json.load(open(".zenodo.json"))
c = yaml.safe_load(open("CITATION.cff"))

zenodo_names = {x["name"] for x in z["creators"]}
cff_names = {f'{a["family-names"]}, {a["given-names"]}' for a in c["authors"]}

errors = []
if zenodo_names != cff_names:
    errors.append(f"authors differ: .zenodo.json={sorted(zenodo_names)} CITATION.cff={sorted(cff_names)}")
if z["license"].lower() != c["license"].lower():
    errors.append(f'license differs: .zenodo.json={z["license"]} CITATION.cff={c["license"]}')

if errors:
    sys.exit("\n".join(errors))
print("metadata OK")
