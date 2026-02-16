### Create a deep agent for research using LangChain

Source: https://docs.langchain.com/oss/javascript/deepagents/quickstart

This TypeScript snippet demonstrates how to initialize a deep agent using `createDeepAgent` from the `deepagents` library. It configures the agent with the previously defined `internetSearch` tool and a `systemPrompt` that guides its behavior as an expert researcher. This setup provides the agent with its core capabilities and initial instructions.

```typescript
import { createDeepAgent } from "deepagents";

// System prompt to steer the agent to be an expert researcher
const researchInstructions = `You are an expert researcher. Your job is to conduct thorough research and then write a polished report.

You have access to an internet search tool as your primary means of gathering information.

## \`internet_search\`

Use this to run an internet search for a given query. You can specify the max number of results to return, the topic, and whether raw content should be included.
`;

const agent = createDeepAgent({
  tools: [internetSearch],
  systemPrompt: researchInstructions,
});
```

--------------------------------

### GET /v2/auth/setup/{provider_id}

Source: https://docs.langchain.com/api-reference/auth-service-v2/oauth-setup-callback

Handles the OAuth setup callback redirect from GitHub Apps. This endpoint processes new installations with code/state and shows a success page for updates, as no token exchange is needed.

```APIDOC
## GET /v2/auth/setup/{provider_id}

### Description
Handle OAuth setup callback redirect from GitHub Apps.

This endpoint handles the "Setup URL" callback from GitHub Apps, which is
triggered when a user installs or updates their GitHub App installation.

For "update" actions (user modified repo access via GitHub), we just show
a success page since no token exchange is needed.

For new installations with code/state, we process similar to the regular
OAuth callback.

### Method
GET

### Endpoint
/v2/auth/setup/{provider_id}

### Parameters
#### Path Parameters
- **provider_id** (string) - Required - Provider Id

#### Query Parameters
- **code** (string) - Optional - Authorization code from OAuth provider
- **state** (string) - Optional - State parameter containing auth_id
- **setup_action** (string) - Optional - Setup action from GitHub App
- **installation_id** (integer) - Optional - GitHub App installation ID
- **error** (string) - Optional - Error code from OAuth provider
- **error_description** (string) - Optional - Error description from OAuth provider

### Response
#### Success Response (200)
- Successful Response

#### Response Example
{}
```

--------------------------------

### Full ClaudeBashToolMiddleware Configuration with Docker in Python

Source: https://docs.langchain.com/oss/python/integrations/middleware/anthropic

This example illustrates a comprehensive setup of `ClaudeBashToolMiddleware`, including the use of `DockerExecutionPolicy` for sandboxed command execution. It demonstrates creating a temporary workspace, defining startup commands, and invoking the agent to execute a bash command, showcasing how to get the result.

```python
import tempfile

from langchain_anthropic import ChatAnthropic
from langchain_anthropic.middleware import ClaudeBashToolMiddleware
from langchain.agents import create_agent
from langchain.agents.middleware import DockerExecutionPolicy

# Create a temporary workspace directory for this demo.
# In production, use a persistent directory path.
workspace = tempfile.mkdtemp(prefix="agent-workspace-")

agent = create_agent(
    model=ChatAnthropic(model="claude-sonnet-4-5-20250929"),
    tools=[],
    middleware=[ # [!code highlight]
        ClaudeBashToolMiddleware( # [!code highlight]
            workspace_root=workspace, # [!code highlight]
            startup_commands=["echo 'Session initialized'"], # [!code highlight]
            execution_policy=DockerExecutionPolicy( # [!code highlight]
                image="python:3.11-slim", # [!code highlight]
            ), # [!code highlight]
        ), # [!code highlight]
    ], # [!code highlight]
)

# Claude can now use its native bash tool
result = agent.invoke(
    {"messages": [{"role": "user", "content": "What version of Python is installed?"}]}
)
print(result["messages"][-1].content)
```

--------------------------------

### Install Elasticsearch Locally using start-local Script (Bash)

Source: https://docs.langchain.com/oss/python/integrations/providers/elasticsearch

These commands demonstrate how to set up a local Elasticsearch instance for development and testing using the `start-local` script. It covers initial download, starting the service, and an option for Elasticsearch-only setup. This method is not recommended for production environments.

```bash
curl -fsSL https://elastic.co/start-local | sh
```

```bash
cd elastic-start-local
./start.sh
```

```bash
curl -fsSL https://elastic.co/start-local | sh -s -- --esonly
```

--------------------------------

### Set up Project Directory and Install Dependencies (Bash)

Source: https://docs.langchain.com/langsmith/observability-quickstart

This snippet provides commands to create a new project directory and install the necessary dependencies for both Python and TypeScript environments. It includes setting up a Python virtual environment and installing `langsmith` and `openai` packages, as well as initializing an npm project and installing `langsmith`, `openai`, `typescript`, and `ts-node` for TypeScript.

```bash
mkdir ls-observability-quickstart && cd ls-observability-quickstart
python -m venv .venv && source .venv/bin/activate
python -m pip install --upgrade pip
pip install -U langsmith openai
```

```bash
mkdir ls-observability-quickstart-ts && cd ls-observability-quickstart-ts
npm init -y
npm install langsmith openai typescript ts-node
npx tsc --init
```

--------------------------------

### Example Usage of Get Assistant by ID in Python

Source: https://docs.langchain.com/langsmith/smith-deployments-sdk

Illustrates how to call the `get` method of `SyncAssistantsClient` to fetch an assistant and print its details. This example shows a typical interaction and the expected JSON output.

```python
assistant = client.assistants.get(
    assistant_id="my_assistant_id"
)
print(assistant)
```

--------------------------------

### Install Debugpy and Start LangGraph Dev Server with Debugging

