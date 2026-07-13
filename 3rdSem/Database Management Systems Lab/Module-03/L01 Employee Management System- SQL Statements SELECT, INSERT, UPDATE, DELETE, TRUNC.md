# Employee Management System- SQL Statements SELECT, INSERT, UPDATE, DELETE, TRUNCATE, DROP, ALTER

**Course:** Database Management Systems Lab  
**Module:** 3 | **Lecture:** 1  
**Date:** 10-Aug-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 2  
**Learning Methodology:** Hands-on Experience  
**Reference:** Lab manual

## Lab Objectives

- Use aggregate functions COUNT, SUM, AVG, MAX, and MIN on the Employee table.
- Group data using GROUP BY and filter groups using HAVING.
- Compute average salary by department and identify departments with more than 3 employees.

## Theory / Concept

Aggregate functions perform calculations on a set of rows and return a single value. COUNT counts rows, SUM adds values, AVG computes the average, MAX finds the maximum, and MIN finds the minimum. GROUP BY groups rows that have the same values in specified columns. HAVING filters groups after aggregation (WHERE filters before aggregation). The order of execution is: FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY.

## SQL Code

```sql
USE EmployeeDB;

-- Total number of employees
SELECT COUNT(*) AS total_employees FROM Employee;

-- Total salary paid by company
SELECT SUM(salary) AS total_salary_expense FROM Employee;

-- Average salary
SELECT AVG(salary) AS average_salary FROM Employee;

-- Highest and lowest salary
SELECT MAX(salary) AS highest_salary, MIN(salary) AS lowest_salary FROM Employee;

-- Count employees by department
SELECT department, COUNT(*) AS employee_count
FROM Employee
GROUP BY department;

-- Average salary by department
SELECT department, AVG(salary) AS avg_salary
FROM Employee
GROUP BY department;

-- Maximum salary in each department
SELECT department, MAX(salary) AS max_salary
FROM Employee
GROUP BY department;

-- Departments with more than 2 employees
SELECT department, COUNT(*) AS emp_count
FROM Employee
GROUP BY department
HAVING COUNT(*) > 2;

-- Average salary by department with rounded values
SELECT department,
       COUNT(*) AS emp_count,
       ROUND(AVG(salary), 2) AS avg_salary,
       SUM(salary) AS total_salary
FROM Employee
GROUP BY department;

-- Departments where average salary > 70000
SELECT department, AVG(salary) AS avg_salary
FROM Employee
GROUP BY department
HAVING AVG(salary) > 70000;
```

## Expected Output

```
mysql> SELECT COUNT(*) AS total_employees FROM Employee;
+-----------------+
| total_employees |
+-----------------+
|              10 |
+-----------------+

mysql> SELECT AVG(salary) AS average_salary FROM Employee;
+---------------+
| average_salary|
+---------------+
|  79100.000000 |
+---------------+

mysql> SELECT MAX(salary) AS highest_salary, MIN(salary) AS lowest_salary FROM Employee;
+----------------+----------------+
| highest_salary | lowest_salary  |
+----------------+----------------+
|      109500.00 |       50000.00 |
+----------------+----------------+

mysql> SELECT department, COUNT(*) AS employee_count FROM Employee GROUP BY department;
+------------+----------------+
| department | employee_count |
+------------+----------------+
| IT         |              4 |
| Finance    |              2 |
| HR         |              2 |
| Sales      |              2 |
+------------+----------------+

mysql> SELECT department, AVG(salary) AS avg_salary FROM Employee GROUP BY department;
+------------+---------------+
| department | avg_salary    |
+------------+---------------+
| IT         |  97500.000000 |
| Finance    |  70000.000000 |
| HR         |  64000.000000 |
| Sales      |  75000.000000 |
+------------+---------------+

mysql> SELECT department, COUNT(*) AS emp_count FROM Employee GROUP BY department HAVING COUNT(*) > 2;
+------------+-----------+
| department | emp_count |
+------------+-----------+
| IT         |         4 |
+------------+-----------+
```

## Homework / Practice

1. Find the total salary paid to employees in the Sales department.
2. List departments where the total salary expense exceeds 150000.
3. Group employees by job_role and count how many employees hold each role.
