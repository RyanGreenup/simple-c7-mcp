# Claude Code Instructions

This file contains instructions for Claude Code when working on this project.

## Project Overview

**Context7 MCP API Server** - A FastAPI-based server providing:
- Context7-compatible MCP (Model Context Protocol) endpoints
- Library metadata management
- Documentation storage and retrieval
- LanceDB vector database integration

## 📚 Documentation Guide

This project has comprehensive documentation. **Always check these files before implementing features.**

### Core Documentation

#### **[IMPLEMENTATION.md](./IMPLEMENTATION.md)** - Master Implementation Checklist
**Purpose:** Complete implementation plan with 25 tracked tasks

**Use this for:**
- Understanding overall project structure
- Finding which features are implemented vs pending
- Getting detailed implementation steps for each endpoint
- Understanding dependencies between tasks

**Key sections:**
- Task breakdown by category (MCP, Library, Document, Infrastructure)
- Recommended implementation order
- File structure and design decisions
- Verification steps

**Status:** All scaffolding complete, 2 tasks done (database layer, library create)

---

#### **[LANCEDB_SCHEMA.md](./LANCEDB_SCHEMA.md)** - Database Schema Reference
**Purpose:** Complete LanceDB schema design and implementation guide

**Use this for:**
- Understanding the Library and Document models
- Database field definitions and rationale
- LanceDB-specific patterns (Pydantic models, vector types)
- Query patterns and examples
- MCP library resolution logic with disambiguation

**Key sections:**
- Complete Pydantic model definitions
- Field-by-field design rationale (why each field exists)
- MCP lookup process with scoring algorithm
- LanceDB best practices
- Migration guide from existing data

**Important notes:**
- LanceDB uses Pydantic models, not SQL schemas
- No joins - uses denormalization for performance
- Vector embeddings dimension: 2560 (configurable)
- Schema must match exactly when appending data

---

#### **[IMPLEMENTATION_STATUS.md](./IMPLEMENTATION_STATUS.md)** - Current Status
**Purpose:** What's working right now

**Use this for:**
- Quick status check before starting work
- Knowing which endpoints are functional
- Understanding what's been tested
- Finding example API usage

**Key sections:**
- Completed features (database layer, library creation)
- Library schema (required vs optional fields)
- Example API requests/responses
- Files created/modified
- Next steps (prioritized)

**Status as of 2026-02-16:** Library creation fully working, document endpoints pending

---

#### **[JUSTFILE_COMMANDS.md](./JUSTFILE_COMMANDS.md)** - Command Reference
**Purpose:** Complete guide to all `just` commands

**Use this for:**
- Running development commands
- Testing API endpoints via CLI
- Understanding command parameters
- Finding example workflows

**Key commands:**
- `just serve` - Start the FastAPI server
- `just create-library name lang eco [desc]` - Create a library
- `just fetch-doc library [query]` - Fetch from Context7
- `just upload-doc file lib_id [title]` - Upload document
- `just demo` - Run complete demo

**Important:** Some commands depend on unimplemented endpoints (see JUSTFILE_IMPLEMENTATION.md)

---

#### **[JUSTFILE_IMPLEMENTATION.md](./JUSTFILE_IMPLEMENTATION.md)** - Justfile Status
**Purpose:** Which just commands work and which are waiting for backend

**Use this for:**
- Understanding command implementation status
- Knowing which tasks unlock which commands
- Testing procedures for each command
- Command design patterns

**Current status:**
- ✅ `create-library` - Fully working
- ⏳ `list-libraries` - Needs Task #16
- ⏳ `upload-doc` - Needs Task #23
- ⏳ `fetch-doc` - Needs Task #23 (partially working)

---

## 🏗️ Project Structure