Source: https://docs.langchain.com/langsmith/quick-start-studio

This snippet shows how to install the `debugpy` package using pip or uv, and then start the LangGraph development server with a specified debug port (e.g., 5678). This enables step-by-step debugging with breakpoints and variable inspection for your local application.

```bash
# Install debugpy package
pip install debugpy
# Start server with debugging enabled
langgraph dev --debug-port 5678
```

```bash
# Install debugpy package
uv add debugpy
# Start server with debugging enabled
langgraph dev --debug-port 5678
```

--------------------------------

### Install Deep Agent Dependencies (Bash)

Source: https://docs.langchain.com/oss/python/deepagents/quickstart

This snippet provides commands to install the necessary Python packages, `deepagents` and `tavily-python`, for developing deep agents. It includes options for both `pip` and `uv` package managers.

```bash
pip install deepagents tavily-python
```

```bash
uv init
uv add deepagents tavily-python
uv sync
```

--------------------------------

### Initialize Modal Account Setup

Source: https://docs.langchain.com/langsmith/webhooks

This command initiates the setup process for your Modal account. It guides the user through the necessary steps to configure their local environment and link it with their Modal account, enabling deployment of Modal applications and services.

```shell
modal setup
```

--------------------------------

### Install LangGraph CLI and Start Local Agent Server

Source: https://docs.langchain.com/langsmith/quick-start-studio

This snippet demonstrates how to install the LangGraph CLI using different package managers (pip, uv, npm) and start the local Agent Server in development mode. The server runs in-memory, watches for code changes, and automatically restarts, providing a local environment for LangSmith Studio.

```bash
pip install -U "langgraph-cli[inmem]"
langgraph dev
```

```bash
uv add "langgraph-cli[inmem]"
langgraph dev
```

```bash
npx @langchain/langgraph-cli dev
```

--------------------------------

### Clone and Setup LangChain Documentation Repository

Source: https://docs.langchain.com/oss/javascript/contributing/documentation

Initialize a local development environment for LangChain documentation by cloning the repository and installing dependencies. This sets up the necessary tools and starts a development server with hot reload capability at localhost:3000.

```bash
git clone https://github.com/langchain-ai/docs.git
```

```bash
cd docs
```

```bash
make install
```

```bash
make dev
```

--------------------------------

### Install `langgraph-cli` with in-memory extra and start `langgraph dev` server

Source: https://docs.langchain.com/langsmith/local-dev-testing

This command sequence first installs the `langgraph-cli` tool, ensuring the `inmem` extra is included for local development. It then starts the `langgraph dev` server, which runs directly in your environment, offering hot reloading and fast startup for iterative development cycles.

```bash
pip install -U "langgraph-cli[inmem]"
langgraph dev
```

--------------------------------

### Run LangGraph Development Server

Source: https://docs.langchain.com/langsmith/set-up-custom-auth

This snippet shows how to install local project dependencies and start the LangGraph development server. It covers different package managers (`pip`, `uv`, `npm`) to get the project running. The server provides API endpoints, a Studio UI link, and API documentation for local development and testing.

```bash
pip install -e .
langgraph dev
```

```bash
uv add .
langgraph dev
```

```bash
npx @langchain/langgraph-cli dev
```

--------------------------------

### Get Assistant Schemas - Python Usage Example

Source: https://docs.langchain.com/langsmith/smith-deployments-sdk

Demonstrates how to instantiate a sync client and retrieve the schema for an assistant. The example connects to a local LangGraph server and prints the returned schema object.

```python
client = get_sync_client(url="http://localhost:2024")
schema = client.assistants.get_schemas(
    assistant_id="my_assistant_id"
)
print(schema)
```

--------------------------------

### Install Deep Agents and LangChain dependencies

Source: https://docs.langchain.com/oss/javascript/deepagents/quickstart

This snippet provides commands to install the necessary packages for building deep agents, including `deepagents`, `langchain`, `@langchain/core`, and `@langchain/tavily`. It covers `npm`, `yarn`, and `pnpm` package managers. These dependencies are crucial for agent functionality and integrating with search providers like Tavily.

```bash
npm install deepagents langchain @langchain/core @langchain/tavily
```

```bash
yarn add deepagents langchain @langchain/core @langchain/tavily
```

```bash
pnpm add deepagents langchain @langchain/core @langchain/tavily
```

--------------------------------

### Create Basic Agent with LangChain and Claude

Source: https://docs.langchain.com/oss/python/langchain/quickstart

Creates a simple AI agent using LangChain that leverages Claude Sonnet 4.5 as the language model and includes a weather tool. The agent accepts user messages and can invoke tools to answer questions. Requires LangChain package installation and ANTHROPIC_API_KEY environment variable setup.

```python
from langchain.agents import create_agent

def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_agent(
    model="claude-sonnet-4-5-20250929",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

# Run the agent
agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather in sf"}]}
)
```

--------------------------------

### Instantiate Deep Agent with Research Instructions (Python)

Source: https://docs.langchain.com/oss/python/deepagents/quickstart

This Python snippet demonstrates how to create a deep agent using the `create_deep_agent` function. It configures the agent with the `internet_search` tool and a detailed system prompt, guiding it to act as an expert researcher capable of thorough investigation and report writing.

```python
# System prompt to steer the agent to be an expert researcher
research_instructions = """You are an expert researcher. Your job is to conduct thorough research and then write a polished report.

You have access to an internet search tool as your primary means of gathering information.

## `internet_search`

Use this to run an internet search for a given query. You can specify the max number of results to return, the topic, and whether raw content should be included.
"""

agent = create_deep_agent(
    tools=[internet_search],
    system_prompt=research_instructions
)
```

--------------------------------

