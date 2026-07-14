# Review Quiz on Security Concepts

**Course:** Database Management Systems  
**Module:** 4 | **Lecture:** 7  
**Date:** 27-Oct-2026  
**Faculty:** ANUPAM DAS  
**CO:** CO 4  
**Learning Methodology:** Chalk & Talk  
**Reference:** Korth & Silberschatz Database System Concepts (7th Ed.)

## Comprehensive Review Quiz

This quiz covers topics from L01 through L06. Each question is followed by a detailed answer. Write your answer first, then compare with the provided answer.

---

### Question 1

What are the three components of the CIA triad? For each component, describe a database security threat that specifically targets it and a countermeasure that protects it.

**Answer:**

- **Confidentiality:** Ensures data is accessible only to authorized users. Threat: SQL injection where an attacker reads sensitive data by bypassing authentication. Countermeasure: parameterized queries and column-level encryption.
- **Integrity:** Ensures data is accurate and unmodified by unauthorized parties. Threat: unauthorized UPDATE or DELETE statements via privilege escalation. Countermeasure: access controls (GRANT/REVOKE) and audit trails to detect tampering.
- **Availability:** Ensures the database is accessible when needed. Threat: Denial of Service (DoS) attack that floods the database with requests. Countermeasure: rate limiting, connection pooling, and redundant failover servers.

---

### Question 2

Compare database-level authentication with OS-level authentication. Give one advantage and one disadvantage of each approach.

**Answer:**

| Aspect              | Database-Level Auth                         | OS-Level Auth                            |
|---------------------|---------------------------------------------|------------------------------------------|
| Credential storage  | Inside the DBMS                             | Operating system manages credentials     |
| Advantage           | Works independently of OS; portable across  | Single sign-on; integrated with domain   |
|                     | different platforms                         | policies (Active Directory)              |
| Disadvantage        | User must remember yet another password;    | Ties database access to OS accounts;     |
|                     | passwords must be managed separately        | less portable across OS platforms        |

---

### Question 3

Write the SQL statements to: (a) create a user `analyst` with password `Secure@123`, (b) grant SELECT on the `sales` table to `analyst`, (c) grant INSERT on `sales` to `manager` with the ability to pass this privilege to others, and (d) revoke the SELECT privilege from `analyst`.

**Answer:**

```sql
-- (a) Create user
CREATE USER 'analyst'@'localhost' IDENTIFIED BY 'Secure@123';

-- (b) Grant SELECT
GRANT SELECT ON sales TO analyst;

-- (c) Grant INSERT with GRANT OPTION
GRANT INSERT ON sales TO manager WITH GRANT OPTION;

-- (d) Revoke SELECT
REVOKE SELECT ON sales FROM analyst;
```

---

### Question 4

Explain the Bell-LaPadula model. What are its two fundamental rules, and what security goal does each enforce? Provide an example.

**Answer:**

The Bell-LaPadula model is a Mandatory Access Control (MAC) model designed to enforce confidentiality. It assigns security labels (e.g., TOP SECRET, SECRET, CONFIDENTIAL, UNCLASSIFIED) to subjects (users) and objects (data).

- **Simple Security Property (No Read Up):** A subject cannot read an object with a higher classification. Example: a user with SECRET clearance cannot read TOP SECRET data.
- **Star Property (No Write Down):** A subject cannot write to an object with a lower classification. Example: a TOP SECRET user cannot write to a CONFIDENTIAL file. This prevents high-classification data from leaking to lower classifications.

Together, these rules ensure that information can only flow upward (toward higher classification) or stay at the same level, never downward.

---

### Question 5

What is RBAC? Describe its three core components and explain how they relate to each other.

**Answer:**

Role-Based Access Control (RBAC) is an access control model where permissions are assigned to roles, and users are assigned to roles.

- **Users:** Individual accounts (people or applications).
- **Roles:** Named groups of permissions (e.g., `clerk`, `manager`, `auditor`).
- **Permissions:** Rights to perform operations on objects (SELECT, INSERT, etc.).

Relationship: Users are assigned to roles (many-to-many). Roles are granted permissions (many-to-many). A user's effective permissions = union of permissions from all roles assigned to that user.

---

### Question 6

Distinguish between symmetric and asymmetric encryption. When would you use each in a database context?

**Answer:**

