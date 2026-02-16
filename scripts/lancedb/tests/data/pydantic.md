### Install and Initialize Pyrefly

Source: https://pyrefly.org/

This command installs Pyrefly using pip and then initializes it in the project. It's the standard way to get started with Pyrefly.

```bash
pip install pyrefly && pyrefly init
```

--------------------------------

### Install HTTPX using pip

Source: https://www.python-httpx.org/

This snippet shows the basic command to install the HTTPX library using pip. It is the primary method for getting started with the library.

```bash
pip install httpx
```

--------------------------------

### Setup Pyrefly with mason.nvim in Neovim

Source: https://pyrefly.org/en/docs/IDE

This snippet shows how to set up the Pyrefly language server using the mason.nvim plugin manager in Neovim. It includes enabling mason and mason-lspconfig, and installing Pyrefly.

```lua
require("mason").setup()
require("mason-lspconfig").setup()
```

--------------------------------

### Paths Object Example

Source: https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.1.0

An example illustrating the structure of the Paths object, showing a GET operation for retrieving pets.

```APIDOC
## Paths Object Example

### Description
Provides a sample of the Paths object, demonstrating how to define an endpoint and its associated operations.

### Example Structure
```json
{
  "/pets": {
    "get": {
      "description": "Returns all pets from the system that the user has access to",
      "responses": {
        "200": {
          "description": "A list of pets.",
          "content": {
            "application/json": {
              "schema": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/pet"
                }
              }
            }
          }
        }
      }
    }
  }
}
```

### YAML Example Structure
```yaml
/pets:
  get:
    description: Returns all pets from the system that the user has access to
    responses:
      '200':
        description: A list of pets.
        content:
          application/json:
            schema:
              type: array
              items:
                $ref: '#/components/schemas/pet'
```
```

--------------------------------

### Installation

Source: https://github.com/koxudaxi/datamodel-code-generator

Instructions on how to install the datamodel-code-generator using pip.

```APIDOC
## Installation

To install `datamodel-code-generator`:

```bash
$ pip install datamodel-code-generator
```
```

--------------------------------

### Parameter Examples

Source: https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.1.0

Shows how to reference examples for API parameters.

```APIDOC
## Parameter Examples

This section demonstrates how to provide examples for API parameters, particularly query parameters.

### Query Parameter Example
An example for a 'zipCode' query parameter can be referenced from the components section.

```yaml
parameters:
  - name: 'zipCode'
    in: 'query'
    schema:
      type: 'string'
      format: 'zip-code'
    examples:
      zip-example:
        $ref: '#/components/examples/zip-example'
```
```

--------------------------------

### OpenAPI Parameter Examples

Source: https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.1.0

Illustrates how to define examples for query parameters in an OpenAPI specification. It shows referencing an example from the components section.

```yaml
parameters:
  - name: 'zipCode'
    in: 'query'
    schema:
      type: 'string'
      format: 'zip-code'
    examples:
      zip-example:
        $ref: '#/components/examples/zip-example'
```

--------------------------------

### Mypy pyproject.toml Configuration Example

Source: https://mypy.readthedocs.io/en/latest/config_file.html

This example demonstrates how to configure mypy using a pyproject.toml file, following PEP 518 standards. It includes global options, per-module overrides, and examples of TOML string formatting.

```toml
# mypy global options:
[tool.mypy]
python_version = "3.9"
warn_return_any = true
warn_unused_configs = true
exclude = [
  '^file1\.py$', # TOML literal string (single-quotes, no escaping necessary)
  '^file2\\.py$', # TOML basic string (double-quotes, backslash and other characters need escaping)
]

# mypy per-module options:
[[tool.mypy.overrides]]
module = "mycode.foo.* disallow_untyped_defs = true

[[tool.mypy.overrides]]
module = "mycode.bar"
warn_return_any = false

[[tool.mypy.overrides]]
module = [
  "somelibrary",
  "some_other_library"
]
ignore_missing_imports = true
```

--------------------------------

### Response Examples

Source: https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.1.0

Illustrates how to include examples for successful API responses.

```APIDOC
## Response Examples

This section covers how to provide examples for successful API responses, such as a confirmation message.

### Success Response Example
A successful booking confirmation can be represented with a referenced example.

```yaml
responses:
  '200':
    description: your car appointment has been booked
    content:
      application/json:
        schema:
          $ref: '#/components/schemas/SuccessResponse'
        examples:
          confirmation-success:
            $ref: '#/components/examples/confirmation-success'
```
```

--------------------------------

### Paths Object Example (YAML)

Source: https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.1.0

An example illustrating the structure of the Paths Object in YAML format, defining a '/pets' endpoint with a GET operation.

```yaml
/pets:
  get:
    description: Returns all pets from the system that the user has access to
    responses:
      '200':
        description: A list of pets.
        content:
          application/json:
            schema:
              type: array
              items:
                $ref: '#/components/schemas/pet'
```

--------------------------------

### Neovim LSP Configuration Example

Source: https://pyrefly.org/en/docs/IDE

A basic Neovim LSP configuration example, potentially for setting up various language servers. This snippet specifies the command and arguments for a language server.

```lua
return {
  cmd = {"pyrefly", "lsp"},
}
```

