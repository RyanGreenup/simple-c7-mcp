#!/usr/bin/env -S uv run
# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "typer",
#     "rich",
#     "httpx",
#     "lancedb",
#     "pandas",
#     "sentence-transformers",
#     "torch",
# ]
# ///

"""
Context7 + LanceDB Integration

Demonstrates fetching documentation from Context7 MCP and storing it
in LanceDB for semantic search.
"""

import json
import re
from datetime import datetime
from pathlib import Path
from typing import Optional, List, Dict, Any

import httpx
import lancedb
import pandas as pd
import typer
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

try:
    from sentence_transformers import SentenceTransformer
    import torch
    HAS_EMBEDDINGS = True
except ImportError:
    HAS_EMBEDDINGS = False

app = typer.Typer(help="Context7 + LanceDB Integration")
console = Console()

MCP_ENDPOINT = "https://mcp.context7.com/mcp"
DEFAULT_DB_PATH = "context7_docs.lance"
DEFAULT_MODEL = "all-MiniLM-L6-v2"

# Global model cache
_model = None


def get_model(model_name: str = DEFAULT_MODEL):
    """Get or create the sentence transformer model."""
    global _model
    if _model is None and HAS_EMBEDDINGS:
        device = "cuda" if torch.cuda.is_available() else "cpu"
        console.print(f"[dim]Loading model '{model_name}' on {device}...[/dim]")
        _model = SentenceTransformer(model_name, device=device)
    return _model


def make_mcp_request(method: str, params: dict) -> dict:
    """Make a request to Context7 MCP."""
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream",
    }

    payload = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": method,
        "params": params
    }

    response = httpx.post(MCP_ENDPOINT, json=payload, headers=headers, timeout=30.0)
    response.raise_for_status()
    return response.json()


def extract_library_id(response_text: str) -> Optional[str]:
    """Extract the first library ID from resolve response."""
    # Look for Context7-compatible library ID patterns
    id_match = re.search(
        r'Context7-compatible library ID:\s*([/\w.-]+/[\w.-]+(?:/[\w.-]+)?)',
        response_text
    )
    if id_match:
        return id_match.group(1)

    # Fallback: find any /org/project pattern (skip generic placeholders)
    all_matches = re.findall(r'/[\w-]+/[\w.-]+(?:/[\w.-]+)?', response_text)
    filtered = [m for m in all_matches if m != '/org/project']
    return filtered[0] if filtered else None


def extract_library_metadata(response_text: str, library_id: str) -> Dict[str, Any]:
    """Extract metadata for a library from resolve response."""
    # Find the section for this library
    sections = response_text.split('----------')

    for section in sections:
        if library_id in section:
            metadata = {
                'library_id': library_id,
                'library_name': '',
                'description': '',
                'snippet_count': 0,
                'source_reputation': 'Unknown',
                'benchmark_score': 0.0,
            }

            # Extract fields
            if match := re.search(r'Title:\s*(.+)', section):
                metadata['library_name'] = match.group(1).strip()

            if match := re.search(r'Description:\s*(.+?)(?=\n-|\n\n|$)', section, re.DOTALL):
                metadata['description'] = match.group(1).strip()

            if match := re.search(r'Code Snippets:\s*(\d+)', section):
                metadata['snippet_count'] = int(match.group(1))

            if match := re.search(r'Source Reputation:\s*(\w+)', section):
                metadata['source_reputation'] = match.group(1)

            if match := re.search(r'Benchmark Score:\s*([\d.]+)', section):
                metadata['benchmark_score'] = float(match.group(1))

            return metadata

    # Default metadata if not found
    return {
        'library_id': library_id,
        'library_name': library_id.split('/')[-1],
        'description': '',
        'snippet_count': 0,
        'source_reputation': 'Unknown',
        'benchmark_score': 0.0,
    }


def chunk_markdown_by_sections(text: str) -> List[Dict[str, str]]:
    """Split markdown documentation into sections with metadata."""
    chunks = []

    # Split by "###" headers and "---" separators
    sections = re.split(r'\n###\s+|^###\s+|\n-{10,}', text)

    for i, section in enumerate(sections):
        section = section.strip()
        if not section:
            continue

        # Extract title (first line) and content
        lines = section.split('\n', 1)
        title = lines[0].strip() if lines else f"Section {i+1}"
        content = lines[1].strip() if len(lines) > 1 else section

        # Extract source URL if present
        source_url = ""
        if match := re.search(r'Source:\s*(https?://\S+)', content):
            source_url = match.group(1)

        # Check if contains code
        has_code = '```' in content

        # Extract code languages
        code_languages = list(set(re.findall(r'```(\w+)', content)))

        chunks.append({
            'title': title,
            'content': content,
            'source_url': source_url,
            'has_code': has_code,
            'code_languages': code_languages,
        })

    return chunks


