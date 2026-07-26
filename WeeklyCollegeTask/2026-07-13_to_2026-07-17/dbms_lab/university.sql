=============================================================================
--  UNIVERSITY DATABASE MANAGEMENT SYSTEM
--  Course       : DBMS Lab
--  Topic        : SQL Joins & Relational Schema Design
--  Description  : Complete university structure demonstrating all types of
--                 SQL joins, constraints, subqueries, and aggregations.
--  Tables       : department, student, professor, course, enrollment
--  Relationships:
--    1. department -> student     (1:M)
--    2. department -> professor   (1:M)
--    3. student    -> enrollment  (1:M)
--    4. course     -> enrollment  (1:M)
--    5. department -> course      (1:M)
--    6. professor  -> course      (1:M)
--    7. student    -> course      (M:M via enrollment)
--  Author       : DBMS Lab
--  Created      : July 2026
=============================================================================

-- ===========================================================================
--  SECTION 1: DATABASE CREATION
--  =========================================================================
--  DDL Commands: CREATE DATABASE, USE
--  Purpose: Creates a new database and selects it for subsequent operations.
-- ===========================================================================

-- Create the database only if it does not already exist (avoids error on re-run)
CREATE DATABASE IF NOT EXISTS University;

-- Switch the current session context to the University database
USE University;

-- ===========================================================================
--  SECTION 2: TABLE DEFINITIONS (DDL)
--  =========================================================================
--  Here we define 5 tables with PRIMARY KEY, FOREIGN KEY, UNIQUE,
--  NOT NULL, DEFAULT, and AUTO_INCREMENT constraints.
--  These enforce entity integrity (PK), referential integrity (FK),
--  and domain integrity (data types + constraints).
-- ===========================================================================

-- ---------------------------------------------------------------------------
--  Table 1: department
--  -------------------------------------------------------------------------
--  Stores all academic departments of the university.
--  Each department has a unique ID, a name, and a campus location.
--  PK: dept_id
-- ---------------------------------------------------------------------------
CREATE TABLE department (
    dept_id      INT PRIMARY KEY AUTO_INCREMENT,  -- Unique identifier for each department
    dept_name    VARCHAR(100) NOT NULL,            -- Name of the department (e.g., Computer Science)
    location     VARCHAR(100)                      -- Physical location on campus (e.g., Building A)
);

-- ---------------------------------------------------------------------------
--  Table 2: student
--  -------------------------------------------------------------------------
--  Stores personal and academic information about each student.
--  FK: dept_id references department(dept_id) with ON DELETE SET NULL
--       meaning if a department is deleted, the student's dept_id becomes NULL
--       instead of deleting the student record.
-- ---------------------------------------------------------------------------
CREATE TABLE student (
    student_id     INT PRIMARY KEY AUTO_INCREMENT,  -- Unique roll number for each student
    first_name     VARCHAR(50) NOT NULL,             -- Student's first name
    last_name      VARCHAR(50) NOT NULL,             -- Student's last name
    dob            DATE,                             -- Date of birth for age calculations
    email          VARCHAR(100) UNIQUE,              -- University email address (must be unique)
    dept_id        INT,                              -- Department the student belongs to
    enrollment_year INT,                             -- Year the student was admitted
    FOREIGN KEY (dept_id) REFERENCES department(dept_id) ON DELETE SET NULL
);

-- ---------------------------------------------------------------------------
--  Table 3: professor
--  -------------------------------------------------------------------------
--  Stores information about faculty members.
--  FK: dept_id references department(dept_id).
--  Each professor belongs to exactly one department.
-- ---------------------------------------------------------------------------
CREATE TABLE professor (
    prof_id      INT PRIMARY KEY AUTO_INCREMENT,   -- Unique faculty ID
    first_name   VARCHAR(50) NOT NULL,              -- Professor's first name
    last_name    VARCHAR(50) NOT NULL,               -- Professor's last name
    email        VARCHAR(100) UNIQUE,                -- Official email address
    dept_id      INT,                                -- Department they teach in
    hire_date    DATE,                               -- Date of joining the university
    FOREIGN KEY (dept_id) REFERENCES department(dept_id) ON DELETE SET NULL
);