--------------------------------

### OpenAPI Response Examples

Source: https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.1.0

Shows how to specify examples for successful responses in OpenAPI, including referencing JSON schemas and example objects.

```yaml
responses:
  '200':
    description: your car appointment has been booked
    content:
      application/json:
        schema:
          $ref: '#/components/schemas/SuccessResponse'
        examples:
          confirmation-success:
            $ref: '#/components/examples/confirmation-success'
```

--------------------------------

### Install datamodel-code-generator using pip

Source: https://koxudaxi.github.io/datamodel-code-generator

Installs the datamodel-code-generator package using pip. This is the primary method for getting the tool onto your system. Ensure you have Python and pip installed.

```bash
pip install datamodel-code-generator
```

--------------------------------

### Paths Object Example (JSON)

Source: https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.1.0

An example illustrating the structure of the Paths Object in JSON format, defining a '/pets' endpoint with a GET operation.

```json
{
  "/pets": {
    "get": {
      "description": "Returns all pets from the system that the user has access to",
      "responses": {
        "200": {
          "description": "A list of pets.",
          "content": {
            "application/json": {
              "schema": {
                "type": "array",
                "items": {
                  "$ref": "#/components/schemas/pet"
                }
              }
            }
          }
        }
      }
    }
  }
}
```

--------------------------------

### JSON Media Type Examples in OpenAPI

Source: https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.1.0

Demonstrates how to define 'application/json' media types with schema references and examples for different pet types. This includes inline examples and references to external example definitions.

```json
{
  "application/json": {
    "schema": {
         "$ref": "#/components/schemas/Pet"
    },
    "examples": {
      "cat" : {
        "summary": "An example of a cat",
        "value":
          {
            "name": "Fluffy",
            "petType": "Cat",
            "color": "White",
            "gender": "male",
            "breed": "Persian"
          }
      },
      "dog": {
        "summary": "An example of a dog with a cat's name",
        "value" :  {
          "name": "Puma",
          "petType": "Dog",
          "color": "Black",
          "gender": "Female",
          "breed": "Mixed"
        }
      },
      "frog": {
          "$ref": "#/components/examples/frog-example"
        }
    }
  }
}
```

```yaml
application/json:
  schema:
    $ref: "#/components/schemas/Pet"
  examples:
    cat:
      summary: An example of a cat
      value:
        name: Fluffy
        petType: Cat
        color: White
        gender: male
        breed: Persian
    dog:
      summary: An example of a dog with a cat's name
      value:
        name: Puma
        petType: Dog
        color: Black
        gender: Female
        breed: Mixed
    frog:
      $ref: "#/components/examples/frog-example"
```

--------------------------------

### Install and Test Rich Library

Source: https://github.com/willmcgugan/rich

Instructions on how to install the Rich library using pip and a command to test its basic output in the terminal. This is the first step to enable rich terminal capabilities.

```python
python -m pip install rich
```

```python
python -m rich
```

--------------------------------

### datamodel-codegen Installation

Source: https://github.com/koxudaxi/datamodel-code-generator

Instructions for installing the datamodel-code-generator tool using pip.

```APIDOC
## Installation

### `datamodel-code-generator`

To install `datamodel-code-generator`:

```bash
$ pip install datamodel-code-generator
```

### `http` extra option

If you want to resolve `$ref` for remote files then you should specify `http` extra option.

```bash
$ pip install 'datamodel-code-generator[http]'
```

### `graphql` extra option

If you want to generate data model from a GraphQL schema then you should specify `graphql` extra option.

```bash
$ pip install 'datamodel-code-generator[graphql]'
```

### Docker Image

The docker image is in Docker Hub

```bash
$ docker pull koxudaxi/datamodel-code-generator
```
```

--------------------------------

### Example YAML Build Configuration

Source: https://peps.python.org/pep-0518

This snippet shows an example of how build requirements can be specified using the YAML format. It lists the necessary packages for the build process.

```yaml
build:
  requires:
    - setuptools
    - wheel>=0.27
```

--------------------------------

### Pydantic Data Validation Example

Source: https://github.com/pydantic/pydantic/tree/main

A basic example demonstrating how to define a Pydantic model for data validation using Python type hints. It shows model instantiation with external data and accessing validated attributes. This requires the 'pydantic' library to be installed.

```python
from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str = 'John Doe'
    signup_ts: Optional[datetime] = None
    friends: list[int] = []


external_data = {
    'id': '123',
    'signup_ts': '2017-06-01 12:22',
    'friends': [1, '2', b'3']
}

user = User(**external_data)

print(user)  #> User id=123 name='John Doe' signup_ts=datetime.datetime(2017, 6, 1, 12, 22) friends=[1, 2, 3]
print(user.id)  #> 123
```

--------------------------------

### Install and Configure Pre-commit Hook

Source: https://pyrefly.org/en/docs/installation

These commands demonstrate how to install the `pre-commit` tool, install the Pyrefly pre-commit hook into your local Git repository, and update hooks. This is typically done once per clone and ensures type checking on every commit.

```Shell
# 1. Once per clone
pip install pre-commit
# or pipx install ‑pre-commit
pre-commit install

# 2. Upgrade hooks when you bump versions in YAML
pre-commit autoupdate

# 3. Manual full run (good before the first push or when you add the hook)
pre-commit run --all-files
```

