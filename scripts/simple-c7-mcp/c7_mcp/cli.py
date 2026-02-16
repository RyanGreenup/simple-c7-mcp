"""Command-line interface entry point."""

from c7_mcp import create_typer
from c7_mcp.commands import users
from c7_mcp.commands.hello import hello

app = create_typer()
_ = app.command()(hello)
app.add_typer(users.app, name="users")

if __name__ == "__main__":
    app()
