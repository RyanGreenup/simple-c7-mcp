# LanceDB Schema Design for Context7 MCP Server

This document describes the database schema design for the Context7-compatible MCP server using LanceDB as the storage backend.

## 📚 Overview

LanceDB is a vector database built on Apache Arrow and Parquet, designed for AI applications. Key characteristics:
- **Columnar storage** - Efficient for analytics and vector search
- **Pydantic models** - Schema definition using Python types
- **Hybrid search** - Combines vector similarity with metadata filtering
- **Embedded** - No separate server process needed
- **ACID transactions** - Safe concurrent access

## 🗄️ Schema Design

We use **two separate tables** to separate library metadata from document chunks:

1. **`libraries`** - Metadata about programming libraries
2. **`documents`** - Chunked documentation with embeddings

---

## Table 1: Libraries (Metadata)

### Purpose
Store metadata about programming libraries to support:
- MCP `resolve-library-id` tool (name → Context7 ID)
- Library disambiguation (multiple libraries with same name)
- Search and discovery
- Documentation quality tracking

### LanceDB Schema (Pydantic Model)

```python
from datetime import datetime
from typing import Optional

from lancedb.pydantic import LanceModel, Vector


class Library(LanceModel):
    """Library metadata for MCP server.

    This model stores information about programming libraries to support
    library resolution, search, and documentation management.
    """

    # ==================== Core Identity ====================
    id: str  # Primary key, e.g., "lib-npm-react", "lib-pypi-requests"
    name: str  # Display name, e.g., "React", "requests", "FastAPI"
    context7_id: str  # Context7 path, e.g., "/npm/react", "/pypi/requests"
    aliases: list[str]  # Alternative names, e.g., ["React", "ReactJS", "react.js"]

    # ==================== Classification ====================
    language: str  # Primary language, e.g., "JavaScript", "Python", "Go"
    ecosystem: str  # Package ecosystem, e.g., "npm", "pypi", "crates.io", "maven"
    category: str  # Library type, e.g., "web-framework", "database-orm", "testing"
    keywords: list[str]  # Searchable terms, e.g., ["reactive", "components", "ui"]

    # ==================== Descriptions ====================
    short_description: str  # One-liner for list views (max 200 chars)
    description: str  # Full description with key features

    # ==================== URLs ====================
    homepage_url: Optional[str] = None  # Official website
    repository_url: Optional[str] = None  # Source code (GitHub, GitLab, etc.)
    logo_url: Optional[str] = None  # Library logo for UI display

    # ==================== Metadata ====================
    author: Optional[str] = None  # Creator/maintainer, e.g., "Facebook", "Pallets"
    license: Optional[str] = None  # License type, e.g., "MIT", "Apache-2.0"
    status: str = "active"  # "active", "deprecated", "archived"

    # ==================== Popularity Metrics ====================
    # Normalized popularity score across ecosystems (0-100)
    # Useful for ranking disambiguation results
    popularity_score: int = 0

    # Raw metrics (ecosystem-specific)
    github_stars: Optional[int] = None
    npm_downloads_weekly: Optional[int] = None
    pypi_downloads_monthly: Optional[int] = None

    # ==================== Documentation ====================
    doc_version: Optional[str] = None  # Version these docs cover, e.g., "18.2.0"
    doc_source_type: Optional[str] = None  # "official", "readthedocs", "github-wiki"
    doc_completeness: float = 0.0  # 0.0-1.0, percentage of API documented
    last_indexed_at: Optional[datetime] = None  # When docs were last scraped

    # ==================== Relationships ====================
    # Related libraries users often need together
    related_libraries: list[str] = []  # e.g., ["react-router", "redux"]

    # Similar alternatives
    alternative_to: list[str] = []  # e.g., ["Vue", "Angular", "Svelte"]

    # Libraries this one replaces/supersedes
    supersedes: list[str] = []  # e.g., ["create-react-app"]

    # Core dependencies
    requires_libraries: list[str] = []  # e.g., ["react"]

    # ==================== Timestamps ====================
    first_release_date: Optional[datetime] = None  # Library age
    last_release_date: Optional[datetime] = None  # Maintenance indicator
    created_at: datetime  # When added to our database
    updated_at: datetime  # Last metadata update

    # ==================== Cached Aggregates ====================
    document_count: int = 0  # Number of doc chunks for this library

    # ==================== Optional: Embeddings ====================
    # Optional: Embed the description for semantic library search
    # description_vector: Vector(1024)  # Uncomment if using embeddings
```

