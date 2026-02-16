# LanceDB

LanceDB is a high-performance, serverless vector database built on the Lance columnar data format. It provides multi-modal storage for vectors, text, images, and structured data with blazing-fast vector similarity search, full-text search, and hybrid search capabilities. LanceDB supports local file storage, cloud object stores (S3, GCS, Azure), and managed cloud deployments, making it ideal for AI applications, RAG pipelines, and machine learning workflows.

The database offers native SDKs for Python, Node.js/TypeScript, Rust, and Java, with automatic embedding generation through integrations with OpenAI, Sentence Transformers, and other embedding providers. Key features include ACID transactions, zero-copy data access via Apache Arrow, automatic indexing (IVF-PQ, HNSW, BTree, Full-Text), versioning with time travel, and seamless integration with pandas, PyArrow, and Polars DataFrames.

## Python SDK

### Connect to Database

Connect to a local or cloud LanceDB database. Supports local filesystem, S3, GCS, Azure Blob Storage, and LanceDB Cloud.

```python
import lancedb

# Connect to local database
db = lancedb.connect("./my_database")

# Connect to S3
db = lancedb.connect("s3://bucket/path/to/database")

# Connect to LanceDB Cloud
db = lancedb.connect(
    "db://my-database",
    api_key="your-api-key"
)

# List all tables
tables = db.table_names()
print(f"Tables: {tables}")
```

### Create Table

Create a new table from data. Supports Python dicts, pandas DataFrames, PyArrow Tables, and Pydantic models.

```python
import lancedb
import pandas as pd

db = lancedb.connect("./my_database")

# Create table from list of dicts
data = [
    {"id": 1, "text": "Hello world", "vector": [0.1, 0.2, 0.3, 0.4]},
    {"id": 2, "text": "Goodbye world", "vector": [0.5, 0.6, 0.7, 0.8]},
]
table = db.create_table("my_table", data)

# Create table from pandas DataFrame
df = pd.DataFrame({
    "id": [1, 2, 3],
    "text": ["doc1", "doc2", "doc3"],
    "vector": [[0.1, 0.2], [0.3, 0.4], [0.5, 0.6]]
})
table = db.create_table("pandas_table", df, mode="overwrite")

# Open existing table
table = db.open_table("my_table")
print(f"Row count: {table.count_rows()}")
```

### Vector Search

Perform approximate nearest neighbor (ANN) vector similarity search with optional filtering.

```python
import lancedb

db = lancedb.connect("./my_database")
table = db.open_table("my_table")

# Basic vector search - returns 10 nearest neighbors
query_vector = [0.1, 0.2, 0.3, 0.4]
results = table.search(query_vector).limit(10).to_pandas()
print(results)

# Vector search with SQL filter
results = (
    table.search([0.1, 0.2, 0.3, 0.4])
    .where("id > 5 AND category = 'electronics'")
    .select(["id", "text", "category"])
    .limit(20)
    .to_pandas()
)

# Vector search with metric type
results = (
    table.search([0.1, 0.2, 0.3, 0.4])
    .metric("cosine")  # "l2", "cosine", or "dot"
    .nprobes(20)       # Number of partitions to search (for IVF index)
    .refine_factor(10) # Refine results for better accuracy
    .limit(10)
    .to_pandas()
)
print(f"Found {len(results)} results")
```

### Full-Text Search

Perform full-text search using BM25 ranking on text columns with a full-text index.

```python
import lancedb

db = lancedb.connect("./my_database")
table = db.open_table("documents")

# Create full-text search index
table.create_fts_index("content")

# Basic full-text search
results = table.search("machine learning", query_type="fts").limit(10).to_pandas()

# Full-text search with filters
results = (
    table.search("neural networks", query_type="fts")
    .where("year >= 2020")
    .select(["title", "content", "year"])
    .limit(20)
    .to_pandas()
)
print(results)
```

### Hybrid Search with Reranking

Combine vector and full-text search with reranking for improved relevance.

