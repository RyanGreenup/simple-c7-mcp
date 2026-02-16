### GET /heroes/

Source: https://fastapi.tiangolo.com/ja/tutorial/sql-databases

Retrieves a list of all heroes, with optional pagination parameters to control the number of results.

```APIDOC
## GET /heroes/

### Description
Retrieves a list of all heroes.

### Method
GET

### Endpoint
/heroes/

### Parameters
#### Path Parameters
(None)

#### Query Parameters
- **offset** (integer) - Optional - Default: 0 - The number of items to skip before returning results.
- **limit** (integer) - Optional - Default: 100 - The maximum number of items to return (max 100).

#### Request Body
(None)

### Request Example
(None)

### Response
#### Success Response (200)
- **id** (integer) - The unique identifier of the hero.
- **name** (string) - The name of the hero.
- **age** (integer | null) - The age of the hero.

#### Response Example
[
  {
    "id": 1,
    "name": "Deadpond",
    "age": 28
  },
  {
    "id": 2,
    "name": "Spider-Boy",
    "age": 16
  }
]
```

--------------------------------

### GET /

Source: https://fastapi.tiangolo.com/index

Retrieves a simple 'Hello World' message from the root endpoint. This is a basic example of a GET request without any parameters.

```APIDOC
## GET /

### Description
Retrieves a simple 'Hello World' message from the root endpoint.

### Method
GET

### Endpoint
/

### Parameters
#### Path Parameters
(None)

#### Query Parameters
(None)

#### Request Body
(None)

### Request Example
(None)

### Response
#### Success Response (200)
- **Hello** (string) - A greeting message.

#### Response Example
{
  "Hello": "World"
}
```

--------------------------------

### Example Content for a Python requirements.txt File

Source: https://fastapi.tiangolo.com/fr/virtual-environments

This snippet presents an example of a `requirements.txt` file, detailing how to specify exact versions of Python packages like FastAPI and Pydantic. This file is then used by package managers to install the defined dependencies.

```text
fastapi[standard]==0.113.0
pydantic==2.8.0
```

--------------------------------

### GET /heroes/

Source: https://fastapi.tiangolo.com/ja/tutorial/sql-databases

Retrieves a paginated list of all heroes from the database. Supports offset and limit parameters for pagination control.

```APIDOC
## GET /heroes/

### Description
Retrieves a paginated list of all heroes from the database. Supports offset and limit query parameters for pagination.

### Method
GET

### Endpoint
/heroes/

### Query Parameters
- **offset** (int) - Optional - Number of records to skip, default is 0
- **limit** (int) - Optional - Maximum number of records to return, default is 100, maximum allowed is 100

### Request Example
GET /heroes/?offset=0&limit=10

### Response
#### Success Response (200)
Returns an array of hero objects:
- **id** (int) - Hero's primary key identifier
- **name** (str) - Hero's name
- **age** (int | None) - Hero's age
- **secret_name** (str) - Hero's secret identity name

#### Response Example
[
  {
    "id": 1,
    "name": "Deadpond",
    "age": 30,
    "secret_name": "Dive Wilson"
  },
  {
    "id": 2,
    "name": "Spider-Boy",
    "age": 25,
    "secret_name": "Peter Parker"
  }
]
```

--------------------------------

### FastAPI Startup Event with Annotated Dependencies

Source: https://fastapi.tiangolo.com/ja/tutorial/sql-databases

Registers a startup event handler that creates database tables when the application starts. Uses Annotated type hints for cleaner dependency injection syntax. Ensures database schema is initialized before the first request arrives.

```python
SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI()

@app.on_event("startup")
def on_startup():
    create_db_and_tables()
```

--------------------------------

### GET /

Source: https://fastapi.tiangolo.com/fr/tutorial/cors_q=

A simple example endpoint demonstrating a basic GET request within a FastAPI application configured with CORSMiddleware. It returns a 'Hello World' message.

```APIDOC
## GET /

### Description
This endpoint serves as a basic example within a FastAPI application configured with CORSMiddleware. It responds to GET requests by returning a simple JSON object containing a greeting message.

### Method
GET

### Endpoint
/

### Parameters
#### Path Parameters
(None)

#### Query Parameters
(None)

#### Request Body
(None)

### Request Example
(No request body required)

### Response
#### Success Response (200)
- **message** (string) - A greeting message.

#### Response Example
{
  "message": "Hello World"
}
```

--------------------------------

### Install FastAPI with Standard Dependencies using pip or uv

Source: https://fastapi.tiangolo.com/fr/virtual-environments

This snippet demonstrates how to directly install FastAPI along with its standard dependencies into your Python environment. It provides commands for both `pip` and `uv` package managers, suitable for quick setups or when not using a `requirements.txt` file.

```bash
pip install "fastapi[standard]"
```

```bash
uv pip install "fastapi[standard]"
```

--------------------------------

### POST /heroes/

Source: https://fastapi.tiangolo.com/ja/tutorial/sql-databases

