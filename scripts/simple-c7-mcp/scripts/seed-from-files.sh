#!/bin/bash
#
# Seed the running c7-mcp server with markdown docs from a directory.
#
# Usage:
#   ./scripts/seed-from-files.sh [DATA_DIR] [API_URL]
#
# Defaults:
#   DATA_DIR  = ../lancedb/tests/data  (relative to this script)
#   API_URL   = http://localhost:8000
#
# Each .md file becomes a document. The filename (minus .md) is used as
# both the library name and document title. Scoped directories like
# @solidjs/ produce libraries named "@solidjs/router" etc.
#
# The script is idempotent — it skips libraries that already exist.

set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "$0")" && pwd)"
DATA_DIR="${1:-${SCRIPT_DIR}/../../lancedb/tests/data}"
API_URL="${2:-http://localhost:8000}"

DATA_DIR="$(cd "$DATA_DIR" && pwd)"

LIB_URL="${API_URL}/api/v1/libraries"
DOC_URL="${API_URL}/api/v1/documents"

success=0
failed=0
skipped=0

create_library() {
    local name="$1"
    local response
    response=$(curl -sf -X POST "$LIB_URL" \
        -H 'Content-Type: application/json' \
        -d "$(printf '{"name":%s,"language":"Unknown","ecosystem":"unknown"}' \
            "$(echo "$name" | python3 -c 'import json,sys; print(json.dumps(sys.stdin.read().strip()))')")" \
        2>&1) && return 0

    # 400 = already exists, that's fine
    if curl -s -o /dev/null -w '%{http_code}' -X POST "$LIB_URL" \
        -H 'Content-Type: application/json' \
        -d "$(printf '{"name":%s,"language":"Unknown","ecosystem":"unknown"}' \
            "$(echo "$name" | python3 -c 'import json,sys; print(json.dumps(sys.stdin.read().strip()))')")" \
        | grep -q '^400$'; then
        return 0
    fi
    return 1
}

get_library_id() {
    local name="$1"
    curl -sf "$LIB_URL" | python3 -c "
import json, sys
libs = json.load(sys.stdin)
for lib in libs:
    if lib['name'] == '$name':
        print(lib['id'])
        sys.exit(0)
sys.exit(1)
"
}

upload_doc() {
    local title="$1"
    local library_id="$2"
    local file="$3"

    # Use python to build the JSON payload safely (handles large content, special chars)
    python3 -c "
import json, sys, urllib.request

content = open('$file', 'r').read()
payload = json.dumps({
    'title': '$title',
    'library_id': '$library_id',
    'content': content
}).encode()

req = urllib.request.Request(
    '$DOC_URL',
    data=payload,
    headers={'Content-Type': 'application/json'}
)
try:
    with urllib.request.urlopen(req) as resp:
        result = json.loads(resp.read())
        print(f\"  doc_id={result['id']}\")
except urllib.error.HTTPError as e:
    body = e.read().decode()
    print(f'  ERROR {e.code}: {body}', file=sys.stderr)
    sys.exit(1)
"
}

echo "Seeding from: $DATA_DIR"
echo "API:          $API_URL"
echo

# Collect all .md files (top-level and scoped dirs)
find "$DATA_DIR" -name '*.md' -type f | sort | while read -r file; do
    rel="${file#"$DATA_DIR/"}"

    # Derive library name from path:
    #   fastapi.md          -> fastapi
    #   @solidjs/start.md   -> @solidjs/start
    dir="$(dirname "$rel")"
    base="$(basename "$rel" .md)"

    if [ "$dir" = "." ]; then
        lib_name="$base"
    else
        lib_name="${dir}/${base}"
    fi

    printf "%-40s " "$lib_name"

    # Create library (idempotent)
    if ! create_library "$lib_name"; then
        echo "FAIL (library create)"
        failed=$((failed + 1))
        continue
    fi

    # Get library ID
    lib_id=$(get_library_id "$lib_name") || {
        echo "FAIL (library lookup)"
        failed=$((failed + 1))
        continue
    }

    # Upload document
    if upload_doc "$lib_name Documentation" "$lib_id" "$file"; then
        echo "OK"
        success=$((success + 1))
    else
        echo "FAIL (doc upload)"
        failed=$((failed + 1))
    fi
done

echo
echo "Done. success=$success failed=$failed"