--------------------------------

### Install Dependencies from requirements.txt - PowerShell

Source: https://code.visualstudio.com/docs/python/python-tutorial

This command installs all the Python packages listed in the 'requirements.txt' file into the current virtual environment. It's a convenient way to set up a project with all its necessary dependencies.

```powershell
pip install -r requirements.txt
```

--------------------------------

### Media Type Examples (Pet)

Source: https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.2

Provides examples for the 'Pet' schema using JSON media type.

```APIDOC
## Media Type Examples (Pet)

### Description
This section demonstrates example request or response bodies for a 'Pet' resource using the `application/json` media type. It includes examples for a cat, a dog, and a reference to another example for a frog.

### Method
GET/POST/PUT/DELETE

### Endpoint
/pets/{petId}

### Parameters
#### Query Parameters
- **petId** (string) - Required - The ID of the pet.

#### Request Body
- **name** (string) - The name of the pet.
- **petType** (string) - The type of the pet (e.g., Cat, Dog, Frog).
- **color** (string) - The color of the pet.
- **gender** (string) - The gender of the pet.
- **breed** (string) - The breed of the pet.

### Request Example (Cat)
```json
{
  "name": "Fluffy",
  "petType": "Cat",
  "color": "White",
  "gender": "male",
  "breed": "Persian"
}
```

### Request Example (Dog)
```json
{
  "name": "Puma",
  "petType": "Dog",
  "color": "Black",
  "gender": "Female",
  "breed": "Mixed"
}
```

### Request Example (Frog Reference)
```json
{
  "$ref": "#/components/examples/frog-example"
}
```

### Response
#### Success Response (200)
- **name** (string) - The name of the pet.
- **petType** (string) - The type of the pet.
- **color** (string) - The color of the pet.
- **gender** (string) - The gender of the pet.
- **breed** (string) - The breed of the pet.

#### Response Example (Cat)
```json
{
  "name": "Fluffy",
  "petType": "Cat",
  "color": "White",
  "gender": "male",
  "breed": "Persian"
}
```
```

--------------------------------

### Model with Example Data

Source: https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.2

Shows how to include an example of the data structure within the schema definition. This is useful for documentation and client generation.

```json
{
  "type": "object",
  "properties": {
    "id": {
      "type": "integer",
      "format": "int64"
    },
    "name": {
      "type": "string"
    }
  },
  "required": [
    "name"
  ],
  "example": {
    "name": "Puma",
    "id": 1
  }
}
```

```yaml
type: object
properties:
  id:
    type: integer
    format: int64
  name:
    type: string
required:
- name
example:
  name: Puma
  id: 1
```

--------------------------------

### Install Pyrefly with UV

Source: https://pyrefly.org/en/docs/installation

Installs Pyrefly using uvx, initializes the project configuration, and runs a type check with error summarization.

```bash
uvx pyrefly init
uvx pyrefly check --summarize-errors
```

--------------------------------

### Install Lambda-Compatible Wheels (arm64)

Source: https://docs.aws.amazon.com/lambda/latest/dg/python-package.html

Installs a pre-compiled wheel distribution compatible with the Lambda arm64 execution environment into a 'package' directory. Requires specifying the platform, Python version, and ensuring binary-only installation. Use for libraries with C/C++ extensions.

```bash
pip install \
 --platform manylinux2014_aarch64 \
 --target=package \
 --implementation cp \
 --python-version 3.x \
 --only-binary=:all: --upgrade \
```

--------------------------------

### Install python-ulid

Source: https://pypi.org/project/python-ulid

Installs the python-ulid library using pip. For Pydantic support, install with the optional dependency.

```bash
pip install python-ulid
```

```bash
pip install python-ulid[pydantic]
```

--------------------------------

### Install HTTPX with Optional HTTP/2 Support (bash)

Source: https://www.python-httpx.org/

This command installs HTTPX along with optional support for HTTP/2. This is useful for applications that need to leverage the newer HTTP protocol.

```bash
pip install httpx[http2]
```

--------------------------------

### OpenAPI Request Body Examples

Source: https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.1.0

Demonstrates defining JSON, XML, and plain text examples for request bodies within an OpenAPI specification. It shows how to reference schemas and provide different example formats.

```yaml
requestBody:
  content:
    'application/json':
      schema:
        $ref: '#/components/schemas/Address'
      examples:
        foo:
          summary: A foo example
          value: {"foo": "bar"}
        bar:
          summary: A bar example
          value: {"bar": "baz"}
    'application/xml':
      examples:
        xmlExample:
          summary: This is an example in XML
          externalValue: 'https://example.org/examples/address-example.xml'
    'text/plain':
      examples:
        textExample:
          summary: This is a text example
          externalValue: 'https://foo.bar/examples/address-example.txt'
```

--------------------------------

### Install Pyrefly with Pip

Source: https://pyrefly.org/en/docs/installation

Installs Pyrefly using pip, initializes the project configuration, and runs a type check with error summarization.

```bash
pip install pyrefly
pyrefly init
pyrefly check --summarize-errors
```

--------------------------------

### Manually Install Python Requirements