```python
import lancedb
from lancedb.rerankers import CohereReranker, RRFReranker, LinearCombinationReranker

db = lancedb.connect("./my_database")
table = db.open_table("documents")

# Create indices for hybrid search
table.create_index("vector", config=lancedb.index.IvfPq())
table.create_fts_index("content")

# Hybrid search with Reciprocal Rank Fusion (RRF)
reranker = RRFReranker()
results = (
    table.search("artificial intelligence", query_type="hybrid")
    .rerank(reranker)
    .limit(10)
    .to_pandas()
)

# Hybrid search with Cohere reranker (requires API key)
reranker = CohereReranker(api_key="your-cohere-api-key")
results = (
    table.search([0.1, 0.2, 0.3, 0.4], query_type="hybrid")
    .rerank(reranker)
    .limit(10)
    .to_pandas()
)

# Linear combination of vector and FTS scores
reranker = LinearCombinationReranker(weight=0.7)  # 70% vector, 30% FTS
results = (
    table.search("query text", query_type="hybrid")
    .rerank(reranker)
    .limit(10)
    .to_pandas()
)
print(results)
```

### Embedding Functions

Use built-in embedding functions to automatically generate vectors from text.

```python
import lancedb
from lancedb.embeddings import get_registry
from lancedb.pydantic import LanceModel, Vector

# Get embedding function from registry
openai = get_registry().get("openai")
embedding_func = openai.create(name="text-embedding-3-small")

# Define schema with embedding function
class Document(LanceModel):
    text: str = embedding_func.SourceField()
    vector: Vector(embedding_func.ndims()) = embedding_func.VectorField()
    metadata: str

db = lancedb.connect("./my_database")

# Create table with automatic embedding
table = db.create_table(
    "documents",
    schema=Document,
    mode="overwrite"
)

# Add data - vectors are generated automatically
table.add([
    {"text": "LanceDB is a vector database", "metadata": "intro"},
    {"text": "It supports hybrid search", "metadata": "features"},
])

# Search with text query - embedding generated automatically
results = table.search("vector database features").limit(5).to_pandas()
print(results)
```

### Sentence Transformers Embeddings

Use open-source sentence transformers models for local embedding generation.

```python
import lancedb
from lancedb.embeddings import get_registry
from lancedb.pydantic import LanceModel, Vector

# Use sentence-transformers (runs locally)
st = get_registry().get("sentence-transformers")
embedding_func = st.create(
    name="all-MiniLM-L6-v2",
    device="cuda"  # or "cpu"
)

class Article(LanceModel):
    title: str
    content: str = embedding_func.SourceField()
    vector: Vector(embedding_func.ndims()) = embedding_func.VectorField()

db = lancedb.connect("./my_database")
table = db.create_table("articles", schema=Article, mode="overwrite")

# Add articles with automatic embedding
table.add([
    {"title": "AI News", "content": "Latest developments in artificial intelligence"},
    {"title": "ML Guide", "content": "Introduction to machine learning concepts"},
])

# Search returns articles with computed distances
results = table.search("deep learning tutorial").limit(5).to_pandas()
print(results[["title", "content", "_distance"]])
```

### Create Vector Index

Create IVF-PQ or HNSW indices for faster approximate nearest neighbor search.

```python
import lancedb

db = lancedb.connect("./my_database")
table = db.open_table("large_table")

# Create IVF-PQ index (good for large datasets)
table.create_index(
    "vector",
    config=lancedb.index.IvfPq(
        num_partitions=256,
        num_sub_vectors=96,
        distance_type="l2"  # "l2", "cosine", or "dot"
    )
)

# Create HNSW-PQ index (better recall, more memory)
table.create_index(
    "vector",
    config=lancedb.index.HnswPq(
        distance_type="cosine",
        num_partitions=1,
        m=20,               # Connections per node
        ef_construction=300 # Build-time search width
    ),
    replace=True
)

# Create scalar index for filtering
table.create_index("category", config=lancedb.index.BTree())

# List all indices
indices = table.list_indices()
for idx in indices:
    print(f"Index: {idx['name']} on column {idx['columns']}")
```

### Add, Update, and Delete Data

Modify table data with insert, update, delete, and merge operations.

