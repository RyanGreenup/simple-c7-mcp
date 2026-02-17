"""MCP JSON-RPC 2.0 endpoint router.

This module implements the Context7-compatible MCP endpoint using JSON-RPC 2.0 protocol.
"""

from fastapi import APIRouter, HTTPException

from c7_mcp.schemas.mcp import (
    JSONRPCRequest,
    JSONRPCResponse,
    JSONRPCResult,
    QueryDocsArgs,
    ResolveLibraryIdArgs,
    TextContent,
)
from c7_mcp.services import mcp as mcp_service

router = APIRouter()


@router.post("/mcp", response_model=JSONRPCResponse)
async def mcp_endpoint(request: JSONRPCRequest) -> JSONRPCResponse:
    """Handle MCP JSON-RPC 2.0 requests.

    This endpoint implements the Context7 MCP protocol for tool invocation.
    Supports the following tools:
    - resolve-library-id: Resolve library name to Context7 ID
    - query-docs: Query documentation by library ID

    Args:
        request: JSON-RPC 2.0 request with method and params.

    Returns:
        JSON-RPC 2.0 response with tool result.

    Raises:
        HTTPException: 400 if method not supported or invalid params.
    """
    # Validate method
    if request.method != "tools/call":
        raise HTTPException(
            status_code=400,
            detail=(
                f"Unsupported method: {request.method}. "
                "Only 'tools/call' is supported."
            ),
        )

    tool_name = request.params.name

    if tool_name == "resolve-library-id":
        args = ResolveLibraryIdArgs.model_validate(request.params.arguments)
        result_text = mcp_service.resolve_library_id(args.library_name, args.query)

    elif tool_name == "query-docs":
        args = QueryDocsArgs.model_validate(request.params.arguments)
        result_text = mcp_service.query_docs(args.library_id, args.query)

    else:
        raise HTTPException(
            status_code=400, detail=f"Unknown tool: {tool_name}"
        )

    # Wrap result in response format
    return JSONRPCResponse(
        id=request.id,
        result=JSONRPCResult(
            content=[TextContent(text=result_text)]
        ),
    )