Source: https://github.com/serverless/serverless-python-requirements/tree/master

Manually trigger the installation of Python requirements and the creation of the requirements.zip file. This is equivalent to what the plugin does during deployment.

```bash
sls requirements install
```

--------------------------------

### Example INI Build Configuration

Source: https://peps.python.org/pep-0518

This example demonstrates an INI-style configuration for build requirements, similar to what `configparser` in Python handles. It highlights potential version skew issues.

```ini
[build]
requires = setuptools
wheel>=0.27
```

--------------------------------

### Install datamodel-code-generator

Source: https://github.com/koxudaxi/datamodel-code-generator

Installs the datamodel-code-generator package using pip. For resolving remote references like $ref, install with the 'http' extra option. For GraphQL schema support, use the 'graphql' extra option.

```bash
$ pip install datamodel-code-generator
```

```bash
$ pip install 'datamodel-code-generator[http]'
```

```bash
$ pip install 'datamodel-code-generator[graphql]'
```

--------------------------------

### Install mkdocstrings with Python Support (pip)

Source: https://mkdocstrings.github.io/

Installs the mkdocstrings package with support for Python documentation generation using pip. This command includes the necessary extras for Python.

```bash
pip install 'mkdocstrings[python]'
```

--------------------------------

### Install datamodel-code-generator via Pip

Source: https://koxudaxi.github.io/datamodel-code-generator

Standard installation of the datamodel-code-generator package using pip. This command installs the base package, enabling basic functionality for code generation.

```bash
$ pip install datamodel-code-generator
```

--------------------------------

### Install Pyrefly with Poetry

Source: https://pyrefly.org/en/docs/installation

Adds Pyrefly as a development dependency using poetry, initializes the project configuration, and runs a type check with error summarization.

```bash
poetry add --group dev pyrefly
poetry run pyrefly init
poetry run pyrefly check --summarize-errors
```

--------------------------------

### Model with Example

Source: https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.1.0

Shows how to include an example payload within the Pydantic model definition.

```APIDOC
## Model with Example

### Description
This Pydantic model definition includes an `example` field, which provides a concrete instance of the model's structure and data. This is useful for documentation and testing purposes.

### Method
N/A (Schema definition)

### Endpoint
N/A (Schema definition)

### Parameters
#### Path Parameters
N/A

#### Query Parameters
N/A

#### Request Body
- **id** (integer) - Optional - The unique identifier of the item (64-bit integer).
- **name** (string) - Required - The name of the item.

### Request Example
```json
{
  "name": "Puma",
  "id": 1
}
```

### Response
#### Success Response (200)
- **id** (integer) - The unique identifier of the item.
- **name** (string) - The name of the item.

#### Response Example
```json
{
  "name": "Puma",
  "id": 1
}
```
```

--------------------------------

### Install mkdocstrings with Python Support (conda)

Source: https://mkdocstrings.github.io/

Installs mkdocstrings and the mkdocstrings-python handler using conda from the conda-forge channel.

```bash
conda install -c conda-forge mkdocstrings mkdocstrings-python
```

--------------------------------

### Parameter Object Examples

Source: https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.2

Provides practical examples of defining API parameters using the Parameter Object structure, covering header, path, query, and complex content-based parameters.

```APIDOC
## Parameter Object Examples

### Header Parameter (Array of integers)

This example defines a required header parameter named `token` that accepts an array of 64-bit integers.

**JSON Definition:**
```json
{
  "name": "token",
  "in": "header",
  "description": "token to be passed as a header",
  "required": true,
  "schema": {
    "type": "array",
    "items": {
      "type": "integer",
      "format": "int64"
    }
  },
  "style": "simple"
}
```

**YAML Definition:**
```yaml
name: token
in: header
description: token to be passed as a header
required: true
schema:
  type: array
  items:
    type: integer
    format: int64
style: simple
```

### Path Parameter (String)

This example defines a required path parameter named `username` of type string.

**JSON Definition:**
```json
{
  "name": "username",
  "in": "path",
  "description": "username to fetch",
  "required": true,
  "schema": {
    "type": "string"
  }
}
```

**YAML Definition:**
```yaml
name: username
in: path
description: username to fetch
required: true
schema:
  type: string
```

### Query Parameter (Array with Explode)

This example defines an optional query parameter named `id` which is an array of strings, using the `form` style and `explode: true` to allow multiple values for the same parameter name.

**JSON Definition:**
```json
{
  "name": "id",
  "in": "query",
  "description": "ID of the object to fetch",
  "required": false,
  "schema": {
    "type": "array",
    "items": {
      "type": "string"
    }
  },
  "style": "form",
  "explode": true
}
```

**YAML Definition:**
```yaml
name: id
in: query
description: ID of the object to fetch
required: false
schema:
  type: array
  items:
    type: string
style: form
explode: true
```

### Query Parameter (Free-form Object)

This example defines a query parameter named `freeForm` that accepts an object with additional string properties, using the `form` style.

**JSON Definition:**
```json
{
  "in": "query",
  "name": "freeForm",
  "schema": {
    "type": "object",
    "additionalProperties": {
      "type": "integer"
    }
  },
  "style": "form"
}
```

**YAML Definition:**
```yaml
in: query
name: freeForm
schema:
  type: object
  additionalProperties:
    type: integer