- **Symmetric encryption (AES):** Same key for encryption and decryption. Fast, suitable for bulk data. Used for Transparent Data Encryption (TDE) and column-level encryption.
- **Asymmetric encryption (RSA):** Public key for encryption, private key for decryption. Slow, used for small data. Used for encrypting symmetric keys (key exchange) and digital certificates.

In practice, hybrid approach: asymmetric encryption exchanges a session key; symmetric encryption protects the actual data.

---

### Question 7

What is Transparent Data Encryption (TDE)? How does it protect data without requiring application changes?

**Answer:**

TDE encrypts database files (data files .mdf, log files .ldf) at the file level. The DBMS automatically encrypts data as it is written to disk and decrypts it as it is read into memory. Applications interact with the database normally (plaintext); they are unaware of the encryption. TDE protects against physical theft of storage media or backup files.

---

### Question 8

Describe the Sony PlayStation Network breach of 2011. List three specific security failures that contributed to the breach.

**Answer:**

The Sony PSN breach compromised 77 million accounts. Attackers used SQL injection on the PSN website to gain entry, then escalated privileges and accessed the backend database. Three failures:

1. **SQL injection vulnerability** in the web application (input was not sanitized).
2. **Weak password hashing** -- passwords were hashed with MD5 without salt, making them easily crackable.
3. **Flat network** -- no segmentation between application and database servers, so once inside, attackers could directly access the database.

---

### Question 9

How does the `WITH GRANT OPTION` affect privilege propagation? Draw a simple authorization graph where DBA grants SELECT to Alice with GRANT OPTION, Alice grants it to Bob, and then DBA revokes from Alice with CASCADE. Who retains the SELECT privilege?

**Answer:**

`WITH GRANT OPTION` allows the grantee to pass the privilege to other users. The authorization graph:

```
DBA --> Alice --> Bob
```

If DBA revokes SELECT from Alice with CASCADE:
- Alice loses SELECT.
- Bob also loses SELECT (because his privilege came through Alice).
If DBA revoked with RESTRICT instead, the REVOKE would fail because Alice already granted it to Bob.

---

### Question 10

What is the difference between DAC, MAC, and RBAC? Give one scenario where MAC would be required over the other models.

**Answer:**

- **DAC:** Object owner controls access. Flexible but can lead to uncontrolled privilege propagation.
- **MAC:** Central authority assigns security labels. Strict control over information flow. Users cannot override.
- **RBAC:** Permissions assigned to roles; users assigned to roles. Most practical for enterprise.

**Scenario requiring MAC:** A military database where documents are classified (TOP SECRET, SECRET, etc.) and data flow must be strictly controlled to prevent leaks. No user, even the document creator, should be able to declassify data.

---

### Question 11

Explain the difference between encryption and hashing. Why is hashing preferred for password storage?

**Answer:**

- **Encryption:** Reversible (can decrypt with key). Output length varies. Used for confidentiality.
- **Hashing:** One-way (cannot reverse). Fixed-length output. Used for integrity verification.

Hashing is preferred for passwords because even if the hash database is stolen, the attacker cannot recover the original passwords (assuming strong hashing like bcrypt with salt). Encryption is reversible, so if the encryption key is compromised, all passwords are exposed.

---

### Question 12

What is SQL injection? Write a vulnerable query and then rewrite it safely using a parameterized query.

**Answer:**

SQL injection is an attack where malicious SQL code is inserted into user input fields and executed by the database.

**Vulnerable code (concatenation):**

```python
query = "SELECT * FROM users WHERE username = '" + user_input + "' AND password = '" + pass_input + "'"
cursor.execute(query)
```

If user_input = `' OR '1'='1`, the query becomes:
```sql
SELECT * FROM users WHERE username = '' OR '1'='1' AND password = ''
```

**Safe code (parameterized query):**

```python
query = "SELECT * FROM users WHERE username = %s AND password = %s"
cursor.execute(query, (user_input, pass_input))
```

User input is treated as data, not executable code.

---

### Question 13

Describe the Equifax breach of 2017. What was the root cause and what specific control would have prevented it?

**Answer:**

Equifax failed to patch Apache Struts (CVE-2017-5638) despite a patch being available two months prior. Attackers exploited this remote code execution vulnerability to access the dispute portal, moved laterally to databases, and exfiltrated 148 million records over 76 days.