Creates a new hero in the database with the provided details. Returns the public representation of the created hero.

```APIDOC
## POST /heroes/

### Description
Creates a new hero in the database with the provided details.

### Method
POST

### Endpoint
/heroes/

### Parameters
#### Path Parameters
(None)

#### Query Parameters
(None)

#### Request Body
- **name** (string) - Required - The hero's name.
- **age** (integer) - Optional - The hero's age.
- **secret_name** (string) - Required - The hero's secret identity.

### Request Example
{
  "name": "Deadpond",
  "secret_name": "Dive Wilson",
  "age": 28
}

### Response
#### Success Response (200)
- **id** (integer) - The unique identifier of the hero.
- **name** (string) - The hero's name.
- **age** (integer) - The hero's age.

#### Response Example
{
  "id": 1,
  "name": "Deadpond",
  "age": 28
}
```

--------------------------------

### GET /heroes/

Source: https://fastapi.tiangolo.com/ja/tutorial/sql-databases_q=

Retrieves a list of heroes from the database. Supports pagination through offset and limit parameters.

```APIDOC
## GET /heroes/

### Description
Retrieves a list of all heroes, with optional pagination to control the number of results.

### Method
GET

### Endpoint
/heroes/

### Parameters
#### Path Parameters
(None)

#### Query Parameters
- **offset** (integer) - Optional - Default 0. The number of items to skip before starting to collect the result set.
- **limit** (integer) - Optional - Default 100, Max 100. The maximum number of items to return.

#### Request Body
(None)

### Request Example
(None)

### Response
#### Success Response (200)
- (array of Hero objects) - A list of hero objects.
  - **id** (integer) - The unique identifier of the hero.
  - **name** (string) - The name of the hero.
  - **age** (integer, optional) - The age of the hero.
  - **secret_name** (string) - The secret identity of the hero.

#### Response Example
```json
[
  {
    "name": "Deadpond",
    "age": 28,
    "secret_name": "Dive Wilson",
    "id": 1
  },
  {
    "name": "Spider-Boy",
    "age": null,
    "secret_name": "Pedro Parqueador",
    "id": 2
  }
]
```
```

--------------------------------

### Install Uvicorn ASGI Server with Standard Dependencies

Source: https://fastapi.tiangolo.com/deployment/manually_q=

This command installs the Uvicorn ASGI server, including its recommended standard dependencies like `uvloop` for high-performance asynchronous operations. This setup is beneficial for production environments and is often included when installing FastAPI with the `[standard]` extra.

```bash
pip install "uvicorn[standard]"
```

--------------------------------

### Install and Run FastAPI CLI Development Mode

Source: https://fastapi.tiangolo.com/pt/release-notes

Install the latest FastAPI version and start a development server using the new FastAPI CLI command. The CLI provides automatic reloading and displays API documentation endpoints. This requires FastAPI 0.111.0 or later.

```bash
$ pip install --upgrade fastapi

$ fastapi dev main.py
```

--------------------------------

### Install Python Packages from requirements.txt using pip or uv

Source: https://fastapi.tiangolo.com/fr/virtual-environments

This snippet illustrates how to install all project dependencies specified in a `requirements.txt` file. This method is crucial for reproducible builds and consistent environments across different development stages. Commands are provided for both `pip` and `uv`.

```bash
pip install -r requirements.txt
```

```bash
uv pip install -r requirements.txt
```

--------------------------------

### Configure SQLite Database Engine and Session

Source: https://fastapi.tiangolo.com/ja/tutorial/sql-databases

Sets up SQLite database connection with SQLModel engine creation and session management. Includes database initialization on startup and dependency injection setup for session handling across endpoints.

```python
from sqlmodel import Session, create_engine
from fastapi import Depends
from typing import Annotated

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]
```

--------------------------------

### FastAPI APIRouter Setup Example

Source: https://fastapi.tiangolo.com/es/reference/apirouter_q=

Complete example demonstrating how to create a FastAPI application with APIRouter, define a Pydantic model for request validation, and include the router in the main application.

```APIDOC
## FastAPI Application Setup with APIRouter

### Description
This example shows the complete setup for a FastAPI application using APIRouter to organize path operations and Pydantic models for request/response validation.

### Code Example
```python
from fastapi import APIRouter, FastAPI
from pydantic import BaseModel

class Item(BaseModel):
    name: str
    description: str | None = None

app = FastAPI()
router = APIRouter()

@router.post("/items/")
def create_item(item: Item):
    return {"message": "Item created"}

app.include_router(router)
```

### Components

#### Item Model
- **name** (string) - Required field for the item name
- **description** (string | None) - Optional field for item description with default value of None

#### Application Setup
1. Create a FastAPI application instance
2. Create an APIRouter instance for organizing endpoints
3. Define path operations using the router decorator
4. Include the router in the main FastAPI application using `include_router()`

### Benefits of Using APIRouter
- Organize related endpoints into logical groups
- Reusable router modules across multiple applications
- Cleaner code structure for larger applications
- Easier to maintain and test individual route groups
```

