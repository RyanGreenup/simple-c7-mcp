# LanceDB Schema for Context7 - Quick Summary

## TL;DR - Recommended Schema

```python
{
    # Core
    'id': str,                      # Unique chunk ID
    'text': str,                    # Documentation content
    'vector': List[float],          # Embedding vector (384-dim)

    # Context7 Metadata
    'library_id': str,              # "/vercel/next.js"
    'library_name': str,            # "Next.js"
    'library_description': str,     # Description
    'benchmark_score': float,       # 0-100 quality score
    'source_reputation': str,       # "High", "Medium", "Low"
    'snippet_count': int,           # Total available snippets

    # Source & Content
    'source_url': str,              # GitHub/docs URL
    'section_title': str,           # Section header
    'has_code': bool,               # Contains code?
    'code_languages': str,          # "typescript,javascript"

    # Tracking
    'chunk_index': int,             # Order in document
    'ingested_at': str,             # ISO timestamp
}
```

## Why This Schema?

### Context7 Provides Rich Metadata

When you call Context7 MCP:

**`resolve-library-id` returns:**
- ✅ Library ID (e.g., `/vercel/next.js`)
- ✅ Benchmark Score (0-100 quality metric)
- ✅ Source Reputation (High/Medium/Low)
- ✅ Snippet Count (available examples)
- ✅ Description

**`query-docs` returns:**
- ✅ Markdown-formatted documentation
- ✅ Code examples with language tags
- ✅ Source URLs (GitHub links)
- ✅ Section structure (### headers)

**→ Store all of this in LanceDB for powerful filtering!**

## Key Benefits

### 1. Quality-Filtered Search
```python
# Only high-quality, reputable sources
table.search(vector).where(
    "benchmark_score > 85 AND source_reputation = 'High'"
)
```

### 2. Library-Specific Queries
```python
# Search just Next.js docs
table.search(vector).where("library_id = '/vercel/next.js'")
```

### 3. Content Type Filtering
```python
# Find TypeScript code examples
table.search(vector).where(
    "has_code = true AND code_languages LIKE '%typescript%'"
)
```

### 4. Source Attribution
Every result includes:
- Original source URL
- Library name and ID
- Quality metrics
- Code language info

## Three Schema Options

### Option 1: Full Schema (Recommended)
**Use when:** You want maximum filtering power

**Storage:** ~500 MB for 100 libraries (200K chunks)

**Advantages:**
- Rich filtering options
- Full source attribution
- Quality-aware ranking

### Option 2: Minimal Schema
```python
{
    'id': str,
    'text': str,
    'vector': List[float],
    'library_id': str,
    'library_name': str,
}
```

**Use when:** Starting simple, will expand later

**Storage:** ~350 MB for 100 libraries

**Advantages:**
- Simpler to manage
- Faster ingestion
- Still allows library filtering

### Option 3: Hybrid (Two Tables)
```python
# Table 1: library_metadata
{
    'library_id': str,
    'name': str,
    'benchmark_score': float,
    'snippet_count': int,
}

# Table 2: documentation_chunks
{
    'id': str,
    'text': str,
    'vector': List[float],
    'library_id': str,  # Foreign key
}
```

**Use when:** Very large collections (1000+ libraries)

**Advantages:**
- Normalized structure
- Easier library updates
- Slightly smaller storage

## Quick Start

### 1. Ingest Documentation
```bash
./context7_lancedb_integration.py ingest "React" "state and hooks"
```

Creates LanceDB table with:
- 8-12 chunks (one per section)
- Full Context7 metadata
- Vector embeddings
- Source URLs

### 2. Search
```bash
./context7_lancedb_integration.py search "How to use useState"
```

Returns:
- Semantically similar chunks
- Library name and score
- Source URLs
- Code detection

### 3. Filter by Library
```bash
./context7_lancedb_integration.py search "API routes" \
  --library "/vercel/next.js"
```

## Schema Mapping: Context7 → LanceDB

| Context7 Field | LanceDB Field | Type | Usage |
|----------------|---------------|------|-------|
| Library ID | `library_id` | str | Primary filter |
| Title | `library_name` | str | Display |
| Description | `library_description` | str | Context |
| Benchmark Score | `benchmark_score` | float | Quality ranking |
| Source Reputation | `source_reputation` | str | Trust filter |
| Code Snippets | `snippet_count` | int | Availability metric |
| Doc Text | `text` | str | Searchable content |
| Source URL | `source_url` | str | Attribution |
| (derived) | `has_code` | bool | Content filter |
| (derived) | `code_languages` | str | Language filter |
| (generated) | `vector` | List[float] | Semantic search |

## Chunking Strategy

### Recommended: Markdown Header Splitting

Context7 returns markdown with clear structure:
```
### Example 1
Content...

### Example 2
Content...
```

**Split by `###` headers** - One chunk per example/section

**Why?**
- ✅ Semantic boundaries (each section is self-contained)
- ✅ Preserves code examples intact
- ✅ Maintains source URL associations
- ✅ Perfect size for embeddings (usually 300-1000 chars)

**Implementation:**
```python
from lance_db_example.chunking import chunk_markdown_by_level3_headers
chunks = chunk_markdown_by_level3_headers(doc_text)
```

## Example Queries

### Find High-Quality TypeScript Examples
```python
results = table.search(query_vector)\
    .where("has_code = true")\
    .where("code_languages LIKE '%typescript%'")\
    .where("benchmark_score > 90")\
    .limit(5)
```

### Search Multiple Libraries
```python
results = table.search(query_vector)\
    .where("library_id IN ('/websites/react_dev', '/vercel/next.js')")\
    .limit(10)
```

### Quality-Ranked Results
```python
# Combine similarity with quality
results = table.search(query_vector).limit(100).to_pandas()
results['combined_score'] = (
    (1 - results['_distance']) * 0.7 +  # 70% similarity
    (results['benchmark_score'] / 100) * 0.3  # 30% quality
)
results = results.sort_values('combined_score', ascending=False).head(10)
```

## Files Provided

1. **`LANCEDB_SCHEMA.md`** - Complete schema documentation
   - Multiple schema options
   - Design patterns
   - Indexing strategies
   - Storage considerations

2. **`context7_lancedb_integration.py`** - Working implementation
   - Ingest from Context7
   - Search with filters
   - Statistics display
   - Full metadata extraction

3. **`INTEGRATION_GUIDE.md`** - Usage guide
   - Workflow examples
   - Advanced usage
   - Performance tips
   - Integration patterns

## Decision Matrix

Choose your schema based on:

| Requirement | Recommendation |
|-------------|----------------|
| Maximum filtering power | Full schema |
| Simple & expandable | Minimal schema |
| Very large collections (1000+ libs) | Hybrid (2 tables) |
| Just getting started | Minimal → expand later |
| Production system | Full schema |

## Bottom Line

**The full schema is recommended because:**

1. **Context7 already provides the metadata** - might as well store it
2. **Storage is cheap** - ~500 MB for 100 libraries is nothing
3. **Filtering is powerful** - quality + library + content type filters
4. **Source attribution** - always know where docs came from
5. **Future-proof** - have the data when you need it

**Start with the integration script** - it implements the full schema and handles all the extraction automatically.

```bash
# One command to ingest with full metadata
./context7_lancedb_integration.py ingest "React" "comprehensive guide"
```

Done! 🎉
