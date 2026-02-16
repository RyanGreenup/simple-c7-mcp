### Create a Solid.js Project with deno

Source: https://docs.solidjs.com/quick-start

This command initializes a new Solid.js project using deno and the create-solid scaffolding tool. It will guide you through project setup options and then install dependencies and start the development server.

```bash
deno init --npm solid
cd solid-project
denoo install
denoo run dev
```

--------------------------------

### Create a Solid.js Project with bun

Source: https://docs.solidjs.com/quick-start

This command initializes a new Solid.js project using bun and the create-solid scaffolding tool. It will guide you through project setup options and then install dependencies and start the development server.

```bash
bun create solid
cd solid-project
bun install
bun run dev
```

--------------------------------

### SolidJS Meta Provider Setup Example

Source: https://docs.solidjs.com/solid-meta/getting-started/installation-and-setup

Demonstrates setting up the MetaProvider and using components like Title, Link, and Meta within a SolidJS application. This enables dynamic management of head tags for SEO and metadata.

```jsx
import { MetaProvider, Title, Link, Meta } from "@solidjs/meta";

const App = () => (
  <MetaProvider>
    <div class="Home">
      <Title>Title of page</Title>
      <Link rel="canonical" href="http://solidjs.com/" />
      <Meta name="example" content="whatever" />
    </div>
  </MetaProvider>
);

```

--------------------------------

### Create a Solid.js Project with npm

Source: https://docs.solidjs.com/quick-start

This command initializes a new Solid.js project using npm and the create-solid scaffolding tool. It will guide you through project setup options and then install dependencies and start the development server.

```bash
npm init solid
cd solid-project
npm install
npm run dev
```

--------------------------------

### Create a Solid.js Project with pnpm

Source: https://docs.solidjs.com/quick-start

This command initializes a new Solid.js project using pnpm and the create-solid scaffolding tool. It will guide you through project setup options and then install dependencies and start the development server.

```bash
pnpm create solid
cd solid-project
pnpm install
pnpm dev
```

--------------------------------

### Install Solid Router with deno

Source: https://docs.solidjs.com/solid-router/getting-started/installation-and-setup

Install the Solid Router package for Deno projects. Deno can manage npm dependencies directly.

```bash
deno add npm:@solidjs/router
```

--------------------------------

### Create a Solid.js Project with yarn

Source: https://docs.solidjs.com/quick-start

This command initializes a new Solid.js project using yarn and the create-solid scaffolding tool. It will guide you through project setup options and then install dependencies and start the development server.

```bash
yarn create solid
cd solid-project
yarn install
yarn dev
```

--------------------------------

### Install Solid Router with npm

Source: https://docs.solidjs.com/solid-router/getting-started/installation-and-setup

Install the Solid Router package using npm. This is a common package manager for JavaScript projects.

```bash
npm i @solidjs/router
```

--------------------------------

### Install @solidjs/meta with bun

Source: https://docs.solidjs.com/solid-meta/getting-started/installation-and-setup

Installs the @solidjs/meta package using bun. This command is for users leveraging the bun runtime and package manager.

```bash
bun i @solidjs/meta
```

--------------------------------

### Install Solid Router with bun

Source: https://docs.solidjs.com/solid-router/getting-started/installation-and-setup

Install the Solid Router package using bun. bun is a fast JavaScript runtime and toolkit that includes a package manager.

```bash
bun i @solidjs/router
```

--------------------------------

### Install Solid Router with pnpm

Source: https://docs.solidjs.com/solid-router/getting-started/installation-and-setup

Install the Solid Router package using pnpm. pnpm is another popular package manager known for its efficiency.

```bash
pnpm i @solidjs/router
```

--------------------------------

### Install @solidjs/meta with pnpm

Source: https://docs.solidjs.com/solid-meta/getting-started/installation-and-setup

Installs the @solidjs/meta package using pnpm. This command is an alternative for users who prefer the pnpm package manager.

```bash
pnpm i @solidjs/meta
```

--------------------------------

### Install Solid Router with yarn

Source: https://docs.solidjs.com/solid-router/getting-started/installation-and-setup

Install the Solid Router package using yarn. yarn is a widely used package manager for JavaScript.

```bash
yarn add @solidjs/router
```

--------------------------------

### Install @solidjs/meta with yarn

Source: https://docs.solidjs.com/solid-meta/getting-started/installation-and-setup

Installs the @solidjs/meta package using yarn. This command is suitable for developers using the yarn package manager.

```bash
yarn add @solidjs/meta
```

--------------------------------

### Install @solidjs/meta with deno

Source: https://docs.solidjs.com/solid-meta/getting-started/installation-and-setup

Installs the @solidjs/meta package using deno. This command specifies the npm specifier for adding the package via deno.

```bash
deno add npm:@solidjs/meta
```

--------------------------------

### Install @solidjs/meta with npm

Source: https://docs.solidjs.com/solid-meta/getting-started/installation-and-setup

Installs the @solidjs/meta package using npm. This is a core dependency for managing head tags in SolidJS applications.

```bash
npm i @solidjs/meta
```

--------------------------------

### Install Project Dependencies with Various Package Managers

Source: https://docs.solidjs.com/solid-start/getting-started

After initializing the project and choosing a template, this command installs the necessary dependencies for the SolidStart application using different package managers.

```bash
npm i

```

```bash
pnpm i

```

```bash
yarn i

```

```bash
bun i

```

```bash
deno i

```

--------------------------------

### Configure Root Router in SolidJS

Source: https://docs.solidjs.com/solid-router/getting-started/installation-and-setup

Sets up the main Router component in a SolidJS application. It imports necessary functions from 'solid-js/web' and '@solidjs/router', renders the Router component, and mounts it to a specified DOM element. Ensures the target element exists before rendering.

```typescript
import { render } from "solid-js/web";
import { Router } from "@solidjs/router";

const wrapper = document.getElementById("app");

if (!wrapper) {
  throw new Error("Wrapper div not found");
}

render(() => <Router />, wrapper);
```

