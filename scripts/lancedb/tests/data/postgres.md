### PostgreSQL Installation Short Version Commands

Source: https://www.postgresql.org/docs/18/install-meson

Complete sequence of commands for a quick PostgreSQL 18 installation using Meson, including setup, build, installation, database initialization, and testing.

```shell
meson setup build --prefix=/usr/local/pgsql
cd build
ninja
su
ninja install
adduser postgres
mkdir -p /usr/local/pgsql/data
chown postgres /usr/local/pgsql/data
su - postgres
/usr/local/pgsql/bin/initdb -D /usr/local/pgsql/data
/usr/local/pgsql/bin/pg_ctl -D /usr/local/pgsql/data -l logfile start
/usr/local/pgsql/bin/createdb test
/usr/local/pgsql/bin/psql test
```

--------------------------------

### PostgreSQL 18: Short Installation Procedure (Shell)

Source: https://www.postgresql.org/docs/18/install-make

This snippet provides a condensed, step-by-step shell command sequence for a basic PostgreSQL 18 installation from source. It covers configuration, building, user setup, data directory initialization, service startup, and basic database operations.

```shell
./configure
make
su
make install
adduser postgres
mkdir -p /usr/local/pgsql/data
chown postgres /usr/local/pgsql/data
su - postgres
/usr/local/pgsql/bin/initdb -D /usr/local/pgsql/data
/usr/local/pgsql/bin/pg_ctl -D /usr/local/pgsql/data -l logfile start
/usr/local/pgsql/bin/createdb test
/usr/local/pgsql/bin/psql test
```

--------------------------------

### Meson Setup Configuration Commands

Source: https://www.postgresql.org/docs/18/install-meson

Meson setup commands for configuring PostgreSQL build with different options including prefix, debug builds, and SSL support.

```shell
meson setup build
# configure with a different installation prefix
meson setup build --prefix=/home/user/pg-install
# configure to generate a debug build
meson setup build --buildtype=debug
# configure to build with OpenSSL support
meson setup build -Dssl=openssl
```

--------------------------------

### libpq Example Program 1: Connect and Query PostgreSQL Database

Source: https://www.postgresql.org/docs/18/libpq-example

This C program demonstrates how to connect to a PostgreSQL database using libpq, execute SQL commands (including setting search path, starting a transaction, declaring a cursor, fetching data, and ending the transaction), and process the results. It requires the libpq library to be installed and accessible. The program takes an optional connection string as a command-line argument; otherwise, it defaults to 'dbname = postgres'.

```c
/*
 * src/test/examples/testlibpq.c
 *
 *
 * testlibpq.c
 *
 *      Test the C version of libpq, the PostgreSQL frontend library.
 */
#include <stdio.h>
#include <stdlib.h>
#include "libpq-fe.h"

static void
exit_nicely(PGconn *conn)
{
    PQfinish(conn);
    exit(1);
}

int
main(int argc, char **argv)
{
    const char *conninfo;
    PGconn     *conn;
    PGresult   *res;
    int         nFields;
    int         i, 
                j;

    /*
     * If the user supplies a parameter on the command line, use it as the
     * conninfo string; otherwise default to setting dbname=postgres and using
     * environment variables or defaults for all other connection parameters.
     */
    if (argc > 1)
        conninfo = argv[1];
    else
        conninfo = "dbname = postgres";

    /* Make a connection to the database */
    conn = PQconnectdb(conninfo);

    /* Check to see that the backend connection was successfully made */
    if (PQstatus(conn) != CONNECTION_OK)
    {
        fprintf(stderr, "%s", PQerrorMessage(conn));
        exit_nicely(conn);
    }

    /* Set always-secure search path, so malicious users can't take control. */
    res = PQexec(conn,
                 "SELECT pg_catalog.set_config('search_path', '', false)");
    if (PQresultStatus(res) != PGRES_TUPLES_OK)
    {
        fprintf(stderr, "SET failed: %s", PQerrorMessage(conn));
        PQclear(res);
        exit_nicely(conn);
    }

    /*
     * Should PQclear PGresult whenever it is no longer needed to avoid memory
     * leaks
     */
    PQclear(res);

    /*
     * Our test case here involves using a cursor, for which we must be inside
     * a transaction block.  We could do the whole thing with a single
     * PQexec() of "select * from pg_database", but that's too trivial to make
     * a good example.
     */

    /* Start a transaction block */
    res = PQexec(conn, "BEGIN");
    if (PQresultStatus(res) != PGRES_COMMAND_OK)
    {
        fprintf(stderr, "BEGIN command failed: %s", PQerrorMessage(conn));
        PQclear(res);
        exit_nicely(conn);
    }
    PQclear(res);

    /*
     * Fetch rows from pg_database, the system catalog of databases
     */
    res = PQexec(conn, "DECLARE myportal CURSOR FOR select * from pg_database");
    if (PQresultStatus(res) != PGRES_COMMAND_OK)
    {
        fprintf(stderr, "DECLARE CURSOR failed: %s", PQerrorMessage(conn));
        PQclear(res);
        exit_nicely(conn);
    }
    PQclear(res);

    res = PQexec(conn, "FETCH ALL in myportal");
    if (PQresultStatus(res) != PGRES_TUPLES_OK)
    {
        fprintf(stderr, "FETCH ALL failed: %s", PQerrorMessage(conn));
        PQclear(res);
        exit_nicely(conn);
    }

    /* first, print out the attribute names */
    nFields = PQnfields(res);
    for (i = 0; i < nFields; i++)
        printf("% -15s", PQfname(res, i));
    printf("\n\n");

    /* next, print out the rows */
    for (i = 0; i < PQntuples(res); i++)
    {
        for (j = 0; j < nFields; j++)
            printf("% -15s", PQgetvalue(res, i, j));
        printf("\n");
    }

    PQclear(res);

    /* close the portal ... we don't bother to check for errors ... */
    res = PQexec(conn, "CLOSE myportal");
    PQclear(res);

    /* end the transaction */
    res = PQexec(conn, "END");
    PQclear(res);

    /* close the connection to the database and cleanup */
    PQfinish(conn);

    return 0;
}

```

--------------------------------

### PostgreSQL: Create Publication for Replication

Source: https://www.postgresql.org/docs/18/logical-replication-quick-setup

On the publisher database, create a publication to specify which tables should be replicated. This example creates a publication named 'mypub' for the 'users' and 'departments' tables.