### Field Design Rationale

#### **Why `ecosystem` instead of just `language`?**
- More precise: "npm" vs "JavaScript" (Deno uses JS but different ecosystem)
- Enables filtering: "Show me all npm packages"
- Disambiguation: "requests" exists in both npm and pypi

#### **Why separate `short_description` and `description`?**
- **short_description**: Display in list views, search results (1 line)
- **description**: Full details for library detail pages, MCP responses

#### **Why `aliases`?**
- Fuzzy matching: Users might search "ReactJS", "react.js", "React"
- Common misspellings or variations
- Enables broader search without complex fuzzy logic

#### **Why `keywords` array?**
- Better than parsing description text
- Structured search: `WHERE 'http' IN keywords`
- Can be curated/edited separately from description
- Useful for MCP disambiguation (match query terms against keywords)

#### **Why `status` field?**
- Prevent recommending deprecated libraries
- Display warnings for archived projects
- Filter out inactive libraries from search

#### **Why popularity metrics?**
- Ranking: When multiple matches, prefer popular ones
- Trust indicator: High stars = battle-tested
- Disambiguation: "requests" in Python (popular) vs npm (obscure)

#### **Why `last_indexed_at`?**
- Know when docs are stale
- Trigger re-indexing for outdated docs
- Display freshness to users

#### **Why relationship fields?**
- `related_libraries`: Suggest complementary packages
- `alternative_to`: Help users explore options
- `supersedes`: Recommend migration paths
- `requires_libraries`: Understand dependencies

---

## Table 2: Documents (Chunked Documentation)

### Purpose
Store chunked documentation with vector embeddings for semantic search.

### LanceDB Schema (Pydantic Model)

```python
from lancedb.pydantic import LanceModel, Vector


class Document(LanceModel):
    """Document chunk with embeddings for semantic search.

    Documents are split into chunks for better retrieval granularity.
    Each chunk has its own embedding for vector similarity search.
    """

    # ==================== Identity ====================
    id: int  # Unique chunk ID
    document_id: str  # Groups chunks from same document, e.g., "doc-react-hooks-intro"
    library_id: str  # Foreign key to libraries table

    # ==================== Content ====================
    title: str  # Document title, e.g., "useState Hook"
    text: str  # Chunk text content

    # ==================== Chunking Info ====================
    chunk_index: int  # Position of this chunk in document (0-based)
    chunk_total: int  # Total number of chunks in document

    # ==================== Source Tracking ====================
    source: str  # Source URL or file path
    source_type: str  # "url", "markdown", "pdf", "html"

    # ==================== Vector Embedding ====================
    vector: Vector(2560)  # Embedding vector (adjust dimension for your model)
    # Common sizes: 384 (MiniLM), 768 (BERT), 1024 (Cohere), 1536 (OpenAI), 2560 (custom)

    # ==================== Metadata ====================
    metadata: dict = {}  # Flexible JSON metadata (headings, code blocks, etc.)

    # ==================== Timestamps ====================
    created_at: datetime  # When chunk was indexed

    # ==================== Optional: Library Denormalization ====================
    # Denormalized for faster filtering without joins
    library_name: str  # e.g., "React"
    library_language: str  # e.g., "JavaScript"
    library_ecosystem: str  # e.g., "npm"
```

### Why Denormalize Library Fields?