style: form
```

### Query Parameter (Complex Content-based)

This example defines a query parameter named `coordinates` that uses `content` to specify its structure when the `application/json` media type is used. It expects an object with `lat` and `long` properties.

**JSON Definition:**
```json
{
  "in": "query",
  "name": "coordinates",
  "content": {
    "application/json": {
      "schema": {
        "type": "object",
        "required": [
          "lat",
          "long"
        ],
        "properties": {
          "lat": {
            "type": "number"
          },
          "long": {
            "type": "number"
          }
        }
      }
    }
  }
}
```

**YAML Definition:**
```yaml
in: query
name: coordinates
content:
  application/json:
    schema:
      type: object
      required:
        - lat
        - long
      properties:
        lat:
          type: number
        long:
          type: number
```

### Request Body Object

Describes a single request body. This is a placeholder for documentation related to request body definitions.
```

--------------------------------

### Example Mypy Configuration (`mypy.ini`)

Source: https://mypy.readthedocs.io/en/stable/config_file.html

An example `mypy.ini` file demonstrating global and per-module configuration options. This file can be placed at the root of a repository to customize Mypy's behavior. It shows how to set options like `warn_return_any` globally and override or set specific options for modules like `mycode.foo.*`, `mycode.bar`, and `somelibrary`.

```ini
# Global options:
[mypy]
warn_return_any = True
warn_unused_configs = True

# Per-module options:
[mypy-mycode.foo.*]
disallow_untyped_defs = True
[mypy-mycode.bar]
warn_return_any = False
[mypy-somelibrary]
ignore_missing_imports = True

```

--------------------------------

### Install Lambda-Compatible Wheels (x86_64)

Source: https://docs.aws.amazon.com/lambda/latest/dg/python-package.html

Installs a pre-compiled wheel distribution compatible with the Lambda x86_64 execution environment into a 'package' directory. Requires specifying the platform, Python version, and ensuring binary-only installation. Use for libraries with C/C++ extensions.

```bash
pip install \
 --platform manylinux2014_x86_64 \
 --target=package \
 --implementation cp \
 --python-version 3.x \
 --only-binary=:all: --upgrade \
```

--------------------------------

### Ensure Pyrefly Installation with mason-lspconfig in Neovim

Source: https://pyrefly.org/en/docs/IDE

Demonstrates how to ensure Pyrefly is installed by adding it to the 'ensure_installed' option within the mason-lspconfig setup in Neovim. This method automatically installs Pyrefly if it's missing.

```lua
require("mason-lspconfig").setup {
  ensure_installed = { "pyrefly" },
}
```

--------------------------------

### Install AWS Lambda Runtime Interface Emulator

Source: https://docs.aws.amazon.com/lambda/latest/dg/python-image.html

Instructions to download and install the AWS Lambda Runtime Interface Emulator for both x86-64 and arm64 architectures on Linux/macOS and Windows PowerShell.

```APIDOC
## Install AWS Lambda Runtime Interface Emulator

This section provides instructions for installing the AWS Lambda Runtime Interface Emulator on your local machine.

### Linux/macOS

To install the x86-64 emulator:
```bash
mkdir -p ~/.aws-lambda-rie && \
curl -Lo ~/.aws-lambda-rie/aws-lambda-rie https://github.com/aws/aws-lambda-runtime-interface-emulator/releases/latest/download/aws-lambda-rie && \
chmod +x ~/.aws-lambda-rie/aws-lambda-rie
```

To install the arm64 emulator, replace the GitHub repository URL with:
```bash
https://github.com/aws/aws-lambda-runtime-interface-emulator/releases/latest/download/aws-lambda-rie-arm64
```

### PowerShell

To install the x86-64 emulator:
```powershell
$dirPath = "$HOME\.aws-lambda-rie"
if (-not (Test-Path $dirPath)) {
    New-Item -Path $dirPath -ItemType Directory
}
$downloadLink = "https://github.com/aws/aws-lambda-runtime-interface-emulator/releases/latest/download/aws-lambda-rie"
$destinationPath = "$HOME\.aws-lambda-rie\aws-lambda-rie"
Invoke-WebRequest -Uri $downloadLink -OutFile $destinationPath
```

To install the arm64 emulator, replace the `$downloadLink` with:
```powershell
https://github.com/aws/aws-lambda-runtime-interface-emulator/releases/latest/download/aws-lambda-rie-arm64
```
```

--------------------------------

### Sphinx Project Configuration Example (Python)

Source: https://www.sphinx-doc.org/en/master/usage/configuration.html

An example configuration file (conf.py) for a Sphinx project. It demonstrates how to set project information (name, copyright, author, version), general configuration (exclude patterns, extensions, language, master document, pygments style, source suffix, template path), and HTML output options (theme, static path).

```Python
# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information
project = 'Test Project'
copyright = '2000-2042, The Test Project Authors'
author = 'The Authors'
version = release = '4.16'

# -- General configuration --------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
exclude_patterns = [ '_build', 'Thumbs.db', '.DS_Store', ]
extensions = []
language = 'en'
master_doc = 'index'
pygments_style = 'sphinx'
source_suffix = '.rst'
templates_path = ['_templates']

# -- Options for HTML output ----------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output
html_theme = 'alabaster'
html_static_path = ['_static']
```

