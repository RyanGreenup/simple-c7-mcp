### Install DuckDB Go Client

Source: https://duckdb.org/docs/stable/clients/go

Installs the DuckDB Go client using the `go get` command. Ensure you have Go installed and configured.

```bash
go get github.com/duckdb/duckdb-go/v2
```

--------------------------------

### Command Line Debugging with LLDB

Source: https://duckdb.org/docs/stable/dev/building/python

Demonstrates how to debug a Python script using lldb. It includes an example Python script and the commands to run it under lldb, set a breakpoint in the DuckDB C++ library, and start execution.

```python
# Example Python script (test.py)
# import duckdb
# print(duckdb.sql("select * from range(1000)").df())
```

```lldb
lldb -- .venv/bin/python3 test.py
```

```lldb
# Set breakpoint (library loads when imported)
(lldb) br s -n duckdb::DuckDBPyRelation::FetchDF
(lldb) r
```

--------------------------------

### Setup DuckDB Tables for Connected Components Example

Source: https://duckdb.org/docs/stable/sql/query_syntax/with

Creates the 'nodes' and 'edges' tables and populates them with sample data to be used in the connected components algorithm example. This setup is a prerequisite for running the subsequent SQL query.

```sql
CREATE TABLE nodes (id INTEGER);
INSERT INTO nodes VALUES (1), (2), (3), (4), (5), (6), (7), (8);
CREATE TABLE edges (node1id INTEGER, node2id INTEGER);
INSERT INTO edges VALUES
    (1, 3), (2, 3), (3, 7), (7, 8), (5, 4), (6, 4);
```

--------------------------------

### Install Ibis with DuckDB Backend

Source: https://duckdb.org/docs/stable/guides/python/ibis

Installs the Ibis framework with the DuckDB backend using pip. The 'examples' extra is optional and allows access to sample data provided by Ibis. This is the primary method for setting up Ibis for DuckDB integration.

```bash
pip install 'ibis-framework[duckdb,examples]'
```

--------------------------------

### Install marimo and DuckDB

Source: https://duckdb.org/docs/stable/guides/python/marimo

Installs marimo with SQL support and DuckDB using pip. This is the initial setup step for using marimo with SQL capabilities.

```shell
pip install "marimo[sql]"
```

--------------------------------

### SQL Example for .read Command

Source: https://duckdb.org/docs/stable/clients/cli/overview

An example SQL file (`select_example.sql`) containing a query to generate a series of numbers.

```sql
SELECT *
FROM generate_series(5);

```

--------------------------------

### Install Development Dependencies with uv

Source: https://duckdb.org/docs/stable/dev/building/python

Installs all necessary development dependencies for the DuckDB Python project using the 'uv' package manager. It includes a two-step process for proper environment setup, first installing dependencies and then building the project without isolation.

```shell
# Install all development dependencies without building the project
uv sync --no-install-project

# Build and install the project without build isolation
uv sync --no-build-isolation
```

--------------------------------

### DuckDB SQL Autocomplete Function Example

Source: https://duckdb.org/docs/stable/core_extensions/autocomplete

This example demonstrates how to use the `sql_auto_complete` function to get suggestions for an SQL query. The function takes a query string as input and returns a list of possible SQL keywords or commands that can complete the input, along with the index where the suggestion should start.

```sql
SELECT * 
FROM sql_auto_complete('SEL');
```

--------------------------------

### Install and Load Community Extensions (Python)

Source: https://duckdb.org/docs/stable/clients/python/overview

This example demonstrates installing and loading community extensions from the DuckDB repository. It specifies `repository="community"` when calling `con.install_extension()` to fetch the 'h3' extension, and then loads it.

```python
import duckdb

con = duckdb.connect()
con.install_extension("h3", repository="community")
con.load_extension("h3")
```

--------------------------------

### Install Pre-Commit Hooks

Source: https://duckdb.org/docs/stable/dev/building/python

Installs git pre-commit hooks to automatically run linting, formatting, and type-checking before each commit. It also shows how to install a post-checkout hook for submodule synchronization.

```shell
uvx pre-commit install
```

```shell
uvx pre-commit install --hook-type post-checkout
```

--------------------------------

### SQL and Dot Command Example for .read

Source: https://duckdb.org/docs/stable/clients/cli/overview

An example file (`write_markdown_to_file.sql`) demonstrating the use of multiple commands, including setting the output mode to markdown and writing results to a file.

```duckdb_cli
.mode markdown
.output series.md
SELECT *
FROM generate_series(5);

```

--------------------------------

### Simple DuckDB Go Example

Source: https://duckdb.org/docs/stable/clients/go

A basic example demonstrating how to use the DuckDB Go client. It includes opening a connection, creating a table, inserting data, querying data, and printing the results. Error handling is included for each step.

```go
package main

import (
	"database/sql"
	"errors"
	"fmt"
	"log"

	_ "github.com/duckdb/duckdb-go/v2"
)

func main() {
	db, err := sql.Open("duckdb", "")
	if err != nil {
		log.Fatal(err)
	}
	defer db.Close()

	_, err = db.Exec(`CREATE TABLE people (id INTEGER, name VARCHAR)`)
	if err != nil {
		log.Fatal(err)
	}
	_, err = db.Exec(`INSERT INTO people VALUES (42, 'John')`)
	if err != nil {
		log.Fatal(err)
	}

	var (
		id   int
		name string
	)
	row := db.QueryRow(`SELECT id, name FROM people`)
	err = row.Scan(&id, &name)
	if errors.Is(err, sql.ErrNoRows) {
		log.Println("no rows")
	} else if err != nil {
		log.Fatal(err)
	}

	fmt.Printf("id: %d, name: %s\n", id, name)
}
```

--------------------------------

### DuckDB SQL: Setup and Summarize TPC-H Table

Source: https://duckdb.org/docs/stable/guides/meta/summarize

This sequence of SQL commands demonstrates how to set up the TPC-H dataset and then use the SUMMARIZE command on the 'lineitem' table. It first installs and loads the 'tpch' extension, generates the data, and then applies SUMMARIZE to inspect the 'lineitem' table's columns.

```sql
INSTALL tpch;
LOAD tpch;
CALL dbgen(sf = 1);

SUMMARIZE lineitem;
```

--------------------------------

### Install Jupyter Notebook with Pip

Source: https://duckdb.org/docs/stable/guides/python/jupyter

Installs the Jupyter Notebook environment. This is necessary for running the provided Python code examples and interactive sessions.

