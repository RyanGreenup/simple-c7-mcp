"""LanceDB database connection and initialization.

This module provides database connection management and schema initialization
for the Context7 MCP server.
"""

import os
from pathlib import Path

import lancedb

from c7_mcp.exceptions import DatabaseError
from c7_mcp.models import Document, Library

# Default database path
DEFAULT_DB_PATH = os.getenv("LANCEDB_PATH", "./lancedb_data")

# Global connection (initialized on first access)
_db_connection = None


def get_db() -> lancedb.DBConnection:
    """Get or create LanceDB connection.

    Returns:
        LanceDB connection instance.

    Example:
        >>> db = get_db()
        >>> libraries = db.open_table("libraries")
    """
    global _db_connection

    if _db_connection is None:
        db_path = Path(DEFAULT_DB_PATH)
        db_path.mkdir(parents=True, exist_ok=True)
        _db_connection = lancedb.connect(str(db_path))

    return _db_connection


def init_schema() -> dict[str, str]:
    """Initialize LanceDB schema by creating required tables.

    Creates the following tables if they don't exist:
    - libraries: Library metadata for MCP resolution
    - documents: Document chunks with embeddings

    Returns:
        Dictionary with table creation status.

    Example:
        >>> status = init_schema()
        >>> print(status)
        {'libraries': 'created', 'documents': 'exists'}
    """
    db = get_db()
    status = {}

    # Create libraries table
    try:
        existing_tables = db.table_names()

        if "libraries" not in existing_tables:
            # Create empty table with schema
            db.create_table("libraries", schema=Library, mode="create")
            status["libraries"] = "created"
        else:
            status["libraries"] = "exists"

        if "documents" not in existing_tables:
            # Create empty table with schema
            db.create_table("documents", schema=Document, mode="create")
            status["documents"] = "created"
        else:
            status["documents"] = "exists"

    except Exception as e:
        status["error"] = str(e)
        raise

    return status


def get_libraries_table():
    """Get the libraries table.

    Returns:
        LanceDB table instance for libraries.

    Raises:
        ValueError: If libraries table doesn't exist.
    """
    db = get_db()

    if "libraries" not in db.table_names():
        raise DatabaseError(
            "Libraries table does not exist. Run init_schema() first."
        )

    return db.open_table("libraries")


def get_documents_table():
    """Get the documents table.

    Returns:
        LanceDB table instance for documents.

    Raises:
        ValueError: If documents table doesn't exist.
    """
    db = get_db()

    if "documents" not in db.table_names():
        raise DatabaseError(
            "Documents table does not exist. Run init_schema() first."
        )

    return db.open_table("documents")


def close_db():
    """Close database connection.

    Call this during application shutdown to ensure clean cleanup.
    """
    global _db_connection

    if _db_connection is not None:
        # LanceDB doesn't require explicit close, but we reset the connection
        _db_connection = None