@app.command()
def ingest(
    library_name: str = typer.Argument(..., help="Library name (e.g., 'React', 'Next.js')"),
    query: str = typer.Argument(..., help="Query for documentation"),
    db_path: Path = typer.Option(DEFAULT_DB_PATH, "--db", "-d", help="LanceDB path"),
    table_name: str = typer.Option("documentation", "--table", "-t", help="Table name"),
    model_name: str = typer.Option(DEFAULT_MODEL, "--model", "-m", help="Embedding model"),
):
    """
    Ingest documentation from Context7 into LanceDB.

    Example:
        ./context7_lancedb_integration.py ingest "React" "How to use hooks"
    """
    console.print(f"\n[bold cyan]📚 Ingesting {library_name} documentation...[/bold cyan]\n")

    # Step 1: Resolve library
    console.print("[yellow]1️⃣  Resolving library ID...[/yellow]")
    resolve_result = make_mcp_request("tools/call", {
        "name": "resolve-library-id",
        "arguments": {
            "libraryName": library_name,
            "query": query
        }
    })

    resolve_text = resolve_result["result"]["content"][0]["text"]
    library_id = extract_library_id(resolve_text)

    if not library_id:
        console.print("[red]❌ Could not extract library ID[/red]")
        raise typer.Exit(1)

    console.print(f"[green]✓ Resolved to: {library_id}[/green]")

    # Extract metadata
    metadata = extract_library_metadata(resolve_text, library_id)
    console.print(f"[dim]  Name: {metadata['library_name']}[/dim]")
    console.print(f"[dim]  Score: {metadata['benchmark_score']}, Snippets: {metadata['snippet_count']}[/dim]")

    # Step 2: Query documentation
    console.print("\n[yellow]2️⃣  Querying documentation...[/yellow]")
    query_result = make_mcp_request("tools/call", {
        "name": "query-docs",
        "arguments": {
            "libraryId": library_id,
            "query": query
        }
    })

    doc_text = query_result["result"]["content"][0]["text"]
    console.print(f"[green]✓ Retrieved {len(doc_text)} characters of documentation[/green]")

    # Step 3: Chunk the documentation
    console.print("\n[yellow]3️⃣  Chunking documentation...[/yellow]")
    chunks = chunk_markdown_by_sections(doc_text)
    console.print(f"[green]✓ Created {len(chunks)} chunks[/green]")

    # Step 4: Generate embeddings
    if not HAS_EMBEDDINGS:
        console.print("[red]❌ sentence-transformers not available[/red]")
        console.print("[yellow]Install with: pip install sentence-transformers torch[/yellow]")
        raise typer.Exit(1)

    console.print("\n[yellow]4️⃣  Generating embeddings...[/yellow]")
    model = get_model(model_name)
    texts = [chunk['content'] for chunk in chunks]
    embeddings = model.encode(texts, show_progress_bar=True)
    console.print(f"[green]✓ Generated {len(embeddings)} embeddings (dim={embeddings.shape[1]})[/green]")

    # Step 5: Prepare data for LanceDB
    console.print("\n[yellow]5️⃣  Preparing data...[/yellow]")
    timestamp = datetime.utcnow().isoformat()

    data = pd.DataFrame({
        'id': [f"{library_id.replace('/', '_')}_{i:04d}" for i in range(len(chunks))],
        'chunk_index': list(range(len(chunks))),
        'text': [chunk['content'] for chunk in chunks],
        'vector': embeddings.tolist(),

        # Library metadata
        'library_id': [library_id] * len(chunks),
        'library_name': [metadata['library_name']] * len(chunks),
        'library_description': [metadata['description']] * len(chunks),

        # Quality metrics
        'source_reputation': [metadata['source_reputation']] * len(chunks),
        'benchmark_score': [metadata['benchmark_score']] * len(chunks),
        'snippet_count': [metadata['snippet_count']] * len(chunks),

        # Chunk metadata
        'section_title': [chunk['title'] for chunk in chunks],
        'source_url': [chunk['source_url'] for chunk in chunks],
        'has_code': [chunk['has_code'] for chunk in chunks],
        'code_languages': [','.join(chunk['code_languages']) for chunk in chunks],

        # Timestamps
        'ingested_at': [timestamp] * len(chunks),
    })

    # Step 6: Store in LanceDB
    console.print("\n[yellow]6️⃣  Storing in LanceDB...[/yellow]")
    db = lancedb.connect(str(db_path))

    if table_name in db.table_names():
        table = db.open_table(table_name)
        table.add(data)
        console.print(f"[green]✓ Added {len(data)} chunks to existing table '{table_name}'[/green]")
    else:
        table = db.create_table(table_name, data)
        console.print(f"[green]✓ Created table '{table_name}' with {len(data)} chunks[/green]")

    # Summary
    console.print("\n[bold green]🎉 Ingestion complete![/bold green]")
    console.print(f"Library: {metadata['library_name']} ({library_id})")
    console.print(f"Chunks: {len(chunks)}")
    console.print(f"Database: {db_path}")
    console.print(f"Table: {table_name}")