```bash
pip install notebook

```

--------------------------------

### Install DuckDB CLI via Script (Linux/macOS)

Source: https://duckdb.org/docs/stable/installation/index

Installs the DuckDB Command Line Interface (CLI) using a shell script. This is a universal method for Linux and macOS.

```shell
curl https://install.duckdb.org | sh
```

--------------------------------

### Verify DuckDB Python Installation

Source: https://duckdb.org/docs/stable/dev/building/python

Executes a simple SQL query using the installed DuckDB Python package to confirm that the installation was successful and the package is functional.

```python
uv run python -c "import duckdb; print(duckdb.sql('SELECT 42').fetchall())"
```

--------------------------------

### Install and Load MySQL Extension

Source: https://duckdb.org/docs/stable/core_extensions/mysql

Instructions for installing and loading the MySQL extension in DuckDB.

```APIDOC
## Install and Load MySQL Extension

To install the `mysql` extension, run:

```sql
INSTALL mysql;
```

The extension is loaded automatically upon first use. If you prefer to load it manually, run:

```sql
LOAD mysql;
```
```

--------------------------------

### Install DuckDB Extensions after Build

Source: https://duckdb.org/docs/stable/dev/building/building_extensions

This snippet shows how to navigate to the extension build directory (release or debug) and then install each built extension using a shell loop. The `../duckdb -c "INSTALL '${EXTENSION}/${EXTENSION}.duckdb_extension';"` command installs the extension.

```shell
# for release builds
cd build/release/extension/
# for debug builds
cd build/debug/extension/
# install extensions
for EXTENSION in *
    ../duckdb -c "INSTALL '${EXTENSION}/${EXTENSION}.duckdb_extension';"
done

```

--------------------------------

### Install DuckDB CLI via Docker

Source: https://duckdb.org/docs/stable/installation/index

Runs the DuckDB Docker image, mounting the current directory as a volume. This allows for isolated DuckDB usage without direct installation.

```docker
docker run --rm -it -v "$(pwd):/workspace" -w /workspace duckdb/duckdb
```

--------------------------------

### Install DuckDB Extension from Explicit Path

Source: https://duckdb.org/docs/stable/extensions/advanced_installation_methods

Demonstrates how to install a DuckDB extension using the `INSTALL` command with a specified file path. This path can be local or remote. Note that compressed `.duckdb_extension.gz` files must be decompressed before installation.

```sql
INSTALL 'path/to/httpfs.duckdb_extension';
```

--------------------------------

### Install DuckDB CLI via Winget (Windows)

Source: https://duckdb.org/docs/stable/installation/index

Installs the DuckDB CLI on Windows using the Winget package manager. This command is suitable for Windows 10 and later.

```shell
winget install DuckDB.cli
```

--------------------------------

### Start DuckDB UI from Command Line

Source: https://duckdb.org/docs/stable/core_extensions/ui

Launches the DuckDB UI in the default browser directly from the command line. This method starts a UI connected to the current DuckDB instance.

```bash
duckdb -ui
```

--------------------------------

### DuckDB: Create Example Table for Prepared Statements

Source: https://duckdb.org/docs/stable/sql/query_syntax/prepared_statements

This SQL snippet creates a 'person' table and inserts sample data, which is used in subsequent examples to demonstrate prepared statement functionalities.

```sql
CREATE TABLE person (name VARCHAR, age BIGINT);
INSERT INTO person VALUES ('Alice', 37), ('Ana', 35), ('Bob', 41), ('Bea', 25);
```

--------------------------------

### Install DuckDB PHP Client using Composer

Source: https://duckdb.org/docs/stable/clients/php

This command installs the DuckDB PHP client automatically using Composer. It is the recommended method for new users. Ensure you have Composer installed and configured to allow execution of the package's code.

```bash
composer require satur.io/duckdb-auto
```

--------------------------------

### Get Supported GDAL Drivers and Formats

Source: https://duckdb.org/docs/stable/core_extensions/spatial/functions

Returns a list of GDAL drivers and file formats that are supported by the current DuckDB installation. This helps in determining which file types can be read or written.

```sql
SELECT ST_Drivers();
```

--------------------------------

### Attach and Use DuckLake Database

Source: https://duckdb.org/docs/stable/core_extensions/ducklake

Example of attaching to a DuckLake formatted database and setting it as the current database context. This assumes the DuckLake extension is installed and loaded.

```sql
ATTACH 'ducklake:metadata.ducklake' AS my_ducklake (DATA_PATH 'data_files');
USE my_ducklake;

```

--------------------------------

### Install DuckDB Extension using SQL

Source: https://duckdb.org/docs/stable/sql/statements/load_and_install

The INSTALL statement downloads an extension from the default catalog or a specified catalog, making it available for loading. It does not load the extension into the current session.

```sql
INSTALL httpfs;

```

```sql
INSTALL h3 FROM community;

```

--------------------------------

### Name Qualification Examples

Source: https://duckdb.org/docs/stable/sql/statements/attach

Provides examples of fully qualified names for catalogs, schemas, and tables, and demonstrates creating objects and referencing columns using these qualified names. It also shows how unqualified names are resolved and how to create tables in the default database.

```sql
ATTACH 'new_db.db';
CREATE SCHEMA new_db.my_schema;
CREATE TABLE new_db.my_schema.my_table (col INTEGER);
SELECT new_db.my_schema.my_table.col FROM new_db.my_schema.my_table;
```

```sql
CREATE TABLE my_table (col INTEGER);
```

--------------------------------

### Install DuckDB Extension from Specific Repository

Source: https://duckdb.org/docs/stable/extensions/installing_extensions

Explicitly installs an extension from a specified repository, either by alias or by URL. This is useful for managing extensions from different sources like 'core', 'core_nightly', or custom repositories, ensuring you get the exact version or build you need.

```sql
INSTALL httpfs FROM core;
-- or
INSTALL httpfs FROM 'http://extensions.duckdb.org';
```

```sql
INSTALL spatial FROM core_nightly;
-- or
INSTALL spatial FROM 'http://nightly-extensions.duckdb.org';
```

```sql
INSTALL custom_extension FROM 'https://my-custom-extension-repository';
```

--------------------------------

### Install DuckDB R Package

Source: https://duckdb.org/docs/stable/installation/index

Installs the DuckDB R package. It supports installation from a specific R-universe repository or CRAN.

```r
install.packages("duckdb", repos = c("https://duckdb.r-universe.dev", "https://cloud.r-project.org"))
```

