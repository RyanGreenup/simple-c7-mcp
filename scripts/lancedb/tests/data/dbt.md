# dbt External Tables

## Overview

The dbt-external-tables package provides macros to create, refresh, and manage external tables across multiple database platforms using dbt's source metadata definitions. This package extends dbt's native `external` property support by automatically generating the DDL/DML commands needed to stage external data sources from cloud storage (S3, GCS, Azure) or external databases into queryable tables within your data warehouse. Instead of manually writing CREATE EXTERNAL TABLE statements for each platform, you define your external sources once in YAML configuration files, and the package handles the database-specific implementation details.

The package supports six major database platforms: Snowflake, BigQuery, Redshift Spectrum, Spark, Synapse, and Azure SQL. It provides sophisticated features like automatic partition management, Snowflake Snowpipe integration for near-real-time data loading, schema inference, and the ability to selectively stage specific sources. By centralizing external table management within dbt's existing source framework, teams can version control their external data definitions, document them alongside other data assets, and automate their creation as part of CI/CD pipelines.

## Installation and Setup

### Install the package via packages.yml

```yaml
# packages.yml
packages:
  - package: dbt-labs/dbt_external_tables
    version: 0.8.0
```

```bash
# Install dependencies
dbt deps
```

### Configure dbt project

```yaml
# dbt_project.yml
name: 'my_project'
version: '1.0.0'
config-version: 2
require-dbt-version: [">=1.0.0", "<2.0.0"]
```

## Primary Macro: stage_external_sources

### Stage all external sources in the project

```bash
# Create external tables if missing, refresh metadata for existing tables
dbt run-operation stage_external_sources

# Output:
# 1 of 1 START external source snowplow.event_ext_tbl
# 1 of 1 (1) create external table "analytics"."snowplow_external"."event_ext_tbl"...
# 1 of 1 (1) CREATE EXTERNAL TABLE
# 1 of 1 (2) alter table "analytics"."snowplow_external"."event_ext_tbl" add partition...
# 1 of 1 (2) ALTER EXTERNAL TABLE
```

### Full refresh mode (drop and recreate all external tables)

```bash
# Force recreation of all external tables
dbt run-operation stage_external_sources --vars "ext_full_refresh: true"

# Output:
# 1 of 1 START external source spectrum.my_partitioned_tbl
# 1 of 1 (1) drop table if exists "db"."spectrum"."my_partitioned_tbl"
# 1 of 1 (1) DROP TABLE
# 1 of 1 (2) create external table "db"."spectrum"."my_partitioned_tbl"...
# 1 of 1 (2) CREATE EXTERNAL TABLE
# 1 of 1 (3) alter table "db"."spectrum"."my_partitioned_tbl"...
# 1 of 1 (3) ALTER EXTERNAL TABLE
```

### Stage specific sources using node selection syntax

```bash
# Stage all external sources from specific source groups
dbt run-operation stage_external_sources --args "select: snowplow logs"

# Stage a single external table
dbt run-operation stage_external_sources --args "select: snowplow.event"

# Stage multiple specific tables
dbt run-operation stage_external_sources --args "select: snowplow.event marketing.leads"
```

## Snowflake External Table Configuration

### Basic Snowflake external table with partitions

```yaml
# models/sources.yml
version: 2

sources:
  - name: snowplow
    database: analytics
    schema: snowplow_external
    loader: S3

    tables:
      - name: event_ext_tbl
        description: "External table of Snowplow events stored as JSON files"
        external:
          location: "@raw.snowplow.snowplow"  # Existing Snowflake stage
          file_format: "( type = json )"
          auto_refresh: true
          partitions:
            - name: collector_hour
              data_type: timestamp
              expression: to_timestamp(substr(metadata$filename, 8, 13), 'YYYY/MM/DD/HH24')

        columns:
          - name: app_id
            data_type: varchar(255)
            description: "Application ID"
          - name: domain_sessionidx
            data_type: int
            description: "A visit / session index"
          - name: etl_tstamp
            data_type: timestamp
            description: "Timestamp event began ETL"
          - name: contexts
            data_type: variant
            description: "Contexts attached to event by Tracker"
```

### Snowflake with schema inference for Parquet files

```yaml
# models/sources.yml
version: 2

sources:
  - name: data_lake
    database: analytics
    schema: external

    tables:
      - name: parquet_with_inferred_schema
        description: "External table using Parquet and inferring the schema"
        external:
          location: "@stage"
          file_format: "my_file_format"  # Named file format required for inference
          infer_schema: true
          partitions:
            - name: section
              data_type: varchar(64)
              expression: "substr(split_part(metadata$filename, 'section=', 2), 1, 1)"

        columns:  # Optional - for documentation/testing
          - name: id
            description: "Unique identifier"
          - name: name
            description: "Name field"
```

