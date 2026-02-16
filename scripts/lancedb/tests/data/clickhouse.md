### Install and Get Help for clickhouse-obfuscator

Source: https://github.com/clickhouse/clickhouse/blob/master/programs/obfuscator/README.md

Demonstrates how to install the ClickHouse client and access the help documentation for the obfuscator tool.

```bash
curl https://clickhouse.com/ | sh
./clickhouse obfuscator --help
```

--------------------------------

### MySQL Table Engine Usage Example - MySQL Setup

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/engines/table-engines/integrations/mysql.md

Provides an example of setting up a table in a MySQL server for use with the ClickHouse MySQL engine.

```text
mysql> CREATE TABLE `test`.`test` (
    ->   `int_id` INT NOT NULL AUTO_INCREMENT,
    ->   `int_nullable` INT NULL DEFAULT NULL,
    ->   `float` FLOAT NOT NULL,
    ->   `float_nullable` FLOAT NULL DEFAULT NULL,
    ->   PRIMARY KEY (`int_id`));
Query OK, 0 rows affected (0,09 sec)

mysql> insert into test (`int_id`, `float`) VALUES (1,2);
Query OK, 1 row affected (0,00 sec)

mysql> select * from test;
+------+----------+-----+----------+
| int_id | int_nullable | float | float_nullable |
+------+----------+-----+----------+
|      1 |         NULL |     2 |           NULL |
+------+----------+-----+----------+
1 row in set (0,00 sec)
```

--------------------------------

### Setup Database with IAA Deflate Codec

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/development/building_and_benchmarking_deflate_qpl.md

Configures and starts a Clickhouse server using the IAA Deflate codec and connects a client. Similar to LZ4 setup, this requires a specific configuration file.

```bash
cd ./database_dir/deflate
[CLICKHOUSE_EXE] server -C config_deflate.xml >&/dev/null&
[CLICKHOUSE_EXE] client
```

--------------------------------

### Example Table Setup

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/sql-reference/aggregate-functions/reference/estimateCompressionRatio.md

Creates a sample table named 'compression_estimate_example' with a 'number' column and populates it with 100,000 numbers for testing the estimateCompressionRatio function.

```SQL
CREATE TABLE compression_estimate_example
(
    `number` UInt64
)
ENGINE = MergeTree()
ORDER BY number
SETTINGS min_bytes_for_wide_part = 0;

INSERT INTO compression_estimate_example
SELECT number FROM system.numbers LIMIT 100_000;
```

--------------------------------

### Setup Database with ZSTD Codec

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/development/building_and_benchmarking_deflate_qpl.md

Configures and starts a Clickhouse server using the ZSTD codec and connects a client. This setup also requires a dedicated configuration file for the ZSTD codec.

```bash
cd ./database_dir/zstd
[CLICKHOUSE_EXE] server -C config_zstd.xml >&/dev/null&
[CLICKHOUSE_EXE] client
```

--------------------------------

### Setup Database with LZ4 Codec

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/development/building_and_benchmarking_deflate_qpl.md

Configures and starts a Clickhouse server using the LZ4 codec and connects a client. This involves specifying a configuration file and ensuring the server runs in the background.

```bash
cd ./database_dir/lz4
[CLICKHOUSE_EXE] server -C config_lz4.xml >&/dev/null&
[CLICKHOUSE_EXE] client
```

--------------------------------

### Protobuf Library and Include Setup

Source: https://github.com/clickhouse/clickhouse/blob/master/contrib/google-protobuf-cmake/CMakeLists.txt

Sets up the Protobuf library and its include directories for use within ClickHouse. It creates an interface library `_protobuf` and an alias `ch_contrib::protobuf`, linking against `_libprotobuf` and setting the include directories. It also lists the well-known Protobuf files that need to be installed.

```cmake
include("${ClickHouse_SOURCE_DIR}/contrib/google-protobuf-cmake/protobuf_generate.cmake")

# These files needs to be installed to make it possible that users can use well-known protobuf types
set(google_proto_files
  ${protobuf_source_dir}/src/google/protobuf/any.proto
  ${protobuf_source_dir}/src/google/protobuf/api.proto
  ${protobuf_source_dir}/src/google/protobuf/descriptor.proto
  ${protobuf_source_dir}/src/google/protobuf/duration.proto
  ${protobuf_source_dir}/src/google/protobuf/empty.proto
  ${protobuf_source_dir}/src/google/protobuf/field_mask.proto
  ${protobuf_source_dir}/src/google/protobuf/source_context.proto
  ${protobuf_source_dir}/src/google/protobuf/struct.proto
  ${protobuf_source_dir}/src/google/protobuf/timestamp.proto
  ${protobuf_source_dir}/src/google/protobuf/type.proto
  ${protobuf_source_dir}/src/google/protobuf/wrappers.proto
)

add_library(_protobuf INTERFACE)
target_link_libraries(_protobuf INTERFACE _libprotobuf)
target_include_directories(_protobuf INTERFACE "${Protobuf_INCLUDE_DIR}")
set_target_properties(_protobuf PROPERTIES google_proto_files "${google_proto_files}")
add_library(ch_contrib::protobuf ALIAS _protobuf)
```

--------------------------------

### Example apt-get update warnings

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/operations/_troubleshooting.md

Illustrates various warning messages that can appear during `apt-get update` for the ClickHouse repository, indicating potential configuration or architecture mismatches.

