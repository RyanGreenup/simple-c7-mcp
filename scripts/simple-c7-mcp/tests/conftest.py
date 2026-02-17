"""Shared pytest fixtures for API integration tests."""

import os

import httpx
import pytest

DEFAULT_BASE_URL = "http://localhost:8000"


def pytest_addoption(parser: pytest.Parser) -> None:
    """Register custom CLI options for integration tests."""
    parser.addoption(
        "--base-url",
        action="store",
        default=None,
        help=f"Base URL for API integration tests (default: {DEFAULT_BASE_URL})",
    )


@pytest.fixture(scope="session")
def base_url(pytestconfig: pytest.Config) -> str:
    """Resolve base URL from CLI option, env var, or fallback default."""
    return (
        pytestconfig.getoption("--base-url")
        or os.getenv("C7_MCP_BASE_URL")
        or DEFAULT_BASE_URL
    )


@pytest.fixture(scope="session")
def client(base_url: str) -> httpx.Client:
    """Return an HTTP client to the live API server."""
    try:
        health = httpx.get(f"{base_url}/health", timeout=5.0)
        if health.status_code >= 500:
            pytest.skip(f"API health check failed: {base_url} returned {health.status_code}")
    except httpx.HTTPError as exc:
        pytest.skip(f"API server not reachable at {base_url}: {exc}")

    with httpx.Client(base_url=base_url, timeout=15.0) as session:
        yield session
