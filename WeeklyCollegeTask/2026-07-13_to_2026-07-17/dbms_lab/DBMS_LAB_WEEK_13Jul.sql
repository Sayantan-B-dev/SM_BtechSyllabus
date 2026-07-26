-- Create database

DROP DATABASE IF EXISTS Student;
CREATE DATABASE Student;
USE Student;

-- Q1. Create the STUDENT table

CREATE TABLE STUDENT (
    Student_roll INT PRIMARY KEY,
    Student_name VARCHAR(30),
    Address VARCHAR(50),
    DOB DATE,
    Dept VARCHAR(10),
    Phone_no BIGINT,
    Marks FLOAT
);

-- Q2. Show the table structure

DESC STUDENT;

-- Q3. Insert 5 records

INSERT INTO STUDENT
(Student_roll, Student_name, Address, DOB, Dept, Phone_no, Marks)
VALUES
(12, 'Sayantan Das', 'Kolkata', '2004-08-15', 'CSE', 912345678, 9.8),
(13, 'Arijit Banerjee', 'Howrah', '2004-02-10', 'CSE', 923456789, 9.4),
(14, 'Souvik Chatterjee', 'Barasat', '2004-11-18', 'ECE', 934567891, 9.1),
(15, 'Aniket Mukherjee', 'Dum Dum', '2005-01-05', 'CSE', 945678912, 9.6),
(16, 'Rohan Ghosh', 'Salt Lake', '2004-06-25', 'IT', 956789123, 9.3);

-- Q4. Display all records

SELECT * FROM STUDENT;

-- Q5. Find the student(s) from Kolkata

SELECT *
FROM STUDENT
WHERE Address = 'Kolkata';

-- Q6. Display details of students from the CSE department

SELECT *
FROM STUDENT
WHERE Dept = 'CSE';

-- Q7. Display only the marks of all students

SELECT Marks
FROM STUDENT;

-- Q8. Display only Student Name and Roll Number

SELECT Student_name, Student_roll
FROM STUDENT;

-- Q9. Delete the record whose roll number is 14

DELETE FROM STUDENT
WHERE Student_roll = 14;

-- Verify deletion

SELECT * FROM STUDENT;

-- Q10. Drop the STUDENT table

DROP TABLE STUDENT;