```text
N: Skipping acquire of configured file 'main/binary-i386/Packages' as repository 'https://packages.clickhouse.com/deb stable InRelease' doesn't support architecture 'i386'

E: Failed to fetch https://packages.clickhouse.com/deb/dists/stable/main/binary-amd64/Packages.gz  File has unexpected size (30451 != 28154). Mirror sync in progress?

E: Repository 'https://packages.clickhouse.com/deb stable InRelease' changed its 'Origin' value from 'Artifactory' to 'ClickHouse'
E: Repository 'https://packages.clickhouse.com/deb stable InRelease' changed its 'Label' value from 'Artifactory' to 'ClickHouse'
N: Repository 'https://packages.clickhouse.com/deb stable InRelease' changed its 'Suite' value from 'stable' to ''
N: This must be accepted explicitly before updates for this repository can be applied. See apt-secure(8) manpage for details.

Err:11 https://packages.clickhouse.com/deb stable InRelease
  400  Bad Request [IP: 172.66.40.249 443]
```

--------------------------------

### System Build Options Output Example

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/operations/system-tables/build_options.md

Example output from querying the system.build_options table, displaying the structure and sample data for build options.

```text
┌─name─────────────┬─value─┐
│ USE_BROTLI       │ 1     │
│ USE_BZIP2        │ 1     │
│ USE_CAPNP        │ 1     │
│ USE_CASSANDRA    │ 1     │
│ USE_DATASKETCHES │ 1     │
└──────────────────┴───────┘
```

--------------------------------

### Example ClickHouse SQL Query

Source: https://github.com/clickhouse/clickhouse/blob/master/tests/integration/README.md

A simple SQL query to select the constant value 1. This demonstrates a basic interaction with ClickHouse and shows the typical output format.

```sql
SELECT 1
```

--------------------------------

### Example Kafka Table Creation

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/engines/table-engines/integrations/kafka.md

Provides SQL examples for creating Kafka tables, demonstrating both concise and detailed settings configurations.

```sql
CREATE TABLE queue (
    timestamp UInt64,
    level String,
    message String
  ) ENGINE = Kafka('localhost:9092', 'topic', 'group1', 'JSONEachRow');

  SELECT * FROM queue LIMIT 5;

  CREATE TABLE queue2 (
    timestamp UInt64,
    level String,
    message String
  ) ENGINE = Kafka SETTINGS kafka_broker_list = 'localhost:9092',
                            kafka_topic_list = 'topic',
```

--------------------------------

### MergeTree Table Setup Example

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/sql-reference/table-functions/mergeTreeIndex.md

SQL statements to create and populate a sample MergeTree table used in the mergeTreeIndex function examples. This includes table definition and data insertion.

```sql
CREATE TABLE test_table
(
    `id` UInt64,
    `n` UInt64,
    `arr` Array(UInt64)
)
ENGINE = MergeTree
ORDER BY id
SETTINGS index_granularity = 3, min_bytes_for_wide_part = 0, min_rows_for_wide_part = 8;

INSERT INTO test_table SELECT number, number, range(number % 5) FROM numbers(5);

INSERT INTO test_table SELECT number, number, range(number % 5) FROM numbers(10, 10);
```

--------------------------------

### Data Insertion Example

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/operations/backup.md

Provides an example of creating a sample table and inserting random data into it, which can be used for backup testing.

```sql
CREATE TABLE data
(
    `key` Int,
    `value` String,
    `array` Array(String)
)
ENGINE = MergeTree
ORDER BY tuple()

```

```sql
INSERT INTO data SELECT *
FROM generateRandom('key Int, value String, array Array(String)')
LIMIT 1000
```

--------------------------------

### Installing ClickHouse via Universal Script (Shell)

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/changelogs/v22.5.1.2079-stable.md

This shell command provides a convenient way to install ClickHouse using its universal installation script. It fetches the script from the official ClickHouse website via `curl` and pipes it directly to the `sh` interpreter for execution, streamlining the setup process.

```Shell
curl https://clickhouse.com/ | sh
```

--------------------------------

### Managing ClickHouse Service with Packages

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/development/tests.md

Demonstrates how to manage the ClickHouse service after installing a package, including starting, stopping, and locating log files.

```bash
sudo clickhouse start
# or
sudo clickhouse stop
# Logs at /etc/clickhouse-server/clickhouse-server.log
```

--------------------------------

### Example Predefined Query Handler Rule (XML)

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/operations/server-configuration-parameters/_server_settings_outside_source.md

An example XML configuration for a ClickHouse HTTP handler rule that matches requests to '/predefined_query' with POST or GET methods and executes a predefined SQL query.

```xml
<http_handlers>
    <rule>
        <url>/predefined_query</url>
        <methods>POST,GET</methods>
        <handler>
            <type>predefined_query_handler</type>
            <query>SELECT * FROM system.settings</query>
        </handler>
    </rule>
</http_handlers>
```

--------------------------------

### Example HTTP Handler Rule (XML)

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/operations/server-configuration-parameters/_server_settings_outside_source.md

An example XML configuration for a ClickHouse HTTP handler rule that matches requests to the root URL ('/') with POST or GET methods and a 'no-cache' pragma header, using a dynamic query handler.

