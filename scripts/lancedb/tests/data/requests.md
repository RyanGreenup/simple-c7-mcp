# requests-cache

## Introduction

requests-cache is a persistent HTTP cache that provides an easy way to get better performance with the Python requests library. It acts as a transparent caching layer for HTTP requests, storing responses in various backend storage systems and retrieving them instantly when the same request is made again. This eliminates redundant network calls and dramatically improves response times, especially useful for applications that repeatedly access the same APIs or web resources.

The library supports multiple storage backends including SQLite, Redis, MongoDB, GridFS, DynamoDB, filesystem, and in-memory storage. It offers flexible expiration strategies through manual configuration, Cache-Control headers, and URL pattern matching. requests-cache can be integrated either as a drop-in replacement for requests.Session or installed globally to transparently cache all requests functions throughout an application.

## API Documentation and Code Examples

### CachedSession - Basic Usage

Drop-in replacement for requests.Session that adds caching capabilities with SQLite backend by default.

```python
import requests_cache

# Create a cached session with SQLite backend
session = requests_cache.CachedSession('demo_cache')

# First request hits the network and caches response
response = session.get('https://httpbin.org/get')
print(response.from_cache)  # False

# Second request returns cached response instantly
response = session.get('https://httpbin.org/get')
print(response.from_cache)  # True

# All standard requests methods work
response = session.post('https://httpbin.org/post', json={'key': 'value'})
response = session.put('https://httpbin.org/put', data='test')
response = session.delete('https://httpbin.org/delete')
```

### install_cache - Global Patching

Install caching globally to make all requests functions automatically cached without modifying code.

```python
import requests
import requests_cache

# Install cache globally
requests_cache.install_cache('global_cache')

# Now all requests functions use caching automatically
response = requests.get('https://httpbin.org/get')
print(response.from_cache)  # False on first call

response = requests.get('https://httpbin.org/get')
print(response.from_cache)  # True on subsequent calls

# Disable caching globally
requests_cache.uninstall_cache()
```

### Expiration - Time-Based Cache Control

Configure cache expiration using various time formats to keep responses fresh.

```python
from datetime import timedelta
from requests_cache import CachedSession

# Set expiration in seconds
session = CachedSession('cache', expire_after=360)
response = session.get('https://httpbin.org/get')
print(f'Expires: {response.expires}')

# Set expiration using timedelta
session = CachedSession('cache', expire_after=timedelta(hours=1))
response = session.get('https://httpbin.org/get')

# Per-request expiration override
response = session.get('https://httpbin.org/delay/1', expire_after=60)

# Check if response is expired
import time
time.sleep(61)
print(response.is_expired)  # True

# Never expire (default)
session = CachedSession('cache', expire_after=-1)
```

### Cache-Control Headers

Automatically use HTTP Cache-Control and other standard headers for expiration.

```python
from requests_cache import CachedSession

# Enable automatic Cache-Control support
session = CachedSession('cache', cache_control=True)

# Server's Cache-Control headers will determine expiration
response = session.get('https://httpbin.org/cache/3600')
print(f'Cached until: {response.expires}')

# Combine with default expiration as fallback
session = CachedSession(
    'cache',
    cache_control=True,
    expire_after=timedelta(days=1)  # Used when server doesn't send Cache-Control
)
```

### URL Pattern Expiration

Define different expiration times for different URL patterns using glob or regex patterns.

```python
from datetime import timedelta
from requests_cache import CachedSession, DO_NOT_CACHE, NEVER_EXPIRE

# Configure per-URL expiration patterns
urls_expire_after = {
    'httpbin.org/image': timedelta(days=7),  # Images expire in 7 days
    '*.fillmurray.com': NEVER_EXPIRE,        # Never expire
    '*.placeholder.com/*': DO_NOT_CACHE,     # Never cache
}

session = CachedSession(
    'cache',
    expire_after=3600,  # Default: 1 hour
    urls_expire_after=urls_expire_after
)

# Each URL will use its matching pattern's expiration
response1 = session.get('https://httpbin.org/get')         # Expires in 1 hour
response2 = session.get('https://httpbin.org/image/jpeg')  # Expires in 7 days
response3 = session.get('https://www.fillmurray.com/460/300')  # Never expires

print(f'Response 1 expires: {response1.expires}')
print(f'Response 2 expires: {response2.expires}')
print(f'Response 3 expires: {response3.expires}')  # None (never)
```