--------------------------------

### Example PATH Variable Before Virtual Environment Activation

Source: https://fastapi.tiangolo.com/uk/virtual-environments

These examples illustrate the typical system PATH environment variable on Linux/macOS and Windows before a Python virtual environment is activated. The PATH defines the directories where the operating system searches for executable programs.

```text
/usr/bin:/bin:/usr/sbin:/sbin
```

```text
C:\Windows\System32
```

--------------------------------

### Example PATH Variable After Virtual Environment Activation

Source: https://fastapi.tiangolo.com/uk/virtual-environments

These examples show how the system PATH environment variable is modified after activating a Python virtual environment. The virtual environment's 'bin' or 'Scripts' directory is prepended to the PATH, ensuring its Python executable is prioritized.

```text
/home/user/code/awesome-project/.venv/bin:/usr/bin:/bin:/usr/sbin:/sbin
```

```text
C:\Users\user\code\awesome-project\.venv\Scripts;C:\Windows\System32
```

--------------------------------

### Illustrate URL Path Component

Source: https://fastapi.tiangolo.com/tutorial/first-steps

This example highlights the 'path' component within a full URL. The path refers to the segment of the URL that follows the domain, starting from the first forward slash, and is crucial for defining specific API endpoints.

```text
https://example.com/items/foo

```

--------------------------------

### GET /items/ - Basic Router Example

Source: https://fastapi.tiangolo.com/pt/reference/apirouter_q=

Demonstrates how to create a FastAPI application with an APIRouter and define a simple GET endpoint that returns a list of items. This example shows the basic setup for organizing endpoints using routers.

```APIDOC
## GET /items/

### Description
Retrieves a list of items. This endpoint demonstrates basic router setup in FastAPI.

### Method
GET

### Endpoint
/items/

### Response
#### Success Response (200)
- **name** (string) - The name of the item

#### Response Example
[
  {"name": "Empanada"},
  {"name": "Arepa"}
]

### Code Example
```python
from fastapi import APIRouter, FastAPI

app = FastAPI()
router = APIRouter()

@router.get("/items/")
def read_items():
    return [{"name": "Empanada"}, {"name": "Arepa"}]

app.include_router(router)
```
```

--------------------------------

### Setup Database and Hero Model - Python

Source: https://fastapi.tiangolo.com/ja/tutorial/sql-databases

This code defines the database connection, creates the database tables, and defines the Hero model with its attributes. It sets up the SQLite database and defines the Hero model using SQLModel, including base classes and data validation.

```python
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select


class HeroBase(SQLModel):
    name: str = Field(index=True)
    age: int | None = Field(default=None, index=True)


class Hero(HeroBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    secret_name: str


class HeroPublic(HeroBase):
    id: int


class HeroCreate(HeroBase):
    secret_name: str


class HeroUpdate(HeroBase):
    name: str | None = None
    age: int | None = None
    secret_name: str | None = None


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]
app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
```

```python
from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select


class HeroBase(SQLModel):
    name: str = Field(index=True)
    age: int | None = Field(default=None, index=True)


class Hero(HeroBase, table=True):
    id: int | None = Field(default=None, primary_key=True)
    secret_name: str


class HeroPublic(HeroBase):
    id: int


class HeroCreate(HeroBase):
    secret_name: str


class HeroUpdate(HeroBase):
    name: str | None = None
    age: int | None = None
    secret_name: str | None = None


sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
```

--------------------------------

### OAuth2 Password Flow Authentication Setup

Source: https://fastapi.tiangolo.com/fr/tutorial/security/first-steps_q=

Complete setup guide for implementing OAuth2 password flow in FastAPI. This includes creating the main application file, installing dependencies, and understanding the authentication workflow.

```APIDOC
## OAuth2 Password Flow Authentication Setup

### Description
This section covers the complete setup for OAuth2 password flow authentication in FastAPI, including dependency installation, application initialization, and the authentication workflow.

### Installation
#### Required Dependencies
```bash
pip install "fastapi[standard]"
pip install python-multipart
```

**Note:** The `python-multipart` package is required because OAuth2 uses form data for transmitting username and password credentials.

### Application Setup
#### main.py
```python
from typing import Annotated
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/items/")
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}
```

### Running the Application
```bash
fastapi dev main.py
```

**Output:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

### Accessing Interactive Documentation
- Navigate to: `http://127.0.0.1:8000/docs`
- Features:
  - "Authorize" button for OAuth2 authentication
  - Lock icon on protected endpoints
  - Interactive authorization form for testing

### OAuth2 Password Flow Workflow
1. **User Authentication:** User enters username and password in frontend
2. **Token Request:** Frontend sends credentials to `tokenUrl` endpoint
3. **Token Generation:** API validates credentials and returns bearer token
4. **Token Storage:** Frontend stores token temporarily
5. **Authenticated Requests:** Frontend includes token in Authorization header: `Bearer {token}`
6. **Token Validation:** API validates token for each protected endpoint request

