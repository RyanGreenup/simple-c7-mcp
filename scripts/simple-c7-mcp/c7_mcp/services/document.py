"""Document management service.

This module provides business logic for document CRUD operations,
including content management and embeddings.
"""

from datetime import datetime
from typing import TypedDict


class DocumentData(TypedDict):
    """Document data structure.

    Attributes:
        id: Document unique identifier.
        title: Document title.
        library_id: Library this document belongs to.
        content: Document content (raw text).
        created_at: Creation timestamp.
        updated_at: Last update timestamp.
        has_embeddings: Whether document has embeddings.
    """

    id: str
    title: str
    library_id: str
    content: str
    created_at: datetime
    updated_at: datetime
    has_embeddings: bool


class EmbeddingData(TypedDict):
    """Embedding data structure.

    Attributes:
        embeddings: List of embedding values.
        dimension: Embedding dimension.
        model: Model used to generate embeddings.
    """

    embeddings: list[float]
    dimension: int
    model: str | None


def list_documents(
    library_id: str | None = None, limit: int = 100, offset: int = 0
) -> list[DocumentData]:
    """List documents, optionally filtered by library.

    Args:
        library_id: Filter by library ID (optional).
        limit: Maximum number of documents to return.
        offset: Number of documents to skip.

    Returns:
        List of documents with metadata.
    """
    import json

    from c7_mcp.db import get_documents_table

    documents = get_documents_table()

    # Query documents with optional library filter
    if library_id:
        results = (
            documents.search()
            .where(f"library_id = '{library_id}'", prefilter=True)
            .limit(limit)
            .to_list()
        )
    else:
        results = documents.search().limit(limit).to_list()

    # Group chunks by document_id and return unique documents
    seen_docs = {}
    for chunk in results:
        doc_id = chunk["document_id"]
        if doc_id not in seen_docs:
            # Check metadata for real embeddings flag
            metadata = json.loads(chunk.get("metadata_json", "{}"))
            has_embeddings = metadata.get("has_real_embeddings", False)

            seen_docs[doc_id] = {
                "id": doc_id,
                "title": chunk["title"],
                "library_id": chunk["library_id"],
                "content": chunk["text"],  # Use first chunk's text as content
                "created_at": chunk["created_at"],
                "updated_at": chunk["created_at"],  # No separate updated_at yet
                "has_embeddings": has_embeddings,
            }

    return list(seen_docs.values())[offset : offset + limit]


def create_document(title: str, content: str, library_id: str) -> DocumentData:
    """Create a document by uploading content.

    Args:
        title: Document title.
        content: Document content (raw text).
        library_id: Library to add document to.

    Returns:
        Created document data.

    Raises:
        ValueError: If library not found.
    """
    import json
    import uuid

    from c7_mcp.db import get_documents_table, get_libraries_table

    libraries = get_libraries_table()
    documents = get_documents_table()
    now = datetime.now()

    # 1. Verify library exists
    existing_lib = (
        libraries.search()
        .where(f"id = '{library_id}'", prefilter=True)
        .limit(1)
        .to_list()
    )

    if not existing_lib:
        raise ValueError(f"Library with ID '{library_id}' not found")

    library = existing_lib[0]

    # 2. Generate unique document ID
    document_id = f"doc-{uuid.uuid4()}"

    # 3. Store content as a single chunk without real embeddings
    # We use a zero vector as placeholder since embeddings will be generated later
    # LanceDB requires vectors to exist, so we create a dummy 2560-dim zero vector
    zero_vector = [0.0] * 2560

    document_data = {
        "id": hash(document_id) & 0x7FFFFFFF,  # Convert to positive int
        "document_id": document_id,
        "library_id": library_id,
        "title": title,
        "text": content,
        "chunk_index": 0,
        "chunk_total": 1,
        "source": "uploaded",
        "source_type": "text",
        "vector": zero_vector,
        "metadata_json": json.dumps({"has_real_embeddings": False}),
        "created_at": now,
        "library_name": library["name"],
        "library_language": library["language"],
        "library_ecosystem": library["ecosystem"],
    }

    # 4. Store in database
    documents.add([document_data])

    # 5. Update library document count
    # Note: LanceDB doesn't support UPDATE, so we need to delete and re-add
    # For now, we skip this and handle it in a future enhancement
    # TODO: Implement document count updates

    # 6. Return DocumentData TypedDict
    return {
        "id": document_id,
        "title": title,
        "library_id": library_id,
        "content": content,
        "created_at": now,
        "updated_at": now,
        "has_embeddings": False,
    }


def fetch_document(title: str, url: str, library_id: str) -> DocumentData:
    """Create a document by fetching content from URL.

    Args:
        title: Document title.
        url: URL to fetch content from.
        library_id: Library to add document to.

    Returns:
        Created document data.

    Raises:
        ValueError: If library not found or URL fetch fails.

    TODO: Implement document fetch logic.
    TODO: 1. Verify library exists
    TODO: 2. Fetch content from URL (handle timeouts, errors)
    TODO: 3. Parse content (handle different formats: HTML, PDF, etc.)
    TODO: 4. Generate unique ID
    TODO: 5. Store parsed content
    TODO: 6. Update library document count
    """
    # Placeholder implementation
    now = datetime.now()
    return {
        "id": "doc-placeholder",
        "title": title,
        "library_id": library_id,
        "content": f"Content fetched from {url}",
        "created_at": now,
        "updated_at": now,
        "has_embeddings": False,
    }


