### Create and Launch Docker Container for Swift Debugging

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Linux.md

Commands to create and launch a Docker container with the Swift development environment. Requires Docker to be installed. The container is configured with necessary capabilities for debugging.

```shell
docker container create swift:focal
docker run --cap-add=SYS_PTRACE \
  --security-opt seccomp=unconfined \
  --security-opt apparmor=unconfined \
  -i -t swift:focal bash
```

--------------------------------

### SQLite.swift Date and Time Functions

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Shows how to use SQLite.swift to access and utilize SQLite's built-in date and time functions. It includes examples for formatting current dates and accessing date expressions.

```swift
DateFunctions.date("now")
// date('now')
Date().date
// date('2007-01-09T09:41:00.000')
Expression<Date>("date").date
// date("date")
```

--------------------------------

### Install CocoaPods and Add SQLite.swift Dependency

Source: https://github.com/stephencelis/sqlite.swift/blob/master/README.md

These commands and Ruby code illustrate how to install CocoaPods and subsequently add the SQLite.swift library to your project's Podfile. CocoaPods is a widely used dependency manager for Objective-C and Swift projects. Remember to run `pod install --repo-update` after modifying your Podfile.

```sh
# Using the default Ruby install will require you to use sudo when
# installing and updating gems.
[sudo] gem install cocoapods
```

```ruby
use_frameworks!

target 'YourAppTargetName' do
    pod 'SQLite.swift', '~> 0.15.0'
end
```

--------------------------------

### Create SQLite Database Connection (Swift)

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Establishes a connection to an SQLite database file. If the file does not exist, it will be created. This is the most basic way to connect to a database.

```swift
let db = try Connection("path/to/db.sqlite3")
```

--------------------------------

### Create a Database Table with Expressions

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Generate a 'CREATE TABLE' SQL statement using SQLite.swift expressions. This example shows how to define columns with primary key and unique constraints. Optional expressions result in nullable columns.

```swift
let users = Table("users")
try db.run(users.create { t in \
    t.column(id, primaryKey: true)\
    t.column(email, unique: true)\
    t.column(name)\
})
```

--------------------------------

### Install CocoaPods Gem

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

This shell command demonstrates how to install the CocoaPods dependency manager using RubyGems. It may require sudo privileges depending on your system's Ruby installation.

```sh
# Using the default Ruby install will require you to use sudo when
# installing and updating gems.
[sudo] gem install cocoapods
```

--------------------------------

### Build Project with Swift Package Manager

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

This command-line instruction demonstrates how to build your project after adding dependencies using the Swift Package Manager. It fetches, compiles, and links the specified packages.

```sh
swift build
```

--------------------------------

### Compile and Run SQLite.swift Tests in LLDB Debugger on Linux

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Linux.md

Steps to compile and run SQLite.swift tests within an LLDB debugger on a Linux environment, typically within a Docker container. This involves updating package lists, installing SQLite development libraries, cloning the repository, building tests, and launching LLDB.

```shell
apt-get update && apt-get install libsqlite3-dev
git clone https://github.com/stephencelis/SQLite.swift.git
swift test
lldb .build/x86_64-unknown-linux-gnu/debug/SQLite.swiftPackageTests.xctest
(lldb) target create ".build/x86_64-unknown-linux-gnu/debug/SQLite.swiftPackageTests.xctest"
(lldb) run
```

--------------------------------

### Inserting Codable Types into SQLite with Swift

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Explains how to insert Swift `Encodable` types directly into SQLite tables using the `insert` method in SQLite.swift. It shows a basic example and mentions optional `userInfo` and `otherSetters` parameters for customization.

```swift
struct User: Encodable {
    let name: String
}
try db.run(users.insert(User(name: "test")))

```

--------------------------------

### Limit and Page Query Results in Swift

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Limits the number of rows returned by a query and allows for pagination using an offset. It utilizes the `limit` function with an optional `offset` parameter to control the result set size and starting point. The generated SQL includes LIMIT and OFFSET clauses.

```swift
users.limit(5)
// SELECT * FROM "users" LIMIT 5
```

```swift
users.limit(5, offset: 5)
// SELECT * FROM "users" LIMIT 5 OFFSET 5
```

--------------------------------

### Select Specific Columns in SQLite.swift

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Demonstrates how to select specific columns from a table in SQLite.swift using the `select` function. It shows how to iterate through the results and access selected columns by their expression. Dependencies include the SQLite.swift library.

```Swift
for user in try db.prepare(users.select(id, email)) {
    print("id: \(user[id]), email: \(user[email])")
    // id: 1, email: alice@mac.com
}
// SELECT "id", "email" FROM "users"
```

```Swift
let sentence = name + " is " + cast(age) as Expression<String?> + " years old!"
for user in users.select(sentence) {
    print(user[sentence])
    // Optional("Alice is 30 years old!")
}
// SELECT ((("name" || ' is ') || CAST ("age" AS TEXT)) || ' years old!') FROM "users"
```

--------------------------------

### Prepare and Bind Statement in Swift

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Demonstrates preparing a single SQL statement with placeholders and binding values to it using the `prepare` and `run` functions in SQLite.swift. This is a safe and efficient way to execute parameterized queries, preventing SQL injection.

