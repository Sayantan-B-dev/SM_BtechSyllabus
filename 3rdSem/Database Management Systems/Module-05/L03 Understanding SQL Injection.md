# Understanding SQL Injection

**Course:** Database Management Systems  
**Module:** 5 | **Lecture:** 3  
**Date:** 30-Oct-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 5  
**Learning Methodology:** Chalk & Talk  
**Reference:** Korth & Silberschatz Database System Concepts (7th Ed.)

## What is SQL Injection?

SQL Injection (SQLi) is a code injection technique where an attacker inserts malicious SQL statements into an application's input fields. When the application fails to properly validate or sanitize user input, the SQL statement is executed by the database server. SQL injection remains one of the most critical and common web application vulnerabilities (consistently ranked in the OWASP Top 10).

## How SQL Injection Works

The root cause: **user input is concatenated directly into a SQL query string**, allowing the input to alter the intended SQL syntax.

### Basic Example: Authentication Bypass

Consider a login form that takes a username and password. The backend code constructs a query like this:

```sql
SELECT * FROM users
WHERE username = 'alice'
  AND password = 'secret123';
```

If the user provides:
- Username: `alice`
- Password: `secret123`

The query returns the row for alice -- login succeeds.

Now consider what happens if an attacker enters:
- Username: `' OR '1'='1`
- Password: `' OR '1'='1`

The query becomes:

```sql
SELECT * FROM users
WHERE username = '' OR '1'='1'
  AND password = '' OR '1'='1';
```

Since `'1'='1'` is always true, the WHERE clause evaluates to true for every row. The query returns all rows. If the application accepts the first row as a successful login, the attacker gains access as the first user (often an administrator).

### More Destructive Injection

An attacker can do much more than bypass login.

#### Retrieving All Data from a Table

Input: `' UNION SELECT * FROM credit_cards --`

```sql
SELECT product_name, price FROM products
WHERE product_id = '' UNION SELECT * FROM credit_cards --';
```

The `UNION` keyword appends results from a different query. The `--` comments out the rest of the original query. Now the application returns credit card data in addition to (or instead of) product data.

#### Modifying Data

Input: `'; UPDATE accounts SET balance = 100000 WHERE account_id = 1234 --`

```sql
SELECT * FROM accounts
WHERE account_id = ''; UPDATE accounts SET balance = 100000 WHERE account_id = 1234 --';
```

The semicolon ends the first query, and the second query executes as a separate statement. The attacker changes their account balance.

#### Deleting Data

Input: `'; DROP TABLE users --`

```sql
SELECT * FROM users
WHERE user_id = ''; DROP TABLE users --';
```

The `DROP TABLE` statement deletes the entire `users` table, causing catastrophic data loss.

## Types of SQL Injection

### 1. In-Band SQL Injection (Most Common)
The attacker uses the same channel to inject the SQL and receive the results.

- **Error-based:** Attacker triggers database errors to gain information about the schema.
- **Union-based:** Uses `UNION` to combine results from multiple tables.

### 2. Blind SQL Injection
The attacker does not see the query results directly but can infer information through true/false responses or time delays.

- **Boolean-based:** Sends a query that returns different results based on a condition. Example: `' OR 1=1 --` (true) vs `' OR 1=2 --` (false).
- **Time-based:** Uses `SLEEP()` or `WAITFOR DELAY` to introduce delays. Example: `' OR IF(1=1, SLEEP(5), 0) --`. The delay confirms the condition is true.

### 3. Out-of-Band SQL Injection
The attacker uses a different channel to receive the output (e.g., DNS or HTTP requests). Used when the database server cannot directly return data.

## Vulnerable Code Examples

### Example 1: Java (Statement -- Vulnerable)

```java
String username = request.getParameter("username");
String password = request.getParameter("password");

// VULNERABLE: concatenating user input into SQL
String query = "SELECT * FROM users WHERE username = '" + username
             + "' AND password = '" + password + "'";
Statement stmt = connection.createStatement();
ResultSet rs = stmt.executeQuery(query);
```

### Example 2: PHP (Vulnerable)