def get_document(doc_id: str) -> DocumentData:
    """Get document details by ID.

    Args:
        doc_id: Document unique identifier.

    Returns:
        Document data with metadata and content.

    Raises:
        ValueError: If document not found.

    TODO: Implement document retrieval logic.
    TODO: 1. Query database by ID
    TODO: 2. Include all metadata
    TODO: 3. Raise ValueError if not found
    """
    # Placeholder implementation
    now = datetime.now()
    return {
        "id": doc_id,
        "title": "Placeholder Document",
        "library_id": "lib-placeholder",
        "content": "Placeholder content",
        "created_at": now,
        "updated_at": now,
        "has_embeddings": False,
    }


def get_content(doc_id: str) -> str:
    """Get raw document content.

    Args:
        doc_id: Document unique identifier.

    Returns:
        Raw document content.

    Raises:
        ValueError: If document not found.

    TODO: Implement content retrieval logic.
    TODO: 1. Query database by ID
    TODO: 2. Return only content field
    TODO: 3. Raise ValueError if not found
    """
    # Placeholder implementation
    return "Placeholder content"


def get_embeddings(doc_id: str) -> EmbeddingData:
    """Get document embeddings.

    Args:
        doc_id: Document unique identifier.

    Returns:
        Embedding data with vectors and metadata.

    Raises:
        ValueError: If document not found or has no embeddings.

    TODO: Implement embeddings retrieval logic.
    TODO: 1. Query database by ID
    TODO: 2. Verify embeddings exist
    TODO: 3. Return embedding vector and metadata
    TODO: 4. Raise ValueError if not found or no embeddings
    """
    # Placeholder implementation
    return {
        "embeddings": [0.1, 0.2, 0.3],
        "dimension": 3,
        "model": "placeholder-model",
    }


def update_content(doc_id: str, content: str) -> DocumentData:
    """Update document content.

    Args:
        doc_id: Document unique identifier.
        content: New document content.

    Returns:
        Updated document data.

    Raises:
        ValueError: If document not found.

    TODO: Implement content update logic.
    TODO: 1. Verify document exists
    TODO: 2. Update content field
    TODO: 3. Invalidate embeddings (set has_embeddings to False)
    TODO: 4. Update updated_at timestamp
    """
    # Placeholder implementation
    now = datetime.now()
    return {
        "id": doc_id,
        "title": "Placeholder Document",
        "library_id": "lib-placeholder",
        "content": content,
        "created_at": now,
        "updated_at": now,
        "has_embeddings": False,
    }


def update_title(doc_id: str, title: str) -> DocumentData:
    """Update document title.

    Args:
        doc_id: Document unique identifier.
        title: New document title.

    Returns:
        Updated document data.

    Raises:
        ValueError: If document not found.

    TODO: Implement title update logic.
    TODO: 1. Verify document exists
    TODO: 2. Update title field
    TODO: 3. Update updated_at timestamp
    """
    # Placeholder implementation
    now = datetime.now()
    return {
        "id": doc_id,
        "title": title,
        "library_id": "lib-placeholder",
        "content": "Placeholder content",
        "created_at": now,
        "updated_at": now,
        "has_embeddings": False,
    }


def update_library(doc_id: str, library_id: str) -> DocumentData:
    """Move document to a different library.

    Args:
        doc_id: Document unique identifier.
        library_id: Target library ID.

    Returns:
        Updated document data.

    Raises:
        ValueError: If document or target library not found.

    TODO: Implement library assignment logic.
    TODO: 1. Verify document exists
    TODO: 2. Verify target library exists
    TODO: 3. Update library_id field
    TODO: 4. Update document counts for both libraries
    TODO: 5. Update updated_at timestamp
    """
    # Placeholder implementation
    now = datetime.now()
    return {
        "id": doc_id,
        "title": "Placeholder Document",
        "library_id": library_id,
        "content": "Placeholder content",
        "created_at": now,
        "updated_at": now,
        "has_embeddings": False,
    }


def update_embeddings(
    doc_id: str, embeddings: list[float], model: str | None = None
) -> DocumentData:
    """Update document embeddings.

    Args:
        doc_id: Document unique identifier.
        embeddings: New embedding values.
        model: Model used to generate embeddings.

    Returns:
        Updated document data.

    Raises:
        ValueError: If document not found.

    TODO: Implement embeddings update logic.
    TODO: 1. Verify document exists
    TODO: 2. Validate embedding dimension consistency
    TODO: 3. Store embeddings and model info
    TODO: 4. Set has_embeddings to True
    TODO: 5. Update updated_at timestamp
    """
    # Placeholder implementation
    now = datetime.now()
    return {
        "id": doc_id,
        "title": "Placeholder Document",
        "library_id": "lib-placeholder",
        "content": "Placeholder content",
        "created_at": now,
        "updated_at": now,
        "has_embeddings": True,
    }


def delete_document(doc_id: str) -> bool:
    """Delete a document.

    Args:
        doc_id: Document unique identifier.

    Returns:
        True if deletion was successful.

    Raises:
        ValueError: If document not found.

    TODO: Implement document deletion logic.
    TODO: 1. Verify document exists
    TODO: 2. Delete document from database
    TODO: 3. Delete associated embeddings
    TODO: 4. Update library document count
    TODO: 5. Clean up associated resources
    """
    # Placeholder implementation
    return True
