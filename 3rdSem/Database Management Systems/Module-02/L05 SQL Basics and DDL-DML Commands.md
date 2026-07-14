# SQL Basics and DDL/DML Commands

**Course:** Database Management Systems  
**Module:** 2 | **Lecture:** 5  
**Date:** 06-Aug-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 2  
**Learning Methodology:** Chalk & Talk  
**Reference:** Korth & Silberschatz Database System Concepts (7th Ed.)

## Introduction to SQL

SQL (Structured Query Language) is the standard language for relational database management. It combines:

- **DDL (Data Definition Language):** CREATE, ALTER, DROP, TRUNCATE -- defines schema
- **DML (Data Manipulation Language):** INSERT, UPDATE, DELETE, SELECT -- manipulates data
- **DCL (Data Control Language):** GRANT, REVOKE -- controls access
- **TCL (Transaction Control Language):** COMMIT, ROLLBACK, SAVEPOINT -- manages transactions

---

## Data Types in SQL

| Data Type | Description | Example |
|-----------|-------------|---------|
| `INT` / `INTEGER` | Whole numbers | `age INT` |
| `VARCHAR(n)` | Variable-length string (max n chars) | `name VARCHAR(50)` |
| `CHAR(n)` | Fixed-length string (padded) | `gender CHAR(1)` |
| `DATE` | Calendar date (YYYY-MM-DD) | `hire_date DATE` |
| `FLOAT` / `REAL` | Floating-point numbers | `salary FLOAT` |
| `DECIMAL(p,s)` | Exact fixed-point (p digits, s decimal) | `price DECIMAL(10,2)` |
| `BOOLEAN` | True/False | `is_active BOOLEAN` |
| `TEXT` | Large variable-length string | `description TEXT` |
| `BLOB` | Binary large object | `photo BLOB` |

---

## DDL: CREATE TABLE

**Syntax:**
```sql
CREATE TABLE table_name (
    column1 datatype constraint,
    column2 datatype constraint,
    ...
    constraint definitions
);
```

### Constraints

| Constraint | Purpose |
|------------|---------|
| `PRIMARY KEY` | Uniquely identifies each row (not null, unique) |
| `FOREIGN KEY` | References a primary key in another table |
| `NOT NULL` | Column cannot have NULL values |
| `UNIQUE` | All values in column must be distinct |
| `CHECK` | Enforces a condition on column values |
| `DEFAULT` | Sets a default value if none provided |

### Example: Creating Tables

```sql
-- Create DEPARTMENT table
CREATE TABLE DEPARTMENT (
    DeptID VARCHAR(5) PRIMARY KEY,
    DName VARCHAR(30) NOT NULL,
    Location VARCHAR(30),
    Budget DECIMAL(12,2) CHECK (Budget >= 0)
);

-- Create EMPLOYEE table with foreign key
CREATE TABLE EMPLOYEE (
    EmpID INT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    DeptID VARCHAR(5),
    Salary DECIMAL(10,2) CHECK (Salary > 0),
    HireDate DATE DEFAULT CURRENT_DATE,
    FOREIGN KEY (DeptID) REFERENCES DEPARTMENT(DeptID)
);
```

---

## DML: INSERT

**Syntax:**
```sql
INSERT INTO table_name (column1, column2, ...)
VALUES (value1, value2, ...);
```

**Example:**
```sql
INSERT INTO DEPARTMENT (DeptID, DName, Location, Budget)
VALUES ('D1', 'IT', 'New York', 500000.00);

INSERT INTO DEPARTMENT
VALUES ('D2', 'HR', 'Chicago', 200000.00);

-- Insert multiple rows
INSERT INTO EMPLOYEE (EmpID, Name, DeptID, Salary)
VALUES
    (101, 'Alice', 'D1', 60000.00),
    (102, 'Bob', 'D2', 45000.00),
    (103, 'Charlie', 'D1', 55000.00);

-- Insert with default value (HireDate uses CURRENT_DATE)
INSERT INTO EMPLOYEE (EmpID, Name, DeptID, Salary)
VALUES (104, 'Diana', 'D1', 70000.00);
```

---

## DML: Basic SELECT

**Syntax:**
```sql
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

**Examples:**
```sql
-- All columns from EMPLOYEE
SELECT * FROM EMPLOYEE;

-- Specific columns
SELECT Name, Salary FROM EMPLOYEE;

-- With WHERE clause
SELECT Name, Salary
FROM EMPLOYEE
WHERE DeptID = 'D1';

-- Using comparison operators
SELECT Name, Salary
FROM EMPLOYEE
WHERE Salary > 50000;
```

---

## DISTINCT and AS Alias

**DISTINCT** removes duplicate rows from the result.

```sql
-- Get unique department IDs
SELECT DISTINCT DeptID FROM EMPLOYEE;

