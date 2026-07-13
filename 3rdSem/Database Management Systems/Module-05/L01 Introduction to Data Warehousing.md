# Introduction to Data Warehousing

**Course:** Database Management Systems  
**Module:** 5 | **Lecture:** 1  
**Date:** 29-Oct-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 5  
**Learning Methodology:** Chalk & Talk  
**Reference:** Korth & Silberschatz Database System Concepts (7th Ed.)

## What is a Data Warehouse?

A data warehouse is a large, centralized repository of data collected from multiple sources, organized for query and analysis rather than transaction processing. It is designed to support business intelligence (BI) activities such as reporting, dashboards, and data analysis.

**Formal definition (Bill Inmon):** A data warehouse is a subject-oriented, integrated, time-variant, and non-volatile collection of data in support of management's decision-making process.

**Key characteristics:**

| Characteristic    | Description                                                               |
|-------------------|---------------------------------------------------------------------------|
| Subject-oriented  | Organized around key subjects (e.g., customer, product, sales) rather     |
|                   | than applications.                                                         |
| Integrated        | Data from multiple sources is cleaned, transformed, and unified into a    |
|                   | consistent format.                                                         |
| Time-variant      | Data is stored with a time dimension, typically 5-10 years of history.    |
|                   | Every data point is associated with a point in time.                      |
| Non-volatile      | Data is loaded in bulk and is read-only. Users query but do not update    |
|                   | or delete individual records.                                             |

## OLTP vs OLAP

Online Transaction Processing (OLTP) and Online Analytical Processing (OLAP) serve fundamentally different purposes.

```
+---------------------------+------------------------------------------+
|      OLTP                 |            OLAP                          |
+---------------------------+------------------------------------------+
| Transaction-oriented      | Analysis-oriented                        |
| Many small transactions   | Few complex queries                      |
| (INSERT, UPDATE, DELETE)  | (SELECT with aggregations)               |
+---------------------------+------------------------------------------+
| Current data (day/week)   | Historical data (years)                  |
| Normalized schema (3NF)   | Denormalized schema (star, snowflake)    |
| High concurrency          | Lower concurrency                        |
| Sub-second response time  | Seconds to minutes for complex queries   |
| Used by operational staff | Used by analysts and executives          |
| Example: order entry      | Example: yearly sales trend analysis     |
+---------------------------+------------------------------------------+
```

### Detailed Differences

| Aspect                | OLTP Database                | Data Warehouse (OLAP)       |
|-----------------------|------------------------------|-----------------------------|
| Purpose               | Run the business             | Analyze the business        |
| Users                 | Clerks, customers, apps      | Analysts, executives        |
| Data volume           | GB to TB                     | TB to PB                    |
| Query complexity      | Simple, pre-defined          | Complex, ad-hoc             |
| Indexing              | B+ tree, hash                | Bitmap, bitmap join         |
| Normalization         | Highly normalized            | Denormalized                |
| Update frequency      | Continuous (real-time)       | Periodic (batch load)       |
| Backup/restore        | Point-in-time, granular      | Full load, less frequent    |
| Example               | ATM withdrawal system        | Quarterly revenue report    |

## Data Warehouse Architecture

A typical data warehouse has three tiers:

```
+--------------------+     +--------------------+     +--------------------+
|                   |     |                   |     |                   |
|   Source Systems  |     |   Staging Area    |     |   Data Warehouse   |
|                   |     |                   |     |                   |
|  +-------------+  |     |  +-------------+  |     |  +-------------+  |
|  | Operational |  |     |  | Extract     |  |     |  | Fact Tables |  |
|  | DB (OLTP)   |----->|  | Transform   |----->|  | Dim Tables  |  |
|  +-------------+  |     |  | Load (ETL)  |  |     |  +-------------+  |
|  +-------------+  |     |  +-------------+  |     |         |         |
|  | CRM System  |  |     |  | Data Quality|  |     |         v         |
|  +-------------+  |     |  | Validation  |  |     |  +-------------+  |
|  +-------------+  |     |  +-------------+  |     |  | Data Marts  |  |
|  | ERP System  |  |     |                   |     |  | (Marketing, |  |
|  +-------------+  |     |                   |     |  |  Sales, HR) |  |
|  +-------------+  |     |                   |     |  +-------------+  |
|  | Flat Files  |  |     |                   |     |                   |
|  +-------------+  |     |                   |     |                   |
+--------------------+     +--------------------+     +--------------------+
```

