# Employee Management System Table Creation with Data Types, Constraints, and Indexes

**Course:** Database Management Systems Lab  
**Module:** 2 | **Lecture:** 2  
**Date:** 27-Jul-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 2  
**Learning Methodology:** Hands-on Experience  
**Reference:** Lab manual

## Lab Objectives

- Create a Department table with appropriate constraints and a primary key.
- Add a foreign key in the Employee table referencing Department.
- Create indexes on columns to improve query performance and view them with SHOW INDEX and DESC.

## Theory / Concept

A foreign key establishes a link between two tables -- it references the PRIMARY KEY of another table, ensuring referential integrity. Indexes are database objects that speed up data retrieval operations. A PRIMARY KEY automatically creates a clustered index. Additional indexes can be created on columns frequently used in WHERE clauses or JOIN conditions. SHOW INDEX displays all indexes on a table.

## SQL Code

```sql
USE EmployeeDB;

-- Create Department table
CREATE TABLE Department (
    dept_id INT PRIMARY KEY AUTO_INCREMENT,
    dept_name VARCHAR(100) NOT NULL UNIQUE,
    location VARCHAR(100) NOT NULL,
    manager_id INT,
    budget DECIMAL(12,2) DEFAULT 0.00 CHECK (budget >= 0)
);

-- Insert departments
INSERT INTO Department (dept_name, location, manager_id, budget) VALUES
('IT', 'Tower A, 5th Floor', 2, 500000.00),
('Finance', 'Tower B, 3rd Floor', 4, 350000.00),
('HR', 'Tower A, 2nd Floor', 10, 200000.00),
('Sales', 'Tower C, 1st Floor', 8, 400000.00),
('Marketing', 'Tower B, 1st Floor', NULL, 250000.00);

-- Add dept_id column to Employee table (if not already present)
ALTER TABLE Employee ADD COLUMN dept_id INT;

-- Add foreign key constraint
ALTER TABLE Employee ADD CONSTRAINT fk_employee_dept
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id);

-- Update existing employees to link to departments
UPDATE Employee SET dept_id = 1 WHERE department = 'IT';
UPDATE Employee SET dept_id = 2 WHERE department = 'Finance';
UPDATE Employee SET dept_id = 3 WHERE department = 'HR';
UPDATE Employee SET dept_id = 4 WHERE department = 'Sales';

-- Create indexes for better performance
CREATE INDEX idx_employee_name ON Employee(emp_name);
CREATE INDEX idx_employee_salary ON Employee(salary);
CREATE INDEX idx_employee_dept_id ON Employee(dept_id);
CREATE UNIQUE INDEX idx_employee_email ON Employee(email);

-- Show indexes on Employee table
SHOW INDEX FROM Employee;

-- Describe Employee table with new columns
DESC Employee;

-- Show all departments
SELECT * FROM Department;

-- Show employees with their department IDs
SELECT emp_id, emp_name, department, dept_id FROM Employee;
```

## Expected Output

```
mysql> SHOW INDEX FROM Employee;
+----------+------------+---------------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| Table    | Non_unique | Key_name            | Seq_in_index | Column_name | Collation | Cardinality | Sub_part | Packed | Null | Index_type | Comment | Index_comment |
+----------+------------+---------------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
| employee |          0 | PRIMARY             |            1 | emp_id      | A         |          10 |     NULL | NULL   |      | BTREE      |         |               |
| employee |          0 | email               |            1 | email       | A         |          10 |     NULL | NULL   |      | BTREE      |         |               |
| employee |          0 | phone               |            1 | phone       | A         |          10 |     NULL | NULL   |      | BTREE      |         |               |
| employee |          0 | idx_employee_email  |            1 | email       | A         |          10 |     NULL | NULL   |      | BTREE      |         |               |
| employee |          1 | idx_employee_name   |            1 | emp_name    | A         |          10 |     NULL | NULL   |      | BTREE      |         |               |
| employee |          1 | idx_employee_salary |            1 | salary      | A         |          10 |     NULL | NULL   |      | BTREE      |         |               |
| employee |          1 | idx_employee_dept_id|            1 | dept_id     | A         |          10 |     NULL | NULL   | YES  | BTREE      |         |               |
+----------+------------+---------------------+--------------+-------------+-----------+-------------+----------+--------+------+------------+---------+---------------+
7 rows in set (0.01 sec)

mysql> SELECT * FROM Department;
+---------+-----------+--------------------+------------+-----------+
| dept_id | dept_name | location           | manager_id | budget    |
+---------+-----------+--------------------+------------+-----------+
|       1 | IT        | Tower A, 5th Floor |          2 | 500000.00 |
|       2 | Finance   | Tower B, 3rd Floor |          4 | 350000.00 |
|       3 | HR        | Tower A, 2nd Floor |         10 | 200000.00 |
|       4 | Sales     | Tower C, 1st Floor |          8 | 400000.00 |
|       5 | Marketing | Tower B, 1st Floor |       NULL | 250000.00 |
+---------+-----------+--------------------+------------+-----------+
5 rows in set (0.00 sec)

mysql> SELECT emp_id, emp_name, department, dept_id FROM Employee;
+--------+--------------+------------+---------+
| emp_id | emp_name     | department | dept_id |
+--------+--------------+------------+---------+
|      1 | Ravi Sharma  | IT         |       1 |
|      2 | Priya Mehta  | IT         |       1 |
|      3 | Amit Joshi   | Finance    |       2 |
|      4 | Sneha Kapoor | Finance    |       2 |
|      5 | Vikram Singh | HR         |       3 |
|      6 | Ananya Das   | IT         |       1 |
|      7 | Rohit Verma  | Sales      |       4 |
|      8 | Neha Agarwal | Sales      |       4 |
|      9 | Karan Patel  | IT         |       1 |
|     10 | Meera Iyer   | HR         |       3 |
+--------+--------------+------------+---------+
10 rows in set (0.00 sec)
```

## Homework / Practice

1. Create an index on the `hire_date` column of the Employee table and verify it using SHOW INDEX.
2. Add a foreign key constraint to ensure `manager_id` in Department references `emp_id` in Employee.
3. Drop the `department` column from Employee since we now have `dept_id` referencing Department.