```swift
let stmt = try db.prepare("INSERT INTO users (email) VALUES (?)")
try stmt.run("alice@mac.com")
db.changes // -> {Some 1}
```

--------------------------------

### Create Table if Not Exists

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Generate a 'CREATE TABLE IF NOT EXISTS' SQL statement. This prevents an error if the table already exists in the database.

```swift
try db.run(users.create(ifNotExists: true) { t in /* ... */ })
```

--------------------------------

### Run VACUUM Command in SQLite.swift

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Demonstrates how to execute the SQLite VACUUM command using the `vacuum()` method provided by SQLite.swift. This command rebuilds the database file, repacking it into a minimal space, which can help reclaim free space and defragment the database.

```swift
try db.vacuum()
```

--------------------------------

### Build Complex SQLite Queries in Swift

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Illustrates how to construct complex SQL SELECT statements in SQLite.swift by chaining functions like `select`, `filter`, `order`, `limit`, and `offset` to modify the query clauses.

```swift
let query = users.select(email)           // SELECT "email" FROM "users"
                 .filter(name != nil)     // WHERE "name" IS NOT NULL
                 .order(email.desc, name) // ORDER BY "email" DESC, "name"
                 .limit(5, offset: 1)     // LIMIT 5 OFFSET 1
```

--------------------------------

### Set Database Key with SQLCipher

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

This Swift code demonstrates how to establish a connection to an encrypted SQLite database using SQLCipher and set or change its encryption key. It requires the `SQLite.swift/SQLCipher` subspec.

```swift
import SQLite

let db = try Connection("path/to/encrypted.sqlite3")
try db.key("secret")
try db.rekey("new secret") // changes encryption key on already encrypted db
```

--------------------------------

### Create a Temporary Database Table

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Generate a 'CREATE TEMPORARY TABLE' SQL statement. This creates a table that exists only for the duration of the database connection.

```swift
try db.run(users.create(temporary: true) { t in /* ... */ })
```

--------------------------------

### Create Index Conditionally (IF NOT EXISTS) in Swift

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Creates an index only if it does not already exist, preventing errors if the index has already been created. This is controlled by the 'ifNotExists' parameter in the createIndex function.

```swift
try db.run(users.createIndex(email, ifNotExists: true))
// CREATE INDEX IF NOT EXISTS "index_users_on_email" ON "users" ("email")
```

--------------------------------

### Join Tables in SQLite.swift

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Illustrates how to join tables in SQLite.swift using the `join` function. It explains the parameters for joining, including the query object for the table being joined, the join condition, and optional join types. Namespacing and aliasing are also discussed for handling ambiguous column names.

```Swift
users.join(posts, on: user_id == users[id])
// SELECT * FROM "users" INNER JOIN "posts" ON ("user_id" = "users"."id")
```

```Swift
let query = users.join(posts, on: user_id == id)
// assertion failure: ambiguous column 'id'
```

```Swift
let query = users.join(posts, on: user_id == users[id])
// SELECT * FROM "users" INNER JOIN "posts" ON ("user_id" = "users"."id")
```

```Swift
let query = users.select(users[*])
// SELECT "users".* FROM "users"
```

```Swift
let managers = users.alias("managers")

let query = users.join(managers, on: managers[id] == users[managerId])
// SELECT * FROM "users"
// INNER JOIN ("users") AS "managers" ON ("managers"."id" = "users"."manager_id")
```

```Swift
let user = try db.pluck(query)
user[id]           // fatal error: ambiguous column 'id'
                   // (please disambiguate: ["users"."id", "managers"."id"])

user[users[id]]    // returns "users"."id"
user[managers[id]] // returns "managers"."id"
```

--------------------------------

### Iterate Over Query Results in Swift

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Explains how to execute a `SELECT` statement using `prepare`, iterate over the resulting rows, and access column data by index or name. Useful for fetching and processing data from the database. Requires SQLite.swift.

```swift
let stmt = try db.prepare("SELECT id, email FROM users")
for row in stmt {
    for (index, name) in stmt.columnNames.enumerated() {
        print ("\(name):\(row[index]!)")
        // id: Optional(1), email: Optional("alice@mac.com")
    }
}
```

--------------------------------

### Connect with URI Parameters (Swift)

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Establishes a database connection using a URI string, allowing for advanced configuration through query parameters like caching modes and locking behavior. This provides fine-grained control over the connection's operational aspects.

```swift
let db = try Connection(.uri("file.sqlite", parameters: [.cache(.private), .noLock(true)]))
```

--------------------------------

### Log SQL Queries with SQLite.swift

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

This snippet demonstrates how to enable SQL query logging using the `trace` function. It is typically used within a DEBUG build configuration to print executed SQL statements to the console for debugging purposes.

```swift
#if DEBUG
    db.trace { print($0) }
#endif
```

--------------------------------

### Implementing Custom SQLite Value Types in Swift

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Provides the definition for the `Value` protocol in SQLite.swift, which enables custom Swift types to be serialized and deserialized for storage in SQLite. It details the required methods and properties for conforming types.

