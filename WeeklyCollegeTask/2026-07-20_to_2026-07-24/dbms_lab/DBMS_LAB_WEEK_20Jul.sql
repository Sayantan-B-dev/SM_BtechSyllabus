DROP DATABASE IF EXISTS Emp;
CREATE DATABASE Emp;
USE Emp;

-- 1. Creating table Employee with attributes like employee id, first name,last name, address 1 , address 2, phone number, salary, date of joining
SELECT '# TASK 1 : >>>CREATING EMPLOYEE AND DESCRIBING THE SCHEMA<<<' as " ";

CREATE TABLE Employee (
  emp_id VARCHAR(30) PRIMARY KEY,
  first_name VARCHAR(30),
  last_name VARCHAR(30),
  address1 VARCHAR(100),
  address2 VARCHAR(100),
  phn_no BIGINT,
  salary BIGINT,
  DOJ DATE
);
DESC Employee;

-- 2. Inserting data into Employee table
SELECT '# TASK 2 : >>>INSERTING INTO EMPLOYEE TABLE<<<' AS " ";

INSERT INTO Employee 
(emp_id, first_name, last_name, address1, address2, phn_no, salary, DOJ)
VALUES
('0001', 'Sayantan', 'Bharati', 'Kolkata', 'Barasat', 9876543210, 90000, '2025-02-16'),
('0002', 'Sayan', 'Bhoumik', 'Howrah', 'Madhyamgram', 9897643210, 54000, '2024-04-11'),
('0003', 'Sayantani', 'Bhattacharjee', 'New Town', 'Habra', 9871468210, 35000, '2023-11-05');

SELECT * FROM Employee;

-- 3. Creating MASTER table with the same attributes with Employee but changing emp_id to id
SELECT '# TASK 3 : >>>CREATING MASTER TABLE AND DESCRIBING IT<<<' AS " ";

CREATE TABLE MASTER (
  id VARCHAR(30) PRIMARY KEY,
  first_name VARCHAR(30),
  last_name VARCHAR(30),
  address1 VARCHAR(100),
  address2 VARCHAR(100),
  phn_no BIGINT,
  salary BIGINT,
  DOJ DATE
);
DESC MASTER;

-- 4. Deleting all records from MASTER
SELECT '# TASK 4 : >>>DELETING ALL RECORDS FROM MASTER<<<' AS " ";

TRUNCATE TABLE MASTER;
SELECT * FROM MASTER;

-- 5. Inserting data into MASTER table
SELECT '# TASK 5 : >>>INSERTING INTO MASTER TABLE<<<' AS " ";

INSERT INTO MASTER
(id, first_name, last_name, address1, address2, phn_no, salary, DOJ)
VALUES
('001', 'Ankit', 'Roy', 'Kolkata', 'Kolkata', 9870684210, 40000, '2025-02-16'),
('002', 'Aniket', 'Bar', 'Kolkata', 'Chakdah', 9876547810, 50000, '2026-09-06'),
('003', 'Ankita', 'Paul', 'Kalyani', 'Barasat', 9871234210, 70000, '2022-12-04');
SELECT * FROM MASTER;


-- 6. Deleting a row from master where id is 001
SELECT '# TASK 6 : >>>DELETING ROW WITH ID 001 AND DISPLAYING<<<' AS " ";

DELETE FROM MASTER WHERE id="001";
SELECT * FROM MASTER;

-- 7. Updating lastname from master where id is 003
SELECT '# TASK 7 : >>>UPDATING LASTNAME FROM MASTER TABLE WHERE ID IS 003 AND DISPLAYING<<<' AS " ";

UPDATE MASTER SET last_name="Sah" WHERE id='003';
SELECT * FROM MASTER;

-- 8. Adding a new column in MASTER named email id
SELECT '# TASK 8 : >>>ADDING A EMAIL ID COLUMN IN MASTER TABLE<<<' AS " ";


ALTER TABLE MASTER ADD email_id VARCHAR(30);
DESC MASTER;

-- 9. Deleting the column address 2 from MASTER table
SELECT '# TASK 9 : >>>DELETING THE ADDRESS 2 COLUMN FROM MASTER TABLE<<<' AS " ";

ALTER TABLE MASTER DROP COLUMN address2;
DESC MASTER;

-- 10. Renaming the MASTER table to MID
SELECT '# TASK 10 : >>>RENAMING THE MASTER TABLE TO MID<<<' AS " ";

RENAME TABLE MASTER TO MID;
DESC MID;

-- 11. Dropping the MID table
SELECT '# TASK 11 : >>>DROPPING THE MID TABLE<<<' AS " ";

TRUNCATE TABLE MID;
