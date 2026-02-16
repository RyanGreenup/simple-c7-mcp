#!/usr/bin/env python3
"""LanceDB document ingestion and search tool.

This module provides functionality to ingest text files into LanceDB
and perform vector similarity searches on the ingested content.
"""

import lancedb
import pandas as pd
import typer
import torch
from pathlib import Path
from typing import Optional
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

from lance_db_example.chunking import chunk_text, get_chunk_stats

try:
    from sentence_transformers import SentenceTransformer
    HAS_SENTENCE_TRANSFORMERS = True
except ImportError:
    HAS_SENTENCE_TRANSFORMERS = False

app = typer.Typer(help="LanceDB document ingestion and search tool")
console = Console()

# Global model cache
_model = None
_device = None


def get_device() -> str:
    """Get the best available device (cuda, mps, or cpu)."""
    global _device
    if _device is None:
        if torch.cuda.is_available():
            _device = "cuda"
            console.print(f"[green]✓ Using CUDA (GPU): {torch.cuda.get_device_name(0)}[/green]")
        elif hasattr(torch.backends, "mps") and torch.backends.mps.is_available():
            _device = "mps"
            console.print("[green]✓ Using Apple Silicon GPU (MPS)[/green]")
        else:
            _device = "cpu"
            console.print("[yellow]⚠ Using CPU (install CUDA for GPU acceleration)[/yellow]")
    return _device


def get_model(model_name: str = "all-MiniLM-L6-v2"):
    """Get or create the sentence transformer model.

    Args:
        model_name: Name of the sentence-transformers model

    Returns:
        SentenceTransformer model
    """
    global _model
    if _model is None:
        device = get_device()
        console.print(f"[dim]Loading model '{model_name}' on {device}...[/dim]")
        _model = SentenceTransformer(model_name, device=device)
    return _model


def create_embeddings(
    texts: list[str],
    use_transformer: bool = True,
    model_name: str = "all-MiniLM-L6-v2"
) -> list[list[float]]:
    """Create embeddings using sentence-transformers or fallback to simple method.

    Args:
        texts: List of text strings
        use_transformer: Whether to use sentence-transformers model
        model_name: Name of the sentence-transformers model

    Returns:
        List of embedding vectors
    """
    if use_transformer and HAS_SENTENCE_TRANSFORMERS:
        model = get_model(model_name)
        embeddings = model.encode(texts, show_progress_bar=True)
        return embeddings.tolist()
    else:
        if use_transformer and not HAS_SENTENCE_TRANSFORMERS:
            console.print("[yellow]⚠ sentence-transformers not available, using simple embeddings[/yellow]")
        return create_simple_embeddings(texts)


def create_simple_embeddings(texts: list[str]) -> list[list[float]]:
    """Create simple embeddings based on character frequencies.

    Note: This is a fallback. For better results, install sentence-transformers.

    Args:
        texts: List of text strings

    Returns:
        List of embedding vectors (32-dimensional)
    """
    embeddings = []

    for text in texts:
        # Simple character frequency-based embedding (for demo purposes)
        text_lower = text.lower()
        text_len = max(len(text), 1)  # Avoid division by zero

        # Create a simple 32-dimensional vector
        vector = []

        # Basic text statistics (5 dimensions)
        vector.append(min(len(text) / 500.0, 1.0))  # Length (normalized)
        vector.append(min(text.count(' ') / 100.0, 1.0))  # Word count
        vector.append(min(text.count('.') / 10.0, 1.0))  # Sentence count
        vector.append(min(text.count(',') / 20.0, 1.0))  # Comma count
        vector.append(min(sum(1 for c in text if c.isupper()) / 50.0, 1.0))  # Capitals

        # Character frequencies for common letters (26 dimensions)
        for char in 'abcdefghijklmnopqrstuvwxyz':
            freq = text_lower.count(char) / text_len
            vector.append(min(freq * 10, 1.0))  # Scale and cap at 1.0

        # Add one more dimension to make it 32
        vector.append(min(text.count('\n') / 10.0, 1.0))  # Newline count

        # Light normalization - just ensure reasonable values
        max_val = max(abs(x) for x in vector) if vector else 1.0
        if max_val > 0:
            vector = [x / max_val for x in vector]

        embeddings.append(vector)

    return embeddings