-- Count distinct salaries
SELECT DISTINCT Salary FROM EMPLOYEE;
```

**AS** gives a column or table an alias (temporary name).

```sql
-- Column alias
SELECT Name AS EmployeeName, Salary AS AnnualSalary
FROM EMPLOYEE;

-- Table alias
SELECT e.Name, d.DName
FROM EMPLOYEE AS e, DEPARTMENT AS d
WHERE e.DeptID = d.DeptID;

-- The AS keyword itself is optional
SELECT Name EmployeeName FROM EMPLOYEE;
```

---

## ORDER BY and LIMIT

**ORDER BY** sorts results in ascending (ASC, default) or descending (DESC) order.

```sql
-- Order by salary ascending
SELECT Name, Salary
FROM EMPLOYEE
ORDER BY Salary;

-- Order by salary descending
SELECT Name, Salary
FROM EMPLOYEE
ORDER BY Salary DESC;

-- Multiple sort keys
SELECT Name, DeptID, Salary
FROM EMPLOYEE
ORDER BY DeptID ASC, Salary DESC;
```

**LIMIT** restricts the number of rows returned.

```sql
-- Top 3 highest paid employees
SELECT Name, Salary
FROM EMPLOYEE
ORDER BY Salary DESC
LIMIT 3;

-- Skip first 2, return next 3 (for pagination)
SELECT Name, Salary
FROM EMPLOYEE
ORDER BY Salary DESC
LIMIT 3 OFFSET 2;
```

---

## Comments in SQL

```sql
-- Single-line comment

/*
   Multi-line
   comment
*/
```

---

## Worked Example: Complete Session

```sql
-- Create database
CREATE DATABASE CompanyDB;
USE CompanyDB;

-- Create tables
CREATE TABLE DEPARTMENT (
    DeptID VARCHAR(5) PRIMARY KEY,
    DName VARCHAR(30) NOT NULL,
    Location VARCHAR(30),
    Budget DECIMAL(12,2)
);

CREATE TABLE EMPLOYEE (
    EmpID INT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    DeptID VARCHAR(5),
    Salary DECIMAL(10,2),
    FOREIGN KEY (DeptID) REFERENCES DEPARTMENT(DeptID)
);

-- Insert data
INSERT INTO DEPARTMENT VALUES
    ('D1', 'IT', 'New York', 500000),
    ('D2', 'HR', 'Chicago', 200000),
    ('D3', 'Finance', 'New York', 400000);

INSERT INTO EMPLOYEE VALUES
    (101, 'Alice', 'D1', 60000),
    (102, 'Bob', 'D2', 45000),
    (103, 'Charlie', 'D1', 55000),
    (104, 'Diana', 'D3', 70000),
    (105, 'Eve', 'D1', 48000);

-- Query: Names of employees in IT ordered by salary desc
SELECT Name, Salary
FROM EMPLOYEE
WHERE DeptID = 'D1'
ORDER BY Salary DESC;

-- Result:
-- Alice  | 60000
-- Charlie| 55000
-- Eve    | 48000

-- Query: Department names and their employee count (with alias)
SELECT d.DName AS Department, COUNT(*) AS EmployeeCount
FROM DEPARTMENT d, EMPLOYEE e
WHERE d.DeptID = e.DeptID
GROUP BY d.DName;
```

---

## Practice Problems

1. Write a CREATE TABLE statement for a `STUDENT` table with columns: RollNo (INT, PK), Name (VARCHAR(50), NOT NULL), Age (INT, CHECK >= 18), Major (VARCHAR(30)).
<details>
<summary>Show Answer</summary>
```sql
CREATE TABLE STUDENT (
    RollNo INT PRIMARY KEY,
    Name VARCHAR(50) NOT NULL,
    Age INT CHECK (Age >= 18),
    Major VARCHAR(30)
);
```
</details>

2. Insert three sample students into the STUDENT table.
<details>
<summary>Show Answer</summary>
```sql
INSERT INTO STUDENT VALUES
    (1, 'Ram', 21, 'CS'),
    (2, 'Shyam', 19, 'Math'),
    (3, 'Sita', 22, 'CS');
```
</details>

3. Write a SELECT query to find the names of all students majoring in 'CS', ordered alphabetically.
<details>
<summary>Show Answer</summary>
```sql
SELECT Name FROM STUDENT WHERE Major = 'CS' ORDER BY Name;
```
</details>

4. What is the difference between CHAR(10) and VARCHAR(10)?
<details>
<summary>Show Answer</summary>
CHAR(10) always stores 10 characters (padded with spaces). VARCHAR(10) stores only the actual characters (up to 10), saving space.
</details>

5. Write a query that returns the top 2 oldest students.
<details>
<summary>Show Answer</summary>
```sql
SELECT * FROM STUDENT ORDER BY Age DESC LIMIT 2;
```
</details>