```r
install.packages("duckdb")
```

```r
options(HTTPUserAgent = sprintf("R/%s R (%s)", getRversion(), paste(getRversion(), R.version["platform"], R.version["arch"], R.version["os"])))
install.packages("duckdb", repos="https://p3m.dev/cran/__linux__/manylinux_2_28/latest/")
```

--------------------------------

### DuckLake Extension Installation and Loading

Source: https://duckdb.org/docs/stable/core_extensions/ducklake

Instructions on how to install and load the DuckLake extension in DuckDB.

```APIDOC
## Installing and Loading DuckLake Extension

### Description
This section details how to install and load the DuckLake extension for use within DuckDB.

### Installation
To install the `ducklake` extension, run the following SQL command:

```sql
INSTALL ducklake;
```

### Loading
The `ducklake` extension is automatically loaded on first use within an `ATTACH` clause. However, it can also be loaded manually using the following command:

```sql
LOAD ducklake;
```
```

--------------------------------

### Install DuckDB Extension from Specific Repository

Source: https://duckdb.org/docs/stable/extensions/overview

Illustrates how to specify a repository (alias or URL) when installing an extension using the `INSTALL` or `FORCE INSTALL` command. This allows for targeted installation from custom or community repositories.

```sql
INSTALL <extension_name> FROM <repository_alias_or_url>;

```

--------------------------------

### Install DuckDB CLI via Homebrew (macOS)

Source: https://duckdb.org/docs/stable/installation/index

Installs the DuckDB CLI on macOS using the Homebrew package manager. Ensure Homebrew is installed and updated before running this command.

```shell
brew install duckdb
```

--------------------------------

### DuckDB C API Prepared Statement Example

Source: https://duckdb.org/docs/stable/clients/c/prepared

This C code demonstrates how to use DuckDB's prepared statements for both INSERT and SELECT operations. It shows the process of preparing a statement, binding integer parameters, executing the statement, and cleaning up resources. The example highlights handling potential errors during preparation and execution.

```c
duckdb_prepared_statement stmt;
duckdb_result result;
if (duckdb_prepare(con, "INSERT INTO integers VALUES ($1, $2)", &stmt) == DuckDBError) {
    // handle error
}

duckdb_bind_int32(stmt, 1, 42); // the parameter index starts counting at 1!
duckdb_bind_int32(stmt, 2, 43);
// NULL as second parameter means no result set is requested
duckdb_execute_prepared(stmt, NULL);
duckdb_destroy_prepare(&stmt);

// we can also query result sets using prepared statements
if (duckdb_prepare(con, "SELECT * FROM integers WHERE i = ?", &stmt) == DuckDBError) {
    // handle error
}
duckdb_bind_int32(stmt, 1, 42);
duckdb_execute_prepared(stmt, &result);

// do something with result

// clean up
duckdb_destroy_result(&result);
duckdb_destroy_prepare(&stmt);

```

--------------------------------

### Run marimo SQL Tutorial

Source: https://duckdb.org/docs/stable/guides/python/marimo

Executes the SQL tutorial provided by marimo to demonstrate its SQL integration capabilities.

```shell
marimo tutorial sql
```

--------------------------------

### DuckDB List of Structs Example

Source: https://duckdb.org/docs/stable/sql/data_types/typecasting

A simple example demonstrating a list containing struct elements in DuckDB.

```sql
SELECT [{'a': 42}, {'b': 84}];

```

--------------------------------

### Install DuckDB Node.js Package

Source: https://duckdb.org/docs/stable/installation/index

Installs the DuckDB Node.js API package using npm. This enables DuckDB integration within Node.js applications.

```javascript
npm install @duckdb/node-api
```

--------------------------------

### Initializing CLI with Custom Configuration File

Source: https://duckdb.org/docs/stable/clients/cli/overview

Demonstrates how to use the `-init` flag to specify a custom initialization file (e.g., `prompt.sql`) for the DuckDB CLI. This file can contain dot commands and SQL statements to configure the CLI on startup.

```bash
duckdb -init prompt.sql

```

--------------------------------

### DuckDB COPY TO Syntax Example

Source: https://duckdb.org/docs/stable/sql/statements/copy

Demonstrates the basic syntax for the COPY TO command in DuckDB, including specifying output file, WITH options for format, delimiter, and header.

```sql
COPY (SELECT 42 AS x, 84 AS y) TO 'out.csv' WITH DELIMITER '|' CSV HEADER;
```

--------------------------------

### Query Installed DuckDB Extensions

Source: https://duckdb.org/docs/stable/extensions/installing_extensions

Retrieves metadata about installed extensions, including their names, versions, the repository they were installed from, and the installation mode. This query is essential for understanding the origins and versions of extensions, especially when working with multiple repositories.

```sql
SELECT extension_name, extension_version, installed_from, install_mode
FROM duckdb_extensions();
```

--------------------------------

### Build and Install DuckDB Python Client from Source

Source: https://duckdb.org/docs/stable/guides/python/install

Installs the DuckDB Python client from its source code. This involves building DuckDB with Python support and then installing the Python package.

```bash
BUILD_PYTHON=1 GEN=ninja make
cd tools/pythonpkg
python setup.py install
```

--------------------------------

### Creating Example Address Table in DuckDB SQL

Source: https://duckdb.org/docs/stable/sql/query_syntax/orderby

Defines and populates an example 'addresses' table used in subsequent ORDER BY clause examples. This table contains address, city, and zip code information.

```sql
CREATE OR REPLACE TABLE addresses AS
    SELECT '123 Quack Blvd' AS address, 'DuckTown' AS city, '11111' AS zip
    UNION ALL
    SELECT '111 Duck Duck Goose Ln', 'DuckTown', '11111'
    UNION ALL
    SELECT '111 Duck Duck Goose Ln', 'Duck Town', '11111'
    UNION ALL
    SELECT '111 Duck Duck Goose Ln', 'Duck Town', '11111-0001';
```

--------------------------------

### Example sqllogictest File Structure

Source: https://duckdb.org/docs/stable/dev/sqllogictest/intro

An example of a self-contained sqllogictest file. It includes test metadata, SQL statements with expected outcomes (statement ok, query II), and result verification.

```sql
# name: test/sql/projection/test_simple_projection.test
# group [projection]

# enable query verification
statement ok
PRAGMA enable_verification

# create table
statement ok
CREATE TABLE a (i INTEGER, j INTEGER);

# insertion: 1 affected row
statement ok
INSERT INTO a VALUES (42, 84);

query II
SELECT * FROM a;
----
42	84

```