```
c7_mcp/
├── api.py                  # FastAPI app with lifespan management
├── cli.py                  # CLI entry point
├── db.py                   # LanceDB connection and initialization
├── models.py               # LanceDB Pydantic models (Library, Document)
│
├── routers/                # FastAPI routers
│   ├── __init__.py
│   ├── mcp.py             # MCP JSON-RPC endpoint (scaffolding)
│   ├── libraries.py       # Library CRUD (create working, rest scaffolded)
│   └── documents.py       # Document CRUD (all scaffolding)
│
├── schemas/                # Pydantic request/response models
│   ├── __init__.py
│   ├── mcp.py             # JSON-RPC 2.0 schemas
│   ├── library.py         # LibraryCreate, LibraryResponse, etc.
│   └── document.py        # DocumentCreate, DocumentResponse, etc.
│
├── services/               # Business logic (TypedDict pattern)
│   ├── mcp.py             # MCP tool implementations (scaffolding)
│   ├── library.py         # Library CRUD (create working, rest scaffolded)
│   └── document.py        # Document CRUD (all scaffolding)
│
└── commands/               # CLI commands
    └── serve.py           # Server startup command
```

## 🎯 Implementation Guidelines

### When Implementing New Features

1. **Check IMPLEMENTATION.md first**
   - Find the task number and description
   - Read the TODO comments in the relevant files
   - Follow the step-by-step implementation guide

2. **Follow Existing Patterns**
   - **Service layer:** Uses TypedDict for return types (see `library.py`)
   - **Routers:** Async functions with clear docstrings
   - **Error handling:** HTTPException with appropriate status codes
   - **Schemas:** Pydantic models with Field validation

3. **Service Layer Pattern Example**
   ```python
   # In c7_mcp/services/library.py
   def create_library(name: str, language: str, ecosystem: str) -> LibraryData:
       """Create a new library.

       Args:
           name: Library name.
           language: Programming language.
           ecosystem: Package ecosystem.

       Returns:
           Created library data.

       Raises:
           ValueError: If library already exists.
       """
       # 1. Validate uniqueness
       # 2. Generate ID
       # 3. Store in database
       # 4. Return LibraryData TypedDict
   ```

4. **Router Pattern Example**
   ```python
   # In c7_mcp/routers/libraries.py
   @router.post("", response_model=LibraryResponse, status_code=201)
   async def create_library(library: LibraryCreate) -> LibraryResponse:
       """Create a new library.

       Args:
           library: Library creation data.

       Returns:
           Created library with metadata.

       Raises:
           HTTPException: 400 if duplicate, 500 if server error.
       """
       try:
           data = library_service.create_library(...)
           return LibraryResponse(**data)
       except ValueError as e:
           raise HTTPException(status_code=400, detail=str(e))
   ```

### Database Considerations

**LanceDB Specifics:**
- Uses Pydantic models, not SQL
- Schema must match exactly when adding data
- No SQL joins - denormalize data for performance
- Vector fields use `Vector(dimension)` type
- Dictionary fields must be JSON strings (`metadata_json: str`)

**Schema Updates:**
If you modify a model in `c7_mcp/models.py`:
1. Stop the server
2. Delete `lancedb_data/` directory
3. Restart server (schema reinitializes)

**Accessing the database:**
```python
from c7_mcp.db import get_libraries_table, get_documents_table

libraries = get_libraries_table()
results = libraries.search().where("ecosystem = 'npm'").limit(10).to_list()
```

### Testing New Features

1. **Type checking:** `uv run pyright c7_mcp/`
2. **Linting:** `uv run ruff check c7_mcp/`
3. **Start server:** `just serve` or `uv run c7-mcp serve`
4. **Test endpoint:** Use `just` commands or `curl`
5. **Check logs:** Server logs in terminal

### Error Handling

**Status Codes:**
- `200 OK` - Successful GET, PUT, PATCH
- `201 Created` - Successful POST
- `400 Bad Request` - Validation errors, duplicates
- `404 Not Found` - Resource not found
- `422 Unprocessable Entity` - Pydantic validation (automatic)
- `500 Internal Server Error` - Unexpected errors
- `501 Not Implemented` - Scaffolding endpoints (use for TODOs)

**Pattern:**
```python
try:
    result = service_function(...)
    return Response(**result)
except ValueError as e:  # Known errors
    raise HTTPException(status_code=400, detail=str(e))
except Exception as e:  # Unexpected errors
    raise HTTPException(status_code=500, detail=f"Failed: {str(e)}")
```

## 🔧 Common Tasks

### Add a New Library Field

1. Update `Library` model in `c7_mcp/models.py`
2. Update `LibraryData` TypedDict in `c7_mcp/services/library.py`
3. Update `LibraryCreate` and `LibraryResponse` in `c7_mcp/schemas/library.py`
4. Update `create_library()` to include new field
5. Delete `lancedb_data/` and restart server
6. Update documentation if needed

