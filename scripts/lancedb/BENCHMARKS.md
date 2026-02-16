# LanceDB Embedding Model Benchmarks

This document describes how to benchmark different embedding models and compare CPU vs GPU performance.

## Quick Reference

| Command | Description |
|---------|-------------|
| `just bench-cpu` | Quick CPU vs GPU benchmark |
| `just benchmark-multi` | Multi-query benchmark (recommended) |
| `just benchmark-4b` | Benchmark Qwen3-4B model |
| `just benchmark-0_6b` | Benchmark Qwen3-0.6B model |
| `just compare-models` | Compare 8B vs 4B models |
| `just compare-all-models` | Compare all three models |
| `just search-cpu "query" 5` | CPU-only search with timing |
| `just search-4b "query" 5` | Search using 4B model |
| `just search-0_6b "query" 5` | Search using 0.6B model |
| `just ingest-4b file.md` | Ingest using 4B model |
| `just ingest-0_6b file.md` | Ingest using 0.6B model |

## Available Models

### Qwen3-Embedding-8B (Default)
- **Model**: `Qwen/Qwen3-Embedding-8B`
- **Embedding Dimension**: 4096
- **VRAM Required**: ~16GB
- **System RAM (CPU)**: ~16GB
- **MTEB Score**: 70.58 (#1 on multilingual leaderboard)
- **Best For**: Highest quality embeddings, multilingual support, code retrieval
- **Recommended GPU**: RTX 3090/4090 (24GB) or better

### Qwen3-Embedding-4B
- **Model**: `Qwen/Qwen3-Embedding-4B`
- **Embedding Dimension**: 2560
- **VRAM Required**: ~8GB
- **System RAM (CPU)**: ~8GB
- **MTEB Score**: ~68.5
- **Best For**: Balance of quality and resource usage
- **Recommended GPU**: RTX 3060 (12GB) or better

### Qwen3-Embedding-0.6B ⚡
- **Model**: `Qwen/Qwen3-Embedding-0.6B`
- **Embedding Dimension**: 1024
- **VRAM Required**: ~1.2GB
- **System RAM (CPU)**: ~1.2GB
- **Parameters**: 600M
- **MTEB Score**: ~65
- **Best For**: CPU inference, edge devices, high throughput, development
- **Recommended**: Any modern CPU or GPU (even integrated graphics)
- **Special**: CPU performance is competitive with GPU for this size!

**⚠️ Important**: Different models produce different embedding dimensions and **cannot share the same database**. You must re-ingest data when switching models.

### all-MiniLM-L6-v2 (Lightweight)
- **Model**: `all-MiniLM-L6-v2`
- **Embedding Dimension**: 384
- **VRAM Required**: ~2GB
- **System RAM (CPU)**: ~2GB
- **MTEB Score**: ~58
- **Best For**: Low-resource environments, fast inference
- **Recommended GPU**: Any modern GPU or CPU

## Benchmark Commands

### 1. Single Query Benchmark
Compare GPU vs CPU for a single search query:

```bash
just benchmark-cpu "your search query" 5
```

**What it does:**
- Runs the same query on GPU and CPU
- Measures total time (includes model loading)
- Shows speedup factor

**Example output:**
```
📊 Results:
  GPU: 19.75s
  CPU: 12.17s
  Speedup: 0.61x faster on GPU
```

**Note**: First run includes ~15-20s model loading time, so CPU may appear faster.

### 2. Quick Benchmark
Fast benchmark with default query:

```bash
just bench-cpu
```

Uses preset query "search query" with 3 results.

### 3. CPU-Only Search
Run a search on CPU with timing and see results:

```bash
just search-cpu "button component" 5
```

**What it does:**
- Forces CPU inference only
- Shows search results
- Displays timing via `time` command

**Use case**: Testing CPU performance without GPU comparison.

### 4. Multi-Query Benchmark (Recommended)
Most realistic benchmark showing true GPU advantage:

```bash
just benchmark-multi
```

**What it does:**
- Runs 3 different queries sequentially
- Model loads once, then stays in memory
- Shows per-query average time
- Demonstrates real-world performance

**Example output:**
```
📊 Results:
  GPU total: 22.5s (7.5s avg per query)
  CPU total: 85.3s (28.4s avg per query)
  Speedup: 3.79x faster on GPU

Note: First query includes model loading time (~15-20s)
      Subsequent queries show true inference speed
```

**Why this matters**: In production, the model loads once and handles many queries. This benchmark shows the true performance difference.

## Qwen3-4B Benchmarks

### Benchmark 4B Model
Test the smaller Qwen3-4B model:

```bash
just benchmark-4b
```

**What it does:**
- Runs 3 queries on GPU and CPU
- Uses Qwen3-Embedding-4B (8GB VRAM)
- Shows performance for the more efficient model

### Compare 8B vs 4B Models
Direct comparison on GPU:

```bash
just compare-models
```

**What it does:**
- Runs same queries on both 8B and 4B models
- Shows speed difference
- Displays memory and quality trade-offs

**What it does:**
- Automatically creates 4B database if missing
- Runs same queries on both models
- Uses separate databases (required for different embedding dimensions)

**Example output:**
```
📊 Comparison:
  8B model: 22.5s (7.5s avg) - 16GB VRAM, dim=4096, MTEB=70.58
  4B model: 15.3s (5.1s avg) - 8GB VRAM, dim=2560, MTEB=~68.5
  4B is 1.47x faster

Trade-off: 4B uses half the VRAM and is faster, but slightly lower quality
```

**Important**: 4B and 8B models use different databases:
- 8B: `lancedb_data/` (dim=4096)
- 4B: `lancedb_data_4b/` (dim=2560)

### Use 4B Model for Operations

Ingest with 4B:
```bash
just ingest-4b path/to/file.md
```

Search with 4B:
```bash
just search-4b "your query" 5
```

## Working with Multiple Models

### Why Separate Databases?

**Different embedding dimensions are incompatible**:
- Qwen3-8B: 4096 dimensions
- Qwen3-4B: 2560 dimensions
- MiniLM: 384 dimensions

You cannot search a database created with one model using a different model. The vector dimensions must match.

### Database Locations

| Model | Database Path | Embedding Dim |
|-------|---------------|---------------|
| Qwen3-8B (default) | `lancedb_data/` | 4096 |
| Qwen3-4B | `lancedb_data_4b/` | 2560 |
| Qwen3-0.6B | `lancedb_data_0_6b/` | 1024 |
| Custom | Specify with `--db` | Varies |

### Creating 4B Database

```bash
# Ingest data with 4B model
just ingest-4b tests/data/solid.md

# Or manually
uv run lance-db-example ingest file.md --model "Qwen/Qwen3-Embedding-4B" --db lancedb_data_4b
```

## Switching Models

### Temporarily Use Different Model

For a single ingestion:
```bash
uv run lance-db-example ingest file.md --model "Qwen/Qwen3-Embedding-4B"
```

For a single search:
```bash
uv run lance-db-example search "query" --model "Qwen/Qwen3-Embedding-4B"
```

### Change Default Model

Edit `lance_db_example/ingest.py` and change the default model:

```python
# Change this line in get_model() function:
def get_model(model_name: str = "Qwen/Qwen3-Embedding-4B"):  # Changed from 8B
```

Also update in both CLI commands:
```python
model: str = typer.Option(
    "Qwen/Qwen3-Embedding-4B",  # Changed from 8B
    ...
)
```

## Performance Expectations

### Model Loading Time
| Model | GPU Loading | CPU Loading |
|-------|-------------|-------------|
| Qwen3-8B | ~15-20s | ~20-30s |
| Qwen3-4B | ~8-12s | ~12-20s |
| Qwen3-0.6B | ~5-8s | ~5-10s |
| MiniLM | ~2-3s | ~3-5s |

### Per-Query Inference (After Loading)
| Model | GPU (RTX 4090) | CPU (Modern x64) |
|-------|----------------|------------------|
| Qwen3-8B | ~0.5-2s | ~10-30s |
| Qwen3-4B | ~0.3-1s | ~5-15s |
| Qwen3-0.6B | ~0.2-0.5s | ~0.5-2s ⚡ |
| MiniLM | ~0.1-0.3s | ~1-3s |

**Factors affecting speed:**
- Query length
- Batch size
- CPU/GPU model
- Number of results requested

## Best Practices

### For Development
- Use **Qwen3-4B** or **MiniLM** for faster iteration
- Switch to **Qwen3-8B** for final quality testing

### For Production
- **High Quality Required**: Qwen3-8B on GPU
- **Balanced**: Qwen3-4B on GPU
- **Low Resource**: MiniLM on CPU or GPU
- **Budget Constraint**: MiniLM on CPU

### For Benchmarking
1. Run `just benchmark-multi` to see real-world performance
2. Test with your actual queries, not generic ones
3. Consider both cold start and warm inference times
4. Benchmark on target hardware (not just development machine)

## Memory Requirements Summary

| Model | GPU VRAM | System RAM (CPU mode) | Embedding Dim |
|-------|----------|------------------------|---------------|
| Qwen3-8B | 16GB | 16GB | 4096 |
| Qwen3-4B | 8GB | 8GB | 2560 |
| Qwen3-0.6B | 1.2GB | 1.2GB | 1024 |
| MiniLM | 2GB | 2GB | 384 |

## Troubleshooting

### Out of Memory on GPU
```bash
# Switch to smaller model
uv run lance-db-example ingest file.md --model "Qwen/Qwen3-Embedding-4B"

# Or use MiniLM
uv run lance-db-example ingest file.md --model "all-MiniLM-L6-v2"
```

### CPU is Faster Than GPU?
This happens on first query due to model loading. Run `just benchmark-multi` to see true performance.

### Want Fastest Possible
- Use MiniLM on GPU
- Reduce batch size
- Use smaller limit in searches

### Want Best Quality
- Use Qwen3-8B on GPU with 24GB+ VRAM
- Accept longer inference times
- Consider caching frequent queries

## Summary

### Quick Start

1. **Run benchmarks** to understand performance:
   ```bash
   just benchmark-multi  # Test default 8B model
   just benchmark-4b     # Test 4B model (if database exists)
   just compare-models   # Compare both models
   ```

2. **Choose your model** based on results:
   - **Best quality**: Qwen3-8B (16GB VRAM, dim=4096)
   - **Balanced**: Qwen3-4B (8GB VRAM, dim=2560)
   - **Fastest/smallest**: MiniLM (2GB VRAM, dim=384)

3. **Create your database**:
   ```bash
   # Using 8B (default)
   just fetch-library "React"

   # Using 4B
   just ingest-4b tests/data/react.md
   ```

4. **Search and query**:
   ```bash
   # 8B database
   just search "hooks" 5
   just shell

   # 4B database
   just search-4b "hooks" 5
   ```

### Key Takeaways

✅ **Model loading dominates single queries** (~15-20s for 8B, ~8-12s for 4B)
✅ **GPU shows 5-50x speedup** on inference after loading
✅ **Different models need separate databases** (different dimensions)
✅ **Use `benchmark-multi`** for realistic performance testing
✅ **4B model is ~2x faster** than 8B with minimal quality loss
