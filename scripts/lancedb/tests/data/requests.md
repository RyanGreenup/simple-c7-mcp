# Requests - Python HTTP Library

Requests is an elegant and simple HTTP library for Python, designed to make HTTP communication straightforward and human-friendly. It abstracts the complexities of making HTTP requests behind a beautiful, simple API, allowing developers to send HTTP/1.1 requests with various methods (GET, POST, PUT, DELETE, etc.) with minimal code. The library handles connection pooling, sessions with cookie persistence, SSL/TLS verification, content decompression, and automatic encoding detection seamlessly.

As one of the most downloaded Python packages with approximately 30 million downloads per week and over 1 million dependent repositories on GitHub, Requests has become the de facto standard for HTTP communication in Python. It supports features like Keep-Alive, international domain names, browser-style SSL verification, Basic and Digest authentication, multipart file uploads, streaming downloads, SOCKS proxy support, and connection timeouts. The library is designed to be compliant with HTTP specifications while maintaining an intuitive developer experience.

## GET Request

Send HTTP GET requests to retrieve data from URLs. The response object contains the status code, headers, and content.

```python
import requests

# Simple GET request
response = requests.get('https://api.github.com/events')

# Check response status
print(response.status_code)  # 200
print(response.ok)           # True

# Access response content
print(response.text)         # Response body as string
print(response.content)      # Response body as bytes
print(response.json())       # Parse JSON response

# Access headers (case-insensitive)
print(response.headers['Content-Type'])    # 'application/json; charset=utf-8'
print(response.headers.get('X-RateLimit-Remaining'))

# GET with URL parameters
params = {'key1': 'value1', 'key2': 'value2'}
response = requests.get('https://httpbin.org/get', params=params)
print(response.url)  # https://httpbin.org/get?key1=value1&key2=value2

# GET with custom headers
headers = {'User-Agent': 'my-app/1.0', 'Accept': 'application/json'}
response = requests.get('https://api.github.com/user', headers=headers)
```

## POST Request

Send HTTP POST requests to submit data to a server. Supports form-encoded data, JSON payloads, and multipart file uploads.

```python
import requests

# POST with form data (automatically form-encoded)
data = {'username': 'john', 'password': 'secret123'}
response = requests.post('https://httpbin.org/post', data=data)
print(response.json()['form'])  # {'username': 'john', 'password': 'secret123'}

# POST with JSON data (automatically serialized and Content-Type set)
payload = {'name': 'John Doe', 'email': 'john@example.com'}
response = requests.post('https://httpbin.org/post', json=payload)
print(response.json()['json'])  # {'name': 'John Doe', 'email': 'john@example.com'}

# POST with raw string data
response = requests.post('https://httpbin.org/post', data='raw string data')

# POST multiple values for same key
data = [('key', 'value1'), ('key', 'value2')]
response = requests.post('https://httpbin.org/post', data=data)
```

## PUT, PATCH, DELETE Requests

Perform resource updates and deletions using standard HTTP methods.

```python
import requests

# PUT request - replace entire resource
data = {'name': 'Updated Name', 'email': 'updated@example.com'}
response = requests.put('https://httpbin.org/put', json=data)
print(response.status_code)  # 200

# PATCH request - partial update
patch_data = {'email': 'newemail@example.com'}
response = requests.patch('https://httpbin.org/patch', json=patch_data)
print(response.json()['json'])  # {'email': 'newemail@example.com'}

# DELETE request
response = requests.delete('https://httpbin.org/delete')
print(response.status_code)  # 200

# HEAD request - get headers only
response = requests.head('https://httpbin.org/get')
print(response.headers)
print(response.text)  # Empty - HEAD doesn't return body

# OPTIONS request
response = requests.options('https://httpbin.org/get')
```

## File Upload

Upload files using multipart form data encoding. Supports single and multiple file uploads with custom filenames and content types.

```python
import requests

# Simple file upload
files = {'file': open('report.pdf', 'rb')}
response = requests.post('https://httpbin.org/post', files=files)

# Upload with custom filename and content type
files = {
    'file': ('custom_name.pdf', open('report.pdf', 'rb'), 'application/pdf')
}
response = requests.post('https://httpbin.org/post', files=files)

# Upload with additional headers per file
files = {
    'file': ('report.pdf', open('report.pdf', 'rb'), 'application/pdf', {'Expires': '0'})
}
response = requests.post('https://httpbin.org/post', files=files)

# Upload string as file
files = {'file': ('data.csv', 'col1,col2\nval1,val2\n', 'text/csv')}
response = requests.post('https://httpbin.org/post', files=files)

# Multiple file upload
files = [
    ('images', ('photo1.png', open('photo1.png', 'rb'), 'image/png')),
    ('images', ('photo2.png', open('photo2.png', 'rb'), 'image/png'))
]
response = requests.post('https://httpbin.org/post', files=files)

# Upload file with additional form data
files = {'file': open('document.pdf', 'rb')}
data = {'description': 'Important document', 'category': 'reports'}
response = requests.post('https://httpbin.org/post', files=files, data=data)
```

