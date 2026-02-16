# LanceDB Schema for Context7 Documentation

## Recommended Schema

Based on the Context7 MCP responses, here's an optimal schema for storing and searching library documentation:

### Core Schema

```python
import pandas as pd
import lancedb
from typing import List, Optional, Dict, Any

# Schema definition
schema = {
    # Unique identifiers
    'id': str,                      # Unique chunk ID (e.g., "react_useState_001")
    'chunk_index': int,             # Order within document (0, 1, 2...)

    # Content
    'text': str,                    # Documentation text/code example
    'vector': List[float],          # Embedding vector (384-dim for all-MiniLM-L6-v2)

    # Library metadata (from resolve-library-id)
    'library_id': str,              # Context7 ID (e.g., "/vercel/next.js")
    'library_name': str,            # Display name (e.g., "Next.js")
    'library_description': str,     # Short description
    'library_version': Optional[str], # Version if specified (e.g., "v14.3.0")

    # Quality metrics
    'source_reputation': str,       # "High", "Medium", "Low", "Unknown"
    'benchmark_score': float,       # 0-100 quality score
    'snippet_count': int,           # Total snippets available for this library

    # Source tracking
    'source_url': str,              # GitHub URL or documentation link
    'source_type': str,             # "github", "website", "docs"
    'section_title': str,           # Section/header title

    # Content metadata
    'has_code': bool,               # Whether chunk contains code
    'code_languages': List[str],    # e.g., ["typescript", "javascript"]
    'content_type': str,            # "example", "reference", "guide", "api"

    # Timestamps
    'ingested_at': str,             # ISO timestamp of ingestion
    'queried_at': str,              # When this was fetched from Context7
}
```

## Example DataFrame Structure

```python
data = pd.DataFrame({
    'id': ['nextjs_api_001', 'nextjs_api_002'],
    'chunk_index': [0, 1],
    'text': [
        '### Create Basic API Route Handler...',
        '### Route Handlers > Overview...'
    ],
    'vector': [embedding_1, embedding_2],  # 384-dim vectors

    # Library info
    'library_id': ['/vercel/next.js', '/vercel/next.js'],
    'library_name': ['Next.js', 'Next.js'],
    'library_description': ['Next.js enables you to create full-stack...', ...],
    'library_version': ['v14.3.0', 'v14.3.0'],

    # Quality
    'source_reputation': ['High', 'High'],
    'benchmark_score': [92.9, 92.9],
    'snippet_count': [2043, 2043],

    # Source
    'source_url': [
        'https://github.com/vercel/next.js/blob/canary/docs/02-pages/...',
        'https://github.com/vercel/next.js/blob/canary/docs/01-app/...'
    ],
    'source_type': ['github', 'github'],
    'section_title': ['Create Basic API Route Handler', 'Route Handlers > Overview'],

    # Content
    'has_code': [True, True],
    'code_languages': [['typescript', 'javascript'], ['typescript']],
    'content_type': ['example', 'reference'],

    # Timestamps
    'ingested_at': ['2026-02-16T02:47:00Z', '2026-02-16T02:47:00Z'],
    'queried_at': ['2026-02-16T02:47:02Z', '2026-02-16T02:47:02Z'],
})
```

## Minimal Schema (Simplified)

If you want to start simple and expand later:

```python
minimal_schema = {
    'id': str,                      # Unique ID
    'text': str,                    # Documentation content
    'vector': List[float],          # Embedding vector
    'library_id': str,              # Context7 library ID
    'library_name': str,            # Display name
    'source_url': str,              # Source link
    'benchmark_score': float,       # Quality metric
}
```

## Table Design Patterns

### Pattern 1: Single Table (Recommended for Most Cases)

Store all documentation in one table with library_id for filtering:

```python
db = lancedb.connect("context7_docs.lance")
table = db.create_table("documentation", data)

# Search within a specific library
results = table.search(query_vector)\
    .where("library_id = '/vercel/next.js'")\
    .limit(5)\
    .to_pandas()
```

### Pattern 2: Table Per Library

Separate table for each library (good for very large collections):

```python
# Create table for each library
table_name = library_id.replace('/', '_')  # "vercel_next.js"
db.create_table(table_name, data)

# Search
table = db.open_table("vercel_next_js")
results = table.search(query_vector).limit(5).to_pandas()
```

### Pattern 3: Hybrid (Library Metadata + Documentation Tables)

Two tables: one for library metadata, one for chunks:

```python
# Libraries table
libraries = pd.DataFrame({
    'library_id': ['/vercel/next.js'],
    'name': ['Next.js'],
    'description': ['...'],
    'benchmark_score': [92.9],
    'snippet_count': [2043],
    'source_reputation': ['High'],
})

# Documentation chunks table (references library_id)
chunks = pd.DataFrame({
    'id': ['chunk_001'],
    'library_id': ['/vercel/next.js'],  # Foreign key
    'text': ['...'],
    'vector': [embedding],
    'source_url': ['...'],
})
```

## Indexing Strategies

### Vector Index
```python
# Create ANN index for fast similarity search
table.create_index(
    metric="cosine",      # or "L2", "dot"
    num_partitions=256,   # Adjust based on dataset size
    num_sub_vectors=96    # For product quantization
)
```

### Scalar Indexes
```python
# Index for filtering by library
table.create_scalar_index("library_id")

# Index for quality filtering
table.create_scalar_index("benchmark_score")

# Index for reputation filtering
table.create_scalar_index("source_reputation")
```

## Query Examples

### 1. Search with Library Filter
```python
# Search Next.js docs only
results = table.search(query_vector)\
    .where("library_id = '/vercel/next.js'")\
    .limit(10)\
    .to_pandas()
```

