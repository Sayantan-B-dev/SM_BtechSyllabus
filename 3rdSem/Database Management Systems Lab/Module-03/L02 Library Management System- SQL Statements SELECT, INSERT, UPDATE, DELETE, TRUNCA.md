# Library Management System- SQL Statements SELECT, INSERT, UPDATE, DELETE, TRUNCATE, DROP, ALTER

**Course:** Database Management Systems Lab  
**Module:** 3 | **Lecture:** 2  
**Date:** 17-Aug-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 2  
**Learning Methodology:** Hands-on Experience  
**Reference:** Lab manual

## Lab Objectives

- Create a Library database with Book, Member, and Loan tables.
- Write basic SELECT queries with WHERE conditions.
- Find overdue books by comparing due dates with the current date.

## Theory / Concept

SELECT queries retrieve data from one or more tables. The WHERE clause filters rows based on conditions. Date functions like CURDATE() return the current date. Overdue books are those where the due_date has passed and the return_date is NULL. Combining conditions using AND allows precise filtering.

## SQL Code

```sql
-- Create Library database
CREATE DATABASE LibraryDB;
USE LibraryDB;

-- Create Book table
CREATE TABLE Book (
    book_id INT PRIMARY KEY AUTO_INCREMENT,
    isbn VARCHAR(20) UNIQUE NOT NULL,
    title VARCHAR(200) NOT NULL,
    author VARCHAR(100) NOT NULL,
    category VARCHAR(50),
    published_year INT,
    total_copies INT DEFAULT 1,
    available_copies INT DEFAULT 1
);

-- Create Member table
CREATE TABLE Member (
    member_id INT PRIMARY KEY AUTO_INCREMENT,
    member_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15),
    join_date DATE DEFAULT (CURRENT_DATE)
);

-- Create Loan table
CREATE TABLE Loan (
    loan_id INT PRIMARY KEY AUTO_INCREMENT,
    book_id INT NOT NULL,
    member_id INT NOT NULL,
    issue_date DATE NOT NULL,
    due_date DATE NOT NULL,
    return_date DATE,
    status VARCHAR(20) DEFAULT 'Issued',
    FOREIGN KEY (book_id) REFERENCES Book(book_id),
    FOREIGN KEY (member_id) REFERENCES Member(member_id)
);

-- Insert sample books
INSERT INTO Book (isbn, title, author, category, published_year, total_copies, available_copies) VALUES
('978-0-13-110362-7', 'The C Programming Language', 'Brian Kernighan', 'Programming', 1978, 5, 4),
('978-0-596-52068-7', 'Learning Python', 'Mark Lutz', 'Programming', 2013, 3, 2),
('978-0-12-374856-0', 'Database System Concepts', 'Abraham Silberschatz', 'Database', 2010, 4, 3),
('978-0-07-352332-3', 'Operating System Concepts', 'Abraham Silberschatz', 'OS', 2012, 3, 1),
('978-0-13-468599-1', 'Computer Networks', 'Andrew Tanenbaum', 'Networking', 2016, 2, 1);

-- Insert sample members
INSERT INTO Member (member_name, email, phone) VALUES
('Alice Johnson', 'alice@email.com', '1111111111'),
('Bob Smith', 'bob@email.com', '2222222222'),
('Carol White', 'carol@email.com', '3333333333'),
('David Brown', 'david@email.com', '4444444444'),
('Emma Davis', 'emma@email.com', '5555555555');

-- Insert sample loans (some overdue, some returned)
INSERT INTO Loan (book_id, member_id, issue_date, due_date, return_date, status) VALUES
(1, 1, '2026-06-01', '2026-06-15', '2026-06-14', 'Returned'),
(2, 2, '2026-06-10', '2026-06-25', NULL, 'Issued'),
(3, 3, '2026-07-01', '2026-07-15', NULL, 'Issued'),
(4, 4, '2026-05-15', '2026-05-30', NULL, 'Issued'),    -- Overdue
(5, 5, '2026-06-20', '2026-07-05', NULL, 'Issued'),     -- Overdue
(1, 2, '2026-07-10', '2026-07-25', NULL, 'Issued'),
(2, 3, '2026-07-05', '2026-07-20', '2026-07-18', 'Returned');

-- Basic SELECT queries
SELECT * FROM Book;
SELECT * FROM Member;
SELECT * FROM Loan;

-- SELECT with WHERE
SELECT title, author, category FROM Book WHERE category = 'Programming';

-- Find available books (available_copies > 0)
SELECT title, available_copies FROM Book WHERE available_copies > 0;

-- Find overdue books (due before today and not returned)
SELECT
    l.loan_id,
    b.title,
    m.member_name,
    l.issue_date,
    l.due_date,
    DATEDIFF(CURDATE(), l.due_date) AS days_overdue
FROM Loan l
JOIN Book b ON l.book_id = b.book_id
JOIN Member m ON l.member_id = m.member_id
WHERE l.return_date IS NULL AND l.due_date < CURDATE();

-- Find books borrowed by a specific member
SELECT b.title, l.issue_date, l.due_date, l.status
FROM Loan l
JOIN Book b ON l.book_id = b.book_id
WHERE l.member_id = 2;
```

## Expected Output

```
mysql> SELECT title, author, category FROM Book WHERE category = 'Programming';
+--------------------------+-----------------+-------------+
| title                    | author          | category    |
+--------------------------+-----------------+-------------+
| The C Programming Language | Brian Kernighan | Programming |
| Learning Python            | Mark Lutz       | Programming |
+--------------------------+-----------------+-------------+

mysql> SELECT title, available_copies FROM Book WHERE available_copies > 0;
+--------------------------+------------------+
| title                    | available_copies |
+--------------------------+------------------+
| The C Programming Language |                4 |
| Learning Python            |                2 |
| Database System Concepts   |                3 |
| Operating System Concepts  |                1 |
| Computer Networks          |                1 |
+--------------------------+------------------+

mysql> -- Overdue books
SELECT l.loan_id, b.title, m.member_name, l.due_date, DATEDIFF(CURDATE(), l.due_date) AS days_overdue
FROM Loan l JOIN Book b ... WHERE l.return_date IS NULL AND l.due_date < CURDATE();
+---------+--------------------------+-------------+------------+--------------+
| loan_id | title                    | member_name | due_date   | days_overdue |
+---------+--------------------------+-------------+------------+--------------+
|       4 | Operating System Concepts | David Brown | 2026-05-30 |           44 |
|       5 | Computer Networks         | Emma Davis  | 2026-07-05 |            8 |
+---------+--------------------------+-------------+------------+--------------+
```

## Homework / Practice

1. Find all books that were published after the year 2000 and belong to the 'Programming' category.
   <details>
   <summary>Show Answer</summary>
   SELECT * FROM Book WHERE publication_year > 2000 AND category = 'Programming';
   </details>

2. List all members who have not returned a book (i.e., have an active loan with return_date IS NULL).
   <details>
   <summary>Show Answer</summary>
   SELECT DISTINCT m.* FROM Member m INNER JOIN Loan l ON m.member_id = l.member_id WHERE l.return_date IS NULL;
   </details>

3. Write a query to show each member and the count of books they have currently issued (not returned).
   <details>
   <summary>Show Answer</summary>
   SELECT m.member_id, m.member_name, COUNT(l.book_id) AS books_issued FROM Member m INNER JOIN Loan l ON m.member_id = l.member_id WHERE l.return_date IS NULL GROUP BY m.member_id;
   </details>