```sql
CREATE PUBLICATION mypub FOR TABLE users, departments;

```

--------------------------------

### PostgreSQL: Create Subscription for Replication

Source: https://www.postgresql.org/docs/18/logical-replication-quick-setup

On the subscriber database, create a subscription to connect to the publisher and receive replicated data. This example creates a subscription named 'mysub', connecting to a database 'foo' on host 'bar' as user 'repuser', and subscribing to the 'mypub' publication.

```sql
CREATE SUBSCRIPTION mysub CONNECTION 'dbname=foo host=bar user=repuser' PUBLICATION mypub;

```

--------------------------------

### Install PostgreSQL World (Binaries and Docs)

Source: https://www.postgresql.org/docs/18/install-make

Installs both the PostgreSQL binaries and documentation. This is a convenient command if both components are to be installed together.

```makefile
make install-world
```

--------------------------------

### PostgreSQL 18: Basic Build (Shell)

Source: https://www.postgresql.org/docs/18/install-make

These shell commands start the build process for PostgreSQL 18 after configuration. 'make' or 'make all' will compile the server, utilities, and client applications.

```shell
make
make all
```

--------------------------------

### Install PostgreSQL Documentation

Source: https://www.postgresql.org/docs/18/install-make

Installs the HTML and man page documentation for PostgreSQL. This command is typically used after the main installation process.

```makefile
make install-docs
```

--------------------------------

### Start PostgreSQL Server

Source: https://www.postgresql.org/docs/18/logical-replication-upgrade

Starts a PostgreSQL server instance using pg_ctl. Requires the data directory path and optional log file.

```Shell
pg_ctl -D /opt/PostgreSQL/data1_upgraded start -l logfile
```

```Shell
pg_ctl -D /opt/PostgreSQL/data2_upgraded start -l logfile
```

--------------------------------

### Setup and Demonstrate Functional Dependencies in PostgreSQL SQL

Source: https://www.postgresql.org/docs/18/multivariate-statistics-examples

This example sets up a table with correlated columns, shows estimation issues without multivariate stats, and demonstrates improvement with functional dependency statistics. It uses PostgreSQL's ANALYZE for statistics collection and EXPLAIN for plan analysis. Inputs are simple SQL commands; outputs are QUERY PLAN details. Requires PostgreSQL database and assumes basic SQL knowledge.

```sql
CREATE TABLE t (a INT, b INT);
INSERT INTO t SELECT i % 100, i % 100 FROM generate_series(1, 10000) s(i);
ANALYZE t;
```

```sql
SELECT relpages, reltuples FROM pg_class WHERE relname = 't';
```

```sql
EXPLAIN (ANALYZE, TIMING OFF, BUFFERS OFF) SELECT * FROM t WHERE a = 1;
```

```sql
EXPLAIN (ANALYZE, TIMING OFF, BUFFERS OFF) SELECT * FROM t WHERE a = 1 AND b = 1;
```

```sql
CREATE STATISTICS stts (dependencies) ON a, b FROM t;
ANALYZE t;
EXPLAIN (ANALYZE, TIMING OFF, BUFFERS OFF) SELECT * FROM t WHERE a = 1 AND b = 1;
```

--------------------------------

### libpq Example Program 2: Asynchronous Notification Interface

Source: https://www.postgresql.org/docs/18/libpq-example

This C program tests libpq's asynchronous notification interface. It connects to a PostgreSQL database and listens for NOTIFY messages. The program exits after receiving a specified number of notifications. It can be triggered by sending NOTIFY commands from another client (like psql) or by using a provided SQL setup with triggers. This example requires the libpq library.

```c
/*
 * src/test/examples/testlibpq2.c
 *
 *
 * testlibpq2.c
 *      Test of the asynchronous notification interface
 *
 * Start this program, then from psql in another window do
 *   NOTIFY TBL2;
 * Repeat four times to get this program to exit.
 *
 * Or, if you want to get fancy, try this:
 * populate a database with the following commands
 * (provided in src/test/examples/testlibpq2.sql):
 *
 *   CREATE SCHEMA TESTLIBPQ2;
 *   SET search_path = TESTLIBPQ2;
 *   CREATE TABLE TBL1 (i int4);
 *   CREATE TABLE TBL2 (i int4);
 *   CREATE RULE r1 AS ON INSERT TO TBL1 DO
 *     (INSERT INTO TBL2 VALUES (new.i); NOTIFY TBL2);
 *
 * Start this program, then from psql do this four times:
 *
 *   INSERT INTO TESTLIBPQ2.TBL1 VALUES (10);
 */

#ifdef WIN32
#include <windows.h>
#endif
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <sys/select.h>
#include <sys/time.h>
#include <sys/types.h>

#include "libpq-fe.h"

static void
exit_nicely(PGconn *conn)
{
    PQfinish(conn);
    exit(1);
}

int
main(int argc, char **argv)
{
    const char *conninfo;
    PGconn     *conn;
    PGresult   *res;
    PGnotify   *notify;
    int         nnotifies;

    /*
     * If the user supplies a parameter on the command line, use it as the
     * conninfo string; otherwise default to setting dbname=postgres and using

```

--------------------------------

### Complete C Program Example Using GET DESCRIPTOR

Source: https://www.postgresql.org/docs/18/ecpg-sql-get-descriptor

Full C program demonstrating complete workflow: connecting to database, allocating descriptor, executing SELECT query, fetching results, retrieving descriptor information, and cleanup. Shows practical usage of GET DESCRIPTOR with header and column data retrieval.

```C
int
main(void)
{
EXEC SQL BEGIN DECLARE SECTION;
    int  d_count;
    char d_data[1024];
    int  d_returned_octet_length;
EXEC SQL END DECLARE SECTION;

    EXEC SQL CONNECT TO testdb AS con1 USER testuser;
    EXEC SQL SELECT pg_catalog.set_config('search_path', '', false); EXEC SQL COMMIT;
    EXEC SQL ALLOCATE DESCRIPTOR d;

    /* Declare, open a cursor, and assign a descriptor to the cursor  */
    EXEC SQL DECLARE cur CURSOR FOR SELECT current_database();
    EXEC SQL OPEN cur;
    EXEC SQL FETCH NEXT FROM cur INTO SQL DESCRIPTOR d;

    /* Get a number of total columns */
    EXEC SQL GET DESCRIPTOR d :d_count = COUNT;
    printf("d_count                 = %d\n", d_count);

    /* Get length of a returned column */
    EXEC SQL GET DESCRIPTOR d VALUE 1 :d_returned_octet_length = RETURNED_OCTET_LENGTH;
    printf("d_returned_octet_length = %d\n", d_returned_octet_length);

    /* Fetch the returned column as a string */
    EXEC SQL GET DESCRIPTOR d VALUE 1 :d_data = DATA;
    printf("d_data                  = %s\n", d_data);

    /* Closing */
    EXEC SQL CLOSE cur;
    EXEC SQL COMMIT;

    EXEC SQL DEALLOCATE DESCRIPTOR d;
    EXEC SQL DISCONNECT ALL;

    return 0;
}
```

