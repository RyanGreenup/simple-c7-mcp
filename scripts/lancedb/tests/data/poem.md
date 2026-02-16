# Poem Framework

Poem is a full-featured web framework for Rust that emphasizes both ease of use and high performance. Built on async/await and the Tokio runtime, it provides a type-safe, ergonomic API for building web applications and services. The framework is designed to minimize the use of generics, making it more approachable while maintaining blazing fast performance and flexible routing capabilities.

The project consists of multiple components working together: the core Poem web framework for HTTP server functionality, Poem-OpenAPI for type-safe OpenAPI v3 specification compliance with automatic documentation generation, Poem-gRPC for high-performance RPC services, Poem-MCP for implementing Model Context Protocol servers, and Poem-Lambda for deploying Poem applications on AWS Lambda. All crates are written in 100% safe Rust with `#![forbid(unsafe_code)]` and support seamless integration with Tower middleware ecosystem.

## Core Framework - HTTP Server

Basic HTTP server with routing and handlers

```rust
use poem::{get, handler, listener::TcpListener, web::Path, Route, Server};

#[handler]
fn hello(Path(name): Path<String>) -> String {
    format!("hello: {}", name)
}

#[tokio::main]
async fn main() -> Result<(), std::io::Error> {
    let app = Route::new().at("/hello/:name", get(hello));
    Server::new(TcpListener::bind("0.0.0.0:3000"))
        .run(app)
        .await
}

// Test:
// curl http://localhost:3000/hello/world
// Returns: "hello: world"
```

## State Management with AddData Middleware

Sharing application state across handlers

```rust
use std::{
    collections::HashMap,
    sync::{Arc, Mutex},
};
use poem::{
    get, handler, listener::TcpListener, middleware::AddData,
    web::{Data, Path}, EndpointExt, Route, Server,
};

struct AppState {
    clients: Mutex<HashMap<String, String>>,
}

#[handler]
fn set_state(Path(name): Path<String>, state: Data<&Arc<AppState>>) -> String {
    let mut store = state.clients.lock().unwrap();
    store.insert(name.to_string(), "some state object".to_string());
    "store updated".to_string()
}

#[handler]
fn get_state(Path(name): Path<String>, state: Data<&Arc<AppState>>) -> String {
    let store = state.clients.lock().unwrap();
    let message = store.get(&name).unwrap();
    message.to_string()
}

#[tokio::main]
async fn main() -> Result<(), std::io::Error> {
    let state = Arc::new(AppState {
        clients: Mutex::new(HashMap::new()),
    });

    let app = Route::new()
        .at("/hello/:name", get(set_state))
        .at("/:name", get(get_state))
        .with(AddData::new(state));

    Server::new(TcpListener::bind("0.0.0.0:3000"))
        .run(app)
        .await
}

// Test:
// curl http://localhost:3000/hello/john
// curl http://localhost:3000/john
// Returns: "some state object"
```

## Custom Middleware Implementation

Creating reusable middleware for logging or other cross-cutting concerns

```rust
use poem::{
    get, handler, listener::TcpListener, Endpoint, EndpointExt,
    IntoResponse, Middleware, Request, Response, Result, Route, Server,
};

struct Log;

impl<E: Endpoint> Middleware<E> for Log {
    type Output = LogImpl<E>;

    fn transform(&self, ep: E) -> Self::Output {
        LogImpl(ep)
    }
}

struct LogImpl<E>(E);

impl<E: Endpoint> Endpoint for LogImpl<E> {
    type Output = Response;

    async fn call(&self, req: Request) -> Result<Self::Output> {
        println!("request: {}", req.uri().path());
        let res = self.0.call(req).await;

        match res {
            Ok(resp) => {
                let resp = resp.into_response();
                println!("response: {}", resp.status());
                Ok(resp)
            }
            Err(err) => {
                println!("error: {err}");
                Err(err)
            }
        }
    }
}

#[handler]
fn index() -> String {
    "hello".to_string()
}

#[tokio::main]
async fn main() -> Result<(), std::io::Error> {
    let app = Route::new().at("/", get(index)).with(Log);
    Server::new(TcpListener::bind("0.0.0.0:3000"))
        .run(app)
        .await
}

// Output logs request path and response status to console
```

