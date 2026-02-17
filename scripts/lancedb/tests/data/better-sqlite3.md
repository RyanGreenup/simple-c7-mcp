# better-sqlite3

better-sqlite3 is the fastest and simplest library for SQLite in Node.js, providing a synchronous API that delivers superior performance compared to asynchronous alternatives. It supports full transaction management, user-defined functions, aggregates, virtual tables, SQLite extensions, 64-bit integers via BigInt, and worker thread support for handling slow queries without blocking the main thread.

The library uses a native C++ addon to interface with SQLite directly, offering features like prepared statements, parameter binding, and database serialization. It's designed for applications that need reliable, high-performance embedded database operations with minimal complexity, outperforming alternatives like node-sqlite3 by up to 24x in certain operations.

## Database Connection

### new Database(path, [options])

Creates a new database connection. If the database file doesn't exist, it's created. Pass `":memory:"` for in-memory databases or an empty string for temporary databases. You can also pass a Buffer from `.serialize()` to open a serialized database directly in memory.

```javascript
const Database = require('better-sqlite3');

// Open a file-based database
const db = new Database('myapp.db');

// Open with options
const db2 = new Database('myapp.db', {
  readonly: false,           // Open in read-only mode
  fileMustExist: false,      // Throw error if file doesn't exist
  timeout: 5000,             // Timeout for locked database (ms)
  verbose: console.log,      // Log all SQL statements
  nativeBinding: './path/to/better_sqlite3.node'  // Custom native addon path
});

// In-memory database
const memDb = new Database(':memory:');

// Temporary database
const tempDb = new Database('');

// Open from serialized buffer
const buffer = existingDb.serialize();
const clonedDb = new Database(buffer);
```

## Prepared Statements

### db.prepare(sql)

Creates a prepared Statement from an SQL string. Prepared statements are compiled once and can be executed multiple times with different parameters for optimal performance.

```javascript
const db = new Database('myapp.db');

// Create table
db.exec(`
  CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    email TEXT UNIQUE,
    age INTEGER
  )
`);

// Prepare statements
const insert = db.prepare('INSERT INTO users (name, email, age) VALUES (?, ?, ?)');
const selectById = db.prepare('SELECT * FROM users WHERE id = ?');
const selectAll = db.prepare('SELECT * FROM users');
const selectByAge = db.prepare('SELECT * FROM users WHERE age >= @minAge');

// Execute with run() - returns { changes, lastInsertRowid }
const info = insert.run('Alice', 'alice@example.com', 30);
console.log(info.changes);        // 1
console.log(info.lastInsertRowid); // 1

// Execute with get() - returns first row or undefined
const user = selectById.get(1);
console.log(user); // { id: 1, name: 'Alice', email: 'alice@example.com', age: 30 }

// Execute with all() - returns array of all rows
const users = selectAll.all();
console.log(users); // [{ id: 1, name: 'Alice', ... }]

// Named parameters with objects
const olderUsers = selectByAge.all({ minAge: 25 });

// Iterate through large result sets efficiently
for (const row of selectAll.iterate()) {
  console.log(row.name);
}
```

## Statement Modifiers

### stmt.pluck(), stmt.expand(), stmt.raw()

Configure how result rows are returned. `pluck()` returns only the first column value, `expand()` namespaces columns by table, and `raw()` returns arrays instead of objects.

```javascript
const db = new Database(':memory:');
db.exec('CREATE TABLE items (id INTEGER PRIMARY KEY, name TEXT, price REAL)');
db.exec("INSERT INTO items VALUES (1, 'Widget', 9.99), (2, 'Gadget', 19.99)");

const select = db.prepare('SELECT id, name, price FROM items');

// Normal mode - returns objects
select.all(); // [{ id: 1, name: 'Widget', price: 9.99 }, ...]

// Pluck mode - returns first column only
select.pluck().all(); // [1, 2]

// Reset and use expand mode - namespaces by table
select.pluck(false).expand().all();
// [{ items: { id: 1, name: 'Widget', price: 9.99 } }, ...]

// Raw mode - returns arrays (best performance for large datasets)
select.expand(false).raw().all();
// [[1, 'Widget', 9.99], [2, 'Gadget', 19.99]]

// Get column metadata
const columns = select.columns();
// [{ name: 'id', column: 'id', table: 'items', database: 'main', type: 'INTEGER' }, ...]
```