--------------------------------

### Install PostgreSQL Binaries without Docs

Source: https://www.postgresql.org/docs/18/install-make

Installs PostgreSQL binaries but excludes documentation. Use this if documentation is not required or will be installed separately.

```makefile
make install-world-bin
```

--------------------------------

### GET DESCRIPTOR Syntax and Basic Usage Examples

Source: https://www.postgresql.org/docs/18/ecpg-sql-get-descriptor

Demonstrates the two syntax forms of GET DESCRIPTOR command - header item retrieval and column-specific data retrieval. Shows basic examples including COUNT, RETURNED_OCTET_LENGTH, and DATA item retrieval.

```SQL
GET DESCRIPTOR _descriptor_name_ _:cvariable_ = _descriptor_header_item_ [, ... ]
GET DESCRIPTOR _descriptor_name_ VALUE _column_number_ _:cvariable_ = _descriptor_item_ [, ... ]
```

```SQL
EXEC SQL GET DESCRIPTOR d :d_count = COUNT;
```

```SQL
EXEC SQL GET DESCRIPTOR d VALUE 1 :d_returned_octet_length = RETURNED_OCTET_LENGTH;
```

```SQL
EXEC SQL GET DESCRIPTOR d VALUE 2 :d_data = DATA;
```

--------------------------------

### Start PostgreSQL server instance

Source: https://www.postgresql.org/docs/18/logical-replication-upgrade

Starts a PostgreSQL server instance using pg_ctl with logging. Brings the upgraded server online after migration completion. Requires the upgraded data directory path and optional log file for output redirection.

```shell
pg_ctl -D /opt/PostgreSQL/data1_upgraded start -l logfile
```

```shell
pg_ctl -D /opt/PostgreSQL/data2_upgraded start -l logfile
```

```shell
pg_ctl -D /opt/PostgreSQL/data3_upgraded start -l logfile
```

--------------------------------

### Install PostgreSQL Binaries and Libraries

Source: https://www.postgresql.org/docs/18/install-make

Installs the core PostgreSQL files into specified directories. Requires appropriate write permissions, typically executed as root. Ensure target directories are created with correct permissions if not installing as root.

```makefile
make install
```

--------------------------------

### Create, start, and drop logical replication slot with two‑phase commit using pg_recvlogical

Source: https://www.postgresql.org/docs/18/logicaldecoding-example

These shell commands create a logical replication slot with two‑phase support, start streaming, prepare a transaction via psql, and later commit the transaction before dropping the slot. Requires PostgreSQL with logical decoding enabled and appropriate privileges.

```Shell
$ pg_recvlogical -d postgres --slot=test --drop-slot
$ pg_recvlogical -d postgres --slot=test --create-slot --enable-two-phase
$ pg_recvlogical -d postgres --slot=test --start -f -
$ psql -d postgres -c "BEGIN;INSERT INTO data(data) VALUES('5');PREPARE TRANSACTION 'test';"
$ psql -d postgres -c "COMMIT PREPARED 'test';"
$ pg_recvlogical -d postgres --slot=test --drop-slot
```

--------------------------------

### Start PostgreSQL Server

Source: https://www.postgresql.org/docs/18/upgrading

This command starts the PostgreSQL database server. It should be executed as the special database user account after initialization or restoration. Ensure the data directory is correctly specified.

```bash
/usr/local/pgsql/bin/postgres -D /usr/local/pgsql/data
```

--------------------------------

### Setup Type and Language for PostgreSQL Transform

Source: https://www.postgresql.org/docs/18/sql-createtransform

Prepares the necessary type and language extension for creating a transform. Requires appropriate privileges and extensions. Demonstrates initial setup steps before defining conversion functions.

```sql
CREATE TYPE hstore ...;

CREATE EXTENSION plpython3u;
```

--------------------------------

### Install PostgreSQL Extension After Setting Search Path

Source: https://www.postgresql.org/docs/18/sql-createextension

This alternative method installs the 'hstore' extension by first setting the 'search_path' to the 'addons' schema and then executing the CREATE EXTENSION command. This approach also places the extension's objects within the specified schema.

```sql
SET search_path = addons;
CREATE EXTENSION hstore;

```

--------------------------------

### CREATE INDEX Examples

Source: https://www.postgresql.org/docs/18/sql-createindex

Practical examples demonstrating various ways to use the CREATE INDEX statement, including unique indexes, indexes with included columns, expression indexes, and more.

```APIDOC
## CREATE INDEX Examples

### Description
A collection of examples showcasing different use cases and configurations for the `CREATE INDEX` statement in PostgreSQL.

### Examples:

1.  **Unique B-tree index on a single column:**
    ```sql
    CREATE UNIQUE INDEX title_idx ON films (title);
    ```

2.  **Unique B-tree index with included columns:**
    ```sql
    CREATE UNIQUE INDEX title_idx ON films (title) INCLUDE (director, rating);
    ```

3.  **B-tree index with deduplication disabled:**
    ```sql
    CREATE INDEX title_idx ON films (title) WITH (deduplicate_items = off);
    ```

4.  **Index on an expression for case-insensitive searches:**
    ```sql
    CREATE INDEX ON films ((lower(title)));
    ```
    *(Note: Index name is omitted, PostgreSQL will generate one.)*

5.  **Index with non-default collation:**
    ```sql
    CREATE INDEX title_idx_german ON films (title COLLATE "de_DE");
    ```

6.  **Index with non-default sort ordering of nulls:**
    ```sql
    CREATE INDEX title_idx_nulls_low ON films (title NULLS FIRST);
    ```

7.  **Unique index with a non-default fill factor:**
    ```sql
    CREATE UNIQUE INDEX title_idx ON films (title) WITH (fillfactor = 70);
    ```

8.  **GIN index with fast updates disabled:**
    ```sql
    CREATE INDEX gin_idx ON documents_table USING GIN (locations) WITH (fastupdate = off);
    ```

9.  **Index residing in a specific tablespace:**
    ```sql
    CREATE INDEX code_idx ON films (code) TABLESPACE indexspace;
    ```

10. **GiST index on a point attribute using a function:**
    ```sql
    CREATE INDEX pointloc ON points USING gist (box(location,location));
    SELECT * FROM points WHERE box(location,location) && '(0,0),(1,1)'::box;
    ```

11. **Index creation without locking out writes (concurrently):**
    ```sql
    CREATE INDEX CONCURRENTLY sales_quantity_index ON sales_table (quantity);
    ```

### Method
SQL Statement

### Endpoint
N/A (SQL Command)

### Parameters
N/A

### Response
N/A
```