--------------------------------

### Python Timedelta Arithmetic Examples

Source: https://docs.python.org/library/datetime.html

Provides examples of `timedelta` arithmetic, including creating a `timedelta` representing ten years, subtracting a year to get nine years, and performing floor division by 3 to get three years. It shows the resulting `timedelta` objects and their day components.

```python
from datetime import timedelta
year = timedelta(days=365)
ten_years = 10 * year
nine_years = ten_years - year
three_years = nine_years // 3

print(f'ten_years: {ten_years}')
print(f'ten_years.days // 365: {ten_years.days // 365}')
print(f'nine_years: {nine_years}')
print(f'three_years: {three_years}')
print(f'three_years.days // 365: {three_years.days // 365}')
```

--------------------------------

### Install HTTPX with CLI Support (bash)

Source: https://www.python-httpx.org/

This command installs HTTPX along with its command-line interface (CLI) client. The CLI allows users to make HTTP requests directly from their terminal.

```bash
pip install 'httpx[cli]'
```

--------------------------------

### Request Body Examples

Source: https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.1.0

Demonstrates how to provide examples for request bodies in different content types.

```APIDOC
## Request Body Examples

This section illustrates how to include examples for request bodies in an API. Examples can be provided for various media types, such as JSON, XML, and plain text.

### JSON Examples
For JSON request bodies, you can define multiple examples with summaries.

```json
requestBody:
  content:
    'application/json':
      schema:
        $ref: '#/components/schemas/Address'
      examples:
        foo:
          summary: A foo example
          value: {"foo": "bar"}
        bar:
          summary: A bar example
          value: {"bar": "baz"}
```

### XML Example
An example for an XML request body can be provided using an `externalValue` reference.

```yaml
requestBody:
  content:
    'application/xml':
      examples:
        xmlExample:
          summary: This is an example in XML
          externalValue: 'https://example.org/examples/address-example.xml'
```

### Plain Text Example
Similarly, a plain text example can be referenced externally.

```yaml
requestBody:
  content:
    'text/plain':
      examples:
        textExample:
          summary: This is a text example
          externalValue: 'https://foo.bar/examples/address-example.txt'
```
```

--------------------------------

### Install python-dotenv

Source: https://saurabh-kumar.com/python-dotenv

Installs the python-dotenv library using pip. This is the first step to using the library in your Python project.

```bash
pip install python-dotenv
```

--------------------------------

### Install Pyrefly with Pixi

Source: https://pyrefly.org/en/docs/installation

Adds Pyrefly using pixi, initializes the project configuration, and runs a type check with error summarization.

```bash
pixi add pyrefly
pixi run pyrefly init
pixi run pyrefly check --summarize-errors
```

--------------------------------

### Path Parameter Example (String)

Source: https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.1.0

Example of a path parameter named 'username' which is a string.

```APIDOC
## Path Parameter Example (String)

### Description
A path parameter of a string value.

### Method
Any

### Endpoint
N/A

### Parameters
#### Path Parameters
- **username** (string) - Required - username to fetch

### Request Example
```yaml
name: username
in: path
description: username to fetch
required: true
schema:
  type: string
```

### Response
#### Success Response (200)
N/A

#### Response Example
N/A
```

--------------------------------

### Example JSON Configuration for Build System

Source: https://peps.python.org/pep-0518

This JSON snippet illustrates a basic configuration for a build system, specifying required packages. JSON was considered but rejected due to verbosity and lack of comment support.

```json
{
  "build": {
    "requires": [
      "setuptools",
      "wheel>=0.27"
    ]
  }
}
```

--------------------------------

### Install email-validator using pip

Source: https://github.com/JoshData/python-email-validator

This command installs the email-validator library from PyPI. You might need to use 'pip3' depending on your Python environment setup.

```bash
pip install email-validator

```

--------------------------------

### Install mkdocstrings-python Handler (pip)

Source: https://mkdocstrings.github.io/

Installs the mkdocstrings-python handler directly using pip. This provides more control over the version of the Python handler.

```bash
pip install mkdocstrings-python
```

--------------------------------

### Configure MkDocs Plugins with Options

Source: https://www.mkdocs.org/user-guide/configuration

Lists plugins to be used during site building, including optional configuration settings. Example shows enabling 'search' and 'your_other_plugin' with specific options for the latter.

```yaml
plugins:
  - search
  - your_other_plugin:
      option1: value
      option2: other value
```

--------------------------------

### Install NumPy Package - Cross-Platform Bash/Command Line

Source: https://code.visualstudio.com/docs/python/python-tutorial

These commands are used to install the NumPy package in a Python virtual environment. The specific command varies based on the operating system (macOS, Windows, Linux). Note that Anaconda distributions typically include NumPy, so this installation is primarily for non-Anaconda environments or specific setups.

```bash
# Don't use with Anaconda distributions because they include matplotlib already.
# macOS
python3 -m pip install numpy

# Windows (may require elevation)
py -m pip install numpy

# Linux (Debian)
apt-get install python3-tk
python3 -m pip install numpy
```

--------------------------------

