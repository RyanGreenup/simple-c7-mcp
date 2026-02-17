"""Document management service.

This module provides business logic for document CRUD operations,
including content management and embeddings.
"""

from datetime import datetime
from typing import TypedDict

from c7_mcp.exceptions import (
    C7Error,
    DocumentNotFoundError,
    EmbeddingDimensionError,
    EmbeddingsNotFoundError,
    LibraryNotFoundError,
    URLFetchError,
)


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
        raise LibraryNotFoundError(library_id)

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
    """
    import json
    import urllib.request
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
        raise LibraryNotFoundError(library_id)

    library = existing_lib[0]

    # 2. Fetch content from URL
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "c7-mcp/1.0"})
        with urllib.request.urlopen(req, timeout=30) as response:
            content = response.read().decode("utf-8", errors="replace")
            content_type = response.headers.get("Content-Type", "")
    except C7Error:
        raise
    except Exception as e:
        raise URLFetchError(url, str(e))

    # 3. Determine source_type from Content-Type or URL extension
    if "html" in content_type:
        source_type = "html"
    elif "json" in content_type:
        source_type = "json"
    elif url.endswith(".md"):
        source_type = "markdown"
    elif url.endswith(".rst"):
        source_type = "rst"
    else:
        source_type = "text"

    # 4. Generate unique document ID and store
    document_id = f"doc-{uuid.uuid4()}"
    zero_vector = [0.0] * 2560

    document_data = {
        "id": hash(document_id) & 0x7FFFFFFF,
        "document_id": document_id,
        "library_id": library_id,
        "title": title,
        "text": content,
        "chunk_index": 0,
        "chunk_total": 1,
        "source": url,
        "source_type": source_type,
        "vector": zero_vector,
        "metadata_json": json.dumps({"has_real_embeddings": False}),
        "created_at": now,
        "library_name": library["name"],
        "library_language": library["language"],
        "library_ecosystem": library["ecosystem"],
    }

    documents.add([document_data])

    return {
        "id": document_id,
        "title": title,
        "library_id": library_id,
        "content": content,
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
    """
    import json

    from c7_mcp.db import get_documents_table

    documents = get_documents_table()
    results = (
        documents.search()
        .where(f"document_id = '{doc_id}'", prefilter=True)
        .limit(1)
        .to_list()
    )
    if not results:
        raise DocumentNotFoundError(doc_id)
    chunk = results[0]
    metadata = json.loads(chunk.get("metadata_json", "{}"))
    return {
        "id": doc_id,
        "title": chunk["title"],
        "library_id": chunk["library_id"],
        "content": chunk["text"],
        "created_at": chunk["created_at"],
        "updated_at": chunk["created_at"],
        "has_embeddings": metadata.get("has_real_embeddings", False),
    }


def get_content(doc_id: str) -> str:
    """Get raw document content.

    Args:
        doc_id: Document unique identifier.

    Returns:
        Raw document content.

    Raises:
        ValueError: If document not found.
    """
    return get_document(doc_id)["content"]


def get_embeddings(doc_id: str) -> EmbeddingData:
    """Get document embeddings.

    Args:
        doc_id: Document unique identifier.

    Returns:
        Embedding data with vectors and metadata.

    Raises:
        ValueError: If document not found or has no embeddings.
    """
    import json

    from c7_mcp.db import get_documents_table

    documents = get_documents_table()
    results = (
        documents.search()
        .where(f"document_id = '{doc_id}'", prefilter=True)
        .limit(1)
        .to_list()
    )
    if not results:
        raise DocumentNotFoundError(doc_id)

    chunk = results[0]
    metadata = json.loads(chunk.get("metadata_json", "{}"))

    if not metadata.get("has_real_embeddings", False):
        raise EmbeddingsNotFoundError(doc_id)

    vector = chunk.get("vector", [])
    return {
        "embeddings": vector,
        "dimension": len(vector),
        "model": metadata.get("embedding_model"),
    }


def update_content(doc_id: str, content: str) -> DocumentData:
    """Update document content.

    Uses delete-then-re-add pattern since LanceDB has no UPDATE.

    Args:
        doc_id: Document unique identifier.
        content: New document content.

    Returns:
        Updated document data.

    Raises:
        ValueError: If document not found.
    """
    import json

    from c7_mcp.db import get_documents_table

    documents = get_documents_table()
    now = datetime.now()

    # 1. Query all chunks for this document
    results = (
        documents.search()
        .where(f"document_id = '{doc_id}'", prefilter=True)
        .limit(1000)
        .to_list()
    )
    if not results:
        raise DocumentNotFoundError(doc_id)

    # 2. Preserve metadata from first chunk
    first_chunk = results[0]
    original_created_at = first_chunk["created_at"]

    # 3. Delete all existing chunks
    documents.delete(f"document_id = '{doc_id}'")

    # 4. Re-add single chunk with new content
    zero_vector = [0.0] * 2560
    document_data = {
        "id": hash(doc_id) & 0x7FFFFFFF,
        "document_id": doc_id,
        "library_id": first_chunk["library_id"],
        "title": first_chunk["title"],
        "text": content,
        "chunk_index": 0,
        "chunk_total": 1,
        "source": first_chunk["source"],
        "source_type": first_chunk["source_type"],
        "vector": zero_vector,
        "metadata_json": json.dumps({"has_real_embeddings": False}),
        "created_at": original_created_at,
        "library_name": first_chunk["library_name"],
        "library_language": first_chunk["library_language"],
        "library_ecosystem": first_chunk["library_ecosystem"],
    }

    documents.add([document_data])

    return {
        "id": doc_id,
        "title": first_chunk["title"],
        "library_id": first_chunk["library_id"],
        "content": content,
        "created_at": original_created_at,
        "updated_at": now,
        "has_embeddings": False,
    }


