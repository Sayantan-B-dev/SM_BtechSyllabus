# Employee Management System- SQL aggregation function

**Course:** Database Management Systems Lab  
**Module:** 3 | **Lecture:** 9  
**Date:** 07-Sep-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 2  
**Learning Methodology:** Hands-on Experience  
**Reference:** Lab manual

## Lab Objectives

- Use the HAVING clause with complex conditions involving multiple aggregate functions.
- Write queries with nested aggregations (aggregate of aggregates).
- Identify departments where the average salary is greater than the overall company average.

## Theory / Concept

HAVING filters groups after aggregation. Complex conditions can combine multiple aggregate functions (e.g., COUNT > 2 AND AVG(salary) > 70000). Nested aggregations involve using a subquery that itself contains an aggregate function, such as comparing each department's average salary to the overall average salary computed in a subquery.

## SQL Code

```sql
USE EmployeeDB;

-- HAVING with multiple conditions
SELECT department,
       COUNT(*) AS emp_count,
       AVG(salary) AS avg_salary,
       SUM(salary) AS total_salary
FROM Employee
GROUP BY department
HAVING COUNT(*) >= 2 AND AVG(salary) > 65000
ORDER BY avg_salary DESC;

-- Departments where AVG(salary) > overall AVG(salary)
SELECT department, AVG(salary) AS dept_avg_salary
FROM Employee
GROUP BY department
HAVING AVG(salary) > (SELECT AVG(salary) FROM Employee);

-- Departments with total salary > 10% of company total
SELECT department, SUM(salary) AS dept_total,
       ROUND(SUM(salary) * 100.0 / (SELECT SUM(salary) FROM Employee), 2) AS pct_of_total
FROM Employee
GROUP BY department
HAVING SUM(salary) > (SELECT SUM(salary) FROM Employee) * 0.1;

-- Departments where max salary is at least 2x min salary
SELECT department,
       MIN(salary) AS min_sal,
       MAX(salary) AS max_sal,
       MAX(salary) / MIN(salary) AS ratio
FROM Employee
GROUP BY department
HAVING MAX(salary) >= 2 * MIN(salary);

-- Nested aggregation: find which job roles have above-average salary within their department
SELECT e.department, e.job_role, AVG(e.salary) AS role_avg_salary
FROM Employee e
GROUP BY e.department, e.job_role
HAVING AVG(e.salary) > (
    SELECT AVG(salary) FROM Employee e2 WHERE e2.department = e.department
);

-- HAVING with OR condition
SELECT department,
       COUNT(*) AS emp_count,
       AVG(salary) AS avg_salary
FROM Employee
GROUP BY department
HAVING COUNT(*) > 3 OR AVG(salary) > 75000;

-- Departments with more than 1 distinct job role
SELECT department, COUNT(DISTINCT job_role) AS distinct_roles, COUNT(*) AS emp_count
FROM Employee
GROUP BY department
HAVING COUNT(DISTINCT job_role) > 1;

-- Using HAVING with aggregate on expression
SELECT department,
       SUM(salary) AS total_salary,
       SUM(CASE WHEN salary > 80000 THEN 1 ELSE 0 END) AS high_earners
FROM Employee
GROUP BY department
HAVING SUM(CASE WHEN salary > 80000 THEN 1 ELSE 0 END) > 0;
```

## Expected Output

```
mysql> SELECT department, AVG(salary) AS dept_avg_salary
FROM Employee GROUP BY department
HAVING AVG(salary) > (SELECT AVG(salary) FROM Employee);
+------------+---------------+
| department | dept_avg_salary|
+------------+---------------+
| IT         |  97500.000000 |
| Sales      |  75000.000000 |
+------------+---------------+
-- Company average is ~73700, so IT (97500) and Sales (75000) are above

mysql> SELECT department, MIN(salary) AS min_sal, MAX(salary) AS max_sal,
       MAX(salary) / MIN(salary) AS ratio
FROM Employee GROUP BY department
HAVING MAX(salary) >= 2 * MIN(salary);
+------------+----------+----------+--------+
| department | min_sal  | max_sal  | ratio  |
+------------+----------+----------+--------+
| HR         | 50000.00 | 78000.00 | 1.5600 |
| IT         | 87500.00 |109500.00 | 1.2514 |
| Sales      | 60000.00 | 90000.00 | 1.5000 |
+------------+----------+----------+--------+
-- Finance excluded: 85000/55000 = 1.545, less than 2x

mysql> SELECT department, COUNT(*) AS emp_count, AVG(salary) AS avg_salary
FROM Employee GROUP BY department
HAVING COUNT(*) > 3 OR AVG(salary) > 75000;
+------------+-----------+---------------+
| department | emp_count | avg_salary    |
+------------+-----------+---------------+
| IT         |         4 |  97500.000000 |
| Sales      |         2 |  75000.000000 |
+------------+-----------+---------------+
-- IT has > 3 employees, Sales avg > 75000

mysql> SELECT department, COUNT(DISTINCT job_role) AS distinct_roles, COUNT(*) AS emp_count
FROM Employee GROUP BY department HAVING COUNT(DISTINCT job_role) > 1;
+------------+----------------+-----------+
| department | distinct_roles | emp_count |
+------------+----------------+-----------+
| Finance    |              2 |         2 |
| HR         |              2 |         2 |
| IT         |              3 |         4 |
| Sales      |              2 |         2 |
+------------+----------------+-----------+
```

## Homework / Practice

1. Find departments where the average salary is between 60000 and 90000, and the department has at least 2 employees.
2. Write a nested query that finds employees whose salary is greater than the average salary of all employees in the same job_role.
3. Use HAVING to identify job roles that appear in more than one department.
