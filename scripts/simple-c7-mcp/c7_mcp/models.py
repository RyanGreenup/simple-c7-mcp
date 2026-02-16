"""LanceDB Pydantic models for schema definition.

This module defines the database schema using Pydantic models
compatible with LanceDB.
"""

from datetime import datetime

from lancedb.pydantic import LanceModel, Vector


class Library(LanceModel):
    """Library metadata for MCP server.

    This model stores information about programming libraries to support
    library resolution, search, and documentation management.
    """

    # ==================== Core Identity ====================
    id: str  # Primary key, e.g., "lib-npm-react"
    name: str  # Display name, e.g., "React", "requests"
    context7_id: str  # Context7 path, e.g., "/npm/react"
    aliases: list[str] = []  # Alternative names

    # ==================== Classification ====================
    language: str  # Primary language
    ecosystem: str  # Package ecosystem, e.g., "npm", "pypi"
    category: str = ""  # Library type, e.g., "web-framework"
    keywords: list[str] = []  # Searchable terms

    # ==================== Descriptions ====================
    short_description: str = ""  # One-liner (max 200 chars)
    description: str = ""  # Full description

    # ==================== URLs ====================
    homepage_url: str = ""  # Official website
    repository_url: str = ""  # Source code
    logo_url: str = ""  # Library logo

    # ==================== Metadata ====================
    author: str = ""  # Creator/maintainer
    license: str = ""  # License type
    status: str = "active"  # "active", "deprecated", "archived"

    # ==================== Popularity Metrics ====================
    popularity_score: int = 0  # Normalized 0-100
    github_stars: int = 0
    npm_downloads_weekly: int = 0
    pypi_downloads_monthly: int = 0

    # ==================== Documentation ====================
    doc_version: str = ""  # Version docs cover
    doc_source_type: str = ""  # "official", "readthedocs"
    doc_completeness: float = 0.0  # 0.0-1.0
    last_indexed_at: datetime | None = None

    # ==================== Relationships ====================
    related_libraries: list[str] = []
    alternative_to: list[str] = []
    supersedes: list[str] = []
    requires_libraries: list[str] = []

    # ==================== Timestamps ====================
    first_release_date: datetime | None = None
    last_release_date: datetime | None = None
    created_at: datetime
    updated_at: datetime

    # ==================== Cached Aggregates ====================
    document_count: int = 0


class Document(LanceModel):
    """Document chunk with embeddings for semantic search.

    Documents are split into chunks for better retrieval granularity.
    Each chunk has its own embedding for vector similarity search.
    """

    # ==================== Identity ====================
    id: int  # Unique chunk ID
    document_id: str  # Groups chunks from same document
    library_id: str  # Foreign key to libraries table

    # ==================== Content ====================
    title: str  # Document title
    text: str  # Chunk text content

    # ==================== Chunking Info ====================
    chunk_index: int  # Position in document (0-based)
    chunk_total: int  # Total chunks in document

    # ==================== Source Tracking ====================
    source: str  # Source URL or file path
    source_type: str = "url"  # "url", "markdown", "pdf", "html"

    # ==================== Vector Embedding ====================
    vector: Vector(2560)  # type: ignore  # Adjust dimension for your model

    # ==================== Metadata ====================
    # Note: LanceDB doesn't support dict type directly
    # Use string fields for metadata or serialize to JSON string
    metadata_json: str = "{}"  # JSON-serialized metadata

    # ==================== Timestamps ====================
    created_at: datetime

    # ==================== Denormalized Library Fields ====================
    library_name: str  # Denormalized for faster filtering
    library_language: str  # Denormalized for faster filtering
    library_ecosystem: str  # Denormalized for faster filtering