def full_update_document(
    doc_id: str, title: str, content: str, library_id: str
) -> DocumentData:
    """Full document update (title, content, and library).

    Uses delete-then-re-add pattern since LanceDB has no UPDATE.
    Invalidates embeddings since content changes.

    Args:
        doc_id: Document unique identifier.
        title: New document title.
        content: New document content.
        library_id: Target library ID.

    Returns:
        Updated document data.

    Raises:
        ValueError: If document or target library not found.
    """
    import json

    from c7_mcp.db import get_documents_table, get_libraries_table

    documents = get_documents_table()
    now = datetime.now()

    # 1. Verify document exists
    results = (
        documents.search()
        .where(f"document_id = '{doc_id}'", prefilter=True)
        .limit(1000)
        .to_list()
    )
    if not results:
        raise DocumentNotFoundError(doc_id)

    first_chunk = results[0]
    original_created_at = first_chunk["created_at"]

    # 2. Verify target library exists
    libraries = get_libraries_table()
    lib_results = (
        libraries.search()
        .where(f"id = '{library_id}'", prefilter=True)
        .limit(1)
        .to_list()
    )
    if not lib_results:
        raise LibraryNotFoundError(library_id)

    library = lib_results[0]

    # 3. Delete all existing chunks
    documents.delete(f"document_id = '{doc_id}'")

    # 4. Re-add with all new values
    zero_vector = [0.0] * 2560
    document_data = {
        "id": hash(doc_id) & 0x7FFFFFFF,
        "document_id": doc_id,
        "library_id": library_id,
        "title": title,
        "text": content,
        "chunk_index": 0,
        "chunk_total": 1,
        "source": first_chunk["source"],
        "source_type": first_chunk["source_type"],
        "vector": zero_vector,
        "metadata_json": json.dumps({"has_real_embeddings": False}),
        "created_at": original_created_at,
        "library_name": library["name"],
        "library_language": library["language"],
        "library_ecosystem": library["ecosystem"],
    }

    documents.add([document_data])

    return {
        "id": doc_id,
        "title": title,
        "library_id": library_id,
        "content": content,
        "created_at": original_created_at,
        "updated_at": now,
        "has_embeddings": False,
    }


def update_title(doc_id: str, title: str) -> DocumentData:
    """Update document title.

    Uses delete-then-re-add pattern since LanceDB has no UPDATE.

    Args:
        doc_id: Document unique identifier.
        title: New document title.

    Returns:
        Updated document data.

    Raises:
        ValueError: If document not found.
    """
    import json

    from c7_mcp.db import get_documents_table

    documents = get_documents_table()
    now = datetime.now()

    results = (
        documents.search()
        .where(f"document_id = '{doc_id}'", prefilter=True)
        .limit(1000)
        .to_list()
    )
    if not results:
        raise DocumentNotFoundError(doc_id)

    first_chunk = results[0]
    original_created_at = first_chunk["created_at"]
    metadata = json.loads(first_chunk.get("metadata_json", "{}"))
    has_embeddings = metadata.get("has_real_embeddings", False)

    documents.delete(f"document_id = '{doc_id}'")

    document_data = {
        "id": hash(doc_id) & 0x7FFFFFFF,
        "document_id": doc_id,
        "library_id": first_chunk["library_id"],
        "title": title,
        "text": first_chunk["text"],
        "chunk_index": 0,
        "chunk_total": 1,
        "source": first_chunk["source"],
        "source_type": first_chunk["source_type"],
        "vector": first_chunk["vector"],
        "metadata_json": first_chunk["metadata_json"],
        "created_at": original_created_at,
        "library_name": first_chunk["library_name"],
        "library_language": first_chunk["library_language"],
        "library_ecosystem": first_chunk["library_ecosystem"],
    }

    documents.add([document_data])

    return {
        "id": doc_id,
        "title": title,
        "library_id": first_chunk["library_id"],
        "content": first_chunk["text"],
        "created_at": original_created_at,
        "updated_at": now,
        "has_embeddings": has_embeddings,
    }