```xml
<http_handlers>
    <rule>
        <url>/</url>
        <methods>POST,GET</methods>
        <headers><pragma>no-cache</pragma></headers>
        <handler>
            <type>dynamic_query_handler</type>
            <query_param_name>query</query_param_name>
        </handler>
    </rule>
</http_handlers>
```

--------------------------------

### ClickHouse Server Unclean Restart Log Example

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/operations/_troubleshooting.md

This log snippet illustrates an error message when attempting to start a second instance of `clickhouse-server` in the same directory, indicating an existing status file.

```text
2019.01.11 15:25:11.151730 [ 1 ] {} <Information> : Starting ClickHouse 19.1.0 with revision 54413
2019.01.11 15:25:11.154578 [ 1 ] {} <Information> Application: starting up
2019.01.11 15:25:11.156361 [ 1 ] {} <Information> StatusFile: Status file ./status already exists - unclean restart. Contents:
PID: 8510
Started at: 2019-01-11 15:24:23
Revision: 54413

2019.01.11 15:25:11.156673 [ 1 ] {} <Error> Application: DB::Exception: Cannot lock file ./status. Another server instance in same directory is already running.
2019.01.11 15:25:11.156682 [ 1 ] {} <Information> Application: shutting down
2019.01.11 15:25:11.156686 [ 1 ] {} <Debug> Application: Uninitializing subsystem: Logging Subsystem
2019.01.11 15:25:11.156716 [ 2 ] {} <Information> BaseDaemon: Stop SignalListener thread
```

--------------------------------

### clickhouse-benchmark Usage Examples

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/operations/utilities/clickhouse-benchmark.md

Demonstrates different ways to run the clickhouse-benchmark tool, including single queries via command line arguments, standard input, and query files.

```bash
$ clickhouse-benchmark --query ["single query"] [keys]

$ echo "single query" | clickhouse-benchmark [keys]

$ clickhouse-benchmark [keys] <<< "single query"

$ clickhouse-benchmark [keys] < queries_file;
```

--------------------------------

### Example Input Table with Date Intervals (Text)

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/sql-reference/aggregate-functions/reference/intervalLengthSum.md

Provides an example input table named `date_interval` with `id`, `start`, and `end` columns. The `start` and `end` values are of `Date` type, demonstrating intervals for day-based calculations.

```Text
┌─id─┬──────start─┬────────end─┐
│ a  │ 2020-01-01 │ 2020-01-04 │
│ a  │ 2020-01-12 │ 2020-01-18 │
└────┴────────────┴────────────┘
```

--------------------------------

### JVM Startup Parameters and Environment Variables

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/operations/tips.md

This snippet shows environment variable definitions and comments related to JVM startup, including setting the Zookeeper configuration directory and noting a TODO for determining necessary JAR files.

```bash
NAME=zookeeper-{{ '{{' }} cluster['name'] {{ '}}' }}
ZOOCFGDIR=/etc/$NAME/conf

# TODO this is really ugly
# How to find out, which jars are needed?
```

--------------------------------

### Example of Clear and Simple Changelog Entry

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/changelog_entry_guidelines.md

Provides an example of a concise and informative changelog entry that explains the change and its benefits.

```text
> Makes page cache settings adjustable on a per-query level. This is needed for faster experimentation and for the possibility of fine-tuning for high-throughput and low-latency queries.
```

--------------------------------

### Example Input Table with DateTime Intervals (Text)

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/sql-reference/aggregate-functions/reference/intervalLengthSum.md

Presents an example input table named `dt_interval` with `id`, `start`, and `end` columns. The `start` and `end` values are of `DateTime` type, illustrating intervals for time-based calculations.

```Text
┌─id─┬───────────────start─┬─────────────────end─┐
│ a  │ 2020-01-01 01:12:30 │ 2020-01-01 02:10:10 │
│ a  │ 2020-01-01 02:05:30 │ 2020-01-01 02:50:31 │
│ a  │ 2020-01-01 03:11:22 │ 2020-01-01 03:23:31 │
└────┴─────────────────────┴─────────────────────┘
```

--------------------------------

### Example Output

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/operations/system-tables/database_engines.md

Shows an example of the output from querying the system.database_engines table.

```text
┌─name─────┐
│ Ordinary │
│ Atomic   │
│ Lazy     │
└──────────┘
```

--------------------------------

### Example Input Table with Float Intervals (Text)

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/sql-reference/aggregate-functions/reference/intervalLengthSum.md

Illustrates an example input table named `fl_interval` with `id`, `start`, and `end` columns. The `start` and `end` values are of `Float32` type, representing numeric intervals for demonstration purposes.

```Text
┌─id─┬─start─┬─end─┐
│ a  │   1.1 │ 2.9 │
│ a  │   2.5 │ 3.2 │
│ a  │     4 │   5 │
└────┴───────┴─────┘
```

--------------------------------

### ClickHouse Client Configuration File Examples

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/interfaces/cli.md

Provides examples of client configuration files in both XML and YAML formats, demonstrating how to set user credentials, security options, and SSL configurations.

```xml
<config>
    <user>username</user>
    <password>password</password>
    <secure>true</secure>
    <openSSL>
      <client>
        <caConfig>/etc/ssl/cert.pem</caConfig>
      </client>
    </openSSL>
</config>
```

```yaml
user: username
password: 'password'
secure: true
openSSL:
  client:
    caConfig: '/etc/ssl/cert.pem'
```

--------------------------------

### system.licenses Table Example Output

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/operations/system-tables/licenses.md

