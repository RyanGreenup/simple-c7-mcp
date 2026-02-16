"""FastAPI application with health check endpoint."""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from c7_mcp.db import close_db, init_schema
from c7_mcp.routers import documents, libraries, mcp


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager for startup/shutdown tasks."""
    # Startup: Initialize database schema
    print("Initializing LanceDB schema...")
    status = init_schema()
    print(f"Schema initialization: {status}")

    yield

    # Shutdown: Close database connections
    print("Closing database connections...")
    close_db()


app = FastAPI(
    title="Context7 MCP API",
    version="0.1.0",
    description="Context7-compatible MCP server with library and document management",
    lifespan=lifespan,
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
