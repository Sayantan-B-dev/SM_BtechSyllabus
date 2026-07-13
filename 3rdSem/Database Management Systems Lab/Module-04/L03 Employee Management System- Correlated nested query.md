# Employee Management System- Correlated nested query

**Course:** Database Management Systems Lab  
**Module:** 4 | **Lecture:** 3  
**Date:** 28-Sep-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 2  
**Learning Methodology:** Hands-on Experience  
**Reference:** Lab manual

## Lab Objectives

- Understand correlated subqueries where the inner query references the outer query.
- Find employees earning more than the average salary of their own department.
- Use EXISTS with correlated subqueries for existence checks.

## Theory / Concept

A correlated subquery is a subquery that references columns from the outer query. It is evaluated once for each row processed by the outer query. Unlike a simple subquery, a correlated subquery cannot be executed independently. EXISTS with a correlated subquery is efficient for checking whether related rows exist. Performance consideration: correlated subqueries can be slow on large datasets; JOINs often perform better.

## SQL Code

```sql
USE EmployeeDB;

-- Correlated subquery: employees earning more than avg salary of their department
SELECT e1.emp_name, e1.department, e1.salary
FROM Employee e1
WHERE e1.salary > (
    SELECT AVG(e2.salary)
    FROM Employee e2
    WHERE e2.department = e1.department
)
ORDER BY e1.department;

-- Same query with department names from Department table
SELECT e.emp_name, d.dept_name, e.salary
FROM Employee e
INNER JOIN Department d ON e.dept_id = d.dept_id
WHERE e.salary > (
    SELECT AVG(e2.salary)
    FROM Employee e2
    WHERE e2.dept_id = e.dept_id
)
ORDER BY d.dept_name;

-- EXISTS with correlated subquery: employees who are working on at least one project
SELECT e.emp_name, e.department
FROM Employee e
WHERE EXISTS (
    SELECT 1
    FROM Works_On w
    WHERE w.emp_id = e.emp_id
);

-- NOT EXISTS: employees working on NO projects
SELECT e.emp_name, e.department
FROM Employee e
WHERE NOT EXISTS (
    SELECT 1
    FROM Works_On w
    WHERE w.emp_id = e.emp_id
);

-- EXISTS: departments that have at least one employee
SELECT d.dept_name
FROM Department d
WHERE EXISTS (
    SELECT 1
    FROM Employee e
    WHERE e.dept_id = d.dept_id
);

-- NOT EXISTS: departments with no employees
SELECT d.dept_name
FROM Department d
WHERE NOT EXISTS (
    SELECT 1
    FROM Employee e
    WHERE e.dept_id = d.dept_id
);

-- Correlated subquery with HAVING: departments where max salary > 2x min salary
SELECT d.dept_name
FROM Department d
WHERE EXISTS (
    SELECT 1
    FROM Employee e
    WHERE e.dept_id = d.dept_id
    GROUP BY e.dept_id
    HAVING MAX(e.salary) > 2 * MIN(e.salary)
);

-- Correlated: employees who have the highest salary in their department
SELECT e.emp_name, e.department, e.salary
FROM Employee e
WHERE e.salary = (
    SELECT MAX(e2.salary)
    FROM Employee e2
    WHERE e2.department = e.department
)
ORDER BY e.department;
```

## Expected Output

```
mysql> SELECT e1.emp_name, e1.department, e1.salary
FROM Employee e1 WHERE e1.salary > (
    SELECT AVG(e2.salary) FROM Employee e2 WHERE e2.department = e1.department
) ORDER BY e1.department;
+--------------+------------+----------+
| emp_name     | department | salary   |
+--------------+------------+----------+
| Sneha Kapoor | Finance    | 85000.00 |  (above 70000 avg)
| Meera Iyer   | HR         | 78000.00 |  (above 64000 avg)
| Priya Mehta  | IT         |109500.00 |  (above 97500 avg)
| Neha Agarwal | Sales      | 90000.00 |  (above 75000 avg)
+--------------+------------+----------+

mysql> -- Employees working on at least one project (EXISTS)
SELECT e.emp_name, e.department FROM Employee e
WHERE EXISTS (SELECT 1 FROM Works_On w WHERE w.emp_id = e.emp_id);
+--------------+------------+
| emp_name     | department |
+--------------+------------+
| Ravi Sharma  | IT         |
| Priya Mehta  | IT         |
| Amit Joshi   | Finance    |
| Sneha Kapoor | Finance    |
| Vikram Singh | HR         |
| Ananya Das   | IT         |
| Rohit Verma  | Sales      |
| Neha Agarwal | Sales      |
| Karan Patel  | IT         |
| Meera Iyer   | HR         |
+--------------+------------+
-- (All 10 employees are on projects)

mysql> -- Highest salary in each department (correlated subquery)
SELECT e.emp_name, e.department, e.salary
FROM Employee e WHERE e.salary = (
    SELECT MAX(e2.salary) FROM Employee e2 WHERE e2.department = e.department
) ORDER BY e.department;
+--------------+------------+----------+
| emp_name     | department | salary   |
+--------------+------------+----------+
| Sneha Kapoor | Finance    | 85000.00 |
| Meera Iyer   | HR         | 78000.00 |
| Priya Mehta  | IT         |109500.00 |
| Neha Agarwal | Sales      | 90000.00 |
+--------------+------------+----------+
```

## Homework / Practice

1. Write a correlated subquery to find employees who have worked more hours than the average hours of all employees on the same project.
2. Use EXISTS to find all projects that have at least 2 employees assigned.
3. Write a correlated subquery to find employees whose salary is less than the average salary of employees in the same job_role.