--------------------------------

### DuckDB Persistent Database Testing with Load and Restart

Source: https://duckdb.org/docs/stable/dev/sqllogictest/persistent_testing

Demonstrates how to use the `load` command to initiate a persistent database from disk and the `restart` command to reload it. This is useful for testing scenarios requiring persistent storage, overriding the default in-memory mode unless `--force-storage` is enabled. The example includes SQL statements for table creation and data insertion.

```sql
# load the DB from disk
load __TEST_DIR__/storage_scan.db

statement ok
CREATE TABLE test (a INTEGER);

statement ok
INSERT INTO test VALUES (11), (12), (13), (14), (15), (NULL)

# ...

restart

query I
SELECT * FROM test ORDER BY a
----
NULL
11
12
13
14
15
```

--------------------------------

### Load DuckDB Extensions via SQL

Source: https://duckdb.org/docs/stable/clients/cli/overview

This snippet illustrates how to load extensions within DuckDB using standard SQL commands. The `INSTALL` command downloads and installs the extension, and the `LOAD` command makes it available for use in subsequent queries. This requires the extension to be available in DuckDB's catalog.

```sql
INSTALL fts;
LOAD fts;
```

--------------------------------

### Initialize and Connect to DuckDB Database (C)

Source: https://duckdb.org/docs/stable/clients/c/connect

Demonstrates the basic process of opening a DuckDB database, connecting to it, executing queries (placeholder), and then properly disconnecting and closing the database to prevent resource leaks. It highlights the use of `duckdb_open` for database initialization and `duckdb_connect` for establishing a connection.

```c
duckdb_database db;
duckdb_connection con;

if (duckdb_open(NULL, &db) == DuckDBError) {
    // handle error
}
if (duckdb_connect(db, &con) == DuckDBError) {
    // handle error
}

// run queries...

// cleanup
duckdb_disconnect(&con);
duckdb_close(&db);

```

--------------------------------

### DuckDB SQL: Example Usage of Table Macro

Source: https://duckdb.org/docs/stable/sql/statements/create_macro

Demonstrates how to use the `get_users` table macro by first creating a sample `users` table and then querying it with a list of user IDs. It also shows an example of defining and using the `checksum` macro on a table.

```sql
CREATE TABLE users AS
    SELECT * 
    FROM (VALUES (1, 'Ada'), (2, 'Bob'), (3, 'Carl'), (4, 'Dan'), (5, 'Eve')) t(uid, name);
SELECT * FROM get_users([1, 5]);

CREATE TABLE tbl AS SELECT unnest([42, 43]) AS x, 100 AS y;
SELECT * FROM checksum('tbl');
```

--------------------------------

### Benchmark File Header Example

Source: https://duckdb.org/docs/stable/dev/benchmark

Example of the header format for a DuckDB benchmark file. It includes the benchmark name and a description of its purpose. This format is used when creating new benchmarks.

```plaintext
# name: benchmark/micro/window/window_fill.benchmark
# description: Measure the perfomance of FILL

```

--------------------------------

### Install Core DuckDB Extension

Source: https://duckdb.org/docs/stable/extensions/installing_extensions

Installs an extension from the default 'core' repository. This ensures the stability and security of the extension as it is built and signed by the core DuckDB team. This command uses the default repository which points to http://extensions.duckdb.org.

```sql
INSTALL httpfs;
```

--------------------------------

### Initializing the Database

Source: https://duckdb.org/docs/stable/clients/nodejs/overview

Demonstrates how to load the DuckDB Node.js package and create a database instance, either in-memory or file-based. Optionally, configuration options like access mode, memory limits, and threads can be provided.

```APIDOC
## Initializing the DuckDB Database

### Description
Load the `duckdb` package and create a database object. You can specify an in-memory database (`':memory:'`) or a file path for a persistent database.

### Method
`new duckdb.Database(path, [options], [callback])`

### Parameters
#### Path Parameters
- **path** (string) - Required - The path to the database file, or `':memory:'` for an in-memory database.

#### Request Body
- **options** (object) - Optional - Configuration options for the database.
  - **access_mode** (string) - Optional - `'READ_WRITE'` or `'READ_ONLY'`.
  - **max_memory** (string) - Optional - e.g., `'512MB'`.
  - **threads** (string) - Optional - e.g., `'4'`.
- **callback** (function) - Optional - A callback function that is invoked after the database is initialized.

### Request Example
```javascript
const duckdb = require('duckdb');

// In-memory database
const db = new duckdb.Database(':memory:');

// Persistent database
// const db = new duckdb.Database('my_database.duckdb');

// With options and callback
const dbWithOptions = new duckdb.Database(':memory:', {
    "access_mode": "READ_WRITE",
    "max_memory": "512MB",
    "threads": "4"
}, (err) => {
  if (err) {
    console.error(err);
  } else {
    console.log('Database initialized successfully');
  }
});
```

### Response
#### Success Response (200)
- **db** (object) - The initialized DuckDB database object.
```

--------------------------------

### INSTALL Statement

Source: https://duckdb.org/docs/stable/sql/statements/load_and_install

The INSTALL statement downloads an extension so it can be loaded into a DuckDB session.

```APIDOC
## INSTALL

The `INSTALL` statement downloads an extension so it can be loaded into a DuckDB session.

### Examples

Install the `httpfs` extension:
```sql
INSTALL httpfs;
```

Install the `h3` community extension:
```sql
INSTALL h3 FROM community;
```

### Syntax

(Syntax details not provided in the input)
```

--------------------------------

### Install Nightly Extension with Stable DuckDB (SQL)

Source: https://duckdb.org/docs/stable/extensions/versioning_of_extensions

This SQL snippet demonstrates how to install and load a nightly build of an extension (e.g., 'aws') while using a stable version of DuckDB. This allows testing new features without fully switching to unstable DuckDB builds.

```sql
INSTALL aws FROM core_nightly;
LOAD aws;
```

--------------------------------

### DuckDB Logging Syntactic Sugar Examples

Source: https://duckdb.org/docs/stable/operations_manual/logging/overview

Demonstrates syntactic sugar in DuckDB for enabling logging, showing equivalent ways to specify storage and configuration parameters. Omitting the 'storage' parameter implies 'file' when 'storage_config' or 'storage_path' is present.

