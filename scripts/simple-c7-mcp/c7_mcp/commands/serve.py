"""Serve command to run the FastAPI server."""

import typer
from granian import Granian
from granian.constants import Interfaces


def serve(
    host: str = typer.Option("127.0.0.1", help="Host to bind to"),
    port: int = typer.Option(8000, help="Port to bind to"),
    reload: bool = typer.Option(False, help="Enable auto-reload on code changes"),
    workers: int = typer.Option(1, help="Number of worker processes"),
) -> None:
    """Start the FastAPI server with Granian.

    Args:
        host: Host address to bind to.
        port: Port number to bind to.
        reload: Enable auto-reload for development.
        workers: Number of worker processes (ignored if reload is True).
    """
    Granian(
        "c7_mcp.api:app",
        address=host,
        port=port,
        interface=Interfaces.ASGI,
        reload=reload,
        workers=1 if reload else workers,
    ).serve()