```swift
protocol Value {
    associatedtype Datatype: Binding
    class var declaredDatatype: String { get }
    class func fromDatatypeValue(datatypeValue: Datatype) -> Self
    var datatypeValue: Datatype { get }
}
```

--------------------------------

### Add SQLite.swift Dependency with Carthage

Source: https://github.com/stephencelis/sqlite.swift/blob/master/README.md

This snippet shows how to declare the SQLite.swift dependency in a Cartfile for use with Carthage. Carthage is a decentralized dependency manager for Cocoa projects. Ensure Carthage is installed before proceeding.

```ruby
github "stephencelis/SQLite.swift" ~> 0.15.4
```

--------------------------------

### Handle SQLite Constraint Errors in Swift

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Demonstrates how to catch specific SQLite constraint errors using pattern matching on `Result.error`. This allows for selective error handling based on the error message and code.

```swift
do {
    try db.run(users.insert(email <- "alice@mac.com"))
    try db.run(users.insert(email <- "alice@mac.com"))
} catch let Result.error(message, code, statement) where code == SQLITE_CONSTRAINT {
    print("constraint failed: (message), in (statement)")
} catch let error {
    print("insertion failed: (error)")
}
```

--------------------------------

### Shell: Swift Package Manager Installation

Source: https://github.com/stephencelis/sqlite.swift/blob/master/README.md

Provides instructions on how to add the SQLite.swift library to a Swift project using the Swift Package Manager. This involves modifying the Package.swift file to include the repository URL and version, followed by building the project using the `swift build` command.

```shell
dependencies: [
    .package(url: "https://github.com/stephencelis/SQLite.swift.git", from: "0.15.4")
]

$ swift build
```

--------------------------------

### Create Temporary Disk-Backed Database Connection (Swift)

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Creates a temporary SQLite database that is stored on disk but managed by the operating system for temporary use. This is achieved by passing `.temporary` to the `Connection` initializer. These databases are also deleted when the connection closes.

```swift
let db = try Connection(.temporary)
```

--------------------------------

### Import SQLite Module in Swift

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

This Swift code snippet shows the basic import statement required to use the SQLite.swift library in your target's source files. This should be placed at the top of any file that utilizes SQLite.swift.

```swift
import SQLite
```

--------------------------------

### Execute Multiple SQL Statements in Swift

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Shows how to execute multiple raw SQL statements atomically using the `execute` function in SQLite.swift. This is useful for initialization scripts or complex transactions. Safely handles SQL injection vulnerabilities.

```swift
try db.execute("""
    BEGIN TRANSACTION;
    CREATE TABLE users (
        id INTEGER PRIMARY KEY NOT NULL,
        email TEXT UNIQUE NOT NULL,
        name TEXT
    );
    CREATE TABLE posts (
        id INTEGER PRIMARY KEY NOT NULL,
        title TEXT NOT NULL,
        body TEXT NOT NULL,
        published_at DATETIME
    );
    PRAGMA user_version = 1;
    COMMIT TRANSACTION;
    """)
```

--------------------------------

### Define Collate Constraint - Swift

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Adds a COLLATE clause to String columns using a collating sequence from the `Collation` enumeration.

```swift
t.column(email, collate: .nocase)
// "email" TEXT NOT NULL COLLATE "NOCASE"
```

```swift
t.column(name, collate: .rtrim)
// "name" TEXT COLLATE "RTRIM"
```

--------------------------------

### Define UNIQUE Constraint in Swift

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Adds a UNIQUE constraint to a table, supporting composite (multi-column) constraints. This differs from column-level unique constraints by its scope.

```swift
t.unique(local, domain)
// UNIQUE("local", "domain")
```

--------------------------------

### Add SQLite.swift Dependency with CocoaPods

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

This Ruby code snippet shows how to add SQLite.swift as a dependency in your Podfile for CocoaPods. It includes `use_frameworks!` and specifies the target application name and pod version.

```ruby
use_frameworks!

target 'YourAppTargetName' do
    pod 'SQLite.swift', '~> 0.15.4'
end
```

--------------------------------

### Dropping SQLite Indexes with Swift

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Demonstrates how to drop an index from a SQLite database table using the `dropIndex` function in SQLite.swift. It includes an option to conditionally drop the index using `ifExists: true`.

```swift
try db.run(users.dropIndex(email))
// DROP INDEX "index_users_on_email"
```

```swift
try db.run(users.dropIndex(email, ifExists: true))
// DROP INDEX IF EXISTS "index_users_on_email"
```

--------------------------------

### Create Read-Only Database Connection (Swift)

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Connects to an SQLite database file that is bundled with the application, intended for read-only access. This is suitable for pre-populated databases that should not be modified by the app. The `readonly` parameter must be set to `true`.

```swift
let path = Bundle.main.path(forResource: "db", ofType: "sqlite3")!

let db = try Connection(path, readonly: true)
```

--------------------------------

### Define Unique Constraint - Swift

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Adds a UNIQUE constraint to a column. For uniqueness across multiple columns, use the `unique` function under Table Constraints.

```swift
t.column(email, unique: true)
// "email" TEXT UNIQUE NOT NULL
```

--------------------------------

