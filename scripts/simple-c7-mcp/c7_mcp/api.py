"""FastAPI application with health check endpoint."""

import re
from contextlib import asynccontextmanager

from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from starlette.types import ASGIApp, Message, Receive, Scope, Send

from c7_mcp.db import close_db, init_schema
from c7_mcp.exceptions import (
    BadRequestError,
    ConflictError,
    DatabaseError,
    NotFoundError,
)
from c7_mcp.routers import documents, libraries, mcp


def _error_slug(exc: Exception) -> str:
    """Convert exception class name to snake_case slug.

    Examples:
        LibraryNotFoundError -> "library_not_found"
        EmbeddingDimensionError -> "embedding_dimension"
    """
    name = type(exc).__name__.removesuffix("Error")
    return re.sub(r"(?<=[a-z0-9])(?=[A-Z])", "_", name).lower()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Application lifespan manager for startup/shutdown tasks."""
    # Startup: Initialize database schema
    print("Initializing LanceDB schema...")
    status = init_schema()
    print(f"Schema initialization: {status}")

    # Start the MCP session manager (mounted sub-app lifespans are not
    # called by FastAPI, so we manage it here).
    async with mcp.mcp_server.session_manager.run():
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


class _McpCorsMiddleware:
    """Always add Access-Control-Expose-Headers for MCP responses.

    The MCP spec requires clients to read the Mcp-Session-Id response
    header.  This middleware unconditionally exposes it so both same-origin
    and cross-origin clients can access it.
    """

    def __init__(self, app: ASGIApp) -> None:
        self.app = app

    async def __call__(self, scope: Scope, receive: Receive, send: Send) -> None:
        if scope["type"] != "http" or not scope["path"].startswith("/mcp"):
            await self.app(scope, receive, send)
            return

        async def _send(message: Message) -> None:
            if message["type"] == "http.response.start":
                headers = list(message.get("headers", []))
                headers.append((b"access-control-expose-headers", b"Mcp-Session-Id"))
                message["headers"] = headers
            await send(message)

        await self.app(scope, receive, _send)


app.add_middleware(_McpCorsMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "POST", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "Accept", "Mcp-Session-Id", "MCP-Protocol-Version"],
    expose_headers=["Mcp-Session-Id"],
)


# --- Global exception handlers ---


@app.exception_handler(NotFoundError)
async def not_found_handler(_request: Request, exc: NotFoundError) -> JSONResponse:
    """Handle not-found errors as 404."""
    return JSONResponse(
        status_code=404,
        content={"error": _error_slug(exc), "message": exc.message},
    )


@app.exception_handler(ConflictError)
async def conflict_handler(_request: Request, exc: ConflictError) -> JSONResponse:
    """Handle conflict errors as 409."""
    return JSONResponse(
        status_code=409,
        content={"error": _error_slug(exc), "message": exc.message},
    )


@app.exception_handler(BadRequestError)
async def bad_request_handler(_request: Request, exc: BadRequestError) -> JSONResponse:
    """Handle bad-request errors as 400."""
    return JSONResponse(
        status_code=400,
        content={"error": _error_slug(exc), "message": exc.message},
    )


@app.exception_handler(DatabaseError)
async def database_error_handler(
    _request: Request, exc: DatabaseError
) -> JSONResponse:
    """Handle database errors as 500."""
    return JSONResponse(
        status_code=500,
        content={"error": _error_slug(exc), "message": exc.message},
    )


# Include REST routers first so they take priority over the catch-all mount.
app.include_router(libraries.router)
app.include_router(documents.router)


@app.get("/health")
async def health_check() -> dict[str, str]:
    """Health check endpoint.

    Returns:
        Dictionary with status information.
    """
    return {"status": "healthy", "service": "c7-mcp"}


# Mount MCP sub-app at root LAST.  The sub-app's internal route is at
# "/mcp" (the FastMCP default), so POST /mcp → sub-app receives "/mcp".
# Because this mount comes after all explicit routes, /health and
# /api/v1/* are matched first and never reach the sub-app.
app.mount("/", mcp.mcp_app)
