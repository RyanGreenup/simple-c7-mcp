# Download Libraries from Context7 into LanceDB

Add library documentation from Context7 to your existing LanceDB for semantic search.

## Quick Start

```bash
# Navigate to the lancedb directory
cd scripts/lancedb

# Fetch and ingest a library
just fetch-library "React"

# Search the newly added library
just search "useState hook" --limit 5
```

## How It Works

The `fetch-library` command executes four steps:

1. **Resolve library name** - Calls Context7 API to find the library ID
2. **Download documentation** - Fetches llms.txt from Context7
3. **Save locally** - Stores the file in `tests/data/{library}.md`
4. **Ingest into LanceDB** - Chunks and embeds the documentation

## Basic Usage

### Fetch a Single Library

```bash
# Fetch React documentation
just fetch-library "React"

# Fetch Next.js documentation
just fetch-library "Next.js"

# Fetch with a specific query hint
just fetch-library "Supabase" "authentication and database queries"
```

The query parameter helps Context7 rank results when multiple libraries match the name.

### Search Across Libraries

Once ingested, search across all libraries:

```bash
# Search all documentation
just search "how to create components"

# Limit results
just search "API routes" --limit 10
```

## How Library Resolution Works

Context7 returns multiple library candidates ranked by relevance. The script:

1. Parses the response for all matching libraries
2. Extracts title, library ID, description, and benchmark score
3. Sorts by benchmark score (highest first)
4. Selects the best match

**Example response:**
```
🔍 Resolving library: React
✓ Selected: React (score: 95.2)
  (Found 3 options, selected highest score)
✓ Resolved library_id: /facebook/react
```

**Alternative matches might include:**
- `/facebook/react` (official React library)
- `/facebook/react-native` (React Native)
- `/vercel/next.js` (Next.js, React framework)

## Download URL Format

Context7 URLs follow this pattern:

```
https://context7.com{library_id}/llms.txt
```

**Examples:**
```
https://context7.com/facebook/react/llms.txt
https://context7.com/vercel/next.js/llms.txt
https://context7.com/websites/daisyui/llms.txt
```

## File Storage

The script saves downloaded files to:

```
tests/data/{safe_name}.md
```

**Name conversion:**
- Converts to lowercase
- Replaces spaces with hyphens
- Replaces dots with hyphens

**Examples:**
```
"React" → tests/data/react.md
"Next.js" → tests/data/next-js.md
"daisyUI" → tests/data/daisyui.md
```

## Ingestion Details

### Chunking Strategy

The script ingests using **markdown header chunking** by default:

```bash
uv run lance-db-example ingest tests/data/react.md --library react
```

**The process:**
1. The script reads the file
2. The script splits chunks by `###` headers
3. The script embeds each chunk (384-dimensional vector)
4. LanceDB stores chunks with metadata

### Database Schema

LanceDB stores each chunk with:

```python
{
  "text": "### Hook: useState\n\nManages state in...",
  "chunk_index": 0,
  "library": "react",
  "title": "react.md",
  "vector": [0.123, -0.456, ...]  # 384 dimensions
}
```

## Add Multiple Libraries

Build a comprehensive knowledge base:

```bash
# Frontend frameworks
just fetch-library "React"
just fetch-library "Vue.js"
just fetch-library "Svelte"

# Backend frameworks
just fetch-library "Express.js"
just fetch-library "FastAPI"
just fetch-library "Django"

# Databases
just fetch-library "MongoDB"
just fetch-library "PostgreSQL"
just fetch-library "Supabase"

# UI libraries
just fetch-library "daisyUI"
just fetch-library "Tailwind CSS"
just fetch-library "shadcn/ui"
```

## Search Specific Libraries

Filter searches to specific libraries:

```python
import lancedb

db = lancedb.connect("./lancedb_data")
table = db.open_table("documentation")

# Embed your query
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('all-MiniLM-L6-v2')
query_vector = model.encode(["How to handle authentication"])[0]

# Search only React docs
results = table.search(query_vector) \
    .where("library = 'react'") \
    .limit(5) \
    .to_pandas()

for _, row in results.iterrows():
    print(f"Score: {row['_distance']}")
    print(f"Library: {row['library']}")
    print(f"Text: {row['text'][:100]}...")
    print("-" * 80)
```

## Manual Download and Ingestion

For manual control:

### Step 1: Get the Library ID

```bash
# Use the Context7 API directly
curl -X POST https://mcp.context7.com/mcp \
  -H "Content-Type: application/json" \
  -d '{
    "jsonrpc": "2.0",
    "id": 1,
    "method": "tools/call",
    "params": {
      "name": "resolve-library-id",
      "arguments": {
        "libraryName": "React",
        "query": "hooks and state management"
      }
    }
  }'
```

Parse the response to extract the library ID (e.g., `/facebook/react`).

### Step 2: Download Documentation

```bash
# Download using the library ID
curl https://context7.com/facebook/react/llms.txt \
  -o tests/data/react.md
```

### Step 3: Ingest into LanceDB

```bash
# Ingest with markdown chunking
uv run lance-db-example ingest tests/data/react.md \
  --library react \
  --chunking-strategy markdown-h3

# Or with character-based chunking
uv run lance-db-example ingest tests/data/react.md \
  --library react \
  --chunking-strategy character \
  --chunk-size 4000 \
  --overlap 400
```

## Using an API Key

For higher rate limits, use a Context7 API key:

```bash
# Set the API key
export CONTEXT7_API_KEY="your-api-key"

# Fetch library (automatically uses the key)
just fetch-library "React"
```