### Managing SQLite Schema Versions with Swift

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Illustrates how to manage database schema versions using the `userVersion` property on a SQLite connection in Swift. This allows for conditional execution of migration scripts based on the current schema version.

```swift
if db.userVersion == 0 {
    // handle first migration
    db.userVersion = 1
}
if db.userVersion == 1 {
    // handle second migration
    db.userVersion = 2
}
```

--------------------------------

### Attach and Detach Databases in SQLite.swift

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Shows how to attach external SQLite databases to an existing connection and detach them. It illustrates specifying read-only mode and aliasing the attached database. The `key` parameter is available for SQLCipher encrypted databases.

```swift
let db = try Connection("db.sqlite")

try db.attach(.uri("external.sqlite", parameters: [.mode(.readOnly)]), as: "external")
// ATTACH DATABASE 'file:external.sqlite?mode=ro' AS 'external'

let table = Table("table", database: "external")
let count = try db.scalar(table.count)
// SELECT count(*) FROM 'external.table'

try db.detach("external")
// DETACH DATABASE 'external'
```

```swift
try db.attach(.uri("encrypted.sqlite"), as: "encrypted", key: "secret")
// ATTACH DATABASE 'encrypted.sqlite' AS 'encrypted' KEY 'secret'
```

--------------------------------

### Use SQLCipher with SQLite.swift via CocoaPods

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

This Ruby code snippet shows how to integrate SQLCipher with SQLite.swift using CocoaPods by specifying the `SQLCipher` subspec. This enables encrypted database functionality.

```ruby
target 'YourAppTargetName' do
  # Make sure you only require the subspec, otherwise you app might link against
  # the system SQLite, which means the SQLCipher-specific methods won't work.
  pod 'SQLite.swift/SQLCipher', '~> 0.15.4'
end
```

--------------------------------

### Serializing UIImage as Binary Data in SQLite with Swift

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Demonstrates how to extend Swift's `UIImage` class to conform to the `Value` protocol for storing binary image data in SQLite. This involves converting `UIImage` to PNG data and vice-versa.

```swift
extension UIImage: Value {
    public class var declaredDatatype: String {
        return Blob.declaredDatatype
    }
    public class func fromDatatypeValue(blobValue: Blob) -> UIImage {
        return UIImage(data: Data.fromDatatypeValue(blobValue))!
    }
    public var datatypeValue: Blob {
        return UIImagePNGRepresentation(self)!.datatypeValue
    }

}
```

--------------------------------

### Drop Column using SchemaChanger in Swift

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Removes a column from an existing table using the SchemaChanger API. This operation is straightforward, requiring only the name of the column to be dropped.

```swift
let schemaChanger = SchemaChanger(connection: db)
try schemaChanger.alter(table: "users") { table in
    table.drop(column: "email")
}
```

--------------------------------

### Insert Row with DEFAULT VALUES in Swift

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Inserts a row using `DEFAULT VALUES` when the `insert` function is called without arguments. This requires that the table has no constraints unfulfilled by default values.

```swift
try db.run(timestamps.insert())
// INSERT INTO "timestamps" DEFAULT VALUES
```

--------------------------------

### Execute Single SQL Statement with Bindings in Swift

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Shows a concise way to execute a single SQL statement with bound parameters using the `run` function in SQLite.swift. This is suitable for INSERT, UPDATE, or DELETE operations where immediate execution is desired.

```swift
try db.run("INSERT INTO users (email) VALUES (?)", "alice@mac.com")
```

--------------------------------

### Create Writable Database Connection in Application Support Directory (macOS, Swift)

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Establishes a writable SQLite database connection in the Application Support directory on macOS. This is a conventional location for application data that should persist. The code ensures the necessary directory structure is created.

```swift
// set the path corresponding to application support
var path = NSSearchPathForDirectoriesInDomains(
    .applicationSupportDirectory, .userDomainMask, true
).first! + "/" + Bundle.main.bundleIdentifier!

// create parent directory inside application support if it doesn’t exist
try FileManager.default.createDirectory(
atPath: path, withIntermediateDirectories: true, attributes: nil
)

let db = try Connection("\(path)/db.sqlite3")
```

--------------------------------

### Create FTS4 Virtual Table in Swift

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Demonstrates creating a full-text search virtual table using the FTS4 module in SQLite.swift. This enables efficient text searching within specified columns. Dependencies include the SQLite.swift library.

```swift
let emails = VirtualTable("emails")
let subject = Expression<String>("subject")
let body = Expression<String>("body")

try db.run(emails.create(.FTS4(subject, body)))
// CREATE VIRTUAL TABLE "emails" USING fts4("subject", "body")
```

--------------------------------

### Add SQLite.swift Dependency with Swift Package Manager

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

This code snippet shows how to add the SQLite.swift library as a dependency in your Swift Package Manager's Package.swift file. It specifies the repository URL and the desired version.

```swift
dependencies: [
  .package(url: "https://github.com/stephencelis/SQLite.swift.git", from: "0.15.4")
]
```

--------------------------------

### Rename and Drop Tables using SchemaChanger in Swift

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Provides functionality to rename an existing table to a new name or to completely drop a table. These operations are handled by the SchemaChanger API, which abstracts the underlying SQL commands.