Example output format for queries against the system.licenses table, showing library details and license paths.

```text
┌─library_name───────┬─license_type─┬─license_path────────────────────────┐
│ aws-c-common       │ Apache       │ /contrib/aws-c-common/LICENSE       │
│ base64             │ BSD 2-clause │ /contrib/aklomp-base64/LICENSE      │
│ brotli             │ MIT          │ /contrib/brotli/LICENSE             │
│ [...]              │ [...]        │ [...]                               │
└────────────────────┴──────────────┴─────────────────────────────────────┘
```

--------------------------------

### Enum8 with negative starting number

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/sql-reference/data-types/enum.md

Example of creating an Enum8 column with a negative starting number for a named value.

```sql
CREATE TABLE t_enum
(
    x Enum8('hello' = -129, 'world')
)
ENGINE = TinyLog
```

--------------------------------

### Getting Time Type Name in ClickHouse

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/sql-reference/data-types/time.md

Example of using the toTime() function with now() to get the current time and its data type.

```sql
SELECT toTime(now()) AS column, toTypeName(column) AS x
```

```text
   ┌────column─┬─x────┐
1. │  18:55:15 │ Time │
   └───────────┴──────┘
```

--------------------------------

### Install ClickHouse Client

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/interfaces/cli.md

Commands to download and install the ClickHouse command-line client. Ensure you have curl installed for downloading.

```bash
curl https://clickhouse.com/ | sh
sudo ./clickhouse install
```

--------------------------------

### ClickHouse Query Example

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/changelogs/v25.7.1.3997-stable.md

An example SQL query to retrieve check start times, names, test names, and report URLs from the 'checks' table. It filters checks based on time, header referrer, test status, and a specific test option, ordering results by check start time.

```SQL
SELECT check_start_time, check_name, test_name, report_url
FROM checks
WHERE check_start_time >= now() - INTERVAL 1 YEAR
  AND (header_ref = 'master' AND startsWith(head_ref, 'ClickHouse/') )
  AND test_status != 'SKIPPED'
  AND (test_status LIKE 'F%' OR test_status LIKE 'E%') 
  AND check_status != 'success'
  AND position(test_name, 'test_options_propagation_enable') > 0
ORDER BY check_start_time
```

--------------------------------

### Start ClickHouse Server Interactively

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/operations/_troubleshooting.md

Run the ClickHouse server directly from the command line with a configuration file. This mode prints all event messages to the console, aiding in debugging.

```bash
$ sudo -u clickhouse /usr/bin/clickhouse-server --config-file /etc/clickhouse-server/config.xml
```

--------------------------------

### Start ClickHouse Server in Interactive Mode

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/operations/_troubleshooting.md

Starts the ClickHouse server interactively, printing all event messages to the console. This is useful for debugging startup issues.

```bash
sudo -u clickhouse /usr/bin/clickhouse-server --config-file /etc/clickhouse-server/config.xml
```

--------------------------------

### Example Output of system.resources

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/operations/system-tables/resources.md

This example shows the typical output format when querying the system.resources table, illustrating the structure of resource information including name, read/write disks, and the creation query.

```text
Row 1:
──────
name:         io_read
read_disks:   ['s3']
write_disks:  []
create_query: CREATE RESOURCE io_read (READ DISK s3)

Row 2:
──────
name:         io_write
read_disks:   []
write_disks:  ['s3']
create_query: CREATE RESOURCE io_write (WRITE DISK s3)
```

--------------------------------

### Explaining AST Graph for System Parts in ClickHouse SQL

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/changelogs/v22.3.1.1262-prestable.md

Illustrates the usage of `EXPLAIN AST GRAPH` to visualize the Abstract Syntax Tree (AST) of a query. This specific example shows how to get the AST graph for a simple `SELECT * FROM system.parts` query, which is useful for understanding query parsing and optimization.

```SQL
explain ast graph = 1 select * from system.parts;
```

--------------------------------

### ClickHouse Benchmark Comparison Mode Example

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/operations/utilities/clickhouse-benchmark.md

Demonstrates how to run the clickhouse-benchmark tool to compare two ClickHouse servers. It pipes a SQL query to the benchmark tool and specifies the hosts and ports for both servers, along with the number of iterations.

```bash
$ echo "SELECT * FROM system.numbers LIMIT 10000000 OFFSET 10000000" | clickhouse-benchmark --host=localhost --port=9001 --host=localhost --port=9000 -i 10
```

--------------------------------

### Get Replica Information Example

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/sql-reference/statements/attach.md

Example query to retrieve replica name and ZooKeeper path for a given table, which is necessary for managing replicated tables.

```SQL
SELECT replica_name, zookeeper_path FROM system.replicas WHERE table='test';
```

--------------------------------

### User Configuration Example: Alice's Settings

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/operations/configuration-files.md

Provides an example of a user-specific configuration file (`alice.xml`) defining user settings, profiles, networks, and quotas.

```xml
<clickhouse>
    <users>
      <alice>
          <profile>analytics</profile>
            <networks>
                  <ip>::/0</ip>
            </networks>
          <password_sha256_hex>...</password_sha256_hex>
          <quota>analytics</quota>
      </alice>
    </users>
</clickhouse>
```

--------------------------------

### SQLite Table Schema Example

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/engines/table-engines/integrations/sqlite.md