--------------------------------

### PostgreSQL Standby Server Configuration Example

Source: https://www.postgresql.org/docs/18/warm-standby

This example demonstrates a basic configuration for a PostgreSQL standby server, including primary connection information, restore command, and archive cleanup command. It shows how to connect to the primary server and manage WAL archiving for the standby.

```postgresql
primary_conninfo = 'host=192.168.1.50 port=5432 user=foo password=foopass options=\"-c wal_sender_timeout=5000\''
restore_command = 'cp /path/to/archive/%f %p'
archive_cleanup_command = 'pg_archivecleanup /path/to/archive %r'
```

--------------------------------

### Initialize New PostgreSQL Database Cluster

Source: https://www.postgresql.org/docs/18/upgrading

This command initializes a new PostgreSQL database cluster in the specified data directory. It requires execution as the special database user account and is a prerequisite for restoring data or starting a new installation.

```bash
/usr/local/pgsql/bin/initdb -D /usr/local/pgsql/data
```

--------------------------------

### PO File Structure Example

Source: https://www.postgresql.org/docs/18/nls-translator

Demonstrates the structure of a PO file, highlighting the 'msgid' (original string) and 'msgstr' (translated string) directives. The translator's task is to fill in the 'msgstr' content.

```gettext
msgid "The file %2$s has %1$u characters."
msgstr "Die Datei %2$s hat %1$u Zeichen."
```

--------------------------------

### Install PL/Perl Validator Function in SQL

Source: https://www.postgresql.org/docs/18/xplang-install

Example for PL/Perl: declares validator for function syntax checking, linked to $libdir/plperl and STRICT. Takes OID, returns void. Ensures PL/Perl function correctness before execution; part of PL/Perl's manual setup.

```sql
CREATE FUNCTION plperl_validator(oid) RETURNS void AS
    '$libdir/plperl' LANGUAGE C STRICT;
```

--------------------------------

### Non-blocking Cancel Request Setup

Source: https://www.postgresql.org/docs/18/libpq-cancel

Starts non-blocking cancel request to PostgreSQL server. Takes PGcancelConn from PQcancelCreate. Returns 1 if cancellation could be started, 0 if not. Use PQcancelSocket to get socket descriptor and PQcancelPoll to proceed with connection sequence. Loop until PGRES_POLLING_OK or PGRES_POLLING_FAILED.

```C
int PQcancelStart(PGcancelConn *cancelConn);

PostgresPollingStatusType PQcancelPoll(PGcancelConn *cancelConn);
```

--------------------------------

### Synonym Dictionary Usage Examples

Source: https://www.postgresql.org/docs/18/textsearch-dictionaries

Shows examples of creating and querying a synonym dictionary in PostgreSQL, including usage with `to_tsvector()` and `to_tsquery()`. It demonstrates how prefix matches are handled.

```SQL
mydb=# CREATE TEXT SEARCH DICTIONARY syn (template=synonym, synonyms='synonym_sample');
mydb=# SELECT ts_lexize('syn', 'indices');
 ts_lexize
-----------
 {index}
(1 row)

mdb=# CREATE TEXT SEARCH CONFIGURATION tst (copy=simple);
mdb=# ALTER TEXT SEARCH CONFIGURATION tst ALTER MAPPING FOR asciiword WITH syn;
mdb=# SELECT to_tsvector('tst', 'indices');
 to_tsvector
-------------
 'index':1
(1 row)

mdb=# SELECT to_tsquery('tst', 'indices');
 to_tsquery
-------------
 'index':*
(1 row)

mdb=# SELECT 'indexes are very useful'::tsvector;
            tsvector
---------------------------------
 'are' 'indexes' 'useful' 'very'
(1 row)

mdb=# SELECT 'indexes are very useful'::tsvector @@ to_tsquery('tst', 'indices');
 ?column?
-----------
t
(1 row)

```

--------------------------------

### Retrieve PostgreSQL build configuration using pg_config

Source: https://www.postgresql.org/docs/18/app-pgconfig

This example demonstrates how to use pg_config to retrieve and apply the build configuration of the current PostgreSQL installation. The command uses eval to properly handle shell quotation marks in the output.

```Shell
eval ./configure `pg_config --configure`
```

--------------------------------

### Get Multiple WAL Records Information

Source: https://www.postgresql.org/docs/18/pgwalinspect

Fetches information for all valid WAL records within a specified range of LSNs. It returns a set of records, with each row representing a single WAL record. The function requires valid start and end LSNs; an error occurs if the start LSN is unavailable. The example demonstrates limiting the output to one record.

```sql
SELECT * FROM pg_get_wal_records_info('0/1E913618', '0/1E913740') LIMIT 1;
```

--------------------------------

### Client-Only PostgreSQL Installation

Source: https://www.postgresql.org/docs/18/install-make

Installs only the PostgreSQL client applications and interface libraries. This is useful for environments that only need to connect to a PostgreSQL server and do not require server components.

```makefile
make -C src/bin install
make -C src/include install
make -C src/interfaces install
make -C doc install
```

--------------------------------

### Install and Strip PostgreSQL Binaries

Source: https://www.postgresql.org/docs/18/install-make

Installs PostgreSQL binaries and libraries after stripping them to reduce file size. This is useful for saving disk space but should only be done if debugging support is not needed.

```makefile
make install-strip
```

--------------------------------

### Synonym File Example

Source: https://www.postgresql.org/docs/18/textsearch-dictionaries