## Transactions

### db.transaction(fn)

Creates a function that always runs inside a transaction. The transaction commits on success and rolls back on error. Nested transactions use savepoints automatically.

```javascript
const db = new Database(':memory:');
db.exec(`
  CREATE TABLE accounts (id INTEGER PRIMARY KEY, name TEXT, balance REAL);
  INSERT INTO accounts VALUES (1, 'Alice', 1000), (2, 'Bob', 500);
`);

const transfer = db.prepare('UPDATE accounts SET balance = balance + ? WHERE id = ?');
const getBalance = db.prepare('SELECT balance FROM accounts WHERE id = ?').pluck();

// Create a transaction function
const transferMoney = db.transaction((fromId, toId, amount) => {
  const fromBalance = getBalance.get(fromId);
  if (fromBalance < amount) {
    throw new Error('Insufficient funds');
  }
  transfer.run(-amount, fromId);
  transfer.run(amount, toId);
  return { fromBalance: fromBalance - amount, toBalance: getBalance.get(toId) };
});

// Transaction commits on success
const result = transferMoney(1, 2, 100);
console.log(result); // { fromBalance: 900, toBalance: 600 }

// Transaction rolls back on error
try {
  transferMoney(1, 2, 10000); // Will fail - insufficient funds
} catch (err) {
  console.log(err.message); // 'Insufficient funds'
  console.log(getBalance.get(1)); // 900 (unchanged)
}

// Different transaction modes
transferMoney(1, 2, 50);           // Uses BEGIN
transferMoney.deferred(1, 2, 50);  // Uses BEGIN DEFERRED
transferMoney.immediate(1, 2, 50); // Uses BEGIN IMMEDIATE
transferMoney.exclusive(1, 2, 50); // Uses BEGIN EXCLUSIVE

// Batch insert with transaction (much faster than individual inserts)
const insertMany = db.transaction((items) => {
  const insert = db.prepare('INSERT INTO accounts (name, balance) VALUES (?, ?)');
  for (const item of items) {
    insert.run(item.name, item.balance);
  }
});

insertMany([
  { name: 'Charlie', balance: 750 },
  { name: 'Diana', balance: 1200 },
]);
```

## User-Defined Functions

### db.function(name, [options], fn)

Registers a user-defined function that can be called from SQL statements. Functions can be deterministic, variadic, and configured for safe integer handling.

```javascript
const db = new Database(':memory:');
db.exec('CREATE TABLE products (id INTEGER PRIMARY KEY, name TEXT, price REAL)');
db.exec("INSERT INTO products VALUES (1, 'laptop', 999.99), (2, 'mouse', 29.99)");

// Simple function
db.function('double', (x) => x * 2);
db.prepare('SELECT double(price) FROM products').pluck().all(); // [1999.98, 59.98]

// Function with multiple arguments
db.function('add', (a, b) => a + b);
db.prepare('SELECT add(10, 20)').pluck().get(); // 30

// Deterministic function (can be optimized by SQLite)
db.function('hash', { deterministic: true }, (str) => {
  let hash = 0;
  for (let i = 0; i < str.length; i++) {
    hash = ((hash << 5) - hash) + str.charCodeAt(i);
    hash |= 0;
  }
  return hash;
});
db.prepare('SELECT hash(name) FROM products').pluck().all();

// Variadic function (accepts any number of arguments)
db.function('concat_all', { varargs: true }, (...args) => args.join(''));
db.prepare("SELECT concat_all('Hello', ' ', 'World', '!')").pluck().get(); // 'Hello World!'

// Direct-only function (cannot be used in views/triggers)
db.function('unsafe_op', { directOnly: true }, () => 'restricted');

// Function with BigInt support
db.function('big_double', { safeIntegers: true }, (n) => n * 2n);
db.prepare('SELECT big_double(9007199254740993)').pluck().get(); // 18014398509481986n
```