### Token Characteristics
- **Expiration:** Tokens expire after a set time period
- **Re-authentication:** Users must log in again after token expiration
- **Security:** Reduces risk compared to permanent credentials
- **Format:** Bearer token sent in Authorization header

### Alternative Syntax (Python 3.9+)
```python
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

@app.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}
```

**Recommendation:** Use `Annotated` version for better type hints and IDE support.
```

--------------------------------

### Define `examples` in Python for OpenAPI

Source: https://fastapi.tiangolo.com/de/reference/openapi/models_q=

Initializes the `examples` schema property to `None`. This property provides an array of example values for a schema or a property, useful for documentation and testing.

```python
examples = None
```

--------------------------------

### GET /

Source: https://fastapi.tiangolo.com/tutorial/first-steps_q=

Retrieves a simple 'Hello World' message from the root endpoint of the FastAPI application.

```APIDOC
## GET /

### Description
Retrieves a simple 'Hello World' message from the root endpoint of the FastAPI application.

### Method
GET

### Endpoint
/

### Parameters
#### Path Parameters
(None)

#### Query Parameters
(None)

#### Request Body
(None)

### Request Example
(No request body)

### Response
#### Success Response (200)
- **message** (string) - A greeting message.

#### Response Example
{
  "message": "Hello World"
}
```

--------------------------------

### Path Operation Function Definition

Source: https://fastapi.tiangolo.com/tutorial/first-steps

Guide to defining path operation functions in FastAPI. Covers function syntax, async vs sync functions, and return value handling.

```APIDOC
## Path Operation Function Definition

### Function Components

#### Path
The URL path where the endpoint is accessible (e.g., `/`, `/items/`, `/users/{user_id}`)

#### Operation
The HTTP method used to access the endpoint (GET, POST, PUT, DELETE, etc.)

#### Function
The Python function decorated with the path operation decorator

### Async vs Sync Functions

#### Async Function (Recommended)
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
```

#### Sync Function
```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}
```

### Return Values

Path operation functions can return:
- **dict** - Automatically converted to JSON
- **list** - Automatically converted to JSON
- **str** - String values
- **int** - Integer values
- **Pydantic models** - Automatically validated and serialized
- **ORM objects** - Automatically converted to JSON
- **Other objects** - Most common Python objects are supported

### Example with Different Return Types

```python
# Dictionary return
@app.get("/dict")
async def return_dict():
    return {"key": "value"}

# List return
@app.get("/list")
async def return_list():
    return [1, 2, 3]

# String return
@app.get("/string")
async def return_string():
    return "Hello"

# Integer return
@app.get("/int")
async def return_int():
    return 42
```
```

--------------------------------

### Authenticate and Deploy FastAPI Application to FastAPI Cloud

Source: https://fastapi.tiangolo.com/tutorial/first-steps_q=

These command-line examples demonstrate the process of deploying a FastAPI application to FastAPI Cloud. The `fastapi login` command is used for user authentication, followed by `fastapi deploy` to push the application, making it accessible via a generated URL.

```cli
fastapi login
fast →fastapi login  
You are logged in to FastAPI Cloud 🚀  
  
restart ↻
```

```cli
fastapi deploy
fast →fastapi deploy  
Deploying to FastAPI Cloud...  
  
✅ Deployment successful!  
  
🐔 Ready the chicken! Your app is ready at https://myapp.fastapicloud.dev  
  
restart ↻
```

--------------------------------

### OAuth2 Authentication Setup

Source: https://fastapi.tiangolo.com/fr/tutorial/security/first-steps

Complete setup guide for implementing OAuth2 password flow authentication in FastAPI. Includes installation requirements, application initialization, and configuration of the OAuth2PasswordBearer security scheme.

```APIDOC
## FastAPI OAuth2 Password Flow Setup

### Installation Requirements

#### Required Packages
```bash
pip install "fastapi[standard]"
```

Or if installing FastAPI without standard dependencies:
```bash
pip install fastapi
pip install python-multipart
```

**Note:** The `python-multipart` package is required because OAuth2 uses form data for sending username and password.

### Application Initialization

#### Basic Setup (Python 3.10+)
```python
from typing import Annotated
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
```

#### Alternative Setup (Python 3.9+)
```python
from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")
```

### Running the Application

```bash
fastapi dev main.py
```

Output:
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

### Interactive Documentation

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

#### Features in Interactive Docs
- Automatic "Authorize" button for OAuth2 authentication
- Lock icon on protected endpoints
- Interactive authorization form for testing
- Automatic API documentation generation

### Configuration Parameters

- **tokenUrl** - The URL endpoint where clients obtain tokens (e.g., "token")
- **scopes** - Optional dictionary of available permission scopes
- **scheme_name** - Name of the security scheme in documentation
```

--------------------------------

### Initialize In-Memory User Database and Password Hashing Setup in Python

Source: https://fastapi.tiangolo.com/advanced/security/oauth2-scopes

This code sets up a mock in-memory user database for demonstration purposes, containing user credentials and roles. It also initializes the PasswordHash utility for secure password management using Argon2.

