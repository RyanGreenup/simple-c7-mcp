# Playwright Documentation

## Introduction

Playwright is a powerful web testing and browser automation framework developed by Microsoft. It enables reliable end-to-end testing for modern web applications by providing a unified API to automate Chromium, Firefox, and WebKit browsers across Windows, macOS, and Linux platforms. The framework is designed with auto-waiting and retry-ability at its core, which means tests are inherently more stable and less flaky compared to traditional testing approaches. Playwright's architecture allows for cross-browser testing with a single API, mobile emulation, network interception, and parallel test execution out of the box.

The core functionality of Playwright revolves around browser automation through a hierarchy of objects: Playwright (the entry point), Browser (browser instance), BrowserContext (isolated browser session), Page (single tab), and Locator (element finder with auto-waiting). Playwright Test, the built-in test runner, extends this with fixtures, assertions, and parallel execution capabilities. The framework supports multiple programming languages including JavaScript/TypeScript, Python, Java, and C#, making it accessible to development teams regardless of their technology stack. Key features include automatic screenshot and video capture, tracing for debugging, and a comprehensive API for handling dialogs, downloads, file uploads, and complex user interactions.

---

## Core APIs

### Playwright Module
The Playwright module is the entry point that provides access to browser engines. It exposes properties for launching Chromium, Firefox, and WebKit browsers, along with device descriptors for mobile emulation and custom selector engines.

```javascript
const { chromium, firefox, webkit, devices } = require('playwright');

(async () => {
  // Launch different browsers
  const browser = await chromium.launch({ headless: false });
  const context = await browser.newContext({
    ...devices['iPhone 13'],  // Mobile emulation
    locale: 'en-US',
    permissions: ['geolocation']
  });
  const page = await context.newPage();
  await page.goto('https://example.com');
  await page.screenshot({ path: 'screenshot.png' });
  await browser.close();
})();
```

### Browser.launch()
Launches a new browser instance with configurable options including headless mode, proxy settings, download paths, and browser-specific arguments.

```javascript
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch({
    headless: false,
    slowMo: 100,  // Slow down operations by 100ms
    devtools: true,
    args: ['--start-maximized'],
    proxy: { server: 'http://proxy.example.com:8080' },
    downloadsPath: './downloads'
  });
  const context = await browser.newContext({ viewport: null });
  const page = await context.newPage();
  await page.goto('https://example.com');
  // Browser remains open for debugging
})();
```

### BrowserContext
BrowserContext provides an isolated browser session with separate cookies, storage, and settings. Multiple contexts can run simultaneously within a single browser instance without interfering with each other.

```javascript
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();

  // Create isolated context with specific settings
  const context = await browser.newContext({
    viewport: { width: 1280, height: 720 },
    userAgent: 'Custom User Agent',
    storageState: 'auth.json',  // Reuse authentication
    recordVideo: { dir: './videos' },
    httpCredentials: { username: 'user', password: 'pass' }
  });

  // Route requests at context level (affects all pages)
  await context.route('**/*.{png,jpg,jpeg}', route => route.abort());

  // Grant permissions
  await context.grantPermissions(['clipboard-read', 'clipboard-write']);

  const page = await context.newPage();
  await page.goto('https://example.com');

  // Save storage state for later reuse
  await context.storageState({ path: 'auth.json' });
  await browser.close();
})();
```

### Page.goto()
Navigates the page to a URL with configurable wait conditions. Returns the main resource response and supports handling redirects, timeouts, and various load states.

```javascript
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  // Navigate with options
  const response = await page.goto('https://example.com', {
    waitUntil: 'networkidle',  // 'load', 'domcontentloaded', 'commit'
    timeout: 30000,
    referer: 'https://google.com'
  });

  console.log(`Status: ${response.status()}`);
  console.log(`URL: ${response.url()}`);

  // Wait for specific load state after navigation
  await page.waitForLoadState('domcontentloaded');
  await browser.close();
})();
```

