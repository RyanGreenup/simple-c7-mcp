"""MCP JSON-RPC 2.0 endpoint router.

This module implements the Context7-compatible MCP endpoint using JSON-RPC 2.0 protocol.
"""

from fastapi import APIRouter, HTTPException

from c7_mcp.schemas.mcp import (
    JSONRPCRequest,
    JSONRPCResponse,
    JSONRPCResult,
    QueryDocsArgs,  # noqa: F401 - Will be used when TODO is implemented
    ResolveLibraryIdArgs,  # noqa: F401 - Will be used when TODO is implemented
    TextContent,
)
from c7_mcp.services import (
    mcp as mcp_service,  # noqa: F401 - Will be used when TODO is implemented
)

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
        HTTPException: 501 if tool not implemented yet.

    TODO: Implement complete JSON-RPC method routing.
    TODO: 1. Validate request.method is "tools/call"
    TODO: 2. Extract tool name from request.params.name
    TODO: 3. Dispatch to appropriate tool handler
    TODO: 4. Handle resolve-library-id tool
    TODO: 5. Handle query-docs tool
    TODO: 6. Wrap result in TextContent and JSONRPCResult
    TODO: 7. Handle errors and return JSON-RPC error responses
    TODO: 8. Add logging for tool invocations
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

    # TODO: Implement tool routing
    if tool_name == "resolve-library-id":
        # TODO: Parse arguments using ResolveLibraryIdArgs
        # TODO: Call mcp_service.resolve_library_id()
        # TODO: Wrap result in TextContent
        result_text = "TODO: Implement resolve-library-id tool"

    elif tool_name == "query-docs":
        # TODO: Parse arguments using QueryDocsArgs
        # TODO: Call mcp_service.query_docs()
        # TODO: Wrap result in TextContent
        result_text = "TODO: Implement query-docs tool"

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
