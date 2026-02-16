"""Pydantic models for MCP JSON-RPC 2.0 protocol.

This module defines the schema for Context7-compatible MCP requests and responses
following the JSON-RPC 2.0 specification.
"""

from typing import Any

from pydantic import BaseModel, Field


class ResolveLibraryIdArgs(BaseModel):
    """Arguments for the resolve-library-id tool.

    Attributes:
        library_name: Name of the library to resolve.
        query: User's query for context.
    """

    library_name: str = Field(..., alias="libraryName")
    query: str


class QueryDocsArgs(BaseModel):
    """Arguments for the query-docs tool.

    Attributes:
        library_id: Context7-compatible library identifier.
        query: Documentation query string.
    """

    library_id: str = Field(..., alias="libraryId")
    query: str


class ToolCallParams(BaseModel):
    """Parameters for the tools/call method.

    Attributes:
        name: Name of the tool to call (resolve-library-id or query-docs).
        arguments: Tool-specific arguments.
    """

    name: str
    arguments: dict[str, Any]


class JSONRPCRequest(BaseModel):
    """JSON-RPC 2.0 request wrapper.

    Attributes:
        jsonrpc: JSON-RPC version (must be "2.0").
        id: Request identifier.
        method: Method name (e.g., "tools/call").
        params: Method parameters.
    """

    jsonrpc: str = Field(default="2.0")
    id: int | str
    method: str
    params: ToolCallParams


class TextContent(BaseModel):
    """Content wrapper with type="text".

    Attributes:
        type: Content type (always "text").
        text: Text content.
    """

    type: str = Field(default="text")
    text: str


class JSONRPCResult(BaseModel):
    """Result wrapper for JSON-RPC responses.

    Attributes:
        content: List of content items (typically TextContent).
    """

    content: list[TextContent]


class JSONRPCResponse(BaseModel):
    """JSON-RPC 2.0 response wrapper.

    Attributes:
        jsonrpc: JSON-RPC version (must be "2.0").
        id: Request identifier (matches request).
        result: Method result.
    """

    jsonrpc: str = Field(default="2.0")
    id: int | str
    result: JSONRPCResult
