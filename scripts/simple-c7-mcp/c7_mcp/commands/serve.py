"""Serve command to run the FastAPI server."""

import typer
import uvicorn


def serve(
    host: str = typer.Option("127.0.0.1", help="Host to bind to"),
    port: int = typer.Option(8000, help="Port to bind to"),
    reload: bool = typer.Option(False, help="Enable auto-reload on code changes"),
) -> None:
    """Start the FastAPI server.

    Args:
        host: Host address to bind to.
        port: Port number to bind to.
        reload: Enable auto-reload for development.
    """
    uvicorn.run(
        "c7_mcp.api:app",
        host=host,
        port=port,
        reload=reload,
    )