### 1. Source Systems
Operational databases (OLTP), CRM, ERP, spreadsheets, log files, external data feeds. These systems are where the raw transactional data resides.

### 2. Staging Area
A temporary storage area where data from multiple sources is extracted and transformed before loading into the warehouse. The ETL (Extract, Transform, Load) process runs here.

### 3. Data Warehouse
The central repository that stores integrated, historical data. Data is organized into fact tables and dimension tables.

### 4. Data Marts
Subsets of the data warehouse tailored to specific departments or business functions. For example, a Sales data mart contains only sales-related data, while an HR data mart contains employee-related data.

## ETL Process

ETL stands for Extract, Transform, Load. It is the backbone of data warehousing.

```
Extract --> Transform --> Load
   |           |            |
   v           v            v
Source      Cleanse,     Target
Systems     Map,        Warehouse
            Aggregate,
            Validate
```

### Extract
Data is extracted from source systems. This can be:
- **Full extraction:** Reading the entire source table.
- **Incremental extraction:** Reading only records changed since the last extraction (using timestamps, change tracking, or CDC -- Change Data Capture).

```sql
-- Example: Extract new orders since last load
SELECT * FROM orders
WHERE order_date > (SELECT MAX(load_timestamp) FROM etl_metadata);
```

### Transform
Data is cleaned, converted, and standardized. Common transformations:

| Transformation        | Example                                            |
|-----------------------|----------------------------------------------------|
| Data cleansing        | Remove NULLs, fix misspellings                     |
| Deduplication         | Remove duplicate customer records                  |
| Data type conversion  | Convert 'MM/DD/YYYY' to DATE type                  |
| Aggregation           | Sum daily sales to monthly                         |
| Derivation            | Calculate full name from first + last name         |
| Lookup / Surrogate key| Map source PK to warehouse surrogate key           |
| Validation            | Reject records with invalid ZIP codes              |

### Load
The transformed data is loaded into the data warehouse. Loading strategies:

- **Full refresh:** Truncate and reload the entire table.
- **Incremental load:** Append only new records.
- **Upsert (merge):** Update existing rows and insert new rows.

```sql
-- Example: Merge statement (UPSERT)
MERGE INTO sales_fact AS target
USING staging_sales AS source
ON target.order_id = source.order_id
WHEN MATCHED THEN
    UPDATE SET target.amount = source.amount
WHEN NOT MATCHED THEN
    INSERT (order_id, date_id, customer_id, amount)
    VALUES (source.order_id, source.date_id, source.customer_id, source.amount);
```

## Star Schema

A star schema is a denormalized dimensional model with a central fact table surrounded by dimension tables.

```
                        +-----------------+
                        |   Date_Dim      |
                        |-----------------|
                        | date_key (PK)   |
                        | year            |
                        | quarter         |
                        | month           |
                        | day             |
                        +-----------------+
                              |
+-----------------+          +-----------------+          +-----------------+
| Customer_Dim    |          |   Sales_Fact    |          | Product_Dim     |
|-----------------|          |-----------------|          |-----------------|
| cust_key (PK)   |<-------->| date_key (FK)   |<-------->| prod_key (PK)   |
| cust_id         |          | cust_key (FK)   |          | prod_id         |
| name            |          | prod_key (FK)   |          | prod_name       |
| city            |          | store_key (FK)  |          | category        |
| state           |          | units_sold      |          | price           |
+-----------------+          | revenue         |          +-----------------+
                             +-----------------+
                                   |
                        +-----------------+
                        | Store_Dim       |
                        |-----------------|
                        | store_key (PK)  |
                        | store_id        |
                        | store_name      |
                        | region          |
                        +-----------------+
```

