# Data Manipulation Operations

**Course:** Database Management Systems  
**Module:** 1 | **Lecture:** 9  
**Date:** 28-Jul-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 1  
**Learning Methodology:** Chalk & Talk  
**Reference:** Korth & Silberschatz Database System Concepts (7th Ed.)

## Notes

### Overview

Data Manipulation Operations are the fundamental ways we interact with data stored in a database. This lecture covers five core operations: INSERT, DELETE, UPDATE, SELECT, and VIEW operations -- along with how integrity constraints are enforced during each.

**Sample tables used throughout this lecture:**

```sql
CREATE TABLE Department (
    dept_id   CHAR(4) PRIMARY KEY,
    dept_name VARCHAR(50) NOT NULL,
    building  VARCHAR(30),
    budget    DECIMAL(12,2) CHECK (budget >= 0)
);

CREATE TABLE Student (
    student_id CHAR(9) PRIMARY KEY,
    name       VARCHAR(50) NOT NULL,
    dept_id    CHAR(4),
    tot_cred   INT DEFAULT 0 CHECK (tot_cred >= 0),
    email      VARCHAR(100) UNIQUE,
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
);

CREATE TABLE Course (
    course_id CHAR(8) PRIMARY KEY,
    title     VARCHAR(100) NOT NULL,
    dept_id   CHAR(4) NOT NULL,
    credits   INT CHECK (credits > 0 AND credits <= 5),
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
);

CREATE TABLE Instructor (
    instructor_id CHAR(5) PRIMARY KEY,
    name          VARCHAR(50) NOT NULL,
    dept_id       CHAR(4),
    salary        DECIMAL(10,2) CHECK (salary >= 0),
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
);

CREATE TABLE Section (
    section_id    INT PRIMARY KEY,
    course_id     CHAR(8) NOT NULL,
    semester      VARCHAR(6) CHECK (semester IN ('Fall', 'Spring', 'Summer')),
    year          INT,
    instructor_id CHAR(5),
    room          VARCHAR(10),
    FOREIGN KEY (course_id) REFERENCES Course(course_id),
    FOREIGN KEY (instructor_id) REFERENCES Instructor(instructor_id)
);

CREATE TABLE Takes (
    student_id CHAR(9),
    section_id INT,
    grade      CHAR(2),
    PRIMARY KEY (student_id, section_id),
    FOREIGN KEY (student_id) REFERENCES Student(student_id)
        ON DELETE CASCADE,
    FOREIGN KEY (section_id) REFERENCES Section(section_id)
        ON DELETE CASCADE
);
```

---

### 1. INSERT Operations

**Purpose:** Add new rows (tuples) to a table.

#### Basic INSERT

```sql
-- Insert with values for all columns (order matters -- matches column order)
INSERT INTO Department
VALUES ('CS', 'Computer Science', 'Science Block', 5000000.00);

-- Insert with explicit column specification (order can differ)
INSERT INTO Department (dept_id, dept_name, budget, building)
VALUES ('EE', 'Electrical Engineering', 3000000.00, 'Engineering Block');

-- Insert multiple rows in one statement
INSERT INTO Department (dept_id, dept_name, building, budget) VALUES
    ('ME', 'Mechanical Engineering', 'Engineering Block', 2500000.00),
    ('CE', 'Civil Engineering', 'Engineering Block', 2000000.00),
    ('PHY', 'Physics', 'Science Block', 1500000.00);
```

#### INSERT with DEFAULT Values

```sql
-- Uses default value for tot_cred (0) and no email
INSERT INTO Student (student_id, name, dept_id)
VALUES ('CS2026001', 'Alice Johnson', 'CS');

-- Uses explicit DEFAULT keyword
INSERT INTO Student (student_id, name, dept_id, tot_cred)
VALUES ('CS2026002', 'Bob Smith', 'EE', DEFAULT);

-- Resulting row: CS2026002, Bob Smith, EE, 0, NULL
```

#### INSERT with SELECT (Copying Data)

```sql
-- Create a backup table
CREATE TABLE StudentBackup AS
SELECT * FROM Student WITH NO DATA;

-- Copy all CS students
INSERT INTO StudentBackup
SELECT * FROM Student WHERE dept_id = 'CS';

-- Insert aggregated data into a summary table
CREATE TABLE DeptSummary (
    dept_id   CHAR(4) PRIMARY KEY,
    avg_cred  DECIMAL(5,2)
);

INSERT INTO DeptSummary (dept_id, avg_cred)
SELECT dept_id, AVG(tot_cred)
FROM Student
WHERE dept_id IS NOT NULL
GROUP BY dept_id;
```