### Example Output for Get Assistant by ID in JSON

Source: https://docs.langchain.com/langsmith/smith-deployments-sdk

Provides an example of the JSON structure returned when retrieving an assistant using the `get` method. It includes fields like `assistant_id`, `graph_id`, timestamps, configuration, context, and metadata.

```json
{
    'assistant_id': 'my_assistant_id',
    'graph_id': 'agent',
    'created_at': '2024-06-25T17:10:33.109781+00:00',
    'updated_at': '2024-06-25T17:10:33.109781+00:00',
    'config': {},
    'context': {},
    'metadata': {'created_by': 'system'}
}
```

--------------------------------

### GET /examples

Source: https://docs.langchain.com/langsmith/manage-datasets-programmatically

Retrieves a list of examples from the LangChain system. This endpoint supports filtering by specific example IDs, dataset name, exact metadata matches, or complex structured metadata queries.

```APIDOC
## GET /examples

### Description
Retrieves a list of examples from the LangChain system. This endpoint supports filtering by specific example IDs, dataset name, exact metadata matches, or complex structured metadata queries.

### Method
GET

### Endpoint
/examples

### Parameters
#### Query Parameters
- **ids** (array of string) - Optional - A comma-separated list of example IDs to retrieve. Example: `?ids=id1,id2,id3`
- **dataset_name** (string) - Optional - Filters examples belonging to a specific dataset by its name.
- **metadata** (object) - Optional - A URL-encoded JSON object for filtering examples by exact metadata key-value matches. For example, to filter by `{"foo": "bar"}`, the query parameter would be `?metadata=%7B%22foo%22%3A%22bar%22%7D`.
- **filter** (string) - Optional - A structured query string for advanced filtering on metadata fields. This supports operators like `has`, `exists`, `and`, `not`. Example: `?filter=and(not(has(metadata, '{"foo": "bar"}')), exists(metadata, "tenant_id"))`

### Request Example
(No request body for GET requests)

### Response
#### Success Response (200)
- **examples** (array of object) - A list of example objects matching the specified criteria. Each object includes details such as `id`, `dataset_id`, `name`, `metadata`, `inputs`, and `outputs`.

#### Response Example
```json
[
  {
    "id": "734fc6a0-c187-4266-9721-90b7a025751a",
    "dataset_id": "some-dataset-id",
    "name": "Example 1",
    "metadata": {
      "foo": "bar",
      "tenant_id": "abc-123"
    },
    "inputs": {
      "query": "What is LangChain?"
    },
    "outputs": {
      "answer": "LangChain is a framework for developing applications powered by language models."
    }
  },
  {
    "id": "d6b4c1b9-6160-4d63-9b61-b034c585074f",
    "dataset_id": "some-dataset-id",
    "name": "Example 2",
    "metadata": {
      "baz": "qux"
    },
    "inputs": {
      "query": "How to use LangChain?"
    },
    "outputs": {
      "answer": "You can use LangChain to chain together various components to build complex LLM applications."
    }
  }
]
```
```

--------------------------------

### Define a Conversational AI Agent with LangChain and LangGraph

Source: https://docs.langchain.com/oss/python/langchain/quickstart

This comprehensive Python snippet illustrates the complete setup of an AI agent using LangChain and LangGraph. It covers defining a system prompt, custom context, tool functions (`get_weather_for_location`, `get_user_location`), configuring a chat model, specifying a structured response format (`ResponseFormat`), setting up an in-memory checkpointer for conversation state, and finally creating the agent. This agent is designed to act as a punny weather forecaster, leveraging tools and user context.

```python
from dataclasses import dataclass

from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain.tools import tool, ToolRuntime
from langgraph.checkpoint.memory import InMemorySaver
from langchain.agents.structured_output import ToolStrategy


# Define system prompt
SYSTEM_PROMPT = """You are an expert weather forecaster, who speaks in puns.

You have access to two tools:

- get_weather_for_location: use this to get the weather for a specific location
- get_user_location: use this to get the user's location

If a user asks you for the weather, make sure you know the location. If you can tell from the question that they mean wherever they are, use the get_user_location tool to find their location."""

# Define context schema
@dataclass
class Context:
    """Custom runtime context schema."""
    user_id: str

# Define tools
@tool
def get_weather_for_location(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

@tool
def get_user_location(runtime: ToolRuntime[Context]) -> str:
    """Retrieve user information based on user ID."""
    user_id = runtime.context.user_id
    return "Florida" if user_id == "1" else "SF"

# Configure model
model = init_chat_model(
    "claude-sonnet-4-5-20250929",
    temperature=0
)

# Define response format
@dataclass
class ResponseFormat:
    """Response schema for the agent."""
    # A punny response (always required)
    punny_response: str
    # Any interesting information about the weather if available
    weather_conditions: str | None = None

# Set up memory
checkpointer = InMemorySaver()

# Create agent
agent = create_agent(
    model=model,
    system_prompt=SYSTEM_PROMPT,
    tools=[get_user_location, get_weather_for_location],
    context_schema=Context,
    response_format=ToolStrategy(ResponseFormat),
    checkpointer=checkpointer
)
```

--------------------------------

### Installation and Setup

Source: https://docs.langchain.com/oss/python/integrations/document_loaders/surrealdb

Instructions for installing the necessary Python packages to use the SurrealDB integration with LangChain.

```APIDOC
## Installation

### Description
Install the required Python libraries for SurrealDB integration with LangChain using pip.

### Method
PACKAGE INSTALLATION

### Endpoint
N/A

### Parameters
N/A

### Request Example
```python
pip install -qU  surrealdb langchain langchain-community
```

### Response
#### Success Response
Successful installation of packages.

#### Response Example
```text
Successfully installed surrealdb-x.y.z langchain-x.y.z langchain-community-x.y.z
```
```

