"""Library management service.

This module provides business logic for library CRUD operations.
"""

import uuid
from datetime import datetime
from typing import TypedDict

from c7_mcp.db import get_libraries_table


class LibraryData(TypedDict):
    """Library data structure.

    Attributes:
        id: Library unique identifier.
        name: Library name.
        context7_id: Context7 compatible path.
        language: Primary programming language.
        ecosystem: Package ecosystem.
        description: Library description.
        short_description: One-liner summary.
        aliases: Alternative names.
        keywords: Searchable terms.
        category: Library type.
        homepage_url: Official website.
        repository_url: Source code URL.
        author: Creator/maintainer.
        license: License type.
        status: Library status.
        popularity_score: Popularity metric.
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
    document_count: int


def list_libraries() -> list[LibraryData]:
    """List all libraries.

    Returns:
        List of all libraries with their metadata.
    """
    libraries = get_libraries_table()

    # Query all libraries
    results = libraries.search().limit(1000).to_list()

    # Convert to LibraryData format
    library_list = []
    for lib in results:
        library_list.append({
            "id": lib["id"],
            "name": lib["name"],
            "context7_id": lib["context7_id"],
            "language": lib["language"],
            "ecosystem": lib["ecosystem"],
            "description": lib["description"],
            "short_description": lib["short_description"],
            "aliases": lib["aliases"],
            "keywords": lib["keywords"],
            "category": lib["category"],
            "homepage_url": lib["homepage_url"],
            "repository_url": lib["repository_url"],
            "author": lib["author"],
            "license": lib["license"],
            "status": lib["status"],
            "popularity_score": lib["popularity_score"],
            "created_at": lib["created_at"],
            "updated_at": lib["updated_at"],
            "document_count": lib["document_count"],
        })

    return library_list


def create_library(
    name: str,
    language: str,
    ecosystem: str,
    description: str = "",
    short_description: str = "",
    context7_id: str | None = None,
    aliases: list[str] | None = None,
    keywords: list[str] | None = None,
    category: str = "",
    homepage_url: str = "",
    repository_url: str = "",
    logo_url: str = "",
    author: str = "",
    license: str = "",
) -> LibraryData:
    """Create a new library.

    Args:
        name: Library name (required).
        language: Primary programming language (required).
        ecosystem: Package ecosystem (required).
        description: Full library description.
        short_description: One-liner summary.
        context7_id: Context7 path, auto-generated if not provided.
        aliases: Alternative names.
        keywords: Searchable terms.
        category: Library type.
        homepage_url: Official website.
        repository_url: Source code URL.
        logo_url: Library logo URL.
        author: Creator/maintainer.
        license: License type.

    Returns:
        Created library data.

    Raises:
        ValueError: If library name already exists in the ecosystem.
    """
    libraries = get_libraries_table()
    now = datetime.now()

    # 1. Validate name uniqueness within ecosystem
    existing = (
        libraries.search()
        .where(f"name = '{name}' AND ecosystem = '{ecosystem}'", prefilter=True)
        .limit(1)
        .to_list()
    )

    if existing:
        raise ValueError(
            f"Library '{name}' already exists in ecosystem '{ecosystem}'"
        )

    # 2. Generate unique ID
    unique_suffix = str(uuid.uuid4())[:8]
    lib_id = f"lib-{ecosystem}-{name.lower().replace(' ', '-')}-{unique_suffix}"

    # 3. Auto-generate context7_id if not provided
    if context7_id is None:
        # Format: /{ecosystem}/{normalized-name}
        normalized_name = name.lower().replace(" ", "-")
        context7_id = f"/{ecosystem}/{normalized_name}"

    # 4. Prepare library data
    library_data = {
        "id": lib_id,
        "name": name,
        "context7_id": context7_id,
        "language": language,
        "ecosystem": ecosystem,
        "description": description,
        "short_description": short_description,
        "aliases": aliases or [],
        "keywords": keywords or [],
        "category": category,
        "homepage_url": homepage_url,
        "repository_url": repository_url,
        "logo_url": logo_url,  # Added missing field
        "author": author,
        "license": license,
        "status": "active",
        "popularity_score": 0,
        "github_stars": 0,
        "npm_downloads_weekly": 0,
        "pypi_downloads_monthly": 0,
        "doc_version": "",
        "doc_source_type": "",
        "doc_completeness": 0.0,
        "last_indexed_at": None,
        "related_libraries": [],
        "alternative_to": [],
        "supersedes": [],
        "requires_libraries": [],
        "first_release_date": None,
        "last_release_date": None,
        "created_at": now,
        "updated_at": now,
        "document_count": 0,
    }

    # 5. Store in database
    libraries.add([library_data])

    # 6. Return LibraryData TypedDict
    return {
        "id": lib_id,
        "name": name,
        "context7_id": context7_id,
        "language": language,
        "ecosystem": ecosystem,
        "description": description,
        "short_description": short_description,
        "aliases": aliases or [],
        "keywords": keywords or [],
        "category": category,
        "homepage_url": homepage_url,
        "repository_url": repository_url,
        "author": author,
        "license": license,
        "status": "active",
        "popularity_score": 0,
        "created_at": now,
        "updated_at": now,
        "document_count": 0,
    }


def get_library(library_id: str) -> LibraryData:
    """Get library details by ID.

    Args:
        library_id: Library unique identifier.

    Returns:
        Library data.

    Raises:
        ValueError: If library not found.
    """
    libraries = get_libraries_table()
    results = (
        libraries.search()
        .where(f"id = '{library_id}'", prefilter=True)
        .limit(1)
        .to_list()
    )
    if not results:
        raise ValueError(f"Library '{library_id}' not found")
    lib = results[0]
    return {
        "id": lib["id"],
        "name": lib["name"],
        "context7_id": lib["context7_id"],
        "language": lib["language"],
        "ecosystem": lib["ecosystem"],
        "description": lib["description"],
        "short_description": lib["short_description"],
        "aliases": lib["aliases"],
        "keywords": lib["keywords"],
        "category": lib["category"],
        "homepage_url": lib["homepage_url"],
        "repository_url": lib["repository_url"],
        "author": lib["author"],
        "license": lib["license"],
        "status": lib["status"],
        "popularity_score": lib["popularity_score"],
        "created_at": lib["created_at"],
        "updated_at": lib["updated_at"],
        "document_count": lib["document_count"],
    }


def update_library(
    library_id: str, name: str, description: str = ""
) -> LibraryData:
    """Update library (full update).

    Uses delete-then-re-add pattern since LanceDB has no UPDATE.

    Args:
        library_id: Library unique identifier.
        name: New library name.
        description: New library description.

    Returns:
        Updated library data.

    Raises:
        ValueError: If library not found or name conflicts.
    """
    libraries = get_libraries_table()
    now = datetime.now()

    # 1. Verify library exists
    existing = (
        libraries.search()
        .where(f"id = '{library_id}'", prefilter=True)
        .limit(1)
        .to_list()
    )
    if not existing:
        raise ValueError(f"Library '{library_id}' not found")

    lib = existing[0]

    # 2. Validate name uniqueness (excluding current library)
    if name != lib["name"]:
        duplicates = (
            libraries.search()
            .where(
                f"name = '{name}' AND ecosystem = '{lib['ecosystem']}'",
                prefilter=True,
            )
            .limit(1)
            .to_list()
        )
        if duplicates:
            raise ValueError(
                f"Library '{name}' already exists in ecosystem '{lib['ecosystem']}'"
            )

    # 3. Delete and re-add with updated fields
    libraries.delete(f"id = '{library_id}'")

    updated_data = {
        "id": lib["id"],
        "name": name,
        "context7_id": lib["context7_id"],
        "language": lib["language"],
        "ecosystem": lib["ecosystem"],
        "description": description,
        "short_description": lib["short_description"],
        "aliases": lib["aliases"],
        "keywords": lib["keywords"],
        "category": lib["category"],
        "homepage_url": lib["homepage_url"],
        "repository_url": lib["repository_url"],
        "logo_url": lib.get("logo_url", ""),
        "author": lib["author"],
        "license": lib["license"],
        "status": lib["status"],
        "popularity_score": lib["popularity_score"],
        "github_stars": lib.get("github_stars", 0),
        "npm_downloads_weekly": lib.get("npm_downloads_weekly", 0),
        "pypi_downloads_monthly": lib.get("pypi_downloads_monthly", 0),
        "doc_version": lib.get("doc_version", ""),
        "doc_source_type": lib.get("doc_source_type", ""),
        "doc_completeness": lib.get("doc_completeness", 0.0),
        "last_indexed_at": lib.get("last_indexed_at"),
        "related_libraries": lib.get("related_libraries", []),
        "alternative_to": lib.get("alternative_to", []),
        "supersedes": lib.get("supersedes", []),
        "requires_libraries": lib.get("requires_libraries", []),
        "first_release_date": lib.get("first_release_date"),
        "last_release_date": lib.get("last_release_date"),
        "created_at": lib["created_at"],
        "updated_at": now,
        "document_count": lib["document_count"],
    }

    libraries.add([updated_data])

    return {
        "id": lib["id"],
        "name": name,
        "context7_id": lib["context7_id"],
        "language": lib["language"],
        "ecosystem": lib["ecosystem"],
        "description": description,
        "short_description": lib["short_description"],
        "aliases": lib["aliases"],
        "keywords": lib["keywords"],
        "category": lib["category"],
        "homepage_url": lib["homepage_url"],
        "repository_url": lib["repository_url"],
        "author": lib["author"],
        "license": lib["license"],
        "status": lib["status"],
        "popularity_score": lib["popularity_score"],
        "created_at": lib["created_at"],
        "updated_at": now,
        "document_count": lib["document_count"],
    }


def partial_update_library(
    library_id: str, name: str | None = None, description: str | None = None
) -> LibraryData:
    """Update library (partial update).

    Uses delete-then-re-add pattern since LanceDB has no UPDATE.
    Only updates fields that are explicitly provided.

    Args:
        library_id: Library unique identifier.
        name: New library name (optional).
        description: New library description (optional).

    Returns:
        Updated library data.

    Raises:
        ValueError: If library not found or name conflicts.
    """
    libraries = get_libraries_table()
    now = datetime.now()

    # 1. Verify library exists
    existing = (
        libraries.search()
        .where(f"id = '{library_id}'", prefilter=True)
        .limit(1)
        .to_list()
    )
    if not existing:
        raise ValueError(f"Library '{library_id}' not found")

    lib = existing[0]

    # 2. Determine new values (use existing if not provided)
    new_name = name if name is not None else lib["name"]
    new_description = description if description is not None else lib["description"]

    # 3. Validate name uniqueness if name changed
    if name is not None and name != lib["name"]:
        duplicates = (
            libraries.search()
            .where(
                f"name = '{name}' AND ecosystem = '{lib['ecosystem']}'",
                prefilter=True,
            )
            .limit(1)
            .to_list()
        )
        if duplicates:
            raise ValueError(
                f"Library '{name}' already exists in ecosystem '{lib['ecosystem']}'"
            )

    # 4. Delete and re-add with updated fields
    libraries.delete(f"id = '{library_id}'")

    updated_data = {
        "id": lib["id"],
        "name": new_name,
        "context7_id": lib["context7_id"],
        "language": lib["language"],
        "ecosystem": lib["ecosystem"],
        "description": new_description,
        "short_description": lib["short_description"],
        "aliases": lib["aliases"],
        "keywords": lib["keywords"],
        "category": lib["category"],
        "homepage_url": lib["homepage_url"],
        "repository_url": lib["repository_url"],
        "logo_url": lib.get("logo_url", ""),
        "author": lib["author"],
        "license": lib["license"],
        "status": lib["status"],
        "popularity_score": lib["popularity_score"],
        "github_stars": lib.get("github_stars", 0),
        "npm_downloads_weekly": lib.get("npm_downloads_weekly", 0),
        "pypi_downloads_monthly": lib.get("pypi_downloads_monthly", 0),
        "doc_version": lib.get("doc_version", ""),
        "doc_source_type": lib.get("doc_source_type", ""),
        "doc_completeness": lib.get("doc_completeness", 0.0),
        "last_indexed_at": lib.get("last_indexed_at"),
        "related_libraries": lib.get("related_libraries", []),
        "alternative_to": lib.get("alternative_to", []),
        "supersedes": lib.get("supersedes", []),
        "requires_libraries": lib.get("requires_libraries", []),
        "first_release_date": lib.get("first_release_date"),
        "last_release_date": lib.get("last_release_date"),
        "created_at": lib["created_at"],
        "updated_at": now,
        "document_count": lib["document_count"],
    }

    libraries.add([updated_data])

    return {
        "id": lib["id"],
        "name": new_name,
        "context7_id": lib["context7_id"],
        "language": lib["language"],
        "ecosystem": lib["ecosystem"],
        "description": new_description,
        "short_description": lib["short_description"],
        "aliases": lib["aliases"],
        "keywords": lib["keywords"],
        "category": lib["category"],
        "homepage_url": lib["homepage_url"],
        "repository_url": lib["repository_url"],
        "author": lib["author"],
        "license": lib["license"],
        "status": lib["status"],
        "popularity_score": lib["popularity_score"],
        "created_at": lib["created_at"],
        "updated_at": now,
        "document_count": lib["document_count"],
    }


def delete_library(library_id: str) -> bool:
    """Delete a library.

    Prevents deletion if library has associated documents.

    Args:
        library_id: Library unique identifier.

    Returns:
        True if deletion was successful.

    Raises:
        ValueError: If library not found or has associated documents.
    """
    from c7_mcp.db import get_documents_table

    libraries = get_libraries_table()

    # 1. Verify library exists
    existing = (
        libraries.search()
        .where(f"id = '{library_id}'", prefilter=True)
        .limit(1)
        .to_list()
    )
    if not existing:
        raise ValueError(f"Library '{library_id}' not found")

    # 2. Check for associated documents
    documents = get_documents_table()
    doc_results = (
        documents.search()
        .where(f"library_id = '{library_id}'", prefilter=True)
        .limit(1)
        .to_list()
    )
    if doc_results:
        raise ValueError(
            f"Library '{library_id}' has associated documents. "
            "Delete all documents first."
        )

    # 3. Delete library
    libraries.delete(f"id = '{library_id}'")

    return True