#### INSERT Violations

```sql
-- Violation 1: NOT NULL
INSERT INTO Student (student_id) VALUES ('CS2026003');
-- ERROR: Column 'name' has no default and is NOT NULL

-- Violation 2: Primary key duplication
INSERT INTO Student VALUES ('CS2026001', 'Charlie', 'CS', 0, 'c@u.edu');
INSERT INTO Student VALUES ('CS2026001', 'Duplicate', 'EE', 0, 'd@u.edu');
-- ERROR: Duplicate primary key value 'CS2026001'

-- Violation 3: Foreign key
INSERT INTO Student VALUES ('CS2026010', 'David', 'XYZ', 0, 'd@u.edu');
-- ERROR: Foreign key violation -- dept_id 'XYZ' does not exist

-- Violation 4: CHECK constraint
INSERT INTO Student VALUES ('CS2026004', 'Eve', 'CS', -5, 'e@u.edu');
-- ERROR: CHECK (tot_cred >= 0) violated

-- Violation 5: UNIQUE constraint
INSERT INTO Student VALUES ('CS2026005', 'Frank', 'CS', 30, 'e@u.edu');
-- ERROR: Duplicate email 'e@u.edu' violates UNIQUE constraint

-- Violation 6: Data type mismatch
INSERT INTO Student VALUES ('CS2026006', 'Grace', 12345, 30, 'g@u.edu');
-- ERROR: dept_id expects CHAR(4), not integer
```

---

### 2. DELETE Operations

**Purpose:** Remove rows from a table.

#### Basic DELETE

```sql
-- Delete all rows (use with extreme caution)
DELETE FROM Student;

-- Delete specific rows
DELETE FROM Student
WHERE student_id = 'CS2026001';

-- Delete based on a condition
DELETE FROM Student
WHERE dept_id = 'PHY' AND tot_cred = 0;
```

#### DELETE with Subqueries

```sql
-- Delete students who have not taken any course
DELETE FROM Student
WHERE student_id NOT IN (
    SELECT DISTINCT student_id FROM Takes
);

-- Delete sections that have no enrollments
DELETE FROM Section
WHERE section_id NOT IN (
    SELECT DISTINCT section_id FROM Takes
);

-- Delete instructors whose department was removed
DELETE FROM Instructor
WHERE dept_id IN (
    SELECT dept_id FROM Department
    WHERE budget = 0
);
```

#### DELETE and Referential Integrity

```sql
-- CASE 1: DELETE parent with ON DELETE RESTRICT
DELETE FROM Department WHERE dept_id = 'CS';
-- ERROR: Referential integrity violation.
-- Students reference Department(dept_id) with RESTRICT (default).
-- Solution: Delete or reassign students first.

-- CASE 2: DELETE parent with ON DELETE CASCADE (Takes table)
DELETE FROM Student WHERE student_id = 'CS2026001';
-- Automatically deletes all rows in Takes where student_id = 'CS2026001'.
-- The cascade propagates: if Takes references Section with CASCADE,
-- sections with no remaining enrollments might also be deleted.

-- CASE 3: DELETE parent with ON DELETE SET NULL
-- (Assuming Instructor.dept_id has ON DELETE SET NULL)
DELETE FROM Department WHERE dept_id = 'PHY';
-- All instructors with dept_id = 'PHY' now have dept_id = NULL.
-- They become "unaffiliated" instructors.
```

#### DELETE vs TRUNCATE Recap

```sql
-- DELETE: DML, row by row, can be rolled back, fires triggers
DELETE FROM Student;

-- TRUNCATE: DDL, deallocates pages, cannot be rolled back, no triggers
TRUNCATE TABLE Student;
```

---

### 3. UPDATE Operations

**Purpose:** Modify existing rows.

#### Basic UPDATE

```sql
-- Update all rows
UPDATE Instructor
SET salary = salary * 1.10;
-- All instructors get a 10% raise

-- Update with WHERE clause
UPDATE Instructor
SET salary = salary * 1.15
WHERE dept_id = 'CS';
-- Only CS instructors get 15% raise

-- Update multiple columns
UPDATE Student
SET dept_id = 'CS',
    tot_cred = tot_cred + 3
WHERE student_id = 'CS2026001';
```

#### UPDATE with Subqueries

