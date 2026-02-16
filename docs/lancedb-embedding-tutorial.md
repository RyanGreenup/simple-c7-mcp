# LanceDB Document Embedding Tutorial

Embed documents into LanceDB for semantic search.

## What is LanceDB?

LanceDB stores document chunks alongside their embeddings (numerical representations of text). You query with natural language. LanceDB finds the most relevant chunks based on meaning, not keywords.

**Use cases:**
- Search technical documentation
- Build RAG (Retrieval-Augmented Generation) systems
- Create semantic knowledge bases
- Power AI assistants with custom knowledge

## Prerequisites

```bash
# Install uv (Python package manager)
curl -LsSf https://astral.sh/uv/install.sh | sh

# Clone or navigate to the lancedb directory
cd scripts/lancedb

# Install dependencies
uv sync
```

**Dependencies installed:**
- `lancedb` - Vector database
- `sentence-transformers` - Embedding models
- `langchain-text-splitters` - Smart text chunking
- `typer` + `rich` - CLI interface

## Quick Start: 3 Commands

```bash
# 1. Ingest a document
uv run lance-db-example ingest sample_document.txt

# 2. Search semantically
uv run lance-db-example search "machine learning"

# 3. View what's stored
uv run lance-db-example stats
```

## The Complete Workflow

### Step 1: Prepare Your Document

Any text file works:
- Markdown documentation (`.md`)
- Plain text (`.txt`)
- Code files with comments (`.py`, `.js`)
- API documentation
- Knowledge base articles

Example `my_docs.md`:
```markdown
### Introduction to Neural Networks

Neural networks are computing systems inspired by biological neural networks.
They learn patterns from data through training.

### Types of Neural Networks

1. Feedforward Networks - Data flows in one direction
2. Convolutional Networks - Excel at image processing
3. Recurrent Networks - Handle sequential data

### Training Process

Training involves adjusting weights to minimize error...
```

### Step 2: Chunk the Document

Break documents into chunks before you embed them. **Chunk size matters:**

**Recommended: 1000 tokens (~750-800 words)**
- Balances context and precision
- Works well with most embedding models
- Typical paragraph or section length
- Good for technical documentation

**Character-based estimation:**
- 1000 tokens ≈ 4000-5000 characters
- English: ~4-5 characters per token
- Code: ~3-4 characters per token

#### Strategy 1: Character-Based

Chunk by character count with overlap:

```bash
# Chunk into ~1000-token pieces (4000 chars) with 400-char overlap
uv run lance-db-example ingest my_docs.md \
  --chunking-strategy character \
  --chunk-size 4000 \
  --overlap 400
```

**Pros:**
- Predictable chunk sizes
- Works for any text type
- Simple to configure

**Cons:**
- May split sentences or code blocks
- Ignores document structure
- Can break semantic units

#### Strategy 2: Markdown Headers (Recommended)

Split by markdown headers to preserve semantic structure:

```bash
# Chunk by ### headers (default for markdown files)
uv run lance-db-example ingest my_docs.md \
  --chunking-strategy markdown-h3 \
  --library my-knowledge-base
```

**How it works:**
1. LangChain parses the markdown structure
2. The tool splits at each `###` heading
3. Each chunk contains a complete section: header, content, and code
4. Metadata (header hierarchy) is preserved

**Pros:**
- ✅ Preserves semantic structure
- ✅ Keeps code blocks intact
- ✅ Natural boundaries
- ✅ Better search relevance
- ✅ Maintains context

**Cons:**
- Only works for markdown
- Variable chunk sizes
- Very long sections may need sub-chunking

**Example output:**
```
Chunk 1:
### Introduction to Neural Networks

Neural networks are computing systems inspired by...

Chunk 2:
### Types of Neural Networks

1. Feedforward Networks - Data flows in one direction
2. Convolutional Networks - Excel at image processing...
```

### Step 3: Generate Embeddings

Embeddings are vectors (arrays of numbers) that represent text. Similar meanings produce similar vectors.

The tool uses **sentence-transformers** with the `all-MiniLM-L6-v2` model:
- Produces 384-dimensional vectors
- Runs on CPU (no GPU required)
- Fast and accurate
- Industry standard