```php
$username = $_POST['username'];
$password = $_POST['password'];

// VULNERABLE: direct concatenation
$query = "SELECT * FROM users WHERE username = '$username' AND password = '$password'";
$result = mysqli_query($conn, $query);
```

### Example 3: Python (Vulnerable)

```python
username = request.form['username']
password = request.form['password']

# VULNERABLE: string formatting
query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
cursor.execute(query)
```

## Prevention Techniques

### 1. Parameterized Queries (Prepared Statements)

**This is the PRIMARY defense.** User input is separated from the SQL logic. Input values are sent as parameters, not as part of the SQL string. The database treats them as data, never as executable code.

```sql
-- The SQL structure is fixed; ? are placeholders
SELECT * FROM users WHERE username = ? AND password = ?
```

The database engine compiles the query structure first, then binds the parameter values. Even if the parameter contains `' OR '1'='1`, it is treated as a literal string, not as SQL code.

#### Parameterized Query Examples by Language

**Java (PreparedStatement -- Safe):**

```java
String username = request.getParameter("username");
String password = request.getParameter("password");

// SAFE: parameterized query
String query = "SELECT * FROM users WHERE username = ? AND password = ?";
PreparedStatement pstmt = connection.prepareStatement(query);
pstmt.setString(1, username);
pstmt.setString(2, password);
ResultSet rs = pstmt.executeQuery();
```

**PHP (PDO -- Safe):**

```php
$username = $_POST['username'];
$password = $_POST['password'];

// SAFE: using PDO prepared statements
$stmt = $pdo->prepare("SELECT * FROM users WHERE username = :username AND password = :password");
$stmt->execute(['username' => $username, 'password' => $password]);
```

**Python (sqlite3 -- Safe):**

```python
username = request.form['username']
password = request.form['password']

# SAFE: parameterized query with ?
query = "SELECT * FROM users WHERE username = ? AND password = ?"
cursor.execute(query, (username, password))
```

**C# (ADO.NET -- Safe):**

```csharp
string username = Request["username"];
string password = Request["password"];

// SAFE: using SqlCommand with parameters
string query = "SELECT * FROM users WHERE username = @username AND password = @password";
SqlCommand cmd = new SqlCommand(query, connection);
cmd.Parameters.AddWithValue("@username", username);
cmd.Parameters.AddWithValue("@password", password);
SqlDataReader reader = cmd.ExecuteReader();
```

### 2. Input Validation and Sanitization

Validate that input matches expected patterns. Reject unexpected input rather than trying to clean it.

```python
import re

# Validate that a user ID is a positive integer
user_id = request.form['user_id']
if not re.match(r'^\d+$', user_id):
    raise ValueError("Invalid user ID")
```

**Whitelist vs Blacklist:**
- **Whitelist (preferred):** Define what is allowed. Reject everything else.
- **Blacklist:** Define what is forbidden. Easy to bypass because attackers find new patterns.

### 3. Stored Procedures

Stored procedures can encapsulate database logic and reduce direct table access. The application calls the procedure with parameters rather than constructing SQL.

```sql
-- Create a stored procedure for login
CREATE PROCEDURE AuthenticateUser
    @username VARCHAR(50),
    @password VARCHAR(50)
AS
BEGIN
    SELECT * FROM users
    WHERE username = @username
      AND password_hash = HASHBYTES('SHA2_256', @password);
END;
```

```python
# Application calls the stored procedure (safe)
cursor.callproc('AuthenticateUser', [username, password])
```

**Important:** Stored procedures must use parameterized queries internally. A stored procedure that concatenates input is still vulnerable.

### 4. Least Privilege

The database account used by the application should have the minimum necessary privileges.

- Application account should only have EXECUTE on specific stored procedures, not direct table access.
- Application account should not have DDL privileges (CREATE, DROP, ALTER).
- Application account should not have access to tables that are not needed by the application.

```sql
-- Create a limited application account
CREATE USER 'webapp'@'localhost' IDENTIFIED BY 'WebAppPass123';

-- Grant only what is needed (no direct table access)
GRANT EXECUTE ON PROCEDURE AuthenticateUser TO webapp;
GRANT EXECUTE ON PROCEDURE GetProductList TO webapp;

-- Do NOT grant:
-- GRANT SELECT, INSERT, UPDATE, DELETE ON *.* TO webapp;
-- GRANT CREATE, DROP, ALTER ON *.* TO webapp;
```