--------------------------------

### Server Setup with MetaProvider in SolidStart

Source: https://docs.solidjs.com/solid-meta/getting-started/server-setup

This snippet demonstrates the server-side setup for SolidStart applications using MetaProvider. It shows how to render the application to a string and include assets, ensuring head tags are managed correctly during server rendering. This requires the '@solidjs/meta' package.

```typescript
import { renderToString, getAssets } from "solid-js/web";
import { MetaProvider } from "@solidjs/meta";
import App from "./App";

// ... within the context of a request ...
const app = renderToString(() => (
  <MetaProvider>
    <App />
  </MetaProvider>
));

res.send(`
  <!DOCTYPE html>
  <html>
    <head>
      ${getAssets()}
    </head>
    <body>
      ${app}
    </body>
  </html>
`);
```

--------------------------------

### Run SolidStart Application Locally with Various Package Managers

Source: https://docs.solidjs.com/solid-start/getting-started

This command starts the development server for the SolidStart application, allowing you to view and test your application locally. It typically runs on port 3000.

```bash
npm run dev

```

```bash
pnpm dev

```

```bash
yarn dev

```

```bash
bun run dev

```

```bash
deno run dev

```

--------------------------------

### SolidStart GET Server Function

Source: https://docs.solidjs.com/solid-start/reference/server/get

This endpoint describes how to use the `GET` function to create server-side functions that are exposed via HTTP GET requests. It explains how arguments are serialized into the URL and how to utilize HTTP cache-control headers.

```APIDOC
## GET /server-function

### Description
Creates a server function that is accessed via an HTTP GET request. Arguments are serialized into the URL, allowing for the use of HTTP cache-control headers. Useful for streaming promises with defined cache lifetimes.

### Method
GET

### Endpoint
`/server-function` (This is a conceptual endpoint, actual routing depends on your setup)

### Parameters
#### Path Parameters
None

#### Query Parameters
- **name** (string) - Required - The name passed to the server function, serialized into the URL.

#### Request Body
None

### Request Example
```json
// No request body for GET, parameters are in URL
// Example URL: /server-function?name=World
```

### Response
#### Success Response (200)
- **hello** (Promise<string>) - A promise that resolves with the provided name after a delay.
- **headers** (object) - Contains cache-control directives.

#### Response Example
```json
{
  "hello": "World" // After the promise resolves
}
```

### Usage Example
```typescript
import { json } from "@solidjs/router";
import { GET } from "@solidjs/start";

const hello = GET(async (name: string) => {
  "use server";
  return json(
    {
      hello: new Promise((r) => setTimeout(() => r(name), 1000))
    },
    {
      headers: {
        "cache-control": "max-age=60"
      }
    }
  );
});
```
```

--------------------------------

### Install Solid Router

Source: https://docs.solidjs.com/guides/routing-and-navigation

Instructions for installing the Solid Router package using various package managers like npm, pnpm, yarn, bun, and deno.

```npm
npm i @solidjs/router
```

```pnpm
pnpm i @solidjs/router
```

```yarn
yarn add @solidjs/router
```

```bun
bun i @solidjs/router
```

```deno
deno add npm:@solidjs/router
```

--------------------------------

### SolidJS createStore Initialization Example

Source: https://docs.solidjs.com/reference/store-utilities/create-store

Demonstrates how to initialize a reactive store using `createStore` in SolidJS. The example shows creating a store with an initial state object containing a `userCount` and an array of `users`, each with their own properties.

```javascript
import { createStore } from "solid-js/store";

// Initialize store
const [store, setStore] = createStore({
  userCount: 3,
  users: [
    {
      id: 0,
      username: "felix909",
      location: "England",
      loggedIn: false,
    },
    {
      id: 1,
      username: "tracy634",
      location: "Canada",
      loggedIn: true,
    },
    {
      id: 1,
      username: "johny123",
      location: "India",
      loggedIn: true,
    },
  ],
});
```

--------------------------------

### Install Zerops CLI globally with deno

Source: https://docs.solidjs.com/guides/deployment-options/zerops

Installs the Zerops CLI globally using deno, making the `zcli` command available system-wide for managing Zerops deployments.

```bash
deno add npm:@zerops/zcli -g
```

--------------------------------

### Create Server GET Function with Cache in SolidStart

Source: https://docs.solidjs.com/solid-start/reference/server/get

Demonstrates how to create a server function using `GET` in SolidStart. This function handles HTTP GET requests, serializes arguments into the URL, and sets a `cache-control` header for a streaming promise. It relies on the `@solidjs/router` and `@solidjs/start` packages.

```typescript
import { json } from "@solidjs/router";
import { GET } from "@solidjs/start";

const hello = GET(async (name: string) => {
  "use server";
  return json( 
    { hello: new Promise((r) => setTimeout(() => r(name), 1000)) }, 
    { headers: { "cache-control": "max-age=60" } } 
  );
});
```

--------------------------------

### Install Zerops CLI globally with bun

Source: https://docs.solidjs.com/guides/deployment-options/zerops

Installs the Zerops CLI globally using bun, making the `zcli` command available system-wide for managing Zerops deployments.

```bash
bun i @zerops/zcli -g
```

--------------------------------

### SolidJS createMemo Basic Usage Example

Source: https://docs.solidjs.com/reference/basic-reactivity/create-memo

An example demonstrating the basic usage of createMemo in SolidJS. It shows how to wrap a function that computes an expensive value, making it reactive and ensuring it only re-runs when its dependencies (a() and b()) change.

```javascript
const value = createMemo(() => computeExpensiveValue(a(), b()))

// read the value
value()
```

--------------------------------

### Install Vercel CLI

Source: https://docs.solidjs.com/guides/deployment-options/vercel

Instructions for installing the Vercel CLI using various package managers like npm, pnpm, yarn, bun, and deno. This tool is essential for deploying projects from your local terminal.

