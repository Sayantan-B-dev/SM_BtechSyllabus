# Security in Data Warehousing

**Course:** Database Management Systems  
**Module:** 5 | **Lecture:** 4  
**Date:** 03-Nov-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 5  
**Learning Methodology:** Chalk & Talk  
**Reference:** Korth & Silberschatz Database System Concepts (7th Ed.)

## Security Challenges in Data Warehousing

Data warehouses present unique security challenges that differ from operational (OLTP) databases. Because data warehouses consolidate sensitive data from multiple sources and serve diverse user communities, the attack surface is larger and the consequences of a breach are more severe.

### Key Differences from OLTP Security

| Aspect                   | OLTP Database                        | Data Warehouse                      |
|--------------------------|--------------------------------------|-------------------------------------|
| Data volume              | GB to TB                             | TB to PB                            |
| User community           | Small, well-defined (e.g., clerks)   | Large, diverse (analysts, managers, |
|                          |                                      | external partners)                  |
| Data sensitivity         | Mixed (some public, some private)    | Highly consolidated sensitive data  |
| Update pattern           | Frequent inserts/updates             | Batch loads (read-mostly)           |
| Query complexity         | Simple, pre-defined                  | Complex ad-hoc queries              |
| Data retention           | Short (current data)                 | Long (years of history)             |
| Regulatory impact        | Limited scope                        | Broad (compliance across all data)  |

### Unique Security Threats

1. **Aggregation and Inference (see below)**
2. **Massive data exfiltration** -- A single query can export terabytes of data.
3. **Privilege escalation** -- Analysts may attempt to access data outside their scope.
4. **Insider threats** -- Users with legitimate access misuse it.
5. **Data poisoning** -- Contaminated data loaded during ETL can corrupt analysis.
6. **Compliance violations** -- GDPR, HIPAA, SOX, PCI DSS apply across all stored data.

## Aggregation and Inference Problems

**Aggregation problem:** A user who cannot access individual records might be able to infer sensitive information by querying aggregate data (SUM, COUNT, AVG).

**Inference problem:** A user combines multiple queries with different filters to deduce the value of a specific individual's data.

### Example of an Inference Attack

Consider a hospital data warehouse with a `patient_visits` fact table. The analyst has access to aggregate queries but not individual records.

**Step 1:** Query the total number of visits by condition.

```sql
SELECT condition, COUNT(*) AS visit_count
FROM patient_visits
GROUP BY condition;
```

Output: `Cancer: 50`, `Flu: 1000`, `HIV: 25`.

**Step 2:** Narrow the query to a specific floor (e.g., "Floor 7" is the oncology ward).

```sql
SELECT condition, COUNT(*) AS visit_count
FROM patient_visits
WHERE department = 'Oncology'
GROUP BY condition;
```

Output: `Cancer: 45`, `HIV: 1`.

**Step 3:** The attacker knows their neighbor, Bob, is on Floor 7. By querying with additional filters (e.g., by age, gender, date), they can narrow the result to a single record and deduce that Bob has HIV.

### Prevention Strategies

| Technique            | Description                                                        |
|----------------------|--------------------------------------------------------------------|
| Cell suppression     | Suppress aggregate values when the count falls below a threshold   |
|                      | (e.g., hide any value with COUNT < 5).                             |
| k-anonymity          | Ensure each record is indistinguishable from at least k-1 others.  |
| Differential privacy | Add controlled noise to query results to mask individual           |
|                      | contributions.                                                      |
| Query restriction    | Block queries that operate on too few rows.                        |
| Audit trails         | Log all queries and review for inference patterns.                 |

## Data Masking

Data masking (also called data obfuscation) replaces sensitive data with realistic but fictitious data. It allows non-production use (testing, training, analytics) without exposing real data.

### Types of Data Masking

| Type                  | Description                                    | Example                             |
|-----------------------|------------------------------------------------|-------------------------------------|
| Static Data Masking   | Create a sanitized copy of the database.       | Replace real SSNs with fake SSNs    |
|                       | Irreversible transformation.                   | before loading into the warehouse.  |
| Dynamic Data Masking  | Mask data in real-time at query time.          | Analyst sees "XXX-XX-6789" instead  |
|                       | Original data remains on disk.                 | of the full SSN.                    |
| On-the-fly Masking    | Mask during ETL as data is loaded.             | Hash PII columns during transform.  |

### Dynamic Data Masking in SQL Server

