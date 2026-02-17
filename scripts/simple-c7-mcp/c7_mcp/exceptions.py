"""Custom exceptions for the Context7 MCP server.

Typed exception hierarchy replacing generic ValueError usage.
Global FastAPI handlers in api.py map these to appropriate HTTP responses.
"""


class C7Error(Exception):
    """Base exception for all Context7 MCP errors."""

    message: str

    def __init__(self, message: str) -> None:
        """Initialize with human-readable message."""
        self.message = message
        super().__init__(message)


# --- 404 Not Found ---


class NotFoundError(C7Error):
    """Resource not found (404)."""


class LibraryNotFoundError(NotFoundError):
    """Library not found by ID."""

    def __init__(self, library_id: str) -> None:
        """Initialize with the missing library ID."""
        self.library_id = library_id
        super().__init__(f"Library '{library_id}' not found")


class DocumentNotFoundError(NotFoundError):
    """Document not found by ID."""

    def __init__(self, doc_id: str) -> None:
        """Initialize with the missing document ID."""
        self.doc_id = doc_id
        super().__init__(f"Document '{doc_id}' not found")


class EmbeddingsNotFoundError(NotFoundError):
    """Document exists but has no embeddings."""

    def __init__(self, doc_id: str) -> None:
        """Initialize with the document ID lacking embeddings."""
        self.doc_id = doc_id
        super().__init__(f"Document '{doc_id}' has no embeddings")


# --- 409 Conflict ---


class ConflictError(C7Error):
    """Resource conflict (409)."""


class LibraryExistsError(ConflictError):
    """Library name already taken in ecosystem."""

    def __init__(self, name: str, ecosystem: str) -> None:
        """Initialize with the conflicting name and ecosystem."""
        self.name = name
        self.ecosystem = ecosystem
        super().__init__(
            f"Library '{name}' already exists in ecosystem '{ecosystem}'"
        )


# --- 400 Bad Request ---


class BadRequestError(C7Error):
    """Client error (400)."""


class EmbeddingDimensionError(BadRequestError):
    """Embedding vector has wrong dimension."""

    def __init__(self, got: int, expected: int) -> None:
        """Initialize with the actual and expected dimensions."""
        self.got = got
        self.expected = expected
        super().__init__(
            f"Embedding dimension mismatch: got {got}, expected {expected}"
        )


class ConstraintError(BadRequestError):
    """Business rule violation (e.g. delete library with documents)."""


class URLFetchError(BadRequestError):
    """Failed to fetch content from URL."""

    def __init__(self, url: str, reason: str) -> None:
        """Initialize with the URL and failure reason."""
        self.url = url
        self.reason = reason
        super().__init__(f"Failed to fetch URL '{url}': {reason}")


# --- 500 Internal ---


class DatabaseError(C7Error):
    """Database-level error (500)."""