### Snowflake Delta table format

```yaml
# models/sources.yml
version: 2

sources:
  - name: data_lake
    database: analytics
    schema: external

    tables:
      - name: delta_tbl
        description: "External table using Delta files"
        external:
          location: "@stage"
          file_format: "( type = parquet )"
          table_format: delta
          auto_refresh: false
```

### Snowflake with AWS SNS auto-refresh

```yaml
# models/sources.yml
version: 2

sources:
  - name: snowplow
    database: analytics
    schema: external

    tables:
      - name: aws_sns_refresh_tbl
        description: "External table using AWS SNS for auto-refresh"
        external:
          location: "@stage"
          file_format: "( type = csv )"
          aws_sns_topic: "arn:aws:sns:us-east-1:123456789012:my_topic"
```

## Snowflake Snowpipe Configuration

### Create Snowpipe for near-real-time data loading

```yaml
# models/sources.yml
version: 2

sources:
  - name: snowplow
    database: analytics
    schema: snowplow_external

    tables:
      - name: event_snowpipe
        description: "Table loaded in near-real time via Snowpipe"
        external:
          location: "@raw.snowplow.snowplow"
          file_format: "{{ target.schema }}.my_json_file_format"
          pattern: ".*[.]json"

          snowpipe:
            auto_ingest: true
            aws_sns_topic: "arn:aws:sns:us-east-1:123456789012:s3-event-topic"
            copy_options: "on_error = continue, enforce_length = false"

        columns:
          - name: app_id
            data_type: varchar(255)
          - name: platform
            data_type: varchar(255)
          - name: etl_tstamp
            data_type: timestamp
```

```bash
# Stage the snowpipe configuration
dbt run-operation stage_external_sources --args "select: snowplow.event_snowpipe"

# Output includes:
# 1. Create empty table with specified columns
# 2. Create snowpipe with auto_ingest enabled
# 3. Backfill existing data with COPY INTO
# 4. Metadata columns added: metadata_filename, metadata_file_row_number, _dbt_copied_at
```

## BigQuery External Table Configuration

### Basic BigQuery external table with CSV files

```yaml
# models/sources.yml
version: 2

sources:
  - name: snowplow
    database: analytics
    loader: gcloud storage

    tables:
      - name: event
        description: "External table of Snowplow events, stored as CSV files in Cloud Storage"
        external:
          location: 'gs://bucket/path/*'
          options:
            format: csv
            skip_leading_rows: 1
            hive_partition_uri_prefix: 'gs://bucket/path/'
          partitions:
            - name: collector_date
              data_type: date

        columns:
          - name: app_id
            data_type: varchar(255)
            description: "Application ID"
          - name: domain_sessionidx
            data_type: int
            description: "A visit / session index"
          - name: etl_tstamp
            data_type: timestamp
            description: "Timestamp event began ETL"
```

### BigQuery with schema inference

```yaml
# models/sources.yml
version: 2

sources:
  - name: snowplow
    database: analytics

    tables:
      - name: event_inferred
        description: "BigQuery automatically infers schema from files"
        external:
          location: 'gs://bucket/path/*'
          options:
            format: csv
            skip_leading_rows: 1
            hive_partition_uri_prefix: 'gs://bucket/path/'
```

### BigQuery with multiple GCS paths

```yaml
# models/sources.yml
version: 2

sources:
  - name: snowplow
    database: analytics

    tables:
      - name: event_multiple_paths
        description: "External table pulling from multiple GCS locations"
        external:
          location: 'gs://placeholder'  # Required but ignored
          options:
            format: csv
            skip_leading_rows: 1
            uris:
              - 'gs://bucket_a/path/*'
              - 'gs://bucket_b/path/*'
              - 'gs://bucket_c/more/specific/path/file.csv'
```

## Redshift Spectrum Configuration

### Redshift external table with partitions

```yaml
# models/sources.yml
version: 2

sources:
  - name: snowplow
    database: analytics
    schema: snowplow_external
    loader: S3

    tables:
      - name: event
        description: "Redshift Spectrum external table"
        external:
          location: "s3://bucket/path"
          row_format: >
            serde 'org.openx.data.jsonserde.JsonSerDe'
            with serdeproperties (
                'strip.outer.array'='false'
            )
          partitions:
            - name: appId
              data_type: varchar(255)
              vals:
                - dev
                - prod
              path_macro: dbt_external_tables.key_value

            - name: collector_date
              data_type: date
              vals:
                macro: dbt.dates_in_range
                args:
                  start_date_str: '2019-08-01'
                  end_date_str: '{{modules.datetime.date.today().strftime("%Y-%m-%d")}}'
                  in_fmt: "%Y-%m-%d"
                  out_fmt: "%Y-%m-%d"
              path_macro: dbt_external_tables.year_month_day

        columns:
          - name: app_id
            data_type: varchar(255)
            description: "Application ID"
          - name: domain_sessionidx
            data_type: int
            description: "A visit / session index"
          - name: etl_tstamp
            data_type: varchar(32)
            description: "Timestamp event began ETL"
          - name: contexts
            data_type: varchar(65000)
            description: "Contexts attached to event by Tracker"
```

