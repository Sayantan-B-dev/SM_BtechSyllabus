# Employee Management System- SQL Statements SELECT, INSERT, UPDATE, DELETE, TRUNCATE, DROP, ALTER

**Course:** Database Management Systems Lab  
**Module:** 2 | **Lecture:** 6  
**Date:** 10-Aug-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 2  
**Learning Methodology:** Hands-on Experience  
**Reference:** Lab manual

## Lab Objectives

- Understand the difference between TRUNCATE and DELETE, and between DROP and TRUNCATE.
- Use SELECT with WHERE, ORDER BY, and LIMIT clauses.
- Use DISTINCT to eliminate duplicate values from query results.

## Theory / Concept

DELETE is a DML command that removes rows one by one and can be rolled back; it can have a WHERE clause. TRUNCATE is a DDL command that removes all rows at once, resets auto-increment counters, and cannot be rolled back in most MySQL configurations. DROP removes the entire table structure and data permanently. SELECT retrieves data; WHERE filters rows, ORDER BY sorts results, LIMIT restricts the number of rows, and DISTINCT returns only unique values.

## SQL Code

```sql
USE EmployeeDB;

-- SELECT with WHERE
SELECT emp_name, department, salary
FROM Employee
WHERE department = 'IT';

-- SELECT with ORDER BY (ascending and descending)
SELECT emp_name, salary
FROM Employee
ORDER BY salary DESC;

-- SELECT with LIMIT (top 3 earners)
SELECT emp_name, salary
FROM Employee
ORDER BY salary DESC
LIMIT 3;

-- SELECT DISTINCT
SELECT DISTINCT department FROM Employee;

-- WHERE with salary range
SELECT emp_name, department, salary
FROM Employee
WHERE salary BETWEEN 50000 AND 80000
ORDER BY salary;

-- Demonstrate DELETE with WHERE (soft approach)
SELECT * FROM Employee WHERE hire_date < '2019-01-01';
-- No matching rows, so DELETE would be safe

-- Demonstrate TRUNCATE vs DELETE
-- Create a temporary table for demonstration
CREATE TABLE TempEmployees AS SELECT * FROM Employee WHERE 1=0;

INSERT INTO TempEmployees SELECT * FROM Employee WHERE dept_id = 2;

SELECT 'Before DELETE', COUNT(*) FROM TempEmployees;

-- DELETE (can be rolled back)
START TRANSACTION;
DELETE FROM TempEmployees WHERE salary < 60000;
SELECT 'After DELETE', COUNT(*) FROM TempEmployees;
ROLLBACK;
SELECT 'After ROLLBACK', COUNT(*) FROM TempEmployees;

-- TRUNCATE (cannot be rolled back effectively)
TRUNCATE TABLE TempEmployees;
SELECT 'After TRUNCATE', COUNT(*) FROM TempEmployees;

-- DROP vs TRUNCATE: DROP removes entire table
DROP TABLE IF EXISTS TempEmployees;
-- Table no longer exists

-- DROP vs TRUNCATE illustration with a new table
CREATE TABLE TestTable (id INT PRIMARY KEY, value VARCHAR(10));
INSERT INTO TestTable VALUES (1, 'A'), (2, 'B');
TRUNCATE TABLE TestTable;  -- Removes all rows, structure remains
INSERT INTO TestTable VALUES (1, 'X');  -- id resets if AUTO_INCREMENT
SELECT * FROM TestTable;
DROP TABLE TestTable;  -- Table is gone entirely
-- SHOW TABLES will no longer show TestTable
```

## Expected Output

```
mysql> SELECT emp_name, department, salary FROM Employee WHERE department = 'IT';
+--------------+------------+----------+
| emp_name     | department | salary   |
+--------------+------------+----------+
| Ravi Sharma  | IT         | 87500.00 |
| Priya Mehta  | IT         |109500.00 |
| Ananya Das   | IT         | 93000.00 |
| Karan Patel  | IT         |100000.00 |
+--------------+------------+----------+

mysql> SELECT emp_name, salary FROM Employee ORDER BY salary DESC LIMIT 3;
+--------------+----------+
| emp_name     | salary   |
+--------------+----------+
| Priya Mehta  |109500.00 |
| Karan Patel  |100000.00 |
| Ananya Das   | 93000.00 |
+--------------+----------+

mysql> SELECT DISTINCT department FROM Employee;
+------------+
| department |
+------------+
| IT         |
| Finance    |
| HR         |
| Sales      |
+------------+

mysql> SELECT emp_name, department, salary FROM Employee WHERE salary BETWEEN 50000 AND 80000;
+--------------+------------+----------+
| emp_name     | department | salary   |
+--------------+------------+----------+
| Vikram Singh | HR         | 50000.00 |
| Amit Joshi   | Finance    | 55000.00 |
| Rohit Verma  | Sales      | 60000.00 |
| Meera Iyer   | HR         | 78000.00 |
+--------------+------------+----------+

-- TRUNCATE vs DELETE demo:
Before DELETE: count = 2 (Finance employees)
After DELETE:  count = 0
After ROLLBACK: count = 2 (DELETE rolled back)
After TRUNCATE: count = 0 (cannot roll back)
```

## Homework / Practice

1. Write a query to display the top 5 highest-paid employees with their names and salaries.
   <details>
   <summary>Show Answer</summary>
   SELECT emp_name, salary FROM Employee ORDER BY salary DESC LIMIT 5;
   </details>

2. Use DISTINCT to find all unique job roles present in the Employee table.
   <details>
   <summary>Show Answer</summary>
   SELECT DISTINCT job_role FROM Employee;
   </details>

3. Explain the difference between TRUNCATE and DELETE in terms of transaction safety and auto-increment reset. Demonstrate by creating a small table with AUTO_INCREMENT and showing the difference.
   <details>
   <summary>Show Answer</summary>
   TRUNCATE is DDL, cannot be rolled back, resets AUTO_INCREMENT counter. DELETE is DML, can be rolled back, does not reset AUTO_INCREMENT. Example: CREATE TABLE Test (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(50)); INSERT INTO Test VALUES (1, 'A'), (2, 'B'); DELETE FROM Test; INSERT INTO Test (name) VALUES ('C'); -- id becomes 3. TRUNCATE TABLE Test; INSERT INTO Test (name) VALUES ('D'); -- id becomes 1.
   </details>
