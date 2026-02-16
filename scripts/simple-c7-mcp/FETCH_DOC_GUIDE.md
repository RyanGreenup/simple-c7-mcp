# fetch-doc Command Guide

Complete guide for using the `just fetch-doc` command effectively with Context7.

## 🎯 Quick Start

```bash
just fetch-doc "solidstart" "How to throw a redirect in SolidStart"
```

## 📚 How It Works

The `fetch-doc` command integrates with Context7's MCP API to intelligently fetch and upload documentation.

### Step-by-Step Flow

```
1. Your Command
   ↓
   just fetch-doc "solidstart" "How to throw a redirect"

2. Context7 MCP API - resolve-library-id
   ↓
   Request: {
     method: "resolve-library-id",
     libraryName: "solidstart",
     query: "How to throw a redirect"  ← Your actual question!
   }

3. Context7 Response
   ↓
   Available libraries ranked by relevance:
   - /websites/solidjs_solid-start (score: 0.95) ✅ Selected
   - /npm/@solidjs/start (score: 0.82)
   - /github/solidjs/solid-start (score: 0.75)

4. Download Documentation
   ↓
   GET https://context7.com/websites/solidjs_solid-start/llms.txt

5. Upload to Your API
   ↓
   POST /api/v1/libraries (create library)
   POST /api/v1/documents (upload doc)
```

## 💡 Why Query Matters

### ❌ Bad: Generic Queries

```bash
# Too generic - Context7 can't disambiguate well
just fetch-doc "solid" "documentation"
just fetch-doc "react" "info"
just fetch-doc "requests" "library"
```

**Problems:**
- Can't distinguish between similar libraries
- No context for relevance scoring
- May return wrong library variant

### ✅ Good: Specific Queries

```bash
# Specific question - Context7 understands intent
just fetch-doc "solidstart" "How to throw a redirect in SolidStart"
just fetch-doc "react" "useState hook for managing component state"
just fetch-doc "requests" "Python HTTP client for making API calls"
```

**Benefits:**
- Clear intent helps disambiguation
- Context7 can rank by relevance
- Returns most appropriate library variant

## 🎨 Query Writing Tips

### 1. Include Your Actual Question (with library name)

**Instead of:**
```bash
just fetch-doc "library" "documentation"
```

**Write:**
```bash
just fetch-doc "library" "How do I [specific task] in [Library]?"
```

**Why include library name in query?**
- Provides additional context for disambiguation
- Matches natural question phrasing
- Helps Context7 rank results better
- Example from Context7: `libraryName: "solidstart"` + `query: "How to throw a redirect in SolidStart"`

### 2. Mention Key Features

**Instead of:**
```bash
just fetch-doc "fastapi" "web framework"
```

**Write:**
```bash
just fetch-doc "fastapi" "REST API with Pydantic validation and OAuth2"
```

### 3. Disambiguate Similar Names

**Instead of:**
```bash
just fetch-doc "start" "documentation"
```

**Write:**
```bash
just fetch-doc "solidstart" "SolidJS meta-framework for server-side rendering"
```

### 4. Include Context

**Instead of:**
```bash
just fetch-doc "ui" "components"
```

**Write:**
```bash
just fetch-doc "daisyui" "Tailwind CSS component library for buttons and cards"
```

## 📋 Real-World Examples

### Frontend Frameworks

```bash
# SolidJS
just fetch-doc "solidjs" "How to use reactive primitives and signals in SolidJS"
just fetch-doc "solidstart" "How to throw a redirect in SolidStart"

# React
just fetch-doc "react" "How to use useState and useEffect hooks in React"
just fetch-doc "next.js" "How to use App router with server components in Next.js"

# Vue
just fetch-doc "vue" "How to use Composition API and reactive refs in Vue 3"
just fetch-doc "nuxt" "How to implement server-side rendering with Nuxt 3"
```

### Backend Frameworks

```bash
# Python
just fetch-doc "fastapi" "How to create a REST API with authentication using FastAPI"
just fetch-doc "django" "How to define ORM models and use the admin interface in Django"
just fetch-doc "flask" "How to create routes and use blueprints in Flask"

# Node.js
just fetch-doc "express" "How to create an HTTP server with middleware in Express"
just fetch-doc "nestjs" "How to use dependency injection and decorators in NestJS"

# Rust
just fetch-doc "axum" "How to build a web API with routing in Axum"
just fetch-doc "actix-web" "How to create HTTP handlers in Actix-web"
```

### Databases

```bash
# SQL
just fetch-doc "postgres" "PostgreSQL window functions and CTEs"
just fetch-doc "sqlite" "Embedded database with full-text search"

# Vector
just fetch-doc "lancedb" "Vector search with Apache Arrow storage"
just fetch-doc "pgvector" "PostgreSQL extension for embeddings"

# Python Data
just fetch-doc "polars" "DataFrame operations and lazy evaluation"
just fetch-doc "duckdb" "In-process SQL analytics with Parquet"
```

### UI Libraries

```bash
# Components
just fetch-doc "daisyui" "Pre-built Tailwind components for forms and buttons"
just fetch-doc "shadcn-ui" "Accessible React components with Radix UI"
just fetch-doc "headlessui" "Unstyled accessible components"

# Styling
just fetch-doc "tailwindcss" "Utility-first CSS with responsive design"
just fetch-doc "unocss" "Instant on-demand atomic CSS engine"
```

