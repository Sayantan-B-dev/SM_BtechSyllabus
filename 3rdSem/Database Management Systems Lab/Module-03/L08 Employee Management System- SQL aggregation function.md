# Employee Management System- SQL aggregation function

**Course:** Database Management Systems Lab  
**Module:** 3 | **Lecture:** 8  
**Date:** 07-Sep-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 2  
**Learning Methodology:** Hands-on Experience  
**Reference:** Lab manual

## Lab Objectives

- Use GROUP BY on multiple columns (department, job_role) for detailed aggregation.
- Introduce ROLLUP and CUBE for generating subtotals and grand totals.
- Compute total salary by department and job role with subtotals.

## Theory / Concept

GROUP BY can group by multiple columns, creating a hierarchy of groups. ROLLUP generates subtotals for each level of the grouping hierarchy and a grand total. CUBE generates subtotals for all possible combinations of grouping columns. For example, GROUP BY department, job_role WITH ROLLUP shows total salary per department per role, subtotals per department, and a grand total.

## SQL Code

```sql
USE EmployeeDB;

-- Add job_role data for employees that have NULL
UPDATE Employee SET job_role = 'Software Engineer' WHERE emp_name = 'Ravi Sharma';
UPDATE Employee SET job_role = 'Accountant' WHERE emp_name = 'Amit Joshi';
UPDATE Employee SET job_role = 'HR Executive' WHERE emp_name = 'Vikram Singh';
UPDATE Employee SET job_role = 'Sales Rep' WHERE emp_name = 'Rohit Verma';

-- GROUP BY on single column
SELECT department, COUNT(*) AS emp_count, SUM(salary) AS total_salary
FROM Employee
GROUP BY department;

-- GROUP BY on multiple columns
SELECT department, job_role, COUNT(*) AS emp_count, SUM(salary) AS total_salary
FROM Employee
GROUP BY department, job_role
ORDER BY department, job_role;

-- GROUP BY with ROLLUP (subtotals per department + grand total)
SELECT
    IFNULL(department, 'ALL DEPARTMENTS') AS department,
    IFNULL(job_role, 'ALL ROLES') AS job_role,
    COUNT(*) AS emp_count,
    SUM(salary) AS total_salary
FROM Employee
GROUP BY department, job_role WITH ROLLUP;

-- ROLLUP on single column
SELECT department, SUM(salary) AS total_salary
FROM Employee
GROUP BY department WITH ROLLUP;

-- Using COALESCE for better labels
SELECT
    COALESCE(department, 'Grand Total') AS department,
    SUM(salary) AS total_salary
FROM Employee
GROUP BY department WITH ROLLUP;

-- Average salary by department and job_role
SELECT department, job_role, AVG(salary) AS avg_salary
FROM Employee
GROUP BY department, job_role
ORDER BY department, avg_salary DESC;

-- Department and job_role combinations with employee count
SELECT department, job_role, COUNT(*) AS emp_count
FROM Employee
GROUP BY department, job_role
HAVING COUNT(*) > 1;
```

## Expected Output

```
mysql> SELECT department, job_role, COUNT(*) AS emp_count, SUM(salary) AS total_salary
FROM Employee GROUP BY department, job_role ORDER BY department, job_role;
+------------+------------------+-----------+--------------+
| department | job_role         | emp_count | total_salary |
+------------+------------------+-----------+--------------+
| Finance    | Accountant       |         1 |     55000.00 |
| Finance    | Finance Manager  |         1 |     85000.00 |
| HR         | HR Executive     |         1 |     50000.00 |
| HR         | HR Manager       |         1 |     78000.00 |
| IT         | DevOps Engineer  |         1 |     93000.00 |
| IT         | Senior Developer |         2 |    209500.00 |
| IT         | Software Engineer|         1 |     87500.00 |
| Sales      | Sales Manager    |         1 |     90000.00 |
| Sales      | Sales Rep        |         1 |     60000.00 |
+------------+------------------+-----------+--------------+

mysql> SELECT COALESCE(department, 'Grand Total') AS department, SUM(salary) AS total_salary
FROM Employee GROUP BY department WITH ROLLUP;
+---------------+--------------+
| department    | total_salary |
+---------------+--------------+
| Finance       |    140000.00 |
| HR            |    128000.00 |
| IT            |    390000.00 |
| Sales         |    150000.00 |
| Grand Total   |    808000.00 |
+---------------+--------------+

mysql> -- ROLLUP on two columns shows subtotals
SELECT IFNULL(department, 'ALL') AS dept, IFNULL(job_role, 'ALL') AS role,
       SUM(salary) AS total_salary
FROM Employee GROUP BY department, job_role WITH ROLLUP;
+-------+--------------------+--------------+
| dept  | role               | total_salary |
+-------+--------------------+--------------+
|Finance| Accountant         |     55000.00 |
|Finance| Finance Manager    |     85000.00 |
|Finance| ALL                |    140000.00 |  (subtotal)
|HR     | HR Executive       |     50000.00 |
|HR     | HR Manager         |     78000.00 |
|HR     | ALL                |    128000.00 |  (subtotal)
|IT     | DevOps Engineer    |     93000.00 |
|IT     | Senior Developer   |    209500.00 |
|IT     | Software Engineer  |     87500.00 |
|IT     | ALL                |    390000.00 |  (subtotal)
|Sales  | Sales Manager      |     90000.00 |
|Sales  | Sales Rep          |     60000.00 |
|Sales  | ALL                |    150000.00 |  (subtotal)
|ALL    | ALL                |    808000.00 |  (grand total)
+-------+--------------------+--------------+
```

## Homework / Practice

1. Use GROUP BY WITH ROLLUP on department and job_role to find the count of employees at each level.
   <details>
   <summary>Show Answer</summary>
   SELECT department, job_role, COUNT(*) AS employee_count FROM Employee GROUP BY department, job_role WITH ROLLUP;
   </details>

2. Write a query that shows the minimum, maximum, and average salary for each job_role across all departments.
   <details>
   <summary>Show Answer</summary>
   SELECT job_role, MIN(salary) AS min_salary, MAX(salary) AS max_salary, AVG(salary) AS avg_salary FROM Employee GROUP BY job_role;
   </details>

3. Explain the difference between ROLLUP and CUBE. Write a query simulating CUBE using UNION (since MySQL does not support CUBE natively).
   <details>
   <summary>Show Answer</summary>
   ROLLUP generates subtotals and grand totals for a hierarchy of columns. CUBE generates subtotals for all combinations of columns. Simulating CUBE: SELECT department, job_role, COUNT(*) FROM Employee GROUP BY department, job_role WITH ROLLUP UNION SELECT department, job_role, COUNT(*) FROM Employee GROUP BY job_role, department WITH ROLLUP;
   </details>