Provides an example of the output from `SHOW CREATE TABLE` for a ClickHouse table backed by SQLite, illustrating the schema and engine configuration.

```text
CREATE TABLE SQLite.table2
(
    `col1` Nullable(Int32),
    `col2` Nullable(String)
)
ENGINE = SQLite('sqlite.db','table2');
```

--------------------------------

### ClickHouse CREATE TABLE Example

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/changelogs/v25.5.1.2782-stable.md

Provides an example of creating a MergeTree table with specific partitioning and primary key configurations.

```sql
CREATE TABLE t0 (
    key Int32,
    value Int32
)
ENGINE=MergeTree()
PRIMARY KEY key
PARTITION BY key % 2;
```

--------------------------------

### Setup Example Table and Data

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/sql-reference/window-functions/last_value.md

Creates a temporary 'salaries' table with player, team, salary, and position data, and inserts sample records. This setup is used to demonstrate the last_value window function.

```sql
DROP TABLE IF EXISTS salaries;
CREATE TABLE salaries
(
    `team` String,
    `player` String,
    `salary` UInt32,
    `position` String
)
Engine = Memory;

INSERT INTO salaries FORMAT VALUES
    ('Port Elizabeth Barbarians', 'Gary Chen', 196000, 'F'),
    ('New Coreystad Archdukes', 'Charles Juarez', 190000, 'F'),
    ('Port Elizabeth Barbarians', 'Michael Stanley', 100000, 'D'),
    ('New Coreystad Archdukes', 'Scott Harrison', 180000, 'D'),
    ('Port Elizabeth Barbarians', 'Robert George', 195000, 'M'),
    ('South Hampton Seagulls', 'Douglas Benson', 150000, 'M'),
    ('South Hampton Seagulls', 'James Henderson', 140000, 'M');
```

--------------------------------

### Initialize Database with SQL and Shell Scripts

Source: https://github.com/clickhouse/clickhouse/blob/master/docker/server/README.md

Demonstrates how to perform custom initialization by placing SQL or shell scripts in the `/docker-entrypoint-initdb.d/` directory. The example shows creating a database and table using a bash script.

```bash
#!/bin/bash
set -e

clickhouse client -n <<-EOSQL
    CREATE DATABASE docker;
    CREATE TABLE docker.docker (x Int32) ENGINE = Log;
EOSQL
```

--------------------------------

### Example Response from system.processes

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/operations/system-tables/processes.md

This snippet shows an example of the data returned when querying the system.processes table. It includes details about the query, user, client information, and performance metrics.

```json
{
    "is_initial_query": 1,
    "user": "default",
    "query_id": "35a360fa-3743-441d-8e1f-228c938268da",
    "address": "::ffff:172.23.0.1",
    "port": 47588,
    "initial_user": "default",
    "initial_query_id": "35a360fa-3743-441d-8e1f-228c938268da",
    "initial_address": "::ffff:172.23.0.1",
    "initial_port": 47588,
    "interface": 1,
    "os_user": "bharatnc",
    "client_hostname": "tower",
    "client_name": "ClickHouse",
    "client_revision": 54437,
    "client_version_major": 20,
    "client_version_minor": 7,
    "client_version_patch": 2,
    "http_method": 0,
    "http_user_agent": null,
    "quota_key": null,
    "elapsed": 0.000582537,
    "is_cancelled": 0,
    "is_all_data_sent": 0,
    "read_rows": 0,
    "read_bytes": 0,
    "total_rows_approx": 0,
    "written_rows": 0,
    "written_bytes": 0,
    "memory_usage": 0,
    "peak_memory_usage": 0,
    "query": "SELECT * from system.processes LIMIT 10 FORMAT Vertical;",
    "thread_ids": [67],
    "ProfileEvents": {"Query":1,"SelectQuery":1,"ReadCompressedBytes":36,"CompressedReadBufferBlocks":1,"CompressedReadBufferBytes":10,"IOBufferAllocs":1,"IOBufferAllocBytes":89,"ContextLock":15,"RWLockAcquiredReadLocks":1},
    "Settings": {"background_pool_size":"32","load_balancing":"random","allow_suspicious_low_cardinality_types":"1","distributed_aggregation_memory_efficient":"1","skip_unavailable_shards":"1","log_queries":"1","max_bytes_before_external_group_by":"20000000000","max_bytes_before_external_sort":"20000000000","allow_introspection_functions":"1"}
}
```

--------------------------------

### Example ZooKeeper Configuration

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/operations/server-configuration-parameters/_server_settings_outside_source.md

An example XML configuration block demonstrating how to set up ZooKeeper connection parameters and load balancing in ClickHouse.

```xml
<zookeeper>
    <node>
        <host>example1</host>
        <port>2181</port>
    </node>
    <node>
        <host>example2</host>
        <port>2181</port>
    </node>
    <session_timeout_ms>30000</session_timeout_ms>
    <operation_timeout_ms>10000</operation_timeout_ms>
    <!-- Optional. Chroot suffix. Should exist. -->
    <root>/path/to/zookeeper/node</root>
    <!-- Optional. Zookeeper digest ACL string. -->
    <identity>user:password</identity>
    <!--<zookeeper_load_balancing>random / in_order / nearest_hostname / hostname_levenshtein_distance / first_or_random / round_robin</zookeeper_load_balancing>-->
    <zookeeper_load_balancing>random</zookeeper_load_balancing>
</zookeeper>
```