### Testing

```bash
# JavaScript
just fetch-doc "vitest" "Unit testing with Vite integration"
just fetch-doc "playwright" "End-to-end testing across browsers"

# Python
just fetch-doc "pytest" "Test fixtures and parametrization"
just fetch-doc "hypothesis" "Property-based testing"
```

## 🚀 Convenience Commands

Pre-configured queries for popular libraries:

```bash
# Built-in convenience commands
just fetch-solidstart    # SolidStart with redirect example
just fetch-fastapi       # FastAPI with auth example
just fetch-react         # React hooks
just fetch-vue           # Vue Composition API
just fetch-daisyui       # DaisyUI components
```

## 🔍 Disambiguation Scenarios

### Scenario 1: Multiple Packages with Same Name

**Library:** "requests"

```bash
# Bad - ambiguous
just fetch-doc "requests" "library"

# Good - specifies Python
just fetch-doc "requests" "Python HTTP client for REST APIs"
```

**Context7 Response:**
- Without context: May return JavaScript `node-fetch` or Python `requests`
- With context: Correctly identifies Python `requests` library

### Scenario 2: Framework vs Sub-package

**Library:** "start"

```bash
# Bad - too vague
just fetch-doc "start" "documentation"

# Good - specifies SolidJS ecosystem
just fetch-doc "solidstart" "SolidJS meta-framework with SSR"
```

### Scenario 3: Version-Specific

**Library:** "vue"

```bash
# Bad - unclear version
just fetch-doc "vue" "components"

# Good - specifies Vue 3 features
just fetch-doc "vue" "Vue 3 Composition API with script setup syntax"
```

## 📊 Context7 Scoring

Context7 ranks libraries by relevance score (0.0 - 1.0):

```
Available Libraries:

1. /websites/solidjs_solid-start
   Score: 0.95
   Match: "SolidStart" + "redirect" in query ✅

2. /npm/@solidjs/start
   Score: 0.82
   Match: Package name similarity

3. /github/solidjs/solid-start
   Score: 0.75
   Match: Repository match
```

Our command automatically selects the **highest scoring** library.

## 🛠️ Advanced Usage

### Check What Was Downloaded

After fetching, the command shows:

```bash
✅ Resolved: SolidStart
   Context7 ID: /websites/solidjs_solid-start
   Score: 0.95

📥 Downloaded: 125430 bytes

✅ Library created: solidstart
   ID: lib-npm-solidstart-abc123

✅ Document uploaded!
   ID: doc-789
   Title: solidstart Documentation
```

### Environment Variables

```bash
# Optional: Set Context7 API key if required
export CONTEXT7_API_KEY="your-key-here"

just fetch-doc "library" "query"
```

### Custom Port

```bash
# Run API on different port
just serve 8080

# In another terminal
just fetch-doc "library" "query" 8080
```

### Batch Fetching

```bash
#!/bin/bash
# fetch-batch.sh

LIBRARIES=(
  "solidstart|How to throw a redirect in SolidStart"
  "fastapi|REST API with Pydantic validation"
  "react|useState and useEffect hooks"
)

for entry in "${LIBRARIES[@]}"; do
  IFS='|' read -r lib query <<< "$entry"
  echo "Fetching: $lib"
  just fetch-doc "$lib" "$query"
  echo ""
done
```

## 🐛 Troubleshooting

### Error: "No libraries found"

**Cause:** Library not available on Context7 or query too vague

**Solution:**
1. Check library name spelling
2. Make query more specific
3. Try alternative library name

```bash
# Try different variations
just fetch-doc "solid-js" "SolidJS reactive framework"
just fetch-doc "solidjs" "Reactive JavaScript library"
```

### Error: "Wrong library selected"

**Cause:** Query doesn't provide enough context

**Solution:** Add more specific details

```bash
# Before
just fetch-doc "start" "documentation"

# After
just fetch-doc "solidstart" "SolidJS meta-framework for server-side rendering"
```

### Error: "Download failed"

**Cause:** Context7 URL not accessible

**Solution:**
1. Check internet connection
2. Verify Context7 service status
3. Try again later

## 💻 Command Line Help

```bash
# Show error with usage examples
just fetch-doc "library" ""

# Output:
❌ Error: query parameter is required

Usage: just fetch-doc LIBRARY 'your question or use case'

Examples:
  just fetch-doc 'solidstart' 'How to throw a redirect in SolidStart'
  just fetch-doc 'fastapi' 'How to create a REST API with authentication'
  just fetch-doc 'react' 'useState hook documentation'

The query helps Context7 find the most relevant library match
and improves documentation quality.
```

## 📚 Further Reading

- [Context7 Documentation](https://context7.com)
- [MCP Protocol Specification](https://github.com/context7/mcp-spec)
- [JUSTFILE_COMMANDS.md](./JUSTFILE_COMMANDS.md) - All commands
- [LANCEDB_SCHEMA.md](./LANCEDB_SCHEMA.md) - Database schema

---

**Pro Tip:** Think of the query as "What would I Google?" - that's the context Context7 needs to find the right library and most relevant documentation!

---

**Last Updated:** 2026-02-16
**Version:** 1.0