**Ingestion generates embeddings automatically.**

### Step 4: Store in LanceDB

```bash
# Basic ingestion
uv run lance-db-example ingest my_docs.md

# With options
uv run lance-db-example ingest my_docs.md \
  --db ./my_database \
  --table documentation \
  --library my-project
```

**LanceDB stores:**
```python
{
  "text": "### Introduction to Neural Networks\n\nNeural networks are...",
  "chunk_index": 0,
  "library": "my-project",
  "title": "my_docs.md",
  "vector": [0.123, -0.456, 0.789, ...]  # 384 dimensions
}
```

### Step 5: Search Semantically

```bash
# Basic search
uv run lance-db-example search "how do neural networks learn"

# With options
uv run lance-db-example search "image processing" \
  --table documentation \
  --limit 10
```

**How search works:**
1. The tool converts your query into an embedding vector
2. LanceDB finds the nearest vectors using cosine similarity
3. LanceDB returns ranked chunks with scores

**Example output:**
```
📊 Search Results for: "how do neural networks learn"
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Result 1 (Score: 0.87)
┌─────────────────────────────────────────────────────┐
│ ### Training Process                                │
│                                                     │
│ Training involves adjusting weights to minimize    │
│ error through backpropagation and gradient descent.│
└─────────────────────────────────────────────────────┘

Result 2 (Score: 0.82)
┌─────────────────────────────────────────────────────┐
│ ### Introduction to Neural Networks                 │
│                                                     │
│ Neural networks learn patterns from data through   │
│ training...                                         │
└─────────────────────────────────────────────────────┘
```

## Advanced Usage

### Chunk Markdown by Headings

API documentation and markdown files benefit from header-based chunking:

```python
from lance_db_example.chunking import chunk_markdown_by_level3_headers

# Read markdown file
with open("api_docs.md", "r") as f:
    markdown_text = f.read()

# Chunk by ### headers
chunks = chunk_markdown_by_level3_headers(markdown_text)

# Each chunk is a complete section
for i, chunk in enumerate(chunks):
    print(f"Chunk {i}: {len(chunk)} chars")
    print(chunk[:100])  # Preview
    print("-" * 80)
```

**Why ### (level 3) headers?**
- Most API docs use ### for individual methods/endpoints
- ## for major sections (too broad)
- #### for sub-details (too granular)
- ### hits the sweet spot for semantic units

**Full control:**
```python
from lance_db_example.chunking import chunk_by_markdown_headers

# Custom header levels
chunks = chunk_by_markdown_headers(
    text,
    headers_to_split_on=[
        ("##", "section"),
        ("###", "subsection"),
        ("####", "detail")
    ],
    strip_headers=False,  # Keep header text
    return_metadata=True  # Include header metadata
)

for chunk in chunks:
    print(f"Section: {chunk['metadata'].get('section', 'N/A')}")
    print(f"Subsection: {chunk['metadata'].get('subsection', 'N/A')}")
    print(f"Content: {chunk['content'][:100]}...")
```

### Character-Based Chunking

For plain text or when you need specific sizes:

```python
from lance_db_example.chunking import chunk_text

text = "Your long document text here..."

# Standard chunking (~1000 tokens = 4000 chars)
chunks = chunk_text(text, chunk_size=4000, overlap=400)

# Technical docs with code (larger chunks)
chunks = chunk_text(text, chunk_size=5000, overlap=500)

# Short-form content (smaller chunks)
chunks = chunk_text(text, chunk_size=2000, overlap=200)
```

**What overlap means:**
- Consecutive chunks share characters
- Shared characters maintain context across boundaries
- Use 10-20% of chunk_size
- Example: 4000-char chunks with 400-char overlap

### Token-Based Chunking

For precise token counts (when using transformer models):

```python
from lance_db_example.chunking import chunk_by_tokens

# Chunk by exact token count
chunks = chunk_by_tokens(
    text,
    max_tokens=1000,
    overlap_tokens=100,
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)
```

### Multiple Documents and Libraries

Organize documents by library/category:

```bash
# Ingest React documentation
uv run lance-db-example ingest react-docs.md \
  --library react \
  --table documentation

# Ingest Next.js documentation
uv run lance-db-example ingest nextjs-docs.md \
  --library nextjs \
  --table documentation

# Ingest Python documentation
uv run lance-db-example ingest python-docs.md \
  --library python \
  --table documentation

# Search across all libraries
uv run lance-db-example search "how to create components" \
  --table documentation
```

**Filter by library in code:**
```python
import lancedb

db = lancedb.connect("./lancedb_data")
table = db.open_table("documentation")

# Search only React docs
results = table.search(query_vector) \
    .where("library = 'react'") \
    .limit(5) \
    .to_pandas()
```

### Fetch and Ingest from Context7

Automatically fetch library docs and ingest:

```bash
# Fetch daisyUI docs and ingest
just fetch-library "daisyUI"

# Fetch React docs
just fetch-library "React" "hooks and state management"

# Fetch Next.js docs
just fetch-library "Next.js" "app router and server actions"
```

**The script:**
1. Calls Context7 API to resolve the library name
2. Downloads llms.txt documentation
3. Saves it to `tests/data/{library}.md`
4. Chunks by markdown headers
5. Ingests chunks into LanceDB

## Chunking Best Practices

### Choose Chunk Size by Use Case

| Use Case | Chunk Size | Strategy |
|----------|-----------|----------|
| API docs (methods) | 1000-1500 tokens | Markdown headers |
| Tutorial content | 800-1200 tokens | Markdown headers |
| Code with comments | 1500-2000 tokens | Character-based |
| Technical articles | 1000 tokens | Character-based |
| Short FAQs | 500-800 tokens | Character-based |
| Book chapters | 2000+ tokens | Paragraph-based |

### Token Budget Considerations

**Embedding models:**
- Most models: 512-token limit
- Modern models: 8192-token limit (e.g., text-embedding-3-large)
- **Stay under model limits!**

**Size guidelines:**
- **Too small** (< 500 tokens): Loses context, fragments meaning
- **Sweet spot** (800-1500 tokens): Balances context and precision
- **Too large** (> 2000 tokens): Dilutes relevance, slows search

**Use 1000 tokens for most cases:**
- Captures complete thoughts
- Fits in most embedding models
- Balances context and retrieval precision
- Works well with RAG systems

### Overlap Recommendations

| Chunk Size | Recommended Overlap |
|-----------|-------------------|
| 500 tokens (~2000 chars) | 50-100 tokens (~200-400 chars) |
| 1000 tokens (~4000 chars) | 100-200 tokens (~400-800 chars) |
| 2000 tokens (~8000 chars) | 200-400 tokens (~800-1600 chars) |

**Rule of thumb: 10-20% overlap**

## Database Management

### List Tables

```bash
uv run lance-db-example list-tables
```

### View Statistics

```bash
uv run lance-db-example stats --table documentation
```

### SQL Queries with DuckDB

Explore your LanceDB data with SQL:

```bash
# Open SQL shell
just shell

# Inside the shell, run queries:
SELECT COUNT(*) FROM docs;
SELECT library, COUNT(*) as chunks FROM docs GROUP BY library;
SELECT text, chunk_index FROM docs WHERE library = 'react' LIMIT 5;
```

### Clean Database

```bash
# Remove all data
just clean-db

# Or manually:
rm -rf ./lancedb_data
```

## Complete Example: End-to-End

```bash
# 1. Fetch library documentation from Context7
cd scripts/lancedb
just fetch-library "SolidJS"

# 2. Ingest with markdown chunking (automatic)
# (Already done by fetch-library)

# 3. Search for specific topics
uv run lance-db-example search "throw redirect" --limit 3

# 4. Check what was stored
uv run lance-db-example stats

# 5. Explore with SQL
just shell
# Run: SELECT text FROM docs WHERE text LIKE '%redirect%' LIMIT 3;
```

## Implementation Details

### Embedding Function

The tool uses sentence-transformers:

```python
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(chunks)
```

**Model specs:**
- Dimensions: 384
- Speed: ~500 sentences/second (CPU)
- Quality: Good for general-purpose semantic search
- Size: 90 MB