```sql
-- regular invocation 
CALL enable_logging(storage = 'file', storage_config = {'path': 'path/to/store/logs'});
```

```sql
-- using shorthand for common path storage config param 
CALL enable_logging(storage = 'file', storage_path = 'path/to/store/logs');
```

```sql
-- omitting `storage = 'file'` -> is implied from presence of `storage_config`
CALL enable_logging(storage_config = {'path': 'path/to/store/logs'});
```

--------------------------------

### Install DuckDB HTTPFS and Iceberg Extensions

Source: https://duckdb.org/docs/stable/guides/network_cloud_storage/s3_iceberg_import

Installs the necessary httpfs and iceberg extensions for S3 and Iceberg integration. These extensions only need to be installed once per DuckDB instance.

```sql
INSTALL httpfs;
INSTALL iceberg;
```

--------------------------------

### Install Pre-release DuckDB Python Client via Pip

Source: https://duckdb.org/docs/stable/guides/python/install

Installs the pre-release (preview or nightly) version of the DuckDB Python client using pip with the --pre flag. This command also upgrades the package if it's already installed.

```bash
pip install duckdb --upgrade --pre
```

--------------------------------

### Install DuckDB CLI via PowerShell Script (Windows Alpha)

Source: https://duckdb.org/docs/stable/installation/index

Installs DuckDB on Windows using an alpha PowerShell script. This method requires administrative privileges and setting execution policy. Use with caution.

```powershell
Set-ExecutionPolicy Bypass -Scope Process -Force
[System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072
iex ((New-Object System.Net.WebClient).DownloadString('https://install.duckdb.org/install.ps1'))
```

--------------------------------

### Configure DuckDB Database Settings using C API

Source: https://duckdb.org/docs/stable/clients/c/config

This example demonstrates how to create a DuckDB configuration object, set various database parameters such as access mode, threads, maximum memory, and default order, and then open the database with these configurations. It also shows the necessary steps for cleaning up the configuration object after use. This requires the DuckDB C API.

```c
duckdb_database db;
duckdb_config config;

// create the configuration object
if (duckdb_create_config(&config) == DuckDBError) {
    // handle error
}
// set some configuration options
duckdb_set_config(config, "access_mode", "READ_WRITE"); // or READ_ONLY
duckdb_set_config(config, "threads", "8");
duckdb_set_config(config, "max_memory", "8GB");
duckdb_set_config(config, "default_order", "DESC");

// open the database using the configuration
if (duckdb_open_ext(NULL, &db, config, NULL) == DuckDBError) {
    // handle error
}
// cleanup the configuration object
duckdb_destroy_config(&config);

// run queries...

// cleanup
duckdb_close(&db);

```

--------------------------------

### Install PostgreSQL Extension

Source: https://duckdb.org/docs/stable/guides/database_integration/postgres

Installs the PostgreSQL extension for DuckDB. This command only needs to be executed once.

```sql
INSTALL postgres;

```

--------------------------------

### type

Source: https://duckdb.org/docs/stable/clients/python/reference

Gets the type of the relation. Detailed examples can be found at the Relational API page.

```APIDOC
## type

### Description
Gets the type of the relation.

### Method
`type`

### Parameters
- `_self` (_duckdb.DuckDBPyRelation_) - The relation object.

### Request Example
```python
relation.type
```

### Response
#### Success Response (str)
The type of the relation as a string.

#### Response Example
```json
"Relation"
```
```

--------------------------------

### Install and Load AWS Extension

Source: https://duckdb.org/docs/stable/core_extensions/aws

Demonstrates how to install and load the AWS extension in DuckDB. This extension enhances httpfs capabilities for S3 access using the AWS SDK.

```sql
INSTALL aws;
LOAD aws;
```

--------------------------------

### DuckDB SQL: Example table creation and GROUPING SETS query

Source: https://duckdb.org/docs/stable/sql/query_syntax/grouping_sets

Provides SQL statements to create a 'students' table and demonstrates a GROUP BY with GROUPING SETS. This example showcases counting students across different course and type combinations, including aggregate results.

```sql
CREATE TABLE students (course VARCHAR, type VARCHAR);
INSERT INTO students (course, type)
VALUES
    ('CS', 'Bachelor'), ('CS', 'Bachelor'), ('CS', 'PhD'), ('Math', 'Masters'),
    ('CS', NULL), ('CS', NULL), ('Math', NULL);


```

```sql
SELECT course, type, count(*)
FROM students
GROUP BY GROUPING SETS ((course, type), course, type, ());

```

--------------------------------

### Get DuckDB Version

Source: https://duckdb.org/docs/stable/configuration/pragmas

Retrieves the current version of the DuckDB installation.

```sql
PRAGMA version;
CALL pragma_version();
```

--------------------------------

### Start DuckDB UI from SQL

Source: https://duckdb.org/docs/stable/core_extensions/ui

Initiates the DuckDB UI by executing a SQL command within a DuckDB client. This command opens the UI in the default browser, connected to the active DuckDB instance.

```sql
CALL start_ui();
```

--------------------------------

### Get Current Local Timestamp

Source: https://duckdb.org/docs/stable/sql/functions/timestamp

Returns the current timestamp at the start of the transaction.

```sql
current_localtimestamp()
```

--------------------------------

### Install DuckDB Extension via Python API

Source: https://duckdb.org/docs/stable/extensions/installing_extensions

Demonstrates installing a DuckDB extension using the Python client API. This method provides an alternative to SQL commands for managing extensions within a Python environment, offering programmatic control over extension installation and loading.

```python
import duckdb

con = duckdb.connect(database=':memory:', read_only=False)

# Install an extension
con.install_extension('httpfs')

# Load the extension (often done automatically after install, but can be explicit)
con.load_extension('httpfs')

con.close()
```

--------------------------------

### Install YouPlot CLI Tool

Source: https://duckdb.org/docs/stable/guides/data_viewers/youplot

This command installs the YouPlot CLI tool using Homebrew on macOS. Ensure Homebrew is installed before running this command. After installation, run `uplot --help` to verify.

```shell
brew install youplot
```

--------------------------------

### Install and Load DuckDB Extensions (Python)

Source: https://duckdb.org/docs/stable/clients/python/overview

This code illustrates how to install and load extensions in DuckDB using its Python API. It first establishes a connection, then uses `con.install_extension()` to install the 'spatial' extension, followed by `con.load_extension()` to enable it for use.