--------------------------------

### BigQuery Callback Handler Setup Example

Source: https://docs.langchain.com/oss/python/integrations/callbacks/google_bigquery

Complete code example demonstrating how to configure and initialize the BigQuery callback handler with custom content formatting, event filtering, and logging parameters.

```APIDOC
## BigQueryCallbackHandler Initialization

### Description
Initialize and configure the BigQuery callback handler with custom settings including event filtering, content formatting, and batch processing.

### Method
POST (Configuration)

### Setup Steps

#### Step 1: Define Custom Content Formatter
```python
import json
import re
from typing import Any

def redact_dollar_amounts(event_content: Any) -> str:
    """
    Custom formatter to redact dollar amounts (e.g., $600, $12.50)
    and ensure JSON output if the input is a dict.
    """
    text_content = ""
    # If the content is a dictionary (e.g., a list of messages), convert it to a JSON string first.
    if isinstance(event_content, dict):
        text_content = json.dumps(event_content)
    else:
        text_content = str(event_content)

    # Regex to find dollar amounts: $ followed by digits, optionally with commas or decimals.
    # Examples: $600, $1,200.50, $0.99
    redacted_content = re.sub(r'\$\d+(?:,\d{3})*(?:\.\d+)?', 'xxx', text_content)

    return redacted_content
```

#### Step 2: Configure BigQueryLoggerConfig
```python
from langchain_google_community.callbacks.bigquery_callback import (
    BigQueryCallbackHandler,
    BigQueryLoggerConfig
)

config = BigQueryLoggerConfig(
    enabled=True,
    event_allowlist=["LLM_REQUEST", "LLM_RESPONSE"],
    shutdown_timeout=10.0,
    max_content_length=500,
    content_formatter=redact_dollar_amounts
)
```

#### Step 3: Initialize the Callback Handler
```python
handler = BigQueryCallbackHandler(
    project_id="your-project-id",
    dataset_id="your_dataset",
    table_id="your_table",
    config=config
)
```

### Configuration Details

#### Parameters
- **project_id** (str) - Required - Your Google Cloud project ID
- **dataset_id** (str) - Required - The BigQuery dataset ID
- **table_id** (str) - Required - The BigQuery table ID
- **config** (BigQueryLoggerConfig) - Required - Configuration object with logging settings

#### Config Settings Used
- **enabled**: True - Enable logging to BigQuery
- **event_allowlist**: ["LLM_REQUEST", "LLM_RESPONSE"] - Only log these specific event types
- **shutdown_timeout**: 10.0 - Wait up to 10 seconds for logs to flush on exit
- **max_content_length**: 500 - Truncate content to 500 characters
- **content_formatter**: redact_dollar_amounts - Apply custom formatting function to redact sensitive data

### Usage
Once initialized, pass the `handler` to your LangChain agent or chain callbacks to automatically log events to BigQuery with the specified configuration.
```

--------------------------------

### Local Development and Deployment Instructions for FastAPI Service

Source: https://docs.langchain.com/langsmith/prompt-commit

These instructions provide the necessary steps to set up and run the FastAPI service locally, including installing Python dependencies, configuring environment variables in a `.env` file, and starting the Uvicorn server. It also suggests deployment to public platforms like Render.com.

```shell
  # To run this server (save as main.py):
  # 1. Install dependencies: pip install fastapi uvicorn pydantic pydantic-settings httpx python-dotenv
  # 2. Create a .env file with your GitHub token and repo details.
  # 3. Run with Uvicorn: uvicorn main:app --reload
  # 4. Deploy to a public platform like Render.com.
```

--------------------------------

### Start SurrealDB Locally

Source: https://docs.langchain.com/oss/python/integrations/vectorstores/surrealdb

Start a SurrealDB instance locally in-memory mode with default root credentials. This is the quickest way to get started with SurrealDB for development and testing purposes.

```bash
surreal start -u root -p root
```

--------------------------------

### Define System Prompt for Agent Behavior

Source: https://docs.langchain.com/oss/python/langchain/quickstart

Create a detailed system prompt that defines the agent's role, behavior, and available tools. This prompt guides the model on how to interact with users and which tools to use for specific tasks.

```python
SYSTEM_PROMPT = """You are an expert weather forecaster, who speaks in puns.

You have access to two tools:

- get_weather_for_location: use this to get the weather for a specific location
- get_user_location: use this to get the user's location

If a user asks you for the weather, make sure you know the location. If you can tell from the question that they mean wherever they are, use the get_user_location tool to find their location."""
```

--------------------------------

### Install Langsmith and OpenAI Dependencies for Vitest

Source: https://docs.langchain.com/langsmith/vitest-jest

Instructions for installing `langsmith` and `openai` as production dependencies. These are required for running LangChain evaluation examples with Vitest.

```bash
yarn add langsmith openai
```

```bash
npm install langsmith openai
```

```bash
pnpm add langsmith openai
```

--------------------------------

### Install OpenAI embeddings provider

Source: https://docs.langchain.com/oss/python/integrations/providers/zeusdb

Install the langchain-openai package to use OpenAI embeddings with ZeusDB. This is required for the quick start examples that use OpenAIEmbeddings.

```bash
pip install langchain-openai
```

--------------------------------

### Invoke Agent and Display Results

Source: https://docs.langchain.com/oss/python/langgraph/quickstart

Demonstrates how to invoke the agent with a human message and iterate through streamed results. Uses pretty_print() to display message outputs in a readable format.

```python
from langchain.messages import HumanMessage


messages = [HumanMessage(content="Add 3 and 4.")]
messages = agent.invoke({"messages": messages})
for m in messages["messages"]:
    m.pretty_print()
```