```npm
npm i vercel -g
```

```pnpm
pnpm i vercel -g
```

```yarn
yarn add vercel -g
```

```bun
bun i vercel -g
```

```deno
deno add npm:vercel -g
```

--------------------------------

### Install Firebase CLI

Source: https://docs.solidjs.com/guides/deployment-options/firebase

Installs the Firebase command-line tool globally using various package managers. Ensure you have Node.js and your preferred package manager (npm, pnpm, yarn, bun, or deno) installed.

```bash
npm i firebase-tools -g
```

```bash
pnpm i firebase-tools -g
```

```bash
yarn add firebase-tools -g
```

```bash
bun i firebase-tools -g
```

```bash
deno add npm:firebase-tools -g
```

--------------------------------

### Initialize SolidStart Project with Various Package Managers

Source: https://docs.solidjs.com/solid-start/getting-started

This command initializes a new SolidStart project using different package managers like npm, pnpm, yarn, bun, and deno. It prompts the user to choose a project name and a template.

```bash
npm init solid@latest

```

```bash
pnpm create solid@latest

```

```bash
yarn create solid@latest

```

```bash
bun create solid@latest

```

```bash
deno init --npm solid@latest

```

--------------------------------

### Setup Router Component in SolidJS

Source: https://docs.solidjs.com/guides/routing-and-navigation

Demonstrates how to set up the main Router component in a SolidJS application to match URLs and display the desired pages. It requires importing `render` from 'solid-js/web' and `Router` from '@solidjs/router'.

```jsx
import { render } from "solid-js/web";
import { Router } from "@solidjs/router";

render(() => <Router />, document.getElementById("root"));
```

--------------------------------

### Show Optimistic UI with SolidJS Router Actions

Source: https://docs.solidjs.com/solid-start/guides/data-mutation

This example demonstrates how to implement optimistic UI updates in SolidJS Router actions. It uses the `useSubmission` hook to access the `pending` and `input` properties, allowing the UI to reflect changes before the server responds. It also fetches and displays a list of posts.

```typescript
import { For, Show } from "solid-js";
import { action, useSubmission, query, createAsync } from "@solidjs/router";

const getPosts = query(async () => {
  const posts = await fetch("https://my-api.com/blog");
  return await posts.json();
}, "posts");

const addPost = action(async (formData: FormData) => {
  const title = formData.get("title");
  await fetch("https://my-api.com/posts", {
    method: "POST",
    body: JSON.stringify({ title }),
  });
}, "addPost");

export default function Page() {
  const posts = createAsync(() => getPosts());
  const submission = useSubmission(addPost);
  return (
    <>
      <form action={addPost}>
        <input type="text" name="title" />
        <button type="submit" disabled={submission.pending}>Add Post</button>
      </form>
      <ul>
        <For each={posts() ?? []}>{(post) => <li>{post.title}</li>}</For>
        <Show when={submission.input?.[0]?.get("title")}><li class="opacity-50">{submission.input?.[0]?.get("title")?.toString()}</li></Show>
      </ul>
    </>
  );
}
```

```javascript
import { For, Show } from "solid-js";
import { action, useSubmission, query, createAsync } from "@solidjs/router";

const getPosts = query(async () => {
  const posts = await fetch("https://my-api.com/blog");
  return await posts.json();
}, "posts");

const addPost = action(async (formData) => {
  const title = formData.get("title");
  await fetch("https://my-api.com/posts", {
    method: "POST",
    body: JSON.stringify({ title }),
  });
}, "addPost");

export default function Page() {
  const posts = createAsync(() => getPosts());
  const submission = useSubmission(addPost);
  return (
    <>
      <form action={addPost}>
        <input type="text" name="title" />
        <button type="submit" disabled={submission.pending}>Add Post</button>
      </form>
      <ul>
        <For each={posts() ?? []}>{(post) => <li>{post.title}</li>}</For>
        <Show when={submission.input?.[0]?.get("title")}><li class="opacity-50">{submission.input?.[0]?.get("title")?.toString()}</li></Show>
      </ul>
    </>
  );
}
```

--------------------------------

### Default SolidStart Project File Structure

Source: https://docs.solidjs.com/solid-start/getting-started

This illustrates the default directory and file structure generated by SolidStart. It includes public assets, source code for routes, client and server entry points, and the application root.

```text
public/
src/
  ├── routes/
  │   ├── index.tsx
  ├── entry-client.tsx
  ├── entry-server.tsx
  ├── app.tsx

```

--------------------------------

### Inject Head Tags with SolidJS Meta Components

Source: https://docs.solidjs.com/solid-meta/getting-started/client-setup

Demonstrates how to inject head tag components such as Title, Link, and Meta into the document's head using SolidJS Meta. This setup requires no special client-side configurations.

```jsx
import { MetaProvider, Title, Link, Meta } from "@solidjs/meta";

const App = () => (
  <MetaProvider>
    {/* Content */}
    <Title>Page Title</Title>
    <Meta name="description" content="A description" />
    <Link rel="stylesheet" href="/style.css" />
  </MetaProvider>
);
```

--------------------------------

### Install Zerops CLI globally with npm

Source: https://docs.solidjs.com/guides/deployment-options/zerops

Installs the Zerops CLI globally using npm, making the `zcli` command available system-wide for managing Zerops deployments.

```bash
npm i @zerops/zcli -g
```

--------------------------------

### Install Netlify CLI with Various Package Managers

Source: https://docs.solidjs.com/guides/deployment-options/netlify

This snippet demonstrates how to install the Netlify CLI globally using different package managers like npm, pnpm, yarn, bun, and deno. Ensure you have your Netlify account and team set up before proceeding with project initialization.

```npm
npm i netlify-cli -g
```

```pnpm
pnpm i netlify-cli -g
```

```yarn
yarn add netlify-cli -g
```

```bun
bun i netlify-cli -g
```