```python
import lancedb

db = lancedb.connect("./my_database")
table = db.open_table("my_table")

# Add new rows
table.add([
    {"id": 100, "text": "New document", "vector": [0.1, 0.2, 0.3, 0.4]},
    {"id": 101, "text": "Another doc", "vector": [0.5, 0.6, 0.7, 0.8]},
])

# Update rows matching a filter
table.update(
    where="id = 100",
    values={"text": "Updated document"}
)

# Delete rows matching a filter
table.delete("id > 1000")

# Merge insert (upsert) - update existing or insert new
table.merge_insert("id")  # Match on 'id' column
    .when_matched_update_all()
    .when_not_matched_insert_all()
    .execute([
        {"id": 100, "text": "Upserted doc", "vector": [0.1, 0.2, 0.3, 0.4]},
        {"id": 200, "text": "New doc", "vector": [0.9, 0.8, 0.7, 0.6]},
    ])

print(f"Total rows: {table.count_rows()}")
```

### Version Control and Time Travel

Access previous versions of data with built-in versioning.

```python
import lancedb

db = lancedb.connect("./my_database")
table = db.open_table("my_table")

# Get current version
current_version = table.version()
print(f"Current version: {current_version}")

# List all versions
versions = table.list_versions()
for v in versions:
    print(f"Version {v['version']} at {v['timestamp']}")

# Checkout a specific version (read-only)
table.checkout(version=5)
historical_data = table.to_pandas()

# Return to latest version
table.checkout_latest()

# Restore to a previous version (creates new version)
table.checkout(version=5)
table.restore()

# Optimize and cleanup old versions
table.optimize()
table.cleanup_old_versions(older_than="7d")
```

## Node.js/TypeScript SDK

### Connect to Database

Connect to LanceDB from Node.js with TypeScript support.

```typescript
import * as lancedb from "@lancedb/lancedb";

// Connect to local database
const db = await lancedb.connect("./my_database");

// Connect to S3
const db = await lancedb.connect("s3://bucket/path/to/database", {
  storageOptions: {
    awsAccessKeyId: "...",
    awsSecretAccessKey: "...",
  },
});

// Connect to LanceDB Cloud
const db = await lancedb.connect("db://my-database", {
  apiKey: "your-api-key",
});

// List tables
const tableNames = await db.tableNames();
console.log("Tables:", tableNames);

// Drop a table
await db.dropTable("old_table");
```

### Create Table

Create tables from JavaScript objects or Arrow tables.

```typescript
import * as lancedb from "@lancedb/lancedb";

const db = await lancedb.connect("./my_database");

// Create table from array of objects
const data = [
  { id: 1, text: "Hello world", vector: [0.1, 0.2, 0.3, 0.4] },
  { id: 2, text: "Goodbye world", vector: [0.5, 0.6, 0.7, 0.8] },
];

const table = await db.createTable("my_table", data, {
  mode: "overwrite",
});

// Create empty table with schema
const schema = new lancedb.Schema([
  new lancedb.Field("id", new lancedb.Int32()),
  new lancedb.Field("text", new lancedb.Utf8()),
  new lancedb.Field(
    "vector",
    new lancedb.FixedSizeList(4, new lancedb.Float32())
  ),
]);
const emptyTable = await db.createEmptyTable("empty_table", schema);

// Open existing table
const existingTable = await db.openTable("my_table");
console.log("Row count:", await existingTable.countRows());
```

### Vector Search

Perform vector similarity search with filtering and pagination.

```typescript
import * as lancedb from "@lancedb/lancedb";

const db = await lancedb.connect("./my_database");
const table = await db.openTable("my_table");

// Basic vector search
const results = await table
  .search([0.1, 0.2, 0.3, 0.4])
  .limit(10)
  .toArray();

console.log("Search results:", results);

// Vector search with filter
const filteredResults = await table
  .query()
  .nearestTo([0.1, 0.2, 0.3, 0.4])
  .where("category = 'tech' AND price < 100")
  .select(["id", "text", "category", "price"])
  .limit(20)
  .toArray();

// Search with distance metric
const cosineResults = await table
  .query()
  .nearestTo([0.1, 0.2, 0.3, 0.4])
  .distanceType("cosine")
  .nprobes(20)
  .refineFactor(10)
  .limit(10)
  .toArrow();

// Iterate over results as record batches
for await (const batch of table.query().nearestTo([0.1, 0.2])) {
  console.log("Batch rows:", batch.numRows);
}
```

