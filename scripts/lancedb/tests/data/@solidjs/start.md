# SolidJS

SolidJS is a declarative JavaScript library for building user interfaces with fine-grained reactivity. Instead of using a Virtual DOM, it compiles JSX templates to real DOM nodes and updates them with precise, surgical reactivity. The library uses a render-once mental model where component functions execute only once to set up the view, while reactive primitives like signals, memos, and effects handle all subsequent updates automatically through dependency tracking.

At its core, SolidJS provides a powerful reactive system that efficiently manages state and side effects. Components are regular JavaScript functions that return JSX, and the framework's compiler transforms this JSX into optimized DOM operations. With a size of under 7KB minified and gzipped, SolidJS delivers performance comparable to vanilla JavaScript while providing a developer experience similar to React. The library supports modern features including Suspense, streaming SSR, progressive hydration, Error Boundaries, concurrent rendering, Context API, and first-class TypeScript support.

## Reactive Primitives

### createSignal - Create reactive state with getter and setter

Creates the most basic reactive primitive for managing state. Returns a tuple with a getter (accessor) function and a setter function. The getter automatically tracks dependencies when called inside reactive contexts, and the setter triggers updates only to dependent computations.

```typescript
import { createSignal, createEffect } from "solid-js";

// Basic counter with type inference
const [count, setCount] = createSignal(0);
console.log(count()); // 0

// Update with a value
setCount(5);
console.log(count()); // 5

// Update with a function (receives previous value)
setCount(prev => prev + 1);
console.log(count()); // 6

// Signal with custom equality function
const [user, setUser] = createSignal(
  { name: "John", age: 30 },
  { equals: (prev, next) => prev.name === next.name && prev.age === next.age }
);

// Automatic dependency tracking in effects
createEffect(() => {
  console.log(`Count is now: ${count()}`);
});

setCount(10); // Logs: "Count is now: 10"

// Signal without initial value (type becomes T | undefined)
const [data, setData] = createSignal<string>();
console.log(data()); // undefined
setData("hello");
console.log(data()); // "hello"
```

### createMemo - Create derived reactive state

Creates a read-only derived signal that memoizes computed values. Only re-evaluates when its dependencies change, and only notifies subscribers if the computed value is different from the previous one.

```typescript
import { createSignal, createMemo, createEffect } from "solid-js";

const [firstName, setFirstName] = createSignal("John");
const [lastName, setLastName] = createSignal("Doe");

// Derived state that automatically updates
const fullName = createMemo(() => `${firstName()} ${lastName()}`);

createEffect(() => {
  console.log(fullName()); // "John Doe"
});

setFirstName("Jane");
// Effect runs, logs: "Jane Doe"

// Memo with initial value and custom equality
const [numbers, setNumbers] = createSignal([1, 2, 3, 4, 5]);

const sum = createMemo(
  (prev = 0) => {
    const nums = numbers();
    return nums.reduce((acc, n) => acc + n, 0);
  },
  0,
  { equals: (a, b) => a === b }
);

console.log(sum()); // 15

setNumbers([2, 3, 4, 5, 6]);
console.log(sum()); // 20

// Memos prevent unnecessary recomputation
const [expensive, setExpensive] = createSignal(100);
const doubled = createMemo(() => {
  console.log("Computing doubled...");
  return expensive() * 2;
});

// Accessing multiple times only computes once
console.log(doubled()); // Logs "Computing doubled...", returns 200
console.log(doubled()); // Returns 200 (no log, uses cached value)
console.log(doubled()); // Returns 200 (no log, uses cached value)
```

### createEffect - Run side effects reactively

Creates a reactive computation that runs after the render phase. Automatically tracks dependencies and re-runs when they change. Use for side effects like logging, DOM manipulation, or subscriptions.

```typescript
import { createSignal, createEffect, onCleanup } from "solid-js";

const [count, setCount] = createSignal(0);
const [enabled, setEnabled] = createSignal(true);

// Basic effect with automatic dependency tracking
createEffect(() => {
  console.log(`Current count: ${count()}`);
});

setCount(5); // Logs: "Current count: 5"

// Effect with cleanup
createEffect(() => {
  if (!enabled()) return;

  const interval = setInterval(() => {
    setCount(c => c + 1);
  }, 1000);

  // Cleanup runs before re-execution or disposal
  onCleanup(() => {
    clearInterval(interval);
    console.log("Interval cleared");
  });
});

// Effect with previous value tracking
createEffect((prevCount = 0) => {
  const currentCount = count();
  console.log(`Changed from ${prevCount} to ${currentCount}`);
  return currentCount;
});

// Conditional subscription based on signal
const [userId, setUserId] = createSignal<string | null>(null);

createEffect(() => {
  const id = userId();
  if (!id) return;

  const unsubscribe = subscribeToUser(id, (data) => {
    console.log("User updated:", data);
  });

  onCleanup(unsubscribe);
});

setUserId("user-123"); // Subscribes to user-123
setUserId("user-456"); // Unsubscribes from user-123, subscribes to user-456
setUserId(null); // Unsubscribes from user-456

function subscribeToUser(id: string, callback: (data: any) => void) {
  console.log(`Subscribed to ${id}`);
  return () => console.log(`Unsubscribed from ${id}`);
}
```

### createResource - Manage async data with Suspense integration

Creates a reactive resource for handling asynchronous data fetching with built-in loading states, error handling, and Suspense integration. Returns a resource accessor and control functions for refetching and mutation.

```typescript
import { createSignal, createResource, Suspense, ErrorBoundary } from "solid-js";
import { render } from "solid-js/web";

// Simple resource without source
const [data] = createResource(async () => {
  const response = await fetch("https://api.example.com/data");
  if (!response.ok) throw new Error("Failed to fetch");
  return response.json();
});

// Resource with reactive source
const [userId, setUserId] = createSignal("123");

const [user, { mutate, refetch }] = createResource(userId, async (id) => {
  const response = await fetch(`https://api.example.com/users/${id}`);
  return response.json();
});

// Access resource states
console.log(user.state); // "pending" | "ready" | "refreshing" | "errored" | "unresolved"
console.log(user.loading); // boolean
console.log(user.error); // Error | undefined
console.log(user.latest); // Latest value, even during refresh

