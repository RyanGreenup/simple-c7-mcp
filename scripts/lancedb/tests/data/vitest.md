# Vitest

Vitest is a next-generation testing framework powered by Vite, designed for modern JavaScript and TypeScript projects. It provides a blazing-fast testing experience with native ESM support, smart watch mode with HMR-like capabilities, and out-of-the-box TypeScript/JSX support. Vitest offers Jest-compatible APIs while leveraging Vite's configuration, transformers, resolvers, and plugins, making it easy to use the same setup from your application.

The framework includes built-in Chai assertions, Jest-compatible expect APIs, Tinyspy for mocking/stubbing/spies, native code coverage via V8 or Istanbul, snapshot testing, and browser testing capabilities. It supports parallel test execution, test filtering, timeouts, retries, and features like projects (workspaces) for monorepo setups. Vitest requires Vite >= v6.0.0 and Node >= v20.0.0.

## Test API

The `test` function (aliased as `it`) defines individual test cases with expectations to verify.

```typescript
import { describe, expect, test } from 'vitest'

// Basic test
test('should work as expected', () => {
  expect(Math.sqrt(4)).toBe(2)
})

// Test with timeout (in milliseconds)
test('async operation', async () => {
  const result = await fetchData()
  expect(result).toBeDefined()
}, 10000)

// Test with options object
test('test with options', { timeout: 5000, retry: 2 }, () => {
  expect(true).toBe(true)
})

// Skipped test
test.skip('skipped test', () => {
  expect(1).toBe(2) // Won't run
})

// Only run this test
test.only('focused test', () => {
  expect(1 + 1).toBe(2)
})

// Test expected to fail
test.fails('expected failure', () => {
  expect(1).toBe(2)
})

// Conditional tests
const isDev = process.env.NODE_ENV === 'development'
test.skipIf(isDev)('production only test', () => {})
test.runIf(isDev)('development only test', () => {})

// Concurrent tests
test.concurrent('concurrent test 1', async ({ expect }) => {
  expect(await asyncOp()).toBe('result')
})

// Parameterized tests with test.each
test.each([
  [1, 1, 2],
  [1, 2, 3],
  [2, 1, 3],
])('add(%i, %i) -> %i', (a, b, expected) => {
  expect(a + b).toBe(expected)
})

// Parameterized tests with test.for (provides TestContext)
test.for([
  { a: 1, b: 1, expected: 2 },
  { a: 1, b: 2, expected: 3 },
])('add($a, $b) -> $expected', ({ a, b, expected }) => {
  expect(a + b).toBe(expected)
})
```

## Describe API

The `describe` function (aliased as `suite`) groups related tests into a suite for organization and shared setup/teardown.

```typescript
import { describe, expect, test, beforeEach, afterEach } from 'vitest'

describe('Math operations', () => {
  test('addition', () => {
    expect(1 + 1).toBe(2)
  })

  test('subtraction', () => {
    expect(5 - 3).toBe(2)
  })
})

// Nested describes
describe('User module', () => {
  describe('when authenticated', () => {
    test('can access dashboard', () => {
      expect(canAccess('dashboard')).toBe(true)
    })
  })

  describe('when not authenticated', () => {
    test('redirects to login', () => {
      expect(getRedirect()).toBe('/login')
    })
  })
})

// Suite with options (applies to all tests in suite)
describe('slow tests', { timeout: 10000 }, () => {
  test('test 1', async () => { /* ... */ })
  test('test 2', async () => { /* ... */ })
})

// Concurrent suite - all tests run in parallel
describe.concurrent('parallel tests', () => {
  test('test 1', async ({ expect }) => { /* ... */ })
  test('test 2', async ({ expect }) => { /* ... */ })
})

// Shuffled suite - tests run in random order
describe.shuffle('randomized tests', () => {
  test('test 1', () => { /* ... */ })
  test('test 2', () => { /* ... */ })
  test('test 3', () => { /* ... */ })
})

// Parameterized describe
describe.each([
  { name: 'admin', role: 'admin' },
  { name: 'user', role: 'user' },
])('$name permissions', ({ role }) => {
  test('has correct role', () => {
    expect(getRole()).toBe(role)
  })
})
```