### Backend Selection

Choose from multiple storage backends with different characteristics and configurations.

```python
from requests_cache import CachedSession
from requests_cache.backends import RedisCache, MongoCache, FileCache

# SQLite backend (default)
session = CachedSession('cache.db', backend='sqlite')

# Redis backend
session = CachedSession('my_cache', backend='redis')

# Redis with custom connection
backend = RedisCache(host='192.168.1.63', port=6379, password='secret')
session = CachedSession(backend=backend)

# MongoDB backend
session = CachedSession('my_db', backend='mongodb')

# Filesystem backend with JSON serialization
session = CachedSession('~/cache_dir', backend='filesystem')

# In-memory backend (no persistence)
session = CachedSession('memory_cache', backend='memory')

# DynamoDB backend
session = CachedSession('my_table', backend='dynamodb')
```

### Advanced Session Configuration

Configure caching behavior with fine-grained control over what gets cached and how requests are matched.

```python
from datetime import timedelta
from requests_cache import CachedSession

session = CachedSession(
    'advanced_cache',
    use_cache_dir=True,                # Save in platform-specific cache directory
    cache_control=True,                # Use Cache-Control headers
    expire_after=timedelta(days=1),    # Default expiration
    allowable_codes=[200, 400],        # Cache these status codes
    allowable_methods=['GET', 'POST'], # Cache these HTTP methods
    ignored_parameters=['api_key', 'token'],  # Exclude from cache key and redact
    match_headers=['Accept-Language'], # Include these headers in cache matching
    stale_if_error=True,               # Return stale cache on errors
    always_revalidate=False,           # Revalidate every request
)

# Make requests with configured behavior
response = session.get(
    'https://api.example.com/data',
    params={'api_key': 'secret123', 'query': 'test'}
)

# api_key is redacted from cached request
print(response.request.url)  # api_key won't appear
```

### Cache Management

Inspect, filter, and manage cached responses programmatically.

```python
from requests_cache import CachedSession

session = CachedSession('cache')

# Populate cache
session.get('https://httpbin.org/get')
session.get('https://httpbin.org/delay/1')

# Get cache information
print(f'Total responses: {len(session.cache.responses)}')
print(f'Cached URLs: {list(session.cache.urls())}')

# Check if URL is cached
print(session.cache.has_url('https://httpbin.org/get'))  # True

# Get cached response by key
cache_key = session.cache.create_key(session.get('https://httpbin.org/get').request)
cached_response = session.cache.get_response(cache_key)

# Delete specific responses
session.cache.delete(urls=['https://httpbin.org/get'])

# Delete expired responses
session.cache.delete(expired=True)

# Clear entire cache
session.cache.clear()
```

### Temporary Cache Control

Temporarily disable or enable caching within specific code blocks.

```python
import requests
import requests_cache

# Using context manager with CachedSession
session = requests_cache.CachedSession('cache')

# Normal cached request
response = session.get('https://httpbin.org/get')
print(response.from_cache)  # May be True

# Temporarily disable cache
with session.cache_disabled():
    response = session.get('https://httpbin.org/ip')
    print(response.from_cache)  # Always False

# Using global patching with context managers
with requests_cache.enabled('temp_cache'):
    response = requests.get('https://httpbin.org/get')
    print(response.from_cache)  # Cached within context

# Temporarily disable global cache
requests_cache.install_cache('cache')
with requests_cache.disabled():
    response = requests.get('https://httpbin.org/get')
    print(response.from_cache)  # Always False
```

### Request Refresh Options

Control when cached responses are revalidated or refreshed.

