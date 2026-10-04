#!/usr/bin/env bash
# Practice upload to the Zenodo SANDBOX (test DOIs, 10.5072/...).
# Usage: ZENODO_TOKEN=... ./zenodo_sandbox.sh FILE [--publish]
# Without --publish it stops at an editable draft.
set -euo pipefail

: "${ZENODO_TOKEN:?set ZENODO_TOKEN (sandbox token, scopes deposit:write + deposit:actions)}"
FILE="${1:?usage: $0 FILE [--publish]}"
[ -f "$FILE" ] || { echo "no such file: $FILE" >&2; exit 1; }
API="${ZENODO_API:-https://sandbox.zenodo.org/api}"
# ponytail: sandbox only; refuse production so a practice run can't publish a real DOI
case "$API" in *sandbox.zenodo.org*) ;; *) echo "refusing non-sandbox API: $API" >&2; exit 1;; esac

auth=(-H "Authorization: Bearer $ZENODO_TOKEN")
json=(-H "Content-Type: application/json")

echo "1. create deposition"
dep=$(curl -fsS -X POST "$API/deposit/depositions" "${auth[@]}" "${json[@]}" -d '{}')
id=$(jq -r .id <<<"$dep")
bucket=$(jq -r .links.bucket <<<"$dep")

echo "2. upload $FILE"
curl -fsS -X PUT "$bucket/$(basename "$FILE")" "${auth[@]}" --upload-file "$FILE" >/dev/null

echo "3. add metadata"
curl -fsS -X PUT "$API/deposit/depositions/$id" "${auth[@]}" "${json[@]}" -d '{
  "metadata": {
    "title": "Sandbox test",
    "upload_type": "dataset",
    "description": "Practice upload",
    "creators": [{"name": "Dykeman, Cass"}]
  }
}' >/dev/null

if [ "${2:-}" = "--publish" ]; then
  echo "4. publish"
  curl -fsS -X POST "$API/deposit/depositions/$id/actions/publish" "${auth[@]}" | jq '{doi, record_url: .links.record_html}'
else
  echo "Draft ready (id $id): https://sandbox.zenodo.org/deposit/$id"
  echo "Re-run with --publish to publish a new one."
fi