## WebSocket Server

Real-time bidirectional communication with WebSocket

```rust
use futures_util::{SinkExt, StreamExt};
use poem::{
    get, handler, listener::TcpListener,
    web::{websocket::{Message, WebSocket}, Data, Path},
    EndpointExt, IntoResponse, Route, Server,
};

#[handler]
fn ws(
    Path(name): Path<String>,
    ws: WebSocket,
    sender: Data<&tokio::sync::broadcast::Sender<String>>,
) -> impl IntoResponse {
    let sender = sender.clone();
    let mut receiver = sender.subscribe();
    ws.on_upgrade(move |socket| async move {
        let (mut sink, mut stream) = socket.split();

        tokio::spawn(async move {
            while let Some(Ok(msg)) = stream.next().await {
                if let Message::Text(text) = msg {
                    if sender.send(format!("{name}: {text}")).is_err() {
                        break;
                    }
                }
            }
        });

        tokio::spawn(async move {
            while let Ok(msg) = receiver.recv().await {
                if sink.send(Message::Text(msg)).await.is_err() {
                    break;
                }
            }
        });
    })
}

#[tokio::main]
async fn main() -> Result<(), std::io::Error> {
    let app = Route::new().at(
        "/ws/:name",
        get(ws.data(tokio::sync::broadcast::channel::<String>(32).0)),
    );
    Server::new(TcpListener::bind("0.0.0.0:3000"))
        .run(app)
        .await
}

// Connect with: ws://127.0.0.1:3000/ws/username
// Messages are broadcast to all connected clients
```

## OpenAPI - Simple REST API

Type-safe OpenAPI v3 compliant API with automatic documentation

```rust
use poem::{listener::TcpListener, Route};
use poem_openapi::{param::Query, payload::PlainText, OpenApi, OpenApiService};

struct Api;

#[OpenApi]
impl Api {
    #[oai(path = "/hello", method = "get")]
    async fn index(&self, name: Query<Option<String>>) -> PlainText<String> {
        match name.0 {
            Some(name) => PlainText(format!("hello, {}!", name)),
            None => PlainText("hello!".to_string()),
        }
    }
}

#[tokio::main]
async fn main() -> Result<(), std::io::Error> {
    let api_service = OpenApiService::new(Api, "Hello World", "1.0")
        .server("http://localhost:3000/api");
    let ui = api_service.swagger_ui();
    let app = Route::new().nest("/api", api_service).nest("/", ui);

    poem::Server::new(TcpListener::bind("0.0.0.0:3000"))
        .run(app)
        .await
}

// Test:
// curl http://localhost:3000/api/hello
// curl http://localhost:3000/api/hello?name=sunli
// Swagger UI: http://localhost:3000/
```

## OpenAPI - CRUD Operations with Database

Complete RESTful API with database integration

