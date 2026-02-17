"""Document management router.

This module implements RESTful CRUD endpoints for document management,
including content upload, URL fetching, and various update operations.
"""

from fastapi import APIRouter, HTTPException, Query

from c7_mcp.exceptions import C7Error
from c7_mcp.schemas.document import (
    ContentUpdate,
    DocumentContent,
    DocumentCreate,
    DocumentEmbeddings,
    DocumentFetch,
    DocumentPretty,
    DocumentResponse,
    DocumentTitle,
    DocumentUpdate,
    EmbeddingsUpdate,
    LibraryAssignment,
    TitleUpdate,
)
from c7_mcp.schemas.library import DeleteResponse
from c7_mcp.services import document as document_service

router = APIRouter(prefix="/api/v1/documents", tags=["documents"])


@router.get("", response_model=list[DocumentResponse])
async def list_documents(
    library_id: str | None = Query(None, description="Filter by library ID"),
    limit: int = Query(100, ge=1, le=1000, description="Maximum documents to return"),
    offset: int = Query(0, ge=0, description="Number of documents to skip"),
) -> list[DocumentResponse]:
    """List documents with optional filtering and pagination.

    Args:
        library_id: Filter documents by library (optional).
        limit: Maximum number of documents to return (1-1000).
        offset: Number of documents to skip for pagination.

    Returns:
        List of documents with metadata (no content).

    Raises:
        HTTPException: 500 if internal server error.
    """
    try:
        documents = document_service.list_documents(
            library_id=library_id, limit=limit, offset=offset
        )
        return [
            DocumentResponse(
                id=doc["id"],
                title=doc["title"],
                library_id=doc["library_id"],
                created_at=doc["created_at"],
                updated_at=doc["updated_at"],
                has_embeddings=doc["has_embeddings"],
            )
            for doc in documents
        ]
    except C7Error:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to list documents: {str(e)}"
        )


@router.post("", response_model=DocumentResponse, status_code=201)
async def create_document(document: DocumentCreate) -> DocumentResponse:
    """Create a document by uploading content.

    Args:
        document: Document creation data (title, content, library_id).

    Returns:
        Created document with metadata.

    Raises:
        HTTPException: 404 if library not found.
        HTTPException: 500 if internal server error.
    """
    try:
        data = document_service.create_document(
            title=document.title,
            content=document.content,
            library_id=document.library_id,
        )
        return DocumentResponse(
            id=data["id"],
            title=data["title"],
            library_id=data["library_id"],
            created_at=data["created_at"],
            updated_at=data["updated_at"],
            has_embeddings=data["has_embeddings"],
        )
    except C7Error:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to create document: {str(e)}"
        )


@router.post("/fetch", response_model=DocumentResponse, status_code=201)
async def fetch_document(document: DocumentFetch) -> DocumentResponse:
    """Create a document by fetching content from URL.

    Args:
        document: Document fetch data (title, url, library_id).

    Returns:
        Created document with metadata.

    Raises:
        HTTPException: 404 if library not found.
        HTTPException: 400 if URL fetch fails.
    """
    try:
        data = document_service.fetch_document(
            title=document.title,
            url=str(document.url),
            library_id=document.library_id,
        )
        return DocumentResponse(
            id=data["id"],
            title=data["title"],
            library_id=data["library_id"],
            created_at=data["created_at"],
            updated_at=data["updated_at"],
            has_embeddings=data["has_embeddings"],
        )
    except C7Error:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to fetch document: {str(e)}"
        )


@router.get("/{doc_id}", response_model=DocumentResponse)
async def get_document(doc_id: str) -> DocumentResponse:
    """Get document metadata by ID (without content).

    Args:
        doc_id: Document unique identifier.

    Returns:
        Document metadata (no content).

    Raises:
        HTTPException: 404 if document not found.
    """
    try:
        data = document_service.get_document(doc_id)
        return DocumentResponse(
            id=data["id"],
            title=data["title"],
            library_id=data["library_id"],
            created_at=data["created_at"],
            updated_at=data["updated_at"],
            has_embeddings=data["has_embeddings"],
        )
    except C7Error:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to get document: {str(e)}"
        )


@router.get("/{doc_id}/content", response_model=DocumentContent)
async def get_document_content(doc_id: str) -> DocumentContent:
    """Get raw document content.

    Args:
        doc_id: Document unique identifier.

    Returns:
        Raw document content.

    Raises:
        HTTPException: 404 if document not found.
    """
    try:
        content = document_service.get_content(doc_id)
        return DocumentContent(content=content)
    except C7Error:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to get content: {str(e)}"
        )


@router.get("/{doc_id}/pretty", response_model=DocumentPretty)
async def get_document_pretty(doc_id: str) -> DocumentPretty:
    """Get formatted document (title + content).

    Args:
        doc_id: Document unique identifier.

    Returns:
        Formatted document with title and content.

    Raises:
        HTTPException: 404 if document not found.
    """
    try:
        data = document_service.get_document(doc_id)
        return DocumentPretty(title=data["title"], content=data["content"])
    except C7Error:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to get document: {str(e)}"
        )


@router.get("/{doc_id}/title", response_model=DocumentTitle)
async def get_document_title(doc_id: str) -> DocumentTitle:
    """Get document title only.

    Args:
        doc_id: Document unique identifier.

    Returns:
        Document title.

    Raises:
        HTTPException: 404 if document not found.
    """
    try:
        data = document_service.get_document(doc_id)
        return DocumentTitle(title=data["title"])
    except C7Error:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to get title: {str(e)}"
        )