### Page.locator()
Creates a Locator object that represents a way to find element(s) on the page. Locators are the central piece of Playwright's auto-waiting and retry-ability, automatically waiting for elements to be actionable before performing operations.

```javascript
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('https://example.com');

  // Various locator strategies
  const byRole = page.locator('role=button[name="Submit"]');
  const byText = page.locator('text=Sign in');
  const byCSS = page.locator('.submit-button');
  const byXPath = page.locator('xpath=//button[@type="submit"]');

  // Chained and filtered locators
  const filteredLocator = page.locator('article')
    .filter({ hasText: 'Featured' })
    .locator('.read-more');

  // Wait for element
  await page.locator('.loading').waitFor({ state: 'hidden' });

  // Get element count
  const count = await page.locator('.item').count();
  console.log(`Found ${count} items`);

  await browser.close();
})();
```

### Page.getByRole()
Locates elements by their ARIA role, which is the recommended way to find elements as it reflects how users and assistive technology perceive the page.

```javascript
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('https://example.com/form');

  // Locate by role with various options
  await page.getByRole('button', { name: 'Submit' }).click();
  await page.getByRole('textbox', { name: 'Email' }).fill('user@example.com');
  await page.getByRole('checkbox', { name: 'Remember me' }).check();
  await page.getByRole('link', { name: /learn more/i }).click();
  await page.getByRole('combobox', { name: 'Country' }).selectOption('US');
  await page.getByRole('heading', { name: 'Welcome', level: 1 }).isVisible();

  // Role options: pressed, checked, selected, expanded, disabled
  await page.getByRole('button', { pressed: true }).click();

  await browser.close();
})();
```

### Page.getByText()
Locates elements by their text content using exact or partial matching. Useful for finding elements that contain specific user-visible text.

```javascript
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('https://example.com');

  // Partial text match (default)
  await page.getByText('Welcome').click();

  // Exact text match
  await page.getByText('Sign in', { exact: true }).click();

  // Case-insensitive regex match
  await page.getByText(/submit/i).click();

  // Combined with other locators
  const article = page.locator('article').filter({ hasText: 'Breaking News' });
  await article.getByText('Read more').click();

  await browser.close();
})();
```

### Page.getByLabel()
Locates form controls by their associated label text. This is the recommended way to interact with form elements as it mimics how users identify fields.

```javascript
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('https://example.com/signup');

  // Fill form using label text
  await page.getByLabel('Username').fill('john_doe');
  await page.getByLabel('Email address').fill('john@example.com');
  await page.getByLabel('Password').fill('securePassword123');
  await page.getByLabel('Confirm password').fill('securePassword123');
  await page.getByLabel('I agree to the terms').check();
  await page.getByLabel('Country').selectOption('United States');

  // Exact matching for labels with similar text
  await page.getByLabel('Phone', { exact: true }).fill('555-0123');

  await browser.close();
})();
```

### Page.getByTestId()
Locates elements by their test ID attribute, which is a dedicated selector for testing that doesn't rely on implementation details like CSS classes or text content.

```javascript
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('https://example.com');

  // Default attribute is 'data-testid'
  await page.getByTestId('submit-button').click();
  await page.getByTestId('username-input').fill('user123');
  await page.getByTestId('login-form').isVisible();

  // Chain with other locators
  const modal = page.getByTestId('confirmation-modal');
  await modal.getByRole('button', { name: 'Confirm' }).click();

  // Custom test ID attribute can be configured in playwright.config.ts:
  // use: { testIdAttribute: 'data-test-id' }

  await browser.close();
})();
```

### Locator.click()
Performs a click action on the element with built-in auto-waiting for actionability checks including visibility, stability, enabled state, and absence of overlays.

