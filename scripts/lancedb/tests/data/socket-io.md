### Socket.IO Server and Client Setup (Vitest - CommonJS)

Source: https://socket.io/docs/v4/testing

Sets up a Socket.IO server and client for testing using Vitest. It requires the 'vitest', 'node:http', and 'socket.io' packages. The setup listens for connections and resolves a promise once the client is connected.

```javascript
const { beforeAll, afterAll, describe, it, expect } = require("vitest");
const { createServer } = require("node:http");
const { Server } = require("socket.io");
const ioc = require("socket.io-client");

function waitFor(socket, event) {
  return new Promise((resolve) => {
    socket.once(event, resolve);
  });
}

describe("my awesome project", () => {
  let io, serverSocket, clientSocket;

  beforeAll(() => {
    return new Promise((resolve) => {
      const httpServer = createServer();
      io = new Server(httpServer);
      httpServer.listen(() => {
        const port = httpServer.address().port;
        clientSocket = ioc(`http://localhost:${port}`);
        io.on("connection", (socket) => {
          serverSocket = socket;
        });
        clientSocket.on("connect", resolve);
      });
    });
  });

  afterAll(() => {
    io.close();
    clientSocket.disconnect();
  });

  it("should work", () => {
    return new Promise((resolve) => {
      clientSocket.on("hello", (arg) => {
        expect(arg).toEqual("world");
        resolve();
      });
      serverSocket.emit("hello", "world");
    });
  });

  it("should work with an acknowledgement", () => {
    return new Promise((resolve) => {
      serverSocket.on("hi", (cb) => {
        cb("hola");
      });
      clientSocket.emit("hi", (arg) => {
        expect(arg).toEqual("hola");
        resolve();
      });
    });
  });

  it("should work with emitWithAck()", async () => {
    serverSocket.on("foo", (cb) => {
      cb("bar");
    });
    const result = await clientSocket.emitWithAck("foo");
    expect(result).toEqual("bar");
  });

  it("should work with waitFor()", () => {
    clientSocket.emit("baz");

    return waitFor(serverSocket, "baz");
  });
});

```

--------------------------------

### Socket.IO Server and Client Setup (Vitest - ES Modules)

Source: https://socket.io/docs/v4/testing

Sets up a Socket.IO server and client for testing using Vitest with ES module syntax. It requires the 'vitest', 'node:http', and 'socket.io' packages. The setup listens for connections and resolves a promise once the client is connected.

```javascript
import { beforeAll, afterAll, describe, it, expect } from "vitest";
import { createServer } from "node:http";
import { io as ioc } from "socket.io-client";
import { Server } from "socket.io";

function waitFor(socket, event) {
  return new Promise((resolve) => {
    socket.once(event, resolve);
  });
}