@app.command()
def ingest(
    file_path: Path = typer.Argument(..., help="Path to the text file to ingest"),
    db_path: Path = typer.Option(
        "./lancedb_data",
        "--db",
        "-d",
        help="Path to LanceDB database directory"
    ),
    table_name: str = typer.Option(
        "documents",
        "--table",
        "-t",
        help="Name of the table to create/update"
    ),
    chunk_size: int = typer.Option(
        500,
        "--chunk-size",
        "-c",
        help="Size of text chunks in characters"
    ),
    overlap: int = typer.Option(
        50,
        "--overlap",
        "-o",
        help="Overlap between chunks in characters"
    ),
    model: str = typer.Option(
        "all-MiniLM-L6-v2",
        "--model",
        "-m",
        help="Sentence transformer model name (use 'simple' for fallback)"
    ),
):
    """Ingest a text file into LanceDB.

    This command reads a text file, splits it into chunks, generates
    embeddings, and stores them in a LanceDB table.

    Example:
        lance-db-example ingest document.txt
        lance-db-example ingest document.txt --db ./my_db --table my_docs
    """
    console.print(f"\n[bold cyan]📄 Ingesting file: {file_path}[/bold cyan]")

    # Read the file
    if not file_path.exists():
        console.print(f"[bold red]❌ Error: File not found: {file_path}[/bold red]")
        raise typer.Exit(1)

    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    console.print(f"[dim]File size: {len(text)} characters[/dim]")

    # Chunk the text
    console.print(f"[yellow]✂️  Chunking text (chunk_size={chunk_size}, overlap={overlap})...[/yellow]")
    chunks = chunk_text(text, chunk_size=chunk_size, overlap=overlap)
    console.print(f"[green]✓ Created {len(chunks)} chunks[/green]")

    # Generate embeddings
    console.print("[yellow]🔢 Generating embeddings...[/yellow]")
    use_transformer = model != "simple"
    embeddings = create_embeddings(chunks, use_transformer=use_transformer, model_name=model)
    console.print(f"[green]✓ Generated {len(embeddings)} embeddings (dim={len(embeddings[0])})[/green]")

    # Create DataFrame
    data = pd.DataFrame({
        'id': range(len(chunks)),
        'text': chunks,
        'vector': embeddings,
        'source': [str(file_path)] * len(chunks),
        'chunk_index': range(len(chunks)),
    })

    # Connect to LanceDB
    console.print(f"[yellow]🗄️  Connecting to LanceDB at {db_path}...[/yellow]")
    db = lancedb.connect(str(db_path))

    # Create or overwrite table
    console.print(f"[yellow]📊 Creating table '{table_name}'...[/yellow]")
    table = db.create_table(table_name, data, mode="overwrite")

    console.print(f"\n[bold green]✅ Successfully ingested {len(chunks)} chunks into '{table_name}'[/bold green]")
    console.print(f"[dim]Database location: {db_path}[/dim]")

    # Show sample
    console.print("\n[bold]Sample chunk:[/bold]")
    sample_text = chunks[0][:200] + "..." if len(chunks[0]) > 200 else chunks[0]
    console.print(Panel(sample_text, title="First Chunk"))


