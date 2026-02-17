# Context7 MCP API Implementation Checklist

This document tracks the implementation progress of all CRUD operations for the Context7-compatible MCP server with library and document management.

## Overview

- **Total Tasks**: 25
- **Completed**: 8
- **In Progress**: 0
- **Not Started**: 17

## 📊 Progress by Category

| Category       | Total | Completed | In Progress | Not Started |
| -------------- | ----- | --------- | ----------- | ----------- |
| MCP Tools      | 2     | 2         | 0           | 0           |
| Library CRUD   | 6     | 2         | 0           | 4           |
| Document CRUD  | 13    | 4         | 0           | 9           |
| Infrastructure | 3     | 0         | 0           | 3           |
| Testing        | 1     | 0         | 0           | 1           |

## 🎯 Recommended Implementation Order

1. **Infrastructure First** (Task #36) - Set up database layer
2. **Error Handling** (Task #37) - Create consistent error responses
3. **Library CRUD** (Tasks #16-21) - Simpler entity, fewer dependencies
4. **Document CRUD** (Tasks #22-35) - Depends on libraries
5. **MCP Tools** (Tasks #14-15) - Depends on both libraries and documents
6. **Testing** (Task #38) - Validate everything works

---

## 🔧 MCP Tools (2 tasks)

### Task #14: Implement MCP resolve-library-id tool

**Status**: ✅ Completed
**Priority**: Medium
**Files**: `c7_mcp/services/mcp.py`, `c7_mcp/routers/mcp.py`

**Implementation Steps**:

- [x] Parse ResolveLibraryIdArgs from request.params.arguments
- [x] Query library database for matching names
- [x] Use query context to disambiguate if multiple matches
- [x] Return standardized library ID format (e.g., /npm/react)
- [x] Handle library not found cases with appropriate error messages
- [ ] Add logging for tool invocations
- [x] Update router to call service function and wrap result in TextContent

---

### Task #15: Implement MCP query-docs tool

**Status**: ✅ Completed
**Priority**: Medium
**Files**: `c7_mcp/services/mcp.py`, `c7_mcp/routers/mcp.py`

**Implementation Steps**:

- [x] Parse QueryDocsArgs from request.params.arguments
- [x] Validate library_id exists in database
- [x] Retrieve and search documentation content
- [x] Use semantic search or vector embeddings for relevance
- [x] Format response with relevant code examples
- [x] Handle library not found or no results cases
- [ ] Add logging for tool invocations
- [x] Update router to call service function and wrap result in TextContent

---

## 📚 Library CRUD (6 tasks)

### Task #16: Implement library list endpoint

**Status**: ⬜ Not Started
**Priority**: High
**Files**: `c7_mcp/services/library.py`, `c7_mcp/routers/libraries.py`
**Endpoint**: `GET /api/v1/libraries`

**Implementation Steps**:

- [ ] Query database for all libraries
- [ ] Include document counts for each library
- [ ] Order by creation date or name
- [ ] Support pagination parameters (limit, offset)
- [ ] Transform LibraryData to LibraryResponse in router
- [ ] Handle database errors with 500 status

---

### Task #17: Implement library create endpoint

**Status**: ⬜ Not Started
**Priority**: High
**Files**: `c7_mcp/services/library.py`, `c7_mcp/routers/libraries.py`
**Endpoint**: `POST /api/v1/libraries`

**Implementation Steps**:

- [ ] Validate name uniqueness in database
- [ ] Generate unique ID for library
- [ ] Store library in database with metadata
- [ ] Initialize empty document collection
- [ ] Transform LibraryData to LibraryResponse in router
- [ ] Handle duplicate name errors with 400 status
- [ ] Handle other errors with 500 status

---

### Task #18: Implement library get endpoint

**Status**: ✅ Completed
**Priority**: High
**Files**: `c7_mcp/services/library.py`, `c7_mcp/routers/libraries.py`
**Endpoint**: `GET /api/v1/libraries/{library_id}`

**Implementation Steps**:

- [x] Query database by library ID
- [x] Count associated documents
- [x] Raise ValueError if library not found
- [x] Transform LibraryData to LibraryResponse in router
- [x] Handle not found errors with 404 status
- [x] Handle other errors with 500 status

---

### Task #19: Implement library full update endpoint

**Status**: ⬜ Not Started
**Priority**: Medium
**Files**: `c7_mcp/services/library.py`, `c7_mcp/routers/libraries.py`
**Endpoint**: `PUT /api/v1/libraries/{library_id}`

**Implementation Steps**:

- [ ] Verify library exists in database
- [ ] Validate name uniqueness (excluding current library)
- [ ] Update all fields (name, description)
- [ ] Update updated_at timestamp
- [ ] Transform LibraryData to LibraryResponse in router
- [ ] Handle not found errors with 404 status
- [ ] Handle duplicate name errors with 400 status
- [ ] Handle other errors with 500 status

---

### Task #20: Implement library partial update endpoint

**Status**: ⬜ Not Started
**Priority**: Medium
**Files**: `c7_mcp/services/library.py`, `c7_mcp/routers/libraries.py`
**Endpoint**: `PATCH /api/v1/libraries/{library_id}`

**Implementation Steps**:

- [ ] Verify library exists in database
- [ ] Update only provided fields
- [ ] Validate name uniqueness if name provided
- [ ] Update updated_at timestamp
- [ ] Transform LibraryData to LibraryResponse in router
- [ ] Handle not found errors with 404 status
- [ ] Handle duplicate name errors with 400 status
- [ ] Handle other errors with 500 status

---

### Task #21: Implement library delete endpoint

**Status**: ✅ Completed
**Priority**: Medium
**Files**: `c7_mcp/services/library.py`, `c7_mcp/routers/libraries.py`
**Endpoint**: `DELETE /api/v1/libraries/{library_id}`

**Implementation Steps**:

- [x] Verify library exists in database
- [x] Decide on handling documents (cascade delete or prevent if has documents)
- [x] Delete library from database
- [x] Clean up associated resources
- [x] Return DeleteResponse with success=True
- [x] Handle not found errors with 404 status
- [x] Handle libraries with documents with 400 status (if preventing deletion)
- [x] Handle other errors with 500 status

**Design Decision**: Prevents deletion if library has associated documents (returns 400). Documents must be deleted first.

---

## 📄 Document CRUD (13 tasks)

### Task #22: Implement document list endpoint

**Status**: ⬜ Not Started
**Priority**: High
**Files**: `c7_mcp/services/document.py`, `c7_mcp/routers/documents.py`
**Endpoint**: `GET /api/v1/documents`

**Implementation Steps**:

- [ ] Query database with filters
- [ ] Apply library_id filter if provided
- [ ] Apply pagination (limit, offset)
- [ ] Order by creation date
- [ ] Include embeddings status (has_embeddings)
- [ ] Transform DocumentData to DocumentResponse (exclude content)
- [ ] Handle errors with 500 status

---

### Task #23: Implement document create endpoint

**Status**: ⬜ Not Started
**Priority**: High
**Files**: `c7_mcp/services/document.py`, `c7_mcp/routers/documents.py`
**Endpoint**: `POST /api/v1/documents`

**Implementation Steps**:

- [ ] Verify library exists in database
- [ ] Generate unique ID for document
- [ ] Store content and metadata
- [ ] Initialize embeddings status as False
- [ ] Update library document count
- [ ] Transform DocumentData to DocumentResponse in router
- [ ] Handle library not found errors with 404 status
- [ ] Handle other errors with 500 status

---

### Task #24: Implement document fetch from URL endpoint

**Status**: ✅ Completed
**Priority**: High
**Files**: `c7_mcp/services/document.py`, `c7_mcp/routers/documents.py`
**Endpoint**: `POST /api/v1/documents/fetch`

**Implementation Steps**:

- [x] Verify library exists in database
- [x] Fetch content from URL (handle timeouts, HTTP errors)
- [x] Parse content (handle different formats: HTML, PDF, Markdown, etc.)
- [x] Extract text content from parsed documents
- [x] Generate unique ID for document
- [x] Store parsed content and metadata
- [ ] Update library document count
- [x] Transform DocumentData to DocumentResponse in router
- [x] Handle library not found errors with 404 status
- [x] Handle URL fetch errors with 400 status
- [x] Handle other errors with 500 status

**Design Decision**: Uses `urllib.request` (stdlib) with 30s timeout. Detects source_type from Content-Type header and URL extension. Sets `source` to the URL.

---

### Task #25: Implement document get metadata endpoint

**Status**: ✅ Completed
**Priority**: High
**Files**: `c7_mcp/services/document.py`, `c7_mcp/routers/documents.py`
**Endpoint**: `GET /api/v1/documents/{doc_id}`

**Implementation Steps**:

- [x] Query database by document ID
- [x] Include all metadata fields
- [x] Raise ValueError if document not found
- [x] Transform DocumentData to DocumentResponse (exclude content) in router
- [x] Handle not found errors with 404 status
- [x] Handle other errors with 500 status

---

### Task #26: Implement document get content endpoint

**Status**: ✅ Completed
**Priority**: High
**Files**: `c7_mcp/services/document.py`, `c7_mcp/routers/documents.py`
**Endpoint**: `GET /api/v1/documents/{doc_id}/content`

**Implementation Steps**:

- [x] Query database by document ID
- [x] Return only content field
- [x] Raise ValueError if document not found
- [x] Return DocumentContent with raw text in router
- [x] Handle not found errors with 404 status
- [x] Handle other errors with 500 status

---

### Task #27: Implement document get pretty endpoint

**Status**: ⬜ Not Started
**Priority**: Medium
**Files**: `c7_mcp/routers/documents.py`
**Endpoint**: `GET /api/v1/documents/{doc_id}/pretty`

**Implementation Steps**:

- [ ] Call document_service.get_document()
- [ ] Return DocumentPretty with title and content
- [ ] Apply formatting (markdown, syntax highlighting, etc.)
- [ ] Handle not found errors with 404 status
- [ ] Handle other errors with 500 status

---

### Task #28: Implement document get title endpoint

**Status**: ⬜ Not Started
**Priority**: Low
**Files**: `c7_mcp/routers/documents.py`
**Endpoint**: `GET /api/v1/documents/{doc_id}/title`

**Implementation Steps**:

- [ ] Call document_service.get_document()
- [ ] Return DocumentTitle with title only
- [ ] Handle not found errors with 404 status
- [ ] Handle other errors with 500 status

---

### Task #29: Implement document get embeddings endpoint

**Status**: ⬜ Not Started
**Priority**: High
**Files**: `c7_mcp/services/document.py`, `c7_mcp/routers/documents.py`
**Endpoint**: `GET /api/v1/documents/{doc_id}/embeddings`

**Implementation Steps**:

- [ ] Query database by document ID
- [ ] Verify embeddings exist
- [ ] Return embedding vector and metadata
- [ ] Return DocumentEmbeddings with vectors in router
- [ ] Handle not found errors with 404 status
- [ ] Handle no embeddings errors with 404 and specific message
- [ ] Handle other errors with 500 status

---

### Task #30: Implement document full update endpoint

**Status**: ⬜ Not Started
**Priority**: Medium
**Files**: `c7_mcp/routers/documents.py`
**Endpoint**: `PUT /api/v1/documents/{doc_id}`

**Implementation Steps**:

- [ ] Combine update_content, update_title, update_library service calls
- [ ] Verify document and target library exist
- [ ] Update all fields (title, content, library_id)
- [ ] Invalidate embeddings after content update (set has_embeddings to False)
- [ ] Update updated_at timestamp
- [ ] Transform DocumentData to DocumentResponse in router
- [ ] Handle not found errors with 404 status
- [ ] Handle other errors with 500 status

---

### Task #31: Implement document update content endpoint

**Status**: ✅ Completed
**Priority**: High
**Files**: `c7_mcp/services/document.py`, `c7_mcp/routers/documents.py`
**Endpoint**: `PATCH /api/v1/documents/{doc_id}/content`

**Implementation Steps**:

- [x] Verify document exists in database
- [x] Update content field
- [x] Invalidate embeddings (set has_embeddings to False)
- [x] Update updated_at timestamp
- [x] Transform DocumentData to DocumentResponse in router
- [x] Handle not found errors with 404 status
- [x] Handle other errors with 500 status

**Design Decision**: Uses delete-then-re-add pattern (LanceDB has no UPDATE). Preserves original `created_at` and all metadata from first chunk.

---

### Task #32: Implement document update title endpoint

**Status**: ⬜ Not Started
**Priority**: Medium
**Files**: `c7_mcp/services/document.py`, `c7_mcp/routers/documents.py`
**Endpoint**: `PATCH /api/v1/documents/{doc_id}/title`

**Implementation Steps**:

- [ ] Verify document exists in database
- [ ] Update title field
- [ ] Update updated_at timestamp
- [ ] Transform DocumentData to DocumentResponse in router
- [ ] Handle not found errors with 404 status
- [ ] Handle other errors with 500 status

---

### Task #33: Implement document move to library endpoint

**Status**: ⬜ Not Started
**Priority**: Medium
**Files**: `c7_mcp/services/document.py`, `c7_mcp/routers/documents.py`
**Endpoint**: `PATCH /api/v1/documents/{doc_id}/library`

**Implementation Steps**:

- [ ] Verify document exists in database
- [ ] Verify target library exists in database
- [ ] Update library_id field
- [ ] Update document counts for both old and new libraries
- [ ] Update updated_at timestamp
- [ ] Transform DocumentData to DocumentResponse in router
- [ ] Handle document not found errors with 404 status
- [ ] Handle library not found errors with 404 status
- [ ] Handle other errors with 500 status

---

### Task #34: Implement document update embeddings endpoint

**Status**: ⬜ Not Started
**Priority**: High
**Files**: `c7_mcp/services/document.py`, `c7_mcp/routers/documents.py`
**Endpoint**: `PATCH /api/v1/documents/{doc_id}/embeddings`

**Implementation Steps**:

- [ ] Verify document exists in database
- [ ] Validate embedding dimension consistency with existing embeddings
- [ ] Store embeddings and model info
- [ ] Set has_embeddings to True
- [ ] Update updated_at timestamp
- [ ] Transform DocumentData to DocumentResponse in router
- [ ] Handle not found errors with 404 status
- [ ] Handle dimension mismatch errors with 400 status
- [ ] Handle other errors with 500 status

---

### Task #35: Implement document delete endpoint

**Status**: ⬜ Not Started
**Priority**: Medium
**Files**: `c7_mcp/services/document.py`, `c7_mcp/routers/documents.py`
**Endpoint**: `DELETE /api/v1/documents/{doc_id}`

**Implementation Steps**:

- [ ] Verify document exists in database
- [ ] Delete document from database
- [ ] Delete associated embeddings
- [ ] Update library document count
- [ ] Clean up associated resources
- [ ] Return DeleteResponse with success=True in router
- [ ] Handle not found errors with 404 status
- [ ] Handle other errors with 500 status

---

## 🏗️ Infrastructure (3 tasks)

### Task #36: Add database layer and models

**Status**: ⬜ Not Started
**Priority**: Critical
**Files**: New directory `c7_mcp/db/`, `c7_mcp/models.py`

**Implementation Steps**:

- [ ] Choose database technology (SQLite, PostgreSQL, LanceDB, etc.)
- [ ] Create database models for Library, Document, Embeddings
- [ ] Set up database connection and session management
- [ ] Create migration system (Alembic or similar)
- [ ] Add database configuration to settings
- [ ] Create initial migration with schema
- [ ] Add database initialization to app startup

**Recommended Approach**:

- Use SQLAlchemy for ORM
- Use Alembic for migrations
- Use SQLite for development, PostgreSQL for production
- Consider LanceDB for vector embeddings storage

---

### Task #37: Add error handling and validation

**Status**: ⬜ Not Started
**Priority**: High
**Files**: `c7_mcp/exceptions.py`, `c7_mcp/api.py`

**Implementation Steps**:

- [ ] Create custom exception classes (LibraryNotFound, DocumentNotFound, etc.)
- [ ] Add global exception handlers in api.py
- [ ] Standardize error response format
- [ ] Add validation for all input fields
- [ ] Add rate limiting if needed
- [ ] Add request/response logging
- [ ] Add error tracking (Sentry or similar)

**Exception Classes to Create**:

- `LibraryNotFoundError`
- `LibraryNameConflictError`
- `DocumentNotFoundError`
- `EmbeddingsNotFoundError`
- `URLFetchError`
- `InvalidEmbeddingDimensionError`

---

### Task #38: Add testing infrastructure

**Status**: ⬜ Not Started
**Priority**: High
**Files**: New directory `tests/`

**Implementation Steps**:

- [ ] Set up pytest and test fixtures
- [ ] Create test database setup/teardown
- [ ] Add unit tests for service layer functions
- [ ] Add integration tests for all API endpoints
- [ ] Add tests for MCP JSON-RPC protocol
- [ ] Add tests for error cases (404, 400, 500)
- [ ] Add tests for pagination and filtering
- [ ] Set up test coverage reporting
- [ ] Add CI/CD integration

**Test Coverage Goals**:

- Service layer: 90%+ coverage
- Router layer: 85%+ coverage
- Overall: 80%+ coverage

---

## 📝 Notes

### Dependencies to Add

- Database ORM: `sqlalchemy`, `alembic`
- HTTP client for URL fetching: `httpx`
- Content parsing: `beautifulsoup4`, `pypdf`, `markdown`
- Vector embeddings: `lancedb` or similar
- Testing: `pytest`, `pytest-asyncio`, `pytest-cov`
- Logging: `structlog` or `loguru`

### Configuration Needed

- Database connection strings
- URL fetch timeouts and retry logic
- Embedding model configuration
- Rate limiting parameters
- CORS settings for API

### Future Enhancements

- Authentication and authorization
- WebSocket support for real-time updates
- Batch operations for bulk imports
- Search API with full-text search
- Export/import functionality
- API versioning strategy

---

## 🎉 Completion Checklist

When all tasks are complete:

- [ ] All 25 implementation tasks completed
- [ ] All tests passing with >80% coverage
- [ ] Documentation updated
- [ ] API examples added
- [ ] Performance benchmarking done
- [ ] Security review completed
- [ ] Deployment guide written
- [ ] Monitoring and logging configured

---

**Last Updated**: 2026-02-17
**Document Version**: 1.1

---

## ✅ Implementation Status Checklist

Numbers indicate recommended implementation order. MCP tools are the end goal;
everything before them unblocks the path to get there.

### Libraries (`/api/v1/libraries`)
- [x]     `GET    /`                  — list all libraries
- [x]     `POST   /`                  — create library
- [x] `1.` `GET    /{id}`              — get library by ID
- [ ] `9.` `PUT    /{id}`              — full update
- [ ] `10.` `PATCH  /{id}`             — partial update
- [x] `8.` `DELETE /{id}`              — delete library

### Documents (`/api/v1/documents`)
- [x]     `GET    /`                  — list documents (filter by library_id)
- [x]     `POST   /`                  — create document (upload content)
- [x] `6.` `POST   /fetch`             — create document (fetch from URL)
- [x] `2.` `GET    /{id}`              — get document metadata
- [x] `3.` `GET    /{id}/content`      — get raw content
- [ ] `11.` `GET   /{id}/pretty`       — get title + content
- [ ] `13.` `GET   /{id}/title`        — get title only
- [ ] `12.` `GET   /{id}/embeddings`   — get embedding vector
- [ ] `14.` `PUT   /{id}`              — full update
- [x] `7.` `PATCH  /{id}/content`      — update content
- [ ] `15.` `PATCH /{id}/title`        — update title
- [ ] `16.` `PATCH /{id}/library`      — move to different library
- [ ] `17.` `PATCH /{id}/embeddings`   — update embeddings
- [ ] `18.` `DELETE /{id}`             — delete document

### MCP Tools (`POST /mcp`)
- [x] `4.` `resolve-library-id` — resolve library name → Context7 ID
- [x] `5.` `query-docs` — query stored docs by library ID + query string