```sql
-- Create a table with masking rules
CREATE TABLE employees (
    emp_id INT PRIMARY KEY,
    emp_name VARCHAR(100) MASKED WITH (FUNCTION = 'default()'),
    ssn VARCHAR(11) MASKED WITH (FUNCTION = 'partial(0, "XXX-XX-", 4)'),
    salary DECIMAL(10,2) MASKED WITH (FUNCTION = 'default()'),
    email VARCHAR(100) MASKED WITH (FUNCTION = 'email()')
);

-- Unmasked user (admin) sees all data
-- Masked user (analyst) sees:
--   emp_name: XXXX
--   ssn: XXX-XX-6789
--   salary: 0.00
--   email: aXXX@XXXX.com

-- Grant unmask permission only to authorized users
GRANT UNMASK TO hr_manager;
```

### Masking Functions

| Function       | Description                           | Input             | Output              |
|----------------|---------------------------------------|-------------------|---------------------|
| `default()`    | Mask all characters (type-dependent)  | 'Alice'           | 'XXXX'              |
| `email()`      | Show first letter, mask rest          | 'alice@abc.com'   | 'aXXX@XXXX.com'     |
| `partial()`    | Show prefix, add mask, show suffix    | '123-45-6789'     | 'XXX-XX-6789'       |
| `random()`     | Replace numeric with random value     | 50000             | 43217               |

## Row-Level Security

Row-Level Security (RLS) restricts which rows a user can access based on a security predicate. Different users see different subsets of data even when querying the same table.

### How RLS Works

A security predicate (a filter function or policy) is defined and attached to a table. Every query on the table is transparently rewritten to include the predicate.

```
Query from user:  SELECT * FROM sales;
                                          |
                                          v
Transformed to:   SELECT * FROM sales
                  WHERE region = 'North America';  (for a NA analyst)
                                          |
                                          v
                  SELECT * FROM sales
                  WHERE region = 'Europe';          (for a EU analyst)
```

### Row-Level Security in SQL Server

```sql
-- 1. Create an inline table-valued function that defines the predicate
CREATE FUNCTION dbo.fn_sales_filter(@region AS VARCHAR(50))
RETURNS TABLE
WITH SCHEMABINDING
AS
RETURN SELECT 1 AS result
WHERE @region = USER_NAME();
-- This predicate filters rows where the region column matches the current user's name.

-- 2. Create a security policy that applies the predicate
CREATE SECURITY POLICY SalesFilter
ADD FILTER PREDICATE dbo.fn_sales_filter(region)
ON dbo.sales
WITH (STATE = ON);

-- Now, user 'North America' sees only NA sales.
-- User 'Europe' sees only EU sales.
```

### Row-Level Security in PostgreSQL

```sql
-- Enable RLS on the table
ALTER TABLE sales ENABLE ROW LEVEL SECURITY;

-- Create a policy
CREATE POLICY sales_region_policy ON sales
FOR SELECT
USING (region = current_setting('app.region'));

-- Users can also be restricted to their own department
CREATE POLICY sales_user_policy ON sales
FOR ALL
USING (salesperson = current_user);
```

## Column-Level Security

Column-level security restricts which columns a user can see. This is typically implemented through views or through fine-grained access control features in the DBMS.

### Using Views for Column Security

```sql
-- Create a view that exposes only non-sensitive columns
CREATE VIEW public_employee_info AS
SELECT emp_id, emp_name, department, job_title
FROM employees;
-- Note: salary, ssn, performance_review columns are excluded.

-- Grant access to the view, not the underlying table
GRANT SELECT ON public_employee_info TO analyst;
```

### Column-Level Security in SQL Server

```sql
-- Deny SELECT on a specific column
DENY SELECT ON employees(ssn) TO analyst;
DENY SELECT ON employees(salary) TO analyst;
```

## Auditing

Auditing tracks all database activities for security analysis, compliance, and forensic investigation.

### What to Audit

| Event Type                 | Examples                                          |
|----------------------------|---------------------------------------------------|
| Login/Logout               | Successful and failed login attempts              |
| DDL statements             | CREATE, ALTER, DROP, TRUNCATE                     |
| DML statements             | SELECT, INSERT, UPDATE, DELETE on sensitive tables|
| Privilege changes          | GRANT, REVOKE, DENY                               |
| Schema changes             | ALTER TABLE, CREATE INDEX                         |
| Sensitive data access      | Queries that access PII or financial columns      |

### Enabling Auditing in SQL Server

```sql
-- Create a server audit
CREATE SERVER AUDIT WarehouseAudit
TO FILE (FILEPATH = 'C:\AuditLogs\');

-- Create a database audit specification
CREATE DATABASE AUDIT SPECIFICATION WarehouseAuditSpec
FOR SERVER AUDIT WarehouseAudit
ADD (SELECT ON schema::dbo BY analyst)
WITH (STATE = ON);

-- Enable the audit
ALTER SERVER AUDIT WarehouseAudit WITH (STATE = ON);
```