--------------------------------

### Define and Bind Arithmetic Tools for LangChain LLM

Source: https://docs.langchain.com/oss/python/langgraph/quickstart

This Python snippet defines a basic `divide` function as an example arithmetic tool. It then demonstrates how to collect a list of such tools (`add`, `multiply`, `divide`), create a dictionary mapping their names to the functions, and bind these tools to a LangChain Language Model (`model`) for tool-calling capabilities.

```python
def divide(a: int, b: int) -> float:
    """Divide `a` and `b`.

    Args:
        a: First int
        b: Second int
    """
    return a / b


# Augment the LLM with tools
tools = [add, multiply, divide]
tools_by_name = {tool.name: tool for tool in tools}
model_with_tools = model.bind_tools(tools)
```

--------------------------------

### Install LangGraph CLI with In-Memory Support

Source: https://docs.langchain.com/oss/python/langchain/sql-agent

Install the LangGraph CLI package with in-memory support for running agents in Studio. This is a prerequisite for the optional Studio setup.

```shell
pip install -U langgraph-cli[inmem]>=0.4.0
```

--------------------------------

### Start of an End-to-End Example in Python

Source: https://docs.langchain.com/oss/python/integrations/document_loaders/docling

This snippet marks the beginning of an end-to-end example, importing the `os` module. The full example would typically include setup, loading, processing, and potentially saving or further utilizing the documents within a LangChain application.

```python
import os
```

--------------------------------

### Create a Bash Script for Remote Sandbox Environment Setup

Source: https://docs.langchain.com/oss/javascript/deepagents/cli

This example provides a `setup.sh` script to configure a remote sandbox. It includes steps for cloning a Git repository, navigating into it, and making environment variables persistent across sessions. Secrets like API keys should be stored in a local `.env` file for the script to access.

```bash
#!/bin/bash
set -e

# Clone repository using GitHub token
git clone https://x-access-token:${GITHUB_TOKEN}@github.com/username/repo.git $HOME/workspace
cd $HOME/workspace

# Make environment variables persistent
cat >> ~/.bashrc <<'EOF'
export GITHUB_TOKEN="${GITHUB_TOKEN}"
export OPENAI_API_KEY="${OPENAI_API_KEY}"
cd $HOME/workspace
EOF

source ~/.bashrc
```

--------------------------------

### Install LangChain v1 and Core Packages

Source: https://docs.langchain.com/oss/javascript/releases/langchain-v1

These commands demonstrate how to install the `langchain` and `@langchain/core` packages using various package managers. This is the essential first step to upgrading an existing project or starting a new one with LangChain v1.

```bash
npm install langchain @langchain/core
```

```bash
pnpm install langchain @langchain/core
```

```bash
yarn add langchain @langchain/core
```

```bash
bun add langchain @langchain/core
```

--------------------------------

### Install LangSmith Tool Server and LangChain CLI

Source: https://docs.langchain.com/langsmith/agent-builder-mcp-framework

Install the required packages to get started with the LangSmith Tool Server and LangChain CLI tools. These packages provide the foundation for building and serving custom toolkits.

```bash
pip install langsmith-tool-server
pip install langchain-cli-v2
```

--------------------------------

### Full Context Editing Configuration Example

Source: https://docs.langchain.com/oss/javascript/langchain/middleware/built-in

Complete example demonstrating context editing middleware with multiple tools and all configuration options. This setup monitors token count, clears older tool outputs when reaching 2000 tokens, preserves the 3 most recent results, and uses a placeholder for cleared content.

```typescript
import { createAgent, contextEditingMiddleware, ClearToolUsesEdit } from "langchain";

const agent = createAgent({
  model: "gpt-4.1",
  tools: [searchTool, calculatorTool, databaseTool],
  middleware: [
    contextEditingMiddleware({
      edits: [
        new ClearToolUsesEdit({
          triggerTokens: 2000,
          keep: 3,
          clearToolInputs: false,
          excludeTools: [],
          placeholder: "[cleared]",
        }),
      ],
    }),
  ],
});
```

--------------------------------

### Build and Compile LangGraph Agent with Nodes and Edges

Source: https://docs.langchain.com/oss/python/langgraph/quickstart

Constructs a StateGraph agent by adding LLM and tool nodes, defining edges for workflow routing, and compiling into an executable agent. The agent uses conditional edges to determine whether to invoke tools or terminate based on LLM output.

```python
agent_builder.add_node("llm_call", llm_call)
agent_builder.add_node("tool_node", tool_node)

# Add edges to connect nodes
agent_builder.add_edge(START, "llm_call")
agent_builder.add_conditional_edges(
    "llm_call",
    should_continue,
    ["tool_node", END]
)
agent_builder.add_edge("tool_node", "llm_call")

# Compile the agent
agent = agent_builder.compile()
```

--------------------------------

### Instantiate `SyncLangGraphClient` (Python)

Source: https://docs.langchain.com/langsmith/smith-deployments-sdk

This example demonstrates how to initialize a top-level synchronous LangGraphClient instance by providing the API URL. Once instantiated, the client can be used to access various sub-clients (e.g., assistants, threads) to interact with the LangGraph API. This setup allows for making synchronous calls to the API.

```python
from langgraph_sdk import get_sync_client

# get top-level synchronous LangGraphClient
client = get_sync_client(url="http://localhost:8123")

# example usage: client.<model>.<method_name>()
assistant = client.assistants.get(assistant_id="some_uuid")
```

--------------------------------

### Install Graph RAG Example Helpers Package

Source: https://docs.langchain.com/oss/python/integrations/retrievers/graph_rag

Install the graph_rag_example_helpers package which provides sample data and datasets for testing and learning Graph RAG functionality with example documents.

