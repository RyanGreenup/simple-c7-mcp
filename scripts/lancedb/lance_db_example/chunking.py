"""Text chunking utilities for document processing.

This module provides functions for intelligently splitting text into
overlapping chunks with sentence boundary detection.
"""

from typing import List


def chunk_text(text: str, chunk_size: int = 500, overlap: int = 50) -> List[str]:
    """Split text into overlapping chunks with sentence boundary detection.

    This function splits a document into manageable chunks while attempting
    to preserve sentence boundaries for better semantic coherence. Chunks
    overlap to maintain context continuity.

    Args:
        text: The text to split into chunks
        chunk_size: Maximum size of each chunk in characters (default: 500)
        overlap: Number of characters to overlap between chunks (default: 50)

    Returns:
        List of text chunks, with empty chunks filtered out

    Example:
        >>> text = "First sentence. Second sentence. Third sentence."
        >>> chunks = chunk_text(text, chunk_size=30, overlap=10)
        >>> len(chunks) > 0
        True
        >>> all(isinstance(chunk, str) for chunk in chunks)
        True

    Notes:
        - Attempts to break at sentence boundaries (., !, ?, or paragraph breaks)
        - Ensures forward progress to avoid infinite loops
        - Filters out empty chunks
        - Strips whitespace from each chunk
    """
    if not text:
        return []

    chunks = []
    start = 0
    text_len = len(text)

    while start < text_len:
        end = min(start + chunk_size, text_len)
        chunk = text[start:end]

        # Try to break at sentence boundary if possible (only if not at end)
        if end < text_len and len(chunk) > 100:
            # Look for sentence endings in the last part of the chunk
            search_start = max(0, len(chunk) - 100)
            search_chunk = chunk[search_start:]

            for delimiter in ['. ', '! ', '? ', '\n\n']:
                last_delim = search_chunk.rfind(delimiter)
                if last_delim != -1:
                    # Adjust end position
                    actual_delim_pos = search_start + last_delim + len(delimiter)
                    end = start + actual_delim_pos
                    chunk = text[start:end]
                    break

        chunk = chunk.strip()
        if chunk:  # Only add non-empty chunks
            chunks.append(chunk)

        # Move start position forward
        # Ensure we make progress to avoid infinite loop
        next_start = max(end - overlap, start + 1)
        if next_start <= start:
            start = end
        else:
            start = next_start

        # Safety check: if we're not making progress, break
        if start >= text_len:
            break

    return chunks


def chunk_by_sentences(text: str, max_sentences: int = 3, overlap_sentences: int = 1) -> List[str]:
    """Split text into chunks by sentence count.

    Alternative chunking strategy that groups sentences together.

    Args:
        text: The text to split
        max_sentences: Maximum number of sentences per chunk
        overlap_sentences: Number of sentences to overlap between chunks

    Returns:
        List of text chunks

    Example:
        >>> text = "First. Second. Third. Fourth."
        >>> chunks = chunk_by_sentences(text, max_sentences=2, overlap_sentences=1)
        >>> len(chunks) > 0
        True
    """
    if not text:
        return []

    # Simple sentence splitting (can be improved with NLTK or spaCy)
    import re
    sentences = re.split(r'(?<=[.!?])\s+', text)
    sentences = [s.strip() for s in sentences if s.strip()]

    if not sentences:
        return []

    chunks = []
    i = 0

    while i < len(sentences):
        # Take max_sentences sentences
        chunk_sentences = sentences[i:i + max_sentences]
        chunk = ' '.join(chunk_sentences)
        chunks.append(chunk)

        # Move forward by (max_sentences - overlap_sentences)
        step = max(1, max_sentences - overlap_sentences)
        i += step

    return chunks


def chunk_by_paragraphs(text: str, max_paragraphs: int = 2) -> List[str]:
    """Split text into chunks by paragraph.

    Args:
        text: The text to split
        max_paragraphs: Maximum number of paragraphs per chunk

    Returns:
        List of text chunks

    Example:
        >>> text = "Para 1.\\n\\nPara 2.\\n\\nPara 3."
        >>> chunks = chunk_by_paragraphs(text, max_paragraphs=1)
        >>> len(chunks) == 3
        True
    """
    if not text:
        return []

    # Split by double newlines (paragraph breaks)
    paragraphs = text.split('\n\n')
    paragraphs = [p.strip() for p in paragraphs if p.strip()]

    if not paragraphs:
        return []

    chunks = []
    for i in range(0, len(paragraphs), max_paragraphs):
        chunk_paras = paragraphs[i:i + max_paragraphs]
        chunk = '\n\n'.join(chunk_paras)
        chunks.append(chunk)

    return chunks


def chunk_by_tokens(
    text: str,
    max_tokens: int = 512,
    overlap_tokens: int = 50,
    tokenizer=None
) -> List[str]:
    """Split text by token count (useful for transformer models).

    Args:
        text: The text to split
        max_tokens: Maximum number of tokens per chunk
        overlap_tokens: Number of tokens to overlap
        tokenizer: Optional tokenizer (if None, uses simple word splitting)

    Returns:
        List of text chunks

    Example:
        >>> text = "word " * 1000
        >>> chunks = chunk_by_tokens(text, max_tokens=100, overlap_tokens=10)
        >>> len(chunks) > 5
        True
    """
    if not text:
        return []

    if tokenizer is None:
        # Simple word-based tokenization
        words = text.split()
        chunks = []
        i = 0

        while i < len(words):
            chunk_words = words[i:i + max_tokens]
            chunk = ' '.join(chunk_words)
            chunks.append(chunk)

            # Move forward
            step = max(1, max_tokens - overlap_tokens)
            i += step

        return chunks
    else:
        # Use provided tokenizer
        tokens = tokenizer.encode(text)
        chunks = []
        i = 0

        while i < len(tokens):
            chunk_tokens = tokens[i:i + max_tokens]
            chunk = tokenizer.decode(chunk_tokens)
            chunks.append(chunk)

            # Move forward
            step = max(1, max_tokens - overlap_tokens)
            i += step

        return chunks


def get_chunk_stats(chunks: List[str]) -> dict:
    """Get statistics about a list of chunks.

    Args:
        chunks: List of text chunks

    Returns:
        Dictionary with statistics

    Example:
        >>> chunks = ["short", "a longer chunk", "medium"]
        >>> stats = get_chunk_stats(chunks)
        >>> stats['count']
        3
        >>> stats['avg_length'] > 0
        True
    """
    if not chunks:
        return {
            'count': 0,
            'total_chars': 0,
            'avg_length': 0,
            'min_length': 0,
            'max_length': 0,
        }

    lengths = [len(chunk) for chunk in chunks]

    return {
        'count': len(chunks),
        'total_chars': sum(lengths),
        'avg_length': sum(lengths) / len(lengths),
        'min_length': min(lengths),
        'max_length': max(lengths),
    }
