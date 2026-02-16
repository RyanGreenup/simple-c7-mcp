"""Python template package."""

import typer


def create_typer() -> typer.Typer:
    """Create a Typer instance with standard settings."""
    return typer.Typer(
        context_settings={"help_option_names": ["-h", "--help"]},
        pretty_exceptions_enable=False,
    )