The single most effective control would have been **a formal patch management policy** that required critical security patches to be applied within 48-72 hours. Network segmentation and encryption would have limited the damage.

---

### Question 14

What is the principle of least privilege? Give two concrete examples of its application in a database context.

**Answer:**

The principle of least privilege states that a user or process should be granted only the minimum permissions necessary to perform its function.

**Examples:**
1. A payroll clerk needs SELECT and UPDATE on the `salary` column but not INSERT or DELETE on any table, and not SELECT on the `manager_reviews` table.
2. A web application should connect to the database using an account that has only EXECUTE permissions on stored procedures, not direct table access. This prevents SQL injection from being used to read arbitrary tables.

---

### Question 15

Explain how SSL/TLS protects data in transit between a database client and server. What prevents a man-in-the-middle attack?

**Answer:**

SSL/TLS provides:
- **Encryption:** All data is encrypted using a symmetric session key.
- **Authentication:** The server presents an X.509 certificate signed by a trusted Certificate Authority (CA). The client verifies the certificate.
- **Integrity:** A message authentication code (MAC) ensures data is not tampered with.

Man-in-the-middle attacks are prevented by **certificate validation**. If an attacker intercepts the connection and presents a fake certificate, the client will reject it because it is not signed by a trusted CA. Clients should be configured to reject connections if certificate validation fails.

---

### Question 16

What is the difference between data at rest encryption and data in transit encryption? Name one technology used for each.

**Answer:**

- **Data at rest:** Encrypts data stored on disk. Protects against physical theft of storage media. Technology: Transparent Data Encryption (TDE), BitLocker, LUKS.
- **Data in transit:** Encrypts data moving over the network. Protects against network sniffing and man-in-the-middle attacks. Technology: TLS/SSL, IPSec.

---

### Question 17

What is the Cambridge Analytica scandal and why is it considered a data breach even though there was no "hack"?

**Answer:**

Cambridge Analytica was not a technical hack but an abuse of authorized access. A researcher created a Facebook quiz app that, under Facebook's then-API policy, collected data on not only the 300,000 users who installed it but also their entire friend network (87 million profiles). This data was harvested without the friends' knowledge or consent and sold for political profiling.

It is a breach because data was accessed and used in ways not authorized by the data subjects. It highlights that access control failures are not always about external attackers; insider threats and overly permissive access policies can be equally damaging.

---

### Question 18

Compare DAC and RBAC. Which model provides better control against privilege creep and why?

**Answer:**

- **DAC:** Owners grant permissions directly to users. Over time, users accumulate many direct permissions (privilege creep). Difficult to audit and revoke.
- **RBAC:** Permissions are tied to roles, not individuals. Users are assigned to roles and change roles as their job changes. Revoking a role immediately removes all associated permissions.

RBAC provides better control against privilege creep because:
- Permissions are managed at the role level, not per-user.
- Auditing role membership is simpler than auditing individual grants.
- Separation of duties can be enforced by defining exclusive roles.

---

### Question 19

In the context of the Marriott/Starwood breach, explain why legacy systems pose a security risk during mergers and acquisitions.

**Answer:**

During the Marriott-Starwood merger, Starwood's reservation database had already been compromised (since 2014). Because Marriott did not perform adequate security due diligence, the compromised legacy system was connected to Marriott's network post-acquisition, giving attackers access to 500 million guest records.

Legacy systems are risky because:
- They may run outdated software with known vulnerabilities.
- Original security controls may have been bypassed over time.
- Administrators may lack familiarity with legacy configurations.
- Security integration is often deprioritized during mergers.

Lesson: Security audits should be a mandatory part of M&A due diligence; legacy systems must be isolated or remediated immediately.

---

### Question 20

List and explain four security layers discussed in L01. How does "defense in depth" apply to database security?

**Answer:**

The four security layers are:
1. **Physical:** Server room locks, CCTV, biometric access. Protects against physical theft.
2. **Network:** Firewalls, VPNs, IDS. Controls what traffic reaches the database.
3. **OS:** Hardening, file permissions, patching. Protects the operating system hosting the DBMS.
4. **DBMS:** Authentication, authorization, encryption, auditing. Core database-level controls.

**Defense in depth** means layering multiple independent controls so that if one layer fails, others still provide protection. For example: a firewall blocks external traffic (network), the OS requires OS login (OS), the DBMS authenticates and authorizes (DBMS), sensitive columns are encrypted (DBMS), and all queries are logged (auditing). An attacker must defeat all layers to succeed.

