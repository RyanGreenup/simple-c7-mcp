#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "typer",
#     "rich",
#     "httpx",
# ]
# ///

"""
Context7 MCP Testing Script

Tests the Context7 MCP server by making forward pass calls to both endpoints:
1. resolve-library-id - Converts library names to Context7 IDs
2. query-docs - Retrieves documentation for a library
"""

import json
from typing import Optional

import httpx
import typer
from rich.console import Console
from rich.json import JSON
from rich.panel import Panel
from rich.syntax import Syntax

app = typer.Typer(help="Test Context7 MCP server endpoints")
console = Console()

# Context7 MCP endpoint
MCP_ENDPOINT = "https://mcp.context7.com/mcp"


def make_mcp_request(method: str, params: dict, api_key: Optional[str] = None) -> dict:
    """Make a request to the Context7 MCP server."""
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream",
    }

    if api_key:
        headers["CONTEXT7_API_KEY"] = api_key

    # MCP request format
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": method,
        "params": params
    }

    console.print(f"\n[bold blue]📤 Request to {method}[/bold blue]")
    console.print(Panel(JSON(json.dumps(payload, indent=2)), title="Request Payload"))

    try:
        response = httpx.post(MCP_ENDPOINT, json=payload, headers=headers, timeout=30.0)

        # Show response status and headers for debugging
        console.print(f"\n[dim]Response Status: {response.status_code}[/dim]")
        console.print(f"[dim]Response Headers: {dict(response.headers)}[/dim]")

        response.raise_for_status()
        result = response.json()

        console.print(f"\n[bold green]📥 Response from {method}[/bold green]")
        console.print(Panel(JSON(json.dumps(result, indent=2)), title="Response"))

        return result
    except httpx.HTTPStatusError as e:
        console.print(f"[bold red]❌ HTTP Status Error: {e}[/bold red]")
        console.print(f"[dim]Response body: {e.response.text}[/dim]")
        raise
    except httpx.HTTPError as e:
        console.print(f"[bold red]❌ HTTP Error: {e}[/bold red]")
        raise
    except Exception as e:
        console.print(f"[bold red]❌ Error: {e}[/bold red]")
        raise


@app.command()
def resolve(
    library_name: str = typer.Argument(..., help="Library name to resolve"),
    query: str = typer.Argument(..., help="User query for relevance ranking"),
    api_key: Optional[str] = typer.Option(None, "--api-key", "-k", help="Context7 API key"),
):
    """
    Test the resolve-library-id endpoint.

    Example:
        python context7_test.py resolve "Next.js" "How to create API routes"
    """
    console.print(f"\n[bold cyan]🔍 Resolving library: {library_name}[/bold cyan]")

    params = {
        "libraryName": library_name,
        "query": query
    }

    result = make_mcp_request("tools/call", {
        "name": "resolve-library-id",
        "arguments": params
    }, api_key)

    # Show the full response text
    try:
        if "result" in result and "content" in result["result"]:
            content = result["result"]["content"]
            if isinstance(content, list) and len(content) > 0:
                text_content = content[0].get("text", "")
                console.print("\n[bold cyan]📄 Available Libraries:[/bold cyan]")
                console.print(Panel(text_content, title="Libraries", expand=False))
    except Exception as e:
        console.print(f"[yellow]⚠ Could not display full text: {e}[/yellow]")

    console.print("\n[bold green]✅ Resolution complete![/bold green]")


@app.command()
def query(
    library_id: str = typer.Argument(..., help="Context7 library ID (e.g., /vercel/next.js)"),
    query_text: str = typer.Argument(..., help="Documentation query"),
    api_key: Optional[str] = typer.Option(None, "--api-key", "-k", help="Context7 API key"),
):
    """
    Test the query-docs endpoint.

    Example:
        python context7_test.py query "/vercel/next.js" "How to use middleware"
    """
    console.print(f"\n[bold cyan]📚 Querying docs for: {library_id}[/bold cyan]")

    params = {
        "libraryId": library_id,
        "query": query_text
    }

    result = make_mcp_request("tools/call", {
        "name": "query-docs",
        "arguments": params
    }, api_key)

    # Show the full documentation text
    try:
        if "result" in result and "content" in result["result"]:
            content = result["result"]["content"]
            if isinstance(content, list) and len(content) > 0:
                doc_text = content[0].get("text", "")
                console.print("\n[bold cyan]📖 Documentation Response:[/bold cyan]")
                console.print(Panel(doc_text, title="Documentation", expand=False))
    except Exception as e:
        console.print(f"[yellow]⚠ Could not display full documentation: {e}[/yellow]")

    console.print("\n[bold green]✅ Query complete![/bold green]")


