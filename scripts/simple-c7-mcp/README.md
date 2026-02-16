# Context7 MCP API Server

A FastAPI-based server providing Context7-compatible MCP (Model Context Protocol) endpoints with library and document management.

## 🚀 Quick Start

```bash
# Install dependencies
uv sync

# Start the server
just serve

# In another terminal, create a library
just create-library "FastAPI" "Python" "pypi" "Modern web framework"

# Fetch documentation from Context7
just fetch-doc "solid-js"
```

## 📚 Documentation

This project has comprehensive documentation. **Start here:**

### For Users

- **[JUSTFILE_COMMANDS.md](./JUSTFILE_COMMANDS.md)** - Complete command reference and examples
- **[IMPLEMENTATION_STATUS.md](./IMPLEMENTATION_STATUS.md)** - Current feature status and what's working

### For Developers

- **[CLAUDE.md](./CLAUDE.md)** - Claude Code instructions and project overview
- **[IMPLEMENTATION.md](./IMPLEMENTATION.md)** - Complete implementation checklist (25 tasks)
- **[LANCEDB_SCHEMA.md](./LANCEDB_SCHEMA.md)** - Database schema design and patterns
- **[JUSTFILE_IMPLEMENTATION.md](./JUSTFILE_IMPLEMENTATION.md)** - Justfile command implementation status

## ✨ Features

### Implemented ✅

- **Library Management**
  - Create libraries with metadata (name, language, ecosystem, etc.)
  - Auto-generate Context7-compatible IDs
  - LanceDB vector database storage

- **API Server**
  - FastAPI with automatic OpenAPI docs
  - Lifespan management for database initialization
  - Proper error handling with status codes

- **CLI Commands**
  - `just create-library` - Create libraries via API
  - `just fetch-doc` - Fetch from Context7 (partial)
  - Development commands (serve, health, lint, format)

### Coming Soon ⏳

- Document upload and management (Task #23)
- Library listing (Task #16)
- MCP tool endpoints (Tasks #14-15)
- Full Context7 integration workflow

## 🏗️ Architecture

```
FastAPI Server (Granian ASGI)
    ↓
Routers (mcp, libraries, documents)
    ↓
Services (business logic with TypedDict)
    ↓
LanceDB (vector database with Pydantic models)
```

**Key Technologies:**
- **FastAPI** - Web framework
- **LanceDB** - Vector database for embeddings
- **Pydantic** - Schema validation
- **Granian** - ASGI server
- **Typer** - CLI framework

## 📖 API Documentation

Start the server and visit:
- **OpenAPI Docs:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

### Key Endpoints

#### Working ✅
- `GET /health` - Health check
- `POST /api/v1/libraries` - Create library

#### Scaffolded ⏳
- `GET /api/v1/libraries` - List libraries (Task #16)
- `POST /api/v1/documents` - Upload document (Task #23)
- `POST /mcp` - MCP JSON-RPC endpoint (Tasks #14-15)

## 🔧 Development

### Setup

```bash
# Install dependencies
uv sync

# Run type checker
just lint

# Format code
just format
```

### Testing

```bash
# Start server
just serve

# Test health endpoint
just health

# Create a library
just create-library "Test" "Python" "pypi" "Test library"

# List libraries (once implemented)
just list-libraries
```

### Database

**Location:** `./lancedb_data/`

**Reset database:**
```bash
just clean-db
just serve  # Schema reinitializes automatically
```

**Schema updates:**
If you modify models in `c7_mcp/models.py`, you must delete `lancedb_data/` and restart.

## 📋 Implementation Status

**Completed Tasks:** 2/25
- ✅ Task #36: Database layer and models
- ✅ Task #17: Library create endpoint

**Next Priorities:**
- Task #23: Document create endpoint (unlocks upload/fetch commands)
- Task #16: Library list endpoint
- Task #18: Library get endpoint

See [IMPLEMENTATION.md](./IMPLEMENTATION.md) for full task list.

## 🎯 Context7 Integration

The server integrates with Context7's MCP API:

1. **Resolve library names** → Context7 library IDs
2. **Download documentation** → Context7 CDN
3. **Store in LanceDB** → Local vector database

**Example workflow:**
```bash
# Fetch solid-js docs from Context7
just fetch-doc "solid-js"

# This will:
# 1. Resolve "solid-js" → "/npm/solid-js"
# 2. Download from https://context7.com/npm/solid-js/llms.txt
# 3. Create library in our system
# 4. Upload document (once Task #23 is done)
```

## 🛠️ Project Structure

```
c7_mcp/
├── api.py              # FastAPI app
├── cli.py              # CLI entry point
├── db.py               # LanceDB connection
├── models.py           # Database models
├── routers/            # API endpoints
│   ├── mcp.py
│   ├── libraries.py
│   └── documents.py
├── schemas/            # Pydantic schemas
│   ├── mcp.py
│   ├── library.py
│   └── document.py
└── services/           # Business logic
    ├── mcp.py
    ├── library.py
    └── document.py
```

## 📊 Database Schema

**Libraries Table:**
- Core: id, name, context7_id, language, ecosystem
- Optional: description, keywords, urls, author, license
- Metadata: popularity_score, status, timestamps

**Documents Table:**
- Core: id, document_id, library_id, title, text
- Vectors: vector embeddings (2560-dim)
- Chunking: chunk_index, chunk_total
- Metadata: source, created_at

See [LANCEDB_SCHEMA.md](./LANCEDB_SCHEMA.md) for complete details.

## 🤝 Contributing

1. Check [IMPLEMENTATION.md](./IMPLEMENTATION.md) for available tasks
2. Read [CLAUDE.md](./CLAUDE.md) for development guidelines
3. Follow existing patterns in `c7_mcp/services/library.py`
4. Run linting: `just lint`
5. Test your changes: `just serve` + manual testing

## 📝 License

[Add license information]

## 🔗 Links

- [Context7 MCP Specification](https://github.com/context7/mcp-spec)
- [LanceDB Documentation](https://lancedb.github.io/lancedb/)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)

---

**Status:** Library creation working, document endpoints pending
**Last Updated:** 2026-02-16
**Next Priority:** Task #23 (document create endpoint)