```deno
deno add npm:netlify-cli -g
```

--------------------------------

### Install Zerops CLI globally with pnpm

Source: https://docs.solidjs.com/guides/deployment-options/zerops

Installs the Zerops CLI globally using pnpm, making the `zcli` command available system-wide for managing Zerops deployments.

```bash
pnpm i @zerops/zcli -g
```

--------------------------------

### SolidStart App with Routing - app.tsx

Source: https://docs.solidjs.com/solid-start/reference/entrypoints/app

This example demonstrates setting up routing within the main App component using FileRoutes from '@solidjs/start/router'. It includes basic navigation links and a Suspense boundary for handling asynchronous operations.

```typescript
import { A, Router } from "@solidjs/router";
import { FileRoutes } from "@solidjs/start/router";
import { Suspense } from "solid-js";

export default function App() {
  return (
    <Router
      root={{
        get children() {
          return (
            <>
              <header>
                <nav>
                  <A href="/">Index</A>
                  <A href="/about">About</A>
                </nav>
              </header>
              <main>
                <Suspense>{FileRoutes()}</Suspense>
              </main>
            </>
          );
        },
      }}
    />
  );
}
```

--------------------------------

### SolidJS Router Initialization with Preloaded Data

Source: https://docs.solidjs.com/guides/routing-and-navigation

Shows a complete example of initializing the SolidJS router, including lazy-loading route components and setting up preload functions for data fetching. The `render` function from `solid-js/web` is used to mount the application.

```jsx
import { lazy } from "solid-js";
import { render } from "solid-js/web";
import { Router, Route } from "@solidjs/router";
import { preloadUser } from "./pages/users/[id].data.js";

const Home = lazy(() => import("./pages/Home"));
const User = lazy(() => import("./pages/users/[id]"));

render(
  () => (
    <Router>
      <Route path="/" component={Home} />
      {/* Route with preload function and dynamic parameter */}
      <Route path="/users/:id" component={User} preload={preloadUser} />
    </Router>
  ),
  document.getElementById("root")
);
```

--------------------------------

### API Routes - Exposing a GraphQL API

Source: https://docs.solidjs.com/solid-start/building-your-application/api-routes

Guide on implementing a GraphQL API within SolidStart using the `graphql` function, requiring a schema and resolvers.

```APIDOC
## Exposing a GraphQL API

### Description
SolidStart simplifies the implementation of GraphQL APIs. This involves defining a GraphQL schema and resolvers, then using the `graphql` function to create an API route handler.

### Prerequisites
- Install the `graphql` library:
  ```bash
  npm install graphql
  # or
  yarn add graphql
  # or
  pnpm add graphql
  ```

### Implementation Steps
1. **Define your GraphQL Schema:** Create a schema string that outlines your data types and queries.
2. **Create Resolvers:** Implement functions that fetch the data for each field in your schema.
3. **Use the `graphql` function:** Pass your schema and resolvers to the `graphql` function provided by SolidStart (or a similar library).

### Example Structure

```javascript
// Example: api/graphql.ts
import { graphql } from "@solidjs/start/server/graphql"; // Assuming this path
import schema from "./schema"; // Your GraphQL schema definition
import resolvers from "./resolvers"; // Your resolver functions

export const POST = graphql(schema, resolvers);
```

### Usage
This setup allows clients to send GraphQL queries to the `/api/graphql` endpoint (or whichever path you define) and receive structured JSON responses based on your schema and resolvers.
```

--------------------------------

### SolidJS createStore Setter Examples

Source: https://docs.solidjs.com/reference/store-utilities/create-store

Provides examples of updating a SolidJS store using the setter function. It covers direct object updates for shallow merging and functional updates that receive the previous state. It also shows how to delete properties by setting them to `undefined`.

```javascript
const [state, setState] = createStore({
  firstName: "John",
  lastName: "Miller",
});

setState({ firstName: "Johnny", middleName: "Lee" }); // ({ firstName: 'Johnny', middleName: 'Lee', lastName: 'Miller' })

setState((state) => ({ preferredName: state.firstName, lastName: "Milner" })); // ({ firstName: 'Johnny', preferredName: 'Johnny', middleName: 'Lee', lastName: 'Milner' })
```

--------------------------------

### Install Vitest Coverage Package

Source: https://docs.solidjs.com/guides/testing

Instructions for installing the necessary package to enable coverage collection in Vitest. It provides commands for common package managers like npm, pnpm, yarn, bun, and deno.

```bash
npm i @vitest/coverage-v8 -D
```

```bash
pnpm i @vitest/coverage-v8 -D
```

```bash
yarn add @vitest/coverage-v8 -D
```

```bash
bun i @vitest/coverage-v8 -d
```

```bash
deno add npm:@vitest/coverage-v8 -D
```

--------------------------------

### Pass Additional Arguments to SolidStart Actions (JS)

Source: https://docs.solidjs.com/solid-start/guides/data-mutation

This JavaScript example illustrates passing extra arguments to SolidStart actions via the `with` method. It defines an action accepting `userId` and form data for submission.

```javascript
import { action } from "@solidjs/router";

const addPost = action(async (userId, formData) => {
  const title = formData.get("title");
  await fetch("https://my-api.com/posts", {
    method: "POST",
    body: JSON.stringify({ userId, title }),
  });
}, "addPost");

export default function Page() {
  const userId = 1;
  return (
    <form method="post" action={addPost.with(userId)}>
      <input type="text" name="title" />
      <button type="submit">Add Post</button>
    </form>
  );
}
```

--------------------------------

### Install TypeScript with bun

Source: https://docs.solidjs.com/configuration/typescript

Command to install TypeScript as a development dependency in a Solid.js project using bun.

```bash
bun i typescript -d
```

--------------------------------

### SolidJS Store unwrap Function Example

Source: https://docs.solidjs.com/reference/store-utilities/unwrap