```sql
-- Set advisor to the instructor with most experience
UPDATE Student s
SET advisor_id = (
    SELECT instructor_id
    FROM Instructor i
    WHERE i.dept_id = s.dept_id
    ORDER BY i.hire_date ASC
    LIMIT 1
);

-- Increase budget for departments with growing enrollment
UPDATE Department d
SET budget = budget * 1.20
WHERE (
    SELECT COUNT(*) FROM Student s
    WHERE s.dept_id = d.dept_id
) > 100;
```

#### UPDATE Violations

```sql
-- Violation: Foreign key
UPDATE Student
SET dept_id = 'XYZ'
WHERE student_id = 'CS2026001';
-- ERROR: 'XYZ' is not a valid department

-- Violation: CHECK constraint
UPDATE Student
SET tot_cred = -10
WHERE student_id = 'CS2026001';
-- ERROR: CHECK (tot_cred >= 0) violated

-- Violation: UNIQUE constraint
INSERT INTO Student VALUES ('CS2026010', 'Hank', 'CS', 30, 'hank@u.edu');
UPDATE Student
SET email = 'hank@u.edu'
WHERE student_id = 'CS2026001';
-- ERROR: Duplicate email violates UNIQUE constraint

-- Violation: Primary key change
UPDATE Student
SET student_id = 'CS2026001'
WHERE student_id = 'CS2026002';
-- ERROR: Duplicate primary key 'CS2026001' (if 'CS2026001' already exists)
```

---

### 4. SELECT Operations

**Purpose:** Retrieve data from the database.

#### Basic SELECT

```sql
-- All columns, all rows
SELECT * FROM Student;

-- Specific columns
SELECT student_id, name FROM Student;

-- Column alias
SELECT student_id AS "Roll Number", name AS "Student Name"
FROM Student;

-- Literal values and expressions
SELECT
    student_id,
    name,
    'Enrolled' AS status,
    tot_cred * 10 AS weighted_score
FROM Student;
```

#### SELECT with Filtering

```sql
-- WHERE clause with comparison operators
SELECT * FROM Student WHERE dept_id = 'CS';
SELECT * FROM Student WHERE tot_cred > 60;
SELECT * FROM Student WHERE tot_cred BETWEEN 30 AND 60;
SELECT * FROM Student WHERE name LIKE 'A%';           -- Starts with A
SELECT * FROM Student WHERE name LIKE '%son';         -- Ends with 'son'
SELECT * FROM Student WHERE dept_id IN ('CS', 'EE');  -- Multiple values

-- NULL handling
SELECT * FROM Student WHERE email IS NULL;
SELECT * FROM Student WHERE email IS NOT NULL;

-- Logical operators
SELECT * FROM Student
WHERE dept_id = 'CS'
  AND tot_cred >= 60
  AND (email IS NOT NULL);
```

#### SELECT with Sorting

```sql
-- Ascending (default)
SELECT * FROM Student ORDER BY name;

-- Descending
SELECT * FROM Student ORDER BY tot_cred DESC;

-- Multiple sort keys
SELECT * FROM Student
ORDER BY dept_id ASC, tot_cred DESC;
```

#### SELECT with Aggregation

```sql
-- Aggregate functions
SELECT COUNT(*) AS total_students FROM Student;
SELECT AVG(tot_cred) AS avg_credits FROM Student;
SELECT MAX(tot_cred) AS max_credits FROM Student;
SELECT MIN(tot_cred) AS min_credits FROM Student;
SELECT SUM(tot_cred) AS total_credits FROM Student;

-- GROUP BY
SELECT dept_id, COUNT(*) AS student_count, AVG(tot_cred) AS avg_cred
FROM Student
GROUP BY dept_id;

-- HAVING (filter groups, similar to WHERE for rows)
SELECT dept_id, COUNT(*) AS student_count
FROM Student
GROUP BY dept_id
HAVING COUNT(*) > 10;
```

#### SELECT with Joins

```sql
-- INNER JOIN (only matching rows)
SELECT s.name, c.title, t.grade
FROM Student s
JOIN Takes t ON s.student_id = t.student_id
JOIN Section sec ON t.section_id = sec.section_id
JOIN Course c ON sec.course_id = c.course_id;

-- LEFT JOIN (all students, even those with no enrollments)
SELECT s.name, t.grade
FROM Student s
LEFT JOIN Takes t ON s.student_id = t.student_id;

-- JOIN with aggregation
SELECT c.title, COUNT(t.student_id) AS enrolled_count
FROM Course c
JOIN Section sec ON c.course_id = sec.course_id
JOIN Takes t ON sec.section_id = t.section_id
WHERE sec.semester = 'Fall' AND sec.year = 2026
GROUP BY c.course_id, c.title;
```

#### SELECT with Set Operations