```python
fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$wagCPXjifgvUFBzq4hqe3w$CYaIb8sB+wtD+Vu/P4uod1+Qof8h+1g7bbDlBID48Rc",
        "disabled": False
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Chains",
        "email": "alicechains@example.com",
        "hashed_password": "$argon2id$v=19$m=65536,t=3,p=4$g2/AV1zwopqUntPKJavBFw$BwpRGDCyUHLvHICnwijyX8ROGoiUPwNKZ7915MeYfCE",
        "disabled": True
    }
}


password_hash = PasswordHash.recommended()
```

--------------------------------

### Initialize FastAPI App with Fake User Database

Source: https://fastapi.tiangolo.com/tutorial/security/simple-oauth2

Set up FastAPI application instance and populate fake_users_db with sample user records containing credentials and metadata. Database includes both active and disabled users for testing authentication flows.

```python
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "fakehashedsecret",
        "disabled": False,
    },
    "alice": {
        "username": "alice",
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        "hashed_password": "fakehashedsecret2",
        "disabled": True,
    },
}

app = FastAPI()


def fake_hash_password(password: str):
    return "fakehashed" + password
```

--------------------------------

### Verify Static Files Serving - ReDoc JavaScript Example

Source: https://fastapi.tiangolo.com/uk/how-to/custom-docs-ui-assets_q=

Example output from accessing a static JavaScript file served by FastAPI. This demonstrates that static files are correctly mounted and accessible at the configured path. The response shows the beginning of the minified ReDoc standalone JavaScript bundle.

```javascript
/*! For license information please see redoc.standalone.js.LICENSE.txt */
!function(e,t){"object"==typeof exports&&"object"==typeof module?module.exports=t(require("null")):
```

--------------------------------

### GET /openapi.json - OpenAPI Schema

Source: https://fastapi.tiangolo.com/tutorial/first-steps

FastAPI automatically generates an OpenAPI schema that defines your entire API structure, including all paths, parameters, request/response models, and other metadata. This schema is used by documentation tools and can be accessed directly.

```APIDOC
## GET /openapi.json

### Description
Returns the OpenAPI schema definition for your entire API. This schema follows the OpenAPI standard and includes all API paths, parameters, request/response models, and metadata. Used by Swagger UI and ReDoc for generating documentation.

### Method
GET

### Endpoint
/openapi.json

### Response
#### Success Response (200)
JSON object containing the complete OpenAPI schema specification including:
- **openapi** (string) - OpenAPI version
- **info** (object) - API metadata (title, version, description)
- **paths** (object) - All API endpoints and their operations
- **components** (object) - Reusable schema definitions

#### Response Example
```json
{
  "openapi": "3.0.2",
  "info": {
    "title": "FastAPI",
    "version": "0.1.0"
  },
  "paths": {
    "/": {
      "get": {
        "summary": "Root",
        "operationId": "root__get",
        "responses": {
          "200": {
            "description": "Successful Response",
            "content": {
              "application/json": {
                "schema": {}
              }
            }
          }
        }
      }
    }
  }
}
```
```

--------------------------------

### Install httpx for FastAPI TestClient

Source: https://fastapi.tiangolo.com/fr/tutorial/testing_q=

Before using FastAPI's `TestClient`, the `httpx` library must be installed. This command demonstrates how to install `httpx` using pip, preferably within a virtual environment, to enable HTTP requests in tests.

```bash
pip install httpx
```

--------------------------------

### Read Heroes GET Endpoint with Pagination

Source: https://fastapi.tiangolo.com/ja/tutorial/sql-databases

Implements GET endpoint to retrieve heroes with offset/limit pagination. Includes query parameter validation using Query with maximum limit of 100 records. Supports both Annotated and traditional parameter styles.

```python
from typing import Annotated
from fastapi import Query

@app.get("/heroes/")
def read_heroes(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> list[Hero]:
    heroes = session.exec(select(Hero).offset(offset).limit(limit)).all()
    return heroes
```

```python
from fastapi import Query

@app.get("/heroes/")
def read_heroes(
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, le=100),
) -> list[Hero]:
    heroes = session.exec(select(Hero).offset(offset).limit(limit)).all()
    return heroes
```

--------------------------------

### GET /heroes/{hero_id}

Source: https://fastapi.tiangolo.com/ja/tutorial/sql-databases

Retrieves a single hero by their ID. Returns the hero data in the HeroPublic response model format. Returns a 404 error if the hero is not found.

```APIDOC
## GET /heroes/{hero_id}

### Description
Retrieve a single hero by their unique identifier. Returns the hero information in the HeroPublic response model format.

### Method
GET

### Endpoint
/heroes/{hero_id}

### Parameters
#### Path Parameters
- **hero_id** (integer) - Required - The unique identifier of the hero to retrieve

### Response
#### Success Response (200)
- **id** (integer) - The unique identifier of the hero
- **name** (string) - The name of the hero
- **secret_name** (string) - The secret identity of the hero
- **age** (integer) - The age of the hero

#### Error Response (404)
- **detail** (string) - "Hero not found" - Returned when the hero_id does not exist

### Response Example
{
  "id": 1,
  "name": "Deadpond",
  "secret_name": "Dive Wilson",
  "age": null
}
```

