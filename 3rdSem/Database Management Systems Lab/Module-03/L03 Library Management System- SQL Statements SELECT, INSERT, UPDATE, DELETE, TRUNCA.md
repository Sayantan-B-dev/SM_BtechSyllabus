# Library Management System- SQL Statements SELECT, INSERT, UPDATE, DELETE, TRUNCATE, DROP, ALTER

**Course:** Database Management Systems Lab  
**Module:** 3 | **Lecture:** 3  
**Date:** 17-Aug-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 2  
**Learning Methodology:** Hands-on Experience  
**Reference:** Lab manual

## Lab Objectives

- Perform advanced queries on the Library database: count books by category.
- Find the most borrowed books and rank them.
- Identify members with more than 3 loans.

## Theory / Concept

Advanced queries combine aggregate functions with GROUP BY, HAVING, and JOIN to extract meaningful insights. COUNT, SUM, and ORDER BY help analyze borrowing patterns. By joining Loan with Book, we can determine which books are most popular. HAVING filters groups, allowing us to find heavy borrowers. Subqueries can be used to find members with loan counts above a threshold.

## SQL Code

```sql
USE LibraryDB;

-- Count books by category
SELECT category, COUNT(*) AS total_books
FROM Book
GROUP BY category
ORDER BY total_books DESC;

-- Most borrowed books (books with highest loan count)
SELECT
    b.book_id,
    b.title,
    b.author,
    COUNT(l.loan_id) AS borrow_count
FROM Book b
LEFT JOIN Loan l ON b.book_id = l.book_id
GROUP BY b.book_id, b.title, b.author
ORDER BY borrow_count DESC;

-- Members with more than 3 loans
SELECT
    m.member_id,
    m.member_name,
    m.email,
    COUNT(l.loan_id) AS total_loans
FROM Member m
JOIN Loan l ON m.member_id = l.member_id
GROUP BY m.member_id, m.member_name, m.email
HAVING COUNT(l.loan_id) > 3;

-- Average number of days books are kept before return
SELECT
    AVG(DATEDIFF(return_date, issue_date)) AS avg_borrow_days
FROM Loan
WHERE return_date IS NOT NULL;

-- Books currently issued (not returned)
SELECT
    b.title,
    m.member_name,
    l.issue_date,
    l.due_date,
    DATEDIFF(l.due_date, CURDATE()) AS days_remaining
FROM Loan l
JOIN Book b ON l.book_id = b.book_id
JOIN Member m ON l.member_id = m.member_id
WHERE l.return_date IS NULL
ORDER BY days_remaining;

-- Category-wise borrowing statistics
SELECT
    b.category,
    COUNT(l.loan_id) AS total_loans,
    COUNT(DISTINCT l.member_id) AS unique_borrowers
FROM Book b
LEFT JOIN Loan l ON b.book_id = l.book_id
GROUP BY b.category
ORDER BY total_loans DESC;

-- Author popularity ranking
SELECT
    author,
    COUNT(l.loan_id) AS total_loans
FROM Book b
LEFT JOIN Loan l ON b.book_id = l.book_id
GROUP BY author
ORDER BY total_loans DESC;
```

## Expected Output

```
mysql> SELECT category, COUNT(*) AS total_books FROM Book GROUP BY category ORDER BY total_books DESC;
+-------------+-------------+
| category    | total_books |
+-------------+-------------+
| Programming |           2 |
| Database    |           1 |
| OS          |           1 |
| Networking  |           1 |
+-------------+-------------+

mysql> SELECT b.title, COUNT(l.loan_id) AS borrow_count
FROM Book b LEFT JOIN Loan l ON b.book_id = l.book_id
GROUP BY b.title ORDER BY borrow_count DESC;
+-----------------------------+--------------+
| title                       | borrow_count |
+-----------------------------+--------------+
| The C Programming Language  |            2 |
| Learning Python             |            2 |
| Database System Concepts    |            1 |
| Operating System Concepts   |            1 |
| Computer Networks           |            1 |
+-----------------------------+--------------+

mysql> -- Members with > 3 loans (none currently, so let's add data)
-- (In practice, after adding more loans, the query would return results)

mysql> SELECT b.category, COUNT(l.loan_id) AS total_loans, COUNT(DISTINCT l.member_id) AS unique_borrowers
FROM Book b LEFT JOIN Loan l ON b.book_id = l.book_id GROUP BY b.category;
+-------------+-------------+------------------+
| category    | total_loans | unique_borrowers |
+-------------+-------------+------------------+
| Database    |           1 |                1 |
| Networking  |           1 |                1 |
| OS          |           1 |                1 |
| Programming |           4 |                3 |
+-------------+-------------+------------------+
```

## Homework / Practice

1. Insert additional loan records and then identify members who have borrowed more than 2 books.
2. Find the most popular author (the author whose books have been borrowed the most times).
3. Write a query that shows the number of loans per month (extract month from issue_date).