```bash
pip install -qU graph_rag_example_helpers
```

--------------------------------

### Set up API keys for Anthropic and Tavily

Source: https://docs.langchain.com/oss/javascript/deepagents/quickstart

This snippet shows how to set environment variables for `ANTHROPIC_API_KEY` and `TAVILY_API_KEY`. These keys are required for authenticating with model providers (e.g., Anthropic) and search services (e.g., Tavily) that the deep agent will utilize. Replace 'your-api-key' and 'your-tavily-api-key' with your actual credentials.

```bash
export ANTHROPIC_API_KEY="your-api-key"
export TAVILY_API_KEY="your-tavily-api-key"
```

--------------------------------

### Full filesystem-based text editor agent example with temporary workspace

Source: https://docs.langchain.com/oss/python/integrations/middleware/anthropic

Complete example demonstrating a filesystem-based text editor agent using a temporary workspace directory. Shows production-ready pattern with tempfile for demo purposes and persistent directory path recommendation.

```python
import tempfile

from langchain_anthropic import ChatAnthropic
from langchain_anthropic.middleware import FilesystemClaudeTextEditorMiddleware
from langchain.agents import create_agent


# Create a temporary workspace directory for this demo.
# In production, use a persistent directory path.
workspace = tempfile.mkdtemp(prefix="editor-workspace-")

agent = create_agent(
    model=ChatAnthropic(model="claude-sonnet-4-5-20250929"),
    tools=[],
    middleware=[
```

--------------------------------

### Install OpenGradient SDK and Initialize Configuration

Source: https://docs.langchain.com/oss/python/integrations/providers/opengradient

Install the OpenGradient SDK package and initialize a new configuration to set up API credentials. Run these commands if you need to create a new API key or configure OpenGradient for the first time.

```bash
pip install opengradient
opengradient config init
```

--------------------------------

### Install Dedoc Library with pip

Source: https://docs.langchain.com/oss/python/integrations/providers/dedoc

Install the Dedoc library using pip package manager. This installation method requires additional dependencies as documented in the Dedoc installation guide.

```bash
pip install dedoc
```

--------------------------------

### Create and Run Weather Forecasting Agent

Source: https://docs.langchain.com/oss/python/langchain/quickstart

Assemble the complete agent with all components including model, system prompt, tools, context schema, response format, and checkpointer. Execute the agent with a user query and thread ID for conversation tracking.

```python
from langchain.agents.structured_output import ToolStrategy

agent = create_agent(
    model=model,
    system_prompt=SYSTEM_PROMPT,
    tools=[get_user_location, get_weather_for_location],
    context_schema=Context,
    response_format=ToolStrategy(ResponseFormat),
    checkpointer=checkpointer
)

# `thread_id` is a unique identifier for a given conversation.
config = {"configurable": {"thread_id": "1"}}

response = agent.invoke(
    {"messages": [{"role": "user", "content": "what is the weather outside?"}]},
    config=config,
    context=Context(user_id="1")
)

print(response['structured_response'])
```

--------------------------------

### Illustrate Gradle Project Directory Structure

Source: https://docs.langchain.com/langsmith/setup-java

This example outlines a basic directory structure for a Gradle-based Java application. It highlights the location of the `build.gradle.kts` file, which is where project dependencies and build configurations are typically defined.

```bash
my-app/
└── build.gradle.kts # Gradle dependencies
```

--------------------------------

### Create an internet search tool with LangChain and Tavily

Source: https://docs.langchain.com/oss/javascript/deepagents/quickstart

This TypeScript snippet defines an `internetSearch` tool using LangChain's `tool` utility and `TavilySearch`. It allows the agent to perform web searches with configurable parameters like query, max results, topic, and raw content inclusion. The tool relies on the `TAVILY_API_KEY` environment variable for authentication and uses Zod for schema validation of its inputs.

```typescript
import { tool } from "langchain";
import { TavilySearch } from "@langchain/tavily";
import { z } from "zod";

const internetSearch = tool(
  async ({
    query,
    maxResults = 5,
    topic = "general",
    includeRawContent = false,
  }: {
    query: string;
    maxResults?: number;
    topic?: "general" | "news" | "finance";
    includeRawContent?: boolean;
  }) => {
    const tavilySearch = new TavilySearch({
      maxResults,
      tavilyApiKey: process.env.TAVILY_API_KEY,
      includeRawContent,
      topic,
    });
    return await tavilySearch._call({ query });
  },
  {
    name: "internet_search",
    description: "Run a web search",
    schema: z.object({
      query: z.string().describe("The search query"),
      maxResults: z
        .number()
        .optional()
        .default(5)
        .describe("Maximum number of results to return"),
      topic: z
        .enum(["general", "news", "finance"])
        .optional()
        .default("general")
        .describe("Search topic category"),
      includeRawContent: z
        .boolean()
        .optional()
        .default(false)
        .describe("Whether to include raw content"),
    }),
  },
);
```

--------------------------------

### Start `langgraph up` with full stack recreation for pre-deployment validation

Source: https://docs.langchain.com/langsmith/local-dev-testing

This command starts the `langgraph up` server and forces a complete recreation of its Docker-based stack. This is crucial for pre-deployment validation, as it ensures that all dependencies are correctly installed and the application builds successfully in a fresh, isolated containerized environment, catching potential build or dependency resolution issues.

```bash
langgraph up --recreate
```

--------------------------------

### Install LangGraph CLI for Studio Agent Setup

Source: https://docs.langchain.com/oss/javascript/langchain/sql-agent

This command globally installs the `langgraph-cli` package, which is essential for running and managing LangGraph agents within the LangSmith Studio environment. It provides the command-line interface needed for project setup and execution.

```shell
npm i -g langgraph-cli@latest
```