```swift
let schemaChanger = SchemaChanger(connection: db)

try schemaChanger.rename(table: "users", to: "users_new")
try schemaChanger.drop(table: "emails", ifExists: false)
```

--------------------------------

### Set Values with SQLite.swift Operators

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Demonstrates how to set values in SQLite.swift using the '<-' operator for inserts/updates, and convenience setters like '++' for atomic increments, and '-=', '+=' for transactional value transfers. These operators simplify common database operations.

```swift
try db.run(counter.update(count <- 0))
// UPDATE "counters" SET "count" = 0 WHERE ("id" = 1)
```

```swift
try db.run(counter.update(count++)) // equivalent to `counter.update(count -> count + 1)`
// UPDATE "counters" SET "count" = "count" + 1 WHERE ("id" = 1)
```

```swift
let amount = 100.0
try db.transaction {
    try db.run(alice.update(balance -= amount))
    try db.run(betty.update(balance += amount))
}
// BEGIN DEFERRED TRANSACTION
// UPDATE "users" SET "balance" = "balance" - 100.0 WHERE ("id" = 1)
// UPDATE "users" SET "balance" = "balance" + 100.0 WHERE ("id" = 2)
// COMMIT TRANSACTION
```

--------------------------------

### Rename Column using SchemaChanger in Swift

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Renames an existing column in a table using the SchemaChanger API. This function takes the current column name and the desired new name as parameters.

```swift
let schemaChanger = SchemaChanger(connection: db)
try schemaChanger.alter(table: "users") { table in
    table.rename(column: "old_name", to: "new_name")
}
```

--------------------------------

### Define FOREIGN KEY Constraint in Swift

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Adds a FOREIGN KEY constraint to a table. It supports all SQLite types, ON UPDATE/ON DELETE actions, and composite keys, offering more flexibility than column-level references.

```swift
t.foreignKey(user_id, references: users, id, delete: .setNull)
// FOREIGN KEY("user_id") REFERENCES "users"("id") ON DELETE SET NULL
```

--------------------------------

### Handling Date-Time Values in SQLite with Swift

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Shows how to map Swift's `Date` type to SQLite's `DATETIME` columns using SQLite.swift. It demonstrates querying posts published after a specific date and filtering posts within a date range.

```swift
let published_at = Expression<Date>("published_at")

let published = posts.filter(published_at <= Date())
// SELECT * FROM "posts" WHERE "published_at" <= '2014-11-18T12:45:30.000'
```

```swift
let startDate = Date(timeIntervalSince1970: 0)
let published = posts.filter(startDate...Date() ~= published_at)
// SELECT * FROM "posts" WHERE "published_at" BETWEEN '1970-01-01T00:00:00.000' AND '2014-11-18T12:45:30.000'
```

--------------------------------

### Insert Multiple Rows into SQLite Table in Swift

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Inserts multiple rows into a table at once using the `insertMany` function with an array of per-row setters. It returns the ROWID of the last inserted row.

```swift
do {
    let lastRowid = try db.run(users.insertMany([mail <- "alice@mac.com"], [email <- "geoff@mac.com"]))
    print("last inserted id: (lastRowid)")
} catch {
    print("insertion failed: (error)")
}
```

--------------------------------

### Define CHECK Constraint in Swift

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Adds a CHECK constraint to a table using a boolean expression. This expression can be constructed using filter operators and functions, similar to column constraints.

```swift
t.check(balance >= 0)
// CHECK ("balance" >= 0.0)
```

--------------------------------

### Query Detailed Schema Index and Column Information

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Fetches detailed information about indexes and columns for a specific table. `indexDefinitions` returns an array of index details, while `columnDefinitions` provides column specifics like primary key status and nullability. This is useful for understanding the intricate structure of a table.

```swift
let indexes = try schema.indexDefinitions("users")
let columns = try schema.columnDefinitions("users")

for index in indexes {
    print("\(index.name) columns\(index.columns))")
}
for column in columns {
    print("\(column.name) pk\(column.primaryKey) nullable: \(column.nullable)")
}
```

--------------------------------

### Create Unique Index on Column in Swift

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Creates a UNIQUE index on a column, ensuring that all values in the indexed column are distinct. This is achieved by setting the 'unique' parameter to true when calling the createIndex function.

```swift
try db.run(users.createIndex(email, unique: true))
// CREATE UNIQUE INDEX "index_users_on_email" ON "users" ("email")
```

--------------------------------

### Decode Codable Types from SQLite Rows

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Demonstrates how to retrieve and decode Decodable types from SQLite database rows using SQLite.swift. It covers direct decoding and manual decoding with custom logic for handling different subclasses.

```swift
let loadedUsers: [User] = try db.prepare(users).map {
    return try row.decode()
}
```

```swift
enum ImageCodingKeys: String, CodingKey {
    case kind
}

enum ImageKind: Int, Codable {
    case png, jpg, heif
}

let loadedImages: [Image] = try db.prepare(images).map {
    let decoder = row.decoder()
    let container = try decoder.container(keyedBy: ImageCodingKeys.self)
    switch try container.decode(ImageKind.self, forKey: .kind) {
    case .png:
        return try PNGImage(from: decoder)
    case .jpg:
        return try JPGImage(from: decoder)
    case .heif:
        return try HEIFImage(from: decoder)
    }
}
```

