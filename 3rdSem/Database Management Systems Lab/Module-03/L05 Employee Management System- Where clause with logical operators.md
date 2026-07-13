# Employee Management System- Where clause with logical operators

**Course:** Database Management Systems Lab  
**Module:** 3 | **Lecture:** 5  
**Date:** 24-Aug-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 2  
**Learning Methodology:** Hands-on Experience  
**Reference:** Lab manual

## Lab Objectives

- Use comparison operators: =, <>, >, <, >=, <= in WHERE clauses.
- Use BETWEEN, IN, and IS NULL operators for range and set-based filtering.
- Practice with salary ranges, department lists, and checking for NULL values.

## Theory / Concept

Comparison operators compare values: = (equal), <> (not equal), > (greater), < (less), >= (greater or equal), <= (less or equal). BETWEEN defines a range (inclusive of boundaries). IN checks if a value matches any in a list. IS NULL checks for NULL values (use IS NULL, not = NULL, since NULL is not a value but the absence of a value).

## SQL Code

```sql
USE EmployeeDB;

-- = operator: exact match
SELECT emp_name, department FROM Employee WHERE department = 'IT';

-- <> operator: not equal
SELECT emp_name, department FROM Employee WHERE department <> 'IT';

-- > and < operators: salary comparison
SELECT emp_name, salary FROM Employee WHERE salary > 80000;
SELECT emp_name, salary FROM Employee WHERE salary < 60000;

-- >= and <=
SELECT emp_name, salary FROM Employee WHERE salary >= 50000 AND salary <= 70000;

-- BETWEEN: salary between 50000 and 80000 (inclusive)
SELECT emp_name, department, salary
FROM Employee
WHERE salary BETWEEN 50000 AND 80000
ORDER BY salary;

-- IN: employees in specific departments
SELECT emp_name, department, salary
FROM Employee
WHERE department IN ('IT', 'Finance', 'HR')
ORDER BY department;

-- NOT IN: employees not in these departments
SELECT emp_name, department, salary
FROM Employee
WHERE department NOT IN ('IT', 'Finance');

-- IS NULL: find employees with no manager
SELECT emp_name, department, manager_id
FROM Employee
WHERE manager_id IS NULL;

-- IS NOT NULL: find employees who have a manager
SELECT emp_name, department, manager_id
FROM Employee
WHERE manager_id IS NOT NULL;

-- Combining multiple operators
SELECT emp_name, department, salary
FROM Employee
WHERE salary BETWEEN 60000 AND 100000
  AND department IN ('IT', 'Sales')
ORDER BY salary DESC;
```

## Expected Output

```
mysql> SELECT emp_name, salary FROM Employee WHERE salary > 80000;
+--------------+----------+
| emp_name     | salary   |
+--------------+----------+
| Ravi Sharma  | 87500.00 |
| Priya Mehta  |109500.00 |
| Ananya Das   | 93000.00 |
| Karan Patel  |100000.00 |
| Sneha Kapoor | 85000.00 |
| Neha Agarwal | 90000.00 |
+--------------+----------+

mysql> SELECT emp_name, department, salary
FROM Employee WHERE salary BETWEEN 50000 AND 80000 ORDER BY salary;
+--------------+------------+----------+
| emp_name     | department | salary   |
+--------------+------------+----------+
| Vikram Singh | HR         | 50000.00 |
| Amit Joshi   | Finance    | 55000.00 |
| Rohit Verma  | Sales      | 60000.00 |
| Meera Iyer   | HR         | 78000.00 |
+--------------+------------+----------+

mysql> SELECT emp_name, department, salary
FROM Employee WHERE department IN ('IT', 'Finance', 'HR') ORDER BY department;
+--------------+------------+----------+
| emp_name     | department | salary   |
+--------------+------------+----------+
| Amit Joshi   | Finance    | 55000.00 |
| Sneha Kapoor | Finance    | 85000.00 |
| Vikram Singh | HR         | 50000.00 |
| Meera Iyer   | HR         | 78000.00 |
| Ravi Sharma  | IT         | 87500.00 |
| Priya Mehta  | IT         |109500.00 |
| Ananya Das   | IT         | 93000.00 |
| Karan Patel  | IT         |100000.00 |
+--------------+------------+----------+

mysql> SELECT emp_name, department, manager_id
FROM Employee WHERE manager_id IS NULL;
+--------------+------------+------------+
| emp_name     | department | manager_id |
+--------------+------------+------------+
| Ravi Sharma  | IT         |       NULL |
| Amit Joshi   | Finance    |       NULL |
| Vikram Singh | HR         |       NULL |
| Rohit Verma  | Sales      |       NULL |
+--------------+------------+------------+
```

## Homework / Practice

1. Find all employees whose salary is NOT between 40000 and 70000 (use NOT BETWEEN).
2. Find employees whose job_role is in ('Developer', 'Manager', 'Analyst') but not in the HR department.
3. List all employees who have a manager (manager_id IS NOT NULL) and earn more than 75000.