// Manually update resource
mutate({ name: "John", id: "123" });

// Refetch with custom info
refetch("manual-refresh");

// Resource with initial value (never undefined)
const [post, postActions] = createResource(
  () => "post-1",
  async (id) => {
    const response = await fetch(`https://api.example.com/posts/${id}`);
    return response.json();
  },
  { initialValue: { id: "post-1", title: "Loading..." } }
);

// post() is always defined: InitializedResource<Post>
console.log(post().title);

// Complete example with Suspense and ErrorBoundary
function UserProfile() {
  const [userId, setUserId] = createSignal("123");

  const [user, { refetch }] = createResource(
    userId,
    async (id, { value, refetching }) => {
      console.log("Fetching user:", id);
      console.log("Previous value:", value);
      console.log("Is refetching:", refetching);

      const response = await fetch(`https://api.example.com/users/${id}`);
      if (!response.ok) throw new Error("User not found");
      return response.json();
    }
  );

  return (
    <div>
      <button onClick={() => setUserId(id => String(Number(id) + 1))}>
        Next User
      </button>
      <button onClick={() => refetch()}>Refresh</button>

      <ErrorBoundary fallback={(err) => <div>Error: {err.message}</div>}>
        <Suspense fallback={<div>Loading user...</div>}>
          <div>
            <h2>{user().name}</h2>
            <p>{user().email}</p>
          </div>
        </Suspense>
      </ErrorBoundary>
    </div>
  );
}

render(() => <UserProfile />, document.getElementById("app")!);
```

### createStore - Manage nested reactive state

Creates a proxy-based store for managing complex nested state. Unlike signals, stores allow fine-grained reactivity for individual properties and nested objects. Use the setter with path syntax to update specific parts of the state tree.

```typescript
import { createStore } from "solid-js/store";
import { createEffect } from "solid-js";

// Create a store with nested data
const [state, setState] = createStore({
  user: {
    name: "John",
    age: 30,
    settings: {
      theme: "dark",
      notifications: true
    }
  },
  todos: [
    { id: 1, text: "Learn Solid", done: false },
    { id: 2, text: "Build app", done: false }
  ]
});

// Fine-grained updates - only affects specific property
setState("user", "name", "Jane");
setState("user", "age", age => age + 1);

// Nested property updates
setState("user", "settings", "theme", "light");

// Array updates
setState("todos", 0, "done", true);
setState("todos", todos => [...todos, { id: 3, text: "Deploy", done: false }]);

// Bulk updates with produce pattern
import { produce } from "solid-js/store";

setState(
  produce((state) => {
    state.user.age += 1;
    state.todos.push({ id: 4, text: "Test", done: false });
  })
);

// Fine-grained reactivity tracks individual properties
createEffect(() => {
  console.log("User name:", state.user.name);
  // Only runs when state.user.name changes, not other properties
});

createEffect(() => {
  console.log("Theme:", state.user.settings.theme);
  // Only runs when theme changes
});

// Array reconciliation with keys
setState("todos", (todo) => todo.id === 1, "done", true);

// Unwrap store to get raw object
import { unwrap } from "solid-js/store";
const rawState = unwrap(state);
console.log(rawState); // Plain JavaScript object

// Modifiers for special operations
import { reconcile } from "solid-js/store";

// Replace entire object while preserving references where possible
const newData = { user: { name: "Bob", age: 25, settings: { theme: "dark", notifications: false } }, todos: [] };
setState(reconcile(newData));

// Mutable modifier for efficient batch updates
import { modifyMutable } from "solid-js/store";

setState("todos", modifyMutable(todos => {
  todos.forEach(todo => todo.done = false);
  todos.push({ id: 5, text: "Review", done: false });
}));
```

## Component Utilities

### createContext and useContext - Share state across component tree

Creates a Context for dependency injection and state management across component boundaries without prop drilling. Provider components pass values down the tree, and child components access them with useContext.

```typescript
import { createContext, useContext, createSignal, ParentComponent } from "solid-js";
import { render } from "solid-js/web";

// Create context with default value
interface ThemeContextValue {
  theme: () => string;
  setTheme: (theme: string) => void;
}

const ThemeContext = createContext<ThemeContextValue>({
  theme: () => "light",
  setTheme: () => {}
});

// Provider component
const ThemeProvider: ParentComponent = (props) => {
  const [theme, setTheme] = createSignal("light");

  const value: ThemeContextValue = {
    theme,
    setTheme
  };

  return (
    <ThemeContext.Provider value={value}>
      {props.children}
    </ThemeContext.Provider>
  );
};

// Consumer components
function ThemeToggle() {
  const { theme, setTheme } = useContext(ThemeContext);

  return (
    <button onClick={() => setTheme(theme() === "light" ? "dark" : "light")}>
      Current: {theme()}
    </button>
  );
}

function ThemedPanel() {
  const { theme } = useContext(ThemeContext);

  return (
    <div style={{ background: theme() === "light" ? "#fff" : "#333" }}>
      <h1>Themed Content</h1>
      <ThemeToggle />
    </div>
  );
}

// App with nested providers
function App() {
  return (
    <ThemeProvider>
      <ThemedPanel />
    </ThemeProvider>
  );
}

render(() => <App />, document.getElementById("app")!);

// Multiple contexts with composition
interface UserContextValue {
  user: () => { name: string; id: string } | null;
  login: (name: string) => void;
  logout: () => void;
}

const UserContext = createContext<UserContextValue>();

function UserProvider(props: { children: any }) {
  const [user, setUser] = createSignal<{ name: string; id: string } | null>(null);

  const login = (name: string) => {
    setUser({ name, id: Math.random().toString() });
  };

  const logout = () => {
    setUser(null);
  };

  return (
    <UserContext.Provider value={{ user, login, logout }}>
      {props.children}
    </UserContext.Provider>
  );
}

function Profile() {
  const userContext = useContext(UserContext);
  if (!userContext) throw new Error("Profile must be used within UserProvider");

  const { user, logout } = userContext;

  return (
    <Show when={user()} fallback={<div>Not logged in</div>}>
      {(u) => (
        <div>
          <p>Welcome, {u().name}!</p>
          <button onClick={logout}>Logout</button>
        </div>
      )}
    </Show>
  );
}
```

### mergeProps - Merge multiple prop objects reactively

Merges multiple prop objects with reactive tracking. Later props override earlier ones. Useful for implementing default props or combining multiple prop sources while maintaining reactivity.

```typescript
import { mergeProps, createSignal, Component } from "solid-js";

