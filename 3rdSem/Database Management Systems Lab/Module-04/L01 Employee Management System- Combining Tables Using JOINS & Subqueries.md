# Employee Management System- Combining Tables Using JOINS & Subqueries

**Course:** Database Management Systems Lab  
**Module:** 4 | **Lecture:** 1  
**Date:** 14-Sep-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 2  
**Learning Methodology:** Hands-on Experience  
**Reference:** Lab manual

## Lab Objectives

- Understand INNER JOIN and its use in combining related tables.
- Join Employee with Department to display employee names along with their department names.
- Write queries that use table aliases for readability.

## Theory / Concept

JOINs combine rows from two or more tables based on a related column. INNER JOIN returns only rows where there is a match in both tables. The syntax is: SELECT columns FROM table1 INNER JOIN table2 ON table1.common_column = table2.common_column. Table aliases (e.g., e for Employee, d for Department) make queries shorter and more readable. Always qualify column names with table aliases when they appear in multiple tables.

## SQL Code

```sql
USE EmployeeDB;

-- Simple INNER JOIN: employee names with department names
SELECT e.emp_name, e.job_role, e.salary, d.dept_name, d.location
FROM Employee e
INNER JOIN Department d ON e.dept_id = d.dept_id
ORDER BY d.dept_name, e.emp_name;

-- INNER JOIN with WHERE filter
SELECT e.emp_name, e.salary, d.dept_name
FROM Employee e
INNER JOIN Department d ON e.dept_id = d.dept_id
WHERE e.salary > 80000
ORDER BY e.salary DESC;

-- INNER JOIN with aggregate
SELECT d.dept_name, COUNT(e.emp_id) AS employee_count, AVG(e.salary) AS avg_salary
FROM Department d
INNER JOIN Employee e ON d.dept_id = e.dept_id
GROUP BY d.dept_name
ORDER BY employee_count DESC;

-- Joining multiple tables (Employee -> Works_On -> Project)
SELECT e.emp_name, p.project_name, w.role, w.hours_worked
FROM Employee e
INNER JOIN Works_On w ON e.emp_id = w.emp_id
INNER JOIN Project p ON w.project_id = p.project_id
ORDER BY e.emp_name;

-- INNER JOIN with three tables including Department
SELECT e.emp_name, d.dept_name, p.project_name, w.hours_worked
FROM Employee e
INNER JOIN Department d ON e.dept_id = d.dept_id
INNER JOIN Works_On w ON e.emp_id = w.emp_id
INNER JOIN Project p ON w.project_id = p.project_id
WHERE p.status = 'Active'
ORDER BY w.hours_worked DESC;

-- Self-contained example with a simpler dataset
SELECT e.emp_name AS employee, d.dept_name AS department, e.salary
FROM Employee e
INNER JOIN Department d ON e.dept_id = d.dept_id
WHERE d.city = 'New York';
```

## Expected Output

```
mysql> SELECT e.emp_name, e.job_role, e.salary, d.dept_name, d.location
FROM Employee e INNER JOIN Department d ON e.dept_id = d.dept_id
ORDER BY d.dept_name, e.emp_name;
+--------------+------------------+----------+-----------+--------------------+
| emp_name     | job_role         | salary   | dept_name | location           |
+--------------+------------------+----------+-----------+--------------------+
| Amit Joshi   | Accountant       | 55000.00 | Finance   | Tower B, 3rd Floor |
| Sneha Kapoor | Finance Manager  | 85000.00 | Finance   | Tower B, 3rd Floor |
| Meera Iyer   | HR Manager       | 78000.00 | HR        | Tower A, 2nd Floor |
| Vikram Singh | HR Executive     | 50000.00 | HR        | Tower A, 2nd Floor |
| Ananya Das   | DevOps Engineer  | 93000.00 | IT        | Tower A, 5th Floor |
| Karan Patel  | Senior Developer |100000.00 | IT        | Tower A, 5th Floor |
| Priya Mehta  | Senior Developer |109500.00 | IT        | Tower A, 5th Floor |
| Ravi Sharma  | Software Engineer| 87500.00 | IT        | Tower A, 5th Floor |
| Neha Agarwal | Sales Manager    | 90000.00 | Sales     | Tower C, 1st Floor |
| Rohit Verma  | Sales Rep        | 60000.00 | Sales     | Tower C, 1st Floor |
+--------------+------------------+----------+-----------+--------------------+

mysql> SELECT d.dept_name, COUNT(e.emp_id) AS employee_count, AVG(e.salary) AS avg_salary
FROM Department d INNER JOIN Employee e ON d.dept_id = e.dept_id
GROUP BY d.dept_name ORDER BY employee_count DESC;
+-----------+----------------+---------------+
| dept_name | employee_count | avg_salary    |
+-----------+----------------+---------------+
| IT        |              4 |  97500.000000 |
| Finance   |              2 |  70000.000000 |
| HR        |              2 |  64000.000000 |
| Sales     |              2 |  75000.000000 |
+-----------+----------------+---------------+

mysql> SELECT e.emp_name, p.project_name, w.role, w.hours_worked
FROM Employee e INNER JOIN Works_On w ON e.emp_id = w.emp_id
INNER JOIN Project p ON w.project_id = p.project_id
ORDER BY e.emp_name;
+--------------+---------------------------+------------------+--------------+
| emp_name     | project_name              | role             | hours_worked |
+--------------+---------------------------+------------------+--------------+
| Ananya Das   | ERP System Upgrade        | DevOps Engineer  |       100.00 |
| Ananya Das   | Data Migration Project    | Cloud Specialist |        40.00 |
| Karan Patel  | Data Migration Project    | Data Analyst     |        90.00 |
...
+--------------+---------------------------+------------------+--------------+
```

## Homework / Practice

1. Write an INNER JOIN query to display all employees along with their department names and the names of projects they are working on.
2. Find the total hours worked by each department on all projects using INNER JOIN and aggregation.
3. Use INNER JOIN to list employees who are working on projects with a budget greater than 100000.
