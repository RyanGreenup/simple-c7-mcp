# vecs - PostgreSQL Vector Store Client

## Introduction

vecs is a Python client library for managing and querying vector stores in PostgreSQL using the pgvector extension. It provides a simple, ergonomic interface for storing vector embeddings alongside traditional relational data, making it ideal for applications like semantic search, recommendation systems, and AI-powered features. The library abstracts the complexity of working with pgvector by offering intuitive APIs for collection management, vector operations, and similarity search.

The core functionality includes vector upsert/update operations with metadata, efficient similarity search with multiple distance measures (cosine, L2, L1, max inner product), MongoDB-like metadata filtering, and support for advanced indexing methods (IVFFlat and HNSW). Additionally, vecs features an extensible adapter system that enables data transformation pipelines, allowing you to work directly with text or other data types that are automatically converted to vectors. This makes vecs particularly powerful for integrating embeddings from OpenAI, Anthropic, HuggingFace, or custom models into PostgreSQL-backed applications.

## API Reference and Code Examples

### Creating a Client Connection

Establish connection to PostgreSQL database with pgvector extension.

```python
import vecs

# Connect to database
DB_CONNECTION = "postgresql://user:password@localhost:5432/dbname"
vx = vecs.create_client(DB_CONNECTION)

# Or use context manager for automatic cleanup
with vecs.create_client(DB_CONNECTION) as vx:
    # Work with collections
    docs = vx.get_or_create_collection(name="documents", dimension=384)
    # Connection automatically closes on exit
```

### Creating and Managing Collections

Get or create a collection to store vectors with specified dimensions.

```python
import vecs

vx = vecs.create_client("postgresql://user:password@localhost:5432/dbname")

# Create or get collection with 384 dimensions (e.g., for all-MiniLM-L6-v2 embeddings)
docs = vx.get_or_create_collection(name="documents", dimension=384)

# List all collections in database
collections = vx.list_collections()
for collection in collections:
    print(f"{collection.name}: {collection.dimension}D, {len(collection)} vectors")

# Delete a collection
vx.delete_collection("old_collection")

# Always disconnect when done
vx.disconnect()
```

### Upserting Vectors with Metadata

Insert or update vectors with associated metadata.

```python
import vecs
import numpy as np

vx = vecs.create_client("postgresql://user:password@localhost:5432/dbname")
docs = vx.get_or_create_collection(name="articles", dimension=384)

# Prepare records: (id, vector, metadata)
records = [
    (
        "article_1",
        [0.1, 0.2, 0.3, ...],  # 384-dimensional vector (can use list or np.array)
        {"title": "Introduction to AI", "year": 2023, "category": "tech", "views": 1500}
    ),
    (
        "article_2",
        np.random.random(384),
        {"title": "Machine Learning Basics", "year": 2022, "category": "tech", "views": 2300}
    ),
    (
        "article_3",
        np.random.random(384),
        {"title": "Data Science Guide", "year": 2023, "category": "data", "views": 980}
    )
]

# Upsert records (insert new or update existing by ID)
docs.upsert(records)
print(f"Collection now has {len(docs)} vectors")

# Update existing record (same ID overwrites)
updated_record = ("article_1", np.random.random(384), {"title": "AI Updated", "year": 2024})
docs.upsert([updated_record])

vx.disconnect()
```

### Creating Indexes for Performance

Build indexes to accelerate similarity search queries.

