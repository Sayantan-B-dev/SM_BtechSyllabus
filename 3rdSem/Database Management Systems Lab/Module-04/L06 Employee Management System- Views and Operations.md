# Employee Management System- Views and Operations

**Course:** Database Management Systems Lab  
**Module:** 4 | **Lecture:** 6  
**Date:** 05-Oct-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 3  
**Learning Methodology:** Hands-on Experience  
**Reference:** Lab manual

## Lab Objectives

- Perform INSERT, UPDATE, and DELETE operations through views (updatable views).
- Drop views using DROP VIEW.
- Understand the concept of materialized views and how they differ from regular views.

## Theory / Concept

A view is updatable if it is based on a single table and does not contain aggregations, GROUP BY, DISTINCT, or set operations. INSERT/UPDATE/DELETE on such views modifies the underlying base table. Materialized views (not natively supported in MySQL) physically store the query result and are refreshed periodically, unlike regular views that are computed on the fly. DROP VIEW removes the view definition without affecting the base tables.

## SQL Code

```sql
USE EmployeeDB;

-- Create an updatable view (single table, no aggregation)
CREATE VIEW EmployeeSalaryView AS
SELECT emp_id, emp_name, department, job_role, salary, dept_id
FROM Employee
WHERE salary > 50000
WITH CHECK OPTION;

-- Select from view
SELECT * FROM EmployeeSalaryView ORDER BY salary;

-- UPDATE through view
UPDATE EmployeeSalaryView
SET salary = 72000
WHERE emp_name = 'Rohit Verma';

-- Verify the update through the view
SELECT * FROM EmployeeSalaryView WHERE emp_name = 'Rohit Verma';

-- Verify the update in the base table
SELECT emp_name, salary FROM Employee WHERE emp_name = 'Rohit Verma';

-- INSERT through view (must satisfy WITH CHECK OPTION)
INSERT INTO EmployeeSalaryView (emp_name, department, job_role, salary, dept_id)
VALUES ('Test User', 'IT', 'Tester', 55000.00, 1);

-- This INSERT would FAIL because salary < 50000 (violates WITH CHECK OPTION):
-- INSERT INTO EmployeeSalaryView (emp_name, department, job_role, salary, dept_id)
-- VALUES ('Low Salary', 'IT', 'Tester', 30000.00, 1);

-- DELETE through view
DELETE FROM EmployeeSalaryView WHERE emp_name = 'Test User';

-- Create a non-updatable view (contains aggregation)
CREATE VIEW DeptSalaryStats AS
SELECT department, COUNT(*) AS emp_count, AVG(salary) AS avg_salary
FROM Employee
GROUP BY department;

-- Attempting UPDATE on this view will fail:
-- UPDATE DeptSalaryStats SET avg_salary = 80000 WHERE department = 'IT';
-- Error: VIEW is not updatable

-- DROP VIEW
DROP VIEW IF EXISTS EmployeeSalaryView;
DROP VIEW IF EXISTS DeptSalaryStats;

-- Demonstrate materialized view concept (simulated with a table)
-- Step 1: Create a regular table to act as materialized view
CREATE TABLE DeptSummaryMV AS
SELECT department, COUNT(*) AS emp_count, SUM(salary) AS total_salary
FROM Employee
GROUP BY department;

-- Step 2: Query the materialized view table
SELECT * FROM DeptSummaryMV;

-- Step 3: When data changes, refresh the materialized view
-- (In production, this would be automated with events or triggers)
TRUNCATE TABLE DeptSummaryMV;
INSERT INTO DeptSummaryMV
SELECT department, COUNT(*), SUM(salary)
FROM Employee
GROUP BY department;

-- After refresh
SELECT * FROM DeptSummaryMV;

-- Clean up
DROP TABLE DeptSummaryMV;
```

## Expected Output