## User-Defined Aggregates

### db.aggregate(name, options)

Registers a user-defined aggregate function for use with GROUP BY. Supports window functions when an `inverse` function is provided.

```javascript
const db = new Database(':memory:');
db.exec(`
  CREATE TABLE sales (id INTEGER PRIMARY KEY, product TEXT, amount REAL, date TEXT);
  INSERT INTO sales VALUES
    (1, 'A', 100, '2024-01-01'),
    (2, 'A', 150, '2024-01-02'),
    (3, 'B', 200, '2024-01-01'),
    (4, 'B', 75, '2024-01-02');
`);

// Simple sum aggregate
db.aggregate('my_sum', {
  start: 0,
  step: (total, value) => total + value,
});
db.prepare('SELECT product, my_sum(amount) FROM sales GROUP BY product').all();
// [{ product: 'A', 'my_sum(amount)': 250 }, { product: 'B', 'my_sum(amount)': 275 }]

// Average with result transformation
db.aggregate('my_avg', {
  start: () => ({ sum: 0, count: 0 }),
  step: (state, value) => {
    state.sum += value;
    state.count += 1;
    return state;
  },
  result: (state) => state.count ? state.sum / state.count : null,
});
db.prepare('SELECT my_avg(amount) FROM sales').pluck().get(); // 131.25

// Collect values into JSON array
db.aggregate('json_agg', {
  start: () => [],
  step: (arr, value) => { arr.push(value); return arr; },
  result: (arr) => JSON.stringify(arr),
});
db.prepare('SELECT product, json_agg(amount) FROM sales GROUP BY product').all();
// [{ product: 'A', 'json_agg(amount)': '[100,150]' }, ...]

// Window function with inverse
db.aggregate('running_sum', {
  start: 0,
  step: (total, value) => total + value,
  inverse: (total, value) => total - value,  // Enables window function
});
db.prepare(`
  SELECT product, amount,
    running_sum(amount) OVER (PARTITION BY product ORDER BY date) as running
  FROM sales
`).all();
```

## Virtual Tables

### db.table(name, definition)

Registers a virtual table that generates rows on-the-fly using a JavaScript generator function. Virtual tables can accept parameters like table-valued functions.

```javascript
const db = new Database(':memory:');
const fs = require('fs');

// Simple virtual table - sequence generator
db.table('sequence', {
  columns: ['value'],
  parameters: ['length', 'start'],
  rows: function* (length, start = 0) {
    if (length === undefined) throw new Error('length required');
    for (let i = 0; i < length; i++) {
      yield { value: start + i };
    }
  },
});
db.prepare('SELECT * FROM sequence(5)').all();
// [{ value: 0 }, { value: 1 }, { value: 2 }, { value: 3 }, { value: 4 }]
db.prepare('SELECT * FROM sequence(3, 10)').all();
// [{ value: 10 }, { value: 11 }, { value: 12 }]

// Virtual table returning arrays instead of objects
db.table('range', {
  columns: ['n'],
  rows: function* (start, end) {
    for (let i = start; i < end; i++) {
      yield [i];  // Array format
    }
  },
});
db.prepare('SELECT * FROM range(1, 4)').pluck().all(); // [1, 2, 3]

// Regex matches as virtual table
db.table('regex_matches', {
  columns: ['match', 'index'],
  rows: function* (pattern, text) {
    const re = new RegExp(pattern, 'g');
    let m;
    while ((m = re.exec(text)) !== null) {
      yield { match: m[0], index: m.index };
    }
  },
});
db.prepare("SELECT * FROM regex_matches('\\d+', 'abc123def456')").all();
// [{ match: '123', index: 3 }, { match: '456', index: 9 }]

// Factory function for CREATE VIRTUAL TABLE
db.table('csv', (filename) => ({
  columns: ['col1', 'col2', 'col3'],  // Would parse from file header
  rows: function* () {
    // Would read and parse CSV file
    yield ['a', 'b', 'c'];
  },
}));
db.exec("CREATE VIRTUAL TABLE my_data USING csv('data.csv')");
```