**Upgrade to better models:**
```python
# Larger, more accurate model
model = SentenceTransformer('all-mpnet-base-v2')  # 768 dims

# OpenAI embeddings (requires API key)
from openai import OpenAI
client = OpenAI()
response = client.embeddings.create(
    model="text-embedding-3-large",
    input=chunks
)
```

### LanceDB Schema

```python
{
  "text": str,           # The chunk text
  "vector": List[float], # Embedding (384 dimensions)
  "chunk_index": int,    # Position in original document
  "library": str,        # Library/category name
  "title": str          # Source document filename
}
```

### Search Algorithm

```python
# 1. Embed query
query_vector = model.encode([query])[0]

# 2. Vector similarity search
results = table.search(query_vector) \
    .limit(limit) \
    .to_pandas()

# 3. Results are ranked by cosine similarity
# Higher score = more relevant
```

## Troubleshooting

### Large Chunks Won't Embed

**Problem:** Chunks exceed model token limit

**Solution:** Reduce chunk size
```bash
uv run lance-db-example ingest docs.md \
  --chunk-size 3000 \  # Reduced from 5000
  --overlap 300
```

### Poor Search Results

**Problem:** Search returns irrelevant results

**Solutions:**
1. Use markdown chunking for structured docs
2. Increase chunk overlap for better context
3. Try different chunk sizes
4. Use more specific queries

### Markdown Chunking Not Working

**Problem:** Falls back to character chunking

**Solution:** Ensure LangChain is installed
```bash
uv add langchain-text-splitters
```

### Out of Memory

**Problem:** Too many documents or chunks

**Solutions:**
1. Process documents in batches
2. Use smaller chunk sizes
3. Reduce overlap
4. Use a smaller embedding model

## Next Steps

### Integrate with LLMs

Build RAG systems with LanceDB chunks:

```python
import lancedb
from openai import OpenAI

# 1. Search for relevant context
db = lancedb.connect("./lancedb_data")
table = db.open_table("documentation")
results = table.search(query_vector).limit(3).to_pandas()

# 2. Build context from top results
context = "\n\n".join(results['text'].tolist())

# 3. Generate answer with LLM
client = OpenAI()
response = client.chat.completions.create(
    model="gpt-4",
    messages=[
        {"role": "system", "content": "Answer using this context: " + context},
        {"role": "user", "content": "How do neural networks learn?"}
    ]
)
```

### Production Deployment

**Recommendations:**
1. Use GPU for faster embedding: `device="cuda"`
2. Batch process large document sets
3. Cache frequently accessed embeddings
4. Use better embedding models (768+ dims)
5. Add metadata filtering for multi-tenant systems
6. Monitor chunk size distribution
7. Implement incremental updates

### Advanced Chunking

**Combine strategies:**
```python
# 1. Split by markdown headers
sections = chunk_markdown_by_level3_headers(text)

# 2. Sub-chunk large sections by tokens
final_chunks = []
for section in sections:
    if len(section) > 5000:
        # Sub-chunk large sections
        sub_chunks = chunk_by_tokens(section, max_tokens=1000)
        final_chunks.extend(sub_chunks)
    else:
        final_chunks.append(section)
```

## Resources

- [LanceDB Documentation](https://lancedb.github.io/lancedb/)
- [Sentence Transformers](https://www.sbert.net/)
- [LangChain Text Splitters](https://python.langchain.com/docs/modules/data_connection/document_transformers/)
- [Context7 MCP](https://context7.com/) - Documentation source

## Summary

**Key points:**

1. **Chunk size matters**: Use ~1000 tokens (4000 chars) for most cases
2. **Strategy matters**: Use markdown headers for structured docs, character-based for plain text
3. **Overlap helps**: 10-20% overlap maintains context
4. **Semantic search works**: Search by meaning, not keywords
5. **LangChain is powerful**: Industry-standard chunking for markdown

**Basic workflow:**
```bash
ingest → chunk → embed → store → search → retrieve
```

**Start here:**
```bash
just demo-solid        # See markdown chunking in action
just fetch-library "React"  # Fetch and ingest real docs
just search "your query"    # Search semantically
```