## Expect API

The `expect` function creates assertions using Jest-compatible APIs alongside built-in Chai assertions.

```typescript
import { expect, test } from 'vitest'

test('assertion examples', () => {
  // Equality
  expect(1 + 1).toBe(2)                    // Strict equality (===)
  expect({ a: 1 }).toEqual({ a: 1 })       // Deep equality
  expect({ a: 1, b: 2 }).toStrictEqual({ a: 1, b: 2 }) // Strict deep equality

  // Truthiness
  expect(true).toBeTruthy()
  expect(false).toBeFalsy()
  expect(null).toBeNull()
  expect(undefined).toBeUndefined()
  expect('value').toBeDefined()

  // Numbers
  expect(10).toBeGreaterThan(5)
  expect(10).toBeGreaterThanOrEqual(10)
  expect(5).toBeLessThan(10)
  expect(0.1 + 0.2).toBeCloseTo(0.3, 5)

  // Strings
  expect('hello world').toContain('world')
  expect('hello world').toMatch(/world/)

  // Arrays
  expect([1, 2, 3]).toContain(2)
  expect([1, 2, 3]).toHaveLength(3)
  expect([{ id: 1 }, { id: 2 }]).toContainEqual({ id: 1 })

  // Objects
  expect({ a: 1, b: 2 }).toHaveProperty('a')
  expect({ a: 1, b: 2 }).toHaveProperty('a', 1)
  expect({ name: 'John', age: 30 }).toMatchObject({ name: 'John' })

  // Exceptions
  expect(() => { throw new Error('fail') }).toThrow()
  expect(() => { throw new Error('fail') }).toThrowError('fail')
  expect(() => { throw new Error('fail') }).toThrowError(/fail/)

  // Negation
  expect(1).not.toBe(2)
  expect([1, 2]).not.toContain(3)

  // Type checking
  expect('string').toBeTypeOf('string')
  expect(new Date()).toBeInstanceOf(Date)

  // Asymmetric matchers
  expect({ id: 1, name: 'test' }).toEqual({
    id: expect.any(Number),
    name: expect.stringContaining('test')
  })
  expect(['apple', 'banana']).toEqual(
    expect.arrayContaining(['apple'])
  )
})

// Async assertions
test('async assertions', async () => {
  await expect(Promise.resolve('value')).resolves.toBe('value')
  await expect(Promise.reject(new Error('fail'))).rejects.toThrow('fail')
})

// Soft assertions (continue on failure)
test('soft assertions', () => {
  expect.soft(1 + 1).toBe(3)  // Fails but continues
  expect.soft(2 + 2).toBe(5)  // Also checked
  // Both failures reported at end
})

// Poll assertions (retry until success)
test('poll assertions', async () => {
  await expect.poll(() => document.querySelector('.element')).toBeTruthy()
})
```

## Snapshot Testing

Snapshot testing captures output and compares it against stored snapshots to detect changes.

```typescript
import { expect, test } from 'vitest'

test('snapshot testing', () => {
  const user = { name: 'John', age: 30, createdAt: new Date('2024-01-01') }

  // Basic snapshot
  expect(user).toMatchSnapshot()

  // Inline snapshot (auto-updated in source)
  expect(user).toMatchInlineSnapshot(`
    {
      "age": 30,
      "createdAt": 2024-01-01T00:00:00.000Z,
      "name": "John",
    }
  `)

  // Snapshot with hint
  expect(user).toMatchSnapshot('user object')

  // Partial snapshot matching
  expect(user).toMatchSnapshot({
    createdAt: expect.any(Date)
  })
})

// File snapshot
test('file snapshot', async () => {
  const html = renderComponent()
  await expect(html).toMatchFileSnapshot('./snapshots/component.html')
})

// Error snapshot
test('error snapshot', () => {
  expect(() => {
    throw new Error('Something went wrong')
  }).toThrowErrorMatchingSnapshot()
})
```

## Mock Functions

The `vi.fn()` function creates mock functions to track calls, arguments, and return values.