```python
import vecs

vx = vecs.create_client("postgresql://user:password@localhost:5432/dbname")
docs = vx.get_or_create_collection(name="articles", dimension=384)

# Insert vectors first
records = [(f"vec{i}", np.random.random(384), {"idx": i}) for i in range(10000)]
docs.upsert(records)

# Auto-select best index method (HNSW if available, otherwise IVFFlat)
docs.create_index()

# Or specify index method and distance measure explicitly
docs.create_index(
    measure=vecs.IndexMeasure.cosine_distance,  # Options: cosine_distance, l2_distance, l1_distance, max_inner_product
    method=vecs.IndexMethod.hnsw,  # Options: auto, hnsw, ivfflat
    index_arguments=vecs.IndexArgsHNSW(
        m=16,  # Max connections per layer (higher = better recall, more memory)
        ef_construction=64  # Size of candidate list during construction (higher = better quality, slower build)
    )
)

# IVFFlat index example (for very large datasets)
docs.create_index(
    measure=vecs.IndexMeasure.cosine_distance,
    method=vecs.IndexMethod.ivfflat,
    index_arguments=vecs.IndexArgsIVFFlat(
        n_lists=100  # Number of inverted lists (rule of thumb: rows/1000 for small datasets)
    ),
    replace=True  # Replace existing index
)

# Check if collection is indexed
if docs.is_indexed_for_measure(vecs.IndexMeasure.cosine_distance):
    print("Collection is indexed for cosine similarity")

vx.disconnect()
```

### Querying Vectors with Similarity Search

Search for similar vectors with optional metadata filtering.

```python
import vecs
import numpy as np

vx = vecs.create_client("postgresql://user:password@localhost:5432/dbname")
docs = vx.get_or_create_collection(name="articles", dimension=384)

# Basic query: find 5 most similar vectors
query_vector = np.random.random(384)
results = docs.query(
    data=query_vector,
    limit=5
)
# Returns: ["article_1", "article_5", ...] (just IDs by default)

# Query with metadata filters
results = docs.query(
    data=query_vector,
    limit=10,
    filters={"year": {"$gte": 2023}},  # Only articles from 2023 or later
    include_value=True,  # Include distance/similarity scores
    include_metadata=True,  # Include metadata in results
    include_vector=False  # Don't include vectors (save bandwidth)
)
# Returns: [("article_1", 0.234, {"title": "...", "year": 2023}), ...]

# Query with complex metadata filters
results = docs.query(
    data=query_vector,
    limit=5,
    filters={
        "$and": [
            {"category": {"$eq": "tech"}},
            {"views": {"$gt": 1000}},
            {"year": {"$in": [2022, 2023]}}
        ]
    },
    include_value=True,
    include_metadata=True
)

# Query with OR logic
results = docs.query(
    data=query_vector,
    limit=5,
    filters={
        "$or": [
            {"category": {"$eq": "urgent"}},
            {"views": {"$gte": 5000}}
        ]
    }
)

# Fine-tune query performance (HNSW-specific)
results = docs.query(
    data=query_vector,
    limit=10,
    ef_search=100  # Larger = more accurate but slower (default: 40)
)

# Fine-tune query performance (IVFFlat-specific)
results = docs.query(
    data=query_vector,
    limit=10,
    probes=20  # Number of lists to scan (higher = more accurate but slower)
)

vx.disconnect()
```

### Metadata Filter Operators

Complete reference for filtering vectors by metadata.

```python
import vecs

vx = vecs.create_client("postgresql://user:password@localhost:5432/dbname")
docs = vx.get_or_create_collection(name="articles", dimension=384)

query_vec = [0.1] * 384

# Equality: $eq
docs.query(data=query_vec, filters={"status": {"$eq": "published"}})

# Not equal: $ne
docs.query(data=query_vec, filters={"status": {"$ne": "draft"}})

# Greater than: $gt
docs.query(data=query_vec, filters={"score": {"$gt": 8.5}})

# Greater than or equal: $gte
docs.query(data=query_vec, filters={"year": {"$gte": 2020}})

# Less than: $lt
docs.query(data=query_vec, filters={"priority": {"$lt": 5}})

# Less than or equal: $lte
docs.query(data=query_vec, filters={"age": {"$lte": 30}})

# In list: $in
docs.query(data=query_vec, filters={"category": {"$in": ["tech", "science", "engineering"]}})

# Array contains scalar: $contains
docs.query(data=query_vec, filters={"tags": {"$contains": "important"}})

# Logical AND: $and
docs.query(
    data=query_vec,
    filters={
        "$and": [
            {"year": {"$eq": 2023}},
            {"category": {"$eq": "tech"}},
            {"views": {"$gte": 1000}}
        ]
    }
)

# Logical OR: $or
docs.query(
    data=query_vec,
    filters={
        "$or": [
            {"priority": {"$eq": "high"}},
            {"urgent": {"$eq": True}}
        ]
    }
)

# Nested logical operators
docs.query(
    data=query_vec,
    filters={
        "$and": [
            {
                "$or": [
                    {"category": {"$eq": "tech"}},
                    {"category": {"$eq": "science"}}
                ]
            },
            {"year": {"$gte": 2022}}
        ]
    }
)

vx.disconnect()
```