```javascript
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('https://example.com');

  // Simple click
  await page.getByRole('button', { name: 'Submit' }).click();

  // Click with options
  await page.locator('.menu-item').click({
    button: 'right',  // 'left', 'right', 'middle'
    clickCount: 2,    // Double-click
    delay: 100,       // Time between mousedown and mouseup
    position: { x: 10, y: 10 },  // Click at specific position
    modifiers: ['Shift', 'Control'],  // Hold modifier keys
    force: true,      // Skip actionability checks
    timeout: 5000
  });

  // Click and wait for navigation
  await Promise.all([
    page.waitForNavigation(),
    page.getByText('Go to dashboard').click()
  ]);

  await browser.close();
})();
```

### Locator.fill()
Fills an input field with text, clearing any existing content first. This method waits for the element to be editable before filling.

```javascript
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('https://example.com/form');

  // Fill clears existing text and types new text
  await page.getByLabel('Username').fill('new_username');

  // Fill textarea
  await page.locator('textarea').fill('This is a multi-line\ntext content');

  // Fill contenteditable
  await page.locator('[contenteditable]').fill('Rich text content');

  // Clear field by filling empty string
  await page.getByLabel('Notes').fill('');

  // For character-by-character input (useful for autocomplete)
  await page.getByLabel('Search').pressSequentially('playwright', { delay: 100 });

  await browser.close();
})();
```

### Locator.check() / Locator.uncheck()
Checks or unchecks a checkbox or radio button, automatically scrolling and waiting for the element to be actionable.

```javascript
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('https://example.com/preferences');

  // Check a checkbox
  await page.getByLabel('Enable notifications').check();

  // Uncheck a checkbox
  await page.getByLabel('Auto-save').uncheck();

  // Check a radio button
  await page.getByRole('radio', { name: 'Dark mode' }).check();

  // Force check (skip actionability)
  await page.getByLabel('Hidden option').check({ force: true });

  // Set checked state (check or uncheck based on boolean)
  await page.getByLabel('Newsletter').setChecked(true);
  await page.getByLabel('Marketing emails').setChecked(false);

  // Verify checked state
  const isChecked = await page.getByLabel('Enable notifications').isChecked();
  console.log(`Notifications enabled: ${isChecked}`);

  await browser.close();
})();
```

### Locator.selectOption()
Selects options in a `<select>` element by value, label, or index. Supports single and multiple selection.

```javascript
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('https://example.com/settings');

  // Select by value
  await page.getByLabel('Country').selectOption('us');

  // Select by label
  await page.getByLabel('Language').selectOption({ label: 'English' });

  // Select by index
  await page.getByLabel('Priority').selectOption({ index: 2 });

  // Multiple selections
  await page.getByLabel('Categories').selectOption(['sports', 'tech', 'news']);

  // Select using different criteria
  await page.locator('select#color').selectOption([
    { value: 'red' },
    { label: 'Blue' },
    { index: 3 }
  ]);

  await browser.close();
})();
```

### Page.screenshot()
Captures a screenshot of the page or a specific element with various options for format, quality, and clipping.

```javascript
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('https://example.com');

  // Full page screenshot
  await page.screenshot({
    path: 'fullpage.png',
    fullPage: true
  });

  // Viewport screenshot
  await page.screenshot({
    path: 'viewport.png',
    type: 'jpeg',
    quality: 80
  });

  // Clipped region
  await page.screenshot({
    path: 'region.png',
    clip: { x: 0, y: 0, width: 800, height: 600 }
  });

  // Element screenshot
  await page.locator('.hero-section').screenshot({ path: 'hero.png' });

  // Screenshot with hidden elements
  await page.screenshot({
    path: 'clean.png',
    mask: [page.locator('.advertisement')],
    maskColor: '#ffffff'
  });

  // Get screenshot as buffer
  const buffer = await page.screenshot();
  console.log(`Screenshot size: ${buffer.length} bytes`);

  await browser.close();
})();
```

### Page.evaluate()
Executes JavaScript code in the browser context and returns the result. Can pass arguments and receive serializable return values.

