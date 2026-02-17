"""MCP JSON-RPC 2.0 endpoint router.

This module implements the Context7-compatible MCP endpoint using JSON-RPC 2.0 protocol.
"""

from typing import Any

from fastapi import APIRouter, HTTPException, Response
from pydantic import ValidationError

from c7_mcp.schemas.mcp import (
    FetchLibraryDocsArgs,
    QueryDocsArgs,
    ResolveLibraryIdArgs,
    ToolCallParams,
)
from c7_mcp.services import mcp as mcp_service

router = APIRouter()


def _validate_tool_args(model: type, arguments: dict) -> object:
    """Validate tool arguments and map schema errors to HTTP 422."""
    try:
        return model.model_validate(arguments)
    except ValidationError as exc:
        raise HTTPException(status_code=422, detail=exc.errors()) from exc


def _jsonrpc_result(req_id: int | str | None, result: dict[str, Any]) -> dict[str, Any]:
    """Build a JSON-RPC success response."""
    response: dict[str, Any] = {"jsonrpc": "2.0", "result": result}
    if req_id is not None:
        response["id"] = req_id
    return response


@router.post("/mcp")
async def mcp_endpoint(request: dict[str, Any]) -> Any:
    """Handle MCP JSON-RPC 2.0 requests.

    This endpoint implements the Context7 MCP protocol for tool invocation.
    Supports the following tools:
    - resolve-library-id: Resolve library name to Context7 ID
    - query-docs: Query documentation by library ID
    - fetch-library-docs: Fetch and ingest docs if library is missing

    Args:
        request: JSON-RPC 2.0 request body.

    Returns:
        JSON-RPC 2.0 response.

    Raises:
        HTTPException: 400 if method not supported or invalid params.
    """
    req_id = request.get("id")
    method = request.get("method")
    params = request.get("params", {}) or {}

    if method == "initialize":
        client_protocol = "2024-11-05"
        if isinstance(params, dict):
            client_protocol = str(params.get("protocolVersion", client_protocol))
        return _jsonrpc_result(
            req_id,
            {
                "protocolVersion": client_protocol,
                "capabilities": {"tools": {"listChanged": False}},
                "serverInfo": {"name": "simple-c7-mcp", "version": "0.1.0"},
            },
        )

    if method == "tools/list":
        return _jsonrpc_result(
            req_id,
            {
                "tools": [
                    {
                        "name": "resolve-library-id",
                        "description": "Resolve library name to Context7-compatible ID",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "libraryName": {"type": "string"},
                                "query": {"type": "string"},
                            },
                            "required": ["libraryName", "query"],
                        },
                    },
                    {
                        "name": "query-docs",
                        "description": "Query documentation by library ID",
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "libraryId": {"type": "string"},
                                "query": {"type": "string"},
                            },
                            "required": ["libraryId", "query"],
                        },
                    },
                    {
                        "name": "fetch-library-docs",
                        "description": (
                            "Fetch and ingest docs from Context7 only if missing "
                            "and fetchIfMissing is true"
                        ),
                        "inputSchema": {
                            "type": "object",
                            "properties": {
                                "libraryName": {"type": "string"},
                                "query": {"type": "string"},
                                "fetchIfMissing": {"type": "boolean"},
                            },
                            "required": ["libraryName"],
                        },
                    },
                ]
            },
        )

    # JSON-RPC notifications do not expect a response body.
    if isinstance(method, str) and method.startswith("notifications/"):
        return Response(status_code=202)

    if method != "tools/call":
        raise HTTPException(
            status_code=400,
            detail=(
                f"Unsupported method: {method}. "
                "Supported: initialize, tools/list, tools/call."
            ),
        )

    try:
        tool_params = ToolCallParams.model_validate(params)
    except ValidationError as exc:
        raise HTTPException(status_code=422, detail=exc.errors()) from exc

    tool_name = tool_params.name

    if tool_name == "resolve-library-id":
        args = _validate_tool_args(ResolveLibraryIdArgs, tool_params.arguments)
        result_text = mcp_service.resolve_library_id(args.library_name, args.query)

    elif tool_name == "query-docs":
        args = _validate_tool_args(QueryDocsArgs, tool_params.arguments)
        result_text = mcp_service.query_docs(args.library_id, args.query)

    elif tool_name == "fetch-library-docs":
        args = _validate_tool_args(FetchLibraryDocsArgs, tool_params.arguments)
        result_text = mcp_service.fetch_library_docs(
            args.library_name,
            args.query,
            args.fetch_if_missing,
        )

    else:
        raise HTTPException(
            status_code=400, detail=f"Unknown tool: {tool_name}"
        )

    return _jsonrpc_result(
        req_id,
        {"content": [{"type": "text", "text": result_text}]},
    )