### Fetching Specific Vectors by ID

Retrieve vectors by their identifiers.

```python
import vecs

vx = vecs.create_client("postgresql://user:password@localhost:5432/dbname")
docs = vx.get_or_create_collection(name="articles", dimension=384)

# Fetch multiple vectors by ID
ids_to_fetch = ["article_1", "article_5", "article_10"]
records = docs.fetch(ids=ids_to_fetch)

# Returns: [("article_1", [0.1, 0.2, ...], {"title": "...", "year": 2023}), ...]
for record_id, vector, metadata in records:
    print(f"ID: {record_id}, Metadata: {metadata}")

# Fetch single vector using indexing
single_record = docs["article_1"]
# Returns: ("article_1", array([0.1, 0.2, ...]), {"title": "...", "year": 2023})

# Non-existent IDs are silently skipped (no error)
records = docs.fetch(ids=["article_1", "does_not_exist", "article_5"])
# Returns only 2 records (article_1 and article_5)

vx.disconnect()
```

### Deleting Vectors

Remove vectors by ID or metadata filters.

```python
import vecs

vx = vecs.create_client("postgresql://user:password@localhost:5432/dbname")
docs = vx.get_or_create_collection(name="articles", dimension=384)

# Delete by IDs
deleted_ids = docs.delete(ids=["article_1", "article_2", "article_3"])
print(f"Deleted {len(deleted_ids)} vectors: {deleted_ids}")

# Delete by metadata filter
deleted_ids = docs.delete(filters={"year": {"$lt": 2020}})
print(f"Deleted {len(deleted_ids)} old articles")

# Delete with complex filter
deleted_ids = docs.delete(
    filters={
        "$and": [
            {"status": {"$eq": "archived"}},
            {"views": {"$lt": 100}}
        ]
    }
)

# Note: Attempting to delete non-existent records does not raise an error
docs.delete(ids=["does_not_exist"])  # Returns []

vx.disconnect()
```

### Text Embedding Adapter

Work with text directly using automatic embedding and chunking.

```python
import vecs
from vecs.adapter import Adapter, ParagraphChunker, TextEmbedding

# Install text embedding support first:
# pip install "vecs[text_embedding]"

vx = vecs.create_client("postgresql://user:password@localhost:5432/dbname")

# Create collection with text adapter pipeline
docs = vx.get_or_create_collection(
    name="blog_posts",
    adapter=Adapter([
        ParagraphChunker(skip_during_query=True),  # Split text into paragraphs
        TextEmbedding(model='all-MiniLM-L6-v2')    # Embed text (384 dimensions)
    ])
)

# Upsert text directly (automatically chunked and embedded)
docs.upsert([
    (
        "post_1",
        """This is the first paragraph of my blog post.

This is the second paragraph with more content.

And here's a third paragraph with conclusions.""",
        {"author": "Alice", "date": "2024-01-15"}
    ),
    (
        "post_2",
        "Short post without paragraph breaks.",
        {"author": "Bob", "date": "2024-01-16"}
    )
])

# Note: post_1 creates 3 vectors (post_1_para_0, post_1_para_1, post_1_para_2)
#       post_2 creates 1 vector (post_2)

# Query with text (automatically embedded, no chunking due to skip_during_query=True)
results = docs.query(
    data="tell me about blog conclusions",
    limit=5,
    include_value=True,
    include_metadata=True
)

# Can still query with raw vectors by skipping adapter
import numpy as np
results = docs.query(
    data=np.random.random(384),
    limit=5,
    skip_adapter=True  # Bypass adapter pipeline
)

# Available models (from sentence-transformers)
# - 'all-mpnet-base-v2' (768 dim)
# - 'all-MiniLM-L6-v2' (384 dim) - fast and good quality
# - 'multi-qa-mpnet-base-dot-v1' (768 dim)
# - 'all-distilroberta-v1' (768 dim)
# See vecs.adapter.TextEmbeddingModel for full list

vx.disconnect()
```