## PRAGMA Statements

### db.pragma(string, [options])

Executes PRAGMA statements to configure database behavior. Use `simple: true` to return just the first value instead of an array.

```javascript
const db = new Database('myapp.db');

// Enable WAL mode for better concurrent performance
db.pragma('journal_mode = WAL');

// Get single value with simple option
const journalMode = db.pragma('journal_mode', { simple: true });
console.log(journalMode); // 'wal'

// Get cache size
const cacheSize = db.pragma('cache_size', { simple: true });
console.log(cacheSize); // -2000 (default, in KB)

// Set cache size
db.pragma('cache_size = 32000');

// List all tables
const tables = db.pragma('table_list');
console.log(tables); // [{ schema: 'main', name: 'users', type: 'table', ... }]

// Get table info
const columns = db.pragma('table_info(users)');
// [{ cid: 0, name: 'id', type: 'INTEGER', notnull: 0, ... }]

// Foreign keys
db.pragma('foreign_keys = ON');
const fkEnabled = db.pragma('foreign_keys', { simple: true });
console.log(fkEnabled); // 1

// Synchronous mode for durability
db.pragma('synchronous = FULL');

// WAL checkpoint to prevent file growth
db.pragma('wal_checkpoint(RESTART)');
```

## Database Backup

### db.backup(destination, [options])

Creates a backup of the database to a file. Returns a Promise. Can monitor progress and control transfer rate.

```javascript
const db = new Database('myapp.db');

// Simple backup
await db.backup('backup.db');
console.log('Backup complete');

// Backup with progress monitoring
await db.backup(`backup-${Date.now()}.db`, {
  progress: ({ totalPages, remainingPages }) => {
    const percent = ((totalPages - remainingPages) / totalPages * 100).toFixed(1);
    console.log(`Backup progress: ${percent}%`);
    return 100;  // Transfer 100 pages per cycle (default)
  },
});

// Backup attached database
db.exec("ATTACH DATABASE 'other.db' AS other");
await db.backup('other-backup.db', { attached: 'other' });

// Controlled backup rate
let paused = false;
const backupPromise = db.backup('slow-backup.db', {
  progress: ({ totalPages, remainingPages }) => {
    if (paused) return 0;  // Pause backup
    return 50;  // Slower transfer rate
  },
});

// Can pause/resume from elsewhere
setTimeout(() => { paused = true; }, 1000);
setTimeout(() => { paused = false; }, 3000);

await backupPromise;
```

## Database Serialization

### db.serialize([options])

Returns a Buffer containing the complete serialized database. Useful for creating in-memory copies or sending databases over network.

```javascript
const db = new Database(':memory:');
db.exec('CREATE TABLE test (id INTEGER PRIMARY KEY, data TEXT)');
db.exec("INSERT INTO test VALUES (1, 'hello'), (2, 'world')");

// Serialize to buffer
const buffer = db.serialize();
console.log(buffer.length); // Size in bytes

// Write to file manually
const fs = require('fs');
fs.writeFileSync('exported.db', buffer);

// Create new database from buffer
const clonedDb = new Database(buffer);
clonedDb.prepare('SELECT * FROM test').all();
// [{ id: 1, data: 'hello' }, { id: 2, data: 'world' }]

// Serialize attached database
db.exec("ATTACH DATABASE ':memory:' AS attached");
db.exec('CREATE TABLE attached.other (val TEXT)');
const attachedBuffer = db.serialize({ attached: 'attached' });
```

