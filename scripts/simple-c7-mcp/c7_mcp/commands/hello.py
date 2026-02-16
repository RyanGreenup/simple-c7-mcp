"""Hello command."""

from typing import Annotated

import typer

from c7_mcp.services.greeting import greet


def hello(name: Annotated[str, typer.Argument()] = "World"):
    """Say hello."""
    print(greet(name))