### Enabling Auditing in Oracle

```sql
-- Audit SELECT statements on sensitive tables
AUDIT SELECT ON sales_fact BY ACCESS WHENEVER SUCCESSFUL;

-- Audit all operations by a specific user
AUDIT ALL BY analyst BY ACCESS;

-- View audit trail
SELECT * FROM dba_audit_trail;
```

## Dynamic Data Masking in Practice

Dynamic Data Masking (DDM) is a built-in SQL Server feature that masks data at query time without modifying the stored data.

**Benefits:**
- No data duplication.
- No application changes needed (masking is applied by the database engine).
- Masking rules can be changed without touching the data.
- Exempt users (with UNMASK permission) see the original data.

**Example: Full Schema with DDM**

```sql
CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    name VARCHAR(100) MASKED WITH (FUNCTION = 'partial(1, "***", 0)'),
    email VARCHAR(100) MASKED WITH (FUNCTION = 'email()'),
    phone VARCHAR(20) MASKED WITH (FUNCTION = 'partial(0, "***-***-", 4)'),
    credit_card VARCHAR(19) MASKED WITH (FUNCTION = 'partial(0, "****-****-****-", 4)'),
    ssn VARCHAR(11) MASKED WITH (FUNCTION = 'partial(0, "***-**-", 4)')
);

-- Insert sample data
INSERT INTO customers VALUES
(1, 'Alice Johnson', 'alice@example.com', '555-123-4567',
 '1234-5678-9012-3456', '123-45-6789');

-- Analyst query (without UNMASK):
SELECT * FROM customers;
-- Result:
-- 1 | A*** | aXXX@XXXX.com | ***-***-4567 | ****-****-****-3456 | ***-**-6789

-- HR manager query (with UNMASK):
SELECT * FROM customers;
-- Result:
-- 1 | Alice Johnson | alice@example.com | 555-123-4567 | 1234-5678-9012-3456 | 123-45-6789
```

## Security in the ETL Pipeline

The ETL process itself is a security vulnerability. Data is extracted from source systems, transformed, and loaded into the warehouse. Each stage must be secured.

### ETL Security Checklist

| Stage      | Security Measure                                           |
|------------|------------------------------------------------------------|
| Extract    | Encrypt connections to source systems (SSH, TLS).          |
|            | Authenticate with limited credentials (not admin).         |
| Transform  | Mask or hash PII before loading.                           |
|            | Validate data to prevent injection (data poisoning).       |
|            | Ensure transformation scripts are version-controlled.      |
| Load       | Encrypt the database connection.                           |
|            | Use limited-privilege warehouse accounts.                  |
|            | Validate data after load (row counts, checksums).          |
| All stages | Audit all ETL runs (who ran it, when, how many rows).      |
|            | Protect ETL credentials (use secrets management).          |

## Summary of Security Measures

| Measure                 | Purpose                                       | Implementation                        |
|-------------------------|-----------------------------------------------|---------------------------------------|
| Row-Level Security      | Different users see different rows.           | Security policies with predicates     |
| Column-Level Security   | Different users see different columns.        | Views, DENY on columns                |
| Dynamic Data Masking    | Mask data at query time without modifying it.  | MASKED WITH clause                     |
| Auditing                | Track who did what and when.                  | Server/database audit specifications  |
| Data Masking (Static)   | Create a sanitized copy for non-production.   | ETL transformations                   |
| Cell Suppression        | Hide small-count aggregates.                  | Application logic or query rewriter   |
| Differential Privacy    | Add noise to protect individuals.             | Statistical noise injection            |
| Encryption              | Protect data at rest and in transit.          | TDE, TLS, column-level encryption     |
| Network Security        | Limit access to warehouse servers.            | Firewalls, VPNs, network segmentation |

---

## Practice Problems

1. Explain the aggregation and inference problems in data warehousing. Give a concrete example of an inference attack and a prevention technique.
2. What is the difference between static data masking and dynamic data masking? When would you use each?
3. Write SQL to set up row-level security on a `sales` table so that salespeople can only see their own records. Assume the `sales` table has a `salesperson` column.
4. Design an audit strategy for a financial data warehouse. List at least five types of events that must be audited and explain why each is important.
5. A healthcare data warehouse contains patient data covered by HIPAA. Describe a layered security approach (at least 4 layers) to protect this warehouse.
