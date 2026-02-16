# Create a Free alternative to context7
## Overview

- Backend Docs fetch (hard and kinda done)
- MCP Fetch (eashy and simple to copy)
  - FastAPI server
    - Semantic search
      - chroma / fass / lancedb
    - Source docs
      - Fetch (just curl)
      - Investigate chunking
  - FastAPI server
- Source code

## Web UI

I'd love a web ui. e.g.

```


  Fetch any library:

  # Fetch more libraries
  just fetch-library "React"
  just fetch-library "Vue.js"
  just fetch-library "Tailwind CSS"
  just fetch-library "Next.js"

  Query with SQL:

  just shell

  Then in DuckDB:
  -- See all libraries
  SELECT library, COUNT(*) FROM docs GROUP BY library;

  -- Browse daisyUI sections
  SELECT title, library FROM docs WHERE library = 'daisyui' LIMIT 10;

  -- Search across all libraries
  SELECT library, title FROM docs WHERE text LIKE '%component%' LIMIT 5;

  -- Full-text search
  SELECT title FROM docs WHERE library = 'daisyui' AND text LIKE '%button%';

  Vector search:

  # Search with embeddings
  just search "button component" --limit 5
  just search "authentication" --limit 3

  Workflow example:

  # 1. Fetch multiple frameworks
  just fetch-library "React"
  just fetch-library "Svelte"
  just fetch-library "Vue.js"

  # 2. Query them all with SQL
  just shell
  # SELECT library, COUNT(*) as sections FROM docs GROUP BY library;

  # 3. Semantic search across all frameworks
  just search "state management hooks" --limit 10

  You now have a complete documentation pipeline: Context7 API → LanceDB → SQL/Vector Search! 🚀

```


## Reflections

It seems like upstash doesn't' really care about us scraping there library. In fact we can publicly iterate over things like:


```
tokens=
curl
. https://context7.com/clickhouse/clickhouse/llms.txt?topic=how+to+deduplicate+table&tokens=10000
```


They're probably a lot more invested in private repo scanning. Which is cool! But not what I **need** right now.
