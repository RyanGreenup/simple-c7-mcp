# Context7 + LanceDB Integration Guide

## Overview

This guide explains how to integrate Context7 MCP with LanceDB for storing and searching library documentation with semantic vector search.

## Architecture

```
┌─────────────────┐
│  Context7 MCP   │  ← Fetch up-to-date docs
│  (Remote API)   │
└────────┬────────┘
         │
         │ 1. resolve-library-id
         │ 2. query-docs
         ↓
┌─────────────────┐
│ Integration     │  ← Chunk & embed
│ Script          │
└────────┬────────┘
         │
         │ Store with metadata
         ↓
┌─────────────────┐
│   LanceDB       │  ← Vector similarity search
│   (Local DB)    │
└─────────────────┘
```

## Recommended Schema

### Core Fields

```python
{
    # Identity
    'id': str,                      # Unique chunk ID
    'chunk_index': int,             # Order within document

    # Content
    'text': str,                    # Documentation text
    'vector': List[float],          # Embedding (384-dim)

    # Library Metadata (from Context7)
    'library_id': str,              # e.g., "/vercel/next.js"
    'library_name': str,            # e.g., "Next.js"
    'library_description': str,     # Short description

    # Quality Metrics (from Context7)
    'source_reputation': str,       # High/Medium/Low
    'benchmark_score': float,       # 0-100 quality score
    'snippet_count': int,           # Available snippets

    # Source Info
    'source_url': str,              # GitHub/docs URL
    'section_title': str,           # Section header

    # Content Metadata
    'has_code': bool,               # Contains code?
    'code_languages': str,          # "typescript,javascript"

    # Timestamps
    'ingested_at': str,             # ISO timestamp
}
```

See `LANCEDB_SCHEMA.md` for complete schema details and design patterns.

## Files

### 1. `context7_lancedb_integration.py`

**Purpose:** Complete integration script for ingesting and searching Context7 docs in LanceDB

**Commands:**
```bash
# Ingest documentation
./context7_lancedb_integration.py ingest "React" "How to use hooks"

# Search documentation
./context7_lancedb_integration.py search "useState examples"

# Search with library filter
./context7_lancedb_integration.py search "API routes" --library "/vercel/next.js"

# Show statistics
./context7_lancedb_integration.py stats
```

**Features:**
- ✅ Fetches from Context7 MCP
- ✅ Extracts library metadata (scores, reputation, etc.)
- ✅ Intelligent markdown chunking by sections
- ✅ Generates embeddings with sentence-transformers
- ✅ Stores in LanceDB with full metadata
- ✅ Vector similarity search with filtering

### 2. `LANCEDB_SCHEMA.md`

**Purpose:** Complete schema documentation

**Contents:**
- Recommended schema (core + minimal versions)
- Table design patterns (single table vs per-library)
- Indexing strategies
- Query examples with filters
- Integration workflow
- Storage considerations
- Chunking strategies

### 3. Context7 Test Suite (in `scripts/context7-api/`)

**Purpose:** Testing and exploring the Context7 MCP API

**Files:**
- `context7_test.py` - CLI for testing MCP endpoints
- `justfile` - Command runner
- Documentation files

## Workflow

### 1. Ingest Documentation

```bash
# Fetch React documentation on hooks
./context7_lancedb_integration.py ingest "React" "How to use hooks"
```

