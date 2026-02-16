"""FastAPI application with health check endpoint."""

from fastapi import FastAPI

from c7_mcp.routers import documents, libraries, mcp

app = FastAPI(
    title="Context7 MCP API",
    version="0.1.0",
    description="Context7-compatible MCP server with library and document management",
)

# Include routers
app.include_router(mcp.router)
app.include_router(libraries.router)
app.include_router(documents.router)


@app.get("/health")
async def health_check() -> dict[str, str]:
    """Health check endpoint.

    Returns:
        Dictionary with status information.
    """
    return {"status": "healthy", "service": "c7-mcp"}