```bash
# Stage Redshift external table with automatic partition generation
dbt run-operation stage_external_sources --args "select: snowplow.event"

# The macro will:
# 1. Generate partition values using the specified macro (dates_in_range)
# 2. Build S3 paths using path_macro for each partition combination
# 3. Create external table with all partition specifications
# 4. Add partitions via ALTER TABLE statements
```

## Spark External Table Configuration

### Spark external table with HDFS location

```yaml
# models/sources.yml
version: 2

sources:
  - name: snowplow
    tables:
      - name: event
        description: "Snowplow events stored as CSV files in HDFS"
        external:
          location: 'hdfs://namenode:9000/data/snowplow/event.csv'
          using: csv
          options:
            sep: '|'
            header: 'true'
            timestampFormat: 'yyyy-MM-dd HH:mm'
          partitions:
            - name: year
              data_type: int
            - name: month
              data_type: int
            - name: day
              data_type: int

        columns:
          - name: app_id
            data_type: string
            description: "Application ID"
          - name: domain_sessionidx
            data_type: int
            description: "A visit / session index"
          - name: etl_tstamp
            data_type: timestamp
            description: "Timestamp event began ETL"
          - name: contexts
            data_type: string
            description: "Contexts attached to event by Tracker"
```

### Spark with various storage locations

```yaml
# models/sources.yml
version: 2

sources:
  - name: data_sources
    tables:
      - name: s3_data
        external:
          location: 's3://bucket/path/data.parquet'
          using: parquet

      - name: azure_data
        external:
          location: 'wasbs://container@account.blob.core.windows.net/path'
          using: json

      - name: dbfs_data
        external:
          location: 'dbfs:/mnt/data/events'
          using: delta
```

## Synapse External Table Configuration

### Synapse with delimited files from Azure storage

```yaml
# models/sources.yml
version: 2

sources:
  - name: marketo
    schema: source_marketo
    loader: ADLSblob

    tables:
      - name: lead_activities
        description: "External table from Azure Data Lake Storage"
        external:
          data_source: SynapseContainer  # Pre-created TYPE='HADOOP'
          location: /marketing/Marketo/LeadActivities/
          file_format: CommaDelimited     # Pre-created file format
          reject_type: VALUE
          reject_value: 0
          ansi_nulls: true
          quoted_identifier: true

        columns:
          - name: id
            description: "Unique Activity ID"
            data_type: int
          - name: leadId
            description: "Lead ID"
            data_type: int
          - name: activityDate
            description: "Date of activity"
            data_type: varchar(255)
          - name: activityTypeId
            description: "Unique identifier for type of activity"
            data_type: int
          - name: campaignId
            description: "Campaign under which activity took place"
            data_type: int
```

```sql
-- Generated DDL:
-- SET ANSI_NULLS ON;
-- SET QUOTED_IDENTIFIER ON;
--
-- CREATE EXTERNAL TABLE [source_marketo].[lead_activities]
-- (
--    [id] [int] NOT NULL,
--    [leadId] [int] NOT NULL,
--    [activityDate] [varchar](255) NOT NULL,
--    [activityTypeId] [int] NOT NULL,
--    [campaignId] [int] NOT NULL,
--    [primaryAttributeValueId] [int] NOT NULL,
--    [primaryAttributeValue] [varchar](255) NOT NULL
-- )
-- WITH (
--   DATA_SOURCE = [SynapseContainer],
--   LOCATION = N'/marketing/Marketo/LeadActivities/',
--   FILE_FORMAT = [CommaDelimited],
--   REJECT_TYPE = VALUE,
--   REJECT_VALUE = 0
-- );
```

### Synapse cross-database query (Azure SQL)

```yaml
# models/sources.yml
version: 2

sources:
  - name: azure_sql_source
    schema: source_external

    tables:
      - name: external_rdbms_table
        description: "Cross-database query from Azure SQL"
        external:
          data_source: AEDW  # Pre-created TYPE='RDBMS'
          schema_name: Business
          object_name: LeadActivities

        columns:
          - name: id
            data_type: int
          - name: leadId
            data_type: int
```

## Advanced Column Features

### Snowflake column expressions and aliases