--------------------------------

### Install and Initialize HuggingFace Chat Model with LangChain

Source: https://docs.langchain.com/oss/python/langchain/multi-agent/subagents-personal-assistant

This snippet demonstrates how to install the LangChain HuggingFace integration and initialize a HuggingFace chat model. It provides examples for both the `init_chat_model` utility function and direct instantiation of the `ChatHuggingFace` class. A `HUGGINGFACEHUB_API_TOKEN` environment variable is required for authentication. Note that the direct class instantiation example is incomplete in the provided text.

```shell
pip install -U "langchain[huggingface]"
```

```python
import os
from langchain.chat_models import init_chat_model

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "hf_..."

model = init_chat_model(
    "microsoft/Phi-3-mini-4k-instruct",
    model_provider="huggingface",
    temperature=0.7,
    max_tokens=1024,
)
```

```python
import os
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "hf_..."

llm = HuggingFaceEndpoint(
```

--------------------------------

### Install langchain-agentql package

Source: https://docs.langchain.com/oss/python/integrations/tools/agentql

Install the langchain-agentql package using pip with quiet and upgrade flags to get the latest version.

```python
pip install --quiet -U langchain-agentql
```

--------------------------------

### Initialize Chat Model and Bind Tools

Source: https://docs.langchain.com/oss/python/langgraph/quickstart

Initializes a Claude chat model with specified temperature and binds the arithmetic tools to enable tool calling. Creates a tools dictionary for lookup during tool execution.

```python
from langchain.tools import tool
from langchain.chat_models import init_chat_model

model = init_chat_model(
    "claude-sonnet-4-5-20250929",
    temperature=0
)

tools = [add, multiply, divide]
tools_by_name = {tool.name: tool for tool in tools}
model_with_tools = model.bind_tools(tools)
```

--------------------------------

### Install LangGraph and Dependencies

Source: https://docs.langchain.com/oss/python/langgraph/use-time-travel

Install required packages for building LangGraph workflows with Anthropic LLM integration. This command installs langchain_core, langchain-anthropic, and langgraph libraries needed for the time-travel example.

```bash
pip install langchain_core langchain-anthropic langgraph
```

--------------------------------

### Example .env configuration for Supabase credentials

Source: https://docs.langchain.com/langsmith/add-auth-server

Illustrates the expected content of the `.env` file after adding the Supabase project URL and service role key. This provides a clear reference for verifying the environment variable setup.

```bash
SUPABASE_URL=your-project-url
SUPABASE_SERVICE_KEY=your-service-role-key
```

--------------------------------

### Setting up ManticoreSearch Docker container and columnar library (Python)

Source: https://docs.langchain.com/oss/python/integrations/vectorstores/manticore_search

This Python script automates the setup of a ManticoreSearch Docker container. It checks for an existing container, starts one if necessary, waits for it to become ready, and then installs the 'manticore-columnar-lib' package inside the container. This package is essential for enabling vector search functionality in ManticoreSearch.

```python
import time

# Start container
containers = !docker ps --filter "name=langchain-manticoresearch-server" -q
if len(containers) == 0:
    !docker run -d -p 9308:9308 --name langchain-manticoresearch-server manticoresearch/manticore:dev
    time.sleep(20)  # Wait for the container to start up

# Get ID of container
container_id = containers[0]

# Install manticore-columnar-lib package as root user
!docker exec -it --user 0 {container_id} apt-get update
!docker exec -it --user 0 {container_id} apt-get install -y manticore-columnar-lib
```

--------------------------------

### Define Agent Entrypoint with Control Flow

Source: https://docs.langchain.com/oss/python/langgraph/quickstart

Creates the main agent function using @entrypoint decorator that orchestrates the interaction between LLM and tools. Implements a loop that continues until the model stops requesting tool calls, handling message aggregation and streaming.

```python
from langgraph.func import entrypoint
from langgraph.graph import add_messages
from langchain.messages import HumanMessage


@entrypoint()
def agent(messages: list[BaseMessage]):
    model_response = call_llm(messages).result()

    while True:
        if not model_response.tool_calls:
            break

        # Execute tools
        tool_result_futures = [
            call_tool(tool_call) for tool_call in model_response.tool_calls
        ]
        tool_results = [fut.result() for fut in tool_result_futures]
        messages = add_messages(messages, [model_response, *tool_results])
        model_response = call_llm(messages).result()

    messages = add_messages(messages, model_response)
    return messages


# Invoke
messages = [HumanMessage(content="Add 3 and 4.")]
for chunk in agent.stream(messages, stream_mode="updates"):
    print(chunk)
    print("\n")
```

--------------------------------

### Example Output of Computer Use Tool

Source: https://docs.langchain.com/oss/python/integrations/chat/google_generative_ai

This snippet provides an example of the structured `tool_call` output generated by the `computer_use` tool. It illustrates how the model's instruction to 'navigate to example.com' is translated into a `tool_call` with the name `open_web_browser` and its associated arguments. This output helps in understanding the model's interaction with the browser environment.

```text
[{'type': 'tool_call',
  'id': '08a8b175-16ab-4861-8965-b736d5d4dd7e',
  'name': 'open_web_browser',
  'args': {}}]
```

--------------------------------

### Install @langchain/classic package with bun

Source: https://docs.langchain.com/oss/javascript/migrate/langchain-v1

Install the @langchain/classic package using bun package manager for legacy LangChain functionality.

```bash
bun add @langchain/classic
```

--------------------------------

### Install and Initialize OpenAI Chat Model with LangChain

Source: https://docs.langchain.com/oss/python/langchain/multi-agent/subagents-personal-assistant

