---
name: sql-query-writing
description: Write, fix or speed up SQL for Postgres, MySQL, BigQuery, Snowflake, Redshift or Databricks, including CTEs, window functions, cohorts and funnels. Use for the query itself, not for reading results.
---

# SQL Query Writing

## Use

Use when the deliverable is a query: a new one from a description, a broken one to repair, or a slow one to speed up.

Interpreting what the result means, or checking whether an analysis holds, belongs to `data/data-analysis`. Designing tables, ownership or migrations belongs to `development/technical-design`.

## Domain inputs and blockers

- **Dialect.** Date arithmetic, safe division, JSON access and identifier case differ enough that a query written for the wrong engine fails. Read it from the supplied query, schema or error text; ask once when it cannot be inferred, then keep using it.
- **Schema.** Table and column names, types, and which column each join uses. Without them, write the query against clearly named placeholders and list them.
- **Business definitions.** What counts as an active user, a completed order, a test account to exclude. When they are not given, write the assumption into a comment at the top of the query.

## Writing rules

1. One CTE per logical step, each with a descriptive name; meaningful aliases instead of single letters.
2. Select the columns that are needed. `SELECT *` stays out of anything that will be saved or scheduled.
3. Filter early, and always filter on the partition or clustering column when the table has one.
4. Know the cardinality of every join. A many-to-many join inflates sums and counts without an error; count distinct entities, or aggregate before joining.
5. Division uses `NULLIF(denominator, 0)` or the engine's safe-division function.
6. Prefer a join or a window function to a correlated subquery, and `EXISTS` to `IN` against a large subquery.
7. Comments explain why a filter or a join condition exists, not what the syntax does.

## Dialect traps

- Date addition, truncation and day-of-week numbering are written differently in every engine; state which dialect a date expression is written for, and do not carry `INTERVAL '1 month'` style syntax into an engine that does not accept it.
- **BigQuery** bills by bytes scanned: filter the partition column, avoid `SELECT *`, estimate with a dry run, and use `APPROX_COUNT_DISTINCT` when an exact count is not required.
- **Snowflake** has clustering keys rather than indexes; semi-structured data is read as `col:key::TYPE`.
- **Redshift** performance depends on distribution and sort keys; a query that redistributes or broadcasts a large table is the first suspect.
- Unquoted identifiers are folded to lower case in Postgres and to upper case in Snowflake, so a quoted mixed-case column must be quoted everywhere.

## Common shapes

- **Latest row per entity or de-duplication**: `ROW_NUMBER()` partitioned by the entity, ordered by recency, keep 1.
- **Running totals and period-over-period**: window functions with an explicit frame, not self-joins.
- **Funnel**: one row per user with the first timestamp of each step, each step required to follow the previous one.
- **Cohort retention**: assign each user to the period of first activity, then count activity by periods since that start; divide by the cohort size, not by the active users of the period.

## Fixing an error

Check in this order, because it follows how often each one is the cause: dialect syntax, column name and case, type mismatch or a missing cast, division by zero, an ambiguous column, a column missing from `GROUP BY`.

## Output

The query, then a short walk-through by CTE, the assumptions it encodes, a performance note when the tables are large, and how to change it for the most likely variation (another period, another grouping).

## Constraints

- Do not invent table or column names; placeholders are marked as placeholders.
- A query that was not run is delivered as not run; do not describe the rows it returns.
- Statements that change or delete data are written only when asked, with the matching `SELECT` first so the affected rows can be inspected.
