# Refactoring: Chunking Module

## Changes Made

Extracted all text chunking logic into a separate module for better code organization and reusability.

## New File Structure

```
lance_db_example/
├── __init__.py
├── cli.py          # CLI entry point
├── ingest.py       # Main logic (ingest, search, embeddings)
└── chunking.py     # Text chunking utilities (NEW)
```

## Chunking Module (`chunking.py`)

### Functions Provided

#### 1. `chunk_text(text, chunk_size=500, overlap=50)`
**Primary chunking function** - Character-based with sentence boundary detection

- Splits text into overlapping chunks
- Attempts to break at sentence boundaries (., !, ?, paragraph breaks)
- Configurable chunk size and overlap
- Ensures forward progress (no infinite loops)
- Filters empty chunks

**Use case:** Default chunking for most documents

#### 2. `chunk_by_sentences(text, max_sentences=3, overlap_sentences=1)`
Groups text by sentence count

- More semantic than character-based
- Preserves complete sentences
- Configurable sentence count and overlap

**Use case:** When you want to preserve sentence boundaries strictly

#### 3. `chunk_by_paragraphs(text, max_paragraphs=2)`
Groups text by paragraphs

- Splits on double newlines (`\n\n`)
- Respects natural document structure
- No overlap

**Use case:** Blog posts, articles with clear paragraph structure

#### 4. `chunk_by_tokens(text, max_tokens=512, overlap_tokens=50, tokenizer=None)`
Token-based chunking for transformer models

- Respects token limits of models (e.g., 512 tokens for BERT)
- Works with or without a tokenizer
- Fallback to word-based splitting if no tokenizer

**Use case:** When working with models with strict token limits

#### 5. `get_chunk_stats(chunks)`
Returns statistics about chunks

```python
{
    'count': 58,
    'total_chars': 12450,
    'avg_length': 214.7,
    'min_length': 89,
    'max_length': 502,
}
```

**Use case:** Debugging, optimization, reporting

## Benefits of Refactoring

### 1. **Separation of Concerns**
- Chunking logic is isolated from ingestion logic
- Easier to test chunking independently
- Clear single responsibility

### 2. **Reusability**
- Chunking functions can be imported by other modules
- Can be used outside of the CLI context
- Easy to use in notebooks or other scripts

### 3. **Extensibility**
- Easy to add new chunking strategies
- Can implement domain-specific chunking
- Simple to experiment with different approaches

### 4. **Testability**
- Chunking logic can be unit tested independently
- Clear inputs and outputs
- No dependencies on CLI or database

### 5. **Documentation**
- All chunking strategies documented in one place
- Clear examples and use cases
- Easy to understand available options

## Migration Guide

### Before (Old Code)
```python
# Chunking was embedded in ingest.py
def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> list[str]:
    # ... chunking logic ...
```

### After (New Code)
```python
# Import from chunking module
from lance_db_example.chunking import chunk_text, get_chunk_stats

# Use as before - API unchanged
chunks = chunk_text(text, chunk_size=500, overlap=50)
stats = get_chunk_stats(chunks)
```

## No Breaking Changes

- All existing functionality preserved
- Same API for `chunk_text()`
- CLI commands work identically
- No changes to user-facing behavior

## Future Enhancements

With this refactoring, we can easily add:

1. **Semantic Chunking**
   - Use embeddings to find natural breakpoints
   - Group semantically related content

2. **Recursive Chunking**
   - Split large chunks recursively
   - Maintain hierarchy

3. **Language-Specific Chunking**
   - Different strategies for different languages
   - Multilingual support

4. **Document-Type Specific**
   - Code chunking (by function/class)
   - Markdown chunking (by headers)
   - HTML chunking (by tags)

5. **Adaptive Chunking**
   - Adjust chunk size based on content
   - Variable overlap based on context

## Testing

All existing tests pass without modification. New unit tests can be added for:

```python
def test_chunk_text():
    text = "First sentence. Second sentence. Third sentence."
    chunks = chunk_text(text, chunk_size=30, overlap=5)
    assert len(chunks) > 0
    assert all(isinstance(c, str) for c in chunks)

def test_chunk_stats():
    chunks = ["short", "medium chunk", "a very long chunk here"]
    stats = get_chunk_stats(chunks)
    assert stats['count'] == 3
    assert stats['avg_length'] > 0
```

## Performance

No performance impact - same underlying algorithm, just better organized.

## Backward Compatibility

✅ 100% backward compatible - existing code works without changes.
