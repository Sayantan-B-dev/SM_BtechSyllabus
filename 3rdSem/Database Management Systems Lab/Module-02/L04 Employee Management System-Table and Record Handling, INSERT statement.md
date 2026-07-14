# Employee Management System-Table and Record Handling, INSERT statement

**Course:** Database Management Systems Lab  
**Module:** 2 | **Lecture:** 4  
**Date:** 03-Aug-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 2  
**Learning Methodology:** Hands-on Experience  
**Reference:** Lab manual

## Lab Objectives

- Use INSERT statement variations: single row, multiple rows, and INSERT INTO ... SELECT.
- Update existing records using UPDATE with WHERE clause.
- Delete records using DELETE with WHERE clause (e.g., delete resigned employees).

## Theory / Concept

The INSERT statement adds new rows to a table. It can insert a single row, multiple rows in one statement, or copy rows from another table using a subquery. UPDATE modifies existing data, and DELETE removes rows. Always use a WHERE clause with UPDATE and DELETE to avoid unintended changes -- omitting WHERE affects all rows. Testing with SELECT before running UPDATE/DELETE is a good practice.

## SQL Code

```sql
USE EmployeeDB;

-- 1. Single row INSERT
INSERT INTO Employee (emp_name, email, phone, department, job_role, salary, hire_date, dept_id)
VALUES ('Sunil Kumar', 'sunil.kumar@company.com', '9000000011', 'IT', 'Junior Developer', 45000.00, '2026-08-01', 1);

-- 2. Multiple rows INSERT
INSERT INTO Department (dept_name, location, budget) VALUES
('Research', 'Tower D, 4th Floor', 300000.00),
('Operations', 'Tower C, 2nd Floor', 180000.00);

-- 3. INSERT INTO ... SELECT (copy employees from Sales department to a new archive table)
CREATE TABLE EmployeeBackup LIKE Employee;
INSERT INTO EmployeeBackup SELECT * FROM Employee WHERE department = 'Sales';

-- 4. UPDATE with WHERE (give 10% raise to IT department employees)
UPDATE Employee
SET salary = salary * 1.10
WHERE dept_id = 1;

-- 5. UPDATE with multiple columns (promote an employee)
UPDATE Employee
SET job_role = 'Senior Developer', salary = 95000.00
WHERE emp_name = 'Karan Patel';

-- 6. DELETE with WHERE (delete resigned employees)
-- First mark an employee as resigned
UPDATE Employee SET status = 'Resigned' WHERE emp_name = 'Sunil Kumar';

-- Now delete all resigned employees
DELETE FROM Employee WHERE status = 'Resigned';

-- 7. Verify the changes
SELECT emp_id, emp_name, department, job_role, salary, status FROM Employee;
SELECT * FROM EmployeeBackup;
```

## Expected Output

```
mysql> SELECT emp_id, emp_name, department, job_role, salary, status FROM Employee;
+--------+--------------+------------+--------------------+----------+--------+
| emp_id | emp_name     | department | job_role           | salary   | status |
+--------+--------------+------------+--------------------+----------+--------+
|      1 | Ravi Sharma  | IT         | Software Engineer  | 82500.00 | Active |
|      2 | Priya Mehta  | IT         | Senior Developer   |104500.00 | Active |
|      3 | Amit Joshi   | Finance    | Accountant         | 55000.00 | Active |
|      4 | Sneha Kapoor | Finance    | Finance Manager    | 85000.00 | Active |
|      5 | Vikram Singh | HR         | HR Executive       | 50000.00 | Active |
|      6 | Ananya Das   | IT         | DevOps Engineer    | 88000.00 | Active |
|      7 | Rohit Verma  | Sales      | Sales Rep          | 60000.00 | Active |
|      8 | Neha Agarwal | Sales      | Sales Manager      | 90000.00 | Active |
|      9 | Karan Patel  | IT         | Senior Developer   | 95000.00 | Active |
|     10 | Meera Iyer   | HR         | HR Manager         | 78000.00 | Active |
+--------+--------------+------------+--------------------+----------+--------+
10 rows in set (0.00 sec)

-- Note: Sunil Kumar was inserted, then marked Resigned, then deleted.
-- IT salaries got 10% raises: Ravi 75000->82500, Priya 95000->104500, Ananya 80000->88000, Karan promoted.
```

## Homework / Practice

1. Insert 3 new employees in the Marketing department in a single INSERT statement.
   <details>
   <summary>Show Answer</summary>
   INSERT INTO employee (emp_name, department, job_role, salary, hire_date) VALUES ('Alice', 'Marketing', 'Executive', 45000, '2024-01-01'), ('Bob', 'Marketing', 'Manager', 65000, '2024-01-15'), ('Charlie', 'Marketing', 'Analyst', 52000, '2024-02-01');
   </details>

2. Update the budget of the IT department to 600000.00.
   <details>
   <summary>Show Answer</summary>
   UPDATE department SET budget = 600000.00 WHERE dept_name = 'IT';
   </details>

3. Delete all employees who were hired before 2019. First use SELECT to verify which employees would be affected.
   <details>
   <summary>Show Answer</summary>
   SELECT * FROM employee WHERE hire_date < '2019-01-01'; DELETE FROM employee WHERE hire_date < '2019-01-01';
   </details>