Illustrates an example synonym file format used by PostgreSQL's synonym dictionary. Each line contains a word followed by its synonym, separated by whitespace. An asterisk indicates a prefix synonym.

```Text
postgres        pgsql
postgresql      pgsql
postgre pgsql
gogle   googl
indices index*
```

--------------------------------

### Starting PostgreSQL Server with Shell Command-Line Parameters

Source: https://www.postgresql.org/docs/18/config-setting

During server startup, the postgres command accepts -c or --name=value options to override postgresql.conf settings. These take precedence over configuration files and ALTER SYSTEM, requiring a server restart to change globally. Example sets logging options; other clients may have similar mechanisms.

```bash
postgres -c log_connections=all --log-destination='syslog'
```

--------------------------------

### Create table for publication example

Source: https://www.postgresql.org/docs/18/logical-replication-col-lists

Creates a sample table with multiple columns to demonstrate column list filtering in publications. The table includes a primary key and several text columns. This is the base table used for replication examples.

```sql
CREATE TABLE t1(id int, a text, b text, c text, d text, e text, PRIMARY KEY(id));
```

--------------------------------

### Install PL/Perl Handler Function in SQL

Source: https://www.postgresql.org/docs/18/xplang-install

Specific example for PL/Perl: declares the call handler function linking to $libdir/plperl. Returns language_handler for processing PL/Perl functions. Used in manual installation of PL/Perl, requires shared object availability.

```sql
CREATE FUNCTION plperl_call_handler() RETURNS language_handler AS
    '$libdir/plperl' LANGUAGE C;
```

--------------------------------

### Install PostgreSQL Extension with Custom Prefix (PostgreSQL Path)

Source: https://www.postgresql.org/docs/18/extend-pgxs

Installs the extension into a specified prefix directory containing 'postgresql' or 'pgsql'. It sets the prefix to '/usr/local/postgresql', installing control and SQL files into share and shared modules into lib. Requires make install and proper pg_config setup for PostgreSQL environment.

```shell
make install prefix=/usr/local/postgresql
```

--------------------------------

### LDAP URL Example

Source: https://www.postgresql.org/docs/18/libpq-ldap

Provides an example LDAP URL used to query the LDAP server for connection parameters. Demonstrates the URL syntax for retrieving information from an LDAP directory.

```url
ldap://ldap.mycompany.com/dc=mycompany,dc=com?description?one?(cn=mydatabase)
```

--------------------------------

### Explain Prepared Statement Execution (SQL)

Source: https://www.postgresql.org/docs/18/sql-prepare

Demonstrates how to use the EXPLAIN command to inspect the query plan for a prepared statement execution. It shows how parameter symbols differ between generic and custom plans.

```sql
EXPLAIN EXECUTE _name_(_parameter_values_);
```

--------------------------------

### Install PostgreSQL Extension

Source: https://www.postgresql.org/docs/18/sql-createlanguage

This SQL command is used to install a PostgreSQL extension, which often includes the setup for new procedural languages. Extensions simplify the process of adding new functionality to the database.

```sql
CREATE EXTENSION plsample;
```

--------------------------------

### Install file_fdw Extension

Source: https://www.postgresql.org/docs/18/file-fdw

This SQL snippet demonstrates how to install the file_fdw extension in PostgreSQL, making its functionality available for use. This is a prerequisite for creating foreign servers and tables with the file_fdw wrapper.

```sql
CREATE EXTENSION file_fdw;

```

--------------------------------

### PostgreSQL: Running intarray Benchmark Tests

Source: https://www.postgresql.org/docs/18/intarray

Provides instructions to set up and run the intarray extension's benchmark test suite against an installed PostgreSQL server, requiring DBD::Pg for execution.

```bash
cd .../contrib/intarray/bench
createdb TEST
psql -c "CREATE EXTENSION intarray" TEST
./create_test.pl | psql TEST
./bench.pl

```

--------------------------------

### Create PL/Perl Language Declaration in SQL

Source: https://www.postgresql.org/docs/18/xplang-install

Example: defines PL/Perl as a TRUSTED language, associating all declared handlers. Enables PL/Perl for database functions. TRUSTED due to safe design; completes manual PL/Perl installation.

```sql
CREATE TRUSTED LANGUAGE plperl
    HANDLER plperl_call_handler
    INLINE plperl_inline_handler
    VALIDATOR plperl_validator;
```

--------------------------------

### PostgreSQL: Start an online backup

Source: https://www.postgresql.org/docs/18/functions-admin

Prepares the server for an online backup by creating a checkpoint and returning the WAL location. Supports an optional 'fast' mode for quicker initiation at the cost of I/O spikes. Requires superuser privileges or EXECUTE permission.

```sql
SELECT pg_backup_start('my_backup_label');
SELECT pg_backup_start('my_backup_label', true);
```

--------------------------------

### Connect to PostgreSQL database using libpq

Source: https://www.postgresql.org/docs/18/libpq-example

Establishes a connection to a PostgreSQL database using connection parameters. Uses environment variables or defaults if no parameters provided. Includes error handling for connection failures and sets a secure search path to prevent malicious user control.

```c
if (argc > 1)
    conninfo = argv[1];
else
    conninfo = "dbname = postgres";

/* Make a connection to the database */
conn = PQconnectdb(conninfo);

/* Check to see that the backend connection was successfully made */
if (PQstatus(conn) != CONNECTION_OK)
{
    fprintf(stderr, "%s", PQerrorMessage(conn));
    exit_nicely(conn);
}

/* Set always-secure search path, so malicious users can't take control. */
res = PQexec(conn,
             "SELECT pg_catalog.set_config('search_path', '', false)");
if (PQresultStatus(res) != PGRES_TUPLES_OK)
{
    fprintf(stderr, "SET failed: %s", PQerrorMessage(conn));
    PQclear(res);
    exit_nicely(conn);
}
```

--------------------------------

### Get Current Date and Time in PostgreSQL

Source: https://www.postgresql.org/docs/18/functions-datetime

Retrieve current timestamps at different transaction scopes. now() and transaction_timestamp() return transaction start time, statement_timestamp() returns statement start time, and timeofday() provides a formatted text string. All reflect the session time zone.