Demonstrates how to import and use the 'unwrap' function from 'solid-js/store' to get the underlying data of a SolidJS store. It shows the type signature for the function.

```typescript
import { unwrap } from "solid-js/store"
import type { Store } from "solid-js/store"

function unwrap<T>(store: Store<T>): T
```

--------------------------------

### HashRouter Setup in SolidJS Application

Source: https://docs.solidjs.com/solid-router/reference/components/hash-router

This code snippet demonstrates the basic setup of the HashRouter in a SolidJS application. It imports necessary components from '@solidjs/router' and renders the application with routes defined. The HashRouter is used as the top-level component to manage routing.

```javascript
import { render } from "solid-js/web";
import { HashRouter, Route } from "@solidjs/router";

const App = (props) => (
  <>
    {/* Root header */}
    {props.children}
  </>);

render(() => {
  /* ... routes */
}, document.getElementById("app"));
```

--------------------------------

### Install TypeScript with deno

Source: https://docs.solidjs.com/configuration/typescript

Command to install TypeScript as a development dependency in a Solid.js project using deno.

```bash
deno add npm:typescript -D
```

--------------------------------

### Server-side Data Fetching with @solidjs/router (JavaScript)

Source: https://docs.solidjs.com/solid-start/building-your-application/data-loading

Demonstrates server-side data fetching in SolidStart using JavaScript with `@solidjs/router`. It utilizes `createAsync` and `query` for efficient data loading and `route.preload()` for prefetching. The example fetches user data and displays names, optimizing performance by reducing client-side waterfalls.

```javascript
// /routes/users.jsx
import { For } from "solid-js";
import { createAsync, query } from "@solidjs/router";
const getUsers = query(async () => {
  const response = await fetch("https://example.com/users");
  return (await response.json());
}, "users");
export const route = {
  preload: () => getUsers(),
};
export default function Page() {
  const users = createAsync(() => getUsers());
  return (
    <For each={users()}>
      {(user) => <div>{user.name}</div>}
    </For>
  );
}
```

--------------------------------

### Install Zerops CLI globally with yarn

Source: https://docs.solidjs.com/guides/deployment-options/zerops

Installs the Zerops CLI globally using yarn, making the `zcli` command available system-wide for managing Zerops deployments.

```bash
yarn add @zerops/zcli -g
```

--------------------------------

### Show Pending UI with SolidStart Actions (JS)

Source: https://docs.solidjs.com/solid-start/guides/data-mutation

This JavaScript example shows how to implement pending UI feedback for SolidStart actions using `useSubmission`. It dynamically updates button text based on whether the action is currently executing.

```javascript
import { action, useSubmission } from "@solidjs/router";

const addPost = action(async (formData) => {
  const title = formData.get("title");
  await fetch("https://my-api.com/posts", {
    method: "POST",
    body: JSON.stringify({ title }),
  });
}, "addPost");

export default function Page() {
  const submission = useSubmission(addPost);
  return (
    <form method="post" action={addPost}>
      <input type="text" name="title" />
      <button type="submit">
        {submission.pending ? "Adding..." : "Add Post"}
      </button>
    </form>
  );
}
```

--------------------------------

### Install Testing Packages (bun)

Source: https://docs.solidjs.com/guides/testing

Installs the essential development dependencies for testing SolidJS applications using bun. This includes the testing framework, DOM environment, and helper libraries for component interaction and assertions.

```bash
bun i vitest jsdom @solidjs/testing-library @testing-library/user-event @testing-library/jest-dom -d
```

--------------------------------

### SolidJS createResource Fetcher Function Example

Source: https://docs.solidjs.com/reference/basic-reactivity/create-resource

An example of an asynchronous fetcher function used with `createResource`. It accepts a source value and an info object containing the last fetched `value` and a `refetching` flag. The function should return the fetched data.

```javascript
async function fetchData(source, { value, refetching }) {
  // Fetch the data and return a value.
  // `source` tells you the current value of the source signal;
  // `value` tells you the last returned value of the fetcher;
  // `refetching` is true when the fetcher is triggered by calling `refetch()`,
  // or equal to the optional data passed: `refetch(info)`
}
```

--------------------------------

### Install Testing Packages (deno)

Source: https://docs.solidjs.com/guides/testing

Installs the essential development dependencies for testing SolidJS applications using deno. This includes the testing framework, DOM environment, and helper libraries for component interaction and assertions.

```bash
deno add npm:vitest jsdom @solidjs/testing-library @testing-library/user-event @testing-library/jest-dom -D
```

--------------------------------

### Handle Errors in SolidStart Actions (JS)

Source: https://docs.solidjs.com/solid-start/guides/data-mutation

This JavaScript example demonstrates how to handle errors within SolidStart actions using `useSubmission`. It conditionally renders an error message if the action fails.

```javascript
import { Show } from "solid-js";
import { action, useSubmission } from "@solidjs/router";

const addPost = action(async (formData) => {
  const title = formData.get("title");
  await fetch("https://my-api.com/posts", {
    method: "POST",
    body: JSON.stringify({ title }),
  });
}, "addPost");

export default function Page() {
  const submission = useSubmission(addPost);
  return (
    <>
      <Show when={submission.error}>
        <p style="color: red;">{submission.error.message}</p>
      </Show>
      <form method="post" action={addPost}>
        <input type="text" name="title" />
        <button type="submit">Add Post</button>
      </form>
    </>
  );
}
```

--------------------------------

### Install Testing Packages (npm)

Source: https://docs.solidjs.com/guides/testing

Installs the essential development dependencies for testing SolidJS applications using npm. This includes the testing framework, DOM environment, and helper libraries for component interaction and assertions.

```bash
npm i vitest jsdom @solidjs/testing-library @testing-library/user-event @testing-library/jest-dom -D
```

--------------------------------

### Pass Additional Arguments to SolidStart Actions (TS)

Source: https://docs.solidjs.com/solid-start/guides/data-mutation