describe("my awesome project", () => {
  let io, serverSocket, clientSocket;

  beforeAll(() => {
    return new Promise((resolve) => {
      const httpServer = createServer();
      io = new Server(httpServer);
      httpServer.listen(() => {
        const port = httpServer.address().port;
        clientSocket = ioc(`http://localhost:${port}`);
        io.on("connection", (socket) => {
          serverSocket = socket;
        });
        clientSocket.on("connect", resolve);
      });
    });
  });

  afterAll(() => {
    io.close();
    clientSocket.disconnect();
  });

  it("should work", () => {
    return new Promise((resolve) => {
      clientSocket.on("hello", (arg) => {
        expect(arg).toEqual("world");
        resolve();
      });
      serverSocket.emit("hello", "world");
    });
  });

  it("should work with an acknowledgement", () => {
    return new Promise((resolve) => {
      serverSocket.on("hi", (cb) => {
        cb("hola");
      });
      clientSocket.emit("hi", (arg) => {
        expect(arg).toEqual("hola");
        resolve();
      });
    });
  });

  it("should work with emitWithAck()", async () => {
    serverSocket.on("foo", (cb) => {
      cb("bar");
    });

```

--------------------------------

### Socket.IO Setup and Teardown with Vitest

Source: https://socket.io/docs/v4/testing

This code block demonstrates the `beforeAll` and `afterAll` hooks in Vitest for setting up and tearing down the Socket.IO server and client instances. It includes creating an HTTP server, initializing Socket.IO, and establishing a client connection.

```typescript
import { beforeAll, afterAll, describe, it, expect } from "vitest";
import { createServer } from "node:http";
import { type AddressInfo } from "node:net";
import { io as ioc, type Socket as ClientSocket } from "socket.io-client";
import { Server, type Socket as ServerSocket } from "socket.io";

function waitFor(socket: ServerSocket | ClientSocket, event: string) {
  return new Promise((resolve) => {
    socket.once(event, resolve);
  });
}

describe("my awesome project", () => {
  let io: Server, serverSocket: ServerSocket, clientSocket: ClientSocket;

  beforeAll(() => {
    return new Promise((resolve) => {
      const httpServer = createServer();
      io = new Server(httpServer);
      httpServer.listen(() => {
        const port = (httpServer.address() as AddressInfo).port;
        clientSocket = ioc(`http://localhost:${port}`);
        io.on("connection", (socket) => {
          serverSocket = socket;
        });
        clientSocket.on("connect", resolve);
      });
    });
  });

  afterAll(() => {
    io.close();
    clientSocket.disconnect();
  });

  // ... test cases ...
});
```

--------------------------------

### Install Vitest for Testing

Source: https://socket.io/docs/v4/testing

This snippet shows how to install Vitest, a modern unit testing framework for Vite projects, as a development dependency using npm. It is essential for running the provided test suite.

```bash
npm install --save-dev vitest
```

--------------------------------

### Install Optional Performance Packages (NPM, Yarn, pnpm, Bun)

Source: https://socket.io/docs/v4/server-installation

Installs optional C++ add-ons (bufferutil and utf-8-validate) that can significantly improve the performance of WebSocket operations like data masking and UTF-8 validation. These packages provide prebuilt binaries for common platforms, reducing the need for a C++ compiler. If not installed, Socket.IO will fall back to its JavaScript implementation.

```bash
npm install --save-optional bufferutil utf-8-validate
```

```bash
yarn add --optional bufferutil utf-8-validate
```

```bash
pnpm add -O bufferutil utf-8-validate
```

```bash
bun add --optional bufferutil utf-8-validate
```

--------------------------------

### Install Bun Engine for Socket.IO (Bun)

Source: https://socket.io/docs/v4/server-installation

Installs the '@socket.io/bun-engine' package, which provides a Bun-specific engine for Socket.IO. This engine is designed to leverage Bun's performance characteristics for improved speed and scalability. It requires both Socket.IO and the Bun engine package to be installed.

```bash
bun add socket.io @socket.io/bun-engine
```

--------------------------------

### Configure Socket.IO with µWebSockets.js Server

Source: https://socket.io/docs/v4/server-installation

Shows how to integrate Socket.IO with a µWebSockets.js application. It involves creating a µWebSockets.js app, creating a Socket.IO server, attaching the Socket.IO server to the µWebSockets.js app using `attachApp`, and then starting the µWebSockets.js server's listener.

```javascript
const { App } = require("uWebSockets.js");
const { Server } = require("socket.io");

const app = App();
const io = new Server();

io.attachApp(app);

io.on("connection", (socket) => {
  // ...
});

app.listen(3000, (token) => {
  if (!token) {
    console.warn("port already in use");
  }
});

```

--------------------------------

### Redis Emitter Installation

Source: https://socket.io/docs/v4/redis-adapter

Instructions for installing the Socket.IO Redis emitter package.

```APIDOC
### Installation​

### Description
Instructions for installing the Socket.IO Redis emitter package.

### Command
```bash
npm install @socket.io/redis-emitter redis  
```
```

--------------------------------

### Install Socket.IO Client with Bun

Source: https://socket.io/docs/v4/client-installation

This command shows how to install the Socket.IO client package using Bun, a fast all-in-one JavaScript runtime. It adds the client to the project's dependencies.

```bash
bun add socket.io-client
```

--------------------------------

### Configure Socket.IO with Bun Engine

Source: https://socket.io/docs/v4/server-installation

Sets up a Socket.IO server to use the Bun-specific engine. This involves importing 'Server' from 'socket.io' and 'Engine' from '@socket.io/bun-engine'. An instance of the Bun engine is created and then bound to the Socket.IO server instance using `io.bind(engine)`. The Bun server handler is then exported.

```javascript
import { Server as Engine } from "@socket.io/bun-engine";
import { Server } from "socket.io";

const io = new Server();

const engine = new Engine({
  path: "/socket.io/",
});

io.bind(engine);

io.on("connection", (socket) => {
  // ...
});

export default {
  port: 3000,
  idleTimeout: 30, // must be greater than the "pingInterval" option of the engine, which defaults to 25 seconds

  ...engine.handler(),
};

```

--------------------------------

### Install eiows Alternative WebSocket Server (NPM, Yarn, pnpm, Bun)

Source: https://socket.io/docs/v4/server-installation

Installs the 'eiows' package, an alternative WebSocket server implementation that can be used with Socket.IO. It's a fork of the deprecated 'uws' package and may offer performance improvements. This requires replacing the default 'ws' engine with 'eiows.Server' during Socket.IO server initialization.

```bash
npm install eiows
```

```bash
yarn add eiows
```

```bash
pnpm add eiows
```

```bash
bun add eiows
```

--------------------------------

### Install µWebSockets.js for Socket.IO (NPM, Yarn, pnpm, Bun)

Source: https://socket.io/docs/v4/server-installation

Installs the 'uWebSockets.js' package, enabling Socket.IO to bind to a µWebSockets.js server for potentially significant performance gains. Note the specific version tag (e.g., '#v20.52.0') required for compatibility.

```bash
npm install uWebSockets.js@uNetworking/uWebSockets.js#v20.52.0
```

```bash
yarn add uWebSockets.js@uNetworking/uWebSockets.js#v20.52.0
```

```bash
pnpm add uWebSockets.js@uNetworking/uWebSockets.js#v20.52.0
```

```bash
bun add uWebSockets.js@uNetworking/uWebSockets.js#v20.52.0
```

--------------------------------

### Server-Side Connection Handling with TypeScript

Source: https://socket.io/docs/v4/migrating-from-2-x-to-3-0

Demonstrates basic server setup using TypeScript with Socket.IO. It initializes a new Server instance and logs connection and disconnection events along with the client socket ID.

```typescript
import { Server, Socket } from "socket.io";

const io = new Server(8080);

io.on("connection", (socket: Socket) => {
    console.log(`connect ${socket.id}`);

    socket.on("disconnect", () => {
        console.log(`disconnect ${socket.id}`);
    });
});

```

--------------------------------

### Clone Socket.IO v4 Chat Example from GitHub

Source: https://socket.io/docs/v4/tutorial/ending-notes

This command clones the Socket.IO v4 chat example project from its GitHub repository. Ensure you have Git installed and configured on your system. This provides a local copy of the example code to start with.

```bash
git clone https://github.com/socketio/chat-example.git  

```

--------------------------------

### Install Socket.IO Redis Adapter

Source: https://socket.io/docs/v4/redis-adapter

Installs the Socket.IO Redis adapter package using npm. This is the first step to integrating Redis-based features with Socket.IO.

```bash
npm install @socket.io/redis-adapter
```

--------------------------------

### Install and Use Socket.IO Redis Emitter

Source: https://socket.io/docs/v4/redis-adapter

This snippet covers the installation of the Redis emitter package and its subsequent usage in a Javascript application. It demonstrates how to create a Redis client, initialize the emitter, and emit messages at regular intervals. Note the difference in client connection handling between different redis package versions.

```bash
npm install @socket.io/redis-emitter redis  
```

```javascript
import { Emitter } from "@socket.io/redis-emitter";  
import { createClient } from "redis";  
  
const redisClient = createClient({ url: "redis://localhost:6379" });  
  
redisClient.connect().then(() => {  
  const emitter = new Emitter(redisClient);  
  
  setInterval(() => {  
    emitter.emit("time", new Date);  
  }, 5000);  
});  
```

```javascript
import { Emitter } from "@socket.io/redis-emitter";  
import { createClient } from "redis";  
  
const redisClient = createClient({ url: "redis://localhost:6379" });  
const emitter = new Emitter(redisClient);  
  
setInterval(() => {  
  emitter.emit("time", new Date);  
}, 5000);  
```

--------------------------------

### Install Socket.IO Latest Version (NPM, Yarn, pnpm, Bun)

Source: https://socket.io/docs/v4/server-installation

Installs the latest stable release of the socket.io package. This is the primary method for incorporating Socket.IO into a Node.js project. No specific dependencies are required beyond the package manager itself.

```bash
npm install socket.io
```

```bash
yarn add socket.io
```

```bash
pnpm add socket.io
```

```bash
bun add socket.io
```

--------------------------------

### Node.js Cluster Setup with @socket.io/sticky

Source: https://socket.io/docs/v4/using-multiple-nodes

This example demonstrates setting up Node.js cluster mode with the @socket.io/sticky package for load balancing. It configures a master process to manage worker processes and sets up sticky sessions for incoming connections. The `cluster-adapter` is used for inter-process communication, enabling broadcasting of events across all connected clients. This setup is particularly useful for handling real-time applications that benefit from multiple server instances.

```javascript
const cluster = require("cluster");
const http = require("http");
const { Server } = require("socket.io");
const numCPUs = require("os").cpus().length;
const { setupMaster, setupWorker } = require("@socket.io/sticky");
const { createAdapter, setupPrimary } = require("@socket.io/cluster-adapter");

if (cluster.isMaster) {
  console.log(`Master ${process.pid} is running`);

  const httpServer = http.createServer();

  // setup sticky sessions
  setupMaster(httpServer, {
    loadBalancingMethod: "least-connection",
  });

  // setup connections between the workers
  setupPrimary();

  // needed for packets containing buffers (you can ignore it if you only send plaintext objects)
  // Node.js < 16.0.0
  cluster.setupMaster({
    serialization: "advanced",
  });
  // Node.js > 16.0.0
  // cluster.setupPrimary({
  //   serialization: "advanced",
  // });

  httpServer.listen(3000);

  for (let i = 0; i < numCPUs; i++) {
    cluster.fork();
  }

  cluster.on("exit", (worker) => {
    console.log(`Worker ${worker.process.pid} died`);
    cluster.fork();
  });
} else {
  console.log(`Worker ${process.pid} started`);

  const httpServer = http.createServer();
  const io = new Server(httpServer);

  // use the cluster adapter
  io.adapter(createAdapter());

  // setup connection with the primary process
  setupWorker(io);

  io.on("connection", (socket) => {
    /* ... */
  });
}

```

--------------------------------

### Configure Socket.IO with eiows WebSocket Engine

Source: https://socket.io/docs/v4/server-installation

Demonstrates how to configure a Socket.IO server to use the 'eiows' WebSocket engine instead of the default 'ws' package. This involves requiring both 'socket.io' and 'eiows', and then passing 'eiows.Server' to the 'wsEngine' option when creating the 'Server' instance.

```javascript
const { Server } = require("socket.io");
const eiows = require("eiows");

const io = new Server(3000, {
  wsEngine: eiows.Server
});

```

--------------------------------

### Install Socket.IO Client with NPM

Source: https://socket.io/docs/v4/client-installation

This command demonstrates how to install the Socket.IO client package using NPM. This is the recommended approach for integrating Socket.IO into projects managed with NPM, allowing for version management and inclusion within build processes.

```bash
npm install socket.io-client
```

--------------------------------

### Install Socket.IO Postgres Adapter

Source: https://socket.io/docs/v4/postgres-adapter

Installs the necessary packages for the Socket.IO Postgres adapter and its PostgreSQL client. For TypeScript users, type definitions for pg are also recommended.

```bash
npm install @socket.io/postgres-adapter pg  

```

--------------------------------

### Install Socket.IO Redis Streams Adapter

Source: https://socket.io/docs/v4/redis-streams-adapter

Installs the necessary packages for the Socket.IO Redis Streams adapter and the 'redis' client. This is the initial step before integrating the adapter into your Socket.IO server.

```bash
npm install @socket.io/redis-streams-adapter redis  
```

--------------------------------

### Install Specific Socket.IO Version (NPM, Yarn, pnpm, Bun)

Source: https://socket.io/docs/v4/server-installation

Installs a particular version of the socket.io package, allowing developers to pin to a specific release. Replace 'version' with the desired tag (e.g., '3.1.0'). This is useful for maintaining compatibility or using features from older releases.

```bash
npm install socket.io@version
```

```bash
yarn add socket.io@version
```

```bash
pnpm add socket.io@version
```

```bash
bun add socket.io@version
```

--------------------------------

### Integrate Socket.IO with Fastify (CommonJS, ES Modules, TypeScript)

Source: https://socket.io/docs/v4/server-initialization

Provides an example of integrating Socket.IO with Fastify using the `fastify-socket.io` plugin. The server must be ready before accessing `server.io`. This example also shows emitting a message from a GET route.

```javascript
const fastify = require("fastify");
const fastifyIO = require("fastify-socket.io");

const server = fastify();
server.register(fastifyIO);

server.get("/", (req, reply) => {
  server.io.emit("hello");
});

server.ready().then(() => {
  // we need to wait for the server to be ready, else `server.io` is undefined
  server.io.on("connection", (socket) => {
    // ...
  });
});

server.listen({ port: 3000 });
```

```javascript
import fastify from "fastify";
import fastifyIO from "fastify-socket.io";

const server = fastify();
server.register(fastifyIO);

server.get("/", (req, reply) => {
  server.io.emit("hello");
});

server.ready().then(() => {
  // we need to wait for the server to be ready, else `server.io` is undefined
  server.io.on("connection", (socket) => {
    // ...
  });
});

server.listen({ port: 3000 });
```

```typescript
import fastify from "fastify";
import fastifyIO from "fastify-socket.io";

const server = fastify();
server.register(fastifyIO);

server.get("/", (req, reply) => {
  server.io.emit("hello");
});

server.ready().then(() => {
  // we need to wait for the server to be ready, else `server.io` is undefined
  server.io.on("connection", (socket) => {
    // ...
  });
});

server.listen({ port: 3000 });
```

--------------------------------

### Install Socket.IO Package

Source: https://socket.io/docs/v4/tutorial/step-3

This command installs the `socket.io` npm package and adds it as a dependency to your `package.json` file. It's the first step in setting up a Socket.IO server.

```bash
npm install socket.io
```

--------------------------------

### Install Socket.IO Postgres Emitter

Source: https://socket.io/docs/v4/postgres-adapter

Installs the necessary packages for the Socket.IO Postgres emitter, allowing packet emission from separate Node.js processes.

```bash
npm install @socket.io/postgres-emitter pg  

```

--------------------------------

### Socket.IO Server and Client Connection with Basic Event Handling (ES Modules)

Source: https://socket.io/docs/v4/testing

Sets up a Socket.IO server and client using ES module syntax. This version demonstrates the same functionality as the CommonJS example but with `import` statements. It utilizes the 'tape' testing framework and Node.js http module.

```javascript
import { test } from "tape";
import { createServer } from "node:http";
import { io as ioc } from "socket.io-client";
import { Server } from "socket.io";

let io, serverSocket, clientSocket;

function waitFor(socket, event) {
  return new Promise((resolve) => {
    socket.once(event, resolve);
  });
}

test("setup", (t) => {
  const httpServer = createServer();
  io = new Server(httpServer);
  httpServer.listen(() => {
    const port = httpServer.address().port;
    clientSocket = ioc(`http://localhost:${port}`);
    io.on("connection", (socket) => {
      serverSocket = socket;
    });
    clientSocket.on("connect", t.end);
  });
});

test("it works", (t) => {
  t.plan(1);
  clientSocket.on("hello", (arg) => {
    t.equal(arg, "world");
  });
  serverSocket.emit("hello", "world");
});

test("it works with an acknowledgement", (t) => {
  t.plan(1);
  serverSocket.on("hi", (cb) => {
    cb("hola");
  });
  clientSocket.emit("hi", (arg) => {
    t.equal(arg, "hola");
  });
});

test("it works with emitWithAck()", async (t) => {
  t.plan(1);
  serverSocket.on("foo", (cb) => {
    cb("bar");
  });
  const result = await clientSocket.emitWithAck("foo");
  t.equal(result, "bar");
});

test("it works with waitFor()", async (t) => {
  t.plan(1);
  clientSocket.emit("baz");

  await waitFor(serverSocket, "baz");
  t.pass();
});

test.onFinish(() => {
  io.close();
  clientSocket.disconnect();
});

```

--------------------------------

### Install Socket.IO Client with Yarn

Source: https://socket.io/docs/v4/client-installation

This command shows how to add the Socket.IO client package to a project using Yarn, a popular JavaScript package manager. This command is equivalent to `npm install` and integrates the client into the project's dependencies.

```bash
yarn add socket.io-client
```

--------------------------------

### Install Socket.IO Cluster Adapter

Source: https://socket.io/docs/v4/cluster-adapter

Installs the @socket.io/cluster-adapter package using npm. This is a prerequisite for using the cluster adapter in your Socket.IO application.

```bash
npm install @socket.io/cluster-adapter  
```

--------------------------------

### Install Socket.IO Client with pnpm

Source: https://socket.io/docs/v4/client-installation

This command illustrates how to install the Socket.IO client package using pnpm, another efficient Node.js package manager. It adds the client to the project's dependencies, similar to NPM and Yarn.

```bash
pnpm add socket.io-client
```

--------------------------------

### Install Socket.IO Admin UI Package

Source: https://socket.io/docs/v4/admin-ui

Installs the necessary npm package for the Socket.IO admin UI. This is the first step for server-side integration.

```bash
npm i @socket.io/admin-ui  
```

--------------------------------

### Import Socket.IO Server (CommonJS)

Source: https://socket.io/docs/v4/tutorial/introduction

This snippet demonstrates importing the Server class from the 'socket.io' package using the legacy CommonJS module syntax. This method is compatible with older Node.js environments or projects not configured for ESM. It's a simple require statement.

```javascript
const { Server } = require("socket.io");
```

--------------------------------

### Install Artillery and Socket.IO v3/v4 Engine

Source: https://socket.io/docs/v4/load-testing

Installs Artillery, a load testing tool, and the necessary engine for compatibility with Socket.IO v3 and v4 servers. This is a prerequisite for using Artillery with modern Socket.IO versions.

```bash
npm install artillery artillery-engine-socketio-v3
```

--------------------------------

### Install MongoDB Adapter and MongoDB Driver

Source: https://socket.io/docs/v4/mongo-adapter

Installs the necessary npm packages for the MongoDB adapter and the MongoDB driver. For TypeScript users, additional type definitions might be required.

```bash
npm install @socket.io/mongo-adapter mongodb  
```

--------------------------------

### Import Socket.IO Server (ES Modules)

Source: https://socket.io/docs/v4/tutorial/introduction

This snippet shows how to import the Server class from the 'socket.io' package using ECMAScript modules (ESM) syntax. This is the recommended approach for modern Node.js projects. No specific inputs or outputs are defined here, as it's a module import statement.

```javascript
import { Server } from "socket.io";
```

--------------------------------

### Server-Side Connection and Event Listener

Source: https://socket.io/docs/v4/emitting-events

A basic server-side setup demonstrating connection handling and listening for a 'ping' event. This code is part of the volatile event example to show client behavior.

```javascript
io.on("connection", (socket) => {
  console.log("connect");

  socket.on("ping", (count) => {
    console.log(count);
  });
});
```

--------------------------------

### Socket.IO Client Custom Path with Namespace Example

Source: https://socket.io/docs/v4/client-options

Demonstrates how to configure a custom path for Socket.IO client connections while also specifying a namespace in the URI. This example shows how HTTP requests will look with the custom path and EIO version.

```javascript
import { io } from "socket.io-client";

const socket = io("https://example.com/order", {
  path: "/my-custom-path/"
});

// HTTP requests will look like: GET https://example.com/my-custom-path/?EIO=4&transport=polling&t=ML4jUwU
```

--------------------------------

### Socket.IO Server and Client Connection with Basic Event Handling (TypeScript)

Source: https://socket.io/docs/v4/testing

Sets up a Socket.IO server and client using TypeScript. This example includes type definitions for sockets and addresses, enhancing code safety and maintainability. It uses the 'tape' testing framework and Node.js http module.

```typescript
import { test } from "tape";
import { createServer } from "node:http";
import { type AddressInfo } from "node:net";
import { io as ioc, type Socket as ClientSocket } from "socket.io-client";
import { Server, type Socket as ServerSocket } from "socket.io";

let io: Server, serverSocket: ServerSocket, clientSocket: ClientSocket;

function waitFor(socket: ServerSocket | ClientSocket, event: string) {
  return new Promise((resolve) => {
    socket.once(event, resolve);
  });
}

test("setup", (t) => {
  const httpServer = createServer();
  io = new Server(httpServer);
  httpServer.listen(() => {
    const port = (httpServer.address() as AddressInfo).port;
    clientSocket = ioc(`http://localhost:${port}`);
    io.on("connection", (socket) => {
      serverSocket = socket;
    });
    clientSocket.on("connect", t.end);
  });
});

test("it works", (t) => {
  t.plan(1);
  clientSocket.on("hello", (arg) => {
    t.equal(arg, "world");
  });
  serverSocket.emit("hello", "world");
});

test("it works with an acknowledgement", (t) => {
  t.plan(1);
  serverSocket.on("hi", (cb) => {
    cb("hola");
  });
  clientSocket.emit("hi", (arg) => {
    t.equal(arg, "hola");
  });
});

test("it works with emitWithAck()", async (t) => {
  t.plan(1);
  serverSocket.on("foo", (cb) => {
    cb("bar");
  });
  const result = await clientSocket.emitWithAck("foo");
  t.equal(result, "bar");
});

test("it works with waitFor()", async (t) => {
  t.plan(1);
  clientSocket.emit("baz");

  await waitFor(serverSocket, "baz");
  t.pass();
});

test.onFinish(() => {
  io.close();
  clientSocket.disconnect();
});

```

--------------------------------

### Install SQLite and Socket.IO Dependencies (Bun)

Source: https://socket.io/docs/v4/tutorial/step-7

Installs the necessary Bun packages for using SQLite and Socket.IO in your Node.js project. Ensure you have Bun installed.

```bash
bun add sqlite sqlite3  
```

--------------------------------

### Install MongoDB Emitter

Source: https://socket.io/docs/v4/mongo-adapter

Installs the necessary npm packages for the MongoDB emitter, allowing packet transmission from separate Node.js processes.

```bash
npm install @socket.io/mongo-emitter mongodb  
```

--------------------------------

### Install GCP Pub/Sub Adapter for Socket.IO

Source: https://socket.io/docs/v4/gcp-pubsub-adapter

Installs the necessary npm package for the Socket.IO GCP Pub/Sub adapter. This allows Socket.IO nodes to communicate via Google Cloud Pub/Sub.

```bash
npm install @socket.io/gcp-pubsub-adapter
```

--------------------------------

### Install Express Dependency

Source: https://socket.io/docs/v4/tutorial/step-1

Installs the specified version of the Express.js framework using npm. This command adds Express as a dependency to your project, making it available for use in your Node.js application.

```bash
npm install express@4
```

--------------------------------

### Example: Socket.IO Client Connection (JavaScript)

Source: https://socket.io/docs/v4/index

Demonstrates an attempt to connect a Socket.IO client to a WebSocket echo server. This example highlights a common pitfall: a Socket.IO client cannot connect to a plain WebSocket server due to protocol differences.

```javascript
const socket = io("ws://echo.websocket.org");  
```

--------------------------------

### Run Artillery Load Test Scenario

Source: https://socket.io/docs/v4/load-testing

Executes a previously defined Artillery load test scenario from the command line. This command will start the test according to the configuration in the specified YAML file.

```bash
npx artillery run my-scenario.yml
```

--------------------------------

### Install SQLite and Socket.IO Dependencies (NPM)

Source: https://socket.io/docs/v4/tutorial/step-7

Installs the necessary npm packages for using SQLite and Socket.IO in your Node.js project. Ensure you have Node.js and npm installed.

```bash
npm install sqlite sqlite3  
```

--------------------------------

### Creating and Using Custom Socket.IO Namespaces (JavaScript)

Source: https://socket.io/docs/v4/namespaces

Provides an example of how to create a custom Socket.IO namespace ('/my-namespace') on the server, set up event listeners for connections, and emit messages to clients within that namespace.

```javascript
const nsp = io.of("/my-namespace");  
  
nsp.on("connection", socket => {  
  console.log("someone connected");  
});  
  
nsp.emit("hi", "everyone!");  

```

--------------------------------

### Standalone Usage of Socket.IO Postgres Adapter

Source: https://socket.io/docs/v4/postgres-adapter

Demonstrates the standalone setup of the Socket.IO Postgres adapter. It initializes a Socket.IO server, configures a PostgreSQL connection pool, creates the necessary attachment table if it doesn't exist, and attaches the adapter to the Socket.IO server.

```javascript
import { Server } from "socket.io";  
import { createAdapter } from "@socket.io/postgres-adapter";  
import pg from "pg";  
  
const io = new Server();  
  
const pool = new pg.Pool({
  user: "postgres",  
  host: "localhost",  
  database: "postgres",  
  password: "changeit",  
  port: 5432,  
});  
  
pool.query(`  
  CREATE TABLE IF NOT EXISTS socket_io_attachments (  
      id          bigserial UNIQUE,  
      created_at  timestamptz DEFAULT NOW(),  
      payload     bytea  
  );
`);  
  
pool.on("error", (err) => {  
  console.error("Postgres error", err);  
});  
  
io.adapter(createAdapter(pool));  
io.listen(3000);  

```

--------------------------------

### Socket.IO v4: Joi Validation Example with Acknowledgements

Source: https://socket.io/docs/v4/listening-to-events

Demonstrates how to use the Joi library for validating incoming payloads on the server before processing them and sending an acknowledgement. This example shows server-side validation for a 'create user' event.

```javascript
const Joi = require("joi");

const userSchema = Joi.object({
  username: Joi.string().max(30).required(),
  email: Joi.string().email().required()
});

io.on("connection", (socket) => {
  socket.on("create user", (payload, callback) => {
    if (typeof callback !== "function") {
      // not an acknowledgement
      return socket.disconnect();
    }
    const { error, value } = userSchema.validate(payload);
    if (error) {
      return callback({
        status: "Bad Request",
        error
      });
    }
    // do something with the value, and then
    callback({
      status: "OK"
    });
  });

});
```

--------------------------------

### Socket.IO Server and Client Connection with Basic Event Handling (JavaScript)

Source: https://socket.io/docs/v4/testing

Sets up a Socket.IO server and client, establishes a connection, and tests basic event emission and reception. It uses the 'tape' testing framework and Node.js http module. The `waitFor` function is a utility for asynchronous event waiting.

```javascript
const test = require("tape");
const { createServer } = require("node:http");
const { Server } = require("socket.io");
const ioc = require("socket.io-client");

let io, serverSocket, clientSocket;

function waitFor(socket, event) {
  return new Promise((resolve) => {
    socket.once(event, resolve);
  });
}

test("setup", (t) => {
  const httpServer = createServer();
  io = new Server(httpServer);
  httpServer.listen(() => {
    const port = httpServer.address().port;
    clientSocket = ioc(`http://localhost:${port}`);
    io.on("connection", (socket) => {
      serverSocket = socket;
    });
    clientSocket.on("connect", t.end);
  });
});

test("it works", (t) => {
  t.plan(1);
  clientSocket.on("hello", (arg) => {
    t.equal(arg, "world");
  });
  serverSocket.emit("hello", "world");
});

test("it works with an acknowledgement", (t) => {
  t.plan(1);
  serverSocket.on("hi", (cb) => {
    cb("hola");
  });
  clientSocket.emit("hi", (arg) => {
    t.equal(arg, "hola");
  });
});

test("it works with emitWithAck()", async (t) => {
  t.plan(1);
  serverSocket.on("foo", (cb) => {
    cb("bar");
  });
  const result = await clientSocket.emitWithAck("foo");
  t.equal(result, "bar");
});

test("it works with waitFor()", async (t) => {
  t.plan(1);
  clientSocket.emit("baz");

  await waitFor(serverSocket, "baz");
  t.pass();
});

test.onFinish(() => {
  io.close();
  clientSocket.disconnect();
});

```

--------------------------------

### Install SQLite and Socket.IO Dependencies (pnpm)

Source: https://socket.io/docs/v4/tutorial/step-7

Installs the necessary pnpm packages for using SQLite and Socket.IO in your Node.js project. Ensure you have Node.js and pnpm installed.

```bash
pnpm add sqlite sqlite3  
```

--------------------------------

### Manager-based Socket.IO Connection Setup

Source: https://socket.io/docs/v4/client-api

Shows how to manually create a `Manager` instance and then obtain `Socket` instances for different namespaces. This approach is useful for managing multiple sockets or fine-grained control over the connection lifecycle.

```javascript
import { Manager } from "socket.io-client";  
  
const manager = new Manager("https://example.com");  
  
const socket = manager.socket("/"); // main namespace  
const adminSocket = manager.socket("/admin"); // admin namespace  
```

--------------------------------

### Install SQLite and Socket.IO Dependencies (Yarn)

Source: https://socket.io/docs/v4/tutorial/step-7

Installs the necessary Yarn packages for using SQLite and Socket.IO in your Node.js project. Ensure you have Node.js and Yarn installed.

```bash
yarn add sqlite sqlite3  
```

--------------------------------

### WebSocket Communication Examples

Source: https://socket.io/docs/v4/socket-io-protocol

Demonstrates various Engine.IO and Socket.IO packet types exchanged over WebSocket.

```APIDOC
## WebSocket Frames

### Description
Illustrates the flow of Engine.IO and Socket.IO packets over an established WebSocket connection.

### Details
- **2probe**: Engine.IO probe request.
- **3probe**: Engine.IO probe response.
- **5**: Engine.IO "upgrade" packet type.
- **42["hello"]**: Socket.IO "EVENT" packet.
- **42["world"]**: Socket.IO "EVENT" packet.
- **40/admin,**: Request to connect to the '/admin' namespace.
- **40/admin,{"sid":"..."}**: Server grants access to the '/admin' namespace.
- **42/admin,1["tellme"]**: Socket.IO "EVENT" packet with an acknowledgement request.
- **461-/admin,1[{"_placeholder":true,"num":0}]**: Socket.IO "BINARY_ACK" packet with a placeholder for binary data.
- **<binary>**: Binary attachment data.
- **2**: Engine.IO "ping" packet type.
- **3**: Engine.IO "pong" packet type.
- **1**: Engine.IO "close" packet type.

### Example Exchange
```
< 2probe
> 3probe
> 5
> 42["hello"]
> 42["world"]
> 40/admin,
< 40/admin,{"sid":"-G5j-67EZFp-q59rADQM"}
> 42/admin,1["tellme"]
< 461-/admin,1[{"_placeholder":true,"num":0}]
< <binary>
...
> 2
< 3
> 1
```
```

--------------------------------

### Install @socket.io/pm2 Package

Source: https://socket.io/docs/v4/pm2

Installs the @socket.io/pm2 package globally. This package acts as a replacement for the standard PM2 utility, enabling advanced features for scaling Socket.IO applications.

```bash
npm install -g @socket.io/pm2

```

--------------------------------

### Connect to Socket.IO with Custom Options

Source: https://socket.io/docs/v4/client-api

Demonstrates connecting to a Socket.IO server with a specific namespace, custom authentication, and query parameters. This example shows the flexibility of the `io()` function for configuring connections.

```javascript
import { io } from "socket.io-client";  
  
const socket = io("ws://example.com/my-namespace", {  
  reconnectionDelayMax: 10000,  
  auth: {  
    token: "123"  
  },  
  query: {  
    "my-key": "my-value"  
  }  
});  
```

--------------------------------

### Redis Emitter Usage (redis@4+)

Source: https://socket.io/docs/v4/redis-adapter

Example usage of the Socket.IO Redis emitter with `redis@4` or later.

```APIDOC
### Usage​ (redis@4+)

### Description
Example usage of the Socket.IO Redis emitter with `redis@4` or later.

### Code Example
```javascript
import { Emitter } from "@socket.io/redis-emitter";  
import { createClient } from "redis";  
  
const redisClient = createClient({ url: "redis://localhost:6379" });  
  
redisClient.connect().then(() => {  
  const emitter = new Emitter(redisClient);  
  
  setInterval(() => {  
    emitter.emit("time", new Date);
  }, 5000);
});
```
```

--------------------------------

### HTTP GET Request for WebSocket Handshake

Source: https://socket.io/docs/v4/engine-io-protocol

Demonstrates the client's HTTP GET request to initiate a WebSocket handshake with the server. This request includes mandatory query parameters for protocol version and transport type.

```http
GET /engine.io/?EIO=4&transport=websocket HTTP/1.1
Host: your_server.com
Upgrade: websocket
Connection: Upgrade
```

--------------------------------

### Setting Up Multiple Namespaces in Socket.IO (JavaScript)

Source: https://socket.io/docs/v4/namespaces

Demonstrates how to define and handle connections for different namespaces ('/orders' and '/users') in Socket.IO. It shows how to attach event listeners for specific events within each namespace.

```javascript
io.of("/orders").on("connection", (socket) => {  
  socket.on("order:list", () => {});  
  socket.on("order:create", () => {});  
});  
  
io.of("/users").on("connection", (socket) => {  
  socket.on("user:list", () => {});  
});  

```

--------------------------------

### Configure Socket.IO Server: Enable v2 Client Compatibility

Source: https://socket.io/docs/v4/server-options

This example shows how to enable compatibility with Socket.IO v2 clients by setting the `allowEIO3` option to `true`. The default value for this option is `false`.

```javascript
const io = new Server(httpServer, {
  allowEIO3: true // false by default
});

```

--------------------------------

### Initialize Socket.IO Server with Port Argument

Source: https://socket.io/docs/v4/server-initialization

Initializes a Socket.IO v4 server by passing the port number as the first argument to the Server constructor. This is a concise way to start the server listening on a specific port. It implicitly starts a Node.js HTTP server.

```javascript
const { Server } = require("socket.io");

const io = new Server(3000, { /* options */ });

io.on("connection", (socket) => {
  // ...
});

```

```javascript
import { Server } from "socket.io";

const io = new Server(3000, { /* options */ });

io.on("connection", (socket) => {
  // ...
});

```

```typescript
import { Server } from "socket.io";

const io = new Server(3000, { /* options */ });

io.on("connection", (socket) => {
  // ...
});

```

--------------------------------

### Client-Side Connection Establishment with TypeScript

Source: https://socket.io/docs/v4/migrating-from-2-x-to-3-0

Illustrates how to connect to a Socket.IO server from a client using TypeScript. It establishes a connection to the default namespace and logs when the client successfully connects, including the socket ID.

```typescript
import { io } from "socket.io-client";

const socket = io("/");

socket.on("connect", () => {
    console.log(`connect ${socket.id}`);
});

```

--------------------------------

### Include Socket.IO Client in HTML (Standalone)

Source: https://socket.io/docs/v4/client-installation

This snippet shows how to include the Socket.IO client JavaScript file directly from the server in an HTML document. It then demonstrates how to initialize a client-side Socket.IO connection using the globally available `io` object. This method assumes the server is configured to serve the client bundle.

```html
<script src="/socket.io/socket.io.js"></script>
<script>
  const socket = io();
</script>
```

--------------------------------

### Socket.IO Room Management Sample Use Cases

Source: https://socket.io/docs/v4/rooms

Provides practical examples of using rooms for common scenarios, such as broadcasting data to all devices of a specific user or sending notifications about a particular entity.

```javascript
function computeUserIdFromHeaders(headers) {  
  // to be implemented  
}  
  
io.on("connection", async (socket) => {  
  const userId = await computeUserIdFromHeaders(socket.handshake.headers);  
  
  socket.join(userId);  
  
  // and then later  
  io.to(userId).emit("hi");  
});  

io.on("connection", async (socket) => {  
  const projects = await fetchProjects(socket);  
  
  projects.forEach(project => socket.join("project:" + project.id));  
  
  // and then later  
  io.to("project:4321").emit("project updated");  
});  
```

--------------------------------

### Install ws Native Add-ons for Socket.IO

Source: https://socket.io/docs/v4/performance-tuning

Installs optional 'bufferutil' and 'utf-8-validate' npm packages to improve WebSocket performance by enabling efficient data payload operations and UTF-8 validation. These packages are optional and the WebSocket server will fallback to JavaScript implementations if unavailable.

```bash
$ npm install --save-optional bufferutil utf-8-validate  

```

--------------------------------

### Install AWS SQS Adapter for Socket.IO

Source: https://socket.io/docs/v4/aws-sqs-adapter

Installs the `@socket.io/aws-sqs-adapter` package using npm. This package is essential for setting up the AWS SQS adapter for Socket.IO clusters.

```bash
npm install @socket.io/aws-sqs-adapter  

```

--------------------------------

### Install Azure Service Bus Adapter for Socket.IO

Source: https://socket.io/docs/v4/azure-service-bus-adapter

Installs the necessary npm package for the Azure Service Bus adapter for Socket.IO. This command is essential before using the adapter in your project.

```bash
npm install @socket.io/azure-service-bus-adapter
```

--------------------------------

### Install Socket.IO and Dependencies for Webpack 5 (Node.js)

Source: https://socket.io/docs/v4/server-with-bundlers

Installs the necessary packages for bundling Socket.IO with Webpack 5 for a Node.js environment. This includes webpack, webpack-cli, and optional but recommended socket.io dependencies for performance.

```bash
npm install -D webpack webpack-cli socket.io bufferutil utf-8-validate  

```

--------------------------------

### Redis Emitter Usage (redis@3)

Source: https://socket.io/docs/v4/redis-adapter

Example usage of the Socket.IO Redis emitter with `redis@3`.

```APIDOC
### Usage​ (redis@3)

### Description
Example usage of the Socket.IO Redis emitter with `redis@3`.

### Code Example
```javascript
import { Emitter } from "@socket.io/redis-emitter";  
import { createClient } from "redis";  
  
const redisClient = createClient({ url: "redis://localhost:6379" });  
const emitter = new Emitter(redisClient);  
  
setInterval(() => {  
  emitter.emit("time", new Date);
}, 5000);
```

### Note
With `redis@3`, calling `connect()` on the Redis client is not needed.
```

--------------------------------

### ES Modules Socket.IO Test Suite with Mocha and Chai

Source: https://socket.io/docs/v4/testing

This snippet showcases a Socket.IO v4 test suite using ES modules, Mocha, and Chai. It mirrors the CommonJS example but utilizes modern import syntax for modules and dependencies.

```javascript
import { createServer } from "node:http";
import { io as ioc } from "socket.io-client";
import { Server } from "socket.io";
import { assert } from "chai";

function waitFor(socket, event) {
  return new Promise((resolve) => {
    socket.once(event, resolve);
  });
}

describe("my awesome project", () => {
  let io, serverSocket, clientSocket;

  before((done) => {
    const httpServer = createServer();
    io = new Server(httpServer);
    httpServer.listen(() => {
      const port = httpServer.address().port;
      clientSocket = ioc(`http://localhost:${port}`);
      io.on("connection", (socket) => {
        serverSocket = socket;
      });
      clientSocket.on("connect", done);
    });
  });

  after(() => {
    io.close();
    clientSocket.disconnect();
  });

  it("should work", (done) => {
    clientSocket.on("hello", (arg) => {
      assert.equal(arg, "world");
      done();
    });
    serverSocket.emit("hello", "world");
  });

  it("should work with an acknowledgement", (done) => {
    serverSocket.on("hi", (cb) => {
      cb("hola");
    });
    clientSocket.emit("hi", (arg) => {
      assert.equal(arg, "hola");
      done();
    });
  });

  it("should work with emitWithAck()", async () => {
    serverSocket.on("foo", (cb) => {
      cb("bar");
    });
    const result = await clientSocket.emitWithAck("foo");
    assert.equal(result, "bar");
  });

  it("should work with waitFor()", () => {
    clientSocket.emit("baz");

    return waitFor(serverSocket, "baz");
  });
});

```

--------------------------------

### Socket.IO Protocol Overhead Example

Source: https://socket.io/docs/v4/index

Shows the structure of a Socket.IO message when sent over a WebSocket connection. It breaks down the packet types and demonstrates how arguments are serialized, providing insight into the protocol's efficiency.

```javascript
socket.emit("hello", "world"); // Sent as: 42["hello","world"]
```