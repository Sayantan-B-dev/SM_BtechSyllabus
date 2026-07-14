# Employee Management System- Correlated nested query

**Course:** Database Management Systems Lab  
**Module:** 4 | **Lecture:** 4  
**Date:** 28-Sep-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 2  
**Learning Methodology:** Hands-on Experience  
**Reference:** Lab manual

## Lab Objectives

- Perform self-joins on a table to relate rows within the same table.
- Implement an employee-manager hierarchy using a self-referencing foreign key.
- List employees along with their manager names.

## Theory / Concept

A self-join is a regular join where a table is joined with itself. It is used to compare rows within the same table. Table aliases are required to distinguish the two instances of the table. The Employee table has a manager_id column that references emp_id of another employee, creating a hierarchical relationship. Use a self-join to pair each employee with their manager.

## SQL Code

```sql
USE EmployeeDB;

-- Ensure manager_id references are correct
-- Ravi Sharma (emp_id=1) manages Priya (2), Ananya (6), Karan (9)
-- Amit Joshi (emp_id=3) manages Sneha (4)
-- Vikram Singh (emp_id=5) manages Meera (10)
-- Rohit Verma (emp_id=7) manages Neha (8)

-- Self-join: employee with their manager
SELECT
    e.emp_name AS employee,
    e.job_role AS employee_role,
    m.emp_name AS manager,
    m.job_role AS manager_role
FROM Employee e
LEFT JOIN Employee m ON e.manager_id = m.emp_id
ORDER BY m.emp_name;

-- Employees who are managers (appear in manager_id column)
SELECT DISTINCT m.emp_name AS manager_name, m.job_role AS manager_role
FROM Employee e
INNER JOIN Employee m ON e.manager_id = m.emp_id
ORDER BY m.emp_name;

-- Employees who are NOT managers (no one reports to them)
SELECT e.emp_name, e.job_role
FROM Employee e
WHERE e.emp_id NOT IN (
    SELECT DISTINCT manager_id FROM Employee WHERE manager_id IS NOT NULL
);

-- Count of direct reports per manager
SELECT
    m.emp_name AS manager,
    m.job_role AS manager_role,
    COUNT(e.emp_id) AS direct_reports
FROM Employee e
INNER JOIN Employee m ON e.manager_id = m.emp_id
GROUP BY m.emp_id, m.emp_name, m.job_role
ORDER BY direct_reports DESC;

-- Full hierarchy: employee -> manager -> senior manager (2 levels of self-join)
SELECT
    e.emp_name AS employee,
    m.emp_name AS manager,
    s.emp_name AS senior_manager
FROM Employee e
LEFT JOIN Employee m ON e.manager_id = m.emp_id
LEFT JOIN Employee s ON m.manager_id = s.emp_id
ORDER BY e.emp_name;

-- Self-join with department info
SELECT
    e.emp_name AS employee,
    d1.dept_name AS employee_dept,
    m.emp_name AS manager,
    d2.dept_name AS manager_dept
FROM Employee e
LEFT JOIN Employee m ON e.manager_id = m.emp_id
LEFT JOIN Department d1 ON e.dept_id = d1.dept_id
LEFT JOIN Department d2 ON m.dept_id = d2.dept_id
ORDER BY e.emp_name;

-- Find employees who earn more than their manager
SELECT
    e.emp_name AS employee,
    e.salary AS emp_salary,
    m.emp_name AS manager,
    m.salary AS manager_salary
FROM Employee e
INNER JOIN Employee m ON e.manager_id = m.emp_id
WHERE e.salary > m.salary;
```

## Expected Output

```
mysql> SELECT e.emp_name AS employee, m.emp_name AS manager
FROM Employee e LEFT JOIN Employee m ON e.manager_id = m.emp_id ORDER BY m.emp_name;
+--------------+--------------+
| employee     | manager      |
+--------------+--------------+
| Priya Mehta  | Ravi Sharma  |
| Ananya Das   | Ravi Sharma  |
| Karan Patel  | Ravi Sharma  |
| Sneha Kapoor | Amit Joshi   |
| Meera Iyer   | Vikram Singh |
| Neha Agarwal | Rohit Verma  |
| Ravi Sharma  | NULL         |
| Amit Joshi   | NULL         |
| Vikram Singh | NULL         |
| Rohit Verma  | NULL         |
+--------------+--------------+

mysql> SELECT m.emp_name AS manager, COUNT(e.emp_id) AS direct_reports
FROM Employee e INNER JOIN Employee m ON e.manager_id = m.emp_id
GROUP BY m.emp_name ORDER BY direct_reports DESC;
+--------------+----------------+
| manager      | direct_reports |
+--------------+----------------+
| Ravi Sharma  |              3 |
| Amit Joshi   |              1 |
| Vikram Singh |              1 |
| Rohit Verma  |              1 |
+--------------+----------------+

mysql> -- Two-level hierarchy
SELECT e.emp_name AS employee, m.emp_name AS manager, s.emp_name AS senior_manager
FROM Employee e LEFT JOIN Employee m ON e.manager_id = m.emp_id
LEFT JOIN Employee s ON m.manager_id = s.emp_id ORDER BY e.emp_name;
+--------------+--------------+----------------+
| employee     | manager      | senior_manager |
+--------------+--------------+----------------+
| Amit Joshi   | NULL         | NULL           |
| Ananya Das   | Ravi Sharma  | NULL           |
| Karan Patel  | Ravi Sharma  | NULL           |
| Meera Iyer   | Vikram Singh | NULL           |
| Neha Agarwal | Rohit Verma  | NULL           |
| Priya Mehta  | Ravi Sharma  | NULL           |
| Ravi Sharma  | NULL         | NULL           |
| Rohit Verma  | NULL         | NULL           |
| Sneha Kapoor | Amit Joshi   | NULL           |
| Vikram Singh | NULL         | NULL           |
+--------------+--------------+----------------+
```

## Homework / Practice

1. Add a column `senior_manager_id` to the Employee table and populate it. Then write a three-level self-join query showing employee, manager, and senior manager.
   <details>
   <summary>Show Answer</summary>
   ALTER TABLE Employee ADD COLUMN senior_manager_id INT; UPDATE Employee SET senior_manager_id = NULL; -- In this dataset, no senior managers exist beyond 2 levels, but we can demonstrate the query structure. SELECT e.emp_name AS employee, m.emp_name AS manager, s.emp_name AS senior_manager FROM Employee e LEFT JOIN Employee m ON e.manager_id = m.emp_id LEFT JOIN Employee s ON m.manager_id = s.emp_id ORDER BY e.emp_name;
   </details>

2. Find employees who have the same job_role as their manager.
   <details>
   <summary>Show Answer</summary>
   SELECT e.emp_name AS employee, e.job_role AS emp_role, m.emp_name AS manager, m.job_role AS manager_role FROM Employee e INNER JOIN Employee m ON e.manager_id = m.emp_id WHERE e.job_role = m.job_role;
   </details>

3. Write a query that shows the organizational hierarchy tree using a self-join, sorted by manager name.
   <details>
   <summary>Show Answer</summary>
   SELECT m.emp_name AS manager, e.emp_name AS employee FROM Employee e LEFT JOIN Employee m ON e.manager_id = m.emp_id ORDER BY m.emp_name, e.emp_name;
   </details>
