"""Library management router.

This module implements RESTful CRUD endpoints for library management.
"""

from fastapi import APIRouter, HTTPException

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
        # Call service function
        libraries = library_service.list_libraries()

        # Transform LibraryData to LibraryResponse
        return [LibraryResponse(**lib) for lib in libraries]

    except Exception as e:
        # Handle unexpected errors
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
        HTTPException: 400 if library name already exists in ecosystem.
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
        # Call service layer
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

        # Transform to response model
        return LibraryResponse(**library_data)

    except ValueError as e:
        # Handle duplicate name or validation errors
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        # Handle unexpected errors
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
        HTTPException: 501 if not implemented yet.

    TODO: Implement library retrieval endpoint.
    TODO: 1. Call library_service.get_library()
    TODO: 2. Transform LibraryData to LibraryResponse
    TODO: 3. Handle not found errors (404)
    TODO: 4. Handle other errors (500)
    """
    raise HTTPException(status_code=501, detail="Not implemented")


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
        HTTPException: 400 if new name already exists.
        HTTPException: 501 if not implemented yet.

    TODO: Implement library full update endpoint.
    TODO: 1. Call library_service.update_library()
    TODO: 2. Transform LibraryData to LibraryResponse
    TODO: 3. Handle not found errors (404)
    TODO: 4. Handle duplicate name errors (400)
    TODO: 5. Handle other errors (500)
    """
    raise HTTPException(status_code=501, detail="Not implemented")


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
        HTTPException: 400 if new name already exists.
        HTTPException: 501 if not implemented yet.

    TODO: Implement library partial update endpoint.
    TODO: 1. Call library_service.partial_update_library()
    TODO: 2. Transform LibraryData to LibraryResponse
    TODO: 3. Handle not found errors (404)
    TODO: 4. Handle duplicate name errors (400)
    TODO: 5. Handle other errors (500)
    """
    raise HTTPException(status_code=501, detail="Not implemented")


@router.delete("/{library_id}", response_model=DeleteResponse)
async def delete_library(library_id: str) -> DeleteResponse:
    """Delete a library.

    Args:
        library_id: Library unique identifier.

    Returns:
        Deletion status and message.

    Raises:
        HTTPException: 404 if library not found.
        HTTPException: 400 if library has documents (decide on cascade behavior).
        HTTPException: 501 if not implemented yet.

    TODO: Implement library deletion endpoint.
    TODO: 1. Call library_service.delete_library()
    TODO: 2. Return DeleteResponse with success=True
    TODO: 3. Handle not found errors (404)
    TODO: 4. Handle libraries with documents (400 or cascade delete)
    TODO: 5. Handle other errors (500)
    """
    raise HTTPException(status_code=501, detail="Not implemented")
