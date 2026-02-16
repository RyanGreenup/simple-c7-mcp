"""FastAPI application with health check endpoint."""

from fastapi import FastAPI

app = FastAPI(title="Context7 MCP API", version="0.1.0")


@app.get("/health")
async def health_check() -> dict[str, str]:
    """Health check endpoint.

    Returns:
        Dictionary with status information.
    """
    return {"status": "healthy", "service": "c7-mcp"}