// Component with default props
interface ButtonProps {
  text?: string;
  variant?: "primary" | "secondary";
  disabled?: boolean;
  onClick?: () => void;
}

const Button: Component<ButtonProps> = (props) => {
  const merged = mergeProps(
    { text: "Click me", variant: "primary" as const, disabled: false },
    props
  );

  return (
    <button
      class={`btn btn-${merged.variant}`}
      disabled={merged.disabled}
      onClick={merged.onClick}
    >
      {merged.text}
    </button>
  );
};

// Usage - overrides only specified props
<Button text="Submit" variant="secondary" />

// Reactive merging with signals
const [config, setConfig] = createSignal({ color: "blue", size: "medium" });
const [overrides, setOverrides] = createSignal({ size: "large" });

const merged = mergeProps(config, overrides);
console.log(merged.color); // "blue"
console.log(merged.size); // "large"

setOverrides({ size: "small", color: "red" });
console.log(merged.color); // "red" (override)
console.log(merged.size); // "small"

// Merge multiple sources
const defaults = { a: 1, b: 2, c: 3 };
const user = { b: 20 };
const system = { c: 300 };

const final = mergeProps(defaults, user, system);
console.log(final); // { a: 1, b: 20, c: 300 }
```

### splitProps - Split props into multiple objects

Splits a props object into multiple objects based on specified keys. Maintains reactivity for all split objects. Useful for separating component-specific props from DOM attributes.

```typescript
import { splitProps, Component, JSX } from "solid-js";

interface InputProps extends JSX.InputHTMLAttributes<HTMLInputElement> {
  label?: string;
  error?: string;
  helperText?: string;
}

const Input: Component<InputProps> = (props) => {
  const [local, input] = splitProps(
    props,
    ["label", "error", "helperText"]
  );

  return (
    <div class="input-wrapper">
      {local.label && <label>{local.label}</label>}
      <input
        {...input}
        class={local.error ? "input-error" : "input"}
      />
      {local.error && <span class="error">{local.error}</span>}
      {local.helperText && <span class="helper">{local.helperText}</span>}
    </div>
  );
};

// Usage with mixed props
<Input
  label="Email"
  type="email"
  placeholder="Enter your email"
  helperText="We'll never share your email"
  required
/>

// Split into multiple groups
interface CardProps extends JSX.HTMLAttributes<HTMLDivElement> {
  title: string;
  subtitle?: string;
  footer?: JSX.Element;
  variant?: "outlined" | "filled";
}

const Card: Component<CardProps> = (props) => {
  const [card, div] = splitProps(
    props,
    ["title", "subtitle", "footer", "variant"]
  );

  return (
    <div {...div} class={`card card-${card.variant || "filled"}`}>
      <div class="card-header">
        <h3>{card.title}</h3>
        {card.subtitle && <p>{card.subtitle}</p>}
      </div>
      <div class="card-body">{props.children}</div>
      {card.footer && <div class="card-footer">{card.footer}</div>}
    </div>
  );
};

// Three-way split
const [style, events, other] = splitProps(
  props,
  ["class", "style"],
  ["onClick", "onMouseEnter", "onMouseLeave"]
);
```

### lazy - Lazy load components

Dynamically imports components with code splitting. Returns a component wrapper that loads the actual component on first render. Integrates with Suspense for loading states.

```typescript
import { lazy, Suspense, Component } from "solid-js";
import { render } from "solid-js/web";

// Lazy load a component
const HeavyChart = lazy(() => import("./components/HeavyChart"));
const AdminPanel = lazy(() => import("./components/AdminPanel"));

function Dashboard() {
  return (
    <div>
      <h1>Dashboard</h1>
      <Suspense fallback={<div>Loading chart...</div>}>
        <HeavyChart data={[1, 2, 3, 4, 5]} />
      </Suspense>
    </div>
  );
}

// Conditional lazy loading with routing
function App() {
  const [route, setRoute] = createSignal("home");

  return (
    <div>
      <nav>
        <button onClick={() => setRoute("home")}>Home</button>
        <button onClick={() => setRoute("admin")}>Admin</button>
      </nav>

      <Suspense fallback={<div>Loading page...</div>}>
        <Switch>
          <Match when={route() === "home"}>
            <div>Home Page</div>
          </Match>
          <Match when={route() === "admin"}>
            <AdminPanel />
          </Match>
        </Switch>
      </Suspense>
    </div>
  );
}

// Preload component before rendering
const ExpensiveComponent = lazy(() => import("./Expensive"));

function Toolbar() {
  return (
    <button
      onMouseEnter={() => ExpensiveComponent.preload()}
      onClick={() => showComponent()}
    >
      Show Component (preloaded on hover)
    </button>
  );
}

// Nested lazy loading with error handling
function ComplexApp() {
  return (
    <ErrorBoundary
      fallback={(err) => <div>Failed to load: {err.message}</div>}
    >
      <Suspense fallback={<div>Loading...</div>}>
        <LazySection />
      </Suspense>
    </ErrorBoundary>
  );
}

const LazySection = lazy(() => import("./Section"));

render(() => <App />, document.getElementById("app")!);
```

## Control Flow Components

### For - Keyed list rendering with item identity

Renders a list by iterating over each item with referential keying. Each item maintains its identity based on reference equality. Use when list items are objects that maintain their identity across updates.

```typescript
import { For, createSignal } from "solid-js";

interface Todo {
  id: number;
  text: string;
  done: boolean;
}