```
mysql> SELECT * FROM EmployeeSalaryView ORDER BY salary;
+--------+--------------+------------+------------------+----------+---------+
| emp_id | emp_name     | department | job_role         | salary   | dept_id |
+--------+--------------+------------+------------------+----------+---------+
|      5 | Vikram Singh | HR         | HR Executive     | 50000.00 |       3 |  (included because > 50000, not >=)
...
|      7 | Rohit Verma  | Sales      | Sales Rep        | 60000.00 |       4 |
...
+--------+--------------+------------+------------------+----------+---------+

mysql> -- After UPDATE through view
UPDATE EmployeeSalaryView SET salary = 72000 WHERE emp_name = 'Rohit Verma';
Query OK, 1 row affected (0.01 sec)

mysql> SELECT emp_name, salary FROM Employee WHERE emp_name = 'Rohit Verma';
+-------------+----------+
| emp_name    | salary   |
+-------------+----------+
| Rohit Verma | 72000.00 |
+-------------+----------+
-- The base table was updated through the view

mysql> -- INSERT through view
INSERT INTO EmployeeSalaryView (...) VALUES ('Test User', 'IT', 'Tester', 55000.00, 1);
Query OK, 1 row affected (0.01 sec)

mysql> -- Materialized view simulation
SELECT * FROM DeptSummaryMV;
+------------+-----------+--------------+
| department | emp_count | total_salary |
+------------+-----------+--------------+
| Finance    |         2 |    140000.00 |
| HR         |         2 |    128000.00 |
| IT         |         4 |    390000.00 |
| Sales      |         2 |    150000.00 |
+------------+-----------+--------------+

mysql> -- After TRUNCATE and re-INSERT (refresh)
SELECT * FROM DeptSummaryMV;
+------------+-----------+--------------+
| department | emp_count | total_salary |
+------------+-----------+--------------+
| Finance    |         2 |    140000.00 |
| HR         |         2 |    128000.00 |
| IT         |         4 |    390000.00 |
| Sales      |         2 |    150000.00 |
+------------+-----------+--------------+
```

## Homework / Practice

1. Create an updatable view for the IT department and successfully insert a new IT employee through it.
   <details>
   <summary>Show Answer</summary>
   CREATE VIEW ITEmployeesView AS SELECT emp_id, emp_name, job_role, salary, dept_id FROM Employee WHERE department = 'IT' WITH CHECK OPTION; INSERT INTO ITEmployeesView (emp_name, job_role, salary, dept_id) VALUES ('Suresh Kumar', 'Software Engineer', 82000.00, 1);
   </details>

2. Try to insert a non-IT employee through the same view with WITH CHECK OPTION. Explain the error.
   <details>
   <summary>Show Answer</summary>
   INSERT INTO ITEmployeesView (emp_name, job_role, salary, dept_id) VALUES ('John Doe', 'Accountant', 60000.00, 2); This fails because WITH CHECK OPTION ensures that any INSERT/UPDATE through the view must satisfy the view's WHERE condition (department = 'IT'). Inserting a non-IT employee (dept_id = 2) violates the condition, so MySQL throws a CHECK OPTION FAILED error.
   </details>

3. Create a table that acts as a materialized view for project summary (project name, total hours, employee count). Write a script to refresh it.
   <details>
   <summary>Show Answer</summary>
   CREATE TABLE ProjectSummaryMV AS SELECT p.project_id, p.project_name, SUM(w.hours_worked) AS total_hours, COUNT(w.emp_id) AS employee_count FROM Project p LEFT JOIN Works_On w ON p.project_id = w.project_id GROUP BY p.project_id, p.project_name; -- Refresh script: TRUNCATE TABLE ProjectSummaryMV; INSERT INTO ProjectSummaryMV SELECT p.project_id, p.project_name, SUM(w.hours_worked), COUNT(w.emp_id) FROM Project p LEFT JOIN Works_On w ON p.project_id = w.project_id GROUP BY p.project_id, p.project_name;
   </details>
