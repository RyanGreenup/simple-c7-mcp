"""Pydantic models for document management.

This module defines schemas for document CRUD operations, including
content upload, URL fetching, and various update operations.
"""

from datetime import datetime

from pydantic import BaseModel, Field, HttpUrl


class DocumentCreate(BaseModel):
    """Schema for creating a document by uploading content.

    Attributes:
        title: Document title.
        library_id: ID of the library this document belongs to.
        content: Document content (raw text).
    """

    title: str = Field(..., min_length=1, max_length=500)
    library_id: str
    content: str


class DocumentFetch(BaseModel):
    """Schema for creating a document by fetching from URL.

    Attributes:
        title: Document title.
        library_id: ID of the library this document belongs to.
        url: URL to fetch content from.
    """

    title: str = Field(..., min_length=1, max_length=500)
    library_id: str
    url: HttpUrl


class DocumentUpdate(BaseModel):
    """Schema for full document update (PUT).

    Attributes:
        title: Document title.
        content: Document content.
        library_id: Library ID.
    """

    title: str = Field(..., min_length=1, max_length=500)
    content: str
    library_id: str


class ContentUpdate(BaseModel):
    """Schema for updating document content only.

    Attributes:
        content: New document content.
    """

    content: str


class TitleUpdate(BaseModel):
    """Schema for updating document title only.

    Attributes:
        title: New document title.
    """

    title: str = Field(..., min_length=1, max_length=500)


class LibraryAssignment(BaseModel):
    """Schema for moving document to a different library.

    Attributes:
        library_id: Target library ID.
    """

    library_id: str


class EmbeddingsUpdate(BaseModel):
    """Schema for updating document embeddings.

    Attributes:
        embeddings: List of embedding values.
        model: Model used to generate embeddings.
    """

    embeddings: list[float]
    model: str | None = None


class DocumentResponse(BaseModel):
    """Schema for document response (metadata only).

    Attributes:
        id: Document unique identifier.
        title: Document title.
        library_id: Library this document belongs to.
        created_at: Creation timestamp.
        updated_at: Last update timestamp.
        has_embeddings: Whether document has embeddings.
    """

    id: str
    title: str
    library_id: str
    created_at: datetime
    updated_at: datetime
    has_embeddings: bool = Field(default=False)


class DocumentContent(BaseModel):
    """Schema for document content response (raw text).

    Attributes:
        content: Raw document content.
    """

    content: str


class DocumentPretty(BaseModel):
    """Schema for formatted document response (title + content).

    Attributes:
        title: Document title.
        content: Document content.
    """

    title: str
    content: str


class DocumentTitle(BaseModel):
    """Schema for document title response.

    Attributes:
        title: Document title.
    """

    title: str


class DocumentEmbeddings(BaseModel):
    """Schema for document embeddings response.

    Attributes:
        embeddings: List of embedding values.
        dimension: Embedding dimension.
        model: Model used to generate embeddings.
    """

    embeddings: list[float]
    dimension: int
    model: str | None = None
