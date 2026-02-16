"""Pydantic models for library management.

This module defines schemas for library CRUD operations.
"""

from datetime import datetime

from pydantic import BaseModel, Field


class LibraryCreate(BaseModel):
    """Schema for creating a new library.

    Attributes:
        name: Library name.
        description: Optional library description.
    """

    name: str = Field(..., min_length=1, max_length=255)
    description: str | None = None


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
        description: Library description.
        created_at: Creation timestamp.
        updated_at: Last update timestamp.
        document_count: Number of documents in library.
    """

    id: str
    name: str
    description: str | None
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