--------------------------------

### Encrypt Existing Database with SQLCipher

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

This Swift code snippet shows how to export an unencrypted SQLite database to an encrypted format using SQLCipher. It requires the `SQLite.swift/SQLCipher` subspec and specifies the output file and encryption key.

```swift
let db = try Connection("path/to/unencrypted.sqlite3")
try db.sqlcipher_export(.uri("encrypted.sqlite3"), key: "secret")
```

--------------------------------

### Pluck First or All SQLite Rows

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Demonstrates how to retrieve a single row or all rows from a SQLite query in Swift. The `pluck` function retrieves the first matching row, while converting the query result to an Array collects all rows.

```swift
if let user = try db.pluck(users) { /* ... */ } // Row
// SELECT * FROM "users" LIMIT 1
```

```swift
let all = Array(try db.prepare(users))
// SELECT * FROM "users"
```

--------------------------------

### Add Column using SchemaChanger in Swift

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Adds a new column to an existing table using the SchemaChanger API. This method allows for specifying column properties such as name, type, nullability, and default value.

```swift
let newColumn = ColumnDefinition(
    name: "new_text_column",
    type: .TEXT,
    nullable: true,
    defaultValue: .stringLiteral("foo")
)

let schemaChanger = SchemaChanger(connection: db)

try schemaChanger.alter(table: "users") { table in
    table.add(column: newColumn)
}
```

--------------------------------

### Create Index on Column in Swift

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Builds a CREATE INDEX statement to create an index on a specified column. The index name is automatically generated based on the table and column names. This is done by calling createIndex on a SchemaType object.

```swift
try db.run(users.createIndex(email))
// CREATE INDEX "index_users_on_email" ON "users" ("email")
```

--------------------------------

### Create Custom Collation Sequence in Swift

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Defines a custom collation sequence named 'NODIACRITIC' that performs case-insensitive and diacritic-insensitive string comparisons. This custom collation can then be applied to sorting clauses in SQL queries.

```swift
try db.createCollation("NODIACRITIC") { lhs, rhs in
    return lhs.compare(rhs, options: .diacriticInsensitiveSearch)
}
```

--------------------------------

### Define PRIMARY KEY Constraint in Swift

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Adds a PRIMARY KEY constraint to a table, supporting all SQLite types, sorting orders, and composite keys. This is defined at the table level, unlike column constraints.

```swift
t.primaryKey(email.asc, name)
// PRIMARY KEY("email" ASC, "name")
```

--------------------------------

### Create Table using SchemaChanger in Swift

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Creates a new table with specified columns using the SchemaChanger API. This method allows defining column properties like name, type, nullability, primary key, and auto-increment behavior.

```swift
let schemaChanger = SchemaChanger(connection: db)

try schemaChanger.create(table: "users") { table in 
    table.add(column: .init(name: "id", primaryKey: .init(autoIncrement: true), type: .INTEGER))
    table.add(column: .init(name: "name", type: .TEXT, nullable: false))
}
```

--------------------------------

### Copy Bundled Database to Documents Directory (Swift)

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

A utility function to copy a pre-bundled SQLite database file from the application's resources to the writable Documents directory. This is useful for seeding the database on the first run. It checks if the destination file already exists to avoid unnecessary copies.

```swift
func copyDatabaseIfNeeded(sourcePath: String) -> Bool {
    let documents = NSSearchPathForDirectoriesInDomains(.documentDirectory, .userDomainMask, true).first!
    let destinationPath = documents + "/db.sqlite3"
    let exists = FileManager.default.fileExists(atPath: destinationPath)
    guard !exists else { return false }
    do {
        try FileManager.default.copyItem(atPath: sourcePath, toPath: destinationPath)
        return true
    } catch {
      print("error during file copy: \(error)")
	    return false
    }
}
```

--------------------------------

### Create FTS4 Table with Tokenizer in Swift

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Illustrates how to create an FTS4 virtual table with a specific tokenizer (e.g., Porter) for advanced text analysis. This allows for customized word stemming and stop word removal during indexing. Requires SQLite.swift.

```swift
try db.run(emails.create(.FTS4([subject, body], tokenize: .Porter)))
// CREATE VIRTUAL TABLE "emails" USING fts4("subject", "body", tokenize=porter)
```

--------------------------------

### Search FTS4 Table with Match Function in Swift

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Demonstrates searching an FTS4 virtual table using the `match` function for pattern matching and keyword searches. This includes wildcard searches and filtering by specific columns. Requires SQLite.swift and an existing FTS4 table.

```swift
try db.run(emails.insert(
    subject <- "Just Checking In",
    body <- "Hey, I was just wondering...did you get my last email?"
))

let wonderfulEmails: QueryType = emails.match("wonder*")
// SELECT * FROM "emails" WHERE "emails" MATCH 'wonder*'

let replies = emails.filter(subject.match("Re:*"))
// SELECT * FROM "emails" WHERE "subject" MATCH 'Re:*'
```