This TypeScript example shows how to pass additional arguments to SolidStart actions using the `with` method. It includes an action that accepts a `userId` and form data for posting.

```typescript
import { action } from "@solidjs/router";

const addPost = action(async (userId: number, formData: FormData) => {
  const title = formData.get("title") as string;
  await fetch("https://my-api.com/posts", {
    method: "POST",
    body: JSON.stringify({ userId, title }),
  });
}, "addPost");

export default function Page() {
  const userId = 1;
  return (
    <form method="post" action={addPost.with(userId)}>
      <input type="text" name="title" />
      <button type="submit">Add Post</button>
    </form>
  );
}
```

--------------------------------

### Install Macaron CSS for Solid.js

Source: https://docs.solidjs.com/guides/styling-components/macaron

These commands show how to install the necessary Macaron CSS packages for Solid.js using different package managers like npm, pnpm, yarn, bun, and deno. Ensure you have the core and solid specific packages installed.

```bash
npm i @macaron-css/core @macaron-css/solid
```

```bash
pnpm i @macaron-css/core @macaron-css/solid
```

```bash
yarn add @macaron-css/core @macaron-css/solid
```

```bash
bun i @macaron-css/core @macaron-css/solid
```

```bash
deno add npm:@macaron-css/core @macaron-css/solid
```

--------------------------------

### Install Tailwind CSS (deno)

Source: https://docs.solidjs.com/guides/styling-components/tailwind

Installs Tailwind CSS, the PostCSS plugin for Tailwind, and PostCSS as development dependencies using deno.

```bash
deno add npm:tailwindcss @tailwindcss/postcss postcss -D
```

--------------------------------

### Install TypeScript with npm

Source: https://docs.solidjs.com/configuration/typescript

Command to install TypeScript as a development dependency in a Solid.js project using npm.

```bash
npm i typescript -D
```

--------------------------------

### SolidJS Switch/Match Example for Basic Routing

Source: https://docs.solidjs.com/reference/components/switch-and-match

Demonstrates a practical use case of the SolidJS Switch and Match components for implementing basic routing logic. It shows how to conditionally render different components based on a 'route' prop.

```jsx
<Switch fallback={<NotFound />}>
  <Match when={route === '/'}>Home</Match>
  <Match when={route === '/about'}>About</Match>
  <Match when={route === '/contact'}>Contact</Match>
</Switch>
```

--------------------------------

### Install Zerops CLI with Curl (Linux/macOS)

Source: https://docs.solidjs.com/guides/deployment-options/zerops

This command uses curl to download and execute the installation script for the Zerops CLI on Linux and macOS systems, enabling manual deployment triggers.

```bash
curl -L https://zerops.io/zcli/install.sh | sh
```

--------------------------------

### Server-Only Database Interaction with SolidJS Router Actions

Source: https://docs.solidjs.com/solid-start/guides/data-mutation

This example shows how to ensure database operations within a SolidJS Router action are server-only. By adding `"use server";` as the first line of the action, you prevent it from running on the client, thus protecting sensitive database credentials and logic.

```typescript
import { action } from "@solidjs/router";
import { db } from "~/lib/db"; // Assuming db is imported from a local library

const addPost = action(async (formData: FormData) => {
  "use server"; // This line ensures the action runs only on the server
  const title = formData.get("title") as string;
  await db.insert("posts").values({ title });
}, "addPost");

export default function Page() {
  return (
    <form action={addPost}>
      <input type="text" name="title" />
      <button type="submit">Add Post</button>
    </form>
  );
}
```

```javascript
import { action } from "@solidjs/router";
import { db } from "~/lib/db"; // Assuming db is imported from a local library

const addPost = action(async (formData) => {
  "use server"; // This line ensures the action runs only on the server
  const title = formData.get("title");
  await db.insert("posts").values({ title });
}, "addPost");

export default function Page() {
  return (
    <form action={addPost}>
      <input type="text" name="title" />
      <button type="submit">Add Post</button>
    </form>
  );
}
```

--------------------------------

### Install Testing Packages (pnpm)

Source: https://docs.solidjs.com/guides/testing

Installs the essential development dependencies for testing SolidJS applications using pnpm. This includes the testing framework, DOM environment, and helper libraries for component interaction and assertions.

```bash
pnpm i vitest jsdom @solidjs/testing-library @testing-library/user-event @testing-library/jest-dom -D
```

--------------------------------

### SolidStart: Catch-all Route Example

Source: https://docs.solidjs.com/solid-start/building-your-application/routing

Illustrates the implementation of a catch-all route in SolidStart using the `[...post].tsx` file naming convention. This route captures all remaining path segments as a single parameter, which can be accessed using `useParams`. This is suitable for blog or dynamic content fetching.

```typescript
import { useParams } from "@solidjs/router";

export default function BlogPage() {
  const params = useParams();
  return (
    <div>
      Blog {params.post}
    </div>
  );
}
```

--------------------------------

### Install Railway CLI using different package managers

Source: https://docs.solidjs.com/guides/deployment-options/railway

This section provides commands for installing the Railway CLI globally using various package managers like npm, pnpm, yarn, bun, and deno. Ensure you have the correct package manager installed for your environment.

```bash
npm i @railway/cli -g
```

```bash
pnpm i @railway/cli -g
```

```bash
yarn add @railway/cli -g
```

```bash
bun i @railway/cli -g
```

```bash
deno add npm:@railway/cli -g
```

--------------------------------

### Solid Router: Basic Nested Route Example

Source: https://docs.solidjs.com/solid-router/concepts/nesting

Demonstrates a basic nested route structure in Solid Router where a parent route and a child route share a common path prefix. This setup ensures the parent component renders for the parent path, and the child component renders for a more specific sub-path.

```typescript
import { Route } from "@solidjs/router";

<Route path="/users/:id" component={User} />

// is equivalent to

<Route path="/users" component={Users}>
  <Route path="/:id" component={User} />
</Route>
```

