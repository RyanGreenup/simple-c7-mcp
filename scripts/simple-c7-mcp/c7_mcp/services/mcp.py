"""MCP tool implementations for Context7 compatibility.

This module provides business logic for MCP tools following the JSON-RPC 2.0 protocol.
"""

import json
import os
import urllib.request


def _guess_language(ecosystem: str) -> str:
    """Best-effort language hint from ecosystem."""
    mapping = {
        "npm": "TypeScript/JavaScript",
        "pypi": "Python",
        "crates": "Rust",
        "nuget": "C#",
        "maven": "Java",
        "go": "Go",
    }
    return mapping.get(ecosystem, "Unknown")


def _resolve_remote_context7_library(
    library_name: str, query: str
) -> tuple[str, str, str]:
    """Resolve a library from Context7 MCP.

    Returns:
        Tuple of (title, context7_id, description).
    """
    mcp_url = "https://mcp.context7.com/mcp"
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream",
    }
    api_key = os.environ.get("CONTEXT7_API_KEY", "")
    if api_key:
        headers["CONTEXT7_API_KEY"] = api_key

    request_data = {
        "jsonrpc": "2.0",
        "id": 1,
        "method": "tools/call",
        "params": {
            "name": "resolve-library-id",
            "arguments": {
                "libraryName": library_name,
                "query": query or f"Official documentation for {library_name}",
            },
        },
    }

    req = urllib.request.Request(
        mcp_url,
        data=json.dumps(request_data).encode("utf-8"),
        headers=headers,
    )
    with urllib.request.urlopen(req, timeout=30) as response:
        result = json.loads(response.read().decode("utf-8"))

    content_text = result["result"]["content"][0]["text"]

    libraries: list[dict[str, str | float]] = []
    current: dict[str, str | float] = {}
    for raw_line in content_text.split("\n"):
        line = raw_line.strip()
        if line.startswith("- Title:"):
            if current.get("id"):
                libraries.append(current)
            current = {"title": line.split("- Title:", 1)[1].strip()}
        elif line.startswith("- Context7-compatible library ID:"):
            current["id"] = line.split("Context7-compatible library ID:", 1)[1].strip()
        elif line.startswith("- Description:"):
            current["description"] = line.split("- Description:", 1)[1].strip()
        elif line.startswith("- Benchmark Score:"):
            try:
                current["score"] = float(
                    line.split("- Benchmark Score:", 1)[1].strip()
                )
            except ValueError:
                current["score"] = 0.0

    if current.get("id"):
        libraries.append(current)

    if not libraries:
        raise ValueError(f"No Context7 library candidates found for '{library_name}'")

    libraries.sort(key=lambda item: float(item.get("score", 0.0)), reverse=True)
    best = libraries[0]
    return (
        str(best.get("title", library_name)),
        str(best["id"]),
        str(best.get("description", "")),
    )


def _find_local_library_by_name_or_context7(
    *, library_name: str, context7_id: str | None = None
) -> dict | None:
    """Find a local library by name or context7_id."""
    from c7_mcp.db import get_libraries_table

    libraries = get_libraries_table()

    if context7_id:
        by_context7 = (
            libraries.search()
            .where(f"context7_id = '{context7_id}'", prefilter=True)
            .limit(1)
            .to_list()
        )
        if by_context7:
            return by_context7[0]

    by_name = (
        libraries.search()
        .where(f"name = '{library_name}'", prefilter=True)
        .limit(1)
        .to_list()
    )
    if by_name:
        return by_name[0]

    return None


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


def fetch_library_docs(
    library_name: str,
    query: str,
    fetch_if_missing: bool,
) -> str:
    """Fetch docs from Context7 only when missing locally and explicitly requested."""
    from c7_mcp.services import document as document_service
    from c7_mcp.services import library as library_service

    existing = _find_local_library_by_name_or_context7(library_name=library_name)
    if existing:
        return (
            f"Library '{existing['name']}' already exists locally "
            f"(id: {existing['id']}, context7_id: {existing['context7_id']}). "
            "Skipping remote fetch."
        )

    if not fetch_if_missing:
        return (
            f"Library '{library_name}' was not found locally. "
            "Remote fetch is disabled unless you explicitly pass "
            "`fetchIfMissing: true`."
        )

    try:
        resolved_title, context7_id, description = _resolve_remote_context7_library(
            library_name,
            query,
        )
    except Exception as exc:
        return f"Failed to resolve '{library_name}' via Context7: {exc}"

    existing_after_resolve = _find_local_library_by_name_or_context7(
        library_name=resolved_title,
        context7_id=context7_id,
    )
    if existing_after_resolve:
        return (
            f"Library '{existing_after_resolve['name']}' already exists locally "
            f"(id: {existing_after_resolve['id']}, "
            f"context7_id: {existing_after_resolve['context7_id']}). "
            "Skipping remote fetch."
        )

    ecosystem = "unknown"
    parts = [p for p in context7_id.split("/") if p]
    if parts:
        ecosystem = parts[0]

    try:
        created_lib = library_service.create_library(
            name=resolved_title,
            language=_guess_language(ecosystem),
            ecosystem=ecosystem,
            description=description,
            context7_id=context7_id,
            aliases=[library_name] if resolved_title != library_name else [],
            keywords=["context7", "auto-fetched"],
            category="documentation",
        )
    except Exception as exc:
        return f"Failed to create local library for '{resolved_title}': {exc}"

    url = f"https://context7.com{context7_id}/llms.txt"
    try:
        doc = document_service.fetch_document(
            title=f"{resolved_title} Documentation",
            url=url,
            library_id=created_lib["id"],
        )
    except Exception as exc:
        return (
            f"Library '{resolved_title}' was created (id: {created_lib['id']}), "
            f"but docs fetch from {url} failed: {exc}"
        )

    return (
        f"Fetched '{resolved_title}' from Context7 and ingested docs. "
        f"library_id={created_lib['id']}, context7_id={context7_id}, "
        f"document_id={doc['id']}."
    )


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
