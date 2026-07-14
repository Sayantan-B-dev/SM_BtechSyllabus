# Employee Management System Table Creation with Data Types, Constraints, and Indexes

**Course:** Database Management Systems Lab  
**Module:** 2 | **Lecture:** 3  
**Date:** 27-Jul-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 2  
**Learning Methodology:** Hands-on Experience  
**Reference:** Lab manual

## Lab Objectives

- Create Project and Works_On tables to model a many-to-many relationship between employees and projects.
- Implement a composite primary key in the Works_On table.
- Insert sample data and display all tables using SELECT *.

## Theory / Concept

A many-to-many relationship (e.g., employees can work on multiple projects, and projects can have multiple employees) is implemented using a junction table with a composite primary key. A composite primary key consists of two or more columns that together uniquely identify each row. The Works_On table links Employee and Project, storing additional attributes like hours_worked and role.

## SQL Code

```sql
USE EmployeeDB;

-- Create Project table
CREATE TABLE Project (
    project_id INT PRIMARY KEY AUTO_INCREMENT,
    project_name VARCHAR(200) NOT NULL,
    description TEXT,
    start_date DATE NOT NULL,
    end_date DATE,
    budget DECIMAL(12,2),
    dept_id INT,
    status VARCHAR(20) DEFAULT 'Active' CHECK (status IN ('Active', 'Completed', 'On Hold', 'Cancelled')),
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
);

-- Create Works_On table (junction for many-to-many)
CREATE TABLE Works_On (
    emp_id INT NOT NULL,
    project_id INT NOT NULL,
    hours_worked DECIMAL(8,2) DEFAULT 0.00,
    role VARCHAR(50),
    assigned_date DATE DEFAULT (CURRENT_DATE),
    PRIMARY KEY (emp_id, project_id),
    FOREIGN KEY (emp_id) REFERENCES Employee(emp_id) ON DELETE CASCADE,
    FOREIGN KEY (project_id) REFERENCES Project(project_id) ON DELETE CASCADE
);

-- Insert sample projects
INSERT INTO Project (project_name, description, start_date, end_date, budget, dept_id, status) VALUES
('ERP System Upgrade', 'Upgrade the existing ERP system to version 5.0', '2026-01-15', '2026-08-30', 150000.00, 1, 'Active'),
('Financial Audit Q2', 'Quarter 2 financial audit and reconciliation', '2026-04-01', '2026-06-30', 50000.00, 2, 'Completed'),
('Employee Wellness Program', 'Design and implement wellness initiatives', '2026-03-01', '2026-09-30', 30000.00, 3, 'Active'),
('Sales CRM Implementation', 'Deploy new CRM system for sales team', '2026-02-01', '2026-07-31', 120000.00, 4, 'Active'),
('Data Migration Project', 'Migrate legacy data to cloud storage', '2026-05-01', '2026-12-31', 200000.00, 1, 'On Hold');

-- Assign employees to projects
INSERT INTO Works_On (emp_id, project_id, hours_worked, role, assigned_date) VALUES
(1, 1, 120.5, 'Developer', '2026-01-15'),
(2, 1, 80.0, 'Tech Lead', '2026-01-15'),
(3, 2, 45.0, 'Accountant', '2026-04-01'),
(4, 2, 60.0, 'Auditor', '2026-04-01'),
(5, 3, 35.0, 'Coordinator', '2026-03-01'),
(6, 1, 100.0, 'DevOps Engineer', '2026-01-20'),
(6, 5, 40.0, 'Cloud Specialist', '2026-05-01'),
(7, 4, 55.0, 'Sales Rep', '2026-02-01'),
(8, 4, 70.0, 'Project Manager', '2026-02-01'),
(9, 5, 90.0, 'Data Analyst', '2026-05-01'),
(10, 3, 25.0, 'HR Partner', '2026-03-15'),
(10, 5, 30.0, 'HR Liaison', '2026-06-01');

-- Display all tables
SELECT * FROM Department;
SELECT * FROM Employee;
SELECT * FROM Project;
SELECT * FROM Works_On;
```

## Expected Output

```
mysql> SELECT * FROM Project;
+------------+---------------------------+--------------------------------+------------+------------+-----------+---------+-----------+
| project_id | project_name              | description                    | start_date | end_date   | budget   | dept_id | status    |
+------------+---------------------------+--------------------------------+------------+------------+----------+---------+-----------+
|          1 | ERP System Upgrade        | Upgrade the existing ERP...    | 2026-01-15 | 2026-08-30 |150000.00 |       1 | Active    |
|          2 | Financial Audit Q2        | Quarter 2 financial audit...   | 2026-04-01 | 2026-06-30 | 50000.00 |       2 | Completed |
|          3 | Employee Wellness Program | Design and implement...        | 2026-03-01 | 2026-09-30 | 30000.00 |       3 | Active    |
|          4 | Sales CRM Implementation  | Deploy new CRM system...       | 2026-02-01 | 2026-07-31 |120000.00 |       4 | Active    |
|          5 | Data Migration Project    | Migrate legacy data to cloud   | 2026-05-01 | 2026-12-31 |200000.00 |       1 | On Hold   |
+------------+---------------------------+--------------------------------+------------+------------+----------+---------+-----------+
5 rows in set (0.00 sec)

mysql> SELECT * FROM Works_On;
+--------+------------+--------------+------------------+---------------+
| emp_id | project_id | hours_worked | role             | assigned_date |
+--------+------------+--------------+------------------+---------------+
|      1 |          1 |       120.50 | Developer        | 2026-01-15    |
|      2 |          1 |        80.00 | Tech Lead        | 2026-01-15    |
|      3 |          2 |        45.00 | Accountant       | 2026-04-01    |
|      4 |          2 |        60.00 | Auditor          | 2026-04-01    |
|      5 |          3 |        35.00 | Coordinator      | 2026-03-01    |
|      6 |          1 |       100.00 | DevOps Engineer  | 2026-01-20    |
|      6 |          5 |        40.00 | Cloud Specialist | 2026-05-01    |
|      7 |          4 |        55.00 | Sales Rep        | 2026-02-01    |
|      8 |          4 |        70.00 | Project Manager  | 2026-02-01    |
|      9 |          5 |        90.00 | Data Analyst     | 2026-05-01    |
|     10 |          3 |        25.00 | HR Partner       | 2026-03-15    |
|     10 |          5 |        30.00 | HR Liaison       | 2026-06-01    |
+--------+------------+--------------+------------------+---------------+
12 rows in set (0.00 sec)
```

## Homework / Practice

1. Add a new project "AI Chatbot Development" and assign 3 employees to it.
   <details>
   <summary>Show Answer</summary>
   INSERT INTO Project (project_name, status, budget) VALUES ('AI Chatbot Development', 'Active', 150000.00); INSERT INTO Works_On (emp_id, project_id, role, hours_worked) VALUES (1, 2, 'Developer', 20), (2, 2, 'Tester', 15), (3, 2, 'Project Lead', 10);
   </details>

2. Query all employees working on project_id = 1 (ERP System Upgrade) along with their roles and hours worked.
   <details>
   <summary>Show Answer</summary>
   SELECT e.emp_name, w.role, w.hours_worked FROM Employee e INNER JOIN Works_On w ON e.emp_id = w.emp_id WHERE w.project_id = 1;
   </details>

3. Write a query to find the total hours worked by each employee across all projects.
   <details>
   <summary>Show Answer</summary>
   SELECT e.emp_name, SUM(w.hours_worked) AS total_hours FROM Employee e INNER JOIN Works_On w ON e.emp_id = w.emp_id GROUP BY e.emp_name;
   </details>