## BigInt Support

### db.defaultSafeIntegers(), stmt.safeIntegers()

Configure handling of 64-bit integers. By default, integers are returned as JavaScript numbers. Enable safe integers to return BigInts for values that exceed JavaScript's safe integer range.

```javascript
const db = new Database(':memory:');
db.exec('CREATE TABLE bigints (id INTEGER PRIMARY KEY, big_value INTEGER)');

// Insert BigInt values
const insert = db.prepare('INSERT INTO bigints (big_value) VALUES (?)');
insert.run(9007199254740993n);  // Larger than Number.MAX_SAFE_INTEGER
insert.run(BigInt('1152735103331642317'));

// Default: returns as Number (may lose precision)
const select = db.prepare('SELECT big_value FROM bigints');
select.pluck().all(); // [9007199254740992, 1152735103331642400] - precision lost!

// Enable safe integers for this statement
select.safeIntegers();
select.pluck().all(); // [9007199254740993n, 1152735103331642317n] - precise!

// Set default for all new statements
db.defaultSafeIntegers(true);
const newSelect = db.prepare('SELECT big_value FROM bigints');
newSelect.pluck().all(); // Returns BigInts by default

// lastInsertRowid also respects safe integers
db.defaultSafeIntegers(true);
const info = insert.run(12345n);
console.log(typeof info.lastInsertRowid); // 'bigint'

// User functions can also use safe integers
db.function('bigAdd', { safeIntegers: true }, (a, b) => a + b);
db.prepare('SELECT bigAdd(?, ?)').pluck().get(9007199254740993n, 1n);
// 9007199254740994n
```

## Error Handling

### SqliteError

All SQLite errors throw SqliteError objects with a `code` property containing the SQLite error code.

```javascript
const Database = require('better-sqlite3');
const { SqliteError } = Database;

const db = new Database(':memory:');
db.exec('CREATE TABLE users (id INTEGER PRIMARY KEY, email TEXT UNIQUE)');
db.exec("INSERT INTO users VALUES (1, 'test@example.com')");

// Catch constraint violations
try {
  db.exec("INSERT INTO users VALUES (2, 'test@example.com')");
} catch (err) {
  if (err instanceof SqliteError) {
    console.log(err.message); // 'UNIQUE constraint failed: users.email'
    console.log(err.code);    // 'SQLITE_CONSTRAINT_UNIQUE'
  }
}

// Handle specific error codes
const insert = db.prepare('INSERT INTO users (email) VALUES (?)');
try {
  insert.run('test@example.com');
} catch (err) {
  switch (err.code) {
    case 'SQLITE_CONSTRAINT_UNIQUE':
      console.log('Email already exists');
      break;
    case 'SQLITE_CONSTRAINT_NOTNULL':
      console.log('Required field missing');
      break;
    case 'SQLITE_BUSY':
      console.log('Database is locked');
      break;
    default:
      throw err;
  }
}

// Check transaction state after errors
const transfer = db.transaction(() => {
  try {
    db.exec('INVALID SQL');
  } catch (err) {
    if (!db.inTransaction) {
      throw err;  // Transaction was forcefully rolled back
    }
    // Handle error within transaction
  }
});
```

## Database Properties and Methods

### db.open, db.inTransaction, db.name, db.memory, db.readonly

Access database state through these read-only properties. Use `db.close()` to close the connection and `db.exec()` to execute multiple SQL statements.