function TodoList() {
  const [todos, setTodos] = createSignal<Todo[]>([
    { id: 1, text: "Learn Solid", done: false },
    { id: 2, text: "Build app", done: false },
    { id: 3, text: "Deploy", done: true }
  ]);

  const addTodo = () => {
    setTodos(prev => [...prev, {
      id: Date.now(),
      text: `Todo ${prev.length + 1}`,
      done: false
    }]);
  };

  const toggleTodo = (id: number) => {
    setTodos(prev => prev.map(todo =>
      todo.id === id ? { ...todo, done: !todo.done } : todo
    ));
  };

  const removeTodo = (id: number) => {
    setTodos(prev => prev.filter(todo => todo.id !== id));
  };

  return (
    <div>
      <button onClick={addTodo}>Add Todo</button>
      <ul>
        <For each={todos()} fallback={<div>No todos yet</div>}>
          {(todo, index) => (
            <li style={{ "text-decoration": todo.done ? "line-through" : "none" }}>
              <span>{index() + 1}. {todo.text}</span>
              <button onClick={() => toggleTodo(todo.id)}>Toggle</button>
              <button onClick={() => removeTodo(todo.id)}>Delete</button>
            </li>
          )}
        </For>
      </ul>
    </div>
  );
}

// Nested For loops
function Grid() {
  const [rows, setRows] = createSignal([
    { id: 1, cells: ["A1", "A2", "A3"] },
    { id: 2, cells: ["B1", "B2", "B3"] },
    { id: 3, cells: ["C1", "C2", "C3"] }
  ]);

  return (
    <table>
      <tbody>
        <For each={rows()}>
          {(row) => (
            <tr>
              <For each={row.cells}>
                {(cell) => <td>{cell}</td>}
              </For>
            </tr>
          )}
        </For>
      </tbody>
    </table>
  );
}
```

### Index - Non-keyed list rendering with index identity

Renders a list by index position. Items are identified by their index, not by reference. Use when list values change frequently but positions are stable, or when items are primitives.

```typescript
import { Index, createSignal } from "solid-js";

function ScoreBoard() {
  const [scores, setScores] = createSignal([100, 95, 87, 82, 76]);

  const incrementScore = (index: number) => {
    setScores(prev => [
      ...prev.slice(0, index),
      prev[index] + 1,
      ...prev.slice(index + 1)
    ]);
  };

  return (
    <div>
      <h2>High Scores</h2>
      <ol>
        <Index each={scores()} fallback={<div>No scores</div>}>
          {(score, index) => (
            <li>
              Player {index + 1}: {score()}
              <button onClick={() => incrementScore(index)}>+1</button>
            </li>
          )}
        </Index>
      </ol>
    </div>
  );
}

// Index with primitive values
function ColorPalette() {
  const [colors, setColors] = createSignal([
    "#FF6B6B", "#4ECDC4", "#45B7D1", "#FFA07A", "#98D8C8"
  ]);

  const changeColor = (index: number) => {
    const newColor = "#" + Math.floor(Math.random()*16777215).toString(16);
    setColors(prev => [
      ...prev.slice(0, index),
      newColor,
      ...prev.slice(index + 1)
    ]);
  };

  return (
    <div class="palette">
      <Index each={colors()}>
        {(color, i) => (
          <div
            class="color-swatch"
            style={{ background: color() }}
            onClick={() => changeColor(i)}
          >
            {color()}
          </div>
        )}
      </Index>
    </div>
  );
}

// Performance comparison: Index vs For with primitives
function NumbersList() {
  const [numbers, setNumbers] = createSignal([1, 2, 3, 4, 5]);

  // Better with Index - values change, not references
  return (
    <Index each={numbers()}>
      {(num, index) => (
        <div>
          Position {index}: {num()}
          <button onClick={() => {
            setNumbers(prev => [
              ...prev.slice(0, index),
              num() * 2,
              ...prev.slice(index + 1)
            ]);
          }}>
            Double
          </button>
        </div>
      )}
    </Index>
  );
}
```

### Show - Conditional rendering with optional keying

Conditionally renders children based on a truthy condition. Supports keyed mode for recreating content on change, or unkeyed mode for preserving content. Provides a callback pattern for accessing the condition value.

```typescript
import { Show, createSignal } from "solid-js";

function UserGreeting() {
  const [user, setUser] = createSignal<{ name: string; email: string } | null>(null);

  return (
    <div>
      <Show
        when={user()}
        fallback={<div>Please log in</div>}
      >
        {(u) => (
          <div>
            <h1>Hello, {u().name}!</h1>
            <p>Email: {u().email}</p>
          </div>
        )}
      </Show>

      <button onClick={() => setUser({ name: "John", email: "john@example.com" })}>
        Login
      </button>
      <button onClick={() => setUser(null)}>Logout</button>
    </div>
  );
}

// Keyed mode - recreates content when condition changes
function KeyedExample() {
  const [userId, setUserId] = createSignal<string | null>("user-1");

  return (
    <Show when={userId()} keyed>
      {(id) => {
        console.log("Creating component for:", id);
        // Component is recreated when userId changes
        return <UserProfile userId={id} />;
      }}
    </Show>
  );
}

// Unkeyed mode (default) - preserves content
function UnkeyedExample() {
  const [isVisible, setIsVisible] = createSignal(true);
  const [count, setCount] = createSignal(0);

  return (
    <div>
      <button onClick={() => setIsVisible(!isVisible())}>Toggle</button>
      <Show when={isVisible()}>
        <div>
          <p>Count: {count()}</p>
          <button onClick={() => setCount(c => c + 1)}>Increment</button>
        </div>
      </Show>
    </div>
  );
}

// Type narrowing with Show
function DataDisplay() {
  const [data, setData] = createSignal<string | number | null>(null);

  return (
    <div>
      <Show when={typeof data() === "string"} fallback={<span>Not a string</span>}>
        {(str) => <div>String value: {str()}</div>}
      </Show>

      <Show when={typeof data() === "number"} fallback={<span>Not a number</span>}>
        {(num) => <div>Number value: {num()}</div>}
      </Show>
    </div>
  );
}

function UserProfile(props: { userId: string }) {
  return <div>Profile for {props.userId}</div>;
}
```

### Switch/Match - Multiple conditional branches

Renders the first matching condition from multiple branches. Works like a switch statement but for JSX. Only evaluates conditions until one matches.

```typescript
import { Switch, Match, createSignal } from "solid-js";

