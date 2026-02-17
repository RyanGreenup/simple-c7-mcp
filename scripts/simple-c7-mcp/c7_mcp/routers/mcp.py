"""MCP endpoint via the official Python MCP SDK (FastMCP).

This module creates a FastMCP server instance, registers Context7-compatible
tools, and exports the streamable HTTP ASGI sub-application for mounting.

The sub-app uses the default ``streamable_http_path="/mcp"`` so the MCP
endpoint lives at ``/mcp`` inside the sub-app.  The parent FastAPI app
mounts the sub-app at ``"/"`` (after its own routes) so that
``POST /mcp`` reaches this handler without a trailing-slash redirect.
"""

from mcp.server.fastmcp import FastMCP

from c7_mcp.services import mcp as mcp_service

mcp_server = FastMCP("simple-c7-mcp")


@mcp_server.tool(name="resolve-library-id")
def resolve_library_id(libraryName: str, query: str) -> str:  # noqa: N803
    """Resolve library name to Context7-compatible ID.

    Args:
        libraryName: Name of the library (e.g., "React", "FastAPI").
        query: User's query for context.
    """
    return mcp_service.resolve_library_id(libraryName, query)


@mcp_server.tool(name="query-docs")
def query_docs(libraryId: str, query: str) -> str:  # noqa: N803
    """Query documentation by library ID.

    Args:
        libraryId: Context7-compatible library identifier.
        query: Documentation query string.
    """
    return mcp_service.query_docs(libraryId, query)


@mcp_server.tool(name="fetch-library-docs")
def fetch_library_docs(
    libraryName: str,  # noqa: N803
    query: str = "",
    fetchIfMissing: bool = False,  # noqa: N803
) -> str:
    """Fetch and ingest docs from Context7 only if missing and fetchIfMissing is true.

    Args:
        libraryName: Name of the library to fetch.
        query: Extra context to disambiguate remote resolution.
        fetchIfMissing: Explicit opt-in to fetch from Context7 if missing.
    """
    return mcp_service.fetch_library_docs(libraryName, query, fetchIfMissing)


mcp_app = mcp_server.streamable_http_app()