### Markdown Chunking Adapter

Automatically chunk markdown documents by headings.

```python
import vecs
from vecs.adapter import Adapter, MarkdownChunker, TextEmbedding

vx = vecs.create_client("postgresql://user:password@localhost:5432/dbname")

# Create collection that chunks markdown by headings
docs = vx.get_or_create_collection(
    name="documentation",
    adapter=Adapter([
        MarkdownChunker(skip_during_query=True),
        TextEmbedding(model='all-MiniLM-L6-v2')
    ])
)

# Upsert markdown documentation
docs.upsert([
    (
        "readme",
        """# Getting Started

Welcome to our project!

## Installation

Run pip install to get started.

## Usage

Here's how to use the library.

### Basic Example

Code example here.

### Advanced Example

More complex code here.

## Contributing

We welcome contributions!
""",
        {"type": "guide", "version": "1.0"}
    )
])

# Creates multiple vectors:
# - readme_head_0: "# Getting Started\nWelcome to our project!"
# - readme_head_1: "## Installation\nRun pip install to get started."
# - readme_head_2: "## Usage\nHere's how to use the library."
# - readme_head_3: "### Basic Example\nCode example here."
# - readme_head_4: "### Advanced Example\nMore complex code here."
# - readme_head_5: "## Contributing\nWe welcome contributions!"

# Query documentation with text
results = docs.query(
    data="how do I install this?",
    limit=3,
    include_metadata=True
)

vx.disconnect()
```

### Custom Adapter Implementation

Create custom adapter steps for specialized transformations.

```python
import vecs
from vecs.adapter import Adapter, AdapterStep, AdapterContext
from typing import Iterable, Tuple, Any, Optional, Dict, Generator

# Define custom adapter step
class CustomPreprocessor(AdapterStep):
    """Example: Uppercase text and add prefix"""

    @property
    def exported_dimension(self) -> Optional[int]:
        # Return None if dimension unknown, or specific int if known
        return None

    def __call__(
        self,
        records: Iterable[Tuple[str, Any, Optional[Dict]]],
        adapter_context: AdapterContext
    ) -> Generator[Tuple[str, Any, Dict], None, None]:
        """Transform records"""
        for record_id, data, metadata in records:
            # Behave differently based on context
            if adapter_context == AdapterContext.upsert:
                # During upsert: preprocess text
                processed_data = f"PROCESSED: {data.upper()}"
            else:  # AdapterContext.query
                # During query: different preprocessing
                processed_data = data.upper()

            # Ensure metadata is dict (not None)
            meta = metadata if metadata is not None else {}
            meta["processed"] = True

            yield (record_id, processed_data, meta)

# Use custom adapter in pipeline
vx = vecs.create_client("postgresql://user:password@localhost:5432/dbname")

docs = vx.get_or_create_collection(
    name="custom_processed",
    adapter=Adapter([
        CustomPreprocessor(),
        TextEmbedding(model='all-MiniLM-L6-v2')
    ])
)

# Use collection with custom adapter
docs.upsert([
    ("doc1", "hello world", {"source": "test"})
])
# Stored as: ("doc1", embedding_of("PROCESSED: HELLO WORLD"), {"source": "test", "processed": True})

results = docs.query(data="hello")
# Queries with: embedding_of("HELLO")

vx.disconnect()
```