LanceDB doesn't have traditional SQL joins. Denormalizing key library fields into the documents table enables:
- **Faster filtering**: `WHERE library_language = 'Python'` without loading libraries table
- **Simpler queries**: No need to join tables for common filters
- **Trade-off**: Slightly more storage for much better query performance

---

## 🔍 MCP Library Lookup Process (LanceDB Implementation)

### Tool: `resolve-library-id`

**Goal**: Convert library name + query context → Context7 ID

### Implementation Strategy

```python
import lancedb
from typing import Optional


class LibraryResolver:
    """Resolves library names to Context7 IDs using LanceDB."""

    def __init__(self, db_path: str = "./lancedb"):
        self.db = lancedb.connect(db_path)
        self.libraries = self.db.open_table("libraries")

    def resolve_library_id(self, library_name: str, query: str) -> str:
        """Resolve library name to Context7 ID.

        Args:
            library_name: Library name to resolve (e.g., "React", "requests")
            query: User's query for context (e.g., "Python HTTP client")

        Returns:
            Context7 ID (e.g., "/npm/react", "/pypi/requests")

        Raises:
            LibraryNotFoundError: If no matching library found
            AmbiguousLibraryError: If multiple matches and can't disambiguate
        """
        # Step 1: Exact name match (case-insensitive)
        exact_matches = self._search_exact_name(library_name)

        # Step 2: If no exact match, try aliases
        if not exact_matches:
            exact_matches = self._search_aliases(library_name)

        # Step 3: If still no match, try fuzzy search
        if not exact_matches:
            exact_matches = self._search_fuzzy_name(library_name)

        # Step 4: Handle results
        if len(exact_matches) == 0:
            raise LibraryNotFoundError(f"Library '{library_name}' not found")

        if len(exact_matches) == 1:
            return exact_matches[0]["context7_id"]

        # Step 5: Disambiguate multiple matches using query context
        best_match = self._disambiguate(exact_matches, query)
        return best_match["context7_id"]

    def _search_exact_name(self, library_name: str) -> list[dict]:
        """Search for exact name match (case-insensitive)."""
        # LanceDB filter syntax
        results = (
            self.libraries
            .search()
            .where(f"name = '{library_name}'", prefilter=True)
            .to_list()
        )
        return results

    def _search_aliases(self, library_name: str) -> list[dict]:
        """Search in aliases array."""
        # Note: LanceDB array contains syntax
        results = (
            self.libraries
            .search()
            .where(f"array_contains(aliases, '{library_name}')", prefilter=True)
            .to_list()
        )
        return results

    def _search_fuzzy_name(self, library_name: str) -> list[dict]:
        """Fuzzy search on name field."""
        # Simple substring search (can be improved with better fuzzy matching)
        results = (
            self.libraries
            .search()
            .where(f"name LIKE '%{library_name}%'", prefilter=True)
            .limit(10)
            .to_list()
        )
        return results

    def _disambiguate(self, matches: list[dict], query: str) -> dict:
        """Disambiguate multiple matches using query context.

        Scoring factors:
        1. Language mentioned in query
        2. Keywords match query terms
        3. Description similarity
        4. Popularity score
        5. Status (active > deprecated)
        """
        query_lower = query.lower()
        query_words = set(query_lower.split())

        # Language hints for detection
        language_hints = {
            "python": ["python", "pip", "pypi", "py"],
            "javascript": ["javascript", "js", "npm", "node", "typescript", "ts"],
            "go": ["go", "golang"],
            "rust": ["rust", "cargo", "crates"],
            "java": ["java", "maven", "gradle"],
            "ruby": ["ruby", "gem", "rails"],
            "php": ["php", "composer"],
            "c++": ["c++", "cpp"],
            "c#": ["c#", "csharp", "dotnet", ".net", "nuget"],
        }

        ecosystem_hints = {
            "npm": ["npm", "node", "javascript", "typescript"],
            "pypi": ["pip", "pypi", "python"],
            "crates.io": ["cargo", "crates", "rust"],
            "maven": ["maven", "gradle", "java"],
        }

        scored_matches = []

        for match in matches:
            score = 0

            # 1. Language detection (+10 points)
            for lang, keywords in language_hints.items():
                if any(kw in query_lower for kw in keywords):
                    if match["language"].lower() == lang:
                        score += 10

            # 2. Ecosystem detection (+10 points)
            for eco, keywords in ecosystem_hints.items():
                if any(kw in query_lower for kw in keywords):
                    if match["ecosystem"].lower() == eco:
                        score += 10

            # 3. Keywords overlap (+1 per matching keyword)
            if match["keywords"]:
                keyword_overlap = len(
                    set(kw.lower() for kw in match["keywords"]) & query_words
                )
                score += keyword_overlap

            # 4. Description word overlap (+0.5 per word)
            if match["description"]:
                desc_words = set(match["description"].lower().split())
                desc_overlap = len(desc_words & query_words)
                score += desc_overlap * 0.5

            # 5. Popularity bonus (+0-5 points scaled)
            # Normalize popularity_score (0-100) to 0-5 bonus
            popularity_bonus = (match.get("popularity_score", 0) / 100) * 5
            score += popularity_bonus

            # 6. Status penalty (-20 for deprecated, -50 for archived)
            if match.get("status") == "deprecated":
                score -= 20
            elif match.get("status") == "archived":
                score -= 50

            scored_matches.append({
                "match": match,
                "score": score,
            })

        # Sort by score (highest first)
        scored_matches.sort(key=lambda x: x["score"], reverse=True)

        # Return best match
        best = scored_matches[0]

        # Log ambiguous resolution for debugging
        print(f"Ambiguous resolution for '{matches[0]['name']}':")
        for sm in scored_matches:
            print(f"  - {sm['match']['context7_id']}: {sm['score']} points")

        return best["match"]


# Usage example
resolver = LibraryResolver()

# Unambiguous case
context7_id = resolver.resolve_library_id("FastAPI", "Python web framework")
# Returns: "/pypi/fastapi"

# Ambiguous case - language helps
context7_id = resolver.resolve_library_id("requests", "Python HTTP client")
# Finds: requests (Python) and requests (npm)
# Detects "Python" in query
# Returns: "/pypi/requests"

# Fuzzy match
context7_id = resolver.resolve_library_id("react-router", "routing for React apps")
# Exact match fails
# Fuzzy finds "react-router-dom"
# Returns: "/npm/react-router-dom"
```