@app.command()
def search(
    query: str = typer.Argument(..., help="Search query text"),
    db_path: Path = typer.Option(
        "./lancedb_data",
        "--db",
        "-d",
        help="Path to LanceDB database directory"
    ),
    table_name: str = typer.Option(
        "documents",
        "--table",
        "-t",
        help="Name of the table to search"
    ),
    limit: int = typer.Option(
        5,
        "--limit",
        "-l",
        help="Maximum number of results to return"
    ),
    model: str = typer.Option(
        "all-MiniLM-L6-v2",
        "--model",
        "-m",
        help="Sentence transformer model name (use 'simple' for fallback)"
    ),
):
    """Search for similar documents using vector similarity.

    This command performs a vector similarity search on the ingested
    documents and returns the most relevant chunks.

    Example:
        lance-db-example search "machine learning concepts"
        lance-db-example search "python programming" --limit 10
    """
    console.print(f"\n[bold cyan]🔍 Searching for: '{query}'[/bold cyan]")

    # Check if database exists
    if not db_path.exists():
        console.print(f"[bold red]❌ Error: Database not found at {db_path}[/bold red]")
        console.print(f"[yellow]💡 Tip: Run 'ingest' command first to create a database[/yellow]")
        raise typer.Exit(1)

    # Connect to LanceDB
    console.print(f"[dim]Connecting to database at {db_path}...[/dim]")
    db = lancedb.connect(str(db_path))

    try:
        table = db.open_table(table_name)
    except Exception as e:
        console.print(f"[bold red]❌ Error: Table '{table_name}' not found[/bold red]")
        console.print(f"[yellow]💡 Available tables: {', '.join(db.table_names())}[/yellow]")
        raise typer.Exit(1)

    # Generate query embedding
    console.print("[dim]Generating query embedding...[/dim]")
    use_transformer = model != "simple"
    query_embedding = create_embeddings([query], use_transformer=use_transformer, model_name=model)[0]

    # Perform search
    console.print(f"[yellow]🔎 Searching (limit={limit})...[/yellow]")
    results = table.search(query_embedding).limit(limit).to_pandas()

    if len(results) == 0:
        console.print("[yellow]⚠️  No results found[/yellow]")
        return

    console.print(f"\n[bold green]✅ Found {len(results)} results[/bold green]\n")

    # Display results in a nice format
    for idx, row in results.iterrows():
        distance = row.get('_distance', 'N/A')
        text = row['text']
        chunk_idx = row.get('chunk_index', idx)

        # Truncate long text
        display_text = text[:300] + "..." if len(text) > 300 else text

        console.print(f"[bold]Result {idx + 1}[/bold] (distance: {distance:.4f}, chunk: {chunk_idx})")
        console.print(Panel(display_text, border_style="blue"))
        console.print()


@app.command()
def list_tables(
    db_path: Path = typer.Option(
        "./lancedb_data",
        "--db",
        "-d",
        help="Path to LanceDB database directory"
    ),
):
    """List all tables in the database.

    Example:
        lance-db-example list-tables
        lance-db-example list-tables --db ./my_db
    """
    if not db_path.exists():
        console.print(f"[bold red]❌ Error: Database not found at {db_path}[/bold red]")
        raise typer.Exit(1)

    db = lancedb.connect(str(db_path))
    tables = db.table_names()

    if not tables:
        console.print("[yellow]No tables found in database[/yellow]")
        return

    console.print(f"\n[bold cyan]📊 Tables in {db_path}:[/bold cyan]\n")

    table_display = Table(show_header=True, header_style="bold magenta")
    table_display.add_column("Table Name", style="cyan")
    table_display.add_column("Row Count", justify="right")

    for table_name in tables:
        table = db.open_table(table_name)
        row_count = table.count_rows()
        table_display.add_row(table_name, str(row_count))

    console.print(table_display)
    console.print()


@app.command()
def stats(
    db_path: Path = typer.Option(
        "./lancedb_data",
        "--db",
        "-d",
        help="Path to LanceDB database directory"
    ),
    table_name: str = typer.Option(
        "documents",
        "--table",
        "-t",
        help="Name of the table"
    ),
):
    """Show statistics about a table.

    Example:
        lance-db-example stats
        lance-db-example stats --table my_docs
    """
    if not db_path.exists():
        console.print(f"[bold red]❌ Error: Database not found at {db_path}[/bold red]")
        raise typer.Exit(1)

    db = lancedb.connect(str(db_path))

    try:
        table = db.open_table(table_name)
    except Exception as e:
        console.print(f"[bold red]❌ Error: Table '{table_name}' not found[/bold red]")
        raise typer.Exit(1)

    row_count = table.count_rows()

    console.print(f"\n[bold cyan]📊 Statistics for table '{table_name}':[/bold cyan]\n")

    stats_table = Table(show_header=False)
    stats_table.add_column("Property", style="cyan")
    stats_table.add_column("Value", style="yellow")

    stats_table.add_row("Database Path", str(db_path))
    stats_table.add_row("Table Name", table_name)
    stats_table.add_row("Row Count", str(row_count))

    # Get schema info
    schema = table.schema
    stats_table.add_row("Columns", str(len(schema)))
    stats_table.add_row("Column Names", ", ".join([field.name for field in schema]))

    console.print(stats_table)
    console.print()


if __name__ == "__main__":
    app()
