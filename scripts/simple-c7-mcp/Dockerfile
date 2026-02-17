FROM python:3.12-slim AS build

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

# Install dependencies first (cached layer)
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-install-project

# Copy application code and install project
COPY README.md ./
COPY c7_mcp/ c7_mcp/
RUN uv sync --frozen --no-editable


FROM python:3.12-slim

# Create non-root user with fixed UID/GID for volume permission consistency
ARG UID=65532
ARG GID=65532
RUN groupadd -g $GID c7mcp && useradd -u $UID -g $GID -d /app -s /sbin/nologin c7mcp

WORKDIR /app

# Copy installed virtualenv and app from build stage
COPY --from=build --chmod=755 /app /app

# Data directory writable by app user, everything else read-only
RUN mkdir -p /app/lancedb_data && chown c7mcp:c7mcp /app/lancedb_data

USER 65532:65532

EXPOSE 8000

CMD ["/app/.venv/bin/c7-mcp", "serve", "--host", "0.0.0.0"]