## Session Objects

Use sessions for persistent parameters, cookie handling, and connection pooling across multiple requests to the same host.

```python
import requests

# Create session - persists cookies and connection pooling
session = requests.Session()

# Set default parameters for all requests in session
session.auth = ('user', 'pass')
session.headers.update({'X-Custom-Header': 'value', 'User-Agent': 'MyApp/1.0'})

# Cookies persist automatically across requests
session.get('https://httpbin.org/cookies/set/sessioncookie/abc123')
response = session.get('https://httpbin.org/cookies')
print(response.json())  # {'cookies': {'sessioncookie': 'abc123'}}

# Session as context manager (auto-closes connections)
with requests.Session() as s:
    s.headers.update({'Authorization': 'Bearer token123'})
    response = s.get('https://api.github.com/user')
    response = s.get('https://api.github.com/user/repos')

# Session-level settings
session = requests.Session()
session.verify = '/path/to/ca-bundle.crt'  # SSL verification
session.cert = ('/path/to/client.cert', '/path/to/client.key')  # Client cert
session.proxies = {'http': 'http://proxy:8080', 'https': 'http://proxy:8080'}
session.max_redirects = 10
session.trust_env = False  # Disable environment variables

# Method-level params override session params
response = session.get('https://httpbin.org/get', headers={'X-Request-ID': '12345'})
```

## Authentication

Support for Basic, Digest, and custom authentication methods.

```python
import requests
from requests.auth import HTTPBasicAuth, HTTPDigestAuth

# Basic Authentication - tuple shorthand
response = requests.get(
    'https://httpbin.org/basic-auth/user/pass',
    auth=('user', 'pass')
)
print(response.status_code)  # 200

# Basic Authentication - explicit class
auth = HTTPBasicAuth('user', 'pass')
response = requests.get('https://httpbin.org/basic-auth/user/pass', auth=auth)

# Digest Authentication
auth = HTTPDigestAuth('user', 'pass')
response = requests.get('https://httpbin.org/digest-auth/auth/user/pass', auth=auth)

# Custom Authentication Handler
class TokenAuth(requests.auth.AuthBase):
    """Custom authentication using Bearer token."""
    def __init__(self, token):
        self.token = token

    def __call__(self, request):
        request.headers['Authorization'] = f'Bearer {self.token}'
        return request

# Use custom auth
response = requests.get('https://api.example.com/data', auth=TokenAuth('mytoken123'))

# Session with persistent auth
session = requests.Session()
session.auth = ('user', 'pass')
response = session.get('https://httpbin.org/basic-auth/user/pass')
```

## Timeouts

Configure connection and read timeouts to prevent hanging requests.

```python
import requests
from requests.exceptions import Timeout, ConnectTimeout, ReadTimeout

# Single timeout value (applies to both connect and read)
try:
    response = requests.get('https://httpbin.org/delay/5', timeout=3)
except Timeout:
    print('Request timed out')

# Separate connect and read timeouts (connect=3.05s, read=27s)
response = requests.get('https://httpbin.org/get', timeout=(3.05, 27))

# No timeout (wait forever) - not recommended for production
response = requests.get('https://httpbin.org/get', timeout=None)

# Handle specific timeout types
try:
    response = requests.get('https://httpbin.org/delay/10', timeout=2)
except ConnectTimeout:
    print('Connection timed out')
except ReadTimeout:
    print('Read timed out')
except Timeout:
    print('Request timed out (connect or read)')

# Session with default timeout
session = requests.Session()
# Note: timeout must be set per-request, not on session
response = session.get('https://httpbin.org/get', timeout=5)
```

## Error Handling

Handle HTTP errors and exceptions properly.

```python
import requests
from requests.exceptions import (
    RequestException, HTTPError, ConnectionError,
    Timeout, TooManyRedirects, JSONDecodeError
)

# Check status and raise exception for 4xx/5xx responses
response = requests.get('https://httpbin.org/status/404')
print(response.status_code)  # 404
print(response.ok)           # False

try:
    response.raise_for_status()
except HTTPError as e:
    print(f'HTTP Error: {e}')  # 404 Client Error: NOT FOUND

# Comprehensive error handling
def safe_request(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.json()
    except ConnectionError:
        print('Failed to connect to server')
    except Timeout:
        print('Request timed out')
    except TooManyRedirects:
        print('Too many redirects')
    except HTTPError as e:
        print(f'HTTP error occurred: {e}')
    except JSONDecodeError:
        print('Response is not valid JSON')
    except RequestException as e:
        print(f'Request failed: {e}')
    return None

# Status code checking
response = requests.get('https://httpbin.org/get')
if response.status_code == requests.codes.ok:
    print('Success!')
elif response.status_code == requests.codes.not_found:
    print('Not found')
```