```javascript
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('https://example.com');

  // Simple evaluation
  const title = await page.evaluate(() => document.title);
  console.log(`Page title: ${title}`);

  // Pass arguments
  const result = await page.evaluate(([a, b]) => a + b, [5, 10]);
  console.log(`Result: ${result}`);  // 15

  // Access page data
  const dimensions = await page.evaluate(() => ({
    width: document.documentElement.clientWidth,
    height: document.documentElement.clientHeight,
    scrollY: window.scrollY
  }));

  // Modify page state
  await page.evaluate(() => {
    localStorage.setItem('theme', 'dark');
    document.body.classList.add('dark-mode');
  });

  // Work with elements
  const innerHTML = await page.locator('.content').evaluate(el => el.innerHTML);

  await browser.close();
})();
```

### Page.route()
Intercepts network requests to modify, mock, or abort them. Useful for testing different server responses without actual backend changes.

```javascript
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  // Block images
  await page.route('**/*.{png,jpg,jpeg,gif}', route => route.abort());

  // Mock API response
  await page.route('**/api/users', route => route.fulfill({
    status: 200,
    contentType: 'application/json',
    body: JSON.stringify([{ id: 1, name: 'John' }, { id: 2, name: 'Jane' }])
  }));

  // Modify request
  await page.route('**/api/**', route => {
    const headers = {
      ...route.request().headers(),
      'Authorization': 'Bearer test-token'
    };
    route.continue({ headers });
  });

  // Conditional routing
  await page.route('**/search**', async route => {
    const request = route.request();
    if (request.method() === 'POST') {
      await route.fulfill({ body: '{"results": []}' });
    } else {
      await route.continue();
    }
  });

  await page.goto('https://example.com');
  await browser.close();
})();
```

### Page.waitForSelector()
Waits for an element matching the selector to appear in the DOM with configurable visibility state. Returns the element handle or null.

```javascript
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('https://example.com');

  // Wait for element to be visible
  await page.waitForSelector('.loading', { state: 'hidden' });

  // Wait for element to appear
  const element = await page.waitForSelector('.dynamic-content', {
    state: 'visible',  // 'attached', 'detached', 'visible', 'hidden'
    timeout: 10000
  });

  // Wait for element to be removed
  await page.waitForSelector('.modal', { state: 'detached' });

  // Preferred modern approach using Locator
  await page.locator('.loading').waitFor({ state: 'hidden' });
  await page.locator('.content').waitFor({ state: 'visible', timeout: 5000 });

  await browser.close();
})();
```

### Page.waitForResponse()
Waits for a matching network response. Useful for asserting API calls or waiting for data to load.

```javascript
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();

  // Wait for specific response
  const responsePromise = page.waitForResponse('**/api/data');
  await page.goto('https://example.com');
  const response = await responsePromise;
  console.log(`Status: ${response.status()}`);

  // Wait with predicate
  const apiResponse = await page.waitForResponse(response =>
    response.url().includes('/api/users') &&
    response.status() === 200 &&
    response.request().method() === 'GET'
  );
  const data = await apiResponse.json();

  // Combine with click action
  const [response2] = await Promise.all([
    page.waitForResponse('**/api/submit'),
    page.getByRole('button', { name: 'Submit' }).click()
  ]);

  await browser.close();
})();
```

### Page.pdf()
Generates a PDF of the page (Chromium only). Supports various paper sizes, margins, headers, footers, and printing options.

```javascript
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('https://example.com/report');

  // Generate PDF with options
  await page.pdf({
    path: 'report.pdf',
    format: 'A4',
    margin: { top: '1cm', right: '1cm', bottom: '1cm', left: '1cm' },
    printBackground: true,
    displayHeaderFooter: true,
    headerTemplate: '<span style="font-size:10px">Report Header</span>',
    footerTemplate: '<span style="font-size:10px">Page <span class="pageNumber"></span> of <span class="totalPages"></span></span>',
    scale: 0.9,
    landscape: false,
    pageRanges: '1-5'
  });

  // Use screen media for PDF
  await page.emulateMedia({ media: 'screen' });
  await page.pdf({ path: 'screen-report.pdf' });

  await browser.close();
})();
```