```rust
use poem::{
    error::InternalServerError, listener::TcpListener,
    middleware::Cors, web::Data, EndpointExt, Result, Route, Server,
};
use poem_openapi::{
    param::Path, payload::{Json, PlainText},
    ApiResponse, Object, OpenApi, OpenApiService,
};

type DbPool = sqlx::SqlitePool;

#[derive(Object)]
struct Todo {
    id: i64,
    description: String,
    done: bool,
}

#[derive(Object)]
struct UpdateTodo {
    description: Option<String>,
    done: Option<bool>,
}

#[derive(ApiResponse)]
enum GetResponse {
    #[oai(status = 200)]
    Todo(Json<Todo>),
    #[oai(status = 404)]
    NotFound(PlainText<String>),
}

struct TodosApi;

#[OpenApi]
impl TodosApi {
    #[oai(path = "/todos", method = "post")]
    async fn create(
        &self,
        pool: Data<&DbPool>,
        description: PlainText<String>,
    ) -> Result<Json<i64>> {
        let id = sqlx::query("insert into todos (description) values (?)")
            .bind(description.0)
            .execute(pool.0)
            .await
            .map_err(InternalServerError)?
            .last_insert_rowid();
        Ok(Json(id))
    }

    #[oai(path = "/todos/:id", method = "get")]
    async fn get(&self, pool: Data<&DbPool>, id: Path<i64>) -> Result<GetResponse> {
        let todo: Option<(i64, String, bool)> =
            sqlx::query_as("select id, description, done from todos where id = ?")
                .bind(id.0)
                .fetch_optional(pool.0)
                .await
                .map_err(InternalServerError)?;

        match todo {
            Some(todo) => Ok(GetResponse::Todo(Json(Todo {
                id: todo.0,
                description: todo.1,
                done: todo.2,
            }))),
            None => Ok(GetResponse::NotFound(PlainText(format!(
                "todo `{}` not found", id.0
            )))),
        }
    }

    #[oai(path = "/todos/:id", method = "delete")]
    async fn delete(&self, pool: Data<&DbPool>, id: Path<i64>) -> Result<()> {
        sqlx::query("delete from todos where id = ?")
            .bind(id.0)
            .execute(pool.0)
            .await
            .map_err(InternalServerError)?;
        Ok(())
    }
}

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let pool = DbPool::connect("sqlite:todos.db").await?;
    let api_service = OpenApiService::new(TodosApi, "Todos", "1.0.0")
        .server("http://localhost:3000");
    let ui = api_service.swagger_ui();

    let route = Route::new()
        .nest("/", api_service)
        .nest("/ui", ui)
        .with(Cors::new())
        .data(pool);

    Server::new(TcpListener::bind("0.0.0.0:3000"))
        .run(route)
        .await?;
    Ok(())
}

// Test:
// curl -X POST http://localhost:3000/todos -d "Buy milk"
// curl http://localhost:3000/todos/1
// curl -X DELETE http://localhost:3000/todos/1
```

## OpenAPI - API Key Authentication

Secure endpoints with JWT-based API key authentication

```rust
use hmac::{Hmac, NewMac};
use jwt::{SignWithKey, VerifyWithKey};
use poem::{
    error::InternalServerError, listener::TcpListener,
    web::Data, EndpointExt, Request, Result, Route,
};
use poem_openapi::{
    auth::ApiKey, payload::{Json, PlainText},
    Object, OpenApi, OpenApiService, SecurityScheme,
};
use serde::{Deserialize, Serialize};
use sha2::Sha256;

const SERVER_KEY: &[u8] = b"123456";
type ServerKey = Hmac<Sha256>;

#[derive(Debug, Serialize, Deserialize)]
struct User {
    username: String,
}

#[derive(SecurityScheme)]
#[oai(
    ty = "api_key",
    key_name = "X-API-Key",
    key_in = "header",
    checker = "api_checker"
)]
struct MyApiKeyAuthorization(User);

async fn api_checker(req: &Request, api_key: ApiKey) -> Option<User> {
    let server_key = req.data::<ServerKey>().unwrap();
    VerifyWithKey::<User>::verify_with_key(api_key.key.as_str(), server_key).ok()
}

#[derive(Object)]
struct LoginRequest {
    username: String,
}

struct Api;

#[OpenApi]
impl Api {
    #[oai(path = "/login", method = "post")]
    async fn login(
        &self,
        server_key: Data<&ServerKey>,
        req: Json<LoginRequest>,
    ) -> Result<PlainText<String>> {
        let token = User { username: req.0.username }
            .sign_with_key(server_key.0)
            .map_err(InternalServerError)?;
        Ok(PlainText(token))
    }

    #[oai(path = "/hello", method = "get")]
    async fn hello(&self, auth: MyApiKeyAuthorization) -> PlainText<String> {
        PlainText(auth.0.username)
    }
}

#[tokio::main]
async fn main() -> Result<(), std::io::Error> {
    let api_service = OpenApiService::new(Api, "Authorization Demo", "1.0")
        .server("http://localhost:3000/api");
    let ui = api_service.swagger_ui();
    let server_key = Hmac::<Sha256>::new_from_slice(SERVER_KEY).expect("valid server key");

    let app = Route::new()
        .nest("/api", api_service)
        .nest("/", ui)
        .data(server_key);

    poem::Server::new(TcpListener::bind("0.0.0.0:3000"))
        .run(app)
        .await
}

// Test:
// TOKEN=$(curl -X POST http://localhost:3000/api/login -H "Content-Type: application/json" -d '{"username":"alice"}')
// curl http://localhost:3000/api/hello -H "X-API-Key: $TOKEN"
// Returns: "alice"
```