-- ---------------------------------------------------------------------------
--  Table 4: course
--  -------------------------------------------------------------------------
--  Stores course offerings. Each course belongs to a department and
--  is taught by a professor.
--  FKs: dept_id, prof_id
-- ---------------------------------------------------------------------------
CREATE TABLE course (
    course_id    INT PRIMARY KEY AUTO_INCREMENT,   -- Unique course identifier
    course_code  VARCHAR(20) UNIQUE NOT NULL,       -- Short code (e.g., CS101)
    course_name  VARCHAR(100) NOT NULL,              -- Full course title
    credits      INT NOT NULL,                       -- Number of credit hours
    dept_id      INT,                                -- Department that offers this course
    prof_id      INT,                                -- Professor assigned to teach this course
    FOREIGN KEY (dept_id) REFERENCES department(dept_id) ON DELETE SET NULL,
    FOREIGN KEY (prof_id) REFERENCES professor(prof_id) ON DELETE SET NULL
);

-- ---------------------------------------------------------------------------
--  Table 5: enrollment
--  -------------------------------------------------------------------------
--  Junction table for the Many-to-Many relationship between student and course.
--  A student can enroll in many courses; a course can have many students.
--  FKs: student_id, course_id with ON DELETE CASCADE
--       (if a student/course is deleted, their enrollments are also deleted).
-- ---------------------------------------------------------------------------
CREATE TABLE enrollment (
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT,   -- Unique enrollment record ID
    student_id     INT NOT NULL,                      -- FK to student
    course_id      INT NOT NULL,                      -- FK to course
    semester       VARCHAR(20),                       -- e.g., 'Fall 2022', 'Spring 2023'
    grade          VARCHAR(2),                        -- Letter grade awarded (A, B+, etc.)
    FOREIGN KEY (student_id) REFERENCES student(student_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES course(course_id) ON DELETE CASCADE
);

-- ===========================================================================
--  SECTION 3: SAMPLE DATA INSERTION (DML)
--  =========================================================================
--  DML Commands: INSERT INTO ... VALUES
--  Purpose: Populate all tables with realistic sample data to test queries.
-- ===========================================================================

-- Insert 4 departments into the department table
INSERT INTO department (dept_name, location) VALUES
('Computer Science', 'Building A'),    -- dept_id = 1
('Mathematics',      'Building B'),    -- dept_id = 2
('Physics',          'Building C'),    -- dept_id = 3
('Electrical Engineering', 'Building D');  -- dept_id = 4

-- Insert 5 students
INSERT INTO student (first_name, last_name, dob, email, dept_id, enrollment_year) VALUES
('Alice',   'Johnson', '2002-05-14', 'alice.j@univ.edu',   1, 2021),  -- CS student
('Bob',     'Smith',   '2001-08-22', 'bob.s@univ.edu',     2, 2020),  -- Math student
('Charlie', 'Brown',   '2003-01-10', 'charlie.b@univ.edu', 1, 2022),  -- CS student
('Diana',   'Prince',  '2002-11-30', 'diana.p@univ.edu',   3, 2021),  -- Physics student
('Eve',     'Davis',   '2000-07-19', 'eve.d@univ.edu',     4, 2019);  -- EE student

-- Insert 4 professors, each in a different department
INSERT INTO professor (first_name, last_name, email, dept_id, hire_date) VALUES
('John',  'Doe',    'john.doe@univ.edu',     1, '2015-09-01'),  -- CS professor (prof_id = 1)
('Jane',  'Taylor', 'jane.taylor@univ.edu',   2, '2018-01-15'),  -- Math professor (prof_id = 2)
('Richard', 'Lee',  'richard.lee@univ.edu',   3, '2020-03-20'),  -- Physics professor (prof_id = 3)
('Emily', 'Clark',  'emily.clark@univ.edu',   4, '2016-06-10');  -- EE professor (prof_id = 4)

-- Insert 6 courses
INSERT INTO course (course_code, course_name, credits, dept_id, prof_id) VALUES
('CS101',  'Intro to Programming', 4, 1, 1),   -- Taught by Prof. Doe (CS)
('CS201',  'Data Structures',      4, 1, 1),   -- Taught by Prof. Doe (CS)
('MATH101','Calculus I',           3, 2, 2),   -- Taught by Prof. Taylor (Math)
('MATH201','Linear Algebra',       3, 2, 2),   -- Taught by Prof. Taylor (Math)
('PHY101', 'Mechanics',            4, 3, 3),   -- Taught by Prof. Lee (Physics)
('EE101',  'Circuits',             3, 4, 4);   -- Taught by Prof. Clark (EE)

-- Insert enrollment records linking students to courses with grades
INSERT INTO enrollment (student_id, course_id, semester, grade) VALUES
(1, 1, 'Fall 2022',   'A'),    -- Alice took CS101 in Fall 2022, got A
(1, 2, 'Spring 2023', 'B+'),   -- Alice took CS201 in Spring 2023, got B+
(2, 3, 'Fall 2022',   'A-'),   -- Bob took MATH101 in Fall 2022, got A-
(3, 1, 'Fall 2023',   'B'),    -- Charlie took CS101 in Fall 2023, got B
(3, 2, 'Fall 2023',   'A'),    -- Charlie took CS201 in Fall 2023, got A
(4, 5, 'Fall 2022',   'C+'),   -- Diana took PHY101 in Fall 2022, got C+
(5, 6, 'Spring 2023', 'B');    -- Eve took EE101 in Spring 2023, got B

-- Note: No student is enrolled in MATH201 (course_id = 4).
-- This will be useful to demonstrate outer joins later.

-- ===========================================================================
--  SECTION 4: SQL JOINS
--  =========================================================================
--  Joins combine rows from two or more tables based on a related column.
--  Types covered:
--    1. INNER JOIN  - Returns only matching rows from both tables.
--    2. LEFT JOIN   - Returns all rows from left table, matching from right.
--    3. RIGHT JOIN  - Returns all rows from right table, matching from left.
--    4. FULL JOIN   - Returns all rows where there is a match in either table
--                     (simulated via UNION of LEFT and RIGHT JOIN).
--    5. CROSS JOIN  - Returns Cartesian product (each row from table1 paired
--                     with every row from table2).
--    6. SELF JOIN   - Joining a table with itself.
-- ===========================================================================

-- ---------------------------------------------------------------------------
--  JOIN TYPE 1: INNER JOIN
--  -------------------------------------------------------------------------
--  Theory: INNER JOIN returns only the rows where the join condition is true
--  in BOTH tables. Rows without a match in either table are excluded.
--
--  Here we join 4 tables (student -> department, student -> enrollment,
--  enrollment -> course) to get a complete picture of each enrollment.
-- ---------------------------------------------------------------------------
SELECT
    s.student_id,                                   -- Unique ID of the student
    CONCAT(s.first_name, ' ', s.last_name) AS name, -- Full name (derived column)
    d.dept_name,                                    -- Department name from department table
    c.course_code,                                  -- Course code from course table
    c.course_name,                                  -- Full course title
    e.grade                                         -- Grade awarded in that course
FROM student s
INNER JOIN department d ON s.dept_id = d.dept_id       -- Link student to their department
INNER JOIN enrollment e ON s.student_id = e.student_id -- Link student to enrollments
INNER JOIN course c ON e.course_id = c.course_id       -- Link enrollment to course details
ORDER BY s.student_id, e.semester;                     -- Order by student ID then semester

-- ---------------------------------------------------------------------------
--  JOIN TYPE 2: LEFT JOIN (a.k.a. LEFT OUTER JOIN)
--  -------------------------------------------------------------------------
--  Theory: LEFT JOIN returns ALL rows from the left table (student), and
--  matching rows from the right table (enrollment, course). If no match
--  exists in the right table, NULL values are returned for its columns.
--
--  Here we can see which students have NO enrollments (they will appear
--  with NULL course_name and NULL grade).
-- ---------------------------------------------------------------------------
SELECT
    s.student_id,
    CONCAT(s.first_name, ' ', s.last_name) AS name,
    c.course_name,
    COALESCE(e.grade, 'Not Enrolled') AS grade  -- Replace NULL with descriptive text
FROM student s
LEFT JOIN enrollment e ON s.student_id = e.student_id  -- Keep all students
LEFT JOIN course c ON e.course_id = c.course_id         -- Keep all enrollments (if any)
ORDER BY s.student_id;

-- ---------------------------------------------------------------------------
--  JOIN TYPE 3: RIGHT JOIN (a.k.a. RIGHT OUTER JOIN)
--  -------------------------------------------------------------------------
--  Theory: RIGHT JOIN returns ALL rows from the right table (course), and
--  matching rows from the left tables (enrollment, student). Courses with
--  no enrolled students will have NULL for student info.
--
--  Here we see all courses including MATH201, which has NO enrolled students.
-- ---------------------------------------------------------------------------
SELECT
    c.course_code,
    c.course_name,
    CONCAT(s.first_name, ' ', s.last_name) AS enrolled_student,
    e.grade
FROM enrollment e
RIGHT JOIN course c ON e.course_id = c.course_id  -- Keep all courses
LEFT JOIN student s ON e.student_id = s.student_id  -- Bring student name if enrolled
ORDER BY c.course_code;

-- ---------------------------------------------------------------------------
--  JOIN TYPE 4: FULL OUTER JOIN (simulated via UNION)
--  -------------------------------------------------------------------------
--  Theory: MySQL does not natively support FULL OUTER JOIN. However, we can
--  simulate it by taking a UNION of:
--    1. LEFT JOIN  (all students + matching enrollments/courses)
--    2. RIGHT JOIN (all courses + matching students/enrollments)
--  UNION removes duplicate rows automatically.
--
--  This gives us EVERY student and EVERY course, matched where possible.
-- ---------------------------------------------------------------------------
-- Part 1: All students with their enrollments (LEFT JOIN)
SELECT
    s.student_id,
    CONCAT(s.first_name, ' ', s.last_name) AS name,
    c.course_code,
    c.course_name,
    e.grade
FROM student s
LEFT JOIN enrollment e ON s.student_id = e.student_id
LEFT JOIN course c ON e.course_id = c.course_id

UNION  -- UNION removes duplicates (use UNION ALL to keep duplicates)

-- Part 2: All courses even if no student is enrolled (RIGHT JOIN)
SELECT
    s.student_id,
    CONCAT(s.first_name, ' ', s.last_name) AS name,
    c.course_code,
    c.course_name,
    e.grade
FROM enrollment e
RIGHT JOIN course c ON e.course_id = c.course_id
LEFT JOIN student s ON e.student_id = s.student_id
ORDER BY student_id, course_code;

-- ---------------------------------------------------------------------------
--  JOIN TYPE 5: CROSS JOIN
--  -------------------------------------------------------------------------
--  Theory: CROSS JOIN produces the Cartesian product of two tables.
--  Each row from table A is paired with EVERY row from table B.
--  If student has 5 rows and course has 6 rows, the result has 5 x 6 = 30 rows.
--  This join has NO ON clause because it pairs all rows unconditionally.
--  Practical use: generating all possible combinations (e.g., scheduling).
-- ---------------------------------------------------------------------------
SELECT
    CONCAT(s.first_name, ' ', s.last_name) AS student_name,
    c.course_name
FROM student s
CROSS JOIN course c
ORDER BY s.last_name, c.course_name;

-- ---------------------------------------------------------------------------
--  JOIN TYPE 6: SELF JOIN
--  -------------------------------------------------------------------------
--  Theory: A SELF JOIN joins a table with itself using aliases.
--  This is useful for comparing rows within the same table.
--  Here we find all pairs of professors who work in the SAME department.
--  Condition p1.prof_id < p2.prof_id avoids duplicate pairs (e.g., (John,Jane)
--  and (Jane,John) would be two rows otherwise).
-- ---------------------------------------------------------------------------
SELECT
    CONCAT(p1.first_name, ' ', p1.last_name) AS professor_1,
    CONCAT(p2.first_name, ' ', p2.last_name) AS professor_2,
    d.dept_name
FROM professor p1
INNER JOIN professor p2
    ON p1.dept_id = p2.dept_id     -- Same department
    AND p1.prof_id < p2.prof_id     -- Each pair appears only once
INNER JOIN department d ON p1.dept_id = d.dept_id
ORDER BY d.dept_name;

-- ===========================================================================
--  SECTION 5: JOINS WITH AGGREGATION (GROUP BY + HAVING)
--  =========================================================================
--  Aggregate functions: COUNT(), SUM(), AVG(), MAX(), MIN()
--  GROUP BY groups rows that have the same values in specified columns.
--  HAVING filters groups after aggregation (WHERE filters before grouping).
-- ===========================================================================

-- ---------------------------------------------------------------------------
--  Query 1: Count the number of students in each department
--  -------------------------------------------------------------------------
--  Uses LEFT JOIN so departments with zero students also appear (count = 0).
-- ---------------------------------------------------------------------------
SELECT
    d.dept_name,
    COUNT(s.student_id) AS student_count  -- Aggregate: count students per department
FROM department d
LEFT JOIN student s ON d.dept_id = s.dept_id  -- LEFT JOIN to include empty departments
GROUP BY d.dept_id                            -- Group by department (use PK to avoid ambiguity)
ORDER BY student_count DESC;                  -- Most students first

-- ---------------------------------------------------------------------------
--  Query 2: Find the average grade (numeric conversion) per course
--  -------------------------------------------------------------------------
--  Note: Grade is stored as VARCHAR (A, B+, etc.). We use a CASE expression
--  to convert letter grades to numeric GPA values for averaging.
-- ---------------------------------------------------------------------------
SELECT
    c.course_code,
    c.course_name,
    COUNT(e.student_id) AS total_students,
    ROUND(AVG(
        CASE e.grade
            WHEN 'A'  THEN 4.0
            WHEN 'A-' THEN 3.7
            WHEN 'B+' THEN 3.3
            WHEN 'B'  THEN 3.0
            WHEN 'B-' THEN 2.7
            WHEN 'C+' THEN 2.3
            WHEN 'C'  THEN 2.0
            WHEN 'D'  THEN 1.0
            WHEN 'F'  THEN 0.0
            ELSE NULL
        END
    ), 2) AS avg_gpa  -- Average GPA rounded to 2 decimal places
FROM course c
LEFT JOIN enrollment e ON c.course_id = e.course_id
GROUP BY c.course_id
ORDER BY avg_gpa DESC;

-- ===========================================================================
--  SECTION 6: JOINS WITH SUBQUERIES
--  =========================================================================
--  Subqueries (nested queries) can be used inside SELECT, FROM, or WHERE.
--  They allow multi-step query logic within a single SQL statement.
-- ===========================================================================

-- ---------------------------------------------------------------------------
--  Query 1: Students enrolled in MORE THAN 1 course
--  -------------------------------------------------------------------------
--  Subquery approach: First count enrollments per student, then filter.
--  HAVING clause filters after GROUP BY.
-- ---------------------------------------------------------------------------
SELECT
    s.student_id,
    CONCAT(s.first_name, ' ', s.last_name) AS name,
    COUNT(e.course_id) AS course_count
FROM student s
INNER JOIN enrollment e ON s.student_id = e.student_id
GROUP BY s.student_id
HAVING course_count > 1         -- Only students with more than 1 enrollment
ORDER BY course_count DESC;

-- ---------------------------------------------------------------------------
--  Query 2: Students who scored an 'A' in ANY course (using IN with subquery)
--  -------------------------------------------------------------------------
--  The subquery first finds all student_ids with grade = 'A', then the outer
--  query fetches their full details.
-- ---------------------------------------------------------------------------
SELECT
    student_id,
    CONCAT(first_name, ' ', last_name) AS name,
    email,
    enrollment_year
FROM student
WHERE student_id IN (
    SELECT DISTINCT student_id
    FROM enrollment
    WHERE grade = 'A'            -- Subquery: find students who got an A
)
ORDER BY last_name;

-- ===========================================================================
--  SECTION 7: COMPLEX JOIN ACROSS 4+ TABLES
--  =========================================================================
--  This query demonstrates joining all 5 tables to produce a comprehensive
--  academic transcript showing: student info -> department -> enrollments ->
--  course details -> professor.
-- ===========================================================================
SELECT
    s.student_id                                              AS roll_no,
    CONCAT(s.first_name, ' ', s.last_name)                    AS student_name,
    d.dept_name                                               AS department,
    c.course_code                                             AS course_code,
    c.course_name                                             AS course_title,
    CONCAT(p.first_name, ' ', p.last_name)                    AS professor_name,
    c.credits                                                 AS credit_hours,
    e.semester                                                AS semester,
    COALESCE(e.grade, 'In Progress')                          AS grade
FROM student s
JOIN department d ON s.dept_id = d.dept_id              -- Student's department
JOIN enrollment e ON s.student_id = e.student_id       -- Enrollment records
JOIN course c ON e.course_id = c.course_id             -- Course details
JOIN professor p ON c.prof_id = p.prof_id              -- Professor teaching the course
ORDER BY s.student_id, e.semester;

-- ===========================================================================
--  SECTION 8: ADDITIONAL USEFUL QUERIES
--  =========================================================================

-- ---------------------------------------------------------------------------
--  Query 1: List courses with NO enrolled students (helpful for scheduling)
--  -------------------------------------------------------------------------
--  Uses LEFT JOIN and IS NULL check.
-- ---------------------------------------------------------------------------
SELECT c.course_code, c.course_name
FROM course c
LEFT JOIN enrollment e ON c.course_id = e.course_id
WHERE e.enrollment_id IS NULL;

-- ---------------------------------------------------------------------------
--  Query 2: Professor workload (how many courses each professor teaches)
--  -------------------------------------------------------------------------
SELECT
    CONCAT(p.first_name, ' ', p.last_name) AS professor,
    d.dept_name,
    COUNT(c.course_id) AS courses_teaching
FROM professor p
LEFT JOIN course c ON p.prof_id = c.prof_id
JOIN department d ON p.dept_id = d.dept_id
GROUP BY p.prof_id
ORDER BY courses_teaching DESC;

-- ---------------------------------------------------------------------------
--  Query 3: Student GPA report (all semesters combined)
--  -------------------------------------------------------------------------
--  Converts letter grades to numeric GPA and averages per student.
-- ---------------------------------------------------------------------------
SELECT
    s.student_id,
    CONCAT(s.first_name, ' ', s.last_name) AS name,
    d.dept_name,
    ROUND(AVG(
        CASE e.grade
            WHEN 'A'  THEN 4.0
            WHEN 'A-' THEN 3.7
            WHEN 'B+' THEN 3.3
            WHEN 'B'  THEN 3.0
            WHEN 'B-' THEN 2.7
            WHEN 'C+' THEN 2.3
            WHEN 'C'  THEN 2.0
            ELSE NULL
        END
    ), 2) AS cumulative_gpa,
    COUNT(e.course_id) AS total_courses_taken
FROM student s
JOIN department d ON s.dept_id = d.dept_id
LEFT JOIN enrollment e ON s.student_id = e.student_id
GROUP BY s.student_id
ORDER BY cumulative_gpa DESC;

-- ---------------------------------------------------------------------------
--  Query 4: Department-wise enrollment statistics (using subquery in FROM)
--  -------------------------------------------------------------------------
SELECT
    d.dept_name,
    dept_stats.total_students,
    dept_stats.total_enrollments,
    ROUND(dept_stats.total_enrollments / NULLIF(dept_stats.total_students, 0), 1) AS avg_courses_per_student
FROM department d
LEFT JOIN (
    SELECT
        s.dept_id,
        COUNT(DISTINCT s.student_id)  AS total_students,
        COUNT(e.enrollment_id)        AS total_enrollments
    FROM student s
    LEFT JOIN enrollment e ON s.student_id = e.student_id
    GROUP BY s.dept_id
) dept_stats ON d.dept_id = dept_stats.dept_id
ORDER BY total_enrollments DESC;

-- ===========================================================================
--  END OF UNIVERSITY DATABASE SCRIPT
--  =========================================================================
--  Queries demonstrated:
--    - All 6 join types (INNER, LEFT, RIGHT, FULL, CROSS, SELF)
--    - Aggregation with GROUP BY / HAVING
--    - Subqueries in WHERE and FROM
--    - CASE expressions for grade conversion
--    - COALESCE for NULL handling
--    - Complex multi-table joins
-- ===========================================================================