**Fact table:** Contains measures (numeric, additive facts) and foreign keys to dimension tables.
**Dimension tables:** Contain descriptive attributes (text, categorical) that provide context for the facts.

### Star Schema Characteristics
- Denormalized dimensions (e.g., region is stored directly in Store_Dim rather than in a separate table).
- Simple, intuitive structure.
- Good query performance with few joins.
- Widely used in data marts.

## Snowflake Schema

A snowflake schema is a normalized version of the star schema. Dimension tables are further split into sub-dimensions.

```
                        +-----------------+
                        |   Date_Dim      |
                        +-----------------+
                              |
+-----------------+          +-----------------+          +-----------------+
| Customer_Dim    |          |   Sales_Fact    |          | Product_Dim     |
|-----------------|          |-----------------|          |-----------------|
| cust_key (PK)   |<-------->| date_key (FK)   |<-------->| prod_key (PK)   |
| cust_id         |          | cust_key (FK)   |          | prod_id         |
| name            |          | prod_key (FK)   |          | prod_name       |
| city_key (FK)   |          | store_key (FK)  |          | category_key(FK)|
+-----------------+          | units_sold      |          +-----------------+
      |                      | revenue         |                |
      v                      +-----------------+                v
+-----------------+                                   +-----------------+
| City_Dim        |           +-----------------+      | Category_Dim    |
|-----------------|           | Store_Dim       |      |-----------------|
| city_key (PK)   |           |-----------------|      | category_key PK |
| city_name       |<--------->| store_key (PK)  |      | category_name   |
| state_key (FK)  |           | store_id        |      | department      |
+-----------------+           | store_name      |      +-----------------+
      |                       | region          |
      v                       +-----------------+
+-----------------+
| State_Dim       |
|-----------------|
| state_key (PK)  |
| state_name      |
| country         |
+-----------------+
```

### Star vs Snowflake

| Aspect              | Star Schema                     | Snowflake Schema                |
|---------------------|---------------------------------|---------------------------------|
| Normalization       | Denormalized dimensions         | Normalized dimensions           |
| Complexity          | Simple, fewer tables            | Complex, more tables            |
| Query performance   | Faster (fewer joins)            | Slower (more joins required)    |
| Storage space       | More (redundant data)           | Less (no redundancy)            |
| Maintenance         | Easier                          | Harder (more FK constraints)    |
| Use case            | Data marts, simple reporting    | Enterprise warehouse, complex   |
|                     |                                 | hierarchies                     |

## Business Intelligence (BI)

Data warehouses are the foundation for Business Intelligence. BI encompasses the tools and processes used to analyze data and support decision-making.

**BI applications built on top of a data warehouse:**

- **Reports:** Scheduled, pre-formatted reports (e.g., monthly sales report).
- **Dashboards:** Real-time visualizations of KPIs (e.g., a dashboard showing current inventory levels).
- **Ad-hoc queries:** Analysts write custom SQL to explore data.
- **Data mining:** Discovering hidden patterns and relationships.
- **OLAP cubes:** Multidimensional analysis with drill-down, roll-up, slice, and dice.

---

## Practice Problems

1. List the four characteristics of a data warehouse according to Inmon's definition. Explain each with an example.
2. Draw a star schema for a university data warehouse. The fact table should track student enrollments. Include at least four dimension tables.
3. Compare OLTP and OLAP systems across at least six dimensions. Provide one example query typical for each.
4. Describe the ETL process step by step. What happens during the Transform phase? Give three examples of transformations.
5. Explain the difference between star schema and snowflake schema. When would you choose one over the other?
