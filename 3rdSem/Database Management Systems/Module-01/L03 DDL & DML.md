# DDL & DML

**Course:** Database Management Systems  
**Module:** 1 | **Lecture:** 3  
**Date:** 14-Jul-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 1  
**Learning Methodology:** Chalk & Talk  
**Reference:** Korth & Silberschatz Database System Concepts (7th Ed.)

## Notes

### Overview of SQL Sublanguages

SQL (Structured Query Language) is divided into several sublanguages. The two most fundamental are:

1. **DDL (Data Definition Language)** -- Used to define and modify database structure.
2. **DML (Data Manipulation Language)** -- Used to manipulate data within the existing structure.

Other sublanguages include:
- **DCL (Data Control Language)**: GRANT, REVOKE.
- **TCL (Transaction Control Language)**: COMMIT, ROLLBACK, SAVEPOINT.

---

### Data Definition Language (DDL)

DDL statements define, modify, and remove database objects (tables, indexes, views, schemas, users).

#### 1. CREATE

Creates a new database object.

**Syntax:**
```sql
CREATE TABLE table_name (
    column1 datatype constraint,
    column2 datatype constraint,
    ...
    table_constraints
);
```

**Example -- Creating a University Database Schema:**

```sql
CREATE DATABASE University;

CREATE TABLE Department (
    dept_id      CHAR(4) PRIMARY KEY,
    dept_name    VARCHAR(50) NOT NULL,
    building     VARCHAR(30),
    budget       DECIMAL(12,2) CHECK (budget >= 0)
);

CREATE TABLE Student (
    student_id   CHAR(9) PRIMARY KEY,
    name         VARCHAR(50) NOT NULL,
    dept_id      CHAR(4),
    tot_cred     INT DEFAULT 0,
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
);

CREATE TABLE Course (
    course_id    CHAR(8) PRIMARY KEY,
    title        VARCHAR(100) NOT NULL,
    dept_id      CHAR(4),
    credits      INT CHECK (credits > 0 AND credits <= 5),
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
);

CREATE TABLE Instructor (
    instructor_id CHAR(5) PRIMARY KEY,
    name          VARCHAR(50) NOT NULL,
    dept_id       CHAR(4),
    salary        DECIMAL(10,2),
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
);

CREATE TABLE Section (
    section_id    INT PRIMARY KEY,
    course_id     CHAR(8),
    semester      VARCHAR(6) CHECK (semester IN ('Fall', 'Spring', 'Summer')),
    year          INT,
    room_number   VARCHAR(10),
    FOREIGN KEY (course_id) REFERENCES Course(course_id)
);

CREATE TABLE Takes (
    student_id    CHAR(9),
    section_id    INT,
    grade         CHAR(2),
    PRIMARY KEY (student_id, section_id),
    FOREIGN KEY (student_id) REFERENCES Student(student_id),
    FOREIGN KEY (section_id) REFERENCES Section(section_id)
);
```

**Other CREATE statements:**
```sql
-- Create an index
CREATE INDEX idx_student_name ON Student(name);

-- Create a view
CREATE VIEW CS_Students AS
SELECT student_id, name FROM Student WHERE dept_id = 'CS';

-- Create a sequence (auto-increment)
CREATE SEQUENCE student_seq START WITH 1000 INCREMENT BY 1;
```

#### 2. ALTER

Modifies an existing database object.

**Examples:**
```sql
-- Add a new column
ALTER TABLE Student ADD COLUMN email VARCHAR(100);

-- Modify a column's datatype
ALTER TABLE Student MODIFY COLUMN name VARCHAR(100);

-- Rename a column (MySQL/PostgreSQL syntax varies)
ALTER TABLE Student RENAME COLUMN tot_cred TO total_credits;

-- Add a constraint
ALTER TABLE Student ADD CONSTRAINT chk_age CHECK (age >= 16);

-- Drop a constraint
ALTER TABLE Student DROP CONSTRAINT chk_age;

-- Add a default value
ALTER TABLE Student ALTER COLUMN dept_id SET DEFAULT 'GEN';
```

#### 3. DROP

Completely removes a database object (structure and data).

```sql
-- Drop a table (with all data)
DROP TABLE Takes;

-- Drop with CASCADE (drops dependent objects too)
DROP TABLE Department CASCADE;

-- Drop a view
DROP VIEW CS_Students;

-- Drop an index
DROP INDEX idx_student_name;

-- Drop the entire database
DROP DATABASE University;
```