function Router() {
  const [route, setRoute] = createSignal<"home" | "about" | "contact" | "404">("home");

  return (
    <div>
      <nav>
        <button onClick={() => setRoute("home")}>Home</button>
        <button onClick={() => setRoute("about")}>About</button>
        <button onClick={() => setRoute("contact")}>Contact</button>
      </nav>

      <Switch fallback={<div>404 Not Found</div>}>
        <Match when={route() === "home"}>
          <div>
            <h1>Home Page</h1>
            <p>Welcome to our site!</p>
          </div>
        </Match>
        <Match when={route() === "about"}>
          <div>
            <h1>About Us</h1>
            <p>We are awesome!</p>
          </div>
        </Match>
        <Match when={route() === "contact"}>
          <div>
            <h1>Contact</h1>
            <p>Email: contact@example.com</p>
          </div>
        </Match>
      </Switch>
    </div>
  );
}

// With value extraction (keyed mode)
function StatusDisplay() {
  const [status, setStatus] = createSignal<
    | { type: "loading" }
    | { type: "success"; data: any }
    | { type: "error"; message: string }
  >({ type: "loading" });

  return (
    <Switch>
      <Match when={status().type === "loading"}>
        <div>Loading...</div>
      </Match>
      <Match when={status().type === "success" && status()}>
        {(s) => <div>Success: {JSON.stringify(s().data)}</div>}
      </Match>
      <Match when={status().type === "error" && status()}>
        {(s) => <div>Error: {s().message}</div>}
      </Match>
    </Switch>
  );
}

// Nested conditions
function PermissionGate() {
  const [user, setUser] = createSignal<{ role: "admin" | "user" | "guest" } | null>(null);
  const [isLoading, setIsLoading] = createSignal(true);

  return (
    <Switch>
      <Match when={isLoading()}>
        <div>Checking permissions...</div>
      </Match>
      <Match when={!user()}>
        <div>Please log in</div>
      </Match>
      <Match when={user()?.role === "admin"}>
        <div>Admin Panel</div>
      </Match>
      <Match when={user()?.role === "user"}>
        <div>User Dashboard</div>
      </Match>
      <Match when={user()?.role === "guest"}>
        <div>Limited Access</div>
      </Match>
    </Switch>
  );
}
```

### ErrorBoundary - Catch and handle errors

Catches JavaScript errors anywhere in the child component tree and displays a fallback UI. Prevents errors from crashing the entire app.

```typescript
import { ErrorBoundary, createSignal } from "solid-js";

function App() {
  return (
    <ErrorBoundary
      fallback={(err, reset) => (
        <div class="error-container">
          <h1>Something went wrong</h1>
          <p>{err.message}</p>
          <button onClick={reset}>Try again</button>
        </div>
      )}
    >
      <BuggyComponent />
    </ErrorBoundary>
  );
}

// Component that might throw
function BuggyComponent() {
  const [count, setCount] = createSignal(0);

  if (count() > 5) {
    throw new Error("Count exceeded maximum!");
  }

  return (
    <div>
      <p>Count: {count()}</p>
      <button onClick={() => setCount(c => c + 1)}>Increment</button>
    </div>
  );
}

// Nested error boundaries for granular error handling
function Dashboard() {
  return (
    <div>
      <h1>Dashboard</h1>

      <ErrorBoundary fallback={<div>Failed to load user widget</div>}>
        <UserWidget />
      </ErrorBoundary>

      <ErrorBoundary fallback={<div>Failed to load stats widget</div>}>
        <StatsWidget />
      </ErrorBoundary>

      <ErrorBoundary fallback={<div>Failed to load chart widget</div>}>
        <ChartWidget />
      </ErrorBoundary>
    </div>
  );
}

// Error boundary with logging
function LoggingErrorBoundary(props: { children: any }) {
  return (
    <ErrorBoundary
      fallback={(err, reset) => {
        console.error("Caught error:", err);

        // Send to error tracking service
        sendToErrorTracker({
          message: err.message,
          stack: err.stack,
          timestamp: Date.now()
        });

        return (
          <div>
            <h2>Oops! Something went wrong</h2>
            <details>
              <summary>Error details</summary>
              <pre>{err.stack}</pre>
            </details>
            <button onClick={reset}>Reload</button>
          </div>
        );
      }}
    >
      {props.children}
    </ErrorBoundary>
  );
}

function sendToErrorTracker(error: any) {
  console.log("Sending to error tracker:", error);
}

function UserWidget() { return <div>User Widget</div>; }
function StatsWidget() { return <div>Stats Widget</div>; }
function ChartWidget() { return <div>Chart Widget</div>; }
```

### Suspense - Handle async loading states

Shows a fallback while waiting for async operations (resources, lazy components) to resolve. Coordinates multiple async operations and displays a single loading state.

```typescript
import { Suspense, createResource, lazy } from "solid-js";
import { render } from "solid-js/web";

function App() {
  const [user] = createResource(fetchUser);
  const [posts] = createResource(fetchPosts);

  return (
    <div>
      <h1>My App</h1>

      {/* Single Suspense for multiple resources */}
      <Suspense fallback={<div>Loading user and posts...</div>}>
        <UserProfile user={user()} />
        <PostsList posts={posts()} />
      </Suspense>
    </div>
  );
}

// Nested Suspense boundaries
function Dashboard() {
  return (
    <div>
      <Suspense fallback={<div>Loading header...</div>}>
        <Header />
      </Suspense>

      <Suspense fallback={<div>Loading main content...</div>}>
        <MainContent />

        <Suspense fallback={<div>Loading sidebar...</div>}>
          <Sidebar />
        </Suspense>
      </Suspense>
    </div>
  );
}

// With lazy components
const HeavyComponent = lazy(() => import("./HeavyComponent"));

function LazyExample() {
  const [show, setShow] = createSignal(false);

  return (
    <div>
      <button onClick={() => setShow(true)}>Load Component</button>

      <Show when={show()}>
        <Suspense fallback={<div>Loading component...</div>}>
          <HeavyComponent />
        </Suspense>
      </Show>
    </div>
  );
}

// Custom loading state
function CustomLoader() {
  return (
    <div class="loader">
      <div class="spinner"></div>
      <p>Please wait...</p>
    </div>
  );
}

function AppWithCustomLoader() {
  const [data] = createResource(fetchData);

  return (
    <Suspense fallback={<CustomLoader />}>
      <DataDisplay data={data()} />
    </Suspense>
  );
}

