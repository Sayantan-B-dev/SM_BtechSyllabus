DROP DATABASE IF EXISTS Emp;
CREATE DATABASE Emp;
USE Emp;

-- 1. Creating table Employee with attributes like employee id, first name,last name, address 1 , address 2, phone number, salary, date of joining
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
INSERT INTO Employee 
(emp_id, first_name, last_name, address1, address2, phn_no, salary, DOJ)
VALUES
('0001', 'Sayantan', 'Bharati', 'Kolkata', 'Barasat', 9876543210, 90000, '2025-02-16'),
('0002', 'Sayan', 'Bhoumik', 'Howrah', 'Madhyamgram', 9897643210, 54000, '2024-04-11'),
('0003', 'Sayantani', 'Bhattacharjee', 'New Town', 'Habra', 9871468210, 35000, '2023-11-05');

SELECT * FROM Employee;

-- 3. Creating MASTER table with the same attributes with Employee but changing emp_id to id
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
TRUNCATE TABLE MASTER;
SELECT * FROM MASTER;

-- 5. Inserting data into MASTER table
INSERT INTO MASTER
(id, first_name, last_name, address1, address2, phn_no, salary, DOJ)
VALUES
('001', 'Ankit', 'Roy', 'Kolkata', 'Kolkata', 9870684210, 40000, '2025-02-16'),
('002', 'Aniket', 'Bar', 'Kolkata', 'Chakdah', 9876547810, 50000, '2026-09-06'),
('003', 'Ankita', 'Paul', 'Kalyani', 'Barasat', 9871234210, 70000, '2022-12-04');
SELECT * FROM MASTER;


-- 6. Deleting a row from master where id is 001
DELETE FROM MASTER WHERE id="001";
SELECT * FROM MASTER;

-- 7. Updating lastname from master where id is 003
UPDATE MASTER SET last_name="Sah" WHERE id='003';
SELECT * FROM MASTER;

-- 8. Adding a new column in MASTER named email id

ALTER TABLE MASTER ADD email_id VARCHAR(30);
DESC MASTER;

-- 9. Deleting the column address 2 from MASTER table
ALTER TABLE MASTER DROP COLUMN address2;
DESC MASTER;

-- 10. Renaming the MASTER table to MID
RENAME TABLE MASTER TO MID;
DESC MID;

-- 11. Dropping the MID table
TRUNCATE TABLE MID;
