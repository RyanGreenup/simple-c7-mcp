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



## Reflections

It seems like upstash doesn't' really care about us scraping there library. In fact we can publicly iterate over things like:


```
tokens=
curl
. https://context7.com/clickhouse/clickhouse/llms.txt?topic=how+to+deduplicate+table&tokens=10000
```


They're probably a lot more invested in private repo scanning. Which is cool! But not what I **need** right now.
