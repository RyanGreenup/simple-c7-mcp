# Markdown Chunking with LangChain

## Overview

The chunking module now includes **industry-standard markdown chunking** using LangChain's `MarkdownHeaderTextSplitter`.

This is particularly useful for:
- API documentation with ### headers
- Code examples with section headers
- Technical documentation
- Knowledge base articles
- Tutorial content

## Why LangChain?

Instead of implementing custom markdown parsing, we use **LangChain** which is:
- ✅ **Industry Standard** - Used by thousands of AI applications
- ✅ **Well-Tested** - Battle-tested in production
- ✅ **Actively Maintained** - Regular updates and improvements
- ✅ **Feature-Rich** - Supports all markdown header levels
- ✅ **Metadata Support** - Preserves header information

**Research Source:** Context7 MCP
**Library ID:** `/websites/python_langchain_v0_2`
**Benchmark Score:** 77.1
**Code Snippets:** 57,671

## Functions

### 1. `chunk_by_markdown_headers()`
**Full-featured markdown chunking with metadata**

```python
from lance_db_example.chunking import chunk_by_markdown_headers

markdown_text = """
### Example 1
Some content here

### Example 2
More content
"""

# Get chunks with metadata
chunks = chunk_by_markdown_headers(markdown_text)

for chunk in chunks:
    print(f"Header: {chunk['metadata']['h3']}")
    print(f"Content: {chunk['content']}")
```

**Parameters:**
- `text` - Markdown text to split
- `headers_to_split_on` - List of (symbol, name) tuples
  Default: `[("#", "h1"), ("##", "h2"), ("###", "h3")]`
- `strip_headers` - Remove header text from chunks (default: False)
- `return_metadata` - Return dicts with metadata (default: True)

**Returns:**
- List of dicts with `content` and `metadata` keys (if `return_metadata=True`)
- List of strings (if `return_metadata=False`)

### 2. `chunk_markdown_by_level3_headers()`
**Specialized for ### headers**

```python
from lance_db_example.chunking import chunk_markdown_by_level3_headers

# Simple level-3 only splitting
chunks = chunk_markdown_by_level3_headers(markdown_text)

for chunk in chunks:
    print(chunk)
    print("-" * 80)
```

**Parameters:**
- `text` - Markdown text with ### headers
- `strip_headers` - Remove ### from output (default: False)

**Returns:**
- List of text chunks (strings only, no metadata)

**Note:** This is a convenience wrapper around `chunk_by_markdown_headers()` that only splits on `###` headers.

## Example Use Case: API Documentation

Perfect for documentation like Context7 MCP output:

```markdown
### Example HTTP Handler Rule (XML)

Source: https://github.com/example/...

An example XML configuration...

\`\`\`xml
<config>...</config>
\`\`\`

--------------------------------

### Another Example

Source: ...

Description...

\`\`\`python
code_here()
\`\`\`
```

**Each ### section becomes one chunk**, including:
- Header text
- Source URL
- Description
- Code blocks
- Everything until the next ### header

## Test Results

```bash
$ uv run python test_markdown_chunking.py

Testing Markdown Chunking with Level 3 Headers
================================================================================

📝 Test 1: chunk_by_markdown_headers() with metadata
Found 3 chunks

Chunk 1:
  Metadata: {'h3': 'Example HTTP Handler Rule (XML)'}
  Content preview: ### Example HTTP Handler Rule (XML)...

Chunk 2:
  Metadata: {'h3': 'ClickHouse Server Unclean Restart Log Example'}
  Content preview: ### ClickHouse Server Unclean Restart Log Example...

✅ All tests completed!
```

## Integration with LanceDB

Use markdown chunking for ingesting documentation:

```python
from lance_db_example.chunking import chunk_markdown_by_level3_headers
import lancedb
import pandas as pd

# Read markdown file
with open("api_docs.md", "r") as f:
    markdown_text = f.read()

# Chunk by ### headers
chunks = chunk_markdown_by_level3_headers(markdown_text)

# Create embeddings and store in LanceDB
# ... (rest of ingestion pipeline)
```

## Fallback Behavior

If `langchain-text-splitters` is not installed:
- ✅ Graceful fallback to regex-based splitting
- ✅ Works without dependencies
- ⚠️ Less robust than LangChain
- ⚠️ No metadata support in fallback mode

**Recommendation:** Install LangChain for production use:
```bash
uv add langchain-text-splitters
```

## Comparison with Character-based Chunking

| Feature | Character Chunking | Markdown Chunking |
|---------|-------------------|-------------------|
| **Preserves structure** | ❌ Arbitrary breaks | ✅ Natural sections |
| **Metadata** | ❌ None | ✅ Header hierarchy |
| **Code blocks** | ⚠️ May split | ✅ Preserved |
| **Best for** | Plain text, prose | Docs, APIs, tutorials |
| **Library** | Built-in | LangChain |

## When to Use Each

### Use Markdown Chunking When:
- ✅ Document has clear header structure
- ✅ Code examples should stay together
- ✅ Section boundaries are important
- ✅ You want semantic chunking
- ✅ Processing API docs or tutorials

### Use Character Chunking When:
- ✅ Plain text without structure
- ✅ Books, articles, or prose
- ✅ Need specific chunk sizes
- ✅ No markdown formatting

## Advanced Usage

### Custom Header Levels

```python
# Only split on ## and ### (skip #)
chunks = chunk_by_markdown_headers(
    text,
    headers_to_split_on=[
        ("##", "section"),
        ("###", "subsection")
    ]
)
```

### Strip Headers for Clean Content

```python
# Remove header text, keep only content
chunks = chunk_markdown_by_level3_headers(
    text,
    strip_headers=True
)
# Output: "Source: https://..." (no "###" line)
```

### Metadata-Rich Chunks

```python
# Get full metadata for each chunk
chunks = chunk_by_markdown_headers(text, return_metadata=True)

for chunk in chunks:
    metadata = chunk['metadata']
    print(f"Section: {metadata.get('h3', 'N/A')}")
    print(f"Subsection: {metadata.get('h4', 'N/A')}")
    print(f"Content length: {len(chunk['content'])}")
```

## References

- **LangChain Documentation:** [MarkdownHeaderTextSplitter](https://python.langchain.com/docs/how_to/markdown_header_metadata_splitter)
- **Research via:** Context7 MCP (`/websites/python_langchain_v0_2`)
- **Alternative Libraries:**
  - LlamaIndex: `/websites/developers_llamaindex_ai_python`
  - text-splitter (Rust): `/benbrandt/text-splitter`

## Dependencies

```toml
dependencies = [
    "langchain-text-splitters>=0.2.0",  # New
    # ... other dependencies
]
```

Installed with: `uv add langchain-text-splitters`

## Summary

✅ **Industry-standard chunking** using LangChain
✅ **Perfect for API docs** with ### headers
✅ **Metadata preservation** for better search
✅ **Tested and proven** in production
✅ **Graceful fallback** without dependencies

Use `chunk_markdown_by_level3_headers()` for the exact use case shown in the example!
