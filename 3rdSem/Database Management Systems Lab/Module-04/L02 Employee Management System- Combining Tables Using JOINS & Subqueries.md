# Employee Management System- Combining Tables Using JOINS & Subqueries

**Course:** Database Management Systems Lab  
**Module:** 4 | **Lecture:** 2  
**Date:** 14-Sep-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 2  
**Learning Methodology:** Hands-on Experience  
**Reference:** Lab manual

## Lab Objectives

- Use LEFT JOIN and RIGHT JOIN to include non-matching rows from one table.
- Simulate FULL OUTER JOIN in MySQL using UNION.
- Examples: all departments even those without employees, all employees even without departments.

## Theory / Concept

LEFT JOIN returns all rows from the left table and matching rows from the right table; non-matching right side columns are NULL. RIGHT JOIN is the opposite. FULL OUTER JOIN returns all rows from both tables (not supported natively in MySQL, but simulated using LEFT JOIN UNION RIGHT JOIN). These are useful when you need to see all records from one table regardless of whether they have matches in the other.

## SQL Code

```sql
USE EmployeeDB;

-- LEFT JOIN: all departments, even those with no employees
SELECT d.dept_name, d.location, e.emp_name, e.job_role
FROM Department d
LEFT JOIN Employee e ON d.dept_id = e.dept_id
ORDER BY d.dept_name;

-- RIGHT JOIN: all employees, even those without a valid dept_id (if any)
SELECT e.emp_name, d.dept_name, d.location
FROM Department d
RIGHT JOIN Employee e ON d.dept_id = e.dept_id
ORDER BY e.emp_name;

-- LEFT JOIN with aggregate: department employee counts including zero
SELECT d.dept_name, COUNT(e.emp_id) AS employee_count
FROM Department d
LEFT JOIN Employee e ON d.dept_id = e.dept_id
GROUP BY d.dept_name
ORDER BY employee_count DESC;

-- FULL OUTER JOIN simulation using UNION
-- All departments and all employees, matched where possible
SELECT d.dept_name, e.emp_name
FROM Department d
LEFT JOIN Employee e ON d.dept_id = e.dept_id
UNION
SELECT d.dept_name, e.emp_name
FROM Department d
RIGHT JOIN Employee e ON d.dept_id = e.dept_id
ORDER BY dept_name, emp_name;

-- LEFT JOIN: projects and their assigned employees (projects with no assignments)
SELECT p.project_name, p.status, e.emp_name, w.role
FROM Project p
LEFT JOIN Works_On w ON p.project_id = w.project_id
LEFT JOIN Employee e ON w.emp_id = e.emp_id
ORDER BY p.project_name;

-- LEFT JOIN with WHERE: departments with no employees
SELECT d.dept_name, d.location
FROM Department d
LEFT JOIN Employee e ON d.dept_id = e.dept_id
WHERE e.emp_id IS NULL;

-- RIGHT JOIN: all employees with department info (even if department is missing)
SELECT e.emp_name, e.department, d.dept_name, d.location
FROM Department d
RIGHT JOIN Employee e ON d.dept_id = e.dept_id;

-- FULL OUTER JOIN with a WHERE to find orphaned records
SELECT d.dept_name AS department, e.emp_name AS employee
FROM Department d
LEFT JOIN Employee e ON d.dept_id = e.dept_id
WHERE e.emp_id IS NULL
UNION
SELECT d.dept_name, e.emp_name
FROM Department d
RIGHT JOIN Employee e ON d.dept_id = e.dept_id
WHERE d.dept_id IS NULL;
```

## Expected Output

```
mysql> SELECT d.dept_name, d.location, e.emp_name, e.job_role
FROM Department d LEFT JOIN Employee e ON d.dept_id = e.dept_id ORDER BY d.dept_name;
+-----------+--------------------+--------------+------------------+
| dept_name | location           | emp_name     | job_role         |
+-----------+--------------------+--------------+------------------+
| Finance   | Tower B, 3rd Floor | Amit Joshi   | Accountant       |
| Finance   | Tower B, 3rd Floor | Sneha Kapoor | Finance Manager  |
| HR        | Tower A, 2nd Floor | Meera Iyer   | HR Manager       |
| HR        | Tower A, 2nd Floor | Vikram Singh | HR Executive     |
| IT        | Tower A, 5th Floor | Ananya Das   | DevOps Engineer  |
| IT        | Tower A, 5th Floor | Karan Patel  | Senior Developer |
| IT        | Tower A, 5th Floor | Priya Mehta  | Senior Developer |
| IT        | Tower A, 5th Floor | Ravi Sharma  | Software Engineer|
| Marketing | Tower B, 1st Floor | NULL         | NULL             |
| Operations| Tower C, 2nd Floor | NULL         | NULL             |
| Research  | Tower D, 4th Floor | NULL         | NULL             |
+-----------+--------------------+--------------+------------------+

mysql> SELECT d.dept_name, COUNT(e.emp_id) AS employee_count
FROM Department d LEFT JOIN Employee e ON d.dept_id = e.dept_id
GROUP BY d.dept_name ORDER BY employee_count DESC;
+-----------+----------------+
| dept_name | employee_count |
+-----------+----------------+
| IT        |              4 |
| Finance   |              2 |
| HR        |              2 |
| Sales     |              2 |
| Marketing |              0 |
| Operations|              0 |
| Research  |              0 |
+-----------+----------------+

mysql> -- Departments with no employees
SELECT d.dept_name, d.location FROM Department d
LEFT JOIN Employee e ON d.dept_id = e.dept_id WHERE e.emp_id IS NULL;
+-----------+--------------------+
| dept_name | location           |
+-----------+--------------------+
| Marketing | Tower B, 1st Floor |
| Operations| Tower C, 2nd Floor |
| Research  | Tower D, 4th Floor |
+-----------+--------------------+
```

## Homework / Practice

1. Use LEFT JOIN to list all projects and the employees assigned to them. Include projects with no employees assigned.
   <details>
   <summary>Show Answer</summary>
   SELECT p.project_name, p.status, e.emp_name, w.role FROM Project p LEFT JOIN Works_On w ON p.project_id = w.project_id LEFT JOIN Employee e ON w.emp_id = e.emp_id ORDER BY p.project_name;
   </details>

2. Write a FULL OUTER JOIN query (using UNION) to find all employees and all projects, showing which employees are assigned to which projects.
   <details>
   <summary>Show Answer</summary>
   SELECT e.emp_name, p.project_name FROM Employee e LEFT JOIN Works_On w ON e.emp_id = w.emp_id LEFT JOIN Project p ON w.project_id = p.project_id UNION SELECT e.emp_name, p.project_name FROM Employee e RIGHT JOIN Works_On w ON e.emp_id = w.emp_id RIGHT JOIN Project p ON w.project_id = p.project_id ORDER BY emp_name, project_name;
   </details>

3. Identify any employees who are not assigned to any project using a LEFT JOIN with a WHERE IS NULL condition.
   <details>
   <summary>Show Answer</summary>
   SELECT e.emp_id, e.emp_name, e.department FROM Employee e LEFT JOIN Works_On w ON e.emp_id = w.emp_id WHERE w.project_id IS NULL;
   </details>
