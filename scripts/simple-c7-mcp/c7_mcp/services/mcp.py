"""MCP tool implementations for Context7 compatibility.

This module provides business logic for MCP tools following the JSON-RPC 2.0 protocol.
"""


def resolve_library_id(library_name: str, query: str) -> str:
    """Resolve library name to Context7-compatible ID.

    Args:
        library_name: Name of the library (e.g., "React", "Python").
        query: User's query for context.

    Returns:
        Formatted list of matching libraries with Context7-compatible IDs.
    """
    from c7_mcp.db import get_libraries_table

    libraries = get_libraries_table()

    # 1. Try exact name match
    results = (
        libraries.search()
        .where(f"name = '{library_name}'", prefilter=True)
        .limit(10)
        .to_list()
    )

    # 2. Fallback: LIKE search
    if not results:
        results = (
            libraries.search()
            .where(f"name LIKE '%{library_name}%'", prefilter=True)
            .limit(10)
            .to_list()
        )

    if not results:
        return f"No libraries found matching '{library_name}'"

    # Sort by popularity_score descending
    results.sort(key=lambda x: x.get("popularity_score", 0), reverse=True)

    lines = []
    for lib in results:
        lines.append(f"- Title: {lib['name']}")
        lines.append(f"- Context7-compatible library ID: {lib['context7_id']}")
        if lib.get("description"):
            lines.append(f"- Description: {lib['description']}")
        lines.append(f"- Benchmark Score: {lib.get('popularity_score', 0)}")
        lines.append("")

    return "\n".join(lines).strip()


def query_docs(library_id: str, query: str) -> str:
    """Query documentation for a library.

    Args:
        library_id: Context7-compatible library identifier.
        query: Documentation query string.

    Returns:
        Documentation content relevant to the query.
    """
    from c7_mcp.db import get_documents_table, get_libraries_table

    libraries = get_libraries_table()
    documents = get_documents_table()

    # Find library by context7_id (MCP clients use context7 IDs)
    lib_results = (
        libraries.search()
        .where(f"context7_id = '{library_id}'", prefilter=True)
        .limit(1)
        .to_list()
    )

    # Fallback: try our internal library ID format
    if not lib_results:
        lib_results = (
            libraries.search()
            .where(f"id = '{library_id}'", prefilter=True)
            .limit(1)
            .to_list()
        )

    if not lib_results:
        return f"Library '{library_id}' not found"

    our_lib_id = lib_results[0]["id"]
    lib_name = lib_results[0]["name"]

    # Get all chunks for this library
    chunks = (
        documents.search()
        .where(f"library_id = '{our_lib_id}'", prefilter=True)
        .limit(100)
        .to_list()
    )

    if not chunks:
        return f"No documentation found for library '{lib_name}'"

    # Simple keyword search — find chunks containing query terms
    query_lower = query.lower()
    query_words = [w for w in query_lower.split() if len(w) > 2]

    scored_chunks = []
    for chunk in chunks:
        text = chunk["text"]
        text_lower = text.lower()
        score = sum(1 for w in query_words if w in text_lower)
        scored_chunks.append((score, text))

    scored_chunks.sort(key=lambda x: x[0], reverse=True)

    # Return top content (cap at ~8000 chars to avoid huge responses)
    combined = ""
    for _, text in scored_chunks:
        if len(combined) + len(text) > 8000:
            break
        combined += text + "\n\n"

    return combined.strip() or chunks[0]["text"]