Get your API key from [context7.com/dashboard](https://context7.com/dashboard).

## View Database Contents

### List All Libraries

```bash
# Open SQL shell
just shell

# Query in DuckDB
SELECT library, COUNT(*) as chunks
FROM docs
GROUP BY library
ORDER BY chunks DESC;
```

**Example output:**
```
┌──────────┬────────┐
│ library  │ chunks │
├──────────┼────────┤
│ react    │ 142    │
│ next-js  │ 98     │
│ daisyui  │ 67     │
└──────────┴────────┘
```

### View Statistics

```bash
uv run lance-db-example stats
```

**Example output:**
```
📊 Database Statistics
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Database: ./lancedb_data
Table: documents
Total chunks: 307
Total libraries: 3

Libraries:
  - react: 142 chunks
  - next-js: 98 chunks
  - daisyui: 67 chunks
```

## Update Existing Libraries

Refresh documentation:

```bash
# Remove old database (WARNING: deletes all data)
just clean-db

# Re-fetch libraries
just fetch-library "React"
just fetch-library "Next.js"
```

**For selective updates:**

```bash
# Delete just the files
rm tests/data/react.md

# Re-download
just fetch-library "React"
```

Ingestion appends to the existing database rather than replacing it.

## Complete Example Workflow

```bash
# 1. Set up the database with multiple libraries
cd scripts/lancedb
just fetch-library "React" "hooks and components"
just fetch-library "Next.js" "app router and server actions"
just fetch-library "Tailwind CSS" "utility classes and styling"

# 2. Verify what was added
just stats

# 3. Search across all libraries
just search "how to style components" --limit 5

# 4. Explore with SQL
just shell
# Run: SELECT library, text FROM docs WHERE text LIKE '%component%' LIMIT 10;
```

## Troubleshooting

### Library Not Found

**Problem:**
```
❌ No libraries found in response
```

**Solutions:**
1. Check spelling of library name
2. Try adding a query hint: `just fetch-library "LibraryName" "specific query"`
3. Use Context7 web interface to verify the library exists

### Download Failed

**Problem:**
```
❌ Failed to download: HTTP Error 404
```

**Causes:**
- Invalid library ID
- Library removed from Context7
- Network connectivity issues

**Solution:**
```bash
# Verify the URL manually
curl -I https://context7.com/facebook/react/llms.txt
```

### Rate Limiting

**Problem:**
```
❌ API request failed: HTTP Error 429
```

**Solution:**

Use an API key:
```bash
export CONTEXT7_API_KEY="your-api-key"
just fetch-library "React"
```

### Duplicate Libraries

**Problem:** Multiple libraries with the same content

**Cause:** Running `fetch-library` multiple times appends data

**Solution:**
```bash
# Clean and rebuild
just clean-db
just fetch-library "React"
```

## Batch Download

Download multiple libraries with a script:

```bash
#!/bin/bash

LIBRARIES=(
  "React"
  "Vue.js"
  "Angular"
  "Svelte"
  "Next.js"
  "Nuxt.js"
  "SvelteKit"
)

for lib in "${LIBRARIES[@]}"; do
  echo "Fetching $lib..."
  just fetch-library "$lib"
  echo ""
done

echo "✅ All libraries downloaded!"
just stats
```

Save as `fetch-all.sh` and run:

```bash
chmod +x fetch-all.sh
./fetch-all.sh
```

## Integrate with RAG Systems

Build retrieval-augmented generation with your multi-library LanceDB:

```python
import lancedb
from openai import OpenAI
from sentence_transformers import SentenceTransformer

# Initialize
db = lancedb.connect("./lancedb_data")
table = db.open_table("documentation")
model = SentenceTransformer('all-MiniLM-L6-v2')
client = OpenAI()

def answer_question(question: str, library_filter: str = None):
    # 1. Embed the question
    query_vector = model.encode([question])[0]

    # 2. Search for relevant chunks
    search = table.search(query_vector).limit(5)

    if library_filter:
        search = search.where(f"library = '{library_filter}'")

    results = search.to_pandas()

    # 3. Build context from results
    context = "\n\n".join(results['text'].tolist())

    # 4. Generate answer with LLM
    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": f"Answer using this documentation:\n\n{context}"},
            {"role": "user", "content": question}
        ]
    )

    return response.choices[0].message.content

# Example usage
answer = answer_question(
    "How do I create a server component in Next.js?",
    library_filter="next-js"
)
print(answer)
```

## Best Practices

1. **Use specific queries** - Help Context7 rank results: `just fetch-library "React" "hooks and state"`
2. **Check what was selected** - Review the resolved library ID before ingestion
3. **Organize by library** - Use the `--library` flag to tag chunks
4. **Monitor database size** - Run `just stats` regularly
5. **Version documentation** - Save downloads to version control for reproducibility
6. **Use API keys** - Avoid rate limits with a Context7 API key
7. **Clean before rebuilding** - Use `just clean-db` to start fresh

## Summary

**Quick workflow:**
```bash
# Fetch → Search → Query
just fetch-library "React"
just search "useState hook"
just shell  # Explore with SQL
```

**Key points:**
- Context7 provides pre-processed documentation as `llms.txt`
- The script resolves libraries by name and query
- Markdown headers define chunk boundaries
- One database holds multiple libraries
- Search across all libraries or filter by one

**Next steps:**
- Build a comprehensive knowledge base with multiple libraries
- Integrate with RAG systems for AI-powered documentation assistance
- Use SQL to explore and analyze your documentation corpus