@router.get("/{doc_id}/embeddings", response_model=DocumentEmbeddings)
async def get_document_embeddings(doc_id: str) -> DocumentEmbeddings:
    """Get document embeddings.

    Args:
        doc_id: Document unique identifier.

    Returns:
        Document embeddings with dimension and model info.

    Raises:
        HTTPException: 404 if document not found or has no embeddings.
    """
    try:
        data = document_service.get_embeddings(doc_id)
        return DocumentEmbeddings(
            embeddings=data["embeddings"],
            dimension=data["dimension"],
            model=data["model"],
        )
    except C7Error:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to get embeddings: {str(e)}"
        )


@router.put("/{doc_id}", response_model=DocumentResponse)
async def update_document(doc_id: str, document: DocumentUpdate) -> DocumentResponse:
    """Update document (full update).

    Args:
        doc_id: Document unique identifier.
        document: Full document update data.

    Returns:
        Updated document metadata.

    Raises:
        HTTPException: 404 if document or target library not found.
    """
    try:
        data = document_service.full_update_document(
            doc_id=doc_id,
            title=document.title,
            content=document.content,
            library_id=document.library_id,
        )
        return DocumentResponse(
            id=data["id"],
            title=data["title"],
            library_id=data["library_id"],
            created_at=data["created_at"],
            updated_at=data["updated_at"],
            has_embeddings=data["has_embeddings"],
        )
    except C7Error:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to update document: {str(e)}"
        )


@router.patch("/{doc_id}/content", response_model=DocumentResponse)
async def update_document_content(
    doc_id: str, content_update: ContentUpdate
) -> DocumentResponse:
    """Update document content only.

    Args:
        doc_id: Document unique identifier.
        content_update: New content.

    Returns:
        Updated document metadata.

    Raises:
        HTTPException: 404 if document not found.
    """
    try:
        data = document_service.update_content(doc_id, content_update.content)
        return DocumentResponse(
            id=data["id"],
            title=data["title"],
            library_id=data["library_id"],
            created_at=data["created_at"],
            updated_at=data["updated_at"],
            has_embeddings=data["has_embeddings"],
        )
    except C7Error:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to update content: {str(e)}"
        )


@router.patch("/{doc_id}/title", response_model=DocumentResponse)
async def update_document_title(
    doc_id: str, title_update: TitleUpdate
) -> DocumentResponse:
    """Update document title only.

    Args:
        doc_id: Document unique identifier.
        title_update: New title.

    Returns:
        Updated document metadata.

    Raises:
        HTTPException: 404 if document not found.
    """
    try:
        data = document_service.update_title(doc_id, title_update.title)
        return DocumentResponse(
            id=data["id"],
            title=data["title"],
            library_id=data["library_id"],
            created_at=data["created_at"],
            updated_at=data["updated_at"],
            has_embeddings=data["has_embeddings"],
        )
    except C7Error:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to update title: {str(e)}"
        )


@router.patch("/{doc_id}/library", response_model=DocumentResponse)
async def update_document_library(
    doc_id: str, library_assignment: LibraryAssignment
) -> DocumentResponse:
    """Move document to a different library.

    Args:
        doc_id: Document unique identifier.
        library_assignment: Target library ID.

    Returns:
        Updated document metadata.

    Raises:
        HTTPException: 404 if document or target library not found.
    """
    try:
        data = document_service.update_library(
            doc_id, library_assignment.library_id
        )
        return DocumentResponse(
            id=data["id"],
            title=data["title"],
            library_id=data["library_id"],
            created_at=data["created_at"],
            updated_at=data["updated_at"],
            has_embeddings=data["has_embeddings"],
        )
    except C7Error:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to move document: {str(e)}"
        )


@router.patch("/{doc_id}/embeddings", response_model=DocumentResponse)
async def update_document_embeddings(
    doc_id: str, embeddings_update: EmbeddingsUpdate
) -> DocumentResponse:
    """Update document embeddings.

    Args:
        doc_id: Document unique identifier.
        embeddings_update: New embeddings and optional model info.

    Returns:
        Updated document metadata.

    Raises:
        HTTPException: 404 if document not found.
        HTTPException: 400 if embedding dimension inconsistent.
    """
    try:
        data = document_service.update_embeddings(
            doc_id,
            embeddings_update.embeddings,
            model=embeddings_update.model,
        )
        return DocumentResponse(
            id=data["id"],
            title=data["title"],
            library_id=data["library_id"],
            created_at=data["created_at"],
            updated_at=data["updated_at"],
            has_embeddings=data["has_embeddings"],
        )
    except C7Error:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to update embeddings: {str(e)}"
        )


@router.delete("/{doc_id}", response_model=DeleteResponse)
async def delete_document(doc_id: str) -> DeleteResponse:
    """Delete a document.

    Args:
        doc_id: Document unique identifier.

    Returns:
        Deletion status and message.

    Raises:
        HTTPException: 404 if document not found.
    """
    try:
        document_service.delete_document(doc_id)
        return DeleteResponse(
            success=True, message=f"Document '{doc_id}' deleted successfully"
        )
    except C7Error:
        raise
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"Failed to delete document: {str(e)}"
        )