### Full-Text Search

Create full-text indices and search text columns.

```typescript
import * as lancedb from "@lancedb/lancedb";

const db = await lancedb.connect("./my_database");
const table = await db.openTable("documents");

// Create full-text search index
await table.createIndex("content", {
  config: lancedb.Index.fts({
    withPosition: true,
    stem: true,
    removeStopWords: true,
    lowercase: true,
  }),
});

// Basic full-text search
const results = await table
  .search("machine learning", "fts")
  .limit(10)
  .toArray();

// Full-text search with filter
const filtered = await table
  .query()
  .fullTextSearch("neural networks")
  .where("year >= 2020")
  .select(["title", "content"])
  .limit(20)
  .toArray();

// Advanced match query with options
const matchQuery = new lancedb.MatchQuery("artificial intelligence", "content", {
  boost: 1.5,
  fuzziness: 1,
  operator: lancedb.Operator.And,
});

const advancedResults = await table
  .query()
  .fullTextSearch(matchQuery)
  .limit(10)
  .toArray();

console.log("Results:", advancedResults);
```

### Create Indices

Create vector and scalar indices for optimized search performance.

```typescript
import * as lancedb from "@lancedb/lancedb";

const db = await lancedb.connect("./my_database");
const table = await db.openTable("large_table");

// Create IVF-PQ vector index
await table.createIndex("vector", {
  config: lancedb.Index.ivfPq({
    numPartitions: 256,
    numSubVectors: 96,
    distanceType: "l2",
  }),
});

// Create HNSW-SQ index (scalar quantization)
await table.createIndex("vector", {
  config: lancedb.Index.hnswSq({
    distanceType: "cosine",
    m: 20,
    efConstruction: 300,
  }),
  replace: true,
});

// Create BTree index for scalar filtering
await table.createIndex("category", {
  config: lancedb.Index.btree(),
});

// Create bitmap index for low-cardinality columns
await table.createIndex("status", {
  config: lancedb.Index.bitmap(),
});

// List indices
const indices = await table.listIndices();
for (const idx of indices) {
  console.log(`Index: ${idx.name} on ${idx.columns}`);
}

// Get index statistics
const stats = await table.indexStats("vector_idx");
console.log("Index stats:", stats);
```

### Add, Update, Delete Data

Modify table data with CRUD operations.

```typescript
import * as lancedb from "@lancedb/lancedb";

const db = await lancedb.connect("./my_database");
const table = await db.openTable("my_table");

// Add new rows
await table.add([
  { id: 100, text: "New document", vector: [0.1, 0.2, 0.3, 0.4] },
  { id: 101, text: "Another doc", vector: [0.5, 0.6, 0.7, 0.8] },
]);

// Update rows with SQL expression
await table.update({
  where: "id = 100",
  values: { text: "Updated text" },
});

// Update with SQL expression for value
await table.update({
  where: "category = 'old'",
  valuesSql: { category: "'new'" },
});

// Delete rows
await table.delete("id > 1000");

// Merge insert (upsert)
await table
  .mergeInsert("id")
  .whenMatchedUpdateAll()
  .whenNotMatchedInsertAll()
  .execute([
    { id: 100, text: "Upserted", vector: [0.1, 0.2, 0.3, 0.4] },
    { id: 200, text: "New row", vector: [0.9, 0.8, 0.7, 0.6] },
  ]);

console.log("Row count:", await table.countRows());
```

### Version Control

Manage table versions with checkout and restore operations.