```sql
-- UNION (combine results, remove duplicates)
SELECT name FROM Student
UNION
SELECT name FROM Instructor;

-- UNION ALL (combine results, keep duplicates)
SELECT dept_id FROM Student
UNION ALL
SELECT dept_id FROM Instructor;

-- INTERSECT (common rows)
SELECT course_id FROM Course
INTERSECT
SELECT course_id FROM Section;

-- EXCEPT (in first but not second)
SELECT dept_id FROM Department
EXCEPT
SELECT dept_id FROM Student;
```

#### SELECT with Subqueries

```sql
-- Subquery in WHERE
SELECT * FROM Student
WHERE dept_id IN (
    SELECT dept_id FROM Department
    WHERE budget > 2000000
);

-- Subquery in FROM (derived table)
SELECT dept_id, avg_cred
FROM (
    SELECT dept_id, AVG(tot_cred) AS avg_cred
    FROM Student
    GROUP BY dept_id
) AS dept_stats
WHERE avg_cred > 50;

-- Subquery in SELECT (scalar subquery)
SELECT
    student_id,
    name,
    (SELECT COUNT(*) FROM Takes t
     WHERE t.student_id = s.student_id) AS course_count
FROM Student s;

-- EXISTS
SELECT d.dept_id, d.dept_name
FROM Department d
WHERE EXISTS (
    SELECT 1 FROM Student s
    WHERE s.dept_id = d.dept_id
    AND s.tot_cred > 100
);
```

---

### 5. VIEW Operations

**Purpose:** A **view** is a virtual table based on a SELECT query. It does not store data physically (unless materialized) -- it provides a customized window into the base tables.

#### Creating Views

```sql
-- Simple view: subset of columns and rows
CREATE VIEW CS_Students AS
SELECT student_id, name, tot_cred
FROM Student
WHERE dept_id = 'CS';

-- View with derived column
CREATE VIEW StudentPerformance AS
SELECT
    s.student_id,
    s.name,
    AVG(
        CASE
            WHEN t.grade = 'A+' THEN 4.0
            WHEN t.grade = 'A'  THEN 4.0
            WHEN t.grade = 'A-' THEN 3.7
            WHEN t.grade = 'B+' THEN 3.3
            WHEN t.grade = 'B'  THEN 3.0
            WHEN t.grade = 'B-' THEN 2.7
            WHEN t.grade = 'C+' THEN 2.3
            WHEN t.grade = 'C'  THEN 2.0
            ELSE 0.0
        END
    ) AS gpa
FROM Student s
JOIN Takes t ON s.student_id = t.student_id
GROUP BY s.student_id, s.name;

-- View joining multiple tables
CREATE VIEW CourseEnrollment AS
SELECT
    c.course_id,
    c.title,
    sec.semester,
    sec.year,
    COUNT(t.student_id) AS enrolled
FROM Course c
JOIN Section sec ON c.course_id = sec.course_id
LEFT JOIN Takes t ON sec.section_id = t.section_id
GROUP BY c.course_id, c.title, sec.semester, sec.year;

-- View with CHECK OPTION (prevents updates that would hide the row)
CREATE VIEW CS_Active_Students AS
SELECT * FROM Student
WHERE dept_id = 'CS'
WITH CHECK OPTION;
```

#### Querying Views

```sql
-- Query a view like a table
SELECT * FROM CS_Students;

-- Filter on a view
SELECT * FROM CS_Students WHERE tot_cred > 60;

-- Join a view with another table
SELECT cs.name, d.dept_name
FROM CS_Students cs
JOIN Department d ON d.dept_id = 'CS';
```

#### Updating Through Views

Views are **updateable** under certain conditions:
- The view is based on a single table.
- The view includes the primary key.
- No aggregate functions, GROUP BY, DISTINCT, or set operations.

```sql
-- Updateable view
CREATE VIEW StudentContact AS
SELECT student_id, name, email
FROM Student;

-- This UPDATE works (view is updateable)
UPDATE StudentContact
SET email = 'alice.new@university.edu'
WHERE student_id = 'CS2026001';

-- Non-updateable view (contains aggregation)
CREATE VIEW DeptStats AS
SELECT dept_id, COUNT(*) AS cnt
FROM Student
GROUP BY dept_id;

-- This UPDATE will fail
UPDATE DeptStats SET cnt = 10 WHERE dept_id = 'CS';
-- ERROR: View with GROUP BY is not updateable
```

#### Dropping Views

```sql
DROP VIEW CS_Students;
DROP VIEW IF EXISTS CS_Students;  -- Avoid error if not found
```

#### Materialized Views