```javascript
const db = new Database('myapp.db', { readonly: false });

// Check database state
console.log(db.open);          // true
console.log(db.name);          // 'myapp.db'
console.log(db.memory);        // false
console.log(db.readonly);      // false
console.log(db.inTransaction); // false

// Execute multiple statements
db.exec(`
  CREATE TABLE IF NOT EXISTS config (key TEXT PRIMARY KEY, value TEXT);
  INSERT OR REPLACE INTO config VALUES ('version', '1.0');
  INSERT OR REPLACE INTO config VALUES ('updated', datetime('now'));
`);

// Load SQLite extensions
// db.loadExtension('./path/to/extension.so');

// Check transaction state
const tx = db.transaction(() => {
  console.log(db.inTransaction); // true
});
tx();

// Close database
process.on('exit', () => db.close());
process.on('SIGINT', () => process.exit(128 + 2));
process.on('SIGTERM', () => process.exit(128 + 15));

console.log(db.open); // false after close()
```

## Unsafe Mode

### db.unsafeMode([toggle])

Enables operations normally blocked for safety, such as mutating the database while iterating through results or bypassing defensive configuration.

```javascript
const db = new Database(':memory:');
db.exec('CREATE TABLE items (id INTEGER PRIMARY KEY, processed INTEGER DEFAULT 0)');
db.exec('INSERT INTO items (id) VALUES (1), (2), (3)');

const select = db.prepare('SELECT * FROM items WHERE processed = 0');
const update = db.prepare('UPDATE items SET processed = 1 WHERE id = ?');

// This would throw an error in safe mode
// for (const row of select.iterate()) {
//   update.run(row.id);  // Error: database is locked
// }

// Enable unsafe mode
db.unsafeMode(true);

// Now mutation during iteration is allowed (use with caution!)
for (const row of select.iterate()) {
  update.run(row.id);  // Works, but may cause undefined behavior
}

// Disable unsafe mode
db.unsafeMode(false);

// Toggle and check
db.unsafeMode();  // Enable
db.unsafeMode(true);  // Enable
db.unsafeMode(false); // Disable
```

## Worker Threads

For CPU-intensive queries, use worker threads to prevent blocking the main event loop. The database connection must be created within the worker since native addons cannot be shared across threads.

```javascript
// worker.js
const { parentPort } = require('worker_threads');
const Database = require('better-sqlite3');

const db = new Database('myapp.db', { readonly: true });

parentPort.on('message', ({ id, sql, params }) => {
  try {
    const stmt = db.prepare(sql);
    const result = params ? stmt.all(...params) : stmt.all();
    parentPort.postMessage({ id, result });
  } catch (error) {
    parentPort.postMessage({ id, error: error.message });
  }
});

// main.js
const { Worker } = require('worker_threads');

const worker = new Worker('./worker.js');
let nextId = 0;
const pending = new Map();

worker.on('message', ({ id, result, error }) => {
  const { resolve, reject } = pending.get(id);
  pending.delete(id);
  if (error) reject(new Error(error));
  else resolve(result);
});

function asyncQuery(sql, ...params) {
  return new Promise((resolve, reject) => {
    const id = nextId++;
    pending.set(id, { resolve, reject });
    worker.postMessage({ id, sql, params });
  });
}

// Usage
const users = await asyncQuery('SELECT * FROM users WHERE age > ?', 25);
console.log(users);
```

## Summary

better-sqlite3 excels in applications requiring fast, synchronous database access with full SQLite feature support. Common use cases include Electron applications, CLI tools, local caching layers, test fixtures, embedded systems, and any Node.js application where synchronous database operations simplify code flow. The library's transaction support makes it ideal for financial applications, inventory systems, and any domain requiring ACID compliance.

Integration patterns typically involve creating a single database instance at application startup, using prepared statements for repeated queries, wrapping related operations in transactions, and enabling WAL mode for concurrent access. For web servers, consider using a connection pool pattern with worker threads for heavy queries. The library integrates seamlessly with ORMs and query builders that support synchronous drivers, and its serialization feature enables easy database snapshotting for backups or testing.