```typescript
import * as lancedb from "@lancedb/lancedb";

const db = await lancedb.connect("./my_database");
const table = await db.openTable("my_table");

// Get current version
const version = await table.version();
console.log("Current version:", version);

// List all versions
const versions = await table.listVersions();
for (const v of versions) {
  console.log(`Version ${v.version} at ${v.timestamp}`);
}

// Checkout specific version
await table.checkout(5);
const historicalData = await table.toArrow();

// Return to latest
await table.checkoutLatest();

// Restore old version
await table.checkout(5);
await table.restore();

// Optimize table
const stats = await table.optimize({
  cleanupOlderThan: new Date(Date.now() - 7 * 24 * 60 * 60 * 1000),
});
console.log("Compaction stats:", stats);
```

## Java SDK

### Connect to LanceDB Cloud

Connect to LanceDB Cloud or Enterprise deployments from Java.

```java
import com.lancedb.LanceDbNamespaceClientBuilder;
import org.lance.namespace.LanceNamespace;

// Connect to LanceDB Cloud
LanceNamespace client = LanceDbNamespaceClientBuilder.newBuilder()
    .apiKey("your-api-key")
    .database("my-database")
    .region("us-east-1")
    .build();

// Connect to LanceDB Enterprise
LanceNamespace enterpriseClient = LanceDbNamespaceClientBuilder.newBuilder()
    .apiKey("your-api-key")
    .database("my-database")
    .endpoint("https://your-enterprise-endpoint.com")
    .build();

// List namespaces
ListNamespacesRequest request = new ListNamespacesRequest();
request.setId(Arrays.asList());
ListNamespacesResponse response = client.listNamespaces(request);
for (String ns : response.getNamespaces()) {
    System.out.println("Namespace: " + ns);
}
```

### Create Table and Insert Data

Create tables and insert data using Apache Arrow IPC format.

```java
import org.apache.arrow.memory.BufferAllocator;
import org.apache.arrow.memory.RootAllocator;
import org.apache.arrow.vector.*;
import org.apache.arrow.vector.ipc.ArrowStreamWriter;
import org.lance.namespace.model.*;

// Create schema
Schema schema = new Schema(Arrays.asList(
    new Field("id", FieldType.nullable(new ArrowType.Int(32, true)), null),
    new Field("text", FieldType.nullable(new ArrowType.Utf8()), null),
    new Field("vector",
        FieldType.nullable(new ArrowType.FixedSizeList(128)),
        Arrays.asList(new Field("item",
            FieldType.nullable(new ArrowType.FloatingPoint(FloatingPointPrecision.SINGLE)),
            null)))
));

try (BufferAllocator allocator = new RootAllocator();
     VectorSchemaRoot root = VectorSchemaRoot.create(schema, allocator)) {

    root.setRowCount(3);
    IntVector idVector = (IntVector) root.getVector("id");
    VarCharVector textVector = (VarCharVector) root.getVector("text");

    for (int i = 0; i < 3; i++) {
        idVector.setSafe(i, i + 1);
        textVector.setSafe(i, ("Document " + i).getBytes());
    }
    idVector.setValueCount(3);
    textVector.setValueCount(3);

    // Serialize to Arrow IPC
    ByteArrayOutputStream out = new ByteArrayOutputStream();
    try (ArrowStreamWriter writer = new ArrowStreamWriter(root, null, Channels.newChannel(out))) {
        writer.start();
        writer.writeBatch();
        writer.end();
    }
    byte[] tableData = out.toByteArray();

    // Create table
    CreateTableRequest request = new CreateTableRequest();
    request.setId(Arrays.asList("my_namespace", "my_table"));
    client.createTable(request, tableData);
}
```

### Vector Search

Perform vector similarity search and retrieve results.