```sql
SELECT now();
-- Result: 2019-12-23 14:39:53.662522-05

SELECT statement_timestamp();
-- Result: 2019-12-23 14:39:53.662522-05

SELECT timeofday();
-- Result: Mon Dec 23 14:39:53.662522 2019 EST

SELECT transaction_timestamp();
-- Result: 2019-12-23 14:39:53.662522-05
```

--------------------------------

### VPATH Build Using Core Script Method

Source: https://www.postgresql.org/docs/18/extend-pgxs

Sets up VPATH build using the make variable VPATH pointing to source tree. It simplifies build process for extensions similar to core code. Dependencies include make and core script setup; inputs are VPATH path; outputs installation from separate directory; offers flexibility in directory layouts.

```shell
make VPATH=/path/to/extension/source/tree
make VPATH=/path/to/extension/source/tree install
```

--------------------------------

### Install PL/Perl Inline Handler Function in SQL

Source: https://www.postgresql.org/docs/18/xplang-install

Example for PL/Perl: declares inline handler for DO commands in PL/Perl. Takes internal, returns void, linked to $libdir/plperl and marked STRICT. Supports anonymous code execution; depends on main handler.

```sql
CREATE FUNCTION plperl_inline_handler(internal) RETURNS void AS
    '$libdir/plperl' LANGUAGE C STRICT;
```

--------------------------------

### SET DESCRIPTOR Usage Examples - Embedded SQL

Source: https://www.postgresql.org/docs/18/ecpg-sql-set-descriptor

Practical examples demonstrating SET DESCRIPTOR command usage in Embedded SQL programs. Shows setting descriptor count, binding parameters with values and indicators. Examples include host variables and literal values for prepared statements.

```SQL
EXEC SQL SET DESCRIPTOR indesc COUNT = 1;
EXEC SQL SET DESCRIPTOR indesc VALUE 1 DATA = 2;
EXEC SQL SET DESCRIPTOR indesc VALUE 1 DATA = :val1;
EXEC SQL SET DESCRIPTOR indesc VALUE 2 INDICATOR = :val1, DATA = 'some string';
EXEC SQL SET DESCRIPTOR indesc VALUE 2 INDICATOR = :val2null, DATA = :val2;
```

--------------------------------

### Setup JSON Data for Path Queries in PostgreSQL

Source: https://www.postgresql.org/docs/18/functions-json

Creates a sample JSON document containing GPS tracker data and stores it in a psql variable using \gset. This setup enables subsequent path expression examples to reference the same data structure. Requires PostgreSQL 12+ with psql client.

```sql
SELECT '{
  "track": {
    "segments": [
      {
        "location":   [ 47.763, 13.4034 ],
        "start time": "2018-10-14 10:05:14",
        "HR": 73
      },
      {
        "location":   [ 47.706, 13.2635 ],
        "start time": "2018-10-14 10:39:21",
        "HR": 135
      }
    ]
  }
}' AS json \gset
```

--------------------------------

### Shell: Stream Logical Decoding Changes with pg_recvlogical

Source: https://www.postgresql.org/docs/18/logicaldecoding-example

This example demonstrates using the `pg_recvlogical` utility to stream logical decoding changes from a PostgreSQL database. It shows creating a slot, starting to receive changes, and processing INSERT/COMMIT transactions. Requires client authentication for replication and sufficient `max_wal_senders`.

```shell
Example 1:
$ pg_recvlogical -d postgres --slot=test --create-slot
$ pg_recvlogical -d postgres --slot=test --start -f -
**Control**+**Z**
$ psql -d postgres -c "INSERT INTO data(data) VALUES('4');"
$ fg
BEGIN 693
table public.data: INSERT: id[integer]:4 data[text]:'4'
COMMIT 693
**Control**+**C**
```

--------------------------------

### Build and Install sepgsql Regression Test Policy (Shell)

Source: https://www.postgresql.org/docs/18/sepgsql

This snippet demonstrates the shell commands to navigate to the sepgsql contrib directory, build the sepgsql-regtest policy package using a provided Makefile, and install it using semodule. It also shows how to verify the installation by listing installed policies.

```shell
$ cd .../contrib/sepgsql
$ make -f /usr/share/selinux/devel/Makefile
$ sudo semodule -u sepgsql-regtest.pp
$ sudo semodule -l | grep sepgsql
sepgsql-regtest 1.07
```

--------------------------------

### Join with pg_class to get table names from OIDs

Source: https://www.postgresql.org/docs/18/ddl-inherit

Shows how to join the tableoid with pg_class system catalog to get human-readable table names instead of numeric OIDs. This query reveals which rows came from the cities table versus the capitals table, making the inheritance hierarchy visible in the results.

```sql
SELECT p.relname, c.name, c.elevation
FROM cities c, pg_class p
WHERE c.elevation > 500 AND c.tableoid = p.oid;
```

--------------------------------

### Get Multiple B-Tree Index Page Statistics (SQL)

Source: https://www.postgresql.org/docs/18/pageinspect

The `bt_multi_page_stats` function is similar to `bt_page_stats` but returns statistics for a range of pages. It takes the index name, starting block number, and the count of pages to retrieve. A negative count retrieves all pages from the starting block to the end.

```sql
SELECT * FROM bt_multi_page_stats('pg_proc_oid_index', 5, 2);
```

--------------------------------

### C-Style Block Comment Example

Source: https://www.postgresql.org/docs/18/sql-syntax-lexical

Illustrates a C-style block comment in SQL, which starts with '/*' and ends with '*/'. These comments support nesting, unlike in standard C.

```sql
/* multiline comment
 * with nesting: /* nested block comment */
 */

```

--------------------------------

### Create Multiple Partitions for Multi-Column Key

Source: https://www.postgresql.org/docs/18/sql-createtable

This is an incomplete example showing the start of creating partitions for a range-partitioned table with multiple columns in its partition key.

```sql
CREATE TABLE measurement_ym_older
    PARTITION OF measurement_year_month

```

--------------------------------

### Execute binary parameter query in C with libpq

Source: https://www.postgresql.org/docs/18/libpq-example

Shows how to pass binary parameters to PostgreSQL using PQexecParams. Includes network byte order conversion for integers.