```typescript
import { expect, test, vi } from 'vitest'

test('mock function basics', () => {
  // Create a mock function
  const mockFn = vi.fn()

  mockFn('arg1', 'arg2')
  mockFn('arg3')

  // Check if called
  expect(mockFn).toHaveBeenCalled()
  expect(mockFn).toHaveBeenCalledTimes(2)
  expect(mockFn).toHaveBeenCalledWith('arg1', 'arg2')
  expect(mockFn).toHaveBeenLastCalledWith('arg3')

  // Access call history
  expect(mockFn.mock.calls).toEqual([['arg1', 'arg2'], ['arg3']])
  expect(mockFn.mock.lastCall).toEqual(['arg3'])
})

test('mock return values', () => {
  const mockFn = vi.fn()

  // Single return value
  mockFn.mockReturnValue(42)
  expect(mockFn()).toBe(42)

  // Return value once
  mockFn.mockReturnValueOnce('first').mockReturnValueOnce('second')
  expect(mockFn()).toBe('first')
  expect(mockFn()).toBe('second')
  expect(mockFn()).toBe(42)  // Falls back to mockReturnValue
})

test('mock implementations', () => {
  const mockFn = vi.fn()

  // Custom implementation
  mockFn.mockImplementation((a, b) => a + b)
  expect(mockFn(1, 2)).toBe(3)

  // Implementation once
  mockFn.mockImplementationOnce((a, b) => a * b)
  expect(mockFn(2, 3)).toBe(6)
  expect(mockFn(2, 3)).toBe(5)  // Back to addition
})

test('mock async functions', async () => {
  const mockFn = vi.fn()

  // Resolved value
  mockFn.mockResolvedValue({ data: 'success' })
  expect(await mockFn()).toEqual({ data: 'success' })

  // Rejected value
  mockFn.mockRejectedValue(new Error('Network error'))
  await expect(mockFn()).rejects.toThrow('Network error')
})

test('mock reset and restore', () => {
  const mockFn = vi.fn(() => 'original')

  mockFn.mockReturnValue('mocked')
  expect(mockFn()).toBe('mocked')

  // Clear call history only
  mockFn.mockClear()
  expect(mockFn.mock.calls).toEqual([])

  // Reset implementation to empty function
  mockFn.mockReset()
  expect(mockFn()).toBeUndefined()
})
```

## Spying on Objects

The `vi.spyOn()` function creates spies on existing object methods to track calls while optionally preserving original behavior.

```typescript
import { expect, test, vi } from 'vitest'

const calculator = {
  add: (a: number, b: number) => a + b,
  multiply: (a: number, b: number) => a * b,
}

test('spying on methods', () => {
  // Create spy (keeps original implementation)
  const addSpy = vi.spyOn(calculator, 'add')

  const result = calculator.add(2, 3)

  expect(result).toBe(5)  // Original behavior
  expect(addSpy).toHaveBeenCalledWith(2, 3)
  expect(addSpy).toHaveReturnedWith(5)
})

test('spy with mock implementation', () => {
  const addSpy = vi.spyOn(calculator, 'add').mockImplementation(() => 999)

  expect(calculator.add(1, 2)).toBe(999)
  expect(addSpy).toHaveBeenCalled()

  // Restore original implementation
  addSpy.mockRestore()
  expect(calculator.add(1, 2)).toBe(3)
})

test('spy on getters and setters', () => {
  const obj = {
    _value: 0,
    get value() { return this._value },
    set value(v) { this._value = v },
  }

  const getSpy = vi.spyOn(obj, 'value', 'get').mockReturnValue(42)
  expect(obj.value).toBe(42)

  const setSpy = vi.spyOn(obj, 'value', 'set')
  obj.value = 100
  expect(setSpy).toHaveBeenCalledWith(100)
})

test('spy on console methods', () => {
  const consoleSpy = vi.spyOn(console, 'log').mockImplementation(() => {})

  console.log('test message')

  expect(consoleSpy).toHaveBeenCalledWith('test message')
  consoleSpy.mockRestore()
})
```

## Module Mocking