### Page.addInitScript()
Adds a script that runs before any page script, useful for modifying the JavaScript environment or mocking browser APIs.

```javascript
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();
  const context = await browser.newContext();

  // Add init script to context (affects all pages)
  await context.addInitScript(() => {
    // Mock Date for consistent testing
    const mockDate = new Date('2024-01-15T10:00:00');
    window.Date = class extends Date {
      constructor() { return mockDate; }
      static now() { return mockDate.getTime(); }
    };
  });

  const page = await context.newPage();

  // Add init script to specific page with arguments
  await page.addInitScript(mock => {
    window.testConfig = mock;
  }, { apiUrl: 'http://test-api.local', debug: true });

  // Load script from file
  await page.addInitScript({ path: './test-helpers.js' });

  await page.goto('https://example.com');
  await browser.close();
})();
```

### BrowserContext.storageState()
Saves and restores browser storage (cookies, localStorage) for session reuse. Essential for authenticated test scenarios.

```javascript
const { chromium } = require('playwright');

(async () => {
  const browser = await chromium.launch();

  // Login and save state
  const context = await browser.newContext();
  const page = await context.newPage();
  await page.goto('https://example.com/login');
  await page.getByLabel('Email').fill('user@example.com');
  await page.getByLabel('Password').fill('password');
  await page.getByRole('button', { name: 'Sign in' }).click();
  await page.waitForURL('**/dashboard');

  // Save authentication state
  await context.storageState({ path: 'auth.json' });
  await context.close();

  // Reuse authentication state in new context
  const authenticatedContext = await browser.newContext({
    storageState: 'auth.json'
  });
  const authenticatedPage = await authenticatedContext.newPage();
  await authenticatedPage.goto('https://example.com/dashboard');
  // Already logged in!

  await browser.close();
})();
```

---

## Test Runner APIs (Playwright Test)

### test()
Declares a test with a title and async body function. The test function receives fixtures as the first argument, providing access to page, context, browser, and custom fixtures.

```javascript
import { test, expect } from '@playwright/test';

test('user can login and view dashboard', async ({ page }) => {
  await page.goto('https://example.com/login');
  await page.getByLabel('Email').fill('user@example.com');
  await page.getByLabel('Password').fill('password');
  await page.getByRole('button', { name: 'Sign in' }).click();

  await expect(page).toHaveURL(/.*dashboard/);
  await expect(page.getByRole('heading', { name: 'Welcome' })).toBeVisible();
});

// Test with tags and annotations
test('checkout process @smoke @critical', {
  tag: ['@e2e', '@payment'],
  annotation: { type: 'issue', description: 'https://github.com/org/repo/issues/123' }
}, async ({ page }) => {
  // Test implementation
});
```

### test.describe()
Groups related tests together with shared hooks and configuration. Supports nesting, tags, annotations, and execution mode configuration.

```javascript
import { test, expect } from '@playwright/test';

test.describe('User Authentication', () => {
  test.beforeEach(async ({ page }) => {
    await page.goto('https://example.com');
  });

  test('successful login', async ({ page }) => {
    await page.getByLabel('Email').fill('user@example.com');
    await page.getByLabel('Password').fill('validpassword');
    await page.getByRole('button', { name: 'Login' }).click();
    await expect(page).toHaveURL(/.*dashboard/);
  });

  test('invalid credentials', async ({ page }) => {
    await page.getByLabel('Email').fill('user@example.com');
    await page.getByLabel('Password').fill('wrongpassword');
    await page.getByRole('button', { name: 'Login' }).click();
    await expect(page.getByText('Invalid credentials')).toBeVisible();
  });

  test.describe('Password Reset', () => {
    test('sends reset email', async ({ page }) => {
      await page.getByText('Forgot password?').click();
      // ...
    });
  });
});

// Configure execution mode
test.describe.configure({ mode: 'parallel', retries: 2 });
```

