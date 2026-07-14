# Authentication Mechanisms

**Course:** Database Management Systems  
**Module:** 4 | **Lecture:** 2  
**Date:** 01-Oct-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 4  
**Learning Methodology:** Chalk & Talk  
**Reference:** Korth & Silberschatz Database System Concepts (7th Ed.)

## What is Authentication?

Authentication is the process of verifying the identity of a user, system, or process. Before a user can access a database, the DBMS must confirm that the user is who they claim to be. This is the first line of defense and is typically the first step before any authorization checks.

The general model is:
1. The user presents credentials (something they know, have, or are).
2. The system verifies those credentials against a stored reference.
3. If matched, the user is authenticated and proceeds to authorization.
4. If not matched, access is denied.

## Authentication Factors

Authentication methods are categorized into three factors:

```
+--------------------+--------------------------------------+----------------------------+
| Factor             | Description                          | Examples                   |
+--------------------+--------------------------------------+----------------------------+
| Knowledge          | Something the user knows             | Password, PIN, passphrase  |
| (Type 1)           |                                      |                            |
+--------------------+--------------------------------------+----------------------------+
| Possession         | Something the user has               | Smart card, hardware token,|
| (Type 2)           |                                      | phone (OTP), certificate   |
+--------------------+--------------------------------------+----------------------------+
| Inherence          | Something the user is                | Fingerprint, iris scan,    |
| (Type 3)           |                                      | voice recognition, face ID |
+--------------------+--------------------------------------+----------------------------+
```

### Single-Factor Authentication (SFA)
Uses only one factor. Example: a password alone. This is the most common but least secure approach.

### Multi-Factor Authentication (MFA)
Uses two or more factors from different categories. Example: a password (knowledge) plus a one-time code from an authenticator app (possession). MFA significantly reduces the risk of credential theft.

## Authentication in DBMS

Database systems support several authentication modes:

### 1. Database-Level Authentication

The user account and password are stored entirely within the database. The DBMS manages its own user repository. This is independent of the operating system.

**CREATE USER**

Creates a new database user account with a password.

```sql
CREATE USER 'alice'@'localhost' IDENTIFIED BY 'StrongP@ss123';

-- In Oracle:
CREATE USER alice IDENTIFIED BY StrongP@ss123;
```

The `'alice'@'localhost'` syntax specifies that user `alice` can only connect from `localhost`. For any host, use `'alice'@'%'`.

**ALTER USER**

Modifies an existing user's properties, such as changing the password or account locking.

```sql
-- Change password
ALTER USER 'alice'@'localhost' IDENTIFIED BY 'NewP@ss456';

-- Lock an account (prevent login)
ALTER USER 'alice'@'localhost' ACCOUNT LOCK;

-- Unlock an account
ALTER USER 'alice'@'localhost' ACCOUNT UNLOCK;
```

**DROP USER**

Removes a user account from the database.

```sql
DROP USER 'alice'@'localhost';
```

### 2. OS-Level Authentication

The DBMS delegates authentication to the operating system. The user logs into the OS, and the DBMS trusts the OS identity. This is common in Oracle (using OS_AUTHENT_PREFIX) and SQL Server (integrated security / Windows Authentication).

Benefits:
- Single sign-on: users do not need a separate database password.
- Centralized management via OS policies.
- No passwords stored in the database.

```sql
-- In Oracle, create a user that authenticates via the OS
-- The OS user must match the prefix + username convention.
CREATE USER ops$virus404 IDENTIFIED EXTERNALLY;
```

```sql
-- In SQL Server, Windows Authentication is the default.
CREATE LOGIN [DOMAIN\jdoe] FROM WINDOWS;
CREATE USER jdoe FOR LOGIN [DOMAIN\jdoe];
```

### 3. Certificate-Based Authentication

The user presents a digital certificate (X.509) issued by a trusted Certificate Authority (CA). The DBMS verifies the certificate's signature and validity.

```sql
-- In SQL Server:
CREATE LOGIN alice WITH PASSWORD = 'p@ssword';
-- Then map a certificate to the login.
CREATE CERTIFICATE AliceCert FROM FILE = 'C:\certs\alice.cer';
CREATE USER alice FROM CERTIFICATE AliceCert;
```

## Password Policies

Strong password policies are essential to prevent brute-force and dictionary attacks. Common policies enforced by database systems:

| Policy                     | Description                                    | Example Setting         |
|----------------------------|------------------------------------------------|-------------------------|
| Minimum length             | Password must be at least N characters.       | 8 characters            |
| Complexity                 | Must include uppercase, lowercase, digit,     | At least 1 of each      |
|                            | and special character.                         |                         |
| Expiration                 | Password expires after N days.                | 90 days                 |
| History                    | Cannot reuse recent passwords.                | Last 5 passwords kept   |
| Account lockout            | Lock account after N failed attempts.         | Lock after 5 failures   |

### Example: Configuring Password Policies in MySQL

```sql
-- Set global password policy
SET GLOBAL validate_password.length = 8;
SET GLOBAL validate_password.mixed_case_count = 1;
SET GLOBAL validate_password.number_count = 1;
SET GLOBAL validate_password.special_char_count = 1;
```

### Example: Password Profile in Oracle

```sql
CREATE PROFILE secure_profile LIMIT
  PASSWORD_LIFE_TIME 90
  PASSWORD_GRACE_TIME 7
  PASSWORD_REUSE_TIME 365
  PASSWORD_REUSE_MAX 5
  FAILED_LOGIN_ATTEMPTS 5
  PASSWORD_LOCK_TIME 1;

ALTER USER alice PROFILE secure_profile;
```

## Common Authentication Mistakes

1. **Default credentials:** Using vendor-default usernames and passwords (e.g., `root` with no password, `sa` with blank password).
2. **Hardcoded credentials:** Embedding database passwords in application source code or configuration files.
3. **Weak passwords:** Short, dictionary words, or patterns like `password123`.
4. **No account lockout:** Attackers can brute-force without limitation.
5. **Overprivileged service accounts:** Application connections using admin accounts instead of least-privilege accounts.

## Best Practices

- Always use strong, unique passwords for each database account.
- Enable MFA for administrative accounts wherever supported.
- Use OS-level authentication for integrated environments.
- Rotate passwords regularly and enforce password history.
- Remove unused accounts promptly.
- Never share accounts between users.
- Audit login failures to detect brute-force attempts.

---

## Practice Problems

1. Write SQL statements to create a user `dbadmin` with password `Admin@2026` that can connect from any host, then lock the account and finally drop it.
   <details>
   <summary>Show Answer</summary>
   ```sql
   CREATE USER 'dbadmin'@'%' IDENTIFIED BY 'Admin@2026';
   ALTER USER 'dbadmin'@'%' ACCOUNT LOCK;
   DROP USER 'dbadmin'@'%';
   ```
   </details>
2. What is multi-factor authentication? Give an example involving all three authentication factors.
   <details>
   <summary>Show Answer</summary>
   Multi-factor authentication (MFA) requires two or more independent credentials from different categories: **Something you know** (password), **something you have** (smartphone/security token), and **something you are** (fingerprint). Example: Logging into a database console with a password (knowledge), a one-time code sent to your phone (possession), and a fingerprint scan (inherence).
   </details>
3. Compare database-level authentication with OS-level authentication. List one advantage and one disadvantage of each.
   <details>
   <summary>Show Answer</summary>
   **Database-level authentication:** Users are created and managed entirely inside the DBMS. *Advantage:* Portable across operating systems. *Disadvantage:* Passwords are stored in the database and must be managed separately. **OS-level authentication:** The DBMS trusts the OS to authenticate users (e.g., Windows integrated authentication). *Advantage:* Centralized user management via OS domain policies. *Disadvantage:* Ties the database to a specific OS authentication infrastructure.
   </details>
4. Explain why password policies such as minimum length and account lockout are important. What attack do they prevent?
   <details>
   <summary>Show Answer</summary>
   Minimum length requirements make brute-force and dictionary attacks exponentially harder by increasing the search space. Account lockout after a few failed attempts prevents automated guessing (online brute-force) by temporarily or permanently disabling the account. Together they defend primarily against **brute-force attacks** and **credential stuffing**.
   </details>
5. How does certificate-based authentication work in a DBMS context?
   <details>
   <summary>Show Answer</summary>
   A client presents an X.509 digital certificate issued by a trusted Certificate Authority (CA). The DBMS verifies the certificate's signature against the CA's root certificate, checks the expiration date, and optionally maps the certificate's Common Name (CN) to a database user. This eliminates the need for password-based login and provides strong, non-repudiable authentication.
   </details>