--------------------------------

### Read Heroes GET Endpoint with Non-Annotated Dependencies

Source: https://fastapi.tiangolo.com/ja/tutorial/sql-databases

Alternative implementation of paginated GET endpoint without Annotated type hints. Uses Query(default=100, le=100) syntax instead of Annotated[int, Query(le=100)]. Functionally equivalent but less preferred approach.

```python
from fastapi import Query

@app.get("/heroes/")
def read_heroes(
    session: Session = Depends(get_session),
    offset: int = 0,
    limit: int = Query(default=100, le=100),
) -> list[Hero]:
    heroes = session.exec(select(Hero).offset(offset).limit(limit)).all()
    return heroes
```

--------------------------------

### Read Single Hero GET Endpoint by ID

Source: https://fastapi.tiangolo.com/ja/tutorial/sql-databases

Retrieves a specific hero by ID from database. Returns 404 HTTPException if hero not found. Uses session.get() for efficient single record lookup.

```python
from fastapi import HTTPException

@app.get("/heroes/{hero_id}", response_model=HeroPublic)
def read_hero(hero_id: int, session: SessionDep):
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return hero
```

```python
@app.get("/heroes/{hero_id}", response_model=HeroPublic)
def read_hero(hero_id: int, session: Session = Depends(get_session)):
    hero = session.get(Hero, hero_id)
    if not hero:
        raise HTTPException(status_code=404, detail="Hero not found")
    return hero
```

--------------------------------

### Identify Path Component in a URL

Source: https://fastapi.tiangolo.com/tutorial/first-steps

This snippet explicitly shows the extracted path component from a given URL. In API development, the path is used to identify and route requests to specific resources or operations.

```text
/items/foo

```

--------------------------------

### GET /heroes/

Source: https://fastapi.tiangolo.com/ja/tutorial/sql-databases

Retrieves a paginated list of all heroes from the database. Supports offset and limit parameters for pagination, with a maximum limit of 100 heroes per request. Returns heroes serialized as HeroPublic objects.

```APIDOC
## GET /heroes/

### Description
Retrieves a paginated list of all heroes with proper validation and serialization using the HeroPublic response model.

### Method
GET

### Endpoint
/heroes/

### Parameters
#### Query Parameters
- **offset** (integer) - Optional - Number of heroes to skip (default: 0)
- **limit** (integer) - Optional - Maximum number of heroes to return, must be <= 100 (default: 100)

### Response
#### Success Response (200)
- **heroes** (array of HeroPublic objects) - List of hero objects containing public fields

### Response Example
```json
[
  {
    "id": 1,
    "name": "Hero Name",
    "secret_name": "Secret Name",
    "age": 30
  },
  {
    "id": 2,
    "name": "Another Hero",
    "secret_name": "Another Secret",
    "age": 25
  }
]
```
```

--------------------------------

### Example API Request and Callback Flow

Source: https://fastapi.tiangolo.com/zh-hant/advanced/openapi-callbacks

This section provides a sequence of examples demonstrating the full callback workflow. It starts with an initial API request to create an invoice, including a callback URL. It then shows the corresponding JSON request body, followed by the dynamically generated callback URL and its JSON payload, and finally, the expected response from the external API.

```http
https://yourapi.com/invoices/?callback_url=https://www.external.org/events
```

```json
{
    "id": "2expen51ve",
    "customer": "Mr. Richie Rich",
    "total": "9999"
}
```

```http
https://www.external.org/events/invoices/2expen51ve
```

```json
{
    "description": "Payment celebration",
    "paid": true
}
```

```json
{
    "ok": true
}
```

--------------------------------

### Authenticate with FastAPI Cloud CLI

Source: https://fastapi.tiangolo.com/tutorial/first-steps

Before deploying an application to FastAPI Cloud, users must authenticate using the command-line interface. This command logs you into your FastAPI Cloud account, enabling subsequent deployment operations.

```bash
fastapi login
fast →fastapi login  
You are logged in to FastAPI Cloud 🚀  
  
restart ↻

```

--------------------------------

### Interactive API Documentation Endpoints

Source: https://fastapi.tiangolo.com/tutorial/first-steps

FastAPI automatically generates interactive API documentation at two endpoints: /docs (Swagger UI) and /redoc (ReDoc). These endpoints provide automatic, interactive exploration of your API schema.

```APIDOC
## GET /docs

### Description
Automatic interactive API documentation provided by Swagger UI. Displays all available endpoints, parameters, request/response schemas, and allows testing endpoints directly from the browser.

### Method
GET

### Endpoint
/docs

### Response
HTML page with interactive Swagger UI documentation

---

## GET /redoc

### Description
Alternative automatic API documentation provided by ReDoc. Displays all available endpoints and schemas in a clean, alternative documentation format.

### Method
GET

### Endpoint
/redoc

### Response
HTML page with ReDoc documentation interface
```