---

## 📊 Query Patterns in LanceDB

### 1. **List All Libraries**

```python
db = lancedb.connect("./lancedb")
libraries = db.open_table("libraries")

# Get all active libraries
results = (
    libraries
    .search()
    .where("status = 'active'", prefilter=True)
    .limit(100)
    .to_list()
)
```

### 2. **Filter by Language**

```python
# Get all Python libraries
python_libs = (
    libraries
    .search()
    .where("language = 'Python'", prefilter=True)
    .to_list()
)
```

### 3. **Filter by Ecosystem**

```python
# Get all npm packages
npm_packages = (
    libraries
    .search()
    .where("ecosystem = 'npm'", prefilter=True)
    .to_list()
)
```

### 4. **Search by Keyword**

```python
# Find libraries with "http" keyword
http_libs = (
    libraries
    .search()
    .where("array_contains(keywords, 'http')", prefilter=True)
    .to_list()
)
```

### 5. **Full-Text Search (if FTS enabled)**

```python
# Search in descriptions
search_results = (
    libraries
    .search("web framework")
    .select(["name", "short_description", "context7_id"])
    .limit(10)
    .to_list()
)
```

### 6. **Semantic Search (if embeddings added)**

```python
# If you add description_vector to Library model
# You can do semantic search

query_embedding = embed_text("fast asynchronous web framework")

similar_libs = (
    libraries
    .search(query_embedding)
    .where("language = 'Python'", prefilter=True)
    .limit(5)
    .to_list()
)
```

