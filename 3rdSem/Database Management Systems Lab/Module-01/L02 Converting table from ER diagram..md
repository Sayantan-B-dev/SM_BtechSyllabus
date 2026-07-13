# Converting table from ER diagram.

**Course:** Database Management Systems Lab  
**Module:** 1 | **Lecture:** 2  
**Date:** 13-Jul-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 1  
**Learning Methodology:** Hands-on Experience  
**Reference:** Lab manual

## Lab Objectives

- Convert a Library Management ER diagram (Book, Member, Loan) into relational tables.
- Use CHECK constraints and DEFAULT values in table definitions.
- Insert sample data into the tables and verify via SELECT queries.

## Theory / Concept

CHECK constraints enforce domain integrity by limiting the values that can be placed in a column. DEFAULT values automatically populate a column when no value is specified during INSERT. In a Library Management system, the Loan table captures the many-to-many relationship between Book and Member, with attributes like issue_date, due_date, and return_date. Constraints ensure that due dates are after issue dates and that only valid status values are entered.

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
    category VARCHAR(50) DEFAULT 'General',
    published_year INT CHECK (published_year >= 1000 AND published_year <= YEAR(CURDATE())),
    total_copies INT DEFAULT 1 CHECK (total_copies >= 0),
    available_copies INT DEFAULT 1 CHECK (available_copies >= 0)
);

-- Create Member table
CREATE TABLE Member (
    member_id INT PRIMARY KEY AUTO_INCREMENT,
    member_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15),
    membership_type VARCHAR(20) DEFAULT 'Standard' CHECK (membership_type IN ('Standard', 'Premium', 'Student')),
    join_date DATE DEFAULT (CURRENT_DATE),
    max_books_allowed INT DEFAULT 3 CHECK (max_books_allowed BETWEEN 1 AND 10)
);

-- Create Loan table
CREATE TABLE Loan (
    loan_id INT PRIMARY KEY AUTO_INCREMENT,
    book_id INT NOT NULL,
    member_id INT NOT NULL,
    issue_date DATE NOT NULL DEFAULT (CURRENT_DATE),
    due_date DATE NOT NULL,
    return_date DATE,
    status VARCHAR(20) DEFAULT 'Issued' CHECK (status IN ('Issued', 'Returned', 'Overdue', 'Lost')),
    fine_amount DECIMAL(10,2) DEFAULT 0.00 CHECK (fine_amount >= 0),
    FOREIGN KEY (book_id) REFERENCES Book(book_id) ON DELETE CASCADE,
    FOREIGN KEY (member_id) REFERENCES Member(member_id) ON DELETE CASCADE,
    CHECK (due_date > issue_date),
    CHECK (return_date IS NULL OR return_date >= issue_date)
);

-- Insert sample books
INSERT INTO Book (isbn, title, author, category, published_year, total_copies, available_copies) VALUES
('978-0-13-110362-7', 'The C Programming Language', 'Brian Kernighan', 'Programming', 1978, 5, 5),
('978-0-596-52068-7', 'Learning Python', 'Mark Lutz', 'Programming', 2013, 3, 3),
('978-0-12-374856-0', 'Database System Concepts', 'Abraham Silberschatz', 'Database', 2010, 4, 4);

-- Insert sample members
INSERT INTO Member (member_name, email, phone, membership_type) VALUES
('Alice Johnson', 'alice@example.com', '1234567890', 'Premium'),
('Bob Smith', 'bob@example.com', '0987654321', 'Student'),
('Carol White', 'carol@example.com', '1122334455', 'Standard');

-- Insert sample loans
INSERT INTO Loan (book_id, member_id, due_date) VALUES
(1, 1, '2026-08-15'),
(2, 2, '2026-08-10'),
(3, 3, '2026-08-20');

-- Return a book
UPDATE Loan SET return_date = '2026-07-20', status = 'Returned' WHERE loan_id = 1;

-- View all data
SELECT * FROM Book;
SELECT * FROM Member;
SELECT * FROM Loan;
```

## Expected Output

```
mysql> SELECT * FROM Book;
+---------+-----------------+--------------------------+---------------------+-------------+----------------+---------------+------------------+
| book_id | isbn            | title                    | author              | category    | published_year | total_copies  | available_copies |
+---------+-----------------+--------------------------+---------------------+-------------+----------------+---------------+------------------+
|       1 | 978-0-13-110362-7 | The C Programming Language | Brian Kernighan     | Programming |          1978 |             5 |                5 |
|       2 | 978-0-596-52068-7 | Learning Python           | Mark Lutz           | Programming |          2013 |             3 |                3 |
|       3 | 978-0-12-374856-0 | Database System Concepts  | Abraham Silberschatz | Database    |          2010 |             4 |                4 |
+---------+-----------------+--------------------------+---------------------+-------------+----------------+---------------+------------------+
3 rows in set (0.00 sec)

mysql> SELECT * FROM Member;
+-----------+--------------+------------------+------------+-----------------+------------+--------------------+
| member_id | member_name  | email            | phone      | membership_type | join_date  | max_books_allowed  |
+-----------+--------------+------------------+------------+-----------------+------------+--------------------+
|         1 | Alice Johnson | alice@example.com| 1234567890 | Premium         | 2026-07-13 |                  3 |
|         2 | Bob Smith    | bob@example.com  | 0987654321 | Student         | 2026-07-13 |                  3 |
|         3 | Carol White  | carol@example.com| 1122334455 | Standard        | 2026-07-13 |                  3 |
+-----------+--------------+------------------+------------+-----------------+------------+--------------------+
3 rows in set (0.00 sec)

mysql> SELECT * FROM Loan;
+---------+---------+-----------+------------+------------+-------------+----------+-------------+
| loan_id | book_id | member_id | issue_date | due_date   | return_date | status   | fine_amount |
+---------+---------+-----------+------------+------------+-------------+----------+-------------+
|       1 |       1 |         1 | 2026-07-13 | 2026-08-15 | 2026-07-20  | Returned |        0.00 |
|       2 |       2 |         2 | 2026-07-13 | 2026-08-10 | NULL        | Issued   |        0.00 |
|       3 |       3 |         3 | 2026-07-13 | 2026-08-20 | NULL        | Issued   |        0.00 |
+---------+---------+-----------+------------+------------+-------------+----------+-------------+
3 rows in set (0.00 sec)
```

## Homework / Practice

1. Add a CHECK constraint to ensure `return_date` is not earlier than `issue_date` (already done; write a similar constraint for `fine_amount` to cap it at 500).
2. Insert a new member of type 'Premium' with max_books_allowed = 7. Then insert a loan for that member.
3. Write a query to list all books that have available_copies > 0 and are of category 'Programming'.