async function fetchUser() {
  const response = await fetch("https://api.example.com/user");
  return response.json();
}

async function fetchPosts() {
  const response = await fetch("https://api.example.com/posts");
  return response.json();
}

async function fetchData() {
  const response = await fetch("https://api.example.com/data");
  return response.json();
}

function UserProfile(props: { user: any }) {
  return <div>User: {props.user.name}</div>;
}

function PostsList(props: { posts: any[] }) {
  return <ul><For each={props.posts}>{post => <li>{post.title}</li>}</For></ul>;
}

function Header() { return <header>Header</header>; }
function MainContent() { return <main>Main</main>; }
function Sidebar() { return <aside>Sidebar</aside>; }
function DataDisplay(props: { data: any }) { return <div>{JSON.stringify(props.data)}</div>; }

render(() => <App />, document.getElementById("app")!);
```

## Rendering and Lifecycle

### render - Mount application to DOM

Mounts a Solid application to a DOM element. Creates the reactive root and initializes the component tree. Returns a disposal function to clean up the application.

```typescript
import { render } from "solid-js/web";
import { createSignal } from "solid-js";

function App() {
  const [count, setCount] = createSignal(0);

  return (
    <div>
      <h1>Count: {count()}</h1>
      <button onClick={() => setCount(c => c + 1)}>Increment</button>
    </div>
  );
}

// Basic render
const dispose = render(() => <App />, document.getElementById("app")!);

// Manual disposal (cleanup)
// dispose();

// Multiple independent apps
render(() => <Header />, document.getElementById("header")!);
render(() => <MainContent />, document.getElementById("main")!);
render(() => <Footer />, document.getElementById("footer")!);

// Conditional rendering
const mountPoint = document.getElementById("app");
if (mountPoint) {
  render(() => <App />, mountPoint);
} else {
  console.error("Mount point not found");
}

// Re-render on route change
let currentDispose: (() => void) | null = null;

function navigate(route: string) {
  if (currentDispose) currentDispose();

  const component = getComponentForRoute(route);
  currentDispose = render(
    () => component,
    document.getElementById("app")!
  );
}

function getComponentForRoute(route: string) {
  return <div>Route: {route}</div>;
}

function Header() { return <header>Header</header>; }
function MainContent() { return <main>Main</main>; }
function Footer() { return <footer>Footer</footer>; }
```

### hydrate - Hydrate server-rendered HTML

Attaches event listeners and reactivity to server-rendered HTML. Used for SSR applications to make static HTML interactive without re-rendering.

```typescript
import { hydrate } from "solid-js/web";
import { createSignal } from "solid-js";

function App() {
  const [count, setCount] = createSignal(0);

  return (
    <div>
      <h1>Count: {count()}</h1>
      <button onClick={() => setCount(c => c + 1)}>Increment</button>
    </div>
  );
}

// Hydrate server-rendered content
hydrate(() => <App />, document.getElementById("app")!);

// With data loaded from server
interface ServerData {
  user: { name: string; id: string };
  posts: any[];
}

declare global {
  interface Window {
    __INITIAL_DATA__: ServerData;
  }
}

function AppWithData() {
  const initialData = window.__INITIAL_DATA__;
  const [user] = createSignal(initialData.user);
  const [posts] = createSignal(initialData.posts);

  return (
    <div>
      <h1>Welcome, {user().name}!</h1>
      <PostsList posts={posts()} />
    </div>
  );
}

hydrate(() => <AppWithData />, document.getElementById("app")!);

function PostsList(props: { posts: any[] }) {
  return <ul><For each={props.posts}>{post => <li>{post.title}</li>}</For></ul>;
}
```

### onMount - Run effect once on mount

Executes a function once after the component is first created and inserted into the DOM. Does not track dependencies or re-run.

```typescript
import { onMount, createSignal } from "solid-js";

function AutoFocusInput() {
  let inputRef: HTMLInputElement | undefined;

  onMount(() => {
    inputRef?.focus();
    console.log("Input mounted and focused");
  });

  return <input ref={inputRef} type="text" placeholder="Auto-focused" />;
}

// Data fetching on mount
function UserProfile() {
  const [user, setUser] = createSignal<any>(null);
  const [loading, setLoading] = createSignal(true);

  onMount(async () => {
    try {
      const response = await fetch("https://api.example.com/user");
      const data = await response.json();
      setUser(data);
    } catch (error) {
      console.error("Failed to fetch user:", error);
    } finally {
      setLoading(false);
    }
  });

  return (
    <Show when={!loading()} fallback={<div>Loading...</div>}>
      <div>User: {user()?.name}</div>
    </Show>
  );
}

// Initialize third-party library
function MapComponent() {
  let mapContainer: HTMLDivElement | undefined;

  onMount(() => {
    const map = new Map(mapContainer!, {
      center: [0, 0],
      zoom: 10
    });

    console.log("Map initialized:", map);
  });

  return <div ref={mapContainer} style={{ width: "100%", height: "400px" }}></div>;
}

class Map {
  constructor(element: HTMLElement, options: any) {}
}
```

### onCleanup - Register cleanup function

Registers a function to run when the reactive scope is disposed or before the effect re-runs. Use for cleanup like removing event listeners, canceling timers, or closing connections.

```typescript
import { createEffect, onCleanup, createSignal } from "solid-js";

function Timer() {
  const [count, setCount] = createSignal(0);
  const [isRunning, setIsRunning] = createSignal(false);

  createEffect(() => {
    if (!isRunning()) return;

    const interval = setInterval(() => {
      setCount(c => c + 1);
    }, 1000);

    onCleanup(() => {
      clearInterval(interval);
      console.log("Timer cleaned up");
    });
  });

  return (
    <div>
      <p>Count: {count()}</p>
      <button onClick={() => setIsRunning(!isRunning())}>
        {isRunning() ? "Stop" : "Start"}
      </button>
    </div>
  );
}

// Event listener cleanup
function ClickTracker() {
  const [clicks, setClicks] = createSignal(0);

  createEffect(() => {
    const handleClick = () => setClicks(c => c + 1);
    document.addEventListener("click", handleClick);

    onCleanup(() => {
      document.removeEventListener("click", handleClick);
      console.log("Removed click listener");
    });
  });

  return <div>Document clicks: {clicks()}</div>;
}