## Streaming Responses

Handle large responses efficiently by streaming content in chunks.

```python
import requests

# Enable streaming (don't download entire response at once)
response = requests.get('https://httpbin.org/stream/100', stream=True)

# Iterate over content in chunks
with requests.get('https://example.com/large-file.zip', stream=True) as r:
    r.raise_for_status()
    with open('large-file.zip', 'wb') as f:
        for chunk in r.iter_content(chunk_size=8192):
            f.write(chunk)

# Stream lines (useful for streaming APIs)
response = requests.get('https://httpbin.org/stream/20', stream=True)
for line in response.iter_lines():
    if line:
        print(line.decode('utf-8'))

# Conditional download based on content length
response = requests.get('https://example.com/file.zip', stream=True)
if int(response.headers.get('content-length', 0)) < 1000000:  # Less than 1MB
    content = response.content
else:
    # Stream large files
    pass

# Access raw socket response
response = requests.get('https://httpbin.org/stream/5', stream=True)
print(response.raw.read(100))  # Read raw bytes
```

## Proxies and SSL

Configure proxy servers and SSL/TLS certificate verification.

```python
import requests

# HTTP and HTTPS proxies
proxies = {
    'http': 'http://10.10.1.10:3128',
    'https': 'http://10.10.1.10:1080'
}
response = requests.get('https://httpbin.org/ip', proxies=proxies)

# Proxy with authentication
proxies = {
    'http': 'http://user:password@10.10.1.10:3128',
    'https': 'http://user:password@10.10.1.10:1080'
}
response = requests.get('https://httpbin.org/ip', proxies=proxies)

# SOCKS proxy (requires requests[socks])
proxies = {
    'http': 'socks5://user:pass@host:port',
    'https': 'socks5://user:pass@host:port'
}
response = requests.get('https://httpbin.org/ip', proxies=proxies)

# SSL certificate verification (enabled by default)
response = requests.get('https://github.com', verify=True)

# Custom CA bundle
response = requests.get('https://internal.example.com', verify='/path/to/ca-bundle.crt')

# Disable SSL verification (not recommended for production)
response = requests.get('https://self-signed.example.com', verify=False)

# Client-side certificate (mTLS)
response = requests.get(
    'https://client-auth.example.com',
    cert=('/path/to/client.cert', '/path/to/client.key')
)

# Session with SSL settings
session = requests.Session()
session.verify = '/path/to/ca-bundle.crt'
session.cert = '/path/to/client.pem'
```

## Cookies

Work with cookies using dict-like interface or RequestsCookieJar for advanced control.

```python
import requests

# Access cookies from response
response = requests.get('https://httpbin.org/cookies/set/mycookie/myvalue')
print(response.cookies['mycookie'])  # 'myvalue'

# Send cookies with request
cookies = {'session_id': 'abc123', 'user': 'john'}
response = requests.get('https://httpbin.org/cookies', cookies=cookies)
print(response.json())  # {'cookies': {'session_id': 'abc123', 'user': 'john'}}

# Use RequestsCookieJar for domain/path control
jar = requests.cookies.RequestsCookieJar()
jar.set('session', 'value1', domain='httpbin.org', path='/cookies')
jar.set('other', 'value2', domain='httpbin.org', path='/other')

response = requests.get('https://httpbin.org/cookies', cookies=jar)
print(response.json())  # Only 'session' cookie sent (path matches)

# Session cookies persist automatically
session = requests.Session()
session.get('https://httpbin.org/cookies/set/session_token/xyz789')
response = session.get('https://httpbin.org/cookies')
print(response.json()['cookies']['session_token'])  # 'xyz789'

# Clear session cookies
session.cookies.clear()
```

## Prepared Requests

Build and modify requests before sending for advanced use cases.

```python
import requests
from requests import Request, Session

# Create and prepare a request
session = Session()

request = Request('POST', 'https://httpbin.org/post',
    data={'key': 'value'},
    headers={'X-Custom': 'header'}
)
prepared = session.prepare_request(request)

# Modify prepared request
prepared.body = 'Modified body content'
prepared.headers['X-Extra'] = 'extra-value'

# Send prepared request
response = session.send(prepared, timeout=5, verify=True)
print(response.status_code)

# Inspect what will be sent
print(prepared.method)   # 'POST'
print(prepared.url)      # 'https://httpbin.org/post'
print(prepared.headers)  # Headers dict
print(prepared.body)     # Request body

# Merge environment settings
settings = session.merge_environment_settings(
    prepared.url,
    proxies={},
    stream=None,
    verify=None,
    cert=None
)
response = session.send(prepared, **settings)
```