--------------------------------

### SolidStart Routing with solid-router using FileRoutes

Source: https://docs.solidjs.com/solid-start/reference/routing/file-routes

This example demonstrates how to use the FileRoutes component from SolidStart with the solid-router library to define routes based on the file structure. It includes Suspense for handling asynchronous operations.

```tsx
import { Suspense } from "solid-js";
import { Router } from "@solidjs/router";
import { FileRoutes } from "@solidjs/start/router";

export default function App() {
  return (
    <main>
      <Router
        root={({ children }) => (
          <>
            <header>
              <A href="/">Home</A>
              <A href="/about">About</A>
              <A href="/blog">Blog</A>
            </header>
            <Suspense>{children}</Suspense>
          </>
        )}
      >
        <FileRoutes />
      </Router>
    </main>
  );
}
```

--------------------------------

### Install TypeScript with pnpm

Source: https://docs.solidjs.com/configuration/typescript

Command to install TypeScript as a development dependency in a Solid.js project using pnpm.

```bash
pnpm i typescript -D
```

--------------------------------

### Install Tailwind CSS (bun)

Source: https://docs.solidjs.com/guides/styling-components/tailwind

Installs Tailwind CSS, the PostCSS plugin for Tailwind, and PostCSS as development dependencies using bun.

```bash
bun i tailwindcss @tailwindcss/postcss postcss -d
```

--------------------------------

### Solid Router: Programmatic Navigation with `useNavigate`

Source: https://docs.solidjs.com/solid-router/concepts/navigation

Shows how to use the `useNavigate` primitive for programmatic navigation. The example demonstrates navigating to '/dashboard' after a login action and using `replace: true` to modify the browser history.

```javascript
import { useNavigate } from "@solidjs/router";

function LoginPage() {
  const navigate = useNavigate();

  return (
    <button onClick={() => {
      // Login logic
      navigate("/dashboard", { replace: true });
    }}>
      Login
    </button>
  );
}
```

--------------------------------

### SolidJS Index Component Example Usage

Source: https://docs.solidjs.com/reference/components/index-component

Illustrates how to use the SolidJS Index component. This example shows rendering a list where each item is displayed, and the item itself is a signal. It also demonstrates using the index as the second argument in the children's render function.

```javascript
<Index each={['A', 'B', 'C']} fallback={<div>Loading...</div>}>
  {(item) => (
    <div>{item()}</div>
  )}
</Index>

<Index each={['A', 'B', 'C']} fallback={<div>Loading...</div>}>
  {(item, index) => (
    <div >#{index} {item()}</div>
  )}
</Index>
```

--------------------------------

### Install TypeScript with yarn

Source: https://docs.solidjs.com/configuration/typescript

Command to install TypeScript as a development dependency in a Solid.js project using yarn.

```bash
yarn add typescript -D
```

--------------------------------

### Importing CSS in SolidStart Component

Source: https://docs.solidjs.com/solid-start/building-your-application/css-and-styling

Demonstrates how to import a CSS file directly alongside a Solid component. This method applies global styles from the imported CSS file to the component.

```tsx
import "./Card.css";

const Card = (props) => {
  return (
    <div class="card">
      <h1>{props.title}</h1>
      <p>{props.text}</p>
    </div>
  );
};
```

--------------------------------

### Install SASS with bun

Source: https://docs.solidjs.com/guides/styling-components/sass

Installs SASS as a development dependency using the bun runtime and package manager. This is a fast alternative for JavaScript development.

```bash
bun i sass -d
```

--------------------------------

### Install SASS with deno

Source: https://docs.solidjs.com/guides/styling-components/sass

Installs SASS from npm as a development dependency using deno. This allows deno users to leverage npm packages.

```bash
deno add npm:sass -D
```

--------------------------------

### API Route with Dynamic Parameters and Data Fetching (SolidStart)

Source: https://docs.solidjs.com/solid-start/building-your-application/api-routes

This example demonstrates an API route in SolidStart that accepts dynamic route parameters (e.g., category and brand) and uses them to fetch data from a store. It showcases accessing params and performing asynchronous operations.

```typescript
import type { APIEvent } from "@solidjs/start/server";
import store from "./store";

export async function GET({ params }: APIEvent) {
  console.log(`Category: ${params.category}, Brand: ${params.brand}`);
  const products = await store.getProducts(params.category, params.brand);
  return products;
}
```

--------------------------------

### Install Tailwind CSS (npm)

Source: https://docs.solidjs.com/guides/styling-components/tailwind

Installs Tailwind CSS, the PostCSS plugin for Tailwind, and PostCSS as development dependencies using npm.

```bash
npm i tailwindcss @tailwindcss/postcss postcss -D
```

--------------------------------

### Install SASS with npm

Source: https://docs.solidjs.com/guides/styling-components/sass

Installs SASS as a development dependency in your project using npm. This command is typically run once to set up SASS compilation capabilities.

```bash
npm i sass -D
```

--------------------------------

### SolidJS createStore Getter Example

Source: https://docs.solidjs.com/reference/store-utilities/create-store

Illustrates using getters within a SolidJS store to define derived values. The example shows a `fullName` getter that dynamically combines `firstName` and `lastName` from the store's user object.

```javascript
const [state, setState] = createStore({
  user: {
    firstName: "John",
    lastName: "Smith",
    get fullName() {
      return `${this.firstName} ${this.lastName}`;
    },
  },
});
```

--------------------------------

### Install Testing Packages (yarn)

Source: https://docs.solidjs.com/guides/testing

Installs the essential development dependencies for testing SolidJS applications using yarn. This includes the testing framework, DOM environment, and helper libraries for component interaction and assertions.

```bash
yarn add vitest jsdom @solidjs/testing-library @testing-library/user-event @testing-library/jest-dom -D
```

--------------------------------

### Install Tailwind CSS (yarn)

Source: https://docs.solidjs.com/guides/styling-components/tailwind