### Example Object Definition and Usage

Source: https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.2

Defines the structure of an Example Object, which can be used to provide literal examples or external references for API schema values. It outlines the 'summary', 'description', 'value', and 'externalValue' fields.

```yaml
schemas:
  properties:
    name:
      type: string
      examples:
        name:
          $ref: http://example.org/petapi-examples/openapi.json#/components/examples/name-example

```

```yaml
requestBody:
  content:
    'application/json':
      schema:
        $ref: '#/components/schemas/Address'
      examples:
        foo:
          summary: A foo example
          value: {"foo": "bar"}
        bar:
          summary: A bar example
          value: {"bar": "baz"}
    'application/xml':
      examples:
        xmlExample:
          summary: This is an example in XML
          externalValue: 'http://example.org/examples/address-example.xml'
    'text/plain':
      examples:
        textExample:
          summary: This is a text example
          externalValue: 'http://foo.bar/examples/address-example.txt'

```

```yaml
parameters:
  - name: 'zipCode'
    in: 'query'
    schema:
      type: 'string'
      format: 'zip-code'
      examples:
        zip-example:
          $ref: '#/components/examples/zip-example'

```

```yaml
responses:
  '200':
    description: your car appointment has been booked
    content:
      application/json:
        schema:
          $ref: '#/components/schemas/SuccessResponse'
        examples:
          confirmation-success:
            $ref: '#/components/examples/confirmation-success'

```

--------------------------------

### License Object Examples

Source: https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.1.0

Defines license information for an API. Key fields are 'name' and either 'identifier' (SPDX expression) or 'url'. Examples are shown in JSON and YAML.

```json
{
  "name": "Apache 2.0",
  "identifier": "Apache-2.0"
}
```

```yaml
name: Apache 2.0
identifier: Apache-2.0
```

--------------------------------

### OpenAPI Path Item Object Example (YAML)

Source: https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.1.0

This YAML object represents an OpenAPI Path Item Object, equivalent to the JSON example, for defining an API endpoint to find pets by ID. It details the GET operation, parameters, and responses.

```yaml
get:
  description: Returns pets based on ID
  summary: Find pets by ID
  operationId: getPetsById
  responses:
    '200':
      description: pet response
      content:
        '*/*' :
          schema:
            type: array
            items:
              $ref: '#/components/schemas/Pet'
    default:
      description: error payload
      content:
        'text/html':
          schema:
            $ref: '#/components/schemas/ErrorModel'
parameters:
- name: id
  in: path
  description: ID of pet to use
  required: true
  schema:
    type: array
    items:
      type: string 
  style: simple

```

--------------------------------

### Example Object

Source: https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.1.0

Defines examples for API requests and responses, including literal values and external references.

```APIDOC
## Example Object

### Description
Provides examples for API request and response data. It can include a short summary, a detailed description, a literal value, or a URI pointing to an external example.

### Fixed Fields

- **summary** (string) - Short description for the example.
- **description** (string) - Long description for the example. CommonMark syntax MAY be used.
- **value** (Any) - Embedded literal example. Mutually exclusive with `externalValue`.
- **externalValue** (string) - A URI that points to the literal example. Mutually exclusive with `value`.
```

--------------------------------

### Run RabbitMQ Docker Image

Source: https://www.rabbitmq.com/download.html

This command allows you to run the latest RabbitMQ 4.x version with management UI enabled using Docker. It exposes ports 5672 for AMQP and 15672 for the management UI. Ensure Docker is installed and running on your system.

```docker
# latest RabbitMQ 4.x
docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:4-management
```

--------------------------------

### Multiple OpenAPI Servers Example (JSON)

Source: https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.2

A JSON example showing how to define multiple server objects within an OpenAPI document, typically in the 'servers' array.

```json
{
  "servers": [
    {
      "url": "https://development.gigantic-server.com/v1",
      "description": "Development server"
    },
    {
      "url": "https://staging.gigantic-server.com/v1",
      "description": "Staging server"
    },
    {
      "url": "https://api.gigantic-server.com/v1",
      "description": "Production server"
    }
  ]
}
```

--------------------------------

### Getting Match Indices with re.Match.start() and re.Match.end() in Python

Source: https://docs.python.org/3/library/re.html

Explains how to use the `start()` and `end()` methods of the re.Match object to retrieve the start and end indices of a substring matched by a specific group. The methods default to the entire match (group 0) and return -1 for groups that did not contribute to the match.

```python
import re

email = "tony@tiremove_thisger.net"
m = re.search("remove_this", email)
print(email[:m.start()] + email[m.end():])

```

--------------------------------

### Install datamodel-code-generator with GraphQL Extra

Source: https://koxudaxi.github.io/datamodel-code-generator

Installs the datamodel-code-generator package with the 'graphql' extra option. This enables the generation of data models from GraphQL schemas.

```bash
$ pip install 'datamodel-code-generator[graphql]'
```

--------------------------------

### OpenAPI Info Object Example (YAML)

Source: https://github.com/OAI/OpenAPI-Specification/blob/main/versions/3.1.0

An example of the Info Object in YAML format, demonstrating how API metadata can be represented.

