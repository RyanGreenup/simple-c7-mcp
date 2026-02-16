#!/usr/bin/env python3
"""Test markdown chunking with level 3 headers."""

from lance_db_example.chunking import chunk_by_markdown_headers, chunk_markdown_by_level3_headers

# Sample markdown text with ### headers (like Context7 MCP documentation)
markdown_text = """### Example HTTP Handler Rule (XML)

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/operations/server-configuration-parameters/_server_settings_outside_source.md

An example XML configuration for a ClickHouse HTTP handler rule that matches requests to the root URL ('/') with POST or GET methods and a 'no-cache' pragma header, using a dynamic query handler.

```xml
<http_handlers>
    <rule>
        <url>/</url>
        <methods>POST,GET</methods>
        <headers><pragma>no-cache</pragma></headers>
        <handler>
            <type>dynamic_query_handler</type>
            <query_param_name>query</query_param_name>
        </handler>
    </rule>
</http_handlers>
```

--------------------------------

### ClickHouse Server Unclean Restart Log Example

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/operations/_troubleshooting.md

This log snippet illustrates an error message when attempting to start a second instance of `clickhouse-server` in the same directory, indicating an existing status file.

```text
2019.01.11 15:25:11.151730 [ 1 ] {} <Information> : Starting ClickHouse 19.1.0 with revision 54413
2019.01.11 15:25:11.154578 [ 1 ] {} <Information> Application: starting up
2019.01.11 15:25:11.156361 [ 1 ] {} <Information> StatusFile: Status file ./status already exists - unclean restart.
```

--------------------------------

### clickhouse-benchmark Usage Examples

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/operations/utilities/clickhouse-benchmark.md

Demonstrates different ways to run the clickhouse-benchmark tool, including single queries via command line arguments, standard input, and query files.

```bash
$ clickhouse-benchmark --query ["single query"] [keys]

$ echo "single query" | clickhouse-benchmark [keys]
```
"""

def test_markdown_chunking():
    """Test markdown chunking functionality."""
    print("=" * 80)
    print("Testing Markdown Chunking with Level 3 Headers")
    print("=" * 80)

    # Test 1: Basic chunking with metadata
    print("\n📝 Test 1: chunk_by_markdown_headers() with metadata")
    print("-" * 80)
    chunks_with_metadata = chunk_by_markdown_headers(markdown_text)

    print(f"Found {len(chunks_with_metadata)} chunks\n")

    for i, chunk in enumerate(chunks_with_metadata, 1):
        print(f"Chunk {i}:")
        print(f"  Metadata: {chunk['metadata']}")
        print(f"  Content preview: {chunk['content'][:100]}...")
        print()

    # Test 2: Chunking without metadata (just strings)
    print("\n📝 Test 2: chunk_by_markdown_headers() without metadata")
    print("-" * 80)
    chunks_only = chunk_by_markdown_headers(markdown_text, return_metadata=False)

    print(f"Found {len(chunks_only)} chunks\n")
    for i, chunk in enumerate(chunks_only, 1):
        print(f"Chunk {i} ({len(chunk)} chars):")
        print(f"  {chunk[:150]}...")
        print()

    # Test 3: Specialized level 3 chunking
    print("\n📝 Test 3: chunk_markdown_by_level3_headers()")
    print("-" * 80)
    level3_chunks = chunk_markdown_by_level3_headers(markdown_text)

    print(f"Found {len(level3_chunks)} level-3 sections\n")
    for i, chunk in enumerate(level3_chunks, 1):
        lines = chunk.split('\n')
        header = lines[0] if lines else ''
        print(f"Chunk {i}:")
        print(f"  Header: {header}")
        print(f"  Lines: {len(lines)}")
        print(f"  Size: {len(chunk)} chars")
        print()

    # Test 4: Strip headers
    print("\n📝 Test 4: chunk_markdown_by_level3_headers() with strip_headers=True")
    print("-" * 80)
    stripped_chunks = chunk_markdown_by_level3_headers(markdown_text, strip_headers=True)

    print(f"Found {len(stripped_chunks)} chunks\n")
    for i, chunk in enumerate(stripped_chunks, 1):
        lines = chunk.split('\n')[:3]  # First 3 lines
        print(f"Chunk {i} (headers stripped):")
        for line in lines:
            print(f"  {line}")
        print()

    print("=" * 80)
    print("✅ All tests completed!")
    print("=" * 80)


if __name__ == "__main__":
    test_markdown_chunking()