```python
import duckdb

con = duckdb.connect()
con.install_extension("spatial")
con.load_extension("spatial")
```

--------------------------------

### Connect to Database using SQLConnect (C++)

Source: https://duckdb.org/docs/stable/guides/odbc/general

Initializes ODBC handles, sets the ODBC version, and establishes a connection to the database using the `SQLConnect` function. This method typically uses a DSN defined in the system's ODBC configuration.

```c++
SQLHANDLE env;
SQLHANDLE dbc;

SQLAllocHandle(SQL_HANDLE_ENV, SQL_NULL_HANDLE, &env);

SQLSetEnvAttr(env, SQL_ATTR_ODBC_VERSION, (void*)SQL_OV_ODBC3, 0);

SQLAllocHandle(SQL_HANDLE_DBC, env, &dbc);

std::string dsn = "DSN=duckdbmemory";
SQLConnect(dbc, (SQLCHAR*)dsn.c_str(), SQL_NTS, NULL, 0, NULL, 0);

std::cout << "Connected!" << std::endl;


```

--------------------------------

### DuckDB SQL: Install non-existent extension

Source: https://duckdb.org/docs/stable/extensions/troubleshooting

This SQL code demonstrates an attempt to install an extension that does not exist in the DuckDB extension repository. It's used to trigger the error message shown in the troubleshooting guide.

```sql
INSTALL non_existing;

```

--------------------------------

### Install Latest DuckDB CLI (Linux/macOS)

Source: https://duckdb.org/docs/stable/operations_manual/installing_duckdb/install_script

This command downloads and executes the official DuckDB installation script for Linux and macOS. It installs the latest stable version to the user's home directory and provides instructions for adding it to the system's PATH.

```shell
curl https://install.duckdb.org | sh

```

--------------------------------

### DuckDB SQL: Create Sequence for Odd Numbers

Source: https://duckdb.org/docs/stable/sql/statements/create_sequence

This example illustrates creating a sequence that generates only odd numbers by specifying a starting value and an increment of 2. This is achieved using the START WITH and INCREMENT BY clauses.

```sql
CREATE SEQUENCE serial START WITH 1 INCREMENT BY 2;
```

--------------------------------

### DuckDB SQL: Create Table and Select Example

Source: https://duckdb.org/docs/stable/sql/dialect/order_preservation

Demonstrates creating a simple table named 'tbl' with two columns 'x' and 'y' and then selecting all rows from it. This serves as a basis for illustrating order preservation.

```sql
CREATE TABLE tbl AS
    SELECT * 
    FROM (VALUES (1, 'a'), (2, 'b'), (3, 'c')) t(x, y);

SELECT * 
FROM tbl;
```

--------------------------------

### DuckDB 1-Based List Indexing Example

Source: https://duckdb.org/docs/stable/sql/dialect/indexing

Demonstrates how DuckDB uses 1-based indexing for accessing elements in lists. The example selects the first element from a list of strings.

```sql
SELECT list[1] AS element
FROM (SELECT ['first', 'second', 'third'] AS list);
```

--------------------------------

### Install and Load SQLSmith Extension

Source: https://duckdb.org/docs/stable/core_extensions/sqlsmith

This code snippet demonstrates how to install and load the SQLSmith extension within a DuckDB environment. Ensure you have the necessary permissions to install extensions.

```sql
INSTALL sqlsmith;
LOAD sqlsmith;

```

--------------------------------

### DuckDB bit_position Function

Source: https://duckdb.org/docs/stable/sql/functions/bitstring

Returns the starting index of the first occurrence of a substring within a BITSTRING. Returns zero if the substring is not found. Indexing starts from 1. Example: `bit_position('010', '1110101')` returns `4`.

```sql
SELECT bit_position('010'::BITSTRING, '1110101'::BITSTRING);
```

--------------------------------

### Install DuckDB Python Client on Alpine Linux

Source: https://duckdb.org/docs/stable/dev/building/linux

Installs necessary packages and then installs the DuckDB Python client from source on Alpine Linux.

```bash
apk add g++ py3-pip python3-dev
pip install duckdb
```

--------------------------------

### Instantiate DuckDB Database (Swift)

Source: https://duckdb.org/docs/stable/clients/swift

Demonstrates how to create an in-memory DuckDB database and a persistent database stored in a file. Both methods require the 'DuckDB' library.

```swift
import DuckDB

// In-memory database
let database = try Database(store: .inMemory)

// Persistent database
let database = try Database(store: .file(at: "test.db"))
```

--------------------------------

### Include SQL Header Files for ODBC

Source: https://duckdb.org/docs/stable/guides/odbc/general

Includes the necessary SQL header files for ODBC development. Requires the 'unixodbc' package to be installed. The installation command varies by operating system (macOS, Ubuntu/Debian, Fedora/CentOS/Red Hat). You must also configure your build system (Makefile or Cmake) to include the header file location.

```c++
#include <sql.h>
#include <sqlext.h>

```

--------------------------------

### PostgreSQL Extension Installation and Loading

Source: https://duckdb.org/docs/stable/core_extensions/postgres

Instructions on how to install and load the PostgreSQL extension in DuckDB.

```APIDOC
## Installing and Loading the PostgreSQL Extension

The `postgres` extension is automatically loaded from the official extension repository on first use. To install and load it manually, use the following commands:

```sql
INSTALL postgres;
LOAD postgres;
```
```

--------------------------------

### Build DuckDB Go Client on Windows

Source: https://duckdb.org/docs/stable/dev/building/windows

This snippet provides the environment variables and commands required to build the DuckDB Go client on Windows. It involves setting the PATH and CGO environment variables to include the DuckDB libraries and then running 'go build'. This method addresses a common 'ld returned 5 exit status' error.

```batch
set PATH=C:\duckdb-go\libs\;%PATH%
set CGO_CFLAGS=-IC:\duckdb-go\libs\
set CGO_LDFLAGS=-LC:\duckdb-go\libs\ -lduckdb
go build

```

--------------------------------

### Anti Join Example (SQL)

Source: https://duckdb.org/docs/stable/sql/query_syntax/from

Demonstrates an anti join, which returns rows from the left table that have no matches in the right table. This example finds cities without corresponding airport names, ignoring NULLs in the right table.

```SQL
SELECT *
FROM city_airport
ANTI JOIN airport_names
    USING (iata);

-- Equivalent to:
SELECT *
FROM city_airport
WHERE iata NOT IN (SELECT iata FROM airport_names WHERE iata IS NOT NULL);
```