This snippet demonstrates how to install the LangChain OpenAI integration and initialize an OpenAI chat model. It provides examples for both the `init_chat_model` utility function and direct instantiation of the `ChatOpenAI` class. An `OPENAI_API_KEY` environment variable is required for authentication.

```shell
pip install -U "langchain[openai]"
```

```python
import os
from langchain.chat_models import init_chat_model

os.environ["OPENAI_API_KEY"] = "sk-..."

model = init_chat_model("gpt-4.1")
```

```python
import os
from langchain_openai import ChatOpenAI

os.environ["OPENAI_API_KEY"] = "sk-..."

model = ChatOpenAI(model="gpt-4.1")
```

--------------------------------

### Start Milvus Server with Docker

Source: https://docs.langchain.com/oss/python/integrations/vectorstores/milvus

Download and start a Milvus Standalone server using Docker. This setup is recommended for production deployments with large datasets (over a million vectors) and provides access to advanced indexing options.

```python
!curl -sfL https://raw.githubusercontent.com/milvus-io/milvus/master/scripts/standalone_embed.sh -o standalone_embed.sh

!bash standalone_embed.sh start
```

--------------------------------

### Install @langchain/classic package with yarn

Source: https://docs.langchain.com/oss/javascript/migrate/langchain-v1

Install the @langchain/classic package using yarn package manager for legacy LangChain functionality.

```bash
yarn add @langchain/classic
```

--------------------------------

### Invoke a deep agent with a user query

Source: https://docs.langchain.com/oss/javascript/deepagents/quickstart

This TypeScript snippet shows how to execute the created deep agent by invoking its `invoke` method with a user message. It then prints the agent's final response to the console. This demonstrates the agent's ability to process a query, utilize its tools, and generate an output.

```typescript
const result = await agent.invoke({
  messages: [{ role: "user", content: "What is langgraph?" }],
});

// Print the agent's response
console.log(result.messages[result.messages.length - 1].content);
```

--------------------------------

### Implement Minimal RAG Application with OpenAI (Python/TypeScript)

Source: https://docs.langchain.com/langsmith/observability-quickstart

This code defines a minimal Retrieval-Augmented Generation (RAG) application. It includes a simple retriever function that returns a fixed document, instantiates an OpenAI client, and a RAG function that combines retrieved documents with a user's question to form a system prompt for the OpenAI chat completion API. The application uses 'gpt-4.1-mini' and demonstrates direct OpenAI SDK usage without any tracing setup. It takes a user question as input and returns the assistant's generated response.

```python
from openai import OpenAI

def retriever(query: str):
    # Minimal example retriever
    return ["Harrison worked at Kensho"]

# OpenAI client call (no wrapping yet)
client = OpenAI()

def rag(question: str) -> str:
    docs = retriever(question)
    system_message = (
        "Answer the user's question using only the provided information below:\n"
        + "\n".join(docs)
    )

    # This call is not traced yet
    resp = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": system_message},
            {"role": "user", "content": question},
        ],
    )
    return resp.choices[0].message.content

if __name__ == "__main__":
    print(rag("Where did Harrison work?"))
```

```typescript
import "dotenv/config";
import OpenAI from "openai";

// Minimal example retriever
function retriever(query: string): string[] {
    return ["Harrison worked at Kensho"];
}

// OpenAI client call (no wrapping yet)
const client = new OpenAI();

async function rag(question: string) {
    const docs = retriever(question);
    const systemMessage =
        "Answer the user's question using only the provided information below:\n" +
        docs.join("\n");

    // This call is not traced yet
    const resp = await client.chat.completions.create({
        model: "gpt-4.1-mini",
        messages: [
            { role: "system", content: systemMessage },
            { role: "user", content: question },
        ],
    });

    return resp.choices[0].message?.content;
}

(async () => {
  console.log(await rag("Where did Harrison work?"));
})();
```

--------------------------------

### Install @langchain/classic package with pnpm

Source: https://docs.langchain.com/oss/javascript/migrate/langchain-v1

Install the @langchain/classic package using pnpm package manager for legacy LangChain functionality.

```bash
pnpm install @langchain/classic
```

--------------------------------

### Install Modal SDK using pip or uv

Source: https://docs.langchain.com/langsmith/webhooks

These commands demonstrate how to install the Modal SDK, a prerequisite for developing applications with Modal. You can choose between `pip` for standard Python package management or `uv` for an alternative, potentially faster, installer, depending on your environment and preference.

```bash
pip install modal
```

```bash
uv add modal
```

--------------------------------

### Create Agent with Memory and Tools

Source: https://docs.langchain.com/oss/javascript/langchain/quickstart

Initialize the agent with the model, system prompt, tools, response format, and a memory checkpointer. The MemorySaver enables conversation persistence across multiple invocations using thread IDs.

```typescript
import { createAgent } from "langchain";
import { MemorySaver } from "@langchain/langgraph";

const checkpointer = new MemorySaver();

const agent = createAgent({
  model,
  systemPrompt,
  responseFormat,
  checkpointer,
  tools: [getUserLocation, getWeather],
});
```

--------------------------------

### Install Required Dependencies for LangChain Integration

Source: https://docs.langchain.com/oss/python/integrations/chat/anthropic

Bash command to install required Python packages for the end-to-end example. Installs langchain-openai for OpenAI model integration and numpy for numerical operations.

```bash
pip install langchain-openai numpy
```

--------------------------------

### Enter SyncLangGraphClient Context Manager (Python)

Source: https://docs.langchain.com/langsmith/smith-deployments-sdk

This Python method defines the entry point for the `SyncLangGraphClient` when used as a context manager. It allows the client to set up necessary resources upon entering a `with` statement, returning an instance of `SyncLangGraphClient` for use within the context.

```python
__enter__() -> SyncLangGraphClient
```