### Batch Operations and Performance

Efficiently handle large datasets with batching.

```python
import vecs
import numpy as np

vx = vecs.create_client("postgresql://user:password@localhost:5432/dbname")
docs = vx.get_or_create_collection(name="large_dataset", dimension=768)

# Generate large batch of vectors
n_vectors = 100000
batch_size = 1000

print(f"Upserting {n_vectors} vectors in batches of {batch_size}...")

# Upsert in batches for memory efficiency
for batch_start in range(0, n_vectors, batch_size):
    batch_end = min(batch_start + batch_size, n_vectors)

    batch_records = [
        (
            f"vec_{i}",
            np.random.random(768),
            {"batch": batch_start // batch_size, "index": i}
        )
        for i in range(batch_start, batch_end)
    ]

    docs.upsert(batch_records)

    if batch_start % 10000 == 0:
        print(f"Upserted {batch_start} vectors...")

print(f"Total vectors in collection: {len(docs)}")

# Create index for fast queries (important for large collections)
print("Creating HNSW index (this may take a few minutes)...")
docs.create_index(
    measure=vecs.IndexMeasure.cosine_distance,
    method=vecs.IndexMethod.hnsw,
    index_arguments=vecs.IndexArgsHNSW(m=16, ef_construction=64)
)

# Query is now fast even with 100k vectors
query_vector = np.random.random(768)
results = docs.query(
    data=query_vector,
    limit=10,
    include_value=True
)

print(f"Found {len(results)} results")
for idx, (vec_id, distance) in enumerate(results):
    print(f"{idx+1}. {vec_id}: distance={distance:.4f}")

vx.disconnect()
```

### Error Handling

Handle common exceptions gracefully.

```python
import vecs
from vecs.exc import (
    CollectionNotFound,
    CollectionAlreadyExists,
    ArgError,
    MismatchedDimension,
    FilterError,
    MissingDependency
)

vx = vecs.create_client("postgresql://user:password@localhost:5432/dbname")

# Handle collection not found
try:
    docs = vx.get_or_create_collection(name="test", dimension=384)
except CollectionNotFound:
    print("Collection does not exist")

# Handle dimension mismatch
try:
    docs = vx.get_or_create_collection(name="test", dimension=384)
    # Try to upsert wrong dimension
    docs.upsert([("id1", [0.1, 0.2], {})])  # Only 2 dims instead of 384
except MismatchedDimension as e:
    print(f"Dimension error: {e}")

# Handle invalid filter syntax
try:
    docs.query(
        data=[0.1] * 384,
        filters={"invalid_filter": "bad_syntax"}  # Missing operator
    )
except FilterError as e:
    print(f"Invalid filter: {e}")

# Handle invalid arguments
try:
    docs.fetch(ids="should_be_list")  # Should be list, not string
except ArgError as e:
    print(f"Invalid argument: {e}")

# Handle missing optional dependencies
try:
    from vecs.adapter import TextEmbedding
    # If sentence-transformers not installed:
    # pip install "vecs[text_embedding]"
except MissingDependency as e:
    print(f"Missing dependency: {e}")
    print("Install with: pip install 'vecs[text_embedding]'")

vx.disconnect()
```

### Integration with OpenAI Embeddings

Use OpenAI's embedding models with vecs.