The `vi.mock()` function replaces module imports with mock implementations.

```typescript
import { expect, test, vi, beforeEach } from 'vitest'

// Basic module mock (hoisted to top of file)
vi.mock('./utils', () => ({
  fetchUser: vi.fn(() => ({ id: 1, name: 'Mock User' })),
  formatDate: vi.fn((date) => 'mocked-date'),
}))

import { fetchUser, formatDate } from './utils'

test('mocked module', () => {
  expect(fetchUser()).toEqual({ id: 1, name: 'Mock User' })
  expect(fetchUser).toHaveBeenCalled()
})

// Partial mock - keep some original exports
vi.mock('./api', async (importOriginal) => {
  const actual = await importOriginal()
  return {
    ...actual,
    fetchData: vi.fn(() => 'mocked'),
  }
})

// Auto-mock with spy option (keeps implementation, adds tracking)
vi.mock('./calculator', { spy: true })

// Using vi.hoisted for variables in mock factory
const mocks = vi.hoisted(() => ({
  mockFn: vi.fn(),
}))

vi.mock('./service', () => ({
  doSomething: mocks.mockFn,
}))

test('using hoisted mock', () => {
  mocks.mockFn.mockReturnValue('test')
  // Now mockFn is accessible in the test
})

// Dynamic mock with vi.doMock (not hoisted)
test('dynamic mock', async () => {
  vi.doMock('./dynamic-module', () => ({
    getValue: () => 'mocked value',
  }))

  const { getValue } = await import('./dynamic-module')
  expect(getValue()).toBe('mocked value')

  vi.doUnmock('./dynamic-module')
})

// Import actual module in mock
vi.mock('./wrapper', async () => {
  const actual = await vi.importActual('./wrapper')
  return {
    ...actual,
    wrappedFn: vi.fn(),
  }
})
```

## Fake Timers

Vitest provides fake timers to control time-dependent code like `setTimeout`, `setInterval`, and `Date`.

```typescript
import { expect, test, vi, beforeEach, afterEach } from 'vitest'

beforeEach(() => {
  vi.useFakeTimers()
})

afterEach(() => {
  vi.useRealTimers()
})

test('setTimeout', () => {
  const callback = vi.fn()
  setTimeout(callback, 1000)

  expect(callback).not.toHaveBeenCalled()

  vi.advanceTimersByTime(1000)

  expect(callback).toHaveBeenCalledTimes(1)
})

test('setInterval', () => {
  const callback = vi.fn()
  setInterval(callback, 100)

  vi.advanceTimersByTime(350)

  expect(callback).toHaveBeenCalledTimes(3)
})

test('run all timers', () => {
  const callback = vi.fn()
  setTimeout(callback, 1000)
  setTimeout(callback, 2000)
  setTimeout(callback, 3000)

  vi.runAllTimers()

  expect(callback).toHaveBeenCalledTimes(3)
})

test('mock system time', () => {
  const mockDate = new Date('2024-01-15T12:00:00Z')
  vi.setSystemTime(mockDate)

  expect(new Date()).toEqual(mockDate)
  expect(Date.now()).toBe(mockDate.getTime())
})

test('advance to next timer', () => {
  const callback1 = vi.fn()
  const callback2 = vi.fn()

  setTimeout(callback1, 100)
  setTimeout(callback2, 200)

  vi.advanceTimersToNextTimer()
  expect(callback1).toHaveBeenCalled()
  expect(callback2).not.toHaveBeenCalled()

  vi.advanceTimersToNextTimer()
  expect(callback2).toHaveBeenCalled()
})

test('async timers', async () => {
  const callback = vi.fn()
  setTimeout(() => Promise.resolve().then(callback), 100)

  await vi.advanceTimersByTimeAsync(100)

  expect(callback).toHaveBeenCalled()
})
```

## Test Hooks

Lifecycle hooks run setup and teardown code before/after tests.

