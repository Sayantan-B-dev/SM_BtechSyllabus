# Employee Management System- Where clause with IN, BETWEEN, LIKE, ORDER BY, GROUP BY and HAVING Clause

**Course:** Database Management Systems Lab  
**Module:** 3 | **Lecture:** 6  
**Date:** 31-Aug-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 2  
**Learning Methodology:** Hands-on Experience  
**Reference:** Lab manual

## Lab Objectives

- Use LIKE operator with wildcards % and _ for pattern matching.
- Use ORDER BY to sort results in ascending and descending order by multiple columns.
- Use GROUP BY with HAVING to filter grouped data.

## Theory / Concept

LIKE performs pattern matching: % matches any sequence of characters (including zero), and _ matches exactly one character. ORDER BY sorts query results -- ASC for ascending (default), DESC for descending. Multiple columns can be specified for sorting (e.g., ORDER BY department ASC, salary DESC). GROUP BY groups rows, and HAVING filters the groups after aggregation.

## SQL Code

```sql
USE EmployeeDB;

-- LIKE: names starting with 'A'
SELECT emp_name, department
FROM Employee
WHERE emp_name LIKE 'A%';

-- LIKE: names ending with 'a'
SELECT emp_name, department
FROM Employee
WHERE emp_name LIKE '%a';

-- LIKE: names containing 'it'
SELECT emp_name, department
FROM Employee
WHERE emp_name LIKE '%it%';

-- LIKE with underscore: exactly 5-letter names
SELECT emp_name, department
FROM Employee
WHERE emp_name LIKE '_____';

-- LIKE: email domain pattern
SELECT emp_name, email
FROM Employee
WHERE email LIKE '%@company.com';

-- NOT LIKE
SELECT emp_name, email
FROM Employee
WHERE emp_name NOT LIKE 'A%';

-- ORDER BY single column (salary descending)
SELECT emp_name, salary
FROM Employee
ORDER BY salary DESC;

-- ORDER BY multiple columns
SELECT department, emp_name, salary
FROM Employee
ORDER BY department ASC, salary DESC;

-- ORDER BY with LIMIT
SELECT emp_name, salary
FROM Employee
ORDER BY salary DESC
LIMIT 5;

-- GROUP BY with HAVING
SELECT department, COUNT(*) AS emp_count, AVG(salary) AS avg_salary
FROM Employee
GROUP BY department
HAVING COUNT(*) >= 2
ORDER BY avg_salary DESC;

-- LIKE + ORDER BY combined
SELECT emp_name, department, salary
FROM Employee
WHERE emp_name LIKE 'S%' OR emp_name LIKE 'K%'
ORDER BY department, salary DESC;
```

## Expected Output

```
mysql> SELECT emp_name, department FROM Employee WHERE emp_name LIKE 'A%';
+-------------+------------+
| emp_name    | department |
+-------------+------------+
| Amit Joshi  | Finance    |
| Ananya Das  | IT         |
+-------------+------------+

mysql> SELECT emp_name, department FROM Employee WHERE emp_name LIKE '%it%';
+-------------+------------+
| emp_name    | department |
+-------------+------------+
| Amit Joshi  | Finance    |
| Rohit Verma | Sales      |
+-------------+------------+

mysql> SELECT department, emp_name, salary
FROM Employee ORDER BY department ASC, salary DESC;
+------------+--------------+----------+
| department | emp_name     | salary   |
+------------+--------------+----------+
| Finance    | Sneha Kapoor | 85000.00 |
| Finance    | Amit Joshi   | 55000.00 |
| HR         | Meera Iyer   | 78000.00 |
| HR         | Vikram Singh | 50000.00 |
| IT         | Priya Mehta  |109500.00 |
| IT         | Karan Patel  |100000.00 |
| IT         | Ananya Das   | 93000.00 |
| IT         | Ravi Sharma  | 87500.00 |
| Sales      | Neha Agarwal | 90000.00 |
| Sales      | Rohit Verma  | 60000.00 |
+------------+--------------+----------+

mysql> SELECT department, COUNT(*) AS emp_count, AVG(salary) AS avg_salary
FROM Employee GROUP BY department HAVING COUNT(*) >= 2 ORDER BY avg_salary DESC;
+------------+-----------+---------------+
| department | emp_count | avg_salary    |
+------------+-----------+---------------+
| IT         |         4 |  97500.000000 |
| Sales      |         2 |  75000.000000 |
| Finance    |         2 |  70000.000000 |
| HR         |         2 |  64000.000000 |
+------------+-----------+---------------+
```

## Homework / Practice

1. Find all employees whose name contains the letter 'e' as the second character (use _ pattern).
   <details>
   <summary>Show Answer</summary>
   SELECT * FROM Employee WHERE emp_name LIKE '_e%';
   </details>

2. List employees sorted by hire_date in descending order (newest first), and limit to the 3 most recent hires.
   <details>
   <summary>Show Answer</summary>
   SELECT * FROM Employee ORDER BY hire_date DESC LIMIT 3;
   </details>

3. Use GROUP BY to find departments where the total salary expense exceeds 150000, sorted by total expense descending.
   <details>
   <summary>Show Answer</summary>
   SELECT department, SUM(salary) AS total_salary FROM Employee GROUP BY department HAVING SUM(salary) > 150000 ORDER BY total_salary DESC;
   </details>