### 2. Quality-Filtered Search
```python
# Only high-quality sources with good scores
results = table.search(query_vector)\
    .where("source_reputation = 'High' AND benchmark_score > 85.0")\
    .limit(10)\
    .to_pandas()
```

### 3. Multi-Library Search
```python
# Search across React and Next.js
results = table.search(query_vector)\
    .where("library_id IN ('/websites/react_dev', '/vercel/next.js')")\
    .limit(10)\
    .to_pandas()
```

### 4. Code-Only Search
```python
# Find code examples only
results = table.search(query_vector)\
    .where("has_code = true AND content_type = 'example'")\
    .limit(10)\
    .to_pandas()
```

## Integration with Context7 Workflow

### Complete Pipeline

```python
from context7_test import make_mcp_request
import lancedb
from sentence_transformers import SentenceTransformer

# 1. Resolve library
resolve_result = make_mcp_request("tools/call", {
    "name": "resolve-library-id",
    "arguments": {
        "libraryName": "React",
        "query": "state management"
    }
})

# Extract library info
library_id = "/websites/react_dev"
library_name = "React"
benchmark_score = 89.2

# 2. Query documentation
query_result = make_mcp_request("tools/call", {
    "name": "query-docs",
    "arguments": {
        "libraryId": library_id,
        "query": "How to use useState"
    }
})

# Extract documentation text
doc_text = query_result["result"]["content"][0]["text"]

# 3. Chunk the documentation
from lance_db_example.chunking import chunk_markdown_by_level3_headers
chunks = chunk_markdown_by_level3_headers(doc_text)

# 4. Generate embeddings
model = SentenceTransformer("all-MiniLM-L6-v2")
embeddings = model.encode(chunks)

# 5. Prepare data for LanceDB
import pandas as pd
from datetime import datetime

data = pd.DataFrame({
    'id': [f"{library_id.replace('/', '_')}_{i}" for i in range(len(chunks))],
    'chunk_index': list(range(len(chunks))),
    'text': chunks,
    'vector': embeddings.tolist(),
    'library_id': [library_id] * len(chunks),
    'library_name': [library_name] * len(chunks),
    'benchmark_score': [benchmark_score] * len(chunks),
    'ingested_at': [datetime.utcnow().isoformat()] * len(chunks),
})

# 6. Store in LanceDB
db = lancedb.connect("context7_docs.lance")
if "documentation" in db.table_names():
    table = db.open_table("documentation")
    table.add(data)  # Append to existing
else:
    table = db.create_table("documentation", data)  # Create new

# 7. Search
query_embedding = model.encode(["How to update state"])[0]
results = table.search(query_embedding)\
    .where(f"library_id = '{library_id}'")\
    .limit(5)\
    .to_pandas()

print(results[['text', 'library_name', 'benchmark_score']])
```

## Chunking Strategy for Context7 Docs

### Recommended: Markdown Header Splitting

Context7 returns markdown-formatted documentation with clear section headers:

```python
from lance_db_example.chunking import chunk_markdown_by_level3_headers

# Context7 docs use ### for sections
doc_text = query_result["result"]["content"][0]["text"]
chunks = chunk_markdown_by_level3_headers(doc_text)

# Each chunk is one complete section/example
# Perfect for semantic search!
```

### Alternative: Paragraph-Based

For very long sections:

```python
from lance_db_example.chunking import chunk_by_paragraphs

chunks = chunk_by_paragraphs(doc_text, min_length=200, max_length=1000)
```

## Schema Benefits

### 1. Library-Aware Search
Filter by specific libraries or versions:
```python
.where("library_id = '/vercel/next.js' AND library_version = 'v14.3.0'")
```

### 2. Quality Ranking
Combine semantic similarity with quality metrics:
```python
results = table.search(query_vector).limit(100).to_pandas()
results['score'] = results['_distance'] * (results['benchmark_score'] / 100)
results = results.sort_values('score').head(10)
```

### 3. Source Attribution
Always know where documentation came from:
```python
print(f"Source: {result['source_url']}")
print(f"Library: {result['library_name']} (score: {result['benchmark_score']})")
```

### 4. Multi-Modal Filtering
Find high-quality code examples:
```python
.where("has_code = true AND benchmark_score > 90 AND source_reputation = 'High'")
```

## Storage Considerations

### Disk Space Estimates

For 100 libraries with average:
- 2000 chunks per library
- 500 chars per chunk
- 384-dim vectors (float32)

```
Text: 200,000 chunks × 500 bytes = 100 MB
Vectors: 200,000 × 384 × 4 bytes = 307 MB
Metadata: ~100 MB
Total: ~500 MB
```

Very manageable for local development!

### Scaling Tips

1. **Use compression**: LanceDB uses Arrow columnar format (efficient)
2. **Index selectively**: Only create indexes you'll use
3. **Prune old data**: Keep only recent/relevant versions
4. **Shard by library**: For 1000+ libraries, use table-per-library pattern

## Next Steps

1. **Start minimal**: Use the simplified schema first
2. **Add metadata**: Expand as you discover what filters you need
3. **Optimize indexes**: Profile your queries and add indexes accordingly
4. **Monitor quality**: Track which sources give best results

## Example CLI Extension

Extend the lance-db-example CLI to ingest from Context7:

```python
@app.command()
def ingest_from_context7(
    library_name: str,
    query: str,
    db_path: Path = typer.Option("context7_docs.lance"),
):
    """Ingest documentation from Context7 MCP."""
    # Resolve library
    # Query docs
    # Chunk with markdown headers
    # Generate embeddings
    # Store in LanceDB
    pass
```

Would you like me to implement this integration?