```java
import org.lance.namespace.model.*;

// Create vector search query
QueryTableRequest query = new QueryTableRequest();
query.setId(Arrays.asList("my_namespace", "my_table"));
query.setK(10);

// Set query vector
List<Float> queryVector = new ArrayList<>();
for (int i = 0; i < 128; i++) {
    queryVector.add(1.0f);
}
QueryTableRequestVector vector = new QueryTableRequestVector();
vector.setSingleVector(queryVector);
query.setVector(vector);

// Add filter
query.setFilter("category = 'electronics'");
query.setPrefilter(true);

// Select columns
query.setColumns(Arrays.asList("id", "text", "category"));

// Execute query
byte[] result = client.queryTable(query);

// Parse results using Arrow reader
try (BufferAllocator allocator = new RootAllocator();
     ArrowFileReader reader = new ArrowFileReader(
         new ByteArraySeekableByteChannel(result), allocator)) {

    for (int i = 0; i < reader.getRecordBlocks().size(); i++) {
        reader.loadRecordBatch(reader.getRecordBlocks().get(i));
        VectorSchemaRoot root = reader.getVectorSchemaRoot();

        for (int row = 0; row < root.getRowCount(); row++) {
            System.out.println("Row " + row + ": " +
                root.getVector("id").getObject(row) + ", " +
                new String((byte[]) root.getVector("text").getObject(row)));
        }
    }
}
```

### Full-Text Search

Perform full-text search queries on text columns.

```java
import org.lance.namespace.model.*;

QueryTableRequest query = new QueryTableRequest();
query.setId(Arrays.asList("my_namespace", "documents"));
query.setK(10);

// Set full-text search query
StringFtsQuery stringQuery = new StringFtsQuery();
stringQuery.setQuery("machine learning neural networks");
stringQuery.setColumns(Arrays.asList("content"));

QueryTableRequestFullTextQuery fts = new QueryTableRequestFullTextQuery();
fts.setStringQuery(stringQuery);
query.setFullTextQuery(fts);

query.setColumns(Arrays.asList("id", "title", "content"));

byte[] result = client.queryTable(query);
System.out.println("Search completed successfully");
```

### Update and Delete Data

Modify existing data with update and delete operations.

```java
import org.lance.namespace.model.*;

// Update rows
UpdateTableRequest updateRequest = new UpdateTableRequest();
updateRequest.setId(Arrays.asList("my_namespace", "my_table"));
updateRequest.setPredicate("id = 1");
updateRequest.setUpdates(Arrays.asList(
    Arrays.asList("text", "'Updated document'"),
    Arrays.asList("category", "'modified'")
));

UpdateTableResponse updateResponse = client.updateTable(updateRequest);
System.out.println("Updated rows: " + updateResponse.getUpdatedRows());

// Delete rows
DeleteFromTableRequest deleteRequest = new DeleteFromTableRequest();
deleteRequest.setId(Arrays.asList("my_namespace", "my_table"));
deleteRequest.setPredicate("id > 1000");

DeleteFromTableResponse deleteResponse = client.deleteFromTable(deleteRequest);
System.out.println("New version after delete: " + deleteResponse.getVersion());

// Merge insert (upsert)
MergeInsertIntoTableRequest mergeRequest = new MergeInsertIntoTableRequest();
mergeRequest.setId(Arrays.asList("my_namespace", "my_table"));
mergeRequest.setOn("id");
mergeRequest.setWhenMatchedUpdateAll(true);
mergeRequest.setWhenNotMatchedInsertAll(true);

MergeInsertIntoTableResponse mergeResponse = client.mergeInsertIntoTable(mergeRequest, data);
System.out.println("Updated: " + mergeResponse.getNumUpdatedRows());
System.out.println("Inserted: " + mergeResponse.getNumInsertedRows());
```

## Summary

LanceDB is designed for building production AI applications that require fast vector similarity search combined with traditional data operations. Its primary use cases include Retrieval-Augmented Generation (RAG) systems, semantic search engines, recommendation systems, image and multi-modal search, and real-time analytics on vector embeddings. The serverless architecture means no infrastructure management, while the Lance columnar format provides efficient storage and zero-copy reads via Apache Arrow.

Integration patterns typically involve using LanceDB as the vector store in LangChain, LlamaIndex, or custom RAG pipelines, where documents are embedded using OpenAI, Sentence Transformers, or other providers, then stored and searched efficiently. The hybrid search capability (combining vector similarity with full-text BM25 ranking and reranking) makes it particularly powerful for applications where keyword matching and semantic understanding both matter. With native support for Python DataFrames, TypeScript Arrow tables, and Java Arrow IPC, LanceDB integrates seamlessly into existing data processing workflows while providing the vector search capabilities needed for modern AI applications.