```python
from requests_cache import CachedSession

session = CachedSession('cache', expire_after=3600)

# Normal cached request
response = session.get('https://httpbin.org/get')

# Soft refresh: revalidate with server using conditional request
response = session.get('https://httpbin.org/get', refresh=True)
print(response.revalidated)  # True if server returned 304 Not Modified

# Hard refresh: force new request and overwrite cache
response = session.get('https://httpbin.org/get', force_refresh=True)
print(response.from_cache)  # False

# Only return if cached, otherwise return 504
response = session.get('https://httpbin.org/get', only_if_cached=True)
if response.status_code == 504:
    print('Not cached')
```

### Stale Response Handling

Configure behavior when cached responses are stale or requests fail.

```python
from requests_cache import CachedSession

# Return stale cache on error
session = CachedSession('cache', stale_if_error=True)

response = session.get('https://httpbin.org/get', expire_after=1)
import time
time.sleep(2)

# If the server is down or returns an error, stale cache is returned
try:
    response = session.get('https://httpbin.org/get')
    print(f'Used stale cache: {response.from_cache}')
except Exception:
    pass

# Limit staleness with time value in seconds
session = CachedSession('cache', stale_if_error=3600)  # Max 1 hour stale
```

### Custom Request Matching

Implement custom cache key generation for specialized matching requirements.

```python
from requests_cache import CachedSession
from requests import PreparedRequest

def custom_key_fn(request: PreparedRequest, **kwargs) -> str:
    """Generate cache key based only on URL path, ignoring query params"""
    from urllib.parse import urlparse
    parsed = urlparse(request.url)
    # Use only scheme, host, and path for matching
    key = f"{request.method}:{parsed.scheme}://{parsed.netloc}{parsed.path}"
    return key

session = CachedSession('cache', key_fn=custom_key_fn)

# Both requests will match the same cache key
response1 = session.get('https://httpbin.org/get?param1=a')
response2 = session.get('https://httpbin.org/get?param2=b')
print(response2.from_cache)  # True (matched despite different params)
```

### Custom Response Filtering

Filter which responses get cached using custom logic.

```python
from requests_cache import CachedSession
from requests import Response

def filter_fn(response: Response) -> bool:
    """Only cache responses with JSON content type"""
    content_type = response.headers.get('Content-Type', '')
    return 'application/json' in content_type

session = CachedSession('cache', filter_fn=filter_fn)

# JSON response will be cached
response1 = session.get('https://httpbin.org/json')
print(response1.from_cache)  # May be True

# HTML response won't be cached
response2 = session.get('https://httpbin.org/html')
print(response2.from_cache)  # Always False
```

### Cache Export and Migration

Export cached data to different backends or formats for backup or migration.

```python
from requests_cache import CachedSession

# Populate source cache with Redis
src_session = CachedSession('my_cache', backend='redis')
src_session.get('https://httpbin.org/get')
src_session.get('https://httpbin.org/json')

# Export to filesystem with JSON serialization
dest_session = CachedSession(
    '~/cache_backup',
    backend='filesystem',
    serializer='json'
)
dest_session.cache.update(src_session.cache)

# List exported files
print(f'Exported {len(dest_session.cache.responses)} responses')
for path in dest_session.cache.paths():
    print(path)

# Can also export using backend classes directly
from requests_cache.backends import RedisCache, FileCache

src_cache = RedisCache()
dest_cache = FileCache('~/backup', serializer='json')
dest_cache.update(src_cache)
```

### Serialization Options

Choose different serialization formats for cached data.

```python
from requests_cache import CachedSession

# Default: Pickle serializer (fastest, most compatible)
session = CachedSession('cache', backend='sqlite')

# JSON serializer (human-readable, slower)
session = CachedSession('cache', backend='sqlite', serializer='json')

# YAML serializer (human-readable, requires pyyaml)
session = CachedSession('cache', backend='sqlite', serializer='yaml')

# BSON serializer (for MongoDB)
session = CachedSession('cache', backend='mongodb', serializer='bson')

# Filesystem backend automatically serializes to files
session = CachedSession('~/cache', backend='filesystem', serializer='json')
response = session.get('https://httpbin.org/get')
# Response saved as JSON file in ~/cache/
```