--------------------------------

### Install and Load TPC-H Extension

Source: https://duckdb.org/docs/stable/core_extensions/tpch

Installs and loads the TPC-H extension into DuckDB. This extension is often included by default or autoloaded on first use, but manual installation and loading are supported.

```sql
INSTALL tpch;
LOAD tpch;
```

--------------------------------

### Install and Load MySQL Extension for DuckDB

Source: https://duckdb.org/docs/stable/core_extensions/mysql

Instructions to install and load the MySQL extension in DuckDB. The extension is often loaded automatically on first use, but manual loading is also supported.

```sql
INSTALL mysql;

LOAD mysql;
```

--------------------------------

### Install Ibis using Mamba

Source: https://duckdb.org/docs/stable/guides/python/ibis

Installs the Ibis framework using the Mamba package manager, known for its speed. This is another alternative installation method, often used for faster package resolution compared to Conda.

```bash
mamba install ibis-framework
```

--------------------------------

### Working Macro Example with 'lower' (DuckDB)

Source: https://duckdb.org/docs/stable/sql/statements/create_macro

Provides an example of a working macro ('low') that correctly uses the 'lower' function, demonstrating standard macro functionality before illustrating a limitation.

```duckdb
CREATE OR REPLACE MACRO low(s) AS lower(s);
SELECT low('AA');

```

--------------------------------

### explain

Source: https://duckdb.org/docs/stable/clients/python/reference

Provides a detailed explanation of the query execution plan.

```APIDOC
## GET /explain

### Description
Provides a detailed explanation of the query execution plan.

### Method
GET

### Endpoint
/explain

### Parameters
#### Path Parameters
None

#### Query Parameters
* **type** (_duckdb.ExplainType_) - Optional - Defaults to 'standard'. The type of explanation to generate (e.g., 'standard', 'json').

### Request Body
None

### Response
#### Success Response (200)
- **str** - A string containing the query execution plan.

#### Response Example
```json
"EXPLAIN SELECT * FROM ..."
```
```

--------------------------------

### DuckDB Relational API: Get Column Names

Source: https://duckdb.org/docs/stable/clients/python/reference/index

Returns a list containing the names of all columns in the relation. This is useful for inspecting the schema of the data. Detailed examples are available on the Relational API page.

```Python
relation.columns
```

--------------------------------

### Parameterizing FILL Benchmark with Arguments

Source: https://duckdb.org/docs/stable/dev/benchmark

Demonstrates how to define parameters for the FILL benchmark using the 'argument' keyword. These arguments, such as scale factor, error rate, and number of keys, allow for flexible benchmark execution with varying settings.

```sql
argument sf 10
argument errors 0.1
argument keys 4
```

--------------------------------

### DuckDB Relational API: Get Alias Name

Source: https://duckdb.org/docs/stable/clients/python/reference/index

Retrieves the alias name of the current relation. This is useful for identifying aliased tables or subqueries. Detailed examples are available on the Relational API page.

```Python
relation.alias()
```

--------------------------------

### Install and Load Inet Extension in DuckDB

Source: https://duckdb.org/docs/stable/core_extensions/inet

This snippet shows how to install and load the 'inet' extension in DuckDB. The extension is usually autoloaded on first use from the official repository, but manual installation and loading are also supported.

```sql
INSTALL inet;
LOAD inet;

```

--------------------------------

### Add DuckDB Rust Crate

Source: https://duckdb.org/docs/stable/installation/index

Adds the DuckDB Rust crate to a Cargo project, with the 'bundled' feature for a self-contained build. This facilitates using DuckDB in Rust applications.

```rust
cargo add duckdb --features bundled
```

--------------------------------

### Format Integers with Specifiers (fmt)

Source: https://duckdb.org/docs/stable/sql/functions/text

Demonstrates formatting integers using various specifiers within the `fmt` function. This includes padding with zeros, converting to hexadecimal or binary, and applying thousand separators with different delimiters.

```sql
SELECT format('{:04d}', 33);
-- Result: 0033

SELECT format('{:x}', 123456789);
-- Result: 75bcd15

SELECT format('{:b}', 123456789);
-- Result: 111010110111100110100010101
```

--------------------------------

### Run Tests by Percentage Range

Source: https://duckdb.org/docs/stable/dev/sqllogictest/debugging

Executes a subset of tests defined by start and end percentages. This allows for running tests proportionally, for example, 10% to 20% of the total test suite.

```bash
build/debug/test/unittest --start-offset-percentage=10 --end-offset-percentage=20
```

--------------------------------

### Install Ibis using Conda

Source: https://duckdb.org/docs/stable/guides/python/ibis

Installs the Ibis framework using the Conda package manager. This is an alternative installation method for users who prefer or require Conda for environment management.

```bash
conda install ibis-framework
```

--------------------------------

### Install Parquet Extension

Source: https://duckdb.org/docs/stable/data/parquet/overview

Installs the 'parquet' extension for DuckDB. This command is necessary if the Parquet functionality is not bundled with your DuckDB client.

```sql
INSTALL parquet;
```

--------------------------------

### DuckDB Relational API: Get Any Value

Source: https://duckdb.org/docs/stable/clients/python/reference/index

Returns the first non-null value from a specified column. Can be applied to the entire column or within window specifications. Detailed examples are available on the Relational API page.

```Python
relation.any_value(column, groups='', window_spec='', projected_columns='')
```

--------------------------------

### Install DuckDB R Client

Source: https://duckdb.org/docs/stable/clients/r

Installs the DuckDB R client package. This is the primary package for interacting with DuckDB from R.

```r
install.packages("duckdb")

```

--------------------------------

### Install Polars and PyArrow

Source: https://duckdb.org/docs/stable/guides/python/marimo

Installs the Polars library with PyArrow support, often used for efficient data manipulation alongside DuckDB in marimo notebooks.

```shell
pip install "polars[pyarrow]"
```

--------------------------------

### Filesystem and Relation Creation

Source: https://duckdb.org/docs/stable/clients/python/reference/index

Methods for checking filesystem registration, and creating relation objects from various data sources like Arrow objects, CSV files, pandas DataFrames, and Parquet files.