**WARNING:** `DROP` is irreversible. Use with extreme care in production.

#### 4. TRUNCATE

Removes **all rows** from a table but keeps the table structure intact.

```sql
TRUNCATE TABLE TemporaryData;
```

**Difference between DROP and TRUNCATE:**

| Aspect | DROP | TRUNCATE |
|---|---|---|
| Removes structure? | Yes | No |
| Removes data? | Yes | Yes |
| Can be rolled back? | No (DDL auto-commits) | No (DDL auto-commits) |
| Speed | Slower (more metadata) | Faster (deallocates pages) |
| Resets auto-increment? | N/A (table gone) | Yes (usually) |

#### 5. RENAME

Changes the name of an existing object.

```sql
-- Rename a table
RENAME TABLE Student TO Pupil;
ALTER TABLE Student RENAME TO Pupil; -- Alternative syntax

-- Rename a column
ALTER TABLE Student RENAME COLUMN tot_cred TO total_credits;
```

---

### Data Manipulation Language (DML)

DML statements operate on the data stored in tables.

#### 1. SELECT (Retrieval)

Retrieves data from one or more tables.

**Basic SELECT:**
```sql
-- All columns, all rows
SELECT * FROM Student;

-- Specific columns
SELECT student_id, name FROM Student;

-- With condition
SELECT name, dept_id FROM Student WHERE dept_id = 'CS';

-- With sorting
SELECT name, tot_cred FROM Student ORDER BY tot_cred DESC;

-- With aggregation
SELECT dept_id, COUNT(*) AS student_count
FROM Student
GROUP BY dept_id
HAVING COUNT(*) > 10;

-- Joining tables
SELECT s.name, c.title, t.grade
FROM Student s
JOIN Takes t ON s.student_id = t.student_id
JOIN Section sec ON t.section_id = sec.section_id
JOIN Course c ON sec.course_id = c.course_id
WHERE s.dept_id = 'CS';
```

#### 2. INSERT

Adds new rows to a table.

```sql
-- Insert with values for all columns
INSERT INTO Department VALUES ('CS', 'Computer Science', 'Science Block', 5000000);

-- Insert with specific columns
INSERT INTO Student (student_id, name, dept_id)
VALUES ('CS2026001', 'Alice Johnson', 'CS');

-- Insert multiple rows
INSERT INTO Course (course_id, title, dept_id, credits) VALUES
('CS101', 'Intro to Programming', 'CS', 4),
('CS201', 'Data Structures', 'CS', 4),
('CS301', 'Database Systems', 'CS', 3);

-- Insert from another table (subquery)
INSERT INTO HonorStudents (student_id, name, dept_id)
SELECT student_id, name, dept_id
FROM Student
WHERE tot_cred > 100;
```

#### 3. UPDATE

Modifies existing rows.

```sql
-- Update all rows
UPDATE Student SET tot_cred = tot_cred + 3;

-- Update with condition
UPDATE Student
SET dept_id = 'CS'
WHERE student_id = 'CS2026001';

-- Update multiple columns
UPDATE Instructor
SET salary = salary * 1.10
WHERE dept_id = 'CS';

-- Update using subquery
UPDATE Student
SET advisor_id = (
    SELECT instructor_id
    FROM Instructor
    WHERE dept_id = Student.dept_id
    LIMIT 1
);
```

#### 4. DELETE

Removes rows from a table.

```sql
-- Delete all rows (slow, logs each row)
DELETE FROM Student;

-- Faster delete all (unlogged, uses TRUNCATE semantics in some DBMS)
-- Actually, use TRUNCATE for this purpose.

-- Delete specific rows
DELETE FROM Student
WHERE student_id = 'CS2026001';

-- Delete with subquery
DELETE FROM Takes
WHERE section_id IN (
    SELECT section_id
    FROM Section
    WHERE year < 2020
);

-- Delete all students from a department
DELETE FROM Student
WHERE dept_id = 'PHY';
```

---

### Procedural vs Declarative DML

| Aspect | Declarative (Non-Procedural) | Procedural |
|---|---|---|
| **What you specify** | What data you want, not how to get it | Both what data and how to retrieve it |
| **Example** | SQL: `SELECT * FROM Student WHERE tot_cred > 60` | PL/SQL, T-SQL, embedded SQL with loops |
| **Ease of use** | Higher -- user writes shorter queries | Lower -- user must specify step-by-step |
| **Optimization** | DBMS optimizes the query plan | Programmer controls execution flow |
| **Language family** | SQL (pure) | PL/SQL, stored procedures, cursors |
| **Performance potential** | Good -- DBMS chooses best plan | Better for complex row-by-row processing |