### Implement a Scaffolded Endpoint

Example: Implementing `list_libraries()`

1. **Find the task:** Task #16 in IMPLEMENTATION.md
2. **Read the TODOs:** In `c7_mcp/services/library.py` and `c7_mcp/routers/libraries.py`
3. **Implement service function:**
   ```python
   def list_libraries() -> list[LibraryData]:
       libraries = get_libraries_table()
       results = libraries.search().limit(100).to_list()
       return [dict(r) for r in results]
   ```
4. **Update router:**
   ```python
   async def list_libraries() -> list[LibraryResponse]:
       data = library_service.list_libraries()
       return [LibraryResponse(**lib) for lib in data]
   ```
5. **Test:** `just list-libraries`

### Add Context7 Integration

The MCP protocol uses JSON-RPC 2.0. See `c7_mcp/routers/mcp.py` for the endpoint structure.

**Example MCP request:**
```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "resolve-library-id",
    "arguments": {
      "libraryName": "React",
      "query": "JavaScript UI library"
    }
  }
}
```

**Implementation guide:** See LANCEDB_SCHEMA.md section "MCP Library Lookup Process"

## 📋 Task Priorities

### High Priority (Unlock Key Features)
- **Task #16:** List libraries - Enables `just list-libraries`
- **Task #23:** Create document - Enables `just upload-doc` and `just fetch-doc`
- **Task #18:** Get library by ID - Basic CRUD completion

### Medium Priority (Complete CRUD)
- **Task #19-21:** Library update/delete endpoints
- **Task #22:** List documents
- **Task #24:** Fetch document from URL
- **Task #25-35:** Remaining document endpoints

### Low Priority (Advanced Features)
- **Task #14-15:** MCP tools (resolve-library-id, query-docs)
- **Task #37:** Error handling infrastructure
- **Task #38:** Testing infrastructure

## 🚨 Important Notes

### Don't Do This
- ❌ Don't modify schemas without deleting `lancedb_data/`
- ❌ Don't use `dict` type in LanceDB models (use JSON strings)
- ❌ Don't skip type checking and linting
- ❌ Don't create endpoints without service layer functions
- ❌ Don't forget to add fields to all three places (model, service, schema)

### Do This
- ✅ Read IMPLEMENTATION.md before implementing
- ✅ Follow existing patterns in `library.py`
- ✅ Use TypedDict for service return types
- ✅ Add comprehensive docstrings (Google style)
- ✅ Test with `just` commands
- ✅ Run type checking and linting
- ✅ Update task status when completing features

## 🔍 Quick Reference

### Start Development
```bash
just serve              # Start server
just health             # Check server
```

### Create a Library
```bash
just create-library "TestLib" "Python" "pypi" "A test library"
```

### Check Implementation Status
- Read IMPLEMENTATION_STATUS.md
- Check task list: `just` commands show status

### Find Code Examples
- Service layer: `c7_mcp/services/library.py` (create_library function)
- Router: `c7_mcp/routers/libraries.py` (create_library endpoint)
- Schema: `c7_mcp/schemas/library.py` (LibraryCreate, LibraryResponse)

### Debug Issues
1. Check server logs (Terminal 1)
2. Run type checker: `uv run pyright c7_mcp/`
3. Run linter: `uv run ruff check c7_mcp/`
4. Check IMPLEMENTATION.md for TODO comments

## 📞 Getting Help

1. **For implementation details:** Read IMPLEMENTATION.md
2. **For database questions:** Read LANCEDB_SCHEMA.md
3. **For current status:** Read IMPLEMENTATION_STATUS.md
4. **For command usage:** Read JUSTFILE_COMMANDS.md
5. **For patterns:** Look at existing working code in `c7_mcp/services/library.py`

## 🎯 Current Focus Areas

Based on JUSTFILE_IMPLEMENTATION.md, the next priority is:

**Task #23: Implement document create endpoint**
- This unlocks `just upload-doc` and `just fetch-doc`
- Enables full Context7 integration workflow
- Required for demo commands

See IMPLEMENTATION.md Task #23 for detailed steps.

---

**Last Updated:** 2026-02-16
**Project Status:** Library creation working, document endpoints pending
**Next Priority:** Task #23 (document create endpoint)