```typescript
import { describe, test, beforeAll, afterAll, beforeEach, afterEach } from 'vitest'

describe('database tests', () => {
  let db: Database

  // Run once before all tests in suite
  beforeAll(async () => {
    db = await Database.connect()
  })

  // Run once after all tests in suite
  afterAll(async () => {
    await db.disconnect()
  })

  // Run before each test
  beforeEach(async () => {
    await db.beginTransaction()
  })

  // Run after each test
  afterEach(async () => {
    await db.rollback()
  })

  test('insert user', async () => {
    await db.insert({ name: 'John' })
    const users = await db.query('SELECT * FROM users')
    expect(users).toHaveLength(1)
  })
})

// Hooks can return cleanup functions
beforeEach(async () => {
  const server = await startServer()

  // Cleanup function (equivalent to afterEach)
  return async () => {
    await server.stop()
  }
})

// aroundEach wraps test execution
import { aroundEach } from 'vitest'

aroundEach(async (runTest) => {
  console.log('before test')
  await runTest()
  console.log('after test')
})

// In-test cleanup with onTestFinished
import { test, onTestFinished } from 'vitest'

test('cleanup in test', () => {
  const resource = acquireResource()

  onTestFinished(() => {
    resource.release()  // Always runs, even on failure
  })

  // test logic...
})
```

## Test Context and Fixtures

Extended test context provides custom fixtures for tests.

```typescript
import { test as baseTest, expect } from 'vitest'

// Define fixtures interface
interface MyFixtures {
  user: { name: string; email: string }
  db: Database
  page: Page
}

// Extend test with fixtures
const test = baseTest.extend<MyFixtures>({
  // Simple fixture
  user: { name: 'John', email: 'john@example.com' },

  // Async fixture with setup/teardown
  db: async ({}, use) => {
    const db = await Database.connect()
    await use(db)
    await db.disconnect()
  },

  // Fixture depending on another fixture
  page: async ({ db }, use) => {
    const page = await createPage(db)
    await use(page)
    await page.close()
  },
})

test('using fixtures', ({ user, db, page }) => {
  expect(user.name).toBe('John')
  expect(db).toBeDefined()
  expect(page).toBeDefined()
})

// Override fixtures for specific tests
test('override fixture', async ({ user }) => {
  expect(user.name).toBe('John')
})

// Scoped fixtures for a suite
describe('admin tests', () => {
  test.scoped({ user: { name: 'Admin', email: 'admin@example.com' } })

  test('admin has different name', ({ user }) => {
    expect(user.name).toBe('Admin')
  })
})

// Access test metadata in fixtures
const testWithMeta = baseTest.extend({
  fixture: async ({ task }, use) => {
    console.log(`Running: ${task.name}`)
    await use('value')
  },
})
```

## Environment Mocking

Mock environment variables and global objects.

```typescript
import { expect, test, vi, beforeEach, afterEach } from 'vitest'

beforeEach(() => {
  // Stub environment variables
  vi.stubEnv('NODE_ENV', 'test')
  vi.stubEnv('API_KEY', 'test-key-123')
})

afterEach(() => {
  // Restore all stubbed envs
  vi.unstubAllEnvs()
})

test('environment variables', () => {
  expect(process.env.NODE_ENV).toBe('test')
  expect(import.meta.env.API_KEY).toBe('test-key-123')
})

// Stub global variables
test('global variables', () => {
  vi.stubGlobal('__VERSION__', '1.0.0')
  vi.stubGlobal('fetch', vi.fn())

  expect(__VERSION__).toBe('1.0.0')
  expect(fetch).toBeDefined()

  vi.unstubAllGlobals()
})

// Mock IntersectionObserver
test('mock IntersectionObserver', () => {
  const mockIntersectionObserver = vi.fn().mockImplementation(() => ({
    observe: vi.fn(),
    unobserve: vi.fn(),
    disconnect: vi.fn(),
  }))

  vi.stubGlobal('IntersectionObserver', mockIntersectionObserver)

  const observer = new IntersectionObserver(() => {})
  expect(mockIntersectionObserver).toHaveBeenCalled()
})
```

## Waiting Utilities

Utilities for waiting on async conditions.