### 7. **Complex Filters**

```python
# Active Python libraries with high popularity
popular_python = (
    libraries
    .search()
    .where("status = 'active' AND language = 'Python' AND popularity_score > 50", prefilter=True)
    .limit(20)
    .to_list()
)
```

---

## 🔧 LanceDB Best Practices

### **1. Use Prefiltering**

```python
# Good - prefilter before vector search
results = table.search(query).where("category = 'web-framework'", prefilter=True)

# Bad - filter after vector search (slower)
results = table.search(query).where("category = 'web-framework'")
```

### **2. Denormalize for Performance**

Instead of joining tables, duplicate frequently-accessed fields:
```python
# In Document model
library_name: str  # Denormalized from Library
library_language: str  # Denormalized from Library
```

### **3. Use Appropriate Vector Dimensions**

```python
# Match your embedding model
Vector(384)   # MiniLM
Vector(768)   # BERT
Vector(1024)  # Cohere
Vector(1536)  # OpenAI ada-002
Vector(2560)  # Custom models
```

### **4. Index Large Tables**

```python
# Create index for faster search
table.create_index(
    metric="cosine",  # or "L2", "dot"
    num_partitions=256,
    num_sub_vectors=96
)
```

### **5. Batch Operations**

```python
# Good - batch insert
libraries = [lib1, lib2, lib3, ...]
table.add(libraries)

# Bad - individual inserts
for lib in libraries:
    table.add([lib])
```

---

## 🚀 Implementation Checklist

### Phase 1: Core Schema
- [ ] Define `Library` Pydantic model
- [ ] Define `Document` Pydantic model
- [ ] Create LanceDB connection utility
- [ ] Implement table creation/initialization
- [ ] Add basic CRUD operations for libraries

### Phase 2: MCP Integration
- [ ] Implement `LibraryResolver` class
- [ ] Add `resolve_library_id()` method
- [ ] Add disambiguation logic
- [ ] Test with ambiguous library names
- [ ] Integrate with MCP router

### Phase 3: Optimization
- [ ] Add vector indexes for faster search
- [ ] Implement caching for frequent queries
- [ ] Add monitoring/logging
- [ ] Benchmark query performance
- [ ] Optimize prefiltering strategies

### Phase 4: Advanced Features
- [ ] Add semantic library search (description embeddings)
- [ ] Implement related libraries suggestions
- [ ] Add popularity score updates (background job)
- [ ] Track library usage analytics
- [ ] Implement library versioning support

---

## 📝 Migration Notes

### Existing Data
If you already have a `docs` table with `library` as a string field:

```python
# Step 1: Extract unique libraries from docs table
docs = db.open_table("docs")
unique_libs = set(doc["library"] for doc in docs.to_pandas()["library"])

# Step 2: Create library records
libraries_data = []
for lib_name in unique_libs:
    libraries_data.append({
        "id": f"lib-{lib_name.lower().replace(' ', '-')}",
        "name": lib_name,
        "context7_id": f"/unknown/{lib_name.lower()}",  # Update manually
        "ecosystem": "unknown",  # Update manually
        "language": "unknown",  # Update manually
        "short_description": "",
        "description": "",
        "status": "active",
        "created_at": datetime.now(),
        "updated_at": datetime.now(),
        # ... other fields
    })

# Step 3: Create libraries table and insert
libraries_table = db.create_table("libraries", schema=Library, mode="overwrite")
libraries_table.add(libraries_data)

# Step 4: Update docs table to reference library_id
# (This may require recreating the docs table with new schema)
```

---

## 🔗 Related Documentation

- [IMPLEMENTATION.md](./IMPLEMENTATION.md) - Full implementation checklist
- [LanceDB Documentation](https://lancedb.github.io/lancedb/)
- [Context7 MCP Specification](https://github.com/context7/mcp-spec)

---

**Last Updated**: 2026-02-16
**Version**: 1.0
