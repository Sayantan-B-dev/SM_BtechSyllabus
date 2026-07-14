# Converting table from ER diagram.

**Course:** Database Management Systems Lab  
**Module:** 1 | **Lecture:** 1  
**Date:** 13-Jul-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 1  
**Learning Methodology:** Hands-on Experience  
**Reference:** Lab manual

## Lab Objectives

- Understand the process of converting an ER diagram into relational tables.
- Learn to use CREATE DATABASE and CREATE TABLE statements with primary and foreign key constraints.
- Implement a Student-Course enrollment system with proper referential integrity.

## Theory / Concept

An ER (Entity-Relationship) diagram models real-world entities and their relationships. Converting an ER diagram to relational tables follows these rules: each entity becomes a table, attributes become columns, and relationships are represented through foreign keys. For a many-to-many relationship like Student-Course enrollment, a junction table (Enrollment) is created with foreign keys referencing both entity tables. Primary keys uniquely identify rows, while foreign keys enforce referential integrity between related tables.

## SQL Code

```sql
-- Create the database
CREATE DATABASE StudentCourseDB;
USE StudentCourseDB;

-- Create Student table
CREATE TABLE Student (
    student_id INT PRIMARY KEY,
    student_name VARCHAR(50) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15),
    dob DATE
);

-- Create Course table
CREATE TABLE Course (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL,
    credits INT NOT NULL CHECK (credits > 0),
    instructor VARCHAR(50)
);

-- Create Enrollment table (junction table for many-to-many relationship)
CREATE TABLE Enrollment (
    enrollment_id INT PRIMARY KEY AUTO_INCREMENT,
    student_id INT NOT NULL,
    course_id INT NOT NULL,
    enrollment_date DATE DEFAULT (CURRENT_DATE),
    grade CHAR(2),
    FOREIGN KEY (student_id) REFERENCES Student(student_id) ON DELETE CASCADE,
    FOREIGN KEY (course_id) REFERENCES Course(course_id) ON DELETE CASCADE,
    UNIQUE (student_id, course_id)
);

-- Show all tables
SHOW TABLES;

-- Describe table structure
DESC Student;
DESC Course;
DESC Enrollment;
```

## Expected Output

```
mysql> SHOW TABLES;
+---------------------------+
| Tables_in_StudentCourseDB |
+---------------------------+
| course                    |
| enrollment                |
| student                   |
+---------------------------+
3 rows in set (0.01 sec)

mysql> DESC Student;
+--------------+--------------+------+-----+---------+-------+
| Field        | Type         | Null | Key | Default | Extra |
+--------------+--------------+------+-----+---------+-------+
| student_id   | int          | NO   | PRI | NULL    |       |
| student_name | varchar(50)  | NO   |     | NULL    |       |
| email        | varchar(100) | NO   | UNI | NULL    |       |
| phone        | varchar(15)  | YES  |     | NULL    |       |
| dob          | date         | YES  |     | NULL    |       |
+--------------+--------------+------+-----+---------+-------+
5 rows in set (0.01 sec)

mysql> DESC Course;
+-------------+--------------+------+-----+---------+-------+
| Field       | Type         | Null | Key | Default | Extra |
+-------------+--------------+------+-----+---------+-------+
| course_id   | int          | NO   | PRI | NULL    |       |
| course_name | varchar(100) | NO   |     | NULL    |       |
| credits     | int          | NO   |     | NULL    |       |
| instructor  | varchar(50)  | YES  |     | NULL    |       |
+-------------+--------------+------+-----+---------+-------+
4 rows in set (0.01 sec)

mysql> DESC Enrollment;
+-----------------+-------------+------+-----+-----------+----------------+
| Field           | Type        | Null | Key | Default   | Extra          |
+-----------------+-------------+------+-----+-----------+----------------+
| enrollment_id   | int         | NO   | PRI | NULL      | auto_increment |
| student_id      | int         | NO   | MUL | NULL      |                |
| course_id       | int         | NO   | MUL | NULL      |                |
| enrollment_date | date        | YES  |     | curdate() |                |
| grade           | char(2)     | YES  |     | NULL      |                |
+-----------------+-------------+------+-----+-----------+----------------+
5 rows in set (0.01 sec)
```

## Homework / Practice

1. Draw an ER diagram for a Hospital system (Doctor, Patient, Appointment) and convert it to SQL tables.
   <details>
   <summary>Show Answer</summary>
   ER Diagram: Doctor (doc_id PK, name, specialization, phone), Patient (pat_id PK, name, phone, address), Appointment (app_id PK, doc_id FK, pat_id FK, app_date, status). Doctor--Appointment (1:N), Patient--Appointment (1:N).
   </details>

2. Add a new table `Department` to the StudentCourseDB and link it to the Course table via a foreign key.
   <details>
   <summary>Show Answer</summary>
   CREATE TABLE Department (dept_id INT PRIMARY KEY, dept_name VARCHAR(100)); ALTER TABLE Course ADD COLUMN dept_id INT; ALTER TABLE Course ADD FOREIGN KEY (dept_id) REFERENCES Department(dept_id);
   </details>

3. Write INSERT statements to add 3 students, 2 courses, and enroll each student in at least one course.
   <details>
   <summary>Show Answer</summary>
   INSERT INTO Student VALUES (1, 'Alice', 'CSE', 2022), (2, 'Bob', 'ECE', 2022), (3, 'Charlie', 'ME', 2022); INSERT INTO Course VALUES (101, 'DBMS', 4), (102, 'OS', 3); INSERT INTO Enrollment VALUES (1, 101, 'A'), (2, 101, 'B'), (3, 102, 'A'), (1, 102, 'B');
   </details>