A **materialized view** physically stores the query result. It must be refreshed when base data changes.

```sql
-- PostgreSQL syntax for materialized view
CREATE MATERIALIZED VIEW DeptEnrollmentStats AS
SELECT d.dept_id, d.dept_name, COUNT(s.student_id) AS student_count
FROM Department d
LEFT JOIN Student s ON d.dept_id = s.dept_id
GROUP BY d.dept_id, d.dept_name;

-- Refresh the materialized view
REFRESH MATERIALIZED VIEW DeptEnrollmentStats;
```

---

### Handling Violations During Operations -- Summary

| Operation | Potential Violation | Prevention / Handling |
|---|---|---|
| **INSERT** | Duplicate PK | Reject. Use `INSERT ... ON DUPLICATE KEY UPDATE` (MySQL) or `ON CONFLICT` (PostgreSQL) for upsert. |
| **INSERT** | NULL in NOT NULL | Reject. Provide value or DEFAULT. |
| **INSERT** | FK not found | Reject. Insert parent first or use deferrable constraints. |
| **INSERT** | CHECK fails | Reject. Validate data before insert. |
| **INSERT** | UNIQUE violation | Reject. Use MERGE / UPSERT pattern. |
| **DELETE** | FK references (RESTRICT) | Reject. Delete children first or use CASCADE. |
| **DELETE** | FK references (CASCADE) | Propagate -- children deleted automatically. |
| **DELETE** | FK references (SET NULL) | FK set to NULL in children. |
| **UPDATE** | FK not found | Reject. Ensure referenced key exists. |
| **UPDATE** | PK duplication | Reject. Choose a unique new PK value. |
| **UPDATE** | CHECK fails | Reject. Ensure new values pass constraints. |
| **UPDATE** | View not updateable | Reject. Update base tables directly. |
| **VIEW** | Create with invalid query | Reject. Validate SELECT before CREATE VIEW. |

---

## Practice Problems

**1.** Write SQL to insert three new departments in one statement: `HR` (Human Resources, Admin Block, budget 1,000,000), `IT` (Information Technology, Tech Park, budget 4,000,000), and `MGMT` (Management, Admin Block, budget 2,500,000).
<details>
<summary>Show Answer</summary>

```sql
INSERT INTO Department (dept_id, dept_name, building, budget) VALUES
    ('HR', 'Human Resources', 'Admin Block', 1000000.00),
    ('IT', 'Information Technology', 'Tech Park', 4000000.00),
    ('MGMT', 'Management', 'Admin Block', 2500000.00);
```
</details>

**2.** A student with ID 'CS2026001' has graduated. Write the SQL to delete this student and all their enrollment records, assuming the foreign key in Takes uses ON DELETE CASCADE.
<details>
<summary>Show Answer</summary>

```sql
DELETE FROM Student WHERE student_id = 'CS2026001';
-- The CASCADE foreign key from Takes to Student will
-- automatically delete all rows in Takes with this student_id.
```
</details>

**3.** Give a 10% salary raise to all instructors in the 'CS' department who earn less than 50,000.
<details>
<summary>Show Answer</summary>

```sql
UPDATE Instructor
SET salary = salary * 1.10
WHERE dept_id = 'CS' AND salary < 50000;
```
</details>

**4.** Create a view `HighPerformers` that shows student_id, name, and GPA for students with GPA above 3.5.
<details>
<summary>Show Answer</summary>

```sql
CREATE VIEW HighPerformers AS
SELECT
    s.student_id,
    s.name,
    AVG(
        CASE
            WHEN t.grade = 'A+' THEN 4.0 WHEN t.grade = 'A'  THEN 4.0
            WHEN t.grade = 'A-' THEN 3.7 WHEN t.grade = 'B+' THEN 3.3
            WHEN t.grade = 'B'  THEN 3.0 WHEN t.grade = 'B-' THEN 2.7
            WHEN t.grade = 'C+' THEN 2.3 WHEN t.grade = 'C'  THEN 2.0
            ELSE 0.0
        END
    ) AS gpa
FROM Student s
JOIN Takes t ON s.student_id = t.student_id
GROUP BY s.student_id, s.name
HAVING AVG(...) > 3.5;
```
</details>

**5.** What happens when you try to `UPDATE` a view that uses GROUP BY? Why?
<details>
<summary>Show Answer</summary>
The UPDATE fails with an error. Views with GROUP BY, aggregation, or DISTINCT are non-updateable because the DBMS cannot uniquely map a view row back to a single base table row. The aggregate values are computed, not stored, so there is no physical row to update.
</details>