```C
uint32_t    binaryIntVal;
const char *paramValues[1];
int         paramLengths[1];
int         paramFormats[1];

binaryIntVal = htonl((uint32_t) 2);

paramValues[0] = (char *) &binaryIntVal;
paramLengths[0] = sizeof(binaryIntVal);
paramFormats[0] = 1;        /* binary */

res = PQexecParams(conn,
                   "SELECT * FROM test1 WHERE i = $1::int4",
                   1,       /* one param */
                   NULL,    /* let the backend deduce param type */
                   paramValues,
                   paramLengths,
                   paramFormats,
                   1);      /* ask for binary results */

if (PQresultStatus(res) != PGRES_TUPLES_OK)
{
    fprintf(stderr, "SELECT failed: %s", PQerrorMessage(conn));
    PQclear(res);
    exit_nicely(conn);
}

show_binary_results(res);
PQclear(res);
```

--------------------------------

### Initialize PostgreSQL Cluster for sepgsql Module

Source: https://www.postgresql.org/docs/18/sepgsql

This script sets up a new PostgreSQL database cluster with sepgsql enabled by exporting data directory, initializing the database, editing configuration to load the module, and applying sepgsql.sql to templates and default database. Requires PostgreSQL installation and SELinux setup. Inputs are paths and database names; outputs initialized cluster with security labels. Limitations include potential warnings from selinux-policy versions.

```bash
$ export PGDATA=/path/to/data/directory
$ initdb
$ vi $PGDATA/postgresql.conf
  change
    #shared_preload_libraries = ''                # (change requires restart)
  to
    shared_preload_libraries = 'sepgsql'          # (change requires restart)
$ for DBNAME in template0 template1 postgres; do
    postgres --single -F -c exit_on_error=true $DBNAME \
      </usr/local/pgsql/share/contrib/sepgsql.sql >/dev/null
  done

```

--------------------------------

### PostgreSQL: Source Code Locations for Planner Statistics

Source: https://www.postgresql.org/docs/18/row-estimation-examples

Provides the file paths within the PostgreSQL source code where different aspects of the planner's statistics and selectivity estimation logic are implemented. This is useful for developers seeking to understand or modify the optimizer's behavior.

```text
src/backend/optimizer/util/plancat.c
src/backend/optimizer/path/clausesel.c
src/backend/utils/adt/selfuncs.c
```

--------------------------------

### SQL Standard Comment Example

Source: https://www.postgresql.org/docs/18/sql-syntax-lexical

Demonstrates a standard SQL comment, which starts with double dashes and extends to the end of the line. This type of comment is removed before syntax analysis.

```sql
-- This is a standard SQL comment

```

--------------------------------

### PostgreSQL array_agg with DISTINCT and ORDER BY

Source: https://www.postgresql.org/docs/18/sql-expressions

Demonstrates the use of array_agg with both DISTINCT and an ORDER BY clause. This example shows how to get an array of unique values sorted in descending order.

```sql
WITH vals (v) AS ( VALUES (1),(3),(4),(3),(2) )
SELECT array_agg(DISTINCT v ORDER BY v DESC) FROM vals;
```

--------------------------------

### Install PostgreSQL Extension into Specific Schema

Source: https://www.postgresql.org/docs/18/sql-createextension

This command installs the 'hstore' extension into the 'addons' schema. It requires superuser privileges and ensures the extension's objects are isolated within the specified schema.

```sql
CREATE EXTENSION hstore SCHEMA addons;

```

--------------------------------

### Interactive createuser command

Source: https://www.postgresql.org/docs/18/app-createuser

This example demonstrates the interactive mode of the createuser command, which prompts the user for additional attributes for the new role. This includes whether the role should be a superuser, allowed to create databases, or create more roles.

```bash
$ **createuser --interactive joe**
Shall the new role be a superuser? (y/n) **n**
Shall the new role be allowed to create databases? (y/n) **n**
Shall the new role be allowed to create more new roles? (y/n) **n**
```

--------------------------------

### Get statistics from hstore keys in PostgreSQL

Source: https://www.postgresql.org/docs/18/hstore

Examples showing how to extract key-value pairs from hstore data and perform statistical analysis on key usage frequency.

```sql
SELECT * FROM each('aaa=>bq, b=>NULL, ""=>1');
```

```sql
CREATE TABLE stat AS SELECT (each(h)).key, (each(h)).value FROM testhstore;
```

```sql
SELECT key, count(*) FROM
  (SELECT (each(h)).key FROM testhstore) AS stat
  GROUP BY key
  ORDER BY count DESC, key;
    key    | count
-----------+-------
 line      |   883
 query     |   207
 pos       |   203
 node      |   202
 space     |   197
 status    |   195
 public    |   194
 title     |   190
 org       |   189
...................
```

--------------------------------

### PostgreSQL Restore Command Examples

Source: https://www.postgresql.org/docs/18/runtime-config-wal

Examples of the `restore_command` setting in PostgreSQL for archive recovery. This command retrieves archived WAL segments. It supports placeholders like %f (WAL file name) and %p (destination path). Handles different operating systems.

```postgresql
restore_command = 'cp /mnt/server/archivedir/%f "%p"'
```

```postgresql
restore_command = 'copy "C:\\server\\archivedir\\%f" "%p"'  # Windows
```

--------------------------------

### C Example: Establishing PostgreSQL Connections with ECPG

Source: https://www.postgresql.org/docs/18/ecpg-sql-connect

Illustrates how to use the ECPG preprocessor in C to establish PostgreSQL database connections. It shows connection using direct database names and user, and then using a connection string, including selecting the version and disconnecting.

```c
int
main(void)
{
EXEC SQL BEGIN DECLARE SECTION;
    char *dbname     = "testdb";    /* database name */
    char *user       = "testuser";  /* connection user name */
    char *connection = "tcp:postgresql://localhost:5432/testdb";
                                    /* connection string */
    char ver[256];                  /* buffer to store the version string */
EXEC SQL END DECLARE SECTION;

    ECPGdebug(1, stderr);

    EXEC SQL CONNECT TO :dbname USER :user;
    EXEC SQL SELECT pg_catalog.set_config('search_path', '', false); EXEC SQL COMMIT;
    EXEC SQL SELECT version() INTO :ver;
    EXEC SQL DISCONNECT;

    printf("version: %s\n", ver);

    EXEC SQL CONNECT TO :connection USER :user;
    EXEC SQL SELECT pg_catalog.set_config('search_path', '', false); EXEC SQL COMMIT;
    EXEC SQL SELECT version() INTO :ver;
    EXEC SQL DISCONNECT;

    printf("version: %s\n", ver);

    return 0;
}

```

--------------------------------

### Start PostgreSQL Base Backup (SQL)

