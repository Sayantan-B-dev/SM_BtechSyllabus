# Creating a college Database, Creating a Student Table, Specifying Relational Data Types, Specifying Constraints, and Creating Indices.

**Course:** Database Management Systems Lab  
**Module:** 2 | **Lecture:** 1  
**Date:** 20-Jul-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 2  
**Learning Methodology:** Hands-on Experience  
**Reference:** Lab manual

## Lab Objectives

- Create an Employee Management database with an Employee table using appropriate data types and constraints.
- Implement NOT NULL, UNIQUE, and PRIMARY KEY constraints.
- Insert 10 sample employee records and verify with SELECT queries.

## Theory / Concept

Data types define the kind of data a column can hold (INT, VARCHAR, DATE, DECIMAL, etc.). Constraints enforce rules at the table level: NOT NULL ensures a column cannot have NULL values, UNIQUE ensures all values in a column are distinct, and PRIMARY KEY uniquely identifies each row (combining NOT NULL and UNIQUE). Choosing appropriate data types and constraints is critical for data integrity and efficient storage.

## SQL Code

```sql
-- Create Employee Management database
CREATE DATABASE EmployeeDB;
USE EmployeeDB;

-- Create Employee table with appropriate constraints
CREATE TABLE Employee (
    emp_id INT PRIMARY KEY AUTO_INCREMENT,
    emp_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15) UNIQUE,
    department VARCHAR(50) NOT NULL,
    job_role VARCHAR(50),
    salary DECIMAL(10,2) NOT NULL CHECK (salary > 0),
    hire_date DATE NOT NULL DEFAULT (CURRENT_DATE),
    manager_id INT,
    status VARCHAR(20) DEFAULT 'Active' CHECK (status IN ('Active', 'Resigned', 'Terminated'))
);

-- Describe the table structure
DESC Employee;

-- Insert 10 sample employees
INSERT INTO Employee (emp_name, email, phone, department, job_role, salary, hire_date, manager_id) VALUES
('Ravi Sharma', 'ravi.sharma@company.com', '9000000001', 'IT', 'Software Engineer', 75000.00, '2020-06-15', NULL),
('Priya Mehta', 'priya.mehta@company.com', '9000000002', 'IT', 'Senior Developer', 95000.00, '2018-03-01', 1),
('Amit Joshi', 'amit.joshi@company.com', '9000000003', 'Finance', 'Accountant', 55000.00, '2021-09-10', NULL),
('Sneha Kapoor', 'sneha.kapoor@company.com', '9000000004', 'Finance', 'Finance Manager', 85000.00, '2019-01-20', 3),
('Vikram Singh', 'vikram.singh@company.com', '9000000005', 'HR', 'HR Executive', 50000.00, '2022-04-05', NULL),
('Ananya Das', 'ananya.das@company.com', '9000000006', 'IT', 'DevOps Engineer', 80000.00, '2020-11-12', 1),
('Rohit Verma', 'rohit.verma@company.com', '9000000007', 'Sales', 'Sales Representative', 60000.00, '2021-07-22', NULL),
('Neha Agarwal', 'neha.agarwal@company.com', '9000000008', 'Sales', 'Sales Manager', 90000.00, '2017-05-30', 7),
('Karan Patel', 'karan.patel@company.com', '9000000009', 'IT', 'Data Analyst', 70000.00, '2022-01-18', 1),
('Meera Iyer', 'meera.iyer@company.com', '9000000010', 'HR', 'HR Manager', 78000.00, '2019-08-14', 5);

-- View all employee records
SELECT * FROM Employee;
```

## Expected Output

```
mysql> DESC Employee;
+-------------+--------------+------+-----+------------+----------------+
| Field       | Type         | Null | Key | Default    | Extra          |
+-------------+--------------+------+-----+------------+----------------+
| emp_id      | int          | NO   | PRI | NULL       | auto_increment |
| emp_name    | varchar(100) | NO   |     | NULL       |                |
| email       | varchar(100) | NO   | UNI | NULL       |                |
| phone       | varchar(15)  | YES  | UNI | NULL       |                |
| department  | varchar(50)  | NO   |     | NULL       |                |
| job_role    | varchar(50)  | YES  |     | NULL       |                |
| salary      | decimal(10,2)| NO   |     | NULL       |                |
| hire_date   | date         | NO   |     | curdate()  |                |
| manager_id  | int          | YES  |     | NULL       |                |
| status      | varchar(20)  | YES  |     | Active     |                |
+-------------+--------------+------+-----+------------+----------------+
10 rows in set (0.01 sec)

mysql> SELECT * FROM Employee;
+--------+--------------+------------------------+------------+------------+--------------------+----------+------------+------------+--------+
| emp_id | emp_name     | email                  | phone      | department | job_role           | salary   | hire_date  | manager_id | status |
+--------+--------------+------------------------+------------+------------+--------------------+----------+------------+------------+--------+
|      1 | Ravi Sharma  | ravi.sharma@company.com| 9000000001 | IT         | Software Engineer   | 75000.00 | 2020-06-15 |       NULL | Active |
|      2 | Priya Mehta  | priya.mehta@company.com| 9000000002 | IT         | Senior Developer    | 95000.00 | 2018-03-01 |          1 | Active |
|      3 | Amit Joshi   | amit.joshi@company.com | 9000000003 | Finance    | Accountant          | 55000.00 | 2021-09-10 |       NULL | Active |
|      4 | Sneha Kapoor | sneha.kapoor@company.com|9000000004 | Finance    | Finance Manager     | 85000.00 | 2019-01-20 |          3 | Active |
|      5 | Vikram Singh | vikram.singh@company.com|9000000005 | HR         | HR Executive        | 50000.00 | 2022-04-05 |       NULL | Active |
|      6 | Ananya Das   | ananya.das@company.com | 9000000006 | IT         | DevOps Engineer     | 80000.00 | 2020-11-12 |          1 | Active |
|      7 | Rohit Verma  | rohit.verma@company.com| 9000000007 | Sales      | Sales Representative| 60000.00 | 2021-07-22 |       NULL | Active |
|      8 | Neha Agarwal | neha.agarwal@company.com|9000000008 | Sales      | Sales Manager       | 90000.00 | 2017-05-30 |          7 | Active |
|      9 | Karan Patel  | karan.patel@company.com | 9000000009 | IT         | Data Analyst        | 70000.00 | 2022-01-18 |          1 | Active |
|     10 | Meera Iyer   | meera.iyer@company.com  | 9000000010 | HR         | HR Manager          | 78000.00 | 2019-08-14 |          5 | Active |
+--------+--------------+------------------------+------------+------------+--------------------+----------+------------+------------+--------+
10 rows in set (0.00 sec)
```

## Homework / Practice

1. Add a CHECK constraint to ensure salary is between 30000 and 200000 using ALTER TABLE.
2. Insert 2 more employees in the 'Marketing' department with appropriate values.
3. Write a query to display only emp_name, department, and salary of all employees sorted by salary in descending order.