```APIDOC
## filesystem_is_registered /websites/duckdb_stable

### Description
Check if a filesystem with the provided name is currently registered.

### Method
GET (Implied)

### Endpoint
/websites/duckdb_stable

### Parameters
#### Query Parameters
- **name** (str) - Required - The name of the filesystem to check.

### Response
#### Success Response (200)
- **bool** (bool) - True if the filesystem is registered, False otherwise.

## from_arrow /websites/duckdb_stable

### Description
Create a relation object from an Arrow object.

### Method
POST (Implied)

### Endpoint
/websites/duckdb_stable

### Parameters
#### Request Body
- **arrow_object** (object) - Required - The Arrow object to convert.

### Response
#### Success Response (200)
- **Relation** (_duckdb.DuckDBPyRelation) - A relation object created from the Arrow object.

## from_csv_auto /websites/duckdb_stable

### Description
Create a relation object from the CSV file in ‘name’.

### Method
POST (Implied)

### Endpoint
/websites/duckdb_stable

### Parameters
#### Request Body
- **path_or_buffer** (object) - Required - Path or buffer containing the CSV data.
- **kwargs** - Optional - Additional keyword arguments for CSV parsing.

### Response
#### Success Response (200)
- **Relation** (_duckdb.DuckDBPyRelation) - A relation object created from the CSV data.

## from_df /websites/duckdb_stable

### Description
Create a relation object from the DataFrame in df.

### Method
POST (Implied)

### Endpoint
/websites/duckdb_stable

### Parameters
#### Request Body
- **df** (pandas.DataFrame) - Required - The pandas DataFrame to convert.

### Response
#### Success Response (200)
- **Relation** (_duckdb.DuckDBPyRelation) - A relation object created from the DataFrame.

## from_parquet /websites/duckdb_stable

### Description
Create a relation object from the Parquet files.

### Method
POST (Implied)

### Endpoint
/websites/duckdb_stable

### Parameters
#### Query Parameters
- **file_glob** (str) - Required (Overload 1) - Glob pattern for Parquet files.
- **file_globs** (Sequence[str]) - Required (Overload 2) - Sequence of glob patterns for Parquet files.
- **binary_as_string** (bool) - Optional - Treat binary data as strings.
- **file_row_number** (bool) - Optional - Include file row number.
- **filename** (bool) - Optional - Include filename.
- **hive_partitioning** (bool) - Optional - Enable Hive partitioning.
- **union_by_name** (bool) - Optional - Union files by column name.
- **compression** (object) - Optional - Compression codec.

### Response
#### Success Response (200)
- **Relation** (_duckdb.DuckDBPyRelation) - A relation object created from the Parquet files.

## read_csv /websites/duckdb_stable

### Description
Create a relation object from the CSV file in ‘name’.

### Method
POST (Implied)

### Endpoint
/websites/duckdb_stable

### Parameters
#### Request Body
- **path_or_buffer** (object) - Required - Path or buffer containing the CSV data.
- **kwargs** - Optional - Additional keyword arguments for CSV parsing.

### Response
#### Success Response (200)
- **Relation** (_duckdb.DuckDBPyRelation) - A relation object created from the CSV data.

```

--------------------------------

### DuckDB get_bit Function

Source: https://duckdb.org/docs/stable/sql/functions/bitstring

Extracts a specific bit from a BITSTRING at a given index. Indexing starts from 0 for the leftmost bit. Example: `get_bit('0110010', 2)` returns `1`.

```sql
SELECT get_bit('0110010'::BITSTRING, 2);
```

--------------------------------

### Explicitly Install and Load DuckDB Extension

Source: https://duckdb.org/docs/stable/extensions/overview

Shows the SQL commands to explicitly install and then load an extension (e.g., 'spatial') into a DuckDB instance. This method works for both autoloadable and non-autoloadable extensions and ensures the extension's functionality is available.

```sql
INSTALL spatial;
LOAD spatial;

```

--------------------------------

### Execute DuckDB Commands Sequentially

Source: https://duckdb.org/docs/stable/clients/cli/arguments

Demonstrates how to execute a sequence of commands, demonstrating the order of processing similar to the SQLite CLI. This example uses different output formats for different commands.

```bash
duckdb -csv -c 'SELECT 42 AS hello' -json -c 'SELECT 84 AS world'
```

--------------------------------

### List DuckDB Extensions using SQL Function

Source: https://duckdb.org/docs/stable/guides/meta/duckdb_environment

Get a list of all available DuckDB extensions and their current status (e.g., loaded, installed) by querying the `duckdb_extensions()` function.

```sql
SELECT *
FROM duckdb_extensions();

```

--------------------------------

### Install DuckDB CLI Client on Ubuntu/Debian

Source: https://duckdb.org/docs/stable/dev/building/linux

Installs necessary packages and builds the DuckDB CLI client from source on Ubuntu and Debian-based systems.

```bash
sudo apt-get update
sudo apt-get install -y git g++ cmake ninja-build libssl-dev libcurl4-openssl-dev
git clone https://github.com/duckdb/duckdb
cd duckdb
GEN=ninja make
```

--------------------------------

### Add DuckDB Java Dependency (Maven/Gradle)

Source: https://duckdb.org/docs/stable/installation/index

Includes DuckDB as a dependency for Java projects using Maven or Gradle build tools. This allows for programmatic access to DuckDB within Java applications.

```xml
<dependency>
    <groupId>org.duckdb</groupId>
    <artifactId>duckdb_jdbc</artifactId>
    <version>1.4.3.0</version>
</dependency>
```

```groovy
implementation("org.duckdb:duckdb_jdbc:1.4.3.0")
```

--------------------------------

### Load DuckDB Extension from Explicit Path

Source: https://duckdb.org/docs/stable/extensions/advanced_installation_methods

Shows how to load a DuckDB extension directly from an explicit file path using the `LOAD` command. This method bypasses any currently installed extensions. Remote paths for compressed files are not supported.

```sql
LOAD 'path/to/httpfs.duckdb_extension';
```

--------------------------------

### Get Current Transaction Timestamp (SQL)

Source: https://duckdb.org/docs/stable/sql/functions/timestamptz

Retrieves the current date and time at the start of the current transaction. This function is always available and does not require specific extensions. It returns a TIMESTAMPTZ value.

```sql
SELECT current_timestamp;
SELECT get_current_timestamp();
SELECT now();
SELECT transaction_timestamp();
```

--------------------------------

### Load DuckDB Extension using SQL

Source: https://duckdb.org/docs/stable/sql/statements/load_and_install

The LOAD statement loads an already installed DuckDB extension into the current session, allowing its functions and types to be used. This command requires the extension to be previously installed.

```sql
LOAD httpfs;

```

```sql
LOAD spatial;

```