## gRPC Server

High-performance RPC services with Protocol Buffers

```rust
use poem::{listener::TcpListener, Server};
use poem_grpc::{Request, Response, RouteGrpc, Status};

poem_grpc::include_proto!("helloworld");

struct GreeterService;

impl Greeter for GreeterService {
    async fn say_hello(
        &self,
        request: Request<HelloRequest>,
    ) -> Result<Response<HelloReply>, Status> {
        let reply = HelloReply {
            message: format!("Hello {}!", request.into_inner().name),
        };
        Ok(Response::new(reply))
    }
}

#[tokio::main]
async fn main() -> Result<(), std::io::Error> {
    let route = RouteGrpc::new().add_service(GreeterServer::new(GreeterService));
    Server::new(TcpListener::bind("0.0.0.0:3000"))
        .run(route)
        .await
}

// Requires helloworld.proto:
// syntax = "proto3";
// package helloworld;
// service Greeter {
//   rpc SayHello (HelloRequest) returns (HelloReply);
// }
// message HelloRequest { string name = 1; }
// message HelloReply { string message = 1; }
```

## MCP Server Implementation

Model Context Protocol server for AI tool integration

```rust
use poem_mcpserver::{stdio::stdio, tool::Text, McpServer, Tools};

struct Counter {
    count: i32,
}

#[Tools]
impl Counter {
    /// Increment the counter by 1
    async fn increment(&mut self) -> Text<i32> {
        self.count += 1;
        Text(self.count)
    }

    /// Decrement the counter by 1
    async fn decrement(&mut self) -> Text<i32> {
        self.count -= 1;
        Text(self.count)
    }

    /// Get the current counter value
    async fn get_value(&self) -> Text<i32> {
        Text(self.count)
    }
}

#[tokio::main]
async fn main() -> std::io::Result<()> {
    stdio(McpServer::new().tools(Counter { count: 0 })).await
}

// The MCP server communicates via stdio and provides tools to AI assistants
// Tools are automatically discovered and can be called with parameters
```

## AWS Lambda Integration

Deploy Poem handlers as AWS Lambda functions

```rust
use poem::handler;
use poem_lambda::Error;

#[handler]
fn index() -> &'static str {
    "hello"
}

#[tokio::main]
async fn main() -> Result<(), Error> {
    poem_lambda::run(index).await
}

// Deploy to AWS Lambda with cargo-lambda:
// cargo lambda build --release
// cargo lambda deploy
```

## Summary

Poem Framework provides a comprehensive solution for building web services in Rust, from simple HTTP APIs to complex distributed systems. The framework excels at type-safe API development through Poem-OpenAPI, which automatically generates OpenAPI v3 specifications and interactive documentation from Rust code. For real-time applications, the framework offers first-class WebSocket support with easy integration into the routing system. The middleware system is powerful yet simple, supporting both custom middleware and compatibility with the Tower ecosystem for reusable components across the Rust web landscape.

The framework's versatility extends to multiple deployment targets and protocols. Applications can be deployed as traditional HTTP servers, AWS Lambda functions, or gRPC services without significant code changes. The MCP Server component enables AI tool integration, making Poem suitable for modern AI-augmented applications. All components share the same async runtime and design principles, providing consistent error handling, request processing, and performance characteristics. With zero unsafe code, comprehensive examples, and active maintenance, Poem offers production-ready infrastructure for building scalable web services in Rust.