```yaml
# models/sources.yml
version: 2

sources:
  - name: snowplow
    database: analytics
    schema: external

    tables:
      - name: event_with_expressions
        external:
          location: "@stage"
          file_format: "( type = json )"

        columns:
          - name: etl_tstamp
            data_type: timestamp
            description: "Timestamp event began ETL"

          - name: etl_date
            data_type: date
            description: "Date extracted from timestamp"
            expression: TRY_TO_DATE(VALUE:etl_tstamp::VARCHAR, 'YYYYMMDD')

          - name: "etl timestamp"
            quote: true
            alias: etl_timestamp
            data_type: timestamp
            description: "Double-quoted identifier with alias"

          - name: app_id
            data_type: varchar(255)
            description: "Application ID"
```

### Snowflake with ignore_case for case-insensitive column matching

```yaml
# models/sources.yml
version: 2

sources:
  - name: snowplow
    database: analytics
    schema: external

    tables:
      - name: event_case_insensitive
        external:
          location: "@stage"
          file_format: "my_json_format"
          ignore_case: true  # Use GET_IGNORE_CASE for column matching

        columns:
          - name: AppId
            data_type: varchar(255)
          - name: UserId
            data_type: varchar(255)
```

## Integration with dbt Models

### Reference external source in dbt model

```sql
-- models/staging/stg_snowplow_events.sql
{{
  config(
    materialized='view'
  )
}}

select
    app_id,
    domain_sessionidx as session_index,
    etl_tstamp::timestamp as etl_timestamp,
    collector_hour,
    parse_json(contexts) as contexts_json
from {{ source('snowplow', 'event_ext_tbl') }}
where collector_hour >= current_date - interval '7 days'
```

```bash
# Workflow: Stage external sources, then run models
dbt run-operation stage_external_sources --args "select: snowplow"
dbt run --models stg_snowplow_events

# Or in CI/CD pipeline:
dbt run-operation stage_external_sources
dbt build  # Run all models, tests, snapshots
```

### Test external source data quality

```yaml
# models/sources.yml
version: 2

sources:
  - name: snowplow
    database: analytics
    schema: snowplow_external

    tables:
      - name: event_ext_tbl
        description: "External table of Snowplow events"
        external:
          location: "@raw.snowplow.snowplow"
          file_format: "( type = json )"

        columns:
          - name: app_id
            data_type: varchar(255)
            description: "Application ID"
            tests:
              - not_null
              - accepted_values:
                  values: ['web', 'mobile', 'server']

          - name: domain_sessionidx
            data_type: int
            description: "A visit / session index"
            tests:
              - not_null
              - dbt_utils.expression_is_true:
                  expression: "> 0"
```

```bash
# Stage external sources and run tests
dbt run-operation stage_external_sources --args "select: snowplow"
dbt test --select source:snowplow
```

## Error Handling and Debugging

### Check which external sources will be staged (dry run)

```bash
# Review compiled SQL without executing
dbt compile --select source:*

# Check sample_analysis directory for generated DDL examples
cat sample_analysis/bigquery_example.sql
cat sample_analysis/snowflake_example.sql
cat sample_analysis/redshift_example.sql
```

### Handle missing or incorrect configurations

```yaml
# models/sources.yml with error handling
version: 2

sources:
  - name: snowplow
    database: analytics
    schema: external

    tables:
      - name: event_with_validation
        external:
          location: "@stage"
          file_format: "( type = json )"
          refresh_on_create: false  # Skip initial refresh to avoid errors

        columns:
          - name: app_id
            data_type: varchar(255)
```

```bash
# Test with single source first
dbt run-operation stage_external_sources --args "select: snowplow.event_with_validation"

# Check for errors in output
# If successful, proceed with full refresh
dbt run-operation stage_external_sources --vars "ext_full_refresh: true" --args "select: snowplow.event_with_validation"
```

## Summary

The dbt-external-tables package is essential for teams managing external data sources across cloud data platforms, providing a declarative approach to external table management that integrates seamlessly with dbt's existing workflows. The primary use case is automating the creation and refresh of external tables that query data directly from cloud storage (S3, GCS, Azure Blob) or external databases without loading data into the warehouse. This is particularly valuable for landing zones where raw data arrives continuously, staging environments that reference large historical datasets, and architectures that separate storage from compute. Teams use this package to eliminate manual DDL scripts, ensure consistency across environments, and version control their external data definitions alongside transformation logic.

Integration patterns typically involve running `stage_external_sources` as a pre-processing step before dbt models execute, either manually during development or automatically in CI/CD pipelines. For Snowflake users, the Snowpipe integration enables near-real-time data ingestion with automatic backfilling and continuous loading. The package's adapter dispatch pattern allows the same YAML configuration to work across different database platforms with minimal changes, making it easier to maintain multi-warehouse architectures or migrate between platforms. Advanced users leverage partition macros for dynamic date-based partitioning, schema inference for evolving data structures, and selective staging to optimize refresh operations for large numbers of external sources.
