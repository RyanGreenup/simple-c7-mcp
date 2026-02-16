# LanceDB Document Ingestion and Search Tool

A command-line tool for ingesting text documents into LanceDB and performing vector similarity searches.

## Features

- 📄 **Document Ingestion**: Read text files and split them into chunks
- 🔢 **Vector Embeddings**: Generate embeddings for semantic search
- 🔍 **Vector Search**: Perform similarity searches on ingested documents
- 📊 **Database Management**: List tables and view statistics
- 🎨 **Rich CLI**: Beautiful terminal interface with progress indicators

## Installation

```bash
cd /home/ryan/Sync/journals/2026/02/16/context-mcp/c7-attempt/scripts/lancedb
uv sync
```

## Usage

### 1. Ingest a Document

Read a text file, chunk it, generate embeddings, and store in LanceDB:

```bash
# Basic usage
uv run lance-db-example ingest sample_document.txt

# With custom options
uv run lance-db-example ingest document.txt \
  --db ./my_database \
  --table my_docs \
  --chunk-size 1000 \
  --overlap 100
```

**Options:**
- `--db, -d`: Database directory path (default: `./lancedb_data`)
- `--table, -t`: Table name (default: `documents`)
- `--chunk-size, -c`: Chunk size in characters (default: 500)
- `--overlap, -o`: Overlap between chunks (default: 50)

### 2. Search Documents

Perform vector similarity search on ingested documents:

```bash
# Basic search
uv run lance-db-example search "machine learning algorithms"

# With options
uv run lance-db-example search "deep learning" \
  --db ./my_database \
  --table my_docs \
  --limit 10
```

**Options:**
- `--db, -d`: Database directory path (default: `./lancedb_data`)
- `--table, -t`: Table name to search (default: `documents`)
- `--limit, -l`: Maximum number of results (default: 5)

### 3. List Tables

View all tables in the database:

```bash
uv run lance-db-example list-tables
uv run lance-db-example list-tables --db ./my_database
```

### 4. View Statistics

Display statistics about a specific table:

```bash
uv run lance-db-example stats
uv run lance-db-example stats --table my_docs --db ./my_database
```

## Quick Start Example

```bash
# 1. Ingest the sample document
uv run lance-db-example ingest sample_document.txt

# 2. Search for content
uv run lance-db-example search "neural networks"

# 3. Try different queries
uv run lance-db-example search "supervised learning"
uv run lance-db-example search "healthcare applications"
uv run lance-db-example search "reinforcement learning"

# 4. View database info
uv run lance-db-example list-tables
uv run lance-db-example stats
```

## How It Works

### Document Ingestion

1. **Read File**: Loads the text file into memory
2. **Chunking**: Splits text into overlapping chunks (default 500 chars with 50 char overlap)
3. **Embeddings**: Generates vector embeddings for each chunk
4. **Storage**: Stores chunks with their embeddings in LanceDB

### Vector Search

1. **Query Embedding**: Converts your search query into a vector
2. **Similarity Search**: Finds the most similar document chunks using vector distance
3. **Results**: Returns ranked results with relevance scores

## Embedding Function

The current implementation uses a simple character frequency-based embedding for demonstration purposes. In production, you should use proper embedding models:

### Using Sentence Transformers (Recommended)

```python
import lancedb
from lancedb.embeddings import get_registry
from lancedb.pydantic import LanceModel, Vector

# Get sentence-transformers embedding function
st = get_registry().get("sentence-transformers")
embedding_func = st.create(name="all-MiniLM-L6-v2", device="cpu")

class Document(LanceModel):
    text: str = embedding_func.SourceField()
    vector: Vector(embedding_func.ndims()) = embedding_func.VectorField()

# Use in your schema
```

### Using OpenAI Embeddings

```python
from lancedb.embeddings import get_registry

openai = get_registry().get("openai")
embedding_func = openai.create(name="text-embedding-3-small")
```

## Project Structure

```
lance_db_example/
├── __init__.py
├── cli.py          # CLI entry point
└── ingest.py       # Main logic (ingest, search, stats)
```

## Advanced Usage

### Custom Chunk Sizes

For technical documents with code:
```bash
uv run lance-db-example ingest code_doc.txt --chunk-size 1000 --overlap 100
```

For short-form content:
```bash
uv run lance-db-example ingest tweets.txt --chunk-size 200 --overlap 20
```

### Multiple Documents

Ingest multiple documents into different tables:
```bash
uv run lance-db-example ingest doc1.txt --table tech_docs
uv run lance-db-example ingest doc2.txt --table business_docs
uv run lance-db-example ingest doc3.txt --table legal_docs
```

Search specific tables:
```bash
uv run lance-db-example search "API design" --table tech_docs
uv run lance-db-example search "contract terms" --table legal_docs
```

## LanceDB Features Used

Based on official LanceDB documentation:

- **Vector Search**: `table.search(vector).limit(n).to_pandas()`
- **Table Creation**: `db.create_table(name, data, mode="overwrite")`
- **Database Connection**: `lancedb.connect(path)`
- **Schema Management**: Automatic schema inference from pandas DataFrame

## Dependencies

- `lancedb>=0.16.0` - Vector database
- `typer>=0.20.0` - CLI framework
- `rich>=13.0.0` - Terminal formatting
- `pandas>=2.0.0` - Data manipulation

## Limitations

The current embedding function is a simple demonstration. For production use:

1. **Install sentence-transformers**: Add `sentence-transformers` to dependencies
2. **Update embedding function**: Replace `create_simple_embeddings()` with proper models
3. **GPU Support**: Use `device="cuda"` for faster embedding generation
4. **API Keys**: If using OpenAI, set `OPENAI_API_KEY` environment variable

## References

- [LanceDB Official Documentation](https://lancedb.github.io/lancedb/)
- [LanceDB Python SDK](https://github.com/lancedb/lancedb)
- Documentation sourced via Context7 MCP

## License

MIT

## Contributing

Feel free to submit issues and enhancement requests!