--------------------------------

### SQL: Get Time64 Type Information

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/sql-reference/data-types/time64.md

Example of using the `toTime64` function with `now()` to get the current time and `toTypeName` to display the data type and its precision. This confirms the data type and precision stored.

```sql
SELECT toTime64(now(), 3) AS column, toTypeName(column) AS x;
```

--------------------------------

### ClickHouse SOURCE Function Example

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/sql-reference/dictionaries/index.md

Shows an example of using the SOURCE function with ClickHouse parameters, including update settings.

```sql
SOURCE(CLICKHOUSE(... update_field 'added_time' update_lag 15))
```

--------------------------------

### quantileTDigestWeighted Example Result

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/sql-reference/aggregate-functions/reference/quantiletdigestweighted.md

Shows the expected output from the quantileTDigestWeighted example query.

```text
┌─quantileTDigestWeighted(number, 1)─┐
│                                4.5 │
└────────────────────────────────────┘
```

--------------------------------

### Example Table Creation

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/sql-reference/statements/select/index.md

SQL statement to create a sample table used in the dynamic column selection examples.

```sql
CREATE TABLE default.col_names (aa Int8, ab Int8, bc Int8) ENGINE = TinyLog
```

--------------------------------

### Generate Setup Dictionary Table C++ Code

Source: https://github.com/clickhouse/clickhouse/blob/master/contrib/qpl-cmake/CMakeLists.txt

Generates C++ code for a setup dictionary table, including headers for deflate utilities and dispatcher. It defines a `setup_dictionary_table_t` and initializes it with a pointer to the setup dictionary function.

```cpp
file(WRITE ${directory}/${PLATFORM_PREFIX}setup_dictionary.cpp "#include \"deflate_slow_utils.h\"\n")
        file(APPEND ${directory}/${PLATFORM_PREFIX}setup_dictionary.cpp "#include \"dispatcher/dispatcher.hpp\"\n")
        file(APPEND ${directory}/${PLATFORM_PREFIX}setup_dictionary.cpp "namespace qpl::core_sw::dispatcher\n{\n")
        file(APPEND ${directory}/${PLATFORM_PREFIX}setup_dictionary.cpp "setup_dictionary_table_t ${PLATFORM_PREFIX}setup_dictionary_table = {\n")

        file(APPEND ${directory}/${PLATFORM_PREFIX}setup_dictionary.cpp "\t reinterpret_cast<void *>(&${PLATFORM_PREFIX}setup_dictionary)};\n")

        file(APPEND ${directory}/${PLATFORM_PREFIX}setup_dictionary.cpp "}\n")
```

--------------------------------

### S3 Table Engine Example

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/engines/table-engines/integrations/s3.md

Demonstrates creating a table using the S3 engine, inserting data, and querying it. It shows how to specify the S3 path, file format, and compression.

```sql
CREATE TABLE s3_engine_table (name String, value UInt32)
    ENGINE=S3('https://clickhouse-public-datasets.s3.amazonaws.com/my-test-bucket-768/test-data.csv.gz', 'CSV', 'gzip')
    SETTINGS input_format_with_names_use_header = 0;

INSERT INTO s3_engine_table VALUES ('one', 1), ('two', 2), ('three', 3);

SELECT * FROM s3_engine_table LIMIT 2;
```

```text
┌─name─┬─value─┐
│ one  │     1 │
│ two  │     2 │
└──────┴───────┘
```

--------------------------------

### ClickHouse numbers Table Function Example: Date Generation

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/sql-reference/table-functions/numbers.md

An example of using the 'numbers' table function to generate a sequence of dates. It demonstrates how to combine the generated numbers with a starting date to create a range of dates.

```SQL
-- Generate a sequence of dates from 2010-01-01 to 2010-12-31
SELECT toDate('2010-01-01') + number AS d FROM numbers(365);
```

--------------------------------

### Salt Initialization Script for Zookeeper

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/operations/tips.md

This Salt stack initialization script defines the service's behavior, including its start and stop conditions, respawn policy, resource limits, pre-start actions (environment sourcing, log directory creation, ownership), and the main execution command. It dynamically includes environment variables and Java options.

```text
description "zookeeper-{{ '{{' }} cluster['name'] {{ '}}' }} centralized coordination service"

start on runlevel [2345]
stop on runlevel [!2345]

respawn

limit nofile 8192 8192

pre-start script
    [ -r "/etc/zookeeper-{{ '{{' }} cluster['name'] {{ '}}' }}/conf/environment" ] || exit 0
    . /etc/zookeeper-{{ '{{' }} cluster['name'] {{ '}}' }}/conf/environment
    [ -d $ZOO_LOG_DIR ] || mkdir -p $ZOO_LOG_DIR
    chown $USER:$GROUP $ZOO_LOG_DIR
end script

script
    . /etc/zookeeper-{{ '{{' }} cluster['name'] {{ '}}' }}/conf/environment
    [ -r /etc/default/zookeeper ] && . /etc/default/zookeeper
    if [ -z "$JMXDISABLE" ]; then
        JAVA_OPTS="$JAVA_OPTS -Dcom.sun.management.jmxremote -Dcom.sun.management.jmxremote.local.only=$JMXLOCALONLY"
    fi
    exec start-stop-daemon --start -c $USER --exec $JAVA --name zookeeper-{{ '{{' }} cluster['name'] {{ '}}' }} \
        -- -cp $CLASSPATH $JAVA_OPTS -Dzookeeper.log.dir=${ZOO_LOG_DIR} \
        -Dzookeeper.root.logger=${ZOO_LOG4J_PROP} $ZOOMAIN $ZOOCFG
end script
```