**Example -- Procedural (PL/SQL) equivalent:**
```sql
-- Cursor-based row-by-row processing (Procedural)
DECLARE
    CURSOR student_cursor IS
        SELECT student_id, name, tot_cred FROM Student WHERE dept_id = 'CS';
    v_student Student%ROWTYPE;
BEGIN
    OPEN student_cursor;
    LOOP
        FETCH student_cursor INTO v_student;
        EXIT WHEN student_cursor%NOTFOUND;
        -- Process each student
        DBMS_OUTPUT.PUT_LINE(v_student.name || ' has ' || v_student.tot_cred || ' credits');
    END LOOP;
    CLOSE student_cursor;
END;
```

Standard SQL is **declarative** -- you say *what* you want, and the DBMS's **query optimizer** determines the most efficient execution plan (which index to use, join order, etc.).

---

### DDL vs DML -- Comparison Table

| Aspect | DDL | DML |
|---|---|---|
| **Full form** | Data Definition Language | Data Manipulation Language |
| **Purpose** | Define/modify structure | Manipulate data |
| **Commands** | CREATE, ALTER, DROP, TRUNCATE, RENAME | SELECT, INSERT, UPDATE, DELETE |
| **Affects** | Database objects (tables, indexes) | Data within objects |
| **Auto-commit** | Yes (implicit commit) | No (explicit COMMIT needed) |
| **Rollback** | Not possible (in most DBMS) | Possible if not committed |
| **Undo recovery** | Cannot be undone | Can be undone via ROLLBACK |
| **Examples** | `ALTER TABLE ADD COLUMN` | `UPDATE Student SET ...` |
| **User base** | DBA, database designers | Application programmers, end users |
| **Locking** | Schema-level locks (exclusive) | Row/table-level locks (shared/exclusive) |
| **Triggers** | Can fire DDL triggers | Can fire DML triggers |
| **Audit** | Part of schema change tracking | Part of data change tracking |

### Summary

- **DDL** defines the blueprint: what tables exist, their columns, constraints, and relationships.
- **DML** fills and modifies the actual data within that blueprint.
- DDL statements auto-commit (permanent immediately), while DML statements need explicit transaction control.
- SQL is primarily declarative: you specify *what* to retrieve, not *how* to retrieve it. Stored procedures offer procedural capabilities for complex logic.
- Both DDL and DML are essential. Without DDL, we cannot structure data; without DML, the structured data remains empty.

---

## Practice Problems

**1.** Write the DDL command to create a table `Employee` with columns `emp_id` (INT, PK), `name` (VARCHAR(50), NOT NULL), `salary` (DECIMAL(10,2)), and `dept_id` (INT, FK referencing Department).
<details>
<summary>Answer</summary>

```sql
CREATE TABLE Employee (
    emp_id      INT PRIMARY KEY,
    name        VARCHAR(50) NOT NULL,
    salary      DECIMAL(10,2),
    dept_id     INT,
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
);
```
</details>

**2.** What is the difference between `DELETE FROM Student` and `TRUNCATE TABLE Student`?
<details>
<summary>Answer</summary>
`DELETE` is DML -- removes rows one by one, can be rolled back, fires triggers, and preserves auto-increment counters. `TRUNCATE` is DDL -- deallocates entire data pages, cannot be rolled back, does not fire triggers, and resets auto-increment counters.
</details>

**3.** Write a DML query to increase the salary of all instructors in the 'CS' department by 15%.
<details>
<summary>Answer</summary>

```sql
UPDATE Instructor
SET salary = salary * 1.15
WHERE dept_id = 'CS';
```
</details>

**4.** Classify these statements as DDL or DML: `CREATE INDEX`, `DELETE`, `RENAME`, `INSERT INTO ... SELECT`, `TRUNCATE`.
<details>
<summary>Answer</summary>
DDL: CREATE INDEX, RENAME, TRUNCATE. DML: DELETE, INSERT INTO ... SELECT.
</details>

**5.** Explain why DDL statements cannot be rolled back with `ROLLBACK` but DML statements can.
<details>
<summary>Answer</summary>
DDL statements auto-commit the current transaction immediately because they modify the data dictionary (system catalog), which must remain consistent. DML statements operate on user data and are wrapped in transactions that can be committed or rolled back explicitly.
</details>