### test.beforeEach() / test.afterEach()
Declares hooks that run before and after each test in the current scope. Receives the same fixtures as tests.

```javascript
import { test, expect } from '@playwright/test';

test.beforeEach(async ({ page }) => {
  // Runs before each test
  await page.goto('https://example.com');
  await page.evaluate(() => localStorage.clear());
});

test.afterEach(async ({ page }, testInfo) => {
  // Runs after each test
  if (testInfo.status !== testInfo.expectedStatus) {
    // Capture screenshot on failure
    await page.screenshot({ path: `failure-${testInfo.title}.png` });
  }
  console.log(`Test "${testInfo.title}" finished with status: ${testInfo.status}`);
});

test('example test', async ({ page }) => {
  // Test starts with page already at example.com
  await expect(page).toHaveTitle(/Example/);
});
```

### test.beforeAll() / test.afterAll()
Declares hooks that run once before/after all tests in the worker. Useful for expensive setup operations shared across tests.

```javascript
import { test, expect } from '@playwright/test';

let sharedData;

test.beforeAll(async ({ browser }) => {
  // Run once per worker before all tests
  console.log('Setting up test data...');
  const page = await browser.newPage();
  await page.goto('https://api.example.com/seed-data');
  sharedData = await page.evaluate(() => window.testData);
  await page.close();
});

test.afterAll(async ({ browser }) => {
  // Run once per worker after all tests
  console.log('Cleaning up test data...');
  const page = await browser.newPage();
  await page.goto('https://api.example.com/cleanup');
  await page.close();
});

test('uses shared data', async ({ page }) => {
  console.log(`Using shared data: ${JSON.stringify(sharedData)}`);
});
```

### test.use()
Configures test options for the current test file or describe block. Can set browser options, viewport, locale, and custom fixtures.

```javascript
import { test, expect } from '@playwright/test';

// Configure for entire file
test.use({
  viewport: { width: 1920, height: 1080 },
  locale: 'de-DE',
  timezoneId: 'Europe/Berlin',
  colorScheme: 'dark',
  permissions: ['geolocation'],
  geolocation: { latitude: 52.52, longitude: 13.405 }
});

test('uses German locale', async ({ page }) => {
  await page.goto('https://example.com');
  // Page renders in German locale
});

test.describe('Mobile tests', () => {
  test.use({
    viewport: { width: 375, height: 667 },
    isMobile: true,
    hasTouch: true
  });

  test('works on mobile', async ({ page }) => {
    await page.goto('https://example.com');
    await expect(page.locator('.mobile-menu')).toBeVisible();
  });
});
```

### test.skip() / test.fixme() / test.fail()
Controls test execution by skipping, marking as fixme, or expecting failure. Can be conditional based on test parameters.

```javascript
import { test, expect } from '@playwright/test';

// Skip a test
test.skip('feature not implemented', async ({ page }) => {
  // This test won't run
});

// Conditionally skip
test('only works in chromium', async ({ page, browserName }) => {
  test.skip(browserName !== 'chromium', 'This feature is Chromium-only');
  await page.goto('https://example.com');
  // Chromium-specific test
});

// Mark as known issue (still runs, reports as fixme)
test.fixme('has known bug', async ({ page }) => {
  // Test runs but is marked as needing attention
});

// Expect test to fail
test('known failing test', async ({ page }) => {
  test.fail();  // Test must fail to pass
  await expect(page.locator('.nonexistent')).toBeVisible();
});

// Conditional failure expectation
test('fails on webkit', async ({ page, browserName }) => {
  test.fail(browserName === 'webkit', 'WebKit has this bug');
  await page.goto('https://example.com');
});
```

### expect()
Playwright's assertion library with web-first assertions that auto-wait and retry until the condition is met or timeout.