--------------------------------

### MySQL Example: Table Creation and Insertion

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/engines/database-engines/mysql.md

Shows a sample MySQL table creation and data insertion process, providing context for ClickHouse data exchange examples.

```text
mysql> USE test;
Database changed

mysql> CREATE TABLE `mysql_table` (
    ->   `int_id` INT NOT NULL AUTO_INCREMENT,
    ->   `float` FLOAT NOT NULL,
    ->   PRIMARY KEY (`int_id`));
Query OK, 0 rows affected (0,09 sec)

mysql> insert into mysql_table (`int_id`, `float`) VALUES (1,2);
Query OK, 1 row affected (0,00 sec)

mysql> select * from mysql_table;
+------+-----+
| int_id | value |
+------+-----+
|      1 |     2 |
+------+-----+
1 row in set (0,00 sec)
```

--------------------------------

### Getting First 5 String Numbers with groupArraySorted (SQL)

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/sql-reference/aggregate-functions/reference/grouparraysorted.md

This example illustrates using `groupArraySorted` with string values. It converts numbers to strings using `toString(number)` and then applies `groupArraySorted(5)` to get the first 5 string representations in ascending order.

```SQL
SELECT groupArraySorted(5)(str) FROM (SELECT toString(number) as str FROM numbers(5));
```

--------------------------------

### Generator Setup Configuration

Source: https://github.com/clickhouse/clickhouse/blob/master/programs/keeper-bench/README.md

Configures the setup phase of the benchmark generator, defining nodes, their data, and repetition counts.

```yaml
node: StringGetter

node:
    name: StringGetter
    data: StringGetter
    repeat: integer
    node: Node
```

```yaml
generator:
    setup:
        node: "node1"
            node:
                name:
                    random_string:
                        size: 20
                data: "somedata"
                repeat: 4
        node:
            name:
                random_string:
                    size: 10
            repeat: 2
```

--------------------------------

### Example: Showing Databases

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/engines/database-engines/postgresql.md

Illustrates how to list all available databases in ClickHouse, including the newly created PostgreSQL-connected database.

```text
SHOW DATABASES;

┌─name──────────┐
│ default       │
│ test_database │
│ system        │
└───────────────┘
```

--------------------------------

### Iceberg Table Engine Example

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/engines/table-engines/integrations/iceberg.md

Provides an example of creating an Iceberg table using the IcebergS3 engine with direct URL and credentials, and another example using named collections for configuration.

```sql
CREATE TABLE iceberg_table ENGINE=IcebergS3('http://test.s3.amazonaws.com/clickhouse-bucket/test_table', 'test', 'test')
```

```xml
<clickhouse>
    <named_collections>
        <iceberg_conf>
            <url>http://test.s3.amazonaws.com/clickhouse-bucket/</url>
            <access_key_id>test</access_key_id>
            <secret_access_key>test</secret_access_key>
        </iceberg_conf>
    </named_collections>
</clickhouse>
```

```sql
CREATE TABLE iceberg_table ENGINE=IcebergS3(iceberg_conf, filename = 'test_table')
```

--------------------------------

### Setup and Generate Changelog (macOS)

Source: https://github.com/clickhouse/clickhouse/blob/master/utils/changelog/README.md

Instructions for setting up the Python environment and generating a changelog on macOS. This involves installing Python via Homebrew, creating a virtual environment, installing dependencies from requirements.txt, and running the changelog script with specific commit hashes.

```bash
brew install python
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
./changelog.py --gh-user-or-token ghp_... --from a79faf5da8027c201a94cdc5c9a6a1d7852d69b5 95ccb0e1a86fd26a50b11a9479586e973dba66ce
```

--------------------------------

### EXPLAIN PIPELINE Example

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/operations/system-tables/processors_profile_log.md

Demonstrates how to use EXPLAIN PIPELINE to visualize query execution stages and then query the system.processors_profile_log table to analyze the performance of individual processors based on the query ID.

```SQL
EXPLAIN PIPELINE
SELECT sleep(1)
```

```SQL
SELECT sleep(1)
SETTINGS log_processors_profiles = 1
```

--------------------------------

### Getting Unidirectional Edges from Hexagon (Example) - ClickHouse SQL

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/sql-reference/functions/geo/h3.md

This example demonstrates how to use the `h3GetUnidirectionalEdgesFromHexagon` function with a specific H3 index. The query selects the unidirectional edges, which are returned as an array of H3 indexes (UInt64), providing a practical application of the function.

```SQL
 SELECT h3GetUnidirectionalEdgesFromHexagon(1248204388774707199) as edges;
```

--------------------------------

### ZooKeeper Configuration Example

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/operations/tips.md

Provides a sample zoo.cfg configuration for ZooKeeper used in a large production environment. It includes essential settings for tick time, synchronization limits, client connections, session timeouts, data directories, and automatic purging of old snapshots and logs.