---

## Practice Problems

1. Write a comprehensive answer comparing all three access control models (DAC, MAC, RBAC) with specific SQL syntax examples for each.
   <details>
   <summary>Show Answer</summary>
   **DAC (Discretionary Access Control):** Data owner controls access. SQL: `GRANT SELECT ON students TO bob;` — bob can further grant it (`WITH GRANT OPTION`). **MAC (Mandatory Access Control):** System-enforced labels. SQL: Not native to standard SQL; implemented via security labels (e.g., Oracle Label Security). Example: A row labeled `TS` (Top Secret) cannot be read by a user with `S` (Secret) clearance. **RBAC (Role-Based Access Control):** Permissions assigned to roles, roles to users. SQL: `CREATE ROLE instructor; GRANT SELECT, INSERT ON grades TO instructor; GRANT instructor TO alice;` — manages permissions efficiently.
   </details>
2. Given a university database with tables `students`, `courses`, `enrollments`, design an RBAC system with at least four roles. Write all GRANT statements.
   <details>
   <summary>Show Answer</summary>
   Roles: `student`, `instructor`, `registrar`, `admin`.
   ```sql
   CREATE ROLE student;
   CREATE ROLE instructor;
   CREATE ROLE registrar;
   CREATE ROLE admin;

   -- Students view their own data
   GRANT SELECT ON students TO student;
   GRANT SELECT ON enrollments TO student;

   -- Instructors manage courses and grades
   GRANT SELECT, INSERT, UPDATE ON courses TO instructor;
   GRANT SELECT, UPDATE ON enrollments TO instructor;

   -- Registrar manages enrollments
   GRANT SELECT, INSERT, UPDATE, DELETE ON enrollments TO registrar;
   GRANT SELECT ON students TO registrar;
   GRANT SELECT ON courses TO registrar;

   -- Admin has full access
   GRANT ALL PRIVILEGES ON ALL TABLES TO admin;
   ```
   </details>
3. Explain how encryption, hashing, and salting work together to protect user passwords in a database. Include SQL examples.
   <details>
   <summary>Show Answer</summary>
   When a user registers: (1) A random **salt** is generated per user. (2) The password + salt are passed through a **hash** function (e.g., SHA-256). (3) The salt and hash are stored in the database — the original password is never stored. When logging in: the system retrieves the salt, hashes the entered password with that salt, and compares it to the stored hash.
   ```sql
   CREATE TABLE users (
       id INT PRIMARY KEY,
       username VARCHAR(50),
       password_hash VARCHAR(256),
       salt VARCHAR(64)
   );

   -- Registration
   INSERT INTO users (username, password_hash, salt)
   VALUES ('alice', SHA2(CONCAT('mypassword', 'random_salt'), 256), 'random_salt');
   ```
   </details>
4. You are hired as a security consultant for a startup. Create a security checklist of 10 items based on the breaches studied in L06.
   <details>
   <summary>Show Answer</summary>
   1. Enforce strong password policies and hash passwords with salt. 2. Apply security patches within 48 hours of release. 3. Implement network segmentation — isolate databases from web servers. 4. Use parameterized queries to prevent SQL injection. 5. Enforce least privilege for all database users and applications. 6. Encrypt sensitive data at rest (TDE) and in transit (TLS). 7. Implement multi-factor authentication for all administrative access. 8. Deploy database activity monitoring (DAM) to detect anomalies. 9. Conduct regular vulnerability assessments and penetration testing. 10. Audit and review third-party API access and vendor permissions.
   </details>
5. The CIA triad is sometimes extended with additional principles. Research and write about Non-Repudiation and Accountability as extensions of the model.
   <details>
   <summary>Show Answer</summary>
   **Non-Repudiation:** Prevents a party from denying an action they performed. In databases, this is achieved through audit logs, digital signatures, and transaction logs — e.g., a signed log entry proves exactly who deleted a record and when. **Accountability:** Ensures that every action can be traced back to an individual. Implementation: database audit trails that record user ID, timestamp, query, and affected rows. Together they extend the CIA triad to the C-I-A-N-A model (Confidentiality, Integrity, Availability, Non-Repudiation, Accountability), providing a more complete security framework.
   </details>