// WebSocket cleanup
function LiveFeed() {
  const [messages, setMessages] = createSignal<string[]>([]);
  const [connected, setConnected] = createSignal(false);

  createEffect(() => {
    if (!connected()) return;

    const ws = new WebSocket("wss://example.com/feed");

    ws.onmessage = (event) => {
      setMessages(prev => [...prev, event.data]);
    };

    onCleanup(() => {
      ws.close();
      console.log("WebSocket closed");
    });
  });

  return (
    <div>
      <button onClick={() => setConnected(!connected())}>
        {connected() ? "Disconnect" : "Connect"}
      </button>
      <ul>
        <For each={messages()}>
          {(msg) => <li>{msg}</li>}
        </For>
      </ul>
    </div>
  );
}
```

## Advanced Reactivity

### createRoot - Create isolated reactive scope

Creates an independent reactive root that doesn't auto-dispose. Use for creating reactive contexts outside of components or for manual lifetime management.

```typescript
import { createRoot, createSignal, createEffect } from "solid-js";

// Create independent reactive scope
const dispose = createRoot((dispose) => {
  const [count, setCount] = createSignal(0);

  createEffect(() => {
    console.log("Count:", count());
  });

  setCount(1); // Logs: "Count: 1"
  setCount(2); // Logs: "Count: 2"

  // Return cleanup function
  return () => {
    console.log("Cleaning up root");
    dispose();
  };
});

// Later: manually dispose
dispose();

// Global state management
interface Store {
  user: () => any;
  setUser: (user: any) => void;
}

const store = createRoot<Store>(() => {
  const [user, setUser] = createSignal<any>(null);

  return { user, setUser };
});

// Use anywhere
store.setUser({ name: "John", id: "123" });
console.log(store.user()); // { name: "John", id: "123" }

// Event bus with reactive state
const eventBus = createRoot(() => {
  const [events, setEvents] = createSignal<Array<{ type: string; data: any }>>([]);

  const emit = (type: string, data: any) => {
    setEvents(prev => [...prev, { type, data }]);
  };

  const subscribe = (type: string, callback: (data: any) => void) => {
    createEffect(() => {
      events()
        .filter(e => e.type === type)
        .forEach(e => callback(e.data));
    });
  };

  return { emit, subscribe };
});

eventBus.subscribe("user-login", (data) => {
  console.log("User logged in:", data);
});

eventBus.emit("user-login", { name: "Jane" });
```

### batch - Batch multiple updates

Defers reactive updates until the batch completes. Prevents multiple re-renders when updating multiple signals at once.

```typescript
import { batch, createSignal, createEffect } from "solid-js";

const [firstName, setFirstName] = createSignal("John");
const [lastName, setLastName] = createSignal("Doe");

let effectRunCount = 0;

createEffect(() => {
  effectRunCount++;
  console.log(`Effect run #${effectRunCount}: ${firstName()} ${lastName()}`);
});

// Without batch - effect runs twice
setFirstName("Jane");
setLastName("Smith");
// Logs:
// "Effect run #2: Jane Doe"
// "Effect run #3: Jane Smith"

// With batch - effect runs once
batch(() => {
  setFirstName("Alice");
  setLastName("Johnson");
});
// Logs:
// "Effect run #4: Alice Johnson"

// Complex state updates
function updateUserProfile(updates: { name?: string; email?: string; age?: number }) {
  batch(() => {
    if (updates.name) setName(updates.name);
    if (updates.email) setEmail(updates.email);
    if (updates.age) setAge(updates.age);
  });
}

const [name, setName] = createSignal("");
const [email, setEmail] = createSignal("");
const [age, setAge] = createSignal(0);

updateUserProfile({ name: "John", email: "john@example.com", age: 30 });
```

### untrack - Disable dependency tracking

Reads signals without creating dependencies. Useful for conditional logic that shouldn't trigger re-runs.

```typescript
import { createSignal, createEffect, untrack } from "solid-js";

const [count, setCount] = createSignal(0);
const [enabled, setEnabled] = createSignal(true);

// Effect only tracks 'enabled', not 'count'
createEffect(() => {
  if (enabled()) {
    console.log("Count is:", untrack(count));
  }
});

setCount(5); // Does NOT trigger effect
setEnabled(false); // Triggers effect

// Conditional tracking
const [source, setSource] = createSignal("A");
const [valueA, setValueA] = createSignal(1);
const [valueB, setValueB] = createSignal(2);

createEffect(() => {
  const src = source();
  const value = src === "A" ? valueA() : untrack(valueB);
  console.log(`Using ${src}: ${value}`);
});

setValueA(10); // Triggers effect
setValueB(20); // Does NOT trigger effect (untracked)
setSource("B"); // Triggers effect, now reads valueB

// Break infinite loops
const [data, setData] = createSignal({ x: 0, y: 0 });

createEffect(() => {
  const current = data();
  // Use untrack to avoid reading data() again
  const magnitude = Math.sqrt(
    untrack(() => current.x ** 2 + current.y ** 2)
  );

  console.log("Magnitude:", magnitude);
});
```

### on - Explicit dependency tracking

Makes dependencies explicit and controls when effects run. Supports deferred execution to skip the first run.

```typescript
import { createSignal, createEffect, on } from "solid-js";

const [a, setA] = createSignal(0);
const [b, setB] = createSignal(0);

// Only track 'a', but can read 'b' without tracking
createEffect(
  on(a, () => {
    console.log(`a = ${a()}, b = ${b()}`);
  })
);

setA(1); // Triggers effect: "a = 1, b = 0"
setB(5); // Does NOT trigger effect
setA(2); // Triggers effect: "a = 2, b = 5"

// Multiple dependencies
createEffect(
  on([a, b], ([aVal, bVal]) => {
    console.log(`Values: ${aVal}, ${bVal}`);
  })
);

// Deferred execution - skip first run
const [count, setCount] = createSignal(0);

createEffect(
  on(
    count,
    () => {
      console.log("Count changed to:", count());
    },
    { defer: true }
  )
);

// Effect doesn't run immediately
setCount(1); // Logs: "Count changed to: 1"