--------------------------------

### Create FTS5 Virtual Table in Swift

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Illustrates creating an FTS5 virtual table, a more advanced full-text search engine than FTS4. It supports features like phrase searching and has a different configuration syntax. Requires SQLite.swift and FTS5 enabled SQLite.

```swift
let emails = VirtualTable("emails")
let subject = Expression<String>("subject")
let body = Expression<String>("body")
let config = FTS5Config()
    .column(subject)
    .column(body, [.unindexed])

try db.run(emails.create(.FTS5(config)))
// CREATE VIRTUAL TABLE "emails" USING fts5("subject", "body" UNINDEXED)

// Note that FTS5 uses a different syntax to select columns, so we need to rewrite
// the last FTS4 query above as:
let replies = emails.filter(emails.match("subject:\"Re:\"*"))
// SELECT * FROM "emails" WHERE "emails" MATCH 'subject:"Re:"*'
```

--------------------------------

### Create In-Memory Database Backup with SQLite.swift

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

This snippet demonstrates how to create an in-memory copy of a persistent SQLite database using the SQLite Online Backup API. It requires an existing database connection and creates a new in-memory connection for the backup target.

```swift
let db = try Connection("db.sqlite")
let target = try Connection(.inMemory)

let backup = try db.backup(usingConnection: target)
try backup.step()
```

--------------------------------

### Configure FTS4 Table with Options in Swift

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Shows how to configure an FTS4 virtual table with various options like unindexed columns, language IDs, and ordering using `FTS4Config`. This provides granular control over indexing and searching behavior. Uses SQLite.swift.

```swift
let emails = VirtualTable("emails")
let subject = Expression<String>("subject")
let body = Expression<String>("body")
let config = FTS4Config()
    .column(subject)
    .column(body, [.unindexed])
    .languageId("lid")
    .order(.desc)

try db.run(emails.create(.FTS4(config)))
// CREATE VIRTUAL TABLE "emails" USING fts4("subject", "body", notindexed="body", languageid="lid", order="desc")
```

--------------------------------

### Apply Custom Collation to Sorting in Swift

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Shows how to use a custom collation sequence ('NODIACRITIC') to sort query results. It demonstrates applying the custom collation to a specific column ('name') using the `collate` function in SQLite.swift.

```swift
restaurants.order(collate(.custom("NODIACRITIC"), name))
```

--------------------------------

### Define Check Constraint - Swift

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Attaches a CHECK constraint using a boolean expression. Boolean expressions can be constructed with filter operators and functions. Refer to the `check` function under Table Constraints for multi-column checks.

```swift
t.column(email, check: email.like("%@%"))
// "email" TEXT NOT NULL CHECK ("email" LIKE '%@%')
```

--------------------------------

### Require Specific SQLite Version with CocoaPods

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

This Ruby code snippet demonstrates how to use the `standalone` subspec with CocoaPods to specify a particular version of SQLite.swift. It also shows how to optionally include specific SQLite features like FTS5.

```ruby
target 'YourAppTargetName' do
  pod 'SQLite.swift/standalone', '~> 0.15.4'
end
```

```ruby
target 'YourAppTargetName' do
  pod 'SQLite.swift/standalone', '~> 0.15.4'
  pod 'sqlite3/fts5', '= 3.15.0'  # SQLite 3.15.0 with FTS5 enabled
end
```

--------------------------------

### Query Schema Object Definitions

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Retrieves generic information about objects within the current database schema using a `SchemaReader`. It allows querying definitions for indexes, tables, and triggers by specifying the object type. This provides a high-level overview of the database structure.

```swift
let schema = db.schema

let indexes = try schema.objectDefinitions(type: .index)
let tables = try schema.objectDefinitions(type: .table)
let triggers = try schema.objectDefinitions(type: .trigger)
```

--------------------------------

### Execute Custom SQL Function with Raw SQL in Swift

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Demonstrates how to execute a custom SQL function ('typeConformsTo') within a raw SQL query using prepared statements. It binds arguments to the prepared statement and iterates over the results. Includes a note on resetting prepared statements to manage transactions.

```swift
let stmt = try db.prepare("SELECT * FROM attachments WHERE typeConformsTo(UTI, ?)")
for row in stmt.bind(kUTTypeImage) { /* ... */ }
```

```swift
someObj.statement = try db.prepare("SELECT * FROM attachments WHERE typeConformsTo(UTI, ?)")
for row in someObj.statement.bind(kUTTypeImage) { /* ... */ }
someObj.statement.reset()
```

--------------------------------

### Drop a Database Table

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Drops a database table by calling the `drop` function on a `SchemaType` object. This generates a `DROP TABLE` statement. An optional `ifExists` parameter can be set to true to include an `IF EXISTS` clause, preventing errors if the table does not exist.

```swift
try db.run(users.drop())
// DROP TABLE "users"

try db.run(users.drop(ifExists: true))
// DROP TABLE IF EXISTS "users"
```

--------------------------------

### Define Typed SQL Expressions

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Define typed SQL expressions for Swift types, mapping them to SQLite counterparts. These expressions are used to represent columns in database tables. Optional types in Swift map to NULLable columns in SQLite.