**What happens:**
1. Calls `resolve-library-id` → Gets `/websites/react_dev` + metadata
2. Calls `query-docs` → Gets markdown documentation
3. Chunks by markdown sections (### headers)
4. Extracts metadata (URLs, code detection, etc.)
5. Generates embeddings (384-dim vectors)
6. Stores in LanceDB with all metadata

**Output:**
```
📚 Ingesting React documentation...

1️⃣  Resolving library ID...
✓ Resolved to: /websites/react_dev
  Name: React
  Score: 89.2, Snippets: 5574

2️⃣  Querying documentation...
✓ Retrieved 15234 characters of documentation

3️⃣  Chunking documentation...
✓ Created 8 chunks

4️⃣  Generating embeddings...
✓ Generated 8 embeddings (dim=384)

5️⃣  Preparing data...
6️⃣  Storing in LanceDB...
✓ Created table 'documentation' with 8 chunks

🎉 Ingestion complete!
```

### 2. Search Documentation

```bash
# Semantic search
./context7_lancedb_integration.py search "How to update component state"
```

**What happens:**
1. Generates query embedding
2. Vector similarity search in LanceDB
3. Returns top N most similar chunks
4. Displays with metadata (library, score, source URL, etc.)

**Output:**
```
🔍 Searching: How to update component state

✓ Found 5 results

╭─ [1] React - Adding State to a Component ─────╮
│ Text:                                          │
│ ### Adding State to a React Component with    │
│ useState                                       │
│                                                │
│ Source: https://react.dev/learn/state          │
│                                                │
│ Library: /websites/react_dev                   │
│ Score: 89.2 | Reputation: High                 │
│ Source: https://react.dev/learn/state          │
│ Code: Yes (javascript,typescript)              │
╰────────────────────────────────────────────────╯
```

### 3. Library-Specific Search

```bash
# Search only Next.js docs
./context7_lancedb_integration.py search "API routes" \
  --library "/vercel/next.js"
```

### 4. View Statistics

```bash
./context7_lancedb_integration.py stats
```

**Output:**
```
📊 Database Statistics

┌─────────────────────┬────────┐
│ Metric              │ Value  │
├─────────────────────┼────────┤
│ Total Chunks        │ 15     │
│ Total Libraries     │ 2      │
│ Avg Chunk Length    │ 823    │
│ Chunks with Code    │ 12     │
│ Avg Benchmark Score │ 91.1   │
└─────────────────────┴────────┘

📚 Libraries

┌────────┬────────┬───────┬────────────┐
│ Library│ Chunks │ Score │ Reputation │
├────────┼────────┼───────┼────────────┤
│ React  │ 8      │ 89.2  │ High       │
│ Next.js│ 7      │ 92.9  │ High       │
└────────┴────────┴───────┴────────────┘
```

## Schema Benefits

### 1. Quality-Aware Search

Combine semantic similarity with quality metrics:

```python
# Search high-quality sources only
results = table.search(query_vector)\
    .where("benchmark_score > 85 AND source_reputation = 'High'")\
    .limit(10)
```

### 2. Library Filtering

Search specific libraries or versions:

```python
# Next.js only
.where("library_id = '/vercel/next.js'")

# Multiple libraries
.where("library_id IN ('/websites/react_dev', '/vercel/next.js')")
```

### 3. Content Type Filtering

Find specific content types:

```python
# Code examples only
.where("has_code = true")

# TypeScript examples
.where("code_languages LIKE '%typescript%'")
```

### 4. Source Attribution

Always know the source:

```python
for result in results:
    print(f"Source: {result['source_url']}")
    print(f"Library: {result['library_name']} (score: {result['benchmark_score']})")
    print(f"Reputation: {result['source_reputation']}")
```

## Advanced Usage

### Multi-Library Documentation Collection

```bash
# Ingest documentation for multiple libraries
./context7_lancedb_integration.py ingest "React" "state management"
./context7_lancedb_integration.py ingest "Next.js" "routing and API routes"
./context7_lancedb_integration.py ingest "Supabase" "authentication and queries"
./context7_lancedb_integration.py ingest "Express.js" "middleware and routing"

# Now search across all libraries
./context7_lancedb_integration.py search "How to handle authentication"
```

### Version-Specific Documentation

```bash
# Ingest specific version (if needed, modify script to accept version)
# Context7 supports version-specific queries like /vercel/next.js/v14.3.0
```

### Custom Chunking Strategies

The script uses markdown section chunking by default. For custom chunking:

1. **Current**: Splits by `###` headers and `---` separators
2. **Alternative**: Modify `chunk_markdown_by_sections()` function
3. **LanceDB Project**: Use the chunking utilities from `scripts/lancedb/`

```python
from lance_db_example.chunking import (
    chunk_markdown_by_level3_headers,
    chunk_by_paragraphs,
    chunk_by_sentences,
)

# Use LangChain-based markdown splitting
chunks = chunk_markdown_by_level3_headers(doc_text)

# Or paragraph-based
chunks = chunk_by_paragraphs(doc_text, min_length=200)
```

## Integration with Existing LanceDB Project

You can integrate this with the existing `scripts/lancedb/` project:

### Option 1: Extend the CLI

Add Context7 commands to `scripts/lancedb/lance_db_example/cli.py`:

```python
from .ingest import app as ingest_app

# Add Context7 subcommand
@ingest_app.command()
def from_context7(library: str, query: str):
    """Ingest from Context7 MCP."""
    # Use the integration script logic
    pass
```

### Option 2: Use as Separate Tool

Keep the integration script standalone and use it to populate the LanceDB database that your main project reads from.

## Performance Optimization

### 1. Batch Ingestion

Modify the script to fetch multiple libraries in one run:

```python
libraries = ["React", "Next.js", "Vue", "Svelte"]
for lib in libraries:
    ingest_library(lib, "comprehensive documentation")
```

### 2. Incremental Updates

Track what's already ingested and only fetch new/updated docs:

```python
# Check if library exists
existing = table.to_pandas()
if library_id not in existing['library_id'].values:
    ingest_library(library_id, query)
```

### 3. Caching

Add caching layer for frequently accessed docs:

```python
import json
from pathlib import Path

cache_dir = Path(".cache/context7")
cache_file = cache_dir / f"{library_id}.json"

if cache_file.exists():
    # Load from cache
    pass
else:
    # Fetch from Context7 and cache
    pass
```

## Comparison: LanceDB Schema vs Context7 API

| Aspect | Context7 API | LanceDB Storage |
|--------|--------------|-----------------|
| **Access** | Remote HTTP calls | Local file access |
| **Latency** | ~1-2 seconds | Milliseconds |
| **Offline** | ❌ Requires internet | ✅ Works offline |
| **Search** | Query-based | Vector similarity |
| **Filtering** | Limited | Rich (SQL-like) |
| **Cost** | API rate limits | Storage space only |
| **Freshness** | Always current | Updated on ingest |

### When to Use Each

**Use Context7 API directly:**
- Need latest documentation
- One-off queries
- Don't want to manage storage

**Use LanceDB:**
- Frequent searches
- Offline access needed
- Want to combine multiple sources
- Need advanced filtering
- Want to cache commonly-used docs

**Best of Both:**
- Periodically refresh LanceDB from Context7
- Use LanceDB for day-to-day searches
- Fall back to Context7 for new libraries

## Next Steps

1. **Try the integration:**
   ```bash
   ./context7_lancedb_integration.py ingest "React" "hooks and state"
   ./context7_lancedb_integration.py search "useState"
   ```

2. **Customize the schema:**
   - Add fields specific to your use case
   - See `LANCEDB_SCHEMA.md` for ideas

3. **Build your documentation collection:**
   - Ingest your most-used libraries
   - Set up periodic refresh schedule

4. **Integrate with your workflow:**
   - Use in your editor/IDE
   - Add to your documentation search tool
   - Combine with local docs

## Files Reference

```
c7-attempt/
├── context7_lancedb_integration.py  # Main integration script
├── LANCEDB_SCHEMA.md                # Schema documentation
├── INTEGRATION_GUIDE.md             # This file
│
└── scripts/
    ├── context7-api/                # Context7 testing suite
    │   ├── context7_test.py
    │   ├── justfile
    │   └── *.md
    │
    └── lancedb/                     # LanceDB project with chunking
        ├── lance_db_example/
        │   ├── chunking.py          # Chunking utilities
        │   └── ingest.py
        └── pyproject.toml
```

## Conclusion

The recommended schema stores all relevant Context7 metadata alongside document chunks, enabling:

✅ **Quality-aware search** - Filter by benchmark scores and reputation
✅ **Library-specific queries** - Search within specific libraries
✅ **Source attribution** - Always know where docs came from
✅ **Content type filtering** - Find code examples, guides, etc.
✅ **Offline access** - No API calls needed after ingestion
✅ **Fast semantic search** - Vector similarity in milliseconds

This provides the best of both worlds: Context7's fresh, high-quality documentation combined with LanceDB's fast local search capabilities.
