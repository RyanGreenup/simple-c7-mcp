# Context7 Forward Pass: Extract Library ID and Content

A **forward pass** retrieves documentation in two steps:

1. **Resolve Library ID** - Convert a library name to a Context7 identifier
2. **Query Documentation** - Retrieve documentation using that identifier

## Step 1: Resolve Library ID

Convert a library name (like "React" or "Next.js") into a structured library ID.

**Endpoint:** `resolve-library-id`

**Input Parameters:**
```json
{
  "libraryName": "React",
  "query": "How to use useState hook"
}
```

**MCP Request Format:**
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "resolve-library-id",
    "arguments": {
      "libraryName": "React",
      "query": "How to use useState hook"
    }
  }
}
```

**Response Structure:**
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "Library ID: /facebook/react\n\nOther available libraries:\n- /facebook/react-native\n- /vercel/next.js"
      }
    ]
  }
}
```

### Extract the Library ID

The response text embeds the library ID in one of these patterns:

- `/org/project` - e.g., `/facebook/react`
- `/org/project/version` - e.g., `/vercel/next.js/v14`

**How to extract it:**

1. Access `result.content[0].text`
2. Search for patterns like `Library ID: /org/project`
3. If you find no explicit label, search for standalone paths matching `/[\w-]+/[\w.-]+`

**Python Example:**
```python
import re

# Extract from response
response_text = resolve_result["result"]["content"][0]["text"]

# Method 1: Look for explicit "Library ID:" pattern
id_match = re.search(
    r'(?:Library ID|libraryId|id):\s*([/\w.-]+/[\w.-]+(?:/[\w.-]+)?)',
    response_text,
    re.IGNORECASE
)

if id_match:
    library_id = id_match.group(1)
else:
    # Method 2: Find standalone library ID patterns
    all_matches = re.findall(r'/[\w-]+/[\w.-]+(?:/[\w.-]+)?', response_text)
    # Filter out generic placeholders like '/org/project'
    filtered = [m for m in all_matches if m != '/org/project']
    library_id = filtered[0] if filtered else all_matches[0]

print(f"Extracted Library ID: {library_id}")
# Output: Extracted Library ID: /facebook/react
```

## Step 2: Query Documentation

Use the library ID to retrieve documentation.

**Endpoint:** `query-docs`

**Input Parameters:**
```json
{
  "libraryId": "/facebook/react",
  "query": "How to use useState hook"
}
```

**MCP Request Format:**
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "query-docs",
    "arguments": {
      "libraryId": "/facebook/react",
      "query": "How to use useState hook"
    }
  }
}
```

**Response Structure:**
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "content": [
      {
        "type": "text",
        "text": "# useState Hook\n\nThe useState hook allows you to add state to function components...\n\n## Basic Usage\n\n```jsx\nimport { useState } from 'react';\n\nfunction Counter() {\n  const [count, setCount] = useState(0);\n  return <button onClick={() => setCount(count + 1)}>{count}</button>;\n}\n```"
      }
    ]
  }
}
```

### Extract the Documentation

Context7 returns the documentation as formatted text (often Markdown).

**How to extract it:**
```python
# Extract documentation text
doc_text = query_result["result"]["content"][0]["text"]

print(doc_text)
# Output: Full documentation with code examples, explanations, etc.
```

## Complete Example

This implementation shows both steps:

```python
import httpx
import re
import json

MCP_ENDPOINT = "https://mcp.context7.com/mcp"

def make_mcp_request(method: str, params: dict) -> dict:
    """Make a request to the Context7 MCP server."""
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": method,
        "params": params
    }

    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream",
    }

    response = httpx.post(MCP_ENDPOINT, json=payload, headers=headers, timeout=30.0)
    response.raise_for_status()
    return response.json()

def forward_pass(library_name: str, user_query: str):
    """Execute a complete forward pass."""

    # Step 1: Resolve library ID
    print(f"Step 1: Resolving '{library_name}'...")

    resolve_result = make_mcp_request("tools/call", {
        "name": "resolve-library-id",
        "arguments": {
            "libraryName": library_name,
            "query": user_query
        }
    })

    # Extract library ID
    response_text = resolve_result["result"]["content"][0]["text"]

    id_match = re.search(
        r'(?:Library ID|libraryId|id):\s*([/\w.-]+/[\w.-]+(?:/[\w.-]+)?)',
        response_text,
        re.IGNORECASE
    )

    if id_match:
        library_id = id_match.group(1)
    else:
        all_matches = re.findall(r'/[\w-]+/[\w.-]+(?:/[\w.-]+)?', response_text)
        filtered = [m for m in all_matches if m != '/org/project']
        library_id = filtered[0] if filtered else all_matches[0]

    print(f"✓ Found library ID: {library_id}")

    # Step 2: Query documentation
    print(f"\nStep 2: Querying documentation...")

    query_result = make_mcp_request("tools/call", {
        "name": "query-docs",
        "arguments": {
            "libraryId": library_id,
            "query": user_query
        }
    })

    # Extract documentation
    doc_text = query_result["result"]["content"][0]["text"]

    print(f"✓ Retrieved documentation ({len(doc_text)} chars)")
    print(f"\n--- Documentation ---")
    print(doc_text)

    return {
        "library_id": library_id,
        "documentation": doc_text
    }

# Example usage
result = forward_pass("React", "How to use useState hook")
print(f"\nLibrary: {result['library_id']}")
print(f"Docs length: {len(result['documentation'])} characters")
```

## Use the Test Script

The project includes a test script that automates both steps:

```bash
# Complete forward pass
just forward "React" "How to use useState hook"

# Or directly with Python
./context7_test.py forward-pass "React" "How to use useState hook"
```

The script resolves the library ID, queries the documentation, and displays both results.

## Common Library ID Formats

| Library | Library ID |
|---------|-----------|
| React | `/facebook/react` |
| Next.js | `/vercel/next.js` |
| Express.js | `/expressjs/express` |
| MongoDB | `/mongodb/mongo` |
| Supabase | `/supabase/supabase` |

## Response Field Reference

### Resolve Response Fields

```
result
└── content (array)
    └── [0]
        ├── type: "text"
        └── text: "Library ID: /org/project\n..."
```

### Query Response Fields

```
result
└── content (array)
    └── [0]
        ├── type: "text"
        └── text: "Full documentation in Markdown..."
```

## Handle Errors

Handle extraction errors:

```python
try:
    library_id = extract_library_id(response_text)
except Exception as e:
    print(f"Could not extract library ID: {e}")
    print("Response text:", response_text)
    return None

if not library_id:
    print("No library ID found in response")
    return None
```

## Best Practices

1. **Validate extraction** - Check that the library ID matches expected patterns
2. **Handle multiple matches** - Responses may include alternative libraries
3. **Preserve the full response** - Store both the library ID and raw response for debugging
4. **Use the query for ranking** - Your query helps Context7 rank relevant libraries
5. **Cache library IDs** - Cache the resolved ID when querying the same library repeatedly

## Advanced: Handle Multiple Library Candidates

The resolve endpoint sometimes returns multiple libraries:

```python
def extract_all_library_ids(response_text: str) -> list[str]:
    """Extract all library IDs from response."""
    all_matches = re.findall(r'/[\w-]+/[\w.-]+(?:/[\w.-]+)?', response_text)
    # Remove duplicates while preserving order
    seen = set()
    unique = []
    for match in all_matches:
        if match not in seen and match != '/org/project':
            seen.add(match)
            unique.append(match)
    return unique

# Get all candidates
candidates = extract_all_library_ids(response_text)
print(f"Found {len(candidates)} library candidates:")
for lib_id in candidates:
    print(f"  - {lib_id}")

# Use the first one (highest ranked)
library_id = candidates[0]
```

## Summary

The forward pass follows four steps:

1. **Resolve**: Send library name + query → receive library ID
2. **Extract ID**: Parse response text for `/org/project` pattern
3. **Query**: Send library ID + query → receive documentation
4. **Extract Docs**: Access `result.content[0].text` for documentation

Both responses use the same structure (`result.content[0].text`) but contain different information. Resolve responses contain library identification metadata; query responses contain documentation.

## See Also

- [Context7 MCP Testing README](../scripts/context7-api/README.md)
- [Justfile Commands](../scripts/context7-api/justfile)
- [Test Script Source](../scripts/context7-api/context7_test.py)