```swift
let id = Expression<Int64>("id")
let email = Expression<String>("email")
let balance = Expression<Double>("balance")
let verified = Expression<Bool>("verified")
let name = Expression<String?>("name")
```

--------------------------------

### Rename a Database Table

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Renames an existing database table using the `rename` function. This function can be called on a `Table` or `VirtualTable` instance, constructing an `ALTER TABLE ... RENAME TO` statement. It requires the new table name as a parameter.

```swift
try db.run(users.rename(Table("users_old")))
// ALTER TABLE "users" RENAME TO "users_old"
```

--------------------------------

### Create In-Memory SQLite Database Connection (Swift)

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Provisions an in-memory SQLite database by omitting the path argument in the `Connection` initializer. In-memory databases are volatile and are automatically deleted when the connection is closed. They offer high performance for temporary data.

```swift
let db = try Connection() // equivalent to `Connection(.inMemory)`
```

--------------------------------

### Create Writable Database Connection in Documents Directory (Swift)

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Creates a writable SQLite database connection within the application's Documents directory on iOS. This location is standard for user-generated data and is backed up by iCloud. The code ensures the directory exists before creating the connection.

```swift
let path = NSSearchPathForDirectoriesInDomains(
    .documentDirectory, .userDomainMask, true
).first!

let db = try Connection("\(path)/db.sqlite3")
```

--------------------------------

### Insert Single Row into SQLite Table in Swift

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Inserts a single row into a table using the `insert` function with a list of setters (column expressions and values). It returns the inserted row's ROWID upon success.

```swift
try db.run(users.insert(email <- "alice@mac.com", name <- "Alice"))
// INSERT INTO "users" ("email", "name") VALUES ('alice@mac.com', 'Alice')
```

```swift
try db.run(users.insert(or: .replace, email <- "alice@mac.com", name <- "Alice B."))
// INSERT OR REPLACE INTO "users" ("email", "name") VALUES ('alice@mac.com', 'Alice B.')
```

```swift
do {
    let rowid = try db.run(users.insert(email <- "alice@mac.com"))
    print("inserted id: (rowid)")
} catch {
    print("insertion failed: (error)")
}
```

--------------------------------

### Updating SQLite Rows with Codable Types in Swift

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Illustrates how to update SQLite table rows using Swift `Encodable` types with the `update` method in SQLite.swift. It includes a warning about updating all rows if no filter is applied and mentions optional parameters.

```swift
try db.run(users.filter(id == userId).update(user))

```

--------------------------------

### Add Column with REFERENCES Constraint in Swift

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Creates a FOREIGN KEY constraint on an Int64 column, linking it to a specific column in another table. This is done using the references parameter within the addColumn function, specifying the referenced table and column.

```swift
try db.run(posts.addColumn(userId, references: users, id)
// ALTER TABLE "posts" ADD COLUMN "user_id" INTEGER REFERENCES "users" ("id")
```

--------------------------------

### Execute Scalar SQL Query in Swift

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Demonstrates fetching a single value (scalar) from a SQL query using the `scalar` function in SQLite.swift. This is efficient for aggregate functions like COUNT or for retrieving a single record. Supports both direct execution and prepared statements.

```swift
let count = try db.scalar("SELECT count(*) FROM users") as! Int64

let stmt = try db.prepare("SELECT count (*) FROM users")
let count = try stmt.scalar() as! Int64
```

--------------------------------

### Set Busy Timeout for SQLite Connection (Swift)

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Configures the busy timeout for an SQLite connection, specifying how long (in seconds) the database will wait before returning an error if it's locked. This helps manage concurrent access to the database by retrying operations.

```swift
db.busyTimeout = 5 // error after 5 seconds (does multiple retries)
```

--------------------------------

### Add Column with CHECK Constraint in Swift

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Attaches a CHECK constraint to a column definition using a boolean expression. This ensures that values inserted into the column meet the specified criteria. It's used within the addColumn function.

```swift
try db.run(users.addColumn(suffix, check: ["JR", "SR"].contains(suffix)))
// ALTER TABLE "users" ADD COLUMN "suffix" TEXT CHECK ("suffix" IN ('JR', 'SR'))
```

--------------------------------

### Add a Column to a Database Table

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Adds a new column to an existing database table using the `addColumn` function. This function is called on a `Table` instance and requires the new column definition as input. It adheres to SQLite's limitations on `ALTER TABLE` statements.

```swift
try db.run(users.addColumn(suffix))
// ALTER TABLE "users" ADD COLUMN "suffix" TEXT
```

--------------------------------

### Sort Query Results in Swift

Source: https://github.com/stephencelis/sqlite.swift/blob/master/Documentation/Index.md

Sorts query results by specified columns in ascending or descending order. It takes column expressions as input and generates the corresponding SQL ORDER BY clause. Dependencies include the `Query` type and `Expression` properties `asc` and `desc`.

```swift
users.order(email, name)
// SELECT * FROM "users" ORDER BY "email", "name"
```

```swift
users.order(email.desc, name.asc)
// SELECT * FROM "users" ORDER BY "email" DESC, "name" ASC
```