"""Hello command."""

from typing import Annotated

import typer

from lance_db_example.services.greeting import greet


def hello(name: Annotated[str, typer.Argument()] = "World"):
    """Say hello."""
    print(greet(name))