```javascript
import { test, expect } from '@playwright/test';

test('comprehensive assertions', async ({ page }) => {
  await page.goto('https://example.com');

  // Page assertions
  await expect(page).toHaveTitle(/Example/);
  await expect(page).toHaveURL('https://example.com/');

  // Locator assertions (auto-wait)
  await expect(page.getByRole('heading')).toBeVisible();
  await expect(page.getByRole('button', { name: 'Submit' })).toBeEnabled();
  await expect(page.getByLabel('Email')).toBeEditable();
  await expect(page.getByLabel('Accept')).toBeChecked();
  await expect(page.locator('.items')).toHaveCount(5);
  await expect(page.getByText('Welcome')).toHaveText('Welcome, John');
  await expect(page.locator('.message')).toContainText('success');
  await expect(page.locator('input')).toHaveValue('test@example.com');
  await expect(page.locator('.box')).toHaveCSS('color', 'rgb(255, 0, 0)');
  await expect(page.locator('.card')).toHaveClass(/active/);
  await expect(page.locator('img')).toHaveAttribute('alt', 'Logo');

  // Soft assertions (continue on failure)
  await expect.soft(page.locator('.warning')).toBeHidden();

  // Negation
  await expect(page.locator('.error')).not.toBeVisible();

  // Custom timeout
  await expect(page.locator('.slow-content')).toBeVisible({ timeout: 30000 });
});
```

### Fixtures
Playwright Test uses fixtures to provide test dependencies. Built-in fixtures include page, context, browser, browserName, and request. Custom fixtures can be created for reusable test setup.

```javascript
import { test as base, expect } from '@playwright/test';

// Define custom fixtures
const test = base.extend({
  // Page fixture with automatic login
  authenticatedPage: async ({ page }, use) => {
    await page.goto('https://example.com/login');
    await page.getByLabel('Email').fill('user@example.com');
    await page.getByLabel('Password').fill('password');
    await page.getByRole('button', { name: 'Login' }).click();
    await page.waitForURL('**/dashboard');
    await use(page);  // Provide the page to the test
    // Cleanup after test
    await page.goto('https://example.com/logout');
  },

  // Data fixture
  testUser: async ({}, use) => {
    const user = { name: 'John', email: 'john@test.com' };
    await use(user);
  },

  // API helper fixture
  api: async ({ request }, use) => {
    const api = {
      createUser: (data) => request.post('/api/users', { data }),
      deleteUser: (id) => request.delete(`/api/users/${id}`)
    };
    await use(api);
  }
});

test('uses custom fixtures', async ({ authenticatedPage, testUser, api }) => {
  await authenticatedPage.getByText(`Welcome, ${testUser.name}`).isVisible();
});

export { test, expect };
```

---

## Summary

Playwright serves as a comprehensive solution for web testing and browser automation, addressing the core challenges of modern web application testing. Its primary use cases include end-to-end testing where complex user workflows need validation across different browsers, visual regression testing through screenshot comparison, API testing combined with UI verification, and performance testing through network interception and timing measurements. The framework excels in CI/CD pipeline integration, supporting headless execution, parallel test runs, and detailed reporting. Developers frequently use Playwright for testing single-page applications (SPAs), progressive web apps (PWAs), and applications requiring authentication flows, file uploads/downloads, and third-party integrations.

Integration patterns with Playwright typically follow the Page Object Model (POM) for maintainable test suites, where page interactions are encapsulated in reusable classes. The framework integrates seamlessly with popular testing tools and CI systems including GitHub Actions, Jenkins, CircleCI, and Azure DevOps. For component testing, Playwright can be combined with frameworks like React, Vue, and Svelte through its component testing capabilities. The storage state feature enables efficient test setup by reusing authentication across test files, while the global setup/teardown hooks allow for database seeding and cleanup operations. Network mocking and request interception make it possible to test applications in isolation, simulating various backend states and error conditions without requiring actual server changes. The trace viewer and video recording features provide powerful debugging capabilities, making it easier to diagnose test failures in CI environments where direct browser access isn't available.