```python
import vecs
from openai import OpenAI

# Initialize clients
vx = vecs.create_client("postgresql://user:password@localhost:5432/dbname")
openai_client = OpenAI(api_key="your-api-key")

# Create collection for OpenAI embeddings (text-embedding-3-small = 1536 dimensions)
docs = vx.get_or_create_collection(name="openai_docs", dimension=1536)

# Generate embeddings with OpenAI
documents = [
    {"id": "doc1", "text": "Python is a programming language", "category": "tech"},
    {"id": "doc2", "text": "Machine learning is a subset of AI", "category": "ai"},
    {"id": "doc3", "text": "PostgreSQL is a database system", "category": "database"}
]

# Batch embed documents
texts = [doc["text"] for doc in documents]
response = openai_client.embeddings.create(
    model="text-embedding-3-small",
    input=texts
)

# Prepare records for vecs
records = [
    (
        doc["id"],
        embedding.embedding,  # OpenAI returns list of floats
        {"text": doc["text"], "category": doc["category"]}
    )
    for doc, embedding in zip(documents, response.data)
]

# Upsert to vecs
docs.upsert(records)

# Create index
docs.create_index()

# Query with new text
query_text = "Tell me about databases"
query_response = openai_client.embeddings.create(
    model="text-embedding-3-small",
    input=[query_text]
)
query_embedding = query_response.data[0].embedding

# Search for similar documents
results = docs.query(
    data=query_embedding,
    limit=3,
    include_value=True,
    include_metadata=True
)

for doc_id, distance, metadata in results:
    print(f"ID: {doc_id}")
    print(f"Text: {metadata['text']}")
    print(f"Distance: {distance:.4f}")
    print()

vx.disconnect()
```

### Direct SQL Access to Collections

Query collections directly with SQL for advanced use cases.

```python
import vecs
from sqlalchemy import text

vx = vecs.create_client("postgresql://user:password@localhost:5432/dbname")

# Create collection through vecs
docs = vx.get_or_create_collection(name="articles", dimension=384)

# Upsert some data
docs.upsert([
    ("article1", [0.1] * 384, {"title": "First Article", "views": 100}),
    ("article2", [0.2] * 384, {"title": "Second Article", "views": 200})
])

# Access underlying SQLAlchemy session for direct SQL
with vx.Session() as session:
    # Collections are stored in 'vecs' schema
    # Table structure: (id TEXT PRIMARY KEY, vec VECTOR(dimension), metadata JSONB)

    # Query metadata directly
    result = session.execute(
        text("SELECT id, metadata FROM vecs.articles WHERE (metadata->>'views')::int > 150")
    )
    for row in result:
        print(f"ID: {row.id}, Metadata: {row.metadata}")

    # Get vector dimension
    result = session.execute(
        text("SELECT vector_dims(vec) as dims FROM vecs.articles LIMIT 1")
    )
    print(f"Vector dimensions: {result.scalar()}")

    # Count vectors
    result = session.execute(
        text("SELECT COUNT(*) FROM vecs.articles")
    )
    print(f"Total vectors: {result.scalar()}")

    session.commit()

# Note: Avoid DDL operations (CREATE, DROP, ALTER) via SQL
# Always use vecs client methods for schema changes

vx.disconnect()
```

## Summary and Use Cases

vecs is designed for developers building AI-powered applications that require efficient vector similarity search. Common use cases include semantic search engines where users search by meaning rather than keywords, recommendation systems that find similar products or content, question-answering systems that retrieve relevant context from document collections, and RAG (Retrieval Augmented Generation) pipelines for LLMs. The library shines in scenarios where you need to combine vector search with traditional database features like metadata filtering, transactions, and relational queries, all within the familiar PostgreSQL ecosystem.

The adapter system enables powerful workflows where you can directly upsert text, markdown, or other data types that are automatically processed into embeddings. This makes vecs particularly effective for document management systems, knowledge bases, and content platforms. Integration patterns typically involve creating collections with appropriate dimensions for your embedding model (384 for all-MiniLM-L6-v2, 768 for larger models, 1536 for OpenAI's text-embedding-3-small), indexing with HNSW for best performance, and querying with metadata filters to narrow results by business logic. The library's support for both built-in adapters and custom adapter implementations makes it extensible for domain-specific requirements while maintaining the simplicity of working with raw vectors when needed.