Source: https://www.postgresql.org/docs/18/continuous-archiving

This SQL code snippet demonstrates how to start a base backup using the `pg_backup_start` function in PostgreSQL. It requires appropriate privileges (superuser or EXECUTE on the function) and maintaining the connection until the backup is complete. The `label` parameter uniquely identifies the backup operation.

```sql
SELECT pg_backup_start(label => 'label', fast => false);
```

--------------------------------

### LINGUAS File Example

Source: https://www.postgresql.org/docs/18/nls-translator

Illustrates how to add language codes to the LINGUAS file to register new translations. This file informs the build system about available language versions.

```text
de fr
```

--------------------------------

### createuser with password assignment and superuser privileges

Source: https://www.postgresql.org/docs/18/app-createuser

This example shows how to create a user 'joe' as a superuser and immediately assign a password. The command prompts for the password twice for confirmation. The underlying SQL command generated by createuser encrypts the password.

```bash
$ **createuser -P -s -e joe**
Enter password for new role: **xyzzy**
Enter it again: **xyzzy**
CREATE ROLE joe PASSWORD 'md5b5f5ba1a423792b526f799ae4eb3d59e' SUPERUSER CREATEDB CREATEROLE INHERIT LOGIN;
```

--------------------------------

### PostgreSQL Configuration for Logical Replication

Source: https://www.postgresql.org/docs/18/logical-replication-quick-setup

Configure PostgreSQL to enable logical replication by setting wal_level to 'logical' in postgresql.conf. Adjust pg_hba.conf to allow replication connections from specific users and hosts using MD5 authentication.

```sql
wal_level = logical

```

```sql
host     all     repuser     0.0.0.0/0     md5

```

--------------------------------

### PostgreSQL POSIX Regular Expression Anchoring and Grouping Examples

Source: https://www.postgresql.org/docs/18/functions-matching

Illustrates advanced POSIX regular expression patterns in PostgreSQL, including anchoring to the start of a string ('^'), using wildcards ('.'), repetition ('*'), alternation ('|'), and grouping with parentheses.

```SQL
SELECT 'abcd' ~ 'bc'; -- true
SELECT 'abcd' ~ 'a.c'; -- true (dot matches any character)
SELECT 'abcd' ~ 'a.*d'; -- true (* repeats preceding pattern)
SELECT 'abcd' ~ '(b|x)'; -- true (| means OR, parentheses group)
SELECT 'abcd' ~ '^a'; -- true (^ anchors to start)
SELECT 'abcd' ~ '^(b|c)'; -- false (anchoring prevents match)
```

--------------------------------

### PostgreSQL CONNECT Command Syntax Examples

Source: https://www.postgresql.org/docs/18/ecpg-sql-connect

Demonstrates various ways to use the CONNECT command in PostgreSQL, including specifying connection targets, names, users, and using different connection string formats like TCP/IP and Unix-domain sockets.

```sql
EXEC SQL CONNECT TO "connectdb" AS main;
EXEC SQL CONNECT TO "connectdb" AS second;
EXEC SQL CONNECT TO "unix:postgresql://200.46.204.71/connectdb" AS main USER connectuser;
EXEC SQL CONNECT TO "unix:postgresql://localhost/connectdb" AS main USER connectuser;
EXEC SQL CONNECT TO 'connectdb' AS main;
EXEC SQL CONNECT TO 'unix:postgresql://localhost/connectdb' AS main USER :user;
EXEC SQL CONNECT TO :db AS :id;
EXEC SQL CONNECT TO :db USER connectuser USING :pw;
EXEC SQL CONNECT TO @localhost AS main USER connectdb;
EXEC SQL CONNECT TO REGRESSDB1 as main;
EXEC SQL CONNECT TO AS main USER connectdb;
EXEC SQL CONNECT TO connectdb AS :id;
EXEC SQL CONNECT TO connectdb AS main USER connectuser/connectdb;
EXEC SQL CONNECT TO connectdb AS main;
EXEC SQL CONNECT TO connectdb@localhost AS main;
EXEC SQL CONNECT TO tcp:postgresql://localhost/ USER connectdb;
EXEC SQL CONNECT TO tcp:postgresql://localhost/connectdb USER connectuser IDENTIFIED BY connectpw;
EXEC SQL CONNECT TO tcp:postgresql://localhost:20/connectdb USER connectuser IDENTIFIED BY connectpw;
EXEC SQL CONNECT TO unix:postgresql://localhost/ AS main USER connectdb;
EXEC SQL CONNECT TO unix:postgresql://localhost/connectdb AS main USER connectuser;
EXEC SQL CONNECT TO unix:postgresql://localhost/connectdb USER connectuser IDENTIFIED BY "connectpw";
EXEC SQL CONNECT TO unix:postgresql://localhost/connectdb USER connectuser USING "connectpw";
EXEC SQL CONNECT TO unix:postgresql://localhost/connectdb?connect_timeout=14 USER connectuser;
```

--------------------------------

### Retrieving Array Dimensions and Length in PostgreSQL

Source: https://www.postgresql.org/docs/18/arrays

Shows how to use PostgreSQL functions to get information about array dimensions and element counts. Includes examples for array_dims, array_upper, array_lower, array_length, and cardinality.

```sql
SELECT array_dims(schedule) FROM sal_emp WHERE name = 'Carol';

SELECT array_upper(schedule, 1) FROM sal_emp WHERE name = 'Carol';

SELECT array_length(schedule, 1) FROM sal_emp WHERE name = 'Carol';

SELECT cardinality(schedule) FROM sal_emp WHERE name = 'Carol';
```

--------------------------------

### Run PostgreSQL Regression Tests

Source: https://www.postgresql.org/docs/18/install-meson

Execute PostgreSQL regression test suite to verify the build works correctly on the target system, including tests against a running instance.

```shell
meson test
# Run against running postgres instance
meson test --setup running
```

--------------------------------

### Prepare a PostgreSQL Statement with Parameter Types (C/C++)

Source: https://www.postgresql.org/docs/18/libpq-exec

The `PQprepare` function submits a request to create a prepared statement for later execution. It allows specifying parameter types by OID, which is crucial for ensuring correct data interpretation by the server, especially when using binary format.

```c
PGresult *PQprepare(PGconn *conn,
                    const char *stmtName,
                    const char *query,
                    int nParams,
                    const Oid *paramTypes);
```