def update_library(doc_id: str, library_id: str) -> DocumentData:
    """Move document to a different library.

    Uses delete-then-re-add pattern since LanceDB has no UPDATE.

    Args:
        doc_id: Document unique identifier.
        library_id: Target library ID.

    Returns:
        Updated document data.

    Raises:
        ValueError: If document or target library not found.
    """
    import json

    from c7_mcp.db import get_documents_table, get_libraries_table

    documents = get_documents_table()
    now = datetime.now()

    # 1. Verify document exists
    results = (
        documents.search()
        .where(f"document_id = '{doc_id}'", prefilter=True)
        .limit(1000)
        .to_list()
    )
    if not results:
        raise DocumentNotFoundError(doc_id)

    first_chunk = results[0]
    original_created_at = first_chunk["created_at"]
    metadata = json.loads(first_chunk.get("metadata_json", "{}"))
    has_embeddings = metadata.get("has_real_embeddings", False)

    # 2. Verify target library exists
    libraries = get_libraries_table()
    lib_results = (
        libraries.search()
        .where(f"id = '{library_id}'", prefilter=True)
        .limit(1)
        .to_list()
    )
    if not lib_results:
        raise LibraryNotFoundError(library_id)

    library = lib_results[0]

    # 3. Delete and re-add with new library
    documents.delete(f"document_id = '{doc_id}'")

    document_data = {
        "id": hash(doc_id) & 0x7FFFFFFF,
        "document_id": doc_id,
        "library_id": library_id,
        "title": first_chunk["title"],
        "text": first_chunk["text"],
        "chunk_index": 0,
        "chunk_total": 1,
        "source": first_chunk["source"],
        "source_type": first_chunk["source_type"],
        "vector": first_chunk["vector"],
        "metadata_json": first_chunk["metadata_json"],
        "created_at": original_created_at,
        "library_name": library["name"],
        "library_language": library["language"],
        "library_ecosystem": library["ecosystem"],
    }

    documents.add([document_data])

    return {
        "id": doc_id,
        "title": first_chunk["title"],
        "library_id": library_id,
        "content": first_chunk["text"],
        "created_at": original_created_at,
        "updated_at": now,
        "has_embeddings": has_embeddings,
    }


def update_embeddings(
    doc_id: str, embeddings: list[float], model: str | None = None
) -> DocumentData:
    """Update document embeddings.

    Uses delete-then-re-add pattern since LanceDB has no UPDATE.

    Args:
        doc_id: Document unique identifier.
        embeddings: New embedding values.
        model: Model used to generate embeddings.

    Returns:
        Updated document data.

    Raises:
        ValueError: If document not found or dimension mismatch.
    """
    import json

    from c7_mcp.db import get_documents_table

    documents = get_documents_table()
    now = datetime.now()

    results = (
        documents.search()
        .where(f"document_id = '{doc_id}'", prefilter=True)
        .limit(1000)
        .to_list()
    )
    if not results:
        raise DocumentNotFoundError(doc_id)

    first_chunk = results[0]
    original_created_at = first_chunk["created_at"]

    # Validate dimension (must match configured vector size of 2560)
    expected_dim = len(first_chunk["vector"])
    if len(embeddings) != expected_dim:
        raise EmbeddingDimensionError(len(embeddings), expected_dim)

    documents.delete(f"document_id = '{doc_id}'")

    metadata: dict[str, bool | str] = {"has_real_embeddings": True}
    if model:
        metadata["embedding_model"] = model

    document_data = {
        "id": hash(doc_id) & 0x7FFFFFFF,
        "document_id": doc_id,
        "library_id": first_chunk["library_id"],
        "title": first_chunk["title"],
        "text": first_chunk["text"],
        "chunk_index": 0,
        "chunk_total": 1,
        "source": first_chunk["source"],
        "source_type": first_chunk["source_type"],
        "vector": embeddings,
        "metadata_json": json.dumps(metadata),
        "created_at": original_created_at,
        "library_name": first_chunk["library_name"],
        "library_language": first_chunk["library_language"],
        "library_ecosystem": first_chunk["library_ecosystem"],
    }

    documents.add([document_data])

    return {
        "id": doc_id,
        "title": first_chunk["title"],
        "library_id": first_chunk["library_id"],
        "content": first_chunk["text"],
        "created_at": original_created_at,
        "updated_at": now,
        "has_embeddings": True,
    }


def delete_document(doc_id: str) -> bool:
    """Delete a document and all its chunks.

    Args:
        doc_id: Document unique identifier.

    Returns:
        True if deletion was successful.

    Raises:
        ValueError: If document not found.
    """
    from c7_mcp.db import get_documents_table

    documents = get_documents_table()

    # Verify document exists
    results = (
        documents.search()
        .where(f"document_id = '{doc_id}'", prefilter=True)
        .limit(1)
        .to_list()
    )
    if not results:
        raise DocumentNotFoundError(doc_id)

    # Delete all chunks for this document
    documents.delete(f"document_id = '{doc_id}'")

    return True