```typescript
import { expect, test, vi } from 'vitest'

test('vi.waitFor - wait for condition', async () => {
  let ready = false
  setTimeout(() => { ready = true }, 100)

  await vi.waitFor(() => {
    if (!ready) throw new Error('Not ready')
    return ready
  }, {
    timeout: 1000,
    interval: 50,
  })

  expect(ready).toBe(true)
})

test('vi.waitUntil - wait for truthy value', async () => {
  let element: HTMLElement | null = null
  setTimeout(() => {
    element = document.createElement('div')
  }, 100)

  const result = await vi.waitUntil(
    () => element,
    { timeout: 1000, interval: 50 }
  )

  expect(result).toBeInstanceOf(HTMLElement)
})

test('expect.poll - retry assertions', async () => {
  let count = 0
  const increment = () => { count++ }
  setInterval(increment, 50)

  await expect.poll(() => count, { timeout: 500 }).toBeGreaterThan(3)
})
```

## Configuration

Vitest configuration in `vitest.config.ts` or `vite.config.ts`.

```typescript
import { defineConfig } from 'vitest/config'

export default defineConfig({
  test: {
    // Test file patterns
    include: ['**/*.{test,spec}.{js,ts,jsx,tsx}'],
    exclude: ['**/node_modules/**', '**/dist/**'],

    // Environment
    environment: 'node', // or 'jsdom', 'happy-dom'

    // Global APIs without imports
    globals: true,

    // Setup files run before each test file
    setupFiles: ['./setup.ts'],

    // Coverage configuration
    coverage: {
      provider: 'v8', // or 'istanbul'
      reporter: ['text', 'html', 'lcov'],
      include: ['src/**/*.ts'],
      exclude: ['**/*.test.ts'],
    },

    // Timeouts
    testTimeout: 5000,
    hookTimeout: 10000,

    // Reporters
    reporters: ['default', 'html'],

    // Parallelism
    fileParallelism: true,
    maxWorkers: 4,
    isolate: true,

    // Mock settings
    clearMocks: true,
    restoreMocks: true,
    mockReset: false,

    // Snapshot settings
    snapshotFormat: {
      printBasicPrototype: false,
    },

    // Type checking
    typecheck: {
      enabled: true,
      include: ['**/*.{test,spec}-d.ts'],
    },

    // Projects (monorepo support)
    projects: [
      './packages/*/vitest.config.ts',
      {
        test: {
          name: 'unit',
          include: ['**/*.unit.test.ts'],
        },
      },
      {
        test: {
          name: 'integration',
          include: ['**/*.integration.test.ts'],
          environment: 'jsdom',
        },
      },
    ],
  },
})
```

## CLI Commands

Common Vitest CLI commands and options.

```bash
# Run tests
npx vitest

# Run tests once (no watch)
npx vitest run

# Run specific test files
npx vitest run src/utils.test.ts

# Run tests matching pattern
npx vitest --testNamePattern="user"

# Run with coverage
npx vitest --coverage

# Update snapshots
npx vitest -u

# Run in UI mode
npx vitest --ui

# Run specific project
npx vitest --project=unit

# Run with specific reporter
npx vitest --reporter=verbose

# Filter by file name
npx vitest user

# Watch specific files
npx vitest --watch src/

# Run changed files only
npx vitest --changed

# Run with specific environment
npx vitest --environment=jsdom

# Show help
npx vitest --help
```

## Summary

Vitest serves as a comprehensive testing solution for modern JavaScript and TypeScript applications, offering seamless integration with Vite-powered projects. Its Jest-compatible API makes migration straightforward while providing enhanced features like native ESM support, TypeScript out-of-the-box, smart watch mode, and excellent IDE integration. The framework excels in unit testing, component testing, integration testing, and snapshot testing scenarios.

For integration patterns, Vitest works naturally with popular frameworks like Vue, React, Svelte, and Solid through browser testing capabilities. It integrates with CI/CD pipelines via reporters (JUnit, JSON, HTML), supports monorepo setups through projects configuration, and provides extensive mocking capabilities for HTTP requests, timers, modules, and environment variables. The test context system with fixtures enables clean, reusable test setup patterns similar to Playwright's approach, making it ideal for both simple projects and complex enterprise applications.
