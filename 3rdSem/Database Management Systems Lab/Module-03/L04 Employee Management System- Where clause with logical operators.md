# Employee Management System- Where clause with logical operators

**Course:** Database Management Systems Lab  
**Module:** 3 | **Lecture:** 4  
**Date:** 24-Aug-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 2  
**Learning Methodology:** Hands-on Experience  
**Reference:** Lab manual

## Lab Objectives

- Use logical operators AND, OR, and NOT in WHERE clauses.
- Combine multiple conditions to filter employee records precisely.
- Examples: employees in IT AND salary > 50000, employees in Finance OR Sales.

## Theory / Concept

Logical operators combine multiple conditions in a WHERE clause. AND returns rows when all conditions are true. OR returns rows when at least one condition is true. NOT negates a condition. Operator precedence: NOT is evaluated first, then AND, then OR. Use parentheses to override the default precedence and make conditions clear.

## SQL Code

```sql
USE EmployeeDB;

-- AND: Employees in IT department AND salary greater than 90000
SELECT emp_name, department, salary
FROM Employee
WHERE department = 'IT' AND salary > 90000;

-- OR: Employees in Finance OR Sales department
SELECT emp_name, department, salary
FROM Employee
WHERE department = 'Finance' OR department = 'Sales';

-- AND + OR combination: IT employees with high salary OR any HR employee
SELECT emp_name, department, salary
FROM Employee
WHERE (department = 'IT' AND salary > 80000) OR department = 'HR';

-- NOT: Employees NOT in IT department
SELECT emp_name, department, salary
FROM Employee
WHERE NOT department = 'IT';

-- NOT with AND: Employees who are NOT in IT AND have salary > 70000
SELECT emp_name, department, salary
FROM Employee
WHERE NOT department = 'IT' AND salary > 70000;

-- Using parentheses for clarity
SELECT emp_name, department, salary
FROM Employee
WHERE (department = 'IT' OR department = 'Finance') AND salary > 75000;

-- Complex condition: employees with salary > 60000 AND (dept IT OR dept Sales)
SELECT emp_name, department, salary
FROM Employee
WHERE salary > 60000 AND (department = 'IT' OR department = 'Sales');

-- NOT with multiple conditions
SELECT emp_name, department, salary
FROM Employee
WHERE NOT (department = 'HR' OR department = 'Finance');
```

## Expected Output

```
mysql> SELECT emp_name, department, salary
FROM Employee WHERE department = 'IT' AND salary > 90000;
+-------------+------------+----------+
| emp_name    | department | salary   |
+-------------+------------+----------+
| Priya Mehta | IT         |109500.00 |
| Karan Patel | IT         |100000.00 |
+-------------+------------+----------+

mysql> SELECT emp_name, department, salary
FROM Employee WHERE department = 'Finance' OR department = 'Sales';
+--------------+------------+----------+
| emp_name     | department | salary   |
+--------------+------------+----------+
| Amit Joshi   | Finance    | 55000.00 |
| Sneha Kapoor | Finance    | 85000.00 |
| Rohit Verma  | Sales      | 60000.00 |
| Neha Agarwal | Sales      | 90000.00 |
+--------------+------------+----------+

mysql> SELECT emp_name, department, salary
FROM Employee WHERE (department = 'IT' AND salary > 80000) OR department = 'HR';
+--------------+------------+----------+
| emp_name     | department | salary   |
+--------------+------------+----------+
| Ravi Sharma  | IT         | 87500.00 |
| Priya Mehta  | IT         |109500.00 |
| Ananya Das   | IT         | 93000.00 |
| Karan Patel  | IT         |100000.00 |
| Vikram Singh | HR         | 50000.00 |
| Meera Iyer   | HR         | 78000.00 |
+--------------+------------+----------+

mysql> SELECT emp_name, department, salary
FROM Employee WHERE NOT (department = 'HR' OR department = 'Finance');
+--------------+------------+----------+
| emp_name     | department | salary   |
+--------------+------------+----------+
| Ravi Sharma  | IT         | 87500.00 |
| Priya Mehta  | IT         |109500.00 |
| Ananya Das   | IT         | 93000.00 |
| Karan Patel  | IT         |100000.00 |
| Rohit Verma  | Sales      | 60000.00 |
| Neha Agarwal | Sales      | 90000.00 |
+--------------+------------+----------+
```

## Homework / Practice

1. Find all employees who are in the IT department OR have a salary greater than 80000.
2. Find employees who are NOT in Sales and have a salary less than 70000.
3. Write a query to find all employees who are in IT or Finance, AND were hired after 2020-01-01.