--------------------------------

### FastAPI GET Path Operation Decorator Definition and Example

Source: https://fastapi.tiangolo.com/zh/reference/apirouter_q=

This snippet defines the `get` decorator in FastAPI, outlining its parameters for configuring HTTP GET endpoints, such as response models, status codes, dependencies, and OpenAPI documentation. It also includes a practical Python example demonstrating how to use `@router.get()` with an `APIRouter` to create a basic GET endpoint.

```python
response_class: Annotated[
        type[Response],
        Doc(
            """
            Response class to be used for this *path operation*.

            This will not be used if you return a response directly.

            Read more about it in the
            [FastAPI docs for Custom Response - HTML, Stream, File, others](https://fastapi.tiangolo.com/advanced/custom-response/#redirectresponse).
            """
        ),
    ] = Default(JSONResponse),
    name: Annotated[
        str | None,
        Doc(
            """
            Name for this *path operation*. Only used internally.
            """
        ),
    ] = None,
    callbacks: Annotated[
        list[BaseRoute] | None,
        Doc(
            """
            List of *path operations* that will be used as OpenAPI callbacks.

            This is only for OpenAPI documentation, the callbacks won't be used
            directly.

            It will be added to the generated OpenAPI (e.g. visible at `/docs`).

            Read more about it in the
            [FastAPI docs for OpenAPI Callbacks](https://fastapi.tiangolo.com/advanced/openapi-callbacks/).
            """
        ),
    ] = None,
    openapi_extra: Annotated[
        dict[str, Any] | None,
        Doc(
            """
            Extra metadata to be included in the OpenAPI schema for this *path
            operation*.

            Read more about it in the
            [FastAPI docs for Path Operation Advanced Configuration](https://fastapi.tiangolo.com/advanced/path-operation-advanced-configuration/#custom-openapi-path-operation-schema).
            """
        ),
    ] = None,
    generate_unique_id_function: Annotated[
        Callable[[APIRoute], str],
        Doc(
            """
            Customize the function used to generate unique IDs for the *path
            operations* shown in the generated OpenAPI.

            This is particularly useful when automatically generating clients or
            SDKs for your API.

            Read more about it in the
            [FastAPI docs about how to Generate Clients](https://fastapi.tiangolo.com/advanced/generate-clients/#custom-generate-unique-id-function).
            """
        ),
    ] = Default(generate_unique_id),
) -> Callable[[DecoratedCallable], DecoratedCallable]:
    """
    Add a *path operation* using an HTTP GET operation.
    """
    return self.api_route(
        path=path,
        response_model=response_model,
        status_code=status_code,
        tags=tags,
        dependencies=dependencies,
        summary=summary,
        description=description,
        response_description=response_description,
        responses=responses,
        deprecated=deprecated,
        methods=["GET"],
        operation_id=operation_id,
        response_model_include=response_model_include,
        response_model_exclude=response_model_exclude,
        response_model_by_alias=response_model_by_alias,
        response_model_exclude_unset=response_model_exclude_unset,
        response_model_exclude_defaults=response_model_exclude_defaults,
        response_model_exclude_none=response_model_exclude_none,
        include_in_schema=include_in_schema,
        response_class=response_class,
        name=name,
        callbacks=callbacks,
        openapi_extra=openapi_extra,
        generate_unique_id_function=generate_unique_id_function,
    )
```

```python
from fastapi import APIRouter, FastAPI

app = FastAPI()
router = APIRouter()

@router.get("/items/")
def read_items():
    return [{"name": "Empanada"}, {"name": "Arepa"}]

app.include_router(router)
```

--------------------------------

### POST /heroes/

Source: https://fastapi.tiangolo.com/ja/tutorial/sql-databases_q=

Creates a new hero entry in the database. The hero's ID will be automatically generated upon successful creation.

```APIDOC
## POST /heroes/

### Description
Creates a new hero entry in the database. The hero's ID will be automatically generated upon successful creation.

### Method
POST

### Endpoint
/heroes/

### Parameters
#### Path Parameters
(None)

#### Query Parameters
(None)

#### Request Body
- **name** (string) - Required - The hero's name.
- **secret_name** (string) - Required - The hero's secret identity.
- **age** (integer, optional) - Optional - The hero's age.

### Request Example
{
  "name": "Deadpond",
  "secret_name": "Dive Wilson",
  "age": 30
}

### Response
#### Success Response (200)
- **id** (integer) - The unique ID of the created hero.
- **name** (string) - The hero's name.
- **secret_name** (string) - The hero's secret identity.
- **age** (integer, optional) - The hero's age.

#### Response Example
{
  "name": "Deadpond",
  "secret_name": "Dive Wilson",
  "id": 1,
  "age": 30
}
```

--------------------------------

### GET /users/ - Read Users Example

Source: https://fastapi.tiangolo.com/es/reference/apirouter

