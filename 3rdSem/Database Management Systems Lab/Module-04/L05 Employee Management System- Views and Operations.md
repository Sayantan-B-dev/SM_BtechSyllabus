# Employee Management System- Views and Operations

**Course:** Database Management Systems Lab  
**Module:** 4 | **Lecture:** 5  
**Date:** 05-Oct-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 3  
**Learning Methodology:** Hands-on Experience  
**Reference:** Lab manual

## Lab Objectives

- Create views using CREATE VIEW to simplify complex queries.
- Query data from views as if they were regular tables.
- Use WITH CHECK OPTION to enforce conditions on view modifications.

## Theory / Concept

A view is a virtual table based on the result of a SELECT query. It does not store data physically; it stores the query definition. Views simplify security by restricting access to specific columns or rows. WITH CHECK OPTION ensures that any INSERT or UPDATE through the view satisfies the view's WHERE condition. Views can be used like tables in SELECT, JOIN, and subquery operations.

## SQL Code

```sql
USE EmployeeDB;

-- Create a view for high-salary employees (salary > 90000)
CREATE VIEW HighSalaryEmployees AS
SELECT emp_id, emp_name, department, job_role, salary
FROM Employee
WHERE salary > 90000
WITH CHECK OPTION;

-- Select from the view
SELECT * FROM HighSalaryEmployees ORDER BY salary DESC;

-- Create a view for department summary
CREATE VIEW DepartmentSummary AS
SELECT
    d.dept_id,
    d.dept_name,
    d.location,
    COUNT(e.emp_id) AS employee_count,
    AVG(e.salary) AS average_salary,
    SUM(e.salary) AS total_salary
FROM Department d
LEFT JOIN Employee e ON d.dept_id = e.dept_id
GROUP BY d.dept_id, d.dept_name, d.location;

-- Select from department summary view
SELECT * FROM DepartmentSummary ORDER BY employee_count DESC;

-- Create a view for active project assignments
CREATE VIEW ActiveProjectAssignments AS
SELECT
    e.emp_name,
    p.project_name,
    w.role,
    w.hours_worked,
    p.status
FROM Employee e
INNER JOIN Works_On w ON e.emp_id = w.emp_id
INNER JOIN Project p ON w.project_id = p.project_id
WHERE p.status = 'Active';

-- Select from the view
SELECT * FROM ActiveProjectAssignments;

-- View for IT department employees only
CREATE VIEW ITEmployees AS
SELECT emp_id, emp_name, job_role, salary, hire_date
FROM Employee
WHERE department = 'IT'
WITH CHECK OPTION;

-- Select from IT view
SELECT * FROM ITEmployees;

-- View with renamed columns
CREATE VIEW EmployeeContactInfo AS
SELECT emp_name AS Name, email AS Email, phone AS Phone, department AS Department
FROM Employee;

SELECT * FROM EmployeeContactInfo WHERE Department = 'Finance';

-- Show all views in the database
SHOW FULL TABLES IN EmployeeDB WHERE TABLE_TYPE LIKE 'VIEW';
```

## Expected Output

```
mysql> SELECT * FROM HighSalaryEmployees ORDER BY salary DESC;
+--------+-------------+------------+------------------+----------+
| emp_id | emp_name    | department | job_role         | salary   |
+--------+-------------+------------+------------------+----------+
|      2 | Priya Mehta | IT         | Senior Developer |109500.00 |
|      9 | Karan Patel | IT         | Senior Developer |100000.00 |
+--------+-------------+------------+------------------+----------+
-- Note: Ananya Das (93000) and Neha Agarwal (90000) are excluded because 90000 is not > 90000

mysql> SELECT * FROM DepartmentSummary ORDER BY employee_count DESC;
+---------+-----------+--------------------+----------------+---------------+---------------+ 
| dept_id | dept_name | location           | employee_count | average_salary | total_salary  |
+---------+-----------+--------------------+----------------+---------------+---------------+ 
|       1 | IT        | Tower A, 5th Floor |              4 |  97500.000000  |   390000.00   |
|       2 | Finance   | Tower B, 3rd Floor |              2 |  70000.000000  |   140000.00   |
|       3 | HR        | Tower A, 2nd Floor |              2 |  64000.000000  |   128000.00   |
|       4 | Sales     | Tower C, 1st Floor |              2 |  75000.000000  |   150000.00   |
|       5 | Marketing | Tower B, 1st Floor |              0 |         NULL   |        NULL   |
|       6 | Research  | Tower D, 4th Floor |              0 |         NULL   |        NULL   |
|       7 | Operations| Tower C, 2nd Floor |              0 |         NULL   |        NULL   |
+---------+-----------+--------------------+----------------+---------------+---------------+ 

mysql> SELECT * FROM ActiveProjectAssignments;
+--------------+--------------------------+------------------+--------------+--------+
| emp_name     | project_name             | role             | hours_worked | status |
+--------------+--------------------------+------------------+--------------+--------+
| Ravi Sharma  | ERP System Upgrade       | Developer        |       120.50 | Active |
| Priya Mehta  | ERP System Upgrade       | Tech Lead        |        80.00 | Active |
| Ananya Das   | ERP System Upgrade       | DevOps Engineer  |       100.00 | Active |
| Vikram Singh | Employee Wellness Program| Coordinator      |        35.00 | Active |
| Meera Iyer   | Employee Wellness Program| HR Partner       |        25.00 | Active |
| Rohit Verma  | Sales CRM Implementation | Sales Rep        |        55.00 | Active |
| Neha Agarwal | Sales CRM Implementation | Project Manager   |        70.00 | Active |
+--------------+--------------------------+------------------+--------------+--------+
```

## Homework / Practice

1. Create a view named `SalesHighPerformers` that shows sales employees with salary > 70000. Use WITH CHECK OPTION.
2. Create a view that joins Employee, Department, and Works_On to show a complete employee work profile.
3. Try inserting a record into HighSalaryEmployees with salary = 85000. What happens? Explain why.
