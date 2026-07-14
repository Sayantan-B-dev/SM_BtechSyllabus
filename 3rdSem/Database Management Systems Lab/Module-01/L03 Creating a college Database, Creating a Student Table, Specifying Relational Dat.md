# Creating a college Database, Creating a Student Table, Specifying Relational Data Types, Specifying Constraints, and Creating Indices.

**Course:** Database Management Systems Lab  
**Module:** 1 | **Lecture:** 3  
**Date:** 20-Jul-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 2  
**Learning Methodology:** Hands-on Experience  
**Reference:** Lab manual

## Lab Objectives

- Create a complete College database with Department, Professor, Student, Course, and Enrollment tables.
- Use ALTER TABLE to add and modify columns.
- Use DESC to view table structures and insert sample records.

## Theory / Concept

A normalized college database captures the relationships between departments, professors, students, and courses. ALTER TABLE allows modification of existing table schemas without dropping them -- you can add, drop, or modify columns, as well as add or drop constraints. DESC (or DESCRIBE) shows the column definitions of a table including data types, nullability, keys, and defaults.

## SQL Code

```sql
-- Create College database
CREATE DATABASE CollegeDB;
USE CollegeDB;

-- Create Department table
CREATE TABLE Department (
    dept_id INT PRIMARY KEY AUTO_INCREMENT,
    dept_name VARCHAR(100) NOT NULL UNIQUE,
    location VARCHAR(100),
    budget DECIMAL(12,2) DEFAULT 0.00
);

-- Create Professor table
CREATE TABLE Professor (
    prof_id INT PRIMARY KEY AUTO_INCREMENT,
    prof_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15),
    dept_id INT,
    hire_date DATE DEFAULT (CURRENT_DATE),
    salary DECIMAL(10,2),
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
);

-- Create Student table
CREATE TABLE Student (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    student_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15),
    dob DATE,
    dept_id INT,
    enrollment_year YEAR DEFAULT (YEAR(CURRENT_DATE)),
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id)
);

-- Create Course table
CREATE TABLE Course (
    course_id INT PRIMARY KEY AUTO_INCREMENT,
    course_code VARCHAR(20) UNIQUE NOT NULL,
    course_name VARCHAR(200) NOT NULL,
    credits INT NOT NULL CHECK (credits BETWEEN 1 AND 6),
    dept_id INT,
    prof_id INT,
    FOREIGN KEY (dept_id) REFERENCES Department(dept_id),
    FOREIGN KEY (prof_id) REFERENCES Professor(prof_id)
);

-- Create Enrollment table
CREATE TABLE Enrollment (
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    semester VARCHAR(10) NOT NULL,
    year YEAR NOT NULL,
    grade VARCHAR(2),
    FOREIGN KEY (student_id) REFERENCES Student(student_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES Course(course_id) ON DELETE CASCADE,
    UNIQUE KEY (student_id, course_id, semester, year)
);

-- ALTER TABLE examples: add a new column
ALTER TABLE Student ADD COLUMN address VARCHAR(255);

-- Modify existing column data type
ALTER TABLE Student MODIFY COLUMN phone VARCHAR(20);

-- Add a CHECK constraint using ALTER
ALTER TABLE Professor ADD CONSTRAINT chk_salary CHECK (salary >= 0);

-- DESC tables
DESC Department;
DESC Professor;
DESC Student;
DESC Course;
DESC Enrollment;

-- Insert sample records
INSERT INTO Department (dept_name, location, budget) VALUES
('Computer Science', 'Block A', 500000.00),
('Mathematics', 'Block B', 300000.00),
('Physics', 'Block C', 400000.00);

INSERT INTO Professor (prof_name, email, phone, dept_id, salary) VALUES
('Dr. Anupam Das', 'adas@college.edu', '1112223333', 1, 95000.00),
('Dr. Suman Roy', 'sroy@college.edu', '4445556666', 2, 85000.00),
('Dr. Priya Singh', 'psingh@college.edu', '7778889999', 3, 90000.00);

INSERT INTO Student (student_name, email, phone, dob, dept_id) VALUES
('Rahul Verma', 'rahul.v@college.edu', '1234567890', '2002-05-14', 1),
('Sneha Patel', 'sneha.p@college.edu', '0987654321', '2001-11-20', 2),
('Amit Kumar', 'amit.k@college.edu', '1122334455', '2003-02-10', 1),
('Neha Gupta', 'neha.g@college.edu', '5566778899', '2002-07-30', 3);

INSERT INTO Course (course_code, course_name, credits, dept_id, prof_id) VALUES
('CS101', 'Database Systems', 4, 1, 1),
('CS102', 'Data Structures', 4, 1, 1),
('MATH201', 'Linear Algebra', 3, 2, 2),
('PHY301', 'Quantum Mechanics', 3, 3, 3);

INSERT INTO Enrollment (student_id, course_id, semester, year) VALUES
(1, 1, 'Fall', 2026),
(1, 2, 'Fall', 2026),
(2, 3, 'Fall', 2026),
(3, 1, 'Fall', 2026),
(4, 4, 'Fall', 2026),
(3, 2, 'Fall', 2026);

-- View all data
SELECT * FROM Department;
SELECT * FROM Professor;
SELECT * FROM Student;
SELECT * FROM Course;
SELECT * FROM Enrollment;
```

