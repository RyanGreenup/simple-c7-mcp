"""Library management router.

This module implements RESTful CRUD endpoints for library management.
"""

from fastapi import APIRouter, HTTPException

from c7_mcp.exceptions import C7Error
from c7_mcp.schemas.library import (
    DeleteResponse,
    LibraryCreate,
    LibraryPartialUpdate,
    LibraryResponse,
    LibraryUpdate,
)
from c7_mcp.services import library as library_service

router = APIRouter(prefix="/api/v1/libraries", tags=["libraries"])


@router.get("", response_model=list[LibraryResponse])
async def list_libraries() -> list[LibraryResponse]:
    """List all libraries.

    Returns:
        List of all libraries with metadata and document counts.

    Raises:
        HTTPException: 500 if internal server error.
    """
    try:
        libraries = library_service.list_libraries()
        return [LibraryResponse(**lib) for lib in libraries]
    except C7Error:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to list libraries: {str(e)}"
        )


@router.post("", response_model=LibraryResponse, status_code=201)
async def create_library(library: LibraryCreate) -> LibraryResponse:
    """Create a new library.

    Args:
        library: Library creation data with required fields:
            - name: Library name
            - language: Programming language
            - ecosystem: Package ecosystem (npm, pypi, etc.)
            And optional fields for description, URLs, metadata, etc.

    Returns:
        Created library with full metadata.

    Raises:
        HTTPException: 409 if library name already exists in ecosystem.
        HTTPException: 500 if database error occurs.

    Example:
        >>> POST /api/v1/libraries
        >>> {
        >>>   "name": "FastAPI",
        >>>   "language": "Python",
        >>>   "ecosystem": "pypi",
        >>>   "description": "Modern Python web framework",
        >>>   "keywords": ["web", "framework", "async"]
        >>> }
    """
    try:
        library_data = library_service.create_library(
            name=library.name,
            language=library.language,
            ecosystem=library.ecosystem,
            description=library.description,
            short_description=library.short_description,
            context7_id=library.context7_id,
            aliases=library.aliases,
            keywords=library.keywords,
            category=library.category,
            homepage_url=library.homepage_url,
            repository_url=library.repository_url,
            logo_url=library.logo_url,
            author=library.author,
            license=library.license,
        )
        return LibraryResponse(**library_data)
    except C7Error:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to create library: {str(e)}"
        )


@router.get("/{library_id}", response_model=LibraryResponse)
async def get_library(library_id: str) -> LibraryResponse:
    """Get library details by ID.

    Args:
        library_id: Library unique identifier.

    Returns:
        Library details with metadata and document count.

    Raises:
        HTTPException: 404 if library not found.
    """
    try:
        data = library_service.get_library(library_id)
        return LibraryResponse(**data)
    except C7Error:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to get library: {str(e)}"
        )


@router.put("/{library_id}", response_model=LibraryResponse)
async def update_library(
    library_id: str, library: LibraryUpdate
) -> LibraryResponse:
    """Update library (full update).

    Args:
        library_id: Library unique identifier.
        library: Full library update data.

    Returns:
        Updated library details.

    Raises:
        HTTPException: 404 if library not found.
        HTTPException: 409 if new name already exists.
    """
    try:
        data = library_service.update_library(
            library_id=library_id,
            name=library.name,
            description=library.description or "",
        )
        return LibraryResponse(**data)
    except C7Error:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to update library: {str(e)}"
        )


@router.patch("/{library_id}", response_model=LibraryResponse)
async def partial_update_library(
    library_id: str, library: LibraryPartialUpdate
) -> LibraryResponse:
    """Update library (partial update).

    Args:
        library_id: Library unique identifier.
        library: Partial library update data (only provided fields updated).

    Returns:
        Updated library details.

    Raises:
        HTTPException: 404 if library not found.
        HTTPException: 409 if new name already exists.
    """
    try:
        data = library_service.partial_update_library(
            library_id=library_id,
            name=library.name,
            description=library.description,
        )
        return LibraryResponse(**data)
    except C7Error:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to update library: {str(e)}"
        )


@router.delete("/{library_id}", response_model=DeleteResponse)
async def delete_library(library_id: str) -> DeleteResponse:
    """Delete a library.

    Args:
        library_id: Library unique identifier.

    Returns:
        Deletion status and message.

    Raises:
        HTTPException: 404 if library not found.
        HTTPException: 400 if library has documents.
    """
    try:
        library_service.delete_library(library_id)
        return DeleteResponse(
            success=True, message=f"Library '{library_id}' deleted successfully"
        )
    except C7Error:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to delete library: {str(e)}"
        )