// Track previous value
createEffect(
  on(count, (value, prevValue) => {
    console.log(`Changed from ${prevValue} to ${value}`);
  })
);
```

### catchError - Handle errors in reactive scope

Catches errors thrown in reactive computations and provides a handler. Prevents errors from propagating up the tree.

```typescript
import { catchError, createSignal, createEffect } from "solid-js";

const [shouldThrow, setShouldThrow] = createSignal(false);

catchError(
  () => {
    createEffect(() => {
      if (shouldThrow()) {
        throw new Error("Something went wrong!");
      }
      console.log("Everything is fine");
    });
  },
  (error) => {
    console.error("Caught error:", error.message);
  }
);

setShouldThrow(true); // Logs: "Caught error: Something went wrong!"

// Nested error handlers
catchError(
  () => {
    console.log("Outer scope");

    catchError(
      () => {
        throw new Error("Inner error");
      },
      (err) => {
        console.error("Inner handler:", err.message);
        // Optionally re-throw to propagate
        // throw err;
      }
    );
  },
  (err) => {
    console.error("Outer handler:", err.message);
  }
);

// Error recovery
function DataComponent() {
  const [data, setData] = createSignal<any>(null);
  const [error, setError] = createSignal<Error | null>(null);

  catchError(
    () => {
      createEffect(async () => {
        try {
          const result = await fetchData();
          setData(result);
        } catch (err) {
          throw err;
        }
      });
    },
    (err) => {
      setError(err as Error);
    }
  );

  return (
    <Show when={!error()} fallback={<div>Error: {error()!.message}</div>}>
      <div>Data: {JSON.stringify(data())}</div>
    </Show>
  );
}

async function fetchData() {
  throw new Error("API error");
}
```

## DOM Manipulation

### Portal - Render outside component hierarchy

Renders children into a different part of the DOM tree. Useful for modals, tooltips, and overlays that need to break out of overflow or z-index contexts.

```typescript
import { Portal, createSignal } from "solid-js";
import { render } from "solid-js/web";

function App() {
  const [showModal, setShowModal] = createSignal(false);

  return (
    <div style={{ overflow: "hidden", height: "100px" }}>
      <button onClick={() => setShowModal(true)}>Open Modal</button>

      <Show when={showModal()}>
        <Portal>
          <div class="modal-overlay" onClick={() => setShowModal(false)}>
            <div class="modal-content" onClick={(e) => e.stopPropagation()}>
              <h2>Modal Title</h2>
              <p>This is rendered in document.body</p>
              <button onClick={() => setShowModal(false)}>Close</button>
            </div>
          </div>
        </Portal>
      </Show>
    </div>
  );
}

// Portal to specific element
function CustomPortal() {
  return (
    <Portal mount={document.getElementById("portal-root")!}>
      <div>Rendered in #portal-root</div>
    </Portal>
  );
}

// Portal with shadow DOM
function IsolatedWidget() {
  return (
    <Portal useShadow>
      <div>
        <style>{`
          .widget { background: blue; color: white; padding: 20px; }
        `}</style>
        <div class="widget">Isolated styles</div>
      </div>
    </Portal>
  );
}

// SVG Portal
function SvgOverlay() {
  return (
    <Portal mount={document.getElementById("svg-container")} isSVG>
      <circle cx="50" cy="50" r="40" fill="red" />
    </Portal>
  );
}

render(() => <App />, document.getElementById("app")!);
```

### Dynamic - Render dynamic components

Renders a component or element dynamically based on a variable. The component type can change reactively.

```typescript
import { Dynamic, createSignal } from "solid-js";

function Button(props: any) {
  return <button {...props}>{props.children}</button>;
}

function Link(props: any) {
  return <a {...props}>{props.children}</a>;
}

function DynamicExample() {
  const [component, setComponent] = createSignal<"button" | "a">("button");

  return (
    <div>
      <Dynamic
        component={component() === "button" ? "button" : "a"}
        href={component() === "a" ? "#" : undefined}
        onClick={() => console.log("Clicked")}
      >
        Click me
      </Dynamic>

      <button onClick={() => setComponent(component() === "button" ? "a" : "button")}>
        Toggle Component
      </button>
    </div>
  );
}

// Dynamic component from registry
function ComponentRegistry() {
  const components = {
    button: Button,
    link: Link,
    text: (props: any) => <span {...props}>{props.children}</span>
  };

  const [selectedType, setSelectedType] = createSignal<keyof typeof components>("button");

  return (
    <div>
      <Dynamic
        component={components[selectedType()]}
        onClick={() => console.log("Clicked")}
      >
        Dynamic Content
      </Dynamic>

      <select onChange={(e) => setSelectedType(e.currentTarget.value as any)}>
        <option value="button">Button</option>
        <option value="link">Link</option>
        <option value="text">Text</option>
      </select>
    </div>
  );
}

// Dynamic with type safety
type ComponentType = typeof Button | typeof Link | "div";

function TypeSafeDynamic() {
  const [comp, setComp] = createSignal<ComponentType>("div");

  return (
    <Dynamic component={comp()} class="dynamic-element">
      Content
    </Dynamic>
  );
}
```

## Summary

SolidJS excels at building reactive user interfaces with minimal overhead and maximum control. The library's fine-grained reactivity system ensures that only the specific DOM nodes affected by state changes are updated, without virtual DOM diffing or unnecessary re-renders. Core use cases include building single-page applications, dashboards with real-time data, complex forms with validation, server-side rendered websites with progressive enhancement, and component libraries. The createSignal, createMemo, and createEffect primitives form the reactive foundation, while createStore handles complex nested state. Control flow components like For, Show, and Switch provide declarative conditional rendering and list management.

Integration patterns leverage the library's flexibility through Context API for dependency injection, Resources for async data fetching with Suspense, lazy loading for code splitting, and Portal for rendering outside the component tree. SolidJS works seamlessly with TypeScript, provides first-class SSR support through solid-start, and integrates with existing tools like Vite and Rollup. The reactive primitives can be used independently of the rendering layer, enabling reactive state management in any JavaScript environment. With its small bundle size, no runtime compilation, and performance matching vanilla JavaScript, SolidJS delivers a powerful developer experience for building fast, maintainable applications.
