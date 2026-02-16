"""Pydantic models for library management.

This module defines schemas for library CRUD operations.
"""

from datetime import datetime

from pydantic import BaseModel, Field


class LibraryCreate(BaseModel):
    """Schema for creating a new library.

    Attributes:
        name: Library name (required).
        language: Primary programming language (required).
        ecosystem: Package ecosystem like npm, pypi (required).
        description: Full library description (optional).
        short_description: One-liner summary (optional).
        context7_id: Context7 path, auto-generated if not provided.
        aliases: Alternative names for the library.
        keywords: Searchable terms.
        category: Library type like web-framework, database-orm.
        homepage_url: Official website URL.
        repository_url: Source code repository URL.
        author: Creator or maintainer name.
        license: License type like MIT, Apache-2.0.
    """

    # Required fields
    name: str = Field(..., min_length=1, max_length=255)
    language: str = Field(..., min_length=1, max_length=100)
    ecosystem: str = Field(..., min_length=1, max_length=100)

    # Optional core fields
    description: str = ""
    short_description: str = Field("", max_length=200)
    context7_id: str | None = None  # Auto-generated if not provided

    # Optional classification
    aliases: list[str] = []
    keywords: list[str] = []
    category: str = ""

    # Optional URLs
    homepage_url: str = ""
    repository_url: str = ""
    logo_url: str = ""

    # Optional metadata
    author: str = ""
    license: str = ""


class LibraryUpdate(BaseModel):
    """Schema for full library update (PUT).

    Attributes:
        name: Library name.
        description: Library description.
    """

    name: str = Field(..., min_length=1, max_length=255)
    description: str | None = None


class LibraryPartialUpdate(BaseModel):
    """Schema for partial library update (PATCH).

    Attributes:
        name: Optional library name.
        description: Optional library description.
    """

    name: str | None = Field(None, min_length=1, max_length=255)
    description: str | None = None


class LibraryResponse(BaseModel):
    """Schema for library response.

    Attributes:
        id: Library unique identifier.
        name: Library name.
        context7_id: Context7 compatible path.
        language: Primary programming language.
        ecosystem: Package ecosystem.
        description: Full library description.
        short_description: One-liner summary.
        aliases: Alternative names.
        keywords: Searchable terms.
        category: Library type.
        homepage_url: Official website.
        repository_url: Source code URL.
        author: Creator/maintainer.
        license: License type.
        status: Library status (active, deprecated, archived).
        popularity_score: Normalized popularity metric.
        created_at: Creation timestamp.
        updated_at: Last update timestamp.
        document_count: Number of documents in library.
    """

    id: str
    name: str
    context7_id: str
    language: str
    ecosystem: str
    description: str
    short_description: str
    aliases: list[str]
    keywords: list[str]
    category: str
    homepage_url: str
    repository_url: str
    author: str
    license: str
    status: str
    popularity_score: int
    created_at: datetime
    updated_at: datetime
    document_count: int = Field(default=0)


class DeleteResponse(BaseModel):
    """Schema for delete operation response.

    Attributes:
        success: Whether deletion was successful.
        message: Optional status message.
    """

    success: bool
    message: str | None = None