## Event Hooks

Attach callbacks to requests for logging, modification, or monitoring.

```python
import requests

# Define hook function
def log_response(response, *args, **kwargs):
    print(f'URL: {response.url}')
    print(f'Status: {response.status_code}')
    print(f'Elapsed: {response.elapsed.total_seconds()}s')

# Single hook
response = requests.get(
    'https://httpbin.org/get',
    hooks={'response': log_response}
)

# Multiple hooks
def add_timestamp(response, *args, **kwargs):
    response.timestamp = response.elapsed.total_seconds()
    return response

def check_status(response, *args, **kwargs):
    if response.status_code >= 400:
        print(f'Error: {response.status_code}')

response = requests.get(
    'https://httpbin.org/get',
    hooks={'response': [log_response, add_timestamp, check_status]}
)
print(response.timestamp)

# Session-level hooks
session = requests.Session()
session.hooks['response'].append(log_response)

# All requests through this session will trigger the hook
response = session.get('https://httpbin.org/get')
response = session.get('https://httpbin.org/headers')
```

## HTTPAdapter and Retries

Configure connection pooling, retries, and custom transport behavior.

```python
import requests
from requests.adapters import HTTPAdapter
from urllib3.util import Retry

# Configure automatic retries
session = requests.Session()

retry_strategy = Retry(
    total=3,                    # Total retry attempts
    backoff_factor=0.5,         # Wait 0.5, 1, 2 seconds between retries
    status_forcelist=[500, 502, 503, 504],  # Retry on these status codes
    allowed_methods=['GET', 'POST'],  # Methods to retry
)

adapter = HTTPAdapter(max_retries=retry_strategy)
session.mount('http://', adapter)
session.mount('https://', adapter)

response = session.get('https://httpbin.org/status/503')  # Will retry

# Configure connection pool size
adapter = HTTPAdapter(
    pool_connections=10,  # Number of connection pools to cache
    pool_maxsize=20,      # Max connections per pool
    max_retries=3,
    pool_block=False      # Don't block when pool is full
)
session.mount('https://', adapter)

# Custom adapter for specific hosts
session = requests.Session()
session.mount('https://api.example.com/', HTTPAdapter(max_retries=5))
session.mount('https://slow-api.example.com/', HTTPAdapter(pool_maxsize=5))
```

## Response Object Properties

Access all information from HTTP responses including content, headers, status, and metadata.

```python
import requests

response = requests.get('https://httpbin.org/get')

# Status information
print(response.status_code)    # 200
print(response.reason)         # 'OK'
print(response.ok)             # True (status < 400)
print(response.is_redirect)    # False

# Content in different formats
print(response.text)           # Decoded text content
print(response.content)        # Raw bytes
print(response.json())         # Parsed JSON (if applicable)

# Encoding
print(response.encoding)       # 'utf-8' (detected or from headers)
print(response.apparent_encoding)  # Detected from content

# Headers (case-insensitive dict)
print(response.headers)
print(response.headers['Content-Type'])
print(response.headers.get('X-Custom', 'default'))

# URL and redirect history
print(response.url)            # Final URL after redirects
print(response.history)        # List of redirect responses

# Request that generated this response
print(response.request.method)
print(response.request.url)
print(response.request.headers)

# Timing
print(response.elapsed)        # timedelta of request duration
print(response.elapsed.total_seconds())

# Links from Link header
print(response.links)          # Parsed link headers

# Cookies
print(response.cookies)        # CookieJar from response
```

## Summary

Requests is the go-to HTTP library for Python developers who need to interact with web services, APIs, and web applications. Its primary use cases include consuming RESTful APIs, web scraping, automated testing, microservice communication, and any application requiring HTTP communication. The library excels at simplifying common patterns like authentication, session management, file uploads, and handling various response formats while providing enough flexibility for advanced scenarios through prepared requests, custom adapters, and hooks.

Integration with Requests follows a straightforward pattern: create a session for persistent configuration and connection reuse, set up authentication and default headers, then make requests using the appropriate HTTP method. For production applications, always configure timeouts, implement proper error handling with try/except blocks around requests, and use raise_for_status() to catch HTTP errors. The library integrates seamlessly with the broader Python ecosystem and serves as the foundation for higher-level libraries like requests-oauthlib for OAuth and requests-toolbelt for advanced multipart encoding.