Installs Tailwind CSS, the PostCSS plugin for Tailwind, and PostCSS as development dependencies using yarn.

```bash
yarn add tailwindcss @tailwindcss/postcss postcss -D
```

--------------------------------

### Login to Vercel CLI

Source: https://docs.solidjs.com/guides/deployment-options/vercel

Command to log in to your Vercel account using the Vercel CLI. After installation, this command initiates the authentication process, allowing you to deploy projects from your local environment.

```shell
vercel
```

--------------------------------

### Install LESS Dev Dependency for SolidJS

Source: https://docs.solidjs.com/guides/styling-components/less

This snippet shows the commands to install LESS as a development dependency in a SolidJS project using different package managers like npm, pnpm, yarn, bun, and deno. Ensure you have the respective package manager installed.

```bash
npm i less -D
```

```bash
pnpm i less -D
```

```bash
yarn add less -D
```

```bash
bun i less -d
```

```bash
deno add npm:less -D
```

--------------------------------

### Install Wrangler CLI

Source: https://docs.solidjs.com/guides/deployment-options/cloudflare

Installs the Wrangler command-line tool globally using various package managers. Wrangler is used for building and deploying Cloudflare Workers and Pages.

```npm
npm i wrangler -g
```

```pnpm
pnpm i wrangler -g
```

```yarn
yarn add wrangler -g
```

```bun
bun i wrangler -g
```

```deno
deno add npm:wrangler -g
```

--------------------------------

### SolidJS MemoryRouter Setup with MemoryHistory

Source: https://docs.solidjs.com/solid-router/reference/components/memory-router

Demonstrates how to set up and use the MemoryRouter with a pre-configured MemoryHistory object in SolidJS. This allows for programmatic navigation and control over the routing state.

```javascript
import { MemoryRouter, createMemoryHistory, A } from "@solidjs/router";
import { Suspense } from "solid-js";

export default function App() {
  const history = createMemoryHistory();
  const toHome = () => {
    history.set({ value: "/" });
  };
  const toAbout = () => {
    history.set({ value: "/about" });
  };

  return (
    <>
      <button onClick={toHome}>Home</button>
      <button onClick={toAbout}>About</button>
      <MemoryRouter history={history}>
        <p>Current route: {history.get()}</p>
        {/* Add your routes here, e.g., <Route path="/" component={Home} /> */}
        <A href="/">Go to /</A>
        <A href="/about">Go to /about</A>
      </MemoryRouter>
    </>
  );
}
```

--------------------------------

### Install Tailwind CSS (pnpm)

Source: https://docs.solidjs.com/guides/styling-components/tailwind

Installs Tailwind CSS, the PostCSS plugin for Tailwind, and PostCSS as development dependencies using pnpm.

```bash
pnpm i tailwindcss @tailwindcss/postcss postcss -D
```

--------------------------------

### Install Zerops CLI with Invoke-Expression (Windows)

Source: https://docs.solidjs.com/guides/deployment-options/zerops

This PowerShell command uses Invoke-Expression to download and execute the Zerops CLI installation script on Windows, facilitating manual deployment triggers.

```powershell
irm https://zerops.io/zcli/install.ps1 | iex
```

--------------------------------

### SCSS Syntax Example

Source: https://docs.solidjs.com/guides/styling-components/sass

An example of SCSS syntax for styling elements like grids, centering content, and cards. SCSS is a superset of CSS and offers enhanced features.

```scss
.grid {
  display: grid;
  &-center {
    place-items: center;
  }
}
.screen {
  min-height: 100vh;
}
.card {
  height: 160px;
  aspect-ratio: 2;
  border-radius: 16px;
  background-color: white;
  box-shadow: 0 0 0 4px hsl(0 0% 0% / 15%);
}
```

--------------------------------

### SolidStart App without Routing - app.tsx

Source: https://docs.solidjs.com/solid-start/reference/entrypoints/app

A minimal example of the App component in SolidStart that does not include routing. It simply renders a basic 'Hello world!' template, suitable for applications where routing is handled elsewhere or not required.

```typescript
export default function App() {
  return (
    <>
      Hello world!
      ============
    </>
  );
}
```

--------------------------------

### SolidJS: Initiate Transition with startTransition

Source: https://docs.solidjs.com/reference/reactive-utilities/start-transition

The `startTransition` function from 'solid-js' allows you to start a transition directly. It takes a callback function as an argument and returns a Promise. This is useful when you don't need to track the pending state associated with a transition.

```typescript
import { startTransition } from "solid-js"

function startTransition(fn: () => void): Promise<void>
```

--------------------------------

### Create CatchAll (404) Route in SolidJS

Source: https://docs.solidjs.com/guides/routing-and-navigation

Demonstrates how to implement a catch-all route for handling 404 Not Found pages in SolidJS applications. The `*` path captures the rest of the URL, and an optional parameter name can be added. Includes `NotFound` component example.

```jsx
import { render } from "solid-js/web";
import { Router, Route } from "@solidjs/router";
import Home from "./pages/Home";
import Users from "./pages/Users";
import NotFound from "./pages/NotFound";

const App = (props) => (
  <>
    {/* Site Title */}
    {props.children}
  </>
);

render(
  () => (
    <Router>
      <App>
        <Route path="/" component={Home} />
        <Route path="/users" component={Users} />
        <Route path="*" component={NotFound} />
      </App>
    </Router>
  ),
  document.getElementById("root")
);
```

--------------------------------

### SolidJS Synchronous Reactivity Example

Source: https://docs.solidjs.com/concepts/intro-to-reactivity

Illustrates synchronous reactivity in SolidJS, where dependent signals are updated immediately and in order after a change. This ensures derived signals are always up-to-date.

```javascript
const [count, setCount] = createSignal(0);
const [double, setDouble] = createSignal(0);

createEffect(() => {
  setDouble(count() * 2);
});

// When count changes, double is updated immediately and in order.
```