@app.command()
def forward_pass(
    library_name: str = typer.Argument("React", help="Library name to test"),
    user_query: str = typer.Argument("How to use useState hook", help="User question"),
    api_key: Optional[str] = typer.Option(None, "--api-key", "-k", help="Context7 API key"),
):
    """
    Execute a complete forward pass: resolve library ID, then query docs.

    This demonstrates the full workflow of using Context7 MCP.

    Example:
        python context7_test.py forward-pass "Next.js" "How to create API routes"
    """
    console.print("\n[bold magenta]🚀 Starting Forward Pass Test[/bold magenta]")
    console.print(f"Library: {library_name}")
    console.print(f"Query: {user_query}\n")

    # Step 1: Resolve library ID
    console.print("[bold yellow]Step 1: Resolving library ID...[/bold yellow]")
    resolve_params = {
        "libraryName": library_name,
        "query": user_query
    }

    resolve_result = make_mcp_request("tools/call", {
        "name": "resolve-library-id",
        "arguments": resolve_params
    }, api_key)

    # Extract library ID from response
    # Note: The actual response format may vary, adjust as needed
    try:
        library_id = None
        if "result" in resolve_result and "content" in resolve_result["result"]:
            content = resolve_result["result"]["content"]
            if isinstance(content, list) and len(content) > 0:
                # Try to parse the library ID from the response
                text_content = content[0].get("text", "")

                # Show the full text content for inspection
                console.print("\n[bold cyan]📄 Full Response Text:[/bold cyan]")
                console.print(Panel(text_content, title="Response Content", expand=False))

                console.print(f"\n[dim]Parsing library ID from response...[/dim]")
                # Look for library ID patterns - they should be in format /org/name or /org/name/version
                import re

                # Try to find the first library in a structured format
                # Look for patterns like "Library ID: /org/project" or just "/org/project" on its own line
                id_match = re.search(r'(?:Library ID|libraryId|id):\s*([/\w.-]+/[\w.-]+(?:/[\w.-]+)?)', text_content, re.IGNORECASE)
                if not id_match:
                    # Look for standalone library ID patterns (more specific than generic /org/project)
                    # Prioritize IDs with more specific names (not just generic placeholders)
                    all_matches = re.findall(r'/[\w-]+/[\w.-]+(?:/[\w.-]+)?', text_content)
                    # Filter out the generic placeholder pattern
                    filtered = [m for m in all_matches if m != '/org/project']
                    if filtered:
                        library_id = filtered[0]
                    elif all_matches:
                        library_id = all_matches[0]
                else:
                    library_id = id_match.group(1)

                if library_id:
                    console.print(f"[bold green]✓ Found library ID: {library_id}[/bold green]")
    except Exception as e:
        console.print(f"[yellow]⚠ Could not auto-extract library ID: {e}[/yellow]")

    if not library_id:
        console.print("\n[yellow]⚠ Could not automatically extract library ID from response.[/yellow]")
        console.print("[yellow]Please review the response above and try the query-docs command manually.[/yellow]")
        return

    # Step 2: Query docs
    console.print(f"\n[bold yellow]Step 2: Querying documentation for {library_id}...[/bold yellow]")
    query_params = {
        "libraryId": library_id,
        "query": user_query
    }

    query_result = make_mcp_request("tools/call", {
        "name": "query-docs",
        "arguments": query_params
    }, api_key)

    # Show the full documentation text
    try:
        if "result" in query_result and "content" in query_result["result"]:
            content = query_result["result"]["content"]
            if isinstance(content, list) and len(content) > 0:
                doc_text = content[0].get("text", "")
                console.print("\n[bold cyan]📖 Documentation Response:[/bold cyan]")
                console.print(Panel(doc_text, title="Documentation", expand=False))
    except Exception as e:
        console.print(f"[yellow]⚠ Could not display full documentation: {e}[/yellow]")

    console.print("\n[bold green]🎉 Forward pass complete![/bold green]")
    console.print(f"Resolved: {library_name} → {library_id}")
    console.print(f"Query: {user_query}")


@app.command()
def list_tools(
    api_key: Optional[str] = typer.Option(None, "--api-key", "-k", help="Context7 API key"),
):
    """
    List available tools from the MCP server.
    """
    console.print("\n[bold cyan]🔧 Listing available tools...[/bold cyan]")

    result = make_mcp_request("tools/list", {}, api_key)

    console.print("\n[bold green]✅ Tools listed![/bold green]")


@app.command()
def debug(
    api_key: Optional[str] = typer.Option(None, "--api-key", "-k", help="Context7 API key"),
):
    """
    Debug the MCP endpoint connection.
    """
    console.print("\n[bold cyan]🔍 Debugging MCP endpoint...[/bold cyan]")
    console.print(f"Endpoint: {MCP_ENDPOINT}\n")

    # Try a simple initialize request
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream",
    }

    if api_key:
        headers["CONTEXT7_API_KEY"] = api_key

    # Try initialize method
    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "initialize",
        "params": {
            "protocolVersion": "2024-11-05",
            "capabilities": {},
            "clientInfo": {
                "name": "context7-test",
                "version": "1.0.0"
            }
        }
    }

    console.print("[bold]Trying initialize request...[/bold]")
    console.print(Panel(JSON(json.dumps(payload, indent=2)), title="Initialize Payload"))

    try:
        response = httpx.post(MCP_ENDPOINT, json=payload, headers=headers, timeout=30.0)
        console.print(f"\n[dim]Status Code: {response.status_code}[/dim]")
        console.print(f"[dim]Headers: {dict(response.headers)}[/dim]")
        console.print(f"[dim]Body: {response.text[:500]}...[/dim]")

        if response.status_code == 200:
            result = response.json()
            console.print(Panel(JSON(json.dumps(result, indent=2)), title="Response"))
        else:
            console.print(f"[yellow]Non-200 status: {response.status_code}[/yellow]")
            console.print(f"[yellow]Body: {response.text}[/yellow]")

    except Exception as e:
        console.print(f"[bold red]❌ Error: {e}[/bold red]")


if __name__ == "__main__":
    app()