## Expected Output

```
mysql> DESC Student;
+-----------------+--------------+------+-----+---------+----------------+
| Field           | Type         | Null | Key | Default | Extra          |
+-----------------+--------------+------+-----+---------+----------------+
| student_id      | int          | NO   | PRI | NULL    | auto_increment |
| student_name    | varchar(100) | NO   |     | NULL    |                |
| email           | varchar(100) | NO   | UNI | NULL    |                |
| phone           | varchar(20)  | YES  |     | NULL    |                |
| dob             | date         | YES  |     | NULL    |                |
| dept_id         | int          | YES  | MUL | NULL    |                |
| enrollment_year | year         | YES  |     | NULL    |                |
| address         | varchar(255) | YES  |     | NULL    |                |
+-----------------+--------------+------+-----+---------+----------------+
8 rows in set (0.01 sec)

mysql> SELECT * FROM Department;
+---------+------------------+----------+-----------+
| dept_id | dept_name        | location | budget    |
+---------+------------------+----------+-----------+
|       1 | Computer Science | Block A  | 500000.00 |
|       2 | Mathematics      | Block B  | 300000.00 |
|       3 | Physics          | Block C  | 400000.00 |
+---------+------------------+----------+-----------+
3 rows in set (0.00 sec)

mysql> SELECT * FROM Course;
+-----------+-------------+------------------+---------+---------+---------+
| course_id | course_code | course_name      | credits | dept_id | prof_id |
+-----------+-------------+------------------+---------+---------+---------+
|         1 | CS101       | Database Systems |       4 |       1 |       1 |
|         2 | CS102       | Data Structures  |       4 |       1 |       1 |
|         3 | MATH201     | Linear Algebra   |       3 |       2 |       2 |
|         4 | PHY301      | Quantum Mechanics|       3 |       3 |       3 |
+-----------+-------------+------------------+---------+---------+---------+
4 rows in set (0.00 sec)
```

## Homework / Practice

1. Add a `date_of_joining` column to the Professor table using ALTER TABLE. Then add a `CHECK` constraint to ensure `salary` is between 30000 and 200000.
   <details>
   <summary>Show Answer</summary>
   ALTER TABLE Professor ADD COLUMN date_of_joining DATE; ALTER TABLE Professor ADD CONSTRAINT chk_prof_salary CHECK (salary BETWEEN 30000 AND 200000);
   </details>

2. Insert two more students and enroll each of them in at least two courses.
   <details>
   <summary>Show Answer</summary>
   INSERT INTO Student VALUES (4, 'David', 'EE', 2023), (5, 'Eve', 'CSE', 2023); INSERT INTO Enrollment VALUES (4, 101, 'A'), (4, 102, 'B'), (5, 101, 'A'), (5, 103, 'A');
   </details>

3. Use DESC to view the structure of the Enrollment table and explain what each column and constraint means.
   <details>
   <summary>Show Answer</summary>
   DESC Enrollment; The Enrollment table has columns: student_id (FK references Student), course_id (FK references Course), grade (VARCHAR). The primary key is (student_id, course_id). Foreign key constraints ensure referential integrity.
   </details>