@app.command()
def search(
    query: str = typer.Argument(..., help="Search query"),
    db_path: Path = typer.Option(DEFAULT_DB_PATH, "--db", "-d", help="LanceDB path"),
    table_name: str = typer.Option("documentation", "--table", "-t", help="Table name"),
    library_filter: Optional[str] = typer.Option(None, "--library", "-l", help="Filter by library ID"),
    limit: int = typer.Option(5, "--limit", "-n", help="Number of results"),
    model_name: str = typer.Option(DEFAULT_MODEL, "--model", "-m", help="Embedding model"),
):
    """
    Search the ingested documentation.

    Example:
        ./context7_lancedb_integration.py search "How to use useState"
        ./context7_lancedb_integration.py search "API routes" --library "/vercel/next.js"
    """
    if not HAS_EMBEDDINGS:
        console.print("[red]❌ sentence-transformers not available[/red]")
        raise typer.Exit(1)

    console.print(f"\n[bold cyan]🔍 Searching: {query}[/bold cyan]\n")

    # Open database
    db = lancedb.connect(str(db_path))
    if table_name not in db.table_names():
        console.print(f"[red]❌ Table '{table_name}' not found[/red]")
        console.print(f"[yellow]Available tables: {', '.join(db.table_names())}[/yellow]")
        raise typer.Exit(1)

    table = db.open_table(table_name)

    # Generate query embedding
    console.print("[dim]Generating query embedding...[/dim]")
    model = get_model(model_name)
    query_embedding = model.encode([query])[0]

    # Build search
    search = table.search(query_embedding).limit(limit)

    if library_filter:
        search = search.where(f"library_id = '{library_filter}'")
        console.print(f"[dim]Filtering by library: {library_filter}[/dim]")

    # Execute search
    results = search.to_pandas()

    if len(results) == 0:
        console.print("[yellow]⚠️  No results found[/yellow]")
        return

    # Display results
    console.print(f"[green]✓ Found {len(results)} results[/green]\n")

    for i, row in results.iterrows():
        # Create result panel
        title = f"{row['library_name']} - {row['section_title']}"

        content = f"[bold]Text:[/bold]\n{row['text'][:300]}...\n\n"
        content += f"[bold]Library:[/bold] {row['library_id']}\n"
        content += f"[bold]Score:[/bold] {row['benchmark_score']:.1f} | "
        content += f"[bold]Reputation:[/bold] {row['source_reputation']}\n"

        if row['source_url']:
            content += f"[bold]Source:[/bold] {row['source_url']}\n"

        if row['has_code']:
            content += f"[bold]Code:[/bold] Yes ({row['code_languages']})\n"

        console.print(Panel(content, title=f"[{i+1}] {title}", border_style="cyan"))
        console.print()


@app.command()
def stats(
    db_path: Path = typer.Option(DEFAULT_DB_PATH, "--db", "-d", help="LanceDB path"),
    table_name: str = typer.Option("documentation", "--table", "-t", help="Table name"),
):
    """Show statistics about the documentation database."""
    db = lancedb.connect(str(db_path))

    if table_name not in db.table_names():
        console.print(f"[red]❌ Table '{table_name}' not found[/red]")
        raise typer.Exit(1)

    table = db.open_table(table_name)
    df = table.to_pandas()

    # Overall stats
    console.print("\n[bold cyan]📊 Database Statistics[/bold cyan]\n")

    stats_table = Table(show_header=True, header_style="bold magenta")
    stats_table.add_column("Metric", style="cyan")
    stats_table.add_column("Value", style="green")

    stats_table.add_row("Total Chunks", str(len(df)))
    stats_table.add_row("Total Libraries", str(df['library_id'].nunique()))
    stats_table.add_row("Avg Chunk Length", f"{df['text'].str.len().mean():.0f} chars")
    stats_table.add_row("Chunks with Code", f"{df['has_code'].sum()} ({df['has_code'].sum()/len(df)*100:.1f}%)")
    stats_table.add_row("Avg Benchmark Score", f"{df['benchmark_score'].mean():.1f}")

    console.print(stats_table)

    # Libraries breakdown
    console.print("\n[bold cyan]📚 Libraries[/bold cyan]\n")

    lib_table = Table(show_header=True, header_style="bold magenta")
    lib_table.add_column("Library", style="cyan")
    lib_table.add_column("Chunks", style="green")
    lib_table.add_column("Score", style="yellow")
    lib_table.add_column("Reputation", style="blue")

    for lib_id in df['library_id'].unique():
        lib_df = df[df['library_id'] == lib_id]
        lib_table.add_row(
            lib_df['library_name'].iloc[0],
            str(len(lib_df)),
            f"{lib_df['benchmark_score'].iloc[0]:.1f}",
            lib_df['source_reputation'].iloc[0]
        )

    console.print(lib_table)


if __name__ == "__main__":
    app()