```bash
# http://hadoop.apache.org/zookeeper/docs/current/zookeeperAdmin.html

# The number of milliseconds of each tick
tickTime=2000
# The number of ticks that the initial
# synchronization phase can take
# This value is not quite motivated
initLimit=300
# The number of ticks that can pass between
# sending a request and getting an acknowledgement
syncLimit=10

maxClientCnxns=2000

# It is the maximum value that client may request and the server will accept.
# It is Ok to have high maxSessionTimeout on server to allow clients to work with high session timeout if they want.
# But we request session timeout of 30 seconds by default (you can change it with session_timeout_ms in ClickHouse config).
maxSessionTimeout=60000000
# the directory where the snapshot is stored.
dataDir=/opt/zookeeper/{{ '{{' }} cluster['name'] {{ '}}' }}/data
# Place the dataLogDir to a separate physical disc for better performance
dataLogDir=/opt/zookeeper/{{ '{{' }} cluster['name'] {{ '}}' }}/logs

autopurge.snapRetainCount=10
autopurge.purgeInterval=1


# To avoid seeks ZooKeeper allocates space in the transaction log file in
```

--------------------------------

### Build Examples for AMD Debug on CI

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/changelogs/v25.7.1.3997-stable.md

Configures the Continuous Integration pipeline to build examples for AMD processors in debug mode.

```bash
# Example CI configuration for building examples
# BUILD_TARGET=x86_64-unknown-linux-gnu

# Configuration for AMD debug builds
# BUILD_TARGET=x86_64-pc-windows-gnu
# BUILD_MODE=Debug
```

--------------------------------

### Comparing Substrings with stringCompare Function (SQL)

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/changelogs/v25.2.1.3085-stable.md

This snippet demonstrates the usage of the new `stringCompare` function in ClickHouse. It allows for lexicographical comparison of specified parts of two strings. The example compares 6 bytes from 'Saxony' starting at offset 0, with 6 bytes from 'Anglo-Saxon' starting at offset 5.

```SQL
SELECT stringCompare('Saxony', 'Anglo-Saxon', 0, 6, 5) AS result
```

--------------------------------

### Example Output from system.workloads Query (Text)

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/operations/system-tables/workloads.md

This text snippet shows an example of the output when querying the `system.workloads` table. It displays three sample workload entries: 'production', 'development', and 'all', detailing their names, parent workloads, and the `CREATE WORKLOAD` statements used for their definition.

```Text
Row 1:
──────
name:         production
parent:       all
create_query: CREATE WORKLOAD production IN `all` SETTINGS weight = 9

Row 2:
──────
name:         development
parent:       all
create_query: CREATE WORKLOAD development IN `all`

Row 3:
──────
name:         all
parent:
create_query: CREATE WORKLOAD `all`
```

--------------------------------

### Creating sum_map Table for sumMapFilteredWithOverflow Example (SQL)

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/sql-reference/aggregate-functions/parametric-functions.md

This SQL snippet creates a `sum_map` table similar to the previous example, but with `status` and `requests` in `statusMap` defined as `UInt8`. This setup is specifically designed to illustrate the overflow behavior of `sumMapFilteredWithOverflow` when sums exceed the `UInt8` maximum value.

```SQL
CREATE TABLE sum_map
(
    `date` Date,
    `timeslot` DateTime,
    `statusMap` Nested(status UInt8, requests UInt8)
)
ENGINE = Log

INSERT INTO sum_map VALUES
    ('2000-01-01', '2000-01-01 00:00:00', [1, 2, 3], [10, 10, 10]),
    ('2000-01-01', '2000-01-01 00:00:00', [3, 4, 5], [10, 10, 10]),
    ('2000-01-01', '2000-01-01 00:01:00', [4, 5, 6], [10, 10, 10]),
    ('2000-01-01', '2000-01-01 00:01:00', [6, 7, 8], [10, 10, 10]);
```

--------------------------------

### Initializing Database with SQL and Shell Scripts

Source: https://github.com/clickhouse/clickhouse/blob/master/docker/server/README.md

This example shows how to extend the ClickHouse Docker image by adding initialization scripts. Scripts in `/docker-entrypoint-initdb.d/` (e.g., `.sql`, `.sh`) are executed during the container's first run to set up databases and users.

```bash
#!/bin/bash
set -e

clickhouse client -n <<-EOSQL
    CREATE DATABASE docker;
    CREATE TABLE docker.docker (x Int32) ENGINE = Log;
EOSQL
```

--------------------------------

### Example Database Creation

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/operations/system-tables/databases.md

This snippet shows a basic SQL command to create a new database named 'test'. This is a prerequisite for having databases to query in the system.databases table.

```sql
CREATE DATABASE test;
```

--------------------------------

### Getting Unidirectional Edge Boundary (Example) - ClickHouse SQL

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/sql-reference/functions/geo/h3.md

This example shows the practical usage of the `h3GetUnidirectionalEdgeBoundary` function with a given H3 index. The query retrieves the geographic coordinates that define the boundary of the specified unidirectional edge, returned as an array of longitude and latitude pairs.

```SQL
 SELECT h3GetUnidirectionalEdgeBoundary(1248204388774707199) as boundary;
```

--------------------------------

### ClickHouse Server Listening Message

Source: https://github.com/clickhouse/clickhouse/blob/master/docs/en/interfaces/postgresql.md

Example log message indicating that the ClickHouse server has started listening for PostgreSQL compatibility protocol connections.

```response
{} <Information> Application: Listening for PostgreSQL compatibility protocol: 127.0.0.1:9005
```