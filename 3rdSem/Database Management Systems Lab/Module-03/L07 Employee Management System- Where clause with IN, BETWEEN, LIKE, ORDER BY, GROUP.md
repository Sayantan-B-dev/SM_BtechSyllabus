# Employee Management System- Where clause with IN, BETWEEN, LIKE, ORDER BY, GROUP BY and HAVING Clause

**Course:** Database Management Systems Lab  
**Module:** 3 | **Lecture:** 7  
**Date:** 31-Aug-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 2  
**Learning Methodology:** Hands-on Experience  
**Reference:** Lab manual

## Lab Objectives

- Use subqueries with IN, EXISTS, and NOT EXISTS operators.
- Find employees working in departments located in 'New York'.
- Identify employees earning above the average salary of the company.

## Theory / Concept

A subquery is a query nested inside another query. It can be used with IN to check membership, with EXISTS to test for the existence of rows, and with comparison operators. Subqueries can return single values (scalar), a list of values, or a table. EXISTS is often more efficient than IN for large datasets because it stops processing as soon as a match is found.

## SQL Code

```sql
USE EmployeeDB;

-- Add location column to Department and update locations
ALTER TABLE Department ADD COLUMN city VARCHAR(50);
UPDATE Department SET city = 'New York' WHERE dept_name IN ('IT', 'Finance');
UPDATE Department SET city = 'Chicago' WHERE dept_name IN ('HR', 'Sales');
UPDATE Department SET city = 'Boston' WHERE dept_name IN ('Marketing', 'Research');

-- Subquery with IN: employees in departments located in New York
SELECT emp_name, department
FROM Employee
WHERE dept_id IN (
    SELECT dept_id FROM Department WHERE city = 'New York'
);

-- Subquery: employees earning above average salary
SELECT emp_name, salary
FROM Employee
WHERE salary > (
    SELECT AVG(salary) FROM Employee
)
ORDER BY salary DESC;

-- Subquery: departments with at least one employee earning > 90000
SELECT dept_name
FROM Department
WHERE dept_id IN (
    SELECT DISTINCT dept_id FROM Employee WHERE salary > 90000
);

-- EXISTS: find departments that have employees
SELECT dept_name
FROM Department d
WHERE EXISTS (
    SELECT 1 FROM Employee e WHERE e.dept_id = d.dept_id
);

-- NOT EXISTS: find departments with no employees
SELECT dept_name
FROM Department d
WHERE NOT EXISTS (
    SELECT 1 FROM Employee e WHERE e.dept_id = d.dept_id
);

-- Scalar subquery in SELECT: show each employee's salary compared to average
SELECT
    emp_name,
    salary,
    (SELECT AVG(salary) FROM Employee) AS company_avg,
    salary - (SELECT AVG(salary) FROM Employee) AS difference
FROM Employee
ORDER BY difference DESC;

-- Subquery with comparison operator: employees earning more than the highest salary in HR
SELECT emp_name, department, salary
FROM Employee
WHERE salary > (
    SELECT MAX(salary) FROM Employee WHERE department = 'HR'
);

-- Multiple levels of subquery
SELECT emp_name, department
FROM Employee
WHERE dept_id IN (
    SELECT dept_id FROM Department
    WHERE dept_id IN (
        SELECT dept_id FROM Project WHERE budget > 100000
    )
);
```

## Expected Output

```
mysql> SELECT emp_name, department FROM Employee
WHERE dept_id IN (SELECT dept_id FROM Department WHERE city = 'New York');
+--------------+------------+
| emp_name     | department |
+--------------+------------+
| Ravi Sharma  | IT         |
| Priya Mehta  | IT         |
| Amit Joshi   | Finance    |
| Sneha Kapoor | Finance    |
| Ananya Das   | IT         |
| Karan Patel  | IT         |
+--------------+------------+

mysql> SELECT emp_name, salary FROM Employee
WHERE salary > (SELECT AVG(salary) FROM Employee) ORDER BY salary DESC;
+--------------+----------+
| emp_name     | salary   |
+--------------+----------+
| Priya Mehta  |109500.00 |
| Karan Patel  |100000.00 |
| Ananya Das   | 93000.00 |
| Neha Agarwal | 90000.00 |
| Ravi Sharma  | 87500.00 |
| Sneha Kapoor | 85000.00 |
+--------------+----------+

mysql> SELECT emp_name, department, salary FROM Employee
WHERE salary > (SELECT MAX(salary) FROM Employee WHERE department = 'HR');
+--------------+------------+----------+
| emp_name     | department | salary   |
+--------------+------------+----------+
| Ravi Sharma  | IT         | 87500.00 |
| Priya Mehta  | IT         |109500.00 |
| Sneha Kapoor | Finance    | 85000.00 |
| Ananya Das   | IT         | 93000.00 |
| Neha Agarwal | Sales      | 90000.00 |
| Karan Patel  | IT         |100000.00 |
+--------------+------------+----------+
(All employees earning more than 78000, which is max salary in HR)

mysql> -- NOT EXISTS: departments with no employees
SELECT dept_name FROM Department d WHERE NOT EXISTS (SELECT 1 FROM Employee e WHERE e.dept_id = d.dept_id);
+------------+
| dept_name  |
+------------+
| Marketing  |
| Research   |
| Operations |
+------------+
```

## Homework / Practice

1. Write a subquery to find employees who work on projects with a budget greater than 100000 (use the Works_On and Project tables).
2. Use EXISTS to find all departments that have at least one project with 'Active' status.
3. Find employees whose salary is higher than the average salary of their own department (correlated subquery).