### SQLite Backend Configuration

Configure SQLite-specific options for performance and reliability.

```python
from requests_cache import CachedSession

# Basic SQLite configuration
session = CachedSession('cache.db', backend='sqlite')

# Use platform-specific cache directory
session = CachedSession('my_cache', backend='sqlite', use_cache_dir=True)
# Saves to ~/.cache/my_cache.sqlite on Linux

# Use temporary directory
session = CachedSession('temp_cache', backend='sqlite', use_temp=True)

# In-memory database (no persistence)
session = CachedSession('cache', backend='sqlite', use_memory=True)

# Performance options
session = CachedSession(
    'cache.db',
    backend='sqlite',
    fast_save=True,      # Faster writes, risk of data loss on crash
    wal=True,            # Write-Ahead Logging: readers don't block writers
    busy_timeout=5000,   # Wait 5s if database is locked
)

# Vacuum database to reclaim space after deletions
session.cache.delete(expired=True, vacuum=True)
```

### Response Inspection

Inspect cached response metadata and properties.

```python
from requests_cache import CachedSession

session = CachedSession('cache', expire_after=3600)
response = session.get('https://httpbin.org/get')

# Check if response came from cache
print(f'From cache: {response.from_cache}')

# Check expiration
print(f'Expires at: {response.expires}')
print(f'Is expired: {response.is_expired}')

# Check if response was revalidated
print(f'Revalidated: {response.revalidated}')

# Get cache key for this response
cache_key = session.cache.create_key(response.request)
print(f'Cache key: {cache_key}')

# Access original request that was cached
print(f'Cached URL: {response.request.url}')
print(f'Cached method: {response.request.method}')
print(f'Cached headers: {response.request.headers}')
```

### Filtering Cached Responses

Query and filter cached responses based on various criteria.

```python
from requests_cache import CachedSession
from datetime import datetime, timedelta

session = CachedSession('cache')

# Populate cache with various responses
session.get('https://httpbin.org/get', expire_after=60)
session.get('https://httpbin.org/json', expire_after=3600)
session.get('https://httpbin.org/html')  # Never expires

# Get all cached responses
all_responses = list(session.cache.filter())
print(f'Total cached: {len(all_responses)}')

# Get only expired responses
expired = list(session.cache.filter(expired=True, valid=False))
print(f'Expired: {len(expired)}')

# Get only valid (non-expired) responses
valid = list(session.cache.filter(valid=True, expired=False))
print(f'Valid: {len(valid)}')

# SQLite backend: get sorted responses
session = CachedSession('cache', backend='sqlite')
# Sort by expiration time
for response in session.cache.sorted(key='expires', limit=10):
    print(f'{response.url}: {response.expires}')

# Sort by size
for response in session.cache.sorted(key='size', reversed=True, limit=5):
    print(f'{response.url}: {len(response.content)} bytes')
```

## Summary

requests-cache is designed for applications that need to optimize HTTP request performance through intelligent caching. Common use cases include web scraping applications that repeatedly access the same URLs, API clients that make redundant requests, development and testing environments where deterministic responses are needed, and any application with rate-limited APIs where minimizing requests is critical. The library excels at reducing latency from seconds to sub-milliseconds for cached responses while maintaining compatibility with the standard requests API.

Integration patterns vary from simple drop-in session replacement for basic caching needs, to global patching for transparent caching across an entire application, to advanced configurations with custom backends, serializers, and matching logic for specialized requirements. The library supports both development workflows (using in-memory or SQLite caches) and production deployments (using Redis, MongoDB, or DynamoDB for distributed caching). With features like conditional requests, stale-while-revalidate, per-URL expiration patterns, and response filtering, requests-cache provides a comprehensive solution for HTTP caching in Python applications.