Example endpoint demonstrating how to create a basic GET route using APIRouter. This route returns a list of users and is tagged for OpenAPI documentation organization.

```APIDOC
## GET /users/

### Description
Retrieve a list of all users from the system.

### Method
GET

### Endpoint
/users/

### Tags
- users

### Response
#### Success Response (200)
- **username** (string) - The username of each user in the list

#### Response Example
```json
[
  {"username": "Rick"},
  {"username": "Morty"}
]
```

### Implementation Example
```python
from fastapi import APIRouter, FastAPI

app = FastAPI()
router = APIRouter()

@router.get("/users/", tags=["users"])
async def read_users():
    return [{"username": "Rick"}, {"username": "Morty"}]

app.include_router(router)
```
```

--------------------------------

### GET /items/

Source: https://fastapi.tiangolo.com/es/reference/fastapi

Retrieves a list of items from the API. This is an example of a basic GET endpoint in FastAPI.

```APIDOC
## GET /items/

### Description
Retrieves a list of items from the API. This is an example of a basic GET endpoint in FastAPI.

### Method
GET

### Endpoint
/items/

### Parameters
(No parameters for this endpoint)

### Request Example
(No request body for this GET endpoint)

### Response
#### Success Response (200)
- **name** (string) - The name of the item.

#### Response Example
```json
[
  {
    "name": "Empanada"
  },
  {
    "name": "Arepa"
  }
]
```
```

--------------------------------

### Implement FastAPI Startup and Shutdown Logic with `lifespan`

Source: https://fastapi.tiangolo.com/advanced/events_q=

This Python example demonstrates how to use `FastAPI`'s `lifespan` parameter with an `@asynccontextmanager` to define operations that run during application startup and shutdown. It simulates loading a machine learning model into memory before the server starts accepting requests and clearing it when the server stops, ensuring proper resource management.

```python
from contextlib import asynccontextmanager

from fastapi import FastAPI


def fake_answer_to_everything_ml_model(x: float):
    return x * 42


ml_models = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    ml_models["answer_to_everything"] = fake_answer_to_everything_ml_model
    yield
    # Clean up the ML models and release the resources
    ml_models.clear()


app = FastAPI(lifespan=lifespan)


@app.get("/predict")
async def predict(x: float):
    result = ml_models["answer_to_everything"](x)
    return {"result": result}
```

--------------------------------

### Activate Virtual Environment across OS/Shells

Source: https://fastapi.tiangolo.com/fr/virtual-environments

Provides commands to activate the virtual environment, which must be done every time you start a new terminal session for the project. Activating ensures that any Python commands or package installations use the isolated environment's dependencies.

```bash
source .venv/bin/activate
```

```powershell
.venv\Scripts\Activate.ps1
```

```bash
source .venv/Scripts/activate
```

--------------------------------

### Run FastAPI application using Uvicorn server (Bash)

Source: https://fastapi.tiangolo.com/deployment/manually

This command initiates the Uvicorn ASGI server to host a FastAPI application. It specifies `main.py` as the module and `app` as the FastAPI instance, binding the server to all available network interfaces (`0.0.0.0`) on port `80`. This setup is typical for both development and production environments, though `--reload` is recommended for development only.

```bash
uvicorn main:app --host 0.0.0.0 --port 80
```

--------------------------------

### Example Component

Source: https://fastapi.tiangolo.com/reference/openapi/models

The Example component provides sample values for request/response bodies and parameters, helping API consumers understand how to use the API.

```APIDOC
## Example Component

### Description
Provides sample values for API requests and responses.

### Properties
- **summary** (string) - Optional - Short summary of the example
- **description** (string) - Optional - Detailed description
- **value** (any) - Optional - The example value
- **externalValue** (string) - Optional - URL to external example

### Example
```json
{
  "summary": "Successful user creation",
  "description": "Example of a successful user creation response",
  "value": {
    "id": 1,
    "name": "John Doe",
    "email": "john@example.com",
    "created_at": "2024-01-15T10:30:00Z"
  }
}
```
```

--------------------------------

### GET /items/ - Basic Router Example

Source: https://fastapi.tiangolo.com/tr/reference/apirouter_q=

Demonstrates how to create a FastAPI application with an APIRouter and define a simple GET endpoint that returns a list of items. This example shows the basic pattern for organizing routes using routers.

```APIDOC
## GET /items/

### Description
Retrieves a list of items. This endpoint demonstrates basic FastAPI routing using APIRouter.

### Method
GET

### Endpoint
/items/

### Parameters
None

### Response
#### Success Response (200)
- **items** (array) - List of item objects
  - **name** (string) - The name of the item

#### Response Example
```json
[
  {"name": "Empanada"},
  {"name": "Arepa"}
]
```

### Implementation Example
```python
from fastapi import APIRouter, FastAPI

app = FastAPI()
router = APIRouter()

@router.get("/items/")
def read_items():
    return [{"name": "Empanada"}, {"name": "Arepa"}]

app.include_router(router)
```
```