```yaml
title: Sample Pet Store App
summary: A pet store manager.
description: This is a sample server for a pet store.
termsOfService: https://example.com/terms/
contact:
  name: API Support
  url: https://www.example.com/support
  email: support@example.com
license:
  name: Apache 2.0
  url: https://www.apache.org/licenses/LICENSE-2.0.html
version: 1.0.1
```

--------------------------------

### Parameter Styling Examples

Source: https://github.com/OAI/OpenAPI-Specification/blob/master/versions/3.0.2

Illustrates how different `style` and `explode` settings affect the serialization of string, array, and object parameters, providing concrete examples for each combination.

```APIDOC
## Parameter Style Examples

Assume a parameter named `color` with the following values:
* `string`: "blue"
* `array`: ["blue", "black", "brown"]
* `object`: { "R": 100, "G": 200, "B": 150 }

The following table shows examples of rendering differences based on `style` and `explode` settings:

| `style` | `explode` | `empty` | `string` | `array` | `object` |
|---|---|---|---|---|---|
| matrix | false | ;color | ;color=blue | ;color=blue,black,brown | ;color=R,100,G,200,B,150 |
| matrix | true | ;color | ;color=blue | ;color=blue;color=black;color=brown | ;R=100;G=200;B=150 |
| label | false | . | .blue | .blue.black.brown | .R.100.G.200.B.150 |
| label | true | . | .blue | .blue.black.brown | .R=100.G=200.B=150 |
| form | false | color= | color=blue | color=blue,black,brown | color=R,100,G,200,B,150 |
| form | true | color= | color=blue | color=blue&color=black&color=brown | R=100&G=200&B=150 |
| simple | false | n/a | blue | blue,black,brown | R,100,G,200,B,150 |
| simple | true | n/a | blue | blue,black,brown | R=100,G=200,B=150 |
| spaceDelimited | false | n/a | n/a | blue%20black%20brown | R%20100%20G%20200%20B%20150 |
| pipeDelimited | false | n/a | n/a | blue%7Cblack%7Cbrown | R%7C100%7CG%7C200 |
| deepObject | true | n/a | n/a | n/a | color[R]=100&color[G]=200&color[B]=150
```

--------------------------------

### ISO 8601 Repeating Intervals Example

Source: https://en.wikipedia.org/wiki/ISO_8601

Demonstrates how to represent repeating time intervals in ISO 8601 format. It specifies the number of repetitions, a start time, and the duration of each interval.

```text
R5/2008-03-01T13:00:00Z/P1Y2M10DT2H30M
```

--------------------------------

### Rich REPL Integration

Source: https://github.com/willmcgugan/rich

Shows how to install Rich's pretty-printing capabilities into the Python REPL. Once installed, all data structures printed in the REPL will be automatically formatted and highlighted.

```python
from rich import pretty
pretty.install()
```

--------------------------------

### Install serverless-python-requirements Plugin

Source: https://github.com/serverless/serverless-python-requirements/tree/master

Command to install the serverless-python-requirements plugin. This command automatically adds the plugin to your project's package.json and the plugins section of serverless.yml.

```bash
sls plugin install -n serverless-python-requirements
```

--------------------------------

### Mypy pyproject.toml Configuration Example

Source: https://mypy.readthedocs.io/en/stable/config_file.html

An example of a pyproject.toml file used for Mypy configuration. It demonstrates setting global options, per-module overrides for strictness, and excluding files. Strings require appropriate quoting and escaping.

```toml
[tool.mypy]
python_version = "3.9"
warn_return_any = true
warn_unused_configs = true
exclude = [
  '^file1\.py$', 
  '^file2\\.py$', 
]

[[tool.mypy.overrides]]
module = "mycode.foo.*"
disallow_untyped_defs = true

[[tool.mypy.overrides]]
module = "mycode.bar"
warn_return_any = false

[[tool.mypy.overrides]]
module = [
  "somelibrary",
  "some_other_library"
]
ignore_missing_imports = true
```

--------------------------------

### Reference Count Example

Source: https://docs.python.org/3/glossary.html

Demonstrates how to get the reference count of an object using `sys.getrefcount()`. This function helps in understanding memory management, though reference counts can vary.

```Python
import sys

x = []
print(sys.getrefcount(x))
```

--------------------------------

### Override Pyrefly LSP Config Command in Neovim

Source: https://pyrefly.org/en/docs/IDE

Example of overriding the default command used to run Pyrefly within Neovim's LSP configuration. This is useful for specifying alternative executables, such as those installed via uv.

```lua
vim.lsp.config('pyrefly', {
  -- example of how to run `uv` installed Pyrefly without adding to your path
  cmd = { 'uvx', 'pyrefly', 'lsp' }
})
```

--------------------------------

### Example mypy.ini Configuration

Source: https://mypy.readthedocs.io/en/latest/config_file.html

An example mypy.ini file demonstrating global and per-module configuration options. Global options apply to all checks, while per-module options override global settings for specific modules or packages. This helps in customizing type checking behavior.

```ini
# Global options:
[mypy]
warn_return_any = True
warn_unused_configs = True

# Per-module options:
[mypy-mycode.foo.*]
disallow_untyped_defs = True
[mypy-mycode.bar]
warn_return_any = False
[mypy-somelibrary]
ignore_missing_imports = True
```