### 5. Escape User Input (Last Resort)

If parameterized queries are not available, escape special characters. Different DBMS use different escape mechanisms. This is error-prone and should only be used when parameterization is impossible.

```php
// Escaping in MySQL (using mysqli_real_escape_string)
$username = mysqli_real_escape_string($conn, $_POST['username']);
$query = "SELECT * FROM users WHERE username = '$username'";
```

## Safe vs Vulnerable: Side-by-Side Comparison

### Login Form Example

```
+----------------------------------+------------------------------------+
| VULNERABLE                       | SAFE                               |
+----------------------------------+------------------------------------+
| Python code:                     | Python code:                       |
| query = f"SELECT * FROM users    | query = "SELECT * FROM users       |
|   WHERE username = '{username}'  |   WHERE username = ?               |
|   AND password = '{password}'"   |   AND password = ?"                |
| cursor.execute(query)            | cursor.execute(query,              |
|                                  |   (username, password))            |
+----------------------------------+------------------------------------+
| Input: username = ' OR '1'='1    | Input: same malicious string       |
| Resulting SQL:                   | SQL sent to server:                |
| SELECT * FROM users              | SELECT * FROM users                |
|   WHERE username = ''            |   WHERE username = ?               |
|     OR '1'='1'                   |   AND password = ?                  |
|     AND password = ''            | (parameters: ["' OR '1'='1",       |
|     OR '1'='1'                   |  "' OR '1'='1"])                   |
|                                  | No injection; returns zero rows.   |
| Returns all users. Attacker      |                                    |
| logs in as first user.           |                                    |
+----------------------------------+------------------------------------+
```

## Additional Defenses

### Web Application Firewall (WAF)
A WAF sits between the user and the web application, inspecting requests for malicious patterns (e.g., `' OR 1=1 --`) and blocking them before they reach the application.

### ORM Frameworks
Object-Relational Mapping frameworks (Hibernate, Entity Framework, Django ORM, SQLAlchemy) typically use parameterized queries internally. Using an ORM reduces the risk of SQL injection if used correctly (but raw queries via ORMs can still be vulnerable).

### Regular Security Testing
- Static Application Security Testing (SAST): Scan source code for vulnerable patterns.
- Dynamic Application Security Testing (DAST): Test running applications with injection payloads.
- Penetration Testing: Manual testing by security professionals.

## SQL Injection Cheat Sheet

| Payload                             | Effect                                               |
|-------------------------------------|------------------------------------------------------|
| `' OR '1'='1`                       | Bypass authentication (always true)                  |
| `' OR 1=1 --`                       | Same as above; comments out rest of query            |
| `' UNION SELECT * FROM users --`    | Retrieve data from another table                     |
| `'; DROP TABLE users --`            | Delete entire table                                  |
| `' OR 1=1 ORDER BY 1 --`            | Test number of columns (enumeration)                 |
| `admin' --`                         | Log in as admin, ignoring password check             |
| `' WAITFOR DELAY '0:0:5' --`        | Time-based blind injection (5 second delay)          |
| `' OR SLEEP(5) --`                  | Same, in MySQL                                      |
| `' UNION SELECT @@version --`       | Get database version                                 |
| `'; EXEC xp_cmdshell 'dir' --`      | Execute OS commands (SQL Server, if enabled)         |

---

## Practice Problems

1. What is SQL injection and why does it occur? Provide a vulnerable SQL query and the resulting query when an attacker inputs `' OR '1'='1`.
2. Write parameterized (safe) versions of the following vulnerable query in Java, Python, and PHP:
   `SELECT * FROM products WHERE category = '` + category + `' AND price < ` + max_price
3. Explain the difference between whitelist validation and blacklist validation. Which one is more secure and why?
4. How does the principle of least privilege help prevent SQL injection damage? Give a specific example with SQL statements.
5. A developer says: "I use stored procedures, so my application is safe from SQL injection." Is this statement always true? Explain.
